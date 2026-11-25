---
layout: post
title: '15 Phương pháp chắn (Barrier Method)'
chapter: "15"
order: 1
categories:
- chapter16
owner: "Minjoo Lee"
lang: vi
---

Ở Chương 14, phương pháp Newton đã chinh phục trọn vẹn các bài toán tối ưu trơn không ràng buộc và có ràng buộc đẳng thức $$Ax = b$$. Nhưng ngoài đời thực, hầu hết các bài toán quan trọng nhất — từ quy hoạch tuyến tính (LP), quy hoạch bậc hai (QP) đến điều khiển tối ưu và danh mục tài chính — đều bị bao vây bởi hàng loạt **ràng buộc bất đẳng thức** $$h_i(x) \le 0$$. Những bức tường cứng ấy khiến nghiệm tối ưu thường nằm ngay trên biên, nơi phương pháp Newton truyền thống hoàn toàn bất lực.

**Phương pháp chắn (Barrier Method)** giải bài toán đó bằng một ý tưởng hình học đầy táo bạo: thay vì để thuật toán va đầu vào các bức tường biên, ta dựng lên một **trường lực đẩy trơn tru bằng hàm chắn logarit** $$-\frac{1}{t}\sum \log(-h_i(x))$$ tăng vọt lên $$+\infty$$ mỗi khi $$x$$ tiến sát biên! Nhờ thế, bài toán có ràng buộc bất đẳng thức biến thành một chuỗi bài toán trơn có ràng buộc đẳng thức — nơi ta có thể thả phương pháp Newton vào chạy băng băng dọc theo **đường trung tâm** cho đến sát nghiệm tối ưu.

## Kiến thức cần nhớ: Bốn trụ cột của Phương pháp chắn (Điểm trong)

- **Xấp xỉ hàm chỉ thị bằng hàm chắn logarit:** Thay bức tường không khả vi $$I_{h_i(x) \le 0}$$ bằng hàm trơn $$-\frac{1}{t}\log(-h_i(x))$$. Khi tham số $$t$$ tăng dần tới $$+\infty$$, hàm chắn bám ngày càng sát hàm chỉ thị gốc.
- **Đường trung tâm (Central Path) $$x^*(t)$$:** Tập hợp các nghiệm của bài toán chắn theo tham số $$t > 0$$ tạo thành một đường cong mượt mà nằm hoàn toàn trong **miền trong chặt** của tập khả thi và dẫn thẳng tới $$x^*$$.
- **Điều kiện KKT nhiễu và khoảng cách dưới tối ưu $$m/t$$:** Mỗi điểm trên đường trung tâm tự động sinh ra một điểm khả thi đối ngẫu với khoảng cách đối ngẫu **đúng bằng $$m/t$$** — một công thức kỳ diệu không phụ thuộc hàm mục tiêu hay hình dạng miền!
- **Thuật toán hai vòng lặp và Pha I tìm điểm khả thi:** Vòng ngoài tăng $$t \leftarrow \mu t$$, vòng trong chạy Newton có ràng buộc đẳng thức (bước định tâm). Khi chưa có điểm khả thi chặt ban đầu, bài toán Pha I tìm điểm xuất phát cũng được giải bằng chính phương pháp chắn.

### Giải thích: Quan sát một nghiệm trượt dọc đường trung tâm về biên

Xét bài toán cực tiểu hóa 1 chiều đơn giản nhất có ràng buộc bất đẳng thức:
$$\min_{x \in \mathbb{R}} x \qquad \text{với điều kiện } -x \le 0 \;\; (\text{tức } x \ge 0).$$
Nghiệm tối ưu hiển nhiên là $$x^* = 0$$ với $$f^* = 0$$ và số ràng buộc bất đẳng thức $$m = 1$$.

1. **Lập bài toán chắn theo tham số $$t > 0$$:**
   $$\min_{x > 0} \bigl(tx - \log x\bigr).$$
2. **Tìm điểm đường trung tâm $$x^*(t)$$:**
   Lấy đạo hàm theo $$x$$ bằng $$0$$:
   $$t - \frac{1}{x} = 0 \implies x^*(t) = \frac{1}{t}.$$
3. **Quan sát sự hội tụ khi tăng $$t$$ theo hệ số $$\mu = 10$$:**
   - $$t = 1$$: $$x^*(1) = 1.0$$, sai số $$f(x^*(1)) - f^* = 1.0 = \frac{1}{1}$$.
   - $$t = 10$$: $$x^*(10) = 0.1$$, sai số $$0.1 = \frac{1}{10}$$.
   - $$t = 1000$$: $$x^*(1000) = 0.001$$, sai số $$0.001 = \frac{1}{1000} = \frac{m}{t}$$!
   Điểm $$x^*(t) = 1/t$$ luôn nằm chặt bên trong miền $$x > 0$$ (không bao giờ chạm tường $$0$$ sớm) nhưng tiến thẳng tới $$0$$ với sai số chính xác bằng $$m/t$$!

---

Trong chương này, chúng ta sẽ tìm hiểu **phương pháp chắn (Barrier Method)** — một phương pháp tối ưu bậc hai quan trọng.

**Phương pháp chắn** được dùng để giải **các bài toán tối ưu trơn có cả ràng buộc bất đẳng thức và ràng buộc đẳng thức**, nhóm bài toán tổng quát và khó nhất trong khuôn khổ các phương pháp bậc hai.

(Nhắc lại: các phương pháp chỉ dùng gradient được gọi là phương pháp bậc nhất, còn các phương pháp dùng thêm ma trận Hessian được gọi là phương pháp bậc hai.)

## Tài liệu tham khảo và đọc thêm
* S. Boyd and L. Vandenberghe (2004), "Convex optimization", Chapter 11
* A. Nemirovski (2004), "Interior-point polynomial time methods in convex programming", Chapter 4
* J. Nocedal and S. Wright (2006), "Numerical optimization", Chapters 14 and 19
