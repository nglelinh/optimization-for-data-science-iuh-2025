---
layout: post
title: 04-07 Biến phụ
chapter: '04'
order: 8
owner: YoungJae Choung
categories:
- chapter04
lang: vi
lesson_type: required
---

Trong quản trị sản xuất, nếu nhà máy có 100 giờ máy nhưng kế hoạch chỉ dùng hết 82 giờ, thì 18 giờ còn thừa không phải là con số vô nghĩa — nó chính là **năng lực dự phòng** (slack) cho biết phân xưởng đó chưa bị quá tải. Trong tối ưu hóa toán học, việc đặt tên chính thức cho phần dự phòng ấy bằng một **biến phụ (slack variable)** $$s_i \ge 0$$ tạo ra một phép biến hình ngoạn mục: mọi bất đẳng thức rườm rà $$g_i(x) \le 0$$ đồng loạt biến thành đẳng thức gọn gàng $$g_i(x) + s_i = 0$$.

Tuy nhiên, phép biến đổi này ẩn chứa một cái bẫy kinh điển mà người mới rất dễ mắc phải: nếu $$g_i(x)$$ là hàm lồi *phi tuyến*, thì đẳng thức $$g_i(x) + s_i = 0$$ sẽ **phá vỡ tính lồi** của dạng chuẩn! Vì thế, bài học này không chỉ giới thiệu cơ chế thêm biến phụ (xương sống của thuật toán Simplex và phương pháp điểm trong), mà còn chỉ rõ ranh giới chính xác khi nào nó giữ nguyên tính lồi.

## Kiến thức cần nhớ: Vai trò của biến phụ trong lý thuyết và thuật toán

Ba trụ cột sau giúp bạn sử dụng biến phụ đúng chỗ và tránh bẫy mất tính lồi:

- **Từ bất đẳng thức sang đẳng thức + nón không âm:** Khi $$g_i(x) = a_i^T x - b_i$$ là hàm affine (như trong Quy hoạch Tuyến tính LP), việc thêm $$s_i \ge 0$$ biến hệ $$Ax \le b$$ thành $$Ax + s = b,\; s \ge 0$$. Tập khả thi biến thành giao của một không gian con affine với góc phần tư không âm — đúng dạng chuẩn mà thuật toán Simplex cần.
- **Cạm bẫy bảo toàn tính lồi với $$g_i$$ phi tuyến:** Nếu $$g_i(x) = x^2 - 1 \le 0$$, việc viết thành $$x^2 - 1 + s = 0, s \ge 0$$ tạo ra ràng buộc đẳng thức *phi affine*! Tập các cặp $$(x, s)$$ thỏa $$s = 1 - x^2$$ là một đường parabol (tập **không lồi**), dù hình chiếu của nó lên trục $$x$$ vẫn là đoạn $$[-1, 1]$$.
- **Ý nghĩa kinh tế & Độ lệch bù (Complementary Slackness):** Giá trị của $$s_i^\star$$ cho biết ngay lập tức ràng buộc thứ $$i$$ có tích cực hay không: $$s_i^\star = 0$$ nghĩa là tài nguyên thứ $$i$$ đã cạn kiệt (nút thắt cổ chai), còn $$s_i^\star > 0$$ nghĩa là tài nguyên vẫn còn dư và giá bóng (nhân tử đối ngẫu $$\lambda_i^\star$$) của nó bằng $$0$$.

### Giải thích: Chuyển bài toán phân bổ tài nguyên sang dạng biến phụ và đọc ý nghĩa nghiệm

Xét bài toán tối đa hóa lợi nhuận (tương đương cực tiểu hóa $$-3x_1 - 5x_2$$) của một xưởng mộc:
$$\max_{x_1, x_2 \ge 0} \; 3x_1 + 5x_2 \quad \text{thỏa mãn} \quad \begin{cases} x_1 \le 4 & \text{(gỗ)} \\ 2x_2 \le 12 & \text{(nhân công)} \\ 3x_1 + 2x_2 \le 18 & \text{(thời gian máy)} \end{cases}$$

