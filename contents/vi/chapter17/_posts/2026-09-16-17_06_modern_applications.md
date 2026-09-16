---
layout: post
title: 17-06 Ứng dụng hiện đại của phương pháp điểm trong nguyên thủy–đối ngẫu (2022–2026)
chapter: '17'
order: 11
owner: Nguyen Le Linh
categories:
- chapter17
lang: vi
lesson_type: optional
---

Phương pháp điểm trong nguyên thủy–đối ngẫu lấy *một* bước Newton trên ánh xạ KKT nhiễu

$$
r_t(x,u,v) = 0
$$

thay vì đẩy bài rào chắn tới độ chính xác cao ở mọi $$t$$. Các đối tượng bạn đã tính trong chương này — khe đối ngẫu thay $$-h(x)^\top u$$, phần dư nguyên thủy và đối ngẫu, khối bù tuyến tính hóa $$U\nabla h(x)\,\Delta x + H(x)\,\Delta u = -Uh(x) - (1/t)\mathbf{1}$$ — đúng là phần dư các bộ giải nón hiện đại in ra. Câu chuyện 2022–2026 là những bộ giải đó thành backend Python mặc định, rồi lên GPU, rồi đụng giới hạn của thư giãn SDP cho kiểm chứng mạng nơ-ron.

## Clarabel: PD-IPM như thư viện, không như bài tập

Clarabel (Goulart & Chen, 2024) cài một vòng lặp điểm trong nguyên thủy–đối ngẫu đồng nhất cho mục tiêu toàn phương trên tích các nón đối xứng và không đối xứng. So với PD-IPM sách giáo khoa, nó thêm: nhúng đồng nhất (để các thể hiện không khả thi và không bị chặn có đường trung tâm đặt được), hiệu chỉnh kiểu Mehrotra, và phân rã LDL thưa của hệ Newton KKT. Tác giả báo bộ giải nhanh và vững hơn vài đối thủ thương mại và mã nguồn mở trên bộ chuẩn, *đặc biệt* trên QP — đúng trường hợp hệ Newton của chương này được dựng cho.

CVXPY 1.5 biến Clarabel thành động cơ mặc định cho các lớp bài trước đây rơi xuống ECOS. Sinh viên viết `prob.solve()` trên một SOCP do đó đang chạy Chương 17, không phải bảng simplex. Biến đối ngẫu CVXPY trả về là $$u,v$$ của chương này; phần dư bù là khe thay. Một sự kiện đó đáng hơn một phép dựng mới: *bạn đã có PD-IPM trên máy tính xách tay*.

## CuClarabel: cùng hệ Newton trên GPU

Chen, Tse, Nobel, Goulart và Boyd (2024) chuyển vòng lặp sang GPU NVIDIA thành **CuClarabel**. Thuật toán vẫn là điểm trong nguyên thủy–đối ngẫu: pha dựng cân bằng dữ liệu, pha giải lập và phân rã hệ Newton, và các nón được xử lý theo chiến lược song song hỗn hợp (ràng buộc tuyến tính trước, rồi các nón khác song song). Đại số tuyến tính ủy thác cho NVIDIA cuDSS, với tùy chọn phân rã độ chính xác hỗn hợp. Các nón được hỗ trợ gồm nón không và không âm, nón bậc hai, nón mũ và lũy thừa, và nón PSD cùng chiều. Bài báo cho thấy IPM GPU thắng IPM CPU trên một dải chương trình nón; các ví dụ công khai gồm QP danh mục — cùng SOCP bạn có thể viết trong JuMP hoặc CVXPY.

Đây là thảo luận độ phức tạp Chương 17 được làm cụ thể. Nút thắt của PD-IPM không bao giờ là ba dòng cập nhật; nó là phân rã KKT. Một khi phân rã đó là giải trực tiếp thưa trên GPU, phương pháp điểm trong trở nên khả dĩ cho cỡ nón mà pipeline khoa học dữ liệu thực sự phát ra (hàng nghìn đến hàng chục nghìn biến), trong khi tách bậc nhất vẫn là công cụ cho hàng triệu biến với độ chính xác vừa phải.

## Thư giãn SDP cho kiểm chứng mạng nơ-ron

Thư giãn semidefinite của mạng ReLU sinh một SDP mà giá trị tối ưu chứng nhận vững (Raghunathan, Steinhardt, Liang, và dòng bộ kiểm SDP-NN). Những SDP đó được giải bằng điểm trong nguyên thủy–đối ngẫu khi cần một *chứng chỉ*: phương pháp bậc nhất có thể trông hội tụ mà không có chứng minh khe đối ngẫu. Một phân tích 2025, “Interior-Point Vanishing Problem in Semidefinite Relaxations for Neural Network Verification” ([arXiv:2506.10269](https://arxiv.org/abs/2506.10269)), chỉ ra điều xảy ra khi thư giãn *không* khả thi chặt: đường trung tâm không có phần trong, đối ngẫu mạnh có thể thất bại, và một PD-IPM theo dõi khe $$X\cdot S$$ có thể không bao giờ tuyên bố tối ưu. Tác giả dùng IPM độ chính xác cao (SDPA-GMP) để chẩn đoán bệnh lý và đề xuất SDP regularize / rút mặt.

Đây là mục SDP của Chương 17 gặp một tác vụ ML hiện đại. Phương trình đường trung tâm $$XS = \tau I$$ giả sử $$X,S\succ 0$$. Nếu phổ diện không có phần trong tương đối, giả thiết sai và thuật toán bạn cài ở 17-02 không chỉ chậm — nó *không đặt được*. Bài học là điều Boyd–Vandenberghe đã dạy: kiểm Slater, rồi mới tin khe.

## Việc nên chạy trong khóa này

Với một lab một giờ, lấy danh mục chỉ-mua-dài nhỏ hoặc SVM lề cứng, giải bằng `cp.CLARABEL`, và in phần dư nguyên thủy, phần dư đối ngẫu, và khe. Rồi đổi nón (hộp so với bậc hai) và xem số vòng Newton. Đó là điểm trong nguyên thủy–đối ngẫu áp vào mô hình khoa học dữ liệu, không cần lý thuyết mới ngoài chương này.

## Nguồn

- P. J. Goulart, Y. Chen, “Clarabel: An interior-point solver for conic programs with quadratic objectives,” 2024. [arXiv:2405.12762](https://arxiv.org/abs/2405.12762)
- Y. Chen, D. Tse, P. Nobel, P. Goulart, S. Boyd, “CuClarabel: GPU Acceleration for a Conic Optimization Solver,” 2024. [arXiv:2412.19027](https://arxiv.org/abs/2412.19027)
- CVXPY 1.5: Clarabel làm backend IPM mặc định.
- “Interior-Point Vanishing Problem in Semidefinite Relaxations for Neural Network Verification,” 2025. [arXiv:2506.10269](https://arxiv.org/abs/2506.10269)
