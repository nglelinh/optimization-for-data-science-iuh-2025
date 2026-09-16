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

Hàm lồi là mục tiêu bạn tin được: cực tiểu địa phương là toàn cục, và chặn dưới cấp một $$f(y)\ge f(x)+\nabla f(x)^\top(y-x)$$ là siêu phẳng tựa của biểu đồ trên. Bài này chỉ ba chỗ hình học đó vẫn làm việc trong học máy 2021–2025 — ngay cả khi *toàn bộ* mạng sâu không lồi.

## Cross-entropy, log-sum-exp và hiệu chỉnh xác suất

Với ánh xạ đặc trưng cố định, hồi quy logistic đa lớp lồi theo trọng số lớp cuối. Với logit $$z\in\mathbb{R}^C$$ và nhãn one-hot $$y$$,

$$
\ell(z,y) = -z_y + \log\sum_{c=1}^C e^{z_c}
$$

lồi theo $$z$$ vì log-sum-exp lồi và tăng theo từng tọa độ, còn $$-z_y$$ affine. Quy tắc hợp thành ở 03-02 chính là chứng chỉ. Xác suất softmax là $$\nabla$$ của log-sum-exp; liên hợp của log-sum-exp là entropy âm trên đơn hình (03-03). Đó là lý do temperature scaling — thay $$z$$ bằng $$z/T$$ và khớp một vô hướng $$T$$ trên tập kiểm — là bài toán *lồi* một chiều.

Guo và cộng sự (2017) phổ biến temperature scaling như ánh xạ hiệu chỉnh sau huấn luyện. Minderer, Djolonga, Romijnders, Hubis, Zhai, Houlsby, Tran và Lucic (*Revisiting the Calibration of Modern Neural Networks*, [NeurIPS 2021](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html); [arXiv:2106.07998](https://arxiv.org/abs/2106.07998)) đo lại hiệu chỉnh trên lưới lớn các mô hình ảnh hiện đại, gồm Vision Transformer và MLP-Mixer, và thấy vài kiến trúc không-tích-chập gần đây *hiệu chỉnh tốt hơn* CNN quá tự tin của thế hệ trước. Nội dung tối ưu cho môn học nhỏ hơn khẳng định thực nghiệm: mất mát bạn đã biết lồi theo logit, và nhiệt độ một tham số là hiệu chỉnh lại lồi.

## Neural collapse: khi mạng không lồi gặp lớp cuối lồi

Sau khi nội suy, bộ phân loại đã huấn luyện thường vào *pha cuối* trong đó đặc trưng lớp cuối sụp về trung bình lớp, các trung bình tạo simplex ETF, và bộ phân loại thẳng hàng với trung bình (Papyan, Han và Donoho, [PNAS 2020](https://www.pnas.org/doi/10.1073/pnas.2015509117)). Zhu, Ding, Zhou và đồng tác giả ([NeurIPS 2021](https://papers.nips.cc/paper/2021/hash/f92586a25bb3145facd64ab20fd554ff-Abstract.html)) phân tích mô hình đặc trưng tự do *tách* lớp cuối: đặc trưng và trọng số phân loại là biến tự do, mất mát là cross-entropy cộng weight decay. Trong mô hình đó địa hình lành — cấu hình ETF là cực tiểu toàn cục duy nhất, các điểm dừng khác là yên ngựa chặt với độ cong âm.

Bài học cho Chương 03 không phải “mạng sâu là lồi.” Mà là mảnh *lồi* bạn gọi được tên (cross-entropy theo kích hoạt và trọng số lớp cuối, cộng regularizer Euclid) đã giải thích một phần đáng kể hình học người ta đo ở cuối huấn luyện. Khi bài báo nói lớp cuối “sụp,” hãy dịch: bài toán lớp cuối lồi, với đặc trưng tự do, muốn một cấu hình rất đối xứng.

## Mất mát đối sánh và surrogate lồi

Học đối sánh tự giám sát (SimCLR, CLIP và các đời sau) thường tối thiểu mất mát kiểu InfoNCE. Với biểu diễn neo $$u$$, dương $$v_+$$ và các âm $$v_1,\ldots,v_K$$,

$$
\ell = -\log \frac{e^{u^\top v_+/\tau}}{e^{u^\top v_+/\tau} + \sum_{k=1}^K e^{u^\top v_k/\tau}}.
$$

Như hàm của *độ tương tự* (hoặc của $$u$$ khi giữ các $$v$$ cố định), đây lại là log-sum-exp của dạng tuyến tính, nên lồi theo $$u$$. Toàn mạng sâu không lồi, nhưng mọi đầu đối sánh trong là bài phân loại lồi trên siêu cầu. Wang và Isola (*Understanding Contrastive Representation Learning through Alignment and Uniformity*, [ICML 2020](https://proceedings.mlr.press/v119/wang20k.html)) tách mục tiêu InfoNCE tiệm cận thành hạng alignment (kéo cặp dương lại) và hạng uniformity (trải đặc trưng trên cầu). Năm 2020 nằm sát trước cửa sổ yêu cầu; cùng mất mát đó vẫn là mặc định trong mô hình thị giác–ngôn ngữ 2022–2026, kể cả các thiết lập kiểu CLIP mà Lion sau này so sánh (Chương 06).

## Ba dòng kiểm tra bằng NumPy

Tính lồi của log-sum-exp không phải khẩu hiệu. Đoạn sau kiểm bất đẳng thức Jensen trên logit ngẫu nhiên — định nghĩa ở 03-01.

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

Nếu đoạn này thất bại trên số thực hữu hạn sau phép dịch max chuẩn, đó là lỗi mã, không phải phản ví dụ.

## Điều cần mang đi

Khi viết mất mát, hãy hỏi nó có lồi theo *đối số cuối* mà bộ giải nhìn thấy không (logit, độ tương tự, dự đoán tuyến tính). Nếu có, quy tắc hợp thành và liên hợp của chương này áp dụng, dù ánh xạ đặc trưng phía trước là Transformer. Hiệu chỉnh, neural collapse và đầu đối sánh là ba câu chuyện khác nhau với cùng nguyên tử lồi: log-sum-exp.

## Nguồn

1. M. Minderer và cộng sự, “Revisiting the Calibration of Modern Neural Networks,” NeurIPS 2021. [tóm tắt](https://proceedings.neurips.cc/paper/2021/hash/8420d359404024567b5aefda1231af24-Abstract.html) · [arXiv:2106.07998](https://arxiv.org/abs/2106.07998)
2. V. Papyan, X. Y. Han và D. L. Donoho, “Prevalence of neural collapse…,” *PNAS* 2020. [DOI](https://www.pnas.org/doi/10.1073/pnas.2015509117)
3. Z. Zhu, T. Ding, J. Zhou và cộng sự, “A Geometric Analysis of Neural Collapse with Unconstrained Features,” NeurIPS 2021. [tóm tắt](https://papers.nips.cc/paper/2021/hash/f92586a25bb3145facd64ab20fd554ff-Abstract.html)
4. T. Wang và P. Isola, “Understanding Contrastive Representation Learning through Alignment and Uniformity,” ICML 2020. [PMLR](https://proceedings.mlr.press/v119/wang20k.html)
