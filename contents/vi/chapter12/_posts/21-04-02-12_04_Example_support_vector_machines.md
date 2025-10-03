---
layout: post
title: 12-04 Ví dụ Máy Vector Hỗ Trợ (Support Vector Machines - SVM)
chapter: '12'
order: 5
owner: Wontak Ryu
categories:
- chapter12
lang: vi
lesson_type: required
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

# Máy Vector Hỗ Trợ (Support Vector Machines - SVM)

## 1. Giới thiệu

**Support Vector Machine (SVM)** là một thuật toán phân loại mạnh mẽ, tìm siêu phẳng tối ưu để phân tách các lớp dữ liệu với **margin lớn nhất**.

### Ý tưởng cốt lõi

- **Siêu phẳng**: $\beta^T x + \beta_0 = 0$ phân tách hai lớp
- **Margin**: Khoảng cách từ siêu phẳng đến điểm gần nhất = $\frac{2}{\|\beta\|}$
- **Mục tiêu**: Maximize margin $\Leftrightarrow$ Minimize $\|\beta\|$

## 2. Hard-Margin SVM (Dữ liệu tách được)

Khi dữ liệu **tách được tuyến tính**:

$$
\begin{align}
&\min_{\beta, \beta_0} &&{\frac{1}{2} \|\beta\|_2^2} \\
&\text{s.t.} && y_i (\beta^T x_i + \beta_0) \geq 1, \quad i = 1, \ldots, n
\end{align}
$$

**Giải thích:**
- Hàm mục tiêu: Minimize $\|\beta\|$ để maximize margin
- Ràng buộc: Mọi điểm phải cách siêu phẳng ít nhất 1 đơn vị (theo metric)

## 3. Soft-Margin SVM (Dữ liệu không tách được)

Trong thực tế, dữ liệu thường **không tách được hoàn toàn**. Giới thiệu **slack variables** $\xi_i \geq 0$:

$$
\begin{align}
&\min_{\beta, \beta_0, \xi} &&{\frac{1}{2} \|\beta\|_2^2 + C\sum_{i=1}^n \xi_i} \\
&\text{s.t.} &&{\xi_i \geq 0, \quad i = 1, \ldots, n}\\
& && y_i (\beta^T x_i + \beta_0) \geq 1 - \xi_i, \quad i = 1, \ldots, n
\end{align}
$$

Với $y \in \{-1, 1\}^n$ và $X \in \mathbb{R}^{n \times p}$.

### Giải thích các thành phần

**1) Slack variable $\xi_i$:**
- $\xi_i = 0$: Điểm phân loại đúng, ngoài margin
- $0 < \xi_i < 1$: Điểm trong margin zone, vẫn đúng phía
- $\xi_i = 1$: Điểm nằm trên siêu phẳng
- $\xi_i > 1$: Điểm bị phân loại sai

**2) Tham số $C > 0$:**
- $C$ lớn: Phạt nặng vi phạm → margin nhỏ, ít misclassify
- $C$ nhỏ: Cho phép nhiều vi phạm → margin lớn
- **Trade-off**: Margin width vs. Training error

**3) Hàm mục tiêu:**
- $\frac{1}{2}\|\beta\|_2^2$: Maximize margin
- $C\sum \xi_i$: Minimize total violation

## 4. Điều kiện KKT cho SVM

### 4.1. Hàm Lagrangian

Với nhân tử Lagrange $v \geq 0$ (cho $\xi_i \geq 0$) và $w \geq 0$ (cho ràng buộc margin):

$$
\begin{align}
L(\beta, \beta_0, \xi, v, w) = &\frac{1}{2} \|\beta\|_2^2 + C\sum_{i=1}^n \xi_i - \sum_{i=1}^n v_i \xi_i \\
&+ \sum_{i=1}^n w_i (1 - \xi_i - y_i (\beta^T x_i + \beta_0))
\end{align}
$$

### 4.2. Điều kiện Stationarity

**1) Đạo hàm theo $\beta$:**
$$
\frac{\partial L}{\partial \beta} = \beta - \sum_{i=1}^n w_i y_i x_i = 0
$$

