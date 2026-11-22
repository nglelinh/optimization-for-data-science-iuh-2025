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
