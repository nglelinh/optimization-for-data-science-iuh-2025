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

Năm 1990, Sebastian Ceria tại CMU đã cài đặt thành công phương pháp mặt phẳng cắt kết hợp với thuật toán nhánh và cận, gọi là nhánh và cắt (branch and cut). Từ đó, mặt phẳng cắt trở thành thành phần cốt lõi của các bộ giải tối ưu thương mại.

## Thuật toán nhánh và cắt
Giả sử có bài toán quy hoạch nguyên sau. Ở đây $$f : \mathbb{R}^{n} \to \mathbb{R}$$ lồi, $$C \subseteq \mathbb{R}^{n}$$ là tập lồi và $$J \subseteq \{1, ..., n\}$$.

> $$
> \begin{align}
>           \min_{x} & \quad {f(x)} \\
> \text{subject to } & \quad  x \in C \\
>                    & \quad  x_j \in \mathbb{Z}, \quad j \in J \\
> \end{align}
> $$

### Thuật toán nhánh và cắt
Trong thuật toán, bài toán lồi được ký hiệu là CR (nới lỏng lồi) và quy hoạch nguyên là IP.

1. Giải bài toán nới lỏng lồi (CR) sau.

> $$
> \begin{align}
> \min_{x} & \quad {f(x)} \\\\
> \text{subject to } & \quad  x \in C
> \end{align}
> $$

2. (CR) không khả thi $$\Rightarrow$$ (IP) không khả thi <br>
3. Nghiệm $$x^{\star}$$ của (CR) khả thi cho (IP) $$\Rightarrow$$ $$x^{\star}$$ là nghiệm của (IP) <br>
4. Nếu nghiệm $$x^{\star}$$ của (CR) không khả thi cho (IP) thì chọn một trong hai cách sau <br>
$$\quad$$4.1 Thêm một lát cắt (cut) rồi quay lại bước 1. <br>
$$\quad$$4.2 Phân nhánh (branch) và giải đệ quy các bài toán con. <br>

Thuật toán nhánh và cắt là thuật toán kết hợp nhánh và cận (branch and bound) với phương pháp mặt phẳng cắt; ở bước 4 ta có thể chọn thực hiện branch-and-bound hay thêm lát cắt. 

## Công nghệ quy hoạch nguyên
Các bộ giải hiện đại như Gurobi, CPLEX, FICO chứa các cài đặt rất hiệu quả của các thuật toán như simplex và điểm trong (interior-point). Đặc biệt với tối ưu nguyên hỗn hợp, hầu hết các bộ giải dùng thuật toán nhánh và cắt, tận dụng nhiều lợi thế của nới lỏng lồi và warm start.

So với khoảng 30 năm trước, hiệu năng của quy hoạch nguyên đã cải thiện vượt bậc. Do đó, nhiều bài toán thực tế mà trước đây chưa giải được nay đã được giải bằng quy hoạch nguyên, và với sự cải thiện của sức mạnh tính toán, nó dự kiến sẽ được sử dụng tích cực hơn nữa.

* Tăng tốc nhờ thuật toán 1990-2016: hơn $$500{,}000$$ lần
* Tăng tốc nhờ phần cứng 1990-2016: hơn $$500{,}000$$ lần
* Tổng tốc độ tăng hơn $$250$$ tỷ lần $$= 2{,}5 \cdot 10^{11}$$
