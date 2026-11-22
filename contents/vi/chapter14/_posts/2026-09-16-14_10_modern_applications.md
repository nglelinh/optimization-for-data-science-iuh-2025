---
layout: post
title: 14-10 Ứng dụng hiện đại của phương pháp Newton (2022–2026)
chapter: '14'
order: 18
owner: Nguyen Le Linh
categories:
- chapter14
lang: vi
lesson_type: optional
---

Phương pháp Newton trong chương này dựa trên mô hình bậc hai cục bộ chính xác

$$
x^{+} = x - t\, \bigl(\nabla^2 f(x)\bigr)^{-1}\nabla f(x),
$$

đi kèm các khái niệm đại lượng giảm Newton (Newton decrement), tính bất biến affine và tính tự hài hòa. Với các mô hình ngôn ngữ lớn, ma trận Hessian đầy đủ không thể lưu trữ trong bộ nhớ; tuy nhiên, cùng một ý tưởng cốt lõi — tiền điều kiện theo độ cong rồi thực hiện bước cập nhật có giảm chấn — đã giúp một số thuật toán giai đoạn 2022–2026 vượt qua Adam đã tinh chỉnh. Bài này mang tính khảo sát: với mỗi phương pháp dưới đây, hãy chú ý cách người ta xấp xỉ ma trận Hessian (dạng đường chéo hoặc tích Kronecker) và những phần nào được lược bỏ để bước cập nhật vẫn tính được trong thực tế.

Các trường hợp dưới đây đều là triển khai thực tế hoặc kết quả thực nghiệm đã qua phản biện. Khác với phần giới thiệu ngắn gọn về Sophia ở Chương 26, mục này tập trung làm rõ *vì sao* tiền điều kiện kiểu Newton có thể đạt chi phí tính toán thấp hơn dự kiến.

## Sophia: Hessian đường chéo cho tiền huấn luyện mô hình ngôn ngữ

Liu, Li, Hall, Liang và Ma (ICLR 2024) đề xuất **Sophia** (*Second-order Clipped Stochastic Optimization*). Bước cập nhật lấy trung bình động hàm mũ của gradient ngẫu nhiên chia cho trung bình động hàm mũ của ước lượng Hessian *đường chéo*, sau đó cắt ngưỡng (clip) theo từng tọa độ. Vì ước lượng Hessian chỉ được cập nhật định kỳ sau mỗi vài bước, chi phí trung bình mỗi bước gần tương đương Adam. Bài báo xét hai bộ ước lượng đường chéo Hessian: bộ ước lượng Hutchinson dùng tích Hessian–vector, và bộ ước lượng Gauss–Newton–Bartlett lấy mẫu nhãn từ phân phối dự báo rồi dùng bình phương gradient của hàm mất mát trên mẫu đó — tuy có độ chệch nhưng luôn không âm và rẻ về mặt tính toán.

Trên các mô hình kiểu GPT có quy mô từ 125 triệu đến 1,5 tỷ tham số, Sophia đạt cùng mức perplexity trên tập kiểm định với khoảng một nửa số bước so với Adam; do chi phí mỗi bước tương đương, tổng chi phí tính toán và thời gian chạy thực tế (wall-clock time) cũng giảm khoảng một nửa. Kết quả lý thuyết (trên một mô hình lồi mạnh đơn giản hóa) cho thấy thời gian hội tụ không còn phụ thuộc mạnh vào số điều kiện khi mỗi tọa độ được chuẩn hóa theo độ cong riêng — tương ứng với trực giác bất biến affine ở [14-02-02]({% multilang_post_url contents/chapter14/2021-03-26-14_02_02_affine_invariance_of_newton_method %}) thu hẹp về nhóm phép biến đổi đường chéo.

