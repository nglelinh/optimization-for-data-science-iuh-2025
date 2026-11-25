---
layout: post
title: 04-01 Thuật ngữ cơ bản
chapter: '04'
order: 2
owner: YoungJae Choung
categories:
- chapter04
lang: vi
lesson_type: required
---

Trước khi xây một tòa nhà cao tầng, kiến trúc sư và kỹ sư kết cấu phải nói chung một ngôn ngữ: thế nào là tải trọng giới hạn, thế nào là vùng an toàn, và biên độ dự phòng được đo ra sao. Trong tối ưu hóa lồi cũng vậy: một sự nhầm lẫn nhỏ giữa *miền xác định* $$D$$ và *tập khả thi*, hay giữa *giá trị tối ưu* $$f^\star$$ và *điểm tối ưu* $$x^\star$$, có thể khiến toàn bộ chứng minh định lý ở các chương sau sụp đổ.

Bài học này đặt nền móng thuật ngữ chuẩn quốc tế cho mọi bài toán tối ưu hóa lồi — từ ràng buộc tích cực (active constraint), nghiệm $$\epsilon$$-cận tối ưu (thứ duy nhất máy tính thực sự đạt được trong thực tế), cho đến lý do cốt tử vì sao ràng buộc đẳng thức $$h_j(x) = 0$$ bắt buộc phải là hàm affine chứ không thể là hàm lồi tùy ý.

## Kiến thức cần nhớ: Bốn mảnh ghép định nghĩa bài toán chuẩn

Khi đọc một bài toán tối ưu hóa bất kỳ, bộ não của người làm tối ưu tự động tách nó thành bốn lớp khái niệm rõ ràng:

- **Hàm mục tiêu & Miền xác định ngầm (Objective & Implicit Domain):** Ngoài các ràng buộc viết tường minh, mỗi hàm toán học như $$\log(x)$$ hay $$\sqrt{x}$$ còn mang theo miền xác định riêng $$\operatorname{dom}(f)$$. Miền chung $$D$$ là giao của mọi miền xác định này — tập khả thi luôn là tập con của $$D$$.
- **Ràng buộc bất đẳng thức lồi và Tập mức dưới (Sublevel Sets):** Bất đẳng thức $$g_i(x) \le 0$$ với $$g_i$$ lồi chính là tập mức dưới tại mức $$0$$ của $$g_i$$, do đó luôn là một tập lồi. Ràng buộc nào đạt dấu bằng $$g_i(x^\star) = 0$$ được gọi là *tích cực* vì nó trực tiếp "chặn" nghiệm tối ưu.
- **Ràng buộc đẳng thức Affine (Affine Equality Constraints):** Đẳng thức $$h_j(x) = 0$$ tương đương với cả $$h_j(x) \le 0$$ lẫn $$-h_j(x) \le 0$$. Để cả hai đều tạo thành tập lồi, $$h_j$$ phải vừa lồi vừa lõm — tức là phải là hàm affine $$a_j^T x = b_j$$.
- **Nghiệm chính xác vs. Nghiệm $$\epsilon$$-cận tối ưu:** Trong số học dấu phẩy động, thuật toán lặp hiếm khi chạm đúng $$f^\star$$ sau hữu hạn bước. Khái niệm điểm khả thi thỏa $$f(x) \le f^\star + \epsilon$$ là cầu nối giữa lý thuyết toán học thuần túy và tiêu chí dừng của bộ giải thực tế.

### Giải thích: Giải phẫu đầy đủ thuật ngữ trên một bài toán cụ thể

Xét bài toán 2 biến:
$$\min_{x_1, x_2} \; f(x_1, x_2) = -\log(x_1) + x_2^2 \quad \text{thỏa mãn} \quad g_1(x) = x_1 + x_2 - 2 \le 0,\quad g_2(x) = -x_2 \le 0.$$

