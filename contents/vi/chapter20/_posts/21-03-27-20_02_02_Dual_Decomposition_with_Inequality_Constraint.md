---
layout: post
title: '20-02-02 Phân rã đối ngẫu với ràng buộc bất đẳng thức'
chapter: '20'
order: 6
owner: Hooncheol Shin
categories:
- chapter20
lang: vi
---

Trong thực tế kỹ thuật và kinh tế, phần lớn ràng buộc tài nguyên không phải là đẳng thức cứng ("dùng đúng bằng $$b$$"), mà là **bất đẳng thức hạn mức** $$\sum_{i=1}^B A_i x_i \le b$$ ("không được vượt quá băng thông $$b$$, ngân sách $$b$$ hay công suất đường dây $$b$$"). Khi đổi dấu `=` thành `≤`, thuật toán phân rã đối ngẫu chỉ thay đổi đúng một chi tiết nhỏ nhưng mang ý nghĩa kinh tế sâu sắc: biến đối ngẫu $$u$$ bắt buộc phải không âm $$u \ge 0$$ nhờ phép chiếu $$u^{(k)} = (\cdot)_+$$ — biểu thị rằng **tài nguyên dư thừa luôn có giá bóng bằng 0**!

## Bản đồ kiến thức nền: Ba đặc trưng của phân rã đối ngẫu với ràng buộc bất đẳng thức

Để hiểu trọn vẹn bài 20-02-02 và diễn giải kinh tế học (Price Update) đi kèm, hãy nắm vững ba ý sau:

- **Phép chiếu không âm $$u_+ = \max(0, u)$$ và điều kiện bù chặt:** Với bài toán bất đẳng thức, điều kiện KKT đòi hỏi $$u \ge 0$$ và $$u_j(\sum_i (A_i x_i)_j - b_j) = 0$$. Nếu một tài nguyên $$j$$ không bị dùng hết ($$\sum_i (A_i x_i)_j < b_j$$), phép cập nhật sẽ đẩy $$u_j$$ giảm dần về $$0$$ và giữ chặt tại $$0$$.
- **Thuật toán hạ dưới gradient chiếu trên đối ngẫu (Projected Dual Subgradient):** Bước cập nhật $$u^{(k)} = \left(u^{(k-1)} + t_k(\sum_i A_i x_i^{(k)} - b)\right)_+$$ chính là một bước tăng gradient chiếu lên tập lồi $$u \ge 0$$ cho hàm đối ngẫu $$g(u)$$.
- **Diễn giải điều chỉnh giá theo trạng thái tắc nghẽn:** Trong mạng viễn thông (tối ưu hóa tốc độ truyền TCP), mỗi liên kết $$j$$ có băng thông tối đa $$b_j$$: khi lưu lượng vượt $$b_j$$, giá tắc nghẽn $$u_j$$ tăng lên buộc các luồng dữ liệu tự giảm tốc độ; khi đường truyền thông thoáng, $$u_j$$ tụt về $$0$$!

### Khung giải thích (nên đọc chậm): Tính tay 2 bước phân rã bất đẳng thức (cả trường hợp chặt và trường hợp dư tài nguyên)

Xét 2 người dùng muốn tối ưu lợi ích (tương đương cực tiểu hóa độ lệch so với mức mong muốn $$3$$ và $$2$$) với hạn mức tổng băng thông $$b$$:

$$\min_{x_1, x_2} \; (x_1 - 3)^2 + (x_2 - 2)^2 \qquad \text{với điều kiện} \qquad x_1 + x_2 \le b.$$

Khởi tạo giá ban đầu $$u^{(0)} = 0$$ và bước học $$t = 0.5$$:

1. **Trường hợp 1 — Băng thông thiếu ($$b = 4 < 3 + 2$$):**
   - **Vòng 1 ($$u^{(0)} = 0$$):** Người 1 chọn $$x_1^{(1)} = 3$$, người 2 chọn $$x_2^{(1)} = 2$$. Tổng $$= 5 > 4$$ (vượt hạn mức $$+1$$).
     Cập nhật giá: $$u^{(1)} = (0 + 0.5(5 - 4))_+ = (0.5)_+ = 0.5$$.
   - **Vòng 2 ($$u^{(1)} = 0.5$$):**
     - Người 1 giải $$\min (x_1 - 3)^2 + 0.5x_1 \implies x_1^{(2)} = 3 - 0.25 = 2.75$$.
     - Người 2 giải $$\min (x_2 - 2)^2 + 0.5x_2 \implies x_2^{(2)} = 2 - 0.25 = 1.75$$.
     - Tổng $$= 4.5 > 4$$ (chỉ còn vượt $$+0.5$$), cập nhật $$u^{(2)} = (0.5 + 0.5(0.5))_+ = 0.75$$, tiến thẳng về nghiệm tối ưu $$u^\star = 1, x^\star = (2.5, 1.5)$$!
2. **Trường hợp 2 — Băng thông dư thừa ($$b = 6 > 3 + 2$$):**
   - **Vòng 1 ($$u^{(0)} = 0$$):** $$x_1^{(1)} = 3, x_2^{(1)} = 2$$, tổng $$= 5 < 6$$ (dư $$-1$$).
   - Phép chiếu cắt âm: $$u^{(1)} = (0 + 0.5(-1))_+ = (-0.5)_+ = 0$$! Giá bóng bị ghim tại $$0$$ và thuật toán dừng ngay tại nghiệm tối ưu $$(3, 2)$$.

---

Xét bài toán tương tự phần trước nhưng thay ràng buộc đẳng thức bằng ràng buộc bất đẳng thức tuyến tính:
> $$
> \begin{equation}
> \min_x \sum_{i=1}^B f_i(x_i) \quad \text{subject to} \quad \sum_{i=1}^B A_i x_i \leq b
> \end{equation}
> $$

## Phân rã đối ngẫu (phương pháp subgradient chiếu)
Do ràng buộc có dạng bất đẳng thức, biến đối ngẫu phải thỏa mãn điều kiện không âm $$u \geq 0$$. Vì vậy, sau bước cập nhật $$u$$, ta chiếu kết quả lên góc phần tư không âm:

> $$
> \begin{alignat}{1}
> x_i^{(k)} & \in \arg \min_{x_i} f_i(x_i) + (u^{(k-1)})^T A_i x_i, \quad i=1,\dots,B  \\
> u^{(k)}   & = \left( u^{(k-1)} + t_k \left(\sum_{i=1}^B A_i x_i^{(k)} - b \right) \right)_+
> \end{alignat}
> $$

trong đó $$u_{+}$$ ký hiệu phép lấy phần không âm theo từng thành phần: $$(u_+)_i = \max \left\{0, u_i \right\}$$ ($$i = 1, \dots, m$$). Hai bước trên được lặp lại với $$k = 1, 2, 3, \dots$$

#### Diễn giải theo cơ chế điều phối giá (price coordination)
Theo Vandenberghe, thuật toán phân rã đối ngẫu có cách hiểu kinh tế trực quan như sau:
> * Hệ thống gồm $$B$$ đơn vị độc lập, mỗi đơn vị tự chọn phương án $$x_i$$ của mình.
> * Mỗi ràng buộc biểu diễn giới hạn của một nguồn lực dùng chung giữa $$B$$ đơn vị, còn biến đối ngẫu $$u_j$$ đóng vai trò đơn giá của nguồn lực thứ $$j$$.
> * Các mức giá được cập nhật theo công thức:
 \begin{equation}
 u_j^{+} = (u_j - t s_j)_{+}, \quad  j=1,\dots,m
 \end{equation}
>
> $$\quad$$ trong đó $$s = b - \sum_{i=1}^B A_ix_i$$ là lượng dư (slack) của nguồn lực: \\
> $$\qquad$$ - nếu $$s_j < 0$$ (nguồn lực $$j$$ bị sử dụng vượt mức cho phép), giá $$u_j$$ được tăng lên; \\
> $$\qquad$$ - nếu $$s_j > 0$$ (nguồn lực $$j$$ vẫn còn dư), giá $$u_j$$ được giảm xuống; \\
> $$\qquad$$ - mức giá luôn được giữ không âm ($$u_j \ge 0$$).
