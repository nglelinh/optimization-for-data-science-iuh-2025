---
layout: post
title: '17-02-03 Thuật toán gốc-đối ngẫu (Primal-Dual Algorithm)'
chapter: '17'
order: 6
owner: Minjoo Lee
categories:
- chapter17
lang: vi
---

Có hướng Newton rồi, nhưng nếu cứ nhắm mắt bước trọn độ dài $$\theta = 1$$ thì chuyện gì sẽ xảy ra? Một biến đối ngẫu $$u_i$$ có thể nhảy vọt xuống số âm, hoặc một ràng buộc $$h_i(x)$$ có thể vượt qua $$0$$ ra ngoài miền xác định, khiến toàn bộ thuật toán sụp đổ ngay lập tức. Thuật toán gốc–đối ngẫu hoàn chỉnh kết hợp hai cơ chế kiểm soát nhịp độ cực kỳ tinh tế: chọn tham số định tâm $$\tau = \sigma \tau(x, u)$$ để quyết định độ "tham lam" khi thu hẹp khoảng cách đối ngẫu, và tìm kiếm theo đường lui hai tầng để bảo đảm cả tính điểm trong lẫn mức giảm chuẩn phần dư.

## Kiến thức cần nhớ: Bốn cơ chế vận hành một vòng lặp PD-IPM hoàn chỉnh

Để tự lập trình được một bộ giải gốc–đối ngẫu chạy ổn định từ đầu đến cuối, cần hiểu rõ vai trò của từng bánh răng sau:

- **Tỉ lệ định tâm $$\sigma \in (0, 1)$$ và tham số mục tiêu $$\tau = \sigma \eta / m$$:** Nếu $$\sigma$$ quá gần $$0$$ (đi thẳng vào biên), bước Newton dễ bị cụt vì đụng rào $$u > 0$$ hoặc $$h(x) < 0$$. Nếu $$\sigma$$ quá gần $$1$$, thuật toán chỉ lo định tâm mà giảm $$\eta$$ rất chậm. Chọn $$\sigma \approx 0.1$$ (tương ứng $$\mu = 10$$) là điểm cân bằng kinh điển.
- **Quy tắc "phần trăm tới biên" (Fraction-to-the-Boundary Rule):** Trước khi tìm kiếm theo đường lui, ta tính bước lớn nhất $$\theta_{\max}$$ sao cho $$u + \theta \Delta u > 0$$ (thường nhân hệ số an toàn $$0.99$$) để chặn ngay nguy cơ vi phạm $$u > 0$$ mà không cần thử sai.
- **Tìm kiếm theo đường lui bảo toàn tính điểm trong:** Giảm dần $$\theta \leftarrow \beta \theta$$ cho đến khi mọi bất đẳng thức gốc đều chặt $$h_i(x + \theta\Delta x) < 0$$, rồi tiếp tục giảm cho đến khi chuẩn vector phần dư tổng giảm đủ: $$\|r_\tau(w + \theta\Delta w)\|_2 \le (1 - \alpha\theta)\|r_\tau(w)\|_2$$.
- **Tiêu chuẩn dừng kép (Feasibility + Optimality):** Thuật toán chỉ dừng khi sai số khả thi gốc–đối ngẫu nhỏ hơn $$\epsilon_{\text{feas}}$$ VÀ khoảng cách đối ngẫu thay thế $$\eta = -h(x)^T u \le \epsilon$$.

### Giải thích: Tính tay bước cực đại $$\theta_{\max}$$ và kiểm tra điều kiện backtracking

Giả sử tại vòng lặp $$k$$ của một bài toán có $$m = 2$$ ràng buộc bất đẳng thức, ta đang ở trạng thái:

$$h(x^{(k)}) = \begin{bmatrix} -1.0 \\ -0.4 \end{bmatrix}, \qquad u^{(k)} = \begin{bmatrix} 0.5 \\ 0.8 \end{bmatrix}, \qquad \|r_\tau(w^{(k)})\|_2 = 1.20.$$

1. **Tính khoảng cách đối ngẫu thay thế và tham số $$\tau$$ mới (với $$\sigma = 0.2$$):**
   $$\eta = -h(x^{(k)})^T u^{(k)} = (1.0)(0.5) + (0.4)(0.8) = 0.82 \implies \tau(x^{(k)}, u^{(k)}) = \frac{0.82}{2} = 0.41.$$
   Suy ra tham số mục tiêu cho bước Newton là $$\tau = \sigma \cdot 0.41 = 0.2 \times 0.41 = 0.082$$.
