---
layout: post
title: 13-06 Tinh tế đối ngẫu & Đối ngẫu kép
chapter: '13'
order: 10
owner: Wontak Ryu
categories:
- chapter13
lang: vi
---

## Tinh tế đối ngẫu
• Đôi khi chúng ta có thể biến đổi các bài toán đối ngẫu thành các bài toán tương đương và vẫn gọi chúng là bài toán đối ngẫu. Ngoài ra, trong đối ngẫu mạnh, chúng ta có thể sử dụng nghiệm của các bài toán đối ngẫu đã biến đổi để phân tích hoặc tính toán các đặc trưng của nghiệm nguyên thủy.

#### [Lưu ý]
Giá trị tối ưu của một bài toán đối ngẫu đã biến đổi không nhất thiết là giá trị tối ưu của nguyên thủy.


• Một cách phổ biến để suy dẫn các bài toán đối ngẫu cho các bài toán không ràng buộc là đầu tiên biến đổi nguyên thủy bằng cách thêm các biến giả và ràng buộc đẳng thức.

Nói chung, cách thực hiện điều này là mơ hồ. Các lựa chọn khác nhau có thể dẫn đến các bài toán đối ngẫu khác nhau.


## Đối ngẫu kép
Hãy xem xét một bài toán tối thiểu hóa tổng quát với ràng buộc tuyến tính:

> $$ \min_x f(x) \text{ với điều kiện } Ax ≤ b, Cx = d$$

Lagrangian như sau:
> $$L(x,u,v) = f(x) + (A^Tu + C^Tv)^Tx−b^Tu−d^Tv$$

Do đó, bài toán đối ngẫu như sau:

> $$ \max_{u,v} −f^∗(−A^Tu−C^Tv)−b^Tu−d^Tv \text{ với điều kiện } u ≥ 0 $$

#### Nhắc lại tính chất

Nếu $$f$$ đóng và lồi, chúng ta đã giải thích trước đó rằng đối ngẫu của đối ngẫu là nguyên thủy trong trường hợp này ($$f^{∗∗} = f$$).

Trên thực tế, mối liên hệ (giữa đối ngẫu và liên hợp đối ngẫu) đi sâu hơn nhiều ngoài các ràng buộc tuyến tính.
Xem xét điều sau:

> $$ 
>\begin{align}
> & \min_x && f(x) \\
> &\text{ với điều kiện } && h_i(x) ≤ 0, i = 1,...m \\
> &&&l_j(x) = 0, j = 1,...r
>\end{align}$$

Nếu $$f$$ và $$h_1,...h_m$$ đóng và lồi, và $$l_1,...l_r$$ là affine, thì đối ngẫu của đối ngẫu là nguyên thủy.

Điều này được cung cấp như một bài toán tối thiểu hóa từ góc độ của các hàm hai biến.

(để biết thêm, đọc Chương 29 và 30 của Rockafellar)
