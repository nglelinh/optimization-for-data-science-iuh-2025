---
layout: post
title: '08 Phương pháp Subgradient'
chapter: '08'
order: 1
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

Hãy tưởng tượng bạn đang trượt tuyết xuống một thung lũng có đáy hình chữ V sắc cạnh thay vì một lòng chảo parabol mượt mà. Ở mọi sườn dốc trơn láng, la bàn đạo hàm $$\nabla f(x)$$ chỉ chính xác hướng dốc nhất để bạn trượt xuống; nhưng ngay khoảnh khắc ván trượt chạm vào sống rãnh gấp khúc của chữ V, độ dốc bị gãy đột ngột và đạo hàm cổ điển biến mất. Thế giới tối ưu hóa hiện đại — từ bài toán Lasso với chuẩn $$\ell_1$$, máy vector hỗ trợ (SVM) với mất mát bản lề (hinge loss), đến mạng nơ-ron dùng hàm kích hoạt ReLU — tràn ngập những "sống rãnh sắc cạnh" như vậy.

Chương 08 mở ra cánh cửa bước qua ranh giới khả vi bằng một ý tưởng thanh lịch đáng kinh ngạc: **phương pháp subgradient**. Thay vì đầu hàng trước những điểm gãy không có tiếp tuyến duy nhất, ta thay gradient bằng *một* siêu phẳng đỡ (supporting hyperplane) bất kỳ nằm dưới đồ thị hàm lồi. Chỉ với thay đổi tưởng chừng nhỏ bé ấy, ta giải được gần như mọi bài toán tối ưu lồi không trơn — đổi lại là một hiện tượng thú vị: giá trị hàm mục tiêu không còn giảm đơn điệu sau từng bước, buộc ta phải nhìn vào hình học khoảng cách tới nghiệm tối ưu $$x^*$$.

## Bản đồ kiến thức nền: Bốn trụ cột của tối ưu không trơn bậc nhất

Để hiểu sâu vì sao phương pháp subgradient vừa đơn giản vừa có những giới hạn rất đặc thù, hãy kết nối bốn nhánh kiến thức nền sau:

- **Giải tích lồi không trơn (Nonsmooth Convex Analysis):** Mở rộng khái niệm đạo hàm thành *dưới vi phân* (subdifferential) $$\partial f(x)$$ — tập tất cả các vector $$g$$ sao cho $$f(y) \ge f(x) + g^T(y - x)$$ với mọi $$y$$. Tại điểm trơn, $$\partial f(x) = \{\nabla f(x)\}$$; tại điểm gấp khúc, $$\partial f(x)$$ là một tập lồi đóng chứa cả "quạt" các hướng dốc hợp lệ.
- **Hình học khoảng cách Euclid và bất đẳng thức năng lượng:** Khi không còn đảm bảo $$f(x^{(k+1)}) < f(x^{(k)})$$, công cụ chứng minh hội tụ chuyển từ việc theo dõi độ giảm của $$f$$ sang theo dõi hàm thế năng $$\|x^{(k)} - x^*\|_2^2$$. Mỗi bước subgradient có thể tạm làm $$f$$ tăng, nhưng vẫn kéo $$x^{(k)}$$ lại gần $$x^*$$ nếu bước đủ nhỏ.
- **Lý thuyết chọn kích thước bước (Step-size Schedules):** Không thể dùng backtracking line search như gradient descent vì $$-g$$ chưa chắc là hướng giảm. Toàn bộ nghệ thuật của chương xoay quanh các quy tắc bước định trước: bước cố định, bước giảm dần thỏa $$\sum t_k = \infty, \sum t_k^2 < \infty$$, và bước Polyak khi biết $$f^*$$.
- **Tối ưu ngẫu nhiên và phân tách cấu trúc:** Khi hàm mục tiêu là tổng của hàng triệu mẫu dữ liệu, subgradient ngẫu nhiên thay tổng lớn bằng một mẫu duy nhất mỗi bước; và khi hàm có phần trơn cộng phần không trơn, tốc độ $$O(1/\epsilon^2)$$ của chương này sẽ là động lực trực tiếp dẫn sang phương pháp gradient gần kề ở Chương 09.

