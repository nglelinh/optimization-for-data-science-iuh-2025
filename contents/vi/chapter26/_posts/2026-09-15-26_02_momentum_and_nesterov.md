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


Trên các hàm bậc hai có số điều kiện xấu, gradient descent thường dao động zíc-zắc: kích thước bước đủ nhỏ để ổn định theo phương có độ cong lớn lại trở nên quá chậm theo phương phẳng. **Động lượng (Momentum)** duy trì một vector vận tốc nhằm tích lũy các thành phần gradient cùng hướng và triệt tiêu các thành phần đổi dấu liên tục. Bài này tập trung vào trực giác hình học theo phong cách Distill thay vì lặp lại biến đổi đại số của FISTA ở [09-05-01]({% multilang_post_url contents/chapter09/20-01-08-09_05_01_accelerated_proximal_gradient_method %}) hay hoạt họa ở [06-06]({% multilang_post_url contents/chapter06/21-03-20-06_06_gradent_descent_with_momentum %}). Bạn nên đọc song song bài viết của Goh, *[Why Momentum Really Works](https://distill.pub/2017/momentum/)* (Distill, 2017).

## Thung lũng bậc hai khiến GD thuần hội tụ chậm

Xét bài toán mô hình cơ bản cho mọi phương pháp bậc nhất:

$$
F(w)=\tfrac12 w^\top A w,\qquad A=\operatorname{diag}(\lambda_1,\ldots,\lambda_d)\succ 0.
$$

Gradient của hàm là $$Aw$$. Gradient descent với tốc độ học $$\eta$$ tạo ra hệ thức tuyến tính $$w_{k+1}=(I-\eta A)w_k$$, nên từng tọa độ riêng tiến triển độc lập theo lũy thừa $$(1-\eta\lambda_i)^k$$. Điều kiện ổn định trên phương có trị riêng lớn nhất đòi hỏi $$\eta<2/\lambda_{\max}$$. Khi đó, trên phương phẳng nhất, hệ số co chỉ đạt $$1-\eta\lambda_{\min}\approx 1-2/\kappa$$ với $$\kappa=\lambda_{\max}/\lambda_{\min}$$ là số điều kiện. Đó là nguồn gốc của quỹ đạo zíc-zắc: điểm lặp bật qua lại giữa hai thành dốc của thung lũng và tiến rất chậm dọc đáy. Chương 06 đã chứng minh cùng hệ số co $$1-m/L$$ dưới giả thiết lồi mạnh; ở đây ta quan sát trực tiếp hiện tượng đó qua hai thang độ cong trên hàm bậc hai.

Mở [gradient_descent_demo.html](https://nglelinh.github.io/interactive_math/optimization/gradient_descent_demo.html) và kéo giãn một trục tọa độ để thấy rõ hành vi này của phương pháp bậc nhất không có bộ nhớ.

## Heavy ball: bộ lọc thông thấp đối với gradient

Phương pháp **heavy ball của Polyak** (1964) bổ sung một biến vận tốc $$v_k$$:

$$
\begin{align}
v_{k+1} &= \beta v_k + \nabla F(w_k), \\
w_{k+1} &= w_k - \eta v_{k+1},
\end{align}
$$

với hệ số $$\beta\in[0,1)$$. Cài đặt `SGD(momentum=…)` của PyTorch thuộc họ này (quy ước nhân thêm $$(1-\beta)$$ ở mục 06-06 chỉ khác ở hệ số tỉ lệ của trung bình trượt mũ). Khai triển truy hồi cho:

$$
v_{k+1}=\sum_{j=0}^{k}\beta^{k-j}\nabla F(w_j),
$$

cho thấy các thành phần gradient *giữ cùng dấu* qua nhiều bước được cộng dồn, còn các thành phần *đổi dấu luân phiên* tự triệt tiêu nhau. Đây chính là một bộ lọc thông thấp rời rạc: thành phần vuông góc với đáy thung lũng dao động rồi tắt dần, còn thành phần dọc theo thung lũng được khuếch đại đều đặn.

Trên cùng hàm bậc hai, khử biến $$v$$ cho ta hệ thức truy hồi bậc hai:

$$
w_{k+1}=\bigl((1+\beta)I-\eta A\bigr)w_k-\beta w_{k-1}.
$$

Mỗi tọa độ riêng ứng với đa thức đặc trưng $$r^2-(1+\beta-\eta\lambda)r+\beta=0$$. Khi biết trước số điều kiện $$\kappa$$, bộ tham số tối ưu (như phân tích của Goh) đặt cả hai nghiệm lên đường tròn bán kính $$(\sqrt{\kappa}-1)/(\sqrt{\kappa}+1)$$:

$$
\eta^\star=\Bigl(\frac{2}{\sqrt{\lambda_{\max}}+\sqrt{\lambda_{\min}}}\Bigr)^2,\qquad
\beta^\star=\Bigl(\frac{\sqrt{\kappa}-1}{\sqrt{\kappa}+1}\Bigr)^2.
$$

Hệ số co cải thiện từ $$1-\Theta(1/\kappa)$$ lên $$1-\Theta(1/\sqrt{\kappa})$$ — cùng mức cải thiện căn bậc hai theo số điều kiện như trong tăng tốc Nesterov. Ý chính cần nhớ không phải hai công thức tham số trên, mà là bản chất của phương pháp: **momentum thay đổi cơ chế tắt dần trong thời gian rời rạc chứ không tính thêm thông tin gradient mới**.

Một trực giác vật lý quen thuộc (đã nhắc ở mục 06-06) là phương trình vi phân heavy-ball $$m\ddot w+\gamma\dot w+\nabla F(w)=0$$: ma sát quá nhỏ gây dao động vượt đích, còn ma sát quá lớn khiến chuyển động chậm chạp. Siêu tham số $$\beta$$ đóng vai trò hệ số ma sát rời rạc tương ứng. Trong thực hành học sâu, các giá trị $$\beta=0.9$$ (hoặc $$0.99$$) là lựa chọn mặc định ổn định vì ta hiếm khi biết trước $$\kappa$$ của một mạng nơ-ron sâu.

## Tăng tốc Nesterov: tính gradient tại điểm nhìn trước

**Tăng tốc Nesterov** giữ nguyên cấu trúc vận tốc nhưng tính gradient tại điểm *nhìn trước (look-ahead)*:

$$
\begin{align}
v_{k+1} &= \beta v_k + \nabla F(w_k-\eta\beta v_k), \\
w_{k+1} &= w_k-\eta v_{k+1}.
\end{align}
$$

Trong heavy ball, gradient tại điểm *hiện tại* được cộng vào vận tốc vốn đã có quán tính lớn; nếu vận tốc đó sắp đưa điểm lặp vượt qua đáy, thuật toán chỉ phát hiện ở bước sau. Ngược lại, bước nhìn trước đánh giá độ dốc tại vị trí ước lượng *phía trước một bước theo vận tốc hiện tại*, giúp hiệu chỉnh hướng sớm hơn một nhịp và giảm biên độ vượt đích.

Đối với hàm *lồi và trơn*, khi lập lịch $$\beta_k$$ thích hợp (công thức cổ điển $$\beta_k=(t_k-1)/t_{k+1}$$ với $$t_{k+1}=(1+\sqrt{1+4t_k^2})/2$$, hoặc trọng số $$(k-2)/(k+1)$$ như trong FISTA ở [09-05-01]({% multilang_post_url contents/chapter09/20-01-08-09_05_01_accelerated_proximal_gradient_method %})), phương pháp đạt tốc độ hội tụ tối ưu trong lớp bậc nhất:

$$
F(w_T)-F^\star=O\bigl(L\|w_0-w^\star\|_2^2/T^2\bigr).
$$

Cần lưu ý định lý này đòi hỏi hàm $$F$$ *lồi* và hệ số $$\beta_k$$ *thay đổi theo vòng lặp*. Tùy chọn Nesterov trong học sâu (`torch.optim.SGD(..., nesterov=True)`) thường dùng $$\beta$$ *hằng số* trên hàm mất mát không lồi; do đó chứng minh lý thuyết giúp hiểu cơ chế giảm dao động, nhưng không nên suy diễn trực tiếp tốc độ $$O(1/T^2)$$ cho độ chính xác trên tập dữ liệu ảnh.

<div class="content-box insight-box">
<strong>Lý thuyết và thực hành.</strong> Tốc độ $$O(1/T^2)$$ của Nesterov đòi hỏi $$\beta_k$$ được lập lịch và $$F$$ lồi trơn; hệ số $$\sqrt{\kappa}$$ của heavy ball đòi hỏi hàm bậc hai (hoặc xấp xỉ bậc hai cục bộ). Phần trực giác giữ lại khi sang huấn luyện với AdamW là cơ chế lọc: các hướng nhất quán được duy trì qua nhiều bước, các hướng dao động bị làm dịu, và bước nhìn trước giúp điều tiết quán tính sớm hơn.
</div>

## Cài đặt và quan sát

Hai phương pháp chỉ khác nhau ở đúng đối số truyền vào gradient. Ngay trên hàm bậc hai hai chiều $$F(w)=\tfrac12 w^\top\operatorname{diag}(1,100)\,w$$, quỹ đạo của chúng đã khác biệt rõ rệt:

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

Hãy xuất phát cả hai thuật toán từ cùng một điểm $$w_0$$, thử các giá trị $$\beta\in\{0,0.5,0.8,0.9,0.99\}$$ với cùng bước $$\eta$$ ổn định cho GD thuần, rồi vẽ các quỹ đạo để quan sát ngưỡng $$\beta$$ bắt đầu làm mượt zíc-zắc và ngưỡng gây dao động vượt đích.

Về liên hệ giữa các chương: FISTA ở Chương 09 là phiên bản *proximal* của cùng cơ chế nhìn trước cho bài toán hợp thành $$g+h$$; Adam ở Chương 26 dùng trung bình trượt mũ cho cả gradient (chính là momentum) lẫn bình phương gradient từng tọa độ; còn giảm phương sai ([26-05]({% multilang_post_url contents/chapter26/2026-09-15-26_05_variance_reduction %})) giải quyết một vấn đề khác — triệt tiêu nhiễu *lấy mẫu* chứ không phải zíc-zắc do *số điều kiện*.

**Bài tập 1.** Cài đặt ba hàm cập nhật trên. Với $$\eta=2/(\lambda_{\min}+\lambda_{\max})$$ (bước tối ưu của GD) và $$\beta=\beta^\star$$, đếm số vòng lặp để đạt $$\|w\|_2\le 10^{-4}$$. Sau đó giữ nguyên $$\eta$$ và đặt $$\beta=0.99$$: phương pháp nào dao động mạnh hơn và vì sao bước nhìn trước cải thiện được hiện tượng đó?

**Bài tập 2.** Trên cùng bài toán bậc hai, thay $$A$$ bằng một ma trận đối xứng xác định dương ngẫu nhiên có cùng tập trị riêng ($$A=Q\operatorname{diag}(\lambda)Q^\top$$). Kiểm chứng rằng lợi ích của momentum phụ thuộc vào *phổ trị riêng* chứ không phụ thuộc vào việc hàm mục tiêu có thẳng hàng theo trục tọa độ hay không.

**Câu hỏi.** Với nhận xét thực nghiệm rằng SGD dễ thoát khỏi vùng trũng nông hơn GD toàn lô, ta nên điều chỉnh $$\beta$$ theo hướng nào khi chuyển từ hàm bậc hai sang một mạng nơ-ron không lồi nhỏ, và mô hình bộ lọc thông thấp dự đoán điều gì đối với thành phần nhiễu gradient đổi dấu liên tục giữa các minibatch?
