---
layout: post
title: 26-03 AdaGrad, trực giác RMSProp, và Adam
chapter: '26'
order: 4
owner: Nguyen Le Linh
categories:
- chapter26
lang: vi
lesson_type: required
---


Không phải mọi tọa độ của vector tham số $$w$$ đều nên dùng chung một tốc độ học vô hướng $$\eta$$. Các đặc trưng ít xuất hiện (chẳng hạn vector one-hot của từ hiếm) cần bước cập nhật hiệu dụng lớn hơn, trong khi các tọa độ thường xuyên có gradient lớn sẽ dễ phân kỳ nếu dùng cùng mức $$\eta$$. Các **phương pháp thích nghi đường chéo** giải quyết vấn đề này bằng cách duy trì ước lượng mô-men bậc hai của gradient cho từng tọa độ và chia bước cập nhật cho căn bậc hai của ước lượng đó.

**AdaGrad** (Duchi, Hazan, Singer, 2011) cộng dồn bình phương gradient theo từng phần tử:

$$
G_{k+1} = G_k + g_k \odot g_k, \qquad w_{k+1} = w_k - \eta\, g_k \oslash \bigl(\sqrt{G_{k+1}}+\varepsilon\bigr),
$$

trong đó $$g_k=\nabla f_{I_k}(w_k)$$, còn $$\odot$$ và $$\oslash$$ lần lượt là phép nhân và phép chia theo từng phần tử. Vì tổng $$G_k$$ chỉ tăng mà không quên quá khứ, tốc độ học hiệu dụng **giảm đơn điệu** về 0. Điều này rất phù hợp với các bài toán lồi có đặc trưng thưa, nhưng lại gây đình trệ khi huấn luyện mạng nơ-ron sâu qua nhiều vòng lặp.

**RMSProp** (Hinton, bài giảng trực tuyến) khắc phục nhược điểm trên bằng cách thay tổng tích lũy bằng trung bình trượt mũ (EMA): $$v_{k+1}=\gamma v_k + (1-\gamma)\,g_k\odot g_k$$, cho phép hệ số tỉ lệ thích nghi linh hoạt theo độ lớn gradient gần đây.

**Adam** (Kingma & Ba, 2015) kết hợp trung bình trượt mũ của mô-men bậc hai (như RMSProp) với trung bình trượt mũ của mô-men bậc nhất (như momentum), đồng thời bổ sung hệ số hiệu chỉnh chệch vì cả hai đại lượng đều khởi tạo từ $$0$$:

$$
\begin{align}
m_{k+1} &= \beta_1 m_k + (1-\beta_1) g_k, \\
v_{k+1} &= \beta_2 v_k + (1-\beta_2)\, g_k\odot g_k, \\
\hat m &= m_{k+1}/(1-\beta_1^{k+1}), \quad
\hat v = v_{k+1}/(1-\beta_2^{k+1}), \\
w_{k+1} &= w_k - \eta\, \hat m \oslash (\sqrt{\hat v}+\varepsilon).
\end{align}
$$

Bộ tham số mặc định $$\beta_1=0.9$$, $$\beta_2=0.999$$, $$\varepsilon=10^{-8}$$ hoạt động ổn định trên rất nhiều bài toán, dù vẫn cần điều chỉnh khi huấn luyện các mô hình đặc thù. Về bản chất, Adam là **tiền điều kiện đường chéo kết hợp momentum**, không phải phương pháp bậc hai vì nó không xây dựng hay xấp xỉ đầy đủ ma trận Hessian.

```python
def adam_step(g, m, v, k, eta=1e-3, b1=0.9, b2=0.999, eps=1e-8):
    m = b1 * m + (1 - b1) * g
    v = b2 * v + (1 - b2) * (g * g)
    mhat = m / (1 - b1 ** (k + 1))
    vhat = v / (1 - b2 ** (k + 1))
    return mhat * eta / (vhat ** 0.5 + eps), m, v
```

Tham khảo bài báo gốc tại [arXiv:1412.6980](https://arxiv.org/abs/1412.6980). Bài tiếp theo sẽ phân tích vì sao việc cộng số hạng phạt $$(\lambda/2)\|w\|_2^2$$ vào hàm mất mát **không** tương đương với suy giảm trọng số (weight decay) trong AdamW.
