---
layout: post
title: 15-09 Ứng dụng hiện đại của phương pháp rào chắn (2022–2026)
chapter: '15'
order: 15
owner: Nguyen Le Linh
categories:
- chapter15
lang: vi
lesson_type: optional
---

Hàm chắn logarit

$$
\phi(x) = -\sum_{i=1}^{m}\log\bigl(-h_i(x)\bigr)
$$

chuyển bài toán có ràng buộc bất đẳng thức thành một họ bài toán trơn không ràng buộc (hoặc chỉ có ràng buộc đẳng thức) theo tham số $$t$$. Đây vẫn là nền tảng cốt lõi của nhiều bộ giải tối ưu lồi trong thực tế, ngay cả khi người dùng không viết tường minh hàm `log`. Mục này khảo sát bốn ứng dụng thực tế giai đoạn 2022–2026 gắn trực tiếp với đường trung tâm của chương: bộ giải mặc định trong CVXPY, các bài toán nón trong tài chính và điều khiển, học tăng cường an toàn, và các lớp tối ưu khả vi.

## Clarabel: bộ giải điểm trong mặc định của CVXPY

Goulart và Chen (2024) giới thiệu **Clarabel**, một bộ giải điểm trong mã nguồn mở cho các bài toán tối ưu nón lồi có hàm mục tiêu bậc hai. Thuật toán sử dụng nhúng tự đối ngẫu đồng nhất (homogeneous self-dual embedding) kết hợp vòng lặp điểm trong: hàm chắn logarit (hoặc hàm chắn tự hài hòa tương ứng trên từng nón) giữ các điểm lặp trong phần trong của góc phần tư không âm, nón bậc hai, nón mũ, nón lũy thừa và nón nửa xác định dương (PSD), trong khi hệ phương trình Newton trên phần dư KKT đồng thời giảm sai số khả thi nguyên thủy, khả thi đối ngẫu và độ lệch bù. Clarabel cũng hỗ trợ phân rã chordal cho các bài toán quy hoạch nửa xác định (SDP) cỡ lớn.

Một thay đổi thực tiễn đáng chú ý là từ phiên bản CVXPY 1.5, Clarabel *thay thế ECOS làm bộ giải mặc định* cho các lớp bài toán mà trước đây ECOS đảm nhiệm (ghi chú phát hành CVXPY 1.5; Goulart & Chen, mục cài đặt). Các bài toán quy hoạch bậc hai (QP) thông thường vẫn thường dùng OSQP (dựa trên ADMM, Chương 21), nhưng LP, SOCP và nhiều mô hình nón mũ nay mặc định chạy bằng phương pháp điểm trong kiểu rào chắn. Nhờ đó, các mô hình viết theo [05-07]({% multilang_post_url contents/chapter05/2026-09-15-05_07_Modeling_with_DCP_CVXPY %}) trực tiếp sử dụng thuật toán Chương 15 ở tầng dưới:

```python
import cvxpy as cp
x = cp.Variable(n)
prob = cp.Problem(cp.Minimize(cp.sum_squares(A @ x - b)), [x >= 0, cp.norm(x, 2) <= 1])
prob.solve(solver=cp.CLARABEL)
```

Kiểm tra `prob.solver_stats` sau khi gọi hàm giải mặc định (khi không chọn OSQP) sẽ cho thấy bài toán đang được giải bằng một phương pháp bám đường trung tâm.

## Tối ưu danh mục, MPC và các bài toán QP nón

Cùng nhóm bộ giải này được dùng rộng rãi trong tối ưu danh mục trung bình–phương sai có ràng buộc rủi ro, quy hoạch bậc hai cho điều khiển dự báo mô hình (MPC), và các bài toán tối ưu vững cỡ nhỏ dạng nón. Các thí nghiệm số của Clarabel và những phiên bản chạy trên GPU sau này (Chương 17) thường lấy bài toán danh mục và điều khiển làm chuẩn đánh giá vì chúng vừa có hàm chắn tự hài hòa cho phương pháp Newton, vừa có cấu trúc thưa thuận lợi cho việc phân rã hệ KKT. Một bài toán danh mục chỉ-mua-dài kèm ràng buộc sai số bám dạng SOCP thực chất là bài toán đường trung tâm Chương 15 với ma trận Hessian gồm ma trận hiệp phương sai cộng thêm thành phần rào chắn trên đơn hình hoặc nón bậc hai.

