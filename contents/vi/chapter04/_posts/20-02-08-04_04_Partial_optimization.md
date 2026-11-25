---
layout: post
title: 04-04 Tối ưu hóa từng phần
chapter: '04'
order: 5
owner: YoungJae Choung
categories:
- chapter04
lang: vi
---

Khi giải một câu đố nhiều tầng, chiến lược tự nhiên nhất của con người là "chia để trị": tạm coi một nhóm biến là cố định, tìm phương án tốt nhất cho nhóm biến còn lại, rồi thay kết quả đó ngược trở lại vào bài toán ban đầu. Trong đại số thông thường, phép thế này luôn hợp lệ; nhưng trong tối ưu hóa lồi, một câu hỏi sống còn hiện ra: *sau khi tối ưu hóa trước một phần biến, bài toán rút gọn có còn giữ được tính lồi hay không?*

May mắn thay, định lý bảo toàn tính lồi qua phép lấy cực tiểu từng phần trả lời là **CÓ** — miễn là hàm gốc lồi *đồng thời* theo cả hai nhóm biến $$(x, y)$$ và miền của $$y$$ là lồi. Phép biến đổi tưởng chừng đơn giản này chính là cây cầu biến đổi bài toán SVM biên mềm kinh điển từ dạng có hàng nghìn biến phụ $$\xi_i$$ thành dạng không ràng buộc với **hàm mất mát bản lề (hinge loss)** quen thuộc trong mọi thư viện học máy hiện đại.

## Bản đồ kiến thức nền: Cơ chế "rút gọn biến" mà vẫn bảo toàn tính lồi

Ba trụ cột sau giải thích khi nào tối ưu hóa từng phần hoạt động và tại sao nó lại mạnh mẽ đến vậy:

- **Tính lồi đồng thời (Joint Convexity):** Điều kiện tiên quyết là $$f(x, y)$$ phải lồi đồng thời theo cặp $$(x, y)$$, chứ không chỉ lồi riêng lẻ theo $$x$$ và riêng lẻ theo $$y$$ (ví dụ $$f(x,y) = xy$$ lồi theo từng biến nhưng không lồi đồng thời!).
- **Phép chiếu trên đồ thị (Epigraph Projection):** Hình học của $$g(x) = \inf_{y \in C} f(x, y)$$ cực kỳ trong sáng: tập trên đồ thị của $$g$$ chính là hình chiếu của tập trên đồ thị của $$f$$ (một tập lồi) xuống không gian của $$(x, t)$$. Vì phép chiếu tuyến tính bảo toàn tính lồi, $$g(x)$$ lập tức thừa hưởng tính lồi.
- **Đánh đổi giữa "nhiều biến – hàm trơn" và "ít biến – hàm không trơn":** Khi bạn khử biến phụ $$\xi_i$$ trong SVM bằng tối ưu hóa từng phần, số biến giảm mạnh nhưng hàm mục tiêu chuyển từ hàm tuyến tính trơn thành hàm $$\max(0, \cdot)$$ không khả vi. Ngược lại, đọc công thức theo chiều ngược lại chính là cách "làm trơn" một hàm cực đại bằng cách thêm biến phụ!

### Khung giải thích (nên đọc chậm): Tính tay hàm rút gọn $$g(x)$$ và kiểm chứng trên một ví dụ SVM mini

Xét bài toán lồi đồng thời theo $$(w, \xi) \in \mathbb{R} \times \mathbb{R}$$:
$$\min_{w, \xi} \; \frac{1}{2} w^2 + 2\xi \quad \text{thỏa mãn} \quad \xi \ge 0,\quad \xi \ge 1 - 2w.$$

1. **Bước 1 — Cố định $$w$$, tối ưu hóa theo biến phụ $$\xi$$:**
   Hai ràng buộc $$\xi \ge 0$$ và $$\xi \ge 1 - 2w$$ gộp lại thành $$\xi \ge \max(0, 1 - 2w)$$.
   Vì hệ số của $$\xi$$ trong hàm mục tiêu là $$+2 > 0$$, muốn cực tiểu hóa $$2\xi$$ ta phải chọn $$\xi$$ nhỏ nhất có thể:
   $$\xi^\star(w) = \max(0, 1 - 2w).$$
2. **Bước 2 — Thay $$\xi^\star(w)$$ vào bài toán gốc:**
   Ta thu được bài toán hoàn toàn không ràng buộc chỉ còn 1 biến $$w$$:
   $$\min_{w \in \mathbb{R}} \; g(w) = \frac{1}{2} w^2 + 2\max(0, 1 - 2w).$$
