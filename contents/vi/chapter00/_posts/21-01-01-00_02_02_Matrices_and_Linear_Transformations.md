---
layout: post
title: 00-02-02 Ma trận và Phép biến đổi Tuyến tính
chapter: '00'
order: 9
owner: GitHub Copilot
lang: vi
categories:
- chapter00
lesson_type: required
---

Đừng chỉ nhìn một ma trận như một bảng số hình chữ nhật; trong tối ưu hóa, mỗi ma trận $$A \in \mathbb{R}^{m \times n}$$ là một **cỗ máy biến hình không gian**: nó kéo giãn, xoay, chiếu hoặc ép phẳng các tập lồi trong $$\mathbb{R}^n$$ thành những hình dạng mới trong $$\mathbb{R}^m$$. Hiểu ma trận như một phép biến đổi tuyến tính giúp bạn hiểu ngay vì sao ảnh affine của một hình cầu là một ellipsoid, hay vì sao hệ ràng buộc $$Ax = b$$ mô tả một không gian con dịch chuyển.

Bài học này kết nối các phép toán đại số trên ma trận với ý nghĩa hình học và cấu trúc nghiệm của hệ phương trình tuyến tính.

## Bản đồ kiến thức nền: Bốn góc nhìn về một ma trận $$A$$

- **Phép biến đổi tuyến tính:** Ánh xạ $$T(x) = Ax$$ bảo toàn tổ hợp tuyến tính: $$A(\alpha x + \beta y) = \alpha Ax + \beta Ay$$. Cột thứ $$j$$ của $$A$$ chính là ảnh của vector cơ sở chuẩn $$e_j$$.
- **Bốn không gian con cơ bản:** Không gian cột $$\mathcal{R}(A)$$ (các đầu ra đạt được), không gian hạch $$\mathcal{N}(A)$$ (các hướng bị triệt tiêu về $$0$$), cùng $$\mathcal{R}(A^T)$$ và $$\mathcal{N}(A^T)$$. Khi giải hệ $$Ax = b$$, tập nghiệm có dạng $$x_p + \mathcal{N}(A)$$.
- **Hạng (Rank), Định thức và Ma trận nghịch đảo:** Với ma trận vuông $$n\times n$$, $$\det(A) \ne 0 \iff \operatorname{rank}(A) = n \iff A$$ khả nghịch. Định thức $$|\det(A)|$$ đo đúng hệ số phóng đại thể tích của phép biến đổi.
- **Ma trận đối xứng và chuyển vị ($$A^T$$):** Xuất hiện dày đặc trong dạng toàn phương $$x^T Q x$$, phương trình chuẩn $$A^T A x = A^T b$$ và biểu diễn đối ngẫu của các phép biến đổi tuyến tính.

### Khung giải thích (nên đọc chậm): Giải mã phép biến đổi $$A = \begin{pmatrix}2 & 1\\ 1 & 2\end{pmatrix}$$ và hệ $$Ax = b$$

Xét ma trận đối xứng $$A = \begin{pmatrix}2 & 1\\ 1 & 2\end{pmatrix}$$ và vector vế phải $$b = \begin{pmatrix}4\\ 5\end{pmatrix}$$:

1. **Kiểm tra khả nghịch và hệ số thể tích:**
   $$\det(A) = 2\cdot 2 - 1\cdot 1 = 3 \ne 0.$$
   Phép biến đổi $$x \mapsto Ax$$ làm diện tích mọi hình trong $$\mathbb{R}^2$$ tăng đúng $$3$$ lần và không làm sụp chiều nào ($$\operatorname{rank}(A) = 2$$, $$\mathcal{N}(A) = \{0\}$$).
2. **Tìm ma trận nghịch đảo:**
   $$A^{-1} = \frac{1}{3}\begin{pmatrix}2 & -1\\ -1 & 2\end{pmatrix}.$$
