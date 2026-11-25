---
layout: post
title: 00-05 Applications and recent developments
chapter: '00'
order: 18
owner: Nguyen Le Linh
categories:
- chapter00
lang: en
lesson_type: optional
---

It is tempting to treat Chapter 00 as dusty textbook review, yet the biggest breakthroughs in modern AI—reverse-mode automatic differentiation, low-rank adaptation (LoRA) of billion-parameter language models, and score-based diffusion models—are direct applications of the multivariable chain rule, low-rank matrix factorization, and log-density gradients. Mastering these fundamentals means you can read cutting-edge machine learning papers without treating their equations as black boxes.

## Key ideas: Where Chapter 00 Math Powers Frontier AI

- **Reverse-Mode AutoDiff & Implicit Gradients:** Scales the multivariable chain rule to compute $$\nabla f(x) \in \mathbb{R}^n$$ in $$O(1)$$ forward-pass multiples via vector-Jacobian products (VJPs), and differentiates right through argmin layers using the implicit function theorem.
- **Low-Rank Matrix Parameterization (LoRA):** Replaces a dense $$d \times k$$ weight update $$\Delta W$$ with a rank-$$r$$ factor $$BA$$ ($$r \ll \min(d, k)$$), cutting memory and optimizer states by orders of magnitude.
- **Score Functions ($$\nabla_x \log p(x)$$):** Diffusion models learn the gradient of the log probability density—a vector field pointing toward high-density data regions—bypassing intractable normalizing constants.
- **Conditioning & Numerical Precision:** Matrix norms, singular values, and Lipschitz bounds govern whether large-scale training stays numerically stable under reduced-precision arithmetic.

### Worked example: LoRA Compression Ratio and Forward Pass

Suppose a transformer projection layer has weight matrix $$W_0 \in \mathbb{R}^{4096 \times 4096}$$ and we adapt it with rank $$r = 8$$ via $$W = W_0 + BA$$ where $$B \in \mathbb{R}^{4096 \times 8}$$ and $$A \in \mathbb{R}^{8 \times 4096}$$.

1. **Compare trainable parameter counts:**
   - Full fine-tuning: $$4096 \times 4096 = 16{,}777{,}216$$ parameters.
   - LoRA ($$r = 8$$): $$4096 \times 8 + 8 \times 4096 = 65{,}536$$ parameters.
   - Compression factor: $$\frac{16{,}777{,}216}{65{,}536} = 256\times$$ fewer trainable parameters (just $$0.390625\%$$ of the full matrix).
2. **Verify a concrete $$2 \times 2$$ rank-1 update:** Let $$W_0 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$, $$B = \begin{pmatrix} 2 \\ -1 \end{pmatrix}$$, $$A = \begin{pmatrix} 1 & 3 \end{pmatrix}$$, and input $$x = \begin{pmatrix} 1 \\ 2 \end{pmatrix}$$.
   - Compute $$Ax = 1(1) + 3(2) = 7$$ (a scalar!).
   - Compute $$B(Ax) = 7\begin{pmatrix} 2 \\ -1 \end{pmatrix} = \begin{pmatrix} 14 \\ -7 \end{pmatrix}$$.
   - Total output: $$W_0 x + B(Ax) = \begin{pmatrix} 1 \\ 2 \end{pmatrix} + \begin{pmatrix} 14 \\ -7 \end{pmatrix} = \begin{pmatrix} 15 \\ -5 \end{pmatrix}$$, matching $$(W_0 + BA)x = \begin{pmatrix} 3 & 6 \\ -1 & -2 \end{pmatrix}\begin{pmatrix} 1 \\ 2 \end{pmatrix} = \begin{pmatrix} 15 \\ -5 \end{pmatrix}$$ without ever materializing the full $$BA$$ matrix.

The calculus, linear algebra, and probability in this chapter are not a warm-up you leave behind. They are the working language of the models you will train after week one. This lesson connects those tools to four developments from roughly 2022–2025 that a data-science student will meet in papers, libraries, and internships. The theory in the earlier lessons does not change; the point is to see *where* gradients, low-rank factorizations, and score functions show up in production systems.

## Automatic differentiation and implicit gradients

