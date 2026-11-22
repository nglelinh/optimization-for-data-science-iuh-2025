---
layout: post
title: 25-03 Ứng dụng hiện đại của MIP trong khoa học dữ liệu
chapter: '25'
order: 10
owner: Nguyen Le Linh
categories:
- chapter25
lang: vi
lesson_type: optional
---


Chương 25 tập trung vào phía *bộ giải* của quy hoạch nguyên hỗn hợp: mặt phẳng cắt, thuật toán nhánh và cắt, cùng hai ví dụ thống kê mở rộng (chọn tập con tốt nhất và hồi quy phân vị nhỏ nhất). Trong giai đoạn 2022–2026, các kỹ thuật này tiếp tục được ứng dụng để *chọn đặc trưng* cho mạng nơ-ron, *chứng nhận* độ bền vững đối kháng, *xây dựng cây quyết định tối ưu* và thậm chí *học chiến lược chọn mặt phẳng cắt*. Bài đọc tùy chọn này tổng hợp bốn hướng ứng dụng đó mà không lặp lại phần suy diễn lát cắt Gomory.

## 1. Chọn tập con tốt nhất: ví dụ tiêu biểu của MIP trong thống kê

Bài toán bình phương tối thiểu ràng buộc chuẩn giả $$\ell_0$$ ở mục 25-02-01 có dạng:

$$
\min_\beta\ \tfrac12\|y-X\beta\|_2^2\qquad\text{subject to}\qquad \|\beta\|_0\le k,
$$

có thể viết lại bằng kỹ thuật big-$$M$$ với biến nhị phân $$z_i$$. Bertsimas, King và Mazumder (*Ann. Statist.* 44(2):813–852, 2016) cho thấy các bộ giải MIP hiện đại kết hợp khởi động nóng đã vượt qua quan niệm cũ rằng bài toán này bất khả thi khi $$p>30$$. Bối cảnh so sánh trong thập niên 2020 không còn đơn giản là MIP đối đầu với Lasso: đó là sự cân nhắc giữa MIP, hạ theo tọa độ dọc đường tham số (Chương 23) và các hàm phạt không lồi (`skglm`) ở quy mô hàng trăm đặc trưng, trong đó MIP mang lại *chứng nhận tối ưu* khi khoảng cách cận (MIP gap) khép kín. Trong thực hành, Lasso hoặc elastic net phù hợp cho bước thăm dò nhanh, còn MIP chọn tập con tốt nhất hữu ích khi bài toán yêu cầu chính xác $$k$$ đặc trưng kèm cận dưới tối ưu có chứng nhận.

## 2. Chọn đặc trưng cho mạng nơ-ron đã huấn luyện

