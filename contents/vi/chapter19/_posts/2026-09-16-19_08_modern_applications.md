---
layout: post
title: 19-08 Ứng dụng hiện đại của phương pháp proximal Newton (2022–2026)
chapter: '19'
order: 12
owner: Nguyen Le Linh
categories:
- chapter19
lang: vi
lesson_type: optional
---

Proximal Newton áp mô hình toàn phương lên mảnh *trơn* $$g$$ và để mảnh *không trơn* $$h$$ trong bài con

$$
v^{+} = \arg\min_v\ \nabla g(x)^\top v + \tfrac12 v^\top H v + h(x+v),\qquad H\approx\nabla^2 g(x).
$$

Khi $$h=\lambda\|\cdot\|_1$$ bài trong là Lasso; khi $$h$$ là hàm chỉ thị nó là toàn phương ràng buộc. Lý thuyết 2014 (Lee, Sun, Saunders) và các cài cổ điển (glmnet, QUIC) vẫn là mô hình tinh thần đúng. Điều đổi năm 2022–2026 là quy mô: bộ giải hợp bậc hai nay hoàn tất các đường ma trận chính xác mà glasso bậc nhất không làm nổi, và thư viện GLM sản xuất thêm một đường Newton–Cholesky tường minh — proximal Newton với $$h=\frac{\alpha}{2}\|\cdot\|_2^2$$.

## Mô hình đồ thị: từ QUIC tới MARS

QUIC (Hsieh, Sustik, Dhillon, Ravikumar, JMLR 2014) là ví dụ đã có ở 19-05: toàn phương Newton trên $$-\log\det\Theta+\langle S,\Theta\rangle$$ với phạt $$\ell_1$$, xuống dốc tọa độ bên trong, và hội tụ siêu tuyến tính. Nó vẫn là tham chiếu chuẩn. **MARS** (Li, Jiang, Sun, JMLR 2023) là phần tiếp thập niên 2020 mà sinh viên nên trích cho ma trận chính xác *chiều cao*. Ước lượng là mất mát D-trace phạt $$\ell_1$$ chứ không phải glasso; thuật toán là sàng thích nghi (bỏ tọa độ đã được KKT chứng nhận bằng không) cộng một lần giải **Lagrange tăng semismooth Newton** (SSNAL) trên mỗi đối ngẫu đã rút. Tác giả báo các đường trên bài $$p\approx 2\times 10^4$$ (biểu hiện gen ung thư vú, hàng trăm triệu biến đối ngẫu trước khi sàng) nơi glasso và QUIC khựng.

Hai đạo lý Chương 19 đi nguyên vẹn. Thứ nhất, đối tượng đắt vẫn là *ánh xạ proximal có thang* (ở đây một hệ Newton đối ngẫu), không phải Hessian đặc hết $$p^2$$ phần tử. Thứ hai, tập hoạt / sàng là cách proximal Newton rẻ hơn gradient proximal: một khi giá đỡ được nhận diện, hội tụ toàn phương trên tập tự do trông như phân tích địa phương ở 19-04. Genomics và trường ngẫu nhiên Markov Gauss là ứng dụng, không phải ẩn dụ — gói tại [QianLI-QL/MARS](https://github.com/QianLI-QL/MARS).

## GLM trong scikit-learn: Newton khi $$h$$ toàn phương, L-BFGS khi không

`PoissonRegressor(..., solver="newton-cholesky")` (scikit-learn 1.2, 2022) và phần mở logistic sau này lập $$H=\nabla^2 g+\alpha I$$ rồi giải bước Newton bằng Cholesky. Số hạng $$\alpha\|w\|_2^2$$ là Tikhonov / ridge: góc nhìn hợp là $$g=$$ âm log-likelihood, $$h=\frac{\alpha}{2}\|w\|_2^2$$, và ánh xạ proximal của một toàn phương lồi mạnh chính là một lần giải tuyến tính — nên proximal Newton *sụp* thành Newton giảm chấn. Đó là bảng “khi nào dùng proximal Newton?” ở 19-03 dưới dạng thư viện: nếu $$h$$ rẻ (ridge, hộp, $$\ell_1$$ với xuống dốc tọa độ), Hessian của $$g$$ đáng lập mỗi khi $$d$$ nhỏ.

Giữ L-BFGS (`solver="lbfgs"`) cho trường hợp rộng, ràng buộc hộp (Chương 18) và SAGA cho trường hợp khổng lồ, thưa, $$\ell_1$$ (Chương 26). Proximal Newton là *phần giữa* của thực đơn đó: $$d$$ vừa, $$g$$ đắt, $$h$$ có cấu trúc.

## glmnet và LIBLINEAR, vẫn là ngựa thồ GLM thưa

**glmnet** của Friedman, Hastie, Tibshirani (trích dẫn 19-05) vẫn là thuật toán đường trong R và các wrapper Python tới 2026: xuống dốc tọa độ vòng trên toàn phương trong, đúng là vòng ngoài proximal-Newton / IRLS. Newton miền tin cậy của LIBLINEAR cho logistic / SVM regularize $$\ell_2$$, và NewGLMNET cho $$\ell_1$$, cùng ý với bộ giải trong khác. Chúng không phải bài mới, nhưng là các mã vẫn huấn luyện logistic thưa trên dữ liệu click-through và y tế bảng trong khi các bài học sâu bàn Sophia. Một khóa dạy proximal Newton rồi không bao giờ gọi tên `glmnet::glmnet` đã bỏ ứng dụng.

Phần tăng 2022–2026 là tích hợp: bản viết lại GLM của scikit-learn, các đường ngoài-lõi kiểu biglasso, và các bộ giải hợp dựa trên SSNAL (dòng Sun–Toh) làm *cùng* vòng ngoài đáng tin ở những cỡ giả thiết “đủ đặc để vừa RAM” của glmnet không phủ.

## Cách phân biệt bài proximal-Newton với bài bậc nhất

Nhìn bài trong. Nếu mỗi vòng giải *toàn phương cộng $$h$$* (Lasso, QP hộp, Newton đối ngẫu trên nón) tới độ chính xác vừa rồi tìm kiếm dòng trên mục tiêu hợp, đó là Chương 19. Nếu mỗi vòng là một bước gradient cộng một phép co dạng đóng, đó là Chương 09. MARS, QUIC, glmnet và Newton–Cholesky nằm phía thứ nhất; ISTA, FISTA và SAGA nằm phía thứ hai. Các bài lai (giải trong không chính xác, $$H_k$$ quasi-Newton) là 19-06, và đó là cách bạn mở rộng khi $$\nabla^2 g$$ chỉ có dưới dạng tích Hessian–vector.

## Nguồn

- Q. Li, B. Jiang, D. Sun, “MARS: A Second-Order Reduction Algorithm for High-Dimensional Sparse Precision Matrices Estimation,” JMLR 24, 2023. [bài báo](https://jmlr.org/papers/v24/21-0699.html)
- C.-J. Hsieh, M. A. Sustik, I. S. Dhillon, P. Ravikumar, “QUIC: Quadratic Approximation for Sparse Inverse Covariance Estimation,” JMLR 15, 2014.
- J. Lee, Y. Sun, M. A. Saunders, “Proximal Newton-type methods for minimizing composite functions,” SIAM J. Optim. 24(3), 2014.
- J. Friedman, T. Hastie, R. Tibshirani, “Regularization paths for generalized linear models via coordinate descent,” J. Stat. Softw. 33(1), 2010 (glmnet; vẫn là đường sản xuất).
- Bộ giải GLM `newton-cholesky` của scikit-learn 1.2+.
