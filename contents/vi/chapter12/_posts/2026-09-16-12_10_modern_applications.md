---
layout: post
title: 12-10 Ứng dụng hiện đại của điều kiện KKT
chapter: '12'
order: 11
owner: Nguyen Le Linh
categories:
- chapter12
lang: vi
lesson_type: optional
---

Trong kỹ thuật hệ thống năng lượng và kinh tế học hiện đại, một trong những minh chứng rõ rệt nhất về sức mạnh thực tiễn của **điều kiện bù KKT** là hiện tượng *tách giá điện theo vùng địa lý* (Locational Marginal Pricing — LMP). Tại sao điện sản xuất ở một tỉnh gió nắng dồi dào có thể chỉ tốn 20 USD/MWh, nhưng cách đó vài trăm km tại trung tâm đô thị, giá điện bán buôn cùng thời điểm lại vọt lên 60 USD/MWh?

Câu trả lời nằm gọn trong một dấu bất đẳng thức: **đường dây truyền tải nối hai vùng đã chạm trần công suất tối đa**! Khi ràng buộc công suất đường dây còn lỏng ($$|f| < F_{\max}$$), điều kiện bù KKT ép nhân tử nghẽn $$\mu^* = 0$$ và giá điện ở hai vùng bằng hệt nhau; nhưng ngay giây phút dòng điện chạm trần $$f = F_{\max}$$, nhân tử KKT $$\mu^*$$ bật dương và chênh lệch giá giữa hai vùng bằng **chính xác $$\mu^*$$**! Bài đọc tổng kết ứng dụng cuối Chương 12 này kết nối hệ điều kiện KKT với 4 lĩnh vực mũi nhọn giai đoạn 2022–2026: tầng tối ưu khả vi, SVM, giá điện LMP và học máy công bằng.

## Kiến thức cần nhớ: Bốn góc nhìn công nghiệp về điều kiện KKT

- **Điều kiện bù trong vận hành lưới điện (LMP & Congestion Rent):** Nhân tử KKT của phương trình cân bằng công suất tại nút $$i$$ là giá biên $$\text{LMP}_i$$; nhân tử KKT $$\mu_{ij}^* \ge 0$$ của giới hạn nhiệt đường dây $$(i, j)$$ chỉ dương khi đường dây nghẽn, tạo ra chênh lệch $$\text{LMP}_j - \text{LMP}_i = \mu_{ij}^*$$.
- **Lấy vi phân ẩn xuyên qua bộ giải tối ưu (`cvxpylayers`, `Theseus`):** Biến hệ KKT thành phương trình hàm ẩn giúp lan truyền ngược gradient xuyên qua các bài toán tối ưu lồi nhúng trong mạng nơ-ron.
- **Định danh vector hỗ trợ và giải thích mô hình (SVM):** Chỉ những điểm dữ liệu có ràng buộc biên chặt ($$\alpha_i^* > 0$$) mới tham gia tạo nên siêu phẳng phân tách.
- **Phát hiện nút thắt công bằng (Active Fairness Constraints):** Trong học máy có ràng buộc công bằng nhóm, nhân tử KKT $$u_g^* > 0$$ chỉ ra chính xác nhóm nhân khẩu học nào đang bị ràng buộc chặt và kéo giảm mục tiêu chính.

### Giải thích: Tính tay giá điện LMP trên lưới 2 nút bị nghẽn đường dây

Xét lưới điện gồm 2 nút nối bởi một đường dây có giới hạn truyền tải $$F_{\max} = 50$$ MWh:
- Nút 1 có nhà máy giá rẻ $$20$$ USD/MWh (công suất đủ lớn), nhu cầu tại nút 1 bằng $$0$$.
- Nút 2 có nhà máy đắt $$60$$ USD/MWh, nhu cầu tại nút 2 là $$D_2 = 80$$ MWh.
- Gọi $$p_1, p_2 \ge 0$$ là công suất phát tại hai nút và $$f$$ là dòng truyền từ nút 1 sang nút 2 ($$f \le 50$$).

1. **Lập bài toán tối ưu và hàm Lagrangian:**
   $$\min_{p_1, p_2, f} \; 20 p_1 + 60 p_2 \quad \text{s.t.} \quad \begin{cases} p_1 - f = 0 & (\text{giá nút 1: } \lambda_1) \\ p_2 + f = 80 & (\text{giá nút 2: } \lambda_2) \\ f - 50 \le 0 & (\text{phí nghẽn: } \mu \ge 0) \end{cases}$$
   Dễ thấy phương án rẻ nhất là đẩy tối đa $$f^* = 50$$ MWh từ nút 1 sang nút 2 ($$p_1^* = 50$$) và phát nốt $$p_2^* = 30$$ MWh tại nút 2.
2. **Giải 3 phương trình dừng KKT theo $$p_1, p_2, f$$:**
   - Theo $$p_1$$: $$20 - \lambda_1^* = 0 \implies \lambda_1^* = 20$$ USD/MWh.
   - Theo $$p_2$$: $$60 - \lambda_2^* = 0 \implies \lambda_2^* = 60$$ USD/MWh.
   - Theo $$f$$: $$\lambda_1^* - \lambda_2^* + \mu^* = 0 \implies \mu^* = \lambda_2^* - \lambda_1^* = 60 - 20 = 40$$ USD/MWh!
3. **Kiểm chứng điều kiện bù KKT:** Vì đường dây chạm trần ($$f^* - 50 = 0$$), $$\mu^* = 40 > 0$$ hoàn toàn hợp lệ! Ngược lại, nếu đường dây được nâng cấp lên $$F_{\max} = 100$$ MWh (ràng buộc lỏng $$80 < 100$$), điều kiện bù ép $$\mu^* = 0$$ và lập tức $$\lambda_1^* = \lambda_2^* = 20$$ USD/MWh — giá điện toàn lưới giảm đồng loạt về mức rẻ nhất!

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
