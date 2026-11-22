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


Các bài từ 26-01 đến 26-05 bao quát bộ công cụ cốt lõi trong chương trình: SGD, momentum theo trực giác Distill, AdaGrad → Adam, **AdamW**, cùng SVRG và SAGA. Bài seminar tùy chọn này điểm qua các bộ tối ưu hiện đại giai đoạn 2021–2026 ở mức *công thức cập nhật* — trình bày ngắn gọn từng phương pháp để đặt SAM, Sophia và Muon lên cùng bảng so sánh với AdamW. Cơ chế tách weight decay đã trình bày ở [26-04]({% multilang_post_url contents/chapter26/2026-09-15-26_04_adamw_and_practice %}), còn góc nhìn tiền điều kiện Hessian của Sophia như họ hàng phương pháp Newton nằm ở [14-10]({% multilang_post_url contents/chapter14/2026-09-16-14_10_modern_applications %}). Cả ba phương pháp trong bài này đều không thuộc nội dung kiểm tra.

Câu hỏi trọng tâm của seminar là: *sau khi AdamW trở thành tiêu chuẩn mặc định, cộng đồng huấn luyện mô hình lớn đang thử nghiệm những bộ tối ưu nào, và mỗi phương pháp khai thác thêm cấu trúc hình học gì?*

## AdamW vẫn là chuẩn đối chiếu

