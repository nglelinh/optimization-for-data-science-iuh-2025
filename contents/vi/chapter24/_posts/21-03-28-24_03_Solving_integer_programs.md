---
layout: post
title: '24-03 Giải quy hoạch nguyên'
chapter: '24'
order: 4
owner: YoungJae Choung
categories:
- chapter24
lang: vi
---

Sau khi biến đổi công thức toán học của quy hoạch nguyên, cần các kỹ thuật như nới lỏng (relaxation) để giải bài toán. Hãy xem các ràng buộc xuất hiện trong quy hoạch nguyên và những cách tiếp cận để giải quyết bài toán.

## Độ khó của quy hoạch nguyên
Giải các bài toán quy hoạch nguyên khó hơn nhiều so với giải các bài toán tối ưu lồi. Quy hoạch nguyên tổng quát là [NP-khó](https://en.wikipedia.org/wiki/NP-hardness), nên nói chung không có thuật toán thời gian đa thức nào được biết. Trong trường hợp này, bằng cách bỏ các ràng buộc nguyên và thực hiện nới lỏng lồi (convex relaxation), ta có thể thu được một cận dưới tiến gần đến giá trị tối ưu.<br><br>
Khi giải bài toán bằng nới lỏng lồi, có thể xảy ra các hạn chế sau:


 * Việc tìm một nghiệm nguyên khả thi có thể trở nên khó khăn.
 * Nghiệm tối ưu thu được dưới điều kiện nới lỏng có thể ở xa nghiệm tối ưu của quy hoạch nguyên.
 * Giá trị sau khi xấp xỉ (làm tròn) có thể khác giá trị tối ưu.


## Khung thuật toán để giải quy hoạch nguyên
Khi $$X$$ lồi và bao gồm các ràng buộc nguyên, quy hoạch nguyên có dạng:

> $$ z : = \min_{x \in X} f(x) $$

Không như tối ưu lồi, không có "điều kiện tối ưu" trực tiếp nào chứng minh một điểm khả thi $$x^{\star} \in X$$ là tối ưu. Thay vào đó, ta có thể dùng phương pháp tìm xấp xỉ của giá trị tối ưu bằng cách tìm cận dưới $$ \underline{z} \leq z$$ và cận trên $$ \bar{z} \geq z$$ trong khi làm cho $$\underline{z} = \bar{z}$$ tiến lại gần nhau.

### Khung thuật toán
Quan sát dãy giảm của các cận trên,
> $$\bar{z_1} \geq \bar{z_2} \geq \dotsc \bar{z_s} \geq z$$

Quan sát dãy tăng của các cận dưới,
> $$\underline{z_1} \leq \underline{z_2} \leq \dotsc \underline{z_t} \leq z $$

Với mọi $$\epsilon > 0$$, giá trị của $$z$$ được xác định trong khoảng thỏa mãn $$\bar{z_s} - \underline{z_t} \leq \epsilon$$.

### Cận gốc (Primal bounds)
Theo công thức của $$z$$ ở trên, với mọi $$x \in X$$ khả thi, $$f(x) \geq z$$ luôn đúng, và khi đó $$f(x)$$ là một cận trên. Tuy nhiên, vì không phải lúc nào cũng tìm được $$x$$ khả thi, nếu giá trị $$x$$ thuộc tập tương ứng thì bài toán có thể giải dễ dàng, nhưng điều này không phải lúc nào cũng xảy ra.


### Cận đối ngẫu (Dual bounds)
Thường còn được gọi là cận dưới, giá trị của chúng được tìm qua nới lỏng. Giải thích chi tiết được bổ sung ở phần tiếp theo.
