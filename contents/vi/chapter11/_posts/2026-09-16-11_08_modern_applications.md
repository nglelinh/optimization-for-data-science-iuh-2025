---
layout: post
title: 11-10 Ứng dụng hiện đại của đối ngẫu Lagrange
chapter: '11'
order: 11
owner: Nguyen Le Linh
categories:
- chapter11
lang: vi
lesson_type: optional
---

# Ứng dụng hiện đại của đối ngẫu Lagrange

Chương 11 nâng đối ngẫu từ LP lên chương trình tổng quát: Lagrangian $$L(x,u,v)$$, hàm đối ngẫu $$g(u,v)=\inf_x L$$, đối ngẫu yếu $$g\le f^\star$$, và đối ngẫu mạnh khi lồi cộng điều kiện ràng buộc. Bài tùy chọn này chỉ ra bốn cách dùng *đối ngẫu ấy* hiện đại — nhân tử như giá, như bán kính bền vững, và như tín hiệu huấn luyện — mà không xây lại $$g$$.

## 1. Học bền vững theo phân phối (DRO)

Thay vì cực tiểu rủi ro thực nghiệm $$\mathbb{E}_{\hat P}[\ell(x,\xi)]$$, DRO giải

$$
\min_x\ \sup_{P\in\mathcal{P}}\ \mathbb{E}_P[\ell(x,\xi)],
$$

trong đó tập mơ hồ $$\mathcal{P}$$ là một quả cầu phân phối (phân kỳ $$\phi$$ hoặc Wasserstein) quanh mẫu. Sup bên trong là bài toán **liên hợp / đối ngẫu**: với quả cầu Wasserstein nó trở thành rủi ro có regularizer mà biến đối ngẫu là giá Lipschitz của việc dời khối. Rahimian và Mehrotra (2022) khảo sát đối ngẫu, cách chỉnh $$\mathcal{P}$$, và các bộ giải. Kuhn, Esfahani, Nguyen và Shafieezadeh-Abadeh (2019) là bài hướng dẫn Wasserstein vẫn được trích 2023–2026 trong các bài ML về nhãn nhiễu, dịch phân phối, và huấn luyện đối kháng. Đối ngẫu mạnh là thứ biến kỳ vọng worst-case vô hạn chiều thành chương trình lồi hữu hạn bạn đưa được cho CVXPY.

## 2. Ràng buộc cứng trong năng lượng và vật lý: OPF-DNN và DC3

Luồng công suất tối ưu AC (OPF) là chương trình không lồi với đẳng thức Kirchhoff và giới hạn nhiệt. Fioretto, Mak và Van Hentenryck (AAAI 2020) huấn luyện mạng dự đoán setpoint đồng thời **cập nhật nhân tử Lagrange bằng bước subgradient** trên phần dư ràng buộc — đối ngẫu Lagrange như một vòng huấn luyện. Donti, Rolnick và Kolter (ICLR 2021) đề xuất **DC3**: hoàn tất đẳng thức một cách khả vi, rồi sửa bất đẳng thức bằng các bước gradient unroll, và minh họa trên AC-OPF. Các bài “học để tối ưu” 2022–2025 giữ cùng ý đối ngẫu: nhân tử không chỉ là chứng chỉ sau việc; chúng là **đặc trưng** mạng được huấn luyện để tôn trọng.

Đối ngẫu yếu vẫn cho cận dù gốc không lồi; đối ngẫu mạnh *không* miễn phí. Phân biệt ấy là cả điểm của chương này.

## 3. Reduction công bằng như trò chơi đối ngẫu

Agarwal và cộng sự (2018) và bộ giảm `ExponentiatedGradient` của Fairlearn (Weerts và cộng sự, 2023) coi ràng buộc tỷ lệ nhóm như một Lagrangian. Người chơi đối ngẫu đặt khối trên nhóm đang bị vi phạm; người chơi gốc giải ERM *có trọng số*. Cotter và cộng sự (2019) mở trò chơi sang ràng buộc tỷ lệ không trơn qua proxy-Lagrangian. Ở cả ba, $$v\ge 0$$ là nhân tử Chương 11 của bất đẳng thức $$g_i(x)\le 0$$, và bù (Chương 12) nói nhóm đã đạt tỷ lệ phải có $$v_i=0$$.

## 4. SVM và máy kernel, vẫn qua đối ngẫu

SVM soft-margin là chương trình tổng quát sách giáo khoa mà đối ngẫu là QP hộp trên hệ số $$\alpha_i$$. `SVC` của sklearn và một đuôi dài các bài 2022–2026 về sinh học tính toán và bảng nhỏ-$$n$$ vẫn *giải đối ngẫu*, vì mẹo kernel là phát biểu về $$g(\alpha)$$, không về $$w$$. Bạn sẽ gặp dạng KKT ở Chương 12; *sự tồn tại* của một $$g$$ hữu ích là chương này.

## Cần nhớ

Lập Lagrangian, cực tiểu theo $$x$$ để được $$g$$, cực đại $$g$$ theo nhân tử. Nếu gốc lồi và một CQ thỏa, bạn được đổi inf và sup. DRO, mạng có ràng buộc, bộ giảm công bằng, và SVM kernel là bốn câu chuyện khác nhau về phép đổi ấy.

**Câu hỏi.** Trong bài DRO Wasserstein, một biến đối ngẫu tối ưu lớn trên bán kính nói gì về chi phí dịch phân phối — và bất đẳng thức nào của chương này làm con số ấy thành cận dưới hợp lệ của rủi ro worst-case?

## Nguồn

- Rahimian, H., & Mehrotra, S. (2022). Frameworks and results in distributionally robust optimization. *Open Journal of Mathematical Optimization*, 3, bài 4. [doi:10.5802/ojmo.15](https://doi.org/10.5802/ojmo.15)
- Kuhn, D., Esfahani, P. M., Nguyen, V. A., & Shafieezadeh-Abadeh, S. (2019). Wasserstein distributionally robust optimization: Theory and applications in machine learning. Trong *Operations Research & Management Science in the Age of Analytics*.
- Fioretto, F., Mak, T. W. K., & Van Hentenryck, P. (2020). Predicting AC optimal power flows: Combining deep learning and Lagrangian dual methods. *AAAI*.
- Donti, P. L., Rolnick, D., & Kolter, J. Z. (2021). DC3: A learning method for optimization with hard constraints. *ICLR*.
- Weerts, H., Dudík, M., Edgar, R., Jalali, A., Lutz, R., & Madaio, M. (2023). Fairlearn: Assessing and improving fairness of AI systems. *JMLR*, 24(257).
- Agarwal, A., Beygelzimer, A., Dudík, M., Langford, J., & Wallach, H. (2018). A reductions approach to fair classification. *ICML*.
- Cotter, A., et al. (2019). Optimization with non-differentiable constraints with applications to fairness, recall, churn, and other goals. *JMLR*, 20(172).
