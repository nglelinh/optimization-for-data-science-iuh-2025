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

Xét bài toán sau. Khác biệt so với bài toán trước là ràng buộc là bất đẳng thức.
> $$
> \begin{equation}
> \min_x \sum_{i=1}^B f_i(x_i) \quad \text{subject to} \quad \sum_{i=1}^B A_i x_i \leq b
> \end{equation}
> $$

## Phân rã đối ngẫu (phương pháp subgradient chiếu)
Với bài toán này, biến đối ngẫu phải luôn không âm, tức là $$u \geq 0$$. Do đó, khi tính giá trị tiếp theo của $$u$$, ta chiếu nó lên góc phần tư không âm.

> $$
> \begin{alignat}{1}
> x_i^{(k)} & \in \arg \min_{x_i} f_i(x_i) + (u^{(k-1)})^T A_i x_i, \quad i=1,\dots,B  \\
> u^{(k)}   & = \left( u^{(k-1)} + t_k \left(\sum_{i=1}^B A_i x_i^{(k)} - b \right) \right)_+
> \end{alignat}
> $$

Ở đây $$u_{+}$$ là phần không âm của $$u$$, tức là $$(u_+)_i = \max \left\{0,u_i \right\}, i=1,\dots,m$$.
Các bước này được lặp lại với $$k=1,2,3,\dots$$

#### Diễn giải điều phối giá (price coordination)
Nói chung, các bài toán phân rã đối ngẫu có thể được diễn giải theo quan điểm điều phối giá như sau. (Vandenberghe)
> * Có $$B$$ đơn vị độc lập, và mỗi đơn vị tự quyết định biến quyết định $$x_i$$ của mình.
> * Mỗi ràng buộc biểu diễn giới hạn về một nguồn lực chung của $$B$$ đơn vị, và biến đối ngẫu $$u_j$$ là giá của nguồn lực $$j$$.
> * Các biến đối ngẫu được cập nhật như sau
 \begin{equation}
 u_j^{+} = (u_j - t s_j)_{+}, \quad  j=1,\dots,m
 \end{equation}
>
> $$\quad$$ trong đó $$s=b-\sum_{i=1}^B A_ix_i$$ là độ chùng (slack): \\
> $$\qquad$$ - nếu $$s_j < 0$$, nguồn lực $$j$$ đang bị sử dụng quá mức, nên giá $$u_j$$ được tăng lên; \\
> $$\qquad$$ - nếu $$s_j > 0$$, nguồn lực $$j$$ đang được sử dụng chưa hết, nên giá $$u_j$$ được giảm xuống; \\
> $$\qquad$$ - giá không bao giờ được phép âm.
