---
layout: post
title: 26-06 Bộ tối ưu thích nghi hiện đại (seminar)
chapter: '26'
order: 7
owner: Nguyen Le Linh
categories:
- chapter26
lang: vi
lesson_type: optional
---


Các bài 26-01 đến 26-05 là ngăn xếp được kiểm tra: SGD, momentum kiểu Distill, AdaGrad → Adam, **AdamW**, và SVRG / SAGA. Seminar tùy chọn này là vườn thú bộ tối ưu 2021–2026 ở độ sâu *thuật toán* — một hệ thức mỗi phương pháp, không phải bài AdamW thứ hai. [26-04]({% multilang_post_url contents/chapter26/2026-09-15-26_04_adamw_and_practice %}) đã sở hữu weight decay tách. Câu chuyện tiền điều kiện Hessian của Sophia như họ hàng Newton nằm ở [14-10]({% multilang_post_url contents/chapter14/2026-09-16-14_10_modern_applications %}); ở đây ta chỉ cần *cập nhật*, để đặt SAM, Sophia và Muon lên cùng bảng với AdamW. Không phương pháp nào trong ba cái được kiểm tra kỳ này.

Câu hỏi: *người ta thực sự huấn luyện mô hình lớn bằng gì sau khi AdamW thành mặc định, và mỗi phương pháp mua thêm hình học nào?*

## AdamW vẫn là baseline

