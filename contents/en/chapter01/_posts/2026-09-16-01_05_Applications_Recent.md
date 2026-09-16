---
layout: post
title: 01-05 Applications and recent developments
chapter: '01'
order: 8
owner: Nguyen Le Linh
categories:
- chapter01
lang: en
lesson_type: optional
---

Chapter 01 defined an optimization problem as “choose $$x\in\mathcal{C}$$ to make $$f$$ small.” That sentence is now the architecture of industrial data science: train a predictor (often by empirical risk minimization), then use the predictor inside a *downstream* decision problem, sometimes with extra constraints that encode fairness or operations limits. This lesson walks through three concrete 2022–2026 settings. The definitions in 01-01 and 01-02 stay as they are; we only change the *examples* you should be able to name.

## Large-scale ERM: compute-optimal language models

Pretraining a language model is empirical risk minimization on next-token (or masked-token) loss. Write $$N$$ for the number of parameters and $$D$$ for the number of training tokens. A fixed compute budget $$C$$ (FLOPs) roughly satisfies $$C \propto N\cdot D$$. The design question is not “is this convex?” — Transformer training is not — but *which* $$(N,D)$$ pair minimizes the loss for that $$C$$.

Hoffmann, Borgeaud, Mensch, Sifre, and colleagues (*Training Compute-Optimal Large Language Models*, [NeurIPS 2022](https://proceedings.neurips.cc/paper/2022/hash/c1e2faff6f588870935f114ebe04a3e5-Abstract-Conference.html); [arXiv:2203.15556](https://arxiv.org/abs/2203.15556)) trained more than 400 models and concluded that, for compute-optimal training, model size and token count should scale together: doubling $$N$$ should come with doubling $$D$$. Their 70B-parameter model Chinchilla, trained on about 1.4T tokens with the same compute as the 280B Gopher model, outperformed Gopher, GPT-3, and other larger-but-undertrained models on a broad suite, including 67.5% on MMLU. DeepMind’s accompanying note is [here](https://deepmind.google/blog/an-empirical-analysis-of-compute-optimal-large-language-model-training/).

For this course the moral is structural. The *form* is still

$$
\min_w \frac{1}{n}\sum_{i=1}^n \ell\bigl(h_w(x_i), y_i\bigr),
$$

but the *decision variables of the outer design problem* are $$N$$ and $$D$$, not only $$w$$. Convexity is not what makes Chinchilla work; a well-posed optimization *question* is.

## Predict, then optimize (and the SPO+ convex surrogate)

Many analytics pipelines do two jobs in sequence: predict a cost vector $$\hat{c}$$ from features, then solve

$$
\min_{z\in\mathcal{Z}} \hat{c}^\top z
$$

for a routing, inventory, or portfolio decision $$z$$. Training the predictor to minimize squared error on $$c$$ can be the wrong objective: a small error in $$\hat{c}$$ that flips the optimal vertex of $$\mathcal{Z}$$ is worse than a large error that leaves the decision unchanged.

Elmachtoub and Grigas (*Smart “Predict, then Optimize”*, [Management Science 68(1):9–26, 2022](https://doi.org/10.1287/mnsc.2020.3922); [arXiv:1710.08005](https://arxiv.org/abs/1710.08005)) define an SPO loss that charges the *decision* error induced by $$\hat{c}$$. That loss is hard to optimize, so they derive a convex surrogate **SPO+** from duality and prove Fisher consistency under mild conditions. The surrogate applies to any polyhedral, convex, or mixed-integer problem with a linear objective. Their experiments on shortest path and portfolio problems show that a linear model trained with SPO+ can beat a more flexible predictor trained on prediction error when the model is misspecified.

This is Chapter 01 in miniature: write the *true* objective (decision quality), then replace it by a convex program you can actually solve.

## Fairness as constrained optimization

Group-fairness requirements — demographic parity, equalized odds, and their relatives — are *constraints* on a classifier, not decorations on a slide. Agarwal, Beygelzimer, Dudík, Langford, and Wallach (*A Reductions Approach to Fair Classification*, [ICML 2018](https://proceedings.mlr.press/v80/agarwal18a.html)) reduce “minimize error subject to fairness inequalities” to a sequence of cost-sensitive classification problems. The feasible set of (randomized) classifiers that meet the constraints is the object you care about; the reduction finds a low-error point in that set.

The same reduction is the engine of the maintained [Fairlearn](https://fairlearn.org/) library (`ExponentiatedGradient` and related `Moment` constraints; user guide: [reductions](https://fairlearn.org/v0.12/user_guide/mitigation/reductions.html)). You will still meet this stack in 2024–2026 course projects and industry fairness reviews. The 2018 paper is older than the 2022–2026 window, but it is the reference the current software cites; treat it as the canonical *formulation*, not as a closed research topic.

A schematic program — not a claim that error and fairness are always convex — is

$$
\begin{align}
\min_h \quad & \widehat{\mathrm{err}}(h) \\
\text{s.t.} \quad & \bigl|\Pr(\hat{Y}=1\mid A=a) - \Pr(\hat{Y}=1\mid A=a')\bigr| \le \epsilon
\end{align}
$$

for a sensitive attribute $$A$$. Chapter 02 will tell you when the constraint set is convex; Chapter 04 will tell you why a local solution of a convex restriction is global.

## How to read an “optimization for DS” paper

Ask four questions that this chapter already equipped you to ask. What is the variable? What is the objective that the authors *claim* to care about, and what surrogate do they actually minimize? What is the feasible set (box constraints, simplex, fairness inequalities, integer hull)? Is the program convex, and if not, which piece is the convex inner solve? Chinchilla, SPO, and Fairlearn are three different answers to those four questions.

## Sources

1. J. Hoffmann et al., “Training Compute-Optimal Large Language Models,” NeurIPS 2022. [abstract](https://proceedings.neurips.cc/paper/2022/hash/c1e2faff6f588870935f114ebe04a3e5-Abstract-Conference.html) · [arXiv:2203.15556](https://arxiv.org/abs/2203.15556)
2. A. N. Elmachtoub and P. Grigas, “Smart ‘Predict, then Optimize’,” *Management Science* 68(1):9–26, 2022. [DOI](https://doi.org/10.1287/mnsc.2020.3922) · [arXiv:1710.08005](https://arxiv.org/abs/1710.08005)
3. A. Agarwal, A. Beygelzimer, M. Dudík, J. Langford, and H. Wallach, “A Reductions Approach to Fair Classification,” ICML 2018. [PMLR](https://proceedings.mlr.press/v80/agarwal18a.html) · [Fairlearn reductions](https://fairlearn.org/v0.12/user_guide/mitigation/reductions.html)
