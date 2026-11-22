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

Cho đến nay, ta luôn giả sử bước định tâm đầu tiên (tại $$t = t^{(0)}$$) đã có sẵn một điểm xuất phát khả thi chặt để tìm $$x^{(0)} = x^*(t^{(0)})$$.

Một điểm $$x$$ được gọi là khả thi chặt nếu thỏa mãn đồng thời:
>$$ h_i(x) \lt 0, \quad i = 1, \cdots, m, \quad Ax = b$$

## Cực tiểu hóa mức bất khả thi lớn nhất
Để tìm một điểm $$x$$ khả thi chặt, ta giải bài toán phụ (Phase I) sau:

>
$$\begin{align}
&\min_{x, s} \        && s \\
&\text{subject to } \ && h_i(x) \le s,& i = 1, \cdots, m \\
                      &&& Ax = b \\
\end{align}$$

Mục tiêu của bài toán này là tìm nghiệm có $$s < 0$$. Cách tiếp cận này được gọi là **phương pháp tìm điểm khả thi (feasibility method)**.

Vì bài toán phụ này dễ dàng tìm được điểm xuất phát khả thi chặt (chỉ cần chọn $$x$$ thỏa $$Ax = b$$ rồi lấy $$s > \max_i h_i(x)$$), ta có thể giải trực tiếp nó bằng phương pháp chắn.

Khi giải bài toán tìm điểm khả thi, không cần đạt độ chính xác cao; chỉ cần dừng ngay khi tìm được một cặp $$(x, s)$$ khả thi với $$s < 0$$.

## Cực tiểu hóa mức bất khả thi cho từng ràng buộc
Một biến thể khác là gán biến phụ $$s_i$$ riêng cho từng ràng buộc bất đẳng thức ($$i = 1, \cdots, m$$) thay vì dùng chung một biến $$s$$:
>
$$\begin{align}
&\min_{x, s} \        && 1^Ts \\
&\text{subject to } \ && h_i(x) \le s_i,& i = 1, \cdots, m \\
                      &&& Ax = b \\
\end{align}$$

Ưu điểm của cách phát biểu này là dựa vào từng thành phần của nghiệm $$s$$, ta biết cụ thể ràng buộc nào đang bị vi phạm: nếu có phần tử $$s_i \ge 0$$ thì ràng buộc bất đẳng thức thứ $$i$$ không được thỏa mãn chặt.
