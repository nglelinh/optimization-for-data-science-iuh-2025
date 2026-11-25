---
layout: post
title: 13-07 Cách dùng hiện đại của liên hợp, chuẩn đối ngẫu và nón đối ngẫu
chapter: '13'
order: 11
owner: Nguyen Le Linh
categories:
- chapter13
lang: vi
lesson_type: optional
redirect_from:
  - /contents/vi/chapter13/13_09_modern_applications/
---

Nhiều người học xong lý thuyết đối ngẫu ở bậc đại học vẫn tự hỏi: những công thức như chuẩn đối ngẫu $$\|y\|_*$$, hàm liên hợp $$f^*$$ hay nón đối ngẫu $$K^*$$ liệu có chỉ nằm trên bảng đen hay thực sự đang chạy bên trong các hệ thống AI hiện đại? Câu trả lời của giai đoạn 2022–2026 là một lời khẳng định vang dội: chúng chính là động cơ toán học đứng sau **phòng thủ tấn công đối kháng (adversarial robustness)**, **sàng lọc đặc trưng siêu tốc**, các **bộ giải nón thế hệ mới** và **kiểm chứng an toàn mạng nơ-ron**.

Khi một kẻ tấn công nhiễu từng pixel ảnh trong quả cầu $$\ell_\infty$$ bán kính $$\epsilon$$, hướng tấn công nguy hiểm nhất không còn là gradient thuần túy mà là vectơ đạt cực đại trong định nghĩa **chuẩn đối ngẫu $$\ell_1$$**. Bài đọc chuyên sâu này nối thẳng các khái niệm vừa học trong Chương 13 với những bài toán mũi nhọn nhất của khoa học máy tính ngày nay.

## Bản đồ kiến thức nền: Bốn mũi nhọn ứng dụng của đối ngẫu trong AI hiện đại

- **Chuẩn đối ngẫu và tấn công đối kháng $$\ell_p$$:** Xấp xỉ bậc nhất mức tăng hàm mất mát dưới nhiễu $$\|\delta\|_p \le \epsilon$$ là $$\max_{\|\delta\|_p \le \epsilon} \nabla \ell(x)^T \delta = \epsilon \|\nabla \ell(x)\|_q$$ — biến chuẩn đối ngẫu thành công cụ định lượng trực tiếp độ nhạy của mạng nơ-ron.
- **Đối ngẫu Lasso và sàng lọc an toàn (Safe Screening):** Nghiệm đối ngẫu $$u$$ cho phép kiểm tra điều kiện $$\vert X_j^T u \vert < \lambda$$ để loại bỏ chắc chắn các đặc trưng có $$\beta_j^\star = 0$$ ngay giữa quá trình lặp, tăng tốc huấn luyện trên dữ liệu hàng triệu chiều.
- **Hàm liên hợp và phân rã Moreau:** Đồng nhất thức $$\operatorname{prox}_{f}(v) + \operatorname{prox}_{f^*}(v) = v$$ cho phép tính toán tử gần kề của một hàm khó thông qua phép chiếu đơn giản lên tập liên hợp.
- **Nón đối ngẫu và kiểm chứng mạng nơ-ron:** Các bộ kiểm chứng như $$\alpha,\beta$$-CROWN dùng biến đối ngẫu không âm (hoặc thuộc nón đối ngẫu) để tạo ra chứng chỉ toán học khẳng định mạng không bao giờ phân loại sai trong vùng nhiễu cho trước.

### Khung giải thích (nên đọc chậm): Tính tay nhiễu đối kháng tối ưu $$\ell_\infty$$ và $$\ell_2$$ bằng chuẩn đối ngẫu

Giả sử tại một ảnh đầu vào $$x \in \mathbb{R}^3$$, gradient của hàm mất mát theo đầu vào là $$g = \nabla_x \ell(x) = (0.8, -0.6, 0.2)^T$$, và kẻ tấn công được phép cộng nhiễu $$\delta$$ với ngân sách $$\epsilon = 0.1$$.

1. **Tấn công dưới ràng buộc $$\|\delta\|_\infty \le 0.1$$ (kiểu FGSM):**
   Ta cần $$\max_{\|\delta\|_\infty \le 0.1} g^T \delta = 0.1 \|g\|_1$$.
   - Nhiễu tối ưu lấy dấu của từng thành phần gradient: $$\delta^\star_{\ell_\infty} = 0.1 \cdot \operatorname{sign}(g) = (0.1, -0.1, 0.1)^T$$.
   - Mức tăng hàm mất mát bậc nhất: $$g^T \delta^\star_{\ell_\infty} = 0.1(\vert 0.8\vert + \vert -0.6\vert + \vert 0.2\vert) = 0.1 \times 1.6 = 0.16$$.
