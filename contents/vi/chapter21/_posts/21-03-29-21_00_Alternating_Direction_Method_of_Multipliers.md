---
layout: post
title: '21 Phương pháp hướng luân phiên của các nhân tử (ADMM)'
chapter: '21'
order: 1
owner: Hooncheol Shin
categories:
- chapter21
lang: vi
---

Nếu Chương 20 giống như việc tháo lắp để hiểu nguyên lý động cơ của ADMM, thì Chương 21 là lúc ta đưa cỗ máy đó ra đường đua thực tế! Từ hồi quy Lasso và Group Lasso trong thống kê nhiều chiều, phân rã ma trận thưa cộng hạng thấp (Robust PCA) trong thị giác máy tính, cho tới tối ưu đồng thuận phân tán trên cụm máy chủ và tái tham số hóa bài toán con cho Fused Lasso 2D — bạn sẽ thấy một bài học sâu sắc của nghệ thuật tối ưu hóa: **cùng một bài toán, chỉ cần khéo chọn cách tách biến cho ADMM, tốc độ hội tụ có thể tăng vọt hàng chục lần!**

## Bản đồ kiến thức nền: Bốn chủ đề ứng dụng trọng tâm của Chương 21

Để định hướng rõ mạch nội dung xuyên suốt Chương 21, hãy nhìn bốn mảng ứng dụng tiêu biểu của ADMM:

- **ADMM dưới góc nhìn toán tử proximal (21-01 & 21-02):** Khi ràng buộc tách biến có dạng $$x = z$$, ADMM trở thành một vòng lặp gọi luân phiên hai toán tử $$\operatorname{prox}_{f, 1/\rho}$$ và $$\operatorname{prox}_{g, 1/\rho}$$, gắn chặt với thuật toán tách Douglas–Rachford kinh điển.
- **Thống kê nhiều chiều & Ma trận có cấu trúc (21-03 & 21-04):** Tách hàm mất mát bậc hai ra khỏi chuẩn $$\ell_1$$ (Lasso), chuẩn $$\ell_1/\ell_2$$ (Group Lasso), hoặc chuẩn hạt nhân (Nuclear Norm / Robust PCA) biến những bài toán khó nhằn thành chuỗi bước cực đơn giản: một phép giải hệ tuyến tính (phân tích Cholesky đúng một lần!) kết hợp ngưỡng mềm / ngưỡng giá trị kỳ dị.
- **Tối ưu phân tán đồng thuận (Consensus ADMM, 21-05):** Nhân bản biến cục bộ $$x_i = x$$ để mỗi nút dữ liệu giải bài toán con riêng hoàn toàn song song, rồi nút trung tâm chỉ việc lấy trung bình cộng.
- **Nghệ thuật tham số hóa bài toán con (21-06):** Thay vì tách biến theo kiểu máy móc, thiết kế các ràng buộc tách biến sao cho bài toán con giải được trong thời gian tuyến tính $$O(n)$$ và các khối biến ít tương quan hơn giúp ADMM hội tụ nhanh vượt bậc.

### Khung giải thích (nên đọc chậm): Bí quyết "phân tích Cholesky một lần" giúp ADMM giải Lasso cực nhanh

Xét bài toán Lasso $$\min_\beta \frac{1}{2}\|y - X\beta\|_2^2 + \lambda\|\beta\|_1$$ với $$X \in \mathbb{R}^{n \times p}$$. Nếu tách biến $$\beta = \alpha$$ và chạy ADMM dạng có tỉ lệ với tham số $$\rho > 0$$:

1. **Bước cập nhật $$\beta^{(k)}$$ (hệ tuyến tính đối xứng xác định dương):**
   $$\beta^{(k)} = (X^T X + \rho I)^{-1}\left(X^T y + \rho(\alpha^{(k-1)} - w^{(k-1)})\right).$$
2. **Bước cập nhật $$\alpha^{(k)}$$ (ngưỡng mềm từng phần tử):**
   $$\alpha^{(k)} = S_{\lambda/\rho}\left(\beta^{(k)} + w^{(k-1)}\right), \qquad w^{(k)} = w^{(k-1)} + \beta^{(k)} - \alpha^{(k)}.$$
