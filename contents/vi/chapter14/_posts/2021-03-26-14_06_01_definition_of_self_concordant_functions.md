---
layout: post
title: 14-06-01 Định nghĩa các hàm tự hài hòa
chapter: '14'
order: 13
owner: Minjoo Lee
categories:
- chapter14
lang: vi
---

Nhìn thoáng qua bất đẳng thức định nghĩa hàm tự hài hòa $$\vert f'''(x) \vert \le 2 (f''(x))^{3/2}$$, nhiều người tự hỏi: *số mũ $$3/2$$ kỳ lạ kia từ đâu chui ra, và tại sao hằng số phía trước lại là số $$2$$?* Không hề ngẫu nhiên chút nào! Số mũ $$3/2$$ là số mũ **duy nhất** làm cho bất đẳng thức hoàn toàn bất biến dưới phép co giãn trục $$x \mapsto \alpha x$$, còn hằng số $$2$$ được chuẩn hóa khớp vừa khít với hàm chắn logarit cơ bản nhất $$f(x) = -\log x$$.

Và để mở rộng từ trục thực $$\mathbb{R}$$ sang không gian nhiều chiều $$\mathbb{R}^n$$ mà không phải vật lộn với ten-xơ đạo hàm bậc ba phức tạp, định nghĩa dùng một thủ thuật cực kỳ thanh lịch: một hàm nhiều biến $$f(x)$$ là tự hài hòa nếu lát cắt của nó dọc theo **mọi đường thẳng** $$g(t) = f(x + tv)$$ đều là hàm tự hài hòa 1 chiều!

## Kiến thức cần nhớ: Cấu trúc đại số và quy tắc bảo toàn tính tự hài hòa

- **Ý nghĩa của số mũ $$3/2$$:** Nếu đổi biến $$h(t) = f(\alpha t)$$, thì $$h''(t) = \alpha^2 f''(\alpha t)$$ và $$h'''(t) = \alpha^3 f'''(\alpha t)$$. Ta thấy $$\vert h''' \vert / (h'')^{3/2} = \vert \alpha^3 f''' \vert / (\alpha^2 f'')^{3/2} = \vert f''' \vert / (f'')^{3/2}$$ — tham số $$\alpha$$ triệt tiêu hoàn toàn!
- **Mở rộng sang $$\mathbb{R}^n$$ qua lát cắt 1D:** $$f: \mathbb{R}^n \to \mathbb{R}$$ tự hài hòa khi và chỉ khi với mọi $$x \in \operatorname{dom} f$$ và mọi hướng $$v \in \mathbb{R}^n$$, hàm $$g(t) = f(x + tv)$$ tự hài hòa trên $$\mathbb{R}$$.
- **Các phép toán bảo toàn tính tự hài hòa:**
  - Tổng của các hàm tự hài hòa là hàm tự hài hòa.
  - Phép hợp với ánh xạ affine $$f(Ax + b)$$ luôn giữ nguyên tính tự hài hòa.
  - Nhân một hàm tự hài hòa với hằng số $$c \ge 1$$ giữ nguyên tính tự hài hòa (còn nếu $$0 < c < 1$$ thì có thể phá vỡ bất đẳng thức vì vế trái nhân $$c$$ còn vế phải nhân $$c^{3/2} < c$$!).
