---
layout: post
title: '15-07 Các phương pháp tìm điểm khả thi'
chapter: "15"
order: 13
categories:
- chapter16
owner: "Minjoo Lee"
lang: vi
---

Cho đến nay, chúng ta đã ngầm giả sử rằng bước centering đầu tiên ($$t = t^{(0)}$$) bắt đầu từ một điểm khả thi chặt để tính $$x^{(0)} = x^*$$.

Điều này có nghĩa là $$x$$ là một điểm khả thi chặt thỏa mãn các điều kiện sau:
>$$ h_i(x) \lt 0, \quad i = 1, \cdots, m, \quad Ax = b$$

## Mức bất khả thi lớn nhất
Làm sao để tìm $$x$$? Ta có thể giải bài toán sau để tìm nó.

>
$$\begin{align}
&\min_{x, s} \        && s \\
&\text{subject to } \ && h_i(x) \le s,& i = 1, \cdots, m \\
                      &&& Ax = b \\
\end{align}$$

Mục tiêu là làm cho nghiệm $$s$$ âm. Bài toán này được gọi là **phương pháp khả thi (feasibility method)**.

Tìm một điểm xuất phát khả thi chặt cho bài toán này thì dễ, nên nó cũng có thể được giải bằng phương pháp chắn. Nghĩa là, bạn có thể thêm các biến bù (slack) vào ràng buộc bất đẳng thức $$h_i(x) \le s$$ và chuyển nó thành ràng buộc đẳng thức để giải.

Khi giải bài toán này không cần độ chính xác cao; chỉ cần tìm được một $$(x,s)$$ khả thi với $$s < 0$$.

## Mức bất khả thi cho từng ràng buộc bất đẳng thức
Bạn cũng có thể định nghĩa và giải bài toán như sau. Phương pháp trước tìm mức bất khả thi lớn nhất cho tất cả các bất đẳng thức, còn bài toán này tìm biến bất khả thi $$s_i, i = 1, \cdots, m$$ cho từng bất đẳng thức.
>
$$\begin{align}
&\min_{x, s} \        && 1^Ts \\
&\text{subject to } \ && h_i(x) \le s_i,& i = 1, \cdots, m \\
                      &&& Ax = b \\
\end{align}$$

Ưu điểm của phương pháp này là bằng cách nhìn vào nghiệm $$s$$, ta biết được bài toán có khả thi hay không. Nghĩa là, nếu có phần tử nào của $$s$$ lớn hơn hoặc bằng 0 thì ràng buộc tương ứng không được thỏa mãn.
