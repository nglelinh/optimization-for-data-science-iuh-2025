---
layout: post
title: 21 Alternating Direction Method of Multipliers
chapter: '21'
order: 1
owner: Hooncheol Shin
categories:
- chapter21
lang: en
---

Chapter 20 built the engine of **ADMM**; Chapter 21 takes that engine out onto the open highway of modern statistical learning, matrix decomposition, and distributed computing. What makes ADMM extraordinary in practice is not just its three-line algorithm, but the *art of variable splitting*: by choosing the right auxiliary variables $$z$$ and linear constraints $$Ax + Bz = c$$, seemingly intractable problems—Lasso, Group Lasso, Sparse PCA, Robust PCA, 2D Total Variation denoising, and multi-machine consensus—fracture into cached linear solves and closed-form proximal operators!

## Background Knowledge Map: The Craft of ADMM Variable Splitting

- **Proximal-Operator Modularity:** Splitting $$\min f(x) + g(x)$$ into $$\min f(x) + g(z) \text{ s.t. } x = z$$ turns ADMM into an alternating pair of proximal maps $$\operatorname{prox}_{f/\rho}$$ and $$\operatorname{prox}_{g/\rho}$$, allowing each piece to use its own specialized closed-form solver.
- **Factorization Caching (Pre-Cholesky Advantage):** In Lasso and ridge-coupled problems, the $$x$$-update solves $$(X^T X + \rho I)\beta = \text{rhs}$$ with the *exact same* matrix at every iteration. Computing the Cholesky factor once at $$k = 0$$ drops every subsequent iteration from $$O(p^3)$$ to $$O(p^2)$$!
- **Matrix & Spectral Splittings:** ADMM extends seamlessly from vectors to matrices—combining nuclear-norm singular-value thresholding (low rank) with entrywise soft-thresholding (sparsity) in Robust PCA and Fantope projections in Sparse PCA.
- **Consensus & Subproblem Parametrization:** Duplicating variables across machines yields *Consensus ADMM* for distributed data, while splitting along orthogonal spatial directions (horizontal vs. vertical chains in 2D Fused Lasso) unlocks dramatic convergence speedups.

### Step-by-Step Worked Example (Read Slowly): Why Pre-Factorizing $$(X^T X + \rho I)$$ Wins

Suppose we solve a Lasso problem with $$X \in \mathbb{R}^{500 \times 100}$$ over $$T = 200$$ ADMM iterations using the split $$\min \frac{1}{2}\|y - X\beta\|_2^2 + \lambda\|\alpha\|_1$$ s.t. $$\beta = \alpha$$.

1. **Examine the $$\beta$$-update linear system:**
   $$\left(X^T X + \rho I\right)\beta^{(k)} = X^T y + \rho\big(\alpha^{(k-1)} - w^{(k-1)}\big).$$
   Notice that the left-hand matrix $$M = X^T X + \rho I \succ 0$$ **never changes across iterations** (as long as $$\rho$$ is fixed)!
2. **Compare naive vs. cached Cholesky cost ($$p = 100, T = 200$$):**
   - **Naive (re-factor every iteration):** $$200 \times \frac{1}{3} p^3 \approx 6.67 \times 10^7$$ FLOPs.
   - **Cached Cholesky (factor $$M = L L^T$$ once, then forward/back-solve):**
     $$\frac{1}{3}(100)^3 + 200 \times 2(100)^2 = 3.33 \times 10^5 + 4.00 \times 10^6 \approx 4.33 \times 10^6 \text{ FLOPs}.$$
3. **Speedup:**
   A single architectural observation—caching $$L$$ outside the ADMM loop—delivers an immediate **15× speedup** (and **150×** at $$p = 1000$$), turning ADMM into a production-grade statistical solver!

This chapter aims to examine ADMM, which was covered in [Chapter 20]({% multilang_post_url contents/chapter20/21-03-27-20_00_Dual_Methods %}), in more detail. The basic concepts are not significantly different in depth from what was covered in Chapter 20, and we will mainly look at application cases.

### Reference Papers

* Boyd, Stephen, et al. [BPCPE11] "Distributed optimization and statistical learning via the alternating direction method of multipliers." Foundations and Trends® in Machine learning 3.1 (2011): 1-122.
* Hong, Mingyi, and Zhi-Quan Luo. [HL12] "On the linear convergence of the alternating direction method of multipliers." Mathematical Programming 162.1-2 (2017): 165-199.
* Deng, Wei, and Wotao Yin. [DY16] "On the global and linear convergence of the generalized alternating direction method of multipliers." Journal of Scientific Computing 66.3 (2016): 889-916.
* Iutzeler, Franck, et al. [IBCH14] "Linear convergence rate for distributed optimization with the alternating direction method of multipliers." 53rd IEEE Conference on Decision and Control. IEEE, 2014.
* Nishihara, Robert, et al. [NLRPJ15] "A general analysis of the convergence of ADMM." arXiv preprint arXiv:1502.02009 (2015).
* Parikh, Neal, and Stephen Boyd. [NB13] "Proximal algorithms." Foundations and Trends® in Optimization 1.3 (2014): 127-239.
* Vu, Vincent Q., et al. [VCLR13] "Fantope projection and selection: A near-optimal convex relaxation of sparse PCA." Advances in neural information processing systems. 2013.
* Candès, Emmanuel J., et al. [CLMW09] "Robust principal component analysis?." Journal of the ACM (JACM) 58.3 (2011): 11.
* Ramdas, Aaditya, and Ryan J. Tibshirani. [RT16] "Fast and flexible ADMM algorithms for trend filtering." Journal of Computational and Graphical Statistics 25.3 (2016): 839-858.
* Wytock, Matt, Suvrit Sra, and Jeremy Z. Kolter. [WSK14] "Fast Newton methods for the group fused lasso." UAI. 2014.
* Barbero, Alvaro, and Suvrit Sra. [BS14] "Modular proximal optimization for multidimensional total-variation regularization." arXiv preprint arXiv:1411.0589 (2014).


ADMM convergence relation, : [BPCPE11], [HL12], [DY16], [IBCH14], [NLRPJ15]  
Sparse subspace estimation : [VCLR13]  
Sparse plus low rank decomposition : [CLMW09]  
Consensus ADMM : [BPCPE11], [NB13]  
Subprogram parameterization : [RT16], [WSK14], [BS14]

## 2026 applications (optional)

The classical examples above (Lasso, sparse-plus-low-rank, consensus, fused lasso) are still the right first pass. A 2022–2026 optional lesson maps the *same* consensus / proximal split onto federated deep learning (**FedADMM**), plug-and-play imaging with CNN denoisers, and online distributed optimal power flow. Start at [21-07 Modern applications of ADMM]({% multilang_post_url contents/chapter21/2026-09-16-21_07_modern_applications %}). It does not replace Boyd et al.; it tells you where the residuals are being monitored in production.
