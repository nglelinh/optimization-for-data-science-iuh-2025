---
layout: post
title: 03-04-04 Các phép toán bảo toàn tính giả lồi
chapter: '03'
order: 12
owner: Minjoo Lee
categories:
- chapter03
lang: vi
---

Một cái bẫy cực kỳ nguy hiểm khi làm việc với hàm giả lồi: khác với hàm lồi, **tổng của hai hàm giả lồi nói chung KHÔNG phải hàm giả lồi**! (Hãy tưởng tượng cộng hai hàm bậc thang ngược chiều nhau tạo thành một đỉnh nhô lên ở giữa.) Thay vào đó, hàm giả lồi lại đóng dưới những phép toán riêng của nó — đặc biệt là **cực đại trọng số không âm**, **hợp thành với hàm không giảm**, và quan trọng nhất: **biểu diễn qua họ hàm lồi $$\phi_t(x) \le 0$$** dùng trực tiếp trong thuật toán chia đôi!

Bài học này hệ thống hóa các quy tắc lắp ghép hàm giả lồi và cách giải bài toán tối ưu giả lồi bằng chuỗi bài toán lồi.

## Kiến thức cần nhớ: Bốn quy tắc bảo toàn và biểu diễn Hàm giả lồi

- **Cực đại từng điểm (không phải phép cộng!):** Nếu $$f_i$$ giả lồi và $$w_i \ge 0$$ thì $$f(x) = \max_i w_i f_i(x)$$ (hoặc $$\sup_{y} w(y) f(x, y)$$) luôn giả lồi. *Cảnh báo:* $$f_1 + f_2$$ không nhất thiết giả lồi!
- **Hợp thành với hàm không giảm và ánh xạ affine:** Nếu $$g$$ giả lồi và $$h: \mathbb{R} \to \mathbb{R}$$ không giảm thì $$h(g(x))$$ giả lồi (nhờ đó mọi phép biến đổi đơn điệu như $$e^{g}, g^3, \ln g$$ bảo toàn tính giả lồi!); hợp thành $$f(Ax + b)$$ hay phân thức tuyến tính cũng bảo toàn tính giả lồi.
- **Cực tiểu hóa từng phần:** Nếu $$f(x, y)$$ giả lồi đồng thời theo $$(x, y)$$ và $$C$$ là tập lồi, thì $$g(x) = \inf_{y \in C} f(x, y)$$ vẫn giả lồi.
- **Biểu diễn qua họ hàm lồi $$\phi_t(x)$$:** Mọi hàm giả lồi đều biểu diễn được tập mức dưới dạng $$f(x) \le t \iff \phi_t(x) \le 0$$ với $$\phi_t$$ là **hàm lồi** theo $$x$$ — đây chính là động cơ của phương pháp chia đôi tối ưu giả lồi!

### Giải thích: Giải tay 3 bước chia đôi cho bài toán giả lồi $$\min_{x \ge 0} \frac{x^2 + 1}{x + 2}$$

Xét bài toán tối ưu giả lồi $$\min_{x \ge 0} f(x) = \frac{x^2 + 1}{x + 2}$$:

1. **Biểu diễn tập mức dưới bằng họ hàm lồi $$\phi_t(x)$$:**
   Với $$x \ge 0$$ (nên $$x + 2 > 0$$), điều kiện $$f(x) \le t$$ tương đương:
   $$\phi_t(x) = x^2 - tx + (1 - 2t) \le 0.$$
   Với mọi $$t$$ cố định, $$\phi_t(x)$$ là **hàm bậc hai lồi** (vì $$\phi_t''(x) = 2 > 0$$)!
