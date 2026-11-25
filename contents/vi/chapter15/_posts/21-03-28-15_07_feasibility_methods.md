---
layout: post
title: '15-07 Các phương pháp tìm điểm khả thi'
chapter: "15"
order: 13
categories:
- chapter16
owner: "Minjoo Lee"
lang: vi
---

Từ đầu Chương 15 đến giờ, ta luôn âm thầm giả định một điều kiện "trời cho": *ta đã có sẵn một điểm xuất phát $$x^{(0)}$$ khả thi chặt* ($$h_i(x^{(0)}) < 0$$ với mọi $$i$$ và $$Ax^{(0)} = b$$) để thả vào phương pháp chắn. Nhưng trên thực tế, với một bài toán có 500 ràng buộc lồng ghép chằng chịt, **chỉ riêng việc tìm ra MỘT điểm nằm bên trong miền khả thi thôi đôi khi đã khó ngang ngửa việc giải bài toán gốc!**

Lời giải đầy thông minh cho bài toán "con gà và quả trứng" này gọi là **Phương pháp Pha I (Phase I)**: ta đặt thêm một biến phụ vô hướng $$s$$ (hoặc vectơ $$s$$) đo *mức độ vi phạm ràng buộc*, nới lỏng các bức tường thành $$h_i(x) \le s$$, rồi dùng chính phương pháp chắn để **cực tiểu hóa $$s$$**! Điều kỳ diệu là với bài toán Pha I này, việc tìm điểm khả thi chặt ban đầu dễ như trở bàn tay: chọn bất kỳ $$x_0$$ nào thỏa $$Ax_0 = b$$ rồi chọn $$s_0 > \max_i h_i(x_0)$$ là xong!

## Kiến thức cần nhớ: Hai chiến lược Pha I kinh điển tìm điểm khả thi chặt

- **Chiến lược 1 — Cực tiểu hóa mức bất khả thi lớn nhất (1 biến phụ $$s$$):**
  $$\min_{x, s} s \qquad \text{với điều kiện } h_i(x) \le s \;\;(i=1,\dots,m), \quad Ax = b.$$
  - Khởi tạo cực dễ: lấy bất kỳ $$x^{(0)}$$ thỏa $$Ax^{(0)} = b$$ và đặt $$s^{(0)} = \max_i h_i(x^{(0)}) + 1$$ → lập tức có $$h_i(x^{(0)}) - s^{(0)} \le -1 < 0$$ (khả thi chặt!).
  - **Tiêu chí dừng sớm cực lợi hại:** Ta **không cần** giải Pha I tới tối ưu! Ngay khoảnh khắc thuật toán bước tới một điểm có $$s < 0$$, điểm $$x$$ tương ứng đã thỏa $$h_i(x) \le s < 0$$ — dừng Pha I ngay và chuyển sang Pha II!
- **Chiến lược 2 — Tổng mức bất khả thi từng ràng buộc ($$m$$ biến phụ $$s_i \ge 0$$):**
  $$\min_{x, s} \mathbf{1}^T s \qquad \text{với điều kiện } h_i(x) \le s_i, \;\; s_i \ge 0, \;\; Ax = b.$$
  Rất hữu ích khi bài toán gốc **vô nghiệm**: nghiệm Pha I sẽ chỉ rõ *chính xác những ràng buộc nào đang mâu thuẫn nhau* (các ràng buộc có $$s_i^* > 0$$)!

### Giải thích: Chạy tay thiết lập bài toán Pha I cho một hệ bất đẳng thức 1 chiều

Giả sử ta cần tìm một điểm khả thi chặt cho hệ hai ràng buộc (không biết trước nghiệm nằm đâu):
$$h_1(x) = x - 5 \le 0, \qquad h_2(x) = 3 - x \le 0 \qquad (\text{miền trong thật là } (3, 5)).$$
Ta thử đại một điểm xuất phát bất kỳ: $$x^{(0)} = 0$$ (rõ ràng bất khả thi vì $$h_2(0) = 3 > 0$$!).

