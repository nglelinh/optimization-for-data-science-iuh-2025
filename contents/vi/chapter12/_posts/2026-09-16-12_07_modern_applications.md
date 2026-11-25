---
layout: post
title: 12-07 Ứng dụng hiện đại của điều kiện KKT
chapter: '12'
order: 8
owner: Nguyen Le Linh
categories:
- chapter12
lang: vi
lesson_type: optional
redirect_from:
  - /contents/vi/chapter12/12_09_modern_applications/
---

Nếu trước năm 2019, bài toán tối ưu lồi và mạng nơ-ron sâu sống ở hai thế giới riêng biệt — mạng nơ-ron dự đoán tham số, sau đó một bộ giải tối ưu chạy tách rời ở bước cuối — thì giai đoạn 2022–2026 đã hợp nhất hai thế giới ấy bằng một đột phá tuyệt đẹp: **lấy vi phân xuyên qua bộ giải tối ưu (Differentiable Optimization Layers — `cvxpylayers`, `OptNet`, `Theseus`)**! Bạn có thể nhúng thẳng cả một bài toán tối ưu lồi làm một tầng (layer) bên trong mạng PyTorch và huấn luyện đầu-cuối bằng lan truyền ngược!

Bí mật giúp ta tính được đạo hàm $$\frac{\partial x^*(\theta)}{\partial \theta}$$ của nghiệm tối ưu $$x^*(\theta)$$ theo tham số đầu vào $$\theta$$ mà không cần mở tung hàng nghìn vòng lặp của bộ giải bên trong chính là **hệ phương trình KKT kết hợp với Định lý Hàm Ẩn (Implicit Function Theorem)**! Vì $$x^*(\theta)$$ và $$(u^*(\theta), v^*(\theta))$$ luôn thỏa đẳng thức KKT $$F(x^*, u^*, v^*; \theta) = 0$$, chỉ cần lấy vi phân hai vế của đúng hệ KKT đó tại điểm nghiệm là ta thu ngay ma trận Jacobian chính xác!

## Bản đồ kiến thức nền: Bốn nhánh ứng dụng hiện đại của điều kiện KKT (2022–2026)

- **Lấy vi phân ẩn xuyên qua bộ giải (`cvxpylayers` & `Theseus`):** Thay vì lưu toàn bộ đồ thị tính toán của vòng lặp tối ưu (tốn bộ nhớ khổng lồ), lan truyền ngược chỉ cần giải *một hệ phương trình tuyến tính duy nhất* từ vi phân của hệ KKT tại điểm tối ưu $$(x^*, u^*, v^*)$$!
- **Giải mã độ thưa của SVM và các mô hình biên rộng:** Điều kiện bù KKT giải thích vì sao chỉ một tập con nhỏ các vector hỗ trợ mới định hình biên quyết định, giúp nén mô hình và phân tích độ nhạy dữ liệu (influence functions).
- **Giá điện biên theo vị trí (LMP) trong vận hành lưới điện:** Điều kiện bù KKT tự động xác định những đường dây truyền tải nào đang bị nghẽn ($$u_l^* > 0$$), từ đó phân tách giá điện theo từng nút địa lý một cách minh bạch.
- **Kiểm soát ràng buộc công bằng trong học máy:** Nhận diện nhóm nhân khẩu học nào đang có ràng buộc công bằng chặt ($$u_g^* > 0$$) giúp kỹ sư AI biết chính xác nhóm nào đang là điểm nghẽn của sự đánh đổi độ chính xác – công bằng.

### Khung giải thích (nên đọc chậm): Tính tay đạo hàm $$\frac{\partial x^*}{\partial \theta}$$ xuyên qua hệ KKT của một tầng tối ưu

Xét một tầng tối ưu lồi cực giản dị (chính là tầng kích hoạt ReLU dưới lăng kính tối ưu!):
$$x^*(\theta) = \arg\min_{x \in \mathbb{R}} \; \frac{1}{2}(x - \theta)^2 \quad \text{s.t.} \quad -x \le 0 \; (\text{tức } x \ge 0).$$

1. **Viết hệ phương trình KKT tại nghiệm $$(x^*(\theta), u^*(\theta))$$:**
   $$\begin{cases} x^* - \theta - u^* = 0 & (\text{dừng}) \\ u^* x^* = 0 & (\text{điều kiện bù}) \end{cases}$$
   Dễ thấy nghiệm đóng là $$x^*(\theta) = \max(0, \theta)$$ và $$u^*(\theta) = \max(0, -\theta)$$.
2. **Lấy vi phân ẩn hai vế hệ KKT theo $$\theta$$ (cách `cvxpylayers` hoạt động!):**
   $$\begin{pmatrix} 1 & -1 \\ u^* & x^* \end{pmatrix} \begin{pmatrix} \frac{\partial x^*}{\partial \theta} \\ \frac{\partial u^*}{\partial \theta} \end{pmatrix} = \begin{pmatrix} 1 \\ 0 \end{pmatrix}.$$
