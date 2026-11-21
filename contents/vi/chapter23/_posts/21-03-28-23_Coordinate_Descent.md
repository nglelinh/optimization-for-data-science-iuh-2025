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

Coordinate descent là một thuật toán tối ưu lặp, di chuyển lần lượt theo từng trục tọa độ để tìm cực tiểu của hàm mục tiêu. Ở mỗi vòng lặp, theo một quy tắc chọn tọa độ, thuật toán xác định một trục tọa độ (coordinate) hoặc một khối tọa độ, rồi cực tiểu hóa hàm theo hướng của trục đó trong khi giữ cố định các trục hoặc khối tọa độ không được chọn (một cách chính xác hoặc không chính xác). Coordinate descent có thể dùng không chỉ với các phương pháp dựa trên gradient mà còn với các phương pháp không dùng gradient. Ngoài ra, tùy trường hợp, có thể dùng line search để xác định kích thước bước phù hợp cho từng trục [16].

Coordinate descent rất đơn giản, dễ cài đặt, và cho hiệu năng rất tốt khi được cài đặt cẩn thận cho các bài toán phù hợp.

**Ví dụ:** hồi quy lasso, lasso GLM (dưới proximal Newton), SVM, group lasso, graphical lasso (áp dụng cho bài toán đối ngẫu), additive modeling, matrix completion, hồi quy với các phạt không lồi

## Tài liệu tham khảo và đọc thêm

**Các nghiên cứu sớm về coordinate descent trong tối ưu:**

* D. Bertsekas and J. Tsitsiklis (1989), “Parallel and distributed domputation: numerical methods”
* Z. Luo and P. Tseng (1992), “On the convergence of the coordinate descent method for convex differentiable minimization”
* J. Ortega and W. Rheinboldt (1970), “Iterative solution of nonlinear equations in several variables”
* P. Tseng (2001), “Convergence of a block coordinate descent method for nondifferentiable minimization”
**Các tài liệu sớm về coordinate descent trong thống kê và ML:**
* I. Daubechies and M. Defrise and C. De Mol (2004), “An iterative thresholding algorithm for linear inverse problems with a sparsity constraint”
* J. Friedman and T. Hastie and H. Hoefling and R. Tibshirani (2007), “Pathwise coordinate optimization”
* W. Fu (1998), “Penalized regressions: the bridge versus the lasso”
* T. Wu and K. Lange (2008), “Coordinate descent algorithms for lasso penalized regression”
* A. van der Kooij (2007), “Prediction accuracy and stability of regresssion with optimal scaling transformations”

**Các ứng dụng của coordinate descent:**

* O. Banerjee and L. Ghaoui and A. d’Aspremont (2007), “Model selection through sparse maximum likelihood estimation”
* J. Friedman and T. Hastie and R. Tibshirani (2007), “Sparse inverse covariance estimation with the graphical lasso”
* J. Friedman and T. Hastie and R. Tibshirani (2009), “Regularization paths for generalized linear models via coordinate descent”
* C.J. Hsieh and K.W. Chang and C.J. Lin and S. Keerthi and S. Sundararajan (2008), “A dual coordinate descent method for large-scale linear SVM”
* R. Mazumder and J. Friedman and T. Hastie (2011), “SparseNet: coordinate descent with non-convex penalties”
* J. Platt (1998), “Sequential minimal optimization: a fast algorithm for training support vector machines”
**Lý thuyết gần đây cho coordinate descent:**
* A. Beck and L. Tetruashvili (2013), “On the convergence of block coordinate descent type methods”
* Y. Nesterov (2010), “Efficiency of coordinate descent methods on huge-scale optimization problems”
* J. Nutini, M. Schmidt, I. Laradji, M. Friedlander, H. Koepke (2015), “Coordinate descent converges faster with the Gauss- Southwell rule than random selection”
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
Xin giới thiệu ngắn gọn các hướng nghiên cứu về phân tích hội tụ của coordinate descent.

* Sự hội tụ của cực tiểu hóa theo từng tọa độ để giải hệ tuyến tính, tức phương pháp Gauss-Seidel, là một chủ đề cổ điển. Ví dụ, xem Golub và van Loan (1996), hoặc Ramdas (2014) với góc nhìn hiện đại về coordinate descent ngẫu nhiên.
* Nesterov (2010) xét coordinate descent ngẫu nhiên cho các hàm trơn và chỉ ra rằng nó đạt tốc độ $$O(1/ε)$$ dưới điều kiện gradient Lipschitz, và tốc độ $$O(\log(1/ε))$$ dưới tính lồi mạnh.
* Richtarik và Takac (2011) mở rộng và đơn giản hóa các kết quả này, xét các hàm dạng trơn cộng với tách được, trong đó mỗi cập nhật coordinate descent áp dụng một phép prox.
* Saha và Tewari (2013) xét cực tiểu hóa các hàm chính quy hóa $$l_1$$ có dạng $$g(β) + λ\|β\|_1$$, với $$g$$ trơn, và nghiên cứu cả coordinate descent tuần hoàn lẫn cực tiểu hóa theo tọa độ tuần hoàn. Dưới các điều kiện (rất lạ) trên $$g$$, họ chỉ ra rằng cả hai phương pháp đều vượt proximal gradient descent về mức tiến triển theo vòng lặp.
* Beck và Tetruashvili (2013) nghiên cứu coordinate descent tuần hoàn cho các hàm trơn nói chung. Họ chỉ ra rằng nó đạt tốc độ $$O(1/ε)$$ dưới điều kiện gradient Lipschitz, và $$O(\log(1/ε))$$ dưới tính lồi mạnh. Họ cũng mở rộng các kết quả này sang trường hợp có ràng buộc với phép chiếu.
* Nutini et al. (2015) phân tích coordinate descent tham lam (quy tắc Gauss-Southwell), và chỉ ra nó đạt tốc độ nhanh hơn coordinate descent ngẫu nhiên đối với một số bài toán.
* Wright (2015) đưa ra sự thống nhất và một bản tóm tắt tuyệt vời. Cũng bao gồm các phiên bản song song (thậm chí bất đồng bộ).
* Lý thuyết tổng quát vẫn chưa hoàn chỉnh; vẫn còn các câu hỏi chưa có lời đáp (ví dụ: chiến lược descent và chiến lược minimization có giống nhau không?)
