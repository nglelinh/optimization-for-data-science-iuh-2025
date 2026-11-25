---
layout: post
title: 24-06 Ứng dụng hiện đại của mô hình nguyên hỗn hợp
chapter: '24'
order: 7
owner: Nguyen Le Linh
categories:
- chapter24
lang: vi
lesson_type: optional
---

Nhiều người lầm tưởng rằng khi học sâu và mạng nơ-ron lên ngôi, quy hoạch số nguyên hỗn hợp (MIP) sẽ dần lùi vào dĩ vãng. Thực tế giai đoạn 2020–2026 lại cho thấy điều hoàn toàn ngược lại: **học máy và MIP đang trở thành cặp bài trùng không thể tách rời**. Mạng nơ-ron cực giỏi trong việc dự báo nhu cầu giao hàng hay thời gian di chuyển từ dữ liệu nhiễu, nhưng nó không thể tự đảm bảo các ràng buộc vận hành bắt buộc như "mỗi phi công nghỉ đủ 12 giờ" hay "tải trọng xe không vượt quá $$Q$$".

Ngược lại, chính học máy cũng đang quay vào *bên trong* bộ giải MIP — thông qua mạng nơ-ron đồ thị (GNN) học cách chọn biến rẽ nhánh trong cuộc thi ML4CO — để tăng tốc vòng lặp nhánh và cận cho các bài toán lặp đi lặp lại mỗi ngày trong công nghiệp.

## Kiến thức cần nhớ: Bốn trụ cột kết nối MIP cổ điển với AI hiện đại

Bài đọc ứng dụng này giúp bạn nhìn thấy vị trí thực tế của bốn mô hình Chương 24 trong hệ thống công nghiệp ngày nay:

- **Kiến trúc "Predict-then-Optimize" (Dự báo rồi Tối ưu):** Trong giao hàng chặng cuối và điện toán biên, mô hình ML ước lượng tham số bất định (thời gian đi lại, lưu lượng người dùng), còn bộ giải MIP biến dự báo đó thành quyết định khả thi 100% dưới mọi ràng buộc cứng.
- **Biểu diễn Đồ thị Hai phía Biến–Ràng buộc (Bipartite Graph Representation):** Mọi bài toán MILP đều tương ứng với một đồ thị hai phía nối mỗi biến $$x_j$$ với các ràng buộc $$i$$ mà nó tham gia (trọng số cạnh là hệ số $$A_{ij}$$). Đây chính là cầu nối cho phép GNN "đọc" được bài toán tối ưu mà không phụ thuộc vào thứ tự đánh số biến.
- **Bắt chước Rẽ nhánh Mạnh (Imitating Strong Branching):** *Strong branching* chọn biến rẽ nhánh cực kỳ thông minh nhưng quá chậm vì phải giải thử hàng trăm LP ở mỗi nút. GNN được huấn luyện để bắt chước quyết định của strong branching trong vài mili-giây.
- **Tính đơn mô-đun toàn phần vs. Ràng buộc thực tế:** Bài toán phân công thuần túy có nghiệm LP tự động nguyên (định lý Birkhoff–von Neumann), nhưng chỉ cần thêm một ràng buộc ca trực hay ngân sách thực tế, cấu trúc đẹp ấy vỡ ngay và MIP thực thụ lập tức cần thiết.

### Giải thích: Tính tay bài toán đặt cụm GPU biên (Edge Facility Location)

Giả sử một nền tảng AI cần phục vụ 2 khu vực người dùng (Vùng 1 và Vùng 2) bằng cách mở cụm GPU tại tối đa 2 vị trí ứng viên (Vị trí A và Vị trí B):
- Chi phí cố định để thuê hạ tầng mỗi ngày: $$f_A = 10$$, $$f_B = 8$$ (đơn vị triệu đồng).
- Chi phí độ trễ và truyền dữ liệu $$c_{ij}$$ khi phục vụ Vùng $$i$$ từ Vị trí $$j$$:
  $$c_{1A} = 2,\; c_{1B} = 6,\qquad c_{2A} = 5,\; c_{2B} = 2.$$

Mô hình MIP là $$\min \sum_{j \in \{A, B\}} f_j y_j + \sum_{i=1}^2 \sum_{j \in \{A, B\}} c_{ij} x_{ij}$$ với $$x_{iA} + x_{iB} = 1$$ và $$x_{ij} \le y_j$$, $$y_j \in \{0, 1\}$$.

1. **Phương án 1 — Chỉ mở Vị trí A ($$y_A = 1, y_B = 0$$):**
   Cả hai vùng bắt buộc định tuyến về A ($$x_{1A} = x_{2A} = 1$$).
   Tổng chi phí: $$10 + (2 + 5) = 17$$.