3. **Giải hệ tuyến tính $$2 \times 2$$ cho hai chế độ:**
   - **Khi $$\theta = 2 > 0$$** ($$x^* = 2, u^* = 0$$): hàng 2 là $$0\frac{\partial x^*}{\partial \theta} + 2\frac{\partial u^*}{\partial \theta} = 0 \implies \frac{\partial u^*}{\partial \theta} = 0$$, thay vào hàng 1 cho $$\frac{\partial x^*}{\partial \theta} = 1$$!
   - **Khi $$\theta = -2 < 0$$** ($$x^* = 0, u^* = 2$$): hàng 2 là $$2\frac{\partial x^*}{\partial \theta} + 0 = 0 \implies \frac{\partial x^*}{\partial \theta} = 0$$, thay vào hàng 1 cho $$\frac{\partial u^*}{\partial \theta} = -1$$!
   Chỉ từ 2 dòng vi phân hệ KKT, ta khôi phục chính xác 100% đạo hàm của hàm ReLU — và cơ chế này mở rộng tức thì lên mọi bài toán QP, SOCP, SDP hàng nghìn biến trong PyTorch!

# Ứng dụng hiện đại của điều kiện KKT

Chương 12 đã trình bày hệ điều kiện KKT — gồm tính khả thi nguyên thủy, tính khả thi đối ngẫu, điều kiện bù yếu và điều kiện dừng của hàm Lagrangian — cùng các ví dụ về SVM, thuật toán water-filling và bài toán phạt $$\ell_1$$. Bài đọc tùy chọn này điểm qua các ứng dụng thực tế giai đoạn 2022–2026 nơi hệ KKT được giải trực tiếp, lấy vi phân ẩn hoặc diễn giải như giá biên trong phần mềm tối ưu, mà không lặp lại phần lý thuyết cơ bản.

## 1. Lấy vi phân xuyên qua bộ giải: cvxpylayers và Theseus

Nếu $$x^\star(\theta)$$ là nghiệm duy nhất của một bài toán quy hoạch lồi phụ thuộc tham số $$\theta$$, định lý hàm ẩn áp dụng lên ánh xạ KKT $$F(x,u,v;\theta)=0$$ cho phép tính đạo hàm $$\mathrm{d}x^\star/\mathrm{d}\theta$$ mà không cần trải ngược (unroll) các bước lặp của bộ giải. Agrawal, Amos, Barratt, Boyd, Diamond và Kolter (NeurIPS 2019) hiện thực hóa ý tưởng này trong thư viện **cvxpylayers** (hỗ trợ PyTorch, JAX và MLX). Trong giai đoạn 2024–2026, đây vẫn là cách làm tiêu chuẩn để nhúng một bài toán QP hoặc SOCP *bên trong* mạng nơ-ron, chẳng hạn trong lớp tối ưu hóa danh mục đầu tư (DeepDow), chính sách điều khiển dự báo mô hình (MPC) và các phép chiếu kiểu sparsemax.

Pineda, Fan, Monge, Venkataraman, Sodhi, Chen, Ortiz, DeTone, Wang, Anderson, Dong, Amos và Mukadam (NeurIPS 2022) phát hành **Theseus**, thư viện chạy trên GPU cho bài toán bình phương tối thiểu *phi tuyến* khả vi dùng trong robot và thị giác máy tính. Quá trình lan truyền ngược dựa trên vi phân ẩn của điều kiện dừng (Gauss–Newton hoặc Levenberg–Marquardt) — tương ứng với hệ KKT của bài toán bình phương tối thiểu phi tuyến có ràng buộc đẳng thức hoặc thành phần điều chuẩn. Công trình năm 2022 là tài liệu tham khảo chính, còn mã nguồn thư viện được dùng trực tiếp trong nhiều hệ thống SLAM và hiệu chỉnh chùm tia (bundle adjustment).

**Liên hệ với giáo trình:** Điều kiện dừng $$\nabla_x L=0$$ tạo thành hệ tuyến tính mà Theseus lấy vi phân, còn điều kiện bù yếu xuất hiện ngay khi lớp tối ưu có ràng buộc bất đẳng thức như trong cvxpylayers.

## 2. Vector hỗ trợ của SVM dưới góc nhìn KKT

Ví dụ trong mục [12-04]({% multilang_post_url contents/chapter12/21-04-02-12_04_Example_support_vector_machines %}) có ý nghĩa trực tiếp trong thực hành. Điều kiện bù yếu cho biết các điểm có $$0<\alpha_i<C$$ nằm đúng trên lề, các điểm có $$\alpha_i=0$$ được phân loại đúng và nằm ngoài vùng lề (không có sai số vi phạm), còn các điểm có $$\alpha_i=C$$ là các vector hỗ trợ chạm giới hạn trên (nằm trong lề hoặc bị phân loại sai). Trong giai đoạn 2022–2026, SVM nhân (kernel SVM) vẫn là công cụ phổ biến trong học máy khoa học cỡ mẫu $$n$$ nhỏ (như hóa tin học, dữ liệu điện não đồ EEG, dữ liệu lâm sàng dạng bảng) chính vì mô hình chỉ phụ thuộc vào tập hữu hạn các vector hỗ trợ này. Khi một bài báo nêu mô hình có “47 vector hỗ trợ”, con số đó chính là kích thước tập ràng buộc tích cực (active set) của hệ KKT.

