---
layout: post
title: 18-08 Ứng dụng hiện đại của phương pháp quasi-Newton (2022–2026)
chapter: '18'
order: 9
owner: Nguyen Le Linh
categories:
- chapter18
lang: vi
lesson_type: optional
---

Trong cơn sốt học sâu hiện đại, nhiều người tưởng rằng Adam đã "đánh bại" mọi thuật toán tối ưu cổ điển. Thế nhưng giai đoạn 2022–2026 lại chứng kiến sự trở lại ngoạn mục của tư duy Quasi-Newton trên hai mặt trận lớn: trong **học máy khoa học (Scientific ML / PINN)**, chiến lược *Adam khởi động + L-BFGS về đích* là tiêu chuẩn bắt buộc để vượt qua số điều kiện khủng khiếp của phương trình đạo hàm riêng; còn trong **huấn luyện mô hình nền tảng quy mô lớn**, các bộ tiền điều kiện có cấu trúc như Shampoo và SOAP chính là hậu duệ phân rã Kronecker mang chung dòng máu độ cong với BFGS.

## Bản đồ kiến thức nền: Ba hướng phát triển của Quasi-Newton trong giai đoạn 2022–2026

Để liên kết lý thuyết Chương 18 với các công trình hàng đầu tại ICML/NeurIPS gần đây, hãy chú ý ba cầu nối then chốt:

- **Số điều kiện phổ của PINN và bài toán ngược (Inverse Problems):** Khác với phân loại ảnh thông thường, hàm mất mát của mạng nơ-ron vật lý chứa đạo hàm bậc hai (toán tử Laplace, Navier–Stokes), khiến tỉ số trị riêng lớn nhất trên nhỏ nhất $$\kappa = \lambda_{\max}/\lambda_{\min}$$ dễ dàng vượt $$10^4\text{–}10^6$$. Bộ tối ưu bậc nhất bị kẹt sớm, còn L-BFGS nén phổ độ cong và hạ sai số xuống thêm 2–4 bậc độ lớn.
- **Chiến lược lai hai giai đoạn (Adam → L-BFGS):** L-BFGS đòi hỏi đánh giá gradient toàn lô (full-batch) chính xác và dễ mắc kẹt ở vùng yên ngựa không lồi nếu khởi tạo ngẫu nhiên. Chạy Adam trước để đi vào thung lũng lồi cục bộ rồi chuyển sang L-BFGS tận dụng trọn vẹn ưu thế của cả hai thế giới.
- **Tiền điều kiện cấu trúc Kronecker (K-FAC, Shampoo, SOAP):** Thay vì xấp xỉ Hessian của toàn bộ mạng bằng một ma trận khổng lồ, các thuật toán này xấp xỉ độ cong cho từng ma trận trọng số $$W \in \mathbb{R}^{d_1 \times d_2}$$ dưới dạng tích Kronecker $$L \otimes R$$, giữ chi phí bộ nhớ cỡ $$O(d_1^2 + d_2^2)$$ nhưng nắm bắt được tương quan chéo giữa các tham số.

### Khung giải thích (nên đọc chậm): Minh họa vì sao số điều kiện $$\kappa = 10^4$$ làm Adam chững lại còn L-BFGS bứt phá

Xét một hàm mục tiêu bậc hai mô phỏng độ cong điển hình của bài toán PDE rời rạc hóa 2 chế độ (tần số thấp và tần số cao):

$$f(w_1, w_2) = \frac{1}{2}\left(w_1^2 + 10{,}000\, w_2^2\right), \qquad \kappa = \frac{\lambda_{\max}}{\lambda_{\min}} = 10{,}000.$$

1. **Hạ gradient chuẩn không tiền điều kiện:** Để ổn định trên trục $$w_2$$, bước học buộc phải thỏa mãn $$\eta < \frac{2}{\lambda_{\max}} = 2 \times 10^{-4}$$. Với $$\eta = 10^{-4}$$, sai số dọc trục $$w_1$$ sau mỗi bước chỉ nhân với $$(1 - 10^{-4}) = 0.9999$$. Muốn giảm sai số xuống $$10^{-4}$$, ta cần cỡ $$\frac{\ln(10^4)}{10^{-4}} \approx 92{,}100$$ vòng lặp!
2. **Hiệu quả tiền điều kiện của Quasi-Newton / L-BFGS:** Chỉ sau $$2$$ bước đo cặp $$(s, y)$$ dọc hai hướng độc lập, xấp xỉ $$H_2$$ khôi phục chính xác ma trận nghịch đảo độ cong $$\operatorname{diag}(1, \; 10^{-4})$$. Số điều kiện hiệu dụng của hệ đã tiền điều kiện $$H_2 \nabla^2 f$$ sụt từ $$\kappa = 10{,}000$$ xuống đúng $$\kappa_{\text{eff}} = 1$$ — và thuật toán nhảy thẳng tới nghiệm tối ưu $$(0, 0)$$ chỉ trong **1 bước Newton**!
3. **Liên hệ thực tế với PINN:** Trong mạng nơ-ron có hàng chục nghìn tham số, L-BFGS (với $$m = 50\text{–}100$$) loại bỏ vài chục chế độ trị riêng lớn nhất gây dao động mạnh, làm giảm $$\kappa_{\text{eff}}$$ hàng trăm lần và đưa sai số PDE từ $$10^{-2}$$ xuống $$10^{-6}$$ chỉ sau vài trăm vòng lặp.

