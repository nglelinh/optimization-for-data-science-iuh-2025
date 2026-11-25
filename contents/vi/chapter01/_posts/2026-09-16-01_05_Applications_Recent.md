---
layout: post
title: 01-05 Ứng dụng và phát triển gần đây
chapter: '01'
order: 6
owner: Nguyen Le Linh
categories:
- chapter01
lang: vi
lesson_type: optional
---

Khi bạn đọc công thức ngắn gọn $$\min_{x \in \mathcal{C}} f(x)$$ ở Chương 01, rất dễ nghĩ nó chỉ dành cho những bài toán nhỏ trên giấy. Nhưng hãy nhìn vào các bài báo AI gây chấn động nhất giai đoạn 2022–2026: từ định luật mở rộng Chinchilla quyết định cách chi hàng chục triệu USD huấn luyện LLM, khung Predict-then-Optimize (SPO+) nối dự báo học máy với quyết định vận trù học, cho đến các ràng buộc công bằng (fairness) trong chấm điểm tín dụng — tất cả đều viết trực tiếp bằng đúng bộ khung của Chương 01!

Bài đọc mở rộng này giúp bạn luyện kỹ năng đọc các bài báo khoa học dữ liệu hiện đại dưới lăng kính của một nhà tối ưu hóa: nhận diện biến, hàm mất mát thay thế và tập ràng buộc.

## Kiến thức cần nhớ: Ba mặt trận ứng dụng hiện đại của khung Chương 01

- **Cực tiểu hóa rủi ro thực nghiệm dưới ngân sách tính toán (Compute-Optimal ERM):** Tối ưu hóa việc phân bổ ngân sách FLOP cố định $$C \approx 6ND$$ giữa kích thước mô hình $$N$$ và số token huấn luyện $$D$$ để cực tiểu hóa hàm mất mát kiểm thử $$L(N, D)$$.
- **Predict-then-Optimize và hàm thay thế lồi SPO+:** Khi đầu ra của mô hình dự báo được nạp vào một bài toán LP hạ nguồn, cực tiểu hóa sai số dự báo MSE chưa chắc cho quyết định tốt nhất; hàm mất mát SPO+ thay thế bài toán rời rạc khó bằng một chặn trên **lồi** tối ưu hóa trực tiếp chất lượng quyết định.
- **Công bằng thuật toán như ràng buộc tối ưu (Fairness-Constrained Optimization):** Biến các tiêu chuẩn đạo đức (như chênh lệch tỷ lệ chọn giữa hai nhóm nhân khẩu học không quá $$\epsilon$$) thành ràng buộc bất đẳng thức tường minh bên cạnh hàm mục tiêu độ chính xác.

### Giải thích: Tính tay phân bổ ngân sách huấn luyện theo luật Chinchilla

Trong nghiên cứu Chinchilla (Hoffmann et al., 2022), tổng chi phí huấn luyện một mô hình ngôn ngữ có $$N$$ tham số trên $$D$$ token xấp xỉ $$C = 6ND$$ (FLOPs), và nghiệm tối ưu của bài toán $$\min_{N, D} L(N, D)$$ dưới ràng buộc $$6ND = C$$ cho tỷ lệ vàng xấp xỉ $$D^* \approx 20 N^*$$.

Giả sử bạn có ngân sách cố định $$C = 6 \times 10^{18}$$ FLOPs:

1. **Thay quan hệ tối ưu $$D = 20N$$ vào ràng buộc ngân sách:**
   $$6 \cdot N \cdot (20N) = 6 \times 10^{18} \implies 120 N^2 = 6 \times 10^{18}.$$
2. **Giải tìm số tham số tối ưu $$N^*$$:**
   $$N^2 = \frac{6 \times 10^{18}}{120} = 5 \times 10^{16} \implies N^* = \sqrt{5} \times 10^8 \approx 2.24 \times 10^8 \text{ (224 triệu tham số)}.$$
3. **Suy ra số token huấn luyện tối ưu $$D^*$$:**
   $$D^* = 20 N^* \approx 4.47 \times 10^9 \text{ (4.47 tỷ token)}.$$
4. **Kiểm tra ngược ràng buộc:** $$6 N^* D^* = 6 \times (2.236 \times 10^8) \times (4.472 \times 10^9) \approx 6.00 \times 10^{18}$$ FLOPs. Nếu bạn phạm sai lầm xây mô hình lớn gấp 4 lần ($$900$$ triệu tham số) nhưng chỉ huấn luyện trên $$1.1$$ tỷ token (cùng ngân sách $$C$$), mô hình sẽ rơi vào vùng *thiếu dữ liệu* và có hàm mất mát kém tối ưu hơn rõ rệt!

---

