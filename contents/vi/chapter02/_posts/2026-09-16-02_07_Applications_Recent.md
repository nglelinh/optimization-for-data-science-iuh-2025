---
layout: post
title: 02-07 Ứng dụng và phát triển gần đây
chapter: '02'
order: 17
owner: Nguyen Le Linh
categories:
- chapter02
lang: vi
lesson_type: optional
---

Đơn hình xác suất (probability simplex), quả cầu chuẩn và đa diện không phải là những hình vẽ cổ điển nằm yên trong sách giáo khoa những năm 1970. Mỗi giây trên toàn cầu, tầng đầu ra **Softmax** của mọi mô hình ngôn ngữ lớn đang chiếu hàng trăm nghìn điểm logit thẳng vào bên trong một **đơn hình xác suất**; các hệ thống học máy bền vững (Distributionally Robust Optimization) đang tối ưu trong **quả cầu Wasserstein** lồi; và các nền tảng phân bổ nguồn lực công bằng đang vận hành trên **đa diện Birkhoff**!

Bài đọc mở rộng này kết nối trực tiếp hình học tập lồi Chương 02 với các chủ đề nghiên cứu mũi nhọn giai đoạn 2022–2026.

## Bản đồ kiến thức nền: Ba miền lồi trong AI và dữ liệu hiện đại

- **Đơn hình xác suất $$\Delta_K$$ và ánh xạ Softmax:** Đầu ra xác suất của mạng phân loại hay LLM luôn bị ràng buộc nằm trong tập lồi $$\Delta_K = \{p \ge 0 : \mathbf{1}^T p = 1\}$$, với các đỉnh là các vector one-hot đại diện cho quyết định chắc chắn tuyệt đối.
- **Quả cầu Wasserstein (Tối ưu bền vững theo phân phối — DRO):** Thay vì tin mù quáng vào phân phối mẫu quan sát được $$\hat P$$, ta tối ưu trường hợp xấu nhất trên một quả cầu lồi các phân phối xác suất quanh $$\hat P$$ đo bằng khoảng cách vận chuyển tối ưu Wasserstein.
- **Đa diện công bằng và phân bổ tài nguyên (Fairness Polytopes):** Các ràng buộc tỷ lệ đại diện nhóm hay ma trận song ngẫu nhiên (Birkhoff polytope) đều tạo thành đa diện lồi, cho phép giải bài toán phân bổ công bằng bằng quy hoạch tuyến tính hoặc chiếu lồi.

### Khung giải thích (nên đọc chậm): Quan sát Softmax và tham số nhiệt độ $$\tau$$ dịch chuyển điểm trong đơn hình $$\Delta_3$$

Cho vector logit đầu ra của 3 lớp $$z = (2, 1, 0)^T$$. Ánh xạ Softmax với nhiệt độ $$\tau > 0$$ là $$p_i(\tau) = \frac{e^{z_i/\tau}}{\sum_j e^{z_j/\tau}} \in \Delta_3$$:

1. **Nhiệt độ chuẩn $$\tau = 1$$:**
   $$e^2 \approx 7.389,\quad e^1 \approx 2.718,\quad e^0 = 1.000 \implies \text{tổng } Z_1 \approx 11.107.$$
   Vector xác suất là:
   $$p(1) \approx \left(\frac{7.389}{11.107},\ \frac{2.718}{11.107},\ \frac{1.000}{11.107}\right) \approx (0.665,\ 0.245,\ 0.090) \in \operatorname{int}(\Delta_3).$$
2. **Hạ nhiệt độ xuống $$\tau = 0.5$$ (nhân đôi logit thành $$(4, 2, 0)$$):**
   $$e^4 \approx 54.598,\quad e^2 \approx 7.389,\quad e^0 = 1.000 \implies \text{tổng } Z_{0.5} \approx 62.987.$$
   Vector xác suất trở thành:
   $$p(0.5) \approx (0.867,\ 0.117,\ 0.016) \in \Delta_3.$$
3. **Trực giác hình học trên đơn hình $$\Delta_3$$:** Khi $$\tau \to 0^+$$, điểm $$p(\tau)$$ tiến sát về **đỉnh cực biên** $$(1, 0, 0)$$ (lựa chọn tham lam argmax); ngược lại khi $$\tau \to \infty$$, $$p(\tau)$$ kéo về đúng **trọng tâm** $$(1/3, 1/3, 1/3)$$ của đơn hình!

---

Tập lồi là miền khả thi mà mọi tổ hợp trung bình có trọng số không âm của các điểm trong đó vẫn nằm lại bên trong miền. Tính chất hình học này giải thích vì sao nhiều tập ràng buộc trong học máy hiện đại có dạng đơn hình, hình cầu hoặc phổ diện (spectrahedron). Bài này điểm qua ba họ tập lồi xuất hiện thường xuyên trong các công trình và thư viện giai đoạn 2022–2025, mỗi họ gắn trực tiếp với một định nghĩa đã học: đơn hình xác suất, quả cầu Wasserstein trong không gian phân phối, và đa diện xác định bởi các bất đẳng thức công bằng hoặc ngân sách.