2. **Thử mức $$t = 1$$:** $$\phi_1(x) = x^2 - x - 1 \le 0$$. Tại $$x = 1 \ge 0$$: $$\phi_1(1) = -1 \le 0$$ (khả thi!) $$\implies p^* \le 1$$.
3. **Thử mức $$t = 0.5$$:** $$\phi_{0.5}(x) = x^2 - 0.5x \le 0$$. Tại $$x = 0 \ge 0$$: $$\phi_{0.5}(0) = 0 \le 0$$ (khả thi!) $$\implies p^* \le 0.5$$.
4. **Thử mức $$t = 0.4$$:** $$\phi_{0.4}(x) = x^2 - 0.4x + 0.2 \le 0$$. Tính biệt thức $$\Delta = (-0.4)^2 - 4(1)(0.2) = 0.16 - 0.80 = -0.64 < 0 \implies \phi_{0.4}(x) > 0\ \forall x$$ (**vô nghiệm**!) $$\implies p^* > 0.4$$.
   Chỉ sau 3 bước kiểm tra khả thi lồi, ta đã kẹp chặt nghiệm tối ưu vào khoảng $$(0.4, 0.5]$$ (nghiệm đúng là $$p^* = 2\sqrt{5} - 4 \approx 0.4721$$ tại $$x^* = \sqrt{5} - 2 \approx 0.236$$)!

---

Phần này trình bày các phép toán bảo toàn tính giả lồi của hàm số.

## Maximum trọng số không âm

Nếu $$f_1, \dots, f_m$$ là các hàm giả lồi và $$w_i \geq 0$$, thì maximum có trọng số không âm của chúng cũng là hàm giả lồi:
>$$f = \max\{w_1f_1, ... ,w_mf_m\}$$ với $$w_i \geq 0$$ là giả lồi

Tổng quát hơn cho họ vô hạn các hàm:
>$$f(x) = \sup_{y \in C}(w(y)g(x,y))$$ với $$w(y) \geq 0$$,
>trong đó $$g(x,y)$$ là hàm giả lồi theo $$x$$ với mọi $$y \in C$$.

<br>

## Hợp thành

Nếu $$g : \mathbb{R}^n \mapsto \mathbb{R}$$ là hàm giả lồi và $$h : \mathbb{R} \mapsto \mathbb{R}$$ không giảm, thì hàm hợp thành $$f = h \circ g$$ cũng là hàm giả lồi:
> $$f = h \circ g$$ là giả lồi nếu $$h$$ không giảm và $$g$$ là giả lồi.

Hợp thành một hàm giả lồi với biến đổi affine hoặc biến đổi tuyến tính-phân thức cũng bảo toàn tính giả lồi: nếu $$f$$ là hàm giả lồi thì $$g(x) = f(Ax + b)$$ giả lồi, và $$\tilde{g}(x) = f((Ax + b)/(c^Tx + d))$$ giả lồi trên miền $$\{x \mid c^Tx + d > 0,\; (Ax + b)/(c^Tx + d) \in \text{dom}f\}$$.

<br>

## Cực tiểu hóa từng phần

Nếu $$f(x, y)$$ là hàm giả lồi đồng thời theo $$(x, y)$$ và $$C$$ là một tập lồi, thì phép lấy infimum theo $$y \in C$$ bảo toàn tính giả lồi:
> $$g(x) = \inf_{y \in C} f(x,y)$$ là giả lồi nếu $$f$$ giả lồi theo $$(x,y)$$ và $$C$$ là một tập lồi.

<br>

## Biểu diễn thông qua họ các hàm lồi

Các tập mức dưới của một hàm giả lồi $$f$$ có thể được biểu diễn bằng các bất đẳng thức liên quan đến một họ hàm lồi $$\phi_t : \mathbb{R}^n \mapsto \mathbb{R}$$ (tham số hóa bởi $$t \in \mathbb{R}$$) sao cho:
>$$f(x) \leq t \Longleftrightarrow \phi_t(x) \leq 0$$

Nói cách khác, tập mức dưới mức $$t$$ của hàm giả lồi $$f$$ trùng với tập mức dưới mức 0 của hàm lồi $$\phi_t$$. Hơn nữa, với mọi $$x \in \mathbb{R}^n$$ và mọi $$s \geq t$$, họ hàm này thỏa mãn tính lồng nhau:
>$$\phi_t(x) \leq 0 \Rightarrow \phi_s(x) \leq 0 \text{ với } s \geq t$$
