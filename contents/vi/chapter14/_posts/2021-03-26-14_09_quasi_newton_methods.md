---
layout: post
title: 14-09 Các phương pháp Quasi-Newton
chapter: '14'
order: 17
owner: Minjoo Lee
categories:
- chapter14
lang: vi
---

Đứng giữa hai thái cực — Gradient Descent quá chậm vì mù độ cong, và Phương pháp Newton quá đắt vì phải tính và nghịch đảo ma trận Hessian $$O(n^3)$$ — các nhà toán học thập niên 1960–1970 đã tìm ra một "vùng đất vàng" đầy thiên tài: **các phương pháp Tựa Newton (Quasi-Newton)**, với đại diện huyền thoại là **BFGS** và phiên bản tiết kiệm bộ nhớ **L-BFGS**.

Ý tưởng của Quasi-Newton giống như việc bạn quan sát sự thay đổi của độ dốc sau mỗi bước đi để **dần dần tự vẽ lại bản đồ độ cong** mà không bao giờ cần tính một đạo hàm bậc hai nào cả! Chỉ từ lịch sử các bước dịch chuyển $$s_k = x^{(k+1)} - x^{(k)}$$ và hiệu gradient $$y_k = \nabla f(x^{(k+1)}) - \nabla f(x^{(k)})$$, BFGS cập nhật một ma trận xấp xỉ nghịch đảo Hessian $$H_k$$ chỉ tốn $$O(n^2)$$ (và L-BFGS chỉ tốn $$O(mn)$$ với $$m \approx 10$$), nhưng vẫn đạt tốc độ **hội tụ siêu tuyến tính** sát nút phương pháp Newton!

## Kiến thức cần nhớ: Cách Quasi-Newton học độ cong chỉ từ đạo hàm bậc nhất

- **Phương trình cát tuyến (Secant Equation):** Vì $$\nabla f(x^{(k+1)}) - \nabla f(x^{(k)}) \approx \nabla^2 f(x^{(k+1)})(x^{(k+1)} - x^{(k)})$$, ma trận xấp xỉ Hessian mới $$B_{k+1}$$ (hoặc nghịch đảo $$H_{k+1} = B_{k+1}^{-1}$$) phải thỏa mãn:
  $$B_{k+1} s_k = y_k \qquad \Longleftrightarrow \qquad H_{k+1} y_k = s_k.$$
- **Cập nhật hạng thấp (Rank-2 Update) của BFGS:** Trong vô số ma trận đối xứng xác định dương thỏa $$H_{k+1} y_k = s_k$$, BFGS chọn ma trận gần $$H_k$$ nhất theo chuẩn có trọng số, cho ra công thức cập nhật chỉ gồm phép nhân vectơ-ma trận tốn $$O(n^2)$$ mà không cần giải hệ tuyến tính!
- **Điều kiện độ cong $$s_k^T y_k > 0$$:** Để $$H_{k+1}$$ luôn xác định dương (đảm bảo hướng đi luôn là hướng giảm), ta cần $$s_k^T y_k > 0$$ — điều kiện này tự động thỏa mãn khi dùng tìm kiếm đường Wolfe cho hàm lồi.
- **L-BFGS cho bài toán lớn:** Thay vì lưu ma trận $$H_k$$ cỡ $$n \times n$$, L-BFGS chỉ lưu $$m$$ cặp vectơ $$(s_i, y_i)$$ gần nhất (thường $$m = 5\text{–}20$$), giảm cả bộ nhớ lẫn chi phí mỗi bước xuống $$O(mn)$$!

### Giải thích: Thực hiện tay 1 bước cập nhật BFGS và kiểm chứng phương trình cát tuyến

Xét hàm bậc hai 2 chiều $$f(x_1, x_2) = x_1^2 + 2x_2^2$$ (Hessian thật là $$Q = \begin{bmatrix} 2 & 0 \\ 0 & 4 \end{bmatrix}$$, nghịch đảo thật là $$Q^{-1} = \begin{bmatrix} 0.5 & 0 \\ 0 & 0.25 \end{bmatrix}$$).
Khởi tạo tại $$x^{(0)} = (1, 1)^T$$ với xấp xỉ nghịch đảo Hessian ban đầu $$H_0 = I_2$$ (chưa biết gì về độ cong).

