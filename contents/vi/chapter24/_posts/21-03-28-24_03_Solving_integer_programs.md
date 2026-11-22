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
