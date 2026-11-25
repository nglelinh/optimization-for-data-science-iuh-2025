---
layout: post
title: 23 Phương Pháp Coordinate Descent
chapter: '23'
order: 1
owner: YoungJae Choung
categories:
- chapter23
lang: vi
---

Hãy tưởng tượng bạn cần chỉnh một hệ thống âm thanh có hàng nghìn nút xoay để âm thanh trong trẻo nhất. Thay vì cố gắng xoay đồng thời cả nghìn nút cùng một lúc (như gradient descent toàn phần), bạn chọn cách cực kỳ giản dị: **giữ nguyên 999 nút kia, chỉ vặn đúng 1 nút sao cho âm thanh hay nhất**, rồi lần lượt chuyển sang nút tiếp theo.

Ý tưởng tưởng chừng quá ngây thơ ấy — **phương pháp hạ theo tọa độ (Coordinate Descent)** — hóa ra lại là một trong những thuật toán nhanh nhất và bền bỉ nhất của thống kê hiện đại. Khi hàm mục tiêu có cấu trúc tách biệt thuận lợi (như hồi quy Lasso, Elastic Net, hay bài toán đối ngẫu SVM), mỗi bước xoay một nút có nghiệm dạng đóng tính trong tích tắc, giúp hạ theo tọa độ đánh bại cả những thuật toán bậc nhất nổi tiếng như proximal gradient hay Nesterov acceleration.

## Bản đồ kiến thức nền: Bốn trụ cột của hạ theo tọa độ

Chương 23 sẽ dẫn bạn đi từ câu hỏi lý thuyết căn bản ("khi nào tối ưu từng trục suy ra tối ưu toàn cục?") đến các bộ giải công nghiệp hàng triệu biến thông qua bốn trụ cột:

- **Điều kiện tối ưu và Tính tách biệt (Separability — Định lý Tseng):** Với hàm lồi khả vi, tối ưu theo mọi trục luôn tương đương tối ưu toàn cục. Nhưng với hàm không trơn, điều này chỉ đúng khi phần không trơn *tách được theo từng tọa độ* (như chuẩn $$\ell_1$$: $$\sum_i |\beta_i|$$), nếu không thuật toán có thể bị kẹt vĩnh viễn tại một góc nhọn.
- **Phép cập nhật dạng đóng và Bảo trì phần dư (Closed-Form Updates & Residual Tracking):** Sức mạnh tốc độ của Coordinate Descent đến từ việc không tính lại toàn bộ tích ma trận-vector $$X\beta$$ ở mỗi bước; chỉ cần cập nhật phần dư $$r \leftarrow r - (\beta_i^{\text{new}} - \beta_i^{\text{old}}) X_i$$ trong thời gian $$O(n)$$.
- **Khởi động nóng dọc đường chính quy hóa (Pathwise Warm Starts):** Trong thống kê, ta hiếm khi chỉ giải Lasso cho một mức $$\lambda$$ duy nhất. Bằng cách giải từ $$\lambda_{\max}$$ (nơi mọi hệ số đều bằng 0) giảm dần xuống, nghiệm bước trước gần như đã trùng với nghiệm bước sau.
- **Chiến lược chọn tọa độ và Tập hoạt động (Cyclic, Randomized & Active Sets):** Ngoài duyệt tuần hoàn theo thứ tự $$1, 2, \dots, p$$, các bộ giải hiện đại kết hợp chọn ngẫu nhiên, quy tắc Gauss–Southwell, và tập hoạt động để chỉ tập trung tính toán trên một nhúm biến khác 0.

### Khung giải thích (nên đọc chậm): Tính tay 2 chu trình Coordinate Descent trên hàm bậc hai 2 biến

Hãy quan sát cách Coordinate Descent trượt dần xuống đáy của một thung lũng elip nghiêng: cực tiểu hóa $$f(x_1, x_2) = x_1^2 + 2x_2^2 + 2x_1 x_2 - 6x_1 - 8x_2$$, bắt đầu từ $$x^{(0)} = (0, 0)$$ (giá trị ban đầu $$f(0, 0) = 0$$).

1. **Rút công thức cập nhật dạng đóng cho từng trục:**
   - Giữ cố định $$x_2$$, đặt $$\frac{\partial f}{\partial x_1} = 2x_1 + 2x_2 - 6 = 0 \Rightarrow x_1 \leftarrow 3 - x_2$$.
   - Giữ cố định $$x_1$$, đặt $$\frac{\partial f}{\partial x_2} = 4x_2 + 2x_1 - 8 = 0 \Rightarrow x_2 \leftarrow 2 - 0.5 x_1$$.