2. **Phương án 2 — Chỉ mở Vị trí B ($$y_A = 0, y_B = 1$$):**
   Cả hai vùng định tuyến về B ($$x_{1B} = x_{2B} = 1$$).
   Tổng chi phí: $$8 + (6 + 2) = 16$$.
3. **Phương án 3 — Mở cả hai vị trí ($$y_A = 1, y_B = 1$$):**
   Mỗi vùng chọn vị trí gần mình nhất ($$x_{1A} = 1, x_{2B} = 1$$) để giảm chi phí truyền xuống còn $$2 + 2 = 4$$, nhưng chi phí cố định tăng lên $$10 + 8 = 18$$.
   Tổng chi phí: $$18 + 4 = 22$$.
4. **Quyết định tối ưu:** Chỉ mở Vị trí B (tổng chi phí **$$16$$**). Dù Vùng 1 chịu độ trễ cao hơn ($$6$$ thay vì $$2$$), mức tiết kiệm chi phí hạ tầng cố định đã bù đắp vượt trội — chính sự đánh đổi định lượng này là lý do MIP giữ vai trò xương sống trong thiết kế mạng lưới kho vận và đám mây!

Chương 24 tập trung vào phần *mô hình hóa* của quy hoạch nguyên hỗn hợp (MIP): biến quyết định nhị phân, phân công, bài toán cái túi và đặt cơ sở. Các khuôn mẫu này vẫn được sử dụng trực tiếp trong nhiều hệ thống thực tế như xếp lịch phi hành đoàn, định tuyến giao hàng chặng cuối (last-mile) và lựa chọn vị trí kho hàng hay cụm GPU biên. Từ khoảng năm 2019, một hướng nghiên cứu mới còn hình thành xung quanh chúng: **học để tối ưu (learning to optimize)** — dùng mạng nơ-ron đồ thị (GNN) để đề xuất biến rẽ nhánh, mặt phẳng cắt hoặc điểm khởi động nóng cho bộ giải MIP. Bài đọc tùy chọn này điểm qua bốn ứng dụng tiêu biểu; các chủ đề mặt phẳng cắt, chọn tập con tốt nhất và kiểm chứng mạng nơ-ron sẽ được trình bày ở [Chương 25]({% multilang_post_url contents/chapter25/21-03-28-25_Mixed_integer_programming %}).

## 1. Xếp lịch phi hành đoàn hàng không

