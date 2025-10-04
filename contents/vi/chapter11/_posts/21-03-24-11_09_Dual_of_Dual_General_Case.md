---
layout: post
title: "11-09 Dual của Dual trong Tối Ưu Convex Tổng Quát"
chapter: "11"
order: 10
owner: "GitHub Copilot"
lang: vi
categories:
  - chapter11
---

Trong chương trước, chúng ta đã thấy rằng đối với Linear Programming, tính chất "dual của dual là primal" luôn đúng. Vậy tính chất này có còn đúng với bài toán tối ưu convex tổng quát không? Bài học này sẽ làm rõ điều đó.

---

## **Nhắc Lại: Dual của Dual trong LP**

Trong Linear Programming, chúng ta có tính chất đẹp:

**Bài toán Primal:**
$$
\begin{align}
\text{minimize} \quad & c^T x \\
\text{subject to} \quad & Ax \geq b, \\
& x \geq 0
\end{align}
$$

**Bài toán Dual:**
$$
\begin{align}
\text{maximize} \quad & b^T y \\
\text{subject to} \quad & A^T y \leq c, \\
& y \geq 0
\end{align}
$$

**Dual của Dual = Primal** (luôn đúng với LP)

Nhưng với bài toán convex tổng quát, điều này có còn đúng không?

---

## **Bài Toán Convex Tổng Quát**

### **Trường Hợp Tổng Quát**

Xét bài toán convex tổng quát (không chỉ LP):

$$
\begin{align}
\text{minimize} \quad & f_0(x) \\
\text{subject to} \quad & f_i(x) \leq 0, \; i = 1, \ldots, m, \\
& h_j(x) = 0, \; j = 1, \ldots, p,
\end{align}
$$

trong đó:
- $f_0, f_1, \ldots, f_m$ là các hàm convex
- $h_1, \ldots, h_p$ là các hàm affine
- $x \in \mathbb{R}^n$ là biến quyết định

---

## **Xây Dựng Dual Problem**

### **Hàm Lagrangian**

Dual được định nghĩa qua Lagrangian:

$$
\mathcal{L}(x, \lambda, \nu) = f_0(x) + \sum_{i=1}^m \lambda_i f_i(x) + \sum_{j=1}^p \nu_j h_j(x)
$$

với:
- $\lambda \in \mathbb{R}^m$, $\lambda \geq 0$: nhân tử Lagrange cho bất đẳng thức
- $\nu \in \mathbb{R}^p$: nhân tử Lagrange cho đẳng thức

### **Dual Function**

$$
g(\lambda, \nu) = \inf_x \mathcal{L}(x, \lambda, \nu)
$$

### **Bài toán Dual**

$$
\begin{align}
\text{maximize} \quad & g(\lambda, \nu) \\
\text{subject to} \quad & \lambda \geq 0
\end{align}
$$

---

## **Dual của Dual Cho Convex Problem**

### **Câu Hỏi Chính**

Nếu ta lấy dual của bài toán dual, có được lại bài toán primal ban đầu không?

### **Kết Quả**