2. **Tấn công dưới ràng buộc $$\|\delta\|_2 \le 0.1$$:**
   Ta cần $$\max_{\|\delta\|_2 \le 0.1} g^T \delta = 0.1 \|g\|_2$$.
   - Tính chuẩn Euclid: $$\|g\|_2 = \sqrt{0.64 + 0.36 + 0.04} = \sqrt{1.04} \approx 1.0198$$.
   - Nhiễu tối ưu cùng hướng với $$g$$: $$\delta^\star_{\ell_2} = 0.1 \frac{g}{\|g\|_2} \approx (0.0784, -0.0588, 0.0196)^T$$.
   - Mức tăng hàm mất mát bậc nhất: $$0.1 \times 1.0198 \approx 0.1020$$.
3. **Ý nghĩa thiết kế:** Cùng một ngân sách $$\epsilon = 0.1$$, quả cầu $$\ell_\infty$$ rộng hơn quả cầu $$\ell_2$$ nên cho phép mức tăng mất mát lớn hơn ($$0.16 > 0.102$$), và muốn phòng thủ theo chuẩn $$\ell_\infty$$ thì ta cần ép **chuẩn đối ngẫu $$\ell_1$$ của gradient** nhỏ xuống!

---

# Cách dùng hiện đại của liên hợp, chuẩn đối ngẫu và nón đối ngẫu

Chương 13 tập trung vào các ứng dụng của lý thuyết đối ngẫu: giải bài toán nguyên thủy thông qua đối ngẫu, chuẩn đối ngẫu, hàm liên hợp, đối ngẫu Lasso và nón đối ngẫu. Bài đọc tùy chọn này gắn các ứng dụng trong khoa học máy tính giai đoạn 2022–2026 vào đúng các cặp tương ứng đó, mà không trình bày lại định nghĩa của $$f^*$$ hay $$\|y\|_*$$.

## 1. Chuẩn đối ngẫu và quả cầu nhiễu đối kháng $$\ell_p$$

Hàm hỗ trợ của quả cầu tấn công $$\ell_p$$ bán kính $$\varepsilon$$ là $$\varepsilon\|g\|_*$$, trong đó $$\|\cdot\|_*$$ là chuẩn đối ngẫu của $$\|\cdot\|_p$$:

$$
\|g\|_\infty=\sup_{\|v\|_1\le 1}g^\top v,\qquad
\|g\|_2=\sup_{\|v\|_2\le 1}g^\top v,\qquad
\|g\|_1=\sup_{\|v\|_\infty\le 1}g^\top v.
$$

Các phương pháp tấn công như FGSM và PGD tuyến tính hóa hàm mất mát rồi dịch chuyển một bước độ dài $$\varepsilon$$ theo hướng cực đại hóa tích vô hướng tương ứng với chuẩn đối ngẫu (lấy dấu của gradient cho tấn công $$\ell_\infty$$, chuẩn hóa theo $$\ell_2$$ cho tấn công $$\ell_2$$). AutoAttack (Croce và Hein, 2020) và bảng chuẩn **RobustBench** (Croce và cộng sự, 2021; duy trì đến 2025) đã chuẩn hóa quy trình đánh giá cho hai cặp đối ngẫu này trên các mô hình quy mô CIFAR và ImageNet. Khi một bài báo báo cáo “độ chính xác bền vững dưới nhiễu $$\ell_\infty$$ mức 0,03”, hình học tấn công được chọn chính là quả cầu ứng với chuẩn đối ngẫu của $$\|\cdot\|_1$$ — tức nội dung mục [13-03 Chuẩn đối ngẫu]({% multilang_post_url contents/chapter13/21-04-05-13_03_Dual_norms %}) đặt trong ngữ cảnh mô hình mối đe dọa.

Độ bền vững được chứng nhận (certified robustness) còn đi xa hơn: một bài toán LP hoặc SDP đối ngẫu (Chương 10 và phần nón đối ngẫu dưới đây) giúp *chứng minh* rằng không có nhiễu nào trong quả cầu bán kính $$\varepsilon$$ có thể làm đổi nhãn dự đoán.

## 2. Đối ngẫu Lasso như chứng chỉ sàng lọc đặc trưng

Bài toán đối ngẫu Lasso trong mục [13-04-01]({% multilang_post_url contents/chapter13/21-04-05-13_04_01_Example_lasso_dual %}) có dạng bài toán chiếu lên đa diện $$\|X^\top\theta\|_\infty\le\lambda$$. Khoảng cách đối ngẫu $$P(\beta)-D(\theta)$$ là một **chứng chỉ tính toán được trực tiếp**. Kỹ thuật sàng lọc an toàn theo khoảng cách đối ngẫu (gap safe screening — Ndiaye, Fercoq, Gramfort, Salmon) loại bỏ sớm các đặc trưng có tích vô hướng với điểm khả thi đối ngẫu $$\theta$$ chắc chắn không thể đạt ngưỡng $$\lambda$$. Bertrand, Klopfenstein, Bannier, Gidel và Massias (NeurIPS 2022) tích hợp kỹ thuật tập làm việc (working set) cùng các kiểm định đối ngẫu này vào thư viện **skglm**, giúp huấn luyện các mô hình tuyến tính tổng quát (GLM) thưa với hàng triệu biến. Guha, Ndiaye và Huo (ICML 2023) tái sử dụng quỹ đạo đối ngẫu (homotopy) để xây dựng tập dự đoán conformal. Ở mọi trường hợp này, việc giải hoặc theo dõi bài toán đối ngẫu đều nhằm giải bài toán gốc nhanh hơn — đúng tinh thần của mục [13-02]({% multilang_post_url contents/chapter13/21-04-05-13_02_Solving_the_primal_via_the_dual %}).

