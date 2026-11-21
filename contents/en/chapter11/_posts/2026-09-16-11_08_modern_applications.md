---
layout: post
title: 11-10 Modern applications of Lagrangian duality
chapter: '11'
order: 11
owner: Nguyen Le Linh
categories:
- chapter11
lang: en
lesson_type: optional
---

# Modern applications of Lagrangian duality

Chapter 11 lifts duality from LPs to a general program: the Lagrangian $$L(x,u,v)$$, the dual function $$g(u,v)=\inf_x L$$, weak duality $$g\le f^\star$$, and strong duality under convexity plus a constraint qualification. This optional lesson shows four modern uses of *that* dual — multipliers as prices, as robustness radii, and as training signals — without re-deriving $$g$$.

## 1. Distributionally robust learning (DRO)

Instead of minimising empirical risk $$\mathbb{E}_{\hat P}[\ell(x,\xi)]$$, DRO solves

$$
\min_x\ \sup_{P\in\mathcal{P}}\ \mathbb{E}_P[\ell(x,\xi)],
$$

where the ambiguity set $$\mathcal{P}$$ is a ball of distributions ($$\phi$$-divergence or Wasserstein) around the sample. The inner supremum is a **conjugate / dual** problem: for a Wasserstein ball it becomes a regularised risk whose dual variable is the Lipschitz price of moving mass. Rahimian and Mehrotra (2022) survey the duality, the calibration of $$\mathcal{P}$$, and the solvers. Kuhn, Esfahani, Nguyen, and Shafieezadeh-Abadeh (2019) is the Wasserstein tutorial still cited in 2023–2026 ML papers on noisy labels, shift, and adversarial training. Strong duality is what turns an infinite-dimensional worst-case expectation into a finite convex program you can hand to CVXPY.

## 2. Hard constraints in energy and physics: OPF-DNN and DC3

AC optimal power flow (OPF) is a nonconvex program with Kirchhoff equalities and thermal limits. Fioretto, Mak, and Van Hentenryck (AAAI 2020) train a network to predict setpoints while **updating Lagrange multipliers by a subgradient step** on constraint residuals — Lagrangian duality as a training loop. Donti, Rolnick, and Kolter (ICLR 2021) propose **DC3**: complete equalities differentiably, then correct inequalities by unrolled gradient steps, and demonstrate it on AC-OPF. Follow-up 2022–2025 “learning to optimize” papers keep the same dual idea: multipliers are not only certificates after the fact; they are **features** the net is trained to respect.

Weak duality still gives a bound even when the primal is nonconvex; strong duality is *not* free. That distinction is the whole point of this chapter.

## 3. Fairness reductions as a dual game

Agarwal et al. (2018) and the Fairlearn `ExponentiatedGradient` reducer (Weerts et al., 2023) treat group-rate constraints as a Lagrangian. The dual player puts mass on the currently violated group; the primal player solves a *weighted* ERM. Cotter et al. (2019) extend the game to nonsmooth rate constraints via a proxy-Lagrangian. In all three, $$v\ge 0$$ is the Chapter 11 multiplier of an inequality $$g_i(x)\le 0$$, and complementary slackness (Chapter 12) says a group that already meets its rate should have $$v_i=0$$.

## 4. SVM and kernel machines, still via the dual

The soft-margin SVM is the textbook general program whose dual is a box-constrained QP in the coefficients $$\alpha_i$$. sklearn’s `SVC` and a long tail of 2022–2026 computational-biology and small-$$n$$ tabular papers still *solve the dual*, because the kernel trick is a statement about $$g(\alpha)$$, not about $$w$$. You will meet the KKT form in Chapter 12; the *existence* of a useful $$g$$ is this chapter.

## What to remember

Form the Lagrangian, minimise in $$x$$ to get $$g$$, maximise $$g$$ in the multipliers. If the primal is convex and a CQ holds, you may swap inf and sup. DRO, constrained nets, fairness reducers, and kernel SVMs are four different stories about that swap.

**Question.** In a Wasserstein DRO problem, what does a large optimal dual variable on the radius tell you about the cost of a distribution shift — and which inequality of this chapter makes that number a valid lower bound on worst-case risk?

## Sources

- Rahimian, H., & Mehrotra, S. (2022). Frameworks and results in distributionally robust optimization. *Open Journal of Mathematical Optimization*, 3, article 4. [doi:10.5802/ojmo.15](https://doi.org/10.5802/ojmo.15)
- Kuhn, D., Esfahani, P. M., Nguyen, V. A., & Shafieezadeh-Abadeh, S. (2019). Wasserstein distributionally robust optimization: Theory and applications in machine learning. In *Operations Research & Management Science in the Age of Analytics*.
- Fioretto, F., Mak, T. W. K., & Van Hentenryck, P. (2020). Predicting AC optimal power flows: Combining deep learning and Lagrangian dual methods. *AAAI*.
- Donti, P. L., Rolnick, D., & Kolter, J. Z. (2021). DC3: A learning method for optimization with hard constraints. *ICLR*.
- Weerts, H., Dudík, M., Edgar, R., Jalali, A., Lutz, R., & Madaio, M. (2023). Fairlearn: Assessing and improving fairness of AI systems. *JMLR*, 24(257).
- Agarwal, A., Beygelzimer, A., Dudík, M., Langford, J., & Wallach, H. (2018). A reductions approach to fair classification. *ICML*.
- Cotter, A., et al. (2019). Optimization with non-differentiable constraints with applications to fairness, recall, churn, and other goals. *JMLR*, 20(172).