Loshchilov và Hutter, ICLR 2019, [arXiv:1711.05101](https://arxiv.org/abs/1711.05101), vẫn là bộ tối ưu được nêu trong công thức kiểu Llama / GPT: $$\eta$$ cỡ $$10^{-4}$$, $$\beta=(0.9,0.95)$$ hoặc $$(0.9,0.999)$$, $$\lambda\approx 0.1$$ tách, warmup rồi cosine. Mọi phương pháp dưới đây được đo *so với* công thức đó. Nếu chỉ nhớ một thuật toán từ Chương 26, nhớ AdamW.

## SAM: một max cục bộ, rồi một bước xuống

Sharpness-Aware Minimization (Foret, Kleiner, Mobahi, Neyshabur, ICLR 2021, [OpenReview](https://openreview.net/forum?id=6Tm1mposlrM)) thay rủi ro từng điểm $$F(w)$$ bằng trường hợp xấu nhất trên *lân cận*

$$
\min_w\ \max_{\|\varepsilon\|_2\le\rho} F(w+\varepsilon)
\approx F\bigl(w+\rho\,\nabla F(w)/\|\nabla F(w)\|_2\bigr).
$$

Thuật toán là hai gradient mỗi bước, không phải tiền điều kiện mới.

1. **Leo (nhiễu).** $$g\leftarrow\nabla F(w)$$, rồi $$\varepsilon\leftarrow\rho\,g/\|g\|_2$$ (hoặc họ hàng chuẩn đối ngẫu).
2. **Xuống (gradient SAM).** Tính $$g_{\mathrm{SAM}}\leftarrow\nabla F(w+\varepsilon)$$ và bước $$w\leftarrow w-\eta\,g_{\mathrm{SAM}}$$ (hoặc đưa $$g_{\mathrm{SAM}}$$ cho AdamW / SGD+momentum).

Bước leo thêm thiên vòng lặp về cực tiểu **phẳng**: một quả cầu nhỏ quanh $$w$$ vẫn có loss nhỏ. Bartlett, Long và Bousquet, *The Dynamics of Sharpness-Aware Minimization*, *JMLR* 24(43), 2023, cho thấy gần một cực tiểu trơn, bước thêm là một cú nảy qua hướng Hessian sắc nhất cộng một trôi *giảm* $$\|\nabla^2 F\|$$. Shin, Lee, Andriushchenko và Lee ([arXiv:2311.17539](https://arxiv.org/abs/2311.17539)) thấy lợi tổng quát hóa của SAM *tăng* theo quá tham số — một cầu tới Chương 28 và câu chuyện PL ở [28-05]({% multilang_post_url contents/chapter28/2026-09-18-28_05_pl_condition %}). SAM dùng trong thị giác và một số fine-tune; tiền huấn luyện LLM đầy đủ thường bỏ qua chi phí gradient nhân đôi. Các biến thể bán kính thích nghi (ASAM, GSAM) đổi quả cầu, không đổi khuôn hai bước.

## Sophia: AdamW với Hessian đường chéo bị cắt

Liu, Li, Hall, Liang và Ma, *Sophia*, ICLR 2024, [OpenReview](https://openreview.net/forum?id=3xHDeA8Noi), giữ moment một kiểu Adam nhưng thay bộ tích lũy moment hai bằng ước lượng Hessian đường chéo *bị cắt*. Viết $$m$$ cho EMA của gradient và $$\hat h$$ cho EMA của ước lượng độ cong đường chéo,

$$
w\leftarrow w-\eta\cdot\operatorname{clip}\bigl(m/(\hat h+\varepsilon),\,\tau\bigr),
$$

với $$\hat h$$ chỉ được làm mới mỗi vài bước (tích Hessian–vector Hutchinson, hoặc ước lượng Gauss–Newton–Bartlett rút một nhãn từ mô hình và bình phương gradient đó). Phép cắt là một vùng tin cậy: một đường chéo cũ hoặc không xác định không được làm nổ bước. Coi Sophia là “AdamW có mẫu số biết độ cong,” không phải Newton đầy đủ — thảo luận bất biến affine và phân tích Hessian thuộc 14-10. Khẳng định là ít bước hơn AdamW trên tiền huấn luyện mô hình ngôn ngữ với chi phí mỗi bước khiêm tốn.

## Muon: trực giao hóa cập nhật lớp ẩn

Jordan, Jin, Boza, Cesista, Newhouse và Bernstein, *Muon*, 2024, [kellerjordan.github.io/posts/muon](https://kellerjordan.github.io/posts/muon/), lấy momentum Nesterov trên mỗi tham số *ma trận* $$W\in\mathbb{R}^{m\times n}$$ và thay cập nhật bằng ma trận trực giao gần nhất, tính bằng vài vòng Newton–Schulz (không SVD trong vòng trong):

$$
\begin{align}
B &\leftarrow \beta B+\nabla_W F,\\
O &\leftarrow \operatorname{NewtonSchulz}(B)\approx\arg\min_{Q^\top Q=I}\|Q-B\|_F,\\
W &\leftarrow W-\eta\,O.
\end{align}
$$

Embedding, đầu ra, và vector ở lại AdamW — trọng số ẩn 2-D muốn một bước trực giao (một phép quay đặc trưng, chuẩn phổ gần hằng); bảng embedding token thì không. NanoGPT speedrunning (cuối 2024) khiến Muon thành mặc định trong cộng đồng đó. Jingyuan Liu et al., *Muon is Scalable for LLM Training*, [arXiv:2502.16982](https://arxiv.org/abs/2502.16982), 2025, thêm weight decay và một tỷ lệ theo tham số, huấn luyện MoE 3B/16B (Moonlight) trên 5.7T token, và báo khoảng $$2\times$$ hiệu quả tính so với AdamW trên đồ thị định luật tỷ lệ. Shah et al., [arXiv:2505.02222](https://arxiv.org/abs/2505.02222), 2025, đẩy biên Pareto đánh đổi tính–thời gian tới 4B tham số. Đây là đối thủ *biết ma trận* nghiêm túc đầu tiên của AdamW đường chéo.

Bản thân Newton–Schulz là một vòng lặp đa thức rẻ trên $$X^\top X$$ đẩy trị riêng singular về $$1$$. Bạn không cần hệ số cho giáo trình này; bạn cần khẩu hiệu: **Muon tiền điều kiện bằng thừa số cực, AdamW tiền điều kiện bằng RMS từng tọa độ**.

## Schedule-free AdamW (con trỏ)

Defazio và cộng sự (2024) đề xuất AdamW *không lịch* thay $$\eta_t$$ giảm bằng trung bình Polyak–Ruppert ẩn. Hữu ích như bài seminar; không phải bộ núm bài tập thứ hai. Ghi chú tùy chọn Chương 06 [06-08]({% multilang_post_url contents/chapter06/2026-09-16-06_08_Applications_Recent %}) đã đặt bài đó cạnh Lion và mép ổn định.

| Phương pháp | Việc / bộ nhớ thêm | Hình học thêm | Sân nhà điển hình (2026) | Kiểm tra? |
|-------------|--------------------|---------------|--------------------------|-----------|
| AdamW | hai EMA | RMS từng tọa độ | mặc định LLM / thị giác | có (26-04) |
| SAM | gradient $$2\times$$ | cực tiểu phẳng (max trong) | thị giác, một số fine-tune | không |
| Sophia | Hessian đường chéo rẻ + cắt | mẫu số biết độ cong | thí nghiệm tiền huấn luyện LM | không |
| Muon | Newton–Schulz trên ma trận ẩn | cập nhật cực / trực giao | NanoGPT, một số tiền huấn luyện LLM | không |

**Bài tập (khảo sát, không phải cuộc đua).** Đọc đoạn blog Muon “dùng AdamW trên embedding và đầu ra” và viết bốn câu: (i) vì sao trọng số ẩn 2-D muốn cập nhật trực giao, (ii) vì sao bảng embedding thì không, (iii) điều này khác $$1/\sqrt{\hat v}$$ *từng tọa độ* của AdamW thế nào, và (iv) vì sao max trong của SAM là phát biểu *phong cảnh* (Ch.28) chứ không phải tiền điều kiện. Không cần chạy huấn luyện.

**Câu hỏi.** Phương pháp nào trong ba cái vẫn còn nghĩa nếu bạn chỉ được *một* gradient mỗi bước — và nó gần đối tượng Chương 26 nào nhất (momentum, moment hai đường chéo, hay giảm phương sai)?

## Nguồn

- I. Loshchilov and F. Hutter, ICLR 2019 — AdamW.
- P. Foret, A. Kleiner, H. Mobahi, B. Neyshabur, ICLR 2021 — SAM.
- P. L. Bartlett et al., *JMLR* 24(43), 2023 — động lực học SAM.
- H. Liu et al., ICLR 2024 — Sophia (cập nhật ở đây; đọc Newton ở 14-10).
- K. Jordan et al., 2024 — Muon.
- Jingyuan Liu et al., [arXiv:2502.16982](https://arxiv.org/abs/2502.16982), 2025 — Muon ở quy mô LLM.
- I. Shah et al., [arXiv:2505.02222](https://arxiv.org/abs/2505.02222), 2025 — hiệu quả tiền huấn luyện Muon.
