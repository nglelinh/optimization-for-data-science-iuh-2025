---
layout: post
title: 14-10 Ứng dụng hiện đại của phương pháp Newton (2022–2026)
chapter: '14'
order: 19
owner: Nguyen Le Linh
categories:
- chapter14
lang: vi
lesson_type: optional
---

Phương pháp Newton trong chương này là mô hình toàn phương địa phương đúng

$$
x^{+} = x - t\, \bigl(\nabla^2 f(x)\bigr)^{-1}\nabla f(x),
$$

kèm Newton decrement, bất biến affine, và tự tương hợp — những thứ làm lý thuyết đứng vững. Hessian đầy đủ của mô hình ngôn ngữ không bao giờ được lưu, nhưng *cùng một ý* — tiền điều kiện bằng độ cong, rồi bước có giảm chấn — là cách một số hệ 2022–2026 thắng Adam đã tinh chỉnh. Bài này là khảo sát, không phải đề thi thuật toán: với mỗi câu chuyện, hãy chỉ ra Hessian (hoặc bản đường chéo / Kronecker thay thế) và nói rõ cái gì bị bỏ để bước còn tính được.

Bốn lát cắt dưới đây là triển khai thật hoặc đo lường đã phản biện, không phải giai thoại. Chúng đứng cạnh nhận xét ở Chương 26 rằng Sophia chỉ là đọc thêm; ở đây ta mở *vì sao* tiền điều kiện kiểu Newton có thể rẻ hơn vẻ ngoài.

## Sophia: Hessian đường chéo cho tiền huấn luyện mô hình ngôn ngữ

Liu, Li, Hall, Liang và Ma (ICLR 2024) đề xuất **Sophia** (*Second-order Clipped Stochastic Optimization*). Cập nhật là trung bình động mũ của gradient ngẫu nhiên chia cho trung bình động mũ của ước lượng Hessian *đường chéo*, rồi cắt theo từng tọa độ. Hessian chỉ được làm mới mỗi vài bước, nên chi phí trung bình mỗi bước gần như Adam. Hai ước lượng trong bài: Hutchinson dùng tích Hessian–vector, và Gauss–Newton–Bartlett lấy nhãn từ phân phối dự báo rồi dùng bình phương gradient của mất mát lấy mẫu lại — chệch, nhưng không âm và rẻ.

Trên các mô hình kiểu GPT từ 125 triệu đến 1,5 tỷ tham số, Sophia đạt cùng perplexity kiểm định với khoảng một nửa số bước của Adam và, vì chi phí mỗi bước tương đương, khoảng một nửa compute và thời gian tường. Lý thuyết (trên một mô hình lồi mạnh đã đơn giản hóa) nói thời gian chạy không nhất thiết phụ thuộc số điều kiện một khi mỗi tọa độ được co bởi độ cong riêng — đúng trực giác bất biến affine ở [14-02-02]({% multilang_post_url contents/chapter14/2021-03-26-14_02_02_affine_invariance_of_newton_method %}), thu hẹp về nhóm đường chéo.

