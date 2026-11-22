---
layout: post
title: '20-03 Augmented Lagrangian'
chapter: '20'
order: 7
owner: Hooncheol Shin
categories:
- chapter20
lang: vi
---

Nhược điểm lớn của phương pháp tăng đối ngẫu (dual ascent) là đòi hỏi điều kiện mạnh — chẳng hạn $$f$$ phải lồi mạnh — để đảm bảo hội tụ. **Phương pháp hàm Lagrange tăng cường (Augmented Lagrangian)**, còn gọi là **phương pháp nhân tử (method of multipliers)**, khắc phục hạn chế này.

Ta viết lại bài toán gốc bằng cách cộng thêm một số hạng phạt bậc hai vào hàm mục tiêu:
>\begin{equation}
\min_x f(x) + \frac{\rho}{2} \lVert Ax - b \rVert _2^2 \quad \text{ subject to } \quad Ax = b
\end{equation}

trong đó $$\rho > 0$$. Nếu $$A$$ có hạng cột đầy đủ, hàm mục tiêu mới trở nên lồi mạnh. Bài toán này hoàn toàn tương đương với bài toán ban đầu vì số hạng phạt $$\frac{\rho}{2}\lVert Ax - b \rVert_2^2$$ bằng $$0$$ tại mọi điểm khả thi $$Ax = b$$.

## Phương pháp Augmented Lagrangian
Áp dụng **dual gradient ascent** cho bài toán đã biến đổi, ta thu được các bước lặp với $$k = 1, 2, 3, \dots$$:
> $$
> \begin{alignat}{1}
> x^{(k)} & \in \arg\min_x f(x) + (u^{(k-1)})^T A x + \frac{\rho}{2} \lVert Ax - b \rVert_2^2  \\
> u^{(k)} & = u^{(k-1)} + \rho (A x^{(k)} - b)
> \end{alignat}
> $$

Ở đây, tham số phạt $$\rho$$ đồng thời được chọn làm độ dài bước cập nhật đối ngẫu ($$t_k = \rho$$).

#### Vì sao chọn độ dài bước $$t_k = \rho$$?

Vì $$x^{(k)}$$ là nghiệm cực tiểu của $$f(x) + (u^{(k-1)})^T Ax + \frac{\rho}{2} \lVert Ax - b\rVert _2^2$$, điều kiện tối ưu bậc nhất cho ta:

> $$
> \begin{alignat}{1}
> 0 & \in \partial f(x^{(k)}) + A^T \left( u^{(k-1)} + \rho (A x^{(k)} -b) \right)  \\
>   & = \partial f(x^{(k)}) + A^T u^{(k)}
> \end{alignat}
> $$

Như vậy, với quy tắc cập nhật $$u^{(k)} = u^{(k-1)} + \rho (A x^{(k)} - b)$$, điểm $$x^{(k)}$$ luôn thỏa mãn điều kiện dừng đối ngẫu $$0 \in \partial f(x^{(k)}) + A^T u^{(k)}$$ ở mọi vòng lặp. Dưới các giả thiết rất nhẹ, phần dư $$Ax^{(k)} - b$$ tiến về $$0$$, các điều kiện KKT dần được thỏa mãn và $$(x^{(k)}, u^{(k)})$$ hội tụ về nghiệm tối ưu.

Ưu điểm của **phương pháp augmented Lagrangian** là tính hội tụ ổn định và vững chắc hơn nhiều so với dual ascent; tuy nhiên, nhược điểm là số hạng bậc hai $$\frac{\rho}{2}\lVert Ax - b \rVert_2^2$$ làm các khối biến liên kết với nhau, phá vỡ tính khả phân (decomposability) của bài toán.
