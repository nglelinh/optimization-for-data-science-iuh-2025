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

Ở chương trước (Chương 20) chúng ta đã tìm hiểu các phương pháp đối ngẫu và ADMM. Trước khi xem các ứng dụng của ADMM, hãy tóm tắt lại phương pháp đối ngẫu, phương pháp augmented Lagrangian, ADMM và ADMM dạng có tỉ lệ.

## Phương pháp đối ngẫu
Xét bài toán sau.

>$$
>\begin{align}
>&\min_{x} &&f(x) \\\\
>&\text{ subject to } &&Ax = b
>\end{align}
>$$

Giả sử $$f$$ lồi chặt và đóng. Hàm Lagrange của bài toán này là
>$$
>\begin{align}
>L(x,u) = f(x)+u^{T}(Ax-b)
>\end{align}
>$$

Bài toán đối ngẫu là
>$$
>\begin{equation}
>\max_u -f^{\ast}(-A^T u) - b^T u
>\end{equation}
>$$

trong đó $$u$$ là biến đối ngẫu.

Dual gradient ascent cho bài toán này lặp lại các cập nhật sau ($$k=1,2,3,...$$).
>$$
>\begin{align}
>x^{(k)}&=\underset{x}{\operatorname{argmin}} L(x,u^{(k-1)}) \\\\
>u^{(k)}&= u^{(k-1)} +t_{k}(Ax^{(k)}-b)
>\end{align}
>$$

Ở đây $$t_{k}$$ là kích thước bước ở vòng lặp thứ $$k$$.

Trong phương pháp đối ngẫu này, như ở cập nhật đầu tiên, biến gốc $$x$$ được đặt bằng điểm cực tiểu của hàm Lagrange tại biến đối ngẫu $$u^{(k-1)}$$ từ bước trước, còn biến đối ngẫu $$u$$ được cập nhật bằng gradient ascent, trong đó $$Ax-b$$ là hướng gradient.

Ưu điểm của phương pháp này là khi $$f$$ có thể phân rã thành $$B$$ phần, $$x$$ cũng có thể chia thành $$B$$ khối $$( x =(x_{1}, ...,x_{B})\in \mathbb{R}^{n}, \text{ where }x_{i}\in \mathbb{R}^{n_{i}})$$ và ma trận $$A$$ thành $$B$$ khối ma trận con $$(A = [A_{1}, ..., A_{B}] \text{ where }A_{i} \in \mathbb{R}^{m \times n_{i}})$$, nên việc tính toán dễ song song hóa và mở rộng. Nhược điểm là cần các điều kiện khắt khe để đảm bảo hội tụ: để đảm bảo tính khả thi gốc, $$f$$ phải lồi mạnh. [[20-01-01]]({% multilang_post_url contents/chapter20/21-03-27-20_01_01_Convergence_Analysis %})

## Phương pháp augmented Lagrangian
Phương pháp augmented Lagrangian, còn gọi là phương pháp nhân tử (method of multipliers), thêm một số hạng bổ sung vào bài toán gốc. Khi các vòng lặp tiến triển, các điều kiện KKT dần được thỏa mãn. So với phương pháp đối ngẫu, nó nới lỏng điều kiện cần cho hội tụ ($$f$$ lồi mạnh). Đổi lại, bài toán không thể được phân rã nữa. Bài toán gốc được định nghĩa như sau.

>$$
>\begin{align}
>&\min_{x} &&f(x)+\frac{\rho}{2}||Ax-b||_{2}^{2}&\\\\
>&\text{subject to} &&Ax=b
>\end{align}
>$$

với $$\rho>0$$. Hàm Lagrange của bài toán này là

>$$
>\begin{align}
>L_{\rho}(x,u)=f(x)+u^{T}(Ax-b)+\frac{\rho}{2}||Ax-b||_{2}^{2}.
>\end{align}
>$$

Dual gradient ascent lặp lại như sau ($$k=1,2,3,...$$).
>$$
>\begin{align}
>x^{(k)}&=\underset{x}{\operatorname{argmin}} L_{\rho}(x,u^{(k-1)}) \\\\
>u^{(k)}&= u^{(k-1)} +\rho(Ax^{(k)}-b)
>\end{align}
>$$

Như đã đề cập ở trên, ưu điểm của phương pháp này là điều kiện hội tụ tốt hơn phương pháp đối ngẫu. Nhược điểm là số hạng bình phương được thêm vào làm mất tính phân rã được.

