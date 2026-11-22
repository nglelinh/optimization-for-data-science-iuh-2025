---
layout: post
title: 03-08 Ứng dụng và phát triển gần đây
chapter: '03'
order: 16
owner: Nguyen Le Linh
categories:
- chapter03
lang: vi
lesson_type: optional
---

Hàm lồi là dạng hàm mục tiêu có cấu trúc thuận lợi nhất trong tối ưu hóa: mọi cực tiểu địa phương đều là cực tiểu toàn cục, và chặn dưới bậc nhất $$f(y)\ge f(x)+\nabla f(x)^\top(y-x)$$ xác định một siêu phẳng hỗ trợ cho epigraph của hàm. Bài này trình bày ba ngữ cảnh trong học máy giai đoạn 2021–2025 nơi cấu trúc lồi vẫn phát huy tác dụng trực tiếp — ngay cả khi *toàn bộ* mạng nơ-ron sâu là không lồi.

## Cross-entropy, log-sum-exp và hiệu chỉnh xác suất

Khi ánh xạ đặc trưng được cố định, bài toán hồi quy logistic đa lớp là bài toán lồi theo trọng số lớp cuối. Với vector logit $$z\in\mathbb{R}^C$$ và nhãn one-hot $$y$$, hàm mất mát

$$
\ell(z,y) = -z_y + \log\sum_{c=1}^C e^{z_c}
$$

là hàm lồi theo $$z$$ vì log-sum-exp lồi và tăng theo từng tọa độ, còn $$-z_y$$ là hàm affine (suy trực tiếp từ các quy tắc hợp thành ở bài 03-02). Gradient của log-sum-exp chính là phân phối xác suất softmax, còn hàm liên hợp của nó là hàm entropy âm trên đơn hình xác suất (bài 03-03). Nhờ cấu trúc này, phương pháp *temperature scaling* — thay $$z$$ bằng $$z/T$$ và điều chỉnh một tham số vô hướng $$T$$ trên tập kiểm định — trở thành một bài toán tối ưu *lồi* một chiều.