2. **Xác định bước cực đại giữ $$u > 0$$:** Giả sử giải hệ Newton ta nhận được $$\Delta u = (-1.0, \; +0.2)^T$$. Thành phần thứ hai tăng ($$\Delta u_2 > 0$$) nên không giới hạn $$\theta$$; thành phần thứ nhất giảm nên cần:
   $$u_1^{(k)} + \theta \Delta u_1 > 0 \iff 0.5 - 1.0\theta > 0 \iff \theta < 0.5.$$
   Áp dụng hệ số an toàn $$0.99$$, ta đặt bước khởi điểm tìm kiếm theo đường lui là $$\theta_{\max} = \min\{1, \; 0.99 \times 0.5\} = 0.495$$.
3. **Kiểm tra điều kiện giảm đủ (với $$\alpha = 0.01, \beta = 0.5$$):**
   - Thử $$\theta = 0.495$$: kiểm tra $$h(x^{(k)} + 0.495\Delta x) < 0$$. Nếu thỏa mãn, tính chuẩn phần dư mới $$\|r_\tau(w^{(k)} + 0.495\Delta w)\|_2$$ và so sánh với ngưỡng $$(1 - 0.01 \times 0.495) \times 1.20 = 1.19406$$.
   - Nếu chuẩn mới là $$0.65 \le 1.19406$$, ta chấp nhận ngay $$\theta_k = 0.495$$ và cập nhật $$w^{(k+1)} = w^{(k)} + 0.495\Delta w$$; ngược lại, giảm $$\theta \leftarrow 0.5 \times 0.495 = 0.2475$$ rồi kiểm tra lại.

---

Để mô tả thuật toán gốc-đối ngẫu, trước hết ta định nghĩa tham số $$\tau(x, u)$$ như sau:
> $$\tau(x,u) := -\frac{h(x)^Tu}{m} \quad \text{với} \quad h (x) \le 0, u \ge 0$$

Lưu ý rằng hai tham số $$t$$ và $$\mu$$ của phương pháp chắn được viết lại thành $$\tau$$ và $$\sigma$$ trong thuật toán gốc-đối ngẫu:
> $$\tau = \frac{1}{t}, \quad \sigma = \frac{1}{\mu}$$

## Thuật toán gốc-đối ngẫu
Thuật toán gồm các bước sau:
> 1. Chọn $$\sigma \in (0,1)$$.<br>
> 2. Chọn điểm khởi tạo $$(x^0,u^0,v^0)$$ thỏa mãn $$h(x^0) < 0$$ và $$u^0 > 0$$.<br>
> 3. Lặp với $$k = 0, 1, \dots$$:<br>
> $$\quad$$ * Tính bước Newton:<br>
> $$\qquad \quad (x,u,v) = (x^k,u^k,v^k)$$ <br>
> $$\qquad \quad$$ tính $$\tau := \sigma \tau(x^k,u^k)$$<br>
> $$\qquad \quad$$ giải hệ Newton để tìm $$(\Delta x,\Delta u,\Delta v)$$ ứng với $$\tau$$ này<br>
> $$\quad$$ * Chọn độ dài bước $$\theta_k$$ bằng tìm kiếm theo đường lui (backtracking line search).<br>
> $$\quad$$ * Cập nhật biến gốc-đối ngẫu:<br>
> $$\qquad \quad (x^{k+1},u^{k+1},v^{k+1}) := (x^k,u^k,v^k) + \theta_k(\Delta x,\Delta u,\Delta v)$$<br>
> 4. Dừng khi $$-h(x^{k+1})^Tu^{k+1} \le \epsilon$$ và $$(\parallel r_{prim} \parallel^2_2 + \parallel r_{dual} \parallel^2_2)^{1/2} \le \epsilon $$.<br>