AdamW (Loshchilov & Hutter, ICLR 2019, [arXiv:1711.05101](https://arxiv.org/abs/1711.05101)) vẫn là bộ tối ưu chuẩn trong các công thức huấn luyện mô hình ngôn ngữ lớn kiểu Llama hay GPT: $$\eta$$ cỡ $$10^{-4}$$, $$\beta=(0.9,0.95)$$ hoặc $$(0.9,0.999)$$, hệ số suy giảm trọng số tách rời $$\lambda\approx 0.1$$, kết hợp warmup và lịch giảm cosine. Mọi bộ tối ưu dưới đây đều được đánh giá dựa trên chuẩn đối chiếu này.

## SAM: cực đại hóa cục bộ trước khi hạ bước

Sharpness-Aware Minimization (Foret, Kleiner, Mobahi, Neyshabur, ICLR 2021, [OpenReview](https://openreview.net/forum?id=6Tm1mposlrM)) thay mục tiêu rủi ro tại một điểm $$F(w)$$ bằng giá trị xấu nhất trong một *lân cận bán kính $$\rho$$*:

$$
\min_w\ \max_{\|\varepsilon\|_2\le\rho} F(w+\varepsilon)
\approx F\bigl(w+\rho\,\nabla F(w)/\|\nabla F(w)\|_2\bigr).
$$

Mỗi bước cập nhật của SAM thực hiện hai lượt tính gradient chứ không tạo ma trận tiền điều kiện mới:

1. **Bước nhiễu (ascent):** Tính $$g\leftarrow\nabla F(w)$$, sau đó đặt $$\varepsilon\leftarrow\rho\,g/\|g\|_2$$ (hoặc dạng tổng quát theo chuẩn đối ngẫu).
2. **Bước hạ (SAM gradient):** Tính $$g_{\mathrm{SAM}}\leftarrow\nabla F(w+\varepsilon)$$ và cập nhật $$w\leftarrow w-\eta\,g_{\mathrm{SAM}}$$ (hoặc đưa $$g_{\mathrm{SAM}}$$ vào bộ tối ưu nền như AdamW hay SGD+momentum).

Bước nhiễu hướng quá trình tối ưu về các cực tiểu **phẳng**, nơi hàm mất mát ít tăng khi tham số dao động trong một hình cầu nhỏ quanh $$w$$. Bartlett, Long và Bousquet (*The Dynamics of Sharpness-Aware Minimization*, *JMLR* 24(43), 2023) chứng minh rằng gần một cực tiểu trơn, bước bổ sung này tạo ra dao động dọc phương Hessian có độ cong lớn nhất kèm xu hướng *giảm* $$\|\nabla^2 F\|$$. Shin, Lee, Andriushchenko và Lee ([arXiv:2311.17539](https://arxiv.org/abs/2311.17539)) ghi nhận lợi ích tổng quát hóa của SAM *tăng* khi mô hình quá tham số hóa — kết nối trực tiếp với Chương 28 và điều kiện PL ở [28-05]({% multilang_post_url contents/chapter28/2026-09-18-28_05_pl_condition %}). Trong thực tế, SAM thường dùng cho thị giác máy tính và tinh chỉnh mô hình; tiền huấn luyện LLM đầy đủ thường tránh dùng vì chi phí tính gradient tăng gấp đôi. Các biến thể bán kính thích nghi (ASAM, GSAM) chỉ thay đổi hình dạng lân cận, giữ nguyên cấu trúc hai bước.

## Sophia: AdamW với ước lượng Hessian đường chéo có cắt ngưỡng

Liu, Li, Hall, Liang và Ma (*Sophia*, ICLR 2024, [OpenReview](https://openreview.net/forum?id=3xHDeA8Noi)) giữ nguyên mô-men bậc nhất kiểu Adam nhưng thay bộ tích lũy mô-men bậc hai bằng ước lượng đường chéo của ma trận Hessian kèm phép *cắt ngưỡng*. Gọi $$m$$ là trung bình trượt mũ của gradient và $$\hat h$$ là trung bình trượt mũ của ước lượng độ cong đường chéo:

$$
w\leftarrow w-\eta\cdot\operatorname{clip}\bigl(m/(\hat h+\varepsilon),\,\tau\bigr),
$$

trong đó $$\hat h$$ chỉ cần cập nhật định kỳ sau mỗi vài bước (bằng tích Hessian–vector Hutchinson hoặc ước lượng Gauss–Newton–Bartlett lấy mẫu nhãn từ đầu ra mô hình rồi bình phương gradient). Phép cắt ngưỡng đóng vai trò vùng tin cậy nhằm ngăn bước cập nhật bùng nổ khi ước lượng đường chéo cũ hoặc không xác định dương. Có thể xem Sophia như “AdamW với mẫu số mang thông tin độ cong” thay vì phương pháp Newton đầy đủ (phần thảo luận về bất biến affine và Hessian nằm ở mục 14-10). Các tác giả báo cáo Sophia cần ít bước hơn AdamW trong tiền huấn luyện mô hình ngôn ngữ với chi phí bổ sung mỗi bước tương đối nhỏ.

## Muon: trực giao hóa bước cập nhật cho ma trận trọng số ẩn

Jordan, Jin, Boza, Cesista, Newhouse và Bernstein (*Muon*, 2024, [kellerjordan.github.io/posts/muon](https://kellerjordan.github.io/posts/muon/)) áp dụng momentum Nesterov lên từng tham số dạng *ma trận* $$W\in\mathbb{R}^{m\times n}$$ rồi thay hướng cập nhật bằng ma trận trực giao gần nhất, tính xấp xỉ qua vài vòng lặp Newton–Schulz (không cần SVD):

$$
\begin{align}
B &\leftarrow \beta B+\nabla_W F,\\
O &\leftarrow \operatorname{NewtonSchulz}(B)\approx\arg\min_{Q^\top Q=I}\|Q-B\|_F,\\
W &\leftarrow W-\eta\,O.
\end{align}
$$

Các lớp nhúng (embedding), lớp đầu ra và tham số vector vẫn dùng AdamW: các ma trận trọng số ẩn 2 chiều hưởng lợi từ bước cập nhật trực giao (chuẩn phổ gần như đồng nhất giữa các phương), trong khi bảng nhúng token có cấu trúc cập nhật thưa theo hàng không phù hợp với trực giao hóa. Sau khi trở nên phổ biến trong cộng đồng tối ưu tốc độ huấn luyện NanoGPT cuối năm 2024, Jingyuan Liu và cộng sự (*Muon is Scalable for LLM Training*, [arXiv:2502.16982](https://arxiv.org/abs/2502.16982), 2025) bổ sung weight decay và hệ số tỉ lệ theo kích thước tham số, huấn luyện mô hình MoE 3B/16B (Moonlight) trên 5,7 nghìn tỷ token và báo cáo hiệu quả tính toán gấp khoảng $$2\times$$ AdamW trên đường cong định luật tỉ lệ. Shah và cộng sự ([arXiv:2505.02222](https://arxiv.org/abs/2505.02222), 2025) tiếp tục khảo sát biên Pareto đánh đổi giữa chi phí tính toán và thời gian đến quy mô 4 tỷ tham số. Đây là đối thủ *nhận biết cấu trúc ma trận* đáng chú ý đầu tiên đối với tiền điều kiện đường chéo của AdamW.

Vòng lặp Newton–Schulz thực chất là một phép lặp đa thức chi phí thấp trên $$X^\top X$$ nhằm kéo các giá trị kỳ dị về $$1$$. Điểm cốt lõi cần nhớ là: **Muon tiền điều kiện bằng nhân tử cực (polar factor) của ma trận, còn AdamW tiền điều kiện bằng căn trung bình bình phương (RMS) từng tọa độ**.

## AdamW không cần lịch tốc độ học (Schedule-free AdamW)

Defazio và cộng sự (2024) đề xuất phiên bản AdamW *không dùng lịch giảm tốc độ học* bằng cách thay lịch giảm $$\eta_t$$ bởi cơ chế lấy trung bình Polyak–Ruppert nội suy. Đây là tài liệu tham khảo tốt cho seminar; phần ghi chú tùy chọn ở [06-08]({% multilang_post_url contents/chapter06/2026-09-16-06_08_Applications_Recent %}) cũng đã đặt phương pháp này cạnh Lion và hiện tượng mép ổn định (edge of stability).

| Phương pháp | Chi phí / bộ nhớ thêm | Cấu trúc hình học khai thác | Ứng dụng điển hình | Kiểm tra? |
|-------------|-----------------------|-----------------------------|--------------------|-----------|
| AdamW | hai trung bình trượt mũ | RMS theo từng tọa độ | chuẩn mặc định cho LLM / thị giác | có (26-04) |
| SAM | gấp đôi lượt tính gradient | cực tiểu phẳng (bài toán max cục bộ) | thị giác, tinh chỉnh mô hình | không |
| Sophia | ước lượng Hessian đường chéo + cắt ngưỡng | mẫu số mang thông tin độ cong | thử nghiệm tiền huấn luyện LM | không |
| Muon | lặp Newton–Schulz trên ma trận ẩn | bước cập nhật trực giao / cực | NanoGPT, một số cấu hình tiền huấn luyện LLM | không |

**Bài tập (khảo sát lý thuyết).** Đọc phần giải thích trong bài viết Muon về lý do “dùng AdamW cho lớp nhúng và đầu ra” rồi trả lời ngắn gọn bốn ý: (i) vì sao ma trận trọng số ẩn 2 chiều phù hợp với bước cập nhật trực giao, (ii) vì sao bảng nhúng token lại không phù hợp, (iii) cơ chế này khác gì với hệ số $$1/\sqrt{\hat v}$$ *từng tọa độ* của AdamW, và (iv) vì sao bài toán cực đại hóa cục bộ của SAM phản ánh tính chất *địa hình hàm mất mát* (Chương 28) hơn là phép tiền điều kiện.

**Câu hỏi.** Trong ba phương pháp (SAM, Sophia, Muon), phương pháp nào vẫn hoạt động được nếu chỉ cho phép tính đúng *một* gradient ở mỗi bước, và nó gần với thành phần nào nhất của Chương 26 (momentum, mô-men bậc hai đường chéo, hay giảm phương sai)?

## Nguồn

- I. Loshchilov and F. Hutter, ICLR 2019 — AdamW.
- P. Foret, A. Kleiner, H. Mobahi, B. Neyshabur, ICLR 2021 — SAM.
- P. L. Bartlett et al., *JMLR* 24(43), 2023 — động lực học SAM.
- H. Liu et al., ICLR 2024 — Sophia (cập nhật ở đây; đọc Newton ở 14-10).
- K. Jordan et al., 2024 — Muon.
- Jingyuan Liu et al., [arXiv:2502.16982](https://arxiv.org/abs/2502.16982), 2025 — Muon ở quy mô LLM.
- I. Shah et al., [arXiv:2505.02222](https://arxiv.org/abs/2505.02222), 2025 — hiệu quả tiền huấn luyện Muon.
