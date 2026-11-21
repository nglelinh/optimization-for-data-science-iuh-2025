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


# Tối ưu phân tán và liên federated

Chương 21 (ADMM) là công cụ *lồi phân tán* đầu tiên của môn: tách mục tiêu có cấu trúc, truyền biến đối ngẫu, và đạt đồng thuận. Học sâu hiếm khi trông như vậy. Mặc định 2026 là **SGD song song dữ liệu**: mỗi worker giữ một mảnh dữ liệu, tính gradient minibatch, và một server (hoặc all-reduce) trung bình các gradient (hoặc trọng số).

**Học liên federated** là cùng ý tưởng với một ràng buộc xã hội: dữ liệu thô không được rời thiết bị. **FedAvg** (McMahan et al., AISTATS 2017) cho mỗi client chạy vài bước SGD cục bộ rồi trung bình *tham số* mỗi vòng. Truyền thông, không phải flop, mới là tài nguyên khan.

Chương này là phần mở đầu. Ta không đi sâu robustness Byzantine hay nén gradient (địa hạt tuần 12 USC CSCI 599). Ta *sẽ* làm sắc tương phản ADMM đến mức bạn không gọi FedAvg là “chỉ là ADMM.”

## Các bài

1. SGD song song dữ liệu và all-reduce
2. FedAvg
3. ADMM so với phương pháp song song dữ liệu / federated
4. Ứng dụng liên federated hiện đại (tùy chọn) — FedProx, SCAFFOLD, FedAdam, y tế

Đọc chính: McMahan et al., [PMLR v54](https://proceedings.mlr.press/v54/mcmahan17a.html). Xem lại Boyd et al., ADMM. Lớp ứng dụng 2020–2026 là [29-04]({% multilang_post_url contents/chapter29/2026-09-16-29_04_modern_federated %}).
