---
layout: post
title: 26-05 Giảm phương sai — SVRG và SAGA
chapter: '26'
order: 6
owner: Nguyen Le Linh
categories:
- chapter26
lang: vi
lesson_type: required
---


Giới hạn $$O(1/\sqrt{T})$$ của SGD trên bài toán tổng hữu hạn lồi Lipschitz không phải là giới hạn bất khả kháng của lớp bài toán này. Đó là hệ quả của việc sử dụng gradient *không chệch nhưng vẫn còn nhiễu* với phương sai không triệt tiêu ngay cả khi $$w$$ đã tới sát điểm cực tiểu. Các phương pháp **giảm phương sai (variance reduction)** tái sử dụng các gradient đã tính trước đó (tại một điểm mốc hoặc trong một bảng lưu trữ) để làm cho nhiễu ước lượng tiến về 0 khi $$w \to w^\star$$. Bài này trình bày hai thuật toán nền tảng là SVRG và SAGA: đủ chi tiết đại số để hiểu *vì sao* phương sai triệt tiêu, đủ rõ ràng để tự cài đặt, và xác định ranh giới thực tế về phạm vi áp dụng của chúng.

Bạn có thể xem lại [26-01]({% multilang_post_url contents/chapter26/2026-09-15-26_01_sgd_and_minibatch %}), phần so sánh toàn lô và ngẫu nhiên ở [08-02-04]({% multilang_post_url contents/chapter08/20-03-29-08_02_04_batch_vs_stochastic_methods %}) và mô phỏng [stochastic_gradient_demo.html](https://nglelinh.github.io/interactive_math/optimization/stochastic_gradient_demo.html) để quan sát quỹ đạo SGD vẫn dao động xung quanh đáy sau khi đã tiến vào vùng lân cận nghiệm: phần dao động dư này chính là vấn đề mà giảm phương sai giải quyết.

## Bài toán tổng hữu hạn và giới hạn của SGD

Hàm rủi ro thực nghiệm là trung bình trên $$n$$ hàm thành phần:

$$
F(w)=\frac{1}{n}\sum_{i=1}^n f_i(w),\qquad
\nabla F(w)=\frac{1}{n}\sum_{i=1}^n \nabla f_i(w).
$$

Một bước SGD đơn mẫu sử dụng $$g_k=\nabla f_{I_k}(w_k)$$. Nếu $$I_k$$ rút đều và độc lập với $$w_k$$ thì $$\mathbb{E}[g_k\mid w_k]=\nabla F(w_k)$$, nhưng phương sai:

$$
\mathbb{E}\bigl[\|g_k-\nabla F(w_k)\|_2^2\mid w_k\bigr]
$$

không nhất thiết tiến về 0 khi $$w_k\to w^\star$$. Ngay tại điểm tối ưu toàn cục $$w^\star$$, từng gradient thành phần $$\nabla f_i(w^\star)$$ vẫn có thể khác 0 và chỉ có *trung bình* của chúng bằng 0 (ví dụ trong hồi quy tuyến tính có nhiễu quan sát). Vì sàn nhiễu khác 0, SGD với bước hằng chỉ dao động trong một hình cầu bán kính tỉ lệ với $$\eta\sigma$$ quanh $$w^\star$$, còn muốn hội tụ chính xác phải giảm tốc độ học nên tốc độ dừng ở $$O(1/\sqrt{T})$$ (hoặc $$O(1/T)$$ khi lồi mạnh).

Gradient descent toàn lô đạt hội tụ tuyến tính dưới tính lồi mạnh (Chương 06), nhưng mỗi bước tốn $$n$$ lượt tính gradient. Giảm phương sai hướng tới mục tiêu đạt tốc độ hội tụ tuyến tính với chi phí phân bổ chỉ cỡ một vài gradient mỗi bước.

## Ý tưởng biến kiểm soát (control variate)

Chọn một điểm mốc (snapshot) $$\tilde w$$ tại đó ta chấp nhận tính *một lần* gradient đầy đủ $$\mu=\nabla F(\tilde w)$$. Với chỉ số ngẫu nhiên $$I$$, xét ước lượng:

$$
g(w)=\nabla f_I(w)-\nabla f_I(\tilde w)+\mu.
$$

Ước lượng này vẫn không chệch đối với $$\nabla F(w)$$:

$$
\mathbb{E}[g(w)]
=\nabla F(w)-\nabla F(\tilde w)+\nabla F(\tilde w)
=\nabla F(w).
$$

Khi $$w=\tilde w$$, ta có $$g(\tilde w)=\mu=\nabla F(\tilde w)$$ *chính xác*, nghĩa là phương sai bằng 0 tại điểm mốc. Khi $$w$$ gần $$\tilde w$$ và mỗi $$\nabla f_i$$ liên tục Lipschitz, hiệu $$\nabla f_I(w)-\nabla f_I(\tilde w)$$ nhỏ, kéo theo phương sai của $$g(w)$$ nhỏ. Đây chính là kỹ thuật **biến kiểm soát**: trừ đi một thành phần nhiễu có tương quan cao rồi cộng bù lại đúng kỳ vọng của nó.

## SVRG (Johnson & Zhang, 2013)

SVRG định kỳ cập nhật điểm mốc ở vòng lặp ngoài và sử dụng ước lượng biến kiểm soát ở vòng lặp trong.

**Vòng ngoài** $$s=0,1,\ldots,S-1$$:

1. Lưu điểm mốc $$\tilde w\leftarrow w$$ và tính gradient đầy đủ $$\mu\leftarrow\nabla F(\tilde w)$$ (tốn $$n$$ gradient thành phần).
2. **Vòng trong** $$t=0,1,\ldots,m-1$$: rút đều chỉ số $$I$$ và cập nhật:
   $$
   g\leftarrow\nabla f_I(w)-\nabla f_I(\tilde w)+\mu,\qquad
   w\leftarrow w-\eta g.
   $$
3. Chọn điểm khởi đầu cho vòng ngoài tiếp theo (bằng trung bình các điểm lặp trong hoặc giữ nguyên $$w$$ cuối cùng), rồi quay lại bước 1.

Với lựa chọn phổ biến $$m=\Theta(n)$$, chi phí *phân bổ* cho mỗi bước trong chỉ tương đương một hằng số nhỏ (khoảng 3 lượt tính gradient thành phần: 1 lượt phân bổ từ gradient đầy đủ và 2 lượt trong vòng trong). Bộ nhớ phụ chỉ gồm một điểm mốc $$\tilde w$$ và một vector $$\mu$$, tức $$O(d)$$, không phụ thuộc số mẫu $$n$$.

<div class="textbook-theorem" markdown="1">
<strong>Định lý (phác thảo cho tổng hữu hạn lồi mạnh).</strong> Nếu mỗi $$f_i$$ trơn-$$L$$ và $$F$$ lồi mạnh-$$\mu$$, thì với bước hằng $$\eta$$ đủ nhỏ và độ dài vòng trong $$m\gtrsim L/\mu$$, thuật toán thỏa mãn:

$$
\mathbb{E}\bigl[F(\tilde w_{s+1})-F^\star\bigr]
\le \rho\,\mathbb{E}\bigl[F(\tilde w_s)-F^\star\bigr]
$$

với hằng số $$\rho<1$$. Tổng số lượt tính gradient thành phần để đạt sai số $$\varepsilon$$ là $$O\bigl((n+\kappa)\log(1/\varepsilon)\bigr)$$, trong đó $$\kappa=L/\mu$$. SGD thuần túy không đạt được tốc độ $$\log(1/\varepsilon)$$ này khi sàn nhiễu dương.
</div>

Ý tưởng chứng minh dựa trên hàm Lyapunov: phương sai ở vòng trong bị chặn bởi khoảng cách $$\|w-\tilde w\|$$, và khoảng cách này co dần khi điểm mốc $$\tilde w$$ tiến gần $$w^\star$$. Điều quan trọng nhất cần nắm vững là cơ chế tại công thức $$g=\nabla f_I(w)-\nabla f_I(\tilde w)+\mu$$ giải thích vì sao phương sai giảm về 0.

## SAGA (Defazio, Bach, Lacoste-Julien, 2014)

SAGA loại bỏ bước tính gradient đầy đủ định kỳ bằng cách duy trì một **bảng** $$g^{(1)},\ldots,g^{(n)}$$ lưu gradient gần nhất của từng hàm thành phần $$f_i$$. Khởi tạo $$g^{(i)}\leftarrow\nabla f_i(w_0)$$ (hoặc khởi tạo bằng 0 kèm giai đoạn làm nóng ngắn) và lưu sẵn trung bình cộng $$\bar g=\frac1n\sum_i g^{(i)}$$.

Ở mỗi bước: rút chỉ số $$I$$, tính gradient mới $$\nabla f_I(w)$$, tạo ước lượng:

$$
g\leftarrow \nabla f_I(w)-g^{(I)}+\bar g,
$$

cập nhật bảng $$g^{(I)}\leftarrow\nabla f_I(w)$$, cập nhật trung bình $$\bar g$$ trong $$O(d)$$ bằng phép cộng trừ một phần tử, rồi cập nhật tham số $$w\leftarrow w-\eta g$$.

Về bản chất, đây là cùng công thức biến kiểm soát nhưng dùng các điểm mốc *cũ riêng cho từng mẫu* thay vì một điểm mốc chung $$\tilde w$$. Đổi lại cho việc bỏ vòng tính gradient đầy đủ là chi phí bộ nhớ $$O(nd)$$ cho $$n$$ vector gradient — hoặc rút xuống $$O(n)$$ số vô hướng với các mô hình tuyến tính (do $$\nabla f_i(w)=(x_i^\top w-y_i)x_i$$ chỉ cần lưu phần dư vô hướng). Chính vì vậy `sklearn.linear_model.LogisticRegression(solver="saga")` rất hiệu quả trên bài toán ERM lồi cỡ vừa, nhưng SAGA không khả thi cho *mạng nơ-ron sâu* quy mô lớn như ImageNet do không thể lưu bảng gradient cho mọi mẫu.

**SAG** (Schmidt, Le Roux, Bach) là phiên bản tiền nhiệm có chệch: thuật toán dùng trực tiếp trung bình bảng đã cập nhật (tức chỉ nhân phần hiệu chỉnh $$\nabla f_I(w)-g^{(I)}$$ với hệ số $$1/n$$ thay vì hệ số $$1$$). Việc dùng hệ số $$1$$ trong SAGA khôi phục tính không chệch và giúp phân tích lý thuyết gọn gàng hơn.

## Minh họa cài đặt SVRG

```python
import numpy as np

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -40.0, 40.0)))

def svrg_logistic(X, y, lam=1e-3, eta=0.1, inner=None, epochs=20):
    n, d = X.shape
    inner = n if inner is None else inner
    w = np.zeros(d)
    for _ in range(epochs):
        p = sigmoid(X @ w)
        mu = X.T @ (p - y) / n + lam * w          # gradient đầy đủ
        w_snap = w.copy()
        for _t in range(inner):
            i = np.random.randint(n)
            xi, yi = X[i], y[i]
            g = (sigmoid(xi @ w) - yi) * xi + lam * w
            g_snap = (sigmoid(xi @ w_snap) - yi) * xi + lam * w_snap
            w = w - eta * (g - g_snap + mu)
    return w
```

Hãy so sánh thời gian thực thi (không chỉ số epoch) giữa đoạn mã trên và SGD minibatch ở mục 26-01 trên bài toán hồi quy logistic có chính quy hóa $$\ell_2$$ (lồi mạnh) với $$n=5000$$ để đạt $$\|\nabla F(w)\|_2\le 10^{-4}$$. Sau đó thử cùng bài toán trên mạng nơ-ron có một lớp ẩn: chi phí tính điểm mốc đầy đủ đòi hỏi $$n$$ lượt lan truyền ngược, bảng gradient của SAGA vượt quá bộ nhớ, và AdamW ở mục 26-04 trở nên thực tế hơn nhiều.

## Bảng so sánh phạm vi sử dụng

| Phương pháp | Bộ nhớ phụ | Chi phí phân bổ mỗi bước | Phạm vi phù hợp | Hội tụ tuyến tính trên tổng hữu hạn lồi mạnh? |
|-------------|------------|--------------------------|-----------------|-----------------------------------------------|
| SGD / mini-batch | không | $$1$$ (hoặc $$B$$) gradient | học sâu | không (do sàn nhiễu) |
| SVRG | một điểm mốc + $$\mu$$ | $$\approx 3$$ gradient | tổng hữu hạn lồi, nghiên cứu | có |
| SAGA | một gradient mỗi mẫu | $$1$$ gradient | ERM lồi cỡ vừa (`solver="saga"`) | có |
| AdamW | hai trung bình trượt mũ | $$1$$ minibatch | mặc định cho học sâu | không phải mục tiêu thiết kế |

Nắm vững SVRG và SAGA giúp nhận diện rõ những bài toán ERM *lồi* (hồi quy logistic, SVM tuyến tính, các dạng Lasso làm trơn) mà ta không nên mặc định dùng Adam. Ngược lại, Adam theo minibatch vẫn vượt trội trên mạng nơ-ron sâu vì ba lý do: (i) chi phí tính hoặc lưu gradient đầy đủ quá lớn, (ii) hàm mất mát không lồi mạnh, và (iii) phần cứng GPU tối ưu cho phép nhân ma trận theo lô lớn thay vì cập nhật đơn mẫu trừ điểm mốc.

Một số hướng liên quan (không kiểm tra): **SARAH** và **SPIDER** thay biến kiểm soát bằng ước lượng đệ quy giúp cải thiện cận lý thuyết; còn **FedAvg** ở Chương 29 *không* phải giảm phương sai (vì chỉ lấy trung bình trọng số), mặc dù biến kiểm soát trong thuật toán SCAFFOLD có thể xem là phiên bản học liên kết của SVRG.

**Bài tập 1.** Chứng minh tính không chệch của ước lượng SVRG trong một dòng, sau đó xây dựng một hàm bậc hai gồm hai thành phần sao cho phương sai của SGD thuần tại $$w^\star$$ dương trong khi phương sai của SVRG tại điểm mốc $$\tilde w = w^\star$$ bằng 0.

**Bài tập 2.** Trên bài toán hồi quy logistic chính quy hóa ridge với $$n=5000$$, vẽ chuẩn gradient theo *tổng số lượt tính gradient thành phần $$f_i$$* cho SGD, SVRG và SAGA (nếu đủ bộ nhớ), đánh dấu các thời điểm tính điểm mốc của SVRG. Tiếp theo, vẽ lại các đường này theo thời gian thực thi (wall-clock time) và quan sát xem thứ tự hiệu năng giữa các phương pháp có thay đổi hay không.

**Câu hỏi.** Ước lượng biến kiểm soát $$g$$ là không chệch với mọi $$w$$, không riêng tại $$\tilde w$$. Vậy tại sao vẫn cần định kỳ cập nhật điểm mốc $$\tilde w$$ — điều gì sẽ xảy ra với $$\mathrm{Var}(g)$$ nếu giữ cố định $$\tilde w$$ khi $$w$$ di chuyển ra xa?
