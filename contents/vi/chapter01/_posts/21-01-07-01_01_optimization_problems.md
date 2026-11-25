---
layout: post
title: 01-01 Bài toán tối ưu hóa?
chapter: '01'
order: 2
owner: Kyeongmin Woo
categories:
- chapter01
lang: vi
lesson_type: required
---

Trước khi máy tính có thể giải bất kỳ bài toán thực tế nào — từ phân bổ vốn đầu tư, thiết kế ăng-ten, đến lập lịch giao hàng — người kỹ sư phải làm công việc quan trọng nhất: **dịch một câu chuyện đời thực thành ngôn ngữ chuẩn của bài toán tối ưu toán học**. Chọn sai biến quyết định hoặc viết thiếu một ràng buộc biên có thể biến một bài toán dễ giải thành bài toán vô nghiệm hoặc cho ra kết quả phi thực tế.

Bài học này đặt ra bộ khung chuẩn mực gồm biến tối ưu, hàm mục tiêu, ràng buộc bất đẳng thức, ràng buộc đẳng thức và phân biệt rõ giá trị tối ưu $$p^*$$ với nghiệm tối ưu $$x^*$$.

## Kiến thức cần nhớ: Giải phẫu một bài toán tối ưu chuẩn

- **Biến quyết định ($$x \in \mathbb{R}^n$$):** Các đại lượng ta thực sự có quyền điều chỉnh (khác với các tham số cố định cho trước của bài toán).
- **Hàm mục tiêu ($$f_0(x)$$):** Thước đo chi phí cần tối thiểu hóa. Nếu bài toán gốc yêu cầu *tối đa hóa* lợi nhuận $$u(x)$$, ta chỉ cần đổi dấu thành *tối thiểu hóa* $$-u(x)$$.
- **Miền khả thi (Feasible Set):** Tập tất cả các điểm $$x$$ thỏa mãn đồng thời mọi ràng buộc $$g_i(x) \le 0$$ và $$h_j(x) = 0$$. Nếu miền này rỗng, bài toán *vô nghiệm* (infeasible, $$p^* = +\infty$$).
- **Giá trị tối ưu ($$p^*$$) và tập nghiệm tối ưu ($$X_{\text{opt}}$$):** Một bài toán có thể có nghiệm duy nhất, vô số nghiệm cùng đạt $$p^*$$, hoặc không bị chặn dưới ($$p^* = -\infty$$).

### Giải thích: Chuẩn hóa và giải tay một bài toán phân bổ chi phí 2 biến

Một xưởng cần sản xuất ít nhất $$5$$ tấn hỗn hợp từ hai nguyên liệu $$x_1, x_2$$ (tấn) với chi phí lần lượt $$3$$ triệu/tấn và $$2$$ triệu/tấn, sao cho dùng tối thiểu $$1$$ tấn loại 1 và $$2$$ tấn loại 2.

1. **Viết lại về dạng chuẩn ($$\min$$ và ràng buộc $$\le 0$$):**
   $$\min_{x_1, x_2} f_0(x) = 3x_1 + 2x_2$$
   với ba ràng buộc bất đẳng thức:
   $$g_1(x) = 5 - x_1 - x_2 \le 0, \qquad g_2(x) = 1 - x_1 \le 0, \qquad g_3(x) = 2 - x_2 \le 0.$$
2. **Xác định các đỉnh của miền khả thi:** Miền khả thi là vùng không bị chặn phía trên bên phải nhưng bị chặn dưới bởi hai góc nhọn:
   - Đỉnh $$A$$ (giao $$x_1 = 1$$ và $$x_1 + x_2 = 5$$): $$A = (1, 4)$$.
   - Đỉnh $$B$$ (giao $$x_2 = 2$$ và $$x_1 + x_2 = 5$$): $$B = (3, 2)$$.
3. **Tính hàm mục tiêu tại các ứng viên:**
   - Tại $$A = (1, 4)$$: $$f_0(1, 4) = 3(1) + 2(4) = 11$$.
   - Tại $$B = (3, 2)$$: $$f_0(3, 2) = 3(3) + 2(2) = 13$$.
   Vì hệ số chi phí đều dương, tăng $$x_1$$ hoặc $$x_2$$ chỉ làm chi phí tăng thêm.
4. **Kết luận:** Nghiệm tối ưu duy nhất là $$x^* = (1, 4)^T$$ với giá trị tối ưu $$p^* = 11$$ triệu đồng; tại $$x^*$$, hai ràng buộc $$g_1(x^*) = 0$$ và $$g_2(x^*) = 0$$ là **ràng buộc chặt** (active), còn $$g_3(x^*) = 2 - 4 = -2 < 0$$ là ràng buộc lỏng.

