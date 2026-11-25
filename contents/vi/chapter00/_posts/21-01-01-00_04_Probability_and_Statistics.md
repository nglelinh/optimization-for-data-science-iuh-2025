---
layout: post
title: 00-04 Xác Suất và Thống Kê
chapter: '00'
order: 14
owner: AI Assistant
categories:
- chapter00
lang: vi
lesson_type: required
---

Trong thế giới lý tưởng của sách giáo khoa cổ điển, mọi hệ số trong hàm mục tiêu và ràng buộc đều biết chính xác tuyệt đối. Nhưng trong khoa học dữ liệu và kỹ thuật hiện đại, dữ liệu luôn kèm nhiễu đo đạc, nhu cầu thị trường biến động ngẫu nhiên và ta chỉ quan sát được một mẫu hữu hạn. Lúc ấy, **xác suất và thống kê** bước vào, biến bài toán học từ dữ liệu thành một bài toán tối ưu hóa trên hàm kỳ vọng hoặc hàm hợp lý.

Phần 00-04 mở ra chiếc cầu nối giữa mô hình xác suất (như phân phối Gauss, Laplace, Bernoulli) với các hàm mất mát quen thuộc trong tối ưu hóa lồi (MSE, MAE, Cross-Entropy, Ridge, Lasso).

## Kiến thức cần nhớ: Xác suất gặp Tối ưu hóa ở đâu?

- **Tối ưu hóa rủi ro kỳ vọng và rủi ro thực nghiệm (ERM):** Ta muốn cực tiểu hóa tổn thất kỳ vọng $$\mathbb{E}[\ell(x, \xi)]$$ nhưng chỉ có $$N$$ mẫu dữ liệu, nên thay bằng trung bình mẫu $$\frac{1}{N}\sum_{i=1}^N \ell(x, \xi_i)$$ — bài toán tối ưu hóa tổng hữu hạn kinh điển.
- **Ước lượng hợp lý tối đa (MLE) và hậu nghiệm tối đa (MAP):** Cực đại hóa xác suất quan sát được dữ liệu tương đương cực tiểu hóa **âm log-hợp lý** (negative log-likelihood). Thêm phân phối tiên nghiệm (prior) sinh ra đúng số hạng điều chuẩn (regularization) trong tối ưu hóa!
- **Bất đẳng thức Jensen và tính lồi:** Cho hàm lồi $$f$$, $$f(\mathbb{E}[X]) \le \mathbb{E}[f(X)]$$. Đây là cầu nối vàng giữa xác suất và tối ưu hóa lồi, xuất hiện trong phân kỳ KL, thuật toán EM và suy luận biến phân.
- **Tối ưu hóa ngẫu nhiên (Stochastic Optimization):** Khi $$N$$ lên tới hàng triệu, tính gradient đầy đủ quá tốn kém; ta ước lượng gradient không chệch từ một mini-batch ngẫu nhiên (SGD).

### Giải thích: Tại sao chọn hàm mất mát $$\ell_2$$ ra Trung bình, còn $$\ell_1$$ ra Trung vị?

Giả sử bạn thu thập $$4$$ phép đo nhiệt độ có một giá trị nhiễu mạnh: $$y = (2, 4, 5, 9)$$, và muốn chọn một con số đại diện $$\theta$$ tốt nhất:

1. **Cực tiểu hóa sai số bình phương ($$\ell_2$$):**
   $$L_2(\theta) = \frac{1}{4}\left[(2-\theta)^2 + (4-\theta)^2 + (5-\theta)^2 + (9-\theta)^2\right].$$
   Lấy đạo hàm theo $$\theta$$ và cho bằng $$0$$:
   $$L_2'(\theta) = -\frac{1}{2}\left[(2-\theta) + (4-\theta) + (5-\theta) + (9-\theta)\right] = 0 \implies 4\theta = 20 \implies \theta_2^* = 5.$$
   Nghiệm tối ưu chính là **trung bình cộng** (bị điểm ngoại lai $$9$$ kéo mạnh lên $$5$$).