1. **Bước 1 — Đưa vào 3 biến phụ không âm $$s_1, s_2, s_3 \ge 0$$:**
   $$\begin{cases} x_1 + s_1 = 4 \\ 2x_2 + s_2 = 12 \\ 3x_1 + 2x_2 + s_3 = 18 \end{cases}, \qquad x_1, x_2, s_1, s_2, s_3 \ge 0.$$
   Vì cả 3 ràng buộc gốc đều tuyến tính, bài toán mở rộng hoàn toàn là một bài toán LP lồi chuẩn.
2. **Bước 2 — Kiểm tra tại phương án tối ưu $$x^\star = (2, 6)$$:**
   Lợi nhuận đạt $$3(2) + 5(6) = 36$$. Thay $$x_1 = 2, x_2 = 6$$ vào các phương trình biến phụ:
   - $$s_1^\star = 4 - 2 = 2 > 0$$ (còn dư 2 đơn vị gỗ — ràng buộc **không tích cực**).
   - $$s_2^\star = 12 - 2(6) = 0$$ (dùng hết nhân công — ràng buộc **tích cực**).
   - $$s_3^\star = 18 - 3(2) - 2(6) = 0$$ (dùng hết thời gian máy — ràng buộc **tích cực**).
3. **Bước 3 — Kiểm chứng phản ví dụ phi tuyến:** Nếu ta có ràng buộc lồi $$x^2 \le 4$$ và đổi thành $$x^2 + s = 4, s \ge 0$$, lấy hai điểm thỏa mãn là $$P_1 = (2, 0)$$ và $$P_2 = (-2, 0)$$. Trung điểm $$M = (0, 0)$$ lại cho $$0^2 + 0 = 0 \neq 4$$! Do đó, chỉ nên dùng biến phụ thành đẳng thức đối với ràng buộc **tuyến tính/affine**.

---

# Biến phụ trong Tối ưu hóa Lồi

## Giới thiệu và động lực

Biến phụ (slack variable) là các biến phụ trợ được đưa thêm vào nhằm chuyển đổi ràng buộc bất đẳng thức thành ràng buộc đẳng thức kèm điều kiện không âm. Phép biến đổi này được sử dụng rộng rãi trong lý thuyết tối ưu hóa, đặc biệt là trong quy hoạch tuyến tính, các phương pháp điểm trong và nhiều thuật toán giải chuẩn khác.

**Tại sao cần dùng biến phụ?**
- Nhiều thuật toán tối ưu hóa được thiết kế để xử lý trực tiếp các ràng buộc đẳng thức kết hợp với điều kiện không âm hiệu quả hơn.
- Biến phụ cho ý nghĩa hình học rõ ràng về mức độ "chặt" (khoảng dư) của từng ràng buộc.
- Đây là bước chuẩn hóa không thể thiếu trong phương pháp đơn hình (Simplex) cho quy hoạch tuyến tính.
- Biến phụ hỗ trợ thuận tiện cho việc phân tích đối ngẫu và phân tích độ nhạy.

## Công thức toán học

Xét bài toán tối ưu hóa lồi dạng chuẩn:

>$$
\begin{aligned}
&\min_x &&f(x) \\
&\text{subject to} &&g_{i}(x) \leq 0, \quad i = 1, \ldots, m\\
&&&Ax = b
\end{aligned}
>$$

Bằng cách đưa vào các **biến phụ** $$s_i \geq 0$$ tương ứng với từng ràng buộc bất đẳng thức, ta có thể viết lại bài toán thành:

>$$
\begin{aligned}
&\min_{x, s} &&f(x)\\
&\text{subject to} &&s_{i} \geq 0, \quad i = 1, \ldots, m\\
&&&g_{i}(x) + s_{i} = 0, \quad i = 1, \ldots, m\\
&&&Ax = b
\end{aligned}
$$

## Giải thích hình học

Biến phụ $$s_i$$ đo lường "khoảng dư" (hay độ lệch so với biên) của ràng buộc thứ $$i$$:

- **$$s_i > 0$$:** Ràng buộc $$g_i(x) \leq 0$$ **không tích cực** (không chặt).
  - Điểm $$x$$ nằm bên trong miền khả thi do ràng buộc thứ $$i$$ xác định.
  - Khi đó $$g_i(x) = -s_i < 0$$.

- **$$s_i = 0$$:** Ràng buộc $$g_i(x) \leq 0$$ **tích cực** (chặt).
  - Điểm $$x$$ nằm đúng trên biên $$g_i(x) = 0$$.
  - Ràng buộc này được thỏa mãn với dấu bằng tại điểm đang xét.