---

Phương pháp quasi-Newton thay ma trận Hessian $$\nabla^2 f(x)$$ bằng một ma trận xấp xỉ $$B$$ thỏa mãn phương trình secant $$B^{+}s = y$$ và (với BFGS/L-BFGS) bảo toàn tính xác định dương dưới điều kiện độ cong $$y^\top s > 0$$. Những ứng dụng tiêu biểu giai đoạn 2022–2026 gắn trực tiếp với chương này không phải các bộ tối ưu tiền huấn luyện LLM ước lượng Hessian đường chéo (vốn thuộc nhóm Newton / Sophia ở Chương 14), mà là các thuật toán lưu giữ lịch sử ngắn các cặp $$(s, y)$$ — tiêu biểu là L-BFGS trong học máy khoa học và mô hình dữ liệu dạng bảng — cùng các bộ tiền điều kiện có cấu trúc (Shampoo / SOAP) mang họ hàng phân rã Kronecker với BFGS.

## PINN: dùng Adam để tiến gần, dùng L-BFGS để hội tụ chính xác

Mạng nơ-ron tích hợp tri thức vật lý (PINN) cực tiểu hóa phần dư chứa các toán tử vi phân. Chính các toán tử vi phân này khiến bài toán tối ưu có số điều kiện rất xấu: phổ trị riêng của Hessian bám theo phổ của phương trình đạo hàm riêng (PDE) rời rạc hóa thay vì phổ của hàm mất mát entropy chéo. Rathore, Lei, Frangella, Lu và Udell (ICML 2024) so sánh Adam, L-BFGS và tổ hợp **Adam+L-BFGS**, cho thấy tổ hợp vượt trội từng phương pháp đơn lẻ, đồng thời đề xuất NysNewton-CG như một cải tiến bậc hai bổ sung. Đóng góp lý thuyết của bài báo là làm rõ mối liên hệ giữa toán tử vi phân điều kiện xấu và Hessian điều kiện xấu của PINN — giải thích vì sao các phương pháp dựa trên phương trình secant (tích lũy thông tin độ cong dọc quỹ đạo) vượt trội các phương pháp thích nghi đường chéo vốn bỏ qua sự tương tác ngoài đường chéo của phần dư.