1. **Xác định miền $$D$$:** Hàm $$-\log(x_1)$$ đòi hỏi $$x_1 > 0$$; các hàm còn lại xác định trên toàn $$\mathbb{R}^2$$. Vậy $$D = \{(x_1, x_2) \in \mathbb{R}^2 : x_1 > 0\}$$.
2. **Xác định tập khả thi $$\mathcal{F}$$:** Là tập các điểm $$(x_1, x_2)$$ thỏa $$x_1 > 0$$, $$x_2 \ge 0$$ và $$x_1 + x_2 \le 2$$ (một tam giác bỏ cạnh trục tung $$x_1 = 0$$). Điểm $$(1, 0.5)$$ là điểm khả thi vì $$1 > 0, 0.5 \ge 0, 1.5 \le 2$$. Điểm $$(0, 1)$$ **không** khả thi dù thỏa $$g_1, g_2 \le 0$$ vì nó nằm ngoài $$D$$.
3. **Tìm điểm tối ưu $$x^\star$$ và giá trị tối ưu $$f^\star$$:** Với mọi $$x_1 \in (0, 2]$$, muốn giảm $$f = -\log(x_1) + x_2^2$$ ta cần $$x_1$$ lớn nhất có thể và $$x_2$$ nhỏ nhất có thể. Chọn $$x_2^\star = 0$$ và đẩy $$x_1$$ sát biên $$x_1 + 0 \le 2$$ cho $$x_1^\star = 2$$. Khi đó $$x^\star = (2, 0)$$ và $$f^\star = -\log(2) \approx -0.6931$$.
4. **Phân loại ràng buộc tại $$x^\star = (2, 0)$$:**
   - $$g_1(2, 0) = 2 + 0 - 2 = 0 \implies$$ **ràng buộc tích cực**.
   - $$g_2(2, 0) = -0 = 0 \implies$$ **ràng buộc tích cực**.
5. **Kiểm tra nghiệm $$\epsilon$$-cận tối ưu:** Xét điểm khả thi $$\tilde{x} = (1.9, 0.1)$$. Ta có $$f(\tilde{x}) = -\log(1.9) + 0.01 \approx -0.6419 + 0.01 = -0.6319$$. Độ lệch so với $$f^\star$$ là $$-0.6319 - (-0.6931) = 0.0612$$. Vậy $$\tilde{x}$$ là điểm $$0.1$$-cận tối ưu (vì $$0.0612 \le 0.1$$) nhưng không phải $$0.05$$-cận tối ưu.

---

## Cơ bản về Tối ưu hóa Lồi

Phần này ôn tập các thuật ngữ cơ bản thường dùng trong các bài toán tối ưu hóa lồi. Một bài toán tối ưu hóa lồi được phát biểu dưới dạng chuẩn như sau:

>$$
\begin{aligned}
&\text{minimize}_{x \in D} &&{f(x)} \\
&\text{subject to} &&{g_{i}(x) \leq 0, \quad i = 1, \dotsc, m} \\
&&&{h_{j}(x) = 0, \quad j = 1, \dotsc, r},\\\\
\end{aligned}
$$

>trong đó $$f$$ và $$g_{i}$$ ($$i=1,\dotsc, m$$) đều là các hàm lồi, $$h_j$$ ($$j = 1, \dotsc, r$$) đều là các hàm affine, và miền xác định của bài toán là $$D = \operatorname{dom}(f) \cap \bigcap_{i=1}^{m} \operatorname{dom}(g_{i}) \cap \bigcap_{j=1}^r \operatorname{dom}(h_{j})$$.

* $$f$$ được gọi là **hàm tiêu chí** hoặc **hàm mục tiêu** (objective function).
* $$g_{i}(x)$$ được gọi là **hàm ràng buộc bất đẳng thức** (inequality constraint function).
* $$h_{j}(x)$$ được gọi là **hàm ràng buộc đẳng thức** (equality constraint function).
* Nếu $$x \in D$$ thỏa mãn $$g_{i}(x) \leq 0$$ với mọi $$i$$ và $$h_{j}(x) = 0$$ với mọi $$j$$, thì $$x$$ được gọi là một **điểm khả thi** (feasible point).
* Trên tập tất cả các điểm khả thi $$x$$, giá trị nhỏ nhất của $$f(x)$$ được gọi là **giá trị tối ưu** (optimal value), ký hiệu là $$f^{\star}$$.
* Nếu $$x$$ khả thi và $$f(x) = f^{\star}$$, thì $$x$$ được gọi là **điểm tối ưu**, **nghiệm tối ưu**, hoặc **điểm cực tiểu** (minimizer).
* Nếu $$x$$ khả thi và $$f(x) \le f^{\star} + \epsilon$$ (với $$\epsilon > 0$$), thì $$x$$ được gọi là điểm **$$\epsilon$$-cận tối ưu** ($$\epsilon$$-suboptimal).
* Nếu $$x$$ khả thi và $$g_i(x) = 0$$, ta nói ràng buộc $$g_i$$ là **ràng buộc tích cực** (hay *hoạt động*, active constraint) tại $$x$$.
* Mọi bài toán cực tiểu hóa lồi đều có thể chuyển tương đương thành một bài toán cực đại hóa lõm:

