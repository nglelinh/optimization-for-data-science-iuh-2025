---
layout: post
title: 05-08 Ứng dụng và phát triển gần đây
chapter: '05'
order: 13
owner: Nguyen Le Linh
categories:
- chapter05
lang: vi
lesson_type: optional
---

Chương 05 phân loại chương trình lồi theo *dáng* mục tiêu và các nón trong ràng buộc: LP, QP, QCQP, SOCP, SDP và quy hoạch hình học. Phân loại đó cũng là API của ngôn ngữ mô hình hóa. Bài này xem ba chỗ các dạng chuẩn ấy là đối tượng sản xuất 2022–2026 — một bộ giải điểm trong hiện đại đi kèm CVXPY, các QP danh mục bạn backtest được, và nới SDP chứng nhận mạng nơ-ron — cùng lời nhắc rằng Lasso và khôi phục thưa vẫn là QP (hoặc QP dạng mở rộng) bạn nên mô hình, không nên tự viết tay.

Bạn đã có lab DCP/CVXPY ở [05-07]({% multilang_post_url contents/chapter05/2026-09-15-05_07_Modeling_with_DCP_CVXPY %}). Coi bài này là phần bạn đồng hành *vì sao các nón này*.

## Clarabel: động cơ điểm trong 2024 cho cả phân loại

