---
layout: post
title: 25-03 Modern applications of MIP in data science
chapter: '25'
order: 10
owner: Nguyen Le Linh
categories:
- chapter25
lang: en
lesson_type: optional
---


Chapter 25 is the *solver* half of mixed-integer programming: cutting planes, branch-and-cut, and two extended examples (best subset, least quantile). Those techniques are now used to *select features*, *certify* neural nets, *grow optimal trees*, and even *learn which cuts* to add. This optional note is the 2022–2026 application layer on top of 25-01 and 25-02; it does not re-derive Gomory cuts.

## 1. Best-subset selection, still the MIP poster child

The $$\ell_0$$-constrained least-squares problem in 25-02-01 is

$$
\min_\beta\ \tfrac12\|y-X\beta\|_2^2\qquad\text{subject to}\qquad \|\beta\|_0\le k,
$$

or the big-$$M$$ form with binaries $$z_i$$. Bertsimas, King, and Mazumder, *Ann. Statist.* 44(2):813–852, 2016, showed that a modern MIP solver plus warm starts can beat the folklore “intractable for $$p>30$$.” The 2020s comparison is no longer MIP versus Lasso on a laptop: it is MIP versus pathwise CD (Chapter 23) versus nonconvex penalties (skglm) on $$p$$ in the hundreds, with a *certificate* when the gap closes. Use Lasso / elastic net to explore; use best-subset MIP when a regulator or a scientist asks for “exactly $$k$$ genes” and a bound on suboptimality.

## 2. Feature selection for trained networks

Zhao, Tsay, and Kronqvist, *Model-based feature selection for neural networks: A mixed-integer programming approach*, [arXiv:2302.10344](https://arxiv.org/abs/2302.10344) (2023), encode a trained ReLU net and solve a sequence of MILPs that search for *sparse inputs* maximizing class confidence, with cardinality and distribution constraints. On MNIST / Fashion-MNIST they keep about 15% of pixels and retrain a smaller, more attack-robust net. This is best-subset thinking applied to the *input*, with the trained network encoded as a piecewise-linear MIP — the same encoding used for verification below.

## 3. Verifying ReLU networks with MILP

A ReLU $$h=\max(0,Wx+b)$$ is a mixed-integer linear constraint (binary activation, big-$$M$$ or a tighter formulation). Asking “does there exist a perturbation of size $$\varepsilon$$ that flips the label?” is then a MILP. Tjeng, Xiao, and Tedrake, *Evaluating Robustness of Neural Networks with Mixed Integer Programming*, ICLR 2019, [OpenReview](https://openreview.net/forum?id=HyGIdiRqtm), combined a tight encoding with progressive bound tightening and verified MNIST nets with over $$10^5$$ units, orders of magnitude beyond the SMT verifier Reluplex. Fischetti and Jo (2018) is the MIP-OR companion. The 2022–2025 literature (stronger ReLU inequalities, dependency analysis, GPU bound propagation) still sits on that formulation. If you understood Gomory and branch-and-cut in this chapter, you can read a verification paper: the “cut” is a linear inequality that a ReLU activation must satisfy.

## 4. Optimal classification trees and learning to cut

Bertsimas and Dunn, *Machine Learning* 106:1039–1082, 2017, write the entire decision tree as a MIP (Optimal Classification Trees, OCT). Hua, Ren, and Cao, NeurIPS 2022 ([paper](https://proceedings.neurips.cc/paper_files/paper/2022/hash/37771cc0be272368102a37f202bb88d8-Abstract-Conference.html)), give a reduced-space branch-and-bound algorithm (RS-OCT) that scales OCT to tables with hundreds of thousands of rows and reports better test accuracy than prior MIP-OCT baselines on large UCI sets. Loss-optimal / logistic trees (TOP, 2024) keep the same MILP backbone and swap the misclassification objective for a piecewise-linear logistic loss.

On the *solver* side, learning to **select cutting planes** (e.g. HGTSM, [arXiv:2410.03112](https://arxiv.org/abs/2410.03112), 2024) trains a heterogeneous graph model on MIPLIB 2017 and ML4CO instances so that the cut sequence of 25-01 is no longer a hand-written heuristic. That is Chapter 25 looking in a mirror: the cutting-plane algorithm became training data.

**Exercise.** Encode a 2-layer ReLU toy $$f(x)=W_2\,\mathrm{ReLU}(W_1 x)$$ with $$W_1\in\mathbb{R}^{3\times 2}$$ as a MILP (binaries for the three hidden units). Maximize $$f(x)_1-f(x)_2$$ subject to $$\|x-x_0\|_\infty\le\varepsilon$$. If the optimal value is positive, you have a certified adversarial example; if the solver proves a non-positive bound, you have a robustness certificate at $$x_0$$. Compare the MIP answer to a projected-gradient attack — the attack can *find* a flip, only the MIP can *prove* there is none.

## Sources

- D. Bertsimas, A. King, R. Mazumder, *Ann. Statist.* 44(2):813–852, 2016 — best subset via MIP.
- Model-based feature selection for NNs, [arXiv:2302.10344](https://arxiv.org/abs/2302.10344), 2023.
- V. Tjeng, K. Xiao, R. Tedrake, ICLR 2019 — MILP robustness verification.
- M. Fischetti and J. Jo, CPAIOR 2018 — deep nets as MIPs.
- D. Bertsimas and J. Dunn, *Mach. Learn.* 106:1039–1082, 2017 — optimal classification trees.
- NeurIPS 2022 RS-OCT — scalable global OCT.
- Learning to select cutting planes, [arXiv:2410.03112](https://arxiv.org/abs/2410.03112), 2024.
