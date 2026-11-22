---
layout: post
title: 29 Tối ưu phân tán và liên federated
chapter: '29'
order: 1
owner: Nguyen Le Linh
categories:
- chapter29
lang: vi
lesson_type: required
---


# Tối ưu phân tán và học liên kết

Chương 21 (ADMM) đã giới thiệu cách tiếp cận *tối ưu lồi phân tán* đầu tiên trong môn học: tách hàm mục tiêu có cấu trúc, trao đổi biến đối ngẫu và đạt đồng thuận. Tuy nhiên, huấn luyện học sâu quy mô lớn thường không đi theo mô hình đó. Cách tiếp cận tiêu chuẩn hiện nay là **SGD song song dữ liệu (data-parallel SGD)**: mỗi nút tính toán giữ một phần dữ liệu, tính gradient trên minibatch cục bộ, rồi máy chủ tham số (hoặc phép toán all-reduce) lấy trung bình các gradient hoặc trọng số.

**Học liên kết (federated learning)** mở rộng ý tưởng này dưới ràng buộc quyền riêng tư: dữ liệu thô không được phép rời khỏi thiết bị hoặc cơ sở sở hữu dữ liệu. Thuật toán **FedAvg** (McMahan và cộng sự, AISTATS 2017) cho mỗi máy khách thực hiện nhiều bước SGD cục bộ rồi mới gửi *tham số* về máy chủ để lấy trung bình theo từng vòng. Trong bối cảnh này, băng thông và số vòng truyền thông — chứ không phải số phép tính dấu phẩy động — mới là nút thắt chính.

Chương này cung cấp phần nhập môn cốt lõi, không đi sâu vào các chủ đề nâng cao như chống lỗi Byzantine hay nén gradient, nhưng sẽ phân biệt rõ bản chất giữa ADMM đồng thuận và FedAvg.

## Nội dung các bài

1. SGD song song dữ liệu và all-reduce.
2. Thuật toán FedAvg.
3. So sánh ADMM với SGD song song dữ liệu và học liên kết.
4. Ứng dụng học liên kết hiện đại (tùy chọn) — FedProx, SCAFFOLD, FedAdam và ứng dụng y tế.

Tài liệu đọc chính: McMahan và cộng sự ([PMLR v54](https://proceedings.mlr.press/v54/mcmahan17a.html)) cùng bài khảo sát ADMM của Boyd và cộng sự. Các mở rộng giai đoạn 2020–2026 được trình bày tại bài tùy chọn [29-04]({% multilang_post_url contents/chapter29/2026-09-16-29_04_modern_federated %}).
