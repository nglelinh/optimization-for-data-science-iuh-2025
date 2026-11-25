---
layout: post
title: 27-03 Chiều nghịch và lan truyền ngược
chapter: '27'
order: 4
owner: Nguyen Le Linh
categories:
- chapter27
lang: vi
lesson_type: required
---

Nếu có một thuật toán duy nhất xứng đáng được gọi là "đòn bẩy tỷ đô" tạo nên kỷ nguyên học sâu hiện đại, đó chắc chắn là **Vi phân tự động chiều nghịch (Reverse-Mode AD)** — mà trong mạng nơ-ron ta quen gọi là **lan truyền ngược (backpropagation)**.

Bí mật kinh tế phi thường của chế độ nghịch nằm ở định lý Baur–Strassen (1983): dù hàm mất mát vô hướng $$\ell(w)$$ phụ thuộc vào **100 tỷ tham số**, chỉ cần chạy một lượt thuận lưu lại các giá trị trung gian rồi đi ngược đồ thị đúng **một lần duy nhất**, ta thu được toàn bộ 100 tỷ đạo hàm riêng với tổng chi phí phép tính không quá $$4$$–$$5$$ lần chi phí lượt thuận! Không có định lý này, mọi mô hình AI hiện đại đều sẽ mất hàng thiên niên kỷ để tính nổi một bước gradient.

## Kiến thức cần nhớ: Ba trụ cột của AD chiều nghịch và Lan truyền ngược

Để làm chủ hoàn toàn cơ chế của `loss.backward()` trong PyTorch và `jax.grad`, hãy nắm chắc ba trụ cột sau:

- **Lượt thuận lưu trữ & Lượt nghịch cộng dồn (Adjoint Accumulation):** Gắn cho mỗi nút $$v$$ biến liên hợp $$\bar{v} = \frac{\partial \ell}{\partial v}$$. Bắt đầu từ $$\bar{\ell} = 1$$, ta đi ngược thứ tự topo và cộng dồn $$\bar{u} \mathrel{+}= \bar{v} \cdot \frac{\partial v}{\partial u}$$ qua mọi mũi tên đi ra khỏi $$u$$.
- **Tích Vector–Jacobian (VJP) và Chi phí $$O(m)$$:** Một lượt nghịch tính chính xác $$\bar{y}^T J_f(x)$$ (một tổ hợp tuyến tính các *hàng* của Jacobian). Khi đầu ra là hàm mất mát vô hướng ($$m = 1$$), chỉ cần đúng **1 lượt nghịch** để lấy toàn bộ gradient $$\nabla_w \ell \in \mathbb{R}^n$$ — độc lập hoàn toàn với $$n$$!
- **Đánh đổi Bộ nhớ – Tính toán (Memory Wall & Gradient Checkpointing):** Điểm yếu duy nhất của chế độ nghịch là phải giữ lại các giá trị kích hoạt trung gian từ lượt thuận (ví dụ $$v_1, v_2$$ trong phép nhân $$v_1 v_2$$) cho tới khi lượt nghịch dùng xong. Khi huấn luyện mạng rất sâu, kỹ thuật *activation checkpointing* chấp nhận bỏ bớt một số nút trung gian rồi tính lại cục bộ lúc đi ngược để tiết kiệm bộ nhớ GPU.

### Giải thích: Chạy tay 1 lượt AD chiều nghịch lấy trọn gradient của $$f(x_1, x_2) = x_1 x_2 + e^{x_1}$$

Ta dùng lại đúng hàm và điểm $$(x_1, x_2) = (0,\; 3)$$ của Bài 27-02 để đối chiếu trực tiếp với chiều thuận!

1. **Pha 1 — Lượt thuận (tính và lưu giá trị các nút vào bộ nhớ):**
   $$v_1 = 0, \qquad v_2 = 3, \qquad v_3 = v_1 v_2 = 0, \qquad v_4 = e^{v_1} = 1, \qquad v_5 = v_3 + v_4 = 1.$$
2. **Pha 2 — Lượt nghịch (khởi tạo $$\bar{v}_5 = 1$$, các $$\bar{v}_k = 0$$ rồi đi ngược từ $$v_5$$ về $$v_1$$):**
   - *Qua nút $$v_5 = v_3 + v_4$$:*
     $$\bar{v}_3 \mathrel{+}= \bar{v}_5 \cdot 1 = 1, \qquad \bar{v}_4 \mathrel{+}= \bar{v}_5 \cdot 1 = 1.$$
   - *Qua nút $$v_4 = e^{v_1}$$ (cần dùng lại $$v_1 = 0$$ đã lưu!):*
     $$\bar{v}_1 \mathrel{+}= \bar{v}_4 \cdot e^{v_1} = 1 \cdot e^0 = 1.$$
   - *Qua nút $$v_3 = v_1 \cdot v_2$$ (cần dùng lại $$v_1 = 0, v_2 = 3$$ đã lưu!):*
     $$\bar{v}_1 \mathrel{+}= \bar{v}_3 \cdot v_2 = 1 \cdot 3 = 3 \implies \text{Tổng } \bar{v}_1 = 1 + 3 = 4!$$
     $$\bar{v}_2 \mathrel{+}= \bar{v}_3 \cdot v_1 = 1 \cdot 0 = 0.$$
