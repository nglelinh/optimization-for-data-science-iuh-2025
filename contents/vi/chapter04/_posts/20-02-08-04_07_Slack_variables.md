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
