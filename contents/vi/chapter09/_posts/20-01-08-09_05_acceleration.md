---
layout: post
title: '09-05 Tăng tốc'
chapter: '09'
order: 6
owner: Kyeongmin Woo
categories:
- chapter09
lang: vi
---

# Tăng tốc

Phương pháp gradient gần kề trên bài toán tổng hợp $$\min_x g(x)+h(x)$$ đã đạt tốc độ hội tụ $$O(1/k)$$ khi $$\nabla g$$ liên tục Lipschitz (bài 09-02). **Tăng tốc (acceleration)** là kỹ thuật bổ sung thành phần động lượng giúp nâng tốc độ hội tụ lên mức tối ưu bậc nhất $$O(1/k^2)$$ cho lớp hàm lồi trơn $$g$$ mà không cần tính ma trận Hessian. Bài học này trình bày góc nhìn trực quan theo phong cách Distill trước khi đi vào phần biến đổi đại số của FISTA. Thuật toán và chứng minh tốc độ $$O(1/k^2)$$ nằm ở [09-05-01]({% multilang_post_url contents/chapter09/20-01-08-09_05_01_accelerated_proximal_gradient_method %}) và [09-05-02]({% multilang_post_url contents/chapter09/20-01-08-09_05_02_convergence_analysis %}); biến thể ngẫu nhiên với hệ số $$\beta$$ cố định dùng trong huấn luyện mạng nơ-ron nằm ở [26-02]({% multilang_post_url contents/chapter26/2026-09-15-26_02_momentum_and_nesterov %}).

## Vì sao bước gradient gần kề tiêu chuẩn dễ dao động zíc-zắc

Có thể hình dung một bước gradient gần kề là: thực hiện một bước gradient trên phần trơn, sau đó điều chỉnh lại bằng $$\operatorname{prox}_{t h}$$. Khi $$h=0$$, thuật toán trở về gradient descent thông thường, và ví dụ kinh điển là thung lũng hẹp $$g(x)=\tfrac12 x^\top\operatorname{diag}(1,L)\,x$$: kích thước bước đủ nhỏ để không dao động theo chiều dốc lại khiến thuật toán tiến rất chậm dọc theo đáy thung lũng. Kỹ thuật động lượng — do Nesterov đề xuất cho hàm lồi trơn năm 1983, và được Beck–Teboulle (2009) mở rộng kèm ánh xạ gần kề thành **FISTA** — lưu lại điểm lặp *trước đó* để ngoại suy vị trí trước khi áp dụng toán tử gần kề.

Bước ngoại suy nhìn trước (look-ahead) của FISTA ở bài 09-05-01 có dạng:

$$
\begin{align}
v^{(k)} &= x^{(k-1)}+\frac{k-2}{k+1}\bigl(x^{(k-1)}-x^{(k-2)}\bigr),\\
x^{(k)} &= \operatorname{prox}_{t_k h}\bigl(v^{(k)}-t_k\nabla g(v^{(k)})\bigr).
\end{align}
$$

