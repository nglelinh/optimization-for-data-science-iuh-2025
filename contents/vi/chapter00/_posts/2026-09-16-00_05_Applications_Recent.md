---
layout: post
title: 00-05 Ứng dụng và phát triển gần đây
chapter: '00'
order: 18
owner: Nguyen Le Linh
categories:
- chapter00
lang: vi
lesson_type: optional
---

Nhiều sinh viên sau khi học xong đạo hàm dây chuyền, hạng ma trận và phân phối chuẩn thường tự hỏi: *"Những công thức thế kỷ 18–19 này thực sự làm gì bên trong các mô hình AI tạo sinh năm 2024–2026?"* Câu trả lời có thể khiến bạn bất ngờ: ba đột phá đình đám nhất gần đây — **vi phân tự động (autodiff)**, **tinh chỉnh hạng thấp LoRA** và **mô hình khuếch tán (diffusion models)** — đều là ứng dụng trực tiếp, tinh tế của đúng những kiến thức nền trong Chương 00.

Bài đọc mở rộng này bắc cây cầu từ các khái niệm đại học cơ bản sang những kiến trúc tối ưu hóa đang chạy trên các hệ thống AI hiện đại nhất.

## Bản đồ kiến thức nền: Công cụ Chương 00 trong hệ thống AI hiện đại

- **Quy tắc dây chuyền → Vi phân tự động chế độ ngược (Reverse-mode Autodiff):** Thay vì tính riêng từng đạo hàm riêng (tốn $$\mathcal{O}(n)$$ lượt chạy), lan truyền ngược tích lũy sản phẩm vector–Jacobian để lấy toàn bộ gradient $$\nabla_\theta L$$ chỉ trong **một** lượt đi ngược với chi phí tương đương lượt đi xuôi.
- **Hạng ma trận (Low-rank Factorization) → LoRA:** Thay vì cập nhật toàn bộ ma trận trọng số khổng lồ $$W \in \mathbb{R}^{d \times k}$$, ta đóng băng $$W_0$$ và chỉ tối ưu phần bù hạng thấp $$\Delta W = BA$$ với $$r \ll \min(d, k)$$, cắt giảm bộ nhớ và chi phí tối ưu hàng chục đến hàng trăm lần.
- **Gradient của log-mật độ → Score Matching & Mô hình khuếch tán:** Học trực tiếp trường vector score $$\nabla_x \log p_t(x)$$ để đảo ngược quá trình thêm nhiễu Gauss từng bước, biến nhiễu trắng thành ảnh hoặc âm thanh chân thực.

### Khung giải thích (nên đọc chậm): Tính tay một lượt Autodiff ngược và đếm tham số LoRA

Hãy kiểm chứng bằng hai phép tính tay gọn gàng:

1. **Autodiff chế độ ngược cho hàm mất mát $$L(w) = (wx - y)^2$$** tại $$x = 2,\ w = 3,\ y = 10$$:
   - *Lượt xuôi (Forward):* $$z = wx = 3 \cdot 2 = 6$$; sai số $$e = z - y = 6 - 10 = -4$$; mất mát $$L = e^2 = 16$$.
   - *Lượt ngược (Backward):*
     $$\frac{\partial L}{\partial e} = 2e = -8, \qquad \frac{\partial L}{\partial z} = \frac{\partial L}{\partial e}\cdot 1 = -8, \qquad \frac{\partial L}{\partial w} = \frac{\partial L}{\partial z}\cdot x = (-8)\cdot 2 = -16.$$
   Dấu âm $$-16$$ báo hiệu cần tăng $$w$$ để kéo $$z=6$$ tiến gần $$y=10$$.
2. **Tiết kiệm tham số của LoRA trên một lớp tuyến tính $$1024 \times 1024$$:**
   - Tinh chỉnh toàn phần $$W_0 \in \mathbb{R}^{1024 \times 1024}$$: cần tối ưu $$1024 \times 1024 = 1{,}048{,}576$$ tham số.
   - Tinh chỉnh LoRA với hạng $$r = 8$$ ($$B \in \mathbb{R}^{1024 \times 8},\ A \in \mathbb{R}^{8 \times 1024}$$): số tham số cần học chỉ là:
     $$1024 \times 8 + 8 \times 1024 = 16{,}384 \text{ tham số},$$
     tức chỉ bằng $$\frac{16{,}384}{1{,}048{,}576} = \frac{1}{64} \approx 1.56\%$$ — tiết kiệm tới **$$98.44\%$$** số biến tối ưu!

---

