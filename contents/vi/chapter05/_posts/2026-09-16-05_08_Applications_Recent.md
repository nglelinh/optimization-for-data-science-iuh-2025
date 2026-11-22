---
layout: post
title: 05-08 Ứng dụng và phát triển gần đây
chapter: '05'
order: 14
owner: Nguyen Le Linh
categories:
- chapter05
lang: vi
lesson_type: optional
---

Chương 05 phân loại các bài toán tối ưu hóa lồi theo cấu trúc hàm mục tiêu và các loại nón trong ràng buộc: LP, QP, QCQP, SOCP, SDP và quy hoạch hình học. Hệ phân loại này cũng chính là giao diện nền tảng của các ngôn ngữ mô hình hóa tối ưu hiện đại. Bài học này điểm qua ba ứng dụng thực tiễn tiêu biểu trong giai đoạn 2022–2026 — bộ giải điểm trong thế hệ mới tích hợp sẵn trong CVXPY, bài toán QP tối ưu hóa danh mục đầu tư có thể kiểm thử trên dữ liệu lịch sử, và kỹ thuật nới lỏng SDP để kiểm chứng độ bền vững của mạng nơ-ron — kèm theo nhận xét về vai trò của dạng QP chuẩn trong bài toán Lasso và khôi phục thưa.

Phần thực hành DCP/CVXPY đã được trình bày ở bài [05-07]({% multilang_post_url contents/chapter05/2026-09-15-05_07_Modeling_with_DCP_CVXPY %}); bài này bổ sung góc nhìn về lý do các lớp nón chuẩn đó quan trọng trong thực tế.

## Clarabel: Bộ giải điểm trong hiện đại cho các bài toán nón

