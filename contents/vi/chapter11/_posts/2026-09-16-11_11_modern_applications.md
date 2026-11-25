---
layout: post
title: 11-11 Ứng dụng hiện đại của đối ngẫu Lagrange
chapter: '11'
order: 12
owner: Nguyen Le Linh
categories:
- chapter11
lang: vi
lesson_type: optional
---

Nếu phải chọn một ứng dụng duy nhất khiến hàng triệu kỹ sư học máy trên toàn thế giới phải thầm cảm ơn Joseph-Louis Lagrange, đó chắc chắn là **bài toán đối ngẫu của Máy vector hỗ trợ (SVM)** và **Thủ thuật nhân (Kernel Trick)**. Trong không gian đặc trưng gốc, bài toán SVM cần tìm một siêu phẳng phân tách trong $$\mathbb{R}^p$$; nhưng khi ta ánh xạ dữ liệu sang không gian đặc trưng phi tuyến có hàng triệu (thậm chí vô hạn!) chiều để tách các lớp dữ liệu xoắn ốc phức tạp, việc tính trực tiếp vector trọng số $$w$$ trở nên bất khả thi.

Chính nhờ **tính đối ngẫu mạnh Lagrange** (được bảo chứng tự động bởi điều kiện Slater tinh gọn vì mọi ràng buộc SVM đều là ràng buộc affine!), ta chuyển bài toán sang biến đối ngẫu $$\alpha \in \mathbb{R}^n$$. Trong bài toán đối ngẫu ấy, vector trọng số $$w$$ biến mất hoàn toàn, chỉ còn lại ma trận tích vô hướng $$x_i^T x_j$$ — thứ có thể thay tức thì bằng hàm nhân $$K(x_i, x_j)$$ như nhân Gaussian RBF! Bài đọc tổng kết cuối chương này kết nối trực tiếp sức mạnh ấy của đối ngẫu Lagrange với bốn trụ cột hiện đại giai đoạn 2022–2026: DRO, ràng buộc vật lý trong năng lượng, công bằng học máy và phương pháp nhân.

## Kiến thức cần nhớ: Bốn cầu nối từ đối ngẫu Lagrange đến hệ thống AI & kỹ thuật hiện đại

- **Thủ thuật nhân (Kernel Trick) sinh ra từ đối ngẫu SVM:** Từ điều kiện dừng $$\nabla_w L = 0 \implies w = \sum_{i=1}^n \alpha_i y_i x_i$$, bài toán đối ngẫu chỉ phụ thuộc vào $$x_i^T x_j$$ và nghiệm $$\alpha_i^*$$ chỉ khác $$0$$ trên một số ít **vector hỗ trợ (support vectors)** nằm sát biên phân loại.
- **Điều chuẩn hóa tự động từ đối ngẫu DRO:** Trong tối ưu bền vững theo phân phối, nhân tử Lagrange của ràng buộc khoảng cách Wasserstein đóng vai trò chính xác là hệ số điều chuẩn phạt chuẩn gradient/Lipschitz của mô hình!
- **Lớp thực thi ràng buộc vật lý (DC3 / OPF-DNN):** Kết hợp hàm phạt Lagrangian vào quá trình huấn luyện mạng nơ-ron cho phép các hệ thống lưới điện thông minh và robot đạt tốc độ suy luận mili-giây mà vẫn tôn trọng định luật bảo toàn năng lượng.
- **Tối ưu minimax công bằng (Fairness Dual Games):** Biến các tiêu chí công bằng phi tuyến thành bài toán điểm yên ngựa Lagrange giữa mô hình dự đoán và bộ trọng số đối ngẫu của từng nhóm dữ liệu.

### Giải thích: Giải tay trọn vẹn bài toán đối ngẫu SVM cho 2 điểm dữ liệu 1D

Xét tập dữ liệu 1D tối giản gồm 2 điểm: $$(x_1, y_1) = (-1, -1)$$ và $$(x_2, y_2) = (+1, +1)$$.
Bài toán gốc Hard-Margin SVM:
$$\min_{w, b} \; \frac{1}{2}w^2 \quad \text{s.t.} \quad y_1(w x_1 + b) \ge 1, \quad y_2(w x_2 + b) \ge 1.$$

1. **Lập bài toán đối ngẫu Lagrange (biến $$\alpha_1, \alpha_2 \ge 0$$):**
   - Ràng buộc từ $$\frac{\partial L}{\partial b} = 0$$: $$\sum \alpha_i y_i = -\alpha_1 + \alpha_2 = 0 \implies \alpha_1 = \alpha_2 = \alpha \ge 0$$.
   - Biểu thức trọng số từ $$\frac{\partial L}{\partial w} = 0$$: $$w = \alpha_1 y_1 x_1 + \alpha_2 y_2 x_2 = \alpha_1(-1)(-1) + \alpha_2(1)(1) = \alpha_1 + \alpha_2 = 2\alpha$$.
   - Hàm mục tiêu đối ngẫu:
     $$g(\alpha) = (\alpha_1 + \alpha_2) - \frac{1}{2}w^2 = 2\alpha - \frac{1}{2}(2\alpha)^2 = 2\alpha - 2\alpha^2.$$
