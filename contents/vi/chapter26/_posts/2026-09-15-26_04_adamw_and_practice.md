---
layout: post
title: 26-04 AdamW và thực hành huấn luyện
chapter: '26'
order: 5
owner: Nguyen Le Linh
categories:
- chapter26
lang: vi
lesson_type: required
---


Regularization L2 cộng $$\frac{\lambda}{2}\|w\|_2^2$$ vào loss, nên gradient thêm $$\lambda w$$. Dưới **Adam**, số hạng đó bị co ngay bởi $$1/(\sqrt{\hat v}+\varepsilon)$$. Tọa độ có mô-men hai lớn *ít* bị decay hơn tọa độ nhỏ. Regularizer bạn tưởng đã viết không phải regularizer mà bộ tối ưu đang áp.

**AdamW** (Loshchilov & Hutter, ICLR 2019, [arXiv:1711.05101](https://arxiv.org/abs/1711.05101)) **tách** decay:

$$
w_{k+1} = w_k - \eta \Bigl( \hat m \oslash (\sqrt{\hat v}+\varepsilon) + \lambda w_k \Bigr).
$$

Weight decay giờ là một lực kéo về gốc trên không gian tham số, độc lập với thang thích nghi. Trong PyTorch đó là `torch.optim.AdamW`, không phải “Adam cộng `weight_decay` trên Adam cũ” (bản sau vẫn ghép trên một số phiên bản — đọc tài liệu đúng năm bạn đang code).

## Các nút thực hành vốn là tối ưu

- **Lịch tốc độ học.** Warmup rồi cosine / giảm tuyến tính là $$\eta_k$$ biến thiên. Lý thuyết SGD lồi đã muốn bước giảm; học sâu phát hiện lại dưới tên “công thức huấn luyện.”
- **Clipping gradient.** Thay $$g$$ bởi $$g\cdot \min(1, \tau/\|g\|)$$ là một trust-region trên bước ngẫu nhiên — thô, và thiết yếu với RNN và transformer.
- **Batch size và $$\eta$$**. Quy tắc scale tuyến tính (Goyal et al.) xem batch lớn hơn như ước lượng ít nhiễu hơn, chịu được $$\eta$$ lớn hơn, cho đến một ngưỡng gãy.
- **Decay ghép hay tách.** Nếu báo cáo “weight decay $$\lambda$$” trong bài, hãy nói đó có phải kiểu AdamW.

Đọc thêm (không thuộc lõi): SAM (Foret et al., ICLR 2021) tìm cực tiểu *phẳng* qua max địa phương; Muon và Sophia là case study zoo tối ưu 2023–2024. Một đoạn trong seminar là đủ.

**Bài tập.** Huấn luyện MLP nhỏ trên two-moons 2-D với Adam và AdamW cùng $$\lambda$$. Vẽ $$\|w\|_2$$ theo epoch. Bạn sẽ thấy quỹ đạo chuẩn tham số khác nhau dù loss huấn luyện trông giống.