### Khung giải thích (nên đọc chậm): Trượt xuống đáy chữ V không trơn trên một ví dụ tính tay

Xét hàm lồi không khả vi một biến $$f(x) = |x - 1| + \frac{1}{2}x^2$$. Điểm gấp khúc nằm ngay tại $$x = 1$$.

1. **Kiểm tra điều kiện tối ưu bằng dưới vi phân:**
   Với $$x > 1$$, $$f'(x) = 1 + x > 2 > 0$$. Với $$x < 1$$, $$f'(x) = -1 + x < 0$$.
   Tại điểm gãy $$x = 1$$, dưới vi phân của $$|x - 1|$$ là đoạn $$[-1, 1]$$, còn đạo hàm của $$\frac{1}{2}x^2$$ là $$1$$, nên:
   $$\partial f(1) = [-1, 1] + 1 = [0, 2].$$
   Vì $$0 \in [0, 2]$$, điểm tối ưu duy nhất chính là điểm không khả vi $$x^* = 1$$ với giá trị tối ưu $$f^* = |1-1| + \frac{1}{2}(1)^2 = 0.5$$.
2. **Chạy hai bước subgradient từ $$x^{(0)} = 2$$ với bước cố định $$t = 0.5$$:**
   - **Bước 1:** Tại $$x^{(0)} = 2 > 1$$, $$g^{(0)} = 1 + 2 = 3$$, $$f(2) = 1 + 2 = 3$$.
     Cập nhật: $$x^{(1)} = 2 - 0.5 \times 3 = 0.5$$.
     Giá trị mới: $$f(0.5) = |0.5 - 1| + \frac{1}{2}(0.25) = 0.625$$ (giảm mạnh từ $$3$$ xuống $$0.625$$).
   - **Bước 2:** Tại $$x^{(1)} = 0.5 < 1$$, $$g^{(1)} = -1 + 0.5 = -0.5$$.
     Cập nhật: $$x^{(2)} = 0.5 - 0.5 \times (-0.5) = 0.75$$.
     Giá trị mới: $$f(0.75) = 0.25 + 0.28125 = 0.53125$$, tiến rất sát $$f^* = 0.5$$.
3. **Điều rút ra:** Dù nghiệm $$x^* = 1$$ nằm đúng tại đỉnh nhọn không có đạo hàm, vòng lặp $$x^{(k)} = x^{(k-1)} - t_k g^{(k-1)}$$ vẫn tiến thẳng về vùng nghiệm mà không cần bất kỳ phép biến đổi trơn hóa nào.

Trong chương này, chúng ta tìm hiểu phương pháp subgradient — thuật toán áp dụng cho các hàm lồi không nhất thiết khả vi, được xây dựng dựa trên khái niệm gradient dưới. Chúng ta cũng sẽ phân tích tính chất hội tụ và tốc độ hội tụ của phương pháp này thông qua các ví dụ cụ thể.

## Ứng dụng hiện đại (2022–2026)

Bài đọc tùy chọn đi kèm liên hệ trực tiếp vòng lặp subgradient (bao gồm biến thể có chiếu và ngẫu nhiên) với các ứng dụng như PGD trong huấn luyện đối kháng / RobustBench, bài toán ràng buộc tỷ lệ trong Fairlearn, và huấn luyện mạng ReLU không trơn. Xem [08-09 Ứng dụng hiện đại của phương pháp subgradient]({% multilang_post_url contents/chapter08/2026-09-16-08_09_modern_applications %}). Khi hàm mục tiêu dạng tổng hữu hạn *thực sự* trơn, giới hạn nhiễu $$O(1/\sqrt{T})$$ của phương pháp ngẫu nhiên trong chương này có thể được khắc phục bằng các kỹ thuật giảm phương sai như SVRG / SAGA — xem [26-05]({% multilang_post_url contents/chapter26/2026-09-15-26_05_variance_reduction %}), nằm cùng nhóm bài về SGD.
