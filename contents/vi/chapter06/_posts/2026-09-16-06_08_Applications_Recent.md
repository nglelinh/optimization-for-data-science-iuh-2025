---
layout: post
title: 06-08 Ứng dụng và phát triển gần đây
chapter: '06'
order: 18
owner: Nguyen Le Linh
categories:
- chapter06
lang: vi
lesson_type: optional
---

Chương 06 xây gradient descent với gradient Lipschitz, quy tắc bước, và tốc độ nhanh hơn khi lồi mạnh. Lý thuyết đó vẫn là bức tranh đúng đầu tiên — và *không* phải toàn bộ cách người ta huấn luyện mạng năm 2022–2026. Bài này thêm ba phát triển thực nghiệm và thuật toán bạn cần trích dẫn được: chế độ mép ổn định của GD full-batch, phương pháp momentum dấu tìm được bằng tìm kiếm chương trình (Lion), và trung bình không lịch bước bỏ nhu cầu biết $$T$$ trước. Các phương pháp thích nghi (AdamW) nằm ở [Chương 26]({{ site.baseurl }}/contents/vi/chapter26/); ta chỉ nhắc khi bài báo dùng chúng làm baseline.

## Mép ổn định: khi chặn bước trong sách giáo khoa thất bại

Nếu $$\nabla f$$ Lipschitz với hằng $$L$$, bổ đề hạ nói rằng bước *cố định* $$t<2/L$$ làm $$f$$ giảm đơn điệu. Cohen, Kaur, Li, Kolter và Talwalkar (*Gradient Descent on Neural Networks Typically Occurs at the Edge of Stability*, [ICLR 2021](https://openreview.net/forum?id=jh-rTtvkGeM); [arXiv:2103.00065](https://arxiv.org/abs/2103.00065)) đo GD full-batch trên mạng hiện đại và thấy một chế độ khác: trị riêng Hessian lớn nhất $$\lambda_{\max}$$ *tăng* cho đến khi lơ lửng vừa trên $$2/t$$, và mất mát huấn luyện dao động trên cửa sổ ngắn nhưng vẫn xu hướng giảm. Điều đó không tương thích với một $$L$$ toàn cục mà bạn coi là cố định.

Arora, Li và Panigrahi (*Understanding Gradient Descent on the Edge of Stability in Deep Learning*, [ICML 2022](https://proceedings.mlr.press/v162/arora22a.html)) đưa một cơ chế: sau khi vào pha mép ổn định, các vòng lặp có thể theo một dòng tất định trên đa tạp mất mát (gần) cực tiểu mà *giảm* độ sắc $$\lambda_{\max}(\nabla^2 L)$$. Họ chứng minh hiện tượng cho GD chuẩn hóa và cho GD trên $$\sqrt{L-L^\star}$$ dưới giả thiết chính quy.

Với chương này, hãy giữ cả hai phát biểu. Bổ đề hạ không sai; giả thuyết “$$L$$ không đổi dọc đường” mới sai. Khi bài tập giả sử chặn trên toàn phương (06-03-01), bạn đang ở chế độ trước mép. Khi bài deep learning nói lần chạy “ở mép ổn định,” họ muốn nói $$\lambda_{\max}\approx 2/t$$ và bạn không nên kỳ vọng giảm đơn điệu.

## Lion: momentum với dấu

Chen, Liang, Huang, Real, Wang, Pham, Dong, Luong, Hsieh, Lu, Le và đồng nghiệp (*Symbolic Discovery of Optimization Algorithms*, [NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/9a39b4925e35cf447ccba8757137d84f-Abstract-Conference.html); [arXiv:2302.06675](https://arxiv.org/abs/2302.06675); mã trong [google/automl/lion](https://github.com/google/automl/tree/master/lion)) tìm trong không gian chương trình tối ưu và ra **Lion** (EvoLved Sign Momentum). Cập nhật giữ một bộ đệm momentum $$m$$ và bước theo *dấu* của hỗn hợp $$m$$ và gradient hiện tại:

$$
\begin{align}
u_t &= \beta_1 m_{t-1} + (1-\beta_1) g_t,\\
\theta_t &= \theta_{t-1} - \eta\,\mathrm{sign}(u_t),\\
m_t &= \beta_2 m_{t-1} + (1-\beta_2) g_t.
\end{align}
$$

Không có tiền điều kiện moment hai, nên bộ nhớ gần SGD-có-momentum hơn Adam. Tác giả báo cáo tăng ImageNet trên ViT, tiết kiệm tính toán trên JFT và khuếch tán, và các lần chạy mô hình ngôn ngữ cạnh tranh; họ cũng ghi các thiết lập mà lợi ích nhỏ. Thực hành mặc định là $$\eta$$ *nhỏ hơn* AdamW, vì $$\|\mathrm{sign}(u)\|_{\infty}=1$$ làm mỗi bước tọa độ đủ lớn.

Chương 06 đã giới thiệu momentum (06-06). Lion là ý đó với dấu theo tọa độ — một biến điệu không-Euclid bạn có thể xem như hạ dốc nhất chuẩn hóa trong hình học $$\ell_\infty$$. Nó *không* thay các chứng minh hội tụ ở 06-03; các chứng minh đó giả sử bước Euclid trơn.

## SGD và AdamW không lịch bước

Lý thuyết cổ điển thường muốn bước giảm phụ thuộc chân trời $$T$$ (hoặc ngân sách bạn công bố trước). Người thực hành thì chọn lịch cosine cũng phụ thuộc $$T$$. Defazio, Yang, Khaled, Mishchenko, Mehta và Cutkosky (*The Road Less Scheduled*, [NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/136b9a13861308c8948cd308ccd02658-Abstract-Conference.html); [arXiv:2405.15682](https://arxiv.org/abs/2405.15682); [facebookresearch/schedule_free](https://github.com/facebookresearch/schedule_free)) nội suy một dãy đã trung bình với dãy gốc kiểu momentum để *không* cần lịch giảm. Schedule-Free AdamW là thuật toán cốt lõi trong mục thắng của họ ở đường đua tự chỉnh 2024 MLCommons AlgoPerf. Thực nghiệm, phương pháp bám biên Pareto “mất mát theo thời gian huấn luyện” mà lẽ ra bạn chỉ có nếu phóng nhiều lần chạy cosine độ dài khác nhau.

Liên kết với chương này là trung bình Polyak–Ruppert và momentum, không phải bổ đề hạ mới. Nếu hiểu vì sao trung bình có thể thay bước giảm (cùng trực giác với SGD nhiễu ở 06-05), bạn đọc phép nội suy của bài báo như một lược đồ trung bình *thực dụng* cuối cùng khớp các lịch đã chỉnh.

## Việc nên làm trong môn này versus về sau

Với bài tập và giữa kỳ, dùng tốc độ Lipschitz và lồi mạnh như viết ở 06-03. Với nhật ký huấn luyện mạng sâu, vẽ mất mát *và*, nếu chịu được chi phí, ước lượng power-iteration của $$\lambda_{\max}$$; hãy kỳ vọng dao động mép ổn định dưới GD full-batch. Với lần chạy ngẫu nhiên lớn, bắt đầu từ AdamW hoặc Schedule-Free AdamW (Chương 26) và coi Lion là baseline momentum thay thế, không phải chứng minh mặc định mới.

## Nguồn

1. J. M. Cohen, S. Kaur, Y. Li, J. Z. Kolter và A. Talwalkar, “Gradient Descent on Neural Networks Typically Occurs at the Edge of Stability,” ICLR 2021. [OpenReview](https://openreview.net/forum?id=jh-rTtvkGeM) · [arXiv:2103.00065](https://arxiv.org/abs/2103.00065)
2. S. Arora, Z. Li và A. Panigrahi, “Understanding Gradient Descent on the Edge of Stability in Deep Learning,” ICML 2022. [PMLR](https://proceedings.mlr.press/v162/arora22a.html)
3. X. Chen và cộng sự, “Symbolic Discovery of Optimization Algorithms,” NeurIPS 2023. [tóm tắt](https://proceedings.neurips.cc/paper_files/paper/2023/hash/9a39b4925e35cf447ccba8757137d84f-Abstract-Conference.html) · [arXiv:2302.06675](https://arxiv.org/abs/2302.06675)
4. A. Defazio, X. Yang, A. Khaled, K. Mishchenko, H. Mehta và A. Cutkosky, “The Road Less Scheduled,” NeurIPS 2024. [tóm tắt](https://proceedings.neurips.cc/paper_files/paper/2024/hash/136b9a13861308c8948cd308ccd02658-Abstract-Conference.html) · [arXiv:2405.15682](https://arxiv.org/abs/2405.15682)
