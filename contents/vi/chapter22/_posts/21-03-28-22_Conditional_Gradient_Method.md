---
layout: post
title: '22 Phương pháp Gradient có điều kiện (Frank-Wolfe)'
chapter: '22'
order: 1
owner: YoungJae Choung
categories:
- chapter22
lang: vi
---

Năm 1956, giữa thời kỳ hoàng kim đầu tiên của quy hoạch tuyến tính, hai nhà toán học Marguerite Frank và Philip Wolfe đặt ra một câu hỏi tưởng chừng nghịch lý: *nếu ta đã có những bộ giải cực nhanh cho bài toán tối ưu tuyến tính trên một đa diện, tại sao lại phải tự làm khó mình bằng các phép chiếu phi tuyến đắt đỏ khi tối ưu một hàm lồi trơn?* Từ câu hỏi đó, **thuật toán Frank–Wolfe** (hay phương pháp gradient có điều kiện) ra đời, mở ra một trường phái tối ưu không cần phép chiếu (*projection-free*) đầy thanh lịch.

Suốt nhiều thập kỷ, Frank–Wolfe từng nằm yên trong sách giáo khoa cổ điển, trước khi bất ngờ hồi sinh mạnh mẽ trong kỷ nguyên dữ liệu lớn và học máy hiện đại. Lý do rất thực tế: khi biến tối ưu là một ma trận triệu chiều bị ràng buộc bởi chuẩn vết (trace norm) hay một kế hoạch vận chuyển trên đơn hình khổng lồ, phép chiếu Euclid đòi hỏi phân tích SVD đầy đủ — quá chậm để chạy lặp hàng nghìn lần — trong khi cực tiểu hóa một hàm tuyến tính chỉ cần tìm đúng *một* cặp vector kỳ dị hàng đầu.

## Kiến thức cần nhớ: Bốn trụ cột của tối ưu không cần phép chiếu

Để nhìn thấy trọn vẹn sức mạnh và giới hạn của Chương 22, bạn hãy đặt thuật toán Frank–Wolfe vào giao điểm của bốn nhánh kiến thức nền tảng:

- **Hình học lồi và các đỉnh cực trị (Convex Geometry & Extreme Points):** Một tập lồi compact $$C$$ luôn có thể được biểu diễn dưới dạng bao lồi của các đỉnh cực trị (*extreme points*). Khi cực tiểu hóa một hàm tuyến tính trên $$C$$, nghiệm luôn đạt được tại một đỉnh — đó là nguyên nhân sâu xa khiến nghiệm của Frank–Wolfe mang cấu trúc thưa (sparse) hoặc hạng thấp (low-rank) một cách tự nhiên.
- **Xấp xỉ bậc nhất và Bộ giải tuyến tính (Linear Minimization Oracle — LMO):** Thay vì dựng hình parabol cục bộ rồi chiếu nghiệm xuống $$C$$ như Projected Gradient Descent, Frank–Wolfe chỉ thay hàm mục tiêu bằng mặt phẳng tiếp tuyến và gọi LMO. Toàn bộ độ phức tạp của tập ràng buộc được "đóng gói" gọn vào một bài toán tuyến tính duy nhất ở mỗi bước.
- **Đối ngẫu Fenchel và Khoảng cách đối ngẫu (Duality Gap):** Không giống nhiều thuật toán bậc nhất khó biết khi nào nên dừng, Frank–Wolfe tự động sinh ra một cận trên chặt cho sai số tối ưu $$f(x^{(k)}) - f^\star$$ miễn phí ngay từ kết quả gọi LMO, giúp kiểm soát độ chính xác một cách định lượng.
- **Động lực hội tụ và Cấu trúc biên (Convergence & Boundary Geometry):** Tốc độ hội tụ cổ điển $$O(1/k)$$ của Frank–Wolfe có thể bị chậm lại vì hiện tượng đi zíc-zắc khi nghiệm nằm trên một mặt biên của đa diện — động lực trực tiếp dẫn đến các biến thể hiện đại như Away-Step hay Pairwise Frank–Wolfe.

### Giải thích: Một bước Frank–Wolfe trên đơn hình xác suất

Hãy tự tay tính một vòng lặp để thấy vì sao không cần phép chiếu mà điểm lặp vẫn không bao giờ rời khỏi miền khả thi. Xét bài toán cực tiểu hóa $$f(x_1, x_2) = \frac{1}{2}(x_1 - 2)^2 + \frac{1}{2}(x_2 - 1)^2$$ trên đơn hình xác suất $$C = \{(x_1, x_2) : x_1 \ge 0,\; x_2 \ge 0,\; x_1 + x_2 = 1\}$$, xuất phát từ đỉnh $$x^{(0)} = (0, 1) \in C$$.

