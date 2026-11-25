---
layout: post
title: 14 Phương pháp Newton
chapter: '14'
order: 1
owner: Minjoo Lee
categories:
- chapter14
lang: vi
---

Nếu Gradient Descent giống như một người leo núi bịt mắt chỉ biết sờ độ dốc ngay dưới chân rồi bước từng bước ngắn xuống thung lũng, thì **Phương pháp Newton** lại mang trên mình một chiếc kính nhìn thấy trọn vẹn **độ cong** của địa hình xung quanh. Trong một hẻm núi dài và hẹp (bài toán có số điều kiện lớn), Gradient Descent có thể mất hàng nghìn bước chạy zích-zắc mệt mỏi, còn phương pháp Newton chỉ cần 5 đến 10 bước để lao thẳng tới đáy với độ chính xác máy tính $$10^{-12}$$.

Chương 14 đưa bạn bước vào thế giới của **tối ưu hóa bậc hai**: từ công thức cập nhật Newton kinh điển, tính bất biến affine kỳ diệu, đại lượng giảm Newton, tìm kiếm đường backtracking, lý thuyết hàm tự hài hòa của Nesterov–Nemirovskii, cho tới các phương pháp Quasi-Newton (BFGS/L-BFGS) và những biến thể bậc hai đang huấn luyện các mô hình AI ngày nay.

## Bản đồ kiến thức nền: Bốn trụ cột của tối ưu hóa bậc hai

- **Xấp xỉ Taylor bậc hai và ma trận Hessian:** Thay vì xấp xỉ hàm mục tiêu bằng mặt phẳng tiếp xúc (bậc nhất), phương pháp Newton khớp một mặt paraboloid $$\tilde{f}(y) = f(x) + \nabla f(x)^T(y-x) + \frac{1}{2}(y-x)^T \nabla^2 f(x)(y-x)$$ rồi nhảy thẳng tới đáy của paraboloid đó.
- **Tính bất biến affine và hình học độ cong:** Phép nhân với nghịch đảo Hessian $$(\nabla^2 f(x))^{-1}$$ tự động "làm tròn" các đường đồng mức méo mó thành hình cầu, khiến phương pháp Newton miễn nhiễm với việc đổi đơn vị đo hay kéo giãn trục tọa độ.
- **Hai pha hội tụ (giảm chấn và bậc hai):** Khi còn xa đáy, backtracking line search giữ bước đi an toàn (pha giảm chấn); khi đã lọt vào vùng lân cận nghiệm, bước Newton thuần túy kích hoạt **hội tụ bậc hai** — số chữ số đúng tăng gấp đôi sau mỗi vòng lặp!
- **Chi phí đại số tuyến tính và xấp xỉ bậc hai:** Mỗi bước Newton đòi hỏi giải hệ tuyến tính cỡ $$n \times n$$ (tốn $$O(n^3)$$ với ma trận đặc), là động lực ra đời của các phương pháp khai thác cấu trúc thưa, Quasi-Newton (BFGS, L-BFGS) và xấp xỉ Hessian đường chéo/khối trong học sâu.

### Khung giải thích (nên đọc chậm): So sánh 1 bước Newton với Gradient Descent trên thung lũng méo

Xét hàm bậc hai 2 chiều có số điều kiện $$\kappa = 100$$:

$$f(x_1, x_2) = \frac{1}{2}x_1^2 + 50x_2^2,$$

nghiệm tối ưu là $$x^\star = (0, 0)^T$$. Xuất phát từ $$x^{(0)} = (10, 1)^T$$:

1. **Tính gradient và ma trận Hessian tại $$x^{(0)} = (10, 1)^T$$:**
   $$\nabla f(x^{(0)}) = \begin{bmatrix} x_1 \\ 100 x_2 \end{bmatrix} = \begin{bmatrix} 10 \\ 100 \end{bmatrix}, \qquad \nabla^2 f(x^{(0)}) = \begin{bmatrix} 1 & 0 \\ 0 & 100 \end{bmatrix}.$$
2. **Bước Gradient Descent (với bước học an toàn lớn nhất $$t = \frac{1}{L} = \frac{1}{100} = 0.01$$):**
   $$x^{(1)}_{\text{GD}} = \begin{bmatrix} 10 \\ 1 \end{bmatrix} - 0.01 \begin{bmatrix} 10 \\ 100 \end{bmatrix} = \begin{bmatrix} 9.9 \\ 0 \end{bmatrix}.$$
   Tọa độ $$x_2$$ về $$0$$ ngay, nhưng $$x_1$$ mới nhích từ $$10$$ xuống $$9.9$$ — mất hàng trăm vòng lặp nữa mới tiến gần $$0$$!
3. **Bước Newton thuần túy:**
   $$x^{(1)}_{\text{Newton}} = x^{(0)} - (\nabla^2 f(x^{(0)}))^{-1}\nabla f(x^{(0)}) = \begin{bmatrix} 10 \\ 1 \end{bmatrix} - \begin{bmatrix} 1 & 0 \\ 0 & 1/100 \end{bmatrix}\begin{bmatrix} 10 \\ 100 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}.$$
   Chỉ sau **đúng 1 bước**, phương pháp Newton hạ cánh chính xác tại nghiệm tối ưu $$(0, 0)^T$$!

---

Trong chương này, chúng ta sẽ tìm hiểu về phương pháp Newton.

Phương pháp Newton là thuật toán tìm giá trị nhỏ nhất của hàm khả vi hai lần dựa trên khai triển Taylor bậc hai. Tại mỗi vòng lặp, phương pháp xấp xỉ hàm mục tiêu bằng một hàm bậc hai và cập nhật nghiệm theo điểm cực tiểu của hàm xấp xỉ đó. Trong vùng lân cận điểm tối ưu, phương pháp đạt tốc độ hội tụ bậc hai, nhanh hơn đáng kể so với phương pháp gradient descent.

## Tài liệu tham khảo và đọc thêm
* S. Boyd and L. Vandenberghe (2004), "Convex optimization", Chapter 9 and 10
* Y. Nesterov (1998), "Introductory lectures on convex optimization: a basic course", Chapter 2
* Y. Nesterov and A. Nemirovskii (1994), "Interior-point polynomial methods in convex programming", Chapter 2
* J. Nocedal and S. Wright (2006), "Numerical optimization", Chapters 6 and 7
* L. Vandenberghe, Lecture notes for EE 236C, UCLA, Spring 2011-2012
