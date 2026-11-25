---
layout: post
title: 11-08 Ứng dụng hiện đại của đối ngẫu Lagrange
chapter: '11'
order: 9
owner: Nguyen Le Linh
categories:
- chapter11
lang: vi
lesson_type: optional
redirect_from:
  - /contents/vi/chapter11/11_10_modern_applications/
---

Trong thực tế giai đoạn 2022–2026, rất ít mô hình học máy hay hệ thống điều khiển được chạy trong "phòng thí nghiệm lý tưởng" nơi phân phối dữ liệu kiểm thử giống hệt dữ liệu huấn luyện. Khi khí hậu biến đổi, hành vi người dùng dịch chuyển, hay cảm biến lưới điện bị nhiễu, mô hình tối ưu theo kỳ vọng thực nghiệm thông thường có thể sụp đổ đột ngột. Giải pháp đột phá của thập kỷ hiện tại là **Tối ưu bền vững theo phân phối (Distributionally Robust Optimization — DRO)**: thay vì tối thiểu hóa mất mát trung bình trên đúng phân phối mẫu $$\hat{P}$$, ta tối thiểu hóa **mất mát kỳ vọng xấu nhất** trên toàn bộ một quả cầu phân phối $$Q$$ nằm gần $$\hat{P}$$ (theo khoảng cách Wasserstein hay $$f$$-divergence)!

Nghe qua thì DRO bất khả thi về mặt tính toán vì bài toán bên trong $$\sup_{Q \in \mathcal{B}(\hat{P}, \rho)} \mathbb{E}_Q[\ell(x, \xi)]$$ tối ưu trên một **không gian vô hạn chiều các phân phối xác suất**! Nhưng phép màu của Chương 11 xuất hiện đúng lúc: bằng cách áp dụng **đối ngẫu mạnh Lagrange** lên bài toán con vô hạn chiều ấy, ta biến nó thành một **bài toán tối ưu lồi hữu hạn chiều chỉ có đúng 1 biến nhân tử Lagrange vô hướng $$\lambda \ge 0$$**!

## Kiến thức cần nhớ: Bốn nhánh ứng dụng hiện đại của đối ngẫu Lagrange (2022–2026)

- **Tối ưu bền vững theo phân phối (DRO):** Đối ngẫu mạnh biến bài toán minimax trên không gian phân phối xác suất (Wasserstein / KL / $$\chi^2$$-divergence) thành bài toán có số hạng điều chuẩn tường minh — hé lộ mối liên hệ sâu sắc rằng DRO thực chất tương đương với việc thêm điều chuẩn chuẩn Lipschitz lên mô hình!
- **Ràng buộc vật lý cứng trong lưới điện và kỹ thuật (OPF-DNN & DC3):** Kết hợp mạng nơ-ron dự đoán nhanh với bước sửa ràng buộc bằng hàm Lagrangian tăng cường (Augmented Lagrangian) giúp giải bài toán điều phối công suất xoay chiều (AC-OPF) nhanh gấp trăm lần bộ giải cổ điển mà vẫn bảo đảm không vi phạm giới hạn nhiệt hay điện áp.
- **Học máy công bằng như trò chơi yên ngựa Lagrange:** Ràng buộc công bằng giữa các nhóm nhân khẩu học được đưa vào hàm Lagrangian và giải bằng vòng lặp cực tiểu hóa theo trọng số mô hình xen kẽ cực đại hóa theo nhân tử Lagrange.
- **Máy vector hỗ trợ (SVM) và thủ thuật nhân (Kernel Trick):** Nhờ đối ngẫu mạnh (Slater tự động thỏa cho ràng buộc affine), bài toán đối ngẫu SVM chỉ phụ thuộc vào tích vô hướng $$x_i^T x_j$$, mở cửa cho mọi nhân phi tuyến $$K(x_i, x_j)$$ trong không gian Hilbert vô hạn chiều!

### Giải thích: Tính tay đối ngẫu Lagrange cho bài toán DRO 2 trạng thái

Giả sử một quyết định đầu tư có 2 kịch bản mất mát là $$\ell_1 = 1$$ và $$\ell_2 = 5$$. Phân phối thực nghiệm hiện tại là $$\hat{p} = (0.5, 0.5)$$ (mất mát trung bình $$0.5(1) + 0.5(5) = 3.0$$). Ta muốn tìm **mất mát kỳ vọng xấu nhất** trên mọi phân phối $$q = (q_1, q_2)$$ cách $$\hat{p}$$ không quá $$\rho = 0.2$$ theo chuẩn $$\ell_1$$ (tức $$|q_1 - 0.5| + |q_2 - 0.5| \le 0.2$$, $$q_1 + q_2 = 1, q \ge 0$$).

1. **Giải trực tiếp bài toán gốc (vì chỉ có 2 trạng thái):**
   Để mất mát lớn nhất, ta chuyển tối đa xác suất từ kịch bản nhẹ ($$\ell_1 = 1$$) sang kịch bản nặng ($$\ell_2 = 5$$): với $$|q_1 - 0.5| + |q_2 - 0.5| = 2|q_2 - 0.5| \le 0.2 \implies q_2 \le 0.6$$.
   Phân phối xấu nhất là $$q^* = (0.4, 0.6)$$, cho mất mát xấu nhất $$p^* = 0.4(1) + 0.6(5) = 3.4$$.
2. **Giải bằng đối ngẫu Lagrange (chỉ 1 nhân tử phạt $$\lambda \ge 0$$ cho ngân sách $$\rho = 0.2$$):**
   Đặt $$\Delta = q - \hat{p} = (-\delta, +\delta)$$ với $$2|\delta| \le 0.2$$. Hàm Lagrangian theo $$\delta$$ là:
   $$L(\delta, \lambda) = 3.0 + (5 - 1)\delta + \lambda(0.2 - 2|\delta|) = 3.0 + 0.2\lambda + (4\delta - 2\lambda|\delta|).$$
   Để $$\sup_\delta L(\delta, \lambda)$$ hữu hạn (không vọt lên $$+\infty$$), ta bắt buộc có $$2\lambda \ge 4 \implies \lambda \ge 2$$! Khi đó $$\sup_\delta (4\delta - 2\lambda|\delta|) = 0$$.
3. **Cực tiểu hóa hàm đối ngẫu $$g(\lambda) = 3.0 + 0.2\lambda$$ trên $$\lambda \ge 2$$:**
   Đạt tại $$\lambda^* = 2$$ với $$d^* = 3.0 + 0.2(2) = 3.4 = p^*$$!
   Ý nghĩa tuyệt đẹp: mất mát DRO bằng **mất mát thực nghiệm ($$3.0$$) cộng thêm bán kính bền vững ($$0.2$$) nhân biên độ dao động mất mát ($$\frac{5-1}{2} = 2$$)** — đúng là công thức điều chuẩn hóa từ đối ngẫu Lagrange!

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
