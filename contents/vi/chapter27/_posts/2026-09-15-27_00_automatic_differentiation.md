---
layout: post
title: 27 Vi phân tự động
chapter: '27'
order: 1
owner: Nguyen Le Linh
categories:
- chapter27
lang: vi
lesson_type: required
---


# Vi phân tự động

Mọi bộ tối ưu ở Chương 26 đều cần tính gradient. Trong thực tế hiện nay, gradient hầu như không còn được tính thủ công trên giấy hay xấp xỉ bằng sai phân hữu hạn. **Vi phân tự động (Automatic Differentiation — AD)** tính đạo hàm *chính xác đến sai số dấu phẩy động* của một chương trình bằng cách áp dụng quy tắc dây chuyền (chain rule) một cách hệ thống lên từng phép toán sơ cấp.

Chương này trả lời ba câu hỏi trọng tâm:

1. **Đồ thị tính toán** là gì, và vì sao một hàm mất mát có thể xem như một chương trình?
2. AD **chiều thuận** tính tích Jacobian–vector như thế nào?
3. Vì sao **lan truyền ngược (backpropagation)** chính là AD chiều nghịch, và vì sao chế độ nghịch là lựa chọn mặc định khi bài toán có một hàm mất mát vô hướng và hàng triệu tham số?

Tài liệu tổng quan nền tảng nên tham khảo là Baydin, Pearlmutter, Radul và Siskind, *Automatic Differentiation in Machine Learning: a Survey*, JMLR 18(153), 2018, [jmlr.org/papers/v18/17-468.html](https://www.jmlr.org/papers/v18/17-468.html). Ngay từ giáo trình cổ điển của Nocedal & Wright, bài toán tính đạo hàm đã là một phần thiết yếu của tối ưu số; vi phân tự động hiện đại là bước hoàn thiện về mặt phần mềm cho nền tảng đó.

## Nội dung các bài

1. Đồ thị tính toán.
2. AD chiều thuận.
3. AD chiều nghịch và lan truyền ngược.
4. Khung vi phân tự động và học máy khoa học (tùy chọn) — PyTorch, JAX, Enzyme, PINN.
5. Tối ưu hai mức và siêu gradient (tùy chọn) — tối ưu siêu tham số (HPO) và học siêu cấp (meta-learning) dưới dạng bài toán lồng nhau.

Bài thực hành chính: tự cài đặt AD chiều nghịch trên một mạng ba nút và đối chiếu với `torch.autograd` — nếu kết quả sai lệch, nguyên nhân nằm ở đồ thị tính toán hoặc thao tác `detach` chứ không phải định nghĩa đạo hàm. Bản đồ các khung phần mềm nằm ở bài tùy chọn [27-04]({% multilang_post_url contents/chapter27/2026-09-16-27_04_autodiff_frameworks %}), còn khuôn khổ tối ưu hai mức cho HPO và MAML (khai triển vòng lặp so với vi phân ẩn) nằm ở [27-05]({% multilang_post_url contents/chapter27/2026-09-18-27_05_bilevel_hypergrad %}).