2. **Cực tiểu hóa sai số tuyệt đối ($$\ell_1$$):**
   $$L_1(\theta) = \frac{1}{4}\left(|2-\theta| + |4-\theta| + |5-\theta| + |9-\theta|\right).$$
   Thử tính trực tiếp:
   - Tại $$\theta = 4$$: $$L_1(4) = \frac{1}{4}(2 + 0 + 1 + 5) = 2$$.
   - Tại $$\theta = 4.5$$: $$L_1(4.5) = \frac{1}{4}(2.5 + 0.5 + 0.5 + 4.5) = 2$$.
   - Tại $$\theta = 5$$: $$L_1(5) = \frac{1}{4}(3 + 1 + 0 + 4) = 2$$.
   - Tại $$\theta = 6$$: $$L_1(6) = \frac{1}{4}(4 + 2 + 1 + 3) = 2.5 > 2$$.
   Mọi điểm **trung vị** $$\theta_1^* \in [4, 5]$$ đều đạt cực tiểu $$2$$, và dù điểm ngoại lai $$9$$ tăng lên $$900$$, tập nghiệm tối ưu $$[4, 5]$$ vẫn hoàn toàn bất biến!

---

## Xác suất và thống kê cho tối ưu hóa lồi

Xác suất và thống kê là nền tảng thiết yếu để hiểu nhiều bài toán tối ưu hóa, đặc biệt trong học máy và khoa học dữ liệu. Phần này giới thiệu các khái niệm xác suất cốt lõi thường xuất hiện trong tối ưu hóa lồi, từ ước lượng hợp lý tối đa đến tối ưu hóa Bayes.

### Vì sao xác suất quan trọng trong tối ưu hóa

Nhiều bài toán tối ưu hóa bắt nguồn trực tiếp từ mô hình hóa thống kê:

- **Ước lượng hợp lý tối đa (MLE)**: tìm bộ tham số làm cực đại hàm hợp lý (likelihood) của dữ liệu quan sát.
- **Tối ưu hóa Bayes**: sử dụng mô hình xác suất để định hướng quá trình tìm kiếm nghiệm tối ưu.
- **Tối ưu hóa ngẫu nhiên**: xử lý tính bất định và nhiễu ngẫu nhiên trong hàm mục tiêu hoặc ràng buộc.
- **Điều chuẩn (Regularization)**: bổ sung phân phối tiên nghiệm (prior) nhằm hạn chế quá khớp (overfitting).
- **Cực tiểu hóa rủi ro**: cực tiểu hóa giá trị kỳ vọng của hàm mất mát trên một phân phối xác suất.

### Các chủ đề chính

1. **Lý thuyết xác suất cơ bản**: không gian mẫu, biến cố và các tiên đề xác suất.
2. **Các phân phối xác suất thông dụng**: phân phối chuẩn, phân phối mũ và các phân phối quan trọng khác.
3. **Kỳ vọng và phương sai**: tính toán và tối ưu hóa giá trị kỳ vọng.
4. **Định lý Bayes**: cơ sở của suy luận và tối ưu hóa Bayes.
5. **Ước lượng thống kê**: kết nối lý thuyết xác suất với bài toán tối ưu hóa.

### Kết nối với tối ưu hóa lồi

Nắm vững xác suất giúp bạn:

- **Xây dựng mô hình bài toán**: chuyển đổi tính bất định trong thực tế thành bài toán tối ưu hóa toán học.
- **Lựa chọn hàm mục tiêu**: chọn hàm mất mát phù hợp dựa trên các giả định xác suất về dữ liệu.
- **Diễn giải kết quả**: hiểu rõ khoảng tin cậy và ý nghĩa thống kê của nghiệm tìm được.
- **Xử lý nhiễu**: ứng phó hiệu quả với sai số đo lường và các quá trình ngẫu nhiên.
- **Thiết kế thuật toán**: xây dựng các phương pháp tối ưu hóa ổn định trước tính bất định.

Nền tảng này sẽ được sử dụng trực tiếp ở các chương sau khi ta phân tích cách các mô hình xác suất dẫn đến bài toán tối ưu hóa lồi trong học máy, thống kê và kỹ thuật.

<div style="background: #e8f4fd; padding: 15px; border-left: 4px solid #2196F3; margin: 20px 0;">
<strong>💡 Lộ trình học:</strong> Bắt đầu từ các khái niệm xác suất cơ bản, sau đó tìm hiểu cách chúng gắn với tối ưu hóa qua ước lượng hợp lý tối đa và phương pháp Bayes. Mỗi bài học kế tiếp giúp làm rõ cách tính bất định và yếu tố ngẫu nhiên hình thành nên các bài toán tối ưu hóa.
</div>
