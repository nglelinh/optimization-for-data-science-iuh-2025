---
layout: post
title: '17-05 Điều kiện tối ưu cho quy hoạch bán xác định (SDP)'
chapter: '17'
order: 9
owner: Minjoo Lee
categories:
- chapter17
lang: vi
---

Nếu quy hoạch tuyến tính tối ưu trên góc phần tư không âm $$x \ge 0$$ của các vector, thì **quy hoạch bán xác định (SDP)** nâng toàn bộ câu chuyện đó lên một chiều không gian hoàn toàn mới: góc nón các ma trận đối xứng nửa xác định dương $$X \succeq 0$$. Điều kỳ diệu là hầu hết công thức đẹp đẽ của LP đều dịch chuyển sang SDP một cách tự nhiên — tích vô hướng vector trở thành tích vết $$\operatorname{tr}(CX)$$, điều kiện bù chặt $$x_i s_i = 0$$ trở thành tích ma trận $$XS = 0$$ — nhưng có một "cạm bẫy" đại số tinh tế xuất hiện: tích hai ma trận đối xứng $$X$$ và $$S$$ nhìn chung **không còn đối xứng** nữa!

## Kiến thức cần nhớ: Mở rộng PD-IPM từ vector sang không gian ma trận đối xứng

Để không bị choáng ngợp trước các ký hiệu toán tử $$\mathcal{A}, \mathcal{A}^*$$ và điều kiện $$XS = \tau I$$, hãy nắm vững bốn trụ cột nền tảng của SDP:

- **Không gian ma trận đối xứng $$\mathbb{S}^n$$ và tích vô hướng vết:** Trang bị tích vô hướng $$\langle C, X \rangle = \operatorname{tr}(CX) = \sum_{i,j} C_{ij} X_{ij}$$ biến $$\mathbb{S}^n$$ thành một không gian Euclid thực thụ, nơi các ràng buộc $$\operatorname{tr}(A_i X) = b_i$$ đóng vai trò các siêu phẳng tuyến tính.
- **Nón nửa xác định dương $$\mathbb{S}_+^n$$ và tính tự đối ngẫu:** Ma trận $$X \succeq 0$$ nghĩa là mọi trị riêng của $$X$$ đều không âm. Nón $$\mathbb{S}_+^n$$ là nón lồi đóng và **tự đối ngẫu** ($$\operatorname{tr}(XS) \ge 0$$ với mọi $$X, S \succeq 0$$), khiến cặp bài toán SDP gốc–đối ngẫu đối xứng hoàn toàn.
- **Điều kiện bù chặt ma trận $$XS = 0$$:** Với $$X, S \succeq 0$$, điều kiện $$\operatorname{tr}(XS) = 0$$ tương đương với $$XS = 0$$. Điều này có nghĩa là $$X$$ và $$S$$ giao hoán và có thể đồng thời chéo hóa: ở hướng nào $$X$$ có trị riêng dương thì $$S$$ bắt buộc có trị riêng bằng $$0$$.
- **Đường trung tâm $$XS = \tau I$$ và bài toán đối xứng hóa hướng Newton:** Khi tuyến tính hóa $$XS = \tau I$$, ta thu được $$X\Delta S + \Delta X S = \tau I - XS$$. Vì vế trái không tự động đối xứng ngay cả khi $$\Delta X, \Delta S \in \mathbb{S}^n$$, các bộ giải SDP phải dùng các phép đối xứng hóa (như hướng AHO, HKM hay Nesterov–Todd) để hệ phương trình vuông và giải được duy nhất.

### Giải thích: Tính tay đường trung tâm SDP $$2 \times 2$$ với $$XS = \tau I$$

Xét bài toán SDP trên không gian ma trận đối xứng $$2 \times 2$$:

$$\min_{X \in \mathbb{S}^2} \; \operatorname{tr}(CX) \qquad \text{với điều kiện} \qquad \operatorname{tr}(X) = 2, \; X \succeq 0, \qquad C = \begin{bmatrix} 1 & 0 \\ 0 & 3 \end{bmatrix}.$$

