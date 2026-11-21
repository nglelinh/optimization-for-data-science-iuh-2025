---
layout: post
title: 13-09 Modern uses of conjugates, dual norms, and dual cones
chapter: '13'
order: 11
owner: Nguyen Le Linh
categories:
- chapter13
lang: en
lesson_type: optional
---

# Modern uses of conjugates, dual norms, and dual cones

Chapter 13 is already titled “uses of duality”: solving the primal via the dual, dual norms, conjugates, the Lasso dual, and dual cones. This optional lesson attaches 2022–2026 CS applications to those *same* correspondences. We do not re-derive $$f^\star$$ or $$\|y\|_*$$.

## 1. Dual norms and adversarial $$\ell_p$$ balls

The support function of an $$\ell_p$$ attack ball of radius $$\varepsilon$$ is $$\varepsilon\|g\|_*$$, where $$\|\cdot\|_*$$ is the dual of $$\|\cdot\|_p$$:

$$
\|g\|_\infty=\sup_{\|v\|_1\le 1}g^\top v,\qquad
\|g\|_2=\sup_{\|v\|_2\le 1}g^\top v,\qquad
\|g\|_1=\sup_{\|v\|_\infty\le 1}g^\top v.
$$

FGSM / PGD linearise the loss and take a step of length $$\varepsilon$$ in the dual-norm direction (sign for $$\ell_\infty$$, normalisation for $$\ell_2$$). AutoAttack (Croce and Hein, 2020) and the **RobustBench** leaderboard (Croce et al., 2021; maintained through 2025) standardised evaluation for those two dual pairs on CIFAR and ImageNet-scale models. When a paper writes “$$\ell_\infty$$ robust accuracy 0.03,” it has chosen the dual of $$\|\cdot\|_1$$ as the attack geometry. That is [13-03 Dual norms]({% multilang_post_url contents/chapter13/21-04-05-13_03_Dual_norms %}) with a threat model.

Certified robustness goes further: a dual LP or SDP (Chapter 10 / dual cones below) *proves* that no perturbation inside the ball flips the label.

## 2. The Lasso dual as a screening certificate

The Lasso dual in [13-04-01]({% multilang_post_url contents/chapter13/21-04-05-13_04_01_Example_lasso_dual %}) is a projection onto a polytope $$\|X^\top\theta\|_\infty\le\lambda$$. The duality gap $$P(\beta)-D(\theta)$$ is a **computable certificate**. Gap-safe screening (Ndiaye, Fercoq, Gramfort, Salmon) discards features whose inner product with a dual-feasible $$\theta$$ cannot reach $$\lambda$$. Bertrand, Klopfenstein, Bannier, Gidel, and Massias (NeurIPS 2022) put working sets and those dual tests into **skglm**, which fits sparse GLMs with millions of coordinates. Guha, Ndiaye, and Huo (ICML 2023) reuse the dual / homotopy path to build conformal sets. In all of these, you solve or *monitor* the dual in order to finish the primal faster — the slogan of [13-02]({% multilang_post_url contents/chapter13/21-04-05-13_02_Solving_the_primal_via_the_dual %}).

## 3. Conjugates, prox operators, and production cone solvers

The identity $$\operatorname{prox}_f(v)+\operatorname{prox}_{f^\star}(v)=v$$ (Moreau) is how modern first-order cone solvers implement projections. OSQP, SCS, and **Clarabel** (Goulart and Chen, 2024) take a problem in a dual-cone form and run ADMM / interior-point iterations whose expensive step is a prox or a conjugate residual. CVXPY’s canonicalization (already in Chapter 05 of this course) is a map *into* that cone language. When you write `cp.norm1(x)` you are asking for the conjugate of an $$\ell_\infty$$ indicator.

## 4. Dual cones and neural-network certificates

A dual-cone membership $$z\in K^*$$ is the inequality that turns a primal cone program into a bound. SDP and LP relaxations of ReLU networks are cone programs; their duals are the bound-propagation functionals of **$$\alpha,\beta$$-CROWN** and the cutting-plane dual of **GCP-CROWN** (Zhang et al., NeurIPS 2022). Winning VNN-COMP from 2021 through 2025 is, in the language of this chapter, “produce a dual-feasible cone certificate fast enough, on a GPU.” Dual cones are not an algebraic curiosity — they are the type of the proof.

## What to remember

| Object in Chapter 13 | 2022–2026 use |
| --- | --- |
| Dual norm $$\|g\|_*$$ | $$\ell_p$$ attack step and RobustBench |
| Lasso dual / gap | skglm screening and conformal sparse GLMs |
| Conjugate $$f^\star$$ and Moreau | Prox in OSQP / SCS / Clarabel / CVXPY |
| Dual cone $$K^*$$ | LP/SDP certificates for NN verification |

**Question.** Why is the dual of an $$\ell_1$$ regulariser an $$\ell_\infty$$ constraint, and how does that single fact give both the Lasso screening test *and* the FGSM sign attack?

## Sources

- Croce, F., & Hein, M. (2020). Reliable evaluation of adversarial robustness with an ensemble of diverse parameter-free attacks. *ICML*.
- Croce, F., et al. (2021). RobustBench: A standardized adversarial robustness benchmark. *NeurIPS Datasets and Benchmarks*. [https://robustbench.github.io/](https://robustbench.github.io/)
- Bertrand, Q., Klopfenstein, Q., Bannier, P.-A., Gidel, G., & Massias, M. (2022). Beyond L1: Faster and better sparse models with skglm. *NeurIPS*.
- Guha, E. K., Ndiaye, E., & Huo, X. (2023). Conformalization of sparse generalized linear models. *ICML*.
- Goulart, P. J., & Chen, Y. (2024). Clarabel: An interior-point solver for conic programs with quadratic objectives. [arXiv:2405.12762](https://arxiv.org/abs/2405.12762)
- Zhang, H., Wang, S., Xu, K., Li, L., Li, B., Jana, S., Hsieh, C.-J., & Kolter, J. Z. (2022). General cutting planes for bound-propagation-based neural network verification. *NeurIPS*.
- Parikh, N., & Boyd, S. (2014). Proximal algorithms. *Foundations and Trends in Optimization*, 1(3). (Moreau identity used by the solvers above)
