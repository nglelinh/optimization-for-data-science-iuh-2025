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

## Phân tích hội tụ
Để tìm hiểu các đặc tính hội tụ của phương pháp Frank-Wolfe, cần định nghĩa hằng số độ cong (curvature constant) của $$f$$ đối với $$C$$ như sau. [Jaggi (2011)]
> $$M = \max_{x,s,y∈C, y = (1−γ)x+γs} \frac{2}{γ^2} \Bigl( f(y) − f(x) − ∇f(x)^T(y − x) \Bigr)$$
> $$γ ∈ [0, 1]$$

Thông qua $$M$$, ta có thể đo mức độ mà hàm $$f$$ lệch khỏi xấp xỉ tuyến tính (linear approximation) của nó.
Ở đây $$M = 0$$ nghĩa là $$f$$ tuyến tính. Đại lượng $$f (y) - f (x) - ∇f (x)^T(y - x)$$ được gọi là độ phân kỳ Bregman (Bregman divergence) xác định bởi $$f$$.

> Định lý: Phương pháp gradient có điều kiện (conditional gradient method) với kích thước bước cố định $$γ_k = 2 / (k + 1), k = 1,2,3, ...$$ thỏa mãn
>  $$f(x^{(k)}) − f^{\star} ≤ \frac{2M}{k + 2}$$

Do đó, số vòng lặp cần thiết để đạt $$f(x^{(k)}) − f^{\star} ≤ \epsilon$$ là $$O(1/\epsilon)$$.

Ta sẽ chứng minh định lý này bằng quy nạp. Tuy nhiên, trước khi vào chứng minh, cần giới thiệu một khái niệm.

## Bất đẳng thức cơ bản
**Bất đẳng thức then chốt** dùng để chứng minh tốc độ hội tụ của Frank-Wolfe như sau:
> $$f(x^{(k)}) ≤  f(x^{(k−1)}) − γ_kg(x^{(k−1)}) + \frac{γ^2_k}{2}M$$

Ở đây $$g(x) = \max_{s∈C} ∇f(x)^T(x − s)$$ là khoảng cách đối ngẫu (duality gap) đã thảo luận trước đó; ta sẽ dùng bất đẳng thức này trong chứng minh quy nạp.

### [Chứng minh]
Để chứng minh bất đẳng thức cơ bản, đặt $$x^+ = x^{(k)}, x = x^{(k−1)}, s = s^{(k−1)}, γ = γ_k$$. Khi đó ta có:
> $$\begin{align}
> f(x^+) &= f\bigl( x + γ(s − x) \bigr) \\\\
> &≤ f(x) + γ∇f(x)^T(s − x) + \frac{γ^2}{2}M \\\\
> &= f(x) − γg(x) + \frac{γ^2}{2}M
> \end{align}$$

Trong phương trình trên, dòng thứ hai dùng định nghĩa của $$M$$, còn dòng thứ ba dùng định nghĩa của $$g$$.

Bây giờ, dùng bất đẳng thức cơ bản, ta chứng minh định lý về tốc độ hội tụ bằng quy nạp.

Với $$k=1$$, dễ dàng kiểm tra định lý thỏa mãn.
Với $$k > 1$$ bất kỳ, giả sử $$f(x^{(k−1)}) − f^{\star} ≤ 2M/(k + 1)$$.

Hãy nhớ lại khoảng cách đối ngẫu $$g(x)$$ nói trên.
> $$g(x^{(k−1)}) ≥ f(x^{(k−1)}) − f^{\star}$$
> $$γ_k = 2/(k + 1)$$

Bây giờ áp dụng bất đẳng thức cơ bản.
> $$f(x^{(k)}) ≤ f(x^{(k−1)}) − \frac{2}{k + 1}\bigl(f(x^{(k−1)}) − f^{\star}\bigr) + \frac{2M}{(k + 1)^2}$$
> $$f(x^{(k)}) − f^{\star} ≤ \Bigl(1 − \frac{2}{k + 1}\Bigr)\bigl(f(x^{(k−1)}) − f^{\star}\bigr) + \frac{2M}{(k + 1)^2}$$
> $$f(x^{(k)}) − f^{\star} ≤ \frac{k − 1}{k + 1} · \frac{2M}{k + 1} + \frac{2M}{(k + 1)^2} = \frac{2Mk}{(k + 1)^2} ≤ \frac{2M}{k + 2} $$

(Ở đây ta dùng $$g(x) ≥ f(x) − f^{\star}$$, nên $$-γ_k g(x^{(k-1)}) ≤ -γ_k (f(x^{(k-1)}) - f^{\star})$$, và bất đẳng thức cuối đúng vì $$k(k+2) ≤ (k+1)^2$$.)

