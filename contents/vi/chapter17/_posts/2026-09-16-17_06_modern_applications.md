---
layout: post
title: 17-06 Ứng dụng hiện đại của phương pháp điểm trong nguyên thủy–đối ngẫu (2022–2026)
chapter: '17'
order: 10
owner: Nguyen Le Linh
categories:
- chapter17
lang: vi
lesson_type: optional
---

Phương pháp điểm trong nguyên thủy–đối ngẫu chỉ thực hiện *một* bước Newton trên hệ phương trình KKT bị nhiễu

$$
r_t(x,u,v) = 0
$$

thay vì giải bài toán rào cản tới độ chính xác cao ở mọi giá trị $$t$$. Những đại lượng bạn đã tính trong chương này — khoảng cách đối ngẫu thay thế $$-h(x)^\top u$$, phần dư nguyên thủy và đối ngẫu, cùng khối bù tuyến tính hóa $$U\nabla h(x)^\top\,\Delta x + H(x)\,\Delta u = -Uh(x) - (1/t)\mathbf{1}$$ — chính là các phần dư mà các bộ giải nón hiện đại hiển thị trong nhật ký chạy. Diễn biến đáng chú ý giai đoạn 2022–2026 là các bộ giải này đã trở thành backend Python mặc định, được tăng tốc trên GPU, và đồng thời chạm tới giới hạn lý thuyết của nới lỏng SDP trong bài toán kiểm chứng mạng nơ-ron.

## Clarabel: PD-IPM dưới dạng thư viện chuẩn

Clarabel (Goulart & Chen, 2024) cài đặt thuật toán điểm trong nguyên thủy–đối ngẫu đồng nhất cho bài toán có hàm mục tiêu bậc hai trên tích các nón đối xứng và không đối xứng. So với PD-IPM cơ bản trong giáo trình, thư viện này bổ sung nhúng đồng nhất (homogeneous embedding — giúp xử lý bài toán không khả thi hoặc không bị chặn với đường trung tâm xác định tốt), bước dự báo – hiệu chỉnh kiểu Mehrotra và phân rã LDL thưa cho hệ Newton KKT. Kết quả thực nghiệm cho thấy bộ giải nhanh và ổn định hơn nhiều đối thủ thương mại lẫn mã nguồn mở trên các bộ kiểm chuẩn, *đặc biệt* trên bài toán QP — đúng lớp bài toán mà hệ Newton của chương này hướng tới.

Từ phiên bản CVXPY 1.5, Clarabel trở thành bộ giải mặc định cho các lớp bài toán trước đây dùng ECOS. Do đó, khi bạn gọi `prob.solve()` trên một bài toán SOCP, hệ thống đang thực thi chính thuật toán của Chương 17 chứ không phải phương pháp đơn hình. Các biến đối ngẫu mà CVXPY trả về chính là $$u, v$$ trong chương này, còn phần dư bù là khoảng cách đối ngẫu thay thế. Nói cách khác, PD-IPM hiện đại đã có sẵn ngay trên máy tính cá nhân thông qua một lệnh gọi thư viện.

## CuClarabel: giải hệ Newton trên GPU

Chen, Tse, Nobel, Goulart và Boyd (2024) chuyển vòng lặp này lên GPU NVIDIA với tên gọi **CuClarabel**. Cấu trúc thuật toán vẫn là điểm trong nguyên thủy–đối ngẫu: pha tiền xử lý cân bằng dữ liệu, pha thiết lập và phân rã hệ Newton, kết hợp chiến lược song song hỗn hợp cho các nón (xử lý ràng buộc tuyến tính trước, sau đó xử lý song song các nón còn lại). Phần đại số tuyến tính được giao cho NVIDIA cuDSS với tùy chọn phân rã độ chính xác hỗn hợp. Bộ giải hỗ trợ nón không, nón không âm, nón bậc hai, nón mũ, nón lũy thừa và nón PSD. Bài báo cho thấy IPM trên GPU vượt trội IPM trên CPU trên nhiều lớp bài toán quy hoạch nón, bao gồm bài toán tối ưu danh mục đầu tư dạng QP và SOCP viết trong JuMP hoặc CVXPY.

