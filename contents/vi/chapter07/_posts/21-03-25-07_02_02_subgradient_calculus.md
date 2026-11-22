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

### Nhân với hằng số dương (Tỷ lệ)

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

Ở đây, tổng của hai tập hợp được định nghĩa theo nghĩa tổng Minkowski: $$A+B= \{a+b:a\in A, b \in B\}$$.

### Hợp thành với ánh xạ affine

>
$$
\eqalign{
	\text{nếu } & g(x)=f(Ax+b), \\
	\text{thì } & \partial g(x) = A^T \partial f(Ax+b)
}
$$

### Giá trị lớn nhất hữu hạn theo điểm

>
$$
\eqalign{
	\text{nếu } & f(x)=\max_{i=1,\dots,m} f_i(x), \\
	\text{thì } & \partial f(x) = \text{conv}\left(\bigcup_{i:f_i(x)=f(x)} \partial f_i(x)\right)
}
$$

Nói cách khác, $$\partial f(x)$$ là bao lồi của hợp các vi phân dưới của những hàm thành phần đạt giá trị lớn nhất $$f(x)$$ tại điểm $$x$$.

### Giá trị lớn nhất tổng quát theo điểm

>$$
\eqalign{
	\text{nếu } & f(x) = \max_{s \in S} f_s(x),\\ 
	\text{thì } & \partial f(x) \supseteq cl \left \{ \text{conv} \left(\bigcup_{s:f_s(x)=f(x)} \partial f_s(x)\right) \right\}
}
$$

Vì $$S$$ có thể là một tập vô hạn, hợp của vô số tập hợp chưa chắc đã là tập đóng. Do đó, cần lấy bao đóng để đảm bảo tập thu được là tập đóng giống như vi phân dưới.

Nếu tập $$S$$ compact (đóng và bị chặn) và các hàm $$f_s$$ liên tục theo $$s$$, thì dấu bao hàm trở thành đẳng thức.

Ví dụ, xét chuẩn $$p$$ của vector $$x$$ viết dưới dạng giá trị lớn nhất theo điểm:
>
\begin{equation}
f(x) =  \vert  \vert x \vert  \vert \_p = \max_{ \vert  \vert z \vert  \vert _q \leq 1} z^Tx, \qquad 1/p + 1/q =1
\end{equation}

Đặt $$f_z(x)=z^Tx$$. Khi đó, mọi $$z^*$$ thỏa mãn $$f(x)=f_{z^*}(x)$$ đều thuộc tập $$\arg\max_{ \vert  \vert z \vert  \vert _q \leq 1} z^Tx$$. Vì $$\partial f_{z^*}(x)=\{z^*\}$$, hợp $$\bigcup \partial f_{z^*}(x)$$ chính là tập $$\arg\max_{ \vert  \vert z \vert  \vert _q \leq 1} z^Tx$$.

Do $$S=\{z: \vert  \vert z \vert  \vert _q \leq 1\}$$ là tập compact và $$f_z(x)=z^Tx$$ tuyến tính, theo quy tắc giá trị lớn nhất tổng quát theo điểm, việc lấy bao lồi rồi lấy bao đóng của $$\bigcup \partial f_{z^*}(x)$$ không bổ sung thêm phần tử nào mới. Do đó, vi phân dưới của $$f(x)$$ là:

>
\begin{equation}
\partial f(x) = \arg\max_{ \vert  \vert z \vert  \vert _q \leq 1} z^T x
\end{equation}
