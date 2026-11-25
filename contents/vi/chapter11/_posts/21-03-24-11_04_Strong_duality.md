---
layout: post
title: 11-04 Tính đối ngẫu mạnh
chapter: '11'
order: 5
owner: Wontak Ryu
categories:
- chapter11
lang: vi
lesson_type: required
---

Đối ngẫu yếu ($$g^* \le f^*$$) luôn đúng nhưng chưa đủ để ta yên tâm thay thế bài toán gốc bằng bài toán đối ngẫu — nếu khoảng cách $$f^* - g^*$$ vẫn lớn, giải xong đối ngẫu ta chỉ biết một cận dưới lỏng lẻo chứ không chạm được tới đáy thực sự $$f^*$$. Câu hỏi sống còn của Chương 11 là: **khi nào khoảng cách ấy thu về đúng bằng $$0$$ ($$f^* = g^*$$ — tính đối ngẫu mạnh)?**

Trong quy hoạch tuyến tính, tính lồi tự nó là đủ. Nhưng với bài toán lồi phi tuyến tổng quát, điều bất ngờ là tính lồi *chưa hoàn toàn đủ* — vẫn tồn tại những bài toán lồi "kỳ dị" trên biên khiến $$g^* < f^*$$! Để loại trừ những điểm kỳ dị đó, ta chỉ cần thêm một điều kiện chuẩn hóa cực kỳ nhẹ gọi là **điều kiện Slater**: tồn tại ít nhất một điểm khả thi chặt nằm *hẳn bên trong* các ràng buộc bất đẳng thức phi tuyến ($$h_i(\tilde{x}) < 0$$). Khi điều kiện Slater thỏa mãn (như trong bài toán SVM lừng danh ở cuối bài), tính đối ngẫu mạnh được bảo chứng 100%!

## Bản đồ kiến thức nền: Bốn trụ cột của tính đối ngẫu mạnh và điều kiện Slater

- **Định nghĩa tính đối ngẫu mạnh:** Xảy ra khi $$f^* = g^*$$ (khoảng cách đối ngẫu tối ưu bằng $$0$$). Điều này cho phép ta giải bài toán đối ngẫu (thường đơn giản hơn hoặc có ít biến hơn, hoặc hỗ trợ thủ thuật nhân — kernel trick trong SVM!) rồi khôi phục nghiệm gốc.
- **Điều kiện Slater (dạng chuẩn và dạng tinh gọn cho ràng buộc affine):**
  - *Dạng chuẩn:* Bài toán gốc lồi và tồn tại $$\tilde{x} \in \operatorname{relint}(\mathcal{D})$$ sao cho $$h_i(\tilde{x}) < 0$$ với mọi $$i$$ và $$l_j(\tilde{x}) = 0$$ với mọi $$j$$.
  - *Dạng tinh gọn (rất hay dùng!):* Các ràng buộc bất đẳng thức **tuyến tính (affine)** chỉ cần thỏa $$h_i(\tilde{x}) \le 0$$ (không cần dấu `<` chặt!); chỉ những ràng buộc *phi tuyến* mới đòi hỏi dấu `<` chặt! Đó là lý do LP (toàn ràng buộc affine) không cần điểm chặt vẫn có đối ngẫu mạnh!
- **Định lý tách siêu phẳng — gốc rễ hình học của Slater:** Điều kiện Slater đảm bảo siêu phẳng đỡ tập $$\mathcal{A} = \{(u, t) : \exists x, h(x) \le u, f(x) \le t\}$$ tại $$(0, f^*)$$ không bị "dựng đứng" song song trục $$t$$, nhờ đó hệ số của $$f(x)$$ khác $$0$$ và chia chuẩn hóa ra được nhân tử Lagrange hữu hạn $$(u^*, v^*)$$.
- **Ứng dụng vàng — Bài toán đối ngẫu SVM:** Trong SVM, mọi ràng buộc $$1 - y_i(x_i^T\beta + \beta_0) - \xi_i \le 0$$ và $$-\xi_i \le 0$$ đều là **ràng buộc affine**! Do đó bài toán SVM tự động thỏa điều kiện Slater tinh gọn và luôn có đối ngẫu mạnh $$f^* = g^*$$!

### Khung giải thích (nên đọc chậm): Đối chiếu 1 bài toán thỏa Slater và 1 bài toán lồi vi phạm Slater

**Trường hợp 1 (Thỏa Slater $$\implies f^* = g^*$$):**
$$\min_{x_1, x_2} \; x_1^2 + x_2^2 \quad \text{s.t.} \quad h_1(x) = 2 - x_1 - x_2 \le 0, \quad h_2(x) = x_1^2 - 4 \le 0.$$
- Chọn điểm thử $$\tilde{x} = (1.5, 1.5)$$: ta có $$h_1(\tilde{x}) = 2 - 3 = -1 < 0$$ và $$h_2(\tilde{x}) = 2.25 - 4 = -1.75 < 0$$.
- Tồn tại điểm khả thi chặt $$\implies$$ điều kiện Slater thỏa mãn $$\implies$$ chắc chắn có **đối ngẫu mạnh** (thực tế $$x^* = (1, 1), f^* = g^* = 2$$).

