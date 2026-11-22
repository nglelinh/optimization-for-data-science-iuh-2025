---
layout: post
title: '19-06 Các phương pháp quasi-Newton proximal'
chapter: '19'
order: 10
owner: Hooncheol Shin
categories:
- chapter19
lang: vi
---

Khi quy mô bài toán tăng lên, việc tính trực tiếp ma trận Hessian trở nên rất tốn kém. **Các phương pháp quasi-Newton proximal** tránh tính Hessian chính xác $$H^{(k-1)} = \nabla^2 g(x^{(k-1)})$$ ở mỗi vòng lặp nhưng vẫn duy trì được tốc độ hội tụ siêu tuyến tính hoặc tuyến tính.

## Các hướng tiếp cận quasi-Newton proximal
* **Lee, Sun và Saunders (2014):** Đề xuất cập nhật ma trận xấp xỉ Hessian theo kiểu BFGS. Phương pháp này hoạt động hiệu quả và đạt tốc độ hội tụ siêu tuyến tính cục bộ.
* **Tseng và Yun (2009):** Đề xuất xấp xỉ Hessian theo khối (blockwise). Cách này áp dụng khi hàm $$f = g + h$$ có cấu trúc tách khối sao cho $$h$$ chỉ phụ thuộc từng nhóm biến riêng biệt. Chi phí tính Hessian theo khối giảm đi đáng kể và phương pháp đạt tốc độ hội tụ tuyến tính.

Các phương pháp quasi-Newton proximal không chỉ hữu ích khi Hessian khó tính toán, mà còn rất giá trị trên những bài toán có số điều kiện xấu (ill-conditioned), nơi ma trận Hessian bị suy biến hoặc gần suy biến.

#### Tài liệu tham khảo
* J. Lee and Y. Sun and M. Saunders (2014), "Proximal Newton-type methods for minimizing composite functions"
* P. Tseng and S. Yun (2009), "A coordinate gradient descent method for nonsmooth separable minimization"
