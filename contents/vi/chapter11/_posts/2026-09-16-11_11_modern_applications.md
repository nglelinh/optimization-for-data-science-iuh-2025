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
