---
layout: post
title: '08-01-08 Phương pháp Subgradient có Chiếu'
chapter: '08'
order: 10
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

Ý tưởng phép chiếu ở ví dụ trước dẫn đến **phương pháp subgradient có chiếu (projected subgradient method)**, dùng để giải các bài toán tối ưu lồi có ràng buộc.

Ký hiệu miền ràng buộc là tập lồi đóng $$C$$, bài toán tối ưu có dạng:

>
$$ \begin{align}
\min_x \text{ }f(x) \quad \text{với điều kiện } x \in C
\end{align} $$

Phương pháp subgradient có chiếu thực hiện tương tự phương pháp subgradient tiêu chuẩn, nhưng sau mỗi bước cập nhật, điểm mới được chiếu trở lại tập ràng buộc $$C$$:

>
$$ \begin{align}
x^{(k)} = P_c(x^{(k-1)} - t_k \cdot g^{(k-1)}), \quad k = 1,2,3,...
\end{align} $$

Nếu phép chiếu $$P_C$$ thực hiện được chính xác, phương pháp này có cùng các tính chất hội tụ và tốc độ hội tụ như phương pháp subgradient không ràng buộc.

Tuy nhiên, cần lưu ý rằng ngay cả khi $$C$$ là một tập lồi có mô tả đơn giản, nếu phép chiếu $$P_C$$ khó tính toán thì thuật toán tổng thể vẫn tốn kém. Một số tập $$C$$ có phép chiếu tương đối dễ tính gồm:

- Tập ảnh affine: {$$Ax + b : x \in \mathbb{R}^{n}$$}
- Tập nghiệm của hệ phương trình tuyến tính: {$$x: Ax=b$$}
- Góc phần tư không âm (nonnegative orthant): $$\mathbb{R}_+^{n} = $$ {$$x: x\ge 0$$}
- Một số quả cầu chuẩn: {$$x: \lVert x \rVert _p \le 1 $$} với $$p=1,2,\infty$$
- Một số đa diện đơn giản và hình nón đơn giản
