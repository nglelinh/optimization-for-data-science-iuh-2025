---
layout: post
title: 02-07 Ứng dụng và phát triển gần đây
chapter: '02'
order: 15
owner: Nguyen Le Linh
categories:
- chapter02
lang: vi
lesson_type: optional
---

Tập lồi là miền khả thi mà bạn có thể *lấy trung bình bên trong*. Sự thật hình học đó giải thích vì sao rất nhiều ràng buộc học máy hiện đại trông như đơn hình, hình cầu, hoặc phổ diện. Bài này gọi tên ba họ tập lồi xuất hiện trong bài báo và thư viện 2022–2025, mỗi họ gắn với một định nghĩa bạn đã có: đơn hình xác suất, quả cầu Wasserstein các phân phối, và đa diện cắt bởi bất đẳng thức công bằng (hoặc ngân sách).

## Đơn hình xác suất, softmax và hình học lớp cuối

Đơn hình chuẩn

$$
\Delta^{n-1} = \bigl\{ p\in\mathbb{R}^n : p\ge 0,\; \mathbf{1}^\top p = 1\bigr\}
$$

là tập lồi (giao của siêu phẳng với orthant không âm). Softmax là ánh xạ trơn *lên* phần trong tương đối của $$\Delta^{n-1}$$. Mọi đầu attention trong Transformer, và mọi mô hình logistic đa lớp, vì thế dùng phi tuyến cuối để chiếu vector logit lên một tập lồi mà bạn vẽ được trong $$\mathbb{R}^2$$ và $$\mathbb{R}^3$$.

