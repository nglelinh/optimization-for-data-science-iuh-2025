---
layout: post
title: '24-03 Giải quy hoạch nguyên'
chapter: '24'
order: 4
owner: YoungJae Choung
categories:
- chapter24
lang: vi
---

Trong tối ưu lồi, chỉ cần thấy $$\nabla f(x^\star) = 0$$ (hoặc điều kiện KKT thỏa mãn), bạn có thể lập tức đóng sổ và tuyên bố: *"Tôi đã tìm được nghiệm tối ưu toàn cục!"* Nhưng trong quy hoạch nguyên, công cụ vi phân biến mất hoàn toàn — tại một điểm lưới nguyên, ta không thể "lấy đạo hàm" sang điểm lưới bên cạnh để biết liệu phía bên kia ngọn đồi có một nghiệm tốt hơn hay không.

Vậy làm sao một bộ giải MIP như Gurobi hay HiGHS có thể **chứng minh chắc chắn 100%** rằng không còn nghiệm nguyên nào tốt hơn nữa mà không phải vét cạn cả $$2^{1000}$$ tổ hợp? Câu trả lời là một chiến lược gọng kìm kinh điển: **kẹp nghiệm tối ưu $$z$$ giữa hai dãy cận — cận gốc (primal bound) chạy từ trên xuống và cận đối ngẫu (dual bound) chạy từ dưới lên** — cho đến khi hai gọng kìm khép chặt vào nhau.

## Kiến thức cần nhớ: Ba trụ cột của khung giải MIP bằng gọng kìm cận

Bài học này đặt ra kiến trúc tổng quát mà mọi bộ giải quy hoạch nguyên hiện đại đều tuân theo:

- **Tính NP-khó và Lý do không có công thức cục bộ:** Quy hoạch nguyên 0–1 có thể mã hóa bài toán 3-SAT, nên trong trường hợp xấu nhất không tồn tại thuật toán thời gian đa thức (nếu $$\text{P} \neq \text{NP}$$). Do đó, chứng nhận tối ưu phải mang tính *toàn cục* thông qua cận dưới.
- **Cận gốc $$\bar{z}$$ (Primal / Upper Bound cho bài toán cực tiểu):** Bất kỳ nghiệm nguyên khả thi $$x \in X$$ nào tìm được (nhờ heuristic, làm tròn thông minh, hay nghiệm nguyên từ cây tìm kiếm) đều cho ngay một cận trên $$\bar{z} = f(x) \ge z^\star$$. Cận trên càng giảm nhanh, bộ giải càng cắt tỉa được nhiều nhánh.
- **Cận đối ngẫu $$\underline{z}$$ (Dual / Lower Bound cho bài toán cực tiểu):** Thu được từ các phép nới lỏng (LP, lồi, Lagrange) hoặc mặt phẳng cắt. Khi khoảng cách tương đối (*MIP gap*) $$\frac{\bar{z} - \underline{z}}{|\bar{z}|}$$ đạt $$0$$ (hoặc nhỏ hơn ngưỡng $$\varepsilon$$, ví dụ $$0.01\%$$), thuật toán dừng với bằng chứng toán học chặt chẽ về chất lượng nghiệm.

### Giải thích: Khép gọng kìm cận gốc – cận đối ngẫu bằng tay

Xét bài toán quy hoạch nguyên cực tiểu hóa:

$$
z^\star = \min_{x_1, x_2 \in \mathbb{Z}_+}\ 5x_1 + 7x_2 \qquad \text{thỏa mãn } 2x_1 + 3x_2 \ge 7.
$$

1. **Bước 1 — Tìm cận đối ngẫu ban đầu $$\underline{z}_0$$ bằng nới lỏng LP:**
   So sánh chi phí trên mỗi đơn vị ràng buộc: biến $$x_1$$ tốn $$5/2 = 2.5$$ mỗi đơn vị, còn biến $$x_2$$ rẻ hơn với $$7/3 \approx 2.333$$ mỗi đơn vị.
   Do đó nghiệm nới lỏng LP dồn hết vào $$x_2$$: $$x_1 = 0,\; x_2 = \frac{7}{3}$$, cho cận dưới $$\underline{z}_0 = 7 \cdot \frac{7}{3} = \frac{49}{3} \approx 16.333$$.
   *Mẹo thắt cận tức thì:* Vì hệ số mục tiêu $$5, 7$$ và biến $$x_1, x_2$$ đều là số nguyên, giá trị tối ưu $$z^\star$$ **bắt buộc là số nguyên**! Vậy ta lập tức làm tròn lên cận dưới: $$\underline{z}_1 = \lceil 16.333 \rceil = 17$$.