2. **Chu trình 1 (từ $$(0, 0)$$):**
   - Cập nhật $$x_1$$: $$x_1^{(1)} = 3 - 0 = 3$$. Điểm tạm là $$(3, 0)$$, giá trị $$f(3, 0) = 9 - 18 = -9$$.
   - Cập nhật $$x_2$$ (dùng ngay $$x_1^{(1)} = 3$$ vừa tính!): $$x_2^{(1)} = 2 - 0.5(3) = 0.5$$. Điểm sau chu trình 1 là $$(3, 0.5)$$, giá trị $$f(3, 0.5) = 9 + 0.5 + 3 - 18 - 4 = -9.5$$.
3. **Chu trình 2 (từ $$(3, 0.5)$$):**
   - Cập nhật $$x_1$$: $$x_1^{(2)} = 3 - 0.5 = 2.5$$.
   - Cập nhật $$x_2$$: $$x_2^{(2)} = 2 - 0.5(2.5) = 0.75$$. Giá trị $$f(2.5, 0.75) = 6.25 + 1.125 + 3.75 - 15 - 6 = -9.875$$.
4. **Đối chiếu với nghiệm chính xác:**
   Giải hệ $$\nabla f = 0$$ ta được $$x^\star = (2, 1)$$ với $$f(2, 1) = -10$$. Chỉ sau 2 chu trình đơn giản không hề cần chọn kích thước bước (learning rate!), sai số đã giảm từ $$10$$ xuống còn $$0.125$$ — giảm tới $$80$$ lần!

Phương pháp hạ theo tọa độ (coordinate descent) là một thuật toán tối ưu lặp, cập nhật biến lần lượt dọc theo từng trục tọa độ nhằm tìm cực tiểu của hàm mục tiêu. Tại mỗi vòng lặp, dựa trên một quy tắc chọn tọa độ nhất định, thuật toán chọn một tọa độ (hoặc một khối tọa độ) rồi cực tiểu hóa hàm mục tiêu theo hướng đó (chính xác hoặc xấp xỉ) trong khi giữ cố định tất cả các tọa độ còn lại. Phương pháp này áp dụng được cho cả các bài toán có gradient lẫn không dùng gradient, và có thể kết hợp với tìm kiếm đường thẳng (line search) để chọn kích thước bước phù hợp cho từng tọa độ [16].

Coordinate descent có cấu trúc đơn giản, dễ cài đặt và đạt hiệu năng tính toán cao khi được triển khai cẩn thận trên các lớp bài toán phù hợp.

**Ví dụ ứng dụng:** hồi quy Lasso, Lasso cho mô hình tuyến tính tổng quát (GLM, kết hợp proximal Newton), SVM, group lasso, graphical lasso (áp dụng cho bài toán đối ngẫu), mô hình cộng tính (additive modeling), hoàn thiện ma trận (matrix completion) và hồi quy với các hàm phạt không lồi.

## Tài liệu tham khảo và đọc thêm

**Các nghiên cứu nền tảng về coordinate descent trong tối ưu hóa:**

* D. Bertsekas and J. Tsitsiklis (1989), “Parallel and distributed computation: numerical methods”
* Z. Luo and P. Tseng (1992), “On the convergence of the coordinate descent method for convex differentiable minimization”
* J. Ortega and W. Rheinboldt (1970), “Iterative solution of nonlinear equations in several variables”
* P. Tseng (2001), “Convergence of a block coordinate descent method for nondifferentiable minimization”

**Các tài liệu nền tảng về coordinate descent trong thống kê và học máy:**

* I. Daubechies and M. Defrise and C. De Mol (2004), “An iterative thresholding algorithm for linear inverse problems with a sparsity constraint”
* J. Friedman and T. Hastie and H. Hoefling and R. Tibshirani (2007), “Pathwise coordinate optimization”
* W. Fu (1998), “Penalized regressions: the bridge versus the lasso”
* T. Wu and K. Lange (2008), “Coordinate descent algorithms for lasso penalized regression”
* A. van der Kooij (2007), “Prediction accuracy and stability of regression with optimal scaling transformations”

**Các ứng dụng tiêu biểu của coordinate descent:**

* O. Banerjee and L. Ghaoui and A. d’Aspremont (2007), “Model selection through sparse maximum likelihood estimation”
* J. Friedman and T. Hastie and R. Tibshirani (2007), “Sparse inverse covariance estimation with the graphical lasso”
* J. Friedman and T. Hastie and R. Tibshirani (2009), “Regularization paths for generalized linear models via coordinate descent”
* C.J. Hsieh and K.W. Chang and C.J. Lin and S. Keerthi and S. Sundararajan (2008), “A dual coordinate descent method for large-scale linear SVM”
* R. Mazumder and J. Friedman and T. Hastie (2011), “SparseNet: coordinate descent with non-convex penalties”
* J. Platt (1998), “Sequential minimal optimization: a fast algorithm for training support vector machines”

**Lý thuyết gần đây cho coordinate descent:**

