---
layout: post
title: 12-09 Ứng dụng hiện đại của điều kiện KKT
chapter: '12'
order: 10
owner: Nguyen Le Linh
categories:
- chapter12
lang: vi
lesson_type: optional
---

# Ứng dụng hiện đại của điều kiện KKT

Chương 12 nêu hệ KKT — khả thi gốc, khả thi đối ngẫu, bù, và dừng của Lagrangian — rồi làm các ví dụ SVM, water-filling, và $$\ell_1$$. Bài tùy chọn này chỉ ra nơi *hệ ấy* được giải, lấy vi phân, hoặc đọc như một giá trong phần mềm 2022–2026. Chúng ta không liệt lại bốn khối.

## 1. Lấy vi phân xuyên qua bộ giải: cvxpylayers và Theseus

Nếu $$x^\star(\theta)$$ là nghiệm duy nhất của chương trình lồi tham số hóa, định lý hàm ẩn áp lên ánh xạ KKT $$F(x,u,v;\theta)=0$$ cho $$\mathrm{d}x^\star/\mathrm{d}\theta$$ mà không unroll bộ giải. Agrawal, Amos, Barratt, Boyd, Diamond và Kolter (NeurIPS 2019) chuyển ý ấy thành **cvxpylayers** (PyTorch / JAX / MLX). Đó vẫn là cách mặc định, năm 2024–2026, để đặt một QP hoặc SOCP *bên trong* mạng: lớp danh mục (DeepDow), chính sách MPC, và các phép chiếu kiểu sparsemax.

Pineda, Fan, Monge, Venkataraman, Sodhi, Chen, Ortiz, DeTone, Wang, Anderson, Dong, Amos và Mukadam (NeurIPS 2022) phát hành **Theseus**, thư viện GPU cho bình phương tối thiểu *phi tuyến* khả vi dùng trong robot và thị giác. Chiều ngược lại là vi phân ẩn của điều kiện dừng (Gauss–Newton / Levenberg–Marquardt) — KKT của NLS có đẳng thức hoặc regularizer. Bài 2022 là bài cần trích; repo là thứ stack SLAM / bundle-adjustment thực sự import.

**Nối với giáo trình.** Dừng $$\nabla_x L=0$$ là hệ tuyến tính Theseus lấy vi phân. Bù xuất hiện ngay khi lớp có bất đẳng thức (cvxpylayers).

## 2. Vector hỗ trợ SVM là một phát biểu KKT

Ví dụ [12-04]({% multilang_post_url contents/chapter12/21-04-02-12_04_Example_support_vector_machines %}) không phải trang trí. Bù nói rằng điểm có $$0<\alpha_i<C$$ nằm trên lề, điểm có $$\alpha_i=0$$ được phân loại đúng với slack, và điểm có $$\alpha_i=C$$ là vector hỗ trợ biên. SVM kernel vẫn là công cụ chuẩn trong ML khoa học nhỏ-$$n$$ 2022–2026 (hóa tin, EEG, dữ liệu lâm sàng dạng bảng) đúng vì tập hữu hạn vector ấy *là* mô hình. Khi bài báo báo “47 vector hỗ trợ,” họ đang báo active set của một hệ KKT.

## 3. LMP điện và bù

Giá biên theo vị trí là biến đối ngẫu của cân bằng công suất và giới hạn dòng (Chương 10). Liang và Dvorkin (2023) đảo LMP công bố để khôi phục giá chào; phép đảo được vì, tại điểm khớp không suy biến, KKT chỉ ra bất đẳng thức nào ràng. Donti, Rolnick và Kolter (2021) huấn luyện DC3 sao cho đầu ra mạng bị kéo về một điểm OPF khả thi KKT. Water-filling trong [12-03]({% multilang_post_url contents/chapter12/21-04-02-12_03_Example_water_filling %}) là cùng bức tranh bù trên kênh Gauss; các bài phân bổ công suất 5G / 6G vẫn viết mực nước ấy như nhân tử của bất đẳng thức tổng công suất.

## 4. Công bằng: ràng buộc nhóm nào chặt?

Trong một khớp Fairlearn / reductions (Weerts và cộng sự, 2023), nhân tử lớn trên equalised odds của nhóm $$a$$ nghĩa là ràng buộc tỷ lệ nhóm ấy **đang ràng** — bù bằng lời. Nhân tử không nghĩa là mô hình không ràng buộc đã thỏa tỷ lệ ấy. Đọc $$(x^\star,v^\star)$$ vì thế là công cụ gỡ lỗi: nó nói ràng buộc xã hội-kỹ thuật *nào* đắt, không chỉ rằng Lagrangian đã được cực tiểu.

## Cần nhớ

KKT là hệ bậc nhất (i) đặc trưng cực tiểu lồi có ràng buộc, (ii) có thể lấy vi phân để huấn luyện một lớp, và (iii) đặt tên các tài nguyên có giá. Nếu bài báo 2024 “nhúng QP vào mạng” hoặc “báo vector hỗ trợ” hoặc “công bố LMP,” họ đang nói về hệ ấy.

**Câu hỏi.** Vì sao vi phân ẩn của KKT cần điều kiện ràng buộc và Jacobian KKT không suy biến — và điều gì hỏng trong một lớp Lasso khi hai đặc trưng trùng nhau?

## Nguồn

- Agrawal, A., Amos, B., Barratt, S., Boyd, S., Diamond, S., & Kolter, J. Z. (2019). Differentiable convex optimization layers. *NeurIPS*. Thư viện: [cvxpylayers](https://www.cvxpylayers.org/)
- Pineda, L., Fan, T., Monge, M., Venkataraman, S., Sodhi, P., Chen, R. T. Q., Ortiz, J., DeTone, D., Wang, A., Anderson, S., Dong, J., Amos, B., & Mukadam, M. (2022). Theseus: A library for differentiable nonlinear optimization. *NeurIPS*. [arXiv:2207.09442](https://arxiv.org/abs/2207.09442)
- Liang, Z., & Dvorkin, Y. (2023). Data-driven inverse optimization for marginal offer price recovery in electricity markets. *ACM e-Energy ’23*.
- Donti, P. L., Rolnick, D., & Kolter, J. Z. (2021). DC3: A learning method for optimization with hard constraints. *ICLR*.
- Weerts, H., Dudík, M., Edgar, R., Jalali, A., Lutz, R., & Madaio, M. (2023). Fairlearn: Assessing and improving fairness of AI systems. *JMLR*, 24(257).