3. **Kết quả sau đúng 1 lượt đi ngược:** Ta đồng thời nhận được **cả vector gradient** $$\nabla f(0, 3) = (\bar{v}_1,\; \bar{v}_2) = (4,\; 0)$$ — đặc biệt chú ý cách hai nhánh từ $$v_4$$ (đóng góp $$1$$) và $$v_3$$ (đóng góp $$3$$) tự động cộng dồn tại $$\bar{v}_1 = 4$$!

**Vi phân tự động chiều nghịch (reverse-mode AD)** gắn cho mỗi nút $$v$$ một biến **liên hợp (adjoint)** $$\bar v = \frac{\partial \ell}{\partial v}$$ đối với đầu ra vô hướng $$\ell$$. Sau lượt thuận lưu lại các giá trị trung gian, thuật toán duyệt *ngược* đồ thị và cộng dồn đạo hàm:

$$
\bar u \mathrel{+}= \bar v\cdot \partial_u h
\quad\text{khi } v=h(u,\ldots).
$$

Chỉ trong một lượt duyệt ngược duy nhất, thuật toán thu được toàn bộ gradient $$\nabla_w \ell$$ — tương ứng với một **tích vector–Jacobian (VJP)** $$(\nabla \ell)^\top J$$. Chi phí tính toán chỉ gấp một hằng số nhỏ lần chi phí lượt thuận và *không phụ thuộc vào số lượng tham số*. Tính chất này chính là nền tảng giúp việc huấn luyện các mạng nơ-ron sâu hàng triệu hoặc hàng tỷ tham số trở nên khả thi.

**Lan truyền ngược (backpropagation)** là trường hợp riêng của AD chiều nghịch áp dụng cho mạng nơ-ron nhiều lớp, trong đó biến liên hợp tại lớp $$k$$ chính là tín hiệu sai số $$\delta^{(k)}$$ quen thuộc (dùng $$k$$ cho chỉ số lớp vì $$\ell$$ đã là hàm mất mát):

$$
\delta^{(k)} = \bigl(W^{(k+1)\top}\delta^{(k+1)}\bigr)\odot \phi'(z^{(k)}).
$$

Về bản chất, không có phép biến đổi đặc biệt nào ngoài quy tắc dây chuyền: mỗi phép nhân ma trận và hàm kích hoạt chỉ là một nút sơ cấp với Jacobian cục bộ đã biết.

```python
# Ví dụ vô hướng: ℓ = (w2 * relu(w1 * x) - y)**2
x, y = 1.5, 0.3
w1, w2 = 0.8, -0.4
z = w1 * x
h = max(z, 0.0)
pred = w2 * h
ell = (pred - y) ** 2
d_ell = 1.0
d_pred = d_ell * 2 * (pred - y)
d_w2 = d_pred * h
d_h = d_pred * w2
d_z = d_h * (1.0 if z > 0 else 0.0)
d_w1 = d_z * x
print(d_w1, d_w2)
```

Bạn có thể đối chiếu kết quả trên với PyTorch bằng cách dựng cùng biểu thức với các tensor đặt `requires_grad=True` rồi gọi `ell.backward()`.

**Đánh đổi bộ nhớ.** Chế độ nghịch phải lưu lại các giá trị trung gian của lượt thuận để dùng khi duyệt ngược. Kỹ thuật *gradient checkpointing* (tính lại một phần lượt thuận khi cần) đánh đổi thời gian tính toán lấy dung lượng bộ nhớ RAM/VRAM khi huấn luyện mô hình lớn — đây là kỹ thuật quản lý bộ nhớ trong cài đặt, không làm thay đổi giá trị đạo hàm.

Tóm lại, hãy ưu tiên chế độ thuận khi bài toán có ít đầu vào và nhiều đầu ra, còn ưu tiên chế độ nghịch khi có một hàm mất mát vô hướng và rất nhiều tham số. Sự kết hợp hai chế độ (chẳng hạn tính tích Hessian–vector bằng lược đồ thuận-trên-nghịch) cho phép các phương pháp bậc hai và tối ưu hai mức giữ chi phí tuyến tính theo số chiều.

### Chế độ thuận và nghịch trong khoảng 3 phút

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/autodiff-forward-reverse_vi.mp4"></video>
</div>

Đồ thị tính toán của x₁x₂ + sin x₁: tiếp tuyến và số đối ngẫu, adjoint đi ngược, ví dụ ReLU của bài 27-03, và đếm số lượt quét.
