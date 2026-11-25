---
layout: post
title: '15-03-02 Khoảng cách dưới tối ưu (Suboptimality gap)'
chapter: '15'
order: 9
owner: Minjoo Lee
categories:
- chapter15
lang: vi
---

Trong hầu hết các thuật toán tối ưu, việc ước lượng xem mình còn cách giá trị tối ưu $$f^*$$ bao xa đòi hỏi phải biết các hằng số khó đo như hằng số lồi mạnh $$m$$ hay bán kính tập khả thi $$R$$. Thế nhưng phương pháp chắn lại sở hữu một công thức chặn sai số gọn gàng đến mức gần như không tưởng:

$$f(x^*(t)) - f(x^*) \le \frac{m}{t}.$$

Hãy dừng lại vài giây để chiêm ngưỡng sự kỳ diệu của công thức này: nó **không phụ thuộc** vào hàm mục tiêu $$f$$ cong hay phẳng, **không phụ thuộc** vào số chiều $$n$$, và chỉ phụ thuộc vào đúng hai con số ta biết rõ mười mươi là **số lượng ràng buộc bất đẳng thức $$m$$** và **tham số chắn $$t$$** do chính tay ta chọn!

## Kiến thức cần nhớ: Cách chứng minh và ứng dụng công thức khoảng cách dưới tối ưu $$m/t$$

- **Chứng minh bằng hàm đối ngẫu Lagrange:** Vì $$x^*(t)$$ cực tiểu hóa hàm Lagrange $$L(x, u^*(t), v^*(t))$$ theo $$x$$ (do điều kiện dừng KKT nhiễu và tính lồi), ta có:
  $$g(u^*(t), v^*(t)) = L(x^*(t), u^*(t), v^*(t)) = f(x^*(t)) + \sum_{i=1}^m u_i^*(t) h_i(x^*(t)) + v^*(t)^T(Ax^*(t) - b).$$
- **Sự rút gọn kỳ diệu nhờ bù yếu nhiễu:** Vì $$Ax^*(t) = b$$ và mỗi số hạng $$u_i^*(t) h_i(x^*(t)) = -\frac{1}{t}$$, tổng $$m$$ số hạng đó bằng đúng $$-\frac{m}{t}$$! Do đó:
  $$g(u^*(t), v^*(t)) = f(x^*(t)) - \frac{m}{t}.$$
- **Suy ra chặn trên sai số tức thì:** Theo tính đối ngẫu yếu $$g(u^*(t), v^*(t)) \le f(x^*)$$, ta lập tức nhận được $$f(x^*(t)) - f(x^*) \le f(x^*(t)) - g(u^*(t), v^*(t)) = \frac{m}{t}$$!
- **Tiêu chí dừng chuẩn vàng:** Muốn đạt độ chính xác $$\epsilon$$, thuật toán chỉ cần tăng $$t$$ cho đến khi $$\frac{m}{t} \le \epsilon$$ (tức $$t \ge \frac{m}{\epsilon}$$) là có chứng chỉ toán học tuyệt đối để dừng!

### Giải thích: Thiết kế ngưỡng dừng $$t$$ và kiểm chứng $$m/t$$ trên bài toán 3 ràng buộc

Xét bài toán tối ưu lồi có $$m = 3$$ ràng buộc bất đẳng thức:
$$\min_{x \in \mathbb{R}^2} x_1 + 2x_2 \qquad \text{với } x_1 \ge 0, \; x_2 \ge 0, \; x_1 + x_2 \ge 1.$$
(Tức $$h_1 = -x_1 \le 0, \; h_2 = -x_2 \le 0, \; h_3 = 1 - x_1 - x_2 \le 0$$; nghiệm tối ưu là $$x^* = (1, 0)^T$$ với $$f^* = 1$$).

1. **Chọn ngưỡng dừng cho sai số mục tiêu $$\epsilon = 10^{-4}$$:**
   Vì có $$m = 3$$ ràng buộc bất đẳng thức, ta chỉ cần chạy phương pháp chắn đến khi:
   $$\frac{m}{t} \le 10^{-4} \iff t \ge \frac{3}{10^{-4}} = 30{,}000.$$