**Định lý:** Nếu thỏa mãn các điều kiện sau:
1. Bài toán primal là **convex**
2. **Strong duality** thỏa mãn (duality gap = 0)
3. Thoả mãn **constraint qualification** (như Slater's condition)

Thì:

$$
\boxed{\text{Dual của Dual} = \text{Primal}}
$$

### **Điều Kiện Quan Trọng**

**Slater's Condition:** Tồn tại điểm strictly feasible:
- $f_i(\tilde{x}) < 0$ với mọi $i = 1, \ldots, m$
- $h_j(\tilde{x}) = 0$ với mọi $j = 1, \ldots, p$

**Lưu ý quan trọng:** Điều này **không luôn đúng** cho bài toán không convex!

---

## **So Sánh: LP vs Convex Optimization**

| Tính chất | Linear Programming | Convex Optimization |
|-----------|-------------------|---------------------|
| **Dual của Dual = Primal** | Luôn đúng | Cần điều kiện |
| **Strong Duality** | Luôn đúng (nếu khả thi) | Cần Slater's condition |
| **Cấu trúc** | Đối xứng hoàn hảo | Đối xứng có điều kiện |
| **Constraint Qualification** | Tự động thỏa mãn | Cần kiểm tra |

---

## **Tại Sao LP Đặc Biệt?**

LP có những tính chất đặc biệt làm cho "dual của dual = primal" luôn đúng:

### **1. Luôn Convex**

- Hàm mục tiêu tuyến tính → convex
- Miền ràng buộc là polyhedron → convex

### **2. Strong Duality Tự Động**

- Không cần điều kiện Slater
- Chỉ cần một trong hai bài toán khả thi
- Duality gap = 0 (nếu optimal tồn tại)

### **3. Cấu Trúc Đối Xứng Hoàn Hảo**

- Ma trận: $(A^T)^T = A$
- Chuyển vị hai lần trả về ban đầu
- Hoán đổi $(b, c)$ hai lần trở về $(b, c)$

### **4. Constraint Qualification**

- Slater's condition tự động thỏa mãn với LP
- Không cần kiểm tra điều kiện strictly feasible

---

## **Ví Dụ Minh Họa**

### **Ví dụ 1: Quadratic Programming - Convex Case**

**Bài toán Primal:**
$$
\begin{align}
\text{minimize} \quad & \frac{1}{2}x^T Q x + c^T x \\
\text{subject to} \quad & Ax \leq b
\end{align}
$$

với $Q \succ 0$ (positive definite).

**Tính chất:**
- Hàm mục tiêu strictly convex
- Constraint affine
- Nếu khả thi → Slater's condition thỏa mãn
- **Dual của dual = Primal** ✓

### **Ví dụ 2: Non-Convex Case**

**Bài toán Primal:**
$$
\text{minimize} \quad x^2 - 2x \quad \text{subject to} \quad x \geq 0
$$

**Vấn đề:**
- Hàm mục tiêu không convex
- Strong duality không đúng
- **Dual của dual ≠ Primal** ✗

**Minh chứng:**

Primal optimal: $x^* = 1$, $p^* = -1$

Dual:
$$
g(\lambda) = \inf_{x \geq 0} (x^2 - 2x - \lambda x) = \inf_{x \geq 0} (x^2 - (2+\lambda)x)
$$

- Nếu $2 + \lambda > 0$: $g(\lambda) = -\infty$ (vô nghiệm)
- Dual problem không bounded

→ Duality gap > 0, dual của dual không trở về primal

### **Ví dụ 3: Convex Không Thỏa Slater**

**Bài toán:**
$$
\text{minimize} \quad x^2 \quad \text{subject to} \quad x^2 \leq 0
$$

**Phân tích:**
- Hàm mục tiêu convex ✓
- Miền khả thi chỉ có một điểm: $x = 0$
- Không tồn tại strictly feasible point
- **Slater's condition không thỏa mãn** ✗

**Kết quả:**
- Primal: $p^* = 0$
- Dual: $d^* = 0$ 
- Strong duality vẫn đúng (may mắn)
- Nhưng cấu trúc không đối xứng hoàn hảo

---

## **Ứng Dụng và Ý Nghĩa**

### **1. Phân Tích Duality Gap**

Khi dual của dual không trở về primal:
- Duality gap > 0
- Cần kiểm tra điều kiện convexity
- Xem xét relaxation methods

### **2. Thiết Kế Thuật Toán**

- **LP**: Có thể chọn giải primal hoặc dual tuỳ ý
- **Convex**: Cần kiểm tra điều kiện trước khi chọn
- **Non-convex**: Dual chỉ cho lower bound

### **3. Lý Thuyết Tối Ưu**

Tính chất này giúp:
- Hiểu sâu về cấu trúc bài toán
- Phát triển điều kiện tối ưu (KKT)
- Thiết kế primal-dual algorithms

---

## **Bài Tập Thực Hành**

### **Bài Tập 1: Kiểm Tra Slater's Condition**

Cho các bài toán sau, kiểm tra Slater's condition và xác định dual của dual có bằng primal không:

a) $\min x^2 + y^2$ s.t. $x + y \geq 2$

b) $\min e^x$ s.t. $x \geq 0$

c) $\min -\log x$ s.t. $x \leq 1$, $x > 0$

### **Bài Tập 2: So Sánh LP và QP**

Cho hai bài toán:

**LP:** $\min c^T x$ s.t. $Ax \leq b$

**QP:** $\min \frac{1}{2}x^T Q x$ s.t. $Ax \leq b$ với $Q \succ 0$

a) Xây dựng dual của mỗi bài toán

b) Kiểm tra tính chất "dual của dual = primal"

c) So sánh điều kiện cần thiết

### **Bài Tập 3: Non-Convex Example**

Xét bài toán:
$$
\min_{x \in \mathbb{R}} x^3 \quad \text{s.t.} \quad x \geq 1
$$

a) Giải bài toán primal

b) Xây dựng bài toán dual

c) Chứng minh dual của dual không trở về primal

---

## **Tóm Tắt**

### **Kết Luận Chính**

1. **LP**: Dual của dual = Primal (luôn đúng)

2. **Convex Optimization**: Dual của dual = Primal (cần điều kiện)
   - Cần: Convexity + Strong duality + Constraint qualification

3. **Non-Convex**: Dual của dual ≠ Primal (thường không đúng)

### **Điều Kiện Quan Trọng**

| Điều kiện | LP | Convex | Non-Convex |
|-----------|-------|---------|------------|
| Convexity | ✓ (tự động) | ✓ (cần check) | ✗ |
| Strong Duality | ✓ (nếu khả thi) | ✓ (cần Slater) | ✗ (thường) |
| Dual = Dual = Primal | ✓ | ✓ (có điều kiện) | ✗ |

### **Ứng Dụng**

- Thiết kế thuật toán primal-dual
- Phân tích sensitivity
- Kiểm tra optimality
- Relaxation methods

---

## **Tài Liệu Tham Khảo**

1. **Boyd, S., & Vandenberghe, L. (2004).** *Convex Optimization.* Cambridge University Press.
   - Chapter 5: Duality (Section 5.4 về dual của dual)

2. **Rockafellar, R. T. (1970).** *Convex Analysis.* Princeton University Press.
   - Chapter 31: Duality correspondences

3. **Bertsekas, D. P. (1999).** *Nonlinear Programming* (2nd ed.). Athena Scientific.
   - Chapter 6: Duality and convex analysis

4. **Nesterov, Y. (2018).** *Lectures on Convex Optimization.* Springer.
   - Chapter 3: Duality Theory (Section 3.4)

---

**Kết nối với các chương khác:**
- **Chương 10**: Dual của dual trong LP (trường hợp đặc biệt)
- **Chương 12**: KKT conditions (ứng dụng của duality)
- **Chương 16**: Interior-Point Methods (algorithms dựa trên duality)

