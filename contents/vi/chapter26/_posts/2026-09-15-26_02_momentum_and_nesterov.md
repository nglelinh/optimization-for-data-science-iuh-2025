---
layout: post
title: 26-02 Momentum và tăng tốc Nesterov
chapter: '26'
order: 3
owner: Nguyen Le Linh
categories:
- chapter26
lang: vi
lesson_type: required
---


Gradient descent trên toàn phương điều kiện xấu đi zíc-zac: bước an toàn với trị riêng sắc thì quá nhỏ theo phương phẳng. **Momentum** giữ một vận tốc tích các thành phần gradient nhất quán và triệt các thành phần dao động. Bài này là *vì sao* theo phong cách Distill, không phải bản sao đại số FISTA ở [09-05-01]({% multilang_post_url contents/chapter09/20-01-08-09_05_01_accelerated_proximal_gradient_method %}) hay hoạt họa trong trang ở [06-06]({% multilang_post_url contents/chapter06/21-03-20-06_06_gradent_descent_with_momentum %}). Đọc Goh, *[Why Momentum Really Works](https://distill.pub/2017/momentum/)* (Distill, 2017), với thung lũng toàn phương mở ở tab khác; ghi chú dưới đây là bản nói trên lớp của bức tranh đó.

## Thung lũng mà GD thuần không đi nổi

Lấy bài toán mô hình mà mọi phương pháp bậc nhất đều đang giải ngầm,

$$
F(w)=\tfrac12 w^\top A w,\qquad A=\operatorname{diag}(\lambda_1,\ldots,\lambda_d)\succ 0.
$$

Gradient là $$Aw$$. Gradient descent với bước $$\eta$$ là hệ thức tuyến tính $$w_{k+1}=(I-\eta A)w_k$$, nên mỗi tọa độ riêng tiến độc lập như $$(1-\eta\lambda_i)^k$$. Ổn định trên trục sắc nhất buộc $$\eta<2/\lambda_{\max}$$. Trục phẳng nhất khi đó chỉ co với $$1-\eta\lambda_{\min}\approx 1-2/\kappa$$, với $$\kappa=\lambda_{\max}/\lambda_{\min}$$ là số điều kiện. Đó là zíc-zac: bạn nảy tường của một hành lang dài và bò dọc hành lang. Chương 06 đã chứng minh cùng hệ số $$1-m/L$$ dưới lồi mạnh; ở đây ta *nhìn* nó như hai thang thời gian trên một toàn phương.

Mở [gradient_descent_demo.html](https://nglelinh.github.io/interactive_math/optimization/gradient_descent_demo.html) và kéo giãn một trục. Quỹ đạo trông “sai” chính là phương pháp bậc nhất tối ưu *không nhớ*.

## Heavy ball: bộ lọc thông thấp trên gradient

**Heavy ball của Polyak** (1964) đưa vào một vận tốc

$$
\begin{align}
v_{k+1} &= \beta v_k + \nabla F(w_k), \\
w_{k+1} &= w_k - \eta v_{k+1},
\end{align}
$$

với $$\beta\in[0,1)$$. `SGD(momentum=…)` của PyTorch thuộc họ này, tùy gradient được nhân trước hay sau khi trộn (quy ước $$(1-\beta)$$ ở 06-06 là trung bình trượt mũ của cùng một đối tượng). Khai triển cho

$$
v_{k+1}=\sum_{j=0}^{k}\beta^{k-j}\nabla F(w_j),
$$

nên hướng *giữ cùng dấu* được khuếch đại và hướng *đổi dấu mỗi bước* bị triệt. Đó đúng là bộ lọc thông thấp rời rạc. Trong hành lang, thành phần pháp tuyến tường dao động rồi tắt; thành phần dọc hành lang nhất quán và trở thành tốc độ hành trình.

Trên cùng toàn phương, hệ thức đóng là bậc hai,

$$
w_{k+1}=(1+\beta)(I-\eta A)w_k-\beta w_{k-1}
$$

(sau y hệt phép viết lại affine thông thường). Mỗi mode riêng có đa thức đặc trưng $$r^2-(1+\beta)(1-\eta\lambda)r+\beta=0$$. Bộ tham số tối ưu của Goh khi biết $$\kappa$$ đặt cả hai nghiệm trên một đường tròn bán kính $$(\sqrt{\kappa}-1)/(\sqrt{\kappa}+1)$$:

$$
\eta^\star=\Bigl(\frac{2}{\sqrt{\lambda_{\max}}+\sqrt{\lambda_{\min}}}\Bigr)^2,\qquad
\beta^\star=\Bigl(\frac{\sqrt{\kappa}-1}{\sqrt{\kappa}+1}\Bigr)^2.
$$

Hệ số co cải thiện từ $$1-\Theta(1/\kappa)$$ thành $$1-\Theta(1/\sqrt{\kappa})$$ — cùng phép màu căn bậc hai của số điều kiện mà tốc độ lồi *tối ưu* của Nesterov sẽ đòi ở mục sau. Bạn không cần thuộc hai hằng số trưng bày; bạn cần khẩu hiệu: **momentum là đổi hệ số tắt dần thời gian rời rạc, không phải một gradient mới**.

Hình ảnh vật lý hữu ích, đã gợi ở 06-06, là ODE heavy-ball $$m\ddot w+\gamma\dot w+\nabla F(w)=0$$. Ma sát quá ít thì bạn quay quỹ đạo; quá nhiều thì bò. Siêu tham số $$\beta$$ là ma sát đó trong thời gian rời rạc. Thực hành học sâu ($$\beta=0.9$$, đôi khi $$0.99$$) là mặc định bền, không phải $$\beta^\star$$ tối ưu của Goh — ta hầu như không biết $$\kappa$$ của một ResNet.

## Nesterov: tính gradient tại chỗ bạn sắp tới

**Tăng tốc Nesterov** giữ cùng vận tốc nhưng tính gradient tại điểm *nhìn trước*

$$
\begin{align}
v_{k+1} &= \beta v_k + \nabla F(w_k-\eta\beta v_k), \\
w_{k+1} &= w_k-\eta v_{k+1}.
\end{align}
$$

Heavy ball cộng gradient tại điểm *hiện tại* vào một vận tốc đã chỉ xuống hành lang; nếu vận tốc đó sắp vượt đích, bạn chỉ biết sau khi đã rời chỗ. Nhìn trước hỏi độ dốc *một bước phía trước theo vận tốc hiện tại*, nên hiệu chỉnh bắt đầu sớm hơn một nhịp. Sơ đồ vector của Distill là slide đúng: hai mũi tên (vận tốc cũ, gradient mới) đối với hai mũi tên (vận tốc cũ, gradient tại điểm ngoại suy). Cặp thứ hai rẽ sớm hơn ở đáy chén.

Trên bài toán *lồi trơn*, một $$\beta_k$$ lên lịch cẩn thận (cổ điển $$\beta_k=(t_k-1)/t_{k+1}$$ với $$t_{k+1}=(1+\sqrt{1+4t_k^2})/2$$, hoặc trọng số FISTA $$(k-2)/(k+1)$$ của [09-05-01]({% multilang_post_url contents/chapter09/20-01-08-09_05_01_accelerated_proximal_gradient_method %})) cho tốc độ bậc nhất tối ưu

$$
F(w_T)-F^\star=O\bigl(L\|w_0-w^\star\|_2^2/T^2\bigr).
$$

Đó là định lý về một $$F$$ *lồi* và momentum *biến thiên theo thời gian*. “Nesterov” trong học sâu (`torch.optim.SGD(..., nesterov=True)`) thường là look-ahead $$\beta$$ *hằng* trên mất mát không lồi. Dùng chứng minh để hiểu *vì sao* nhìn trước làm giảm dao động; đừng trích $$O(1/T^2)$$ cho accuracy CIFAR.

<div class="content-box insight-box">
<strong>Lý thuyết ≠ thực hành.</strong> $$O(1/T^2)$$ của Nesterov cần $$\beta_k$$ lên lịch và $$F$$ lồi trơn. Bộ $$\sqrt{\kappa}$$ của heavy ball cần toàn phương (hoặc một chén toàn phương địa phương). Điều chuyển sang huấn luyện AdamW là trực giác bộ lọc: hướng nhất quán được nhớ lâu hơn; hướng dao động bị triệt; nhìn trước tiêu bộ nhớ đó cẩn thận hơn một chút.
</div>

## Cài gì, và xem gì

Hai phương pháp khác nhau ở đúng một đối số gradient. Trên toàn phương lớp học $$F(w)=\tfrac12 w^\top\operatorname{diag}(1,100)\,w$$ chúng đã trông khác:

```python
import numpy as np

A = np.diag([1.0, 100.0])

def gd(w, eta):
    return w - eta * (A @ w)

def heavy_ball(w, v, eta, beta):
    v = beta * v + A @ w
    return w - eta * v, v

def nesterov(w, v, eta, beta):
    look = w - eta * beta * v
    v = beta * v + A @ look
    return w - eta * v, v
```

Xuất phát cả hai từ cùng $$w_0$$, quét $$\beta\in\{0,0.5,0.8,0.9,0.99\}$$ ở bước ổn định với GD thuần, và vẽ hai quỹ đạo. $$\beta$$ đầu tiên làm hết zíc-zac nhìn thấy là bài Distill trong một hình; $$\beta$$ rồi *vượt* gốc là bức tranh “ma sát quá ít”.

FISTA ở Chương 09 là anh em *proximal* của cùng look-ahead (tổng hợp $$g+h$$, trọng số lên lịch). Adam ở Chương 26 sẽ đặt trung bình trượt mũ trên gradient *và* trên bình phương từng tọa độ — momentum là trung bình thứ nhất trong hai cái đó. Giảm phương sai ([26-05]({% multilang_post_url contents/chapter26/2026-09-15-26_05_variance_reduction %})) là thuốc khác cho bệnh khác: nó giết nhiễu *lấy mẫu*, không phải zíc-zac *điều kiện*.

**Bài tập 1.** Cài ba cập nhật trên. Với $$\eta=2/(\lambda_{\min}+\lambda_{\max})$$ (bước GD tối ưu) và $$\beta=\beta^\star$$, đếm số vòng tới $$\|w\|_2\le 10^{-4}$$. Rồi phá bộ tham số: giữ $$\eta$$ và đặt $$\beta=0.99$$. Phương pháp nào dao động hơn, và vì sao nhìn trước giúp?

**Bài tập 2.** Trên cùng toàn phương, thay $$A$$ bằng ma trận SPD ngẫu nhiên cùng trị riêng ($$A=Q\operatorname{diag}(\lambda)Q^\top$$). Tự thuyết phục rằng lợi của momentum là *phổ*, không phải thẳng trục.

**Câu hỏi.** Cho quan sát thực nghiệm rằng SGD thường thoát lưu vực nông khéo hơn GD cả lô, bạn nên tăng hay giảm $$\beta$$ khi chuyển từ thung lũng toàn phương sang một mạng không lồi nhỏ — và bức tranh bộ lọc của Distill dự đoán gì về gradient nhiễu đổi dấu mỗi minibatch?
