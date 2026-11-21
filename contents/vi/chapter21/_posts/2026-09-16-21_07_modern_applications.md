---
layout: post
title: 21-08 Ứng dụng hiện đại của ADMM
chapter: '21'
order: 9
owner: Nguyen Le Linh
categories:
- chapter21
lang: vi
lesson_type: optional
---


Các bài trước trong chương này coi ADMM là phương pháp tách *lồi có cấu trúc*: hai (hoặc nhiều) khối proximal dễ, một bước nâng đối ngẫu, và phần dư bạn có thể theo dõi. Câu chuyện đó không kết thúc năm 2011. Từ 2022 đến 2026, cùng mẫu đồng thuận / Lagrangian tăng cường xuất hiện trong học sâu liên federated, tạo ảnh tính toán với bộ khử nhiễu học được, và điều độ hệ thống điện trực tuyến. Ghi chú tùy chọn này là bản đồ các triển khai đó, không phải lần suy diễn thứ hai của ADMM dạng chuẩn hóa.

Nhắc lại dạng đồng thuận từ [21-05]({% multilang_post_url contents/chapter21/21-03-29-21_05_Consensus_ADMM %}):

$$
\min_{x_1,\ldots,x_B,z}\ \sum_{i=1}^B f_i(x_i)\qquad\text{subject to}\qquad x_i=z.
$$

Mỗi client (hoặc mỗi khối ảnh, hoặc mỗi vùng điện) giữ một $$f_i$$ riêng; server chỉ trung bình và cập nhật đối ngẫu. Mọi ứng dụng dưới đây là chuyên biệt hóa của khuôn đó.

## 1. FedADMM: học đồng thuận khi client dị chất

**Học liên federated** (Chương 29) thường trung bình *trọng số* sau vài bước SGD cục bộ (FedAvg). Đó *không* phải ADMM: không có phần dư đối ngẫu, và trôi cục bộ là cố ý. Một dòng 2022–2023 đặt lại biến đối ngẫu.

