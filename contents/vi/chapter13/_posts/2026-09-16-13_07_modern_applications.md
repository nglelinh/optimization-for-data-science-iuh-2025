---
layout: post
title: 13-09 Cách dùng hiện đại của liên hợp, chuẩn đối ngẫu và nón đối ngẫu
chapter: '13'
order: 11
owner: Nguyen Le Linh
categories:
- chapter13
lang: vi
lesson_type: optional
---

# Cách dùng hiện đại của liên hợp, chuẩn đối ngẫu và nón đối ngẫu

Chương 13 vốn đã mang tên “cách dùng đối ngẫu”: giải gốc qua đối ngẫu, chuẩn đối ngẫu, liên hợp, đối ngẫu Lasso, và nón đối ngẫu. Bài tùy chọn này gắn các ứng dụng CS 2022–2026 vào *cùng* các tương ứng ấy. Chúng ta không xây lại $$f^\star$$ hay $$\|y\|_*$$.

## 1. Chuẩn đối ngẫu và quả cầu đối kháng $$\ell_p$$

Hàm tựa của quả cầu tấn công $$\ell_p$$ bán kính $$\varepsilon$$ là $$\varepsilon\|g\|_*$$, trong đó $$\|\cdot\|_*$$ là đối ngẫu của $$\|\cdot\|_p$$:

$$
\|g\|_\infty=\sup_{\|v\|_1\le 1}g^\top v,\qquad
\|g\|_2=\sup_{\|v\|_2\le 1}g^\top v,\qquad
\|g\|_1=\sup_{\|v\|_\infty\le 1}g^\top v.
$$

FGSM / PGD tuyến tính hóa hàm mất mát và bước dài $$\varepsilon$$ theo hướng chuẩn đối ngẫu (dấu cho $$\ell_\infty$$, chuẩn hóa cho $$\ell_2$$). AutoAttack (Croce và Hein, 2020) và bảng **RobustBench** (Croce và cộng sự, 2021; duy trì đến 2025) chuẩn hóa đánh giá cho hai cặp đối ngẫu ấy trên mô hình quy mô CIFAR và ImageNet. Khi bài báo viết “độ chính xác bền $$\ell_\infty$$ 0,03,” họ đã chọn đối ngẫu của $$\|\cdot\|_1$$ làm hình học tấn công. Đó là [13-03 Chuẩn đối ngẫu]({% multilang_post_url contents/chapter13/21-04-05-13_03_Dual_norms %}) với một mô hình đe dọa.

Độ bền được chứng nhận đi xa hơn: một LP hoặc SDP đối ngẫu (Chương 10 / nón đối ngẫu dưới đây) *chứng minh* không nhiễu nào trong quả cầu đảo nhãn.

## 2. Đối ngẫu Lasso như chứng chỉ sàng

Đối ngẫu Lasso trong [13-04-01]({% multilang_post_url contents/chapter13/21-04-05-13_04_01_Example_lasso_dual %}) là chiếu lên polytope $$\|X^\top\theta\|_\infty\le\lambda$$. Khe đối ngẫu $$P(\beta)-D(\theta)$$ là **chứng chỉ tính được**. Screening an toàn theo khe (Ndiaye, Fercoq, Gramfort, Salmon) loại đặc trưng mà tích trong với một $$\theta$$ khả thi đối ngẫu không thể đạt $$\lambda$$. Bertrand, Klopfenstein, Bannier, Gidel và Massias (NeurIPS 2022) đưa working set và các kiểm định đối ngẫu ấy vào **skglm**, khớp GLM thưa với hàng triệu tọa độ. Guha, Ndiaye và Huo (ICML 2023) tái sử dụng đường đối ngẫu / homotopy để dựng tập conformal. Ở tất cả những chỗ ấy, bạn giải hoặc *theo dõi* đối ngẫu để xong gốc nhanh hơn — khẩu hiệu của [13-02]({% multilang_post_url contents/chapter13/21-04-05-13_02_Solving_the_primal_via_the_dual %}).

