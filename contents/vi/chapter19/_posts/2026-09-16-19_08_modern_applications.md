---
layout: post
title: 19-08 Ứng dụng hiện đại của phương pháp proximal Newton (2022–2026)
chapter: '19'
order: 12
owner: Nguyen Le Linh
categories:
- chapter19
lang: vi
lesson_type: optional
---

Nhiều thuật toán tối ưu cổ điển bị bỏ lại phía sau khi dữ liệu phình to lên hàng chục nghìn chiều, nhưng phương pháp Newton proximal giai đoạn 2022–2026 lại có một hành trình ngược lại: càng ở những bài toán thống kê nhiều chiều gai góc — như ước lượng đồ thị thưa (graphical lasso) với hàng chục nghìn nút, hay mô hình tuyến tính tổng quát nhiều biến (GLM) tích hợp trong `scikit-learn` — sự kết hợp giữa **độ cong bậc hai cục bộ** và **sàng lọc tập hoạt động (active-set screening)** càng tỏ ra không thể thay thế.

## Bản đồ kiến thức nền: Ba xu hướng ứng dụng Newton proximal giai đoạn 2022–2026

Để thấy lý thuyết Chương 19 đang vận hành như thế nào trong các thư viện thực chiến hôm nay, hãy điểm qua ba trục phát triển chính:

- **Sàng lọc an toàn (Safe Screening) + Tập tự do cho Graphical Lasso quy mô lớn:** Các phiên bản kế thừa `QUIC` (như BigQUIC và các biến thể phân khối song song) phân rã ma trận hiệp phương sai mẫu thành các thành phần liên thông trước khi gọi Newton proximal, mở rộng khả năng giải từ vài trăm lên hàng chục nghìn biến.
- **Bộ giải Newton–Cholesky cho GLM trong hệ sinh thái Python:** Trong các phiên bản mới của `scikit-learn` và `glum`, khi số mẫu $$n \gg p$$, việc tính trực tiếp Hessian $$X^T W X$$ và giải bằng Cholesky (hoặc kết hợp hạ tọa độ có phạt $$\ell_1/\ell_2$$) nhanh hơn gấp nhiều lần so với L-BFGS thuần túy.
- **Newton proximal không chính xác có điều khiển thích nghi (Adaptive Inexactness):** Thay vì giải bài toán con bên trong tới sai số máy ngay từ những vòng lặp đầu còn xa nghiệm, các bộ giải hiện đại nới lỏng dung sai bài toán con ở giai đoạn đầu và chỉ siết chặt khi gần nghiệm — giữ nguyên hội tụ siêu tuyến tính nhưng cắt giảm 50–70% thời gian chạy.

### Khung giải thích (nên đọc chậm): Tính nhanh mức tiết kiệm bộ nhớ nhờ tập hoạt động trong Graphical Lasso

Xét bài toán ước lượng ma trận chính xác đối xứng $$\Theta \in \mathbb{S}^p$$ với $$p = 1{,}000$$ biến (ví dụ mạng biểu hiện 1.000 gen):

1. **Kích thước bài toán không khai thác độ thưa:**
   - Số biến tự do trong ma trận đối xứng $$\Theta$$ là $$N = \frac{p(p+1)}{2} \approx 500{,}500$$ biến.
   - Nếu lập trực tiếp ma trận Hessian đầy đủ $$\Theta^{-1} \otimes \Theta^{-1}$$ kích thước $$N \times N$$, số phần tử sẽ lên tới $$N^2 \approx 2.5 \times 10^{11}$$ — tương đương **2 Terabyte RAM**, hoàn toàn bất khả thi!
2. **Sức mạnh của tập tự do (Free Set) trong Proximal Newton (`QUIC`):**
   - Nhờ phạt $$\lambda\|\Theta\|_1$$, giả sử mỗi gen chỉ kết nối trung bình với $$10$$ gen khác, nên số cạnh khác $$0$$ (tập tự do) chỉ là $$s \approx \frac{1{,}000 \times 10}{2} + 1{,}000 = 6{,}000$$ biến!
   - Bài toán con bậc hai được hạ tọa độ giải **chỉ trên $$6{,}000$$ tọa độ tự do** thay vì $$500{,}500$$ tọa độ — giảm kích thước không gian tìm kiếm gần **83 lần**, đồng thời mỗi phép cập nhật tọa độ chỉ dùng hai cột của ma trận $$W = \Theta^{-1}$$ đã tính sẵn nên bộ nhớ chỉ tốn cỡ $$p^2 \approx 8\text{ MB}$$!

