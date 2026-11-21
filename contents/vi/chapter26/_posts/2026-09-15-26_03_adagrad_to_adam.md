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


Không phải mọi tọa độ của $$w$$ nên chia một số vô hướng $$\eta$$. Đặc trưng ít khi “bắn” (token one-hot) cần bước hiệu dụng lớn hơn; tọa độ gradient khổng lồ sẽ nổ nếu nhận cùng $$\eta$$. **Phương pháp thích nghi đường chéo** giữ ước lượng mô-men hai và chia.

**AdaGrad** (Duchi, Hazan, Singer, 2011) tích phương gradient

$$
G_{k+1} = G_k + g_k \odot g_k, \qquad w_{k+1} = w_k - \eta\, g_k \oslash \bigl(\sqrt{G_{k+1}}+\varepsilon\bigr),
$$

với $$g_k=\nabla f_{I_k}(w_k)$$ và $$\odot,\oslash$$ theo từng phần tử. Bộ tích không quên, nên bước hiệu dụng **co đơn điệu**. Lý tưởng cho bài lồi thưa và vụng cho chạy học sâu dài.

**RMSProp** (Hinton, ghi chú bài giảng) thay tổng bằng trung bình động mũ $$v_{k+1}=\gamma v_k + (1-\gamma)\,g_k\odot g_k$$. Thang đo lại thở được.

**Adam** (Kingma & Ba, 2015) ghép EMA mô-men hai với mô-men một giống momentum, cộng hiệu chỉnh chệch vì cả hai EMA bắt đầu từ không:

$$
\begin{align}
m_{k+1} &= \beta_1 m_k + (1-\beta_1) g_k, \\
v_{k+1} &= \beta_2 v_k + (1-\beta_2)\, g_k\odot g_k, \\
\hat m &= m_{k+1}/(1-\beta_1^{k+1}), \quad
\hat v = v_{k+1}/(1-\beta_2^{k+1}), \\
w_{k+1} &= w_k - \eta\, \hat m \oslash (\sqrt{\hat v}+\varepsilon).
\end{align}
$$

Nút mặc định $$\beta_1=0.9$$, $$\beta_2=0.999$$, $$\varepsilon=10^{-8}$$ là điểm xuất phát bền đến mức bất ngờ — không phải định luật tự nhiên. Adam là **tiền điều kiện đường chéo** cộng momentum, không phải phương pháp bậc hai: nó không lập Hessian.

```python
def adam_step(g, m, v, k, eta=1e-3, b1=0.9, b2=0.999, eps=1e-8):
    m = b1 * m + (1 - b1) * g
    v = b2 * v + (1 - b2) * (g * g)
    mhat = m / (1 - b1 ** (k + 1))
    vhat = v / (1 - b2 ** (k + 1))
    return mhat * eta / (vhat ** 0.5 + eps), m, v
```

Đọc bài báo [arXiv:1412.6980](https://arxiv.org/abs/1412.6980). Bài sau: vì sao cộng $$(\lambda/2)\|w\|_2^2$$ vào loss **không** giống weight decay của AdamW.