Bài toán ghép cặp chuyến bay và xếp lịch phi hành đoàn là một quy hoạch nguyên với các ràng buộc chặt về giờ trực, thời gian nghỉ và cấu hình đội bay. Bộ dữ liệu chuẩn công khai **air05** trong MIPLIB 2017 (Gleixner, Hendel, Gamrath và cộng sự, *Math. Prog. Comput.* 13:443–490, 2021, [doi:10.1007/s12532-020-00194-3](https://doi.org/10.1007/s12532-020-00194-3)) vẫn được dùng để đánh giá các chiến lược rẽ nhánh mới. Một nghiên cứu giải thích năm 2025 (biểu diễn bài toán xếp lịch `air05` dưới dạng đồ thị hai phía biến–ràng buộc; [arXiv:2512.01698](https://arxiv.org/abs/2512.01698)) đặt ra câu hỏi gắn trực tiếp với Chương 24: sau khi mô hình hóa bài toán thành MIP, liệu phép nhúng đồ thị bằng GNN có đủ tốt để thay thế các đặc trưng thủ công trong bộ giải hay không? Trong quy trình đó, MIP không bị thay thế mà đóng vai trò *nguồn sinh nhãn* cho hệ thống học máy.

## 2. Phân công và định tuyến giao hàng chặng cuối

Bài toán phân công ở mục 24-02 là khối con cốt lõi trong nhiều hệ thống logistics hiện đại. Giao hàng chặng cuối và điều phối giao đồ ăn theo yêu cầu thường được mô hình hóa dưới dạng MIP định tuyến phương tiện (hoặc MIP kết hợp sinh cột) với ràng buộc khung thời gian và ca làm việc của tài xế. Chuyên khảo *Vehicle Routing* của Toth và Vigo là tài liệu nền tảng cho hướng này; cách triển khai phổ biến trong thập niên 2020 là dùng mô hình học có giám sát để *dự báo* thời gian di chuyển và nhu cầu, rồi đưa các tham số đó vào bộ giải MIP để xuất ra lộ trình khả thi trong vài phút. Mô hình học máy đảm nhận phần dự báo từ dữ liệu, còn quy hoạch nguyên đảm bảo các ràng buộc cứng (“một tài xế, một xe, tải trọng tối đa $$Q$$”) mà mạng nơ-ron không tự đảm bảo được. Cách phân tách trách nhiệm — học những quy luật khó viết công thức và tối ưu những ràng buộc cần chứng nhận chặt — là kiến trúc phổ biến kết hợp vận trù học và học máy hiện nay.

## 3. Đặt cơ sở cho kho vận và điện toán biên

Bài toán đặt cơ sở (cũng ở mục 24-02) là khung mô hình để quyết định mở trung tâm hoàn tất đơn hàng (fulfillment center), nút bộ nhớ đệm hay **điểm suy luận GPU biên**. Biến nhị phân $$y_j$$ quyết định việc mở địa điểm $$j$$ với chi phí cố định $$f_j$$, còn biến luồng liên tục (hoặc nguyên) $$x_{ij}$$ phân bổ nhu cầu từ vùng $$i$$ sang địa điểm $$j$$. Nhiều nghiên cứu về điện toán đám mây và học máy biên giữ nguyên cấu trúc này, với $$f_j$$ là chi phí hạ tầng máy chủ hoặc bản quyền và $$c_{ij}$$ là độ trễ hay chi phí truyền dữ liệu ra ngoài (egress). Mô hình MIP giữ nguyên, chỉ khác ở chỗ dữ liệu đầu vào trong hàm mục tiêu đến từ mô hình dự báo nhu cầu.

## 4. Học quy tắc rẽ nhánh và cuộc thi ML4CO

Gasse, Chételat, Ferroni, Charlin và Lodi (*Exact Combinatorial Optimization with Graph Convolutional Neural Networks*, NeurIPS 2019) huấn luyện mạng nơ-ron tích chập đồ thị để bắt chước chiến lược rẽ nhánh mạnh (strong branching). Cuộc thi NeurIPS 2021 **ML4CO** (Ecole và cộng sự) chuẩn hóa hướng này thành các bài toán đánh giá công khai cho việc học heuristic gốc, tinh chỉnh cấu hình và chọn biến rẽ nhánh trên các họ MIP. Các nghiên cứu giai đoạn 2024–2025 tiếp tục mở rộng sang học *chuỗi mặt phẳng cắt* và thử nghiệm bộ giải học tăng cường đầu–cuối (sẽ đề cập thêm ở Chương 25). Điểm cốt lõi cần ghi nhớ là: trong thực tế, ứng dụng MIP thường xuất hiện dưới dạng một *phân phối* các bài toán cùng họ, và mô hình học máy hoạt động *bên trong* vòng lặp nhánh và cận của mục 24-05 chứ không thay thế các ràng buộc nguyên.

**Bài tập.** Lấy mô hình bài toán phân công từ mục 24-02 với $$n=8$$ và ma trận chi phí ngẫu nhiên. Giải bài toán bằng hai cách: (i) dùng bộ giải MIP hoặc `scipy.optimize.linear_sum_assignment`; và (ii) giải bài toán nới lỏng LP với $$x_{ij}\in[0,1]$$ rồi làm tròn. Quan sát số lần nghiệm nới lỏng LP tự động là nghiệm nguyên (định lý Birkhoff–von Neumann đảm bảo điều này *luôn* đúng cho bài toán phân công thuần). Sau đó thêm một ràng buộc bổ sung (chẳng hạn ràng buộc “người 1 không làm các công việc 1–3” hoặc thêm ràng buộc ghép cặp/ngân sách) để quan sát sự khác biệt giữa bài toán phân công chuẩn trong sách giáo khoa và bài toán MIP xếp lịch thực tế.

## Nguồn

- A. Gleixner et al., *MIPLIB 2017*, *Math. Prog. Comput.* 13:443–490, 2021.
- M. Gasse, D. Chételat, N. Ferroni, L. Charlin, A. Lodi, NeurIPS 2019 — rẽ nhánh GNN.
- A. Prouvost, A. Chowdhury, et al. / Ecole et al., cuộc thi NeurIPS 2021 ML4CO.
- P. Toth and D. Vigo (eds.), *Vehicle Routing: Problems, Methods, and Applications*, SIAM, 2nd ed., 2014.
- D. Bertsimas and J. Tsitsiklis, *Introduction to Linear Optimization* — gán và định vị cơ sở như xương sống mô hình.
- Nhúng GNN air05, [arXiv:2512.01698](https://arxiv.org/abs/2512.01698), 2025 — xếp kíp như instance học đồ thị.
