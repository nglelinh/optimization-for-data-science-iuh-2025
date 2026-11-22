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
