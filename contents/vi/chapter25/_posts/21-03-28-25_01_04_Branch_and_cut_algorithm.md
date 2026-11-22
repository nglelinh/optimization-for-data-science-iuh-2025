---
layout: post
title: '25-01-04 Thuật toán nhánh và cắt (Branch and cut)'
chapter: '25'
order: 6
owner: YoungJae Choung
categories:
- chapter25
lang: vi
---

Năm 1990, Sebastian Ceria tại Đại học Carnegie Mellon đã triển khai thành công sự kết hợp giữa phương pháp mặt phẳng cắt và thuật toán nhánh và cận, tạo nên thuật toán **nhánh và cắt (branch and cut)**. Kể từ đó, cách tiếp cận này trở thành nền tảng cốt lõi của các bộ giải tối ưu thương mại hiện đại.

## Thuật toán nhánh và cắt

Xét bài toán quy hoạch nguyên (IP), trong đó $$f : \mathbb{R}^{n} \to \mathbb{R}$$ là hàm lồi, $$C \subseteq \mathbb{R}^{n}$$ là tập lồi và $$J \subseteq \{1, \dots, n\}$$:

> $$
> \begin{align}
>           \min_{x} & \quad {f(x)} \\
> \text{subject to } & \quad  x \in C \\
>                    & \quad  x_j \in \mathbb{Z}, \quad j \in J
> \end{align}
> $$

### Các bước thực hiện

Ký hiệu bài toán nới lỏng lồi là (CR) và quy hoạch nguyên là (IP):

1. Giải bài toán nới lỏng lồi (CR):

> $$
> \begin{align}
> \min_{x} & \quad {f(x)} \\\\
> \text{subject to } & \quad  x \in C
> \end{align}
> $$

2. Nếu (CR) vô nghiệm $$\Rightarrow$$ (IP) vô nghiệm (dừng). <br>
3. Nếu nghiệm $$x^{\star}$$ của (CR) khả thi cho (IP) $$\Rightarrow$$ $$x^{\star}$$ là nghiệm tối ưu của (IP) (dừng). <br>
4. Nếu $$x^{\star}$$ chưa thỏa mãn ràng buộc nguyên, chọn một trong hai thao tác: <br>
$$\quad$$ 4.1 Thêm một hoặc nhiều mặt phẳng cắt (cut) rồi quay lại bước 1. <br>
$$\quad$$ 4.2 Phân nhánh (branch) thành các bài toán con và giải đệ quy.

Như vậy, thuật toán nhánh và cắt tích hợp mặt phẳng cắt trực tiếp vào bên trong cây nhánh và cận: tại mỗi nút, bộ giải có thể siết chặt bài toán nới lỏng bằng lát cắt trước khi quyết định phân nhánh.

## Tiến bộ của công nghệ giải quy hoạch nguyên

Các bộ giải hiện đại như Gurobi, CPLEX và FICO Xpress sở hữu những cài đặt rất hiệu quả của phương pháp đơn hình (simplex) và điểm trong (interior-point). Riêng với quy hoạch nguyên hỗn hợp, hầu hết các bộ giải đều dùng kiến trúc nhánh và cắt, khai thác mạnh nới lỏng lồi và khởi động nóng (warm start).

Trong khoảng 30 năm qua, tốc độ giải quy hoạch nguyên đã tăng lên rất lớn, giúp nhiều bài toán thực tế từng không thể giải nay giải được trong thời gian ngắn:

* Tăng tốc nhờ cải tiến thuật toán (1990–2016): hơn $$500{,}000$$ lần.
* Tăng tốc nhờ cải tiến phần cứng (1990–2016): hơn $$500{,}000$$ lần.
* Tổng mức tăng tốc: hơn $$250$$ tỷ lần ($$2{,}5 \cdot 10^{11}$$).
