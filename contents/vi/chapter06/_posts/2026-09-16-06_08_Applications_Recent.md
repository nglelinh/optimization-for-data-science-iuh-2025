---
layout: post
title: 06-08 Ứng dụng và phát triển gần đây
chapter: '06'
order: 20
owner: Nguyen Le Linh
categories:
- chapter06
lang: vi
lesson_type: optional
---

Suốt Chương 06, bạn đã nắm vững định lý cổ điển: Gradient Descent chỉ ổn định khi kích thước bước $$t < 2/L$$, và nếu vượt quá ngưỡng đó thuật toán sẽ phân kỳ. Thế nhưng vào năm 2021, khi các nhà nghiên cứu đo trực tiếp độ cong Hessian trong quá trình huấn luyện mạng nơ-ron sâu thật, họ phát hiện một hiện tượng gây chấn động: **độ sắc nét $$\lambda_{\max}(\nabla^2 L)$$ tự động tăng vọt lên chạm đúng ngưỡng $$2/t$$ rồi dao động ổn định ngay trên "mép vực" đó trong suốt hàng nghìn vòng lặp mà không hề phân kỳ!**

Hiện tượng **Mép ổn định (Edge of Stability)** cùng với sự ra đời của các bộ tối ưu thế hệ mới như **Lion** (tìm ra bằng tiến hóa chương trình tự động của Google Brain, chỉ dùng dấu của momentum) và **Schedule-Free SGD/AdamW** (bỏ hoàn toàn lịch giảm tốc độ học thủ công) cho thấy lý thuyết Gradient Descent của Chương 06 vẫn đang tiến hóa sôi động từng năm!

## Kiến thức cần nhớ: Ba bước tiến hiện đại vượt ra ngoài khung GD cổ điển

Để kết nối lý thuyết Chương 06 với nghiên cứu tối ưu hóa giai đoạn 2021–2026, hãy nắm ba trụ cột:

- **Mép ổn định (Edge of Stability — Cohen et al.):** Trên mạng nơ-ron phi lồi, bước học cố định $$\eta$$ không khiến hàm mất mát phân kỳ khi $$\lambda_{\max}$$ vượt $$2/\eta$$; thay vào đó, độ cong tự điều chỉnh xoay quanh đúng ranh giới $$2/\eta$$ và hàm mất mát vẫn giảm dần theo xu hướng dài hạn dù dao động cục bộ.
- **Lion (EvoLved Sign Momentum):** Cập nhật tham số chỉ bằng **dấu** ($$\operatorname{sign}$$) của tổ hợp momentum: $$x_{t+1} = x_t - \eta \operatorname{sign}(\beta_1 m_{t-1} + (1-\beta_1) g_t)$$. Mọi tọa độ di chuyển cùng một biên độ $$\eta$$ (tương ứng chuẩn $$\ell_\infty$$ thay vì $$\ell_2$$!), giúp tiết kiệm một nửa bộ nhớ trạng thái so với AdamW!
- **Tối ưu hóa không cần lịch học (Schedule-Free Optimization):** Thay vì phải đoán trước tổng số bước $$T$$ để thiết kế lịch cosine decay, phương pháp Schedule-Free duy trì hai chuỗi lặp (một chuỗi cập nhật và một chuỗi trung bình nội suy) để tự động đạt tốc độ hội tụ tối ưu cho mọi thời điểm dừng!

### Giải thích: Tính tay sự khác biệt giữa bước GD chuẩn và bước Lion (Sign Momentum)

Giả sử tại một bước huấn luyện, hai tọa độ của vector gradient (sau khi trộn momentum) có độ lớn chênh lệch cực mạnh:
$$u = (0.01,\; -10.0)^T, \qquad \text{với tốc độ học } \eta = 0.1.$$

1. **Cập nhật của GD / Momentum chuẩn (theo chuẩn $$\ell_2$$):**
   $$\Delta x_{\text{GD}} = -0.1 \begin{pmatrix} 0.01 \\ -10.0 \end{pmatrix} = \begin{pmatrix} -0.001 \\ +1.000 \end{pmatrix}.$$
   Tọa độ thứ nhất nhích đi cực chậm ($$0.001$$), trong khi tọa độ thứ hai nhảy vọt gấp **1.000 lần** ($$1.0$$), dễ gây mất ổn định!
2. **Cập nhật của Lion (theo dấu $$\operatorname{sign}(u)$$, chuẩn $$\ell_\infty$$):**
   $$\operatorname{sign}(u) = \begin{pmatrix} +1 \\ -1 \end{pmatrix} \implies \Delta x_{\text{Lion}} = -0.1 \begin{pmatrix} +1 \\ -1 \end{pmatrix} = \begin{pmatrix} -0.1 \\ +0.1 \end{pmatrix}.$$
   Cả hai tọa độ đều bước đi đều đặn đúng biên độ $$\eta = 0.1$$ bất kể gradient lớn hay nhỏ! (Vì bước luôn có độ lớn cố định $$\eta$$, Lion thường dùng $$\eta$$ nhỏ hơn AdamW khoảng 3–10 lần và kết hợp weight decay lớn hơn để giữ ổn định!)

