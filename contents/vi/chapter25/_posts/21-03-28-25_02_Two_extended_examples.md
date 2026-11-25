---
layout: post
title: '25-02 Hai ví dụ mở rộng'
chapter: '25'
order: 7
owner: YoungJae Choung
categories:
- chapter25
lang: vi
---

Trong nhiều thập kỷ, sách giáo khoa thống kê từng dạy một quan niệm gần như bất di bất dịch: các bài toán thống kê lý tưởng như **chọn đúng $$k$$ biến tốt nhất** (ràng buộc $$\|\beta\|_0 \le k$$) hay **hồi quy bình phương trung vị nhỏ nhất** (LMS, chống nhiễu tới 50%) tuy đẹp về mặt thống kê nhưng là *NP-khó*, nên buộc phải thay thế bằng các xấp xỉ lồi như Lasso ($$\ell_1$$) hay hồi quy Huber.

Hai bài học mở rộng tiếp theo sẽ đảo ngược quan niệm cũ đó: nhờ sự nhảy vọt của công nghệ **Nhánh và Cắt** kết hợp với khởi động nóng từ tối ưu bậc nhất, cả hai bài toán thống kê kinh điển này đều có thể được mô hình hóa gọn gàng thành **quy hoạch nguyên hỗn hợp (MIP)** và giải chính xác ở quy mô thực tế!

## Kiến thức cần nhớ: Ba trụ cột nối Thống kê cổ điển với MIP hiện đại

Trước khi đi sâu vào chi tiết của từng mô hình ở mục 25-02-01 và 25-02-02, hãy nhìn bức tranh chung qua ba trụ cột:

- **Tính phi lồi của các chuẩn thống kê lý tưởng:** Cả phép đếm số biến khác không $$\|\beta\|_0$$ lẫn phép lấy trung vị phần dư $$\operatorname{median}|r_i|$$ đều là các hàm không lồi, không liên tục hoặc đa cực tiểu cục bộ — khiến gradient descent thông thường dễ bị mắc kẹt.
- **Sức mạnh mã hóa của Biến nhị phân $$z_i \in \{0, 1\}$$:** Chỉ cần gắn một công tắc $$z_i$$ cho mỗi *đặc trưng* (chọn hay không chọn trong Best Subset) hoặc cho mỗi *mẫu dữ liệu* (tính vào phần dư trung vị hay bỏ qua như điểm ngoại lai trong LMS), ta chuyển toàn bộ tính phi lồi về dạng quy hoạch nguyên hỗn hợp có cấu trúc chặt chẽ.
- **Chiến lược Lai (Hybrid Warm-Start + MIP):** Tối ưu bậc nhất rời rạc chạy cực nhanh để tìm một nghiệm khả thi chất lượng cao (cận trên $$\bar{z}$$ tốt ngay từ giây đầu tiên), sau đó bộ giải MIP tiếp quản để vừa cải thiện thêm nghiệm vừa cung cấp **chứng nhận tối ưu toàn cục** qua MIP gap.

### Giải thích: Minh họa nhỏ vì sao LMS chống điểm ngoại lai vượt trội hơn LS

Xét bộ dữ liệu 1 biến chỉ gồm 3 điểm $$(x_i, y_i)$$: $$(1, 1)$$, $$(2, 2)$$, và một điểm ngoại lai nặng $$(3, 10)$$. Ta muốn khớp đường thẳng đi qua gốc tọa độ $$y = \beta x$$.

1. **Ước lượng Bình phương tối thiểu (OLS — cực tiểu $$\sum (y_i - \beta x_i)^2$$):**
   $$\hat{\beta}_{\text{OLS}} = \frac{\sum x_i y_i}{\sum x_i^2} = \frac{1(1) + 2(2) + 3(10)}{1^2 + 2^2 + 3^2} = \frac{35}{14} = 2.5.$$
   Chỉ vì 1 điểm ngoại lai $$(3, 10)$$, đường hồi quy bị kéo lệch hoàn toàn từ hệ số góc đúng $$1.0$$ lên thành $$2.5$$ (sai số trên hai điểm sạch lên tới $$1.5$$ và $$3.0$$)!
2. **Ước lượng Bình phương trung vị nhỏ nhất (LMS — cực tiểu $$\operatorname{median}|y_i - \beta x_i|$$):**
   Xét $$\beta = 1$$: ba phần dư tuyệt đối là $$|1 - 1| = 0$$, $$|2 - 2| = 0$$, và $$|10 - 3| = 7$$.
   Sắp xếp tăng dần: $$(0,\; 0,\; 7)$$ — **trung vị bằng đúng $$0$$**!
3. **Ý nghĩa:** Vì trung vị không thể âm, $$\hat{\beta}_{\text{LMS}} = 1$$ đạt cực tiểu tuyệt đối $$0$$ và hoàn toàn miễn nhiễm trước điểm ngoại lai $$(3, 10)$$ — dù bạn đổi $$10$$ thành $$1{,}000{,}000$$! Nhưng để tìm được $$\beta$$ như vậy trong không gian nhiều chiều, ta cần công cụ MIP ở hai bài học tiếp theo.

Phần này trình bày hai ví dụ ứng dụng mở rộng của quy hoạch số nguyên hỗn hợp trong thống kê và học máy:

* Chọn tập con tốt nhất (Best subset selection)
* Hồi quy bình phương trung vị nhỏ nhất và hồi quy phân vị nhỏ nhất (Least median of squares / Least quantile regression)
