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

Chương này nhằm xem xét chi tiết hơn ADMM, đã được đề cập ở [Chương 20]({% multilang_post_url contents/chapter20/21-03-27-20_00_Dual_Methods %}). Các khái niệm cơ bản không khác biệt đáng kể về độ sâu so với những gì đã học ở Chương 20, và chúng ta chủ yếu sẽ xem các trường hợp ứng dụng.

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


Quan hệ hội tụ của ADMM: [BPCPE11], [HL12], [DY16], [IBCH14], [NLRPJ15]  
Ước lượng không gian con thưa: [VCLR13]  
Phân rã thưa cộng hạng thấp: [CLMW09]  
ADMM đồng thuận (Consensus ADMM): [BPCPE11], [NB13]  
Tham số hóa bài toán con: [RT16], [WSK14], [BS14]