## Ví dụ thực tế: Phân bổ tài nguyên

Xét bài toán phân bổ tài nguyên đơn giản sau:

**Bài toán gốc:**
>$$
\begin{aligned}
&\max &&3x_1 + 2x_2 \\
&\text{thỏa mãn} &&x_1 + x_2 \leq 4 \quad \text{(giờ lao động)}\\
&&&2x_1 + x_2 \leq 6 \quad \text{(đơn vị nguyên liệu)}\\
&&&x_1, x_2 \geq 0
\end{aligned}
>$$

**Sau khi thêm biến phụ:**
>$$
\begin{aligned}
&\max &&3x_1 + 2x_2 \\
&\text{subject to} &&x_1 + x_2 + s_1 = 4\\
&&&2x_1 + x_2 + s_2 = 6\\
&&&x_1, x_2, s_1, s_2 \geq 0
\end{aligned}
>$$

**Ý nghĩa:**
- $$s_1$$: số giờ lao động chưa sử dụng.
- $$s_2$$: số đơn vị nguyên liệu chưa sử dụng.
- Nếu $$s_1 = 0$$ tại nghiệm tối ưu: toàn bộ quỹ giờ lao động đã được sử dụng hết.
- Nếu $$s_2 > 0$$ tại nghiệm tối ưu: vẫn còn một phần nguyên liệu chưa được sử dụng.

## Các tính chất và lưu ý quan trọng

### 1. Tính tương đương của hai bài toán
Bài toán gốc và bài toán sau khi thêm biến phụ **tương đương về mặt toán học**:
- Có cùng giá trị mục tiêu tối ưu.
- Có cùng thành phần nghiệm tối ưu $$x^*$$.
- Giá trị tối ưu $$s_i^*$$ của các biến phụ cho biết trực tiếp ràng buộc nào là tích cực tại nghiệm.

### 2. Điều kiện bảo toàn tính lồi
**Lưu ý quan trọng:** Phép đưa thêm biến phụ chỉ bảo toàn tính lồi của bài toán **khi $$g_i(x)$$ là hàm affine**.

- **Nếu $$g_i(x) = a_i^T x - b_i$$ (affine):** Ràng buộc $$g_i(x) + s_i = 0$$ là đẳng thức affine, nên bài toán viết lại vẫn là bài toán lồi.
- **Nếu $$g_i(x)$$ là hàm lồi phi tuyến:** Ràng buộc đẳng thức $$g_i(x) + s_i = 0$$ không còn là hàm affine, làm phá vỡ tính lồi của bài toán.

### 3. Tác động đến kích thước bài toán
- Bài toán gốc có $$n$$ biến.
- Bài toán với biến phụ có $$n + m$$ biến.
- Đánh đổi: số biến tăng lên nhưng cấu trúc ràng buộc trở nên đồng nhất và dễ xử lý hơn đối với nhiều thuật toán.

## Ví dụ: Chuẩn hóa bài toán quy hoạch tuyến tính

**Dạng bất đẳng thức:**
>$$
\begin{aligned}
&\min &&c^T x \\
&\text{thỏa mãn} &&Ax \leq b\\
&&&x \geq 0
\end{aligned}
>$$

**Dạng chuẩn với biến phụ:**
>$$
\begin{aligned}
&\min &&c^T x \\
&\text{subject to} &&Ax + s = b\\
&&&x, s \geq 0
\end{aligned}
>$$

trong đó $$s \in \mathbb{R}^m$$ là vectơ các biến phụ.

## Các điểm chính

1. **Công cụ chuyển đổi:** Biến phụ chuyển ràng buộc bất đẳng thức thành ràng buộc đẳng thức kèm điều kiện không âm.
2. **Ý nghĩa hình học:** Đo lường khoảng dư so với biên ràng buộc.
3. **Hỗ trợ thuật toán:** Là thành phần chuẩn trong phương pháp đơn hình và nhiều bộ giải tối ưu hóa.
4. **Điều kiện bảo toàn tính lồi:** Chỉ bảo toàn tính lồi đối với các ràng buộc affine.
5. **Ý nghĩa ứng dụng:** Phản ánh trực tiếp lượng tài nguyên dư thừa trong các bài toán phân bổ kinh tế.
