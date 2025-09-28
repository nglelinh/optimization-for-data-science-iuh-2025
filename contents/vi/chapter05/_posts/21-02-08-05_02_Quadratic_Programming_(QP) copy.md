---
layout: post
title: 05-02 Quy Hoạch Bậc Hai (QP)
chapter: '05'
order: 3
owner: Hooncheol Shin
categories:
- chapter05
lang: vi
lesson_type: required
---

Một **Chương trình Bậc hai** (QP) là một bài toán tối ưu lồi trong đó hàm mục tiêu là một hàm bậc hai lồi và tất cả các hàm ràng buộc đều là affine. Chương trình bậc hai tổng quát được phát biểu như:

### Chương trình Bậc hai Tổng quát
$$
\begin{align}
    \text{minimize}_{x} \quad &\frac{1}{2}x^T P x + q^T x + r \\
    \text{subject to} \quad &Gx \preceq h \\
    &Ax = b
\end{align}
$$

**trong đó:**
- $$P \in \mathbb{S}_{+}^n$$ (ma trận bán xác định dương)
- $$G \in \mathbb{R}^{m \times n}$$ (ma trận ràng buộc bất đẳng thức)  
- $$A \in \mathbb{R}^{p \times n}$$ (ma trận ràng buộc đẳng thức)
- $$x \in \mathbb{R}^n$$ (biến quyết định)

**Tính chất Chính của QP:**
- Hằng số $$r$$ trong hàm mục tiêu không ảnh hưởng đến quá trình tối ưu hóa hoặc kết quả và có thể bỏ qua.
- Nếu $$P \in \mathbb{S}_{+}^n$$ không được thỏa mãn, bài toán không lồi.
- Ngay cả khi không được nêu rõ, QP giả định $$P \in \mathbb{S}_{+}^n$$.
- Bài toán trên tìm nghiệm tối ưu $$x^*$$ của hàm bậc hai lồi $$\frac{1}{2}x^T P x + q^T x + r$$ trên một tập khả thi đa diện.

### Hiểu về $$\mathbb{S}_{+}^n$$ (Nón Bán xác định Dương)

Ký hiệu $$\mathbb{S}_{+}^n$$ đại diện cho **nón bán xác định dương**, đây là một khái niệm cơ bản trong tối ưu lồi:

**Định nghĩa:**
> $$\mathbb{S}_{+}^n = \{ X \in \mathbb{S}^n : X \succeq 0 \}$$

**trong đó:**
- $$\mathbb{S}^n$$ là tập tất cả các **ma trận đối xứng** $$n \times n$$
- $$X \succeq 0$$ có nghĩa là ma trận $$X$$ là **bán xác định dương**

**Tính chất Chính:**

1. **Điều kiện bán xác định dương**: Một ma trận $$P$$ là bán xác định dương nếu:
   - Tất cả các giá trị riêng của $$P$$ đều không âm ($$\lambda_i \geq 0$$)
   - Với mọi vector $$v$$, chúng ta có $$v^T P v \geq 0$$

2. **Tính chất nón lồi**: $$\mathbb{S}_{+}^n$$ là một nón lồi vì nếu $$\theta_1, \theta_2 \geq 0$$ và $$A, B \in \mathbb{S}_{+}^n$$, thì $$\theta_1 A + \theta_2 B \in \mathbb{S}_{+}^n$$

**Ví dụ cho $$n=2$$:**
Với ma trận $$2 \times 2$$ $$P = \begin{bmatrix} a & b \\ b & c \end{bmatrix}$$, điều kiện $$P \in \mathbb{S}_{+}^2$$ yêu cầu:
- $$a \geq 0$$ (các phần tử đường chéo không âm)
- $$c \geq 0$$ (các phần tử đường chéo không âm)  
- $$ac \geq b^2$$ (định thức không âm)

