---
layout: post
title: 15-09 Ứng dụng hiện đại của phương pháp rào chắn (2022–2026)
chapter: '15'
order: 20
owner: Nguyen Le Linh
categories:
- chapter15
lang: vi
lesson_type: optional
---

Rào logarit

$$
\phi(x) = -\sum_{i=1}^{m}\log\bigl(-h_i(x)\bigr)
$$

biến bài có ràng buộc bất đẳng thức thành một họ bài trơn không ràng buộc (hoặc chỉ ràng buộc đẳng thức) đánh chỉ số bằng tham số siết $$t$$. Đó vẫn là cách các bộ giải lồi công nghiệp suy nghĩ, ngay khi người dùng không bao giờ gõ `log`. Bài này theo rào chắn từ đường trung tâm bạn đã dựng trong chương tới bốn chỗ sinh viên thực sự gặp năm 2022–2026: động cơ mặc định của CVXPY, bộ giải nón thời GPU, học tăng cường an toàn, và lớp điều khiển khả vi.

## Clarabel: IPM kiểu rào chắn làm động cơ mặc định của CVXPY

Goulart và Chen (2024) mô tả **Clarabel**, bộ giải điểm trong mã nguồn mở cho chương trình nón lồi có mục tiêu toàn phương. Thuật toán là nhúng đồng nhất chuyên biệt hóa thành vòng lặp điểm trong: một rào kiểu log (hoặc tương tự tự tương hợp trên từng nón nguyên tử) giữ các điểm lặp trong phần trong của orthant không âm, nón bậc hai, nón mũ và lũy thừa, và nón PSD, trong khi hệ Newton trên phần dư KKT đẩy khả thi nguyên thủy, khả thi đối ngẫu, và bù. Phân rã chordal có sẵn cho SDP lớn.

Sự kiện phần mềm đổi bài tập về nhà: từ CVXPY 1.5, Clarabel *thay ECOS làm mặc định* cho các lớp bài mà ECOS từng được gọi tự động (ghi chú phát hành CVXPY 1.5; Goulart & Chen, mục cài đặt). QP vẫn thường về OSQP (bộ giải ADMM, Chương 21), nhưng LP, SOCP và nhiều mô hình nón mũ nay âm thầm chạy phương pháp rào / điểm trong. Thói quen mô hình hóa từ [05-07]({% multilang_post_url contents/chapter05/2026-09-15-05_07_Modeling_with_DCP_CVXPY %}) do đó có động cơ Chương 15 phía dưới:

```python
import cvxpy as cp
x = cp.Variable(n)
prob = cp.Problem(cp.Minimize(cp.sum_squares(A @ x - b)), [x >= 0, cp.norm(x, 2) <= 1])
prob.solve(solver=cp.CLARABEL)
```

Hỏi `prob.solver_stats` sau một lần giải mặc định: nếu bạn không chỉ định OSQP, bạn đang nhìn một phương pháp đường trung tâm. Đó là câu trả lời hiện đại gọn nhất cho “rào chắn dùng ở đâu trong khoa học dữ liệu?” — *bên trong lớp mô hình hóa bạn đã dạy*.

## Danh mục, MPC, và các QP nón khác

Cùng ngăn xếp bộ giải là đường sản xuất cho danh mục trung bình–phương sai và ràng buộc rủi ro, QP điều khiển dự báo mô hình (MPC), và các nón tối ưu vững nhỏ. Mục số của Clarabel và bản GPU sau này (Chương 17) dùng QP danh mục và điều khiển làm ví dụ chạy đúng vì chúng *đủ tự tương hợp* cho Newton và *đủ có cấu trúc* cho phân rã KKT thưa. Sinh viên khoa học dữ liệu viết danh mục chỉ-mua-dài với SOCP sai số bám không phải “làm tài chính thay ML”; họ đang sinh đường trung tâm Chương 15 trên bài có Hessian là hiệp phương sai cộng số hạng rào trên đơn hình (hoặc trên nón bậc hai).

