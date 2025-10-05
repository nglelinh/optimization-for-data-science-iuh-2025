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

Như đã đề cập trước đó, $$B$$ là một ma trận xấp xỉ $$\nabla^2 f(x)$$. Để ma trận $$B$$ có các tính chất tương tự như Hessian $$\nabla^2 f(x)$$, nó phải thỏa mãn một điều kiện gọi là phương trình secant.

Khi $$x^{k+1} = x^k + s^k$$ và $$f$$ khả vi hai lần, khai triển Taylor bậc nhất của $$\nabla f(x^k + s^k)$$ cho thấy Hessian thực có tính chất sau.

>$$
\nabla f(x^k + s^k) \approx \nabla f(x^k) + \nabla^2 f(x^k) s^k$$

Ở đây, chúng ta gọi ma trận xấp xỉ của $$\nabla^2 f(x^k)$$ là $$B^{k+1}$$. Ma trận này thỏa mãn phương trình sau.

>$$
\nabla f(x^k + s^k) = \nabla f(x^k) + B^{k+1} s^k$$

Nếu $$x^{k+1} = x^k + s^k, y^k = \nabla f(x^{k + 1}) - \nabla f(x^k)$$, thì phương trình trên có thể được viết lại như sau, và đây được gọi là phương trình secant.

>$$
B^{k+1} s^k = y^k
$$

# Trực quan về Phương trình Secant

Khi $$x$$ là trục hoành và $$\nabla f(x)$$ là trục tung, $$B^{k+1}$$ bằng hệ số góc của đường thẳng đi qua hai điểm $$(x^k, \nabla f(x^k))$$ và $$(x^{k+1}, \nabla f(x^{k+1}))$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter18/intuition_of_secant_eq.png" alt="[Fig1] Trực quan về phương trình secant" width="70%">
  <figcaption style="text-align: center;">[Fig1] Trực quan về phương trình secant</figcaption>
</p>
</figure>

# Các điều kiện để xác định $$B^+$$

Dựa trên ma trận $$B$$ hiện tại, có ba điều kiện để tính toán $$B^+$$ tiếp theo.

1. $$B^+$$ là ma trận đối xứng: Vì nó là một xấp xỉ của Hessian.
2. $$B^+$$ gần với $$B$$: Một điều kiện để xác định duy nhất $$B^+$$. Vì $$B$$ đã chứa thông tin hữu ích, chúng ta chọn ma trận gần nhất với $$B$$ trong số các $$B^+$$ thỏa mãn phương trình secant.
3. $$B$$ là xác định dương $$\Rightarrow B^+$$ là xác định dương: Để đảm bảo tối ưu toàn cục, chúng ta duy trì tính lồi của bài toán. (tham khảo: [Phân tích hessian](https://web.stanford.edu/group/sisl/k12/optimization/MO-unit4-pdfs/4.10applicationsofhessians.pdf))

# Điều kiện Độ cong

Việc $$B^+$$ là xác định dương và $$B^+ s = y$$ hàm ý sự thật sau.

>$$
s^T y = s^T B^+ s > 0.
$$

(tham khảo: [Ma trận xác định dương trên WikiPedia](https://en.wikipedia.org/wiki/Positive-definite_matrix))

Ở đây, $$s^T y > 0$$ được gọi là điều kiện độ cong. Nếu điều kiện độ cong được thỏa mãn, phương trình secant $$B^+ s = y$$ luôn có nghiệm ($$B^+$$).