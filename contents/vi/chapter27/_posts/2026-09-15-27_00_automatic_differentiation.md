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

Mọi bộ tối ưu ở Chương 26 đều cần gradient. Năm 2026 gradient đó hầu như không còn được tính trên giấy và hầu như không phải sai phân hữu hạn. **Vi phân tự động (AD)** tính đạo hàm *chính xác* của một chương trình bằng cách áp quy tắc chuỗi có hệ thống lên các phép toán sơ cấp.

Chương này trả lời ba câu:

1. **Đồ thị tính toán** là gì, và vì sao hàm mất mát “chỉ là một chương trình”?
2. AD **thuận** tính tích Jacobian–vector thế nào?
3. Vì sao **lan truyền ngược** là AD nghịch, và vì sao chế độ nghịch là mặc định đúng khi ta có một loss vô hướng và hàng triệu tham số?

Khảo sát để để trên bàn là Baydin, Pearlmutter, Radul, Siskind, *Automatic Differentiation in Machine Learning: a Survey*, JMLR 18(153), 2018, [jmlr.org/papers/v18/17-468.html](https://www.jmlr.org/papers/v18/17-468.html). Nocedal & Wright đã coi “tính đạo hàm” là một phần của tối ưu số; AD là chương đó sau khi phần mềm bắt kịp.

## Các bài

1. Đồ thị tính toán
2. Chế độ thuận
3. Chế độ nghịch và lan truyền ngược
4. Khung vi phân tự động và ML khoa học (tùy chọn) — PyTorch, JAX, Enzyme, PINN
5. Tối ưu hai mức và siêu gradient (tùy chọn) — HPO / meta như một khuôn lồng

Lab: reverse mode thủ công trên mạng ba nút so với `torch.autograd` — nếu chúng lệch, đồ thị hoặc `detach` của bạn sai, không phải định nghĩa đạo hàm. Bản đồ phần mềm tùy chọn là [27-04]({% multilang_post_url contents/chapter27/2026-09-16-27_04_autodiff_frameworks %}). Khuôn HPO / MAML lồng nhau — tháo cuộn so với vi phân ẩn — là [27-05]({% multilang_post_url contents/chapter27/2026-09-18-27_05_bilevel_hypergrad %}).
