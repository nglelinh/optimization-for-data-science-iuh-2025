---
layout: post
title: 26-06 Bộ tối ưu thích nghi hiện đại (khảo sát)
chapter: '26'
order: 7
owner: Nguyen Le Linh
categories:
- chapter26
lang: vi
lesson_type: optional
---


Các bài 26-01 đến 26-05 là ngăn xếp được kiểm tra: SGD, momentum, AdaGrad → Adam, **AdamW**, và một con trỏ giảm phương sai. Khảo sát tùy chọn này là vườn thú bộ tối ưu 2023–2026 ở độ sâu *một đoạn mỗi thuật toán*. Đừng coi đây là bài AdamW thứ hai; [26-04]({% multilang_post_url contents/chapter26/2026-09-15-26_04_adamw_and_practice %}) đã sở hữu weight decay tách. Câu hỏi ở đây: *người ta thực sự huấn luyện mô hình lớn bằng gì sau khi AdamW thành mặc định?*

## AdamW vẫn là baseline

Loshchilov và Hutter, ICLR 2019, [arXiv:1711.05101](https://arxiv.org/abs/1711.05101), vẫn là bộ tối ưu được nêu trong công thức kiểu Llama / GPT: $$\eta$$ cỡ $$10^{-4}$$, $$\beta=(0.9,0.95)$$ hoặc $$(0.9,0.999)$$, $$\lambda\approx 0.1$$ tách, warmup rồi cosine. Mọi phương pháp dưới đây được đo *so với* công thức đó. Nếu chỉ nhớ một thuật toán từ Chương 26, nhớ AdamW.

## SAM: tối ưu một max cục bộ, không phải một điểm

Sharpness-Aware Minimization (Foret, Kleiner, Mobahi, Neyshabur, ICLR 2021, [OpenReview](https://openreview.net/forum?id=6Tm1mposlrM)) thay $$F(w)$$ bằng trường hợp xấu nhất trên *lân cận*

$$
\min_w\ \max_{\|\varepsilon\|_2\le\rho} F(w+\varepsilon)\ \approx\ F\bigl(w+\rho\,\nabla F(w)/\|\nabla F(w)\|_2\bigr).
$$

Một gradient thêm (leo tới $$w+\varepsilon$$, rồi xuống tại điểm đó) thiên SGD về cực tiểu **phẳng**. Bartlett, Long và Bousquet, *The Dynamics of Sharpness-Aware Minimization*, *JMLR* 24(43), 2023, [jmlr.org/papers/v24/23-043.html](https://www.jmlr.org/papers/v24/23-043.html), cho thấy bước thêm, gần một cực tiểu trơn, là một cú nảy qua hướng Hessian sắc nhất cộng một trôi *giảm* $$\|\nabla^2 F\|$$. Shin, Lee, Andriushchenko và Lee ([arXiv:2311.17539](https://arxiv.org/abs/2311.17539), 2023/2024) thấy lợi tổng quát hóa của SAM *tăng* theo quá tham số — một cầu tới Chương 28. SAM dùng trong thị giác và một số fine-tune; tiền huấn luyện LLM đầy đủ thường bỏ qua chi phí gradient nhân đôi.

## Sophia: Hessian đường chéo rẻ

Liu, Li, et al., *Sophia: A Scalable Stochastic Second-order Optimizer for Language Model Pre-training*, ICLR 2024, [OpenReview](https://openreview.net/forum?id=3xHDeA8Noi), giữ moment kiểu Adam nhưng thay bộ tích lũy moment hai bằng ước lượng Hessian đường chéo *bị cắt* (Hutchinson hoặc Gauss–Newton rẻ). Khẳng định là ít bước hơn AdamW trên tiền huấn luyện mô hình ngôn ngữ với chi phí mỗi bước khiêm tốn. Coi Sophia là “AdamW với mẫu số biết độ cong,” không phải Newton đầy đủ.

## Muon: trực giao hóa cập nhật lớp ẩn

Jordan, Jin, Boza, Jiacheng, Cesista, Newhouse và Bernstein, *Muon: An optimizer for hidden layers in neural networks*, 2024, [kellerjordan.github.io/posts/muon](https://kellerjordan.github.io/posts/muon/), lấy momentum Nesterov trên mỗi tham số *ma trận* và thay cập nhật bằng ma trận trực giao gần nhất (lặp Newton–Schulz — không SVD trong vòng trong). Embedding, đầu ra, và vector ở lại AdamW. NanoGPT speedrunning (cuối 2024) khiến Muon thành mặc định trong cộng đồng đó. Jingyuan Liu et al., *Muon is Scalable for LLM Training*, [arXiv:2502.16982](https://arxiv.org/abs/2502.16982), 2025, thêm weight decay và một tỷ lệ theo tham số, huấn luyện MoE 3B/16B (Moonlight) trên 5.7T token, và báo khoảng $$2\times$$ hiệu quả tính so với AdamW trên đồ thị định luật tỷ lệ. Shah et al., *Practical Efficiency of Muon for Pretraining*, [arXiv:2505.02222](https://arxiv.org/abs/2505.02222), 2025, đẩy biên Pareto đánh đổi tính–thời gian tới 4B tham số. Đây là đối thủ *biết ma trận* nghiêm túc đầu tiên của AdamW đường chéo; **không** kiểm tra kỳ này.

## Schedule-free AdamW (con trỏ)

Defazio và cộng sự (2024) đề xuất AdamW *không lịch* thay $$\eta_t$$ giảm bằng trung bình Polyak–Ruppert ẩn. Hữu ích như bài seminar; không phải bộ núm bài tập thứ hai.

| Phương pháp | Việc / bộ nhớ thêm | Sân nhà điển hình (2026) | Kiểm tra? |
|-------------|--------------------|--------------------------|-----------|
| AdamW | hai EMA | mặc định LLM / thị giác | có (26-04) |
| SAM | gradient $$2\times$$ | thị giác cực tiểu phẳng, một số fine-tune | không |
| Sophia | Hessian đường chéo rẻ | thí nghiệm tiền huấn luyện LM | không |
| Muon | Newton–Schulz trên ma trận ẩn | NanoGPT, một số tiền huấn luyện LLM | không |

**Bài tập (khảo sát, không phải cuộc đua).** Đọc đoạn blog Muon “dùng AdamW trên embedding và đầu ra” và viết bốn câu: (i) vì sao trọng số ẩn 2-D muốn cập nhật trực giao, (ii) vì sao bảng embedding thì không, (iii) điều này khác $$1/\sqrt{\hat v}$$ *từng tọa độ* của AdamW thế nào, và (iv) vì sao max trong của SAM là phát biểu *phong cảnh* (Ch.28) chứ không phải tiền điều kiện. Không cần chạy huấn luyện.

## Nguồn

- I. Loshchilov and F. Hutter, ICLR 2019 — AdamW.
- P. Foret, A. Kleiner, H. Mobahi, B. Neyshabur, ICLR 2021 — SAM.
- P. L. Bartlett et al., *JMLR* 24(43), 2023 — động lực học SAM.
- H. Liu et al., ICLR 2024 — Sophia.
- K. Jordan et al., 2024 — Muon.
- Jingyuan Liu et al., [arXiv:2502.16982](https://arxiv.org/abs/2502.16982), 2025 — Muon ở quy mô LLM.
- I. Shah et al., [arXiv:2505.02222](https://arxiv.org/abs/2505.02222), 2025 — hiệu quả tiền huấn luyện Muon.
