---
layout: post
title: '20-02-02 Phân rã đối ngẫu với ràng buộc bất đẳng thức'
chapter: '20'
order: 6
owner: Hooncheol Shin
categories:
- chapter20
lang: vi
---

Xét bài toán tương tự phần trước nhưng thay ràng buộc đẳng thức bằng ràng buộc bất đẳng thức tuyến tính:
> $$
> \begin{equation}
> \min_x \sum_{i=1}^B f_i(x_i) \quad \text{subject to} \quad \sum_{i=1}^B A_i x_i \leq b
> \end{equation}
> $$

## Phân rã đối ngẫu (phương pháp subgradient chiếu)
Do ràng buộc có dạng bất đẳng thức, biến đối ngẫu phải thỏa mãn điều kiện không âm $$u \geq 0$$. Vì vậy, sau bước cập nhật $$u$$, ta chiếu kết quả lên góc phần tư không âm:

> $$
> \begin{alignat}{1}
> x_i^{(k)} & \in \arg \min_{x_i} f_i(x_i) + (u^{(k-1)})^T A_i x_i, \quad i=1,\dots,B  \\
> u^{(k)}   & = \left( u^{(k-1)} + t_k \left(\sum_{i=1}^B A_i x_i^{(k)} - b \right) \right)_+
> \end{alignat}
> $$

trong đó $$u_{+}$$ ký hiệu phép lấy phần không âm theo từng thành phần: $$(u_+)_i = \max \left\{0, u_i \right\}$$ ($$i = 1, \dots, m$$). Hai bước trên được lặp lại với $$k = 1, 2, 3, \dots$$

#### Diễn giải theo cơ chế điều phối giá (price coordination)
Theo Vandenberghe, thuật toán phân rã đối ngẫu có cách hiểu kinh tế trực quan như sau:
> * Hệ thống gồm $$B$$ đơn vị độc lập, mỗi đơn vị tự chọn phương án $$x_i$$ của mình.
> * Mỗi ràng buộc biểu diễn giới hạn của một nguồn lực dùng chung giữa $$B$$ đơn vị, còn biến đối ngẫu $$u_j$$ đóng vai trò đơn giá của nguồn lực thứ $$j$$.
> * Các mức giá được cập nhật theo công thức:
 \begin{equation}
 u_j^{+} = (u_j - t s_j)_{+}, \quad  j=1,\dots,m
 \end{equation}
>
> $$\quad$$ trong đó $$s = b - \sum_{i=1}^B A_ix_i$$ là lượng dư (slack) của nguồn lực: \\
> $$\qquad$$ - nếu $$s_j < 0$$ (nguồn lực $$j$$ bị sử dụng vượt mức cho phép), giá $$u_j$$ được tăng lên; \\
> $$\qquad$$ - nếu $$s_j > 0$$ (nguồn lực $$j$$ vẫn còn dư), giá $$u_j$$ được giảm xuống; \\
> $$\qquad$$ - mức giá luôn được giữ không âm ($$u_j \ge 0$$).
