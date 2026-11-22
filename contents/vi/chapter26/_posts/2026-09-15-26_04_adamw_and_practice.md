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


Chính quy hóa $$\ell_2$$ cộng thêm số hạng $$\frac{\lambda}{2}\|w\|_2^2$$ vào hàm mất mát, khiến gradient tăng thêm $$\lambda w$$. Khi tối ưu bằng **Adam**, thành phần $$\lambda w$$ này cũng bị chia bởi $$1/(\sqrt{\hat v}+\varepsilon)$$. Hệ quả là các tọa độ có mô-men bậc hai lớn chịu lực suy giảm *nhỏ hơn* so với các tọa độ có mô-men bậc hai nhỏ; tức là bộ tối ưu không còn áp dụng đúng phép suy giảm trọng số đồng đều như mục đích ban đầu.

**AdamW** (Loshchilov & Hutter, ICLR 2019, [arXiv:1711.05101](https://arxiv.org/abs/1711.05101)) **tách rời** bước suy giảm trọng số khỏi phần thích nghi:

$$
w_{k+1} = w_k - \eta \Bigl( \hat m \oslash (\sqrt{\hat v}+\varepsilon) + \lambda w_k \Bigr).
$$

Lúc này, suy giảm trọng số (weight decay) tác động trực tiếp như một lực co về gốc tọa độ trên không gian tham số, độc lập với hệ số co giãn thích nghi $$\sqrt{\hat v}$$. Trong PyTorch, điều này tương ứng với `torch.optim.AdamW`, khác với `torch.optim.Adam` có tham số `weight_decay` (vốn cộng trực tiếp vào gradient theo kiểu chính quy hóa $$\ell_2$$).

## Các kỹ thuật thực hành gắn liền với tối ưu hóa

* **Lịch tốc độ học (learning rate schedule):** Khởi động tăng dần (warmup) rồi giảm theo hàm cosine hoặc tuyến tính chính là cách chọn dãy bước $$\eta_k$$ biến thiên. Lý thuyết SGD lồi đã chỉ ra nhu cầu giảm dần tốc độ học; học sâu mở rộng thêm giai đoạn warmup để ổn định giai đoạn đầu khi ước lượng mô-men còn nhiễu.
* **Cắt ngưỡng gradient (gradient clipping):** Thay $$g$$ bằng $$g\cdot \min(1, \tau/\|g\|)$$ đóng vai trò như một vùng tin cậy đơn giản giới hạn độ dài bước ngẫu nhiên, đặc biệt quan trọng khi huấn luyện mạng hồi quy (RNN) và transformer.
* **Quan hệ giữa kích thước lô và tốc độ học $$\eta$$:** Quy tắc tỉ lệ tuyến tính (Goyal và cộng sự) coi minibatch lớn hơn là ước lượng ít nhiễu hơn nên có thể tăng $$\eta$$ tương ứng cho tới một ngưỡng bão hòa.
* **Phân biệt rõ cơ chế weight decay:** Khi báo cáo tham số “weight decay $$\lambda$$” trong thực nghiệm, cần nêu rõ đó là dạng tách rời (kiểu AdamW) hay cộng vào hàm mất mát (chính quy hóa $$\ell_2$$).

Tài liệu đọc thêm (không thuộc phần lõi): SAM (Foret và cộng sự, ICLR 2021) hướng đến các cực tiểu *phẳng* thông qua bài toán cực đại hóa cục bộ; còn Muon và Sophia là các bộ tối ưu mới đáng chú ý giai đoạn 2023–2025. Bài seminar tùy chọn [26-06]({% multilang_post_url contents/chapter26/2026-09-16-26_06_modern_optimizers %}) tóm tắt công thức cập nhật của từng phương pháp (không lặp lại phần phân tích Sophia theo góc nhìn Newton ở mục 14-10); nội dung này không kiểm tra trong học kỳ.

**Bài tập.** Huấn luyện một mạng MLP nhỏ trên tập dữ liệu 2 chiều `two-moons` bằng cả Adam và AdamW với cùng hệ số $$\lambda$$, sau đó vẽ đồ thị chuẩn $$\|w\|_2$$ theo epoch. Dù đường hàm mất mát huấn luyện trông khá tương đồng, quỹ đạo của chuẩn tham số $$\|w\|_2$$ sẽ khác biệt rõ rệt giữa hai bộ tối ưu.
