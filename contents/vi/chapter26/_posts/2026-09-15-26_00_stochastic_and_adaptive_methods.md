---
layout: post
title: 26 Phương pháp ngẫu nhiên và thích nghi cho học máy
chapter: '26'
order: 1
owner: Nguyen Le Linh
categories:
- chapter26
lang: vi
lesson_type: required
---

Nếu bạn muốn huấn luyện một mô hình ngôn ngữ trên hàng nghìn tỷ token bằng gradient descent toàn lô (full-batch GD), bạn sẽ phải đọc hết toàn bộ kho văn bản internet chỉ để thực hiện... **đúng một bước cập nhật trọng số**. Trong thế giới dữ liệu khổng lồ của học máy hiện đại, sự hoàn hảo của gradient chính xác lại trở thành kẻ thù lớn nhất của tốc độ.

Chương 26 đánh dấu bước ngoặt từ tối ưu cổ điển sang **tối ưu ngẫu nhiên và thích nghi** — động cơ thực sự vận hành đằng sau PyTorch, JAX và mọi hệ thống học sâu ngày nay. Thay vì chờ tính đủ gradient của $$n$$ mẫu, ta chấp nhận một ước lượng nhiễu từ một lô nhỏ (minibatch) để đi nhanh gấp hàng nghìn lần, rồi dùng **động lượng (momentum)**, **co giãn thích nghi theo tọa độ (Adam/AdamW)** và **giảm phương sai (SVRG/SAGA)** để thuần hóa nhiễu đó.

## Kiến thức cần nhớ: Bốn trụ cột của tối ưu ngẫu nhiên hiện đại

![Tối ưu hóa Ngẫu nhiên & Thích nghi Quy mô lớn]({{ site.baseurl }}/img/chapter_img/zero_fill/ch26_stochastic_adaptive_opt.svg)

Toàn bộ Chương 26 được xây dựng trên bốn trụ cột kỹ thuật bổ trợ cho nhau:

- **Ước lượng ngẫu nhiên và Đánh đổi Phương sai – Tốc độ (SGD & Minibatch):** Thay tổng $$n$$ thành phần bằng trung bình trên $$B$$ mẫu ngẫu nhiên giữ nguyên tính không chệch ($$\mathbb{E}[g_k] = \nabla F(w_k)$$) nhưng tạo ra sàn nhiễu tỉ lệ với $$\sigma^2 / B$$, dẫn tới tốc độ $$O(1/\sqrt{T})$$ thay vì $$O(1/T)$$.
- **Lọc nhiễu và Tăng tốc bằng Quán tính (Momentum & Nesterov):** Tích lũy trung bình trượt của các gradient quá khứ vừa giúp triệt tiêu dao động zíc-zắc trên hẻm hẹp (số điều kiện $$\kappa$$ lớn), vừa tăng cường tốc độ dọc theo đáy thung lũng.
- **Tiền điều kiện đường chéo thích nghi (AdaGrad → RMSProp → Adam → AdamW):** Tự động gán một tốc độ học riêng cho từng tham số dựa trên lịch sử bình phương gradient, và đặc biệt tách rời suy giảm trọng số (weight decay) khỏi phép chia thích nghi trong AdamW.
- **Biến kiểm soát giảm phương sai (SVRG & SAGA):** Khi bài toán có dạng tổng hữu hạn lồi mạnh, ta tận dụng một "mốc" gradient cũ để triệt tiêu phương sai khi tiến gần nghiệm, khôi phục hội tụ tuyến tính với chi phí mỗi bước chỉ bằng SGD!

### Giải thích: So sánh tay 1 epoch của Full-Batch GD và SGD

Xét bài toán cực tiểu hóa tổng hữu hạn gồm $$n = 2$$ mẫu:

$$
F(w) = \frac{1}{2}\Bigl[f_1(w) + f_2(w)\Bigr] = \frac{1}{2}\left[\frac{1}{2}(w - 2)^2 + \frac{1}{2}(w - 6)^2\right],
$$

có nghiệm tối ưu toàn cục là trung bình cộng $$w^\star = 4$$. Xuất phát từ $$w_0 = 0$$ với tốc độ học $$\eta = 0.5$$, hãy so sánh kết quả sau **đúng 2 lần tính gradient đơn mẫu (1 epoch)**:

1. **Full-Batch GD (dùng cả 2 lần tính gradient cho 1 bước duy nhất):**
   - Tính $$\nabla f_1(0) = 0 - 2 = -2$$ và $$\nabla f_2(0) = 0 - 6 = -6$$.
   - Gradient toàn lô: $$\nabla F(0) = \frac{-2 + (-6)}{2} = -4$$.
   - Sau 1 epoch: $$w_1^{\text{GD}} = 0 - 0.5(-4) = 2.0$$ (vẫn còn cách đích $$|2.0 - 4| = 2.0$$).
2. **SGD (cập nhật ngay sau mỗi mẫu, tổng vẫn chỉ 2 lần tính gradient):**
   - *Bước 1 (mẫu 1):* $$\nabla f_1(0) = -2 \Rightarrow w_{0.5} = 0 - 0.5(-2) = 1.0$$.
   - *Bước 2 (mẫu 2, tính tại điểm mới $$w_{0.5} = 1.0$$!):* $$\nabla f_2(1.0) = 1.0 - 6 = -5 \Rightarrow w_1^{\text{SGD}} = 1.0 - 0.5(-5) = 3.5$$!