---

Phương pháp proximal Newton xây dựng mô hình bậc hai cho thành phần *trơn* $$g$$ và giữ nguyên thành phần *không trơn* $$h$$ trong bài toán con:

$$
v^{+} = \arg\min_v\ \nabla g(x)^\top v + \tfrac12 v^\top H v + h(x+v),\qquad H\approx\nabla^2 g(x).
$$

Khi $$h = \lambda\|\cdot\|_1$$, bài toán con có dạng Lasso; khi $$h$$ là hàm chỉ thị của một tập lồi, bài toán con trở thành quy hoạch bậc hai có ràng buộc. Khung lý thuyết của Lee, Sun và Saunders (2014) cùng các thư viện kinh điển (glmnet, QUIC) vẫn giữ nguyên giá trị cốt lõi. Điểm thay đổi lớn trong giai đoạn 2022–2026 nằm ở quy mô bài toán: các bộ giải tổng hợp bậc hai hiện nay giải được toàn bộ đường điều chuẩn cho ma trận chính xác (precision matrix) nhiều chiều mà các thuật toán bậc nhất như glasso không kham nổi, đồng thời các thư viện GLM phổ biến đã tích hợp thêm bộ giải Newton–Cholesky tường minh — tức proximal Newton với $$h = \frac{\alpha}{2}\|\cdot\|_2^2$$.

## Mô hình đồ thị: từ QUIC đến MARS

QUIC (Hsieh, Sustik, Dhillon, Ravikumar, JMLR 2014) là ví dụ kinh điển đã nêu ở bài 19-05: áp dụng mô hình bậc hai Newton lên $$-\log\det\Theta + \langle S, \Theta \rangle$$ kèm phạt $$\ell_1$$, giải bài toán con bằng hạ theo tọa độ và đạt tốc độ hội tụ siêu tuyến tính. Bước tiến tiếp theo của thập niên 2020 cho ước lượng ma trận chính xác *nhiều chiều* là **MARS** (Li, Jiang, Sun, JMLR 2023). Thuật toán này tối ưu hàm mất mát D-trace có phạt $$\ell_1$$ thay cho glasso, kết hợp kỹ thuật sàng lọc thích nghi (loại bỏ các tọa độ đã được điều kiện KKT xác nhận bằng $$0$$) với bộ giải **hàm Lagrange tăng cường kết hợp Newton bán trơn (semismooth Newton augmented Lagrangian — SSNAL)** trên bài toán đối ngẫu đã rút gọn. Các tác giả báo cáo giải được toàn bộ đường điều chuẩn cho bài toán $$p \approx 2 \times 10^4$$ (dữ liệu biểu hiện gen ung thư vú, tương ứng hàng trăm triệu biến đối ngẫu trước khi sàng lọc) — quy mô mà glasso và QUIC gặp bế tắc.

