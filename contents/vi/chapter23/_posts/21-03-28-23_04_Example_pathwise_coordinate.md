---
layout: post
title: '23-04 Ví dụ: Pathwise coordinate descent cho lasso'
chapter: '23'
order: 5
owner: YoungJae Choung
categories:
- chapter23
lang: vi
---

Trong thực hành khoa học dữ liệu, hiếm khi nào ta biết trước giá trị $$\lambda$$ tối ưu cho hồi quy Lasso; thông thường ta phải thử cả một lưới $$50$$ đến $$100$$ giá trị $$\lambda$$ để chọn bằng kiểm định chéo (cross-validation). Nếu giải độc lập 100 bài toán từ con số 0, thời gian tính toán sẽ nhân lên 100 lần.

Friedman, Hastie, Hoefling và Tibshirani (2007, 2009) đã nghĩ ra một chiến lược vừa thông minh vừa đẹp mắt gọi là **hạ theo tọa độ dọc đường chính quy hóa (Pathwise Coordinate Descent)** — trái tim của thư viện `glmnet` lừng danh. Thay vì giải lẻ tẻ, họ bắt đầu từ mức phạt lớn nhất $$\lambda_{\max}$$ nơi nghiệm bằng $$0$$ hoàn toàn, rồi giảm dần $$\lambda$$ từng nấc nhỏ, dùng nghiệm trước làm điểm khởi tạo nóng (*warm start*) và chỉ chạy vòng lặp trên tập các biến thực sự hoạt động (*active set*).

## Bản đồ kiến thức nền: Ba trụ cột của chiến lược Pathwise + Active Set

Để hiểu vì sao giải **cả 100 giá trị $$\lambda$$** theo đường chính quy hóa lại có thể nhanh hơn giải **một giá trị $$\lambda$$ nhỏ duy nhất** từ điểm khởi tạo 0, hãy nắm ba trụ cột sau:

- **Ngưỡng triệt tiêu $$\lambda_{\max}$$ từ điều kiện KKT:** Từ điều kiện tối ưu $$X_j^T(y - X\beta) = \lambda v_j$$ với $$|v_j| \le 1$$, nghiệm $$\beta = 0$$ là tối ưu khi và chỉ khi $$\lambda \ge \max_{1 \le j \le p} |X_j^T y|$$. Đây là điểm neo khởi đầu hoàn hảo cho toàn bộ đường nghiệm, không cần đoán mò.
- **Khởi động nóng (Warm Starts) trên lưới logarit:** Đường nghiệm $$\beta^\star(\lambda)$$ là một hàm liên tục (thực tế là tuyến tính từng khúc) theo $$\lambda$$. Khi giảm từ $$\lambda_k$$ sang $$\lambda_{k+1}$$ đủ gần nhau, $$\beta^\star(\lambda_k)$$ đã nằm rất sát $$\beta^\star(\lambda_{k+1})$$, giúp vòng lặp hội tụ chỉ sau vài lượt quét.
- **Tập hoạt động (Active Set) và Kiểm tra KKT:** Ở vùng $$\lambda$$ lớn đến trung bình, hầu hết tọa độ đều bằng $$0$$. Thuật toán chỉ lặp đi lặp lại trên tập nhỏ các tọa độ khác $$0$$ cho đến khi hội tụ, sau đó mới quét 1 lượt duy nhất qua các tọa độ ngoài tập hoạt động để kiểm tra điều kiện KKT $$|X_j^T(y - X\beta)| \le \lambda$$. Nếu không tọa độ nào vi phạm, ta chắc chắn 100% đã tìm đúng nghiệm toàn cục!

### Khung giải thích (nên đọc chậm): Tính tay 2 nấc của Pathwise Coordinate Descent + kiểm tra KKT

Xét bài toán Lasso 2 đặc trưng với ma trận thiết kế và nhãn:

$$
X = \begin{pmatrix} 1 & 0 \\ 1 & 1 \\ 0 & 1 \end{pmatrix}, \qquad y = \begin{pmatrix} 4 \\ 2 \\ 0 \end{pmatrix}, \qquad \|X_1\|_2^2 = 2,\; \|X_2\|_2^2 = 2.
$$

1. **Bước 0 — Tìm $$\lambda_{\max}$$:**
   Tính tương quan ban đầu với $$y$$:
   $$|X_1^T y| = |1(4) + 1(2) + 0(0)| = 6, \qquad |X_2^T y| = |0(4) + 1(2) + 1(0)| = 2.$$
   Vậy $$\lambda_{\max} = \max(6, 2) = 6$$. Tại $$\lambda_1 = 6$$, nghiệm chính xác là $$\beta^\star(6) = (0, 0)$$ với tập hoạt động $$\mathcal{A} = \emptyset$$.
2. **Bước 1 — Hạ xuống $$\lambda_2 = 4$$ với khởi động nóng từ $$(0, 0)$$:**
   Kiểm tra KKT tại $$(0, 0)$$ với $$\lambda_2 = 4$$: tọa độ 1 có $$|X_1^T y| = 6 > 4$$ (vi phạm KKT!), còn tọa độ 2 có $$|X_2^T y| = 2 \le 4$$ (thỏa mãn).
   Đưa tọa độ 1 vào tập hoạt động: $$\mathcal{A} = \{1\}$$.
