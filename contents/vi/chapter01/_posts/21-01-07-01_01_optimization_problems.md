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