Chương 01 định nghĩa bài toán tối ưu hóa là “chọn $$x\in\mathcal{C}$$ để làm $$f(x)$$ nhỏ nhất”. Cấu trúc này hiện là nền tảng của khoa học dữ liệu trong công nghiệp: huấn luyện mô hình dự đoán (thường qua cực tiểu hóa rủi ro thực nghiệm), sau đó đưa dự đoán vào một bài toán ra quyết định *ở bước tiếp theo*, đôi khi kèm theo ràng buộc công bằng hoặc giới hạn vận hành. Bài đọc này xem xét ba bối cảnh cụ thể giai đoạn 2022–2026. Các định nghĩa ở 01-01 và 01-02 giữ nguyên; ta chỉ cập nhật những *ví dụ* điển hình mà người làm khoa học dữ liệu cần nắm được.

## ERM quy mô lớn: mô hình ngôn ngữ tối ưu theo tính toán

Tiền huấn luyện mô hình ngôn ngữ lớn là một bài toán cực tiểu hóa rủi ro thực nghiệm với hàm mất mát dự đoán token kế tiếp (hoặc token bị che). Gọi $$N$$ là số tham số và $$D$$ là số token huấn luyện. Với ngân sách tính toán cố định $$C$$ (tính bằng FLOPs), ta có quan hệ xấp xỉ $$C \propto N\cdot D$$. Câu hỏi thiết kế trung tâm không phải “bài toán này có lồi không?” — huấn luyện Transformer là không lồi — mà là cặp $$(N,D)$$ nào cho giá trị mất mát nhỏ nhất dưới ngân sách $$C$$ cho trước.

