---
layout: post
title: 20-06 Ứng dụng hiện đại của phương pháp đối ngẫu (2022–2026)
chapter: '20'
order: 14
owner: Nguyen Le Linh
categories:
- chapter20
lang: vi
lesson_type: optional
---

Các phương pháp (sub)gradient đối ngẫu, phân rã đối ngẫu, hàm Lagrange tăng cường và ADMM trong chương này đều xoay quanh một ý tưởng cốt lõi: *định giá một ràng buộc đồng thuận hoặc nguồn lực chung bằng biến đối ngẫu để mỗi khối biến có thể tự tối ưu độc lập*. Đây cũng chính là cơ chế đứng sau học liên bang (federated learning). Khi học đến FedAvg ở Chương 29, ta có thể nhìn nhận FedADMM như phiên bản có máy chủ trung tâm của Chương 20: biến đối ngẫu đóng vai trò mức giá điều chỉnh liên tục cho yêu cầu "mô hình cục bộ của mỗi client phải khớp với mô hình toàn cục".

## FedADMM: dùng biến đối ngẫu xử lý tính không đồng nhất giữa các client

Zhou và Li (2022/23, [arXiv:2204.10607](https://arxiv.org/abs/2204.10607)) biểu diễn bài toán cực tiểu hóa rủi ro thực nghiệm liên bang dưới dạng bài toán đồng thuận và áp dụng **ADMM không chính xác (inexact ADMM)**. Các client có thể giải gần đúng bài toán con hàm Lagrange tăng cường, máy chủ có thể bỏ qua các nút chậm (stragglers), và không cần đồng bộ giao tiếp sau mỗi bước cập nhật cục bộ. Các biến đối ngẫu hấp thụ tính không đồng nhất về phân phối dữ liệu (statistical heterogeneity) mà FedAvg chỉ xử lý bằng phép lấy trung bình đơn giản. Nhiều biến thể FedADMM khác (Gong et al. 2022; Wang et al. 2023; Zhang et al. 2021) đều kế thừa khung thuật toán này.

**FedADMM-InSa** (Song, Wang và Zuazua, 2024, [arXiv:2402.13989](https://arxiv.org/abs/2402.13989)) bổ sung hai thành phần thực hành quan trọng: một *tiêu chí kiểm tra độ không chính xác khả thi* (implementable inexactness criterion) mà từng client tự đánh giá từ phần dư cục bộ, và một *tham số phạt tự thích nghi* $$\beta_i^k$$ thay cho việc chỉnh tay tham số hàm Lagrange tăng cường như ở bài 20-03. Trên các thí nghiệm báo cáo, sự kết hợp này tăng độ chính xác khoảng 8% đồng thời giảm khối lượng tính toán cục bộ khoảng 56% so với các phương pháp đối chứng. Thuật toán không dựa trên một định lý đối ngẫu mới mà là sự kỹ thuật hóa phân rã đối ngẫu cùng các nguyên tắc của Boyd, Parikh, Chu, Peleato và Eckstein cho bối cảnh tham gia từng phần trong học liên bang.

Chỉ cần viết bài toán đồng thuận dưới dạng

$$
\min_{w_1,\ldots,w_N,z}\ \sum_{i=1}^N f_i(w_i)\quad\text{s.t.}\quad w_i=z,
$$

toàn bộ phần còn lại chính là quy trình của Chương 20: đối ngẫu hóa ràng buộc $$w_i = z$$, cộng số hạng phạt bậc hai $$\frac{\beta}{2}\|w_i-z\|_2^2$$, rồi cập nhật luân phiên $$w_i$$, $$z$$ và các nhân tử đối ngẫu. FedAvg có thể xem là trường hợp đặc biệt khi bỏ qua các nhân tử đối ngẫu và chỉ lấy bước gradient trên $$f_i$$.

## Ràng buộc đối ngẫu phi tập trung: DFedADMM

Khi không có máy chủ trung tâm, ràng buộc đồng thuận được xác định trên một đồ thị mạng. **DFedADMM** và **DFedADMM-SAM** (Li, Shen, Li, Yin và Tao, 2023, [arXiv:2308.08290](https://arxiv.org/abs/2308.08290)) gắn một biến đối ngẫu trên từng cạnh (hoặc sai lệch giữa các nút láng giềng) để các mục tiêu cục bộ không đồng nhất không trôi lệch độc lập khỏi nhau. Thành phần SAM (tối ưu hóa nhận biết độ sắc — Sharpness-Aware Minimization) đóng vai trò điều chuẩn cục bộ nhằm hạn chế quá khớp trên dữ liệu không đồng nhất, còn cơ chế *đối ngẫu* đến trực tiếp từ Chương 20. Bài báo thiết lập tốc độ hội tụ cho bài toán không lồi phụ thuộc vào khoảng cách phổ (spectral gap) của ma trận gossip — cùng cấu trúc ma trận Laplacian đồ thị như trong ADMM đồng thuận cổ điển.

Góc nhìn này giúp kết nối trực tiếp với gossip SGD trong tối ưu phân tán: gossip bậc nhất tương ứng với phân rã đối ngẫu đơn giản không có số hạng hàm Lagrange tăng cường, còn DFedADMM khôi phục cả số hạng tăng cường lẫn bộ nhớ đối ngẫu.

## Học tăng cường liên bang: dùng ADMM cho bước gradient chính sách tự nhiên

Bài báo tại NeurIPS 2023 “Improved Communication Efficiency in Federated Natural Policy Gradient via ADMM-based Gradient Updates” thay bước giải hệ phương trình ma trận Fisher tốn chi phí truyền thông $$O(d^2)$$ bằng một phép tách ADMM chỉ truyền $$O(d)$$ số thực mỗi vòng. Natural Policy Gradient (NPG) liên bang thực chất là một bước cập nhật bậc hai (liên hệ với Chương 14), và việc giảm chi phí truyền thông đạt được nhờ *phân rã đối ngẫu chính hệ Newton đó*. Thí nghiệm trên các tác vụ MuJoCo cho thấy phương pháp đạt phần thưởng tương đương FedNPG đầy đủ với chi phí truyền thông ngang với FedPPO bậc nhất.

Nguyên tắc chung cần ghi nhớ: bất cứ khi nào một phương pháp liên bang cần giải một bước Newton hoặc phép chiếu có liên kết giữa các nút, ADMM giúp tách rời bài toán mà không phải truyền cả ma trận qua mạng.

## Phân rã đối ngẫu ngoài học máy trung tâm dữ liệu

Cấu trúc đối ngẫu tách khối vẫn là công cụ chủ lực giai đoạn 2022–2026 trong bài toán trào lưu công suất tối ưu (OPF) của hệ thống điện, điều độ năng lượng đa chu kỳ và một số bài toán học máy y tế bảo vệ quyền riêng tư: mỗi tác nhân giữ riêng biến $$x_i$$, còn bộ điều phối cập nhật nhân tử $$\lambda$$ trên các ràng buộc liên kết (cân bằng dòng công suất hoặc rủi ro chung). Nghiên cứu Bayesian-ADMM (2025, [arXiv:2506.13150](https://arxiv.org/abs/2506.13150)) diễn giải lại điểm bất động của ADMM dưới góc nhìn đối ngẫu Bayes biến phân và thu lại các biến thể học liên bang kiểu Newton và kiểu Adam bằng cách thay đổi phân phối hậu nghiệm thuộc họ mũ.

Chương 29 sẽ so sánh FedAvg và ADMM dưới góc độ thiết kế *hệ thống*. Còn về mặt tối ưu hóa, điểm khác biệt cốt lõi nằm ở đây: **biến đối ngẫu đóng vai trò bộ nhớ lưu giữ mức vi phạm đồng thuận**. Khi bỏ biến đối ngẫu, ta thu được phép lấy trung bình; khi giữ biến đối ngẫu kèm số hạng Lagrange tăng cường bậc hai, ta thu được các phương pháp của chương này — lý do khiến chúng liên tục được sử dụng mỗi khi dữ liệu học liên bang có tính không đồng nhất cao.

## Nguồn

- S. Zhou, G. Y. Li, “Federated Learning via Inexact ADMM,” 2022. [arXiv:2204.10607](https://arxiv.org/abs/2204.10607)
- Y. Song, Z. Wang, E. Zuazua, “FedADMM-InSa: An Inexact and Self-Adaptive ADMM for Federated Learning,” 2024. [arXiv:2402.13989](https://arxiv.org/abs/2402.13989)
- Q. Li, L. Shen, G. Li, Q. Yin, D. Tao, “DFedADMM: Dual Constraints Controlled Model Inconsistency for Decentralized Federated Learning,” 2023. [arXiv:2308.08290](https://arxiv.org/abs/2308.08290)
- “Improved Communication Efficiency in Federated Natural Policy Gradient via ADMM-based Gradient Updates,” NeurIPS 2023.
- “Federated ADMM from Bayesian Duality,” 2025. [arXiv:2506.13150](https://arxiv.org/abs/2506.13150)
- S. Boyd, N. Parikh, E. Chu, B. Peleato, J. Eckstein, “Distributed Optimization and Statistical Learning via the Alternating Direction Method of Multipliers,” *Found. Trends Mach. Learn.* 2011 (khung thuật toán nền tảng cho các công trình trên).
