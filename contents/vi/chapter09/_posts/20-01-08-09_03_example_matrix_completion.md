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

Năm 2006, Netflix treo giải thưởng 1 triệu đô la cho bất kỳ đội ngũ nào cải thiện hệ thống gợi ý phim thêm 10%. Bài toán cốt lõi nghe rất giản dị: bạn có một bảng khổng lồ gồm hàng trăm nghìn người dùng và hàng chục nghìn bộ phim, nhưng hơn 98% số ô trong bảng bị bỏ trống vì mỗi người chỉ chấm điểm vài chục phim. Làm thế nào để điền chính xác những ô trống còn lại?

Nếu ma trận điểm số hoàn toàn ngẫu nhiên thì bài toán vô nghiệm. Chìa khóa cứu rỗi là giả thiết **hạng thấp (low-rank)**: thị hiếu của hàng trăm nghìn người thực chất chỉ bị chi phối bởi vài chục "nhân tố ẩn" (thể loại, đạo diễn, độ hài hước...). Nhưng cực tiểu hóa $$\operatorname{rank}(X)$$ lại là bài toán NP-khó! Giống như cách chuẩn $$\ell_1$$ thay thế cho chuẩn $$\ell_0$$ (số phần tử khác 0) ở vector, **chuẩn vết / chuẩn hạt nhân** $$\|X\|_* = \sum_i \sigma_i(X)$$ (tổng các giá trị kỳ dị) là bao lồi chặt nhất của $$\operatorname{rank}(X)$$. Và khi đưa vào phương pháp gradient gần kề, toán tử prox của chuẩn hạt nhân hóa ra có một vẻ đẹp đối xứng đến ngỡ ngàng: **co ngưỡng mềm trực tiếp lên các giá trị kỳ dị của SVD!**

## Kiến thức cần nhớ: Bốn trụ cột của bài toán hoàn thiện ma trận

- **Phân rã giá trị kỳ dị (SVD) và hạng ma trận:** Mọi ma trận $$X \in \mathbb{R}^{m \times n}$$ đều viết được dưới dạng $$X = U \Sigma V^T$$ với các giá trị kỳ dị $$\sigma_1 \ge \sigma_2 \ge \dots \ge \sigma_r > 0$$. Hạng của $$X$$ chính là số lượng giá trị kỳ dị khác $$0$$ — tức là chuẩn $$\ell_0$$ của vector $$\sigma(X)$$.
- **Chuẩn vết / Chuẩn hạt nhân (Trace / Nuclear Norm):** Thay $$\|\sigma(X)\|_0$$ bằng $$\|\sigma(X)\|_1 = \sum_{i=1}^r \sigma_i(X) = \|X\|_*$$ biến bài toán tìm ma trận hạng thấp thành một bài toán tối ưu lồi không trơn nhưng toàn cục!
- **Toán tử chiếu lên tập quan sát $$P_\Omega(X)$$:** Tập chỉ số $$\Omega$$ ghi lại các ô đã biết điểm. Phần trơn của hàm mục tiêu là $$g(X) = \frac{1}{2}\|P_\Omega(X) - P_\Omega(Y)\|_F^2$$, có gradient cực gọn $$\nabla g(X) = P_\Omega(X - Y)$$ với hằng số Lipschitz $$L = 1$$ (cho phép dùng bước cố định $$t = 1$$!).
- **Định lý co ngưỡng giá trị kỳ dị (Singular Value Thresholding — SVT):** Toán tử gần kề của $$\lambda\|X\|_*$$ là:
  $$\operatorname{prox}_{\lambda \|\cdot\|_*}(Z) = U \cdot \operatorname{diag}\big(\max(\sigma_i - \lambda, 0)\big) \cdot V^T.$$
  Các giá trị kỳ dị nhỏ hơn $$\lambda$$ bị cắt thẳng về $$0$$, hạ thấp trực tiếp hạng của ma trận sau mỗi bước lặp!

### Giải thích: Tính tay 1 bước thuật toán Soft-Impute (Proximal GD) cho ma trận $$2 \times 2$$

