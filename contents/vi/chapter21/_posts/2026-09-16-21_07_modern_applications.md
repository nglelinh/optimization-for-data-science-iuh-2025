---
layout: post
title: 21-07 Ứng dụng hiện đại của ADMM
chapter: '21'
order: 8
owner: Nguyen Le Linh
categories:
- chapter21
lang: vi
lesson_type: optional
redirect_from:
  - /contents/vi/chapter21/21_08_modern_applications/
---

Một trong những ý tưởng táo bạo và giàu sức sống nhất của thập kỷ qua trong xử lý ảnh tính toán là **Plug-and-Play ADMM (PnP-ADMM)**: trong thuật toán ADMM tách biến $$\min f(x) + g(z) \text{ s.t. } x = z$$, bước cập nhật $$z^{(k)} = \operatorname{prox}_{g, 1/\rho}(x^{(k)} + w^{(k-1)})$$ thực chất chính là một **bộ khử nhiễu Gaussian** với phương sai nhiễu $$\sigma^2 = 1/\rho$$! Vậy tại sao phải giới hạn mình ở những hàm điều chuẩn $$g(z)$$ viết tay bằng công thức toán học (như Total Variation) khi ta có thể "cắm thẳng" (plug-and-play) một mạng nơ-ron khử nhiễu học sâu hiện đại (như DnCNN hay Diffusion denoiser) vào đúng vị trí của $$\operatorname{prox}_g$$? Bài 21-07 mở ra cánh cửa ứng dụng ADMM giai đoạn 2022–2026 trong tạo ảnh tính toán, học liên kết và điều độ năng lượng.

## Kiến thức cần nhớ: Ba trụ cột ứng dụng ADMM hiện đại (2022–2026)

Để thấy vì sao khuôn mẫu tách biến đơn giản từ năm 1975 vẫn là xương sống của nhiều hệ thống AI và kỹ thuật hiện đại, hãy điểm qua ba hướng triển khai nổi bật:

- **Plug-and-Play ADMM (PnP-ADMM) trong tạo ảnh tính toán:** Tách bài toán tái tạo ảnh y tế (MRI, CT) hoặc kính thiên văn thành hai bước rõ rệt: bước vật lý $$x^{(k)}$$ đảm bảo khớp đúng dữ liệu đo lường $$Ax \approx y$$, còn bước tiên nghiệm $$z^{(k)} = D_\sigma(x^{(k)} + w^{(k-1)})$$ thay toán tử proximal bằng một bộ khử nhiễu học sâu có tính không giãn (non-expansive) để bảo toàn hội tụ điểm bất động!
- **Học liên kết không đồng nhất (Federated ADMM):** Kết hợp đồng thuận phân tán của bài 21-05 với các bước cập nhật SGD cục bộ trên thiết bị biên, dùng biến đối ngẫu để triệt tiêu độ lệch phân phối dữ liệu giữa các máy khách.
- **Điều độ lưới điện trực tuyến (Online Distributed OPF):** Các vùng lưới điện tối ưu lịch phát điện cục bộ riêng tư và chỉ trao đổi công suất trên đường dây liên kết thông qua ADMM đồng thuận ở chu kỳ vài giây đến vài phút.

### Giải thích: Chạy tay 1 vòng PnP-ADMM khử mờ tín hiệu 2 điểm bằng bộ khử nhiễu thay cho $$\operatorname{prox}_g$$

Giả sử ta đo được tín hiệu bị làm mờ 1 chiều $$y = 0.5 x_1 + 0.5 x_2 = 5$$ (chỉ có 1 phương trình cho 2 ẩn số $$(x_1, x_2)$$ nên bài toán ngược bị thiếu dữ kiện!). Ta chạy 1 vòng PnP-ADMM với $$\rho = 1$$, khởi tạo $$z^{(0)} = (0, 0)^T, w^{(0)} = (0, 0)^T$$, và dùng một bộ khử nhiễu $$D_\sigma$$ có tính làm mượt kéo hai điểm kề nhau lại gần trung bình của chúng (ví dụ $$D_\sigma(a, b) = (0.75a + 0.25b, \; 0.25a + 0.75b)$$):

1. **Bước 1 — Khớp vật lý (giải bài toán con trơn $$x^{(1)}$$):**
   $$x^{(1)} = \arg\min_{x_1, x_2} \left\{ \frac{1}{2}(0.5 x_1 + 0.5 x_2 - 5)^2 + \frac{1}{2}(x_1^2 + x_2^2) \right\}.$$
   Vì đối xứng theo $$x_1, x_2$$, đặt $$x_1 = x_2 = c$$: đạo hàm $$(c - 5)(0.5) + c = 0 \implies 1.5c = 2.5 \implies x^{(1)} = \left(\frac{5}{3}, \; \frac{5}{3}\right)^T \approx (1.67, 1.67)^T$$.
