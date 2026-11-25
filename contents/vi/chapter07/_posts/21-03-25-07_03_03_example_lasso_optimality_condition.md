---
layout: post
title: '07-03-03 Ví dụ: Điều kiện tối ưu Lasso'
chapter: '07'
order: 9
owner: Kyeongmin Woo
categories:
- chapter07
lang: vi
---

Năm 1996, Robert Tibshirani giới thiệu **Lasso** ($$\min_\beta \frac{1}{2}\|y - X\beta\|_2^2 + \lambda\|\beta\|_1$$) và làm thay đổi mãi mãi thống kê hiện đại: chỉ bằng việc thay phạt bình phương $$\|\beta\|_2^2$$ thành chuẩn $$\ell_1$$ $$\|\beta\|_1$$, mô hình bỗng tự động phát hiện và giữ lại vài chục biến quan trọng nhất trong hàng chục nghìn biến nhiễu!

Nhưng chính xác **cơ chế toán học nào** khiến Lasso đặt hàng loạt hệ số $$\beta_j^\star$$ về đúng số $$0$$? Câu trả lời không thể đến từ đạo hàm cổ điển (vì $$|\beta_j|$$ không khả vi tại $$0$$), mà đến trực tiếp từ điều kiện tối ưu subgradient $$0 \in -X^T(y - X\beta^\star) + \lambda \partial\|\beta^\star\|_1$$!

## Bản đồ kiến thức nền: Đọc hiểu Điều kiện KKT/Subgradient của Lasso

Ba trụ cột sau giải mã trọn vẹn phương trình tối ưu của Lasso:

- **Tách điều kiện tối ưu theo từng đặc trưng $$j = 1, \dots, p$$:** Ký hiệu $$X_j$$ là cột thứ $$j$$ của ma trận dữ liệu và $$r^\star = y - X\beta^\star$$ là vector phần dư tối ưu. Điều kiện $$0 \in \partial f(\beta^\star)$$ viết ra từng tọa độ trở thành:
  $$X_j^T (y - X\beta^\star) = \lambda s_j, \qquad s_j \in \begin{cases} \{\operatorname{sign}(\beta_j^\star)\} & \text{nếu } \beta_j^\star \neq 0 \\ [-1, 1] & \text{nếu } \beta_j^\star = 0 \end{cases}$$
- **Ý nghĩa thống kê tuyệt đẹp — Tương quan với phần dư:**
  - Mọi biến được chọn ($$\beta_j^\star \neq 0$$) đều có tích vô hướng với phần dư đạt **đúng ngưỡng tới hạn** $$|X_j^T r^\star| = \lambda$$ (cùng dấu với $$\beta_j^\star$$)!
  - Mọi biến bị loại về $$0$$ ($$\beta_j^\star = 0$$) đều có tương quan với phần dư bị chặn dưới ngưỡng: $$|X_j^T r^\star| \le \lambda$$!
- **Ngưỡng $$\lambda_{\max}$$ ép toàn bộ mô hình về $$0$$:** Khi $$\beta^\star = 0$$, phần dư là $$r^\star = y$$. Do đó $$\beta^\star = 0$$ là nghiệm tối ưu toàn cục khi và chỉ khi $$\lambda \ge \|X^T y\|_\infty = \max_j |X_j^T y|$$!

### Khung giải thích (nên đọc chậm): Kiểm chứng trực tiếp nghiệm Lasso bằng điều kiện subgradient

Cho $$X = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$ (2 đặc trưng trực giao), $$y = \begin{pmatrix} 3 \\ 0.6 \end{pmatrix}$$ và $$\lambda = 1$$. Ta kiểm chứng nghiệm đề xuất $$\beta^\star = (2,\; 0)^T$$:

1. **Bước 1 — Tính vector phần dư $$r^\star = y - X\beta^\star$$:**
   $$r^\star = \begin{pmatrix} 3 \\ 0.6 \end{pmatrix} - \begin{pmatrix} 2 \\ 0 \end{pmatrix} = \begin{pmatrix} 1 \\ 0.6 \end{pmatrix}.$$
2. **Bước 2 — Tính $$X^T r^\star$$ cho từng tọa độ:**
   - Tọa độ 1 (có $$\beta_1^\star = 2 > 0$$): $$X_1^T r^\star = 1$$. So sánh với $$\lambda \operatorname{sign}(\beta_1^\star) = 1 \cdot (+1) = 1$$. **Khớp chính xác!**
   - Tọa độ 2 (có $$\beta_2^\star = 0$$): $$X_2^T r^\star = 0.6$$. Kiểm tra điều kiện $$|X_2^T r^\star| \le \lambda$$: $$|0.6| \le 1$$ (tương ứng $$s_2 = 0.6 \in [-1, 1]$$). **Khớp chính xác!**
3. **Bước 3 — Tìm ngưỡng $$\lambda_{\max}$$ để cả hai biến đều bằng 0:**
   $$\lambda_{\max} = \max(|X_1^T y|,\; |X_2^T y|) = \max(3,\; 0.6) = 3.$$
   Thật vậy, hễ $$\lambda \ge 3$$, cả $$|3| \le \lambda$$ lẫn $$|0.6| \le \lambda$$ đều thỏa, nên $$\beta^\star = (0, 0)^T$$ ngay lập tức!

---

Xét bài toán Lasso sau:
>
\begin{equation}
\min_{\beta} \frac{1}{2}  \| y-X\beta \|_2^2 + \lambda \| \beta \|_1
\end{equation}

trong đó $$y \in \mathbb{R}^n$$, $$X \in \mathbb{R}^{n \times p}$$ và $$\lambda \geq 0$$.

Điều kiện tối ưu theo gradient dưới của bài toán này được viết như sau:
>
$$
\eqalign{
0 \in \partial\left(\frac{1}{2} \| y-X\beta \|_2^2 + \lambda \| \beta \|_1\right)
&\quad \Longleftrightarrow \quad 0 \in - X^T (y-X\beta) + \lambda \partial  \| \beta \|_1 \\
&\quad \Longleftrightarrow \quad X^T (y-X\beta)  = \lambda v \\
& \quad \text{với } v \in \partial  \| \beta \|_1 \text{ nào đó}
}\\
$$

Với $$\beta=(\beta_1,\beta_2,\dots,\beta_p )$$, các thành phần của gradient dưới $$v=(v_1,v_2,\dots,v_p)$$ thỏa mãn:

$$
v_i = 
\begin{cases}
 1   &\text{nếu } \beta_i > 0 \\
-1   &\text{nếu } \beta_i < 0 \\
[-1,1]   &\text{nếu } \beta_i = 0
\end{cases}
, i \in \{1,2,\dots,p \}
$$

Bất kỳ $$\beta$$ nào thỏa mãn phương trình sau đều là nghiệm tối ưu:
>
\begin{equation}
X^T(y-X\beta) = \lambda v 
\end{equation}

Viết theo từng tọa độ, $$\beta$$ là nghiệm tối ưu khi và chỉ khi:
>
$$
\begin{cases}
X_i^T(y-X\beta) = \lambda \cdot \text{sign}(\beta_i) &\text{nếu } \beta_i \neq 0 \\
 |X_i^T(y-X\beta)|  \leq \lambda &\text{nếu } \beta_i = 0 
\end{cases}$$

trong đó $$X_i$$ ($$i \in \{1,2,\dots, p \}$$) ký hiệu cột thứ $$i$$ của ma trận $$X$$.