$$
\Rightarrow \boxed{\beta^\star = \sum_{i=1}^n w_i^\star y_i x_i}
$$

**Ý nghĩa quan trọng:** Nghiệm tối ưu là tổ hợp tuyến tính của các điểm dữ liệu!

**2) Đạo hàm theo $\beta_0$:**
$$
\boxed{\sum_{i=1}^n w_i^\star y_i = 0}
$$

**3) Đạo hàm theo $\xi_i$:**
$$
C - v_i - w_i = 0 \Rightarrow \boxed{v_i^\star = C - w_i^\star}
$$

**Suy ra:** $0 \leq w_i^\star \leq C$ (vì $v_i^\star \geq 0$)

### 4.3. Complementary Slackness

**1) Cho $\xi_i \geq 0$:**
$$
v_i^\star \xi_i^\star = 0, \quad i = 1, \ldots, n
$$

**2) Cho ràng buộc margin:**
$$
w_i^\star (1 - \xi_i^\star - y_i (\beta^{\star T} x_i + \beta_0^\star)) = 0, \quad i = 1, \ldots, n
$$

### 4.4. Phân tích các trường hợp

#### **Trường hợp 1: $w_i^\star = 0$ (Non-support vector)**

- Từ $v_i^\star = C > 0$ → $\xi_i^\star = 0$ (CS 1)
- Từ CS 2: Ràng buộc margin không chặt
- **Kết luận:** $y_i(\beta^{\star T} x_i + \beta_0^\star) > 1$ 
- Điểm nằm **ngoài margin**, phân loại đúng, không ảnh hưởng đến nghiệm

#### **Trường hợp 2: $0 < w_i^\star < C$ (Support vector trên margin)**

- Cả $v_i^\star$ và $w_i^\star$ đều dương
- Từ CS: $\xi_i^\star = 0$ và $y_i(\beta^{\star T} x_i + \beta_0^\star) = 1$
- **Kết luận:** Điểm nằm **đúng trên margin boundary**
- Quan trọng nhất trong xác định siêu phẳng!

#### **Trường hợp 3: $w_i^\star = C$ (Support vector vi phạm margin)**

- Từ $v_i^\star = 0$: không ràng buộc $\xi_i^\star$
- Từ CS 2: $y_i(\beta^{\star T} x_i + \beta_0^\star) = 1 - \xi_i^\star$

**Phân loại con:**
- $\xi_i^\star = 0$: Trên margin (giống trường hợp 2)
- $0 < \xi_i^\star < 1$: Trong margin zone, phân loại đúng
- $\xi_i^\star \geq 1$: Bị phân loại sai (misclassified)

## 5. Support Vectors

### Định nghĩa

**Support vectors** là các điểm có $w_i^\star > 0$.

Từ điều kiện stationarity:
$$
\beta^\star = \sum_{i: w_i^\star > 0} w_i^\star y_i x_i
$$

→ **Chỉ support vectors quyết định siêu phẳng!**

### Phân loại Support Vectors

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter12/svm.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">$$ \text{[Hình 1] Minh họa các support vectors với } \xi^\star \neq 0 \text{ [3]}$$ </figcaption>
</p>
</figure>

**1) Support vectors trên margin** ($\xi_i^\star = 0$, $0 < w_i^\star \leq C$):
- Nằm đúng trên đường biên margin
- $y_i(\beta^{\star T} x_i + \beta_0^\star) = 1$
- Quan trọng nhất trong xác định siêu phẳng

**2) Support vectors trong margin** ($0 < \xi_i^\star < 1$, $w_i^\star = C$):
- Nằm giữa margin và siêu phẳng
- Vẫn phân loại đúng nhưng vi phạm margin
- Thường là outliers hoặc điểm gần biên

**3) Support vectors bị misclassify** ($\xi_i^\star \geq 1$, $w_i^\star = C$):
- Nằm sai phía siêu phẳng
- Bị phân loại sai
- Đóng góp nhiều vào penalty $C\sum \xi_i$

### Ý nghĩa thực tiễn

1. **Hiệu quả tính toán:**
   - Chỉ cần lưu trữ $s$ support vectors (thường $s \ll n$)
   - Prediction: $\hat{y} = \text{sign}(\sum_{SV} w_i y_i \langle x_i, x \rangle + \beta_0)$

