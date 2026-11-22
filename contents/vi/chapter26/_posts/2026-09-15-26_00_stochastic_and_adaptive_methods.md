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
