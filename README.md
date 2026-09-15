# Optimization in Data Science — IUH

Bilingual (English / Vietnamese) course site for **Optimization in Data Science** at the Industrial University of Ho Chi Minh City (IUH). This repository **is** the course: lessons live under `contents/en/` and `contents/vi/` and are published at

**[https://nglelinh.github.io/optimization-for-data-science-iuh-2025/](https://nglelinh.github.io/optimization-for-data-science-iuh-2025/)**

Start here on *this* site. External lecture videos and textbooks are optional companions, not the primary reading path.

## Who this course is for

The notes are written for IUH data-science students who already know multivariable calculus and basic linear algebra, and who need optimization as the language of machine learning: empirical risk minimization, regularized models, constrained inference, and the algorithms that actually train models.

You will learn to recognize convex structure, formulate canonical programs, run first- and second-order methods, read duality and KKT conditions, and — in the 2026 modern track — connect that classical spine to SGD, adaptive optimizers, automatic differentiation, nonconvex deep-learning landscapes, and distributed / federated training.

## How to read the notes

- **English:** [`contents/en/chapter00/`](contents/en/chapter00/) … [`contents/en/chapter29/`](contents/en/chapter29/)
- **Tiếng Việt:** [`contents/vi/chapter00/`](contents/vi/chapter00/) … [`contents/vi/chapter29/`](contents/vi/chapter29/)
- Each chapter folder has a landing page (`index.html`) plus dated lesson posts in `_posts/`.
- Interactive HTML demos (gradient descent, proximal maps, Newton, KKT, …) are mapped in [INTERACTIVE_DEMOS.md](INTERACTIVE_DEMOS.md).

## Contents on this site

Links in the **Lesson** column go to the English landing page on this repository (Vietnamese: swap `/en/` for `/vi/`). Book / lecture / slide columns are *optional* CMU and Stanford companions.

| Ch | Title | Lesson (this site) | Optional lecture | Optional slides |
|:--:|:------|:-------------------|:-----------------|:----------------|
| 00 | Foundations (calculus, linear algebra, analysis, probability) | [EN](contents/en/chapter00/) · [VI](contents/vi/chapter00/) | — | — |
| 01 | Introduction | [EN](contents/en/chapter01/) · [VI](contents/vi/chapter01/) | [CMU](https://www.youtube.com/watch?v=XFKBNJ14UmY) | [CMU](http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/intro.pdf) |
| 02 | Convex sets | [EN](contents/en/chapter02/) · [VI](contents/vi/chapter02/) | [Stanford](https://www.youtube.com/watch?v=P3W_wFZ2kUo) | [Stanford](https://web.stanford.edu/class/ee364a/lectures/sets.pdf) |
| 03 | Convex functions | [EN](contents/en/chapter03/) · [VI](contents/vi/chapter03/) | [Stanford](https://www.youtube.com/watch?v=kcOodzDGV4c) | [Stanford](https://see.stanford.edu/materials/lsocoee364a/03ConvexFunctions.pdf) |
| 04 | Convex optimization basics | [EN](contents/en/chapter04/) · [VI](contents/vi/chapter04/) | [CMU](https://www.youtube.com/watch?v=Gij3dlqLUN8) | [CMU](http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/convex-opt.pdf) |
| 05 | Canonical problems (LP, QP, SOCP, SDP, …) + CVXPY lab | [EN](contents/en/chapter05/) · [VI](contents/vi/chapter05/) | [CMU](https://www.youtube.com/watch?v=pfxVy4EUqzE) | [CMU](http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/canonical-probs.pdf) |
| 06 | Gradient descent | [EN](contents/en/chapter06/) · [VI](contents/vi/chapter06/) | [CMU](https://www.youtube.com/watch?v=sLMJal3KwPs) | [CMU](http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/grad-descent.pdf) |
| 07 | Subgradients | [EN](contents/en/chapter07/) · [VI](contents/vi/chapter07/) | [CMU](https://www.youtube.com/watch?v=58pUZYUvpdQ) | [CMU](http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/subgrad.pdf) |
| 08 | Subgradient method | [EN](contents/en/chapter08/) · [VI](contents/vi/chapter08/) | [CMU](https://www.youtube.com/watch?v=n_6MxWriulk) | [CMU](http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/sg-method.pdf) |
| 09 | Proximal gradient and acceleration | [EN](contents/en/chapter09/) · [VI](contents/vi/chapter09/) | [CMU](https://www.youtube.com/watch?v=h7dniG0c2ng) | [CMU](http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/prox-grad.pdf) |
| 10 | Duality in linear programs | [EN](contents/en/chapter10/) · [VI](contents/vi/chapter10/) | [CMU](https://www.youtube.com/watch?v=OQncSb3PIWA) | [CMU](http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/dual-lps.pdf) |
| 11 | Duality in general programs | [EN](contents/en/chapter11/) · [VI](contents/vi/chapter11/) | [CMU](https://www.youtube.com/watch?v=LBHKx8PmcnQ) | [CMU](http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/dual-gen.pdf) |
| 12 | KKT conditions | [EN](contents/en/chapter12/) · [VI](contents/vi/chapter12/) | [CMU](https://www.youtube.com/watch?v=V6sL3uXNZ3g) | [CMU](http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/kkt.pdf) |
| 13 | Duality uses and correspondences | [EN](contents/en/chapter13/) · [VI](contents/vi/chapter13/) | [CMU](https://www.youtube.com/watch?v=AST64aGULkk) | [CMU](http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/dual-corres.pdf) |
| 14 | Newton's method | [EN](contents/en/chapter14/) · [VI](contents/vi/chapter14/) | [CMU](https://www.youtube.com/watch?v=1B918uZBOss) | [CMU](http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/newton.pdf) |
| 15 | Barrier method | [EN](contents/en/chapter15/) · [VI](contents/vi/chapter15/) | [CMU](https://www.youtube.com/watch?v=_DD17Mj5Y6Y) | [CMU](http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/barr-method.pdf) |
| 16 | Duality revisited | [EN](contents/en/chapter16/) · [VI](contents/vi/chapter16/) | [CMU](https://www.youtube.com/watch?v=MwOjRfU2aU8) | [CMU](http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/dual-revisited.pdf) |
| 17 | Primal–dual interior-point methods | [EN](contents/en/chapter17/) · [VI](contents/vi/chapter17/) | [CMU](https://www.youtube.com/watch?v=haktqAajo70) | [CMU](http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/primal-dual.pdf) |
| 18 | Quasi-Newton methods | [EN](contents/en/chapter18/) · [VI](contents/vi/chapter18/) | [CMU](https://www.youtube.com/watch?v=2eSrCuyPscg) | [CMU](http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/quasi-newton.pdf) |
| 19 | Proximal Newton method | [EN](contents/en/chapter19/) · [VI](contents/vi/chapter19/) | [CMU](https://www.youtube.com/watch?v=dFqMgOO6DT0) | [CMU](http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/prox-newton.pdf) |
| 20 | Dual methods | [EN](contents/en/chapter20/) · [VI](contents/vi/chapter20/) | [CMU](https://www.youtube.com/watch?v=OsnQ_QC4Fjc) | [CMU](http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/dual-meth.pdf) |
| 21 | ADMM | [EN](contents/en/chapter21/) · [VI](contents/vi/chapter21/) | [CMU](https://www.youtube.com/watch?v=1tyl_F8j3wA) | [CMU](http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/admm.pdf) |
| 22 | Conditional gradient (Frank–Wolfe) | [EN](contents/en/chapter22/) · [VI](contents/vi/chapter22/) | [CMU](https://www.youtube.com/watch?v=6u0XyY3aeBo) | [CMU](http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/cond-grad.pdf) |
| 23 | Coordinate descent | [EN](contents/en/chapter23/) · [VI](contents/vi/chapter23/) | [CMU](https://www.youtube.com/watch?v=6u0XyY3aeBo) | [CMU](http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/coord-desc.pdf) |
| 24 | Mixed-integer programming 1 | [EN](contents/en/chapter24/) · [VI](contents/vi/chapter24/) | [CMU](https://www.youtube.com/watch?v=RQmFpY9W40c) | [CMU](http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/integer1.pdf) |
| 25 | Mixed-integer programming 2 | [EN](contents/en/chapter25/) · [VI](contents/vi/chapter25/) | [CMU](https://www.youtube.com/watch?v=E9VP8sfGiIc) | [CMU](http://www.stat.cmu.edu/~ryantibs/convexopt-F16/lectures/integer2.pdf) |

## 2026 modern track

Chapters 00–25 keep the classical convex spine (sets and functions → first-order and proximal methods → duality / KKT → Newton, barrier, IPM → ADMM, Frank–Wolfe, coordinate descent, MIP). The **2026 modern track** adds the pieces that peer Opt-for-ML courses (EPFL CS-439, MIT 6.7220, USC CSCI 599) treat as first-class for data science:

| Ch | Title | Why it is here | Lesson (this site) |
|:--:|:------|:---------------|:-------------------|
| 26 | Stochastic and adaptive methods for ML | SGD / minibatch, momentum and Nesterov, AdaGrad → Adam → AdamW | [EN](contents/en/chapter26/) · [VI](contents/vi/chapter26/) |
| 27 | Automatic differentiation | Forward / reverse mode, computational graphs, backpropagation | [EN](contents/en/chapter27/) · [VI](contents/vi/chapter27/) |
| 28 | Nonconvex landscapes for deep learning | Critical points, saddles, overparameterization | [EN](contents/en/chapter28/) · [VI](contents/vi/chapter28/) |
| 29 | Distributed and federated optimization | Data-parallel SGD, FedAvg, and how they differ from ADMM in Ch.21 | [EN](contents/en/chapter29/) · [VI](contents/vi/chapter29/) |

These are starter modules: enough mathematics and code to sit in lecture, not a full rewrite of chapters 00–25. Advanced optimizer geometry (SAM, Muon, Sophia) is further reading only.

A short **CVXPY / DCP modeling lab** (Lasso or hard-margin SVM) lives in [Chapter 05](contents/en/chapter05/) next to the canonical-problem taxonomy.

Interactive demos that pair with Chapters 06, 09, 12, 14, 18 (and the SGD story in 08 / 26) are listed in [INTERACTIVE_DEMOS.md](INTERACTIVE_DEMOS.md).

## Course objectives

Students who work through the classical spine and the modern track should be able to:

- formulate an empirical-risk or constrained inference problem and say whether it is convex;
- choose among gradient, proximal, Newton, and interior-point methods with a reason;
- write a small disciplined-convex model in CVXPY and a small SGD / Adam loop by hand;
- explain what reverse-mode autodiff computes, and why overparameterized networks still train;
- contrast ADMM-style consensus with data-parallel SGD and FedAvg.

## Attribution and lineage

The classical chapters are adapted, with gratitude, from the open project **[Convex Optimization for All](https://convex-optimization-for-all.github.io/)** (ModuLabs; Jinwoo Park and co-authors — see [AUTHORS.md](AUTHORS.md)). The mathematical spine follows **Boyd & Vandenberghe**, *Convex Optimization*, and the lecture sequence of **Ryan Tibshirani** (CMU).

Read the IUH lessons first. Use the upstream COFA site, the Boyd book, and the CMU / Stanford videos when you want a second explanation — they are references, not a redirect for weekly reading.

### Primary references

- [Boyd & Vandenberghe, *Convex Optimization*](https://web.stanford.edu/~boyd/cvxbook/)
- [Stanford EE364a lecture videos (2014)](https://www.youtube.com/playlist?list=PL3940DD956CDF0622)
- [CMU Convex Optimization (2016)](http://www.stat.cmu.edu/~ryantibs/convexopt-F16/)
- [CMU Convex Optimization (2019–)](http://www.stat.cmu.edu/~ryantibs/convexopt/)
- [Baydin et al., Automatic Differentiation in Machine Learning (JMLR 2018)](https://www.jmlr.org/papers/v18/17-468.html)
- [Kingma & Ba, Adam (2015)](https://arxiv.org/abs/1412.6980) · [Loshchilov & Hutter, AdamW (ICLR 2019)](https://arxiv.org/abs/1711.05101)
- [McMahan et al., FedAvg (AISTATS 2017)](https://proceedings.mlr.press/v54/mcmahan17a.html)

## Local folders vs this repo

The **canonical course site is this GitHub repository**. A Mac folder named `LinearAlgebra/` may look like a Jekyll checkout of the same `_config.yml` but is an incomplete, misnamed scaffold (mostly Chapter 00). A Mac folder named `Optimization/` holds labs, books, midterms, and finals — teaching operations, not the deployed notes. See [AGENTS.md](AGENTS.md).

## Site theme and contributors

Theme: [Lanyon](https://github.com/poole/lanyon) by [Mark Otto](https://github.com/mdo).

Original COFA authors and reviewers are listed in [AUTHORS.md](AUTHORS.md). IUH adaptation and the 2026 modern track: Nguyen Le Linh (`nglelinh`).

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="http://www.linkedin.com/in/enfow"><img src="https://avatars.githubusercontent.com/u/31348169?v=4?s=100" width="100px;" alt="KyeongMin WOO"/><br /><sub><b>KyeongMin WOO</b></sub></a><br /><a href="https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/commits?author=enfow" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/RRoundTable"><img src="https://avatars.githubusercontent.com/u/27891090?v=4?s=100" width="100px;" alt="Wontak Ryu"/><br /><sub><b>Wontak Ryu</b></sub></a><br /><a href="https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/commits?author=RRoundTable" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/LEEMINJOO"><img src="https://avatars.githubusercontent.com/u/42792260?v=4?s=100" width="100px;" alt="LEEMINJOO"/><br /><sub><b>LEEMINJOO</b></sub></a><br /><a href="https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/commits?author=LEEMINJOO" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/hunhoon21"><img src="https://avatars.githubusercontent.com/u/36983960?v=4?s=100" width="100px;" alt="HoonCheol Shin"/><br /><sub><b>HoonCheol Shin</b></sub></a><br /><a href="https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/commits?author=hunhoon21" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/curt-park/"><img src="https://avatars.githubusercontent.com/u/14961526?v=4?s=100" width="100px;" alt="Jinwoo Park (Curt)"/><br /><sub><b>Jinwoo Park (Curt)</b></sub></a><br /><a href="https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/commits?author=Curt-Park" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/YoungJaeChoung"><img src="https://avatars.githubusercontent.com/u/29696891?v=4?s=100" width="100px;" alt="YoungJaeChoung"/><br /><sub><b>YoungJaeChoung</b></sub></a><br /><a href="https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/commits?author=YoungJaeChoung" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/isingmodel"><img src="https://avatars.githubusercontent.com/u/31462012?v=4?s=100" width="100px;" alt="Kibum Fred Kim"/><br /><sub><b>Kibum Fred Kim</b></sub></a><br /><a href="https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/commits?author=isingmodel" title="Code">💻</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/cneyang"><img src="https://avatars.githubusercontent.com/u/50402681?v=4?s=100" width="100px;" alt="Eugene Yang"/><br /><sub><b>Eugene Yang</b></sub></a><br /><a href="https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/issues?q=author%3Acneyang" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://seong7.github.io"><img src="https://avatars.githubusercontent.com/u/52827441?v=4?s=100" width="100px;" alt="Seongjin Kim"/><br /><sub><b>Seongjin Kim</b></sub></a><br /><a href="https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/commits?author=seong7" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://hgs3896.github.io"><img src="https://avatars.githubusercontent.com/u/1921149?v=4?s=100" width="100px;" alt="Ham Ji Seong"/><br /><sub><b>Ham Ji Seong</b></sub></a><br /><a href="https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/commits?author=hgs3896" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://seolhokim.github.io"><img src="https://avatars.githubusercontent.com/u/38997792?v=4?s=100" width="100px;" alt="seolhokim"/><br /><sub><b>seolhokim</b></sub></a><br /><a href="#maintenance-seolhokim" title="Maintenance">🚧</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/RektPunk"><img src="https://avatars.githubusercontent.com/u/110188257?v=4?s=100" width="100px;" alt="RektPunk"/><br /><sub><b>RektPunk</b></sub></a><br /><a href="https://github.com/convex-optimization-for-all/convex-optimization-for-all.github.io/commits?author=RektPunk" title="Documentation">📖</a></td>
    </tr>
  </tbody>
</table>
<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome.
