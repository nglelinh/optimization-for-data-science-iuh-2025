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

(Sub)gradient đối ngẫu, phân rã đối ngẫu, Lagrange tăng, và cái nhìn đầu về ADMM trong chương này đều chia một động tác: *định giá một ràng buộc đồng thuận hoặc tài nguyên và để mỗi khối tự tối ưu*. Đó cũng là động tác phía sau học liên bang. Sinh viên 2026 đã gặp FedAvg ở Chương 29 nên nhận ra FedADMM như Chương 20 có máy chủ: biến đối ngẫu là giá chạy của “mô hình địa phương của bạn phải khớp mô hình toàn cục.”

## FedADMM: biến đối ngẫu chống dị chất khách

Zhou và Li (2022/23, [arXiv:2204.10607](https://arxiv.org/abs/2204.10607)) viết rủi ro thực nghiệm liên bang như bài đồng thuận và áp **ADMM không chính xác**. Khách có thể giải bài con Lagrange tăng gần đúng; máy chủ có thể bỏ qua kẻ chậm; giao tiếp không cần xảy ra mọi bước địa phương. Các biến đối ngẫu hấp thụ dị chất thống kê mà FedAvg chỉ xử bằng trung bình. Các biến thể FedADMM sau (Gong et al. 2022; Wang et al. 2023; Zhang et al. 2021) giữ bộ xương đó.

**FedADMM-InSa** (Song, Wang và Zuazua, 2024, [arXiv:2402.13989](https://arxiv.org/abs/2402.13989)) thêm hai mảnh còn thiếu từ phiếu thực hành của chương này: một *kiểm không chính xác triển khai được* mà mỗi khách tự đánh từ phần dư địa phương, và một *phạt tự thích nghi* $$\beta_i^k$$ đóng vai trò tham số AL mà bạn từng chỉnh tay ở 20-03. Trên các thử họ báo, tổ hợp tăng độ chính xác khoảng 8% đồng thời cắt việc địa phương khoảng 56% so với các baseline họ so. Thuật toán không phải định lý đối ngẫu mới; nó là phân rã đối ngẫu với các bảo vệ Boyd, Parikh, Chu, Peleato và Eckstein đã khuyến, được kỹ thuật hóa cho tham gia từng phần của FL.

Viết dạng đồng thuận một lần,

$$
\min_{w_1,\ldots,w_N,z}\ \sum_{i=1}^N f_i(w_i)\quad\text{s.t.}\quad w_i=z,
$$

và phần còn lại của Chương 20 là phương pháp: đối ngẫu hóa $$w_i=z$$, lấy số hạng AL $$\frac{\beta}{2}\|w_i-z\|_2^2$$, và xen kẽ $$w_i$$, $$z$$, và các nhân tử. FedAvg là trường hợp riêng ném nhân tử đi và lấy một bước gradient trên $$f_i$$.

## Ràng buộc đối ngẫu phân tán: DFedADMM

Khi không có máy chủ, đồng thuận là một đồ thị. **DFedADMM** và **DFedADMM-SAM** (Li, Shen, Li, Yin và Tao, 2023, [arXiv:2308.08290](https://arxiv.org/abs/2308.08290)) đặt một biến đối ngẫu trên mỗi cạnh (hoặc bất đồng láng giềng) để các mục tiêu địa phương dị chất không thể trôi độc lập. SAM (cực tiểu nhận biết độ sắc) là regularizer địa phương thêm chống quá khớp dị chất; phần *đối ngẫu* là Chương 20. Bài cho tốc độ không lồi phụ thuộc khe phổ của ma trận gossip — cùng Laplacian đồ thị xuất hiện trong ADMM đồng thuận cổ điển.

Đây là cách đọc đúng cho sinh viên sẽ gặp gossip SGD trong hệ phân tán: gossip bậc nhất là phân rã đối ngẫu với cập nhật đối ngẫu bước đơn vị và không AL; DFedADMM trả lại AL và bộ nhớ đối ngẫu.

## RL liên bang: ADMM trên một bước gradient chính sách tự nhiên

Bài NeurIPS 2023 “Improved Communication Efficiency in Federated Natural Policy Gradient via ADMM-based Gradient Updates” thay một lần giải Fisher $$O(d^2)$$ bằng một tách ADMM giao tiếp $$O(d)$$ số mỗi vòng. NPG liên bang là một bước chính sách bậc hai (họ hàng Chương 14); việc giảm giao tiếp là *phân rã đối ngẫu của hệ Newton đó*. Thí nghiệm trên tác vụ MuJoCo cho thấy thưởng ngang FedNPG đầy đủ và giao tiếp tương đương FedPPO bậc nhất.

Khuôn cần nhớ: mỗi khi một phương pháp liên bang muốn một Newton hoặc chiếu địa phương *khớp nối*, ADMM là cách bạn tháo khớp mà không gửi một ma trận.

## Phân rã đối ngẫu ngoài trung tâm dữ liệu

Cùng đối ngẫu tách được theo khối là cách OPF hệ thống điện, điều độ năng lượng nhiều chu kỳ, và một số mô hình y tế bảo vệ riêng tư vẫn được giải năm 2022–2026: mỗi tác nhân giữ $$x_i$$, một điều phối cập nhật $$\lambda$$ trên các ràng buộc nối (cân bằng dòng, rủi ro chung). Bayesian-ADMM (2025, [arXiv:2506.13150](https://arxiv.org/abs/2506.13150)) viết lại điểm cố định ADMM như đối ngẫu Bayes biến phân và lấy lại các biến thể liên bang kiểu Newton và kiểu Adam bằng cách đổi hậu nghiệm họ mũ — một con trỏ mức khảo sát, không phải thuật toán bắt buộc mới.

Chương 29 sẽ đối chiếu FedAvg với ADMM như lựa chọn *hệ thống*. Bài này là lý do tối ưu chúng khác nhau: **biến đối ngẫu là bộ nhớ của đồng thuận bị vi phạm**. Nếu bạn xóa chúng, bạn được trung bình. Nếu bạn giữ chúng và một AL toàn phương, bạn được các phương pháp của chương này, vì thế chúng tái xuất hiện mỗi lần dữ liệu liên bang dị chất.

## Nguồn

- S. Zhou, G. Y. Li, “Federated Learning via Inexact ADMM,” 2022. [arXiv:2204.10607](https://arxiv.org/abs/2204.10607)
- Y. Song, Z. Wang, E. Zuazua, “FedADMM-InSa: An Inexact and Self-Adaptive ADMM for Federated Learning,” 2024. [arXiv:2402.13989](https://arxiv.org/abs/2402.13989)
- Q. Li, L. Shen, G. Li, Q. Yin, D. Tao, “DFedADMM: Dual Constraints Controlled Model Inconsistency for Decentralized Federated Learning,” 2023. [arXiv:2308.08290](https://arxiv.org/abs/2308.08290)
- “Improved Communication Efficiency in Federated Natural Policy Gradient via ADMM-based Gradient Updates,” NeurIPS 2023.
- “Federated ADMM from Bayesian Duality,” 2025. [arXiv:2506.13150](https://arxiv.org/abs/2506.13150)
- S. Boyd, N. Parikh, E. Chu, B. Peleato, J. Eckstein, “Distributed Optimization and Statistical Learning via the Alternating Direction Method of Multipliers,” *Found. Trends Mach. Learn.* 2011 (bộ xương mà tất cả các bài trên tái dùng).
