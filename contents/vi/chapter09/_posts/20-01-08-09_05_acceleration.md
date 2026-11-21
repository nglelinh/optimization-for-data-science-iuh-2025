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

Proximal gradient descent trên bài toán tổng hợp $$\min_x g(x)+h(x)$$ đã có tốc độ sạch $$O(1/k)$$ khi $$\nabla g$$ Lipschitz (bài 09-02). **Tăng tốc** là bộ nhớ thêm nâng tốc độ đó lên $$O(1/k^2)$$ bậc nhất tối ưu trên $$g$$ lồi trơn, mà không lập Hessian. Trang này là *bức tranh* kiểu Distill đứng trước đại số FISTA. Thuật toán và chứng minh $$O(1/k^2)$$ nằm ở [09-05-01]({% multilang_post_url contents/chapter09/20-01-08-09_05_01_accelerated_proximal_gradient_method %}) và [09-05-02]({% multilang_post_url contents/chapter09/20-01-08-09_05_02_convergence_analysis %}); họ hàng ngẫu nhiên, $$\beta$$ hằng dùng để huấn luyện mạng là [26-02]({% multilang_post_url contents/chapter26/2026-09-15-26_02_momentum_and_nesterov %}).

## Vì sao một bước proximal trần đi zíc-zac

Viết một bước proximal gradient như “bước gradient trên phần trơn, rồi bật lại bằng $$\operatorname{prox}_{t h}$$.” Khi $$h=0$$ đây là gradient descent thường, và phản ví dụ lớp học lại là thung lũng dài $$g(x)=\tfrac12 x^\top\operatorname{diag}(1,L)\,x$$. Bước đủ nhỏ để không nảy tường sắc thì bò dọc sàn. Momentum — ý tưởng Nesterov đưa vào cho bài lồi trơn năm 1983, và Beck–Teboulle (2009) quấn quanh ánh xạ proximal thành **FISTA** — lưu vị trí *trước đó* và ngoại suy trước prox.

Look-ahead FISTA của 09-05-01 là

$$
\begin{align}
v^{(k)} &= x^{(k-1)}+\frac{k-2}{k+1}\bigl(x^{(k-1)}-x^{(k-2)}\bigr),\\
x^{(k)} &= \operatorname{prox}_{t_k h}\bigl(v^{(k)}-t_k\nabla g(v^{(k)})\bigr).
\end{align}
$$

Trọng số $$(k-2)/(k+1)$$ bắt đầu từ không (bước đầu *chính là* proximal gradient) và leo tới $$1$$. Lịch đó không phải mặc định thẩm mỹ; nó là analogue rời rạc của tắt dần thời gian liên tục làm khép chứng minh $$O(1/k^2)$$ của Nesterov. Bài Distill của Goh *[Why Momentum Really Works](https://distill.pub/2017/momentum/)* là cùng hình học không có prox: một hệ thức bậc hai mà nghiệm đặc trưng có thể đặt trên đường tròn bán kính $$(\sqrt{\kappa}-1)/(\sqrt{\kappa}+1)$$, biến cuộc bò $$1-\Theta(1/\kappa)$$ thành cú lướt $$1-\Theta(1/\sqrt{\kappa})$$.

## Nesterov so với “Nesterov PyTorch”

Hai đối tượng cùng tên trong giáo trình này, và chúng không hoán đổi được.

Trên $$g$$ *lồi trơn* (hoặc tổng hợp $$g+h$$ với $$h$$ lồi), Nesterov / FISTA dùng trọng số momentum **lên lịch** và tính gradient trơn tại điểm ngoại suy $$v$$. Định lý là $$g(x^{(k)})+h(x^{(k)})-F^\star=O(1/k^2)$$, khớp cận dưới bậc nhất của [06-03-06]({% multilang_post_url contents/chapter06/21-03-20-06_03_06_can_we_do_better %}). Các đường ISTA-đối-FISTA trên Lasso ở [09-05-03]({% multilang_post_url contents/chapter09/20-01-08-09_05_03_example_FISTA %}) là hình bạn phải vẽ lại được.

Trên *mạng sâu*, `torch.optim.SGD(..., nesterov=True)` thường là look-ahead $$\beta\approx 0.9$$ **hằng** trên mất mát không lồi. Trực giác bộ lọc còn lại — hướng nhất quán được nhớ lâu hơn, hướng dao động triệt nhau, nhìn trước giảm vượt đích — nhưng giấy chứng nhận $$O(1/k^2)$$ thì không. Bài 26-02 là chỗ phân biệt đó được viết đủ, gồm đa thức đặc trưng heavy-ball và so sánh NumPy hai dòng.

<div class="content-box insight-box">
<strong>Một câu để giữ.</strong> FISTA là look-ahead của Nesterov <em>cộng</em> một prox, với trọng số phụ thuộc $$k$$. Momentum học sâu là cùng look-ahead với trọng số bị đóng băng. Dùng định lý lên lịch trên Lasso và hồi quy logistic; dùng thung lũng Distill cho mọi thứ khác.
</div>

## Khi tăng tốc là núm sai để vặn trước

Tăng tốc không phải tốc độ miễn phí. Cùng quán tính lướt xuống thung lũng lồi có thể vượt một gấp không trơn hoặc một lưu vực nhỏ, đó là vì sao [09-05-04]({% multilang_post_url contents/chapter09/20-01-08-09_05_04_is_acceleration_always_useful %}) tồn tại và vì sao FISTA khởi động lại là cách sửa chuẩn. Nếu phần trơn rẻ và lồi mạnh, một bước proximal gradient chỉnh tốt (hoặc anh em giảm phương sai ở [26-05]({% multilang_post_url contents/chapter26/2026-09-15-26_05_variance_reduction %})) có thể thắng phương pháp tăng tốc không restart trên thời gian tường. Theo dõi hàm mục tiêu; nếu thấy “gợn Nesterov” nổi tiếng, hãy restart hoặc hạ $$\beta$$.

**Bài tập.** Trên thung lũng $$g(x)=\tfrac12 x^\top\operatorname{diag}(1,100)\,x$$ với $$h=0$$, vẽ ISTA (GD trần), FISTA với trọng số $$(k-2)/(k+1)$$, và Nesterov $$\beta$$ hằng từ 26-02. Lịch nào tới $$\|x\|_2\le 10^{-4}$$ trước, và lịch nào rung quanh gốc nếu bạn quên restart?

**Câu hỏi.** Trọng số FISTA tiến tới $$1$$. $$\beta^\star$$ heavy-ball tối ưu của Distill khi biết $$\kappa$$ thì nhỏ hơn $$1$$ nghiêm ngặt. Vì sao cả hai đều có thể đúng — và điều gì đổi khi bạn *không* biết $$\kappa$$?