Đạo lý mô hình hóa giống Boyd & Vandenberghe, Chương 11: *đừng tự viết gradient chiếu trên nón nếu IPM rào chắn chỉ cách một `solve()`.* Tách bậc nhất (OSQP, SCS) thắng khi cần khởi động ấm 100 Hz; rào chắn thắng khi cần chứng chỉ độ chính xác cao và chiều vẫn vừa hệ Newton thưa.

## Rào logarit trong RL ràng buộc và an toàn

Liu, Ding và Liu (*IPO: Interior-Point Policy Optimization under Constraints*, AAAI 2020) đặt rào logarit lên ràng buộc chi phí của MDP ràng buộc rồi chạy phương pháp bậc nhất kiểu PPO trên mục tiêu trơn thu được. Rào trong bài đó không được giải bằng Newton — chính sách là mạng nơ-ron — nhưng *phép đưa về* đúng là Chương 15: bất đẳng thức thành phạt có gradient nổ ở biên, nên điểm lặp ở lại khả thi chặt nếu xuất phát khả thi. OmniSafe (Ji, Zhou, Zhang, Dai, Pan, Sun, Huang, Geng, Liu, Yang; JMLR 2024) và Safety Gymnasium (Ji et al., NeurIPS 2023 Datasets) đóng gói IPO cạnh PPO-Lagrangian, nên sinh viên 2024–2026 gặp rào log trong README *tối ưu chính sách* chứ không chỉ trong chương giải tích lồi.

So sánh sắc về sư phạm. IPO là phương pháp rào với bộ giải trong *ngẫu nhiên, bậc nhất*; Clarabel là phương pháp rào với bộ giải trong *xác định, Newton*. Cùng ý ngoài, chế độ tính toán đối ngược. Khi ràng buộc là nón lồi trên vài trăm biến, Newton trên rào là tối ưu; khi “biến” là chính sách sâu, bạn giữ rào và bỏ Hessian.

## Lớp khả vi vẫn gọi bộ giải rào chắn

Agrawal, Amos, Barratt, Boyd, Diamond và Kolter (NeurIPS 2019) giới thiệu **cvxpylayers**: một bài CVXPY trở thành lớp PyTorch / JAX mà lượt ngược vi phân ánh xạ nghiệm. Lượt thuận vẫn là IPM hoặc bộ giải nón bậc nhất; lượt ngược áp vi phân ẩn cho hệ KKT — cùng Jacobian mà phương pháp Newton phân rã trong chương này. Suốt 2022–2026 khuôn mẫu này là chuẩn trong MPC khả vi, dự báo có cấu trúc, và kiến trúc “tối ưu như một lớp”: bạn *không* bung gradient descent qua 50 bước chiếu nếu bộ giải rào trả nghiệm và một phân rã tái dùng cho adjoint.

Đó là chuyển giao sâu nhất của Chương 15: hệ Newton của đường trung tâm không chỉ là thuật toán cho $$x^\star(t)$$, mà còn là ánh xạ tuyến tính cho phép hệ học coi `solve()` như một nguyên thủy khả vi.

## Nguồn

- P. J. Goulart, Y. Chen, “Clarabel: An interior-point solver for conic programs with quadratic objectives,” 2024. [arXiv:2405.12762](https://arxiv.org/abs/2405.12762)
- Ghi chú phát hành CVXPY 1.5: Clarabel thay ECOS làm mặc định cho các lớp bài từng thuộc ECOS.
- Y. Liu, J. Ding, X. Liu, “IPO: Interior-Point Policy Optimization under Constraints,” AAAI 2020.
- J. Ji et al., “OmniSafe: An Infrastructure for Accelerating Safe Reinforcement Learning Research,” JMLR 25(285), 2024; “Safety Gymnasium,” NeurIPS 2023 Datasets.
- A. Agrawal, B. Amos, S. Barratt, S. Boyd, S. Diamond, J. Z. Kolter, “Differentiable Convex Optimization Layers,” NeurIPS 2019 (cvxpylayers; vẫn là giao diện 2022–2026).
