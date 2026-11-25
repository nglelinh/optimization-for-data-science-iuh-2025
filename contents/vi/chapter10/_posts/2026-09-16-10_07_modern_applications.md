---
layout: post
title: 10-07 Ứng dụng hiện đại của đối ngẫu LP
chapter: '10'
order: 8
owner: Nguyen Le Linh
categories:
- chapter10
lang: vi
lesson_type: optional
redirect_from:
  - /contents/vi/chapter10/10_09_modern_applications/
---

Quy hoạch tuyến tính và tính đối ngẫu của nó đã gần 80 tuổi, nhưng giai đoạn 2022–2026 lại chứng kiến một cuộc "hồi sinh rực rỡ" của đối ngẫu LP trong những bài toán tiên phong nhất của trí tuệ nhân tạo và khoa học dữ liệu. Từ việc **chứng nhận an toàn cho mạng nơ-ron sâu** (khẳng định không tồn tại bất kỳ nhiễu đối kháng nào đánh lừa được mô hình), định giá điện năng theo thời gian thực trên lưới điện quốc gia, cho tới bài toán vận chuyển tối ưu (Optimal Transport / khoảng cách Wasserstein) so sánh hai phân phối xác suất trong mô hình sinh — tất cả đều chạy dựa trên cặp Primal–Dual LP!

Điểm mấu chốt khiến đối ngẫu LP trở nên bất khả chiến bại trong các ứng dụng kiểm chứng an toàn là **tính đối ngẫu yếu**: ngay cả khi bạn không có đủ thời gian giải bài toán LP hàng triệu biến tới nghiệm chính xác tuyệt đối, *bất kỳ nghiệm đối ngẫu khả thi nào* cũng đã cung cấp ngay một **chứng chỉ cận dưới toán học 100% chặt chẽ**!

## Kiến thức cần nhớ: Bốn miền ứng dụng hiện đại của đối ngẫu LP (2022–2026)

- **Kiểm chứng mạng nơ-ron (Neural Network Verification — $$\alpha,\beta$$-CROWN):** Nới lỏng hàm kích hoạt phi tuyến ReLU $$y = \max(0, x)$$ trên đoạn $$[l, u]$$ thành một tam giác lồi (Planet relaxation) biến bài toán kiểm chứng thành LP; giải bài toán đối ngẫu trên GPU cho ra cận dưới an toàn chỉ trong vài mili-giây!
- **Thị trường điện và giá bóng theo nút (Locational Marginal Pricing — LMP):** Bộ điều độ lưới điện giải LP điều phối công suất phát (DC-OPF) mỗi 5 phút; biến đối ngẫu của ràng buộc cân bằng cung–cầu tại mỗi nút lưới chính là giá điện bán buôn tại địa điểm đó!
- **Luồng cực đại – lát cắt cực tiểu thời gian gần tuyến tính:** Đột phá lý thuyết năm 2022 (Chen–Kyng–Liu–Peng–Probst Gutenberg–Sachdeva) giải Max Flow và Min-Cost Flow trong thời gian gần tuyến tính $$m^{1+o(1)}$$ nhờ kết hợp phương pháp điểm trong với cấu trúc dữ liệu động trên cặp Primal–Dual.
- **Vận chuyển tối ưu (Optimal Transport / Earth Mover's Distance):** Bài toán Kantorovich tìm kế hoạch vận chuyển khối lượng xác suất rẻ nhất là một LP khổng lồ, còn bài toán đối ngẫu Kantorovich–Rubinstein chính là nền tảng của WGAN và các thước đo khoảng cách phân phối hiện đại.

### Giải thích: Tính tay nới lỏng tam giác LP cho một nơ-ron ReLU

Trong kiểm chứng mạng nơ-ron, giả sử đầu vào $$x$$ của một nút ReLU $$y = \max(0, x)$$ bị chặn trong đoạn $$[l, u] = [-1, 2]$$ (trạng thái không ổn định vì $$l < 0 < u$$).

1. **Dựng ba ràng buộc tuyến tính bao quanh đồ thị gấp khúc $$y = \max(0, x)$$ trên $$[-1, 2]$$:**
   - Hai cạnh dưới (nằm dưới chữ V): $$y \ge 0$$ và $$y \ge x$$.
   - Một cạnh trên nối hai đầu mút $$(-1, 0)$$ và $$(2, 2)$$:
     $$y \le \frac{u}{u - l}(x - l) = \frac{2}{2 - (-1)}(x + 1) = \frac{2}{3}x + \frac{2}{3}.$$
2. **Kiểm tra độ chặt tại ba điểm mốc:**
   - Tại $$x = -1$$: $$0 \le y \le \frac{2}{3}(-1 + 1) = 0 \implies y = 0$$ (khớp chính xác!).
   - Tại $$x = 2$$: $$2 \le y \le \frac{2}{3}(3) = 2 \implies y = 2$$ (khớp chính xác!).
   - Tại điểm gãy $$x = 0$$: $$0 \le y \le \frac{2}{3}$$ (chấp nhận khoảng nới lỏng tối đa $$\frac{2}{3}$$ để đổi lấy tính tuyến tính!).
3. **Vai trò của đối ngẫu LP:** Bằng cách gán biến đối ngẫu cho 3 ràng buộc tam giác này ở mọi nơ-ron, các trình kiểm chứng như CROWN lan truyền ngược chứng chỉ cận dưới qua toàn bộ mạng nơ-ron mà không cần chạy thuật toán đơn hình chậm chạp!

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
