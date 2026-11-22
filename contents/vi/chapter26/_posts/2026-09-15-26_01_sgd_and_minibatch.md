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

**Câu hỏi.** Nếu SGD thường dễ thoát khỏi các vùng trũng nông hơn so với GD toàn lô, nhận xét này nên ảnh hưởng thế nào đến cách chọn kích thước minibatch ban đầu cho một mô hình quá tham số hóa?