Giả sử ta quan sát 3 ô của một ma trận $$2 \times 2$$ và khuyết ô $$(2, 2)$$ (đánh dấu `?`):
$$Y = \begin{pmatrix} 4 & 0 \\ 0 & ? \end{pmatrix}, \quad \Omega = \{(1,1), (1,2), (2,1)\}.$$
Xét bài toán $$\min_X \frac{1}{2}\|P_\Omega(X) - P_\Omega(Y)\|_F^2 + \lambda\|X\|_*$$ với $$\lambda = 1.5$$, bước cố định $$t = 1$$ (vì $$L = 1$$). Khởi tạo $$X^{(0)} = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$$.

1. **Nhịp 1 — Bước gradient trên phần quan sát $$\Omega$$:**
   - Hiệu trên các ô quan sát: $$P_\Omega(X^{(0)} - Y) = \begin{pmatrix} 2 - 4 & 0 - 0 \\ 0 - 0 & 0 \end{pmatrix} = \begin{pmatrix} -2 & 0 \\ 0 & 0 \end{pmatrix}$$ (ô khuyết $$(2,2)$$ luôn có gradient bằng $$0$$!).
   - Ma trận trung gian $$Z^{(1)} = X^{(0)} - 1 \cdot \nabla g(X^{(0)}) = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix} - \begin{pmatrix} -2 & 0 \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 4 & 0 \\ 0 & 2 \end{pmatrix}$$.
   (Nhận xét trực giác: $$Z^{(1)}$$ giữ nguyên giá trị dự đoán cũ ở ô khuyết, và kéo các ô quan sát về đúng dữ liệu $$Y$$!)
2. **Nhịp 2 — Phân rã SVD và co ngưỡng mềm giá trị kỳ dị với $$\lambda = 1.5$$:**
   - Vì $$Z^{(1)}$$ đã là ma trận đường chéo không âm, các giá trị kỳ dị là $$\sigma_1 = 4$$ và $$\sigma_2 = 2$$ ($$U = V = I_2$$).
   - Áp dụng $$\max(\sigma_i - 1.5, 0)$$:
     $$\sigma_1' = \max(4 - 1.5, 0) = 2.5, \quad \sigma_2' = \max(2 - 1.5, 0) = 0.5.$$
   - Kết quả sau bước 1: $$X^{(1)} = \begin{pmatrix} 2.5 & 0 \\ 0 & 0.5 \end{pmatrix}$$.
3. **Điều gì xảy ra nếu ta tăng lực phạt lên $$\lambda = 2.5$$?**
   Khi đó $$\sigma_2' = \max(2 - 2.5, 0) = 0$$, nên $$X^{(1)} = \begin{pmatrix} 1.5 & 0 \\ 0 & 0 \end{pmatrix}$$ có **hạng đúng bằng 1**! Bằng cách lặp lại hai nhịp "điền dữ liệu quan sát $$\to$$ co ngưỡng SVD", thuật toán vừa khớp các ô đã biết vừa ép cấu trúc hạng thấp lên toàn ma trận.

# Ví dụ: hoàn thiện ma trận (Matrix completion)

Trong nhiều bài toán thực tế, dữ liệu đo đạc được biểu diễn dưới dạng ma trận, trong đó phần lớn các phần tử bị thiếu và chỉ một số ít phần tử được quan sát. Bài toán dự đoán các phần tử bị thiếu từ các phần tử đã biết được gọi là **hoàn thiện ma trận (matrix completion)**.

Một ứng dụng quen thuộc là hệ thống gợi ý, nơi ta cần ước lượng mức độ quan tâm của người dùng đối với những sản phẩm hoặc dịch vụ mà họ chưa từng đánh giá.

## Phát biểu bài toán hoàn thiện ma trận
Cho ma trận dữ liệu quan sát $$Y \in \mathbb{R}^{m\times n}$$, với $$\Omega$$ là tập hợp các chỉ số $$(i,j)$$ tại đó giá trị $$Y_{ij}$$ đã được quan sát. Ta cần tìm ma trận ước lượng $$B$$ để điền vào các vị trí bị thiếu thông qua bài toán tối ưu:

> $$\min_B \frac{1}{2} \sum_{(i,j)\in\Omega} (Y_{ij} −B_{ij})^2 + \lambda\lVert B \rVert_{tr}$$