Ở mỗi vòng lặp, thuật toán tính một bước Newton $$(\Delta x, \Delta u, \Delta v)$$ rồi cập nhật đồng thời các biến để thu được $$(x^{k+1}, u^{k+1}, v^{k+1})$$. Độ dài bước $$\theta_k$$ được xác định qua tìm kiếm theo đường lui nhằm giữ $$h(x) < 0$$ và $$u > 0$$, đồng thời làm giảm chuẩn phần dư. Thuật toán dừng khi khoảng cách đối ngẫu thay thế và chuẩn phần dư gốc – đối ngẫu đều không vượt quá ngưỡng $$\epsilon$$.

## Tìm kiếm theo đường lui (Backtracking line search)
Vì thuật toán gốc-đối ngẫu chỉ thực hiện một bước Newton mỗi vòng lặp, ta nên xem bước này là một hướng dịch chuyển về phía nghiệm chứ không phải bước nhảy trực tiếp tới nghiệm chính xác. Do đó, cần chọn độ dài bước $$\theta$$ thích hợp cho phép cập nhật:

> $$x^+ = x + \theta \Delta x, \quad  u^+ = u + \theta \Delta u, \quad v^+ = v + \theta \Delta v$$

Quá trình chọn $$\theta$$ nhằm đạt hai mục tiêu:

* Duy trì điều kiện điểm trong $$h(x^+) < 0, u^+ > 0$$.
* Làm giảm chuẩn phần dư $$\parallel r(x,u,v) \parallel$$.

Để thực hiện điều này, ta áp dụng **tìm kiếm theo đường lui nhiều giai đoạn (multi-stage backtracking line search)**:

#### Giai đoạn 1: duy trì tính khả thi đối ngẫu $$u \gt 0$$
Bắt đầu bằng bước lớn nhất $$\theta_{\max} \le 1$$ sao cho $$u + \theta \Delta u \ge 0$$:

> $$\theta_{\max} = \min \Biggl\{1,\  \min \Bigl\{ -\frac{u_i}{\Delta u_i} : \Delta u_i < 0 \Bigr\} \Biggr\}$$

Công thức trên được suy ra trực tiếp từ bất đẳng thức:

> $$\begin{align}
&u + \theta \Delta u && \ge 0  \\\\
\Leftrightarrow \quad &u && \ge -\theta \Delta u \\\\
\Leftrightarrow \quad &- u/\Delta u && \ge \theta \quad  \text{ với các thành phần có }\Delta u \lt 0  \\\\
\end{align}$$

#### Giai đoạn 2: duy trì tính khả thi gốc ngặt $$h(x) \lt 0$$
Chọn các tham số $$\alpha, \beta \in (0,1)$$, khởi tạo $$\theta = 0.99\theta_{\max}$$ (nhờ nhân $$0.99$$ mà $$u^+ > 0$$ ngặt), sau đó:

* Lặp cập nhật $$\theta = \beta\theta$$ cho đến khi $$h_i(x^+) < 0$$ với mọi $$i = 1, \dots, m$$.

Bước này đảm bảo $$x^+$$ nằm trong miền trong của các ràng buộc bất đẳng thức.

#### Giai đoạn 3: giảm chuẩn phần dư $$\parallel r(x,u,v) \parallel$$
* Tiếp tục cập nhật $$\theta = \beta \theta$$ cho đến khi $$\| r(x^+,u^+,v^+) \| \le (1-\alpha \theta) \| r(x,u,v) \|$$.

Điều kiện ở Giai đoạn 3 tương tự điều kiện giảm đủ trong backtracking line search tiêu chuẩn. Vế phải của bất đẳng thức xuất phát từ phương trình Newton:
> $$\begin{align}
\Delta w = (\Delta x, \Delta u, \Delta v) &= -r^{\prime}(w)^{-1} r(w) \\\\
\Leftrightarrow r(w)  &=  -r^{\prime}(w) \Delta w \\\\
\end{align}$$

Thay $$r^{\prime}(w) \Delta w = -r(w)$$ vào khai triển Taylor bậc nhất, ta có:
> $$\begin{align}
r(w + \theta \Delta w) & \approx r(w) +  r^{\prime}(w) (\theta \Delta w) \\\\
&\approx (1-\theta) r(w) \\\\
\end{align}$$

Do đó, với hệ số chiết khấu $$\alpha \in (0, 1)$$, ta yêu cầu mức giảm $$\|r(w + \theta \Delta w)\| \le (1-\alpha \theta) \|r(w)\|$$.