Cơ chế cắt ngưỡng theo tọa độ đóng vai trò tương tự miền tin cậy (trust region): khi ước lượng Hessian cục bộ đã cũ hoặc không xác định dương, bước Newton thuần túy có thể tăng quá mạnh; việc cắt ngưỡng khôi phục tính ổn định của bước "Newton có giảm chấn" tương tự tìm kiếm đường backtracking. Mã nguồn chính thức: [Liuhong99/Sophia](https://github.com/Liuhong99/Sophia). Ở mức độ khảo sát, trọng tâm là nắm được công thức cập nhật của Sophia và lý do vì sao ma trận Hessian *đường chéo* là dạng xấp xỉ còn phù hợp với bộ nhớ GPU khi huấn luyện mô hình hàng tỷ tham số.

## K-FAC cho transformer, mạng tích chập và mạng đồ thị

Kronecker-Factored Approximate Curvature (K-FAC; Martens & Grosse, 2015) xấp xỉ ma trận Fisher / Gauss–Newton tổng quát của từng lớp mạng bằng tích Kronecker — đây là độ cong của hàm mất mát *kỳ vọng*, không phải Hessian thô, nhưng lại là đối tượng mà các phương pháp kiểu Newton trong học sâu thực sự nghịch đảo. Eschenhagen, Immer, Turner, Schneider và Hennig (NeurIPS 2023) mở rộng khung K-FAC cho các lớp *chia sẻ trọng số* như lớp tích chập, lớp hồi quy, mạng đồ thị (GNN) và transformer. Các tác giả phân biệt **K-FAC-expand** (tương ứng cách phân rã KFC trước đây) và **K-FAC-reduce**, chứng minh tính chính xác của từng biến thể trên mạng tuyến tính sâu trong chế độ chia sẻ trọng số tương ứng, đồng thời cho thấy cả hai đạt cùng ngưỡng chất lượng kiểm định trên GNN và Vision Transformer với khoảng 50–75% số bước của phương pháp bậc nhất kèm mức giảm thời gian chạy thực tế tương ứng.

Đây là dạng phương pháp Newton với phép nghịch đảo có cấu trúc: thuật toán vẫn giải hệ tuyến tính theo ma trận độ cong xấp xỉ, nhưng cấu trúc tích Kronecker thu nhỏ bài toán về kích thước ma trận hiệp phương sai của các giá trị kích hoạt thay vì kích thước toàn bộ ma trận trọng số. Nếu Sophia là xấp xỉ Newton trên đường chéo thì K-FAC là xấp xỉ Newton trên cấu trúc Kronecker. Câu hỏi cốt lõi tương tự phân tích hàm tự hài hòa: *ta chấp nhận tính phần độ cong nào và giữ lại tính bất biến nào?*

## Newton–Cholesky cho mô hình tuyến tính tổng quát trong scikit-learn

Ứng dụng hiện đại của phương pháp Newton không chỉ giới hạn ở mô hình ngôn ngữ. Từ phiên bản scikit-learn 1.2 (2022), thư viện bổ sung `solver="newton-cholesky"` cho các mô hình tuyến tính tổng quát (GLM) như `PoissonRegressor`, `GammaRegressor`, `TweedieRegressor`, và sau đó mở rộng sang hồi quy logistic nhị phân. Bộ giải thực hiện trực tiếp bước Newton–Raphson — tương đương phương pháp bình phương tối thiểu tái trọng số lặp (IRLS) — bằng cách phân rã Cholesky trên ma trận Hessian tường minh. Tài liệu thư viện nêu rõ đây là lựa chọn phù hợp khi số mẫu lớn hơn nhiều so với số đặc trưng ($$n_{\text{mẫu}} \gg n_{\text{đặc trưng}}$$, đặc biệt với biến mã hóa one-hot có hạng mục hiếm), trong đó bộ nhớ tăng theo bình phương số đặc trưng do phải lưu tường minh ma trận Hessian.

Đây là phương pháp Newton chính xác của Chương 14 mà không cần xấp xỉ. Ma trận Hessian IRLS của GLM có dạng ma trận Gram $$X^\top W X$$ với ma trận trọng số đường chéo $$W$$ phụ thuộc vào giá trị kỳ vọng hiện tại, và phân rã Cholesky cho cách tính ổn định số học khi áp dụng $$(\nabla^2 f)^{-1}$$. Người học có thể chạy thử trực tiếp

```python
from sklearn.linear_model import PoissonRegressor
PoissonRegressor(solver="newton-cholesky", alpha=1e-4).fit(X, y)
```

và so sánh số vòng lặp với `solver="lbfgs"`. Khi ma trận thiết kế có nhiều mẫu và ít đặc trưng (dạng cao và hẹp), phương pháp Newton chính xác là một bộ giải thực tế và hiệu quả.

## Điểm cốt lõi cần ghi nhớ

AdaHessian (Yao, Gholami, Shen, Keutzer, Mahoney, AAAI 2021) là tiền thân trực tiếp của Sophia, kết hợp ước lượng đường chéo Hutchinson với động lượng kiểu Adam. SOAP và Shampoo (Chương 18) mở rộng từ đường chéo sang tiền điều kiện Kronecker hoặc theo cơ sở riêng. Trong khi đó, phương pháp Newton đầy đủ vẫn giữ vai trò trung tâm trong các mô hình tuyến tính tổng quát, phương pháp hạt nhân cỡ vừa, và các bước định tâm của phương pháp chắn cũng như phương pháp nguyên thủy–đối ngẫu ở Chương 15 và 17.

Có thể tóm gọn tinh thần của tối ưu bậc hai hiện đại trong học máy như sau: thay vì xây dựng tường minh toàn bộ $$\nabla^2 f$$ rồi phân rã ở mọi bước, đa số thuật toán ước lượng độ cong theo cấu trúc gọn nhẹ, giảm chấn hoặc cắt ngưỡng bước cập nhật, và phân bổ chi phí ước lượng độ cong qua nhiều vòng lặp. Trường hợp ngoại lệ — bộ giải Newton–Cholesky cho GLM — đồng thời cho thấy rằng khi kích thước đặc trưng đủ nhỏ để lập Hessian trực tiếp, phương pháp Newton chính xác vẫn hiệu quả hơn các phương pháp bậc nhất.

## Nguồn

- H. Liu, Z. Li, D. Hall, P. Liang, T. Ma, “Sophia: A Scalable Stochastic Second-order Optimizer for Language Model Pre-training,” ICLR 2024. [arXiv:2305.14342](https://arxiv.org/abs/2305.14342)
- R. Eschenhagen, A. Immer, R. Turner, F. Schneider, P. Hennig, “Kronecker-Factored Approximate Curvature for Modern Neural Network Architectures,” NeurIPS 2023.
- Z. Yao, A. Gholami, S. Shen, K. Keutzer, M. W. Mahoney, “ADAHESSIAN: An Adaptive Second Order Optimizer for Machine Learning,” AAAI 2021.
- Ghi chú phát hành scikit-learn 1.2 và tài liệu bộ giải `newton-cholesky` (2022–); PR GLM [#24637](https://github.com/scikit-learn/scikit-learn/pull/24637).
