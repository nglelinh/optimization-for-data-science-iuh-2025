---
layout: post
title: '08-02-04 So sánh Phương pháp Batch và Ngẫu nhiên'
chapter: '08'
order: 15
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

Trong phòng thí nghiệm học máy, có một biểu đồ quen thuộc đến mức gần như thành biểu tượng: trục hoành là thời gian tính toán (tính bằng số lượt quét dữ liệu — epochs), trục tung là sai số $$f(x) - f^*$$. Đường cong của phương pháp ngẫu nhiên lao dốc thẳng đứng ngay trong epoch đầu tiên, bỏ xa phương pháp batch một khoảng mênh mông; nhưng rồi đến gần đáy, nó bắt đầu rung lắc đi ngang, để đường cong chậm rãi nhưng vững chãi của phương pháp batch âm thầm vượt qua ở độ chính xác cao.

Bài học này đặt hai phương pháp lên bàn cân thực chiến. Không có kẻ thắng tuyệt đối trong mọi chế độ: hiểu rõ thời điểm chuyển giao giữa "giai đoạn tiếp cận nhanh độ chính xác vừa" (vùng thống trị của stochastic) và "giai đoạn tinh chỉnh độ chính xác cao" (vùng ưu thế của batch) là kỹ năng cốt lõi giúp bạn chọn thuật toán — hoặc thiết kế chiến lược lai (tăng dần cỡ mini-batch theo thời gian).

## Kiến thức cần nhớ: Bốn tiêu chí đối chiếu Batch và Ngẫu nhiên

- **Chi phí trên mỗi đơn vị giảm sai số ban đầu:** Khi còn xa nghiệm tối ưu, phương sai nhiễu nhỏ hơn rất nhiều so với tín hiệu hướng đi chung. Nhờ cập nhật $$m$$ lần trong thời gian batch cập nhật 1 lần, phương pháp ngẫu nhiên giảm sai số ban đầu nhanh vượt trội.
- **Độ chính xác yêu cầu ($$\epsilon$$ vừa vs. $$\epsilon$$ cực nhỏ):** Trong học máy thống kê, sai số tổng quát hóa vốn đã bị giới hạn bởi nhiễu dữ liệu (ví dụ $$\epsilon \sim 10^{-2}$$ hay $$10^{-3}$$), nên ta hiếm khi cần tối ưu chính xác tới $$10^{-10}$$ — đó là lý do phương pháp ngẫu nhiên thống trị huấn luyện mô hình lớn. Ngược lại, trong tối ưu kỹ thuật hoặc bài toán ràng buộc chặt, độ chính xác cao lại cực kỳ quan trọng.
- **Khả năng song song hóa phần cứng (Vectorization / GPU):** Phương pháp batch (và mini-batch lớn) tận dụng rất tốt phép nhân ma trận song song trên GPU/TPU, trong khi cập nhật từng mẫu $$B=1$$ mang tính tuần tự cao và lãng phí băng thông tính toán.
- **Chiến lược lai (Growing Mini-batch & Variance Reduction):** Bắt đầu bằng mini-batch nhỏ để lao nhanh về vùng nghiệm, sau đó tăng dần cỡ lô (hoặc chuyển sang phương pháp giảm phương sai như SVRG/SAGA khi hàm trơn) giúp gặt hái ưu điểm của cả hai thế giới.

### Giải thích: Bảng tính tay so sánh ngân sách giữa Batch và Stochastic với $$m = 10{,}000$$

Giả sử ta có tập dữ liệu $$m = 10{,}000$$ mẫu với $$R = 1, G = 1$$. Quy đổi mọi chi phí về **số lượt tính $$g_i$$** (1 epoch = $$10{,}000$$ lượt tính).

1. **Mục tiêu độ chính xác vừa ($$\epsilon = 0.05$$, phổ biến trong học máy):**
   - **Stochastic:** Cần $$k \approx \frac{1}{0.05^2} = 400$$ lượt tính $$g_i$$ = **0.04 epoch** (mới duyệt 4% dữ liệu!).
   - **Batch:** Cần $$k \approx 400$$ vòng lặp batch = $$400 \times 10{,}000 = 4{,}000{,}000$$ lượt tính $$g_i$$ = **400 epochs**.
   - *Kết luận:* Stochastic nhanh hơn tới **10,000 lần** về số phép tính lý thuyết ở ngưỡng sai số vừa!
2. **Mục tiêu độ chính xác cao khi có bước cố định ($$t = 0.01$$):**
   - Với **Batch**, nếu bài toán có thêm cấu trúc trơn cục bộ gần nghiệm, ta có thể dùng bước lớn hơn hoặc chuyển sang phương pháp bậc hai/proximal để đạt $$\epsilon = 10^{-6}$$ trong vài trăm bước.
   - Với **Stochastic** bước cố định $$t = 0.01$$, sai số kẹt mãi ở sàn $$O(G^2 t / 2) = 0.005$$; muốn hạ xuống $$\epsilon = 10^{-4}$$ phải giảm bước xuống $$10^{-4}$$ và chạy tới $$10^8$$ bước = **10,000 epochs**!
3. **Bài học thực hành:** Dùng mini-batch nhỏ (ví dụ $$B = 64$$ hoặc $$256$$) để vừa tận dụng song song hóa, vừa đạt tiến độ nhanh trong vài epoch đầu, rồi giảm learning rate theo lịch hoặc tăng cỡ lô ở giai đoạn cuối.

Đặc điểm hội tụ của phương pháp batch và phương pháp ngẫu nhiên có thể tóm tắt như sau:

Nhìn chung, phương pháp ngẫu nhiên tiến nhanh về vùng lân cận nghiệm tối ưu trong giai đoạn đầu, nhưng thường dao động và khó hội tụ chính xác khi đã đến gần nghiệm tối ưu. Ngược lại, phương pháp batch tiến chậm hơn ở giai đoạn đầu nhưng hội tụ ổn định và chính xác hơn về điểm tối ưu.

Hình dưới đây so sánh quá trình hội tụ của hai phương pháp trên bài toán [hồi quy logistic](https://en.wikipedia.org/wiki/Logistic_regression) không có chính quy hóa:

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter08/08_02_stochastic_vs_batch.png" alt="stochastic_vs_batch" width="80%" height="80%">
</p>
  <figcaption style="text-align: center;">[Fig 3] So sánh Batch vs Stochastic Gradient Descent [2]</figcaption>
</figure>

Khi mỗi hàm thành phần $$f_i$$ đều trơn, phần dao động còn lại của đường ngẫu nhiên quanh điểm tối ưu chính là sàn nhiễu mà các phương pháp giảm phương sai trong [26-05 SVRG và SAGA]({% multilang_post_url contents/chapter26/2026-09-15-26_05_variance_reduction %}) loại bỏ — mà không cần tính lại toàn bộ gradient batch ở mỗi bước.
