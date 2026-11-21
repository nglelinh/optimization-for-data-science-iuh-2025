---
layout: post
title: '20-01 Các phương pháp dual (sub)gradient'
chapter: '20'
order: 2
owner: Hooncheol Shin
categories:
- chapter20
lang: vi
---

Ngay cả khi không thể tìm được dạng đóng của đối ngẫu (hàm liên hợp), ta vẫn có thể dùng phương pháp subgradient hoặc gradient dựa trên đối ngẫu.

Ví dụ, xét bài toán sau.
>\begin{equation}
\min_x f(x) \text{ subject to } Ax = b
\end{equation}

Bài toán đối ngẫu của bài toán này như sau, trong đó $$f^{\ast}$$ là hàm liên hợp của $$f$$.
>\begin{equation}
\max_u -f^{\ast}(-A^T u) - b^T u
\end{equation}

Định nghĩa $$g(u) = -f^{\ast}(-A^Tu)-b^Tu$$. Khi đó một subgradient của $$g(u)$$ là
>\begin{equation}
\partial g(u) = A \partial f^{\ast}(-A^Tu) - b
\end{equation}

Viết phần tử của $$\partial f^{\ast}(-A^Tu)$$ là $$x$$, biểu thức này có thể được biểu diễn như sau

>\begin{equation}
\partial g(u) = Ax-b \quad \text{where} \quad x \in \arg\min_z f(z) + u^T A z
\end{equation}

## Phương pháp dual subgradient
**Phương pháp dual subgradient** cực đại hóa hàm mục tiêu đối ngẫu. Bắt đầu từ $$u^{(0)}$$, nó lặp lại các bước sau với $$k=1,2,3,\dots$$
> $$
> \begin{alignat}{1}
> x^{(k)} & \in \arg \min_x f(x) + ({u^{(k-1)}})^T A x  \\
> u^{(k)} & = u^{(k-1)} + t_k (A x^{(k)} - b) 
> \end{alignat}
> $$

Ở đây các kích thước bước $$t_k$$ ($$k=1,2,3,\dots$$) được chọn theo cách chuẩn.

#### Trường hợp lồi chặt
Nếu $$f$$ lồi chặt thì $$f^{\ast}$$ khả vi.

Khi đó thuật toán trở thành **dual gradient ascent**, lặp lại các bước sau với $$k=1,2,3,\dots$$
> $$
> \begin{alignat}{1}
> x^{(k)} & = \arg \min_x f(x) + ({u^{(k-1)}})^T A x  \\
> u^{(k)} & = u^{(k-1)} + t_k (A x^{(k)}-b) 
> \end{alignat}
> $$

Khác biệt so với phiên bản trước là $$x^{(k)}$$ là duy nhất. (Lưu ý quan hệ với $$\text{argmin}$$ giờ là "$$=$$" thay vì "$$\in$$".)

Một lần nữa, các kích thước bước $$t_k$$ ($$k=1,2,3,\dots$$) được chọn theo cách chuẩn, và khi tính $$\text{argmin}$$ ta có thể áp dụng proximal gradient hay tăng tốc như bình thường.