Nguyên tắc thực hành vẫn nhất quán với Boyd & Vandenberghe, Chương 11: không cần tự cài đặt gradient chiếu trên nón khi bộ giải điểm trong đã có sẵn qua một lệnh `solve()`. Các phương pháp tách bậc nhất (như OSQP, SCS) có ưu thế khi cần khởi động ấm ở tần số cao (ví dụ 100 Hz), còn phương pháp chắn và điểm trong nổi trội khi cần độ chính xác cao và số chiều vẫn phù hợp để giải hệ Newton thưa.

## Hàm chắn logarit trong học tăng cường an toàn

Liu, Ding và Liu (*IPO: Interior-Point Policy Optimization under Constraints*, AAAI 2020) áp dụng hàm chắn logarit cho các ràng buộc chi phí trong quá trình quyết định Markov có ràng buộc (CMDP), sau đó tối ưu hàm mục tiêu trơn thu được bằng phương pháp bậc nhất kiểu PPO. Dù không giải bằng phương pháp Newton vì chính sách được tham số hóa bởi mạng nơ-ron, *ý tưởng chuyển đổi bài toán* vẫn là Chương 15: ràng buộc bất đẳng thức trở thành số hạng phạt có gradient tiến ra vô cùng ở biên, giúp các bước cập nhật duy trì tính khả thi chặt nếu xuất phát từ chính sách khả thi. Các thư viện như OmniSafe (Ji, Zhou, Zhang, Dai, Pan, Sun, Huang, Geng, Liu, Yang; JMLR 2024) và Safety Gymnasium (Ji et al., NeurIPS 2023 Datasets) tích hợp IPO song song với PPO-Lagrangian, đưa hàm chắn logarit trực tiếp vào quy trình tối ưu chính sách.

Sự đối chiếu này làm rõ bản chất hai tầng của phương pháp: IPO là phương pháp chắn dùng bộ giải bên trong *ngẫu nhiên, bậc nhất*; Clarabel là phương pháp chắn dùng bộ giải bên trong *xác định, bậc hai (Newton)*. Khi ràng buộc là nón lồi trên vài trăm đến vài nghìn biến, giải hệ Newton trên hàm chắn là lựa chọn tối ưu; khi biến tối ưu là trọng số mạng nơ-ron sâu, ta giữ lại hàm chắn nhưng bỏ qua ma trận Hessian.

## Các lớp tối ưu khả vi dựa trên bộ giải điểm trong

Agrawal, Amos, Barratt, Boyd, Diamond và Kolter (NeurIPS 2019) giới thiệu **cvxpylayers**, cho phép nhúng một bài toán CVXPY thành một lớp khả vi trong PyTorch hoặc JAX. Ở lượt truyền xuôi (forward pass), hệ thống giải bài toán bằng bộ giải điểm trong hoặc bộ giải nón bậc nhất; ở lượt truyền ngược (backward pass), đạo hàm được tính bằng vi phân ẩn trên hệ điều kiện KKT — sử dụng chính ma trận Jacobian mà phương pháp Newton đã phân rã trong chương này. Giai đoạn 2022–2026, cách tiếp cận này trở thành khuôn mẫu tiêu chuẩn trong MPC khả vi, dự báo có cấu trúc và các kiến trúc "tối ưu như một lớp" (optimization as a layer), giúp tránh phải khai triển ngược qua hàng chục bước gradient chiếu.

Nói cách khác, hệ phương trình Newton của đường trung tâm không chỉ dùng để tính điểm $$x^\star(t)$$, mà còn cung cấp ánh xạ tuyến tính cho phép các hệ thống học sâu lấy đạo hàm trực tiếp qua lời gọi `solve()`.

## Nguồn

- P. J. Goulart, Y. Chen, “Clarabel: An interior-point solver for conic programs with quadratic objectives,” 2024. [arXiv:2405.12762](https://arxiv.org/abs/2405.12762)
- Ghi chú phát hành CVXPY 1.5: Clarabel thay ECOS làm mặc định cho các lớp bài từng thuộc ECOS.
- Y. Liu, J. Ding, X. Liu, “IPO: Interior-Point Policy Optimization under Constraints,” AAAI 2020.
- J. Ji et al., “OmniSafe: An Infrastructure for Accelerating Safe Reinforcement Learning Research,” JMLR 25(285), 2024; “Safety Gymnasium,” NeurIPS 2023 Datasets.
- A. Agrawal, B. Amos, S. Barratt, S. Boyd, S. Diamond, J. Z. Kolter, “Differentiable Convex Optimization Layers,” NeurIPS 2019 (cvxpylayers; vẫn là giao diện 2022–2026).