1. **Bước đi đầu tiên (giống GD vì $$H_0 = I$$):**
   - $$\nabla f(x^{(0)}) = (2, 4)^T$$, hướng tìm kiếm $$p_0 = -H_0 \nabla f(x^{(0)}) = (-2, -4)^T$$.
   - Chọn bước tối ưu theo đường thẳng $$t_0 = \frac{\nabla f^T p_0}{-p_0^T Q p_0} = \frac{20}{2(4) + 4(16)} = \frac{20}{72} = \frac{5}{18} \approx 0.2778$$.
   - Giả sử để tính tay cực gọn, ta đi một bước $$t_0 = 0.25$$ (thỏa điều kiện giảm mạnh):
     $$x^{(1)} = (1, 1)^T + 0.25(-2, -4)^T = (0.5, 0)^T.$$
2. **Tính cặp cát tuyến $$(s_0, y_0)$$:**
   - $$s_0 = x^{(1)} - x^{(0)} = (-0.5, -1)^T$$.
   - $$\nabla f(x^{(1)}) = (1, 0)^T \implies y_0 = \nabla f(x^{(1)}) - \nabla f(x^{(0)}) = (-1, -4)^T$$.
   - Kiểm tra điều kiện độ cong: $$s_0^T y_0 = (-0.5)(-1) + (-1)(-4) = 4.5 > 0$$ (đặt $$\rho_0 = \frac{1}{s_0^T y_0} = \frac{2}{9}$$).
3. **Tính $$H_1 = (I - \rho_0 s_0 y_0^T) H_0 (I - \rho_0 y_0 s_0^T) + \rho_0 s_0 s_0^T$$ và kiểm chứng $$H_1 y_0 = s_0$$:**
   - Do $$H_0 = I$$, ta có $$I - \rho_0 s_0 y_0^T = I - \frac{2}{9}\begin{bmatrix} 0.5 & 2 \\ 1 & 4 \end{bmatrix} = \frac{1}{9}\begin{bmatrix} 8 & -4 \\ -2 & 1 \end{bmatrix}$$.
   - Tính trực tiếp:
     $$H_1 = \frac{1}{81}\begin{bmatrix} 8 & -4 \\ -2 & 1 \end{bmatrix}\begin{bmatrix} 8 & -2 \\ -4 & 1 \end{bmatrix} + \frac{2}{9}\begin{bmatrix} 0.25 & 0.5 \\ 0.5 & 1 \end{bmatrix} = \frac{1}{81}\begin{bmatrix} 80 & -20 \\ -20 & 5 \end{bmatrix} + \frac{1}{81}\begin{bmatrix} 4.5 & 9 \\ 9 & 18 \end{bmatrix} = \frac{1}{81}\begin{bmatrix} 84.5 & -11 \\ -11 & 23 \end{bmatrix}.$$
   - **Kiểm tra phương trình cát tuyến:**
     $$H_1 y_0 = \frac{1}{81}\begin{bmatrix} 84.5(-1) + (-11)(-4) \\ (-11)(-1) + 23(-4) \end{bmatrix} = \frac{1}{81}\begin{bmatrix} -40.5 \\ -81 \end{bmatrix} = \begin{bmatrix} -0.5 \\ -1 \end{bmatrix} = s_0!$$
   Không hề dùng đạo hàm bậc hai, $$H_1$$ đã khớp chính xác độ cong dọc theo hướng vừa đi — và trên hàm bậc hai 2 chiều, chỉ sau 2 bước BFGS sẽ khớp trọn vẹn $$Q^{-1}$$!

---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
    });
</script>

Khi chi phí tính ma trận Hessian quá lớn hoặc ma trận Hessian bị suy biến, ta có thể dùng các phương pháp tựa Newton (quasi-Newton) để thay $$\nabla^{2}f(x)$$ bằng một ma trận xấp xỉ xác định dương $$H \succ 0$$:

>\begin{align}
>x^{+} = x - tH^{-1}\nabla f(x)
>\end{align}

Một số đặc điểm chính của các phương pháp quasi-Newton (xem chi tiết tại [Chương 18]({% multilang_post_url contents/chapter18/21-03-23-18_00_Quasi_Newton_methods %})):

* Ma trận xấp xỉ Hessian $$H$$ (hoặc nghịch đảo $$H^{-1}$$) được cập nhật sau mỗi bước với mục tiêu tính $$H^{-1}\nabla f(x)$$ với chi phí thấp.
* Tốc độ hội tụ là siêu tuyến tính, chậm hơn tốc độ bậc hai của phương pháp Newton đầy đủ; thông thường, khoảng $$n$$ bước quasi-Newton mang lại mức tiến triển tương đương một bước Newton.
* Nhiều phương pháp quasi-Newton cập nhật $$H$$ ở mỗi vòng lặp bằng các công thức cập nhật bậc thấp dựa trên thông tin gradient thu được từ các bước trước.