**Tại sao điều này quan trọng đối với QP?**
- Điều kiện $$P \in \mathbb{S}_{+}^n$$ đảm bảo rằng hàm bậc hai $$(1/2)x^T P x + q^T x + r$$ là **lồi**
- Không có điều kiện này, bài toán có thể có nhiều cực tiểu địa phương và sẽ không là một bài toán tối ưu lồi
- Điều này đảm bảo rằng bất kỳ cực tiểu địa phương nào cũng là cực tiểu toàn cục

### Hiểu về $$Gx \preceq h$$ (Bất đẳng thức Theo thành phần)

Ký hiệu $$Gx \preceq h$$ đại diện cho **ràng buộc bất đẳng thức theo thành phần**, đây là cách gọn gàng để viết nhiều ràng buộc bất đẳng thức tuyến tính:

**Định nghĩa:**
$$Gx \preceq h \quad \Leftrightarrow \quad (Gx)_i \leq h_i \text{ với mọi } i = 1, 2, \ldots, m$$

**where:**
- $$G \in \mathbb{R}^{m \times n}$$ is the constraint matrix
- $$x \in \mathbb{R}^n$$ is the decision variable vector
- $$h \in \mathbb{R}^m$$ is the right-hand side vector
- $$m$$ is the number of inequality constraints

**Expanded Form:**
The single matrix inequality $$Gx \preceq h$$ is equivalent to the system:
$$
\begin{align}
g_1^T x &\leq h_1 \\
g_2^T x &\leq h_2 \\
&\vdots \\
g_m^T x &\leq h_m
\end{align}
$$

where $$g_i^T$$ is the $$i$$-th row of matrix $$G$$.

**Example:**
Consider $$G = \begin{bmatrix} 1 & 2 \\ -1 & 3 \\ 0 & -1 \end{bmatrix}$$, $$x = \begin{bmatrix} x_1 \\ x_2 \end{bmatrix}$$, and $$h = \begin{bmatrix} 5 \\ 2 \\ -1 \end{bmatrix}$$

Then $$Gx \preceq h$$ means:
$$
\begin{align}
x_1 + 2x_2 &\leq 5 \\
-x_1 + 3x_2 &\leq 2 \\
-x_2 &\leq -1 \quad \text{(i.e., } x_2 \geq 1\text{)}
\end{align}
$$

**Geometric Interpretation:**
- Each inequality $$g_i^T x \leq h_i$$ defines a **half-space** in $$\mathbb{R}^n$$
- The feasible region is the **intersection** of all these half-spaces
- This intersection forms a **polyhedron** (or polytope if bounded)
- The constraint $$Gx \preceq h$$ defines the **polyhedral feasible set** for the QP

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter05/05_02_geometric_interpretation_of_QP.png" alt="[Fig 1] Geometric interpretation of QP [1]" width="70%">
  <figcaption style="text-align: center;">[Fig 1] Geometric interpretation of QP [1]</figcaption>
</p>
</figure>

## QP in Standard Form

The standard form of a quadratic program is:

### Standard Form QP
$$
\begin{align}
    \text{minimize}_{x} \quad &\frac{1}{2}x^T P x + q^T x + r \\
    \text{subject to} \quad &A x = b \\
    &x \succeq 0
\end{align}
$$

Any general quadratic program can be converted to standard form using the following steps:

### Converting QPs to Standard Form

**Step 1.** Use slack variables $$s$$ to convert inequality constraints into equality constraints:
$$
\begin{align}
    \text{minimize}_{x, s} \quad &\frac{1}{2}x^T P x + q^T x + r \\
    \text{subject to} \quad &Gx + s = h \\
    &Ax = b \\
    &s \succeq 0
\end{align}
$$

**Step 2.** Replace $$x$$ with two nonnegative variables:
$$x = x^{+} - x^{-}, \quad \text{where } x^{+}, x^{-} \succeq 0$$

$$
\begin{align}
    \text{minimize}_{x^{+}, x^{-}, s} \quad &\frac{1}{2}(x^{+} - x^{-})^T P (x^{+} - x^{-}) + q^T x^{+} - q^T x^{-} + r\\
    \text{subject to} \quad &Gx^{+} - Gx^{-} + s = h \\
    &Ax^{+} - Ax^{-} = b \\
    &s \succeq 0 \\
    &x^{+} \succeq 0, \quad x^{-} \succeq 0