Một đơn hình bất ngờ hơn xuất hiện *cuối* quá trình huấn luyện. Papyan, Han và Donoho (*Prevalence of neural collapse*, [PNAS 2020](https://www.pnas.org/doi/10.1073/pnas.2015509117); [arXiv:2008.08186](https://arxiv.org/abs/2008.08186)) đo một *khung chặt đều góc đơn hình* (simplex ETF) giữa các trung bình lớp ở lớp cuối: các trung bình đã tâm tạo cấu hình điểm đối xứng nhất trên mặt cầu. Zhu, Ding, Zhou và cộng sự (*A Geometric Analysis of Neural Collapse with Unconstrained Features*, [NeurIPS 2021](https://papers.nips.cc/paper/2021/hash/f92586a25bb3145facd64ab20fd554ff-Abstract.html)) sau đó chỉ ra rằng, trong mô hình đặc trưng tự do đơn giản với cross-entropy và weight decay, các cấu hình ETF là cực tiểu toàn cục và mọi điểm dừng khác là yên ngựa chặt. Ngôn ngữ tập lồi không phải trang trí: ETF là một tập con cụ thể của mặt cầu, còn đơn hình xác suất là tập mà bộ phân loại thật sự xuất ra.

Khi kiểm “$$C$$ có lồi không?” trên bài tập, hãy gồm $$\Delta^{n-1}$$ và quả cầu Euclid. Hai tập đó là hình học của phân loại và của nhiều regularizer.

## Quả cầu Wasserstein như tập nhập nhằng

Tối ưu vững theo phân phối (DRO) thay một phân phối huấn luyện $$\hat{P}$$ bằng một *tập* phân phối, rồi tối ưu chống lại phần tử tệ nhất trong tập đó. Quả cầu Wasserstein

$$
\mathcal{B}_\varepsilon(\hat{P}) = \bigl\{ Q : W_p(Q,\hat{P}) \le \varepsilon\bigr\}
$$

là tập lồi trong không gian độ đo xác suất (quả cầu vận chuyển tối ưu). Các quyết định sống sót trước $$Q\in\mathcal{B}_\varepsilon(\hat{P})$$ tệ nhất thường có dạng viết lại hữu hạn chiều lồi.

Hai tài liệu bạn mở được: Gao và Kleywegt, “Distributionally Robust Stochastic Optimization with Wasserstein Distance,” [*Mathematics of Operations Research* 48(2):603–655, 2023](https://doi.org/10.1287/moor.2022.1275), chứng minh đối ngẫu mạnh cho DRO Wasserstein và mô tả cấu trúc phân phối trường hợp xấu. Tutorial của Kuhn, Mohajerin Esfahani, Nguyen và Shafieezadeh-Abadeh, *Wasserstein Distributionally Robust Optimization* ([INFORMS TutORials 2019](https://doi.org/10.1287/educ.2019.0198); [arXiv:1908.08729](https://arxiv.org/abs/1908.08729), sửa tháng 11/2024) là bản đọc được và nối quả cầu với phân loại, hồi quy và MLE. Khảo sát rộng hơn năm 2025 trên *Acta Numerica* ([Kuhn, Shafiee, et al.](https://www.cambridge.org/core/journals/acta-numerica/article/distributionally-robust-optimization/5B4E65E3A5A2AEF24E218A6B34E6EAA2)) đặt quả cầu Wasserstein cạnh các tập nhập nhằng khác.

Động thái mô hình hóa giống “thay ước lượng điểm bằng tập bất định lồi” trong lập trình tuyến tính vững, chỉ khác là “điểm” là phân phối. Nếu bạn chứng nhận được $$\mathcal{B}_\varepsilon(\hat{P})$$ lồi và ánh xạ trường hợp xấu trong là lồi theo quyết định, chương trình DRO ngoài là bài tối ưu lồi mà Chương 04 sẽ chính thức hóa.

## Polytope công bằng và phân bổ tài nguyên

Bất đẳng thức tuyến tính trên xác suất định nghĩa đa diện. Ràng buộc kiểu demographic parity

$$
\bigl| \mathbb{E}[h(X)\mid A=a] - \mathbb{E}[h(X)\mid A=a'] \bigr| \le \epsilon
$$

cắt một polytope trong không gian bộ phân loại (ngẫu nhiên hóa). Agarwal, Beygelzimer, Dudík, Langford và Wallach ([ICML 2018](https://proceedings.mlr.press/v80/agarwal18a.html)) coi các lát cắt đó là tập khả thi của một phép quy; [Fairlearn](https://fairlearn.org/v0.12/user_guide/mitigation/reductions.html) vẫn lộ chúng như đối tượng `Moment` năm 2025–2026.

Cùng bức tranh đó phủ ràng buộc ngân sách và phân bổ: $$x\ge 0$$, $$\mathbf{1}^\top x = 1$$ (danh mục trên đơn hình), hoặc $$0\le x\le 1$$, $$Ax\le b$$ (polytope mix truyền thông kiểu knapsack). Siêu phẳng tách ở phần sau chương này chính là chứng chỉ rằng một $$x$$ ứng viên nằm ngoài polytope — cùng loại chứng chỉ bộ giải dùng khi trả về trạng thái không khả thi.

## Hai dòng hình ảnh cần giữ

Mọi ràng buộc hiện đại trong bài này là giao của các mảnh lồi bạn gọi được tên:

$$
\mathcal{C} = \Delta^{n-1} \cap \{ x : Fx \le g \} \qquad\text{hoặc}\qquad \mathcal{B}_\varepsilon(\hat{P}).
$$

Nếu chứng minh từng mảnh lồi thì giao lồi, và mọi tìm kiếm địa phương ở lại trong $$\mathcal{C}$$ là tìm trên tập không có “lỗ.” Đó là toàn bộ lý do Chương 02 tồn tại, viết lại bằng ngôn ngữ attention, DRO và công bằng.

## Nguồn

1. V. Papyan, X. Y. Han và D. L. Donoho, “Prevalence of neural collapse during the terminal phase of deep learning training,” *PNAS* 117(40):24652–24663, 2020. [DOI](https://www.pnas.org/doi/10.1073/pnas.2015509117) · [arXiv:2008.08186](https://arxiv.org/abs/2008.08186)
2. Z. Zhu, T. Ding, J. Zhou và cộng sự, “A Geometric Analysis of Neural Collapse with Unconstrained Features,” NeurIPS 2021. [tóm tắt](https://papers.nips.cc/paper/2021/hash/f92586a25bb3145facd64ab20fd554ff-Abstract.html)
3. R. Gao và A. J. Kleywegt, “Distributionally Robust Stochastic Optimization with Wasserstein Distance,” *Math. Oper. Res.* 48(2):603–655, 2023. [DOI](https://doi.org/10.1287/moor.2022.1275)
4. D. Kuhn, P. Mohajerin Esfahani, V. A. Nguyen và S. Shafieezadeh-Abadeh, “Wasserstein Distributionally Robust Optimization,” INFORMS TutORials 2019; arXiv:1908.08729 (sửa 2024). [arXiv](https://arxiv.org/abs/1908.08729)
5. A. Agarwal và cộng sự, “A Reductions Approach to Fair Classification,” ICML 2018. [PMLR](https://proceedings.mlr.press/v80/agarwal18a.html) · [Fairlearn](https://fairlearn.org/v0.12/user_guide/mitigation/reductions.html)
