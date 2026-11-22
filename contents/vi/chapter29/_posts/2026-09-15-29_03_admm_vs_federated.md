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


[Chương 21]({{ site.baseurl }}/contents/vi/chapter21/) đã trình bày **phương pháp hướng luân phiên của các nhân tử (ADMM)**. Dạng đồng thuận giải bài toán:

$$
\min_{x_1,\ldots,x_P,z} \sum_{p=1}^P f_p(x_p) \quad\text{subject to}\quad x_p=z,
$$

thông qua hàm Lagrangian tăng cường: cập nhật các biến gốc cục bộ $$x_p$$ (thường dưới dạng toán tử proximal), lấy trung bình cập nhật biến toàn cục $$z$$, và cập nhật biến đối ngẫu theo phần dư. Khi mỗi $$f_p$$ lồi và các bước con được giải đủ chính xác, ADMM có lý thuyết hội tụ hoàn chỉnh và là công cụ chuẩn mực cho các bài toán tách **lồi có cấu trúc** (Lasso phân tán, quy hoạch bậc hai đồng thuận, một số bài toán nới lỏng SDP).

Ngược lại, SGD song song dữ liệu và FedAvg được thiết kế cho bối cảnh khác hẳn:

| Tiêu chí | ADMM (Ch. 21) | SGD song song dữ liệu | FedAvg |
|----------|---------------|-----------------------|--------|
| Hàm mục tiêu $$f$$ điển hình | lồi, thường có cấu trúc hợp thành | ERM không lồi / mạng sâu | không lồi, ERM cục bộ *không đồng nhất* |
| Đại lượng lấy trung bình | biến gốc $$z$$ và biến đối ngẫu | **gradient** (hoặc trọng số đồng bộ) mỗi bước | **trọng số** sau $$E$$ bước cục bộ |
| Biến đối ngẫu | có, phần dư thúc đẩy đồng thuận | không | không |
| Tài nguyên khan hiếm | số vòng lặp của bài toán lồi cỡ vừa | băng thông kết nối liên nút mỗi bước | **số vòng truyền thông** (thiết bị gián đoạn, Wi-Fi) |
| Tiêu chí chứng nhận | khoảng cách đối ngẫu / phần dư | không (bài toán không lồi) | không |

Gọi FedAvg là “ADMM bỏ biến đối ngẫu” dễ làm mờ đi sự khác biệt bản chất: FedAvg *chủ động* cho phép các máy khách chạy nhiều bước cục bộ và chấp nhận độ trôi trước khi trung bình hóa tham số, trong khi ADMM *phạt trực tiếp* sự sai lệch giữa các nút qua biến đối ngẫu ở mọi vòng lặp. Nên dùng ADMM khi bài toán viết được dưới dạng đồng thuận lồi và cần theo dõi phần dư; dùng SGD song song dữ liệu khi huấn luyện mô hình lớn trên cụm máy chủ tập trung; và dùng FedAvg khi dữ liệu phải ở lại thiết bị đầu cuối còn chi phí truyền thông là nút thắt chính.

**Bài thực hành.** Với 3 máy khách chia nhau dữ liệu của một bài toán hồi quy logistic lồi, hãy giải cùng bài toán bằng (i) ADMM đồng thuận và (ii) FedAvg với $$E\in\{1,5\}$$, sau đó so sánh hàm mất mát huấn luyện theo *số vòng truyền thông* thay vì theo số lượt tính gradient cục bộ.

**Câu hỏi.** Trong những tình huống nào một phương pháp không cần phép chiếu hoặc phương pháp tách biến (như Frank–Wolfe hay ADMM) vẫn có thể vượt trội hơn SGD song song dữ liệu trên cùng một cụm tính toán?