Goulart và Chen (*Clarabel: An interior-point solver for conic programs with quadratic objectives*, [arXiv:2405.12762](https://arxiv.org/abs/2405.12762), 2024; tài liệu [clarabel.org](https://clarabel.org/); [trang trích dẫn](https://oxfordcontrol.github.io/ClarabelDocs/stable/citing/)) xây dựng phương pháp điểm trong nhúng thuần nhất cho các bài toán quy hoạch nón có hàm mục tiêu bậc hai. Bộ giải hỗ trợ trực tiếp các loại nón đã học trong chương này — nón không âm, nón bậc hai, nón nửa xác định (có hỗ trợ phân rã chordal) và một số nón không đối xứng — đồng thời được tích hợp làm bộ giải mặc định trong CVXPY. Kết quả thực nghiệm cho thấy Clarabel đạt hiệu năng cao trên các bài toán QP so với nhiều bộ giải mã nguồn mở và thương mại.

Điểm đáng chú ý về mặt thực hành là: khi mô hình đã được chuẩn hóa theo DCP, ta không cần tự cài đặt thuật toán giải Lasso bằng tay mà chỉ cần chuyển bài toán quy hoạch nón chuẩn cho một bộ giải điểm trong (IPM). Việc chuyển đổi giữa `solver=cp.CLARABEL`, `cp.OSQP` hay `cp.SCS` thực chất là so sánh hiệu quả của các thuật toán trên cùng một dạng chuẩn. OSQP (Stellato, Banjac, O’Donoghue, Bemporad và Boyd, *Math. Prog. Comp.* 2020) vẫn là lựa chọn bậc nhất quen thuộc cho nhiều bài toán QP điều khiển và tài chính, còn Clarabel là bộ giải điểm trong hiện đại tiêu biểu của năm 2024.

## Tối ưu hóa danh mục đầu tư dưới dạng QP thực tế

Bài toán phân bổ danh mục trung bình–phương sai của Markowitz là một bài toán QP:

$$
\begin{align}
\min_x \quad & x^\top \Sigma x - \gamma \hat{r}^\top x \\
\text{s.t.} \quad & \mathbf{1}^\top x = 1, \quad x\in\mathcal{X},
\end{align}
$$

trong đó $$\mathcal{X}$$ là tập đa diện biểu diễn các ràng buộc như không bán khống (long-only), giới hạn đòn bẩy hoặc giới hạn vòng quay danh mục. Boyd, Busseti, Diamond, Kahn, Koh, Nystrup và Speth (*Multi-Period Trading via Convex Optimization*, [*Found. Trends Optim.* 2017](https://stanford.edu/~boyd/papers/cvx_portfolio.html)) mở rộng mô hình QP này cho cả bài toán một kỳ và nhiều kỳ có tính đến chi phí giao dịch và chi phí nắm giữ. Thư viện đi kèm [cvxportfolio](https://www.cvxportfolio.com/) (tiếp tục được bảo trì đến giữa thập niên 2020, phiên bản v1.5) cho phép kiểm thử trực tiếp các chiến lược `SinglePeriodOptimization` và `MultiPeriodOptimization` trên dữ liệu thị trường thực tế thông qua `StockMarketSimulator`.

Dù chuyên khảo gốc công bố năm 2017, mô hình QP chuẩn vẫn giữ nguyên giá trị nền tảng, trong khi hệ sinh thái bộ giải (OSQP, Clarabel) và phần mềm mô phỏng liên tục được cập nhật. Với hướng mở rộng bền vững theo phân phối (DRO) dùng khoảng cách Wasserstein gần đây hơn (Gao và Kleywegt, [*Math. Oper. Res.* 2023](https://doi.org/10.1287/moor.2022.1275); xem Chương 02), bài toán sau khi lấy đối ngẫu cũng quy về dạng QP hoặc SOCP.

## Nới lỏng SDP trong kiểm chứng mạng nơ-ron

Bài toán kiểm tra độ bền vững cục bộ của mạng nơ-ron ReLU — xác minh rằng không có nhiễu đầu vào trong bán kính $$\varepsilon$$ nào làm thay đổi nhãn dự đoán — vốn là một bài toán khả thi không lồi. Bằng cách thay tích của các đầu ra kích hoạt bằng một ma trận mô-men nửa xác định dương, ta thu được một bài toán *nới lỏng* SDP (kết hợp ý tưởng nới lỏng ở bài 04-08 với nón SDP của bài 05-05). Lan, Zheng và Lomuscio (*Tight Neural Network Verification via Semidefinite Relaxations and Linear Reformulations*, [AAAI 2022](https://doi.org/10.1609/aaai.v36i7.20689)) kết hợp nới lỏng SDP theo từng lớp với các lát cắt tuyến tính hóa (RLT), giúp tăng mạnh tỉ lệ chứng nhận bền vững trên mạng MNIST (chẳng hạn tăng từ 0% lên 82% trên mạng khoảng 10 nghìn nút trong thực nghiệm của họ). Trước đó, hướng nới lỏng SDP theo lớp kết hợp lát cắt tam giác cũng đã được Batten, Kouvaros, Lomuscio và Zheng giới thiệu tại [IJCAI 2021](https://doi.org/10.24963/ijcai.2021/301).

Mặc dù khó áp dụng SDP trực tiếp cho các mạng cỡ ImageNet, khuôn mẫu mô hình hóa ở đây rất rõ ràng: các ràng buộc tổ hợp hoặc song tuyến được thay bằng điều kiện $$X\succeq 0$$ kèm các đẳng thức tuyến tính, sau đó bộ giải SDP của Chương 05 sẽ giúp chứng nhận tính chất hoặc đưa ra chặn chặt.

## Khôi phục thưa vẫn dựa trên nền tảng QP chuẩn

Bài toán Lasso:

$$
\min_x \tfrac12\|Ax-b\|_2^2 + \lambda \|x\|_1
$$

là công cụ quen thuộc cho bài toán khôi phục thưa trong xử lý ảnh y khoa và thống kê chiều cao, đồng thời dễ dàng biểu diễn trong CVXPY bằng vài hàm nguyên tử (xem bài 05-07). Nhiều nghiên cứu sau năm 2021 phát triển hướng *khai triển thuật toán* (algorithm unrolling), chuyển các bước lặp hạ gradient cận kề (như ISTA) của bài toán QP này thành các lớp mạng nơ-ron có thể học bước nhảy và từ điển từ dữ liệu (Monga, Li và Eldar, “Algorithm Unrolling,” [*IEEE Signal Processing Magazine*, 2021](https://doi.org/10.1109/MSP.2020.3016905)). Tuy vậy, cấu trúc toán học cốt lõi vẫn là cùng một bài toán QP; nắm vững cách viết Lasso về dạng QP với biến phụ giúp người học tiếp cận các mô hình ISTA khai triển một cách trực tiếp.

## Nguồn

1. P. J. Goulart và Y. Chen, “Clarabel: An interior-point solver for conic programs with quadratic objectives,” arXiv:2405.12762, 2024. [arXiv](https://arxiv.org/abs/2405.12762) · [clarabel.org](https://clarabel.org/)
2. S. Boyd, E. Busseti, S. Diamond và cộng sự, “Multi-Period Trading via Convex Optimization,” *Found. Trends Optim.*, 2017. [trang](https://stanford.edu/~boyd/papers/cvx_portfolio.html) · [cvxportfolio](https://www.cvxportfolio.com/)
3. J. Lan, Y. Zheng và A. Lomuscio, “Tight Neural Network Verification via Semidefinite Relaxations and Linear Reformulations,” AAAI 2022. [DOI](https://doi.org/10.1609/aaai.v36i7.20689)
4. B. Batten, P. Kouvaros, A. Lomuscio và Y. Zheng, “Efficient Neural Network Verification via Layer-based Semidefinite Relaxations and Linear Cuts,” IJCAI 2021. [DOI](https://doi.org/10.24963/ijcai.2021/301)
5. V. Monga, Y. Li và Y. C. Eldar, “Algorithm Unrolling: Interpretable, Efficient Deep Learning for Signal and Image Processing,” *IEEE SPM* 38(2):18–44, 2021. [DOI](https://doi.org/10.1109/MSP.2020.3016905)