2. **Kiểm chứng trực tiếp đẳng thức $$f(x^*(t)) - g(u^*(t)) = m/t$$ tại $$t = 10$$:**
   Giả sử tại $$t = 10$$, điểm đường trung tâm $$x^*(10)$$ có $$h_1, h_2, h_3 < 0$$ và $$u_i^*(10) = -\frac{1}{10 h_i(x^*(10))}$$.
   Khi thay vào hàm Lagrange gốc:
   $$g(u^*(10)) = f(x^*(10)) + \underbrace{u_1^* h_1}_{-0.1} + \underbrace{u_2^* h_2}_{-0.1} + \underbrace{u_3^* h_3}_{-0.1} = f(x^*(10)) - 0.3.$$
   Vậy khoảng cách đối ngẫu luôn chính xác bằng $$0.3 = \frac{3}{10}$$, đảm bảo chắc chắn $$f(x^*(10)) - 1 \le 0.3$$!

---

Khoảng cách dưới tối ưu giữa giá trị $$f(x^*(t))$$ tại điểm đường trung tâm và giá trị tối ưu $$f(x^*)$$ của bài toán gốc là bao nhiêu?

Trước hết, từ tính lồi của $$f$$ và $$h_i$$ (đồ thị hàm lồi luôn nằm trên tiếp tuyến khai triển Taylor bậc nhất của nó), ta có hai bất đẳng thức:

>$$
>\begin{align}
>f(x^*) &\ge f(x^*(t)) + \nabla f(x^*(t))^T (x^* - x^*(t)) \\\\
>h_i(x^*) &\ge h_i(x^*(t)) + \nabla h_i(x^*(t))^T (x^* - x^*(t)), \quad i = 1, \cdots, m
>\end{align}
>$$

Từ bất đẳng thức thứ hai, chuyển vế ta thu được:

$$
h_i(x^*(t)) - h_i(x^*) \le \nabla h_i(x^*(t))^T (x^*(t) - x^*), \quad i = 1, \cdots, m
$$

## Dẫn xuất khoảng cách dưới tối ưu

Kết hợp hai bất đẳng thức trên với điều kiện KKT nhiễu ở mục trước (với $$u_i(t) > 0$$), ta có:

$$
\begin{align}
f(x^*(t)) - f(x^*) + \sum_{i=1}^{m} u_i(t) (h_i(x^*(t)) - h_i(x^*) ) &\le \left\langle \nabla f(x^*(t)) + \sum_{i=1}^{m} u_i(t) \nabla h_i(x^*(t)), \quad x^*(t) - x^* \right\rangle \\\\
&= \left\langle -A^Tv, \quad x^*(t) - x^* \right\rangle \\\\
\end{align}
$$

Vì $$Ax^*(t) = b$$ và $$Ax^* = b$$, nên $$\langle -A^Tv, x^*(t) - x^* \rangle = -v^T A(x^*(t) - x^*) = 0$$.

Chuyển tổng ở vế trái sang vế phải và rút gọn:

$$
\begin{align}
f(x^*(t)) - f(x^*) &\le - \sum_{i=1}^{m} u_i(t) (h_i(x^*(t)) - h_i(x^*) ) \\\\
&= \frac{m}{t} + \sum_{i=1}^{m} u_i(t) h_i(x^*) \\\\
&\le \frac{m}{t}
\end{align}
$$

Ở dòng thứ hai, ta thay $$u_i(t) \cdot h_i(x^*(t)) = - \frac{1}{t}$$ từ điều kiện KKT nhiễu để thu được $$\frac{m}{t}$$. Ở dòng cuối, tổng $$\sum_{i=1}^{m} u_i(t) h_i(x^*) \le 0$$ vì $$u_i(t) > 0$$ và $$h_i(x^*) \le 0$$.

Như vậy, ta thu được cận trên cho khoảng cách dưới tối ưu, đồng thời là tiêu chí dừng hữu ích cho phương pháp chắn (mối liên hệ với khoảng cách đối ngẫu cũng sẽ được phân tích thêm ở các chương sau):

>$$
>\begin{align}
>f(x^*(t)) - f(x^*) \le \frac{m}{t}
>\end{align}
>$$
