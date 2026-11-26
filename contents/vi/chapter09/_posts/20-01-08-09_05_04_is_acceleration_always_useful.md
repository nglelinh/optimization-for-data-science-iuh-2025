---
layout: post
title: '09-05-04 Tăng tốc có luôn hữu ích không?'
chapter: '09'
order: 10
owner: Kyeongmin Woo
categories:
- chapter09
lang: vi
---

Nếu FISTA nhanh hơn ISTA theo lý thuyết từ $$O(1/k)$$ lên $$O(1/k^2)$$ mà chi phí mỗi vòng gần như bằng nhau, tại sao không mặc định bật tăng tốc cho mọi bài toán tối ưu trên đời? Người làm tối ưu giàu kinh nghiệm hiểu ngay câu ngạn ngữ quen thuộc: *"Không có bữa trưa nào hoàn toàn miễn phí."* Quán tính giúp viên bi lao nhanh dọc thung lũng dài, nhưng chính quán tính ấy cũng làm viên bi **lao lố qua đáy**, phóng đại nhiễu gradient ngẫu nhiên, và tạo ra những gợn sóng dao động kéo dài trên các bài toán điều kiện xấu!

Bài học ngắn nhưng cực kỳ thực chiến này giúp bạn phát triển trực giác kỹ sư: biết khi nào FISTA là vũ khí hủy diệt, khi nào nó gây hại (gradient nhiễu, bước prox xấp xỉ không đủ chính xác, bài toán cần giảm đơn điệu tuyệt đối), và cách khắc phục thanh lịch nhất trong thực tế — **khởi động lại thích nghi (adaptive restart)** của O'Donoghue & Candès (2015).

## Kiến thức cần nhớ: Bốn tình huống giới hạn của kỹ thuật tăng tốc

- **Mất tính đơn điệu và gợn sóng Nesterov (Overshooting & Ripples):** Vì hệ số quán tính $$\beta_k \to 1$$ gần như không có ma sát khi $$k$$ lớn, điểm lặp thường trượt vượt qua đáy nghiệm rồi vòng ngược lại, tạo ra hình răng cưa trên đồ thị loss.
- **Nhạy cảm với nhiễu gradient và sai số prox (Error Accumulation):** Trong phương pháp không tăng tốc, sai số tính gần đúng ở bước cũ bị tắt dần; còn trong FISTA, hệ số quán tính lớn có thể *tích lũy và khuếch đại* sai số của gradient ngẫu nhiên (mini-batch) hoặc sai số giải gần đúng bài toán con prox!
- **Chi phí ẩn khi đánh giá tính đơn điệu (MFISTA):** Nếu ứng dụng đòi hỏi $$f(x^{(k)})$$ không bao giờ tăng (ví dụ tái tạo ảnh y tế cần bảo chứng giảm năng lượng từng bước), biến thể Monotone FISTA phải tính thêm giá trị hàm $$f$$ ở mỗi bước và chọn điểm tốt hơn.
- **Kỹ thuật khởi động lại thích nghi (Adaptive Restart):** Ngay khi phát hiện đà quán tính đang kéo ngược chiều với hướng giảm (tức $$(y^{(k)} - x^{(k+1)})^T(x^{(k+1)} - x^{(k)}) > 0$$ hoặc $$f(x^{(k+1)}) > f(x^{(k)})$$), ta đặt lại $$t_k = 1$$ (xóa quán tính về $$0$$). Chỉ một câu lệnh `if` ấy xóa sạch gợn sóng và thậm chí đạt hội tụ tuyến tính (hàm mũ) trên các hàm lồi mạnh cục bộ!

### Giải thích: Tính tay kiểm tra điều kiện Adaptive Restart khi FISTA trượt lố

Giả sử trên một bài toán 1D có nghiệm $$x^* = 0$$, FISTA đang chạy tới vòng $$k$$ với:
- Điểm cũ $$x^{(k)} = 0.2$$,
- Điểm ngoại suy trượt lố sang bên kia đáy $$y^{(k)} = -0.3$$,
- Bước prox kéo ngược lại về phía $$0$$ nên $$x^{(k+1)} = -0.1$$.

