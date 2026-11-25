---
layout: post
title: 15-02 Đường trung tâm
chapter: '15'
order: 6
owner: Minjoo Lee
categories:
- chapter15
lang: vi
---

Nếu ví miền khả thi của bài toán tối ưu như một căn phòng đa giác nhiều góc cạnh, và nghiệm tối ưu $$x^*$$ là một kho báu nằm ép sát vào một góc tường, thì **đường trung tâm (central path)** $$\{x^*(t) \mid t > 0\}$$ chính là "con đường cao tốc mượt mà" xuất phát từ chính giữa căn phòng (tâm giải tích ứng với $$t \to 0$$), uốn lượn nhẹ nhàng xuyên qua khoảng không rộng rãi ở giữa để tránh các vách tường gồ ghề, và chỉ rẽ vào chạm đúng góc kho báu $$x^*$$ khi $$t \to +\infty$$.

Điều kỳ diệu nhất về đường trung tâm là: ta **không cần** phải tìm chính xác mọi điểm trên đường cong đó. Chỉ cần đi từng bước nhảy lớn dọc theo "hành lang lân cận" của đường trung tâm, ta vừa giữ ma trận Hessian không bị suy biến quá sớm, vừa tiến theo cấp số nhân về đích!

## Bản đồ kiến thức nền: Hình học và ý nghĩa vật lý của đường trung tâm

- **Định nghĩa chính thức:** Với mỗi $$t > 0$$, $$x^*(t) = \arg\min \{t f(x) + \phi(x) \mid Ax = b\}$$. Dưới giả thiết tập khả thi chặt khác rỗng và $$\nabla^2 (t f + \phi) \succ 0$$, điểm $$x^*(t)$$ tồn tại duy nhất và biến thiên trơn theo $$t$$.
- **Diễn giải lực vật lý (Force-Field Interpretation) cho bài toán LP:** Khi $$f(x) = c^T x$$, điều kiện dừng $$t c + \nabla \phi(x) = 0$$ có nghĩa là tại $$x^*(t)$$, trọng lực không đổi $$-tc$$ kéo hạt về hướng $$-c$$ đang **cân bằng hoàn hảo** với tổng các lực đẩy điện tích $$\frac{1}{-h_i(x)}\nabla h_i(x)$$ phát ra từ các bức tường ràng buộc!
- **Hai đầu mút của đường trung tâm:** Khi $$t \to 0^+$$, $$x^*(t)$$ tiến về **tâm giải tích (analytic center)** của tập khả thi (độc lập với hàm mục tiêu $$f$$). Khi $$t \to +\infty$$, $$x^*(t)$$ hội tụ về nghiệm tối ưu $$x^*$$ (và nếu có nhiều nghiệm tối ưu, nó hội tụ về tâm giải tích của mặt tối ưu!).

### Khung giải thích (nên đọc chậm): Tính giải tích toàn bộ đường trung tâm $$x^*(t)$$ cho một bài toán LP trên đoạn thẳng

Xét bài toán LP 1 chiều:
$$\min_{x \in \mathbb{R}} x \qquad \text{với điều kiện } 0 \le x \le 4 \;\; (\text{tức } h_1 = -x \le 0, \; h_2 = x - 4 \le 0).$$
Hàm chắn là $$\phi(x) = -\log(x) - \log(4 - x)$$.

1. **Thiết lập phương trình đường trung tâm:**
   $$\frac{d}{dx}\bigl(tx - \log x - \log(4 - x)\bigr) = t - \frac{1}{x} + \frac{1}{4 - x} = 0.$$
2. **Quy đồng giải phương trình bậc hai theo $$x$$:**
   $$t x(4 - x) - (4 - x) + x = 0 \iff t x^2 - (4t + 2)x + 4 = 0.$$
   Vì $$x^*(t) \in (0, 4)$$, ta chọn nghiệm nhỏ hơn:
   $$x^*(t) = \frac{(2t + 1) - \sqrt{4t^2 + 1}}{t}.$$
3. **Thử các mốc $$t$$ để nhìn đường trung tâm chạy:**
   - Khi $$t \to 0^+$$: $$x^*(t) \to 2$$ (tâm giải tích nằm đúng chính giữa đoạn $$[0, 4]$$!).
   - Tại $$t = 1$$: $$x^*(1) = 3 - \sqrt{5} \approx 0.764$$.
   - Tại $$t = 10$$: $$x^*(10) = \frac{21 - \sqrt{401}}{10} \approx \frac{21 - 20.025}{10} = 0.0975$$.
   - Khi $$t \to +\infty$$: $$x^*(t) \approx \frac{1}{t} \to 0 = x^*$$!
   Lưu ý tại $$t = 10$$, sai số $$f(x^*(10)) - f^* = 0.0975 \le \frac{m}{t} = \frac{2}{10} = 0.2$$ (thực tế còn chặt hơn vì ràng buộc $$x \le 4$$ không tích cực!).

---

Ký hiệu $$x^*(t)$$ là nghiệm của bài toán chắn ứng với tham số $$t > 0$$:

>$$
>\begin{align}
> &\min_{x} \ &&  tf(x) + \phi(x) \\
> &\text{thỏa mãn } \ && Ax = b \\
> \end{align}
>$$

Khi đó, tập hợp $$\{x^*(t) \mid t > 0 \}$$ được gọi là **đường trung tâm (central path)**.

Dưới các điều kiện phù hợp, đường trung tâm tạo thành một đường cong trơn trong $$\mathbb{R}^n$$ và hội tụ về nghiệm tối ưu $$x^*$$ của bài toán gốc khi $$t \to \infty$$.

Nói cách khác, thay vì tìm trực tiếp nghiệm tối ưu nằm trên biên, ta giải một chuỗi bài toán chắn với các giá trị $$t$$ tăng dần để đi dọc theo đường trung tâm từ bên trong miền khả thi tiến dần ra biên.

## Ví dụ: đường trung tâm của một bài toán LP
Xét bài toán quy hoạch tuyến tính (LP):
>$$
>\begin{align*}
>&\min_{x} \ && c^Tx \\
>&\text{thỏa mãn } \ && a_i^Tx \le b_i, \quad i = 1, \cdots , 6 \\
>\end{align*}
>$$

Trong hình dưới đây, các đường nét đứt biểu diễn đường đồng mức của hàm chắn logarit $$\phi$$.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_central_path_02.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] Đường trung tâm [1]</figcaption>
</p>
</figure>

Khi $$t \to \infty$$, đường trung tâm hội tụ về đỉnh tối ưu $$x^*$$. Tại mỗi điểm $$x^*(t)$$ trên đường trung tâm, siêu phẳng $$c^Tx = c^Tx^*(t)$$ tiếp xúc với đường đồng mức của $$\phi$$ đi qua $$x^*(t)$$.

### Đường trung tâm dẫn tới đỉnh tối ưu (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/central-path_vi.mp4"></video>
</div>

Khi $$t$$ tăng dần, nghiệm $$x^*(t)$$ của bài toán chắn trượt dọc theo đường trung tâm tiến về đỉnh tối ưu.

### Tự tay thử: trượt dọc đường trung tâm

<div class="opx-explainer" data-opx="barrier" data-lang="vi"></div>