Tham số cắt là bản kỹ thuật của miền tin cậy: khi Hessian địa phương cũ hoặc không xác định, bước Newton thô có thể nổ; cắt theo tọa độ trả lại kỷ luật “Newton giảm chấn” mà bạn đã gặp với backtracking. Mã chính thức: [Liuhong99/Sophia](https://github.com/Liuhong99/Sophia). Đọc ở độ sâu khảo sát: không cần tái dựng ước lượng Bartlett, nhưng phải viết được công thức cập nhật và giải thích vì sao Hessian *đường chéo* là đối tượng duy nhất còn vừa bộ nhớ GPU cạnh mô hình tỷ tham số.

## K-FAC cho transformer, convnet và đồ thị

Kronecker-Factored Approximate Curvature (K-FAC; Martens & Grosse, 2015) xấp xỉ ma trận Fisher / Gauss–Newton tổng quát của một lớp bằng tích Kronecker — đó là độ cong của mất mát *kỳ vọng*, không phải Hessian thô, nhưng đúng là đối tượng các phương pháp kiểu Newton thực sự đảo trong học sâu. Eschenhagen, Immer, Turner, Schneider và Hennig (NeurIPS 2023) bổ sung khung cho lớp *chia sẻ trọng số* — ánh xạ tuyến tính trong convolution, ô hồi quy, mạng đồ thị và transformer. Họ tách **K-FAC-expand** (phân rã kiểu KFC lịch sử) khỏi **K-FAC-reduce**, chứng minh tính đúng của từng biến thể trên mạng tuyến tính sâu ở chế độ chia sẻ tương ứng, và cho thấy cả hai đạt một mốc kiểm định cố định trên GNN và Vision Transformer với khoảng 50–75% số bước bậc nhất, kèm lợi ích thời gian tường tương đương.

Đây là Newton với nghịch đảo có cấu trúc: vẫn giải hệ tuyến tính với Hessian xấp xỉ, nhưng nhân tử Kronecker giữ phép giải ở cỡ hiệp phương sai kích hoạt chứ không phải cỡ ma trận trọng số. Nếu Sophia là “Newton trên đường chéo,” K-FAC là “Newton trên đại số Kronecker.” Câu hỏi sư phạm giống phân tích tự tương hợp: *bạn chịu tính độ cong nào, và giữ bất biến nào?*

## Newton–Cholesky cho mô hình tuyến tính tổng quát trong scikit-learn

Không phải câu chuyện Newton hiện đại nào cũng là mô hình ngôn ngữ. scikit-learn 1.2 (2022) thêm `solver="newton-cholesky"` cho các ước lượng GLM (`PoissonRegressor`, `GammaRegressor`, `TweedieRegressor`), sau đó mở sang hồi quy logistic nhị phân. Bộ giải thực hiện bước Newton–Raphson — tương đương bình phương tối thiểu tái trọng số lặp — và phân rã Hessian tường minh bằng Cholesky. Tài liệu thư viện nói thẳng: đây là mặc định đúng khi $$n_{\text{mẫu}} \gg n_{\text{đặc trưng}}$$ (nhất là one-hot có mức hiếm), và bộ nhớ tỉ lệ bình phương số đặc trưng vì Hessian bị *lập*.

Đây là thuật toán Chương 14 không xấp xỉ. Hessian IRLS của GLM là ma trận Gram $$X^\top W X$$ với trọng số đường chéo $$W$$ phụ thuộc kỳ vọng hiện tại; Cholesky là cách ổn định số để áp $$(\nabla^2 f)^{-1}$$. Sinh viên chỉ gặp Newton trên bảng nên chạy

```python
from sklearn.linear_model import PoissonRegressor
PoissonRegressor(solver="newton-cholesky", alpha=1e-4).fit(X, y)
```

và so số vòng với `solver="lbfgs"`. Khi thiết kế cao và gầy, Newton đúng không phải xa xỉ — đó là bộ giải sản xuất.

## Điều cần giữ từ khảo sát

AdaHessian (Yao, Gholami, Shen, Keutzer, Mahoney, AAAI 2021) là tiền thân trực tiếp của Sophia: đường chéo Hutchinson với mô-men kiểu Adam. SOAP và Shampoo (Chương 18) thay đường chéo bằng tiền điều kiện Kronecker hoặc cơ sở riêng và là họ hàng, không phải đối thủ. Newton đầy đủ vẫn đúng trên GLM, phương pháp hạt nhân cỡ vừa, và các bước định tâm của rào chắn / nguyên thủy–đối ngẫu ở Chương 15 và 17.

Một câu thi hữu ích: *học máy bậc hai hiện đại hầu như không phải “lập $$\nabla^2 f$$ rồi phân rã”; mà là “ước lượng độ cong có cấu trúc, giảm chấn hoặc cắt bước, và khấu hao ước lượng trên nhiều vòng.”* Ngoại lệ — GLM Newton–Cholesky — chứng minh quy tắc bằng đúng những trường hợp lập Hessian vẫn rẻ hơn đi bộ bậc nhất.

## Nguồn

- H. Liu, Z. Li, D. Hall, P. Liang, T. Ma, “Sophia: A Scalable Stochastic Second-order Optimizer for Language Model Pre-training,” ICLR 2024. [arXiv:2305.14342](https://arxiv.org/abs/2305.14342)
- R. Eschenhagen, A. Immer, R. Turner, F. Schneider, P. Hennig, “Kronecker-Factored Approximate Curvature for Modern Neural Network Architectures,” NeurIPS 2023.
- Z. Yao, A. Gholami, S. Shen, K. Keutzer, M. W. Mahoney, “ADAHESSIAN: An Adaptive Second Order Optimizer for Machine Learning,” AAAI 2021.
- Ghi chú phát hành scikit-learn 1.2 và tài liệu bộ giải `newton-cholesky` (2022–); PR GLM [#24637](https://github.com/scikit-learn/scikit-learn/pull/24637).
