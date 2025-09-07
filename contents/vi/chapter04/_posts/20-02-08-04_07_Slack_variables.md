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

# Biến Phụ trong Tối ưu hóa Lồi

## Giới thiệu và Động lực

Biến phụ là các biến phụ trợ được giới thiệu để biến đổi ràng buộc bất đẳng thức thành ràng buộc đẳng thức. Biến đổi này là cơ bản trong lý thuyết tối ưu hóa và có ứng dụng thực tế trong quy hoạch tuyến tính, các phương pháp điểm trong, và nhiều thuật toán tối ưu hóa.

**Tại sao chúng ta cần biến phụ?**
- Nhiều thuật toán tối ưu hóa được thiết kế để xử lý ràng buộc đẳng thức hiệu quả hơn
- Chúng cung cấp giải thích hình học về mức độ "chặt" của ràng buộc
- Chúng thiết yếu trong phương pháp simplex cho quy hoạch tuyến tính
- Chúng giúp trong lý thuyết đối ngẫu và phân tích độ nhạy

## Công thức Toán học

Xem xét bài toán tối ưu hóa lồi tiêu chuẩn:

>$$
\begin{aligned}
&\min_x &&f(x) \\
&\text{subject to} &&g_{i}(x) \leq 0, \quad i = 1, \ldots, m\\
&&&Ax = b
\end{aligned}
>$$

Bằng cách giới thiệu **biến phụ** $$s_i \geq 0$$ cho mỗi ràng buộc bất đẳng thức, chúng ta có thể tái công thức hóa thành:

>$$
\begin{aligned}
&\min_{x, s} &&f(x)\\
&\text{subject to} &&s_{i} \geq 0, \quad i = 1, \ldots, m\\
&&&g_{i}(x) + s_{i} = 0, \quad i = 1, \ldots, m\\
&&&Ax = b
\end{aligned}
$$

## Giải thích Hình học

Biến phụ $$s_i$$ biểu diễn "khoảng trống" hoặc "biên độ" trong ràng buộc thứ $$i$$:

- **$$s_i > 0$$**: Ràng buộc $$g_i(x) \leq 0$$ **không hoạt động** (không ràng buộc)
  - Điểm $$x$$ nằm trong phần trong của vùng khả thi được định nghĩa bởi ràng buộc $$i$$
  - Chúng ta có $$g_i(x) = -s_i < 0$$

- **$$s_i = 0$$**: Ràng buộc $$g_i(x) \leq 0$$ **hoạt động** (ràng buộc)
  - Điểm $$x$$ nằm chính xác trên biên được định nghĩa bởi $$g_i(x) = 0$$
  - Ràng buộc này "chặt" tại nghiệm tối ưu

## Ví dụ Thực tế: Phân bổ Tài nguyên

Xem xét một bài toán phân bổ tài nguyên đơn giản:

**Bài toán Gốc:**
>$$
\begin{aligned}
&\max &&3x_1 + 2x_2 \\
&\text{thỏa mãn} &&x_1 + x_2 \leq 4 \quad \text{(giờ lao động)}\\
&&&2x_1 + x_2 \leq 6 \quad \text{(đơn vị nguyên liệu)}\\
&&&x_1, x_2 \geq 0
\end{aligned}
>$$

**Với Biến Phụ:**
>$$
\begin{aligned}
&\max &&3x_1 + 2x_2 \\
&\text{subject to} &&x_1 + x_2 + s_1 = 4\\
&&&2x_1 + x_2 + s_2 = 6\\
&&&x_1, x_2, s_1, s_2 \geq 0
\end{aligned}
>$$

**Giải thích:**
- $$s_1$$: giờ lao động chưa sử dụng
- $$s_2$$: đơn vị nguyên liệu chưa sử dụng
- Nếu $$s_1 = 0$$ tại tối ưu: tất cả lao động được sử dụng
- Nếu $$s_2 > 0$$ tại tối ưu: một số nguyên liệu vẫn chưa được sử dụng

## Các Tính chất và Cân nhắc Quan trọng

### 1. Tương đương của các Bài toán
Các công thức gốc và biến phụ là **tương đương về mặt toán học**:
- Cùng giá trị mục tiêu tối ưu
- $$x^*$$ tối ưu giống nhau trong cả hai công thức
- Các biến phụ $$s_i^*$$ tại tối ưu cho chúng ta biết ràng buộc nào hoạt động

### 2. Bảo toàn Tính lồi
**Lưu ý Quan trọng:** Biến đổi bảo toàn tính lồi **chỉ khi** $$g_i(x)$$ là **hàm affine**.

- **Nếu $$g_i(x) = a_i^T x - b_i$$ (affine)**: Bài toán tái công thức vẫn lồi
- **Nếu $$g_i(x)$$ là phi tuyến**: Ràng buộc đẳng thức $$g_i(x) + s_i = 0$$ có thể phá hủy tính lồi

### 3. Tác động Độ phức tạp
- Bài toán gốc: $$n$$ biến
- Với biến phụ: $$n + m$$ biến
- Đánh đổi: nhiều biến hơn nhưng cấu trúc ràng buộc đơn giản hơn

## Ví dụ: Chuyển đổi Chương trình Tuyến tính

**Dạng Gốc:**
>$$
\begin{aligned}
&\min &&c^T x \\
&\text{thỏa mãn} &&Ax \leq b\\
&&&x \geq 0
\end{aligned}
>$$

**Dạng Tiêu chuẩn với Biến Phụ:**
>$$
\begin{aligned}
&\min &&c^T x \\
&\text{subject to} &&Ax + s = b\\
&&&x, s \geq 0
\end{aligned}
>$$

Trong đó $$s \in \mathbb{R}^m$$ là vector của các biến phụ.

## Các Điểm Chính

1. **Công cụ Biến đổi**: Biến phụ chuyển đổi bất đẳng thức thành đẳng thức
2. **Ý nghĩa Hình học**: Chúng đo "mức độ chặt" của ràng buộc
3. **Kích hoạt Thuật toán**: Thiết yếu cho nhiều thuật toán tối ưu hóa
4. **Điều kiện Lồi**: Chỉ bảo toàn tính lồi cho ràng buộc affine
5. **Hiểu biết Thực tế**: Cung cấp giải thích kinh tế trong các bài toán tài nguyên

Hiểu về biến phụ là quan trọng cho:
- Triển khai các thuật toán tối ưu hóa
- Giải thích kết quả tối ưu hóa
- Phân tích độ nhạy ràng buộc
- Kết nối lý thuyết với thực hành tính toán
