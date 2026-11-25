---
layout: post
title: '22-03 Phân tích hội tụ'
chapter: '22'
order: 4
owner: YoungJae Choung
categories:
- chapter22
lang: vi
---

Một thuật toán tối ưu đẹp đến đâu cũng phải trả lời một câu hỏi lạnh lùng: *nó hội tụ nhanh cỡ nào, và điều gì quyết định tốc độ ấy?* Ở các phương pháp gradient trước đây, tốc độ hội tụ thường phụ thuộc vào hằng số Lipschitz $$L$$ của gradient đo theo chuẩn Euclid. Nhưng Frank–Wolfe lại có một đặc tính hết sức bất ngờ: nếu bạn kéo giãn hay xoay hệ tọa độ bằng một phép biến đổi tuyến tính khả nghịch, toàn bộ quỹ đạo điểm lặp của Frank–Wolfe **không hề thay đổi**.

Vì thuật toán bất biến dưới phép biến đổi affine, công cụ đo độ cong để phân tích hội tụ của nó cũng phải bất biến affine! Đó là lý do Martin Jaggi (2011) đưa ra **hằng số độ cong $$M$$** dựa trên độ phân kỳ Bregman, giúp rút gọn toàn bộ chứng minh hội tụ tốc độ $$O(1/k)$$ thành một bất đẳng thức duy nhất cực kỳ trong sáng.

## Kiến thức cần nhớ: Ba trụ cột của chứng minh hội tụ Frank–Wolfe

Trước khi theo dõi từng dòng biến đổi quy nạp trong bài, hãy nắm chắc ba khái niệm làm xương sống cho chứng minh:

- **Độ phân kỳ Bregman và Hằng số độ cong $$M$$:** Đại lượng $$D_f(y, x) = f(y) - f(x) - \nabla f(x)^T(y - x)$$ đo khoảng cách từ hàm $$f$$ tới mặt phẳng tiếp tuyến của nó tại $$x$$. Hằng số $$M$$ chuẩn hóa đại lượng này theo $$\gamma^2/2$$ trên mọi đoạn thẳng nằm trong $$C$$, nên nó vừa đo "độ cong" của $$f$$, vừa đo "đường kính" của tập $$C$$ — và hoàn toàn không phụ thuộc vào việc ta chọn chuẩn nào.
- **Bất đẳng thức giảm theo khoảng cách đối ngẫu:** Ở mỗi bước, mức giảm hàm mục tiêu được điều khiển bởi hai lực đối lập: lực kéo xuống $$-\gamma_k g(x^{(k-1)})$$ tỉ lệ thuận với khoảng cách đối ngẫu, và sai số độ cong $$+\frac{\gamma_k^2}{2} M$$. Khi $$\gamma_k$$ nhỏ dần theo quy luật $$2/(k+1)$$, số hạng bậc nhất luôn thắng thế số hạng bậc hai.
- **Tính bất biến affine (Affine Invariance) và Độ bền với LMO xấp xỉ:** Không chỉ bất biến khi đổi hệ tọa độ (điểm yếu của Projected Gradient Descent khi bài toán bị kéo lệch điều kiện), khung phân tích bằng $$M$$ còn cho phép LMO giải *gần đúng* với sai số $$\delta$$ mà vẫn giữ nguyên bậc hội tụ $$O(1/k)$$.

### Giải thích: Tính tay hằng số độ cong $$M$$ và kiểm chứng bất đẳng thức cơ bản

Hãy kiểm chứng trực tiếp từng đại lượng trong định lý hội tụ trên một bài toán 1 chiều cực kỳ trong sáng: cực tiểu hóa $$f(x) = \frac{1}{2}x^2$$ trên đoạn $$C = [-1, 1]$$ (nghiệm tối ưu $$x^\star = 0, f^\star = 0$$).