3. **Kết luận trực giác:** Với cùng ngân sách tính toán 1 epoch, SGD đã tiến tới $$3.5$$ (chỉ còn cách đích $$0.5$$ — gấp 4 lần gần hơn GD!), vì nó biết tận dụng ngay thông tin của mẫu 1 trước khi xử lý mẫu 2. Cái giá phải trả sẽ lộ diện ở gần đích $$w = 4$$: khi đó $$\nabla f_1(4) = +2 \neq 0$$ và $$\nabla f_2(4) = -2 \neq 0$$, khiến SGD tiếp tục rung lắc quanh $$4$$ nếu không giảm $$\eta$$ hoặc dùng kỹ thuật giảm phương sai.

# Phương pháp ngẫu nhiên và thích nghi cho học máy

Các Chương 06–09 tập trung vào phương pháp bậc nhất **toàn lô (full-batch)**, nơi mỗi bước tính gradient (hoặc toán tử proximal) đều duyệt qua toàn bộ tập huấn luyện. Trong học máy hiện đại, cách làm đó hiếm khi khả thi ở quy mô lớn. Chương này trình bày bộ công cụ tiêu chuẩn cho bài toán cực tiểu hóa rủi ro thực nghiệm (ERM):

$$
\min_w F(w) = \frac{1}{n}\sum_{i=1}^n f_i(w), \qquad f_i(w) = \ell\bigl(h_w(x_i), y_i\bigr).
$$

Các ý tưởng liên quan đã xuất hiện trong [06-05 Hạ gradient ngẫu nhiên]({% multilang_post_url contents/chapter06/21-03-20-06_05_stochastic_gradient_descent %}) và phần dưới đạo hàm ngẫu nhiên ở Chương 08. Ở đây, ta trình bày có hệ thống từ SGD và minibatch đến hai thành phần cốt lõi trong mọi thư viện học sâu: **động lượng (momentum) / tăng tốc Nesterov** và **điều chỉnh bước học thích nghi theo tọa độ** (AdaGrad → trực giác RMSProp → Adam → AdamW). Bài bắt buộc cuối cùng giới thiệu các phương pháp giảm phương sai (SVRG, SAGA) để làm rõ khi nào lý thuyết tối ưu lồi cho tốc độ vượt trội hơn Adam.

## Vì sao cần tách thành một chương riêng

Với các tập dữ liệu lớn như ImageNet hay kho ngữ liệu của mô hình ngôn ngữ, gradient descent toàn lô không chỉ bị giới hạn bởi số vòng lặp mà chủ yếu bị chặn bởi *bộ nhớ và thời gian thực thi (wall-clock time)*. Thay gradient đầy đủ bằng một ước lượng không chệch (hoặc gần không chệch) tính từ một mẫu hoặc một minibatch kích thước $$B\ll n$$ cho phép thực hiện nhiều bước cập nhật tham số hơn trong cùng một khoảng thời gian, đánh đổi bằng nhiễu lấy mẫu. Các phương pháp thích nghi xử lý nhiễu này bằng cách co giãn tốc độ học riêng theo từng tọa độ, còn momentum tích lũy vận tốc để củng cố các hướng giảm ổn định.

Nhiều giáo trình tối ưu cho học máy hiện đại đều đặt chủ đề này ở phần cốt lõi, chẳng hạn MIT 6.7220 (S25), EPFL CS-439, USC CSCI 599 và BU EC525.

## Nội dung các bài

1. SGD và minibatch — ước lượng không chệch, xáo trộn dữ liệu và tốc độ hội tụ $$O(1/\sqrt{T})$$.
2. Momentum và tăng tốc Nesterov — heavy ball so với nhìn trước; diễn giải trực quan theo phong cách Distill.
3. Từ AdaGrad đến Adam — tiền điều kiện đường chéo theo từng tọa độ.
4. AdamW và thực hành huấn luyện — tách suy giảm trọng số (weight decay), lịch tốc độ học và cắt ngưỡng gradient.
5. Giảm phương sai — SVRG và SAGA cho bài toán tổng hữu hạn, và khi nào Adam theo minibatch vẫn hiệu quả hơn.
6. Bộ tối ưu thích nghi hiện đại (seminar tùy chọn) — SAM, Sophia và Muon so với chuẩn AdamW.

Các mô phỏng tương tác cho SGD nằm trong [`interactive_math/optimization`](https://github.com/nglelinh/interactive_math/tree/main/optimization). Bài phân tích trực quan về momentum nằm ở [26-02]({% multilang_post_url contents/chapter26/2026-09-15-26_02_momentum_and_nesterov %}) (nên đọc kèm FISTA ở [09-05]({% multilang_post_url contents/chapter09/20-01-08-09_05_acceleration %})). Các bộ tối ưu SAM, Muon và Sophia là tài liệu **đọc thêm** (không nằm trong phạm vi kiểm tra) tại bài seminar tùy chọn [26-06]({% multilang_post_url contents/chapter26/2026-09-16-26_06_modern_optimizers %}).