3. **Điểm ăn tiền về hiệu năng tính toán (giả sử $$p = 1{,}000$$ và chạy $$200$$ vòng lặp):**
   - Ma trận $$M = X^T X + \rho I$$ **không hề thay đổi** qua suốt $$200$$ vòng lặp (khi giữ cố định $$\rho$$)!
   - Ta chỉ cần phân tích Cholesky $$M = L L^T$$ **duy nhất một lần** trước vòng lặp (tốn $$\frac{1}{3}p^3 \approx 3.3 \times 10^8$$ phép toán).
   - Ở cả $$200$$ vòng lặp sau đó, mỗi bước chỉ giải hai hệ tam giác tốn $$2p^2 = 2 \times 10^6$$ phép toán — **rẻ hơn 165 lần** so với việc giải lại hệ tuyến tính từ đầu ở mỗi bước!

---

Chương này đi sâu hơn vào phương pháp ADMM đã được giới thiệu ở [Chương 20]({% multilang_post_url contents/chapter20/21-03-27-20_00_Dual_Methods %}). Về mặt khái niệm cơ bản, nội dung không mở rộng thêm nhiều so với Chương 20 mà chủ yếu tập trung vào các bài toán và trường hợp ứng dụng cụ thể.

### Các bài báo tham khảo

* Boyd, Stephen, et al. [BPCPE11] "Distributed optimization and statistical learning via the alternating direction method of multipliers." Foundations and Trends® in Machine learning 3.1 (2011): 1-122.
* Hong, Mingyi, and Zhi-Quan Luo. [HL12] "On the linear convergence of the alternating direction method of multipliers." Mathematical Programming 162.1-2 (2017): 165-199.
* Deng, Wei, and Wotao Yin. [DY16] "On the global and linear convergence of the generalized alternating direction method of multipliers." Journal of Scientific Computing 66.3 (2016): 889-916.
* Iutzeler, Franck, et al. [IBCH14] "Linear convergence rate for distributed optimization with the alternating direction method of multipliers." 53rd IEEE Conference on Decision and Control. IEEE, 2014.
* Nishihara, Robert, et al. [NLRPJ15] "A general analysis of the convergence of ADMM." arXiv preprint arXiv:1502.02009 (2015).
* Parikh, Neal, and Stephen Boyd. [NB13] "Proximal algorithms." Foundations and Trends® in Optimization 1.3 (2014): 127-239.
* Vu, Vincent Q., et al. [VCLR13] "Fantope projection and selection: A near-optimal convex relaxation of sparse PCA." Advances in neural information processing systems. 2013.
* Candès, Emmanuel J., et al. [CLMW09] "Robust principal component analysis?." Journal of the ACM (JACM) 58.3 (2011): 11.
* Ramdas, Aaditya, and Ryan J. Tibshirani. [RT16] "Fast and flexible ADMM algorithms for trend filtering." Journal of Computational and Graphical Statistics 25.3 (2016): 839-858.
* Wytock, Matt, Suvrit Sra, and Jeremy Z. Kolter. [WSK14] "Fast Newton methods for the group fused lasso." UAI. 2014.
* Barbero, Alvaro, and Suvrit Sra. [BS14] "Modular proximal optimization for multidimensional total-variation regularization." arXiv preprint arXiv:1411.0589 (2014).

Phân tích hội tụ của ADMM: [BPCPE11], [HL12], [DY16], [IBCH14], [NLRPJ15]  
Ước lượng không gian con thưa: [VCLR13]  
Phân rã thưa cộng hạng thấp: [CLMW09]  
ADMM đồng thuận (Consensus ADMM): [BPCPE11], [NB13]  
Tham số hóa bài toán con: [RT16], [WSK14], [BS14]

## Ứng dụng giai đoạn 2022–2026 (tùy chọn)

Các ví dụ cổ điển trên (Lasso, phân rã thưa cộng hạng thấp, đồng thuận, fused lasso) vẫn là nền tảng cốt lõi để tiếp cận ADMM. Bên cạnh đó, một bài học tùy chọn tổng hợp giai đoạn 2022–2026 sẽ mở rộng *cùng* cấu trúc tách đồng thuận và toán tử proximal sang học sâu liên kết (**FedADMM**), tạo ảnh plug-and-play với bộ khử nhiễu CNN, và bài toán tối ưu dòng công suất (OPF) phân tán trực tuyến. Bạn có thể đọc tiếp tại [21-07 Ứng dụng hiện đại của ADMM]({% multilang_post_url contents/chapter21/2026-09-16-21_07_modern_applications %}). Bài học này không thay thế tài liệu của Boyd và cộng sự, mà minh họa những hệ thống thực tế nơi phần dư vẫn đóng vai trò giám sát quan trọng.
