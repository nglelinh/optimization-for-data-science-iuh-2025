---
layout: post
title: 01-05 Ứng dụng và phát triển gần đây
chapter: '01'
order: 8
owner: Nguyen Le Linh
categories:
- chapter01
lang: vi
lesson_type: optional
---

Chương 01 định nghĩa bài toán tối ưu là “chọn $$x\in\mathcal{C}$$ để làm $$f$$ nhỏ.” Câu đó hiện là kiến trúc của khoa học dữ liệu công nghiệp: huấn luyện bộ dự đoán (thường bằng tối thiểu hóa rủi ro thực nghiệm), rồi dùng bộ dự đoán trong một bài toán quyết định *phía sau*, đôi khi với ràng buộc công bằng hoặc giới hạn vận hành. Bài này đi qua ba bối cảnh cụ thể 2022–2026. Định nghĩa ở 01-01 và 01-02 giữ nguyên; ta chỉ đổi các *ví dụ* bạn cần gọi được tên.

## ERM quy mô lớn: mô hình ngôn ngữ tối ưu theo tính toán

Tiền huấn luyện mô hình ngôn ngữ là tối thiểu hóa rủi ro thực nghiệm trên mất mát token kế (hoặc token che). Gọi $$N$$ là số tham số và $$D$$ là số token huấn luyện. Ngân sách tính toán cố định $$C$$ (FLOPs) xấp xỉ thỏa $$C \propto N\cdot D$$. Câu hỏi thiết kế không phải “bài này có lồi không?” — huấn luyện Transformer không lồi — mà cặp $$(N,D)$$ nào làm mất mát nhỏ nhất với $$C$$ đó.