1. **Lập bài toán Pha I (chiến lược 1 biến $$s$$):**
   $$\min_{x, s} s \qquad \text{với } x - 5 - s \le 0 \quad \text{và} \quad 3 - x - s \le 0.$$
2. **Tìm điểm khả thi chặt ban đầu cho Pha I từ $$x^{(0)} = 0$$:**
   - Tính $$h_1(0) = -5$$, $$h_2(0) = 3 \implies \max(h_1, h_2) = 3$$.
   - Chọn $$s^{(0)} = 3 + 1 = 4$$.
   - Kiểm tra độ dư tại $$(x^{(0)}, s^{(0)}) = (0, 4)$$:
     $$h_1(0) - 4 = -9 < 0, \qquad h_2(0) - 4 = -1 < 0.$$
     Hoàn toàn khả thi chặt cho bài toán Pha I!
3. **Quan sát Pha I thu hẹp $$s$$:**
   - Khi chạy phương pháp chắn giảm $$s$$, cặp $$(x, s)$$ di chuyển về phía nghiệm tối ưu Pha I là $$(x^*, s^*) = (4, -1)$$.
   - Ngay khi thuật toán đi qua điểm $$(x, s) = (3.8, -0.5)$$ có $$s = -0.5 < 0$$, ta kiểm tra bài toán gốc: $$h_1(3.8) = -1.2 < 0$$ và $$h_2(3.8) = -0.8 < 0$$! Ta dừng Pha I ngay lập tức và lấy $$x = 3.8$$ làm điểm khởi tạo khả thi chặt cho Pha II!

---

Cho đến nay, ta luôn giả sử bước định tâm đầu tiên (tại $$t = t^{(0)}$$) đã có sẵn một điểm xuất phát khả thi chặt để tìm $$x^{(0)} = x^*(t^{(0)})$$.

Một điểm $$x$$ được gọi là khả thi chặt nếu thỏa mãn đồng thời:
>$$ h_i(x) \lt 0, \quad i = 1, \cdots, m, \quad Ax = b$$

## Cực tiểu hóa mức bất khả thi lớn nhất
Để tìm một điểm $$x$$ khả thi chặt, ta giải bài toán phụ (Phase I) sau:

>
$$\begin{align}
&\min_{x, s} \        && s \\
&\text{subject to } \ && h_i(x) \le s,& i = 1, \cdots, m \\
                      &&& Ax = b \\
\end{align}$$

Mục tiêu của bài toán này là tìm nghiệm có $$s < 0$$. Cách tiếp cận này được gọi là **phương pháp tìm điểm khả thi (feasibility method)**.

Vì bài toán phụ này dễ dàng tìm được điểm xuất phát khả thi chặt (chỉ cần chọn $$x$$ thỏa $$Ax = b$$ rồi lấy $$s > \max_i h_i(x)$$), ta có thể giải trực tiếp nó bằng phương pháp chắn.

Khi giải bài toán tìm điểm khả thi, không cần đạt độ chính xác cao; chỉ cần dừng ngay khi tìm được một cặp $$(x, s)$$ khả thi với $$s < 0$$.

## Cực tiểu hóa mức bất khả thi cho từng ràng buộc
Một biến thể khác là gán biến phụ $$s_i$$ riêng cho từng ràng buộc bất đẳng thức ($$i = 1, \cdots, m$$) thay vì dùng chung một biến $$s$$:
>
$$\begin{align}
&\min_{x, s} \        && 1^Ts \\
&\text{subject to } \ && h_i(x) \le s_i,& i = 1, \cdots, m \\
                      &&& Ax = b \\
\end{align}$$

Ưu điểm của cách phát biểu này là dựa vào từng thành phần của nghiệm $$s$$, ta biết cụ thể ràng buộc nào đang bị vi phạm: nếu có phần tử $$s_i \ge 0$$ thì ràng buộc bất đẳng thức thứ $$i$$ không được thỏa mãn chặt.
