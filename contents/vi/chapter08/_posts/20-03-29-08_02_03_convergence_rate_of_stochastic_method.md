---
layout: post
title: '08-02-03 Tốc độ Hội tụ của Phương pháp Ngẫu nhiên'
chapter: '08'
order: 14
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

Nếu cả hai biến thể — tuần hoàn và ngẫu nhiên — đều hội tụ, tại sao giới học máy gần như luôn xáo trộn dữ liệu ngẫu nhiên thay vì giữ nguyên thứ tự cố định? Câu trả lời nằm gọn trong bài học này: **phụ thuộc vào số lượng thành phần $$m$$ trong tốc độ hội tụ**. Một phép so sánh tinh tế về cách hằng số Lipschitz $$G$$ nhân lên theo $$m$$ sẽ cho thấy sự chênh lệch khổng lồ khi $$m$$ lên tới hàng triệu.

Khi ta chạy phương pháp batch trên $$\sum_{i=1}^m f_i(x)$$, hằng số Lipschitz của tổng có thể lớn tới $$G_{\text{batch}} = mG$$ và mỗi bước tốn $$m$$ phép tính subgradient. Biến thể ngẫu nhiên phá vỡ vòng lặp lồng nhau ấy: nhờ tính không chệch, nó đạt độ chính xác $$\epsilon$$ chỉ sau số vòng lặp tỷ lệ với $$m^2 G^2 / \epsilon^2$$ (tức trung bình chỉ $$m G^2 / \epsilon^2$$ lượt quét toàn bộ dữ liệu — tương đương batch), trong khi với bài toán lấy trung bình $$\frac{1}{m}\sum f_i(x)$$, tốc độ $$O(G^2/\epsilon^2)$$ thậm chí **độc lập hoàn toàn với kích thước tập dữ liệu $$m$$**!

## Kiến thức cần nhớ: Ba trụ cột so sánh tốc độ batch, tuần hoàn và ngẫu nhiên

- **Chuẩn hóa hàm tổng vs. hàm trung bình:** Nếu viết $$\min_x \frac{1}{m}\sum_{i=1}^m f_i(x)$$ với mỗi $$f_i$$ là $$G$$-Lipschitz, thì hàm trung bình cũng $$G$$-Lipschitz. Khi đó:
  - *Subgradient batch* cần $$O(R^2 G^2 / \epsilon^2)$$ bước, mỗi bước tốn $$m$$ đánh giá $$\implies$$ tổng chi phí $$O(m R^2 G^2 / \epsilon^2)$$ đánh giá subgradient.
  - *Subgradient ngẫu nhiên* cần $$O(R^2 G^2 / \epsilon^2)$$ bước, mỗi bước tốn đúng $$1$$ đánh giá $$\implies$$ tổng chi phí $$O(R^2 G^2 / \epsilon^2)$$ — **giảm đúng $$m$$ lần**!
- **Lý do bản tuần hoàn chậm hơn bản ngẫu nhiên trong trường hợp xấu nhất:** Trong một chu kỳ tuần hoàn, sai số trượt (drift) giữa điểm đầu chu kỳ và điểm giữa chu kỳ tích lũy tuyến tính theo $$m$$, khiến cận lý thuyết xấu nhất bị nhân thêm hệ số theo $$m$$ so với bản rút thăm ngẫu nhiên.
- **Phân tích theo đơn vị "epoch" (một lượt quét $$m$$ mẫu):** Để so sánh công bằng, ta luôn quy đổi về tổng số phép tính subgradient thành phần $$g_i$$. Một bước batch tiêu tốn tài nguyên bằng $$m$$ bước ngẫu nhiên.

### Giải thích: Tính tổng số phép tính subgradient khi $$m = 1{,}000$$ mẫu

Xét bài toán trung bình $$f(x) = \frac{1}{1000}\sum_{i=1}^{1000} f_i(x)$$ với $$R = 1$$, $$G = 1$$, mục tiêu đạt sai số $$\epsilon = 0.1$$.

1. **Phương pháp subgradient batch:**
   - Số vòng lặp cần theo cận lý thuyết: $$k_{\text{batch}} = \frac{R^2 G^2}{\epsilon^2} = \frac{1^2 \cdot 1^2}{0.1^2} = 100$$ vòng lặp.
   - Mỗi vòng lặp phải tính cả $$m = 1{,}000$$ subgradient thành phần.
   - **Tổng chi phí:** $$100 \times 1{,}000 = 100{,}000$$ lần tính $$g_i$$ (tức 100 epochs).
2. **Phương pháp subgradient ngẫu nhiên (chọn đều $$i_k$$):**
   - Số vòng lặp cần theo cận kỳ vọng: $$k_{\text{stoch}} = \frac{R^2 G^2}{\epsilon^2} = 100$$ vòng lặp.
   - Mỗi vòng lặp chỉ tính đúng $$1$$ subgradient thành phần!
   - **Tổng chi phí:** $$100 \times 1 = 100$$ lần tính $$g_i$$ (chỉ bằng **0.1 epoch** — tức chưa đọc hết nổi 10% tập dữ liệu đã đạt cận kỳ vọng $$\epsilon = 0.1$$!).
3. **Lưu ý quan trọng khi $$\epsilon$$ rất nhỏ:** Nếu ta đòi độ chính xác siêu cao $$\epsilon = 10^{-4}$$, số bước ngẫu nhiên vọt lên $$10^8$$ (tức $$100{,}000$$ epochs), và vì bước phải thu cực nhỏ nên bản ngẫu nhiên bắt đầu lộ nhược điểm dao động kéo dài.

Tốc độ hội tụ lý thuyết có sự khác biệt giữa cách chọn chỉ số tuần hoàn và cách chọn chỉ số ngẫu nhiên.

[Tốc độ hội tụ]({% multilang_post_url contents/chapter08/20-03-29-08_01_04_convergence_rate %}) của phương pháp subgradient batch là $$O(G_{batch}^{2}/\epsilon^{2})$$, trong đó $$G_{batch}$$ là hằng số Lipschitz của hàm tổng $$\sum f_i$$ (có bậc $$mG$$ nếu mỗi $$f_i$$ có hằng số Lipschitz là $$G$$).

- **Phương pháp tuần hoàn**: Số bước cập nhật cần thiết là $$O(m^{3}G^{2}/\epsilon^{2})$$. Nếu quy đổi một chu kỳ (duyệt qua đủ $$m$$ hàm thành phần) là tương đương về chi phí với một bước của phương pháp subgradient batch, thì phương pháp tuần hoàn cần $$O(m^{2}G^{2}/\epsilon^{2})$$ chu kỳ.
- **Phương pháp ngẫu nhiên**: Số bước cập nhật cần thiết là $$O(m^{2}G^{2}/\epsilon^{2})$$, tương đương $$O(mG^{2}/\epsilon^2)$$ chu kỳ — nhanh hơn $$m$$ lần so với phương pháp batch và phương pháp tuần hoàn ($$O(m^2G^2/\epsilon^2)$$ chu kỳ). Theo đánh giá Big-O, khi $$m$$ lớn, phương pháp ngẫu nhiên có tốc độ hội tụ tốt hơn.

Mặc dù cận Big-O của hai phương pháp chênh nhau một hệ số $$m$$, cần lưu ý rằng cận của phương pháp tuần hoàn là đánh giá cho trường hợp xấu nhất, còn cận của phương pháp ngẫu nhiên là đánh giá theo kỳ vọng (trường hợp trung bình). Trong thực tế, mức chênh lệch có thể không lớn như kết quả tiệm cận gợi ý.