\end{align}
$$

**Step 3.** Define $$\tilde{x}$$, $$\tilde{q}$$, $$\tilde{b}$$, $$\tilde{A}$$, $$\tilde{P}$$:

$$
\tilde{x} =
\begin{bmatrix}
x^{+} \\
x^{-} \\
s
\end{bmatrix}, \quad
\tilde{q} =
\begin{bmatrix}
q \\
-q \\
0
\end{bmatrix}, \quad
\tilde{b} =
\begin{bmatrix}
h \\
b
\end{bmatrix}
$$

$$
\tilde{A} =
\begin{bmatrix}
G & -G & I \\
A & -A & O
\end{bmatrix}, \quad
\tilde{P} =
\begin{bmatrix}
 P & -P & O \\
-P &  P & O \\
 O &  O & O
\end{bmatrix}
$$

**Step 4.** Substitute the expressions from Step 3 into the formulation:

$$
\begin{align}
    \text{minimize}_{\tilde{x}} \quad &\frac{1}{2}\tilde{x}^T \tilde{P} \tilde{x} + \tilde{q}^T \tilde{x} + r \\
    \text{subject to} \quad &\tilde{A} \tilde{x} = \tilde{b} \\
    &\tilde{x} \succeq 0
\end{align}
$$

## Linear Programming as a Special Case of QP

If the quadratic term is removed from the objective function of a quadratic program, it takes the form of a linear program. Thus, LP is a special case of QP, denoted as LP $$\subseteq$$ QP.

### Recall: General LP
$$
\begin{align}
    \text{minimize}_{x} \quad &c^T x + d \\
    \text{subject to} \quad &Gx \preceq h \\
    &Ax = b
\end{align}
$$
where $$G \in \mathbb{R}^{m \times n}$$ and $$A \in \mathbb{R}^{p \times n}$$.

### Ví dụ 1: Tối ưu hóa Danh mục Đầu tư

Bài toán này bao gồm việc cân bằng hợp lý giữa hiệu suất và rủi ro khi tạo một danh mục tài chính.

$$
\begin{align}
    \text{maximize}_{x} \quad &\mu^T x - \frac{\gamma}{2}x^T P x \\
    \text{subject to} \quad &\mathbf{1}^Tx = 1 \\
    &x \succeq 0
\end{align}
$$

**trong đó:**
- $$\mu$$: lợi nhuận kỳ vọng của các tài sản
- $$P$$: ma trận hiệp phương sai của lợi nhuận tài sản  
- $$\gamma$$: tham số tránh rủi ro (siêu tham số)
- $$x$$: nắm giữ danh mục (phần trăm)



### Ví dụ 2: Máy Vector Hỗ trợ (SVM)

Máy Vector Hỗ trợ (SVM) là một ví dụ của chương trình bậc hai. Dưới đây là C-SVM, một biến thể của SVM. Giải thích chi tiết về SVM nằm ngoài phạm vi của chương này và do đó sẽ được bỏ qua.

$$
\begin{align}
    \text{minimize}_{\beta, \beta_0, \xi} \quad &\frac{1}{2} \| \beta \|_2^2 + C \sum_{i=1}^{n} \xi_i \\
    \text{subject to} \quad &\xi_i \geq 0, \quad i = 1, \ldots, n \\
    &y_i (x_i^T \beta + \beta_0) \geq 1 - \xi_i, \quad i = 1, \ldots, n
\end{align}
$$

**cho trước:** $$y \in \{-1, 1\}^n$$ và $$X \in \mathbb{R}^{n \times p}$$ có các hàng $$x_1, \ldots, x_n$$.

### Ví dụ 3: Bình phương Tối thiểu trong Hồi quy

Bài toán tối thiểu hóa hàm bậc hai lồi sau tương ứng với một QP (không ràng buộc):
$$\| Ax - b \|_2^2 = x^T A^TA x - 2b^TAx + b^Tb$$