1. **Tính giá trị và gradient tại điểm hiện tại:** Tại $$x^{(0)} = (0, 1)$$, ta có $$f(x^{(0)}) = \frac{1}{2}(-2)^2 + \frac{1}{2}(0)^2 = 2$$ và $$\nabla f(x^{(0)}) = (x_1 - 2,\; x_2 - 1) = (-2, 0)$$.
2. **Gọi bộ giải tuyến tính (LMO):** Ta tìm $$s^{(0)} = \arg\min_{s \in C} \langle (-2, 0), s \rangle = \arg\min_{s \in C} (-2s_1)$$. Vì $$s_1 \in [0, 1]$$, biểu thức $$-2s_1$$ nhỏ nhất khi $$s_1 = 1, s_2 = 0$$, tức đỉnh $$s^{(0)} = (1, 0)$$.
3. **Di chuyển bằng tổ hợp lồi:** Điểm mới có dạng $$x(\gamma) = (1 - \gamma)(0, 1) + \gamma(1, 0) = (\gamma, 1 - \gamma)$$ với $$\gamma \in [0, 1]$$. Vì cả $$x^{(0)}$$ và $$s^{(0)}$$ đều nằm trong tập lồi $$C$$, mọi $$\gamma \in [0, 1]$$ tự động bảo đảm $$x(\gamma) \in C$$ — hoàn toàn không cần chiếu!
4. **Chọn bước và kiểm tra dừng:** Thay vào hàm mục tiêu, $$f(x(\gamma)) = \frac{1}{2}(\gamma - 2)^2 + \frac{1}{2}(-\gamma)^2 = \gamma^2 - 2\gamma + 2$$, đạt cực tiểu trên $$[0, 1]$$ tại $$\gamma_1 = 1$$ (cũng trùng với bước chuẩn $$\gamma_1 = \frac{2}{1+1} = 1$$). Ta nhận $$x^{(1)} = (1, 0)$$ với $$f(x^{(1)}) = 1$$. Tại đây, $$\nabla f(1, 0) = (-1, -1)$$; với mọi $$s \in C$$ thì $$\langle \nabla f(x^{(1)}), s \rangle = -(s_1 + s_2) = -1 = \langle \nabla f(x^{(1)}), x^{(1)} \rangle$$, nên khoảng cách đối ngẫu bằng $$0$$ — ta đã chạm đúng nghiệm tối ưu toàn cục chỉ sau một bước!

Chương này trình bày thuật toán Frank-Wolfe do Marguerite Frank và Philip Wolfe đề xuất năm 1956.

Thuật toán Frank-Wolfe là một phương pháp tối ưu lặp bậc nhất dành cho bài toán tối ưu lồi có ràng buộc, còn được gọi là phương pháp gradient có điều kiện (conditional gradient method), phương pháp gradient rút gọn (reduced gradient method) hoặc thuật toán tổ hợp lồi (convex combination algorithm). Tại mỗi vòng lặp, thuật toán xấp xỉ tuyến tính hàm mục tiêu xung quanh điểm hiện tại, tìm cực tiểu của hàm tuyến tính đó trên tập ràng buộc, rồi di chuyển theo hướng tới điểm cực tiểu vừa tìm được.

[15] Wikipedia. [Frank–Wolfe algorithm](https://en.wikipedia.org/wiki/Frank%E2%80%93Wolfe_algorithm)

## Ứng dụng giai đoạn 2022–2026 (tùy chọn)

Nhờ chỉ cần một bộ giải cực tiểu tuyến tính (linear minimization oracle) thay vì phép chiếu, thuật toán Frank–Wolfe tiếp tục được ứng dụng rộng rãi trong thập niên 2020: từ SVM có cấu trúc, bài toán vận chuyển tối ưu bán nới lỏng (ứng dụng chuyển màu ảnh), vận chuyển tối ưu không cân bằng 1 chiều, cho đến các phương pháp giải thích mạng nơ-ron có ràng buộc (tối ưu độ méo–tốc độ trên hình cầu $$\ell_1$$ hoặc đa diện Birkhoff). Bạn có thể tham khảo bài đọc tùy chọn [22-05 Ứng dụng hiện đại của Frank–Wolfe]({% multilang_post_url contents/chapter22/2026-09-16-22_05_modern_applications %}) sau khi học xong các mục 22-02 đến 22-04; bài đọc này bổ sung bối cảnh ứng dụng và không thay thế phần phân tích hội tụ.
