---
layout: post
title: 10-10 Ứng dụng hiện đại của đối ngẫu LP
chapter: '10'
order: 11
owner: Nguyen Le Linh
categories:
- chapter10
lang: vi
lesson_type: optional
---

Nếu có ai hỏi *"Học biến đối ngẫu và giá bóng LP để làm gì ngoài đời?"*, hãy kể cho họ nghe về hóa đơn tiền điện mỗi tháng. Trên các thị trường điện hiện đại như PJM, ERCOT hay châu Âu, cứ mỗi 5 đến 15 phút, một bài toán quy hoạch tuyến tính khổng lồ lại được giải để quyết định nhà máy điện nào phát bao nhiêu megawatt sao cho chi phí toàn hệ thống thấp nhất mà không làm quá tải bất kỳ đường dây truyền tải nào. Và con số quyết định giá mua bán điện tại từng khu vực không phải do ai đoán mò — nó chính là **nghiệm đối ngẫu (giá bóng)** của ràng buộc cân bằng cung–cầu!

Bài đọc tổng kết ứng dụng cuối chương này kết nối trực tiếp lý thuyết đối ngẫu LP của Chương 10 với bốn lĩnh vực mũi nhọn giai đoạn 2022–2026: kiểm chứng mạng nơ-ron, thị trường năng lượng, thuật toán luồng đồ thị tốc độ gần tuyến tính và vận chuyển tối ưu — giúp bạn nhìn thấy tư duy Primal–Dual đang vận hành thế giới thực như thế nào.

## Bản đồ kiến thức nền: Bốn góc nhìn công nghiệp về sức mạnh của đối ngẫu LP

- **Giá bóng trong kinh tế năng lượng (Market Clearing & Shadow Pricing):** Nghiệm đối ngẫu của ràng buộc $$\sum_g p_g = D$$ đo chính xác chi phí biên để cung cấp thêm 1 MWh điện; khi đường dây truyền tải bị nghẽn (ràng buộc bất đẳng thức chặt), biến đối ngẫu của đường dây trở nên dương và tạo ra chênh lệch giá giữa hai vùng!
- **Chứng chỉ an toàn không cần giải chính xác (Dual Bounds in AI Safety):** Trong bài toán kiểm chứng độ bền vững mạng nơ-ron, bất kỳ điểm khả thi nào của bài toán đối ngẫu LP đều là một cận dưới toán học hợp lệ, cho phép chứng nhận an toàn nhanh gấp hàng nghìn lần giải Primal LP.
- **Đối ngẫu Kantorovich trong học máy phân phối (Optimal Transport):** Thay vì giải LP có $$n^2$$ biến vận chuyển giữa hai đám mây điểm cỡ $$n$$, bài toán đối ngẫu chỉ có $$2n$$ biến thế năng (potentials), giúp tính khoảng cách Wasserstein khả thi trên tập dữ liệu lớn.
- **Thuật toán luồng đồ thị thế hệ mới:** Các bước tiến gần tuyến tính sau 2022 cho bài toán Max Flow / Min-Cost Flow đều khai thác cấu trúc cây khung và phép cập nhật song hành trên cả biến luồng gốc lẫn thế năng đỉnh đối ngẫu.

### Khung giải thích (nên đọc chậm): Tính tay giá điện biên (giá bóng đối ngẫu) cho hệ thống 2 nhà máy

Giả sử lưới điện cần đáp ứng phụ tải $$D = 130$$ MWh bằng 2 nhà máy phát điện:
- Nhà máy 1 (thủy điện): công suất tối đa $$100$$ MWh, chi phí phát $$20$$ USD/MWh.
- Nhà máy 2 (nhiệt điện khí): công suất tối đa $$100$$ MWh, chi phí phát $$50$$ USD/MWh.

1. **Lập và giải bài toán gốc (LP điều phối tối thiểu hóa chi phí):**
   $$\min_{p_1, p_2} \; 20 p_1 + 50 p_2 \quad \text{s.t.} \quad \begin{cases} p_1 + p_2 = 130 & (\text{giá bóng } \lambda \in \mathbb{R}) \\ 0 \le p_1 \le 100 & (\text{phí nghẽn } \mu_1 \ge 0) \\ 0 \le p_2 \le 100 & (\text{phí nghẽn } \mu_2 \ge 0) \end{cases}$$
   Hiển nhiên ta khai thác tối đa nhà máy rẻ trước: $$p_1^* = 100$$ MWh, phần còn lại lấy từ nhà máy đắt: $$p_2^* = 30$$ MWh. Tổng chi phí: $$20(100) + 50(30) = 3{,}500$$ USD.