Hoffmann, Borgeaud, Mensch, Sifre và cộng sự (*Training Compute-Optimal Large Language Models*, [NeurIPS 2022](https://proceedings.neurips.cc/paper/2022/hash/c1e2faff6f588870935f114ebe04a3e5-Abstract-Conference.html); [arXiv:2203.15556](https://arxiv.org/abs/2203.15556)) huấn luyện hơn 400 mô hình và chỉ ra rằng, để tối ưu theo ngân sách tính toán, kích thước mô hình và lượng dữ liệu huấn luyện cần tăng cùng tỷ lệ: khi tăng gấp đôi $$N$$ thì cũng nên tăng gấp đôi $$D$$. Mô hình Chinchilla 70 tỷ tham số, huấn luyện trên khoảng 1.4 nghìn tỷ token với cùng ngân sách tính toán như Gopher 280 tỷ tham số, vượt trội hơn Gopher, GPT-3 và nhiều mô hình lớn hơn nhưng thiếu dữ liệu trên nhiều bộ kiểm chuẩn, đạt 67.5% trên MMLU. Bài giới thiệu kèm theo của DeepMind nằm [tại đây](https://deepmind.google/blog/an-empirical-analysis-of-compute-optimal-large-language-model-training/).

Đối với khóa học này, bài học rút ra mang tính cấu trúc. *Dạng bài toán* vẫn là

$$
\min_w \frac{1}{n}\sum_{i=1}^n \ell\bigl(h_w(x_i), y_i\bigr),
$$

nhưng *biến quyết định của bài toán thiết kế bên ngoài* là $$N$$ và $$D$$, không chỉ riêng trọng số $$w$$. Điều giúp Chinchilla thành công không phải tính lồi, mà là việc *đặt đúng* bài toán tối ưu hóa.

## Predict-then-optimize và hàm thay thế lồi SPO+

Nhiều quy trình phân tích gồm hai bước nối tiếp: dự đoán vector chi phí $$\hat{c}$$ từ đặc trưng đầu vào, sau đó giải bài toán

$$
\min_{z\in\mathcal{Z}} \hat{c}^\top z
$$

để đưa ra quyết định định tuyến, tồn kho hoặc phân bổ danh mục $$z$$. Huấn luyện bộ dự đoán nhằm cực tiểu hóa sai số bình phương trên $$c$$ có thể không phản ánh đúng mục tiêu cuối cùng: một sai số nhỏ của $$\hat{c}$$ nhưng làm thay đổi đỉnh tối ưu của $$\mathcal{Z}$$ có thể gây thiệt hại lớn hơn nhiều so với một sai số lớn nhưng không làm đổi quyết định.

Elmachtoub và Grigas (*Smart “Predict, then Optimize”*, [Management Science 68(1):9–26, 2022](https://doi.org/10.1287/mnsc.2020.3922); [arXiv:1710.08005](https://arxiv.org/abs/1710.08005)) định nghĩa hàm mất mát SPO để đo trực tiếp *sai số quyết định* gây ra bởi $$\hat{c}$$. Do hàm mất mát này khó tối ưu trực tiếp, họ xây dựng hàm thay thế (surrogate) lồi **SPO+** từ tính đối ngẫu và chứng minh tính vững Fisher (Fisher consistency) dưới các điều kiện nhẹ. Hàm thay thế này áp dụng được cho mọi bài toán tối ưu đa diện, lồi hoặc quy hoạch nguyên hỗn hợp có hàm mục tiêu tuyến tính. Các thực nghiệm trên bài toán đường đi ngắn nhất và tối ưu danh mục cho thấy mô hình tuyến tính huấn luyện theo SPO+ có thể vượt qua các bộ dự đoán phức tạp hơn nhưng chỉ tối ưu sai số dự đoán khi mô hình bị chỉ định sai (misspecified).

Đây là tinh thần của Chương 01 ở dạng cô đọng: viết ra mục tiêu *thực sự* (chất lượng quyết định), rồi thay thế bằng một bài toán quy hoạch lồi có thể giải hiệu quả.

## Công bằng như bài toán tối ưu có ràng buộc

Các tiêu chí công bằng theo nhóm — như demographic parity, equalized odds và các biến thể liên quan — thực chất là các *ràng buộc* trên bộ phân loại chứ không chỉ là khẩu hiệu trình bày. Agarwal, Beygelzimer, Dudík, Langford và Wallach (*A Reductions Approach to Fair Classification*, [ICML 2018](https://proceedings.mlr.press/v80/agarwal18a.html)) quy bài toán “cực tiểu hóa sai số phân loại dưới các bất đẳng thức công bằng” về một dãy các bài toán phân loại nhạy chi phí. Đối tượng cốt lõi ở đây là tập khả thi gồm các bộ phân loại (ngẫu nhiên hóa) thỏa mãn ràng buộc công bằng; phép quy về tìm một điểm có sai số thấp trong tập đó.

Cơ chế quy về này là nền tảng của thư viện đang được duy trì [Fairlearn](https://fairlearn.org/) (`ExponentiatedGradient` và các ràng buộc `Moment`; tài liệu hướng dẫn: [reductions](https://fairlearn.org/v0.12/user_guide/mitigation/reductions.html)). Bộ công cụ này vẫn xuất hiện phổ biến trong các đồ án giai đoạn 2024–2026 và các quy trình kiểm toán công bằng trong công nghiệp. Dù bài báo gốc công bố năm 2018 (trước mốc 2022–2026), đây vẫn là tài liệu chuẩn mà phần mềm hiện hành trích dẫn và triển khai.

Một mô hình phác thảo — không hàm ý rằng sai số và ràng buộc công bằng luôn lồi — có dạng:

$$
\begin{align}
\min_h \quad & \widehat{\mathrm{err}}(h) \\
\text{s.t.} \quad & \bigl|\Pr(\hat{Y}=1\mid A=a) - \Pr(\hat{Y}=1\mid A=a')\bigr| \le \epsilon
\end{align}
$$

với $$A$$ là thuộc tính nhạy cảm. Chương 02 sẽ phân tích khi nào tập ràng buộc là tập lồi, còn Chương 04 sẽ giải thích vì sao nghiệm địa phương của phiên bản lồi hóa cũng là nghiệm toàn cục.

## Cách đọc một bài báo “tối ưu hóa cho khoa học dữ liệu”

Hãy đặt bốn câu hỏi nền tảng mà chương này trang bị: Biến quyết định là gì? Hàm mục tiêu mà tác giả *thực sự* quan tâm là gì, và hàm thay thế (surrogate) họ thực sự cực tiểu hóa là gì? Tập khả thi có dạng nào (hình hộp, đơn hình, bất đẳng thức công bằng hay bao lồi nguyên)? Bài toán có lồi không, và nếu không thì bài toán con nào bên trong là lồi? Chinchilla, SPO và Fairlearn là ba cách trả lời khác nhau cho chính bốn câu hỏi này.

## Nguồn

1. J. Hoffmann và cộng sự, “Training Compute-Optimal Large Language Models,” NeurIPS 2022. [tóm tắt](https://proceedings.neurips.cc/paper/2022/hash/c1e2faff6f588870935f114ebe04a3e5-Abstract-Conference.html) · [arXiv:2203.15556](https://arxiv.org/abs/2203.15556)
2. A. N. Elmachtoub và P. Grigas, “Smart ‘Predict, then Optimize’,” *Management Science* 68(1):9–26, 2022. [DOI](https://doi.org/10.1287/mnsc.2020.3922) · [arXiv:1710.08005](https://arxiv.org/abs/1710.08005)
3. A. Agarwal, A. Beygelzimer, M. Dudík, J. Langford và H. Wallach, “A Reductions Approach to Fair Classification,” ICML 2018. [PMLR](https://proceedings.mlr.press/v80/agarwal18a.html) · [Fairlearn reductions](https://fairlearn.org/v0.12/user_guide/mitigation/reductions.html)