## 3. Giá biên theo vị trí (LMP) trong thị trường điện và điều kiện bù

Giá biên theo vị trí (Locational Marginal Price — LMP) là các biến đối ngẫu ứng với ràng buộc cân bằng công suất và giới hạn truyền tải đường dây (Chương 10). Liang và Dvorkin (2023) sử dụng tối ưu hóa ngược trên dữ liệu LMP công bố để khôi phục giá chào bán của các nhà máy điện; phép khôi phục này thực hiện được vì tại điểm cân bằng không suy biến, hệ KKT xác định rõ ràng buộc bất đẳng thức nào đang chặt. Donti, Rolnick và Kolter (2021) huấn luyện phương pháp DC3 sao cho đầu ra của mạng nơ-ron được hiệu chỉnh về điểm khả thi KKT của bài toán trào lưu công suất tối ưu (OPF). Thuật toán water-filling trong [12-03]({% multilang_post_url contents/chapter12/21-04-02-12_03_Example_water_filling %}) cũng mang cấu trúc điều kiện bù tương tự trên kênh nhiễu Gauss; các nghiên cứu phân bổ công suất cho mạng 5G/6G vẫn biểu diễn mực nước như nhân tử đối ngẫu của ràng buộc tổng công suất.

## 4. Tính công bằng trong học máy: nhận diện ràng buộc nhóm đang chặt

Trong khung công cụ Fairlearn theo cách tiếp cận quy giảm (Weerts và cộng sự, 2023), một nhân tử Lagrange có giá trị lớn gắn với tiêu chí equalised odds của nhóm $$a$$ cho thấy ràng buộc tỷ lệ lỗi của nhóm đó **đang chặt** — đây chính là ý nghĩa trực tiếp của điều kiện bù yếu. Ngược lại, nhân tử bằng không cho thấy mô hình không ràng buộc đã tự thỏa mãn tiêu chí đó (hoặc ràng buộc không còn tác động biên). Vì vậy, việc quan sát cặp nghiệm $$(x^\star,v^\star)$$ đóng vai trò như một công cụ chẩn đoán: nó chỉ ra ràng buộc xã hội–kỹ thuật nào đang tạo ra chi phí đánh đổi lớn nhất, thay vì chỉ cho biết hàm Lagrangian đã đạt cực tiểu.

## Tóm tắt

Hệ KKT là tập điều kiện bậc nhất giúp: (i) đặc trưng nghiệm tối ưu của bài toán lồi có ràng buộc, (ii) lấy vi phân ẩn để huấn luyện các lớp tối ưu trong mạng học sâu, và (iii) gán giá biên cho các tài nguyên bị giới hạn. Khi các nghiên cứu hiện đại đề cập đến việc nhúng QP vào mạng nơ-ron, báo cáo số lượng vector hỗ trợ hay công bố giá điện LMP, nền tảng toán học chung đằng sau đều là hệ KKT.

**Câu hỏi gợi mở:** Vì sao phép lấy vi phân ẩn qua hệ KKT đòi hỏi điều kiện ràng buộc (constraint qualification) và ma trận Jacobian KKT không suy biến? Điều gì xảy ra trong một lớp Lasso khi hai đặc trưng trùng hệt nhau?

## Nguồn

- Agrawal, A., Amos, B., Barratt, S., Boyd, S., Diamond, S., & Kolter, J. Z. (2019). Differentiable convex optimization layers. *NeurIPS*. Thư viện: [cvxpylayers](https://www.cvxpylayers.org/)
- Pineda, L., Fan, T., Monge, M., Venkataraman, S., Sodhi, P., Chen, R. T. Q., Ortiz, J., DeTone, D., Wang, A., Anderson, S., Dong, J., Amos, B., & Mukadam, M. (2022). Theseus: A library for differentiable nonlinear optimization. *NeurIPS*. [arXiv:2207.09442](https://arxiv.org/abs/2207.09442)
- Liang, Z., & Dvorkin, Y. (2023). Data-driven inverse optimization for marginal offer price recovery in electricity markets. *ACM e-Energy ’23*.
- Donti, P. L., Rolnick, D., & Kolter, J. Z. (2021). DC3: A learning method for optimization with hard constraints. *ICLR*.
- Weerts, H., Dudík, M., Edgar, R., Jalali, A., Lutz, R., & Madaio, M. (2023). Fairlearn: Assessing and improving fairness of AI systems. *JMLR*, 24(257).
