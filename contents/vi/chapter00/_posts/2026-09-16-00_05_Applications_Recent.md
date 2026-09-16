---
layout: post
title: 00-05 Ứng dụng và phát triển gần đây
chapter: '00'
order: 17
owner: Nguyen Le Linh
categories:
- chapter00
lang: vi
lesson_type: optional
---

Giải tích, đại số tuyến tính và xác suất trong chương này không phải phần “khởi động” rồi bỏ lại. Đó là ngôn ngữ làm việc của các mô hình bạn sẽ huấn luyện ngay sau tuần đầu. Bài này nối những công cụ ấy với bốn phát triển khoảng 2022–2025 mà sinh viên khoa học dữ liệu sẽ gặp trong bài báo, thư viện và thực tập. Lý thuyết các bài trước không đổi; mục tiêu là thấy *chỗ nào* gradient, phân tích hạng thấp và hàm score xuất hiện trong hệ thống thật.

## Vi phân tự động và gradient ẩn

Lan truyền ngược là quy tắc chuỗi trên đồ thị tính toán. Các framework hiện đại cài *vi phân tự động*: bạn viết hàm Python $$f$$, thư viện trả $$\nabla f$$ mà không cần Jacobian viết tay. Chuyên khảo 2024–2025 của Blondel và Roulet, *The Elements of Differentiable Programming* ([arXiv:2403.14606](https://arxiv.org/abs/2403.14606)), coi đây là mô hình lập trình chứ không phải mẹo: nếu chương trình ghép từ các nguyên tử khả vi, việc tối ưu tham số bằng gradient được định nghĩa tốt, kể cả khi có luồng điều khiển.

Một cách dùng giải tích Chương 00 kín đáo hơn là **định lý hàm ẩn**. Nếu bộ giải trả $$x^\star(\theta)$$ xác định bởi ánh xạ tối ưu $$F(x,\theta)=0$$ (ví dụ $$\nabla_x L(x,\theta)=0$$), bạn **không** lan truyền ngược qua mọi vòng lặp trong. Vi phân đồng nhất thức $$F(x^\star(\theta),\theta)=0$$ cho hệ tuyến tính

$$
\nabla_\theta x^\star = - \bigl(\nabla_x F\bigr)^{-1} \nabla_\theta F.
$$

Blondel, Berthet, Cuturi, Frostig, Hoyer, Llinares-López, Pedregosa và Vert cài cơ chế này thành *vi phân ẩn tự động* trong JAXopt ([NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/hash/228b9279ecf9bbafe582406850c57115-Abstract-Conference.html); [github.com/google/jaxopt](https://github.com/google/jaxopt)). Người dùng viết $$F$$ bằng Python; JAX vi phân $$F$$ và giải hệ tuyến tính. Chỉnh siêu tham số hồi quy ridge, meta-learning và các lớp tối ưu đều quy về đồng nhất thức này. Khi gặp điều kiện tối ưu cấp một ở Chương 04, hãy đọc lại đoạn này: cùng điều kiện $$\nabla f(x)=0$$ chính là thứ vi phân ẩn tuyến tính hóa.

## Cập nhật hạng thấp: LoRA như đại số tuyến tính

Fine-tune mô hình ngôn ngữ lớn bằng cách đổi mọi phần tử của ma trận trọng số $$W_0\in\mathbb{R}^{d\times k}$$ tốn bộ nhớ và tốn chỗ lưu bản sao theo tác vụ. Hu, Shen, Wallis, Allen-Zhu, Li, Wang, Wang và Chen (*LoRA*, [ICLR 2022](https://openreview.net/forum?id=nZeVKeeFYf9); [arXiv:2106.09685](https://arxiv.org/abs/2106.09685)) đóng băng $$W_0$$ và học hiệu chỉnh hạng $$r$$

$$
W = W_0 + BA, \qquad B\in\mathbb{R}^{d\times r},\; A\in\mathbb{R}^{r\times k},\; r\ll \min(d,k).
$$

Số tham số huấn luyện giảm từ $$dk$$ xuống $$r(d+k)$$. Trên mô hình cỡ GPT-3, bài báo báo cáo giảm tham số huấn luyện hàng bậc độ lớn mà không thêm độ trễ suy luận, vì có thể gộp $$B$$ và $$A$$ vào $$W$$ sau khi train. Nội dung đại số tuyến tính Chương 00 chính là thứ giúp kiểm được khẳng định: hạng, chi phí nhân ma trận, và ý tưởng rằng một cập nhật có cấu trúc có thể sống trong không gian con mỏng. Các thư viện adapter trên Hugging Face (PEFT) là phân tích này cộng kỹ thuật hệ thống.

## Score matching và mô hình khuếch tán

Mô hình sinh ảnh bằng cách khử nhiễu Gauss dần dần, về bản chất, là một bài xác suất. Gọi $$p_t$$ là họ mật độ đã làm mượt và $$s_\theta(x,t)$$ xấp xỉ *score* $$\nabla_x \log p_t(x)$$. Huấn luyện tối thiểu hóa hồi quy có trọng số trên score; lấy mẫu là tích phân phương trình vi phân thường (hoặc ngẫu nhiên) dẫn bởi $$s_\theta$$. Karras, Aittala, Aila và Laine (*Elucidating the Design Space of Diffusion-Based Generative Models*, [NeurIPS 2022](https://proceedings.neurips.cc/paper/2022/hash/a98846e9d9cc01cfb87eb694d946ce6b-Abstract-Conference.html); [arXiv:2206.00364](https://arxiv.org/abs/2206.00364); mã [NVlabs/edm](https://github.com/NVlabs/edm)) viết lại nhiều công thức khuếch tán phổ biến thành một không gian thiết kế: tiền điều kiện mạng, lịch nhiễu, và bộ lấy mẫu. FID CIFAR-10 có điều kiện lớp $$1.79$$ với 35 lần đánh giá mạng trở thành triển khai tham chiếu.

Những gì bạn cần từ Chương 00 vừa phải và chính xác: gradient của log-mật độ, họ Gauss, và việc ODE/SDE là đối tượng giải tích. Không cần toàn bộ giải tích ngẫu nhiên để thấy vì sao “dự đoán nhiễu rồi bước Euler” là một phương pháp số trên trường score.

## Kiểm tra số nhỏ (kích thước LoRA)

Đoạn sau không huấn luyện Transformer; chỉ kiểm tra rằng phân tích hạng thấp có đúng số tham số mà bài LoRA quảng cáo. Chạy sau khi ôn nhân ma trận ở 00-02.

```python
import numpy as np

d, k, r = 4096, 4096, 8
full = d * k
lora = r * (d + k)
print("full params:", full)
print("LoRA params:", lora)
print("ratio:", full / lora)

W0 = np.random.randn(d, k)
A = np.random.randn(r, k)
B = np.random.randn(d, r)
W = W0 + B @ A
print("W shape:", W.shape, "rank bound:", r)
```

## Điều cần mang đi

Khi một bài báo nói “chúng tôi vi phân qua ánh xạ KKT,” “chúng tôi chèn adapter hạng $$r$$,” hoặc “chúng tôi khớp score của nhiễu Gauss,” đó là ngôn ngữ Chương 00. Các chương sau thêm tính lồi, dạng chuẩn và thuật toán; chúng không thay thế đạo hàm, phân tích nhân tử hay mật độ.

## Nguồn

1. M. Blondel và V. Roulet, *The Elements of Differentiable Programming*, arXiv:2403.14606, 2024 (sửa 2025). [https://arxiv.org/abs/2403.14606](https://arxiv.org/abs/2403.14606)
2. M. Blondel và cộng sự, “Efficient and Modular Implicit Differentiation,” NeurIPS 2022. [bài báo](https://proceedings.neurips.cc/paper_files/paper/2022/hash/228b9279ecf9bbafe582406850c57115-Abstract-Conference.html) · [JAXopt](https://github.com/google/jaxopt)
3. E. J. Hu và cộng sự, “LoRA: Low-Rank Adaptation of Large Language Models,” ICLR 2022. [OpenReview](https://openreview.net/forum?id=nZeVKeeFYf9) · [arXiv:2106.09685](https://arxiv.org/abs/2106.09685)
4. T. Karras, M. Aittala, T. Aila và S. Laine, “Elucidating the Design Space of Diffusion-Based Generative Models,” NeurIPS 2022. [tóm tắt](https://proceedings.neurips.cc/paper/2022/hash/a98846e9d9cc01cfb87eb694d946ce6b-Abstract-Conference.html) · [arXiv:2206.00364](https://arxiv.org/abs/2206.00364)
