---
layout: post
title: '24-05 Thuật toán nhánh và cận (B&B)'
chapter: '24'
order: 6
owner: YoungJae Choung
categories:
- chapter24
lang: vi
---

Mục này trình bày cách giải bài toán quy hoạch nguyên bằng thuật toán nhánh và cận (Branch and Bound) kết hợp với nới lỏng lồi.

## Định nghĩa và nguyên lý

Nhánh và cận là thuật toán tiêu chuẩn và phổ biến nhất để giải chính xác quy hoạch nguyên. Về bản chất, đây là chiến lược chia để trị: phân hoạch bài toán gốc thành các bài toán con nhỏ hơn và loại bỏ sớm những nhánh không thể chứa nghiệm tối ưu.

Nếu tập khả thi được phân hoạch thành $$X = X_{1} \cup X_{2} \cup \dotsc \cup X_{k}$$, thì:
> $$ \min_{x \in X} f(x) = \min_{i = 1, \dotsc , k} \lbrace \min_{x \in X_{i}} f(x) \rbrace .$$

Bất kỳ nghiệm khả thi nào tìm được đều cung cấp một cận trên toàn cục $$u(X)$$. Với mỗi bài toán con trên $$X_i$$, ta tính một cận dưới $$l(X_i)$$. Nếu $$l(X_i) \geq u(X)$$, bài toán con $$\min_{x \in X_i} f(x)$$ chắc chắn không thể cải thiện nghiệm tốt nhất hiện có nên có thể cắt tỉa (loại bỏ) hoàn toàn.

Xét bài toán quy hoạch nguyên (IP):

> $$
> \begin{align}
> &\min_{x} &&f(x) \\\\
> &\text{subject to } && x \in C \\\\
> &&&x_j \in \mathbb{Z}, \quad j \in J
> \end{align}$$
> $$\begin{align}
> \text{trong đó } f \text{ lồi, } f : \mathbb{R}^{n} \rightarrow \mathbb{R}, \quad C \subseteq \mathbb{R}^n 
> \quad \text{và} \quad J \subseteq \lbrace 1, \dotsc, n \rbrace
> \end{align}
> $$

và bài toán nới lỏng lồi tương ứng (CR):

> $$
> \begin{align}
> &\min_{x} &&f(x) \\\\
> &\text{subject to } &&x \in C
> \end{align}$$
> $$\begin{align}
> \text{trong đó } f \text{ lồi, } f : \mathbb{R}^{n} \rightarrow \mathbb{R}, \quad C \subseteq \mathbb{R}^n.
> \end{align}
> $$

Thuật toán nhánh và cận giải đệ quy trên từng nút bài toán con theo quy trình sau:

* Giải bài toán nới lỏng (CR) tại nút hiện tại:
  * Nếu (CR) vô nghiệm thì (IP) trên nhánh này cũng vô nghiệm — dừng (cắt tỉa).
  * Nếu nghiệm $$x^{\star}$$ của (CR) đã thỏa mãn toàn bộ ràng buộc nguyên của (IP) thì $$x^{\star}$$ là nghiệm tối ưu cục bộ của nhánh; cập nhật cận trên toàn cục nếu $$f(x^{\star})$$ nhỏ hơn cận trên hiện tại, rồi dừng.
* Nếu $$x^{\star}$$ chưa nguyên, giá trị tối ưu của (CR) cung cấp cận dưới cho nhánh hiện tại.
* Nếu cận dưới này lớn hơn hoặc bằng cận trên toàn cục hiện có — dừng (cắt tỉa).
* Ngược lại, chia tập ràng buộc (thường bằng cách rẽ nhánh trên một biến nguyên $$x_j$$ đang nhận giá trị phân số: $$x_j \leq \lfloor x_j^\star \rfloor$$ và $$x_j \geq \lceil x_j^\star \rceil$$) rồi giải đệ quy từng bài toán con.

## Xử lý sau khi phân nhánh

* Sau khi phân nhánh, từng bài toán con được giải và đánh giá theo cùng quy tắc trên.
* Bất kỳ bài toán con nào có cận dưới lớn hơn hoặc bằng cận trên hiện tại đều bị cắt tỉa mà không cần phân nhánh thêm.
* Nới lỏng lồi là cách phổ biến và đáng tin cậy nhất để tính cận dưới, bên cạnh các lựa chọn khác như nới lỏng Lagrange.

### Nhánh và cận trong 18 giây

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/branch-bound_vi.mp4"></video>
</div>

Thuật toán giải LP nới lỏng, rẽ nhánh theo một biến đang nhận giá trị phân số, và cắt bỏ mọi nút có cận dưới không thể cải thiện nghiệm nguyên tốt nhất đã tìm được.

### Tự tay thử: duyệt qua nhánh và cận

<div class="opx-explainer" data-opx="bnb" data-lang="vi"></div>