Goulart và Chen (*Clarabel: An interior-point solver for conic programs with quadratic objectives*, [arXiv:2405.12762](https://arxiv.org/abs/2405.12762), 2024; tài liệu [clarabel.org](https://clarabel.org/); [trang trích dẫn](https://oxfordcontrol.github.io/ClarabelDocs/stable/citing/)) xây phương pháp điểm trong nhúng thuần nhất cho chương trình lồi với ràng buộc nón và mục tiêu toàn phương. Bộ giải nói các nón mà chương này đã đặt tên — không âm, bậc hai, nửa xác định (kèm phân rã chordal), và một số nón không đối xứng — và được phân phối như bộ giải chuẩn trong CVXPY. Hồ sơ số của họ đặc biệt mạnh trên QP so với vài mã nguồn mở và thương mại.

Điểm sư phạm rất thẳng: một khi mô hình DCP đã chuẩn hóa, bạn không còn “làm Lasso bằng Python.” Bạn đang đưa một chương trình nón cho một IPM. Đổi `solver=cp.CLARABEL` versus `cp.OSQP` versus `cp.SCS` là thí nghiệm trên *dạng chuẩn + thuật toán*, không phải viết lại khoa học. OSQP (Stellato, Banjac, O’Donoghue, Bemporad và Boyd, *Math. Prog. Comp.* 2020) vẫn là bộ giải QP cấp một đầu tiên cho nhiều QP điều khiển và danh mục; Clarabel là đối tác điểm trong 2024 bạn cần biết tên.

## Xây danh mục như QP có thể đưa vào vận hành

Phân bổ trung bình–phương sai Markowitz là QP

$$
\begin{align}
\min_x \quad & x^\top \Sigma x - \gamma \hat{r}^\top x \\
\text{s.t.} \quad & \mathbf{1}^\top x = 1, \quad x\in\mathcal{X},
\end{align}
$$

với $$\mathcal{X}$$ là polytope long-only, đòn bẩy, hoặc giới hạn doanh số. Boyd, Busseti, Diamond, Kahn, Koh, Nystrup và Speth (*Multi-Period Trading via Convex Optimization*, [*Found. Trends Optim.* 2017](https://stanford.edu/~boyd/papers/cvx_portfolio.html)) đặt phiên bản một kỳ và nhiều kỳ của QP này — cộng chi phí giao dịch và nắm giữ — trong một khung. Thư viện kèm [cvxportfolio](https://www.cvxportfolio.com/) (vẫn được duy trì giữa thập niên 2020, tài liệu hiện tại v1.5) là cách *chạy* bài báo đó trên dữ liệu thị trường gần đây: chính sách `SinglePeriodOptimization` / `MultiPeriodOptimization` trong `StockMarketSimulator`.

Chuyên khảo 2017 cũ hơn 2022; lý do nó thuộc đây là *dạng chuẩn* chưa bị thay, chỉ stack bộ giải (OSQP / Clarabel) và API phần mềm thay đổi. Nếu cần đối tác khoa học 2022–2023, danh mục DRO Wasserstein (Gao và Kleywegt, [*Math. Oper. Res.* 2023](https://doi.org/10.1287/moor.2022.1275); xem Chương 02) là QP hoặc SOCP sau khi viết đối ngẫu.

## Nới SDP cho kiểm chứng mạng nơ-ron

Hỏi một mạng ReLU có vững địa phương không — “không nhiễu bán kính $$\varepsilon$$ nào đổi lớp dự đoán” — là bài khả thi không lồi. Thay tích các kích hoạt bằng ma trận moment nửa xác định dương cho một *nới* SDP (cùng ý nới như 04-08, nay trong nón SDP của 05-05). Lan, Zheng và Lomuscio (*Tight Neural Network Verification via Semidefinite Relaxations and Linear Reformulations*, [AAAI 2022](https://doi.org/10.1609/aaai.v36i7.20689)) kết hợp SDP theo lớp với lát cắt reformulation-linearization (RLT) và báo cáo tăng lớn tỷ lệ chứng nhận vững trên mạng MNIST (ví dụ từ 0% lên 82% chứng nhận trên mạng ~10k nút trong bảng của họ). SDP theo lớp cộng lát cắt tam giác sớm hơn nằm ở Batten, Kouvaros, Lomuscio và Zheng ([IJCAI 2021](https://doi.org/10.24963/ijcai.2021/301)).

Bạn sẽ không giải SDP cỡ ImageNet trong môn này. Bạn *sẽ* nhận ra khuôn mẫu: ràng buộc tổ hợp hoặc song tuyến được thay bằng $$X\succeq 0$$ cộng đẳng thức tuyến tính, và một bộ giải cho lớp SDP của Chương 05 hoặc chứng nhận tính chất hoặc trả về một chặn.

## Khôi phục thưa vẫn là QP chuẩn

Lasso

$$
\min_x \tfrac12\|Ax-b\|_2^2 + \lambda \|x\|_1
$$

là công cụ khôi phục thưa trong ảnh y và thống kê chiều cao. Trong CVXPY chỉ vài nguyên tử (xem 05-07). *Khoa học* sau 2021 thường là *bung* vòng lặp proximal-gradient của QP đó thành mạng (Monga, Li và Eldar, “Algorithm Unrolling,” [*IEEE Signal Processing Magazine*, 2021](https://doi.org/10.1109/MSP.2020.3016905)) để bước và từ điển trở thành huấn luyện được. Đối tượng trong vẫn là cùng QP. Nếu viết được Lasso như QP với slack, bạn đọc được bài ISTA đã bung mà không cần lý thuyết mới.

## Nguồn

1. P. J. Goulart và Y. Chen, “Clarabel: An interior-point solver for conic programs with quadratic objectives,” arXiv:2405.12762, 2024. [arXiv](https://arxiv.org/abs/2405.12762) · [clarabel.org](https://clarabel.org/)
2. S. Boyd, E. Busseti, S. Diamond và cộng sự, “Multi-Period Trading via Convex Optimization,” *Found. Trends Optim.*, 2017. [trang](https://stanford.edu/~boyd/papers/cvx_portfolio.html) · [cvxportfolio](https://www.cvxportfolio.com/)
3. J. Lan, Y. Zheng và A. Lomuscio, “Tight Neural Network Verification via Semidefinite Relaxations and Linear Reformulations,” AAAI 2022. [DOI](https://doi.org/10.1609/aaai.v36i7.20689)
4. B. Batten, P. Kouvaros, A. Lomuscio và Y. Zheng, “Efficient Neural Network Verification via Layer-based Semidefinite Relaxations and Linear Cuts,” IJCAI 2021. [DOI](https://doi.org/10.24963/ijcai.2021/301)
5. V. Monga, Y. Li và Y. C. Eldar, “Algorithm Unrolling: Interpretable, Efficient Deep Learning for Signal and Image Processing,” *IEEE SPM* 38(2):18–44, 2021. [DOI](https://doi.org/10.1109/MSP.2020.3016905)
