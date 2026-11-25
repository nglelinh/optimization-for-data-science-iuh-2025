---
layout: post
title: 05-03 Quy Hoạch Bậc Hai với Ràng buộc Bậc Hai (QCQP)
chapter: '05'
order: 9
owner: Hooncheol Shin
categories:
- chapter05
lang: vi
---

Trong Quy hoạch Bậc hai (QP), hàm mục tiêu đã có độ cong bậc hai nhưng tập khả thi vẫn bị đóng khung bởi các bức tường phẳng tuyến tính. Thế nhưng ngoài đời thực, nhiều giới hạn vật lý mang hình dạng **cong tròn hoặc ellipsoid**: năng lượng phát sóng của một dàn ăng-ten không vượt quá $$P_{\max}$$ ($$\|x\|_2^2 \le P_{\max}$$), hay phương sai rủi ro của danh mục đầu tư không vượt quá ngưỡng $$\sigma_{\max}^2$$ ($$x^T \Sigma x \le \sigma_{\max}^2$$).

Khi ta cho phép cả hàm mục tiêu lẫn các ràng buộc bất đẳng thức đều là các hàm bậc hai lồi, ta bước lên nấc thang mới mang tên **QCQP (Quadratically Constrained Quadratic Programming)** — lớp bài toán lồi tổng quát hóa trực tiếp QP và là tiền đề ngay trước Quy hoạch Nón Bậc hai (SOCP).

## Kiến thức cần nhớ: Khi tập khả thi là giao của các khối Ellipsoid

Ba trụ cột sau định hình toàn bộ bản chất của QCQP lồi:

- **Điều kiện lồi cho mọi ma trận bậc hai:** Một bài QCQP có dạng $$\min \frac{1}{2}x^T P_0 x + q_0^T x + r_0$$ với ràng buộc $$\frac{1}{2}x^T P_i x + q_i^T x + r_i \le 0$$ ($$i = 1, \dots, m$$) và $$Ax = b$$. Bài toán là **lồi** khi và chỉ khi mọi ma trận $$P_0, P_1, \dots, P_m$$ đều nửa xác định dương ($$\in \mathbb{S}_+^n$$). (Nếu chỉ một $$P_i$$ có trị riêng âm, bài toán lập tức trở nên phi lồi và có thể NP-khó!)
- **Hình học giao các Ellipsoid:** Mỗi ràng buộc $$\frac{1}{2}x^T P_i x + q_i^T x + r_i \le 0$$ với $$P_i \succ 0$$ xác định một khối ellipsoid đặc; giao của chúng là một tập lồi có biên cong trơn (trừ các đường giao giữa hai mặt ellipsoid).
- **Hệ phân cấp bao hàm:** Nếu đặt $$P_1 = \dots = P_m = 0$$, QCQP thu về đúng **QP**. Ngược lại, mọi bài QCQP lồi đều chuyển được về **SOCP** nhờ phân rã căn bậc hai ma trận $$P_i = L_i^T L_i$$ (Cholesky), giúp giải hiệu quả bằng bộ giải nón điểm trong!

### Giải thích: Giải tay một bài QCQP tối thiểu hóa khoảng cách trên hình tròn

Xét bài toán QCQP 2 biến:
$$\min_{x \in \mathbb{R}^2} \; f_0(x) = (x_1 - 3)^2 + (x_2 - 4)^2 \quad \text{thỏa mãn} \quad x_1^2 + x_2^2 \le 4.$$

1. **Bước 1 — Viết dưới dạng chuẩn QCQP và kiểm tra tính lồi:**
   - Hàm mục tiêu: $$\frac{1}{2} x^T (2I) x + (-6, -8) x + 25$$, có $$P_0 = 2I \succ 0$$.
   - Ràng buộc: $$\frac{1}{2} x^T (2I) x - 4 \le 0$$, có $$P_1 = 2I \succ 0$$.
   - Vậy đây là QCQP lồi chặt!
2. **Bước 2 — Kiểm tra điểm cực tiểu tự do:**
   Cực tiểu tự do của $$f_0$$ là $$x_{\text{free}} = (3, 4)$$. Kiểm tra ràng buộc: $$3^2 + 4^2 = 25 > 4$$ (không khả thi!). Do đó nghiệm tối ưu buộc phải nằm trên biên đường tròn $$x_1^2 + x_2^2 = 4$$ (bán kính $$R = 2$$).
3. **Bước 3 — Dùng trực giác hình học (hoặc KKT):**
   Bài toán tương đương tìm điểm trên hình tròn tâm $$(0, 0)$$ bán kính $$2$$ gần điểm $$a = (3, 4)$$ nhất!
   Khoảng cách từ gốc tọa độ đến $$a$$ là $$\|a\|_2 = \sqrt{3^2 + 4^2} = 5$$.
   Điểm gần nhất nằm đúng trên tia nối gốc tọa độ tới $$a$$ với độ dài $$2$$:
   $$x^\star = 2 \cdot \frac{(3, 4)}{5} = (1.2,\; 1.6).$$
4. **Bước 4 — Kiểm chứng KKT:**
   Tại $$x^\star = (1.2, 1.6)$$, $$\nabla f_0(x^\star) = 2(x^\star - a) = (-3.6, -4.8)$$, còn $$\nabla g_1(x^\star) = 2x^\star = (2.4, 3.2)$$.
   Ta thấy $$\nabla f_0(x^\star) + \lambda \nabla g_1(x^\star) = 0$$ với nhân tử Lagrange $$\lambda = 1.5 > 0$$! Giá trị tối ưu là $$f_0^\star = (5 - 2)^2 = 9$$.

---

Nếu các ràng buộc bất đẳng thức tuyến tính trong một bài toán quy hoạch bậc hai được thay bằng các ràng buộc bậc hai lồi, ta thu được **bài toán quy hoạch bậc hai có ràng buộc bậc hai** (Quadratically Constrained Quadratic Programming - QCQP).

### Bài toán Quy hoạch Bậc hai có Ràng buộc Bậc hai
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{(1/2)x^T P_0 x + q_0^T x + r_0} \\\\
>    &\text{subject to } &&{(1/2)x^T P_i x + q_i^T x + r_i \leq 0}, \quad i = 1, \dotsc, m\\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&P_i \in \mathbb{S}_{+}^n \text{ với } i = 0, \dotsc, m, \text{ và } A \in \mathbb{R}^{p \times n}.
>\end{align} $$

## Mối quan hệ giữa QP và QCQP
Khi $$P_i = 0$$ với mọi $$i = 1, \dotsc, m$$ trong các ràng buộc của QCQP, bài toán rút gọn về một bài toán QP. Do đó, QP là một trường hợp đặc biệt của QCQP, ký hiệu $$QP \subseteq QCQP$$.

### Nhắc lại: Bài toán Quy hoạch Bậc hai
>$$
>\begin{align}
>    &\text{minimize}_{x} &&{(1/2)x^T P x + q^T x + r} \\\\
>    &\text{subject to } &&{Gx \preceq h} \\\\
>    & &&{Ax = b},\\\\
>    & \text{where } &&P \in \mathbb{S}_{+}^n, \; G \in \mathbb{R}^{m \times n}, \text{ và } A \in \mathbb{R}^{p \times n}.
>\end{align} $$