2. **Bước 2 — Cắm bộ khử nhiễu học sâu $$z^{(1)} = D_\sigma(x^{(1)} + w^{(0)})$$:**
   Thay vì tính $$\operatorname{prox}_g$$ từ một hàm $$g$$ tường minh, ta đưa thẳng $$v = (1.67, 1.67)^T$$ vào mạng khử nhiễu $$D_\sigma$$ (giả sử với nhiễu thực tế trên ảnh, $$v = (2.2, 1.1)^T \implies z^{(1)} = (1.925, 1.375)^T$$ đã mượt hơn hẳn).
3. **Bước 3 — Cập nhật biến đối ngẫu:** $$w^{(1)} = w^{(0)} + x^{(1)} - z^{(1)}$$, đẩy sai lệch vào vòng kế tiếp để tín hiệu cuối cùng vừa khớp sát phép đo vật lý $$y = 5$$, vừa mang đầy đủ đặc trưng tự nhiên mà mạng khử nhiễu đã học!

---

Các bài trước trong chương này xem ADMM như một phương pháp tách bài toán *lồi có cấu trúc*: gồm hai (hoặc nhiều) khối proximal dễ tính, một bước cập nhật đối ngẫu, cùng các phần dư có thể theo dõi trực tiếp. Tuy nhiên, phạm vi ứng dụng của ADMM không dừng lại ở năm 2011. Giai đoạn 2022–2026, cùng khuôn mẫu đồng thuận và Lagrangian tăng cường này tiếp tục xuất hiện trong học sâu liên kết, tạo ảnh tính toán với bộ khử nhiễu học được, và điều độ hệ thống điện trực tuyến. Bài đọc tùy chọn này phác họa các hướng triển khai đó thay vì suy diễn lại ADMM dạng chuẩn hóa.

Nhắc lại bài toán đồng thuận từ [21-05]({% multilang_post_url contents/chapter21/21-03-29-21_05_Consensus_ADMM %}):

$$
\min_{x_1,\ldots,x_B,z}\ \sum_{i=1}^B f_i(x_i)\qquad\text{subject to}\qquad x_i=z.
$$

Mỗi máy khách (hoặc mỗi khối ảnh, mỗi vùng lưới điện) giữ một hàm mục tiêu cục bộ $$f_i$$ riêng; máy chủ chỉ thực hiện phép lấy trung bình và cập nhật biến đối ngẫu. Tất cả các ứng dụng dưới đây đều là những chuyên biệt hóa của khuôn mẫu này.

## 1. FedADMM: học đồng thuận khi dữ liệu giữa các máy khách không đồng nhất

**Học liên kết (federated learning)** (Chương 29) thường lấy trung bình *trọng số* sau một số bước SGD cục bộ (thuật toán FedAvg). Cách làm đó *không* phải là ADMM: không có biến đối ngẫu theo dõi sai lệch và hiện tượng trôi cục bộ (client drift) xuất hiện tự nhiên. Một hướng nghiên cứu giai đoạn 2022–2023 đã đưa biến đối ngẫu quay trở lại.