1. **Tính chính xác hằng số độ cong $$M$$:**
   Với $$x, s \in [-1, 1]$$ và $$y = x + \gamma(s - x)$$, ta tính độ phân kỳ Bregman:
   $$f(y) - f(x) - f'(x)(y - x) = \frac{1}{2}(x + \gamma(s-x))^2 - \frac{1}{2}x^2 - x \cdot \gamma(s-x) = \frac{1}{2}\gamma^2 (s - x)^2.$$
   Nhân với $$\frac{2}{\gamma^2}$$, ta thu được biểu thức đơn giản $$(s - x)^2$$. Giá trị lớn nhất trên $$[-1, 1]$$ đạt tại $$s = 1, x = -1$$, cho ra chính xác $$M = (1 - (-1))^2 = 4$$.
2. **Chạy bước $$k = 1$$ từ $$x^{(0)} = 1$$ với $$\gamma_1 = \frac{2}{1+1} = 1$$:**
   Ta có $$f(x^{(0)}) = 0.5$$, $$f'(1) = 1$$, LMO chọn $$s^{(0)} = -1$$, khoảng cách đối ngẫu $$g(x^{(0)}) = 1 \cdot (1 - (-1)) = 2$$.
   Điểm mới $$x^{(1)} = (1 - 1)(1) + 1(-1) = -1$$, với $$f(x^{(1)}) = 0.5$$.
   Kiểm tra bất đẳng thức cơ bản:
   $$f(x^{(0)}) - \gamma_1 g(x^{(0)}) + \frac{\gamma_1^2}{2} M = 0.5 - 1 \cdot 2 + \frac{1}{2} \cdot 4 = 0.5 = f(x^{(1)}).$$
   Dấu bằng xảy ra tuyệt đối!
3. **Chạy bước $$k = 2$$ với $$\gamma_2 = \frac{2}{2+1} = \frac{2}{3}$$:**
   Tại $$x^{(1)} = -1$$, ta có $$f'(-1) = -1$$, LMO chọn $$s^{(1)} = 1$$, khoảng cách đối ngẫu $$g(x^{(1)}) = (-1)(-1 - 1) = 2$$.
   Điểm mới: $$x^{(2)} = \left(1 - \frac{2}{3}\right)(-1) + \frac{2}{3}(1) = \frac{1}{3}$$, nên $$f(x^{(2)}) = \frac{1}{18} \approx 0.0556$$.
   Kiểm tra bất đẳng thức cơ bản và cận định lý:
   - Vế phải bất đẳng thức cơ bản: $$0.5 - \frac{2}{3}(2) + \frac{(2/3)^2}{2}(4) = 0.5 - \frac{4}{3} + \frac{8}{9} = \frac{1}{18} = f(x^{(2)})$$.
   - Cận lý thuyết từ định lý: $$f(x^{(2)}) - f^\star = \frac{1}{18} \le \frac{2M}{2 + 2} = \frac{8}{4} = 2$$ — hoàn toàn nhất quán!

## Phân tích hội tụ

Để phân tích tốc độ hội tụ của thuật toán Frank-Wolfe, trước hết ta định nghĩa hằng số độ cong (curvature constant) của hàm $$f$$ trên tập $$C$$ [Jaggi (2011)]:
> $$M = \max_{x,s,y\in C,\; y = (1−\gamma)x+\gamma s,\; \gamma \in [0, 1]} \frac{2}{\gamma^2} \Bigl( f(y) − f(x) − \nabla f(x)^T(y − x) \Bigr)$$

Hằng số $$M$$ đo mức độ sai lệch của hàm $$f$$ so với xấp xỉ tuyến tính của nó trên $$C$$; chẳng hạn $$M = 0$$ khi $$f$$ là hàm tuyến tính. Đại lượng $$f(y) - f(x) - \nabla f(x)^T(y - x)$$ chính là độ phân kỳ Bregman (Bregman divergence) sinh bởi $$f$$.

> **Định lý:** Phương pháp gradient có điều kiện với kích thước bước cố định $$\gamma_k = 2 / (k + 1)$$ ($$k = 1, 2, 3, \ldots$$) thỏa mãn:
> $$f(x^{(k)}) − f^{\star} \leq \frac{2M}{k + 2}$$

Do đó, số vòng lặp cần thiết để đạt sai số $$f(x^{(k)}) − f^{\star} \leq \epsilon$$ là $$O(1/\epsilon)$$.