2. **Giải bài toán đối ngẫu lồi $$\max_{\alpha \ge 0} (2\alpha - 2\alpha^2)$$:**
   Đạo hàm $$2 - 4\alpha = 0 \implies \alpha^* = 0.5$$, tức $$\alpha_1^* = \alpha_2^* = 0.5 > 0$$ (cả hai điểm đều là vector hỗ trợ!).
   Giá trị đối ngẫu tối ưu: $$g^* = 2(0.5) - 2(0.25) = 0.5$$.
3. **Khôi phục siêu phẳng phân tách tối ưu:**
   - Trọng số: $$w^* = 2\alpha^* = 1$$.
   - Hệ số tự do $$b^*$$ từ điều kiện chặt $$y_2(w^* x_2 + b^*) = 1 \implies 1(1 + b^*) = 1 \implies b^* = 0$$.
   - Giá trị gốc: $$\frac{1}{2}(w^*)^2 = 0.5 = g^*$$, với độ rộng lề cực đại $$\frac{1}{|w^*|} = 1$$! Mọi thứ khớp chặt tuyệt đối nhờ đối ngẫu mạnh!

# Ứng dụng hiện đại của đối ngẫu Lagrange

Chương 11 mở rộng lý thuyết đối ngẫu từ quy hoạch tuyến tính sang các bài toán tối ưu tổng quát: hàm Lagrangian $$L(x,u,v)$$, hàm đối ngẫu $$g(u,v)=\inf_x L$$, tính đối ngẫu yếu $$g\le f^\star$$ và tính đối ngẫu mạnh khi bài toán lồi kèm điều kiện chuẩn hóa ràng buộc. Bài đọc tùy chọn này trình bày bốn ứng dụng hiện đại của cơ chế đối ngẫu đó — trong đó nhân tử Lagrange đóng vai trò như giá biên, bán kính bền vững hoặc tín hiệu huấn luyện.

## 1. Tối ưu bền vững theo phân phối (DRO)

Thay vì cực tiểu hóa rủi ro thực nghiệm $$\mathbb{E}_{\hat P}[\ell(x,\xi)]$$, bài toán tối ưu bền vững theo phân phối (Distributionally Robust Optimization – DRO) giải:

$$
\min_x\ \sup_{P\in\mathcal{P}}\ \mathbb{E}_P[\ell(x,\xi)],
$$

trong đó tập bất định $$\mathcal{P}$$ là một quả cầu phân phối (theo phân kỳ $$\phi$$ hoặc khoảng cách Wasserstein) quanh phân phối thực nghiệm. Bài toán $$\sup$$ bên trong là một bài toán **liên hợp / đối ngẫu**: với quả cầu Wasserstein, nó biến đổi thành bài toán cực tiểu hóa rủi ro có điều chuẩn, trong đó biến đối ngẫu đóng vai trò như hằng số phạt Lipschitz cho chi phí dịch chuyển khối lượng xác suất. Rahimian và Mehrotra (2022) tổng hợp lý thuyết đối ngẫu, cách chọn tập $$\mathcal{P}$$ và các bộ giải tương ứng. Công trình hướng dẫn về Wasserstein DRO của Kuhn, Esfahani, Nguyen và Shafieezadeh-Abadeh (2019) vẫn được trích dẫn rộng rãi giai đoạn 2023–2026 trong các nghiên cứu học máy về nhãn nhiễu, dịch chuyển phân phối và huấn luyện đối kháng. Chính tính đối ngẫu mạnh giúp chuyển bài toán kỳ vọng trường hợp xấu nhất vô hạn chiều thành một bài toán lồi hữu hạn chiều có thể giải bằng CVXPY.

## 2. Ràng buộc cứng trong năng lượng và vật lý: OPF-DNN và DC3

Bài toán luồng công suất tối ưu xoay chiều (AC-OPF) là một bài toán tối ưu không lồi với các phương trình đẳng thức Kirchhoff và giới hạn nhiệt của đường dây. Fioretto, Mak và Van Hentenryck (AAAI 2020) huấn luyện mạng nơ-ron dự đoán điểm vận hành đồng thời **cập nhật nhân tử Lagrange bằng các bước dưới đạo hàm (subgradient)** theo độ vi phạm ràng buộc — sử dụng đối ngẫu Lagrange trực tiếp như một vòng lặp huấn luyện. Donti, Rolnick và Kolter (ICLR 2021) đề xuất phương pháp **DC3**: hoàn tất các ràng buộc đẳng thức một cách khả vi, rồi hiệu chỉnh các ràng buộc bất đẳng thức bằng các bước gradient trải phẳng (unrolled), và kiểm chứng trên bài toán AC-OPF. Các nghiên cứu "học để tối ưu" (learning to optimize) giai đoạn 2022–2025 tiếp tục khai thác cùng cơ chế này: nhân tử Lagrange không chỉ là chứng chỉ kiểm tra sau khi giải, mà trở thành tín hiệu trực tiếp định hướng quá trình huấn luyện mạng.

