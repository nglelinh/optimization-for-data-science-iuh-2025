---
layout: post
title: 18-01 Phương trình Secant và Điều kiện Độ cong
chapter: '18'
order: '2'
owner: Hooncheol Shin
categories:
- chapter18
lang: vi
---

# Phương trình Secant

Như đã trình bày ở phần trước, $$B$$ là ma trận xấp xỉ Hessian $$\nabla^2 f(x)$$. Để $$B$$ mang các tính chất tương tự Hessian thực, nó cần thỏa mãn một điều kiện gọi là **phương trình secant (secant equation)**.

Với $$x^{k+1} = x^k + s^k$$ và $$f$$ khả vi hai lần, khai triển Taylor bậc nhất của $$\nabla f(x^k + s^k)$$ cho thấy Hessian thực thỏa mãn xấp xỉ:

>$$
\nabla f(x^k + s^k) \approx \nabla f(x^k) + \nabla^2 f(x^k) s^k$$

Thay $$\nabla^2 f(x^k)$$ bằng ma trận xấp xỉ mới $$B^{k+1}$$, ta yêu cầu phương trình sau được thỏa mãn chính xác:

>$$
\nabla f(x^k + s^k) = \nabla f(x^k) + B^{k+1} s^k$$

Đặt $$s^k = x^{k+1} - x^k$$ và $$y^k = \nabla f(x^{k+1}) - \nabla f(x^k)$$, phương trình trên được viết gọn thành **phương trình secant**:

>$$
B^{k+1} s^k = y^k
$$

# Ý nghĩa hình học của phương trình Secant

Trong trường hợp một chiều với $$x$$ là trục hoành và $$\nabla f(x)$$ là trục tung, $$B^{k+1}$$ chính là hệ số góc của cát tuyến đi qua hai điểm $$(x^k, \nabla f(x^k))$$ và $$(x^{k+1}, \nabla f(x^{k+1}))$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter18/intuition_of_secant_eq.png" alt="[Fig1] Trực quan về phương trình secant" width="70%">
  <figcaption style="text-align: center;">[Fig1] Trực quan về phương trình secant</figcaption>
</p>
</figure>

# Các điều kiện xác định $$B^+$$

Từ ma trận $$B$$ hiện tại, ta đặt ra ba yêu cầu để xác định ma trận cập nhật $$B^+$$:

1. **$$B^+$$ đối xứng:** Phản ánh tính đối xứng của ma trận Hessian.
2. **$$B^+$$ gần $$B$$ nhất:** Giúp xác định duy nhất $$B^+$$. Vì $$B$$ đã tích lũy thông tin độ cong từ các bước trước, ta chọn ma trận gần $$B$$ nhất (theo một chuẩn thích hợp) trong số các ma trận thỏa mãn phương trình secant.
3. **Bảo toàn tính xác định dương ($$B \succ 0 \Rightarrow B^+ \succ 0$$):** Đảm bảo hướng cập nhật $$p = -(B^+)^{-1}\nabla f(x)$$ luôn là hướng giảm của hàm mục tiêu (tham khảo: [Phân tích Hessian](https://web.stanford.edu/group/sisl/k12/optimization/MO-unit4-pdfs/4.10applicationsofhessians.pdf)).

# Điều kiện độ cong (Curvature Condition)

Nếu $$B^+$$ xác định dương và thỏa mãn phương trình secant $$B^+ s = y$$, thì nhất thiết phải có:

>$$
s^T y = s^T B^+ s > 0.
$$

(tham khảo: [Ma trận xác định dương trên Wikipedia](https://en.wikipedia.org/wiki/Positive-definite_matrix))

Bất đẳng thức $$s^T y > 0$$ được gọi là **điều kiện độ cong (curvature condition)**. Khi điều kiện này thỏa mãn (và $$s \neq 0$$), luôn tồn tại ma trận đối xứng xác định dương $$B^+$$ thỏa mãn phương trình secant $$B^+ s = y$$.