2. **Ổn định của mô hình:**
   - Chỉ phụ thuộc support vectors
   - Các điểm xa margin không ảnh hưởng
   - Robust với outliers (nếu $C$ phù hợp)

3. **Sparsity:**
   - Nhiều $w_i = 0$ (non-support vectors)
   - Mô hình "sparse" và dễ giải thích

## 6. Ví dụ Chi tiết

### Ví dụ 1D: Dữ liệu đơn giản

**Dữ liệu:**
- Lớp $+1$: $x_1 = 3, x_2 = 4$
- Lớp $-1$: $x_3 = 1, x_4 = 2$

**Bài toán hard-margin:**
$$
\begin{align}
\min_{\beta, \beta_0} \quad &\frac{1}{2}\beta^2 \\
\text{s.t.} \quad &3\beta + \beta_0 \geq 1, \quad 4\beta + \beta_0 \geq 1 \\
&-\beta - \beta_0 \geq 1, \quad -2\beta - \beta_0 \geq 1
\end{align}
$$

**Giải pháp hình học:**
- Siêu phẳng tối ưu nằm giữa $x = 2$ và $x = 3$
- Điểm gần nhất: $x_2 = 4$ và $x_4 = 2$

**Điều kiện margin chặt:**
$$
\begin{cases}
4\beta + \beta_0 = 1 \\
2\beta + \beta_0 = -1
\end{cases}
\Rightarrow \beta = 1, \quad \beta_0 = -3
$$

**Nghiệm:**
- Siêu phẳng: $x - 3 = 0$ hay $x = 3$ (sai! phải là $x=2.5$)
- Hãy kiểm tra lại...

**Sửa lại:** Điểm gần nhất phải là $x = 3$ (lớp +1) và $x = 2$ (lớp -1):
$$
\begin{cases}
3\beta + \beta_0 = 1 \\
2\beta + \beta_0 = -1
\end{cases}
\Rightarrow \beta = 2, \quad \beta_0 = -5
$$

- Siêu phẳng: $2x - 5 = 0$ hay $x = 2.5$ ✓
- Margin: $\frac{2}{|\beta|} = \frac{2}{2} = 1$
- Support vectors: $x = 3$ và $x = 2$

## 7. Bài toán Đối ngẫu

### Dual Problem

Thế các điều kiện stationarity vào Lagrangian:

$$
\begin{align}
\max_{w} \quad &\sum_{i=1}^n w_i - \frac{1}{2} \sum_{i,j} w_i w_j y_i y_j \langle x_i, x_j \rangle \\
\text{s.t.} \quad &\sum_{i=1}^n w_i y_i = 0 \\
&0 \leq w_i \leq C, \quad i = 1, \ldots, n
\end{align}
$$

### Ưu điểm

1. **Kernel trick**: Chỉ phụ thuộc vào $\langle x_i, x_j \rangle$ → có thể dùng kernel
2. **Ít ràng buộc hơn**: Chỉ 1 ràng buộc đẳng thức + box constraints
3. **Solver hiệu quả**: SMO, LIBSVM

## 8. Ứng dụng KKT trong SVM

### 8.1. Kiểm tra tính tối ưu

Dùng điều kiện KKT để verify nghiệm:
1. Primal/Dual feasibility
2. Stationarity
3. Complementary slackness

### 8.2. Tính $\beta_0$

Từ support vectors trên margin ($0 < w_i < C$):
$$
\beta_0 = y_i - \beta^T x_i = y_i - \sum_{j} w_j y_j \langle x_j, x_i \rangle
$$

**Thực tế:** Lấy trung bình trên tất cả SV trên margin:
$$
\beta_0 = \frac{1}{|S|} \sum_{i \in S} \left( y_i - \sum_{j} w_j y_j \langle x_j, x_i \rangle \right)
$$

### 8.3. Lọc Support Vectors

Trước khi giải, loại bỏ điểm chắc chắn không phải SV:
$$
y_i(\beta_{\text{init}}^T x_i + \beta_{0,\text{init}}) \gg 1
$$

