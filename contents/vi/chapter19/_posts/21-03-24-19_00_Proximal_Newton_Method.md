---
layout: post
title: '19 Phương pháp Proximal Newton'
chapter: '19'
order: 1
owner: Hooncheol Shin
categories:
- chapter19
lang: vi
---

Trong học máy hiện đại, hiếm khi nào hàm mục tiêu hoàn toàn trơn tru: một bài toán hồi quy logistic có phạt Lasso $$\ell_1$$, hay ước lượng ma trận hiệp phương sai thưa (graphical lasso), luôn là phép cộng của hai thế giới đối lập — một hàm mất mát trơn $$g(x)$$ và một hàm điều chuẩn sắc cạnh, không khả vi $$h(x)$$. Phương pháp hạ gradient proximal (Chương 9) xử lý được $$h(x)$$ nhưng lại chỉ dùng một hằng số bước vô hướng, nên ì ạch khi $$g(x)$$ cong lệch theo các trục khác nhau. Chương 19 mang sức mạnh độ cong bậc hai của phương pháp Newton ghép trực tiếp vào khung proximal: ta xấp xỉ bậc hai phần trơn $$g(x)$$ bằng đúng ma trận Hessian $$\nabla^2 g(x)$$, nhưng giữ nguyên vẹn phần không trơn $$h(x)$$!

## Bản đồ kiến thức nền: Bốn nhánh kiến thức hội tụ trong Chương 19

Trước khi đi sâu vào các bài học của chương này, hãy xem bốn mảng kiến thức kết nối với nhau ra sao:

- **Tối ưu hóa hàm tổng hợp (Composite Optimization):** Tách hàm mục tiêu $$f(x) = g(x) + h(x)$$ thành phần trơn $$g$$ (khả vi hai lần) và phần không trơn $$h$$ (lồi, có cấu trúc đặc biệt như $$\lambda\|x\|_1$$ hay hàm chỉ thị $$I_C(x)$$).
- **Ánh xạ proximal có tỉ lệ (Scaled Proximal Map):** Tổng quát hóa khoảng cách Euclid $$\frac{1}{2t}\|z - x\|_2^2$$ thành chuẩn cảm sinh bởi ma trận Hessian $$\frac{1}{2}\|z - x\|_H^2$$, giúp bước đi uốn lượn đúng theo hình dạng elip độ cong cục bộ của $$g$$.
- **Thuật toán hai tầng (Outer Newton + Inner Solver):** Khác với proximal gradient vốn có công thức đóng, bài toán con bậc hai có phạt $$h$$ thường không có nghiệm đóng và phải giải bằng một bộ giải bên trong cực nhanh (như hạ tọa độ trong `glmnet` và `QUIC`).
- **Biến thể Quasi-Newton và Newton chiếu:** Khi Hessian quá đắt, ta thay bằng xấp xỉ BFGS hoặc xấp xỉ theo khối (Proximal Quasi-Newton); khi $$h = I_C$$ là hàm chỉ thị ràng buộc, ta cần cẩn trọng để có phiên bản **Projected Newton** thực sự giảm hàm mục tiêu.

### Khung giải thích (nên đọc chậm): So sánh 1 bước Proximal Gradient và 1 bước Proximal Newton trên cùng bài toán

Xét bài toán hàm tổng hợp 1 chiều $$f(x) = g(x) + h(x)$$ với $$g(x) = 2x^2$$ (độ cong không đổi $$g''(x) = 4$$) và $$h(x) = |x|$$, có nghiệm tối ưu chính xác là $$x^\star = 0$$. Bắt đầu từ $$x^{(0)} = 1$$ ($$g'(1) = 4$$):

1. **Một bước Proximal Gradient với bước học bảo thủ $$t = 0.1$$:**
   - Bước gradient trơn: $$z = x^{(0)} - t g'(x^{(0)}) = 1 - 0.1(4) = 0.6$$.
   - Ngưỡng mềm (soft-thresholding) với ngưỡng $$t = 0.1$$: $$x^{(1)}_{\text{PGD}} = S_{0.1}(0.6) = 0.6 - 0.1 = 0.5$$.
   (Nghiệm mới chỉ đi được nửa đường về $$0$$.)
2. **Một bước Proximal Newton với độ cong chính xác $$H = g''(1) = 4$$:**
   - Giải bài toán con: $$v^{(1)} = \arg\min_v \left(4v + \frac{1}{2}(4)v^2 + |1 + v|\right)$$.
   - Đặt $$y = 1 + v$$, bài toán viết lại thành $$\arg\min_y \left(2y^2 + |y|\right) = \operatorname{prox}_{|\cdot|/4}(0) = S_{0.25}(0) = 0$$!
   - Suy ra $$v^{(1)} = -1$$ và $$x^{(1)}_{\text{PN}} = 1 + (-1) = 0 = x^\star$$ — **chạm trúng nghiệm tối ưu chính xác chỉ sau 1 bước duy nhất!**

---

Trong chương này, chúng ta tìm hiểu **phương pháp Proximal Newton**, **phương pháp Proximal Quasi-Newton** và **phương pháp Projected Newton**.

### Tài liệu tham khảo

Phương pháp Proximal Newton:

* J. Friedman and T. Hastie and R. Tibshirani (2009), "Regularization paths for generalized linear models via coordinate descent"
* C.J. Hsieh and M.A. Sustik and I. Dhillon and P. Ravikumar (2011), "Sparse inverse covariance matrix estimation using quadratic approximation"
* M. Patriksson (1998), "Cost approximation: a unified framework of descent algorithms for nonlinear programs"
* J. Lee and Y. Sun and M. Saunders (2014), "Proximal Newton-type methods for minimizing composite functions"
* P. Tseng and S. Yun (2009), "A coordinate gradient descent method for nonsmooth separable minimization"

Phương pháp Projected Newton:

* A. Barbero and S. Sra (2011), "Fast Newton-type methods for total variation regularization"
* D. Bertsekas (1982), "Projected Newton methods for optimization problems with simple constraints"
* D. Kim and S. Sra. and I. Dhillon (2010), "Tackling box-constrained optimization via a new projected quasi-Newton approach"
* M. Schmidt and D. Kim and S. Sra (2011), "Projected Newton-type methods in machine learning"