Tốc độ hội tụ đã chứng minh này khớp với tốc độ đã biết của projected gradient descent khi $$∇f$$ là Lipschitz.

Bây giờ hãy so sánh các giả thiết này.
Thật vậy, nếu $$∇f$$ là Lipschitz với hằng số $$L$$ thì $$M ≤ diam^2(C) · L$$, trong đó $$diam^2(C) = max_{x,s∈C} ||x − s||^2$$.

Để kiểm tra điều này, cần nhớ rằng $$∇f$$ Lipschitz với hằng số $$L$$ tương đương với bất đẳng thức sau.
> $$f(y) − f(x) − ∇f(x)^T(y − x) ≤ \frac{L}{2} \| y − x \|^2_2$$

Lấy cực đại trên mọi $$y = (1-γ) x + γs$$ và nhân với $$\frac{2}{γ^2}$$ ta được:
> $$M ≤ \max_{x,s,y∈C, y=(1−γ)x+γs} \frac{2}{γ^2}·\frac{L}{2} \| y − x \|^2_2 = \max_{x,s∈C} L \| x − s \|^2_2$$

Như vậy ta đã có một cận cho $$M$$. Về cơ bản, độ cong bị chặn ở đây không lớn hơn độ cong được giả định cho proximal gradient.

## Tính bất biến affine
Hãy nhớ lại các khái niệm đã học.

* Gradient Descent: $$x^+ = x − t∇f(x)$$
* Phương pháp Newton thuần túy: $$x^+ = x − ∇^2f(x)^{−1}∇f(x)$$

Gradient descent không bất biến affine (affine invariant). Nghĩa là, hiệu năng của gradient descent có thể được cải thiện bằng cách co giãn các tọa độ. Ngược lại, phương pháp Newton bất biến affine. Nghĩa là thuật toán này hoạt động như nhau dưới mọi phép biến đổi affine của biến.

Phương pháp gradient có điều kiện tương tự gradient descent nhưng bất biến affine.

Tính chất quan trọng của Frank-Wolfe: bước cập nhật **bất biến affine**.
Cho ma trận không suy biến $$A : \mathbb{R}^n → \mathbb{R}^n$$, ta có thể định nghĩa $$x = Ax', h(x') = f(Ax')$$.
Khi đó Frank-Wolfe trên $$h(x')$$ có thể được tính như sau.

> $$\begin{array}{rcl}
> s' & = & \arg\min_{z∈A^{−1}C} ∇h(x')^Tz \\\\
> (x')^+ & = & (1 − γ)x' + γs'
> \end{array}$$

Nhân với $$A$$ ta được đúng bước cập nhật Frank-Wolfe thực hiện trên $$f (x)$$.
Thậm chí phân tích hội tụ cũng bất biến affine.

Hằng số độ cong $$M$$ của $$h$$ như sau.
> $$M = \max_{x',s',y'∈A^{−1}C, y'=(1−γ)x'+γs'} \frac{2}{γ^2} \Bigl( h(y') − h(x') − ∇h(x')^T(y' − x') \Bigr)$$

Nó trùng với của $$f$$ vì $$∇h(x')^T(y' − x') = ∇f(x)^T(y − x)$$.

Tuy nhiên, tính bất biến affine không hiển nhiên trong cận của $$M$$.
> $$M ≤ \max_{x,s∈C} L||x − s||^2_2$$

Vì đường kính của $$C$$ không bất biến affine, đây là điều đáng suy ngẫm thêm.

## Cập nhật không chính xác
Các cập nhật Frank-Wolfe không chính xác cũng đã được phân tích. [Jaggi (2011)]</br>
Chọn $$s^{(k−1)}$$ sao cho
> $$∇f(x^{(k−1)})^Ts^{(k−1)} ≤ \min_{s∈C} ∇f(x^{(k−1)})^Ts + \frac{Mγ_k}{2} · δ$$

trong đó $$δ ≥ 0$$ là tham số không chính xác. Dùng điều này, ta thu được tốc độ như sau.

> Định lý: Phương pháp gradient có điều kiện với kích thước bước cố định $$γ_k=2/(k+1),k=1,2,3, ... $$ và tham số không chính xác $$δ≥0$$ thỏa mãn
> $$f(x^{(k)}) − f^{\star} ≤ \frac{2M}{k + 2} (1 + δ)$$

Lưu ý: Sai số tối ưu hóa ở bước $$k$$ là $$\frac{Mγ_k}{2} · δ.$$ Vì $$γ_k → 0$$, ý đồ là sai số biến mất dần theo thời gian.
