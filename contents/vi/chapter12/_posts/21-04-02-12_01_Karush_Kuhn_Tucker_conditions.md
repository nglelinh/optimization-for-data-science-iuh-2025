---
layout: post
title: 12-01 Điều kiện Karush-Kuhn-Tucker
chapter: '12'
order: 2
owner: Wontak Ryu
categories:
- chapter12
lang: vi
lesson_type: required
---

Nhiều sinh viên học thuộc lòng 4 dòng điều kiện KKT rất nhanh, nhưng lại thường lúng túng trước câu hỏi sắc bén nhất của bài học này: **khi nào KKT là điều kiện *cần*, và khi nào KKT là điều kiện *đủ*?** Nếu bạn giải hệ phương trình KKT cho một bài toán không lồi, liệu nghiệm tìm ra có chắc chắn là cực tiểu toàn cục không? Ngược lại, nếu một bài toán lồi có nghiệm tối ưu $$x^*$$, liệu $$x^*$$ có *luôn luôn* thỏa KKT không?

Bài học này giải mã trọn vẹn mối quan hệ logic hai chiều ấy chỉ bằng đúng một chuỗi bất đẳng thức 4 dòng nối từ Chương 11:
$$f(x^*) = g(u^*, v^*) = \inf_x L(x, u^*, v^*) \le L(x^*, u^*, v^*) = f(x^*) + \sum u_i^* h_i(x^*) + \sum v_j^* l_j(x^*) \le f(x^*).$$
Vì hai đầu chuỗi đều là $$f(x^*)$$, mọi dấu $$\le$$ ở giữa **bắt buộc trở thành dấu bằng**! Dấu bằng thứ nhất cho ta *điều kiện dừng* ($$x^*$$ cực tiểu hóa $$L$$); dấu bằng thứ hai cho ta *điều kiện bù* ($$u_i^* h_i(x^*) = 0$$)! Không có phép thuật nào cả — toàn bộ hệ KKT bật ra chỉ từ đúng một chuỗi bất đẳng thức kẹp!

## Kiến thức cần nhớ: Bốn trụ cột logic về điều kiện KKT

- **Điều kiện cần (Necessity — Cần đối ngẫu mạnh!):** Cho bài toán bất kỳ (kể cả không lồi) có nghiệm tối ưu gốc $$x^*$$ và đối ngẫu $$(u^*, v^*)$$ thỏa **đối ngẫu mạnh** ($$f^* = g^*$$), thì $$(x^*, u^*, v^*)$$ *bắt buộc* thỏa mãn cả 4 điều kiện KKT. (Lưu ý: nếu bài toán lồi *không* có đối ngẫu mạnh vì vi phạm Slater, nghiệm tối ưu có thể không thỏa KKT!)
- **Điều kiện đủ (Sufficiency — Cần tính lồi!):** Nếu bài toán là **bài toán lồi** ($$f, h_i$$ lồi và $$l_j$$ affine), thì bất kỳ bộ $$(x^*, u^*, v^*)$$ nào thỏa 4 điều kiện KKT đều **chắc chắn** là cặp nghiệm tối ưu toàn cục gốc–đối ngẫu với khoảng cách đối ngẫu bằng $$0$$!
- **Hợp nhất cho bài toán lồi thỏa Slater:** Khi bài toán lồi và thỏa điều kiện Slater, KKT trở thành **điều kiện cần và đủ ($$\Longleftrightarrow$$)** để đặc trưng toàn bộ tập nghiệm tối ưu!
- **Lưu ý quan trọng về bài toán không lồi:** Với bài toán không lồi, một điểm thỏa KKT chỉ là *ứng viên dừng* — nó có thể là cực tiểu địa phương, điểm yên ngựa, thậm chí cực đại địa phương!

### Giải thích: Giải tay bài toán 2 biến có ràng buộc bất đẳng thức bằng hệ KKT

Tìm nghiệm tối ưu toàn cục của bài toán lồi:
$$\min_{x_1, x_2 \in \mathbb{R}} \; f(x_1, x_2) = x_1^2 + x_2^2 \quad \text{s.t.} \quad h(x_1, x_2) = 4 - x_1 - x_2 \le 0.$$

