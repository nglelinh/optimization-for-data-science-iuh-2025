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

Bài toán tối ưu hóa là bài toán trong đó, trong số nhiều ứng viên có thể, chúng ta tìm kiếm nghiệm tối ưu (giá trị tối ưu) hoặc một giá trị gần với tối ưu.

**Trong khoa học dữ liệu và học máy**, tối ưu hóa có mặt ở khắp mọi nơi:
- **Huấn luyện mạng nơ-ron**: Tìm kiếm trọng số để giảm thiểu lỗi dự đoán
- **Hồi quy tuyến tính**: Tìm đường thẳng khớp nhất để giảm thiểu bình phương sai số
- **Phân cụm**: Tối ưu hóa tâm cụm để giảm thiểu phương sai trong cụm
- **Lựa chọn đặc trưng**: Chọn tập con đặc trưng tốt nhất để tối đa hóa hiệu suất mô hình
- **Điều chỉnh siêu tham số**: Tìm tỷ lệ học tối ưu, tham số chính quy, v.v.

Mỗi khi bạn huấn luyện một mô hình học máy, bạn đang giải một bài toán tối ưu hóa!

## Bài toán tối ưu hóa toán học
Một bài toán tối ưu hóa toán học có thể được biểu diễn như sau:

>$$\begin{align*} 
>&\min_{x\in D}\ && f(x) \\
>&\text{với điều kiện} && g_i(x) \le 0,\ i = 1, ..., m \\
>&&& h_j(x) = 0,\ j = 1,\ ..., r
>\end{align*}$$

**Bài toán Tối ưu hóa Toán học ở dạng chuẩn**

* $$x \in \mathbb{R}^n$$ là biến tối ưu hóa
* $$f: \mathbb{R}^n \rightarrow \mathbb{R}$$ là hàm mục tiêu hoặc hàm chi phí
* $$g_i: \mathbb{R}^n \rightarrow \mathbb{R}, i = 1, ..., m$$ là các hàm ràng buộc bất đẳng thức
* $$h_j: \mathbb{R}^n \rightarrow \mathbb{R}, j = 1, ..., r$$ là các hàm ràng buộc đẳng thức

Vector $$x$$ mà tối thiểu hóa hàm mục tiêu $$f$$ trên miền khả thi (tập hợp tất cả các điểm thỏa mãn các ràng buộc) được ký hiệu là $$x^*$$ và được gọi là nghiệm tối ưu.

**Các ràng buộc có thể được phân loại thành hai loại:**

1. Ràng buộc tường minh: Các ràng buộc được chỉ định trực tiếp trong bài toán tối ưu hóa. Trong dạng chuẩn ở trên, các ràng buộc được biểu diễn bởi các hàm $$g_i$$ và $$h_j$$ là tường minh. Nếu không có ràng buộc tường minh, bài toán được gọi là bài toán không ràng buộc.
2. Ràng buộc ngầm: Các ràng buộc không được chỉ định trực tiếp, nhưng phát sinh từ giao của các miền của hàm mục tiêu và các hàm ràng buộc.

$$D = dom(f) \cap \bigcap_{i=1}^m {\rm dom}(g_i) \cap \bigcap_{j=1}^r dom(h_j)$$<br/>

**Ghi chú:** $$dom(f)$$ có nghĩa là miền của hàm $$f$$.

>**Ví dụ: ràng buộc ngầm ↔ ràng buộc tường minh**
>
>Giả sử bài toán tối ưu hóa được cho như sau:
>
>$$\begin{align*} \text{tối thiểu } & & \log(x) \end{align*}$$
>
>Ở đây, miền của hàm mục tiêu $$\log(x)$$ là $$x > 0$$, nên $$x > 0$$ là một ràng buộc ngầm. Nếu chúng ta viết điều này dưới dạng bài toán tối ưu hóa với ràng buộc tường minh:
>
>$$\begin{align*} &\text{tối thiểu } && \log(x) \\ &\text{với điều kiện } &&x > 0 \end{align*}$$

> **💡 Mẹo chuyên nghiệp**: Bắt đầu với các công thức lồi khi có thể - chúng dễ giải và hiểu hơn. Chỉ chuyển sang các mô hình phi lồi phức tạp khi các phương pháp đơn giản hơn không đáp ứng được yêu cầu của bạn.
