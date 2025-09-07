---
layout: post
title: 07-02-02 Phép tính gradient dưới
chapter: '07'
order: 5
owner: Kyeongmin Woo
categories:
- chapter07
lang: vi
---

Các quy tắc cơ bản sau đây áp dụng cho vi phân dưới của các hàm lồi:

### Tỷ lệ

>
$$
\eqalign{
	\text{nếu } & a>0, \\
	\text{thì } &\partial (af) = a\cdot \partial f
}
$$

### Phép cộng

>
$$\partial(f_1 + f_2) = \partial f_1 + \partial f_2$$

Ở đây, tổng của hai tập hợp $$A+B= \{a+b:a\in A, b \in B\}$$ được định nghĩa là tập hợp tất cả các tổng có thể.

### Hợp thành affine

>
$$
\eqalign{
	\text{nếu } & g(x)=f(Ax+b), \\
	\text{thì } & \partial g(x) = A^T \partial f(Ax+b)
}
$$

### Maximum điểm hữu hạn

>
$$
\eqalign{
	\text{nếu } & f(x)=\max_{i=1,\dots,m} f_i(x), \\
	\text{thì } & \partial f(x) = \text{conv}\left(\bigcup_{i:f_i(x)=f(x)} \partial f_i(x)\right)
}
$$

Tức là, $$\partial f(x)$$ được định nghĩa là bao lồi của hợp các vi phân dưới của các hàm đạt giá trị $$f(x)$$ tại $$x$$.

### Maximum điểm tổng quát

>$$
\eqalign{
	\text{nếu } & f(x) = \max_{s \in S} f_s(x),\\ 
	\text{thì } & \partial f(x) \supseteq cl \left \{ \text{conv} \left(\bigcup_{s:f_s(x)=f(x)} \partial f_s(x)\right) \right\}
}
$$

Ở đây, $$S$$ có thể là một tập vô hạn, nên hợp của vô số tập hợp có thể không đóng. Do đó, chúng ta lấy bao đóng để đảm bảo vi phân dưới là một tập đóng.

Mặt khác, nếu tập hợp $$S$$ compact (đóng và bị chặn), và các hàm $$f_s$$ liên tục theo $$s$$, thì quan hệ đẳng thức được thiết lập.

Ví dụ, đối với hàm p-norm $$f(x)$$ sau đây:
>
\begin{equation}
f(x) =  \vert  \vert x \vert  \vert \_p = \max_{ \vert  \vert z \vert  \vert _q \leq 1} z^Tx, \qquad 1/p + 1/q =1
\end{equation}

Nếu đặt $$f_z(x)=z^Tx$$, thì $$z^*$$ sao cho $$f(x)=f_{z^*}(x)$$ thuộc $$\arg\max_{ \vert  \vert z \vert  \vert _q \leq 1} z^Tx$$.

Mặt khác, vì $$\partial f_{z^*}(x)=z^*$$, nên $$\bigcup \partial f_{z^*}(x)$$ là hợp của tất cả $$z^*$$, do đó $$\partial f(x) = \arg\max_{ \vert  \vert z \vert  \vert _q \leq 1} z^Tx$$.

Ở đây, $$S={z: \vert  \vert z \vert  \vert _q \leq 1}$$ là tập compact, và $$f_z(x)=z^Tx$$ là tuyến tính, nên

theo quy tắc maximum điểm tổng quát, việc lấy bao lồi rồi bao đóng của $$\bigcup \partial f_{z^*}(x)$$ không thêm phần tử nào mới.

Do đó, gradient dưới của hàm $$f(x)$$ như sau:

>
\begin{equation}
\partial f(x) = \arg\max_{ \vert  \vert z \vert  \vert _q \leq 1} z^T x
\end{equation}