Ta sẽ chứng minh định lý này bằng quy nạp dựa trên một bất đẳng thức cơ bản dưới đây.

## Bất đẳng thức cơ bản

**Bất đẳng thức then chốt** dùng trong chứng minh hội tụ của Frank-Wolfe là:
> $$f(x^{(k)}) \leq f(x^{(k−1)}) − \gamma_k g(x^{(k−1)}) + \frac{\gamma^2_k}{2}M$$

trong đó $$g(x) = \max_{s\in C} \nabla f(x)^T(x − s)$$ là khoảng cách đối ngẫu đã giới thiệu ở bài trước.

### [Chứng minh]

Đặt $$x^+ = x^{(k)}, x = x^{(k−1)}, s = s^{(k−1)}, \gamma = \gamma_k$$. Khi đó:
> $$\begin{align}
> f(x^+) &= f\bigl( x + \gamma(s − x) \bigr) \\\\
> &\leq f(x) + \gamma\nabla f(x)^T(s − x) + \frac{\gamma^2}{2}M \\\\
> &= f(x) − \gamma g(x) + \frac{\gamma^2}{2}M
> \end{align}$$

Ở đây, bất đẳng thức thứ hai suy trực tiếp từ định nghĩa của $$M$$ và đẳng thức thứ ba suy từ định nghĩa của $$g(x)$$.

Bây giờ, ta dùng bất đẳng thức cơ bản để chứng minh định lý bằng quy nạp.

Với $$k=1$$, định lý dễ dàng kiểm tra là đúng (khi $$\gamma_1 = 1$$, ta có $$f(x^{(1)}) - f^\star \leq f(x^{(0)}) - f^\star - g(x^{(0)}) + \frac{M}{2} \leq \frac{M}{2} \leq \frac{2M}{3}$$).  
Với $$k > 1$$, giả sử theo giả thiết quy nạp rằng $$f(x^{(k−1)}) − f^{\star} \leq 2M/(k + 1)$$.

Nhắc lại hai quan hệ:
> $$g(x^{(k−1)}) \geq f(x^{(k−1)}) − f^{\star}$$
> $$\gamma_k = 2/(k + 1)$$

Áp dụng bất đẳng thức cơ bản:
> $$f(x^{(k)}) \leq f(x^{(k−1)}) − \frac{2}{k + 1}\bigl(f(x^{(k−1)}) − f^{\star}\bigr) + \frac{2M}{(k + 1)^2}$$
> $$f(x^{(k)}) − f^{\star} \leq \Bigl(1 − \frac{2}{k + 1}\Bigr)\bigl(f(x^{(k−1)}) − f^{\star}\bigr) + \frac{2M}{(k + 1)^2}$$
> $$f(x^{(k)}) − f^{\star} \leq \frac{k − 1}{k + 1} \cdot \frac{2M}{k + 1} + \frac{2M}{(k + 1)^2} = \frac{2Mk}{(k + 1)^2} \leq \frac{2M}{k + 2}$$

(Bất đẳng thức trên dùng $$g(x) \geq f(x) − f^{\star}$$ nên $$-\gamma_k g(x^{(k-1)}) \leq -\gamma_k (f(x^{(k-1)}) - f^{\star})$$, và bất đẳng thức cuối đúng vì $$k(k+2) = k^2 + 2k \leq (k+1)^2$$.)

Tốc độ hội tụ $$O(1/k)$$ này trùng với tốc độ của projected gradient descent khi $$\nabla f$$ liên tục Lipschitz.

Hãy so sánh giả thiết của hai phương pháp. Nếu $$\nabla f$$ là $$L$$-Lipschitz thì $$M \leq \text{diam}^2(C) \cdot L$$, trong đó $$\text{diam}^2(C) = \max_{x,s\in C} \|x − s\|_2^2$$. Thật vậy, tính chất $$L$$-Lipschitz của $$\nabla f$$ cho:
> $$f(y) − f(x) − \nabla f(x)^T(y − x) \leq \frac{L}{2} \| y − x \|^2_2$$