## Phương pháp hướng luân phiên của các nhân tử (ADMM)
ADMM kết hợp ưu điểm của phương pháp đối ngẫu và phương pháp augmented Lagrangian. Giả sử bài toán có dạng sau.

>$$
>\begin{align}
>\min_{x} f(x)+g(z) \qquad \text{subject to  }Ax+Bz=c
>\end{align}
>$$

Với bài toán này ta có thể định nghĩa augmented Lagrangian với $$\rho>0$$.
>$$
>\begin{align}
>&L_{\rho} (x,z,u) = f(x)+g(z)+u^{T}(Ax+Bz-c)+\frac{\rho}{2}||Ax+Bz-c||_{2}^{2}\\\\
>\end{align}
>$$

Sau đó ta cập nhật các biến bằng cách lặp lại như sau.
>$$
>\begin{align}
>&\text{for k = 1,2,3,...}\\\\
>&x^{(k)}=\underset{x}{\operatorname{argmin}} L_{\rho}(x,z^{(k-1)},u^{(k-1)})\\\\
>&z^{(k)}=\underset{z}{\operatorname{argmin}} L_{\rho}(x^{(k)},z,u^{(k-1)})\\\\
>&u^{(k)}=u^{(k-1)}+\rho(Ax^{(k)}+Bz^{(k)}-c)
>\end{align}
>$$

Trong ADMM, các biến gốc $$x, z$$ không được cập nhật đồng thời mà lần lượt từng biến. Khi cập nhật tuần tự, biến còn lại lấy giá trị mới nhất. Nghĩa là khi cập nhật $$z$$ ở vòng lặp $$k$$, ta dùng $$x^{(k)}$$ thay vì giá trị $$x^{(k-1)}$$ của vòng lặp trước, và khi cập nhật $$u$$ ta dùng ngay các biến gốc $$x^{(k)}, z^{(k)}$$ vừa tính ở vòng lặp hiện tại.

## Hội tụ của ADMM
Không cần giả sử $$A$$ và $$B$$ trong ràng buộc có hạng đầy đủ, và chỉ với các giả thiết khiêm tốn trên $$f$$ và $$g$$, ADMM thỏa mãn các điều sau với mọi $$\rho > 0$$.

* Hội tụ phần dư: $$r^{(k)} = A x^{(k)} + B z^{(k)} - c \to 0$$ khi $$k \to \infty$$, tức là các điểm lặp gốc tiến đến tính khả thi.
* Hội tụ hàm mục tiêu: $$f(x^{(k)}) + g(z^{(k)}) \to f^{\star} + g^{\star}$$, trong đó $$f^{\star} + g^{\star}$$ là giá trị mục tiêu gốc tối ưu.
* Hội tụ đối ngẫu: $$u^{(k)} \to u^{\star}$$, trong đó $$u^{\star}$$ là một nghiệm đối ngẫu.

Tốc độ hội tụ nói chung chưa được biết và vẫn đang được nghiên cứu. Các tài liệu tham khảo về hội tụ được nêu trong [phần giới thiệu Chương 21]({% multilang_post_url contents/chapter21/21-03-29-21_00_Alternating_Direction_Method_of_Multipliers %}).

## ADMM dạng có tỉ lệ
ADMM có thể được viết dưới dạng có tỉ lệ bằng cách thay biến đối ngẫu $$u$$ bằng biến có tỉ lệ $$w=u/\rho$$. Khi đó các bước ADMM trở thành
>$$
>\begin{align}
&x^{(k)} = \underset{x}{\operatorname{argmin}} f(x) + \frac{\rho}{2} ||Ax + Bz^{(k-1)} - c + w^{(k-1)} ||_2^2 \\\\
&z^{(k)} = \underset{z}{\operatorname{argmin}} g(z) + \frac{\rho}{2} || Ax^{(k)} + Bz - c + w^{(k-1)} ||_2^2  \\\\
&w^{(k)} = w^{(k-1)} + Ax^{(k)} + Bz^{(k)} - c 
\end{align}
>$$

Ở đây $$w^{(k)}$$ là tổng dồn các phần dư đến vòng lặp $$k$$, cũng có thể viết là
>$$
>\begin{align}
w^{(k)} = w^{(0)} + \sum_{i=1}^k (Ax^{(i)} + Bz^{(i)} - c) 
\end{align}
>$$
