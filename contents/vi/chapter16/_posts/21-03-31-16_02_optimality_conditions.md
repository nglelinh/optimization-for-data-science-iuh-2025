---
layout: post
title: 16-02 Điều kiện tối ưu
chapter: '16'
order: 3
owner: Minjoo Lee
categories:
- chapter16
lang: vi
---

Nếu đặt hệ điều kiện tối ưu **KKT** của bài toán gốc và hệ phương trình **Đường trung tâm (Central Path)** của bài toán chắn cạnh nhau trên hai cột, bạn sẽ ngỡ ngàng nhận ra chúng giống nhau gần như từng ký tự! Khác biệt duy nhất nằm ở đúng một phương trình: điều kiện bù yếu $$u_i h_i(x) = 0$$ được dịch chuyển mượt mà thành $$-u_i h_i(x) = \frac{1}{t}$$ (hay trong LP dạng chuẩn là $$x_i s_i = \mu$$ với $$\mu = 1/t$$).

Cú đặt cạnh nhau có chủ đích ở mục 16-02 chính là bản thiết kế kỹ thuật cho toàn bộ Chương 17: phương pháp điểm trong nguyên thủy – đối ngẫu sẽ **không** lập bài toán chắn thuần nguyên thủy nữa, mà trực tiếp áp dụng **phương pháp Newton để giải hệ phương trình đường trung tâm** $$F_\mu(x, y, s) = 0$$ trong khi giảm dần $$\mu \to 0$$!

## Bản đồ kiến thức nền: Bốn mảnh ghép so sánh KKT và Đường trung tâm

- **Hệ điều kiện KKT cho bài toán tổng quát:** Gồm 4 khối: (1) Điều kiện dừng, (2) Khả thi nguyên thủy, (3) Khả thi đối ngẫu, và (4) Bù yếu $$u_i h_i(x) = 0$$. Khi đối ngẫu mạnh thỏa mãn, KKT vừa là điều kiện **cần** vừa là điều kiện **đủ** cho tối ưu toàn cục.
- **Hệ phương trình đường trung tâm:** Giữ nguyên (1), siết chặt (2) và (3) thành khả thi chặt ($$h_i(x) < 0, u_i > 0$$), và thay (4) bằng $$-u_i h_i(x) = 1/t$$.
- **Dạng đặc biệt cực đẹp của Quy hoạch tuyến tính (LP dạng chuẩn):**
  - **KKT của LP:** $$Ax = b, \; x \ge 0$$; $$A^T y + s = c, \; s \ge 0$$; và $$X S \mathbf{1} = 0$$ (tức $$x_i s_i = 0 \;\forall i$$).
  - **Đường trung tâm của LP:** Chỉ thay đúng phương trình cuối thành $$X S \mathbf{1} = \mu \mathbf{1}$$ (tức $$x_i s_i = \mu > 0$$ với $$\mu = 1/t$$)!
- **Khoảng cách đối ngẫu trực tiếp trong LP:** Với mọi cặp $$(x, y, s)$$ khả thi nguyên thủy – đối ngẫu, ta có $$c^T x - b^T y = (A^T y + s)^T x - (Ax)^T y = s^T x = \sum_{i=1}^n x_i s_i$$! Trên đường trung tâm, tổng này bằng đúng $$n\mu = n/t$$!

### Khung giải thích (nên đọc chậm): Giải hệ phương trình đường trung tâm của LP dạng chuẩn bằng tay

Quay lại bài toán LP 2 biến ở bài trước: $$\min 3x_1 + 5x_2$$ thỏa $$x_1 + 2x_2 = 4, \; x_1, x_2 \ge 0$$ (có nghiệm KKT gốc $$x^\star = (0, 2), \; y^\star = 2.5, \; s^\star = (0.5, 0)$$). Hãy giải hệ đường trung tâm với tham số nhiễu $$\mu = 0.5$$ (tức $$t = 2$$):

1. **Viết đầy đủ 5 phương trình của đường trung tâm LP ($$x > 0, s > 0$$):**
   - Khả thi nguyên thủy: $$x_1 + 2x_2 = 4$$.
   - Khả thi đối ngẫu: $$y + s_1 = 3$$ và $$2y + s_2 = 5$$.
   - Bù yếu nhiễu: $$x_1 s_1 = 0.5$$ và $$x_2 s_2 = 0.5$$.