1. **Viết hệ 4 điều kiện KKT với nhân tử $$u \ge 0$$:**
   - Dừng: $$\begin{cases} 2x_1 - u = 0 \\ 2x_2 - u = 0 \end{cases} \implies x_1 = x_2 = \frac{u}{2}$$.
   - Khả thi gốc: $$4 - x_1 - x_2 \le 0$$.
   - Khả thi đối ngẫu: $$u \ge 0$$.
   - Bù: $$u(4 - x_1 - x_2) = 0$$.
2. **Xét 2 trường hợp của điều kiện bù $$u(4 - x_1 - x_2) = 0$$:**
   - *Trường hợp 1 ($$u = 0$$ — ràng buộc lỏng):* Từ điều kiện dừng suy ra $$x_1 = x_2 = 0$$. Kiểm tra khả thi gốc: $$4 - 0 - 0 = 4 > 0$$ (vi phạm!) $$\implies$$ loại!
   - *Trường hợp 2 ($$u > 0$$ — ràng buộc chặt):* Buộc có $$4 - x_1 - x_2 = 0$$. Thay $$x_1 = x_2 = u/2$$ vào:
     $$4 - \frac{u}{2} - \frac{u}{2} = 0 \implies u^* = 4 > 0 \implies x_1^* = 2, \; x_2^* = 2.$$
3. **Chốt tối ưu toàn cục nhờ Điều kiện đủ:** Vì $$f(x) = x_1^2 + x_2^2$$ lồi và $$h(x)$$ tuyến tính, bộ $$(x^*, u^*) = ((2, 2), 4)$$ thỏa đủ 4 điều kiện KKT chắc chắn là **nghiệm tối ưu toàn cục duy nhất** với $$f^* = 8$$!

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Xét bài toán tối ưu hóa tổng quát sau:

>$$
>\begin{align}
>    &\min_{x} &&{f(x)} \\\\
>    &\text{với điều kiện } &&{h_i(x) \le 0, \text{ } i=1,\dots,m} \\\\
>    & &&{l_j(x) = 0, \text{ } j=1,\dots,r}.\\\\
>\end{align}
>$$

**Các điều kiện Karush–Kuhn–Tucker (KKT)** (gọi tắt là **điều kiện KKT**) bao gồm bốn nhóm điều kiện sau [3]:

* $$0 \in \partial \big( f(x) + \sum_{i=1}^{m} \lambda_i h_i(x) + \sum_{j=1}^{r} \nu_j l_j(x) \big)$$ (**Điều kiện dừng**): Khi cố định $$\lambda, \nu$$, dưới vi phân (subdifferential) của hàm Lagrangian theo $$x$$ chứa vector $$0$$.
* $$\lambda_i \cdot h_i(x) = 0 \text{ với mọi } i$$ (**Điều kiện bù yếu**): Với mỗi $$i$$, ít nhất một trong hai đại lượng $$\lambda_i$$ và $$h_i(x)$$ bằng $$0$$.
* $$h_i(x) \le 0, l_j(x) = 0 \text{ với mọi } i, j$$ (**Tính khả thi nguyên thủy**): Điểm $$x$$ thỏa mãn toàn bộ các ràng buộc của bài toán nguyên thủy.
* $$\lambda_i \ge 0 \text{ với mọi } i$$ (**Tính khả thi đối ngẫu**): Các nhân tử tương ứng với ràng buộc bất đẳng thức thỏa mãn điều kiện không âm của bài toán đối ngẫu.

## Điều kiện đủ

Đối với bài toán nguyên thủy lồi, nếu tồn tại bộ $$(x^\star, \lambda^\star, \nu^\star)$$ thỏa mãn các điều kiện KKT, thì biến đổi sau cho thấy $$(x^\star, \lambda^\star, \nu^\star)$$ là cặp nghiệm tối ưu nguyên thủy và đối ngẫu với khoảng cách đối ngẫu bằng không:

>$$
>\begin{align}
>    g(\lambda^\star, \nu^\star) &= \min_x L(x, \lambda^\star, \nu^\star) \\\\
>                                &= L(x^\star, \lambda^\star, \nu^\star) \\\\
>                                &= f(x^\star) + \sum_{i=1}^m \lambda_i^\star h_i(x^\star) + \sum_{j=1}^r \nu_j^\star l_j(x^\star) \\\\
>                                &= f(x^\star)
>\end{align}
>$$

