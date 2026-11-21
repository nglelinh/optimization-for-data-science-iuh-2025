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


Chương 24 là nửa *mô hình hóa* của quy hoạch nguyên hỗn hợp: quyết định nhị phân, gán, knapsack, và định vị cơ sở. Những khuôn đó không ở lại sách giáo khoa. Xếp kíp bay, định tuyến last-mile, và đặt kho hay site GPU biên vẫn được giải như MIP, và từ khoảng 2019 một ngành thứ hai lớn lên quanh chúng: **học để tối ưu** — mạng nơ-ron đồ thị đề xuất nhánh, cắt, hoặc khởi động nóng cho bộ giải MIP. Ghi chú tùy chọn này là bốn ứng dụng hướng khoa học dữ liệu. Mặt phẳng cắt, chọn tập con tốt nhất, và kiểm chứng mạng nơ-ron chờ [Chương 25]({% multilang_post_url contents/chapter25/21-03-28-25_Mixed_integer_programming %}).

## 1. Xếp kíp hàng không, vẫn là MIP sống

Ghép ca / xếp lịch kíp là quy hoạch nguyên với ràng buộc trực, nghỉ, và đội tàu. Instance công khai **air05** trong MIPLIB 2017 (Gleixner, Hendel, Gamrath, et al., *Math. Prog. Comput.* 13:443–490, 2021, [doi:10.1007/s12532-020-00194-3](https://doi.org/10.1007/s12532-020-00194-3)) là instance mà mọi heuristic rẽ nhánh mới vẫn bị đo. Một nghiên cứu giải thích 2025 (air05 xếp kíp như đồ thị hai phía biến–ràng buộc; [arXiv:2512.01698](https://arxiv.org/abs/2512.01698)) hỏi một câu khoa học dữ liệu mà Chương 24 đã chuẩn bị: một khi bạn *mô hình* MIP, một GNN nhúng đồ thị đó đủ tốt để thay đặc trưng bộ giải viết tay không? MIP không biến mất; nó trở thành *máy sinh nhãn* cho một pipeline học.

## 2. Gán và định tuyến last-mile

Bài toán gán ở 24-02 là oracle tuyến tính bên trong rất nhiều logistics hiện đại. Giao hàng last-mile và định tuyến đồ ăn theo yêu cầu là MIP định tuyến xe (hoặc MIP + sinh cột) với cửa sổ thời gian và ca tài xế. Chuyên khảo *Vehicle Routing* của Toth và Vigo là tài liệu cổ điển; nếp 2020s là thời gian đi và nhu cầu được *dự báo* bởi mô hình có giám sát, rồi đưa vào MIP phải trả về tuyến khả thi trong vài phút. Nhà khoa học dữ liệu sở hữu dự báo; quy hoạch nguyên sở hữu logic “một tài xế, một xe, sức chứa $$Q$$” mà mạng nơ-ron sẽ vui vẻ vi phạm. Sự tách đó — học cái bạn không viết được, tối ưu cái bạn phải chứng nhận — là mặc định 2026 trong vận hành + ML.

## 3. Định vị cơ sở cho kho và tính toán biên

Định vị cơ sở (cũng 24-02) là cách nền tảng quyết định mở fulfillment center, cache, hoặc **site suy luận GPU** nào. Nhị phân $$y_j$$ mở site $$j$$ với chi phí $$f_j$$; dòng liên tục (hoặc nguyên) $$x_{ij}$$ gửi nhu cầu $$i$$ tới $$j$$. Các bài báo cloud và edge-ML tái sử dụng đúng bộ xương này: $$f_j$$ là chi phí rack / giấy phép, $$c_{ij}$$ là độ trễ hoặc egress. MIP giống nhau; “dữ liệu” trong mục tiêu là mặt nhu cầu học được. Nếu viết được công thức 24-02, bạn đọc được những bài đó.

## 4. Học rẽ nhánh và cuộc thi ML4CO

Gasse, Chételat, Ferroni, Charlin và Lodi, *Exact Combinatorial Optimization with Graph Convolutional Neural Networks*, NeurIPS 2019, dạy GNN bắt chước chuyên gia strong branching. Cuộc thi NeurIPS 2021 **ML4CO** (Ecole et al.) biến ý tưởng đó thành chuẩn công khai: học heuristic gốc, cấu hình, hoặc rẽ nhánh trên các họ MIP. Các bài theo 2024–2025 học *chuỗi cắt* và thậm chí thử bộ giải RL đầu-cuối; những cái đó thuộc Chương 25 hơn (mặt phẳng cắt) và được trích ở đó. Với chương này, nhớ một câu: một ứng dụng MIP hiện đại thường là một *phân phối* instance, và một mô hình khoa học dữ liệu ngồi *bên trong* vòng branch-and-bound của 24-05, nó không thay ràng buộc nguyên.

**Bài tập.** Lấy công thức gán từ 24-02 với $$n=8$$ chi phí ngẫu nhiên. Giải (i) bằng bộ giải MIP hoặc `scipy.optimize.linear_sum_assignment` và (ii) bằng nới $$x_{ij}\in[0,1]$$ rồi làm tròn. Đếm bao nhiêu lần nới LP đã nguyên (Birkhoff–von Neumann nói *luôn* với gán thuần — đó là điểm). Rồi thêm một bất đẳng thức, “người 1 không làm việc 1–3,” và xem nới cần rẽ nhánh. Sửa nhỏ đó là khoảng cách giữa gán sách giáo khoa và MIP ghép kíp.

## Nguồn

- A. Gleixner et al., *MIPLIB 2017*, *Math. Prog. Comput.* 13:443–490, 2021.
- M. Gasse, D. Chételat, N. Ferroni, L. Charlin, A. Lodi, NeurIPS 2019 — rẽ nhánh GNN.
- A. Prouvost, A. Chowdhury, et al. / Ecole et al., cuộc thi NeurIPS 2021 ML4CO.
- P. Toth and D. Vigo (eds.), *Vehicle Routing: Problems, Methods, and Applications*, SIAM, 2nd ed., 2014.
- D. Bertsimas and J. Tsitsiklis, *Introduction to Linear Optimization* — gán và định vị cơ sở như xương sống mô hình.
- Nhúng GNN air05, [arXiv:2512.01698](https://arxiv.org/abs/2512.01698), 2025 — xếp kíp như instance học đồ thị.