>$$
\begin{aligned}
&\text{maximize}_{x \in D} &&-f(x)\\
&\text{subject to} &&g_{i}(x) \leq 0, \quad i = 1, \dotsc, m\\
&&&h_{j}(x) = 0, \quad j = 1, \dotsc, r,\\\\
\end{aligned}
$$

>trong đó $$f$$ và $$g_{i}$$ ($$i=1,\dotsc, m$$) đều là các hàm lồi, $$h_j$$ ($$j = 1, \dotsc, r$$) đều là các hàm affine, và miền xác định của bài toán là $$D = \operatorname{dom}(f) \cap \bigcap_{i=1}^{m} \operatorname{dom}(g_{i}) \cap \bigcap_{j=1}^r \operatorname{dom}(h_{j})$$.

### Tập khả thi

Tập khả thi (còn gọi là miền khả thi hoặc không gian nghiệm khả thi) là tập hợp tất cả các điểm khả thi, biểu diễn toàn bộ các phương án thỏa mãn đồng thời mọi ràng buộc của bài toán.

Tập khả thi, thường ký hiệu là $$S$$ hoặc $$\mathcal{F}$$, được định nghĩa như sau:

> $$ S = \{ \mathbf{x} \in X \mid g_i(\mathbf{x}) \le 0 \text{ với mọi } i=1, \dots, m, \text{ và } h_j(\mathbf{x}) = 0 \text{ với mọi } j=1, \dots, r \} $$

### Tính chất của tập khả thi

1. **Tính lồi:** Nếu tất cả các hàm ràng buộc bất đẳng thức $$g_i(\mathbf{x})$$ đều lồi và tất cả các hàm ràng buộc đẳng thức $$h_j(\mathbf{x})$$ đều affine, thì tập khả thi $$S$$ là một **tập lồi**. Đây là tính chất nền tảng của tối ưu hóa lồi, góp phần đảm bảo mọi cực tiểu địa phương cũng là cực tiểu toàn cục.
2. **Tính bị chặn:** Một tập khả thi có thể **bị chặn** (nằm gọn trong một vùng hữu hạn) hoặc **không bị chặn** (trải dài vô hạn theo ít nhất một hướng).
3. **Tập rỗng:** Tập khả thi có thể rỗng ($$S = \emptyset$$), nghĩa là không tồn tại điểm nào thỏa mãn đồng thời mọi ràng buộc. Khi đó, bài toán tối ưu hóa được gọi là **không khả thi** (infeasible).
4. **Đa diện lồi bị chặn và tập đa diện (Polytope / Polyhedron):** Trong quy hoạch tuyến tính, tập khả thi khác rỗng và bị chặn được gọi là **đa diện lồi bị chặn** (polytope). Nếu tập khả thi khác rỗng nhưng có thể không bị chặn, nó được gọi là **tập đa diện** (polyhedron). Cả hai đều là tập lồi.
5. **Đỉnh (điểm cực biên):** Đối với bài toán quy hoạch tuyến tính, nếu tồn tại nghiệm tối ưu (và tập khả thi không chứa đường thẳng), thì luôn tồn tại ít nhất một nghiệm tối ưu nằm tại một đỉnh (còn gọi là điểm cực biên) của tập khả thi. Tính chất này là cơ sở của các thuật toán duyệt đỉnh như phương pháp đơn hình (Simplex).