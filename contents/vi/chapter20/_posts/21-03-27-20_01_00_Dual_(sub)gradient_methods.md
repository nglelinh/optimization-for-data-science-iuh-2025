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

Ngay cả khi không thể tìm được biểu thức dạng đóng cho hàm liên hợp (và do đó cho hàm mục tiêu đối ngẫu), ta vẫn có thể áp dụng phương pháp gradient hoặc dưới vi phân (subgradient) trực tiếp trên bài toán đối ngẫu.

Xét bài toán tối ưu có ràng buộc đẳng thức:
>\begin{equation}
\min_x f(x) \text{ subject to } Ax = b
\end{equation}

Bài toán đối ngẫu tương ứng — viết qua hàm liên hợp $$f^{\ast}$$ của $$f$$ — có dạng:
>\begin{equation}
\max_u -f^{\ast}(-A^T u) - b^T u
\end{equation}

Đặt $$g(u) = -f^{\ast}(-A^Tu) - b^Tu$$. Khi đó, dưới vi phân của $$g(u)$$ là:
>\begin{equation}
\partial g(u) = A \partial f^{\ast}(-A^Tu) - b
\end{equation}

Lấy một phần tử $$x \in \partial f^{\ast}(-A^Tu)$$, theo tính chất hàm liên hợp ở bài trước, ta có thể biểu diễn phần tử thuộc $$\partial g(u)$$ như sau:

>\begin{equation}
Ax - b \in \partial g(u) \quad \text{với} \quad x \in \arg\min_z f(z) + u^T A z
\end{equation}

## Phương pháp dual subgradient
**Phương pháp dual subgradient** cực đại hóa hàm mục tiêu đối ngẫu $$g(u)$$. Bắt đầu từ điểm khởi tạo $$u^{(0)}$$, thuật toán lặp các bước sau với $$k = 1, 2, 3, \dots$$:
> $$
> \begin{alignat}{1}
> x^{(k)} & \in \arg \min_x f(x) + ({u^{(k-1)}})^T A x  \\
> u^{(k)} & = u^{(k-1)} + t_k (A x^{(k)} - b) 
> \end{alignat}
> $$

trong đó dãy độ dài bước $$t_k$$ ($$k = 1, 2, 3, \dots$$) được chọn theo các quy tắc chuẩn của phương pháp subgradient.

#### Trường hợp $$f$$ lồi chặt
Nếu $$f$$ lồi chặt thì $$f^{\ast}$$ khả vi, và thuật toán trở thành **tăng gradient đối ngẫu (dual gradient ascent)** với các bước lặp ($$k = 1, 2, 3, \dots$$):
> $$
> \begin{alignat}{1}
> x^{(k)} & = \arg \min_x f(x) + ({u^{(k-1)}})^T A x  \\
> u^{(k)} & = u^{(k-1)} + t_k (A x^{(k)}-b) 
> \end{alignat}
> $$

Khác biệt so với dạng tổng quát là nghiệm $$x^{(k)}$$ là duy nhất (dùng ký hiệu "$$=$$" thay cho "$$\in$$"). Khi giải bài toán con tìm $$x^{(k)}$$, ta có thể áp dụng các kỹ thuật tăng tốc hoặc proximal gradient như thông thường.