Trọng số $$(k-2)/(k+1)$$ khởi đầu từ $$0$$ (bước đầu tiên trùng với gradient gần kề tiêu chuẩn) và tăng dần tiến tới $$1$$. Lịch trình này không phải lựa chọn tùy ý, mà là phiên bản rời rạc của cơ chế tắt dần trong thời gian liên tục giúp hoàn tất chứng minh tốc độ $$O(1/k^2)$$ của Nesterov. Bài viết trên Distill của Goh, *[Why Momentum Really Works](https://distill.pub/2017/momentum/)*, minh họa đúng hình học này trong trường hợp không có prox: một hệ thức truy hồi bậc hai với nghiệm đặc trưng nằm trên đường tròn bán kính $$(\sqrt{\kappa}-1)/(\sqrt{\kappa}+1)$$, cải thiện hệ số co từ $$1-\Theta(1/\kappa)$$ thành $$1-\Theta(1/\sqrt{\kappa})$$.

## Tăng tốc Nesterov lý thuyết và “Nesterov trong PyTorch”

Hai khái niệm mang cùng tên trong giáo trình này có bản chất khác nhau và không thể dùng thay thế cho nhau một cách tùy tiện.

Trên hàm $$g$$ *lồi trơn* (hoặc bài toán tổng hợp $$g+h$$ với $$h$$ lồi), Nesterov / FISTA sử dụng trọng số động lượng **thay đổi theo lịch trình** và tính gradient của phần trơn tại điểm ngoại suy $$v$$. Khi đó ta có bảo đảm $$g(x^{(k)})+h(x^{(k)})-F^\star=O(1/k^2)$$, đạt đúng cận dưới lý thuyết của các phương pháp bậc nhất ở [06-03-06]({% multilang_post_url contents/chapter06/21-03-20-06_03_06_can_we_do_better %}). Biểu đồ so sánh ISTA và FISTA trên bài toán Lasso ở [09-05-03]({% multilang_post_url contents/chapter09/20-01-08-09_05_03_example_FISTA %}) là kết quả thực nghiệm cần nắm vững.

Trên *mạng nơ-ron sâu*, `torch.optim.SGD(..., nesterov=True)` thường dùng hệ số động lượng **cố định** $$\beta\approx 0.9$$ trên hàm mất mát không lồi. Trực giác về bộ lọc vẫn hữu ích — các hướng nhất quán được tích lũy, các hướng dao động triệt tiêu nhau, và bước nhìn trước giúp giảm hiện tượng vượt đích — nhưng không còn bảo đảm lý thuyết $$O(1/k^2)$$. Bài 26-02 phân tích chi tiết sự khác biệt này, bao gồm đa thức đặc trưng của phương pháp heavy-ball và đoạn mã so sánh ngắn bằng NumPy.

<div class="content-box insight-box">
<strong>Điểm cốt lõi cần nhớ.</strong> FISTA là bước nhìn trước Nesterov <em>kết hợp</em> toán tử gần kề với trọng số thay đổi theo $$k$$. Động lượng trong học sâu dùng cùng ý tưởng nhìn trước nhưng cố định trọng số. Áp dụng định lý theo lịch trình cho các bài toán lồi như Lasso hay hồi quy logistic; dùng trực giác thung lũng của Distill cho các bài toán khác.
</div>

## Khi tăng tốc chưa chắc là lựa chọn tối ưu

Tăng tốc không mang lại lợi ích miễn phí trong mọi trường hợp. Chính quán tính giúp di chuyển nhanh dọc đáy thung lũng lồi cũng có thể khiến quỹ đạo vượt quá điểm gấp khúc không trơn hoặc vùng cực tiểu hẹp — đó là lý do tồn tại bài [09-05-04]({% multilang_post_url contents/chapter09/20-01-08-09_05_04_is_acceleration_always_useful %}) và kỹ thuật khởi động lại (restart) cho FISTA. Nếu phần trơn có chi phí tính thấp và lồi mạnh, phương pháp gradient gần kề được tinh chỉnh tốt (hoặc các phương pháp giảm phương sai ở [26-05]({% multilang_post_url contents/chapter26/2026-09-15-26_05_variance_reduction %})) có thể nhanh hơn phương pháp tăng tốc không có restart xét theo thời gian thực thi thực tế. Cần theo dõi giá trị hàm mục tiêu: nếu xuất hiện dao động kiểu “gợn sóng Nesterov”, hãy áp dụng restart hoặc giảm $$\beta$$.

**Bài tập.** Trên thung lũng $$g(x)=\tfrac12 x^\top\operatorname{diag}(1,100)\,x$$ với $$h=0$$, hãy vẽ đường hội tụ của ISTA (GD tiêu chuẩn), FISTA với trọng số $$(k-2)/(k+1)$$, và Nesterov với $$\beta$$ cố định từ bài 26-02. Phương pháp nào đạt $$\|x\|_2\le 10^{-4}$$ sớm nhất, và phương pháp nào dao động quanh gốc tọa độ nếu không dùng restart?

**Câu hỏi.** Trọng số của FISTA tiến tới $$1$$, trong khi trọng số heavy-ball tối ưu $$\beta^\star$$ theo bài Distill (khi biết số điều kiện $$\kappa$$) luôn nhỏ hơn $$1$$ nghiêm ngặt. Vì sao cả hai kết quả này đều đúng — và điều gì thay đổi khi ta *không* biết trước $$\kappa$$?