* A. Beck and L. Tetruashvili (2013), “On the convergence of block coordinate descent type methods”
* Y. Nesterov (2010), “Efficiency of coordinate descent methods on huge-scale optimization problems”
* J. Nutini, M. Schmidt, I. Laradji, M. Friedlander, H. Koepke (2015), “Coordinate descent converges faster with the Gauss-Southwell rule than random selection”
* A. Ramdas (2014), “Rows vs columns for linear systems of equations—randomized Kaczmarz or coordinate descent?”
* P. Richtarik and M. Takac (2011), “Iteration complexity of randomized block-coordinate descent methods for minimizing a composite function”
* A. Saha and A. Tewari (2013), “On the nonasymptotic convergence of cyclic coordinate descent methods”
* S. Wright (2015), “Coordinate descent algorithms”

**Các quy tắc sàng lọc (screening) và tài liệu về graphical lasso:**

* L. El Ghaoui and V. Viallon and T. Rabbani (2010), “Safe feature elimination in sparse supervised learning”
* R. Tibshirani, J. Bien, J. Friedman, T. Hastie, N. Simon, J. Taylor, and R. J. Tibshirani (2011), “Strong rules for discarding predictors in lasso-type problems”
* R. Mazumder and T. Hastie (2011), “The graphical lasso: new insights and alternatives”
* R. Mazumder and T. Hastie (2011), “Exact covariance thresholding into connected components for large-scale graphical lasso”
* J. Wang, P. Wonka, and J. Ye (2015), “Lasso screening rules via dual polytope projection”
* D. Witten and J. Friedman and N. Simon (2011), “New insights and faster computations for the graphical lasso”

**Phân tích hội tụ:**<br>
Dưới đây là tóm lược các hướng nghiên cứu chính về hội tụ của coordinate descent:

* Hội tụ của cực tiểu hóa từng tọa độ khi giải hệ phương trình tuyến tính (phương pháp Gauss-Seidel) là một kết quả cổ điển; xem Golub và van Loan (1996) hoặc Ramdas (2014) với góc nhìn hiện đại về coordinate descent ngẫu nhiên.
* Nesterov (2010) phân tích coordinate descent ngẫu nhiên trên hàm trơn và chứng minh tốc độ hội tụ $$O(1/\varepsilon)$$ dưới điều kiện gradient Lipschitz, cùng tốc độ $$O(\log(1/\varepsilon))$$ khi hàm lồi mạnh.
* Richtarik và Takac (2011) mở rộng và đơn giản hóa các kết quả này cho bài toán tổng của hàm trơn và hàm tách được, trong đó mỗi bước tọa độ áp dụng một toán tử proximal.
* Saha và Tewari (2013) xét bài toán chính quy hóa $$l_1$$ dạng $$g(\beta) + \lambda\|\beta\|_1$$ với $$g$$ trơn, nghiên cứu cả hạ theo tọa độ tuần hoàn lẫn cực tiểu hóa theo tọa độ tuần hoàn; dưới một số điều kiện đặc thù trên $$g$$, họ chỉ ra hai phương pháp này đạt tiến triển theo vòng lặp tốt hơn proximal gradient descent.
* Beck và Tetruashvili (2013) nghiên cứu coordinate descent tuần hoàn cho hàm trơn tổng quát, chứng minh tốc độ $$O(1/\varepsilon)$$ dưới điều kiện gradient Lipschitz và $$O(\log(1/\varepsilon))$$ khi hàm lồi mạnh, đồng thời mở rộng cho bài toán có ràng buộc với phép chiếu.
* Nutini và cộng sự (2015) phân tích coordinate descent tham lam (quy tắc Gauss-Southwell) và chỉ ra phương pháp này hội tụ nhanh hơn chọn tọa độ ngẫu nhiên trên một số lớp bài toán.
* Wright (2015) trình bày cái nhìn thống nhất và tổng quan hệ thống về các thuật toán coordinate descent, bao gồm cả các biến thể song song và bất đồng bộ.
* Lý thuyết tổng quát vẫn còn một số câu hỏi mở (chẳng hạn sự tương đương giữa chiến lược giảm dần theo gradient từng tọa độ và chiến lược cực tiểu hóa chính xác từng tọa độ).

## Ứng dụng giai đoạn 2022–2026 (tùy chọn)

Hạ theo tọa độ dọc đường chính quy hóa (pathwise coordinate descent) vẫn là nền tảng cốt lõi để `glmnet` và `sklearn.linear_model.lasso_path` ước lượng các mô hình GLM thưa. Bài báo JSS năm 2023 mở rộng `glmnet` cho *mọi* họ GLM; thư viện `skglm` (NeurIPS 2022) kết hợp tập hoạt động (working set) và các hàm phạt không lồi ở quy mô hàng triệu đặc trưng; còn hạ theo tọa độ đối ngẫu trong LIBLINEAR vẫn là bộ giải chuẩn cho SVM tuyến tính. Bạn có thể đọc tiếp tại [23-05 Ứng dụng hiện đại của hạ theo tọa độ]({% multilang_post_url contents/chapter23/2026-09-16-23_05_modern_applications %}) sau khi hoàn thành các ví dụ Lasso và pathwise.
