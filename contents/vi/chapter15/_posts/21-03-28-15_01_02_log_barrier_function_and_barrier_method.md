---
layout: post
title: '15-01-02 Hàm chắn logarit và phương pháp chắn'
chapter: '15'
order: 4
owner: Minjoo Lee
categories:
- chapter15
lang: vi
---

Vì sao trong vô số hàm tăng lên $$+\infty$$ khi $$u \to 0^-$$ (như $$-1/u$$ hay $$1/u^2$$), lịch sử tối ưu hóa lại tôn vinh **hàm chắn logarit** $$\phi(x) = -\sum_{i=1}^m \log(-h_i(x))$$ làm "nữ hoàng" của phương pháp điểm trong?

Lý do không chỉ vì logarit trơn và lồi, mà còn bởi hai phép màu toán học hiếm có: thứ nhất, $$-\log(-u)$$ là **hàm tự hài hòa** chuẩn mực (nên phương pháp Newton chạy trên nó không bị ảnh hưởng bởi sự bùng nổ đạo hàm gần biên); thứ hai, đạo hàm của $$-\log(-u)$$ là $$-1/u$$ lại khớp khít một cách hoàn hảo với điều kiện **bù yếu (complementary slackness)** $$u_i h_i(x) = 0$$ trong hệ KKT khi thay $$0$$ bằng $$-1/t$$!

## Bản đồ kiến thức nền: Từ hàm chắn logarit đến bài toán chắn tương đương

- **Định nghĩa hàm chắn logarit:** $$\phi(x) = -\sum_{i=1}^m \log(-h_i(x))$$ với miền xác định là tập khả thi chặt $$\{x : h_i(x) < 0 \;\forall i\}$$.
- **Tính lồi của $$\phi(x)$$:** Vì mỗi $$h_i(x)$$ lồi nên $$-h_i(x)$$ lõm và dương trên miền trong; hàm $$-\log(\cdot)$$ lồi và nghịch biến, do đó theo quy tắc hợp hàm lồi, $$-\log(-h_i(x))$$ luôn là hàm lồi!
- **Hai cách viết tương đương của bài toán chắn:** Cực tiểu hóa $$f(x) + \frac{1}{t}\phi(x)$$ hoàn toàn tương đương (có cùng tập nghiệm $$x^*(t)$$) với cực tiểu hóa $$t f(x) + \phi(x)$$ thỏa $$Ax = b$$. Dạng $$t f(x) + \phi(x)$$ được ưa chuộng hơn vì giữ hệ số trước $$\phi(x)$$ bằng $$1$$, bảo toàn nguyên vẹn tính **tự hài hòa** của hàm chắn!

### Khung giải thích (nên đọc chậm): Tính nghiệm bài toán chắn trên đoạn $$[0, 2]$$ và thấy rõ vai trò hệ số $$t$$

Xét bài toán cực tiểu hóa $$\min_x (x - 3)^2$$ trên đoạn $$0 \le x \le 2$$ (tức $$h_1(x) = -x \le 0$$ và $$h_2(x) = x - 2 \le 0$$). Nghiệm gốc rõ ràng là $$x^* = 2$$ (nằm ngay sát biên phải).

1. **Viết hàm chắn logarit:**
   $$\phi(x) = -\log(x) - \log(2 - x), \qquad x \in (0, 2).$$
2. **Tìm tâm giải tích (Analytic Center) khi $$t = 0$$:**
   $$\phi'(x) = -\frac{1}{x} + \frac{1}{2 - x} = 0 \implies x^*(0) = 1$$ (chính giữa đoạn $$(0, 2)$$, nơi lực đẩy từ hai tường $$0$$ và $$2$$ cân bằng nhau!).
3. **Giải bài toán chắn $$\min_{x \in (0,2)} t(x - 3)^2 - \log(x) - \log(2 - x)$$ tại $$t = 1$$ và $$t = 10$$:**
   Điều kiện đạo hàm bằng $$0$$: $$2t(x - 3) - \frac{1}{x} + \frac{1}{2 - x} = 0$$.
   - Tại $$t = 1$$: thử $$x \approx 1.68$$: $$2(1.68 - 3) - \frac{1}{1.68} + \frac{1}{0.32} = -2.64 - 0.595 + 3.125 = -0.11 \approx 0$$ (nghiệm chính xác $$x^*(1) \approx 1.691$$).
   - Tại $$t = 10$$: thử $$x \approx 1.95$$: $$20(1.95 - 3) - \frac{1}{1.95} + \frac{1}{0.05} = -21.0 - 0.513 + 20.0 = -1.51 \implies$$ tiến sát hơn nữa: $$x^*(10) \approx 1.953$$!
   Khi $$t$$ tăng từ $$0 \to 1 \to 10$$, lực hút của hàm mục tiêu thắng dần lực đẩy của bức tường $$x = 2$$, kéo nghiệm từ tâm $$1.0 \to 1.691 \to 1.953 \to 2.0$$!

---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Trước khi phát biểu phương pháp chắn, ta xem xét cách xấp xỉ hàm chỉ thị bằng hàm chắn trơn.

## Xấp xỉ hàm chỉ thị
Hình dưới đây minh họa hàm chỉ thị và các hàm chắn tương ứng. Đường nét đứt là hàm chỉ thị $$I_C$$, còn các đường nét liền là hàm chắn $$\phi(x) = -1/t\log(-x)$$ ứng với $$t = 0.5, 1, 2$$. Hàm chắn xấp xỉ hàm chỉ thị một cách trơn tru, và khi $$t$$ tăng (chẳng hạn $$t = 2$$ trong hình), xấp xỉ càng sát hàm chỉ thị.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_barrier_function_01.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">$$\text{[Hình 1] Hàm chắn }\phi(x) = -1/t\log(-x) [1]$$</figcaption>
</p>
</figure>

## Hàm chắn logarit
Giả sử $$h_1, \cdots , h_m : \mathbb{R}^n \to \mathbb{R}$$ là các hàm lồi và khả vi hai lần. Trên tập $$\{x : h_i(x) \lt 0, i = 1, \cdots , m \}$$, **hàm chắn logarit (logarithmic barrier function)** được định nghĩa là:

>
\begin{align}
\phi(x) = - \sum_{i=1}^{m} \log(-h_i(x))
\end{align}

Tập xác định trên được giả sử là phần trong khác rỗng của tập khả thi $$C$$.

## Phương pháp chắn
Sử dụng hàm chắn logarit với tham số $$t \gt 0$$, bài toán tối ưu ban đầu được xấp xỉ bởi bài toán có ràng buộc đẳng thức sau:
>
$$\begin{align}
&\min_{x}           && f(x) + \frac{1}{t} \phi(x) & \qquad      & \min_{x} && tf(x) + \phi(x) \\
&\text{subject to } && Ax = b                     & \iff \qquad & \text{subject to } && Ax = b \\
\end{align}$$

Phương pháp giải bài toán xấp xỉ này bằng phương pháp Newton được gọi là **phương pháp chắn (barrier method)**.