Hoffmann, Borgeaud, Mensch, Sifre và đồng nghiệp (*Training Compute-Optimal Large Language Models*, [NeurIPS 2022](https://proceedings.neurips.cc/paper/2022/hash/c1e2faff6f588870935f114ebe04a3e5-Abstract-Conference.html); [arXiv:2203.15556](https://arxiv.org/abs/2203.15556)) huấn luyện hơn 400 mô hình và kết luận rằng, để tối ưu theo tính toán, kích thước mô hình và số token phải tăng cùng nhau: nhân đôi $$N$$ thì nên nhân đôi $$D$$. Mô hình 70B tham số Chinchilla, huấn luyện khoảng 1.4T token với cùng tính toán như Gopher 280B, vượt Gopher, GPT-3 và các mô hình lớn hơn nhưng thiếu dữ liệu trên nhiều bài, kể cả 67.5% trên MMLU. Ghi chú kèm của DeepMind nằm [ở đây](https://deepmind.google/blog/an-empirical-analysis-of-compute-optimal-large-language-model-training/).

Với môn học, bài học mang tính cấu trúc. *Dạng* vẫn là

$$
\min_w \frac{1}{n}\sum_{i=1}^n \ell\bigl(h_w(x_i), y_i\bigr),
$$

nhưng *biến quyết định của bài toán thiết kế ngoài* là $$N$$ và $$D$$, không chỉ $$w$$. Tính lồi không phải thứ làm Chinchilla chạy được; một câu hỏi tối ưu *đặt đúng* mới là.

## Predict-then-optimize và surrogate lồi SPO+

Nhiều pipeline phân tích làm hai việc nối tiếp: dự đoán vector chi phí $$\hat{c}$$ từ đặc trưng, rồi giải

$$
\min_{z\in\mathcal{Z}} \hat{c}^\top z
$$

cho quyết định định tuyến, tồn kho hoặc danh mục $$z$$. Huấn luyện bộ dự đoán để tối thiểu sai số bình phương trên $$c$$ có thể là mục tiêu sai: một sai số nhỏ của $$\hat{c}$$ làm lật đỉnh tối ưu của $$\mathcal{Z}$$ tệ hơn một sai số lớn nhưng không đổi quyết định.

Elmachtoub và Grigas (*Smart “Predict, then Optimize”*, [Management Science 68(1):9–26, 2022](https://doi.org/10.1287/mnsc.2020.3922); [arXiv:1710.08005](https://arxiv.org/abs/1710.08005)) định nghĩa mất mát SPO tính *sai số quyết định* do $$\hat{c}$$ gây ra. Mất mát đó khó tối ưu, nên họ suy ra surrogate lồi **SPO+** từ đối ngẫu và chứng minh tính nhất quán Fisher trong điều kiện nhẹ. Surrogate áp dụng cho mọi bài toán đa diện, lồi, hoặc hỗn hợp nguyên với mục tiêu tuyến tính. Thí nghiệm đường đi ngắn nhất và danh mục cho thấy mô hình tuyến tính huấn luyện bằng SPO+ có thể thắng bộ dự đoán linh hoạt hơn nhưng tối ưu sai số dự đoán khi mô hình bị đặc tả sai.

Đây là Chương 01 thu nhỏ: viết mục tiêu *thật* (chất lượng quyết định), rồi thay bằng một chương trình lồi mà ta giải được.

## Công bằng như tối ưu có ràng buộc

Các yêu cầu công bằng nhóm — demographic parity, equalized odds và họ hàng — là *ràng buộc* trên bộ phân loại, không phải trang trí trên slide. Agarwal, Beygelzimer, Dudík, Langford và Wallach (*A Reductions Approach to Fair Classification*, [ICML 2018](https://proceedings.mlr.press/v80/agarwal18a.html)) quy “tối thiểu lỗi với bất đẳng thức công bằng” về một dãy bài phân loại nhạy chi phí. Tập khả thi các bộ phân loại (ngẫu nhiên hóa) thỏa ràng buộc mới là đối tượng bạn quan tâm; phép quy tìm điểm lỗi thấp trong tập đó.

Cùng phép quy đó là động cơ của thư viện đang được duy trì [Fairlearn](https://fairlearn.org/) (`ExponentiatedGradient` và các ràng buộc `Moment`; hướng dẫn: [reductions](https://fairlearn.org/v0.12/user_guide/mitigation/reductions.html)). Bạn vẫn gặp stack này trong đồ án 2024–2026 và rà soát công bằng trong ngành. Bài 2018 cũ hơn cửa sổ 2022–2026, nhưng đó là tài liệu mà phần mềm hiện tại trích dẫn; hãy coi là *công thức* chuẩn, không phải đề tài đã đóng.

Một chương trình sơ đồ — không phải khẳng định rằng lỗi và công bằng luôn lồi — là

$$
\begin{align}
\min_h \quad & \widehat{\mathrm{err}}(h) \\
\text{s.t.} \quad & \bigl|\Pr(\hat{Y}=1\mid A=a) - \Pr(\hat{Y}=1\mid A=a')\bigr| \le \epsilon
\end{align}
$$

với thuộc tính nhạy $$A$$. Chương 02 sẽ nói khi nào tập ràng buộc lồi; Chương 04 sẽ nói vì sao nghiệm địa phương của một thu hẹp lồi là toàn cục.

## Cách đọc một bài “tối ưu cho KHDL”

Hỏi bốn câu mà chương này đã trang bị. Biến là gì? Mục tiêu mà tác giả *khẳng định* quan tâm là gì, và surrogate họ thật sự tối thiểu là gì? Tập khả thi là gì (hộp, đơn hình, bất đẳng thức công bằng, bao lồi nguyên)? Chương trình có lồi không, và nếu không thì mảnh nào là bài giải lồi bên trong? Chinchilla, SPO và Fairlearn là ba câu trả lời khác nhau cho bốn câu đó.

## Nguồn

1. J. Hoffmann và cộng sự, “Training Compute-Optimal Large Language Models,” NeurIPS 2022. [tóm tắt](https://proceedings.neurips.cc/paper/2022/hash/c1e2faff6f588870935f114ebe04a3e5-Abstract-Conference.html) · [arXiv:2203.15556](https://arxiv.org/abs/2203.15556)
2. A. N. Elmachtoub và P. Grigas, “Smart ‘Predict, then Optimize’,” *Management Science* 68(1):9–26, 2022. [DOI](https://doi.org/10.1287/mnsc.2020.3922) · [arXiv:1710.08005](https://arxiv.org/abs/1710.08005)
3. A. Agarwal, A. Beygelzimer, M. Dudík, J. Langford và H. Wallach, “A Reductions Approach to Fair Classification,” ICML 2018. [PMLR](https://proceedings.mlr.press/v80/agarwal18a.html) · [Fairlearn reductions](https://fairlearn.org/v0.12/user_guide/mitigation/reductions.html)