Hai nguyên lý cốt lõi của Chương 19 vẫn được bảo toàn nguyên vẹn. Thứ nhất, phép toán tốn kém nhất vẫn là *ánh xạ proximal có tỉ lệ* (ở đây là hệ Newton đối ngẫu), chứ không phải việc lưu toàn bộ ma trận Hessian dày đặc $$p^2$$ phần tử. Thứ hai, chiến lược tập hoạt động / sàng lọc là yếu tố giúp proximal Newton vượt trội proximal gradient: một khi tập giá (support — tập các tọa độ khác 0) được nhận diện, thuật toán đạt hội tụ bậc hai trên tập biến tự do đúng như phân tích cục bộ ở bài 19-04. Mã nguồn được công bố tại [QianLI-QL/MARS](https://github.com/QianLI-QL/MARS).

## GLM trong scikit-learn: dùng Newton khi $$h$$ bậc hai, dùng L-BFGS khi không

Từ scikit-learn 1.2 (2022), `PoissonRegressor(..., solver="newton-cholesky")` và phần mở rộng sau đó cho hồi quy logistic tạo trực tiếp ma trận $$H = \nabla^2 g + \alpha I$$ rồi giải bước Newton bằng phân rã Cholesky. Hạng tử phạt $$\alpha\|w\|_2^2$$ chính là điều chuẩn Tikhonov / ridge: dưới góc nhìn bài toán tổng hợp với $$g$$ là âm log-likelihood và $$h = \frac{\alpha}{2}\|w\|_2^2$$, ánh xạ proximal của một hàm bậc hai lồi mạnh trở thành một hệ phương trình tuyến tính — nên proximal Newton suy biến về phương pháp Newton có điều chuẩn (damped Newton). Đây là minh họa thực tế cho bảng so sánh ở bài 19-03: khi $$h$$ dễ xử lý (ridge, ràng buộc hộp, hoặc $$\ell_1$$ với hạ theo tọa độ) và số đặc trưng $$d$$ nhỏ, việc lập Hessian của $$g$$ mang lại lợi ích rõ rệt.

Trong thực hành, L-BFGS (`solver="lbfgs"`) phù hợp với bài toán nhiều đặc trưng hoặc có ràng buộc hộp (Chương 18), còn SAGA phù hợp với bài toán rất lớn, thưa có phạt $$\ell_1$$ (Chương 26). Proximal Newton chiếm vị trí trung gian quan trọng: số chiều $$d$$ vừa phải, chi phí tính $$g$$ cao và $$h$$ có cấu trúc tốt.

## glmnet và LIBLINEAR: công cụ chủ lực cho GLM thưa

**glmnet** (Friedman, Hastie, Tibshirani — đã dẫn ở bài 19-05) đến năm 2026 vẫn là bộ giải tiêu chuẩn cho đường điều chuẩn trong R và các gói giao tiếp Python: vòng lặp hạ theo tọa độ trên bài toán con bậc hai nằm bên trong vòng ngoài proximal-Newton / IRLS. Bộ giải Newton miền tin cậy của LIBLINEAR cho hồi quy logistic / SVM điều chuẩn $$\ell_2$$ và NewGLMNET cho $$\ell_1$$ cũng vận hành theo cùng nguyên lý với bộ giải con khác nhau. Đây là những công cụ thực tế vẫn đang huấn luyện mô hình tuyến tính thưa trên dữ liệu tỷ lệ nhấp (click-through) và dữ liệu y tế dạng bảng hàng ngày.

Bước phát triển của giai đoạn 2022–2026 tập trung vào mở rộng quy mô và tích hợp hệ thống: bản viết lại GLM trong scikit-learn, các công cụ tính toán ngoài bộ nhớ chính (out-of-core) như `biglasso`, và các bộ giải dựa trên SSNAL (hướng nghiên cứu của Sun–Toh) giúp đưa cùng khung vòng ngoài đáng tin cậy này lên các bài toán vượt quá giới hạn bộ nhớ RAM của `glmnet`.

## Cách phân biệt bài toán proximal Newton với phương pháp bậc nhất

Hãy quan sát bài toán con bên trong ở mỗi vòng lặp. Nếu mỗi bước giải một bài toán *toàn phương cộng $$h$$* (Lasso, QP có ràng buộc hộp, hoặc hệ Newton đối ngẫu trên nón) tới độ chính xác vừa đủ rồi tìm kiếm theo đường thẳng trên hàm mục tiêu tổng hợp, đó là lớp thuật toán Chương 19 (MARS, QUIC, glmnet, Newton–Cholesky). Ngược lại, nếu mỗi bước chỉ gồm một bước gradient cộng một phép co ngưỡng dạng đóng, đó là lớp thuật toán bậc nhất Chương 09 (ISTA, FISTA, SAGA). Các phương án lai (giải bài toán con không chính xác, dùng xấp xỉ quasi-Newton $$H_k$$) thuộc bài 19-06 và là cách mở rộng khi $$\nabla^2 g$$ chỉ có thể tiếp cận qua tích Hessian–vector.

## Nguồn

- Q. Li, B. Jiang, D. Sun, “MARS: A Second-Order Reduction Algorithm for High-Dimensional Sparse Precision Matrices Estimation,” JMLR 24, 2023. [bài báo](https://jmlr.org/papers/v24/21-0699.html)
- C.-J. Hsieh, M. A. Sustik, I. S. Dhillon, P. Ravikumar, “QUIC: Quadratic Approximation for Sparse Inverse Covariance Estimation,” JMLR 15, 2014.
- J. Lee, Y. Sun, M. A. Saunders, “Proximal Newton-type methods for minimizing composite functions,” SIAM J. Optim. 24(3), 2014.
- J. Friedman, T. Hastie, R. Tibshirani, “Regularization paths for generalized linear models via coordinate descent,” J. Stat. Softw. 33(1), 2010 (glmnet; vẫn là đường sản xuất).
- Bộ giải GLM `newton-cholesky` của scikit-learn 1.2+.