**Trường hợp 2 (Bài toán lồi nổi tiếng của Boyd–Vandenberghe *vi phạm* Slater $$\implies g^* < f^*$$):**
$$\min_{x_1 \in \mathbb{R},\; x_2 > 0} \; f(x_1, x_2) = e^{-x_1} \quad \text{s.t.} \quad h(x_1, x_2) = \frac{x_1^2}{x_2} \le 0.$$
- Đây là bài toán **lồi** (hàm bậc hai chia tuyến tính $$x_1^2/x_2$$ lồi trên $$x_2 > 0$$).
- Vì $$x_1^2 \ge 0$$ và $$x_2 > 0$$, ràng buộc $$x_1^2/x_2 \le 0$$ ép buộc $$x_1 = 0$$ (không hề tồn tại điểm nào làm $$x_1^2/x_2 < 0$$ $$\implies$$ **Slater thất bại!**).
- Giá trị tối ưu gốc: $$f^* = e^0 = 1$$.
- Hàm đối ngẫu với mọi $$u \ge 0$$: $$g(u) = \inf_{x_1, x_2 > 0} \left(e^{-x_1} + u\frac{x_1^2}{x_2}\right) = 0$$ (chỉ cần cho $$x_1$$ lớn tùy ý để $$e^{-x_1} \to 0$$, rồi chọn $$x_2 = x_1^3$$ để $$\frac{x_1^2}{x_2} = \frac{1}{x_1} \to 0$$!).
- Vậy $$g^* = 0 < 1 = f^*$$ — khoảng cách đối ngẫu bằng $$1$$ ngay cả khi bài toán hoàn toàn lồi!

Khi giá trị tối ưu của bài toán gốc và bài toán đối ngẫu bằng nhau ($$f^* = g^*$$), ta nói **tính đối ngẫu mạnh (strong duality)** thỏa mãn. **Điều kiện Slater** là một điều kiện đủ phổ biến bảo đảm tính đối ngẫu mạnh.

## Điều kiện Slater

Nếu bài toán gốc là bài toán tối ưu lồi và tồn tại ít nhất một điểm $$x \in \mathbb{R}^n$$ **khả thi chặt** (strictly feasible), tức thỏa mãn:

>
$$
\begin{equation}
h_1(x)<0,\dots,h_m(x)<0, \text{ and } l_1(x) = 0,\dots,l_r(x) = 0,
\end{equation}
$$

thì tính đối ngẫu mạnh được thỏa mãn ($$f^* = g^*$$).

**Lưu ý quan trọng:** Đối với các ràng buộc bất đẳng thức là hàm affine, điều kiện bất đẳng thức chặt ($$< 0$$) không bắt buộc — chỉ cần thỏa mãn bất đẳng thức không chặt ($$\leq 0$$).

## Ví dụ: Bài toán đối ngẫu của Support Vector Machine (SVM)

Cho $$y \in \{-1, 1\}^n$$ và ma trận dữ liệu $$X \in \mathbb{R}^{n \times p}$$ (với các hàng của $$X$$ là các mẫu $$x_1^T, \dots, x_n^T$$), bài toán SVM lề mềm được phát biểu như sau:

>
$$
\begin{alignat}{1}
\min_{\beta, \beta_0, \xi} & \quad \frac{1}{2}\parallel\beta\parallel_2^2 + C \sum_{i=1}^n \xi_i   \\\\
                                  s.t. & \quad \xi_i \geq 0, i=1,\dots,n   \\\\
                                       & \quad y_i(x_i^T \beta + \beta_0) \geq 1 - \xi_i, i=1,\dots,n
\end{alignat}
$$

Đưa vào các biến đối ngẫu $$v, w \geq 0$$, ta lập hàm Lagrangian:

>
$$
\begin{equation}
L(\beta,\beta_0,\xi,v,w) = \frac{1}{2} \parallel\beta\parallel_2^2 + C\sum_{i=1}^n \xi_i - \sum_{i=1}^n v_i \xi_i +  \sum_{i=1}^n w_i (1-\xi_i - y_i(x_i^T\beta + \beta_0))
\end{equation}
$$

Cực tiểu hóa theo $$\beta, \beta_0, \xi$$, ta thu được hàm đối ngẫu Lagrange:

>
$$
g(v,w) = 
\begin{cases}
-\frac{1}{2} w^T\tilde{X}\tilde{X}^T w +  1^Tw, &\text{if $w=C1-v, w^Ty=0$} \\\\
-\infty, &\text{otherwise}
\end{cases}
$$

trong đó $$\tilde{X} = \text{diag}(y) X$$. Khử biến bù $$v \geq 0$$ (từ $$w = C\mathbf{1} - v$$ suy ra $$w \leq C\mathbf{1}$$), ta thu được bài toán đối ngẫu của SVM:

>
$$
\begin{alignat}{1}
\max_{w}  & \quad -\frac{1}{2} w^T\tilde{X}\tilde{X}^T w +  1^Tw \\\\
     s.t. &  \quad 0 \leq w \leq C1, w^Ty = 0
\end{alignat}
$$

Vì bài toán gốc có hàm mục tiêu lồi, các ràng buộc bất đẳng thức đều là hàm affine theo $$(\beta, \beta_0, \xi)$$ và luôn tồn tại điểm khả thi, nên điều kiện Slater được thỏa mãn và tính đối ngẫu mạnh đúng đối với SVM.

### Đối ngẫu mạnh và Slater trong khoảng 3 phút

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/strong-duality-slater_vi.mp4"></video>
</div>

Hàm đối ngẫu g(λ) nằm dưới p*, khoảng cách đối ngẫu làm chứng chỉ, hình (u, t) của đường tì, và một bài lồi không thỏa Slater có khoảng cách bằng 1.