3. **Bước 3 — Giải bài toán rút gọn theo từng khoảng:**
   - Nếu $$w \ge 0.5$$: $$\max(0, 1-2w) = 0 \implies g(w) = \frac{1}{2}w^2$$, đạt cực tiểu trên $$[0.5, \infty)$$ tại $$w = 0.5$$ với $$g(0.5) = 0.125$$.
   - Nếu $$w < 0.5$$: $$g(w) = \frac{1}{2}w^2 + 2 - 4w$$. Đạo hàm $$g'(w) = w - 4 < 0$$ với mọi $$w < 0.5$$, nên hàm giảm nghiêm ngặt đến sát $$w = 0.5$$.
4. **Kết luận & Kiểm tra ngược:** Nghiệm tối ưu là $$w^\star = 0.5$$, kéo theo $$\xi^\star = \max(0, 1 - 2(0.5)) = 0$$, và giá trị tối ưu $$g^\star = 0.125$$. Phép tối ưu từng phần đã thu gọn bài toán 2 biến có 2 ràng buộc bất đẳng thức về đúng một hàm 1 biến lồi!

---

[Nhắc lại:]({% multilang_post_url contents/chapter03/21-02-12-03_02_operations_that_preserve_convexity %})
Nếu $$C$$ là tập lồi và $$f$$ là hàm lồi đồng thời theo $$(x, y)$$, thì hàm $$g(x) = \min_{y \in C} f(x, y)$$ là hàm lồi theo $$x$$.

Do đó, phép tối ưu hóa từng phần trên một tập con các biến trong bài toán tối ưu hóa lồi vẫn bảo toàn tính lồi.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter04/partial-optimization.png" alt="[Fig1] partial optimization of a convex problem [3]">
  <figcaption style="text-align: center;">[Hình 1] Tối ưu hóa từng phần của một bài toán lồi [3]</figcaption>
</p>
</figure>
<br>

### Ví dụ: Dạng hàm mất mát hinge của SVM
Đối với tập dữ liệu không tách tuyến tính được, bài toán máy vectơ hỗ trợ (SVM) biên mềm được phát biểu như sau:
>$$
\begin{aligned}
&\min_{\beta, \beta_{0}, \xi} &&\frac{1}{2}\|\beta\|_2^2 + C \sum_{i=1}^{n} \xi_{i} \\
&\text{subject to} &&{\xi}_{i} \ge 0, \\ 
&&&y_{i}(x_{i}^T \beta + \beta_{0}) \ge 1 - {\xi}_{i}, \\
&&&i = 1, \dotsc, n. \\
\end{aligned}
$$

Hai nhóm ràng buộc trên có thể gộp lại thành một ràng buộc duy nhất theo $$\xi_i$$:
> $$
\begin{aligned}
{\xi}_{i} \ge \max\{0, 1 - y_{i} (x_{i}^T \beta + \beta_{0})\} \\
\end{aligned}
$$

Với mỗi cặp $$(\beta, \beta_0)$$ cố định, giá trị nhỏ nhất có thể của $$\xi_{i}$$ chính là $$\max\{0, 1 - y_{i} (x_{i}^T \beta + \beta_{0})\}$$. Khi tối ưu hóa riêng theo biến $$\xi$$, ta định nghĩa hàm mục tiêu rút gọn $$\tilde{f}$$ như sau:

> $$
\begin{aligned}
\frac{1}{2} \|\beta\|_{2}^{2} + C \sum_{i=1}^{n} {\xi}_{i} &\ge \frac{1}{2} \|\beta\|_{2}^{2} + C \sum_{i=1}^{n} \max({0, 1 - y_{i} (x_{i}^T \beta + \beta_{0})})\\
&= \min\left\{\frac{1}{2} \|\beta\|_{2}^{2} + C \sum_{i=1}^{n} \xi_{i} \;\middle|\; \xi_{i} \ge 0, \ y_{i}(x_{i}^T \beta + \beta_{0}) \ge 1 - \xi_{i}, \ i = 1, \dotsc, n\right\} \\
&= \tilde{f}(\beta, \beta_{0}). \\
\end{aligned}
$$

Sử dụng hàm mục tiêu rút gọn $$\tilde{f}$$ giúp loại bỏ hoàn toàn các biến phụ $$\xi$$, đồng thời chuyển bài toán ban đầu từ dạng có ràng buộc sang bài toán tối ưu hóa lồi không ràng buộc tương đương:

>$$
\begin{aligned}
\min_{\beta, \beta_0} \frac{1}{2} \|\beta\|_2^2 + C \sum_{i=1}^{n} \max\{0, 1 - y_{i} (x_{i}^{T} \beta + \beta_{0}) \}
\end{aligned}
$$