3. **Giải duy nhất hệ $$Ax = b$$:**
   $$x = A^{-1}b = \frac{1}{3}\begin{pmatrix}2\cdot 4 - 1\cdot 5\\ -1\cdot 4 + 2\cdot 5\end{pmatrix} = \frac{1}{3}\begin{pmatrix}3\\ 6\end{pmatrix} = \begin{pmatrix}1\\ 2\end{pmatrix}.$$
4. **Kiểm tra ngược:** $$A\begin{pmatrix}1\\ 2\end{pmatrix} = 1\begin{pmatrix}2\\ 1\end{pmatrix} + 2\begin{pmatrix}1\\ 2\end{pmatrix} = \begin{pmatrix}4\\ 5\end{pmatrix} = b$$. Vector $$b$$ chính là tổ hợp tuyến tính duy nhất của hai cột của $$A$$ với trọng số $$1$$ và $$2$$.

---

Bài học này trình bày về ma trận, các phép toán trên ma trận và phép biến đổi tuyến tính — những công cụ cơ bản để biểu diễn và giải các bài toán tối ưu hóa.

---

## Ma trận và các phép toán ma trận

### Ma trận là gì?

Một **ma trận** (matrix) là một bảng số hình chữ nhật gồm các phần tử sắp xếp theo hàng và cột. Ma trận được dùng để biểu diễn dữ liệu, phép biến đổi, hệ phương trình và mối quan hệ giữa các biến.

**Dạng tổng quát:**
$$\mathbf{A} = \begin{pmatrix} 
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}$$

Đây là ma trận cỡ $$m \times n$$ ($$m$$ hàng, $$n$$ cột).

**Ví dụ:**
$$\mathbf{A} = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$$ là ma trận cỡ $$2 \times 3$$.

### Phép cộng ma trận

Hai ma trận cùng kích thước được cộng bằng cách cộng từng cặp phần tử ở vị trí tương ứng:

$$\mathbf{A} + \mathbf{B} = \begin{pmatrix} a_{11} + b_{11} & a_{12} + b_{12} \\ a_{21} + b_{21} & a_{22} + b_{22} \end{pmatrix}$$

**Ví dụ:**
$$\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} + \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} = \begin{pmatrix} 6 & 8 \\ 10 & 12 \end{pmatrix}$$

### Phép nhân vô hướng

Nhân mọi phần tử của ma trận với một số vô hướng $$c$$:

$$c\mathbf{A} = \begin{pmatrix} ca_{11} & ca_{12} \\ ca_{21} & ca_{22} \end{pmatrix}$$

### Phép nhân ma trận

Với hai ma trận $$\mathbf{A}_{m \times n}$$ và $$\mathbf{B}_{n \times p}$$, ma trận tích $$\mathbf{C}_{m \times p} = \mathbf{AB}$$ có phần tử ở hàng $$i$$, cột $$j$$ bằng tích vô hướng của hàng $$i$$ của $$\mathbf{A}$$ với cột $$j$$ của $$\mathbf{B}$$:

$$c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}$$

**Ví dụ:**
$$\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} = \begin{pmatrix} 1 \cdot 5 + 2 \cdot 7 & 1 \cdot 6 + 2 \cdot 8 \\ 3 \cdot 5 + 4 \cdot 7 & 3 \cdot 6 + 4 \cdot 8 \end{pmatrix} = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}$$

**Lưu ý:** Phép nhân ma trận **không có tính giao hoán** — nói chung $$\mathbf{AB} \neq \mathbf{BA}$$.

---

## Phép biến đổi tuyến tính

Một **phép biến đổi tuyến tính** là ánh xạ $$T: \mathbb{R}^n \to \mathbb{R}^m$$ bảo toàn phép cộng vector và phép nhân vô hướng. Mọi phép biến đổi tuyến tính giữa các không gian hữu hạn chiều đều có thể biểu diễn bằng một ma trận.

### Định nghĩa

Ánh xạ $$T(\mathbf{v}) = \mathbf{Av}$$ là tuyến tính khi và chỉ khi:

1. **Tính cộng:** $$T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$$
2. **Tính thuần nhất:** $$T(c\mathbf{v}) = cT(\mathbf{v})$$