Giải tích, đại số tuyến tính và xác suất trong chương này không chỉ là phần “khởi động” rồi bỏ qua; đó là ngôn ngữ làm việc trực tiếp của các mô hình bạn sẽ huấn luyện ngay từ những tuần đầu tiên. Bài đọc này kết nối các công cụ đó với bốn hướng phát triển giai đoạn 2022–2025 mà sinh viên khoa học dữ liệu thường gặp trong bài báo khoa học, thư viện mã nguồn và thực tập. Phần lý thuyết ở các bài trước không thay đổi; mục tiêu ở đây là chỉ ra *vị trí* của gradient, phân tích hạng thấp và hàm score trong các hệ thống thực tế.

## Vi phân tự động và gradient ẩn

Lan truyền ngược thực chất là quy tắc dây chuyền áp dụng trên đồ thị tính toán. Các thư viện hiện đại triển khai *vi phân tự động* (automatic differentiation): bạn viết hàm Python $$f$$, thư viện tự động tính $$\nabla f$$ mà không cần viết tay ma trận Jacobian. Chuyên khảo năm 2024–2025 của Blondel và Roulet, *The Elements of Differentiable Programming* ([arXiv:2403.14606](https://arxiv.org/abs/2403.14606)), xem đây là một mô hình lập trình hoàn chỉnh chứ không chỉ là kỹ thuật tính toán: miễn là chương trình được cấu thành từ các phép toán cơ bản khả vi, việc tối ưu tham số bằng gradient vẫn được định nghĩa chặt chẽ, ngay cả khi có cấu trúc điều khiển.

Một ứng dụng tinh tế hơn của giải tích Chương 00 là **định lý hàm ẩn**. Khi bộ giải trả về nghiệm $$x^\star(\theta)$$ thỏa mãn điều kiện tối ưu $$F(x,\theta)=0$$ (chẳng hạn $$\nabla_x L(x,\theta)=0$$), ta **không** cần lan truyền ngược qua toàn bộ các vòng lặp bên trong. Lấy vi phân đồng nhất thức $$F(x^\star(\theta),\theta)=0$$ dẫn đến hệ phương trình tuyến tính

$$
\nabla_\theta x^\star = - \bigl(\nabla_x F\bigr)^{-1} \nabla_\theta F.
$$

Blondel, Berthet, Cuturi, Frostig, Hoyer, Llinares-López, Pedregosa và Vert triển khai cơ chế này thành *vi phân ẩn tự động* trong thư viện JAXopt ([NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/hash/228b9279ecf9bbafe582406850c57115-Abstract-Conference.html); [github.com/google/jaxopt](https://github.com/google/jaxopt)). Người dùng chỉ cần định nghĩa ánh xạ $$F$$ bằng Python; JAX tự động lấy vi phân của $$F$$ và giải hệ tuyến tính tương ứng. Các bài toán chọn siêu tham số cho hồi quy ridge, học siêu tham số (meta-learning) và các tầng tối ưu đều quy về đồng nhất thức này. Khi học đến điều kiện tối ưu bậc nhất ở Chương 04, hãy quay lại đọc đoạn này: chính điều kiện $$\nabla f(x)=0$$ là biểu thức được tuyến tính hóa trong vi phân ẩn.

## Cập nhật hạng thấp: LoRA dưới góc nhìn đại số tuyến tính

Tinh chỉnh (fine-tune) mô hình ngôn ngữ lớn bằng cách cập nhật toàn bộ phần tử của ma trận trọng số $$W_0\in\mathbb{R}^{d\times k}$$ tiêu tốn rất nhiều bộ nhớ và dung lượng lưu trữ cho từng tác vụ. Hu, Shen, Wallis, Allen-Zhu, Li, Wang, Wang và Chen (*LoRA*, [ICLR 2022](https://openreview.net/forum?id=nZeVKeeFYf9); [arXiv:2106.09685](https://arxiv.org/abs/2106.09685)) giữ cố định $$W_0$$ và chỉ học một phần hiệu chỉnh hạng $$r$$:

$$
W = W_0 + BA, \qquad B\in\mathbb{R}^{d\times r},\; A\in\mathbb{R}^{r\times k},\; r\ll \min(d,k).
$$

Số tham số cần huấn luyện giảm từ $$dk$$ xuống còn $$r(d+k)$$. Trên mô hình cỡ GPT-3, bài báo ghi nhận số tham số huấn luyện giảm đi nhiều bậc độ lớn mà không làm tăng độ trễ suy luận, vì tích $$BA$$ có thể gộp trực tiếp vào $$W_0$$ sau khi huấn luyện. Kiến thức đại số tuyến tính ở Chương 00 giúp kiểm chứng ngay khẳng định này: hạng ma trận, chi phí phép nhân ma trận và ý tưởng rằng phép cập nhật có cấu trúc có thể nằm gọn trong một không gian con số chiều nhỏ. Các thư viện adapter trên Hugging Face (PEFT) được xây dựng trên nền phân tích này kết hợp với kỹ thuật hệ thống.

## Score matching và mô hình khuếch tán

Các mô hình sinh ảnh bằng cách khử nhiễu Gauss từng bước về bản chất là một bài toán xác suất. Gọi $$p_t$$ là họ mật độ xác suất đã được làm mượt theo mức nhiễu và $$s_\theta(x,t)$$ là mạng xấp xỉ hàm *score* $$\nabla_x \log p_t(x)$$. Quá trình huấn luyện cực tiểu hóa sai số hồi quy có trọng số trên hàm score; quá trình sinh mẫu quy về giải phương trình vi phân thường (ODE) hoặc phương trình vi phân ngẫu nhiên (SDE) dẫn hướng bởi $$s_\theta$$. Karras, Aittala, Aila và Laine (*Elucidating the Design Space of Diffusion-Based Generative Models*, [NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/hash/a98846e9d9cc01cfb87eb694d946ce6b-Abstract-Conference.html); [arXiv:2206.00364](https://arxiv.org/abs/2206.00364); mã nguồn [NVlabs/edm](https://github.com/NVlabs/edm)) thống nhất nhiều biến thể khuếch tán phổ biến vào chung một không gian thiết kế gồm tiền điều kiện mạng, lịch nhiễu và bộ lấy mẫu, đạt chỉ số FID $$1.79$$ trên CIFAR-10 có điều kiện lớp chỉ với 35 lần đánh giá mạng và trở thành bản triển khai tham chiếu.

Những kiến thức Chương 00 cần dùng ở đây hoàn toàn cụ thể và vừa sức: gradient của log-mật độ, phân phối chuẩn Gauss và góc nhìn giải tích về ODE/SDE. Ta chưa cần đến toàn bộ lý thuyết giải tích ngẫu nhiên để hiểu vì sao quy trình “dự đoán nhiễu rồi cập nhật bước Euler” thực chất là một phương pháp số trên trường score.

## Kiểm tra số nhỏ (kích thước tham số LoRA)

Đoạn mã dưới đây không huấn luyện Transformer mà chỉ kiểm tra số lượng tham số của phân tích hạng thấp đúng như công thức LoRA nêu trên. Bạn có thể chạy thử sau khi ôn lại phép nhân ma trận ở bài 00-02.

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

## Điểm cốt lõi cần ghi nhớ

Khi một bài báo viết “vi phân qua ánh xạ KKT”, “chèn adapter hạng $$r$$” hay “khớp hàm score của nhiễu Gauss”, đó đều là ứng dụng trực tiếp của các khái niệm trong Chương 00. Các chương tiếp theo sẽ bổ sung tính lồi, dạng chuẩn và thuật toán tối ưu, nhưng tất cả đều đứng trên nền tảng đạo hàm, phân tích ma trận và mật độ xác suất.

## Nguồn

1. M. Blondel và V. Roulet, *The Elements of Differentiable Programming*, arXiv:2403.14606, 2024 (sửa 2025). [https://arxiv.org/abs/2403.14606](https://arxiv.org/abs/2403.14606)
2. M. Blondel và cộng sự, “Efficient and Modular Implicit Differentiation,” NeurIPS 2022. [bài báo](https://proceedings.neurips.cc/paper_files/paper/2022/hash/228b9279ecf9bbafe582406850c57115-Abstract-Conference.html) · [JAXopt](https://github.com/google/jaxopt)
3. E. J. Hu và cộng sự, “LoRA: Low-Rank Adaptation of Large Language Models,” ICLR 2022. [OpenReview](https://openreview.net/forum?id=nZeVKeeFYf9) · [arXiv:2106.09685](https://arxiv.org/abs/2106.09685)
4. T. Karras, M. Aittala, T. Aila và S. Laine, “Elucidating the Design Space of Diffusion-Based Generative Models,” NeurIPS 2022. [tóm tắt](https://proceedings.neurips.cc/paper_files/paper/2022/hash/a98846e9d9cc01cfb87eb694d946ce6b-Abstract-Conference.html) · [arXiv:2206.00364](https://arxiv.org/abs/2206.00364)
