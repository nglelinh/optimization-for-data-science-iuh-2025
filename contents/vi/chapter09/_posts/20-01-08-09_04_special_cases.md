---
layout: post
title: '09-04 Các trường hợp đặc biệt'
chapter: '09'
order: 5
owner: Kyeongmin Woo
categories:
- chapter09
lang: vi
---

Trong toán học, dấu hiệu của một khái niệm thực sự sâu sắc là nó có khả năng "thống nhất nhiều vùng đất tưởng chừng rời rạc dưới cùng một mái nhà". Phương pháp gradient gần kề chính là một khái niệm như vậy. Khi ta lần lượt bật tắt hai thành phần $$g(x)$$ và $$h(x)$$ trong bài toán tổng hợp $$\min_x g(x) + h(x)$$, hàng loạt thuật toán kinh điển mà bạn đã học trước đây bỗng đồng loạt hiện ra như những lát cắt đặc biệt của cùng một công thức duy nhất!

Đặt $$h = 0$$, ta thu lại ngay **Gradient Descent**. Đặt $$h = I_C$$ (hàm chỉ thị của tập lồi đóng $$C$$), toán tử prox biến thành phép chiếu Euclid $$P_C$$ và ta thu lại **Projected Gradient Descent**. Còn nếu đặt $$g = 0$$, ta khám phá ra một thuật toán cực kỳ mạnh mẽ của lý thuyết tối ưu hiện đại: **Thuật toán tối ưu gần kề (Proximal Point / Proximal Minimization Algorithm)** — thuật toán hội tụ cho *mọi* kích thước bước $$t > 0$$ lớn tùy ý!

## Bản đồ kiến thức nền: Bốn nhánh kết nối của phương pháp gradient tổng quát

- **$$h(x) = 0 \implies$$ Gradient Descent cổ điển:** Khi không có phần không trơn, $$\operatorname{prox}_{t \cdot 0}(v) = \arg\min_z \frac{1}{2t}\|z - v\|_2^2 = v$$ (ánh xạ đồng nhất), nên $$x^{(k)} = x^{(k-1)} - t_k \nabla g(x^{(k-1)})$$.
- **$$h(x) = I_C(x) \implies$$ Projected Gradient Descent:** Hàm chỉ thị bằng $$0$$ trên $$C$$ và $$+\infty$$ ngoài $$C$$ biến bài toán con prox thành $$\arg\min_{z \in C} \|z - v\|_2^2 = P_C(v)$$. Mọi định lý hội tụ $$O(1/k)$$ của Chương 09 lập tức áp dụng miễn phí cho bài toán trơn có ràng buộc lồi!
- **$$g(x) = 0 \implies$$ Thuật toán tối ưu gần kề (Proximal Point Algorithm):** Công thức $$x^{(k)} = \operatorname{prox}_{t_k h}(x^{(k-1)})$$ không cần $$h$$ khả vi và không hề bị giới hạn bởi $$t \le 1/L$$; bước $$t_k$$ càng lớn, mỗi vòng lặp càng tiến gần nghiệm tối ưu toàn cục (nhưng bài toán con càng khó giải).
- **Toán tử gần kề xấp xỉ (Inexact Proximal Methods):** Khi $$\operatorname{prox}_{t h}$$ không có công thức đóng, ta có thể giải gần đúng bài toán con bằng một vòng lặp trong (inner solver). Để vẫn giữ tốc độ hội tụ $$O(1/k)$$, sai số giải bài toán con ở bước $$k$$ phải giảm đủ nhanh (cỡ $$\varepsilon_k \sim O(1/k^2)$$ hoặc khả tổng).

### Khung giải thích (nên đọc chậm): Tính tay so sánh Gradient Descent và Proximal Minimization trên $$f(x) = \frac{1}{2}x^2$$

Xét hàm đơn giản $$f(x) = \frac{1}{2}x^2$$ (nghiệm $$x^* = 0$$, độ cong $$L = 1$$), khởi tạo tại $$x^{(0)} = 4$$, thử một kích thước bước **rất lớn** $$t = 3$$ (vượt xa ngưỡng $$2/L = 2$$ của Gradient Descent!).

1. **Coi $$g(x) = \frac{1}{2}x^2, h(x) = 0$$ (Gradient Descent tường minh):**
   $$x^{(1)} = x^{(0)} - t \nabla g(x^{(0)}) = 4 - 3(4) = -8.$$
   $$x^{(2)} = -8 - 3(-8) = +16.$$
   Dãy bùng nổ ra vô cực vì bước $$t = 3$$ vượt ngưỡng ổn định $$2/L = 2$$!
2. **Coi $$g(x) = 0, h(x) = \frac{1}{2}x^2$$ (Proximal Minimization / bước ẩn):**
   Giải bài toán con $$\min_z \left\{\frac{1}{2t}(z - x)^2 + \frac{1}{2}z^2\right\}$$ bằng cách cho đạo hàm bằng $$0$$:
   $$\frac{z - x}{t} + z = 0 \implies z = \frac{x}{1 + t}.$$
   Với $$t = 3$$ và $$x^{(0)} = 4$$:
   - $$x^{(1)} = \frac{4}{1 + 3} = 1.0$$
   - $$x^{(2)} = \frac{1.0}{4} = 0.25$$
   - $$x^{(3)} = \frac{0.25}{4} = 0.0625$$!
   Càng chọn $$t$$ lớn (ví dụ $$t = 99$$), $$x^{(1)} = \frac{4}{100} = 0.04$$ tiến thẳng về $$0$$ gần như tức thì — đây chính là khác biệt bản chất giữa sơ đồ *tường minh* (explicit) và sơ đồ *ẩn* (implicit) trong giải tích số!