## 3. Liên hợp, toán tử prox, và bộ giải nón sản xuất

Đẳng thức $$\operatorname{prox}_f(v)+\operatorname{prox}_{f^\star}(v)=v$$ (Moreau) là cách các bộ giải nón bậc nhất hiện đại cài chiếu. OSQP, SCS, và **Clarabel** (Goulart và Chen, 2024) nhận bài toán dạng nón đối ngẫu và chạy vòng ADMM / điểm trong mà bước đắt là một prox hoặc phần dư liên hợp. Chuẩn hóa của CVXPY (đã có ở Chương 05) là ánh xạ *vào* ngôn ngữ nón ấy. Khi bạn viết `cp.norm1(x)` bạn đang xin liên hợp của chỉ báo $$\ell_\infty$$.

## 4. Nón đối ngẫu và chứng chỉ mạng nơ-ron

Thuộc nón đối ngẫu $$z\in K^*$$ là bất đẳng thức biến chương trình nón gốc thành một cận. Các nới SDP và LP của mạng ReLU là chương trình nón; đối ngẫu của chúng là các phiếm hàm lan truyền cận của **$$\alpha,\beta$$-CROWN** và đối ngẫu mặt cắt của **GCP-CROWN** (Zhang và cộng sự, NeurIPS 2022). Thắng VNN-COMP từ 2021 đến 2025, bằng ngôn ngữ chương này, là “đưa ra chứng chỉ nón khả thi đối ngẫu đủ nhanh, trên GPU.” Nón đối ngẫu không phải tò mò đại số — chúng là kiểu của chứng minh.

## Cần nhớ

| Đối tượng Chương 13 | Cách dùng 2022–2026 |
| --- | --- |
| Chuẩn đối ngẫu $$\|g\|_*$$ | Bước tấn công $$\ell_p$$ và RobustBench |
| Đối ngẫu / khe Lasso | Screening skglm và GLM thưa conformal |
| Liên hợp $$f^\star$$ và Moreau | Prox trong OSQP / SCS / Clarabel / CVXPY |
| Nón đối ngẫu $$K^*$$ | Chứng chỉ LP/SDP cho kiểm chứng NN |

**Câu hỏi.** Vì sao đối ngẫu của regularizer $$\ell_1$$ là ràng buộc $$\ell_\infty$$, và sự thật đơn ấy cho cả kiểm định sàng Lasso *lẫn* tấn công dấu FGSM như thế nào?

## Nguồn

- Croce, F., & Hein, M. (2020). Reliable evaluation of adversarial robustness with an ensemble of diverse parameter-free attacks. *ICML*.
- Croce, F., et al. (2021). RobustBench: A standardized adversarial robustness benchmark. *NeurIPS Datasets and Benchmarks*. [https://robustbench.github.io/](https://robustbench.github.io/)
- Bertrand, Q., Klopfenstein, Q., Bannier, P.-A., Gidel, G., & Massias, M. (2022). Beyond L1: Faster and better sparse models with skglm. *NeurIPS*.
- Guha, E. K., Ndiaye, E., & Huo, X. (2023). Conformalization of sparse generalized linear models. *ICML*.
- Goulart, P. J., & Chen, Y. (2024). Clarabel: An interior-point solver for conic programs with quadratic objectives. [arXiv:2405.12762](https://arxiv.org/abs/2405.12762)
- Zhang, H., Wang, S., Xu, K., Li, L., Li, B., Jana, S., Hsieh, C.-J., & Kolter, J. Z. (2022). General cutting planes for bound-propagation-based neural network verification. *NeurIPS*.
- Parikh, N., & Boyd, S. (2014). Proximal algorithms. *Foundations and Trends in Optimization*, 1(3). (đẳng thức Moreau mà các bộ giải trên dùng)
