---
layout: post
title: 13-10 Cách dùng hiện đại của liên hợp, chuẩn đối ngẫu và nón đối ngẫu
chapter: '13'
order: 14
owner: Nguyen Le Linh
categories:
- chapter13
lang: vi
lesson_type: optional
---

Khi một mô hình tối ưu lồi hiện đại (như CVXPY gọi bộ giải Clarabel hay SCS) trả về nghiệm trong vài mili-giây, điều gì thực sự diễn ra bên dưới nắp ca-pô? Thay vì viết một thuật toán riêng cho từng bài toán, các bộ giải nón hiện đại quy toàn bộ về một cặp bài toán nguyên thủy – đối ngẫu trên tích các nón tự đối ngẫu, nơi **hàm liên hợp**, **toán tử gần kề (proximal operator)** và **nón đối ngẫu** phối hợp nhịp nhàng.

Bài đọc mở rộng này giúp bạn nhìn xuyên qua lớp vỏ thư viện để thấy cách bốn công cụ của Chương 13 (chuẩn đối ngẫu, đối ngẫu Lasso, phân rã Moreau qua hàm liên hợp và nón đối ngẫu) trở thành nền tảng cho cả bộ giải tối ưu công nghiệp lẫn hệ thống kiểm chứng an toàn AI giai đoạn 2022–2026.

## Bản đồ kiến thức nền: Hệ sinh thái thuật toán dựa trên đối ngẫu hiện đại

- **Phép chiếu nón và phân rã Moreau:** Mọi vectơ $$v$$ đều phân tách trực giao duy nhất thành hình chiếu lên nón $$K$$ và hình chiếu lên nón cực $$-K^*$$: $$v = \Pi_K(v) + \Pi_{-K^*}(v)$$. Đây là trái tim của các bộ giải tách toán tử như ADMM và SCS.
- **Chứng chỉ đối ngẫu cho tính khả thi và tối ưu:** Các bộ giải nón hiện đại không chỉ xuất ra nghiệm $$x^\star$$ mà còn xuất ra biến đối ngẫu $$y^\star, s^\star \in K^*$$ để chứng minh tính tối ưu (duality gap $$\approx 0$$) hoặc chứng minh bài toán vô nghiệm (chứng chỉ Farkas tổng quát).
- **Biên an toàn trong kiểm chứng mạng nơ-ron:** Khi nới lỏng hàm kích hoạt phi tuyến ReLU thành bao lồi, việc cực đại hóa hàm đối ngẫu tạo ra chặn dưới hợp lệ cho biên phân loại ngay cả khi chưa chạy đến hội tụ hoàn toàn.
- **Sàng lọc đặc trưng bằng quả cầu an toàn (Gap Safe Screening):** Từ khoảng cách đối ngẫu tại vòng lặp $$k$$, ta dựng được một quả cầu chắc chắn chứa $$u^\star$$ để loại sớm các biến Lasso bằng $$0$$ mà không hề đánh mất tính chính xác toàn cục.

### Khung giải thích (nên đọc chậm): Kiểm chứng tay đồng nhất thức Moreau cho chuẩn $$\ell_1$$ và liên hợp $$\ell_\infty$$

Xét hàm không trơn $$f(x) = \|x\|_1$$ trên $$\mathbb{R}^2$$ và hàm liên hợp của nó $$f^*(y) = I_{\{\|y\|_\infty \le 1\}}(y)$$. Đồng nhất thức Moreau khẳng định với mọi $$v \in \mathbb{R}^2$$:

$$\operatorname{prox}_f(v) + \operatorname{prox}_{f^*}(v) = v.$$

Hãy kiểm chứng trực tiếp bằng tay với điểm $$v = (2.5, -0.4)^T$$:

1. **Tính $$\operatorname{prox}_{f^*}(v)$$ (phép chiếu Euclid lên khối hộp $$[-1, 1]^2$$):**
   Với mỗi tọa độ, ta kẹp giá trị vào đoạn $$[-1, 1]$$:
   $$\operatorname{prox}_{f^*}(v) = \Pi_{[-1, 1]^2}\begin{bmatrix} 2.5 \\ -0.4 \end{bmatrix} = \begin{bmatrix} 1.0 \\ -0.4 \end{bmatrix}.$$
2. **Suy ra $$\operatorname{prox}_f(v)$$ bằng phép trừ đơn giản (không cần giải tối ưu lại!):**
   $$\operatorname{prox}_f(v) = v - \operatorname{prox}_{f^*}(v) = \begin{bmatrix} 2.5 \\ -0.4 \end{bmatrix} - \begin{bmatrix} 1.0 \\ -0.4 \end{bmatrix} = \begin{bmatrix} 1.5 \\ 0.0 \end{bmatrix}.$$
3. **Đối chiếu trực tiếp với định nghĩa ngưỡng mềm (Soft-Thresholding):**
   - Tọa độ 1: $$\operatorname{sign}(2.5)\max(\vert 2.5\vert - 1, 0) = +1.5$$.
   - Tọa độ 2: $$\operatorname{sign}(-0.4)\max(\vert -0.4\vert - 1, 0) = 0.0$$.
   Kết quả trùng khớp hoàn toàn! Trong thực tế, kỹ thuật này cho phép tính nhanh toán tử prox của bất kỳ chuẩn phức tạp nào (như Group Lasso hay chuẩn vết) chỉ bằng cách chiếu lên quả cầu chuẩn đối ngẫu.

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
