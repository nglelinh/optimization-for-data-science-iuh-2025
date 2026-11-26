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

Khi một mô hình học sâu cần huấn luyện trên hàng nghìn tỷ token hoặc dữ liệu y tế nằm rải rác tại hàng trăm bệnh viện không thể gom chung về một máy chủ vì luật bảo mật, bài toán tối ưu không còn chỉ là câu chuyện giữa hàm mục tiêu và một bộ vi xử lý duy nhất. **Nút thắt cổ chai lớn nhất dịch chuyển từ phép tính dấu phẩy động (FLOPs) sang băng thông truyền thông (communication)!**

Chương 29 khép lại toàn bộ hành trình tối ưu hóa bằng hai mô hình tính toán phân tán trụ cột của kỷ nguyên hiện đại: **SGD song song dữ liệu** (trái tim của các cụm siêu máy tính GPU trong trung tâm dữ liệu) và **Học liên kết — Federated Learning** (nơi dữ liệu nằm yên tại thiết bị/bệnh viện, còn mô hình đi "du lịch" để học và hội tụ qua thuật toán **FedAvg**).

## Kiến thức cần nhớ: Bốn trụ cột của Tối ưu phân tán và Học liên kết

![Tối ưu hóa Phân tán và Học Liên kết (FedAvg)]({{ site.baseurl }}/img/chapter_img/zero_fill/ch29_federated_averaging.svg)

Bốn bài học của Chương 29 kết nối trực tiếp toán học tối ưu với kiến trúc hệ thống phân tán qua bốn trụ cột:

- **Song song dữ liệu đồng bộ (Data-Parallel SGD & All-Reduce):** Trong trung tâm dữ liệu có mạng tốc độ cao (NVLink/InfiniBand), mọi GPU đồng bộ gradient ở *mỗi bước* để tái tạo chính xác toán học của minibatch lớn $$PB$$ mà giảm thời gian chạy thực tế gần tuyến tính theo số GPU.
- **Học liên kết và Bội bước cục bộ (Federated Learning & FedAvg):** Khi các máy khách là điện thoại hay bệnh viện nối qua mạng chậm/không ổn định và dữ liệu phải giữ cục bộ vì quyền riêng tư, mỗi máy khách tự chạy $$E$$ epoch cục bộ trước khi gửi trọng số về máy chủ, cắt giảm số vòng truyền thông hàng chục đến hàng trăm lần.
- **Dữ liệu Không đồng nhất và Trôi cục bộ (Non-IID & Client Drift):** Đánh đổi lớn nhất của việc tăng số bước cục bộ $$E$$ là khi dữ liệu giữa các máy khách khác phân phối, mỗi máy khách tự kéo mô hình về cực tiểu riêng của mình, khiến trung bình trọng số bị lệch khỏi cực tiểu toàn cục.
- **Cầu nối ADMM vs. FedAvg và Các biến thể hiện đại:** Đối chiếu rõ khi nào dùng ADMM đồng thuận (bài toán lồi có cấu trúc, dùng biến đối ngẫu triệt tiêu trôi) và khi nào dùng FedAvg / FedProx / SCAFFOLD / FedAdam (mạng sâu phi lồi, hạn chế băng thông).

### Giải thích: Tính tay ngân sách băng thông giữa Data-Parallel SGD và FedAvg

Giả sử bạn huấn luyện một mô hình có $$d = 10^7$$ tham số (mỗi tham số `float32` chiếm $$4$$ byte, nên kích thước toàn bộ mô hình hoặc một vector gradient là $$M = 40\text{ MB}$$). Mỗi máy khách cần thực hiện tổng cộng $$100$$ bước cập nhật SGD cục bộ:

1. **Chế độ SGD song song dữ liệu (đồng bộ sau mỗi $$1$$ bước):**
   - Số vòng truyền thông: $$100$$ vòng.
   - Tổng lượng dữ liệu mỗi máy khách phải tải lên (chỉ tính chiều gửi):
     $$100 \times 40\text{ MB} = 4{,}000\text{ MB} = 4\text{ GB}.$$
   Trên mạng di động 4G/Wi-Fi không ổn định với hàng nghìn thiết bị, gửi 4 GB cho mỗi 100 bước là hoàn toàn bất khả thi!
2. **Chế độ FedAvg (mỗi máy khách chạy $$E = 10$$ bước cục bộ rồi mới đồng bộ 1 lần):**
   - Số vòng truyền thông giảm xuống còn: $$\frac{100}{10} = 10$$ vòng.
   - Tổng lượng dữ liệu mỗi máy khách tải lên:
     $$10 \times 40\text{ MB} = 400\text{ MB}$$ — **giảm đúng 10 lần băng thông!**
3. **Thông điệp cốt lõi:** Toàn bộ nghệ thuật của học liên kết nằm ở việc chọn $$E$$ đủ lớn để tiết kiệm băng thông như phép tính trên, nhưng đồng thời kiểm soát được sai số trôi cục bộ (client drift) do sự khác biệt dữ liệu giữa các máy khách gây ra!

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