# Các trường hợp đặc biệt

Phương pháp gradient gần kề còn được gọi là phương pháp gradient descent tổng hợp (composite gradient descent) hoặc gradient descent tổng quát (generalized gradient descent).

Lý do phương pháp này mang tính **"tổng quát"** là vì nó bao hàm các thuật toán quen thuộc sau như những trường hợp đặc biệt:

- $$h = 0 \to$$ phương pháp gradient descent
- $$h = I_C \to$$ phương pháp gradient descent có chiếu (projected gradient descent)
- $$g = 0 \to$$ thuật toán tối ưu gần kề (proximal minimization algorithm)

Nhờ cùng nằm trong khuôn khổ chung này, tất cả các thuật toán trên đều thừa hưởng tốc độ hội tụ $$O(1/\epsilon)$$.

## Gradient descent có chiếu (Projected gradient descent)
Với $$I_C(x)$$ là hàm chỉ thị của một tập lồi đóng $$C \subseteq \mathbb{R}^n$$, bài toán tối ưu có ràng buộc trên tập $$C$$ có thể được viết lại thành bài toán không ràng buộc như sau (lưu ý $$C$$ cần là tập đóng để phép chiếu được xác định duy nhất):

> $$ \min_{x \in C} g(x) \iff \min_x g(x) + I_C(x)$$
>
> $$I_C(x) = 
>\begin{cases}
>0, & x \in C \\
>\infty, & x \notin C
>\end{cases}$$

Khi đó, ánh xạ gần kề của $$I_C$$ là:

> $$
>\begin{align}
>\text{prox}_t(x)  
>&= \underset{z}{\text{argmin}} \frac{1}{2t} \lVert x−z \rVert_2^2 + I_C(z) \\
>& = \underset{z \in C}{\text{argmin}} \lVert x−z \rVert_2^2
>\end{align} $$

Do đó $$\text{prox}_t(x) = P_C(x)$$ chính là phép chiếu Euclid lên tập $$C$$.

Bước cập nhật gradient gần kề trở thành $$x^+ = P_C (x−t \nabla g(x) )$$: sau khi thực hiện một bước gradient descent, ta chiếu điểm vừa thu được trở về tập khả thi $$C$$.

Trong hình minh họa dưới đây, hình chữ nhật màu hồng là tập khả thi $$C$$. Khi bước gradient descent đưa điểm lặp ra ngoài $$C$$, phép chiếu $$P_C$$ đưa điểm đó quay lại điểm gần nhất thuộc $$C$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter09/projected_gradient_descent.png" width="80%" height="80%">
  <figcaption style="text-align: center;">[Hình 1] Projected Gradient Descent [3]</figcaption>
</p>
</figure>

## Thuật toán tối ưu gần kề (Proximal Minimization Algorithm)

Xét bài toán cực tiểu hóa một hàm lồi $$h$$ không nhất thiết khả vi, tương ứng với trường hợp $$g(x) = 0$$:
>
\begin{align}
\min_x h(x)
\end{align}

Công thức lặp gradient gần kề rút gọn thành:
> $$
\begin{align}
x^{(k)} &= \text{prox}_{t_k} \big(x^{(k-1)} - t_k \nabla g ( x^{(k-1)} ) \big) , \qquad k = 1, 2, 3, ... \\
&= \text{prox}_{t_k} \big(x^{(k-1)} \big) ,  \qquad \qquad \qquad \qquad \; k = 1, 2, 3, ... \\
\end{align} $$

Hay viết tường minh:
> $$x^+ = \underset{z}{\text{argmin}} \frac{1}{2t} \lVert x−z \rVert_2^2 + h(z)$$

Thuật toán này được gọi là **thuật toán tối ưu gần kề (PMA)**. Về số bước lặp, PMA hội tụ nhanh hơn phương pháp subgradient; tuy nhiên, thuật toán chỉ thực sự hữu ích khi ánh xạ gần kề của $$h$$ có thể tính được hiệu quả (ví dụ ở dạng đóng).

## Khi ánh xạ gần kề không thể tính chính xác
Về mặt lý thuyết, khi áp dụng phương pháp gradient gần kề cho $$f = g + h$$, ta giả định bài toán con xác định $$\text{prox}_t(x)$$ được giải chính xác:
>  $$\text{prox}_t(x )= \underset{z}{\text{argmin}} \frac{1}{2t} \lVert x−z \rVert_2^2 + h(z)$$

Nếu bài toán con này chỉ được giải xấp xỉ, nhìn chung không tự động đảm bảo kết quả hội tụ ban đầu. Tuy nhiên, nếu sai số xấp xỉ của toán tử gần kề giảm đủ nhanh và được kiểm soát chặt chẽ, tốc độ hội tụ ban đầu vẫn được bảo toàn (Schmidt et al. (2011), Convergence rates of inexact proximal-gradient methods for convex optimization).

Trong thực hành, khi phải tính gần đúng $$\text{prox}_t$$, người ta thường giải bài toán con với độ chính xác cao.