Zhao, Tsay và Kronqvist (*Model-based feature selection for neural networks: A mixed-integer programming approach*, [arXiv:2302.10344](https://arxiv.org/abs/2302.10344), 2023) mã hóa một mạng ReLU đã huấn luyện thành bài toán MILP và giải một chuỗi MILP nhằm tìm *tập đầu vào thưa* cực đại hóa độ tin cậy phân lớp dưới ràng buộc về số lượng và phân phối. Trên MNIST và Fashion-MNIST, nhóm tác giả giữ lại khoảng 15% số điểm ảnh để huấn luyện lại mạng nhỏ gọn hơn và ít nhạy cảm với tấn công đối kháng hơn. Đây chính là tư duy chọn tập con tốt nhất áp dụng cho *đầu vào* của mạng nơ-ron tuyến tính từng khúc — sử dụng cùng cách mã hóa MILP như trong bài toán kiểm chứng bên dưới.

## 3. Kiểm chứng mạng ReLU bằng MILP

Một nút kích hoạt ReLU $$h=\max(0,Wx+b)$$ có thể mã hóa chính xác bằng ràng buộc tuyến tính nguyên hỗn hợp (sử dụng biến nhị phân chỉ trạng thái kích hoạt và kỹ thuật big-$$M$$ hoặc công thức chặt hơn). Khi đó, câu hỏi “liệu có tồn tại nhiễu trong bán kính $$\varepsilon$$ làm đảo nhãn dự đoán không?” trở thành một bài toán MILP. Tjeng, Xiao và Tedrake (*Evaluating Robustness of Neural Networks with Mixed Integer Programming*, ICLR 2019, [OpenReview](https://openreview.net/forum?id=HyGIdiRqtm)) kết hợp mã hóa chặt với kỹ thuật thắt chặn dần và kiểm chứng được các mạng trên MNIST có hơn $$10^5$$ đơn vị, nhanh hơn nhiều bậc so với bộ kiểm chứng SMT Reluplex; bài báo của Fischetti và Jo (2018) là nghiên cứu song hành từ góc nhìn vận trù học. Các công trình giai đoạn 2022–2025 (bất đẳng thức ReLU chặt hơn, phân tích phụ thuộc, lan truyền cận trên GPU) đều xây dựng trên nền tảng này: mỗi “lát cắt” chính là một bất đẳng thức tuyến tính hợp lệ mà phép biến đổi ReLU phải thỏa mãn.

## 4. Cây phân loại tối ưu và học chọn mặt phẳng cắt

Bertsimas và Dunn (*Machine Learning* 106:1039–1082, 2017) mô hình hóa toàn bộ cây quyết định dưới dạng MIP (Optimal Classification Trees — OCT). Hua, Ren và Cao (NeurIPS 2022, [bài báo](https://proceedings.neurips.cc/paper_files/paper/2022/hash/37771cc0be272368102a37f202bb88d8-Abstract-Conference.html)) đề xuất thuật toán nhánh và cận trên không gian thu gọn (RS-OCT), mở rộng quy mô OCT lên các bảng dữ liệu hàng trăm nghìn dòng và đạt độ chính xác kiểm tra cao hơn các phương pháp MIP-OCT trước đó trên các tập UCI lớn. Các mô hình cây tối ưu hàm mất mát logistic (TOP, 2024) giữ cùng cấu trúc MILP và thay hàm mất mát phân loại sai bằng xấp xỉ tuyến tính từng khúc của hàm mất mát logistic.

Ở góc độ *bộ giải*, hướng nghiên cứu **học chọn mặt phẳng cắt** (chẳng hạn HGTSM, [arXiv:2410.03112](https://arxiv.org/abs/2410.03112), 2024) huấn luyện mô hình đồ thị dị chất trên MIPLIB 2017 và các bộ bài toán ML4CO để tự động lựa chọn chuỗi mặt phẳng cắt thay cho heuristic viết tay — biến chính thuật toán mặt phẳng cắt của mục 25-01 thành dữ liệu huấn luyện cho học máy.

**Bài tập.** Mã hóa một mạng ReLU hai lớp cỡ nhỏ $$f(x)=W_2\,\mathrm{ReLU}(W_1 x)$$ với $$W_1\in\mathbb{R}^{3\times 2}$$ thành bài toán MILP (dùng 3 biến nhị phân cho ba đơn vị ẩn). Cực đại hóa $$f(x)_1-f(x)_2$$ dưới ràng buộc $$\|x-x_0\|_\infty\le\varepsilon$$. Nếu giá trị tối ưu dương, ta tìm được một ví dụ đối kháng hợp lệ; nếu bộ giải chứng minh cận trên không dương, ta có chứng nhận độ bền vững tại $$x_0$$. So sánh kết quả MIP với tấn công bằng gradient có chiếu (PGD): PGD có thể *tìm* được ví dụ làm đảo nhãn nếu tồn tại, nhưng chỉ MIP mới có thể *chứng minh* rằng không tồn tại ví dụ đối kháng nào trong lân cận đó.

## Nguồn

- D. Bertsimas, A. King, R. Mazumder, *Ann. Statist.* 44(2):813–852, 2016 — tập con tốt nhất qua MIP.
- Chọn đặc trưng dựa trên mô hình cho NN, [arXiv:2302.10344](https://arxiv.org/abs/2302.10344), 2023.
- V. Tjeng, K. Xiao, R. Tedrake, ICLR 2019 — kiểm chứng bền vững MILP.
- M. Fischetti and J. Jo, CPAIOR 2018 — mạng sâu như MIP.
- D. Bertsimas and J. Dunn, *Mach. Learn.* 106:1039–1082, 2017 — cây phân loại tối ưu.
- NeurIPS 2022 RS-OCT — OCT toàn cục khả mở.
- Học chọn mặt phẳng cắt, [arXiv:2410.03112](https://arxiv.org/abs/2410.03112), 2024.