Số hạng thứ nhất đo sai số bình phương giữa $$B$$ và dữ liệu quan sát được trên $$\Omega$$, còn số hạng thứ hai khuyến khích ma trận $$B$$ có hạng thấp (dựa trên giả định rằng ma trận dữ liệu nằm gần một không gian chiều thấp). Nhờ đó, $$B$$ khôi phục các phần tử còn thiếu theo cấu trúc hạng thấp phù hợp với các quan sát hiện có.

### [Tham khảo] Chuẩn vết (Trace Norm)
Chuẩn vết (hay chuẩn hạt nhân — nuclear norm) của một ma trận được định nghĩa là tổng các giá trị kỳ dị của nó:

> $$\lVert B \rVert_{tr} = \text{trace}(\sqrt{B^* B}) = \sum_{i=1}^r \sigma_i(B), \quad r = rank(B)$$

trong đó $$B^* B$$ là ma trận nửa xác định dương và các giá trị kỳ dị được sắp theo thứ tự giảm dần $$\sigma_1(B) \ge ... \ge \sigma_r(B) \ge 0$$.

### [Tham khảo] Chính quy hóa chuẩn $$\ell_1$$ và chuẩn vết
Bài toán trên có thể xem như phiên bản ma trận của bài toán ngưỡng mềm vector: chuẩn $$\ell_1$$ cho vector ($$\lVert \cdot \rVert_{1}$$) được thay bằng chuẩn vết cho ma trận ($$\lVert \cdot \rVert_{tr}$$), với vai trò hoàn toàn tương tự.

Trong khi chuẩn $$\ell_1$$ thúc đẩy tính thưa của các phần tử trong vector, chuẩn vết thúc đẩy tính thưa trên vector các giá trị kỳ dị của ma trận. Với ma trận đường chéo, các phần tử đường chéo chính là các giá trị kỳ dị, nên cực tiểu hóa chuẩn vết tương đương với cực tiểu hóa chuẩn $$\ell_1$$ của vector đường chéo. Theo nghĩa đó, chuẩn vết $$\lVert B \rVert_{tr}$$ đóng vai trò là xấp xỉ lồi cho $$\text{Rank}(B)$$.

## Áp dụng phương pháp gradient gần kề
Để đưa bài toán về dạng tổng hợp chuẩn của phương pháp gradient gần kề, ta định nghĩa toán tử chiếu lên tập chỉ số quan sát.

### Toán tử chiếu
Định nghĩa toán tử chiếu $$P_\Omega$$ như sau:

> $$[ P_\Omega(B) ] _{ij} =
> \begin{cases}
B_{ij}, & (i,j) ∈ \Omega \\\
0, & (i,j) \notin \Omega
> \end{cases}$$

### Hàm mục tiêu
Sử dụng toán tử chiếu, hàm mục tiêu được viết gọn thành:

>$$f(B) = \underbrace{ \frac{1}{2} \lVert P_\Omega(Y) − P_\Omega(B) \rVert_F^2 }_{g(B)} + \underbrace{ \lambda \lVert B \rVert_{tr} }_{h(B)}$$

Khi đó, $$f(B)$$ được tách thành phần khả vi $$g(B)$$ và phần không khả vi $$h(B)$$.

### Ánh xạ gần kề
Để áp dụng phương pháp gradient gần kề, ta cần gradient của $$g(B)$$ và ánh xạ gần kề của $$h(B)$$:

* Gradient của $$g(B)$$: $$\nabla g(B) = −(P_\Omega(Y )−P_\Omega(B))$$.
* Ánh xạ gần kề:

> $$ \begin{align}
\text{prox}_t (B) = \underset{Z}{\text{argmin}} \frac{1}{2t} \Vert B−Z \Vert_F^2 + \lambda \Vert Z \Vert_{tr}
\end{align} $$

### Phân tích SVD và toán tử ngưỡng mềm ma trận
Ánh xạ gần kề trên chính là toán tử ngưỡng mềm ma trận ở mức $$\lambda t$$: $$\text{prox}_t(B) = S_{\lambda t}(B)$$.

Nếu phân tích giá trị kỳ dị (SVD) của $$B$$ là $$B = U \Sigma V^T$$, thì toán tử ngưỡng mềm ma trận $$S_\lambda(B)$$ được tính bởi:

> $$ S_\lambda(B) = U \Sigma_\lambda V^T$$

trong đó $$\Sigma_\lambda$$ là ma trận đường chéo với các phần tử:

