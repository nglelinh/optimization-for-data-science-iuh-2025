---
layout: post
title: '21 Phương pháp hướng luân phiên của các nhân tử (ADMM)'
chapter: '21'
order: 1
owner: Hooncheol Shin
categories:
- chapter21
lang: vi
---

Chương này đi sâu hơn vào phương pháp ADMM đã được giới thiệu ở [Chương 20]({% multilang_post_url contents/chapter20/21-03-27-20_00_Dual_Methods %}). Về mặt khái niệm cơ bản, nội dung không mở rộng thêm nhiều so với Chương 20 mà chủ yếu tập trung vào các bài toán và trường hợp ứng dụng cụ thể.

### Các bài báo tham khảo

* Boyd, Stephen, et al. [BPCPE11] "Distributed optimization and statistical learning via the alternating direction method of multipliers." Foundations and Trends® in Machine learning 3.1 (2011): 1-122.
* Hong, Mingyi, and Zhi-Quan Luo. [HL12] "On the linear convergence of the alternating direction method of multipliers." Mathematical Programming 162.1-2 (2017): 165-199.
* Deng, Wei, and Wotao Yin. [DY16] "On the global and linear convergence of the generalized alternating direction method of multipliers." Journal of Scientific Computing 66.3 (2016): 889-916.
* Iutzeler, Franck, et al. [IBCH14] "Linear convergence rate for distributed optimization with the alternating direction method of multipliers." 53rd IEEE Conference on Decision and Control. IEEE, 2014.
* Nishihara, Robert, et al. [NLRPJ15] "A general analysis of the convergence of ADMM." arXiv preprint arXiv:1502.02009 (2015).
* Parikh, Neal, and Stephen Boyd. [NB13] "Proximal algorithms." Foundations and Trends® in Optimization 1.3 (2014): 127-239.
* Vu, Vincent Q., et al. [VCLR13] "Fantope projection and selection: A near-optimal convex relaxation of sparse PCA." Advances in neural information processing systems. 2013.
* Candès, Emmanuel J., et al. [CLMW09] "Robust principal component analysis?." Journal of the ACM (JACM) 58.3 (2011): 11.
* Ramdas, Aaditya, and Ryan J. Tibshirani. [RT16] "Fast and flexible ADMM algorithms for trend filtering." Journal of Computational and Graphical Statistics 25.3 (2016): 839-858.
* Wytock, Matt, Suvrit Sra, and Jeremy Z. Kolter. [WSK14] "Fast Newton methods for the group fused lasso." UAI. 2014.
* Barbero, Alvaro, and Suvrit Sra. [BS14] "Modular proximal optimization for multidimensional total-variation regularization." arXiv preprint arXiv:1411.0589 (2014).

Phân tích hội tụ của ADMM: [BPCPE11], [HL12], [DY16], [IBCH14], [NLRPJ15]  
Ước lượng không gian con thưa: [VCLR13]  
Phân rã thưa cộng hạng thấp: [CLMW09]  
ADMM đồng thuận (Consensus ADMM): [BPCPE11], [NB13]  
Tham số hóa bài toán con: [RT16], [WSK14], [BS14]

## Ứng dụng giai đoạn 2022–2026 (tùy chọn)

Các ví dụ cổ điển trên (Lasso, phân rã thưa cộng hạng thấp, đồng thuận, fused lasso) vẫn là nền tảng cốt lõi để tiếp cận ADMM. Bên cạnh đó, một bài học tùy chọn tổng hợp giai đoạn 2022–2026 sẽ mở rộng *cùng* cấu trúc tách đồng thuận và toán tử proximal sang học sâu liên kết (**FedADMM**), tạo ảnh plug-and-play với bộ khử nhiễu CNN, và bài toán tối ưu dòng công suất (OPF) phân tán trực tuyến. Bạn có thể đọc tiếp tại [21-07 Ứng dụng hiện đại của ADMM]({% multilang_post_url contents/chapter21/2026-09-16-21_07_modern_applications %}). Bài học này không thay thế tài liệu của Boyd và cộng sự, mà minh họa những hệ thống thực tế nơi phần dư vẫn đóng vai trò giám sát quan trọng.
