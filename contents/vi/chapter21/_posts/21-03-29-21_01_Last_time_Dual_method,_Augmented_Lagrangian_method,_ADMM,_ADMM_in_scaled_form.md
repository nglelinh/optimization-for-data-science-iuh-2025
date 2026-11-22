---
layout: post
title: 21-01 Last time - Dual method, Augmented Lagrangian method, ADMM, ADMM in scaled
  form
chapter: '21'
order: 2
owner: Hooncheol Shin
categories:
- chapter21
lang: vi
---

Ở Chương 20, chúng ta đã tìm hiểu các phương pháp đối ngẫu và ADMM. Trước khi đi vào các ứng dụng cụ thể của ADMM, hãy ôn lại phương pháp đối ngẫu, phương pháp Lagrangian tăng cường (augmented Lagrangian), ADMM và ADMM ở dạng chuẩn hóa (scaled form).

## Phương pháp đối ngẫu

Xét bài toán tối ưu sau:

>$$
>\begin{align}
>&\min_{x} &&f(x) \\\\
>&\text{ subject to } &&Ax = b
>\end{align}
>$$

Giả sử $$f$$ là hàm lồi chặt và đóng. Hàm Lagrange của bài toán là:
>$$
>\begin{align}
>L(x,u) = f(x)+u^{T}(Ax-b)
>\end{align}
>$$

Bài toán đối ngẫu tương ứng là:
>$$
>\begin{equation}
>\max_u -f^{\ast}(-A^T u) - b^T u
>\end{equation}
>$$

trong đó $$u$$ là biến đối ngẫu.

Phương pháp tăng gradient đối ngẫu (dual gradient ascent) lặp lại các bước cập nhật sau với $$k=1,2,3,\ldots$$:
>$$
>\begin{align}
>x^{(k)}&=\underset{x}{\operatorname{argmin}} L(x,u^{(k-1)}) \\\\
>u^{(k)}&= u^{(k-1)} +t_{k}(Ax^{(k)}-b)
>\end{align}
>$$

Ở đây $$t_{k}$$ là kích thước bước tại vòng lặp thứ $$k$$.

Trong phương pháp này, biến gốc $$x$$ được cập nhật tại điểm cực tiểu hóa hàm Lagrange ứng với biến đối ngẫu $$u^{(k-1)}$$ từ bước trước, còn biến đối ngẫu $$u$$ được cập nhật theo bước tăng gradient dọc theo hướng $$Ax-b$$.

Ưu điểm của phương pháp đối ngẫu là khi $$f$$ phân rã được thành $$B$$ thành phần độc lập, biến $$x$$ có thể chia thành $$B$$ khối $$(x =(x_{1}, \ldots, x_{B})\in \mathbb{R}^{n}, \text{ với } x_{i}\in \mathbb{R}^{n_{i}})$$ và ma trận $$A$$ chia thành $$B$$ khối con tương ứng $$(A = [A_{1}, \ldots, A_{B}] \text{ với } A_{i} \in \mathbb{R}^{m \times n_{i}})$$, nhờ đó dễ dàng song song hóa và mở rộng quy mô. Nhược điểm là điều kiện đảm bảo hội tụ khá khắt khe: để bảo đảm tính khả thi của bài toán gốc, $$f$$ phải là hàm lồi mạnh [[20-01-01]]({% multilang_post_url contents/chapter20/21-03-27-20_01_01_Convergence_Analysis %}).

## Phương pháp Lagrangian tăng cường

Phương pháp Lagrangian tăng cường (augmented Lagrangian), còn gọi là phương pháp nhân tử (method of multipliers), bổ sung thêm một số hạng phạt bậc hai vào hàm mục tiêu. Khi quá trình lặp tiến triển, các điều kiện KKT dần được thỏa mãn. So với phương pháp đối ngẫu, phương pháp này nới lỏng điều kiện hội tụ (không đòi hỏi $$f$$ lồi mạnh), nhưng đổi lại bài toán không còn tách rời được thành các khối độc lập. Bài toán gốc được viết lại như sau:

>$$
>\begin{align}
>&\min_{x} &&f(x)+\frac{\rho}{2}||Ax-b||_{2}^{2}&\\\\
>&\text{subject to} &&Ax=b
>\end{align}
>$$

với $$\rho>0$$. Hàm Lagrange tăng cường của bài toán là:

>$$
>\begin{align}
>L_{\rho}(x,u)=f(x)+u^{T}(Ax-b)+\frac{\rho}{2}||Ax-b||_{2}^{2}.
>\end{align}
>$$