2. **Giải rút gọn theo 1 biến $$y$$:**
   Từ $$s_1 = 3 - y > 0$$ và $$s_2 = 5 - 2y > 0$$ (nên $$y < 2.5$$), ta suy ra:
   $$x_1 = \frac{0.5}{3 - y}, \qquad x_2 = \frac{0.5}{5 - 2y}.$$
   Thay vào $$x_1 + 2x_2 = 4$$:
   $$\frac{0.5}{3 - y} + \frac{1}{5 - 2y} = 4.$$
   Thử kiểm tra nhanh giá trị $$y \approx 2.345$$:
   - $$s_1 = 3 - 2.345 = 0.655 \implies x_1 = \frac{0.5}{0.655} \approx 0.763$$.
   - $$s_2 = 5 - 4.690 = 0.310 \implies x_2 = \frac{0.5}{0.310} \approx 1.613$$.
   - Kiểm tra $$x_1 + 2x_2 = 0.763 + 3.226 = 3.989 \approx 4$$ (nghiệm chính xác là $$y(\mu) \approx 2.346, \; x(\mu) \approx (0.765, 1.618), \; s(\mu) \approx (0.654, 0.309)$$).
3. **Kiểm chứng khoảng cách đối ngẫu $$c^T x - b^T y = x^T s = n\mu$$:**
   - $$c^T x \approx 3(0.765) + 5(1.618) = 10.385$$; $$b^T y \approx 4(2.346) = 9.384$$.
   - Hiệu $$c^T x - b^T y \approx 1.00 = 2 \times 0.5 = n\mu$$! Khớp chính xác lý thuyết!

---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

Trong phần này, chúng ta ôn lại các điều kiện tối ưu KKT cho bài toán nguyên thủy và bài toán rào cản (barrier) tương ứng, sau đó so sánh sự khác biệt giữa hai hệ điều kiện này.
<br/>

## Điều kiện tối ưu KKT

Hãy xem lại các điều kiện KKT đã trình bày ở Chương 12 — đây là công cụ cốt lõi để kiểm tra tính tối ưu của nghiệm.

### Bài toán nguyên thủy
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad f(x) \\\\
>    \text{subject to} &\quad h_i(x) \leq 0, i = 1, \ldots, m \\\\
>    &\quad l_j(x) = 0, j = 1, \ldots, r
>\end{align}
>$$

Khi bài toán nguyên thủy là bài toán lồi, các điều kiện KKT trở thành điều kiện đủ cho tính tối ưu nguyên thủy – đối ngẫu. Cụ thể, giả sử $$f, h_1, \dots, h_m$$ lồi, $$l_1, \dots, l_r$$ là các hàm affine (và các hàm đều khả vi): nếu $$x^\star, u^\star, v^\star$$ thỏa mãn các điều kiện KKT dưới đây, thì $$x^\star$$ và $$(u^\star, v^\star)$$ lần lượt là nghiệm tối ưu nguyên thủy và đối ngẫu với khoảng cách đối ngẫu bằng $$0$$. <br>

* Tham khảo: [12-01 Điều kiện KKT]({% multilang_post_url contents/chapter12/21-04-02-12_00_KKT_conditions %})

### Điều kiện KKT cho bài toán nguyên thủy đã cho
>$$
>\begin{align}
>l_i(x^\star) &= 0, \quad i=1, \dots, r\\\\
>u_i^\star, -h_i(x^\star) &\ge 0, \quad i=1, \dots, m\\\\
>u_i^\star h_i(x^\star) &= 0, \quad i=1, \dots, m\\\\
>\nabla f(x^\star) + \sum_{i=1}^m \nabla h_i(x^\star) u^\star_i + \sum_{i=1}^r \nabla l_i(x^\star) v_i^\star &= 0.\\\\
>\end{align}
>$$

## Phương trình đường trung tâm (Central Path)

Tiếp theo, ta xét các điều kiện xác định tính tối ưu của bài toán rào cản.

### Bài toán rào cản

>$$
\begin{align}
    \mathop{\text{minimize}}_x &\quad f(x) + \tau \phi(x) \\\\
    &\quad l_j(x) = 0, j = 1, \ldots, r  \\\\
\end{align}$$
>
>$$ \text{trong đó } \phi(x) = - \sum_{i=1}^m \log \big( -h_i(x) \big).$$


Từ các điều kiện KKT của bài toán rào cản, ta thu được hệ điều kiện tối ưu sau. Cần chú ý sự khác biệt ở ràng buộc bất đẳng thức (chuyển thành bất đẳng thức ngặt) và điều kiện bù chặt (chuyển từ $$0$$ thành $$-\tau$$) so với hệ điều kiện KKT của bài toán nguyên thủy ở trên. (Tham khảo: [15-03-01 Điều kiện KKT bị nhiễu]({% multilang_post_url contents/chapter15/21-03-28-15_03_01_perturbed_kkt_conditions %}))

### Điều kiện tối ưu cho bài toán rào cản (và bài toán đối ngẫu của nó)