## Đơn hình xác suất, softmax và hình học lớp cuối

Đơn hình chuẩn

$$
\Delta^{n-1} = \bigl\{ p\in\mathbb{R}^n : p\ge 0,\; \mathbf{1}^\top p = 1\bigr\}
$$

là một tập lồi (giao của một siêu phẳng với góc phần tư không âm). Hàm softmax là ánh xạ trơn đưa vector logit *vào* phần trong tương đối của $$\Delta^{n-1}$$. Nhờ vậy, mọi đầu attention trong kiến trúc Transformer và mọi mô hình hồi quy logistic đa lớp đều dùng tầng phi tuyến cuối để chiếu vector logit lên một tập lồi có thể hình dung trực tiếp trong $$\mathbb{R}^2$$ và $$\mathbb{R}^3$$.

Một cấu trúc đơn hình khác xuất hiện ở giai đoạn *cuối* quá trình huấn luyện mạng nơ-ron sâu. Papyan, Han và Donoho (*Prevalence of neural collapse*, [PNAS 2020](https://www.pnas.org/doi/10.1073/pnas.2015509117); [arXiv:2008.08186](https://arxiv.org/abs/2008.08186)) quan sát thấy các vector trung bình lớp (đã quy tâm) ở tầng áp chót hội tụ về một *khung chặt đều góc đơn hình* (simplex equiangular tight frame, gọi tắt là simplex ETF) — cấu hình điểm đối xứng nhất trên mặt cầu. Zhu, Ding, Zhou và cộng sự (*A Geometric Analysis of Neural Collapse with Unconstrained Features*, [NeurIPS 2021](https://papers.nips.cc/paper/2021/hash/f92586a25bb3145facd64ab20fd554ff-Abstract.html)) sau đó chứng minh rằng trong mô hình đặc trưng không ràng buộc với hàm mất mát cross-entropy và suy giảm trọng số (weight decay), mọi cấu hình ETF đều là cực tiểu toàn cục còn mọi điểm dừng khác đều là điểm yên ngựa chặt. Như vậy, hình học tập lồi gắn trực tiếp với cấu trúc nghiệm của bài toán: ETF là một tập con xác định trên mặt cầu, còn đơn hình xác suất là miền đầu ra thực tế của bộ phân loại.

Khi luyện tập kiểm tra tính lồi của một tập $$C$$, nên luôn đưa $$\Delta^{n-1}$$ và hình cầu Euclidean vào nhóm ví dụ nền tảng, vì đây là cấu trúc hình học của nhiều bài toán phân loại và chuẩn hóa (regularization).

## Quả cầu Wasserstein như tập bất định phân phối

Tối ưu hóa vững theo phân phối (Distributionally Robust Optimization — DRO) thay phân phối thực nghiệm $$\hat{P}$$ bằng một *tập* các phân phối lân cận, rồi tối ưu theo trường hợp xấu nhất trong tập đó. Quả cầu Wasserstein

$$
\mathcal{B}_\varepsilon(\hat{P}) = \bigl\{ Q : W_p(Q,\hat{P}) \le \varepsilon\bigr\}
$$

là một tập lồi trong không gian các độ đo xác suất (quả cầu theo khoảng cách vận chuyển tối ưu). Nhờ đó, bài toán tối ưu chống lại phân phối xấu nhất $$Q\in\mathcal{B}_\varepsilon(\hat{P})$$ thường có thể viết lại thành một bài toán tối ưu lồi hữu hạn chiều.

Hai tài liệu tham khảo chính gồm: Gao và Kleywegt, “Distributionally Robust Stochastic Optimization with Wasserstein Distance,” [*Mathematics of Operations Research* 48(2):603–655, 2023](https://doi.org/10.1287/moor.2022.1275), chứng minh đối ngẫu mạnh cho DRO Wasserstein và mô tả cấu trúc phân phối trường hợp xấu nhất; và bài hướng dẫn của Kuhn, Mohajerin Esfahani, Nguyen và Shafieezadeh-Abadeh, *Wasserstein Distributionally Robust Optimization* ([INFORMS TutORials 2019](https://doi.org/10.1287/educ.2019.0198); [arXiv:1908.08729](https://arxiv.org/abs/1908.08729), bản cập nhật tháng 11/2024), trình bày rõ mối liên hệ giữa quả cầu Wasserstein với các bài toán phân loại, hồi quy và ước lượng hợp lý cực đại (MLE). Ngoài ra, bài khảo sát tổng quan năm 2025 trên *Acta Numerica* ([Kuhn, Shafiee, et al.](https://www.cambridge.org/core/journals/acta-numerica/article/distributionally-robust-optimization/5B4E65E3A5A2AEF24E218A6B34E6EAA2)) đặt quả cầu Wasserstein trong tương quan với các loại tập bất định phân phối khác.

Cách mô hình hóa này tương tự việc thay ước lượng điểm bằng một tập bất định lồi trong quy hoạch tuyến tính vững, chỉ khác ở chỗ "điểm" ở đây là một phân phối xác suất. Khi $$\mathcal{B}_\varepsilon(\hat{P})$$ là tập lồi và hàm mục tiêu ứng với phân phối xấu nhất lồi theo biến quyết định, bài toán DRO bên ngoài trở thành một bài toán tối ưu lồi — dạng bài sẽ được hệ thống hóa ở Chương 04.

## Polytope công bằng và phân bổ tài nguyên

Các bất đẳng thức tuyến tính trên xác suất xác định một đa diện. Chẳng hạn, ràng buộc ngang bằng nhân khẩu học (demographic parity)

$$
\bigl| \mathbb{E}[h(X)\mid A=a] - \mathbb{E}[h(X)\mid A=a'] \bigr| \le \epsilon
$$

cắt ra một polytope trong không gian các bộ phân loại ngẫu nhiên hóa. Agarwal, Beygelzimer, Dudík, Langford và Wallach ([ICML 2018](https://proceedings.mlr.press/v80/agarwal18a.html)) xây dựng phương pháp quy giảm (reductions) xem các ràng buộc này là miền khả thi; thư viện [Fairlearn](https://fairlearn.org/v0.12/user_guide/mitigation/reductions.html) vẫn cung cấp cơ chế này thông qua đối tượng `Moment` trong các phiên bản 2025–2026.

Cấu trúc hình học tương tự cũng mô tả các ràng buộc ngân sách và phân bổ tài nguyên: $$x\ge 0$$, $$\mathbf{1}^\top x = 1$$ (phân bổ danh mục trên đơn hình), hoặc $$0\le x\le 1$$, $$Ax\le b$$ (polytope phân bổ ngân sách truyền thông dạng bài toán cái túi). Siêu phẳng phân tách ở phần sau của chương chính là chứng chỉ cho thấy một nghiệm ứng viên $$x$$ nằm ngoài polytope — cũng là dạng chứng chỉ mà các bộ giải tối ưu dùng để khẳng định bài toán vô nghiệm.

## Hai công thức hình học cốt lõi

Mọi miền ràng buộc được nhắc tới trong bài đều có thể biểu diễn dưới dạng giao của các tập lồi cơ bản hoặc quả cầu trong không gian phân phối:

$$
\mathcal{C} = \Delta^{n-1} \cap \{ x : Fx \le g \} \qquad\text{hoặc}\qquad \mathcal{B}_\varepsilon(\hat{P}).
$$

Khi từng thành phần là tập lồi thì giao của chúng cũng lồi, đảm bảo mọi bước tìm kiếm địa phương trong $$\mathcal{C}$$ diễn ra trên một miền không có "lỗ hổng". Đó chính là vai trò nền tảng của Chương 02 khi nhìn qua các bài toán attention, DRO và công bằng trong học máy.

## Nguồn

1. V. Papyan, X. Y. Han và D. L. Donoho, “Prevalence of neural collapse during the terminal phase of deep learning training,” *PNAS* 117(40):24652–24663, 2020. [DOI](https://www.pnas.org/doi/10.1073/pnas.2015509117) · [arXiv:2008.08186](https://arxiv.org/abs/2008.08186)
2. Z. Zhu, T. Ding, J. Zhou và cộng sự, “A Geometric Analysis of Neural Collapse with Unconstrained Features,” NeurIPS 2021. [tóm tắt](https://papers.nips.cc/paper/2021/hash/f92586a25bb3145facd64ab20fd554ff-Abstract.html)
3. R. Gao và A. J. Kleywegt, “Distributionally Robust Stochastic Optimization with Wasserstein Distance,” *Math. Oper. Res.* 48(2):603–655, 2023. [DOI](https://doi.org/10.1287/moor.2022.1275)
4. D. Kuhn, P. Mohajerin Esfahani, V. A. Nguyen và S. Shafieezadeh-Abadeh, “Wasserstein Distributionally Robust Optimization,” INFORMS TutORials 2019; arXiv:1908.08729 (sửa 2024). [arXiv](https://arxiv.org/abs/1908.08729)
5. A. Agarwal và cộng sự, “A Reductions Approach to Fair Classification,” ICML 2018. [PMLR](https://proceedings.mlr.press/v80/agarwal18a.html) · [Fairlearn](https://fairlearn.org/v0.12/user_guide/mitigation/reductions.html)
