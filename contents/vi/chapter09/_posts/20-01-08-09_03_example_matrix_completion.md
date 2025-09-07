---
layout: post
title: '09-03 Ví dụ: hoàn thiện ma trận'
chapter: '09'
order: 4
owner: Kyeongmin Woo
categories:
- chapter09
lang: vi
---

# Ví dụ: hoàn thiện ma trận (Matrix completion)

Trong nhiều ứng dụng, dữ liệu đo được thường được biểu diễn dưới dạng ma trận. Trong những trường hợp này, hầu hết các phần tử trong ma trận có thể trống, chỉ có một vài phần tử chứa dữ liệu quan sát được, dẫn đến một ma trận thưa. Thách thức điền vào các phần tử bị thiếu trong ma trận như vậy được gọi là bài toán **hoàn thiện ma trận**.

Ví dụ, vấn đề này có thể xảy ra trong các hệ thống gợi ý khi đề xuất sản phẩm hoặc dịch vụ cho khách hàng chưa từng mua hàng.

## Bài toán hoàn thiện ma trận
Bài toán **hoàn thiện ma trận** có thể được phát biểu như sau:

Gọi ma trận $$Y \in \mathbb{R}^{m\times n}$$ biểu diễn dữ liệu quan sát được, và $$Y_{ij}, (i,j) \in \Omega$$ ký hiệu các phần tử chứa dữ liệu quan sát được. Ma trận $$B$$ là ma trận ước lượng được sử dụng để dự đoán các phần tử bị thiếu.

> $$\min_B \frac{1}{2} \sum_{(i,j)\in\Omega} (Y_{ij} −B_{ij})^2 + \lambda\lVert B \rVert_{tr}$$

Số hạng đầu tiên trong hàm mục tiêu nhằm tối thiểu hóa lỗi giữa ma trận $$B$$ và dữ liệu quan sát được, trong khi số hạng thứ hai khuyến khích ma trận $$B$$ có hạng thấp. (Giả định rằng ma trận B nằm trên một đa tạp chiều thấp.) Do đó, ma trận $$B$$ điền vào các phần tử bị thiếu với các giá trị chiều thấp nhất phù hợp với dữ liệu quan sát được.

### [Tham khảo] Chuẩn vết (Trace Norm)
Chuẩn vết của một ma trận được định nghĩa là tổng các giá trị kỳ dị của nó.

> $$\lVert B \rVert_{tr} = \text{trace}(\sqrt{B^* B}) = \sum_{i=1}^r \sigma_i(B), \quad r = rank(B)$$

Ở đây, $$B^* B$$ là nửa xác định dương, và các giá trị kỳ dị được sắp xếp theo thứ tự $$\sigma_1(X) \ge ... \ge \sigma_r(X) \ge 0$$.

### [Tham khảo] Bộ chính quy hóa chuẩn **L1** so với Bộ chính quy hóa chuẩn vết
Bài toán này có thể được hiểu như ngưỡng mềm ma trận, trong đó vector trong ngưỡng mềm ban đầu được thay thế bằng ma trận. Trong số hạng chính quy hóa, bộ chính quy hóa chuẩn **L1** cho vector ($$\lVert \cdot \rVert_{1}$$) được thay thế bằng bộ chính quy hóa chuẩn vết ($$\lVert \cdot \rVert_{tr}$$) cho ma trận, và thực sự, chức năng của hai bộ chính quy hóa này là tương tự.

Bộ chính quy hóa chuẩn **L1** tạo ra tính thưa trong vector, trong khi bộ chính quy hóa chuẩn vết tương tự tạo ra tính thưa trong vector giá trị kỳ dị của ma trận. Khi ma trận là đường chéo, các phần tử đường chéo có thể được xem như vector giá trị kỳ dị, và bộ chính quy hóa chuẩn vết tối thiểu hóa tổng các giá trị kỳ dị, thúc đẩy tính thưa trong vector giá trị kỳ dị.

Trong bối cảnh này, chuẩn vết $$\lVert B \rVert_{tr}$$ đóng vai trò như một xấp xỉ cho $$\text{Rank}(B)$$.

## Phương pháp gradient gần kề
Khi bài toán này được đóng khung bằng toán tử chiếu, phương pháp gradient gần kề có thể được sử dụng hiệu quả.
### Toán tử chiếu
Hãy định nghĩa toán tử chiếu $$P_\Omega$$ cho các giá trị quan sát được như sau:

> $$[ P_\Omega(B) ] _{ij} =
> \begin{cases}
B_{ij}, & (i,j) ∈ \Omega \\\
0, & (i,j) \notin \Omega
> \end{cases}$$

### Hàm mục tiêu
Sử dụng toán tử chiếu, hàm mục tiêu được định nghĩa là:

>$$f(B) = \underbrace{ \frac{1}{2} \lVert P_\Omega(Y) − P_\Omega(B) \rVert_F^2 }_{g(B)} + \underbrace{ \lambda \lVert B \rVert_{tr} }_{h(B)}$$

Bây giờ, hàm $$f(B)$$ bao gồm một phần khả vi $$g(B)$$ và một phần không khả vi $$h(B)$$.