Quy trình huấn luyện phổ biến trong thực tế — hình thành từ trước năm 2024 và vẫn là chuẩn mực đến năm 2026 — là chạy Adam để đưa nghiệm vào vùng lồi bậc hai (quadratic bowl), sau đó chuyển sang L-BFGS kèm tìm kiếm theo đường thẳng thỏa mãn điều kiện Wolfe. Urbán, Stefanou, Pons et al. (2024, [arXiv:2405.04230](https://arxiv.org/abs/2405.04230)) phân tích chiến lược hai giai đoạn này và định lượng mức cải thiện độ chính xác mà BFGS / L-BFGS mang lại sau pha khởi đầu bằng Adam. Đây chính là ứng dụng trực tiếp của thuật toán đệ quy hai vòng ở bài 18-07.

## BFGS tự co giãn trên PINN, PIKAN và DeepONet

Kiyani, Shukla, Urbán, Darbon và Karniadakis (2025, [arXiv:2501.16371](https://arxiv.org/abs/2501.16371)) quay lại lớp Broyden ở bài 18-05. **BFGS tự co giãn (self-scaled BFGS)** và **Broyden tự co giãn** hiệu chỉnh tỷ lệ của xấp xỉ Hessian dựa trên cặp độ cong gần nhất — một cơ chế ổn định kinh điển (Oren–Luenberger) giúp hạn chế sự biến động quá lớn của độ dài bước trên phần dư PDE. Trên các phương trình Burgers, Allen–Cahn, Kuramoto–Sivashinsky, Ginzburg–Landau cũng như trên mạng Kolmogorov–Arnold tích hợp vật lý (PIKAN), các tác giả ghi nhận mức giảm phần dư theo hàng bậc độ lớn mà *không* cần kỹ thuật gán trọng số hàm mất mát thích nghi thường thấy ở PINN. Cùng công thức cập nhật này cũng cải thiện hiệu quả huấn luyện DeepONet.

Có thể xem đây là minh họa thực nghiệm trực tiếp cho lớp Broyden: $$\phi = 0$$ là BFGS, $$\phi = 1$$ là DFP, còn phiên bản tự co giãn sử dụng tham số $$\phi$$ phụ thuộc dữ liệu kết hợp hệ số co giãn vô hướng. Điều kiện độ cong $$y^\top s > 0$$ được đảm bảo bởi bước tìm kiếm theo đường thẳng; khi điều kiện này không thỏa mãn, cặp $$(s, y)$$ sẽ bị bỏ qua — đúng như cơ chế bảo vệ tiêu chuẩn trong mọi cài đặt L-BFGS.

## L-BFGS-B: lựa chọn mặc định tiêu chuẩn trong học máy dữ liệu bảng

Hàm `LogisticRegression(solver="lbfgs")` và họ mô hình tuyến tính tổng quát (GLM) trong scikit-learn (`solver="lbfgs"`, dùng mặc định bên cạnh `newton-cholesky`) đều gọi bộ giải **L-BFGS-B** của SciPy (L-BFGS có ràng buộc hộp). Với số mẫu $$n$$ ở mức hàng chục nghìn và số đặc trưng $$d$$ từ vài trăm đến vài nghìn, L-BFGS-B vẫn là lựa chọn phù hợp nhất: rẻ hơn so với tính trực tiếp Hessian, chính xác hơn SGD trên các bài toán GLM lồi và hỗ trợ khởi động ấm dọc theo đường điều chuẩn. Hugging Face Trainer cũng cung cấp tùy chọn `optim="lbfgs"` cho các bài toán tinh chỉnh cỡ nhỏ. Điểm rút ra quan trọng — đối lập với câu chuyện Sophia ở bài toán LLM lớn — là: *khi mô hình đủ nhỏ để lưu xấp xỉ Hessian bằng vài chục vector trên CPU, phương pháp quasi-Newton thường vượt trội Adam*.

Một đoạn mã kiểm chứng ngắn gọn:

```python
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(solver="lbfgs", max_iter=200, C=1.0)
clf.fit(X, y)
print(clf.n_iter_)
```

Hãy so sánh với `solver="newton-cholesky"` (Chương 14) trên ma trận thiết kế nhiều mẫu ($$n \gg d$$) và với `solver="saga"` trên ma trận thiết kế nhiều đặc trưng ($$d \gg n$$). Việc chọn giữa Newton, L-BFGS và phương pháp bậc nhất giảm phương sai phụ thuộc trực tiếp vào kích thước $$(n, d)$$ và cấu trúc ràng buộc.

## SOAP: hệ cơ sở vector riêng của Shampoo như một phương pháp quasi-Newton có cấu trúc

Vyas, Morwani, Zhao, Kwun, Shapira, Brandfonbrener, Janson và Kakade (ICLR 2025) giới thiệu **SOAP** (*ShampoO with Adam in the Preconditioner's eigenbasis*). Shampoo (Gupta, Koren, Singer, 2018; cùng các triển khai quy mô lớn giai đoạn 2023–2024) duy trì các ma trận mô-men bậc hai phân rã theo tích Kronecker, mang bản chất lai giữa quasi-Newton và gradient tự nhiên có cấu trúc. SOAP chứng minh rằng Shampoo với nghịch đảo căn bậc hai tương đương với việc chạy Adafactor trong hệ cơ sở vector riêng của Shampoo, từ đó *thay* Adafactor bằng AdamW trong hệ cơ sở biến đổi chậm này. Trên các mô hình ngôn ngữ 360 triệu và 660 triệu tham số ở chế độ kích thước lô lớn, SOAP giảm hơn 40% số vòng lặp và hơn 35% thời gian chạy thực tế (wall-clock time) so với AdamW, đồng thời giảm khoảng 20% so với Shampoo.

Dù không dùng các cặp $$(s, y)$$ như L-BFGS, SOAP chia sẻ chung nguyên lý thiết kế với DFP/BFGS: *ước lượng thông tin độ cong xác định dương, dễ nghịch đảo với chi phí thấp và cập nhật theo chu kỳ chậm hơn tốc độ cập nhật gradient.* Siêu tham số tần suất phân rã trị riêng đóng vai trò tương tự kích thước bộ nhớ $$m$$ của L-BFGS. Trong giảng dạy và thực hành, có thể đặt SOAP cạnh K-FAC (Chương 14) khi thảo luận lý thuyết, và đặt L-BFGS cạnh PINN trong bài thực hành.

## Nguồn

- P. Rathore, W. Lei, Z. Frangella, L. Lu, M. Udell, “Challenges in Training PINNs: A Loss Landscape Perspective,” ICML 2024, PMLR 235.
- W. Urbán et al., “Unveiling the optimization process of Physics Informed Neural Networks,” 2024. [arXiv:2405.04230](https://arxiv.org/abs/2405.04230)
- E. Kiyani, K. Shukla, J. F. Urbán, J. Darbon, G. E. Karniadakis, “Optimizing the Optimizer for Physics-Informed Neural Networks and Kolmogorov-Arnold Networks,” 2025. [arXiv:2501.16371](https://arxiv.org/abs/2501.16371)
- N. Vyas et al., “SOAP: Improving and Stabilizing Shampoo using Adam,” ICLR 2025. [arXiv:2409.11321](https://arxiv.org/abs/2409.11321)
- SciPy `L-BFGS-B`; scikit-learn `LogisticRegression(solver="lbfgs")`.