Hai điều kiện trên có thể gộp thành một điều kiện tương đương: $$T(c_1\mathbf{u} + c_2\mathbf{v}) = c_1T(\mathbf{u}) + c_2T(\mathbf{v})$$.

### Phép nhân ma trận với vector

Nếu $$\mathbf{A}$$ là ma trận $$m \times n$$ và $$\mathbf{v}$$ là vector cột $$n \times 1$$, thì tích $$\mathbf{Av}$$ là vector cột $$m \times 1$$:

$$ \mathbf{w} = \mathbf{Av} = \begin{pmatrix} 
a_{11}v_1 + a_{12}v_2 + \cdots + a_{1n}v_n \\
a_{21}v_1 + a_{22}v_2 + \cdots + a_{2n}v_n \\
\vdots \\
a_{m1}v_1 + a_{m2}v_2 + \cdots + a_{mn}v_n
\end{pmatrix} $$

**Ví dụ:**
$$\begin{pmatrix} 2 & 1 \\ 0 & 3 \end{pmatrix} \begin{pmatrix} 4 \\ 5 \end{pmatrix} = \begin{pmatrix} 2 \cdot 4 + 1 \cdot 5 \\ 0 \cdot 4 + 3 \cdot 5 \end{pmatrix} = \begin{pmatrix} 13 \\ 15 \end{pmatrix}$$

---

## Các phép biến đổi 2D thường gặp

Quan sát các phép biến đổi hình học trong mặt phẳng giúp hình dung rõ cách ma trận tác động lên vector.

### Phép co giãn (Scaling)

**Ma trận co giãn:**
$$\mathbf{S} = \begin{pmatrix} s_x & 0 \\ 0 & s_y \end{pmatrix}$$

- Co giãn tọa độ $$x$$ theo hệ số $$s_x$$ và tọa độ $$y$$ theo hệ số $$s_y$$.
- **Ví dụ:** $$\begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$$ nhân đôi tọa độ $$x$$ và nhân ba tọa độ $$y$$.

### Phép quay (Rotation)

**Ma trận quay ngược chiều kim đồng hồ một góc $$\theta$$:**
$$\mathbf{R} = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$$

- **Ví dụ:** phép quay $$90°$$ có ma trận $$\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$$, biến điểm $$(x, y)$$ thành $$(-y, x)$$.

### Phép phản xạ (Reflection)

**Phản xạ qua trục $$x$$:**
$$\mathbf{F}_x = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

**Phản xạ qua trục $$y$$:**
$$\mathbf{F}_y = \begin{pmatrix} -1 & 0 \\ 0 & 1 \end{pmatrix}$$

**Phản xạ qua đường thẳng $$y = x$$:**
$$\mathbf{F}_{y=x} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$

### Phép trượt (Shearing)

**Trượt ngang:**
$$\mathbf{H} = \begin{pmatrix} 1 & k \\ 0 & 1 \end{pmatrix}$$

Biến điểm $$(x, y)$$ thành $$(x + ky, y)$$.

---

## Các loại ma trận đặc biệt

### Ma trận đơn vị

**Ma trận đơn vị** $$\mathbf{I}$$ đóng vai trò phần tử đơn vị (tương tự số 1) đối với phép nhân ma trận:

$$\mathbf{I}_n = \begin{pmatrix} 
1 & 0 & \cdots & 0 \\
0 & 1 & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & 1
\end{pmatrix}$$

**Tính chất:** $$\mathbf{AI} = \mathbf{IA} = \mathbf{A}$$ với mọi ma trận $$\mathbf{A}$$ có kích thước tương thích.

### Ma trận chuyển vị

**Chuyển vị** $$\mathbf{A}^T$$ thu được bằng cách đổi hàng thành cột (lật ma trận qua đường chéo chính):

$$\text{Nếu } \mathbf{A} = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}, \text{ thì } \mathbf{A}^T = \begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}$$