- **Các hàm tự hài hòa tiêu biểu:** Mọi hàm tuyến tính, hàm bậc hai lồi ($$f''' = 0$$), hàm $$-\log x$$, hàm $$-\sum \log(b_i - a_i^T x)$$, và $$-\log\det X$$ trên nón ma trận xác định dương.

### Giải thích: Kiểm tra trực tiếp hai hàm — một hàm tự hài hòa và một hàm KHÔNG tự hài hòa

1. **Kiểm tra $$f(x) = -\log(x) + 3x^2 - 5x$$ trên $$x > 0$$:**
   - $$f''(x) = \frac{1}{x^2} + 6 > \frac{1}{x^2}$$.
   - $$f'''(x) = -\frac{2}{x^3} \implies \vert f'''(x) \vert = \frac{2}{x^3}$$.
   - So sánh với $$2(f''(x))^{3/2}$$:
     $$2(f''(x))^{3/2} = 2\left(\frac{1}{x^2} + 6\right)^{3/2} > 2\left(\frac{1}{x^2}\right)^{3/2} = \frac{2}{x^3} = \vert f'''(x) \vert.$$
   Bất đẳng thức thỏa mãn tại mọi $$x > 0$$ → **tự hài hòa!**
2. **Kiểm tra $$h(x) = e^x$$ trên $$\mathbb{R}$$:**
   - $$h''(x) = e^x$$, $$h'''(x) = e^x$$.
   - Xét tỷ số: $$\frac{\vert h'''(x) \vert}{(h''(x))^{3/2}} = \frac{e^x}{e^{3x/2}} = e^{-x/2}$$.
   - Khi $$x = -4$$, tỷ số bằng $$e^2 \approx 7.39 > 2$$ (và khi $$x \to -\infty$$, tỷ số vọt lên $$+\infty$$).
   → $$e^x$$ **KHÔNG** tự hài hòa trên $$\mathbb{R}$$! (Tuy nhiên $$e^x - \log x$$ hay $$e^x$$ trên nửa trục bị chặn dưới có thể xử lý bằng cách cộng thêm số hạng chắn hoặc giới hạn miền).

---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
    });
</script>
## Tự hài hòa trên $$\mathbb{R}$$
Một hàm lồi $$f : \mathbb{R} \rightarrow \mathbb{R}$$ được gọi là **tự hài hòa (self-concordant)** nếu nó thỏa mãn bất đẳng thức:
>$$
>\begin{align}
>|f^{'''}(x)| \leq 2f^{''}(x)^{3/2} \qquad \text{for all }x\in \text{dom }f.
>\end{align}
>$$

Ví dụ đơn giản: mọi hàm tuyến tính ($$ax+b$$) và hàm bậc hai lồi đều là hàm tự hài hòa vì đạo hàm bậc ba của chúng bằng $$0$$.

## Tự hài hòa trên $$\mathbb{R}^{n}$$
Một hàm $$f : \mathbb{R}^{n}\rightarrow \mathbb{R}$$ được gọi là tự hài hòa nếu nó tự hài hòa dọc theo mọi đường thẳng cắt miền xác định của nó. Cụ thể, với mọi $$x\in \text{dom}\, f$$ và mọi vector $$v$$, nếu hàm một biến $$g(t) = f(x+tv)$$ là tự hài hòa thì $$f$$ là hàm tự hài hòa trên $$\mathbb{R}^{n}$$.

## Ví dụ về hàm tự hài hòa

1) $$f : \mathbb{R}^{n}_{++}\rightarrow \mathbb{R}$$, $$f(x) = -\sum^{n}_{i=1}\log(x_{i})$$.

Ta có thể dễ dàng kiểm tra rằng hàm một biến $$f(t) = -\log{t}$$ là tự hài hòa. Hơn nữa, tổng của các hàm tự hài hòa cũng là hàm tự hài hòa: với hai hàm tự hài hòa $$f_{1}, f_{2} : \mathbb{R}\rightarrow \mathbb{R}$$, ta có [3]:
>$$
>\begin{align}
>|f_{1}^{'''}(x)+f_{2}^{'''}(x)|  \leq & |f^{'''}_{1}(x)|+|f^{'''}_{2}(x)|\\\\
> \leq &2\big( f^{''}_{1}(x)^{3/2}+f^{''}_{2}(x)^{3/2}\big)\\\\
>\leq &2\big( f^{''}_{1}(x)+f^{''}_{2}(x) \big)^{3/2}.
>\end{align}
>$$

Bước cuối sử dụng bất đẳng thức:
>$$
>\begin{align}
>(u^{3/2}+v^{3/2})^{2/3} \leq u+v, \qquad u, v \geq 0.
>\end{align}
>$$
