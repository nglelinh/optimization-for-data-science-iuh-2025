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

Khi bài toán lớn dần, việc tính Hessian trở nên rất đắt. **Các phương pháp quasi-Newton proximal** tránh tính Hessian $$H^{(k-1)} = \nabla^2 g(x^{(k-1)})$$ ở mỗi bước, mà vẫn đạt tốc độ hội tụ siêu tuyến tính hoặc tuyến tính.

## Phương pháp quasi-Newton proximal
* Lee (2014) đề xuất cập nhật xấp xỉ Hessian theo kiểu BFGS. Phương pháp này hoạt động rất tốt và có tốc độ hội tụ siêu tuyến tính cục bộ.
* Tseng và Yun (2009) đề xuất xấp xỉ Hessian theo khối (blockwise). Cách này chỉ hoạt động khi $$f = g + h$$ có thể được tách thành các phần mà $$h$$ chỉ phụ thuộc vào một số biến tối ưu. Việc tính Hessian theo khối nhanh hơn rất nhiều. Phương pháp này có tốc độ hội tụ tuyến tính.

Các phương pháp quasi-Newton hữu ích không chỉ khi Hessian khó tính, mà còn trong các bài toán điều kiện xấu (ill-conditioned) mà Hessian là suy biến hoặc gần suy biến.

#### Tài liệu tham khảo
* J. Lee and Y. Sun and M. Saunders (2014), "Proximal Newton-type methods for minimizing composite functions"
* P. Tseng and S. Yun (2009), "A coordinate gradient descent method for nonsmooth separable minimization"
