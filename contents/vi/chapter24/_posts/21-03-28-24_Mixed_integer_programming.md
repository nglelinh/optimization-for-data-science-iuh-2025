---
layout: post
title: 24 Quy Hoạch Số Nguyên Hỗn Hợp (Phần I)
chapter: '24'
order: 1
owner: YoungJae Choung
categories:
- chapter24
lang: vi
---

Chương này giới thiệu định nghĩa, tính chất và các ví dụ kinh điển của quy hoạch số nguyên hỗn hợp (Mixed Integer Programming — MIP), đồng thời trình bày cách tiếp cận tìm nghiệm tối ưu gián tiếp thông qua các bài toán nới lỏng (relaxation) và thuật toán nhánh và cận.

## Ứng dụng giai đoạn 2022–2026 (tùy chọn)

Các mô hình phân công, bài toán cái túi (knapsack) và đặt cơ sở không chỉ là ví dụ kinh điển trong giáo trình: xếp lịch phi hành đoàn (bộ chuẩn MIPLIB `air05`), định tuyến giao hàng chặng cuối (last-mile) kết hợp dự báo nhu cầu, và lựa chọn vị trí kho hàng hay cụm GPU biên đều trực tiếp kế thừa khung mô hình ở mục 24-02. Bên cạnh đó, từ sau NeurIPS 2019, một hướng nghiên cứu mới — học quy tắc rẽ nhánh ngay bên trong thuật toán nhánh và cận — đã phát triển mạnh quanh các mô hình này. Bạn có thể đọc tiếp tại [24-06 Ứng dụng hiện đại của mô hình nguyên hỗn hợp]({% multilang_post_url contents/chapter24/2026-09-16-24_06_modern_applications %}); các chủ đề chọn đặc trưng, kiểm chứng mạng nơ-ron và cây quyết định tối ưu sẽ được trình bày ở Chương 25.