2. **Đọc ra nghiệm đối ngẫu (giá điện thị trường $$\lambda^*$$ và lợi nhuận nghẽn $$\mu_1^*, \mu_2^*$$):**
   - Nhà máy 2 chưa chạm trần ($$0 < 30 < 100$$) $$\implies$$ theo điều kiện bù, $$\mu_2^* = 0$$ và điều kiện dừng $$50 - \lambda^* + \mu_2^* = 0 \implies \lambda^* = 50$$ USD/MWh!
   - Nhà máy 1 chạm trần ($$p_1^* = 100$$) $$\implies$$ $$20 - \lambda^* + \mu_1^* = 0 \implies \mu_1^* = 50 - 20 = 30$$ USD/MWh!
3. **Kiểm chứng ý nghĩa giá bóng:** Nếu nhu cầu tăng thêm $$1$$ MWh (lên $$131$$ MWh), chỉ nhà máy 2 còn dư công suất nên chi phí hệ thống tăng đúng $$\lambda^* = 50$$ USD; còn nếu mở rộng nhà máy thủy điện thêm $$1$$ MWh (lên $$101$$ MWh), nó thay thế $$1$$ MWh nhiệt điện khí và tiết kiệm cho hệ thống đúng $$\mu_1^* = 30$$ USD!

# Ứng dụng hiện đại của đối ngẫu LP

Chương 10 đã trình bày cách xây dựng bài toán đối ngẫu của quy hoạch tuyến tính, tính đối ngẫu yếu và mạnh, điều kiện bù, cùng hai ví dụ kinh điển là luồng cực đại – lát cắt cực tiểu và trò chơi ma trận. Bài đọc tùy chọn này giới thiệu bốn lĩnh vực trong khoa học máy tính và khoa học dữ liệu giai đoạn 2022–2026 nơi các chứng chỉ đối ngẫu đó được sử dụng trực tiếp.

Với một LP gốc $$\min\{c^\top x:Ax=b,\,Gx\le h\}$$ và bài toán đối ngẫu tương ứng, mọi cặp biến đối ngẫu khả thi $$(u, v)$$ đều tạo thành một **cận dưới** cho giá trị tối ưu gốc; tại điểm tối ưu, cận này đạt dấu bằng và mọi ràng buộc bất đẳng thức không chặt đều có nhân tử đối ngẫu bằng $$0$$.

## 1. Kiểm chứng mạng nơ-ron qua LP và mặt cắt

Bài toán kiểm tra xem một bộ phân loại có bị đổi nhãn trong vùng nhiễu $$\ell_\infty$$ hay không là một bài toán không lồi do các hàm kích hoạt ReLU. Cách nới lỏng tiêu chuẩn là thay mỗi hàm ReLU bằng bao lồi dạng tam giác tuyến tính (Ehlers; Wong và Kolter). Khi đó, các biến đối ngẫu của LP nới lỏng đóng vai trò là **nhân tử lan truyền cận**. Zhang, Wang, Xu, Li, Li, Jana, Hsieh và Kolter (NeurIPS 2022) đã bổ sung **mặt cắt tổng quát** vào bài toán đối ngẫu này (GCP-CROWN) và tích hợp vào công cụ **$$\alpha,\beta$$-CROWN** — hệ thống đứng đầu cuộc thi International Verification of Neural Networks (VNN-COMP) liên tiếp các năm 2021–2025. Phần tính toán hiệu năng cao nằm ở bước lan truyền cận trên GPU, còn chứng chỉ toán học vẫn dựa trên nguyên lý cơ bản: nếu giá trị đối ngẫu của LP đã siết chặt lớn hơn $$0$$, thì không tồn tại ví dụ đối kháng nào trong vùng xét.

Ở đây, tính đối ngẫu yếu của Chương 10 được dùng trực tiếp như một **chứng chỉ an toàn**, chứ không mang ý nghĩa định giá kinh tế.

## 2. Thị trường điện: LP khớp lệnh và giá bóng

Thị trường điện năng ngày tới (day-ahead) vận hành dựa trên một bài toán quy hoạch tuyến tính hỗn hợp nguyên nhằm cực tiểu hóa tổng chi phí chào giá dưới các ràng buộc cân bằng công suất và giới hạn truyền tải đường dây. Biến đối ngẫu của bản nới lỏng tuyến tính tương ứng chính là vector **giá biên theo vị trí** (Locational Marginal Price – LMP). Sau biến động giá năng lượng tại châu Âu năm 2022, các biến đối ngẫu này phản ánh trực tiếp con số trên hóa đơn điện. Liang và Dvorkin (ACM e-Energy 2023) đã sử dụng tối ưu nghịch trên lịch phát điện và dữ liệu LMP công bố để khôi phục mức giá chào của các nhà máy bằng cách giải ngược hệ điều kiện KKT và quan hệ đối ngẫu của LP khớp lệnh. Nhiều nghiên cứu giai đoạn 2022–2023 về đấu giá điện ngày tới ở châu Âu cũng biểu diễn giá theo vùng trực tiếp như biến đối ngẫu của bài toán LP tối đa hóa phúc lợi có ràng buộc lưới truyền tải.