Bài toán đối ngẫu tương ứng là $$\max_{y \in \mathbb{R}} \; 2y$$ với điều kiện $$S = C - yI = \begin{bmatrix} 1 - y & 0 \\ 0 & 3 - y \end{bmatrix} \succeq 0$$.

1. **Nghiệm tối ưu KKT ($$\tau = 0$$):** Điều kiện $$S \succeq 0$$ đòi hỏi $$1 - y \ge 0$$ và $$3 - y \ge 0 \implies y \le 1$$. Do đó $$y^\star = 1$$, $$S^\star = \operatorname{diag}(0, 2)$$. Để $$\operatorname{tr}(X^\star) = 2$$ và $$X^\star S^\star = 0$$, ta buộc phải có $$X^\star = \operatorname{diag}(2, 0)$$. Kiểm tra giá trị tối ưu: $$\operatorname{tr}(CX^\star) = 1(2) + 3(0) = 2 = 2y^\star$$.
2. **Tìm điểm trên đường trung tâm tại $$\tau = 0.2$$:** Ta cần $$X, S \succ 0$$ đường chéo $$X = \operatorname{diag}(x_1, x_2)$$, $$S = \operatorname{diag}(1-y, 3-y)$$ thỏa mãn $$XS = 0.2 I$$ và $$x_1 + x_2 = 2$$:
   $$x_1 = \frac{0.2}{1 - y}, \qquad x_2 = \frac{0.2}{3 - y} \implies \frac{0.2}{1 - y} + \frac{0.2}{3 - y} = 2.$$
3. **Giải phương trình bậc hai cho $$y$$:** Rút gọn cho $$y^2 - 3.8y + 2.6 = 0$$. Lấy nghiệm thỏa mãn $$y < 1$$ (để $$S \succ 0$$):
   $$y(0.2) = \frac{3.8 - \sqrt{3.8^2 - 4(2.6)}}{2} = \frac{3.8 - \sqrt{4.04}}{2} \approx 0.8950.$$
4. **Kiểm tra cặp ma trận đường trung tâm:**
   - $$S(0.2) \approx \operatorname{diag}(0.1050, \; 2.1050) \succ 0$$.
   - $$X(0.2) \approx \operatorname{diag}(1.9048, \; 0.0950) \succ 0$$ (tổng vết $$= 1.9998 \approx 2$$).
   - Khoảng cách đối ngẫu: $$\operatorname{tr}(X(0.2)S(0.2)) = 2 \times 0.2 = 0.4 = n\tau$$, đúng bằng công thức tổng quát cho ma trận cỡ $$n \times n$$!

---

Trong phần này, chúng ta xét phương pháp điểm trong gốc-đối ngẫu áp dụng cho bài toán quy hoạch bán xác định (SDP — semidefinite programming).

## Quy hoạch bán xác định (SDP)
Bài toán SDP gốc được phát biểu như sau:
>$$
>\begin{align}
>    &\min_{X} && {C \cdot X} \\\\
>    &\text{subject to } && {A_i \cdot X = b_i, i = 1,...,m} \\\\
>    & &&{X \succeq 0}
>\end{align}
>$$


Bài toán SDP đối ngẫu tương ứng là:
>$$
>\begin{align}
>    &\max_{y} && {b^Ty} \\\\
>    &\text{subject to } && {\sum^m_{i=1} y_iA_i + S = C} \\\\
>    & &&{S \succeq 0}
>\end{align}
>$$

Nhắc lại rằng tích vô hướng vết (trace inner product) trên không gian ma trận đối xứng $$\mathbb{S}^n$$ được định nghĩa là:
> $$X \cdot S = \text{trace}(XS)$$

## Điều kiện tối ưu cho SDP
Cặp bài toán SDP gốc và đối ngẫu có thể được viết gọn bằng toán tử tuyến tính $$\mathcal{A}: \mathbb{S}^n \to \mathbb{R}^m$$ và toán tử liên hợp $$\mathcal{A}^*$$ của nó:

>$$
>\begin{align}
>    &\min_{X} && {C \cdot X} & \qquad \qquad \qquad & \max_{y,S}  && {b^Ty} \\\\
>    &\text{subject to } && {\mathcal{A}(X) = b} & \qquad \qquad \qquad & \text{subject to } && {\mathcal{A}^{*}(y) + S = C} \\\\
>    & &&{X \succeq 0} & \qquad \qquad \qquad & &&{S \succeq 0}
>\end{align}
>$$


Giả sử tính đối ngẫu mạnh được thỏa mãn, thì $$X^{\star}$$ và $$(y^{\star}, S^{\star})$$ là cặp nghiệm tối ưu gốc – đối ngẫu khi và chỉ khi $$(X^{\star}, y^{\star}, S^{\star})$$ thỏa mãn hệ điều kiện sau:

> $$
> \begin{array}{rcl}
> \mathcal{A}^*(y) + S & = & C \\\
> \mathcal{A}(X) & = & b \\\
> XS & = & 0 \\\
> X,S & \succeq & 0
> \end{array}
> $$


## Đường trung tâm cho SDP
**Bài toán chắn gốc**
>$$
>\begin{align}
>    &\min_{X} && {C \cdot X - \tau \log\det(X)} \\\\
>    &\text{subject to } && {\mathcal{A}(X) = b} 
>\end{align}
>$$


**Bài toán chắn đối ngẫu**
>$$
>\begin{align}
>    &\max_{y, S} && {b^Ty + \tau \log\det(S)} \\\\
>    &\text{subject to } && {\mathcal{A}^*(y) + S = C} 
>\end{align}
>$$


**Điều kiện tối ưu cho các bài toán chắn gốc và đối ngẫu**
> $$
> \begin{array}{rcl}
> \mathcal{A}^*(y) + S & = & C \\\
> \mathcal{A}(X) & = & b \\\
> XS & = & \tau I \\\
> X,S & \succ & 0
> \end{array}
> $$


## Bước Newton
Hệ phương trình đường trung tâm gốc:
> $$
> \begin{array}{rcl}
> \mathcal{A}^*(y) + \tau X^{-1} & = & C \\\
> \mathcal{A}(X) & = & b \\\
> X & \succ & 0
> \end{array}
> $$


Phương trình Newton tương ứng (sử dụng vi phân $$d(X^{-1}) = -X^{-1} \Delta X X^{-1}$$):
> $$-\tau X^{-1}\Delta X X^{-1} +\mathcal{A}^*(\Delta y) = -(\mathcal{A}^*(y) + \tau X^{-1} -C)$$
> $$\mathcal{A}(\Delta X) = -(\mathcal{A}(X)-b)$$

Hệ phương trình đường trung tâm và phương trình Newton cho bài toán đối ngẫu theo $$(y, S)$$ được xây dựng hoàn toàn tương tự.

## Bước Newton gốc-đối ngẫu 
Hệ phương trình đường trung tâm gốc-đối ngẫu:
> $$\begin{bmatrix}
\mathcal{A}^*(y) + S - C  \\\
\mathcal{A}(X) - b \\\
XS
\end{bmatrix} =
\begin{bmatrix}
0 \\\
0 \\\
\tau I
\end{bmatrix}
, \quad X, S \succ 0
$$

Hệ bước Newton:
> $$\begin{bmatrix}
0 & \mathcal{A}^* & I \\\
\mathcal{A} & 0 & 0 \\\
S & 0 & X 
\end{bmatrix}
\begin{bmatrix}
\Delta X \\\
\Delta y \\\
\Delta S
\end{bmatrix}= -
\begin{bmatrix}
\mathcal{A}^*(y) + S - C \\\
\mathcal{A}(X) - b \\\
XS - \tau I 
\end{bmatrix}$$