Backpropagation is the chain rule applied to a computation graph. Modern frameworks implement *automatic differentiation*: you write a Python function $$f$$, and the library returns $$\nabla f$$ without a handwritten Jacobian. Blondel and Roulet’s 2024–2025 monograph *The Elements of Differentiable Programming* ([arXiv:2403.14606](https://arxiv.org/abs/2403.14606)) treats this as a programming model, not a trick: if a program is assembled from differentiable atoms, gradient-based optimization of its parameters is well-defined, including programs with control flow.

A second, quieter use of Chapter 00 calculus is the **implicit function theorem**. If a solver returns $$x^\star(\theta)$$ defined by an optimality map $$F(x,\theta)=0$$ (for example $$\nabla_x L(x,\theta)=0$$), you do **not** backpropagate through every inner iteration. Differentiating the identity $$F(x^\star(\theta),\theta)=0$$ yields the linear system

$$
\nabla_\theta x^\star = - \bigl(\nabla_x F\bigr)^{-1} \nabla_\theta F.
$$

Blondel, Berthet, Cuturi, Frostig, Hoyer, Llinares-López, Pedregosa, and Vert implement this as *automatic implicit differentiation* in JAXopt ([NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/hash/228b9279ecf9bbafe582406850c57115-Abstract-Conference.html); [github.com/google/jaxopt](https://github.com/google/jaxopt)). The user supplies $$F$$ in Python; JAX differentiates $$F$$ and solves the linear system. Hyperparameter tuning of ridge regression, meta-learning, and optimization layers all reduce to this identity. When you later meet first-order optimality in Chapter 04, reread this paragraph: the same $$\nabla f(x)=0$$ condition is what implicit differentiation linearizes.

## Low-rank updates: LoRA as linear algebra

Fine-tuning a large language model by changing every entry of a weight matrix $$W_0\in\mathbb{R}^{d\times k}$$ is expensive in memory and in storage of task-specific copies. Hu, Shen, Wallis, Allen-Zhu, Li, Wang, Wang, and Chen (*LoRA*, [ICLR 2022](https://openreview.net/forum?id=nZeVKeeFYf9); [arXiv:2106.09685](https://arxiv.org/abs/2106.09685)) freeze $$W_0$$ and learn a rank-$$r$$ correction

$$
W = W_0 + BA, \qquad B\in\mathbb{R}^{d\times r},\; A\in\mathbb{R}^{r\times k},\; r\ll \min(d,k).
$$

The number of trainable parameters drops from $$dk$$ to $$r(d+k)$$. On GPT-3-scale models the paper reports order-of-magnitude reductions in trainable parameters with no extra inference latency, because $$B$$ and $$A$$ can be merged into $$W$$ after training. The linear-algebra content of Chapter 00 is exactly what makes the claim checkable: rank, matrix multiplication cost, and the idea that a structured update can live in a thin subspace. Adapter libraries you will see in Hugging Face (PEFT) are this factorization plus engineering.

## Score matching and diffusion models

A generative model that samples images by gradually denoising Gaussian noise is, at heart, a probability exercise. Let $$p_t$$ be a family of smoothed densities and let $$s_\theta(x,t)$$ approximate the *score* $$\nabla_x \log p_t(x)$$. Training minimizes a weighted regression on scores; sampling integrates an ordinary differential (or stochastic differential) equation driven by $$s_\theta$$. Karras, Aittala, Aila, and Laine (*Elucidating the Design Space of Diffusion-Based Generative Models*, [NeurIPS 2022](https://proceedings.neurips.cc/paper/2022/hash/a98846e9d9cc01cfb87eb694d946ce6b-Abstract-Conference.html); [arXiv:2206.00364](https://arxiv.org/abs/2206.00364); code [NVlabs/edm](https://github.com/NVlabs/edm)) rewrite several popular diffusion recipes as one design space: preconditioning of the network, the noise schedule, and the sampler. Their class-conditional CIFAR-10 FID of $$1.79$$ with 35 network evaluations became a standard reference implementation.

What you need from Chapter 00 is modest and precise: the gradient of a log-density, the Gaussian family, and the fact that an ODE/SDE is a calculus object. You do not need the full stochastic-analysis machinery to see why “predict the noise, then take an Euler step” is a numerical method for a score field.

## A compact numerical check (LoRA shapes)

The following snippet does not train a Transformer; it only checks that a low-rank factorization has the parameter count the LoRA paper advertises. Run it after you review matrix multiplication in 00-02.

```python
import numpy as np

d, k, r = 4096, 4096, 8
full = d * k
lora = r * (d + k)
print("full params:", full)
print("LoRA params:", lora)
print("ratio:", full / lora)

W0 = np.random.randn(d, k)
A = np.random.randn(r, k)
B = np.random.randn(d, r)
W = W0 + B @ A
print("W shape:", W.shape, "rank bound:", r)
```

## What to carry forward

When a paper says “we differentiate through the KKT map,” “we inject a rank-$$r$$ adapter,” or “we match the score of a Gaussian perturbation,” it is speaking Chapter 00. The later chapters add convexity, canonical forms, and algorithms; they do not replace derivatives, factorizations, or densities.

## Sources

1. M. Blondel and V. Roulet, *The Elements of Differentiable Programming*, arXiv:2403.14606, 2024 (rev. 2025). [https://arxiv.org/abs/2403.14606](https://arxiv.org/abs/2403.14606)
2. M. Blondel et al., “Efficient and Modular Implicit Differentiation,” NeurIPS 2022. [paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/228b9279ecf9bbafe582406850c57115-Abstract-Conference.html) · [JAXopt](https://github.com/google/jaxopt)
3. E. J. Hu et al., “LoRA: Low-Rank Adaptation of Large Language Models,” ICLR 2022. [OpenReview](https://openreview.net/forum?id=nZeVKeeFYf9) · [arXiv:2106.09685](https://arxiv.org/abs/2106.09685)
4. T. Karras, M. Aittala, T. Aila, and S. Laine, “Elucidating the Design Space of Diffusion-Based Generative Models,” NeurIPS 2022. [abstract](https://proceedings.neurips.cc/paper/2022/hash/a98846e9d9cc01cfb87eb694d946ce6b-Abstract-Conference.html) · [arXiv:2206.00364](https://arxiv.org/abs/2206.00364)