**Các tính chất:**
- $$(\mathbf{A}^T)^T = \mathbf{A}$$
- $$(\mathbf{A} + \mathbf{B})^T = \mathbf{A}^T + \mathbf{B}^T$$
- $$(\mathbf{AB})^T = \mathbf{B}^T\mathbf{A}^T$$

### Ma trận đối xứng

Một ma trận vuông là **đối xứng** nếu $$\mathbf{A} = \mathbf{A}^T$$:

$$\mathbf{A} = \begin{pmatrix} 1 & 2 & 3 \\ 2 & 4 & 5 \\ 3 & 5 & 6 \end{pmatrix}$$

Ma trận đối xứng có nhiều tính chất đặc biệt (như giá trị riêng thực và khả năng chéo hóa trực giao) rất quan trọng trong tối ưu hóa.

### Ma trận nghịch đảo

**Ma trận nghịch đảo** $$\mathbf{A}^{-1}$$ của ma trận vuông $$\mathbf{A}$$ thỏa mãn:

$$\mathbf{A}\mathbf{A}^{-1} = \mathbf{A}^{-1}\mathbf{A} = \mathbf{I}$$

**Với ma trận $$2 \times 2$$:**
$$\mathbf{A}^{-1} = \frac{1}{\det(\mathbf{A})} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}$$

trong đó $$\mathbf{A} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$$ và $$\det(\mathbf{A}) = ad - bc$$.

**Lưu ý:** Không phải ma trận vuông nào cũng có nghịch đảo. Một ma trận **khả nghịch** (không suy biến) khi và chỉ khi định thức của nó khác không.

---

## Ứng dụng trong tối ưu hóa

Ma trận và phép biến đổi tuyến tính xuất hiện xuyên suốt các bài toán tối ưu hóa:

### 1. Hệ phương trình tuyến tính

Nhiều bài toán tối ưu hóa quy về việc giải hệ $$\mathbf{Ax} = \mathbf{b}$$:
- **Nghiệm duy nhất:** $$\mathbf{x} = \mathbf{A}^{-1}\mathbf{b}$$ (khi $$\mathbf{A}$$ vuông và khả nghịch).
- **Bình phương tối thiểu:** cực tiểu hóa $$\|\mathbf{Ax} - \mathbf{b}\|^2$$ khi hệ không có nghiệm chính xác.

### 2. Dạng toàn phương

Các hàm toàn phương rất phổ biến trong tối ưu hóa:
$$f(\mathbf{x}) = \mathbf{x}^T\mathbf{Q}\mathbf{x} + \mathbf{c}^T\mathbf{x} + d$$

Ma trận $$\mathbf{Q}$$ quyết định độ cong và tính lồi của hàm số.

### 3. Quy hoạch tuyến tính

Dạng chuẩn: cực tiểu hóa $$\mathbf{c}^T\mathbf{x}$$ với điều kiện $$\mathbf{Ax} = \mathbf{b}$$, $$\mathbf{x} \geq \mathbf{0}$$.

### 4. Biểu diễn ràng buộc

- **Ràng buộc đẳng thức:** $$\mathbf{Ax} = \mathbf{b}$$
- **Ràng buộc bất đẳng thức:** $$\mathbf{Ax} \leq \mathbf{b}$$

### 5. Phép đổi biến

Áp dụng phép đổi biến tuyến tính $$\mathbf{y} = \mathbf{T}\mathbf{x}$$ có thể đơn giản hóa cấu trúc của bài toán tối ưu hóa.

### Ví dụ: Tối ưu danh mục đầu tư

Trong tài chính định lượng, bài toán cực tiểu hóa rủi ro danh mục có dạng:
$$\text{cực tiểu hóa } \mathbf{w}^T\mathbf{\Sigma}\mathbf{w}$$

trong đó $$\mathbf{w}$$ là vector trọng số phân bổ vốn và $$\mathbf{\Sigma}$$ là ma trận hiệp phương sai lợi suất của các tài sản.

Nắm vững ma trận và phép biến đổi tuyến tính cung cấp nền tảng để mô hình hóa, phân tích và giải hiệu quả nhiều bài toán tối ưu hóa.