---

Chương 06 trình bày nền tảng cổ điển của gradient descent gồm tính liên tục Lipschitz của gradient, các quy tắc chọn kích thước bước và tốc độ hội tụ nhanh hơn dưới giả thiết lồi mạnh. Khung lý thuyết đó vẫn là điểm khởi đầu đúng đắn, nhưng chưa phản ánh đầy đủ thực tế huấn luyện mạng nơ-ron sâu giai đoạn 2022–2026. Bài đọc này bổ sung ba phát triển thực nghiệm và thuật toán tiêu biểu: chế độ mép ổn định (edge of stability) của gradient descent toàn tập (full-batch GD), phương pháp momentum theo dấu tìm được qua tìm kiếm chương trình (**Lion**), và phương pháp trung bình không lịch bước (schedule-free averaging) không cần biết trước tổng số bước $$T$$. Các thuật toán thích ứng như AdamW được trình bày ở [Chương 26]({{ site.baseurl }}/contents/vi/chapter26/) và chỉ được nhắc tới ở đây khi đóng vai trò mốc so sánh trong các bài báo.

## Mép ổn định: khi cận bước cổ điển không còn mô tả đủ thực tế

Nếu $$\nabla f$$ liên tục Lipschitz toàn cục với hằng số $$L$$, bổ đề giảm khẳng định rằng kích thước bước *cố định* $$t < 2/L$$ đảm bảo hàm mục tiêu $$f$$ giảm đơn điệu. Tuy nhiên, Cohen, Kaur, Li, Kolter và Talwalkar (*Gradient Descent on Neural Networks Typically Occurs at the Edge of Stability*, [ICLR 2021](https://openreview.net/forum?id=jh-rTtvkGeM); [arXiv:2103.00065](https://arxiv.org/abs/2103.00065)) đã đo đạc full-batch GD trên các mạng nơ-ron hiện đại và ghi nhận một hành vi khác: trị riêng lớn nhất của Hessian $$\lambda_{\max}$$ tăng dần cho đến khi dao động ngay trên ngưỡng $$2/t$$; giá trị mất mát huấn luyện dao động ngắn hạn nhưng vẫn có xu hướng giảm về dài hạn. Hiện tượng này không phù hợp với giả định một hằng số $$L$$ cố định trên toàn miền.

Arora, Li và Panigrahi (*Understanding Gradient Descent on the Edge of Stability in Deep Learning*, [ICML 2022](https://proceedings.mlr.press/v162/arora22a.html)) đề xuất cơ chế giải thích: sau khi bước vào pha mép ổn định, quỹ đạo lặp bám theo một dòng tất định dọc theo đa tạp (gần) cực tiểu của hàm mất mát, đồng thời làm *giảm* độ sắc (sharpness) $$\lambda_{\max}(\nabla^2 L)$$. Họ chứng minh hiện tượng này cho gradient descent chuẩn hóa và cho gradient descent trên hàm $$\sqrt{L - L^\star}$$ dưới các giả thiết chính quy.

Trong phạm vi chương này, cả hai góc nhìn đều cần được phân biệt rõ. Bổ đề giảm không sai; điều không còn đúng trên mạng sâu là giả thiết "$$L$$ không đổi dọc theo quỹ đạo". Khi làm các bài tập giả định cận trên bậc hai (06-03-01), ta đang xét chế độ trước mép ổn định. Khi các công trình học sâu mô tả quá trình huấn luyện đang ở "mép ổn định", điều đó có nghĩa là $$\lambda_{\max} \approx 2/t$$ và hàm mất mát không còn giảm đơn điệu qua từng bước.

## Lion: momentum theo dấu

Chen, Liang, Huang, Real, Wang, Pham, Dong, Luong, Hsieh, Lu, Le và cộng sự (*Symbolic Discovery of Optimization Algorithms*, [NeurIPS 2023](https://proceedings.neurips.cc/paper_files/paper/2023/hash/9a39b4925e35cf447ccba8757137d84f-Abstract-Conference.html); [arXiv:2302.06675](https://arxiv.org/abs/2302.06675); mã nguồn tại [google/automl/lion](https://github.com/google/automl/tree/master/lion)) đã thực hiện tìm kiếm trong không gian các chương trình tối ưu và phát hiện thuật toán **Lion** (EvoLved Sign Momentum). Thuật toán chỉ lưu một bộ đệm momentum $$m$$ và cập nhật tham số theo *dấu* của tổ hợp tuyến tính giữa $$m$$ và gradient hiện tại:

$$
\begin{align}
u_t &= \beta_1 m_{t-1} + (1-\beta_1) g_t,\\
\theta_t &= \theta_{t-1} - \eta\,\mathrm{sign}(u_t),\\
m_t &= \beta_2 m_{t-1} + (1-\beta_2) g_t.
\end{align}
$$

Do không sử dụng ước lượng mô-men bậc hai, mức tiêu thụ bộ nhớ của Lion gần với SGD có momentum hơn là Adam. Nhóm tác giả báo cáo cải thiện trên ImageNet với ViT, tiết kiệm chi phí tính toán trên tập JFT và mô hình khuếch tán, cùng kết quả cạnh tranh trên mô hình ngôn ngữ (đồng thời cũng ghi nhận các thiết lập mà mức cải thiện nhỏ). Về mặt thực hành, tốc độ học $$\eta$$ của Lion thường được chọn *nhỏ hơn* so với AdamW, vì $$\|\mathrm{sign}(u)\|_{\infty}=1$$ khiến biên độ cập nhật trên mọi tọa độ đều bằng nhau.

Chương 06 giới thiệu phương pháp momentum ở mục 06-06. Lion là biến thể lấy dấu theo từng tọa độ của ý tưởng đó — một phương pháp phi Euclid có thể xem như hạ dốc nhất chuẩn hóa trong hình học $$\ell_\infty$$. Lưu ý rằng Lion không thay thế các chứng minh hội tụ ở mục 06-03, vốn được xây dựng cho bước cập nhật Euclid trơn.

## SGD và AdamW không cần lịch giảm bước

Lý thuyết tối ưu cổ điển thường yêu cầu lịch giảm tốc độ học phụ thuộc vào tổng số bước $$T$$ (ngân sách lặp định trước), và trong thực tế lịch cosine cũng cần biết trước $$T$$. Defazio, Yang, Khaled, Mishchenko, Mehta và Cutkosky (*The Road Less Scheduled*, [NeurIPS 2024](https://proceedings.neurips.cc/paper_files/paper/2024/hash/136b9a13861308c8948cd308ccd02658-Abstract-Conference.html); [arXiv:2405.15682](https://arxiv.org/abs/2405.15682); mã nguồn tại [facebookresearch/schedule_free](https://github.com/facebookresearch/schedule_free)) đề xuất nội suy giữa dãy tham số đã lấy trung bình và dãy lặp gốc kiểu momentum để loại bỏ hoàn toàn lịch giảm tốc độ học. **Schedule-Free AdamW** là thuật toán cốt lõi trong giải pháp giành vị trí dẫn đầu của nhóm ở hạng mục tự điều chỉnh (self-tuning) tại cuộc thi 2024 MLCommons AlgoPerf. Về mặt thực nghiệm, phương pháp này bám sát đường biên Pareto giữa mất mát và thời gian huấn luyện mà thông thường chỉ đạt được khi phải chạy nhiều lịch cosine với các độ dài $$T$$ khác nhau.

Điểm kết nối với chương này nằm ở cơ chế trung bình Polyak–Ruppert và momentum, chứ không phải một bổ đề giảm mới. Nếu đã hiểu vì sao lấy trung bình có thể thay thế việc giảm kích thước bước (cùng trực giác với SGD có nhiễu ở mục 06-05), ta có thể xem phép nội suy của bài báo là một lược đồ trung bình thực dụng đạt hiệu năng ngang bằng các lịch giảm tốc độ học đã tinh chỉnh.

## Định hướng Áp dụng: Học phần và Thực hành

Đối với bài tập và kỳ thi trong môn học, hãy áp dụng các kết quả tốc độ hội tụ theo hằng số Lipschitz và tính lồi mạnh ở mục 06-03. Khi theo dõi quá trình huấn luyện mạng sâu, bên cạnh đường cong mất mát, nếu chi phí tính toán cho phép, hãy ước lượng $$\lambda_{\max}$$ bằng phương pháp lặp lũy thừa (power iteration) và lưu ý khả năng xuất hiện dao động mép ổn định dưới full-batch GD. Với các bài toán huấn luyện ngẫu nhiên quy mô lớn, nên bắt đầu từ AdamW hoặc Schedule-Free AdamW (Chương 26), và xem Lion như một lựa chọn momentum thay thế đáng cân nhắc.

## Nguồn

1. J. M. Cohen, S. Kaur, Y. Li, J. Z. Kolter và A. Talwalkar, “Gradient Descent on Neural Networks Typically Occurs at the Edge of Stability,” ICLR 2021. [OpenReview](https://openreview.net/forum?id=jh-rTtvkGeM) · [arXiv:2103.00065](https://arxiv.org/abs/2103.00065)
2. S. Arora, Z. Li và A. Panigrahi, “Understanding Gradient Descent on the Edge of Stability in Deep Learning,” ICML 2022. [PMLR](https://proceedings.mlr.press/v162/arora22a.html)
3. X. Chen và cộng sự, “Symbolic Discovery of Optimization Algorithms,” NeurIPS 2023. [tóm tắt](https://proceedings.neurips.cc/paper_files/paper/2023/hash/9a39b4925e35cf447ccba8757137d84f-Abstract-Conference.html) · [arXiv:2302.06675](https://arxiv.org/abs/2302.06675)
4. A. Defazio, X. Yang, A. Khaled, K. Mishchenko, H. Mehta và A. Cutkosky, “The Road Less Scheduled,” NeurIPS 2024. [tóm tắt](https://proceedings.neurips.cc/paper_files/paper/2024/hash/136b9a13861308c8948cd308ccd02658-Abstract-Conference.html) · [arXiv:2405.15682](https://arxiv.org/abs/2405.15682)