> $$(\Sigma_\lambda)_{ii} = \max \{ \Sigma_{ii} −\lambda,0 \}$$

### [Tham khảo] Cách suy ra công thức $$(\Sigma_\lambda)_{ii} = \max \{ \Sigma_{ii} −\lambda,0 \}$$
Đặt $$Z = \text{prox}_t(B)$$. Từ điều kiện tối ưu bậc một theo biến $$Z$$ của bài toán định nghĩa $$\text{prox}_t(B)$$, ta có:

> $$0 ∈ Z − B + \lambda t \cdot \partial \lVert Z \rVert_{tr}$$

Biến đổi biểu thức trên với $$t = 1$$ (tương ứng hằng số Lipschitz $$L = 1$$) và chọn thành phần $$W = 0$$ cho các giá trị kỳ dị dương:

>$$\begin{align}
Z & = B - \lambda t \cdot \partial \lVert Z \rVert_{tr} \\
 & = U \Sigma V^T - \lambda t \cdot (UV^T + W) \\
 & = U (\Sigma - \lambda t) V^T - \lambda t  W \\
 & = U (\Sigma - \lambda ) V^T  \\
\end{align}$$

Do đó $$\text{prox}_1(B) = S_\lambda(B) = Z$$, với các giá trị kỳ dị được co ngưỡng mềm theo công thức:

> $$(\Sigma_\lambda)_{ii} = \max \{ \Sigma_{ii} −\lambda,0 \}$$

### [Tham khảo] Vi phân dưới của chuẩn vết
Với phân tích SVD rút gọn $$Z = U \Sigma V^T$$, vi phân dưới của chuẩn vết được cho bởi:
> $$\partial \lVert Z \rVert_{tr} = \{UV^T + W : \lVert W \rVert_{op} ≤ 1, U^TW = 0, WV = 0 \}$$

trong đó $$\lVert W \rVert_{op}$$ là chuẩn toán tử (giá trị kỳ dị lớn nhất của $$W$$) không vượt quá 1, và không gian cột/hàng của $$W$$ trực giao với $$U$$ và $$V$$.

* Tham khảo chứng minh chi tiết tại: [Derivative of the nuclear norm with respect to its argument](https://math.stackexchange.com/questions/701062/derivative-of-the-nuclear-norm-with-respect-to-its-argument)

### Bước cập nhật gradient gần kề
Công thức cập nhật gradient gần kề cho bài toán hoàn thiện ma trận là:

> $$B^+ = S_{\lambda t} ( B + t( P_\Omega(Y) − P_\Omega(B) ) )$$

Vì $$\nabla g(B)$$ liên tục Lipschitz với hằng số $$L = 1$$, ta có thể chọn kích thước bước cố định $$t = 1$$. Khi đó, công thức cập nhật rút gọn thành:

> $$B^+ = S_\lambda (P_\Omega(Y) + P_\Omega^\bot (B) )$$

trong đó $$P_\Omega^\bot$$ là phép chiếu lên tập các vị trí không quan sát được, thỏa mãn $$P_\Omega(B) + P_\Omega^\bot (B) = B$$.

Trong biểu thức này, $$P_\Omega(Y)$$ giữ nguyên các giá trị đã quan sát, còn $$P_\Omega^\bot (B)$$ lấy các giá trị ước lượng hiện tại ở các vị trí bị thiếu. Sau đó, phép tính $$S_\lambda$$ chỉ cần thực hiện phân tích SVD và áp dụng co ngưỡng $$(\Sigma_\lambda)_{ii} = \max \{ \Sigma_{ii} −\lambda,0 \}$$.

## Thuật toán Soft-Impute
Thuật toán thu được có tên gọi là **Soft-Impute**, mang lại cách giải đơn giản và hiệu quả cho bài toán hoàn thiện ma trận. Dù chi phí SVD trên ma trận cỡ lớn có thể cao, nhưng nhờ cấu trúc đặc biệt gồm một ma trận thưa $$P_\Omega(Y)$$ cộng với một ma trận hạng thấp $$P_\Omega^\bot (B)$$, phép phân tích SVD trong Soft-Impute có thể được thực hiện rất hiệu quả.

* Tham khảo thêm: Mazumder et al. (2011), "Spectral regularization algorithms for learning large incomplete matrices".