### Ánh xạ gần kề
Để áp dụng phương pháp gradient gần kề, chúng ta cần tính gradient của hàm $$g(B)$$ và định nghĩa ánh xạ gần kề.

* Gradient của $$g(B)$$: $$\nabla g(B) = −(P_\Omega(Y )−P_\Omega(B))$$
* Ánh xạ gần kề: 

> $$ \begin{align}
\text{prox}_t (B) = \underset{Z}{\text{argmin}} \frac{1}{2t} \Vert B−Z \Vert_F^2 + \lambda \Vert Z \Vert_{tr}
\end{align} $$

### SVD ma trận & Ngưỡng mềm
Ánh xạ gần kề tương ứng với ngưỡng mềm ma trận ở mức $$\lambda$$: $$\text{prox}_t(B) = S_{\lambda t}(B)$$.

Thông thường, ma trận $$B$$ có kích thước lớn, vì vậy Phân tích Giá trị Kỳ dị (SVD) được sử dụng để tối thiểu hóa tải tính toán. Nếu chúng ta thực hiện SVD sao cho $$B = U \Sigma V^T$$, thì $$S_\lambda(B)$$ có thể được định nghĩa là:

> $$ S_\lambda(B) = U \Sigma_\lambda V^T$$

Ở đây, $$\Sigma_\lambda$$ là một ma trận đường chéo được định nghĩa như sau:

> $$(\Sigma_\lambda)_{ii} = \max \{ \Sigma_{ii} −\lambda,0 \}$$
 

### [Reference] $$(\Sigma_\lambda)_{ii} = \max \{ \Sigma_{ii} −\lambda,0 \}$$  inducement
How is this expression derived? Assuming $$\text{prox}_t(B) = Z$$, we have:
(Differentiating the right-hand side of $$\text{prox}_t(B)$$ with respect to Z yields the following result.)

> $$0 ∈ Z − B + \lambda t \cdot \partial \lVert Z \rVert_{tr}$$

Rearranging this expression gives:

>$$\begin{align}
Z & = B - \lambda t \cdot \partial \lVert Z \rVert_{tr} \\
 & = U \Sigma V^T - \lambda t \cdot (UV^T + W) \\
 & = U (\Sigma - \lambda t) V^T - \lambda t  W \\
 & = U (\Sigma - \lambda ) V^T  \\
\end{align}$$

The final expression can be obtained when the Lipschitz constant is $$L=1$$ and $$W$$ is 0.

Thus, we have $$\text{prox}_t(B) = S_\lambda(B) = Z$$, leading to the derivation of the following expression:

> $$(\Sigma_\lambda)_{ii} = \max \{ \Sigma_{ii} −\lambda,0 \}$$

### [Reference] Derivative of Trace Norm
If $$Z = U \Sigma V^T$$, the derivative of the trace norm is given by: 
> $$\partial \lVert Z \rVert_{tr} = \{UV^T + W : \lVert W \rVert_{op} ≤ 1, U^TW = 0, WV = 0 \}$$

Here, $$\lVert W \rVert_{op}$$ represents the operator norm, with the largest singular value being less than 1. Additionally, $$W$$ is orthogonal to both $$U^T$$ and $$V$$.

* For proof, refer to [Derivative of the nuclear norm with respect to its argument](https://math.stackexchange.com/questions/701062/derivative-of-the-nuclear-norm-with-respect-to-its-argument)

### Proximal gradient update
Now, let's define the proximal gradient update equation.

> $$B^+ = S_{\lambda t} ( B + t( P_\Omega(Y) − P_\Omega(B) ) )$$

When $$L = 1$$, $$\nabla g(B)$$ is Lipschitz continuous, allowing us to choose a fixed step size of $$t = 1$$.

Consequently, the update equation simplifies to:

> $$B^+ = S_\lambda (P_\Omega(Y) + P_\Omega^\bot (B) )$$

Ở đây, $$P_\Omega^\bot$$ biểu diễn phép chiếu lên các giá trị không quan sát được, thỏa mãn phương trình $$P_\Omega(B) + P_\Omega^\bot (B) = B$$.

Trong phương trình này, $$P_\Omega(Y)$$ biểu thị phần quan sát được, trong khi $$P_\Omega^\bot (B)$$ biểu thị phần bị thiếu. Hàm $$S_\lambda$$ rất đơn giản để tính toán, vì nó chỉ yêu cầu thực hiện SVD và tính toán $$(\Sigma_\lambda)_{ii} = \max \{ \Sigma_{ii} −\lambda,0 \}$$.

## Thuật toán Soft-Impute
Thuật toán này được biết đến với tên **Soft-Impute** và cung cấp một giải pháp đơn giản nhưng hiệu quả cho bài toán hoàn thiện ma trận. Khi xử lý các ma trận lớn, chi phí tính toán của SVD có thể cao. Tuy nhiên, do tính thưa của $$P_\Omega(Y)$$ và hạng thấp của $$P_\Omega^\bot (B)$$ trong thuật toán này, SVD có thể được thực hiện một cách hiệu quả.

* Để biết thêm thông tin chi tiết, vui lòng tham khảo bài báo: Mazumder et al. (2011), "Spectral regularization algorithms for learning
large incomplete matrices"

