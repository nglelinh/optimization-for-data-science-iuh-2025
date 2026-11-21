---
layout: post
title: 09-06 Modern applications of proximal GD and acceleration
chapter: '09'
order: 13
owner: Nguyen Le Linh
categories:
- chapter09
lang: en
lesson_type: optional
---

# Modern applications of proximal GD and acceleration

Chapter 09 studies composite problems $$\min_x g(x)+h(x)$$ with $$g$$ smooth and $$h$$ prox-friendly, the proximal-gradient iteration, and Nesterov / FISTA acceleration. This optional lesson stays on that template and shows where it ran in imaging, sparse GLMs, and *unrolled* networks from 2022 to 2026.

Recall the FISTA pair already in [09-05-03]({% multilang_post_url contents/chapter09/20-01-08-09_05_03_example_FISTA %}):

$$
y^{k}=x^{k-1}+\frac{t_{k-1}-1}{t_k}(x^{k-1}-x^{k-2}),\qquad
x^{k}=\operatorname{prox}_{t_k h}\bigl(y^{k}-t_k\nabla g(y^{k})\bigr).
$$

When $$h=\lambda\|\cdot\|_1$$ the prox is soft-thresholding — the same map as Chapter 07.

## 1. MRI / CT reconstruction: FISTA, then PnP-FISTA

Compressed-sensing MRI and sparse-view CT are composite least-squares plus a sparsity or total-variation regulariser. Classical FISTA (Beck and Teboulle, 2009) is still the CPU/GPU baseline in hospital research code. The 2023 IEEE SPM tutorial of Kamilov, Bouman, Buzzard, and Wohlberg explains why labs then **replace the prox of $$h$$ by a learned denoiser** and keep the gradient step of $$g$$ (the physical forward model). That hybrid is **plug-and-play (PnP)**; their Algorithm 4 is literally **PnP-FISTA**. Applications they survey include bio-microscopy, CT, MRI, and ptycho-tomography.

The data-fidelity piece is the smooth $$g$$ of this chapter; the denoiser plays the role of $$\operatorname{prox}_{t h}$$. You should be able to write the iteration before you discuss the neural net.

## 2. Algorithm unrolling: FISTA-Net and pFISTA-DR

Unrolling (Monga, Li, and Eldar, 2021) turns a fixed number of proximal-gradient / FISTA steps into a neural architecture whose step sizes, thresholds, and even the prox are trained. Xiang, Dong, and Yang (2021) published **FISTA-Net** in *IEEE TMI*: cascade of gradient, proximal, and momentum modules, evaluated on electromagnetic tomography and X-ray CT. Qu, Zhang, Kang, Lin, Lin, She, Wu, Wang, and Zheng (2024) unrolled **projected FISTA** for radial MRI (**pFISTA-DR**) and reported reconstruction dropping from about 48 s/slice to 0.55 s/slice on clinical data. Zhang, Chen, Xiong, and Zhang (2023) survey the same idea as *physics-inspired compressive sensing*: the ISTA/FISTA skeleton stays, the linear maps become learned.

**Course link.** If you cannot write FISTA on paper, an unrolled net is just another black box. The point of this chapter is that the skip / momentum connection *is* Nesterov’s $$t_k$$ sequence.

## 3. Elastic net and matrix completion in production solvers

The elastic net $$\tfrac12\|X\beta-y\|_2^2+\lambda\bigl(\alpha\|\beta\|_1+(1-\alpha)\tfrac12\|\beta\|_2^2\bigr)$$ is proximal gradient (or coordinate descent on a quadratic-plus-$$\ell_1$$) with a **ridge-adjusted soft-threshold**. Tay, Narasimhan, and Hastie (2023) made that path the default for every GLM family in glmnet — genomics, click prediction, and Cox models included. The matrix-completion example of [09-03]({% multilang_post_url contents/chapter09/20-01-08-09_03_example_matrix_completion %}) is the same composite pattern (smooth data term + nuclear-norm prox = singular-value thresholding) that still sits under recommender and single-cell imputation pipelines.

ISTA / FISTA are not always the fastest *CPU* method for Lasso (coordinate descent plus screening usually wins; see Chapter 13), but they are the methods you can **GPU-batch, unroll, or swap the prox of**. That is why imaging and differentiable programming standardised on them.

## 4. A tiny ISTA step

```python
import numpy as np

def soft_threshold(z, t):
    return np.sign(z) * np.maximum(np.abs(z) - t, 0.0)

def ista_step(x, A, b, lam, t):
    # t < 1 / ||A||^2 for the quadratic g(x) = 0.5 ||Ax - b||^2
    return soft_threshold(x - t * A.T @ (A @ x - b), t * lam)
```

FISTA only changes the *point* at which you evaluate $$\nabla g$$, using the momentum of Section 09-05. PnP-FISTA changes `soft_threshold` to `denoiser`. FISTA-Net makes `t` and the denoiser learnable.

## What to remember

Composite structure (smooth likelihood + prox-friendly regulariser) is why proximal gradient exists. Acceleration is a $$t_k$$ schedule, not a different model. From 2022 to 2026 the same schedule is (i) a solver, (ii) a plug-and-play wrapper around a CNN denoiser, and (iii) a neural net obtained by unrolling ten to forty steps.

**Question.** When would you keep a true prox (soft-threshold, SVT) instead of replacing it by a learned denoiser — and what does Chapter 09’s theory still guarantee in the PnP case?

## Sources

- Beck, A., & Teboulle, M. (2009). A fast iterative shrinkage-thresholding algorithm for linear inverse problems. *SIAM J. Imaging Sciences*, 2(1), 183–202. (classical FISTA)
- Kamilov, U. S., Bouman, C. A., Buzzard, G. T., & Wohlberg, B. (2023). Plug-and-play methods for integrating physical and learned models in computational imaging. *IEEE Signal Processing Magazine*, 40(1), 85–97.
- Monga, V., Li, Y., & Eldar, Y. C. (2021). Algorithm unrolling: Interpretable, efficient deep learning for signal and image processing. *IEEE Signal Processing Magazine*, 38(2), 18–44.
- Xiang, J., Dong, Y., & Yang, Y. (2021). FISTA-Net: Learning a fast iterative shrinkage thresholding network for inverse problems in imaging. *IEEE Transactions on Medical Imaging*, 40(5), 1329–1339.
- Qu, B., Zhang, J., Kang, T., Lin, J., Lin, M., She, H., Wu, Q., Wang, M., & Zheng, G. (2024). Radial magnetic resonance image reconstruction with a deep unrolled projected fast iterative soft-thresholding network. *Computers in Biology and Medicine*, 168, 107707.
- Zhang, J., Chen, B., Xiong, R., & Zhang, Y. (2023). Physics-inspired compressive sensing: Beyond deep unrolling. *IEEE Signal Processing Magazine*, 40(1), 58–72.
- Tay, J. K., Narasimhan, B., & Hastie, T. (2023). Elastic net regularization paths for all generalized linear models. *Journal of Statistical Software*, 106(1).
