---
layout: post
title: 26-01 SGD và minibatch
chapter: '26'
order: 2
owner: Nguyen Le Linh
categories:
- chapter26
lang: vi
lesson_type: required
---

Năm 1951, Herbert Robbins và Sutton Monro xuất bản một bài báo thống kê ngắn chỉ 8 trang về xấp xỉ ngẫu nhiên — đặt nền móng toán học cho **Hạ gradient ngẫu nhiên (SGD)**. Hơn bảy thập kỷ sau, công thức một dòng $$w_{k+1} = w_k - \eta_k \nabla f_{I_k}(w_k)$$ ấy vẫn là nhịp tim của cả ngành học máy.

Điều thú vị nhất của SGD nằm ở sự cân bằng tinh tế của kích thước lô $$B$$ (minibatch size) và cách lấy mẫu: tăng $$B$$ giúp giảm phương sai nhiễu theo tỷ lệ $$1/B$$ và tận dụng tối đa năng lực song song của GPU, nhưng vượt quá ngưỡng bão hòa phần cứng, tăng $$B$$ lại khiến số bước cập nhật mỗi giây giảm đi. Thêm vào đó, trong thực tế hầu như ai cũng **xáo trộn dữ liệu không hoàn lại (random reshuffling)** thay vì lấy mẫu i.i.d. — và hóa ra toán học hiện đại đã chứng minh cách làm thực tế đó *nhanh hơn* lấy mẫu có hoàn lại!

## Kiến thức cần nhớ: Ba trụ cột của SGD và Minibatch

Để hiểu đúng cả định lý hội tụ lẫn cách chỉnh `batch_size` và `lr` khi huấn luyện mô hình, hãy nắm ba trụ cột sau:

- **Tính không chệch và Sàn phương sai (Unbiasedness & Variance Floor):** Với bước học cố định $$\eta$$, SGD hội tụ nhanh về một quả cầu bán kính tỉ lệ với $$\eta \sigma^2 / B$$ quanh nghiệm $$w^\star$$ rồi dừng lại ở "sàn nhiễu" đó. Muốn sai số tiến hẳn về $$0$$, ta buộc phải giảm dần $$\eta_k$$ theo điều kiện Robbins–Monro ($$\sum \eta_k = \infty,\; \sum \eta_k^2 < \infty$$).
- **Quy luật mở rộng tuyến tính theo kích thước lô (Batch Size Scaling):** Khi tăng kích thước lô lên $$B$$ lần (trong vùng nhiễu chiếm ưu thế), phương sai giảm $$B$$ lần, cho phép tăng tốc độ học lên tương ứng mà vẫn giữ ổn định động lực học — nhưng chỉ hiệu quả tới ngưỡng *kích thước lô tới hạn (critical batch size)*.
- **Xáo trộn không hoàn lại vs. Lấy mẫu i.i.d.:** Lấy mẫu không hoàn lại trong mỗi epoch tạo ra **tương quan âm** giữa các gradient liên tiếp trong cùng một epoch (nếu đầu epoch bốc phải mẫu lệch dương, cuối epoch chắc chắn sẽ bốc mẫu lệch âm để bù lại), giúp triệt tiêu sai số tích lũy nhanh hơn lấy mẫu i.i.d.

### Giải thích: Tính tay phương sai của Minibatch — có hoàn lại so với không hoàn lại

Giả sử tại điểm $$w_k$$ hiện tại, tập dữ liệu có $$n = 4$$ mẫu với 4 giá trị gradient vô hướng là $$1,\; 3,\; 5,\; 7$$. Gradient toàn lô chính xác là $$\mu = \frac{1 + 3 + 5 + 7}{4} = 4$$.

1. **SGD đơn mẫu ($$B = 1$$):**
   Bốn độ lệch so với $$\mu = 4$$ là $$-3,\; -1,\; +1,\; +3$$.
   Phương sai ước lượng là:
   $$\sigma^2 = \frac{(-3)^2 + (-1)^2 + 1^2 + 3^2}{4} = \frac{9 + 1 + 1 + 9}{4} = 5.0.$$
2. **Minibatch $$B = 2$$ lấy mẫu i.i.d. (có hoàn lại):**
   Hai mẫu độc lập có trung bình $$\bar{g}_2 = \frac{g_{I_1} + g_{I_2}}{2}$$, nên phương sai giảm đúng một nửa:
   $$\operatorname{Var}_{\text{i.i.d.}}(\bar{g}_2) = \frac{\sigma^2}{2} = \frac{5.0}{2} = 2.5.$$
3. **Minibatch $$B = 2$$ lấy mẫu không hoàn lại (xáo trộn thực tế):**
   Có đúng $$\binom{4}{2} = 6$$ cặp mẫu khác nhau có thể rút ra, với các trung bình cộng lần lượt là:
   $$\frac{1+3}{2}=2,\quad \frac{1+5}{2}=3,\quad \frac{1+7}{2}=4,\quad \frac{3+5}{2}=4,\quad \frac{3+7}{2}=5,\quad \frac{5+7}{2}=6.$$
   Phương sai trên 6 cặp này là:
   $$\operatorname{Var}_{\text{no-repl}}(\bar{g}_2) = \frac{(2-4)^2 + (3-4)^2 + 0^2 + 0^2 + (5-4)^2 + (6-4)^2}{6} = \frac{4 + 1 + 1 + 4}{6} = \frac{10}{6} \approx 1.667!$$