1. **Kiểm tra hai vector trong tiêu chuẩn khởi động lại gradient (O'Donoghue–Candès):**
   - Hướng dịch chuyển thực tế của bước lặp: $$d_{\text{move}} = x^{(k+1)} - x^{(k)} = -0.1 - 0.2 = -0.3$$ (đang lao về bên trái).
   - Hướng ngược bước prox (xấp xỉ gradient tại $$y^{(k)}$$): $$d_{\text{grad}} = y^{(k)} - x^{(k+1)} = -0.3 - (-0.1) = -0.2$$ (chỉ sang trái, nghĩa là hướng giảm $$-d_{\text{grad}} = +0.2$$ lại đang kéo sang **bên phải**!).
2. **Tính tích vô hướng kiểm tra:**
   $$(y^{(k)} - x^{(k+1)})^T (x^{(k+1)} - x^{(k)}) = (-0.2) \times (-0.3) = +0.06 > 0!$$
3. **Hành động của bộ giải:** Tích vô hướng **dương** báo hiệu góc giữa hướng đà quán tính và hướng giảm đang là góc tù — quán tính vừa đẩy ta vượt qua đáy! Thuật toán lập tức **restart**: đặt lại $$t_{k+1} = 1$$ (xóa đà về $$0$$) và đặt $$y^{(k+1)} = x^{(k+1)} = -0.1$$ để bước sau tiến thẳng vào $$x^* = 0$$ mà không dao động qua lại nữa.

# Tăng tốc có luôn hữu ích không?

Mặc dù các phương pháp tăng tốc như FISTA đạt tốc độ hội tụ lý thuyết nhanh hơn, trong thực tế việc dùng tăng tốc không phải lúc nào cũng mang lại hiệu quả tốt hơn.

## Khi nào tăng tốc có thể kém hiệu quả
- Nếu bài toán có điều kiện tốt (số điều kiện $$\kappa = L/\mu$$ nhỏ), phương pháp gradient gần kề thường đã hội tụ nhanh, với tốc độ tuyến tính. Khi đó tăng tốc lợi rất ít, thậm chí động lượng có thể làm chậm hơn một chút. Ví dụ, với một bài Lasso 2 chiều có $$\kappa = 3$$, ISTA cần 14 vòng lặp còn FISTA cần 16 vòng.
- Tăng tốc có lợi nhất khi bài toán có điều kiện xấu ($$\kappa$$ lớn). Lúc đó gradient gần kề thường chạy rất chậm, còn FISTA giảm số vòng lặp đi nhiều lần. Đổi lại, giá trị hàm mục tiêu có thể dao động.
- Nếu $$g$$ không trơn, hoặc $$\nabla g$$ không có hằng số Lipschitz phù hợp, thì đảm bảo $$O(1/k^2)$$ không còn áp dụng được.
- Hiện tượng "gợn sóng Nesterov" khiến giá trị hàm mục tiêu không giảm đơn điệu: nó có thể tăng lên vài vòng rồi mới giảm tiếp.

## Kinh nghiệm thực hành
- Nên dùng tăng tốc khi phần trơn của bài toán có điều kiện xấu, vì đó là lúc tăng tốc có lợi nhất.
- Khi bài toán có điều kiện tốt, phương pháp gradient gần kề thường là đủ.
- Theo dõi giá trị hàm mục tiêu. Nếu dao động lớn, dùng cơ chế khởi động lại (restart, đặt lại $$t_k = 1$$ khi hàm mục tiêu tăng) thay vì bỏ hẳn tăng tốc.

## Kỹ thuật Làm trơn Nesterov (Smoothing) và Khoảng cách Dư (Excessive Gap)

Trong giáo trình *Lectures on Convex Optimization* (Chương 6), Yurii Nesterov chỉ ra cách phá vỡ cận dưới $$O(1/\varepsilon^2)$$ của bài toán lồi **không trơn** có cấu trúc minimax $$f(x) = \max_{u \in Q_2} \langle Ax, u \rangle - \phi(u)$$:
- Bằng cách thêm thành phần điều chuẩn lồi mạnh $$\mu d_2(u)$$ vào hàm mục tiêu đối ngẫu, ta thu được hàm xấp xỉ trơn $$f_\mu(x)$$ với hằng số Lipschitz $$L_\mu = \|A\|^2 / \mu$$.
- Áp dụng **Phương pháp Gradient Nhanh (FGM)** lên $$f_\mu(x)$$ đạt tốc độ hội tụ **$$O(1/\varepsilon)$$** thay vì $$O(1/\varepsilon^2)$$ của dưới-gradient cổ điển — và kỹ thuật **Khoảng cách Dư (Excessive Gap)** còn tự động giảm $$\mu_k \to 0$$ theo từng vòng lặp mà không cần biết trước độ chính xác $$\varepsilon$$.