Thuật toán tăng gradient đối ngẫu lặp lại các bước sau ($$k=1,2,3,\ldots$$):
>$$
>\begin{align}
>x^{(k)}&=\underset{x}{\operatorname{argmin}} L_{\rho}(x,u^{(k-1)}) \\\\
>u^{(k)}&= u^{(k-1)} +\rho(Ax^{(k)}-b)
>\end{align}
>$$

Như đã nêu, ưu điểm của phương pháp này là điều kiện hội tụ nhẹ hơn so với phương pháp đối ngẫu, còn nhược điểm là số hạng phạt bậc hai ghép chéo các biến làm mất tính phân rã.

## Phương pháp hướng luân phiên của các nhân tử (ADMM)

ADMM kết hợp ưu điểm của cả phương pháp đối ngẫu lẫn phương pháp Lagrangian tăng cường. Xét bài toán có dạng:

>$$
>\begin{align}
>\min_{x, z} f(x)+g(z) \qquad \text{subject to  }Ax+Bz=c
>\end{align}
>$$

Với $$\rho>0$$, hàm Lagrangian tăng cường được định nghĩa là:
>$$
>\begin{align}
>&L_{\rho} (x,z,u) = f(x)+g(z)+u^{T}(Ax+Bz-c)+\frac{\rho}{2}||Ax+Bz-c||_{2}^{2}\\\\
>\end{align}
>$$

Các biến được cập nhật luân phiên qua từng vòng lặp:
>$$
>\begin{align}
>&\text{for k = 1,2,3,...}\\\\
>&x^{(k)}=\underset{x}{\operatorname{argmin}} L_{\rho}(x,z^{(k-1)},u^{(k-1)})\\\\
>&z^{(k)}=\underset{z}{\operatorname{argmin}} L_{\rho}(x^{(k)},z,u^{(k-1)})\\\\
>&u^{(k)}=u^{(k-1)}+\rho(Ax^{(k)}+Bz^{(k)}-c)
>\end{align}
>$$

Trong ADMM, hai biến gốc $$x$$ và $$z$$ không được cập nhật đồng thời mà lần lượt theo thứ tự, luôn sử dụng giá trị mới nhất của biến còn lại. Cụ thể, tại vòng lặp $$k$$, bước cập nhật $$z$$ sử dụng $$x^{(k)}$$ thay vì $$x^{(k-1)}$$, và bước cập nhật $$u$$ dùng cả $$x^{(k)}$$ lẫn $$z^{(k)}$$ vừa tính được.

## Hội tụ của ADMM

Không cần giả sử hai ma trận ràng buộc $$A$$ và $$B$$ có hạng đầy đủ, và chỉ với các giả thiết tương đối nhẹ trên $$f$$ và $$g$$, ADMM đảm bảo các tính chất sau với mọi $$\rho > 0$$:

* Hội tụ phần dư: $$r^{(k)} = A x^{(k)} + B z^{(k)} - c \to 0$$ khi $$k \to \infty$$, nghĩa là các điểm lặp gốc tiến dần về miền khả thi.
* Hội tụ hàm mục tiêu: $$f(x^{(k)}) + g(z^{(k)}) \to f^{\star} + g^{\star}$$, trong đó $$f^{\star} + g^{\star}$$ là giá trị tối ưu của bài toán gốc.
* Hội tụ biến đối ngẫu: $$u^{(k)} \to u^{\star}$$, trong đó $$u^{\star}$$ là một nghiệm đối ngẫu.

Tốc độ hội tụ trong trường hợp tổng quát vẫn là chủ đề được nghiên cứu tích cực. Các tài liệu tham khảo chi tiết về hội tụ được liệt kê ở [phần giới thiệu Chương 21]({% multilang_post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %}).

## ADMM dạng chuẩn hóa (scaled form)

ADMM có thể viết gọn hơn dưới dạng chuẩn hóa bằng cách đặt biến đối ngẫu có tỉ lệ $$w=u/\rho$$. Khi đó, các bước cập nhật trở thành:
>$$
>\begin{align}
&x^{(k)} = \underset{x}{\operatorname{argmin}} f(x) + \frac{\rho}{2} ||Ax + Bz^{(k-1)} - c + w^{(k-1)} ||_2^2 \\\\
&z^{(k)} = \underset{z}{\operatorname{argmin}} g(z) + \frac{\rho}{2} || Ax^{(k)} + Bz - c + w^{(k-1)} ||_2^2  \\\\
&w^{(k)} = w^{(k-1)} + Ax^{(k)} + Bz^{(k)} - c 
\end{align}
>$$

Ở đây $$w^{(k)}$$ chính là tổng tích lũy của các phần dư tính đến vòng lặp $$k$$, và có thể viết tường minh là:
>$$
>\begin{align}
w^{(k)} = w^{(0)} + \sum_{i=1}^k (Ax^{(i)} + Bz^{(i)} - c) 
\end{align}
>$$
