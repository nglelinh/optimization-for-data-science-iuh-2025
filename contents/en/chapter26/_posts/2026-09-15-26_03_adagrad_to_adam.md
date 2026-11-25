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

In a neural language model, the embedding vector for the word "the" receives a gradient on almost every sentence, while the embedding for "eigenvector" fires once every thousand batches. Handing both parameters the same scalar learning rate $$\eta$$ forces an impossible compromise: either "the" explodes or "eigenvector" never learns. Adaptive methods—starting with AdaGrad (2011), refined by RMSProp (2012), and unified with momentum in Adam (2015)—solve this by maintaining a per-coordinate running meter of gradient energy and normalizing every step automatically.

## Key ideas: From AdaGrad to RMSProp and Adam

- **AdaGrad (Cumulative Squared Gradients):** Tracks $$G_t = \sum_{\tau=1}^t g_\tau \odot g_\tau$$ and scales coordinate $$j$$ by $$\frac{\eta}{\sqrt{G_{t,j} + \varepsilon}}$$. Brilliant for sparse convex features, but because $$G_t$$ grows monotonically forever, the effective step size eventually vanishes to zero in deep nonconvex training.
- **RMSProp (Exponential Moving Average):** Replaces the infinite sum $$G_t$$ with an exponential moving average $$v_t = \beta_2 v_{t-1} + (1 - \beta_2) g_t^2$$, letting the preconditioner forget ancient curvature and adapt smoothly across non-stationary loss landscapes.
- **Adam (First + Second Moments):** Combines exponential momentum $$m_t = \beta_1 m_{t-1} + (1 - \beta_1) g_t$$ with RMSProp’s second-moment accumulator $$v_t = \beta_2 v_{t-1} + (1 - \beta_2) g_t^2$$, producing an approximately scale-invariant step $$-\eta \frac{\hat{m}_t}{\sqrt{\hat{v}_t} + \varepsilon}$$.
- **Zero-Initialization Bias Correction:** Because $$m_0 = 0$$ and $$v_0 = 0$$ bias early estimates heavily toward zero (especially when $$\beta_2 = 0.999$$), dividing by $$(1 - \beta_1^t)$$ and $$(1 - \beta_2^t)$$ makes $$\hat{m}_t$$ and $$\hat{v}_t$$ exact unbiased moment estimators at early steps.

### Worked example: Hand-Tracing Two Steps of Adam on Two Disproportionate Coordinates

Suppose a 2D parameter $$w_0 = (0, 0)^\top$$ sees a tiny gradient on coordinate 1 and a huge gradient on coordinate 2: $$g_1 = (0.1,\ 10)^\top$$ and $$g_2 = (0.1,\ 10)^\top$$. Use $$\eta = 0.1$$, $$\beta_1 = 0.9$$, $$\beta_2 = 0.99$$, $$\varepsilon = 0$$ (for clean hand arithmetic).

1. **Step $$t = 1$$ ($$g_1 = (0.1,\ 10)$$):**
   - $$m_1 = (1 - 0.9)(0.1, 10) = (0.01,\ 1.0)$$, bias-corrected $$\hat{m}_1 = \frac{m_1}{1 - 0.9} = (0.1,\ 10)$$.
   - $$v_1 = (1 - 0.99)(0.01, 100) = (0.0001,\ 1.0)$$, bias-corrected $$\hat{v}_1 = \frac{v_1}{1 - 0.99} = (0.01,\ 100)$$.
   - Normalized step: $$\frac{\hat{m}_1}{\sqrt{\hat{v}_1}} = \left(\frac{0.1}{0.1},\ \frac{10}{10}\right) = (1,\ 1)$$!
   - Update: $$w_1 = (0, 0) - 0.1(1, 1) = (-0.1,\ -0.1)$$.
2. **Observe what just happened:** Even though coordinate 2’s gradient was **100× larger** than coordinate 1’s, Adam moved *both* coordinates by the exact same step size $$-0.1$$!
3. **Without bias correction at $$t = 1$$:** Notice $$\frac{m_1}{\sqrt{v_1}} = \left(\frac{0.01}{0.01},\ \frac{1.0}{1.0}\right) = (1, 1)$$ only accidentally matched because $$1 - \beta_1 = 0.1 = \sqrt{1 - \beta_2}$$; if $$\beta_2 = 0.999$$ (the default!), $$\frac{m_1}{\sqrt{v_1}} = \frac{0.1}{\sqrt{0.001}} \approx 3.16\times$$ too large—proving why bias correction is vital at $$t = 1$$!

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

### AdaGrad → RMSProp → Adam in about 3 minutes

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/adagrad-rmsprop-adam_en.mp4"></video>
</div>

Three adaptive steps on the same skewed quadratic: AdaGrad slows down, RMSProp jitters around the solution, Adam with bias correction.