Gong, Li và Freris ([arXiv:2204.03529](https://arxiv.org/abs/2204.03529), 2022) giới thiệu **FedADMM**. Mỗi client $$i$$ cực tiểu hóa gần đúng Lagrangian tăng cường (vài bước SGD cục bộ được phép — cập nhật $$x$$ *không chính xác*), server trung bình các biến gốc, và đối ngẫu $$w_i$$ tích lũy bất đồng $$x_i-z$$. Chi phí truyền mỗi vòng khớp FedAvg, nhưng đối ngẫu thích nghi với **dị chất thống kê** mà không cần hệ số proximal chỉnh tay. Cùng bài báo ghi nhận giảm tới 87% số vòng so với FedAvg/FedProx trên CIFAR-10 / Fashion-MNIST với phân hoạch non-IID.

Zhou và Li, *Federated Learning via Inexact ADMM*, IEEE TPAMI 45(8):9699–9708, 2023, [doi:10.1109/TPAMI.2023.3243080](https://doi.org/10.1109/TPAMI.2023.3243080), bổ sung lý thuyết: giải cục bộ không chính xác, tham gia một phần, và mục tiêu không lồi. Thông điệp cho môn này thật cụ thể. Nếu bạn viết được chương trình đồng thuận và quan tâm phần dư, ADMM vẫn là ngôn ngữ đúng. Nếu mô hình là mạng sâu và tài nguyên khan là *số vòng*, FedADMM là phương ngữ thập niên 2020 của [21-05]({% multilang_post_url contents/chapter21/21-03-29-21_05_Consensus_ADMM %}) — không thay FedAvg, và không phải “SGD cộng nhân tử Lagrange.”

Một theo dõi y khoa 2025–2026 (FL tăng cường ADMM trên PIMA diabetes và X-quang ngực) đặt FedADMM cạnh SCAFFOLD và FedDyn. Đó là *ứng dụng*, không phải thuật toán mới: bệnh viện không được gộp ảnh, và phần dư gốc–đối ngẫu là một kiểm tra sức khỏe hữu ích.

## 2. Plug-and-play ADMM trong tạo ảnh tính toán

Phục hồi ảnh là bài toán hợp thành kinh điển

$$
\min_x\ \tfrac12\|Ax-b\|_2^2 + g(x),
$$

với $$A$$ là mờ / lấy mẫu thưa và $$g$$ là regularizer. ADMM cổ điển dùng $$\mathrm{prox}_g$$. **Plug-and-play (PnP) ADMM** thay prox đó bằng một bộ khử nhiễu có sẵn $$D_{\sigma}$$ — BM3D hôm qua, CNN hôm nay — và giữ bước $$x$$ trung thành dữ liệu.

Chan, Wang và Elgendy, *IEEE Trans. Computational Imaging* 3:84–98, 2017 (trực tuyến 2016), [doi:10.1109/TCI.2016.2629286](https://doi.org/10.1109/TCI.2016.2629286), chứng minh hội tụ điểm bất động cho bộ khử nhiễu *bị chặn* dưới lược đồ continuation, với siêu phân giải và ảnh đơn photon làm ví dụ chạy. Sóng 2022–2023 biến bộ khử nhiễu thành mạng sâu. Zhang, Li, Zuo, Zhang, Van Gool và Timofte, *Plug-and-Play Image Restoration with Deep Denoiser Prior*, IEEE TPAMI 44(10):6360–6376, 2022, [doi:10.1109/TPAMI.2021.3088914](https://doi.org/10.1109/TPAMI.2021.3088914), thả một DRUNet đã huấn luyện vào nhiều bài toán ngược. Hurault, Chambolle, Leclaire và Papadakis ([arXiv:2210.10605](https://arxiv.org/abs/2210.10605), 2023) tuyến tính hóa bước $$x$$ của ADMM để toán tử mờ không đều không cần CG bên trong. Shoushtari, Liu, Schniter và Kamilov ([arXiv:2311.18810](https://arxiv.org/abs/2311.18810), 2023) giải thích vì sao PnP-ADMM thường hội tụ ngay cả với CNN *giãn nở* nếu coi $$D_{\sigma}$$ là ước lượng MMSE (do đó là prox của một $$g$$ có thể không lồi).

Bài học khoa học dữ liệu: ADMM là *giao diện mô-đun*. Một khối là vật lý ($$A$$, likelihood Poisson); khối kia là prior học được. Bạn không huấn luyện lại mạng cho mọi camera. Đó là lý do nhóm tạo ảnh tính toán vẫn dạy ADMM sau khi mọi người khác chuyển sang Adam.

## 3. Tối ưu dòng công suất phân tán

Optimal power flow (OPF) là QCQP không lồi trên lưới: điện áp, phát điện, giới hạn đường dây. Các vùng từ chối chia sẻ toàn bộ dữ liệu mạng, và năng lượng tái tạo khiến bài toán *trực tuyến*. ADMM đồng thuận tách lưới tại nút biên: mỗi vùng giải OPF cục bộ, đối ngẫu trên điện áp chung ép thỏa Kirchhoff.

Wang, Pu, Huang, Yu, Shi và Wang, *Online ADMM for Distributed Optimal Power Flow via Lagrangian Duality*, *Energies* 15(24):9525, 2022, [doi:10.3390/en15249525](https://doi.org/10.3390/en15249525), chạy ADMM đồng thuận trên OPF *đối ngẫu* để chỉ nhân tử biên di chuyển, và làm vậy *trực tuyến* khi nguồn phân tán dao động. Thí nghiệm IEEE 30-bus so sánh OPF tĩnh và động: vòng lặp ADMM trực tuyến bám ramp tái tạo mà không khiến máy phát cổ điển giật như OPF ngoại tuyến giải lại toàn bộ. Đây là khuôn đồng thuận của Boyd với $$f_i$$ hệ thống điện, và là lời nhắc rằng “tối ưu phân tán” năm 2026 không chỉ là all-reduce GPU.

## Giữ lại gì, gửi sang Chương 29 cái gì

| Ứng dụng | Tách gì | Trung bình gì | Chứng nhận |
|----------|---------|---------------|------------|
| FedADMM | loss huấn luyện cục bộ | gốc $$z$$ và đối ngẫu | phần dư (và tốc độ không lồi) |
| PnP tạo ảnh | trung thành dữ liệu vs bộ khử nhiễu | ảnh / đối ngẫu | điểm bất động của prox-denoiser |
| OPF phân tán | vùng điện | điện áp biên / nhân tử | phần dư cân bằng công suất |
| FedAvg (Ch.29) | ERM cục bộ | **trọng số** sau $$E$$ bước | không |

**Bài tập.** Lấy cập nhật đồng thuận dạng chuẩn hóa từ 21-05 và viết *phác thảo* FedADMM 3 client (không cần huấn luyện): mỗi client một bước gradient trên $$\frac12\|x_i-x_i^{\mathrm{data}}\|_2^2+\frac{\rho}{2}\|x_i-z+u_i\|_2^2$$, rồi trung bình. Vẽ $$\|x_i-z\|$$ so với một lần chạy kiểu FedAvg trung bình-không-đối-ngẫu. Lần có đối ngẫu phải kéo ba $$x_i$$ lại; lần không đối ngẫu để lại khe đúng bằng độ lệch dữ liệu.

## Nguồn

- S. Boyd et al., *Foundations and Trends in ML* 3(1):1–122, 2011 — ADMM đồng thuận.
- Y. Gong, Y. Li, N. M. Freris, [arXiv:2204.03529](https://arxiv.org/abs/2204.03529), 2022 — FedADMM.
- S. Zhou and G. Y. Li, *IEEE TPAMI* 45(8):9699–9708, 2023 — ADMM không chính xác cho FL.
- S. H. Chan, X. Wang, O. A. Elgendy, *IEEE TCI* 3:84–98, 2017 — hội tụ PnP-ADMM.
- K. Zhang et al., *IEEE TPAMI* 44(10):6360–6376, 2022 — bộ khử nhiễu PnP sâu.
- S. Hurault et al., [arXiv:2210.10605](https://arxiv.org/abs/2210.10605), 2023 — PnP-ADMM tuyến tính hóa.
- S. Shoushtari et al., [arXiv:2311.18810](https://arxiv.org/abs/2311.18810), 2023 — PnP-ADMM không lồi.
- S. Wang, L. Pu, X. Huang, Y. Yu, Y. Shi, H. Wang, *Energies* 15(24):9525, 2022 — OPF phân tán trực tuyến.
