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

Nếu bạn có một bài toán với $$100$$ biến nhị phân, tổng số tổ hợp lên tới $$2^{100} \approx 1.26 \times 10^{30}$$ — nhiều hơn số nguyên tử trong một ngọn núi. Vét cạn là bất khả thi. Thế nhưng thuật toán **Nhánh và Cận (Branch and Bound)**, được Ailsa Land và Alison Doig giới thiệu năm 1960, vẫn thường xuyên giải chính xác những bài toán hàng chục nghìn biến chỉ trong vài giây.

Bí quyết của Nhánh và Cận nằm ở hai chữ **cắt tỉa (pruning)**: thay vì đi xuống tận đáy của mọi nhánh cây, ta giải nhanh bài toán nới lỏng lồi tại mỗi nút để lấy cận dưới; ngay khi thấy cận dưới của một nhánh đã tệ hơn (hoặc bằng) nghiệm nguyên tốt nhất đang giữ trong tay, ta lập tức chém phăng cả nhánh cây hàng tỷ nút phía dưới đó mà không bỏ sót nghiệm tối ưu!

## Kiến thức cần nhớ: Ba trụ cột điều khiển cây Nhánh và Cận

Khi theo dõi một cây Nhánh và Cận, mọi thao tác ở mỗi nút đều quy về ba quy tắc rõ ràng:

- **Quy tắc phân nhánh (Branching):** Khi nghiệm nới lỏng $$x^\star$$ tại một nút còn chứa thành phần phân số $$x_j^\star \notin \mathbb{Z}$$ (với $$j \in J$$), ta tách nút đó thành hai bài toán con loại trừ hoàn toàn điểm phân số này: nhánh trái thêm $$x_j \le \lfloor x_j^\star \rfloor$$ và nhánh phải thêm $$x_j \ge \lceil x_j^\star \rceil$$. Hợp của hai nhánh vẫn phủ trọn mọi điểm nguyên khả thi.
- **Ba điều kiện cắt tỉa (Fathoming / Pruning Rules):** Một nút con được đóng lại ngay lập tức (không cần phân nhánh tiếp) nếu rơi vào một trong ba trường hợp: (1) *Vô nghiệm* (bài toán nới lỏng không có nghiệm); (2) *Cắt theo cận* (cận dưới $$l(X_i) \ge u$$, không thể tốt hơn kỷ lục hiện tại); hoặc (3) *Nghiệm nguyên* (nghiệm nới lỏng tự động nguyên — lúc này ta cập nhật kỷ lục $$u \leftarrow \min(u, l(X_i))$$).
- **Chiến lược duyệt cây (Node & Variable Selection):** Chọn nút nào mở tiếp (duyệt sâu để sớm tìm nghiệm khả thi hạ $$u$$, hay duyệt nút có cận dưới nhỏ nhất *best-first* để nhanh nâng cận toàn cục) và chọn biến phân số nào để rẽ nhánh quyết định trực tiếp kích thước cây tìm kiếm.

### Giải thích: Chạy tay trọn vẹn một cây Nhánh và Cận

Hãy tự tay giải bài toán quy hoạch nguyên cực tiểu hóa:

$$
\min_{x_1, x_2 \in \mathbb{Z}_+}\ -5x_1 - 4x_2 \qquad \text{thỏa mãn } 2x_1 + 2x_2 \le 5.
$$

Khởi tạo kỷ lục (cận trên toàn cục) $$u = +\infty$$.

1. **Nút gốc $$N_0$$ (chưa thêm ràng buộc nhánh):**
   Giải nới lỏng LP: vì hệ số $$-5 < -4$$, dồn hết vào $$x_1$$ cho ra $$x^{(0)} = (2.5,\; 0)$$, cận dưới $$l(N_0) = -12.5$$.
   Vì $$x_1 = 2.5$$ là số phân số, ta rẽ nhánh thành $$N_1: x_1 \le 2$$ và $$N_2: x_1 \ge 3$$.
2. **Nút $$N_2$$ ($$x_1 \ge 3$$):**
   Ràng buộc $$2x_1 + 2x_2 \le 5$$ với $$x_1 \ge 3, x_2 \ge 0$$ cho $$6 \le 5$$ — **Vô nghiệm → Cắt tỉa (infeasibility)!**
3. **Nút $$N_1$$ ($$x_1 \le 2$$):**
   Giải LP trên $$2x_1 + 2x_2 \le 5,\; x_1 \le 2$$: lấy tối đa $$x_1 = 2$$, phần dư cho $$x_2 = 0.5$$. Nghiệm $$x^{(1)} = (2,\; 0.5)$$, cận dưới $$l(N_1) = -5(2) - 4(0.5) = -12$$.
   Vì $$x_2 = 0.5$$ phân số, rẽ nhánh thành $$N_{1a}: x_2 \le 0$$ và $$N_{1b}: x_2 \ge 1$$.
4. **Nút $$N_{1a}$$ ($$x_1 \le 2,\; x_2 \le 0$$):**
   LP cho nghiệm $$x = (2, 0)$$ — **toàn số nguyên!** Giá trị bằng $$-10$$. Cập nhật kỷ lục $$u = -10$$ và **Cắt tỉa (integrality)**.
5. **Nút $$N_{1b}$$ ($$x_1 \le 2,\; x_2 \ge 1$$):**
   Từ $$2x_1 + 2(1) \le 5 \Rightarrow x_1 \le 1.5$$. Nghiệm LP là $$(1.5, 1)$$ với $$l(N_{1b}) = -7.5 - 4 = -11.5 < -10$$ (chưa cắt được vì còn hy vọng!). Rẽ nhánh trên $$x_1$$:
   - $$N_{1b1}$$ ($$x_1 \ge 2, x_2 \ge 1$$): $$2(2)+2(1) = 6 > 5$$ — **Vô nghiệm → Cắt tỉa!**
   - $$N_{1b2}$$ ($$x_1 \le 1, x_2 \ge 1$$): LP cho nghiệm nguyên $$(1, 1)$$ với giá trị $$-9 \ge u = -10$$ — **Cắt tỉa (theo cận)!**
6. **Kết luận:** Hết nút mở! Nghiệm tối ưu được chứng nhận chắc chắn là $$x^\star = (2, 0)$$ với giá trị $$-10$$. Cả ba quy tắc cắt tỉa (vô nghiệm, nguyên, theo cận) đều đã hoạt động nhịp nhàng!

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

### Nhánh và cận từng bước (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/branch-bound_vi.mp4"></video>
</div>

Thuật toán giải LP nới lỏng, rẽ nhánh theo một biến đang nhận giá trị phân số, và cắt bỏ mọi nút có cận dưới không thể cải thiện nghiệm nguyên tốt nhất đã tìm được.

Lưu ý: video giải bài toán dạng cực đại ($$\max\ 5x_1 + 4x_2$$), còn bài viết dùng dạng cực tiểu. Hai dạng tương đương vì $$\max_x c^Tx = -\min_x (-c^Tx)$$. Khi làm với dạng cực đại, hai cận đổi vai: giá trị LP nới lỏng ở mỗi nút là cận **trên**, nghiệm nguyên tốt nhất đã có là cận **dưới**, và nút bị cắt tỉa khi cận trên của nó không vượt được nghiệm nguyên tốt nhất.

### Tự tay thử: duyệt qua nhánh và cận

<div class="opx-explainer" data-opx="bnb" data-lang="vi"></div>