4. **Nhận xét:** Phương sai giảm hẳn từ $$2.5$$ xuống $$1.667$$ (bằng đúng hệ số hiệu chỉnh tổng thể hữu hạn $$\frac{n-B}{n-1} = \frac{4-2}{4-1} = \frac{2}{3}$$ nhân với $$2.5$$). Đó chính là lý do định lượng vì sao `shuffle=True` trong `DataLoader` luôn vượt trội lấy mẫu i.i.d.!

Hàm rủi ro thực nghiệm là trung bình cộng trên $$n$$ mẫu dữ liệu, và gradient của nó cũng có dạng trung bình tương ứng:

$$
\nabla F(w) = \frac{1}{n}\sum_{i=1}^n \nabla f_i(w).
$$

**Hạ gradient ngẫu nhiên (Stochastic Gradient Descent — SGD)** thay toàn bộ tổng trên bằng gradient tại một chỉ số ngẫu nhiên $$I_k$$ rút (có hoàn lại hoặc không hoàn lại) từ $$\{1,\ldots,n\}$$:

$$
w_{k+1} = w_k - \eta_k \nabla f_{I_k}(w_k).
$$

Nếu $$I_k$$ được chọn đều và độc lập với $$w_k$$, ước lượng gradient là **không chệch**: $$\mathbb{E}[\nabla f_{I_k}(w_k)\mid w_k]=\nabla F(w_k)$$. Một **minibatch** kích thước $$B$$ lấy trung bình trên $$B$$ mẫu như vậy. Khi các mẫu độc lập, phương sai của ước lượng giảm theo tỉ lệ $$1/B$$, trong khi thời gian tính mỗi bước tăng gần tuyến tính theo $$B$$ cho tới khi tận dụng hết năng lực song song của GPU. Đây là sự đánh đổi cơ bản khi chọn kích thước lô.

## Các tốc độ hội tụ cần nắm

Dưới các giả thiết chuẩn về tính Lipschitz và phương sai bị chặn, SGD trên hàm mục tiêu lồi Lipschitz với tốc độ học giảm dần $$\eta_k \propto 1/\sqrt{k}$$ (hoặc bước hằng kết hợp lấy trung bình điểm lặp) thỏa mãn:

$$
\mathbb{E}\bigl[F(\bar w_T)-F^\star\bigr] = O\bigl(\sigma / \sqrt{T}\bigr)
$$

theo số bước *ngẫu nhiên* $$T$$ (Bubeck, Chương 6). Với bài toán trơn và lồi mạnh, SGD có thể đạt tốc độ tuyến tính nếu nhiễu triệt tiêu tại điểm cực tiểu, nhưng mạng nơ-ron sâu nhìn chung không lồi mạnh. Bài học thực hành rút ra là: **nhiều bước cập nhật rẻ với gradient nhiễu thường đạt hiệu quả thực tế tốt hơn ít bước với gradient chính xác**.

Chương 06 đã so sánh GD và SGD trên tổng nhỏ; bạn có thể mở lại [stochastic_gradient_demo.html](https://nglelinh.github.io/interactive_math/optimization/stochastic_gradient_demo.html) để quan sát quỹ đạo nhiễu vẫn tiến đều về đáy.

## Xáo trộn dữ liệu so với lấy mẫu i.i.d.

Phân tích lý thuyết thường giả sử các chỉ số được rút độc lập cùng phân phối (i.i.d.). Tuy nhiên, trong thực hành người ta hầu như luôn dùng **xáo trộn ngẫu nhiên (random reshuffling)**: hoán vị toàn bộ $$n$$ mẫu ở đầu mỗi epoch rồi duyệt tuần tự không hoàn lại. Lấy mẫu không hoàn lại thường hội tụ nhanh hơn về mặt thực nghiệm và cũng là chủ đề nghiên cứu lý thuyết tích cực giai đoạn 2010–2020. Về mặt triển khai, nên xáo trộn lại dữ liệu ở mỗi epoch để tránh lặp cố định cùng một thứ tự.

## Minh họa với hồi quy logistic

```python
import numpy as np

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -40, 40)))

def sgd_logistic(X, y, eta=0.1, batch=16, epochs=20):
    n, d = X.shape
    w = np.zeros(d)
    for _ in range(epochs):
        idx = np.random.permutation(n)
        for s in range(0, n, batch):
            j = idx[s:s + batch]
            p = sigmoid(X[j] @ w)
            g = X[j].T @ (p - y[j]) / len(j)
            w -= eta * g
    return w
```

Hãy thử so sánh `batch=1`, `batch=16` và `batch=n` (gradient đầy đủ) trên một tập dữ liệu phân loại nhị phân theo thời gian thực thi (wall-clock time) cần để đạt cùng một mức hàm mất mát, chứ không chỉ đếm số epoch.

### SGD và minibatch trong khoảng 3 phút

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/sgd-minibatch_vi.mp4"></video>
</div>

Ví dụ m = 3 điểm: một bước GD so với một epoch SGD, bước hằng so với bước giảm dần, rồi ảnh hưởng của kích thước batch.

**Câu hỏi.** Nếu SGD thường dễ thoát khỏi các vùng trũng nông hơn so với GD toàn lô, nhận xét này nên ảnh hưởng thế nào đến cách chọn kích thước minibatch ban đầu cho một mô hình quá tham số hóa?