**Liên hệ với giáo trình:** Điều kiện bù khẳng định chỉ những đường dây bị nghẽn ($$Gx = h$$) mới có thành phần giá tắc nghẽn $$v$$ khác $$0$$.

## 3. Bài toán luồng cực đại – lát cắt cực tiểu sau năm 2022

Định lý trong bài [10-03]({% multilang_post_url contents/chapter10/21-03-22-10_03_Max_flow_and_min_cut %}) tiếp tục là cơ sở cho các bài toán phân đoạn ảnh, phát hiện cộng đồng và đánh giá độ tin cậy mạng truyền thông. Các bộ giải quy mô lớn hiện nay (như Gurobi, HiGHS, OR-Tools) đều xuất trực tiếp vector nghiệm đối ngẫu; các quy trình khoa học dữ liệu liên quan đến phân bổ băng thông hay phân tách đồ thị nguồn – đích đều khai thác trực tiếp vector này. Một hướng kết hợp phổ biến gần đây trong khoa học máy tính là học dung lượng cạnh bằng mạng nơ-ron đồ thị (GNN), sau đó đặt bài toán đối ngẫu luồng cực đại cổ điển như một lớp tối ưu bên trong — tương tự tư tưởng tối ưu khả vi ở Chương 12, nhưng bài toán lõi là một LP.

## 4. Vận chuyển tối ưu như một bài toán LP cỡ lớn

Bài toán vận chuyển tối ưu Kantorovich:

$$
\min_{\pi\ge 0}\ \langle C,\pi\rangle\quad\text{s.t.}\quad \pi\mathbf{1}=a,\ \pi^\top\mathbf{1}=b
$$

là một bài toán LP. Bài toán đối ngẫu của nó là $$\max_{f,g} f^\top a + g^\top b$$ với ràng buộc $$f_i + g_j \le C_{ij}$$, trong đó $$(f, g)$$ được gọi là các **thế Kantorovich** (Kantorovich potentials). Chuyên khảo của Peyré và Cuturi (2019) vẫn là tài liệu chuẩn cho các bài toán tính toán vận chuyển tối ưu; các ứng dụng giai đoạn 2022–2026 như thích nghi miền, chưng cất dữ liệu và căn chỉnh dữ liệu đơn bào vẫn giải phiên bản có điều chuẩn (Sinkhorn) hoặc không điều chuẩn, rồi đọc nghiệm đối ngẫu như một ánh xạ ghép mềm. Theo tính đối ngẫu yếu, không có phương án vận chuyển nào có chi phí thấp hơn giá trị của bất kỳ cặp thế khả thi nào.

## Tóm tắt

Đối ngẫu LP đóng vai trò như một **chứng chỉ**: chứng chỉ bất khả thi (trong kiểm chứng mạng nơ-ron), giá biên (trong thị trường điện), lát cắt (trong mạng luồng) hoặc cận chi phí ghép (trong vận chuyển tối ưu). Nếu ta tìm được một nghiệm gốc khả thi và một nghiệm đối ngẫu khả thi có cùng giá trị mục tiêu, bài toán đã được giải tối ưu theo tính đối ngẫu mạnh của LP.

**Câu hỏi tự kiểm tra:** Trong GCP-CROWN, vì sao việc *bổ sung* một mặt cắt hợp lệ vào LP gốc chỉ có thể làm *tăng* (hoặc giữ nguyên) cận dưới đối ngẫu? Kết quả nào trong chương này giải thích điều đó?

## Nguồn

- Zhang, H., Wang, S., Xu, K., Li, L., Li, B., Jana, S., Hsieh, C.-J., & Kolter, J. Z. (2022). General cutting planes for bound-propagation-based neural network verification. *NeurIPS*. [arXiv:2208.05740](https://arxiv.org/abs/2208.05740). Công cụ: [α,β-CROWN](https://github.com/Verified-Intelligence/alpha-beta-CROWN) (vô địch VNN-COMP 2021–2025).
- Liang, Z., & Dvorkin, Y. (2023). Data-driven inverse optimization for marginal offer price recovery in electricity markets. *ACM e-Energy ’23*.
- Peyré, G., & Cuturi, M. (2019). Computational optimal transport. *Foundations and Trends in Machine Learning*, 11(5–6). (tham chiếu LP/đối ngẫu chuẩn vẫn dùng trong pipeline OT 2022–2026)
- Boyd, S., & Vandenberghe, L. (2004). *Convex Optimization*, Ch. 5 (đối ngẫu LP và giá bóng).