1. Hàm $$L(x,\lambda^\star,\nu^\star) = f(x) + \sum_{i=1}^{m} \lambda_i^\star h_i(x) + \sum_{j=1}^{r} \nu_j^\star l_j(x)$$ là hàm lồi theo $$x$$ (vì là tổng các hàm lồi với hệ số không âm đối với $$h_i$$ và các hàm affine $$l_j$$).
2. Vì $$0 \in \partial \big( f(x^\star) + \sum_{i=1}^{m} \lambda_i^\star h_i(x^\star) + \sum_{j=1}^{r} \nu_j^\star l_j(x^\star) \big)$$, nên $$\min_x L(x, \lambda^\star, \nu^\star) = L(x^\star, \lambda^\star, \nu^\star)$$.
3. Nhờ điều kiện bù yếu và tính khả thi nguyên thủy, ta có $$f(x^\star) + \sum_{i=1}^m \lambda_i^\star h_i(x^\star) + \sum_{j=1}^r \nu_j^\star l_j(x^\star) = f(x^\star)$$.

## Điều kiện cần

Ngược lại, nếu $$(x^\star, \lambda^\star, \nu^\star)$$ là nghiệm tối ưu nguyên thủy và đối ngẫu với khoảng cách đối ngẫu bằng không (chẳng hạn khi bài toán thỏa mãn điều kiện Slater), thì mọi bất đẳng thức trong chuỗi dưới đây đều trở thành đẳng thức, suy ra $$(x^\star, \lambda^\star, \nu^\star)$$ thỏa mãn các điều kiện KKT:

>$$
>\begin{align}
>    f(x^\star) &= g(\lambda^\star, \nu^\star) \\\\
>                   &= \min_x  \big( f(x) + \sum_{i=1}^{m} \lambda_i^\star h_i(x) + \sum_{j=1}^{r} \nu_j^\star l_j(x) \big) \\\\
>                   &\le f(x^\star) + \sum_{i=1}^m \lambda_i^\star h_i(x^\star) + \sum_{j=1}^r \nu_j^\star l_j(x^\star) \\\\
>                   &\le f(x^\star)
>\end{align}
>$$

1. Đẳng thức $$f(x^\star) = g(\lambda^\star, \nu^\star)$$ thể hiện khoảng cách đối ngẫu bằng không.
2. Để có $$f(x^\star) + \sum_{i=1}^m \underbrace{\lambda_i^\star h_i(x^\star)}_{0} + \sum_{j=1}^r \underbrace{\nu_j^\star l_j(x^\star)}_{0} = f(x^\star)$$, điều kiện bù yếu và tính khả thi nguyên thủy phải được thỏa mãn.
3. Khi đẳng thức này đúng, mọi bất đẳng thức trong chuỗi suy dẫn trên đều là đẳng thức; đặc biệt $$x^\star$$ đạt cực tiểu của $$L(x, \lambda^\star, \nu^\star)$$, dẫn đến điều kiện dừng.

## Tổng kết

Tóm lại, đối với bài toán tối ưu lồi, các điều kiện KKT là:

* Điều kiện đủ cho cặp nghiệm tối ưu nguyên thủy và đối ngẫu có khoảng cách đối ngẫu bằng không.
* Điều kiện cần cho cặp nghiệm tối ưu nguyên thủy và đối ngẫu khi tính đối ngẫu mạnh được thỏa mãn.

Nói cách khác, với các bài toán thỏa mãn tính đối ngẫu mạnh, ta có tương đương sau:

>$$
>\begin{align}
>    x^\star, \lambda^\star, \nu^\star \text{ là nghiệm nguyên thủy và đối ngẫu} \\\\
>    \Leftrightarrow x^\star, \lambda^\star, \nu^\star \text{ thỏa mãn các điều kiện KKT} \\\\
>\end{align}
>$$

### KKT qua ví dụ đổ nước trong khoảng 3 phút

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/kkt-water-filling_vi.mp4"></video>
</div>

Giải bài đổ nước với α = (0,1; 0,4; 0,8; 1,2) bằng bốn điều kiện KKT, đọc ý nghĩa của λ, và ba cách đoán sai bị KKT loại.
