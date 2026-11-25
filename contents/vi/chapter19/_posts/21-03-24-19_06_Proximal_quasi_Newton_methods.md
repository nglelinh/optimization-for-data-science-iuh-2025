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

Ở bài 19-03 ta đã thấy điểm yếu lớn nhất của Newton proximal: khi số chiều $$n$$ lên đến hàng chục nghìn, ngay cả việc tính và lưu ma trận Hessian chính xác $$H = \nabla^2 g(x)$$ đã bất khả thi, chưa nói đến giải bài toán con bậc hai dày đặc bên trong. Một ý tưởng hết sức tự nhiên nảy ra từ Chương 18: **ta thay Hessian chính xác $$\nabla^2 g(x)$$ bằng một ma trận xấp xỉ rẻ tiền hơn $$B_k$$ (BFGS, L-BFGS, hoặc đường chéo/theo khối)!** Đó chính là họ **phương pháp Quasi-Newton proximal**.

## Bản đồ kiến thức nền: Ba hướng thiết kế ma trận xấp xỉ độ cong cho bài toán tổng hợp

Tùy vào cấu trúc của hàm không trơn $$h$$ và kích thước bài toán, người ta chọn một trong ba chiến lược xấp xỉ Hessian sau:

- **Proximal BFGS / L-BFGS (Lee, Sun & Saunders, 2014):** Xây dựng $$B_k$$ từ các cặp $$(s_i, y_i)$$ của hàm trơn $$g$$ (chú ý chỉ dùng biến thiên gradient của phần trơn $$y_k = \nabla g(x_{k+1}) - \nabla g(x_k)$$!). Phương pháp đạt hội tụ **siêu tuyến tính cục bộ** mà không cần tính đạo hàm bậc hai.
- **Xấp xỉ theo khối (Blockwise Coordinate Gradient — Tseng & Yun, 2009):** Khi $$h(x) = \sum_b h_b(x_b)$$ tách được theo từng khối biến (như Group Lasso), ta chọn $$B_k$$ là ma trận khối đường chéo. Bài toán con lập tức tách thành nhiều bài toán nhỏ độc lập nhau, giải song song cực nhanh và đảm bảo hội tụ tuyến tính toàn cục.
- **Xấp xỉ đường chéo cộng hạng thấp (Diagonal + Low-Rank):** Đặc biệt với L-BFGS, vì $$B_k = \gamma_k I + U M U^T$$ có cấu trúc đường chéo cộng hạng $$2m$$, ta có thể giải bài toán con $$\operatorname{prox}_{B_k}$$ bằng thuật toán hạ tọa độ hoặc bài toán đối ngẫu chỉ cỡ $$2m$$ biến (với $$m \approx 10$$)!

### Khung giải thích (nên đọc chậm): So sánh chi phí giải bài toán con khi $$B_k$$ là ma trận đường chéo vs. ma trận đầy đủ

Xét bài toán 2 biến với $$h(x) = |x_1| + |x_2|$$ tại $$x = (1, 1)^T$$, $$\nabla g(x) = (2, 4)^T$$, và xét hai lựa chọn ma trận xấp xỉ Hessian:

1. **Lựa chọn 1 — Xấp xỉ đường chéo (Barzilai–Borwein / đường chéo Hessian) $$B_{\text{diag}} = \begin{bmatrix} 2 & 0 \\ 0 & 8 \end{bmatrix}$$:**
   - Bài toán con tách rời hoàn toàn từng biến:
     $$v_1 = S_{1/2}(1 - 2/2) - 1 = 0 - 1 = -1 \implies x_1^+ = 0,$$
     $$v_2 = S_{1/8}(1 - 4/8) - 1 = S_{0.125}(0.5) - 1 = -0.625 \implies x_2^+ = 0.375.$$
   - **Chi phí:** Nghiệm dạng đóng chính xác ngay trong $$O(n)$$ phép toán, không cần vòng lặp bên trong!
2. **Lựa chọn 2 — Xấp xỉ BFGS đầy đủ $$B_{\text{BFGS}} = \begin{bmatrix} 2 & 1 \\ 1 & 8 \end{bmatrix}$$:**
   - Vì có phần tử ngoài đường chéo $$1$$ (tạo số hạng chéo $$v_1 v_2$$), hai biến $$v_1$$ và $$v_2$$ **dính chặt vào nhau** nên không còn công thức đóng theo từng tọa độ nữa; ta phải chạy vài vòng lặp hạ tọa độ bên trong (cố định $$v_2$$ cập nhật $$v_1$$ rồi ngược lại).
   - **Đổi lại:** Nắm bắt được tương quan chéo giữa $$x_1$$ và $$x_2$$, giúp hội tụ siêu tuyến tính thay vì tuyến tính!

---

Khi quy mô bài toán tăng lên, việc tính trực tiếp ma trận Hessian trở nên rất tốn kém. **Các phương pháp quasi-Newton proximal** tránh tính Hessian chính xác $$H^{(k-1)} = \nabla^2 g(x^{(k-1)})$$ ở mỗi vòng lặp nhưng vẫn duy trì được tốc độ hội tụ siêu tuyến tính hoặc tuyến tính.

## Các hướng tiếp cận quasi-Newton proximal
* **Lee, Sun và Saunders (2014):** Đề xuất cập nhật ma trận xấp xỉ Hessian theo kiểu BFGS. Phương pháp này hoạt động hiệu quả và đạt tốc độ hội tụ siêu tuyến tính cục bộ.
* **Tseng và Yun (2009):** Đề xuất xấp xỉ Hessian theo khối (blockwise). Cách này áp dụng khi hàm $$f = g + h$$ có cấu trúc tách khối sao cho $$h$$ chỉ phụ thuộc từng nhóm biến riêng biệt. Chi phí tính Hessian theo khối giảm đi đáng kể và phương pháp đạt tốc độ hội tụ tuyến tính.

Các phương pháp quasi-Newton proximal không chỉ hữu ích khi Hessian khó tính toán, mà còn rất giá trị trên những bài toán có số điều kiện xấu (ill-conditioned), nơi ma trận Hessian bị suy biến hoặc gần suy biến.

#### Tài liệu tham khảo
* J. Lee and Y. Sun and M. Saunders (2014), "Proximal Newton-type methods for minimizing composite functions"
* P. Tseng and S. Yun (2009), "A coordinate gradient descent method for nonsmooth separable minimization"