Guo và cộng sự (2017) đã phổ biến temperature scaling như một bước hiệu chỉnh xác suất sau huấn luyện. Minderer, Djolonga, Romijnders, Hubis, Zhai, Houlsby, Tran và Lucic (*Revisiting the Calibration of Modern Neural Networks*, [NeurIPS 2021](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html); [arXiv:2106.07998](https://arxiv.org/abs/2106.07998)) khảo sát lại độ hiệu chỉnh trên diện rộng nhiều mô hình thị giác hiện đại như Vision Transformer và MLP-Mixer, cho thấy một số kiến trúc không dùng tích chập có độ hiệu chỉnh tốt hơn các mạng CNN quá tự tin trước đây. Dưới góc độ tối ưu hóa, điểm cốt lõi rất gọn: hàm mất mát là lồi theo logit, nên bước hiệu chỉnh bằng một tham số nhiệt độ là một bài toán tối ưu lồi.

## Neural collapse: khi mạng không lồi gặp lớp cuối lồi

Sau khi đạt mức nội suy trên tập huấn luyện, các mô hình phân loại sâu thường bước vào *giai đoạn cuối* với hiện tượng đặc trưng lớp áp chót hội tụ về trung bình lớp, các trung bình lớp tạo thành một khung chặt đều góc đơn hình (simplex ETF), và các vector trọng số phân loại thẳng hàng với các trung bình lớp đó (Papyan, Han và Donoho, [PNAS 2020](https://www.pnas.org/doi/10.1073/pnas.2015509117)). Zhu, Ding, Zhou và cộng sự ([NeurIPS 2021](https://papers.nips.cc/paper/2021/hash/f92586a25bb3145facd64ab20fd554ff-Abstract.html)) phân tích mô hình đặc trưng không ràng buộc tách riêng lớp cuối — coi đặc trưng và trọng số phân loại là các biến tự do với hàm mất mát cross-entropy kèm suy giảm trọng số (weight decay) — và chỉ ra rằng địa hình tối ưu có cấu trúc thuận lợi: mọi cấu hình ETF đều là cực tiểu toàn cục, còn mọi điểm dừng khác đều là điểm yên ngựa chặt có độ cong âm.

Bài học cho Chương 03 không phải là "mạng nơ-ron sâu là lồi", mà là thành phần *lồi* ở lớp cuối (cross-entropy theo đặc trưng và trọng số kèm số hạng chuẩn hóa Euclidean) đã giải thích phần lớn cấu trúc hình học quan sát được ở cuối quá trình huấn luyện: khi đặc trưng đủ tự do, bài toán lớp cuối tự nhiên dẫn đến một cấu hình rất đối xứng.

## Mất mát đối sánh và thành phần lồi

Các phương pháp học đối sánh tự giám sát (như SimCLR, CLIP và các biến thể tiếp theo) thường cực tiểu hóa hàm mất mát dạng InfoNCE. Với vector biểu diễn neo $$u$$, mẫu dương $$v_+$$ và các mẫu âm $$v_1,\ldots,v_K$$:

$$
\ell = -\log \frac{e^{u^\top v_+/\tau}}{e^{u^\top v_+/\tau} + \sum_{k=1}^K e^{u^\top v_k/\tau}}.
$$

Xét theo các độ tương tự (hoặc theo $$u$$ khi cố định các vector $$v$$), biểu thức này tiếp tục có dạng log-sum-exp của các hàm tuyến tính nên là hàm lồi theo $$u$$. Dù toàn bộ mạng nơ-ron không lồi, đầu đối sánh ở lớp trên cùng vẫn là một bài toán phân loại lồi trên mặt cầu. Wang và Isola (*Understanding Contrastive Representation Learning through Alignment and Uniformity*, [ICML 2020](https://proceedings.mlr.press/v119/wang20k.html)) phân tích mục tiêu InfoNCE ở giới hạn tiệm cận thành hai thành phần: *alignment* (kéo cặp mẫu dương lại gần nhau) và *uniformity* (phân bố đều đặc trưng trên mặt cầu). Dù công bố năm 2020, hàm mất mát này vẫn là tiêu chuẩn trong nhiều mô hình thị giác–ngôn ngữ giai đoạn 2022–2026, bao gồm các thiết lập kiểu CLIP được so sánh với bộ tối ưu Lion ở Chương 06.

## Kiểm chứng nhanh bằng NumPy

Đoạn mã sau kiểm tra trực tiếp bất đẳng thức Jensen (định nghĩa ở bài 03-01) cho hàm log-sum-exp trên hai vector logit ngẫu nhiên:

```python
import numpy as np

def lse(z):
    m = np.max(z)
    return m + np.log(np.sum(np.exp(z - m)))

rng = np.random.default_rng(0)
z1, z2 = rng.normal(size=5), rng.normal(size=5)
t = 0.3
lhs = lse((1 - t) * z1 + t * z2)
rhs = (1 - t) * lse(z1) + t * lse(z2)
print(lhs, "<=", rhs, "?", lhs <= rhs + 1e-12)
```

Nếu đoạn kiểm tra này sai trên các số thực hữu hạn sau khi đã dịch theo giá trị lớn nhất `m`, nguyên nhân chắc chắn nằm ở lỗi lập trình chứ không phải phản ví dụ toán học.

## Điểm cốt lõi cần nhớ

Khi thiết kế một hàm mất mát, câu hỏi đầu tiên nên đặt ra là liệu hàm có lồi theo *đối số cuối cùng* mà nó nhận vào hay không (logit, độ tương tự hoặc dự đoán tuyến tính). Nếu có, toàn bộ các quy tắc hợp thành và lý thuyết hàm liên hợp trong chương này đều áp dụng được, bất kể kiến trúc trích xuất đặc trưng phía trước là gì. Hiệu chỉnh xác suất, hiện tượng neural collapse và hàm mất mát đối sánh là ba bài toán khác nhau nhưng cùng dựa trên một khối xây dựng lồi chung: hàm log-sum-exp.

## Nguồn

1. M. Minderer và cộng sự, “Revisiting the Calibration of Modern Neural Networks,” NeurIPS 2021. [tóm tắt](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html) · [arXiv:2106.07998](https://arxiv.org/abs/2106.07998)
2. V. Papyan, X. Y. Han và D. L. Donoho, “Prevalence of neural collapse…,” *PNAS* 2020. [DOI](https://www.pnas.org/doi/10.1073/pnas.2015509117)
3. Z. Zhu, T. Ding, J. Zhou và cộng sự, “A Geometric Analysis of Neural Collapse with Unconstrained Features,” NeurIPS 2021. [tóm tắt](https://papers.nips.cc/paper/2021/hash/f92586a25bb3145facd64ab20fd554ff-Abstract.html)
4. T. Wang và P. Isola, “Understanding Contrastive Representation Learning through Alignment and Uniformity,” ICML 2020. [PMLR](https://proceedings.mlr.press/v119/wang20k.html)