Kết quả này minh họa trực tiếp phân tích độ phức tạp ở Chương 17: nút thắt tính toán của PD-IPM không nằm ở các phép cập nhật biến mà nằm ở bước phân rã hệ KKT. Khi phép phân rã ma trận thưa này được tăng tốc trực tiếp trên GPU, phương pháp điểm trong trở nên khả thi cho các bài toán nón cỡ vài nghìn đến hàng chục nghìn biến trong quy trình khoa học dữ liệu thực tế, trong khi các phương pháp tách bậc nhất vẫn phù hợp hơn với quy mô hàng triệu biến ở mức độ chính xác vừa phải.

## Nới lỏng SDP cho kiểm chứng mạng nơ-ron

Nới lỏng bán xác định (SDP relaxation) của mạng ReLU tạo ra một bài toán SDP mà giá trị tối ưu đóng vai trò chứng chỉ cho độ bền vững (robustness) của mạng (Raghunathan, Steinhardt, Liang và các công trình về kiểm chứng SDP-NN). Những bài toán SDP này thường được giải bằng phương pháp điểm trong nguyên thủy–đối ngẫu khi cần một *chứng chỉ đáng tin cậy*, bởi các phương pháp bậc nhất có thể có vẻ hội tụ nhưng không cung cấp bảo chứng về khoảng cách đối ngẫu. Tuy nhiên, một nghiên cứu năm 2025, “Interior-Point Vanishing Problem in Semidefinite Relaxations for Neural Network Verification” ([arXiv:2506.10269](https://arxiv.org/abs/2506.10269)), chỉ ra vấn đề phát sinh khi bài toán nới lỏng *không* khả thi ngặt: đường trung tâm không có điểm trong, tính đối ngẫu mạnh có thể không còn đúng, và PD-IPM theo dõi khoảng cách $$X\cdot S$$ có thể không bao giờ xác nhận được tính tối ưu. Các tác giả sử dụng IPM độ chính xác cao (SDPA-GMP) để chẩn đoán hiện tượng này và đề xuất các kỹ thuật điều chuẩn SDP cũng như rút gọn mặt (facial reduction).

Đây là nơi mục SDP của Chương 17 giao thoa trực tiếp với học máy hiện đại. Phương trình đường trung tâm $$XS = \tau I$$ đòi hỏi điều kiện điểm trong $$X, S \succ 0$$. Nếu đa diện phổ (spectrahedron) không có phần trong tương đối, giả thiết này bị vi phạm và thuật toán ở bài 17-02 không chỉ chậm đi mà trở nên *không đặt chỉnh (ill-posed)*. Bài học thực tiễn vẫn là nguyên tắc kinh điển của Boyd–Vandenberghe: cần kiểm tra điều kiện Slater trước khi tin cậy vào khoảng cách đối ngẫu.

## Thực hành gợi ý trong khóa học

Trong một buổi thực hành khoảng một giờ, bạn có thể lấy một bài toán danh mục đầu tư chỉ mua (long-only portfolio) cỡ nhỏ hoặc SVM lề cứng, giải bằng `cp.CLARABEL`, và in ra phần dư nguyên thủy, phần dư đối ngẫu cùng khoảng cách đối ngẫu. Sau đó, hãy thử thay đổi loại nón ràng buộc (từ ràng buộc hộp sang nón bậc hai) để quan sát sự thay đổi về số vòng lặp Newton. Đây là cách trực quan nhất để thấy phương pháp điểm trong nguyên thủy–đối ngẫu vận hành trên mô hình khoa học dữ liệu mà không cần thêm lý thuyết ngoài chương này.

## Nguồn

- P. J. Goulart, Y. Chen, “Clarabel: An interior-point solver for conic programs with quadratic objectives,” 2024. [arXiv:2405.12762](https://arxiv.org/abs/2405.12762)
- Y. Chen, D. Tse, P. Nobel, P. Goulart, S. Boyd, “CuClarabel: GPU Acceleration for a Conic Optimization Solver,” 2024. [arXiv:2412.19027](https://arxiv.org/abs/2412.19027)
- CVXPY 1.5: Clarabel làm backend IPM mặc định.
- “Interior-Point Vanishing Problem in Semidefinite Relaxations for Neural Network Verification,” 2025. [arXiv:2506.10269](https://arxiv.org/abs/2506.10269)
