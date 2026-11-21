---
layout: post
title: 29-03 ADMM so với song song dữ liệu và FedAvg
chapter: '29'
order: 4
owner: Nguyen Le Linh
categories:
- chapter29
lang: vi
lesson_type: required
---


[Chương 21]({{ site.baseurl }}/contents/vi/chapter21/) nghiên cứu **phương pháp hướng xen kẽ của nhân tử**. Dạng đồng thuận giải

$$
\min_{x_1,\ldots,x_P,z} \sum_{p=1}^P f_p(x_p) \quad\text{subject to}\quad x_p=z,
$$

bằng yên ngựa Lagrangian tăng cường: cập nhật nguyên thủy $$x_p$$ (thường là proximal), một trung bình $$z$$, và lên dual trên phần dư. Khi mỗi $$f_p$$ lồi và các bước đúng, ADMM có lý thuyết hội tụ chín và là đúng công cụ cho các tách **lồi có cấu trúc** (Lasso phân tán, QP đồng thuận, một số nới SDP).

SGD song song dữ liệu và FedAvg sống ở không gian thiết kế khác:

| | ADMM (Ch.21) | SGD song song dữ liệu | FedAvg |
|--|--------------|----------------------|--------|
| $$f$$ điển hình | lồi, thường hợp thành | ERM không lồi / mạng sâu | không lồi, ERM cục bộ *dị thể* |
| Thứ được trung bình | nguyên thủy $$z$$ và dual | **gradient** (hoặc trọng số đồng bộ) mỗi bước | **trọng số** sau $$E$$ bước cục bộ |
| Biến đối ngẫu | có, phần dư dẫn đồng thuận | không | không |
| Tài nguyên khan | vòng lặp của bài lồi cỡ vừa | băng thông interconnect mỗi bước | **vòng** (máy ngủ, Wi-Fi) |
| Chứng chỉ | duality gap / phần dư | không (không lồi) | không |

Gọi FedAvg là “ADMM không dual” che mất điểm chính: FedAvg *cố ý* để client trôi rồi mới trung bình tham số. ADMM *phạt* sự không đồng thuận mỗi vòng. Dùng ADMM khi viết được chương trình đồng thuận lồi và muốn phần dư để theo dõi. Dùng SGD song song dữ liệu khi huấn luyện một mạng dùng chung trên cụm bạn kiểm soát. Dùng FedAvg khi dữ liệu không được chuyển và truyền thông đắt.

Lab IUH thực tế: ba client, một mục tiêu logistic lồi chia theo mẫu — giải bằng (i) ADMM đồng thuận và (ii) FedAvg với $$E\in\{1,5\}$$. So loss huấn luyện theo *vòng truyền thông*, không theo số lần tính gradient cục bộ.

**Câu hỏi.** Trong tình huống nào một phương pháp không chiếu hoặc tách (Frank–Wolfe, ADMM) vẫn có thể thắng SGD song song dữ liệu trên một cụm — ngay cả năm 2026?