Gong, Li và Freris ([arXiv:2204.03529](https://arxiv.org/abs/2204.03529), 2022) đề xuất **FedADMM**. Mỗi máy khách $$i$$ cực tiểu hóa xấp xỉ hàm Lagrangian tăng cường (cho phép thực hiện vài bước SGD cục bộ — tức bước cập nhật $$x$$ *không chính xác*), máy chủ lấy trung bình các biến gốc, còn biến đối ngẫu $$w_i$$ tích lũy độ lệch $$x_i-z$$. Chi phí truyền thông mỗi vòng tương đương FedAvg, nhưng biến đối ngẫu tự thích nghi với **tính không đồng nhất về thống kê (statistical heterogeneity)** mà không cần tinh chỉnh thủ công hệ số proximal. Bài báo ghi nhận giảm tới 87% số vòng giao tiếp so với FedAvg/FedProx trên CIFAR-10 và Fashion-MNIST dưới phân hoạch non-IID.

Zhou và Li, *Federated Learning via Inexact ADMM*, IEEE TPAMI 45(8):9699–9708, 2023, [doi:10.1109/TPAMI.2023.3243080](https://doi.org/10.1109/TPAMI.2023.3243080), bổ sung cơ sở lý thuyết cho trường hợp giải cục bộ không chính xác, tham gia một phần (partial participation) và hàm mục tiêu không lồi. Có thể rút ra điểm chính rất rõ ràng: nếu bài toán có thể phát biểu dưới dạng đồng thuận và cần theo dõi phần dư, ADMM vẫn là công cụ thích hợp. Khi mô hình là mạng sâu và nút thắt nằm ở *số vòng truyền thông*, FedADMM đóng vai trò là biến thể thập niên 2020 của [21-05]({% multilang_post_url contents/chapter21/21-03-29-21_05_Consensus_ADMM %}) — không thay thế FedAvg và cũng không đơn thuần là “SGD cộng thêm nhân tử Lagrange”.

Một nghiên cứu ứng dụng y khoa giai đoạn 2025–2026 (học liên kết tăng cường bằng ADMM trên bộ dữ liệu tiểu đường PIMA và ảnh X-quang ngực) so sánh FedADMM với SCAFFOLD và FedDyn. Đây là một *triển khai ứng dụng* hơn là thuật toán mới: các bệnh viện không thể gộp chung dữ liệu ảnh, và phần dư gốc–đối ngẫu cung cấp một chỉ báo hữu ích để kiểm tra quá trình hội tụ.

## 2. Plug-and-play ADMM trong tạo ảnh tính toán

Phục hồi ảnh là bài toán tối ưu hợp thành kinh điển:

$$
\min_x\ \tfrac12\|Ax-b\|_2^2 + g(x),
$$

trong đó $$A$$ mô tả toán tử làm mờ hoặc lấy mẫu thưa và $$g$$ là hàm chính quy hóa. ADMM cổ điển sử dụng toán tử $$\mathrm{prox}_g$$. **Plug-and-play (PnP) ADMM** thay thế bước proximal đó bằng một bộ khử nhiễu có sẵn $$D_{\sigma}$$ — trước đây là BM3D, hiện nay thường là mạng CNN — đồng thời giữ nguyên bước cập nhật $$x$$ đảm bảo tính trung thành với dữ liệu (data fidelity).

Chan, Wang và Elgendy, *IEEE Trans. Computational Imaging* 3:84–98, 2017 (trực tuyến 2016), [doi:10.1109/TCI.2016.2629286](https://doi.org/10.1109/TCI.2016.2629286), chứng minh hội tụ điểm bất động đối với bộ khử nhiễu *bị chặn* theo lược đồ tiếp diễn (continuation), sử dụng bài toán siêu phân giải và ảnh đơn photon làm ví dụ minh họa. Giai đoạn 2022–2023 đánh dấu sự chuyển dịch sang bộ khử nhiễu bằng mạng sâu. Zhang, Li, Zuo, Zhang, Van Gool và Timofte, *Plug-and-Play Image Restoration with Deep Denoiser Prior*, IEEE TPAMI 44(10):6360–6376, 2022, [doi:10.1109/TPAMI.2021.3088914](https://doi.org/10.1109/TPAMI.2021.3088914), tích hợp một mạng DRUNet đã huấn luyện sẵn vào nhiều bài toán ngược khác nhau. Hurault, Chambolle, Leclaire và Papadakis ([arXiv:2210.10605](https://arxiv.org/abs/2210.10605), 2023) tuyến tính hóa bước cập nhật $$x$$ của ADMM để xử lý toán tử mờ không đồng nhất mà không cần vòng lặp liên hợp gradient (CG) bên trong. Shoushtari, Liu, Schniter và Kamilov ([arXiv:2311.18810](https://arxiv.org/abs/2311.18810), 2023) giải thích vì sao PnP-ADMM vẫn thường hội tụ ngay cả với các mạng CNN *giãn nở* khi xem $$D_{\sigma}$$ như một ước lượng MMSE (tương ứng với toán tử proximal của một hàm $$g$$ có thể không lồi).

Điểm quan trọng về mặt kỹ thuật: ADMM đóng vai trò như một *giao diện mô-đun*. Một khối biểu diễn mô hình vật lý ($$A$$, hàm hợp lý Poisson), còn khối kia là tri thức tiên nghiệm học từ dữ liệu. Nhờ đó, không cần huấn luyện lại mạng nơ-ron cho từng thiết bị máy ảnh riêng biệt. Đây là lý do cộng đồng tạo ảnh tính toán vẫn duy trì giảng dạy và sử dụng ADMM bên cạnh các bộ tối ưu như Adam.

## 3. Tối ưu dòng công suất phân tán

Bài toán tối ưu dòng công suất (Optimal Power Flow — OPF) là một bài toán quy hoạch bậc hai có ràng buộc bậc hai (QCQP) không lồi trên lưới điện, liên quan đến điện áp, công suất phát và giới hạn đường dây. Các vùng vận hành thường không chia sẻ toàn bộ dữ liệu lưới nội bộ, trong khi nguồn năng lượng tái tạo biến động liên tục khiến bài toán mang tính *trực tuyến*. ADMM đồng thuận tách lưới điện tại các nút biên: mỗi vùng tự giải bài toán OPF cục bộ, còn biến đối ngẫu trên điện áp biên buộc các vùng thỏa mãn định luật Kirchhoff.

Wang, Pu, Huang, Yu, Shi và Wang, *Online ADMM for Distributed Optimal Power Flow via Lagrangian Duality*, *Energies* 15(24):9525, 2022, [doi:10.3390/en15249525](https://doi.org/10.3390/en15249525), triển khai ADMM đồng thuận trên bài toán OPF *đối ngẫu* để chỉ trao đổi các nhân tử tại biên và cập nhật *trực tuyến* khi nguồn phát phân tán dao động. Thực nghiệm trên lưới IEEE 30 nút so sánh OPF tĩnh và động cho thấy vòng lặp ADMM trực tuyến bám sát độ dốc biến thiên của nguồn tái tạo mà không làm các tổ máy phát truyền thống thay đổi công suất đột ngột như khi giải lại toàn bộ OPF ngoại tuyến. Đây chính là khuôn mẫu đồng thuận của Boyd áp dụng cho hàm mục tiêu $$f_i$$ của hệ thống điện, cho thấy “tối ưu phân tán” hiện nay không chỉ giới hạn ở tác vụ all-reduce trên cụm GPU.

## So sánh phạm vi với Chương 29

| Ứng dụng | Thành phần tách | Đại lượng lấy trung bình | Tiêu chí kiểm chứng |
|----------|-----------------|--------------------------|---------------------|
| FedADMM | hàm mất mát huấn luyện cục bộ | biến gốc $$z$$ và đối ngẫu | phần dư (và tốc độ hội tụ không lồi) |
| PnP tạo ảnh | độ trung thành dữ liệu và bộ khử nhiễu | ảnh / biến đối ngẫu | điểm bất động của bộ khử nhiễu proximal |
| OPF phân tán | các vùng lưới điện | điện áp biên / nhân tử | phần dư cân bằng công suất |
| FedAvg (Ch. 29) | ERM cục bộ | **trọng số** sau $$E$$ bước | không có |

**Bài tập.** Lấy các bước cập nhật đồng thuận dạng chuẩn hóa từ mục 21-05 và viết *phác thảo* thuật toán FedADMM cho 3 máy khách (không cần huấn luyện mạng): mỗi máy khách thực hiện một bước gradient trên $$\frac12\|x_i-x_i^{\mathrm{data}}\|_2^2+\frac{\rho}{2}\|x_i-z+u_i\|_2^2$$, sau đó lấy trung bình. Vẽ đồ thị $$\|x_i-z\|$$ và so sánh với cách lấy trung bình kiểu FedAvg không có biến đối ngẫu. Phiên bản có biến đối ngẫu sẽ kéo cả ba $$x_i$$ hội tụ về cùng một điểm, còn phiên bản không có biến đối ngẫu sẽ giữ lại khoảng cách lệch đúng bằng độ chênh lệch giữa dữ liệu của các máy khách.

## Nguồn

- S. Boyd et al., *Foundations and Trends in ML* 3(1):1–122, 2011 — ADMM đồng thuận.
- Y. Gong, Y. Li, N. M. Freris, [arXiv:2204.03529](https://arxiv.org/abs/2204.03529), 2022 — FedADMM.
- S. Zhou and G. Y. Li, *IEEE TPAMI* 45(8):9699–9708, 2023 — ADMM không chính xác cho FL.
- S. H. Chan, X. Wang, O. A. Elgendy, *IEEE TCI* 3:84–98, 2017 — hội tụ PnP-ADMM.
- K. Zhang et al., *IEEE TPAMI* 44(10):6360–6376, 2022 — bộ khử nhiễu PnP sâu.
- S. Hurault et al., [arXiv:2210.10605](https://arxiv.org/abs/2210.10605), 2023 — PnP-ADMM tuyến tính hóa.
- S. Shoushtari et al., [arXiv:2311.18810](https://arxiv.org/abs/2311.18810), 2023 — PnP-ADMM không lồi.
- S. Wang, L. Pu, X. Huang, Y. Yu, Y. Shi, H. Wang, *Energies* 15(24):9525, 2022 — OPF phân tán trực tuyến.