---

Bài toán tối ưu hóa là bài toán tìm nghiệm tốt nhất (nghiệm tối ưu) — hoặc một nghiệm đủ gần tối ưu — trong tập hợp các phương án khả dĩ.

**Trong khoa học dữ liệu và học máy**, tối ưu hóa hiện diện ở hầu hết mọi tác vụ:
- **Huấn luyện mạng nơ-ron**: tìm bộ trọng số làm cực tiểu sai số dự đoán.
- **Hồi quy tuyến tính**: tìm siêu phẳng khớp nhất làm cực tiểu tổng bình phương sai số.
- **Phân cụm**: tối ưu vị trí tâm cụm nhằm cực tiểu hóa phương sai trong từng cụm.
- **Lựa chọn đặc trưng**: chọn tập con đặc trưng phù hợp nhất để tối đa hóa hiệu năng mô hình.
- **Tinh chỉnh siêu tham số**: tìm tốc độ học, hệ số điều chuẩn và các siêu tham số tối ưu.

Mỗi khi bạn huấn luyện một mô hình học máy, thực chất bạn đang giải một bài toán tối ưu hóa.

## Bài toán tối ưu hóa toán học

Một bài toán tối ưu hóa toán học có thể viết ở dạng tổng quát như sau:

>$$\begin{align*} 
>&\min_{x\in D}\ && f(x) \\
>&\text{với điều kiện} && g_i(x) \le 0,\ i = 1, ..., m \\
>&&& h_j(x) = 0,\ j = 1,\ ..., r
>\end{align*}$$

**Bài toán tối ưu hóa toán học ở dạng chuẩn**

* $$x \in \mathbb{R}^n$$ là biến tối ưu hóa (biến quyết định).
* $$f: \mathbb{R}^n \rightarrow \mathbb{R}$$ là hàm mục tiêu (hoặc hàm chi phí).
* $$g_i: \mathbb{R}^n \rightarrow \mathbb{R},\ i = 1, ..., m$$ là các hàm ràng buộc bất đẳng thức.
* $$h_j: \mathbb{R}^n \rightarrow \mathbb{R},\ j = 1, ..., r$$ là các hàm ràng buộc đẳng thức.

Vector $$x$$ làm cực tiểu hàm mục tiêu $$f$$ trên miền khả thi (tập hợp tất cả các điểm thỏa mãn mọi ràng buộc) được ký hiệu là $$x^*$$ và gọi là **nghiệm tối ưu**.

**Các ràng buộc được chia thành hai loại:**

1. **Ràng buộc tường minh:** Các ràng buộc được nêu trực tiếp trong bài toán. Trong dạng chuẩn ở trên, các điều kiện liên quan đến $$g_i$$ và $$h_j$$ là ràng buộc tường minh. Nếu không có ràng buộc tường minh nào, bài toán được gọi là bài toán không ràng buộc.
2. **Ràng buộc ngầm:** Các ràng buộc không viết tường minh, nhưng phát sinh từ giao miền xác định của hàm mục tiêu và tất cả các hàm ràng buộc:

$$D = dom(f) \cap \bigcap_{i=1}^m {\rm dom}(g_i) \cap \bigcap_{j=1}^r dom(h_j)$$<br/>

**Ghi chú:** $$dom(f)$$ ký hiệu miền xác định của hàm $$f$$.

>**Ví dụ: Ràng buộc ngầm ↔ Ràng buộc tường minh**
>
>Xét bài toán tối ưu hóa sau:
>
>$$\begin{align*} \text{tối thiểu } & & \log(x) \end{align*}$$
>
>Ở đây, miền xác định của hàm mục tiêu $$\log(x)$$ là $$x > 0$$, nên $$x > 0$$ là một ràng buộc ngầm. Khi viết lại với ràng buộc tường minh, bài toán trở thành:
>
>$$\begin{align*} &\text{tối thiểu } && \log(x) \\ &\text{với điều kiện } &&x > 0 \end{align*}$$

> **💡 Lưu ý thực hành**: Khi có thể, hãy bắt đầu với mô hình tối ưu hóa lồi vì chúng dễ phân tích và giải chính xác hơn. Chỉ nên chuyển sang các mô hình không lồi phức tạp hơn khi mô hình lồi không đáp ứng được yêu cầu bài toán.
