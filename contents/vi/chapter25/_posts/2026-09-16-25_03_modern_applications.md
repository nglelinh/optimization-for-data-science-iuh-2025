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


Chương 25 là nửa *bộ giải* của quy hoạch nguyên hỗn hợp: mặt phẳng cắt, branch-and-cut, và hai ví dụ mở rộng (tập con tốt nhất, phân vị nhỏ nhất). Những kỹ thuật đó nay được dùng để *chọn đặc trưng*, *chứng nhận* mạng nơ-ron, *mọc cây tối ưu*, và thậm chí *học cắt nào* cần thêm. Ghi chú tùy chọn này là lớp ứng dụng 2022–2026 chồng lên 25-01 và 25-02; nó không suy diễn lại cắt Gomory.

## 1. Chọn tập con tốt nhất, vẫn là poster MIP

Bài toán bình phương tối thiểu ràng buộc $$\ell_0$$ ở 25-02-01 là

$$
\min_\beta\ \tfrac12\|y-X\beta\|_2^2\qquad\text{subject to}\qquad \|\beta\|_0\le k,
$$

hoặc dạng big-$$M$$ với nhị phân $$z_i$$. Bertsimas, King và Mazumder, *Ann. Statist.* 44(2):813–852, 2016, cho thấy bộ giải MIP hiện đại cộng khởi động nóng có thể thắng lore “bất khả thi khi $$p>30$$.” So sánh thập niên 2020 không còn là MIP versus Lasso trên laptop: đó là MIP versus CD theo đường (Chương 23) versus penalty không lồi (skglm) trên $$p$$ hàng trăm, với *chứng nhận* khi khe đóng. Dùng Lasso / elastic net để thăm dò; dùng MIP tập con tốt nhất khi nhà quản lý hoặc nhà khoa học đòi “đúng $$k$$ gene” và một chặn dưới tối ưu.

## 2. Chọn đặc trưng cho mạng đã huấn luyện

Zhao, Tsay và Kronqvist, *Model-based feature selection for neural networks: A mixed-integer programming approach*, [arXiv:2302.10344](https://arxiv.org/abs/2302.10344) (2023), mã hóa một mạng ReLU đã huấn luyện và giải một dãy MILP tìm *đầu vào thưa* cực đại hóa độ tin cậy lớp, với ràng buộc lực lượng và phân phối. Trên MNIST / Fashion-MNIST họ giữ khoảng 15% pixel và huấn luyện lại mạng nhỏ hơn, bền tấn công hơn. Đây là tư duy tập con tốt nhất áp lên *đầu vào*, với mạng đã huấn luyện được mã hóa như MIP từng khúc tuyến tính — cùng mã hóa dùng cho kiểm chứng bên dưới.

## 3. Kiểm chứng mạng ReLU bằng MILP

Một ReLU $$h=\max(0,Wx+b)$$ là ràng buộc tuyến tính nguyên hỗn hợp (kích hoạt nhị phân, big-$$M$$ hoặc công thức chặt hơn). Hỏi “có nhiễu kích thước $$\varepsilon$$ làm đảo nhãn không?” khi đó là một MILP. Tjeng, Xiao và Tedrake, *Evaluating Robustness of Neural Networks with Mixed Integer Programming*, ICLR 2019, [OpenReview](https://openreview.net/forum?id=HyGIdiRqtm), kết hợp mã hóa chặt với thắt chặn dần và kiểm chứng mạng MNIST hơn $$10^5$$ đơn vị, hơn verifier SMT Reluplex nhiều bậc. Fischetti và Jo (2018) là bài đồng hành MIP-OR. Văn liệu 2022–2025 (bất đẳng thức ReLU mạnh hơn, phân tích phụ thuộc, lan truyền chặn GPU) vẫn đứng trên công thức đó. Nếu bạn hiểu Gomory và branch-and-cut trong chương này, bạn đọc được bài kiểm chứng: “cắt” là bất đẳng thức tuyến tính mà một kích hoạt ReLU phải thỏa.

## 4. Cây phân loại tối ưu và học cắt

Bertsimas và Dunn, *Machine Learning* 106:1039–1082, 2017, viết cả cây quyết định như một MIP (Optimal Classification Trees, OCT). Hua, Ren và Cao, NeurIPS 2022 ([bài báo](https://proceedings.neurips.cc/paper_files/paper/2022/hash/37771cc0be272368102a37f202bb88d8-Abstract-Conference.html)), đưa thuật toán branch-and-bound không gian thu hẹp (RS-OCT) khiến OCT lên bảng trăm nghìn dòng và báo độ chính xác kiểm tra tốt hơn các baseline MIP-OCT trước trên tập UCI lớn. Cây tối ưu loss / logistic (TOP, 2024) giữ cùng xương sống MILP và đổi mục tiêu phân loại sai lấy loss logistic từng khúc tuyến tính.

Về phía *bộ giải*, học **chọn mặt phẳng cắt** (ví dụ HGTSM, [arXiv:2410.03112](https://arxiv.org/abs/2410.03112), 2024) huấn luyện mô hình đồ thị dị chất trên MIPLIB 2017 và instance ML4CO để chuỗi cắt của 25-01 không còn là heuristic viết tay. Đó là Chương 25 soi gương: thuật toán mặt phẳng cắt trở thành dữ liệu huấn luyện.

**Bài tập.** Mã hóa đồ chơi ReLU 2 lớp $$f(x)=W_2\,\mathrm{ReLU}(W_1 x)$$ với $$W_1\in\mathbb{R}^{3\times 2}$$ thành MILP (nhị phân cho ba đơn vị ẩn). Cực đại hóa $$f(x)_1-f(x)_2$$ với $$\|x-x_0\|_\infty\le\varepsilon$$. Nếu giá trị tối ưu dương, bạn có ví dụ đối kháng được chứng nhận; nếu bộ giải chứng minh chặn không dương, bạn có chứng nhận bền vững tại $$x_0$$. So đáp án MIP với tấn công gradient chiếu — tấn công có thể *tìm* đảo nhãn, chỉ MIP *chứng minh* là không có.

## Nguồn

- D. Bertsimas, A. King, R. Mazumder, *Ann. Statist.* 44(2):813–852, 2016 — tập con tốt nhất qua MIP.
- Chọn đặc trưng dựa trên mô hình cho NN, [arXiv:2302.10344](https://arxiv.org/abs/2302.10344), 2023.
- V. Tjeng, K. Xiao, R. Tedrake, ICLR 2019 — kiểm chứng bền vững MILP.
- M. Fischetti and J. Jo, CPAIOR 2018 — mạng sâu như MIP.
- D. Bertsimas and J. Dunn, *Mach. Learn.* 106:1039–1082, 2017 — cây phân loại tối ưu.
- NeurIPS 2022 RS-OCT — OCT toàn cục khả mở.
- Học chọn mặt phẳng cắt, [arXiv:2410.03112](https://arxiv.org/abs/2410.03112), 2024.
