---
layout: post
title: 26-03 AdaGrad, RMSProp intuition, and Adam
chapter: '26'
order: 4
owner: Nguyen Le Linh
categories:
- chapter26
lang: en
lesson_type: required
---


Not every coordinate of $$w$$ should share one scalar $$\eta$$. Features that fire rarely (think one-hot tokens) need larger effective steps; coordinates with huge gradients would explode if given the same $$\eta$$. **Diagonal adaptive methods** keep a running second-moment estimate and divide.

**AdaGrad** (Duchi, Hazan, Singer, 2011) accumulates squared gradients

$$
G_{k+1} = G_k + g_k \odot g_k, \qquad w_{k+1} = w_k - \eta\, g_k \oslash \bigl(\sqrt{G_{k+1}}+\varepsilon\bigr),
$$

where $$g_k=\nabla f_{I_k}(w_k)$$ and $$\odot,\oslash$$ are elementwise. The accumulator never forgets, so the effective step **shrinks monotonically**. That is ideal for sparse convex problems and awkward for long deep-learning runs.

**RMSProp** (Hinton, lecture note) replaces the sum by an exponential moving average $$v_{k+1}=\gamma v_k + (1-\gamma)\,g_k\odot g_k$$. The scale can breathe again.

**Adam** (Kingma & Ba, 2015) pairs that second-moment EMA with a momentum-like first moment, plus bias correction because both EMAs start at zero:

$$
\begin{align}
m_{k+1} &= \beta_1 m_k + (1-\beta_1) g_k, \\
v_{k+1} &= \beta_2 v_k + (1-\beta_2)\, g_k\odot g_k, \\
\hat m &= m_{k+1}/(1-\beta_1^{k+1}), \quad
\hat v = v_{k+1}/(1-\beta_2^{k+1}), \\
w_{k+1} &= w_k - \eta\, \hat m \oslash (\sqrt{\hat v}+\varepsilon).
\end{align}
$$

Default knobs $$\beta_1=0.9$$, $$\beta_2=0.999$$, $$\varepsilon=10^{-8}$$ are a surprisingly robust starting point — not laws of nature. Adam is a **diagonal preconditioner** plus momentum, not a second-order method: it never forms a Hessian.

```python
def adam_step(g, m, v, k, eta=1e-3, b1=0.9, b2=0.999, eps=1e-8):
    m = b1 * m + (1 - b1) * g
    v = b2 * v + (1 - b2) * (g * g)
    mhat = m / (1 - b1 ** (k + 1))
    vhat = v / (1 - b2 ** (k + 1))
    return mhat * eta / (vhat ** 0.5 + eps), m, v
```

Read the paper as [arXiv:1412.6980](https://arxiv.org/abs/1412.6980). Next lesson: why adding $$(\lambda/2)\|w\|_2^2$$ to the loss is **not** the same as AdamW weight decay.
