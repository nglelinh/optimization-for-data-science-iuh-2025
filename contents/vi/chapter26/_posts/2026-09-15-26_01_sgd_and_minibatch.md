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


Rủi ro thực nghiệm là một trung bình. Gradient của nó cũng vậy:

$$
\nabla F(w) = \frac{1}{n}\sum_{i=1}^n \nabla f_i(w).
$$

**Hạ gradient ngẫu nhiên** thay tổng bằng một chỉ số ngẫu nhiên $$I_k$$ rút (có hoặc không hoàn lại) từ $$\{1,\ldots,n\}$$:

$$
w_{k+1} = w_k - \eta_k \nabla f_{I_k}(w_k).
$$

Nếu $$I_k$$ đều và độc lập với $$w_k$$, cập nhật là ước lượng **không chệch**: $$\mathbb{E}[\nabla f_{I_k}(w_k)\mid w_k]=\nabla F(w_k)$$. Một **minibatch** kích thước $$B$$ trung bình $$B$$ số hạng như vậy. Phương sai giảm như $$1/B$$ với các lần rút độc lập; thời gian tường mỗi bước tăng gần tuyến tính theo $$B$$ cho đến khi bão hòa GPU. Đó là đánh đổi nền tảng.

## Các tốc độ cần thuộc

Dưới giả thiết Lipschitz / phương sai bị chặn chuẩn, SGD trên mục tiêu lồi Lipschitz với bước $$\eta_k \propto 1/\sqrt{k}$$ (hoặc bước hằng rồi lấy trung bình) thỏa

$$
\mathbb{E}\bigl[F(\bar w_T)-F^\star\bigr] = O\bigl(\sigma / \sqrt{T}\bigr)
$$

theo số bước *ngẫu nhiên* (Bubeck, Ch. 6). Bài toán trơn lồi mạnh có thể đạt tốc độ tuyến tính nếu nhiễu tắt tại cực tiểu, nhưng mạng sâu không lồi mạnh. Thông điệp thực hành: **nhiều bước với gradient nhiễu thường thắng ít gradient chính xác**.

Chương 06 đã so GD và SGD trên tổng nhỏ. Mở lại [stochastic_gradient_demo.html](https://nglelinh.github.io/interactive_math/optimization/stochastic_gradient_demo.html) và xem một quỹ đạo nhiễu vẫn xuôi dốc.

## Xáo trộn so với i.i.d.

Lý thuyết thích mẫu độc lập. Thực hành dùng **xáo lại ngẫu nhiên**: hoán vị $$n$$ mẫu mỗi epoch rồi đi hết hoán vị. Vòng không hoàn lại thường hội tụ nhanh hơn trên thực nghiệm; chứng minh là chủ đề nghiên cứu 2010–2020. Với môn này: xáo mỗi epoch, đừng tái sử dụng cùng thứ tự (dễ tuần hoàn).

## Một vòng logistic nhỏ

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

So `batch=1`, `batch=16`, và `batch=n` (gradient đầy đủ) trên một đám mây hai lớp: thời gian tường tới một mất mát huấn luyện cố định, không chỉ số epoch.

**Câu hỏi.** Nếu SGD thường thoát lưu vực nông giỏi hơn GD cả lô, điều đó nên ảnh hưởng thế nào tới lựa chọn batch size đầu tiên trên mô hình quá tham số?
