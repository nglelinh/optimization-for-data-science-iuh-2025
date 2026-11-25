---
layout: post
title: 14-07 So sánh với phương pháp bậc nhất
chapter: '14'
order: 15
owner: Minjoo Lee
categories:
- chapter14
lang: vi
---

Nếu phương pháp Newton hội tụ nhanh gấp hàng trăm, hàng nghìn lần Gradient Descent, tại sao ngày nay thế giới học sâu (Deep Learning) vẫn huấn luyện các mô hình tỷ tham số chủ yếu bằng các phương pháp bậc nhất như SGD và Adam? Câu trả lời không nằm ở *số vòng lặp*, mà nằm ở **chi phí trên mỗi vòng lặp** và **bộ nhớ lưu trữ**.

Bài học này đặt Phương pháp Newton và Gradient Descent lên bàn cân định lượng theo số chiều $$n$$ — từ bộ nhớ, độ phức tạp tính toán mỗi bước, độ nhạy với số điều kiện, cho đến khả năng mở rộng lên bài toán lớn. Hiểu rõ sự đánh đổi này sẽ giúp bạn chọn đúng vũ khí cho từng quy mô bài toán thực tế.

## Bản đồ kiến thức nền: Bốn trục so sánh giữa Bậc nhất và Bậc hai

- **Bộ nhớ lưu trữ:** Gradient Descent chỉ cần lưu vectơ $$x$$ và gradient $$\nabla f(x)$$ — tốn $$O(n)$$. Phương pháp Newton phải lưu ma trận Hessian $$n \times n$$ — tốn $$O(n^2)$$. Với $$n = 10^6$$ biến, riêng ma trận Hessian đã ngốn hàng terabyte RAM!
- **Chi phí mỗi vòng lặp:** GD tốn $$O(n)$$ (hoặc chi phí tính 1 lần gradient). Newton phải giải hệ tuyến tính $$H v = -g$$ — tốn $$O(n^3)$$ với ma trận đặc (có thể giảm xuống $$O(n)$$ hoặc $$O(n^{1.5})$$ nếu Hessian thưa có cấu trúc).
- **Tốc độ hội tụ và độ chính xác:** GD hội tụ tuyến tính (hoặc dưới tuyến tính), rất nhạy với số điều kiện $$\kappa = L/m$$; cần $$O(\kappa \log(1/\epsilon))$$ bước. Newton hội tụ bậc hai gần nghiệm, bất biến affine, hầu như không phụ thuộc $$\kappa$$ và đạt $$\epsilon = 10^{-12}$$ chỉ sau 5–15 bước.
- **Quy tắc chọn nhanh trong thực hành:** $$n \le 10^3$$–$$10^4$$ và cần độ chính xác cao (tài chính, điều khiển, quy hoạch lồi) → chọn **Newton**. $$n \ge 10^5$$–$$10^9$$ và chỉ cần độ chính xác vừa phải (học sâu, dữ liệu lớn) → chọn **bậc nhất** (hoặc L-BFGS / xấp xỉ bậc hai).

### Khung giải thích (nên đọc chậm): Tính toán chi phí thực tế bằng con số ở hai quy mô $$n = 100$$ và $$n = 100{,}000$$

Giả sử bài toán lồi mạnh có số điều kiện xấu $$\kappa = 10^4$$ và yêu cầu sai số $$\epsilon = 10^{-8}$$.
- Số bước GD ước lượng: $$k_{\text{GD}} \approx \kappa \ln(1/\epsilon) \approx 10^4 \times 18.4 \approx 184{,}000$$ bước (mỗi bước tốn cỡ $$c_1 n^2$$ phép tính nếu có ma trận dữ liệu đặc, hoặc $$O(n)$$ cho hàm tách biến; giả sử đơn giản mỗi bước GD tốn $$10n$$ phép tính, còn giải Cholesky bước Newton tốn $$\frac{1}{3}n^3$$ phép tính).
- Số bước Newton ước lượng: $$k_{\text{NT}} \approx 15$$ bước.

Hãy so sánh tổng số phép tính dấu phẩy động (FLOPs):

1. **Ở quy mô nhỏ $$n = 100$$:**
   - **GD:** $$184{,}000 \times (10 \times 100) \approx 1.84 \times 10^8$$ FLOPs.
   - **Newton:** $$15 \times \frac{1}{3}(100)^3 = 5 \times 10^6$$ FLOPs — **nhanh hơn GD gần 37 lần**, bộ nhớ Hessian chỉ $$100^2 \times 8\text{ B} = 80\text{ KB}$$!
2. **Ở quy mô lớn $$n = 100{,}000$$ (ma trận Hessian đặc):**
   - **GD:** $$184{,}000 \times (10 \times 10^5) \approx 1.84 \times 10^{11}$$ FLOPs (chạy vài giây), bộ nhớ chỉ vài MB.
   - **Newton đặc:** $$15 \times \frac{1}{3}(10^5)^3 = 5 \times 10^{15}$$ FLOPs (chạy hàng ngày!), bộ nhớ Hessian là $$(10^5)^2 \times 8\text{ B} = 80\text{ GB}$$ RAM — **không khả thi nếu không khai thác độ thưa hoặc dùng Quasi-Newton!**

---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
    });
</script>

Trong mục này, ta so sánh tổng quát giữa phương pháp Newton và gradient descent trên miền xác định có số chiều $$n$$.

| Tiêu chí | Phương pháp Newton | Gradient descent |
| -------- | -------- | -------- |
| Bộ nhớ | $$O(n^{2})$$ (lưu trữ ma trận Hessian cỡ $$n \times n$$) | $$O(n)$$ (lưu trữ vector gradient $$n$$ chiều) |
| Chi phí tính toán mỗi bước | $$O(n^{3})$$ phép tính (giải hệ tuyến tính cỡ $$n \times n$$) | $$O(n)$$ phép tính (cộng vector $$n$$ chiều) |
| Tìm kiếm đường backtracking | $$O(n)$$ | $$O(n)$$ |
| Độ nhạy với số điều kiện (conditioning) | Bất biến affine, không phụ thuộc số điều kiện của hệ tọa độ | Chịu ảnh hưởng mạnh bởi số điều kiện |
| Độ ổn định triển khai | Nhạy cảm hơn với lỗi cài đặt và sai số số học | Ổn định hơn phương pháp Newton |

## Ví dụ

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter14/gd(1).jpeg" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] Hồi quy logistic [3]</figcaption>
</p>
</figure>

Hình 1 biểu diễn lại ví dụ hồi quy logistic ở mục [14-04]({% multilang_post_url contents/chapter14/2021-03-26-14_04_backtracking_line_search %}) nhưng với trục hoành là thời gian tính toán thực tế. Theo phân tích lý thuyết, phương pháp Newton gồm hai giai đoạn: ở giai đoạn giảm chấn ban đầu, mức giảm sai số theo từng bước tương đương gradient descent nhưng chi phí mỗi bước là $$O(n^{3})$$ nên thời gian chạy thực tế có thể chậm hơn; khi bước vào giai đoạn thuần túy (backtracking không còn cần thu nhỏ bước), phương pháp đạt hội tụ bậc hai và giảm sai số rất nhanh.

### Tự tay thử: Newton so với gradient descent

<div class="opx-explainer" data-opx="newton" data-lang="vi"></div>
