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

Hơn bốn thập kỷ sau bài báo của Karmarkar, phương pháp điểm trong gốc–đối ngẫu không hề trở thành "kiến thức sách giáo khoa cũ kỹ" — ngược lại, giai đoạn 2022–2026 chứng kiến một làn sóng tái kiến trúc mạnh mẽ. Các bộ giải mới viết bằng Rust và Julia như Clarabel đã trở thành nhân mặc định của CVXPY, các bộ giải LP/QP điểm trong được đưa lên GPU để xử lý bài toán hàng chục triệu biến, đồng thời nới lỏng SDP lại trở thành công cụ trung tâm trong bài toán kiểm chứng độ bền vững (robustness verification) của mạng nơ-ron sâu.

## Kiến thức cần nhớ: Ba động lực nâng cấp PD-IPM trong kỷ nguyên hiện đại

Để hiểu vì sao các hệ thống tối ưu giai đoạn 2022–2026 vẫn xoay quanh khung PD-IPM của Chương 17 nhưng khác xa cài đặt cơ bản, hãy chú ý ba bước tiến sau:

- **Nhúng tự đối ngẫu đồng nhất (Homogeneous Self-Dual Embedding):** PD-IPM cơ bản dễ bị phân kỳ khi bài toán vô nghiệm hoặc không bị chặn. Các bộ giải hiện đại (Clarabel, Mosek, ECOS) nhúng bài toán vào một hệ đồng nhất thêm biến vô hướng $$(\tau_{\text{hom}}, \kappa)$$ để đồng thời giải tối ưu HOẶC trả về chứng chỉ Farkas khẳng định vô nghiệm trong đúng một lần chạy.
- **Tích các nón đối xứng và bất đối xứng:** Bài toán hiện đại không chỉ có LP hay SDP mà kết hợp cả nón bậc hai (SOC), nón mũ (exponential cone — cho hồi quy logistic, entropy) và nón lũy thừa (power cone). Clarabel mở rộng hàm chắn và bước Newton gốc–đối ngẫu trực tiếp trên tích các nón này.
- **Tăng tốc phần cứng và bài toán kiểm chứng học sâu:** Việc giải hệ KKT khối (chiếm >85% thời gian chạy) đang được tăng tốc bằng phân rã Cholesky/LDL song song trên GPU và tiền điều kiện lặp, đồng thời mở ra cuộc đua giữa độ chặt của nới lỏng SDP và giới hạn bộ nhớ $$O(n^2)$$ khi kiểm chứng mạng nơ-ron.

### Giải thích: Nhúng đồng nhất phát hiện bài toán vô nghiệm như thế nào?

Giả sử bạn đưa vào bộ giải một bài toán LP 1 biến **vô nghiệm** (infeasible):

$$\min_{x} \; x \qquad \text{với điều kiện} \qquad x = -1, \quad x \ge 0.$$

Hãy xem điều gì xảy ra với PD-IPM thường so với nhúng đồng nhất (như trong Clarabel):

1. **Điều gì làm PD-IPM thường lúng túng?** Ràng buộc $$x = -1$$ và $$x \ge 0$$ mâu thuẫn nhau, nên không tồn tại điểm khả thi gốc; trong khi bài toán đối ngẫu $$\max_y (-y) \text{ s.t. } y \le 1$$ không bị chặn trên ($$y \to -\infty$$). Nếu chạy PD-IPM thường, giá trị $$y^{(k)} \to -\infty$$ còn phần dư $$r_{\text{prim}} = x + 1$$ không bao giờ về $$0$$, khiến thuật toán chạy hết số vòng lặp rồi báo lỗi số học.
2. **Cách nhúng đồng nhất xử lý:** Thay vì cố định vế phải $$b = -1$$ và $$c = 1$$, ta nhân chúng với một biến vô hướng $$\tau_{\text{hom}} \ge 0$$ và bổ sung biến bù $$\kappa \ge 0$$ với điều kiện bù chặt $$\tau_{\text{hom}}\kappa = 0$$:
   $$Ax - b\tau_{\text{hom}} = 0 \implies x + \tau_{\text{hom}} = 0, \qquad A^T y + s - c\tau_{\text{hom}} = 0 \implies y + s - \tau_{\text{hom}} = 0.$$
3. **Kết quả hội tụ sạch sẽ:** Khi thuật toán hội tụ, ta thu được $$\tau_{\text{hom}}^\star = 0$$, $$\kappa^\star > 0$$, $$x^\star = 0$$, $$y^\star = -1$$, $$s^\star = 1 \ge 0$$. Kiểm tra bất đẳng thức Farkas:
   $$A^T y^\star = -1 \le 0 \quad \text{và} \quad b^T y^\star = (-1)(-1) = +1 > 0.$$
   Bộ giải trả về ngay một **chứng chỉ toán học chính xác** khẳng định bài toán gốc vô nghiệm — không cần đoán qua ngưỡng dừng hay chạy thêm Pha I!

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