## 3. Hàm liên hợp, toán tử prox và các bộ giải nón trong thực tế

Đẳng thức Moreau $$\operatorname{prox}_f(v)+\operatorname{prox}_{f^\star}(v)=v$$ là cơ sở để các bộ giải quy hoạch nón bậc nhất hiện đại cài đặt phép chiếu. Các bộ giải như OSQP, SCS và **Clarabel** (Goulart và Chen, 2024) nhận bài toán ở dạng cặp nón nguyên thủy–đối ngẫu và chạy vòng lặp ADMM hoặc phương pháp điểm trong, trong đó bước tốn chi phí chính là tính toán tử prox hoặc đánh giá phần dư liên hợp. Quy trình chuẩn hóa (canonicalization) của CVXPY (đã giới thiệu ở Chương 05) chuyển đổi mô hình người dùng viết sang ngôn ngữ nón này; chẳng hạn, khi viết `cp.norm1(x)`, hệ thống thực chất đang sử dụng mối liên hệ liên hợp với hàm chỉ thị của quả cầu $$\ell_\infty$$.

## 4. Nón đối ngẫu và chứng chỉ kiểm chứng mạng nơ-ron

Điều kiện thuộc nón đối ngẫu $$z\in K^*$$ chính là bất đẳng thức chuyển bài toán quy hoạch nón nguyên thủy thành một cận chứng nhận được. Các phép nới lỏng LP và SDP cho mạng ReLU là những bài toán quy hoạch nón; bài toán đối ngẫu của chúng tương ứng với các phiếm hàm lan truyền cận trong **$$\alpha,\beta$$-CROWN** và bài toán đối ngẫu mặt cắt trong **GCP-CROWN** (Zhang và cộng sự, NeurIPS 2022). Dưới góc nhìn của chương này, việc dẫn đầu cuộc thi kiểm chứng mạng nơ-ron VNN-COMP giai đoạn 2021–2025 thực chất là tạo ra được các chứng chỉ khả thi đối ngẫu trên nón đủ nhanh bằng GPU. Như vậy, nón đối ngẫu không chỉ là khái niệm đại số thuần túy mà đóng vai trò trực tiếp như cấu trúc của chứng chỉ kiểm chứng.

## Tóm tắt

| Đối tượng Chương 13 | Ứng dụng giai đoạn 2022–2026 |
| --- | --- |
| Chuẩn đối ngẫu $$\|g\|_*$$ | Bước tấn công đối kháng $$\ell_p$$ và RobustBench |
| Đối ngẫu và khoảng cách đối ngẫu Lasso | Sàng lọc đặc trưng trong skglm và GLM thưa conformal |
| Hàm liên hợp $$f^\star$$ và đẳng thức Moreau | Toán tử prox trong OSQP, SCS, Clarabel và CVXPY |
| Nón đối ngẫu $$K^*$$ | Chứng chỉ LP/SDP trong kiểm chứng mạng nơ-ron |

**Câu hỏi gợi mở:** Vì sao đối ngẫu của thành phần điều chuẩn $$\ell_1$$ là ràng buộc chuẩn $$\ell_\infty$$, và mối liên hệ này đồng thời giải thích cả quy tắc sàng lọc đặc trưng trong Lasso lẫn bước tấn công lấy dấu FGSM như thế nào?

## Nguồn

- Croce, F., & Hein, M. (2020). Reliable evaluation of adversarial robustness with an ensemble of diverse parameter-free attacks. *ICML*.
- Croce, F., et al. (2021). RobustBench: A standardized adversarial robustness benchmark. *NeurIPS Datasets and Benchmarks*. [https://robustbench.github.io/](https://robustbench.github.io/)
- Bertrand, Q., Klopfenstein, Q., Bannier, P.-A., Gidel, G., & Massias, M. (2022). Beyond L1: Faster and better sparse models with skglm. *NeurIPS*.
- Guha, E. K., Ndiaye, E., & Huo, X. (2023). Conformalization of sparse generalized linear models. *ICML*.
- Goulart, P. J., & Chen, Y. (2024). Clarabel: An interior-point solver for conic programs with quadratic objectives. [arXiv:2405.12762](https://arxiv.org/abs/2405.12762)
- Zhang, H., Wang, S., Xu, K., Li, L., Li, B., Jana, S., Hsieh, C.-J., & Kolter, J. Z. (2022). General cutting planes for bound-propagation-based neural network verification. *NeurIPS*.
- Parikh, N., & Boyd, S. (2014). Proximal algorithms. *Foundations and Trends in Optimization*, 1(3). (trình bày đẳng thức Moreau mà các bộ giải trên sử dụng)