>$$
\begin{align}
l_i(x^\star(t)) &= 0, \quad i=1, \dots, r\\\\
u_i(t), -h_i(x^\star(t)) &\gt 0, \quad i=1, \dots, m\\\\
u_i(t) h_i(x^\star(t)) &= -\tau, \quad i=1, \dots, m\\\\
\nabla f(x^\star(t)) + \sum_{i=1}^m \nabla h_i(x^\star(t)) u_i(t) + \sum_{i=1}^r \nabla l_i(x^\star(t)) \hat{v}_i^\star &= 0,\\\\
\end{align} \\\\
$$
>
>$$\text{trong đó } \tau = \frac{1}{t}, u_i(t) = - \frac{1}{t h_i(x^\star(t))}, \quad \hat{v} = \frac{1}{t}v.$$

## Trường hợp đặc biệt: quy hoạch tuyến tính

### Nhắc lại: Bài toán nguyên thủy của LP dạng chuẩn
>$$
>\begin{align}
>    \mathop{\text{minimize}}_x &\quad c^Tx \\\\
>    \text{subject to} &\quad Ax = b \\\\
>    &\quad x \ge 0
>\end{align}
>$$

### Nhắc lại: Bài toán đối ngẫu của LP
>$$
>\begin{align}
>    \mathop{\text{maximize}}_{s,y} &\quad b^Ty \\\\
>    \text{subject to} &\quad A^Ty +  s = c \\\\
>    &\quad s \ge 0
>\end{align}
>$$

Quy hoạch tuyến tính có tính chất thuận lợi là luôn thỏa mãn tính đối ngẫu mạnh theo điều kiện Slater tinh chỉnh (khi khả thi), bởi mọi ràng buộc bất đẳng thức đều là affine. Các điều kiện tối ưu cho LP như sau:

>$$
>\begin{align}
>A^T y^\star + s^\star &= c\\\\
>Ax^\star &= b\\\\
>X S \mathbb{1} &= 0\\\\
>x^\star, s^\star &\ge 0,\\\\
>\end{align}$$
> 
>$$\text{trong đó }X = Diag(x^\star), S = Diag(s^\star)$$

Lưu ý rằng $$X S \mathbb{1} = 0$$ tương đương với $$Xs^\star = (x_1^\star s_1^\star, \dots, x_n^\star s_n^\star)^T = 0$$. Cách ký hiệu bằng ma trận đường chéo $$X, S$$ sẽ rất thuận tiện khi trình bày các thuật toán ở phần sau.

### Thuật toán giải quy hoạch tuyến tính

Có hai lớp phương pháp tiêu biểu để giải LP dựa trên hệ điều kiện tối ưu trên:

1. Phương pháp đơn hình (Simplex): Duy trì các điều kiện 1, 2 và 3 (hoặc tính khả thi cơ sở và bù chặt) trong khi từng bước đạt tới điều kiện 4 (tính không âm đối ngẫu).
2. Phương pháp điểm trong (Interior-point method): Duy trì điều kiện 4 (tính dương ngặt) trong khi tiến dần tới việc thỏa mãn các điều kiện 1, 2 và 3. Phương pháp này sẽ được trình bày chi tiết ở chương tiếp theo.

## Đường trung tâm cho quy hoạch tuyến tính

### Nhắc lại: Bài toán rào cản cho LP
>$$
\begin{align}
    \mathop{\text{minimize}}_x &\quad c^Tx - \tau \sum_{i=1}^n \log(x_i)\\\\
    \text{subject to} &\quad Ax = b, \\\\
    \text{trong đó}  &\quad \tau > 0
\end{align}$$


### Nhắc lại: Bài toán đối ngẫu của bài toán rào cản cho LP
>$$
>\begin{align}
>    \mathop{\text{maximize}}_{s,y} &\quad b^Ty + \tau \sum_{i=1}^n \log(s_i)\\\\
>    \text{subject to} &\quad A^Ty +  s = c \\\\
>\end{align}
>$$

Các điều kiện tối ưu cho bài toán rào cản của LP là:

>$$
\begin{align}
A^T y^\star + s^\star &= c\\\\
Ax^\star &= b\\\\
X S \mathbb{1} &= \tau \mathbb{1}\\\\
x^\star, s^\star &\gt 0,\\\\
\text{trong đó} &\quad X = Diag(x^\star), S = Diag(s^\star)
\end{align}$$

Hai điều kiện 3 và 4 thể hiện rõ sự khác biệt so với hệ điều kiện KKT của bài toán LP gốc.

### KKT: pháp tuyến và nhân tử Lagrange (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/kkt-normals_vi.mp4"></video>
</div>

Tại điểm tối ưu, $$-\nabla f(x^*)$$ là tổ hợp tuyến tính không âm của các pháp tuyến ràng buộc đang tác dụng, còn các ràng buộc không tác dụng có nhân tử bằng $$0$$.

### Tự tay thử: nhân tử KKT

<div class="opx-explainer" data-opx="kkt" data-lang="vi"></div>