Cần lưu ý rằng tính đối ngẫu yếu vẫn cung cấp cận dưới ngay cả khi bài toán gốc không lồi, nhưng tính đối ngẫu mạnh không tự động được bảo đảm — đây chính là ranh giới quan trọng của Chương 11.

## 3. Quy giảm công bằng như một trò chơi đối ngẫu

Agarwal và cộng sự (2018) cùng phương pháp `ExponentiatedGradient` trong thư viện Fairlearn (Weerts và cộng sự, 2023) biểu diễn các ràng buộc công bằng theo nhóm dưới dạng một hàm Lagrangian. Trong trò chơi hai người tương ứng, phía đối ngẫu tăng trọng số lên các nhóm đang bị vi phạm ràng buộc, còn phía gốc giải bài toán cực tiểu hóa rủi ro thực nghiệm (ERM) có trọng số. Cotter và cộng sự (2019) mở rộng khung này sang các ràng buộc tỷ lệ không khả vi thông qua proxy-Lagrangian. Ở cả ba phương pháp, $$v \ge 0$$ là nhân tử Lagrange cho ràng buộc bất đẳng thức $$g_i(x) \le 0$$, và theo điều kiện bù (Chương 12), nhóm nào đã thỏa mãn chặt chẽ tiêu chí công bằng (ràng buộc lỏng) sẽ có nhân tử $$v_i = 0$$.

## 4. Máy vector hỗ trợ (SVM) và phương pháp nhân (kernel)

Bài toán SVM lề mềm là ví dụ kinh điển của tối ưu tổng quát với bài toán đối ngẫu là một quy hoạch bậc hai có ràng buộc hộp trên các hệ số $$\alpha_i$$. Trình giải `SVC` trong scikit-learn cùng nhiều nghiên cứu giai đoạn 2022–2026 trong sinh học tính toán và bài toán dữ liệu bảng cỡ nhỏ vẫn giải trực tiếp bài toán đối ngẫu, bởi kỹ thuật nhân (kernel trick) được áp dụng trên hàm đối ngẫu $$g(\alpha)$$ thay vì trực tiếp trên vector trọng số $$w$$. Dạng điều kiện tối ưu KKT sẽ được phân tích ở Chương 12, còn cơ sở tồn tại của hàm đối ngẫu $$g$$ nằm ở chương này.

## Tóm tắt

Quy trình tổng quát gồm ba bước: lập hàm Lagrangian, cực tiểu hóa theo $$x$$ để thu được hàm đối ngẫu $$g$$, và cực đại hóa $$g$$ theo các nhân tử đối ngẫu. Khi bài toán gốc lồi và thỏa mãn một điều kiện chuẩn hóa ràng buộc (CQ), ta có thể hoán đổi thứ tự $$\inf$$ và $$\sup$$ (đối ngẫu mạnh). DRO, mạng nơ-ron có ràng buộc vật lý, quy giảm công bằng và SVM nhân là bốn ứng dụng khác nhau của cùng nguyên lý này.

**Câu hỏi tự kiểm tra:** Trong bài toán Wasserstein DRO, một biến đối ngẫu tối ưu có giá trị lớn ứng với bán kính quả cầu cho biết điều gì về độ nhạy với dịch chuyển phân phối, và bất đẳng thức nào trong chương này bảo đảm giá trị đó tạo thành cận dưới hợp lệ cho rủi ro trường hợp xấu nhất?

## Nguồn

- Rahimian, H., & Mehrotra, S. (2022). Frameworks and results in distributionally robust optimization. *Open Journal of Mathematical Optimization*, 3, bài 4. [doi:10.5802/ojmo.15](https://doi.org/10.5802/ojmo.15)
- Kuhn, D., Esfahani, P. M., Nguyen, V. A., & Shafieezadeh-Abadeh, S. (2019). Wasserstein distributionally robust optimization: Theory and applications in machine learning. Trong *Operations Research & Management Science in the Age of Analytics*.
- Fioretto, F., Mak, T. W. K., & Van Hentenryck, P. (2020). Predicting AC optimal power flows: Combining deep learning and Lagrangian dual methods. *AAAI*.
- Donti, P. L., Rolnick, D., & Kolter, J. Z. (2021). DC3: A learning method for optimization with hard constraints. *ICLR*.
- Weerts, H., Dudík, M., Edgar, R., Jalali, A., Lutz, R., & Madaio, M. (2023). Fairlearn: Assessing and improving fairness of AI systems. *JMLR*, 24(257).
- Agarwal, A., Beygelzimer, A., Dudík, M., Langford, J., & Wallach, H. (2018). A reductions approach to fair classification. *ICML*.
- Cotter, A., et al. (2019). Optimization with non-differentiable constraints with applications to fairness, recall, churn, and other goals. *JMLR*, 20(172).
