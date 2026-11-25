---
layout: post
title: '17-02 Phương pháp điểm trong gốc-đối ngẫu'
chapter: '17'
order: 3
owner: Minjoo Lee
categories:
- chapter17
lang: vi
---

Trong phương pháp chắn cổ điển, mỗi khi tăng $$t$$ lên $$\mu t$$, ta phải dừng lại giữa đường để giải chính xác bài toán định tâm bằng nhiều bước Newton — giống như một người leo núi cứ đi được vài chục mét lại dựng lều đo đạc lại bản đồ thật tỉ mỉ. Phương pháp điểm trong gốc–đối ngẫu đặt ra một triết lý táo bạo hơn hẳn: **vừa bước đi, vừa chỉnh hướng**, cập nhật đồng thời cả $$(x, u, v)$$ bằng duy nhất một bước Newton mà thậm chí không cần bắt buộc điểm hiện tại phải nằm sẵn trên mặt phẳng khả thi $$Ax = b$$.

## Kiến thức cần nhớ: Bốn mảnh ghép tạo nên lợi thế của PD-IPM

Để hiểu đúng bảng so sánh giữa phương pháp chắn và phương pháp điểm trong gốc–đối ngẫu, hãy tách riêng bốn khía cạnh thiết kế thuật toán:

- **Chiến lược vòng lặp đơn (Single-Loop Update):** Thay vì cấu trúc hai vòng lặp lồng nhau (outer loop tăng $$t$$, inner loop chạy Newton định tâm), PD-IPM chỉ có một vòng lặp duy nhất: mỗi bước tính một hướng Newton và cập nhật ngay $$\tau$$.
- **Khởi tạo không khả thi (Infeasible Start):** Trong nhiều bài toán thực tế, ngay cả việc tìm một điểm ban đầu thỏa mãn $$Ax^{(0)} = b$$ cũng tốn kém. PD-IPM chỉ yêu cầu $$h(x^{(0)}) < 0$$ và $$u^{(0)} > 0$$, còn phần dư đẳng thức $$Ax - b$$ được triệt tiêu dần cùng lúc với phần dư đối ngẫu.
- **Định hướng đồng thời gốc–đối ngẫu (Coupled Primal-Dual Direction):** Bước Newton của PD-IPM lấy thông tin độ cong từ cả $$\nabla^2 f(x)$$ lẫn các biến đối ngẫu $$u$$, giúp hướng đi bám đường trung tâm mượt hơn và tránh hiện tượng lệch hướng khi tiến gần biên.
- **Tốc độ hội tụ siêu tuyến tính thực tiễn:** Khi đủ gần nghiệm tối ưu và giảm $$\tau$$ linh hoạt theo khoảng cách đối ngẫu hiện tại, PD-IPM thường đạt hội tụ siêu tuyến tính (thậm chí bậc hai trong các biến thể predictor-corrector), vượt xa tốc độ tuyến tính của phương pháp chắn thuần túy.

### Giải thích: Quan sát một điểm lặp không khả thi vẫn có thể "tự kéo" về miền khả thi

Xét bài toán quy hoạch bậc hai 2 biến:

$$\min_{x_1, x_2} \; \frac{1}{2}(x_1^2 + x_2^2) \qquad \text{với điều kiện} \qquad x_1 + x_2 = 2, \; -x_1 \le 0, \; -x_2 \le 0.$$

Nghiệm tối ưu là $$x^\star = (1, 1)$$, $$u^\star = (0, 0)$$, $$v^\star = -1$$. Giả sử ta khởi tạo tại một điểm **không khả thi đẳng thức** $$x^{(0)} = (2, 1)$$ (vì $$2 + 1 = 3 \ne 2$$), nhưng vẫn nằm chặt trong miền bất đẳng thức $$(x_1, x_2 > 0)$$, cùng $$u^{(0)} = (0.5, 0.5)$$, $$v^{(0)} = -1$$, và chọn $$\tau = 0.1$$:

1. **Đo ba độ lệch (phần dư):**
   - Lệch ràng buộc đẳng thức: $$r_{\text{prim}} = x_1 + x_2 - 2 = 2 + 1 - 2 = +1$$.
   - Lệch điều kiện dừng (đối ngẫu): $$r_{\text{dual}} = \nabla f(x) - u + v\mathbf{1} = \begin{bmatrix} 2 - 0.5 - 1 \\ 1 - 0.5 - 1 \end{bmatrix} = \begin{bmatrix} 0.5 \\ -0.5 \end{bmatrix}$$.
   - Lệch bù chặt bị nhiễu: $$r_{\text{cent}} = \begin{bmatrix} -u_1 x_1 + \tau \\ -u_2 x_2 + \tau \end{bmatrix} = \begin{bmatrix} -1 + 0.1 \\ -0.5 + 0.1 \end{bmatrix} = \begin{bmatrix} -0.9 \\ -0.4 \end{bmatrix}$$.
2. **Tác dụng của bước Newton gốc–đối ngẫu:** Hệ tuyến tính Newton buộc $$\Delta x_1 + \Delta x_2 = -r_{\text{prim}} = -1$$. Do đó, ngay khi cập nhật với độ dài bước $$\theta \in (0, 1]$$, sai số ràng buộc đẳng thức mới giảm chính xác theo tỉ lệ $$(1 - \theta) r_{\text{prim}}$$. Nếu lấy $$\theta = 1$$, điểm lặp trở nên khả thi đẳng thức **ngay lập tức chỉ sau 1 bước** mà không cần bước Pha I (Phase I) riêng biệt!

---

Tương tự phương pháp chắn, **phương pháp điểm trong gốc-đối ngẫu** cũng nhằm tính xấp xỉ các điểm dọc theo đường trung tâm. Tuy nhiên, giữa hai phương pháp có một số điểm khác biệt quan trọng.

## Khác biệt giữa phương pháp điểm trong gốc-đối ngẫu và phương pháp chắn
* Thông thường chỉ thực hiện **một bước Newton** ở mỗi vòng lặp (không cần vòng lặp trong riêng cho bước định tâm — centering).
* **Các điểm lặp không nhất thiết phải khả thi** trong quá trình chạy (thuật toán đưa điểm lặp tiến dần về miền khả thi kết hợp với tìm kiếm theo đường lui — backtracking line search).
* Thường **hiệu quả hơn** trong thực tế; đặc biệt dưới các điều kiện phù hợp, phương pháp đạt tốc độ hội tụ nhanh hơn hội tụ tuyến tính.
* Kém trực quan hơn một chút so với phương pháp chắn.