3. **Vòng trong — Giải chỉ trên tập hoạt động $$\mathcal{A} = \{1\}$$:**
   Cập nhật riêng $$\beta_1$$:
   $$\beta_1 = S_{\lambda_2 / \|X_1\|_2^2}\!\left(\frac{X_1^T y}{\|X_1\|_2^2}\right) = S_{4/2}\!\left(\frac{6}{2}\right) = S_2(3) = 1.$$
   Điểm ứng viên là $$\hat{\beta} = (1, 0)$$.
4. **Kiểm tra KKT cho tọa độ không hoạt động $$j = 2$$:**
   Tính phần dư: $$r = y - X\hat{\beta} = (4, 2, 0)^T - 1 \cdot (1, 1, 0)^T = (3, 1, 0)^T$$.
   Kiểm tra $$|X_2^T r| = |0(3) + 1(1) + 1(0)| = 1 \le 4 = \lambda_2$$ — **thỏa mãn KKT**!
   Thuật toán dừng ngay tại $$\beta^\star(4) = (1, 0)$$ mà không cần cập nhật tọa độ 2 dù chỉ một lần. Trên bài toán $$p = 100{,}000$$ đặc trưng, cơ chế này giúp tiết kiệm hơn $$99\%$$ khối lượng tính toán!

Mục này trình bày tổng quan thuật toán hạ theo tọa độ dọc đường chính quy hóa (pathwise coordinate descent) cho bài toán hồi quy Lasso [[Friedman et al. (2007)](https://arxiv.org/pdf/0708.1485.pdf)] [[Friedman et al. (2009)](https://www.jstatsoft.org/article/view/v033i01/v33i01.pdf)].

>**Bài toán hồi quy Lasso:**
> $$
> \min_{\beta} \frac{1}{2} \| y - X\beta \|_2^2 + \lambda \|\beta\|_1
> $$

Ở [07-03-03 Ví dụ: Điều kiện tối ưu của Lasso]({% multilang_post_url contents/chapter07/21-03-25-07_03_03_example_lasso_optimality_condition %}), ta đã suy ra điều kiện tối ưu bậc nhất cho bài toán này. Nghiệm tối ưu $$\beta$$ thỏa mãn hệ điều kiện sau:

>
> $$
> \begin{align}
> X_1^T(y-X\beta) &= \lambda v_1\\\\
> X_2^T(y-X\beta) &= \lambda v_2\\\\
> \dots\\\\
> X_p^T(y-X\beta) &= \lambda v_p
> \end{align}
> $$

**Lưu ý:** $$X_i$$ ($$i \in \{ 1,2,\dots,p \}$$) là cột thứ $$i$$ của ma trận $$X$$, còn $$v=(v_1,v_2,\dots,v_p)$$ là một dưới đạo hàm (subgradient) của $$\|\beta\|_1$$ tại $$\beta=(\beta_1,\beta_2,\dots,\beta_p)$$:

>
$$
v_i, i \in \{1,2,\dots,p \} = 
\begin{cases}
\{ 1 \}  &\text{if $\beta_i > 0$} \\
\{-1 \}  &\text{if $\beta_i < 0$} \\
[-1,1]   &\text{if $\beta_i = 0$}
\end{cases}
$$

Nhờ hệ điều kiện tối ưu này, ta có thể kiểm tra riêng từng thành phần của $$\beta$$ xem đã tối ưu hay chưa, từ đó chỉ tập trung cập nhật những tọa độ chưa thỏa điều kiện. Ngoài ra, coordinate descent trên Lasso hội tụ rất nhanh khi $$\lambda$$ lớn (vì nghiệm rất thưa); tận dụng tính chất này bằng cách giảm dần $$\lambda$$ và dùng nghiệm trước làm điểm khởi tạo (warm start) giúp tăng tốc đáng kể.

## Thuật toán

### Vòng ngoài (chiến lược pathwise):
* Giải lần lượt theo dãy tham số giảm dần $$\lambda_1 > \lambda_2 > \dots > \lambda_r$$.
* Dùng nghiệm tối ưu tìm được tại $$\lambda_k$$ làm điểm khởi tạo (warm start) cho coordinate descent tại $$\lambda_{k+1}$$.

### Vòng trong (chiến lược tập hoạt động — active set):
* Thực hiện một hoặc vài chu trình tọa độ đầy đủ, rồi ghi nhận các tọa độ khác 0 của $$\beta$$ vào tập hoạt động $$A$$.
* Lặp các chu trình coordinate descent chỉ trên tập $$A$$ cho đến khi hội tụ.
* Kiểm tra điều kiện tối ưu cho toàn bộ $$p$$ tọa độ của $$\beta$$; nếu có tọa độ nào vi phạm, bổ sung tọa độ đó vào $$A$$ và quay lại bước trước.

## Ghi chú

* Về mặt thực nghiệm, giải dọc theo đường tham số $$\lambda$$ (pathwise) thường nhanh hơn nhiều so với việc giải trực tiếp tại một giá trị $$\lambda$$ nhỏ riêng lẻ.
* Chiến lược tập hoạt động tận dụng triệt để tính thưa của nghiệm; do đó coordinate descent cho hồi quy Lasso chạy nhanh hơn nhiều so với hồi quy ridge (tham khảo: [phân tích so sánh hồi quy ridge và lasso](https://www.analyticsvidhya.com/blog/2016/01/complete-tutorial-ridge-lasso-regression-python/)).
* Pathwise coordinate descent hiện vẫn là một trong những thuật toán nhanh nhất cho bài toán hồi quy Lasso.