2. **Bước 2 — Tìm cận gốc ban đầu $$\bar{z}_0$$ bằng làm tròn khả thi:**
   Làm tròn nghiệm LP $$(0, 2.333)$$ lên thành điểm nguyên khả thi $$(0, 3)$$ (kiểm tra: $$2(0)+3(3)=9 \ge 7$$).
   Chi phí là $$\bar{z}_0 = 5(0) + 7(3) = 21$$. Lúc này ta biết chắc $$17 \le z^\star \le 21$$ (khoảng cận bằng $$4$$).
3. **Bước 3 — Cải thiện nghiệm khả thi để khép kín khoảng cận:**
   Thử tổ hợp nguyên $$(x_1, x_2) = (2, 1)$$: kiểm tra ràng buộc $$2(2) + 3(1) = 7 \ge 7$$ (khả thi!).
   Giá trị mục tiêu mới là $$\bar{z}_1 = 5(2) + 7(1) = 17$$.
4. **Chứng nhận tối ưu:** Lúc này $$\underline{z}_1 = 17 = \bar{z}_1$$ (khoảng cận bằng $$0$$)! Ta không cần thử thêm bất kỳ điểm nguyên nào khác mà vẫn chứng minh được 100% rằng $$(2, 1)$$ là nghiệm tối ưu toàn cục!

Sau khi mô hình hóa một bài toán dưới dạng quy hoạch nguyên, ta cần các kỹ thuật như nới lỏng (relaxation) và khép khoảng cận để tìm nghiệm. Mục này trình bày độ khó cơ bản của quy hoạch nguyên và khung thuật toán tổng quát để giải nó.

## Độ khó của quy hoạch nguyên

Giải quy hoạch nguyên khó hơn nhiều so với tối ưu lồi. Quy hoạch nguyên tổng quát thuộc lớp bài toán [NP-khó](https://en.wikipedia.org/wiki/NP-hardness), nên nhìn chung không tồn tại thuật toán thời gian đa thức được biết. Khi bỏ các ràng buộc nguyên để thực hiện nới lỏng lồi (convex relaxation), ta thu được một cận dưới cho giá trị tối ưu, nhưng cách làm này vẫn gặp ba hạn chế chính:

* Việc tìm được một nghiệm nguyên khả thi từ nghiệm nới lỏng có thể rất khó.
* Giá trị tối ưu của bài toán nới lỏng có thể cách xa giá trị tối ưu thực của quy hoạch nguyên.
* Nghiệm thu được sau khi làm tròn nghiệm nới lỏng có thể không tối ưu (thậm chí không khả thi).

## Khung thuật toán giải quy hoạch nguyên

Xét bài toán quy hoạch nguyên với tập khả thi $$X$$ (bao gồm các ràng buộc lồi và ràng buộc nguyên):

> $$ z := \min_{x \in X} f(x) $$

Khác với tối ưu lồi, ta không có điều kiện tối ưu bậc nhất đơn giản để chứng nhận ngay một điểm khả thi $$x^{\star} \in X$$ là tối ưu toàn cục. Thay vào đó, các thuật toán giải quy hoạch nguyên hoạt động bằng cách liên tục cập nhật một cận dưới $$\underline{z} \leq z$$ và một cận trên $$\bar{z} \geq z$$ cho đến khi khoảng cách giữa chúng đủ nhỏ.

### Khung thuật toán chung

Xây dựng dãy cận trên không tăng:
> $$\bar{z}_1 \geq \bar{z}_2 \geq \dotsc \geq \bar{z}_s \geq z$$

và dãy cận dưới không giảm:
> $$\underline{z}_1 \leq \underline{z}_2 \leq \dotsc \leq \underline{z}_t \leq z$$

Với sai số cho trước $$\epsilon > 0$$, thuật toán dừng khi $$\bar{z}_s - \underline{z}_t \leq \epsilon$$, đảm bảo nghiệm tương ứng với $$\bar{z}_s$$ cách giá trị tối ưu thực không quá $$\epsilon$$.

### Cận gốc (Primal bounds)

Với mọi điểm khả thi $$x \in X$$, giá trị hàm mục tiêu $$f(x) \geq z$$ lập tức cung cấp một cận trên (cận gốc). Tuy nhiên, trên thực tế việc tìm được các điểm khả thi $$x \in X$$ có chất lượng tốt không phải lúc nào cũng đơn giản.

### Cận đối ngẫu (Dual bounds)

Cận đối ngẫu (hay cận dưới) thường được tính thông qua các bài toán nới lỏng. Nội dung chi tiết về các phương pháp nới lỏng được trình bày ở mục tiếp theo.