→ Tăng hiệu quả cho datasets lớn

## 9. Bài tập Thực hành

### Bài tập 1: Phân tích Support Vectors

Cho nghiệm SVM với $C = 1$:
```
w = (0, 0.5, 0.3, 1, 0, 1, 0.2)
ξ = (0, 0, 0.2, 0.8, 0, 1.5, 0)
```

**Yêu cầu:**
a) Xác định support vectors  
b) Phân loại theo vị trí (trên margin, trong margin, misclassified)  
c) Giải thích $w_1 = 0$ nhưng $\xi_1 = 0$

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Support vectors:** $i \in \{2, 3, 4, 6, 7\}$ (vì $w_i > 0$)

**b) Phân loại:**
- **Trên margin**: $i = 2, 7$ ($\xi_i = 0$, $0 < w_i < C$)
- **Trong margin**: $i = 3, 4$ ($0 < \xi_i < 1$, $w_i = C$)
- **Misclassified**: $i = 6$ ($\xi_6 = 1.5 > 1$, $w_6 = C$)

**c)** $w_1 = 0$ nghĩa là không phải SV. Từ CS: $v_1 = C - 0 = 1 > 0$ → $\xi_1 = 0$ ✓  
Điểm $x_1$ nằm xa margin, phân loại đúng.

</details>

---

### Bài tập 2: Tính toán từ KKT

Cho $C = 2$, $n = 3$, $p = 2$:
```
x₁ = (0, 1), y₁ = +1, w₁ = 0.5
x₂ = (1, 0), y₂ = +1, w₂ = 0.5  
x₃ = (0, 0), y₃ = -1, w₃ = 1
```
$\xi_1 = \xi_2 = 0$, $\xi_3 = 0.2$.

**Yêu cầu:**
a) Tính $\beta$ từ stationarity  
b) Tính $\beta_0$ từ SV trên margin  
c) Kiểm tra CS cho $i=3$

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a)** $\beta = \sum w_i y_i x_i = 0.5(0,1) + 0.5(1,0) + 1 \cdot (-1)(0,0) = (0.5, 0.5)$

**b)** Từ $i=1$: $y_1(\beta^T x_1 + \beta_0) = 1$  
$1 \cdot (0.5 + \beta_0) = 1$ → $\beta_0 = 0.5$

**c)** CS: $w_3(1 - \xi_3 - y_3(\beta^T x_3 + \beta_0)) = 0$  
$y_3(\beta^T x_3 + \beta_0) = -1(0.5) = -0.5$  
$1(1 - 0.2 - (-0.5)) = 1.3 \neq 0$ ✗  

**Kết luận:** CS vi phạm! Có lỗi trong dữ liệu.

</details>

---

## 10. Tóm tắt

### Các điểm chính

1. **SVM tìm siêu phẳng** với margin lớn nhất
2. **Soft-margin** cho phép vi phạm qua $\xi_i$, điều khiển bởi $C$
3. **Điều kiện KKT** cho:
   - $\beta = \sum w_i y_i x_i$ (chỉ phụ thuộc support vectors)
   - Phân loại điểm thành SV và non-SV
4. **Support vectors** quyết định siêu phẳng, thường $s \ll n$
5. **Complementary slackness** giải thích khi nào $w_i = 0$ hay $w_i > 0$

### Ý nghĩa thực tiễn

Điều kiện KKT không dùng trực tiếp để giải SVM (dùng SMO, LIBSVM), nhưng giúp:
- Kiểm chứng tính tối ưu
- Hiểu cấu trúc nghiệm (sparsity, support vectors)
- Phát triển thuật toán hiệu quả
- Phân tích độ nhạy của mô hình

---

## 📚 Tài liệu tham khảo

1. **Vapnik, V. N.** (1995). *The Nature of Statistical Learning Theory*. Springer.
2. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Chapter 12.
3. **Hastie, T., et al.** (2009). *The Elements of Statistical Learning* (2nd ed.). Springer. Chapter 12.
4. **Cristianini, N., & Shawe-Taylor, J.** (2000). *An Introduction to Support Vector Machines*. Cambridge University Press.