Thay $$y = (1-\gamma) x + \gamma s$$, nhân cả hai vế với $$\frac{2}{\gamma^2}$$ và lấy cực đại trên $$C$$:
> $$M \leq \max_{x,s,y\in C,\; y=(1−\gamma)x+\gamma s} \frac{2}{\gamma^2}\cdot\frac{L}{2} \| y − x \|^2_2 = \max_{x,s\in C} L \| x − s \|^2_2$$

Như vậy, điều kiện hằng số độ cong $$M$$ bị chặn không mạnh hơn giả thiết độ trơn Lipschitz dùng trong proximal gradient descent.

## Tính bất biến affine

Nhắc lại hai phương pháp đã học:

* Gradient descent: $$x^+ = x − t\nabla f(x)$$
* Phương pháp Newton thuần túy: $$x^+ = x − \nabla^2f(x)^{−1}\nabla f(x)$$

Gradient descent không bất biến affine (affine invariant), tức tốc độ hội tụ của nó thay đổi khi ta co giãn hệ tọa độ. Ngược lại, phương pháp Newton bất biến affine — hoạt động như nhau dưới mọi phép biến đổi tuyến tính khả nghịch của biến.

Phương pháp gradient có điều kiện (Frank-Wolfe) là phương pháp bậc nhất nhưng lại có **tính bất biến affine**.

Xét một ma trận khả nghịch $$A : \mathbb{R}^n \to \mathbb{R}^n$$ và đặt phép đổi biến $$x = Ax',\; h(x') = f(Ax')$$. Khi áp dụng Frank-Wolfe cho $$h(x')$$ trên tập $$A^{-1}C$$:

> $$\begin{array}{rcl}
> s' & = & \arg\min_{z\in A^{−1}C} \nabla h(x')^Tz \\\\
> (x')^+ & = & (1 − \gamma)x' + \gamma s'
> \end{array}$$

Nhân hai vế với $$A$$ ta thu được chính xác bước cập nhật Frank-Wolfe trên $$f(x)$$ và tập $$C$$. Hơn nữa, ngay cả phân tích hội tụ cũng bất biến affine vì hằng số độ cong $$M$$ của $$h$$:
> $$M = \max_{x',s',y'\in A^{−1}C,\; y'=(1−\gamma)x'+\gamma s'} \frac{2}{\gamma^2} \Bigl( h(y') − h(x') − \nabla h(x')^T(y' − x') \Bigr)$$

bằng đúng hằng số độ cong của $$f$$ do $$\nabla h(x')^T(y' − x') = \nabla f(x)^T(y − x)$$.

Tuy nhiên, tính bất biến affine không thể hiện rõ trong cận trên:
> $$M \leq \max_{x,s\in C} L\|x − s\|^2_2$$

vì đường kính của tập $$C$$ (theo chuẩn Euclid) không bất biến affine.

## Cập nhật không chính xác

Trường hợp bài toán con tuyến tính được giải gần đúng cũng đã được phân tích trong [Jaggi (2011)]. Giả sử tại bước $$k$$, ta chọn $$s^{(k−1)} \in C$$ sao cho:
> $$\nabla f(x^{(k−1)})^Ts^{(k−1)} \leq \min_{s\in C} \nabla f(x^{(k−1)})^Ts + \frac{M\gamma_k}{2} \cdot \delta$$

trong đó $$\delta \geq 0$$ là tham số sai số. Khi đó tốc độ hội tụ thu được là:

> **Định lý:** Phương pháp gradient có điều kiện với kích thước bước cố định $$\gamma_k=2/(k+1)$$ ($$k=1,2,3,\ldots$$) và tham số sai số $$\delta \geq 0$$ thỏa mãn:
> $$f(x^{(k)}) − f^{\star} \leq \frac{2M}{k + 2} (1 + \delta)$$

Lưu ý rằng ngưỡng sai số cho phép ở bước $$k$$ là $$\frac{M\gamma_k}{2} \cdot \delta$$. Vì $$\gamma_k \to 0$$, yêu cầu về độ chính xác của bộ giải bài toán con cần siết chặt dần theo thời gian.
