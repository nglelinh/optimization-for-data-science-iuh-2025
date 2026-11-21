---
layout: default
title: Interactive demos
permalink: /INTERACTIVE_DEMOS/
---

# Interactive demos and short videos

Companion visuals for **Optimization in Data Science (IUH)**. The Jekyll lessons stay in this repository; the browser demos live in [nglelinh/interactive_math](https://github.com/nglelinh/interactive_math) under `optimization/`.

**Open a demo.** Prefer the live GitHub Pages copies when they load:

`https://nglelinh.github.io/interactive_math/optimization/<file>.html`

Source (always available):

`https://github.com/nglelinh/interactive_math/blob/main/optimization/<file>.html`

A related simplex tableau lives in the same repo at [`linear-programming/simplex_optimization_demo.html`](https://github.com/nglelinh/interactive_math/blob/main/linear-programming/simplex_optimization_demo.html).

## Chapter → demo map

| Course chapter | Topic | Demo HTML (in `optimization/`) |
|----------------|-------|--------------------------------|
| [Ch.05](contents/en/chapter05/) Canonical problems | Least squares | [`least_squares_problems.html`](https://github.com/nglelinh/interactive_math/blob/main/optimization/least_squares_problems.html) |
| [Ch.05](contents/en/chapter05/) / Simplex lesson | Simplex (LP) | [`../linear-programming/simplex_optimization_demo.html`](https://github.com/nglelinh/interactive_math/blob/main/linear-programming/simplex_optimization_demo.html) |
| [Ch.06](contents/en/chapter06/) Gradient descent | 3D GD + theory | [`gradient_descent_demo.html`](https://github.com/nglelinh/interactive_math/blob/main/optimization/gradient_descent_demo.html), [`gradient_descent_illustration.html`](https://github.com/nglelinh/interactive_math/blob/main/optimization/gradient_descent_illustration.html) |
| [Ch.07](contents/en/chapter07/)–[08](contents/en/chapter08/) Subgradient | Subgradient steps | [`subgradient_demo.html`](https://github.com/nglelinh/interactive_math/blob/main/optimization/subgradient_demo.html), [`subgradient_illustration.html`](https://github.com/nglelinh/interactive_math/blob/main/optimization/subgradient_illustration.html) |
| [Ch.08](contents/en/chapter08/) / [Ch.26](contents/en/chapter26/) SGD | Stochastic gradient | [`stochastic_gradient_demo.html`](https://github.com/nglelinh/interactive_math/blob/main/optimization/stochastic_gradient_demo.html), [`stochastic_gradient_illustration.html`](https://github.com/nglelinh/interactive_math/blob/main/optimization/stochastic_gradient_illustration.html) |
| [Ch.09](contents/en/chapter09/) Proximal gradient | Prox operator + PGD | [`proximal_operator_demo.html`](https://github.com/nglelinh/interactive_math/blob/main/optimization/proximal_operator_demo.html), [`proximal_gradient_demo.html`](https://github.com/nglelinh/interactive_math/blob/main/optimization/proximal_gradient_demo.html), [`proximal_gradient_illustration.html`](https://github.com/nglelinh/interactive_math/blob/main/optimization/proximal_gradient_illustration.html) |
| [Ch.12](contents/en/chapter12/) KKT | Lagrangian / KKT | [`kkt_conditions_demo.html`](https://github.com/nglelinh/interactive_math/blob/main/optimization/kkt_conditions_demo.html), [`lagrangian_kkt_conditions.html`](https://github.com/nglelinh/interactive_math/blob/main/optimization/lagrangian_kkt_conditions.html), [`lagrangian_kkt_clean.html`](https://github.com/nglelinh/interactive_math/blob/main/optimization/lagrangian_kkt_clean.html) |
| [Ch.14](contents/en/chapter14/) Newton | Newton steps | [`newtons_method_demo.html`](https://github.com/nglelinh/interactive_math/blob/main/optimization/newtons_method_demo.html), [`newton_method_illustration.html`](https://github.com/nglelinh/interactive_math/blob/main/optimization/newton_method_illustration.html) |
| [Ch.18](contents/en/chapter18/) Quasi-Newton | BFGS-style steps | [`quasi_newton_demo.html`](https://github.com/nglelinh/interactive_math/blob/main/optimization/quasi_newton_demo.html), [`quasi_newton_illustration.html`](https://github.com/nglelinh/interactive_math/blob/main/optimization/quasi_newton_illustration.html) |
| [Ch.28](contents/en/chapter28/) Landscapes | Loss surfaces | [`loss_function_landscapes.html`](https://github.com/nglelinh/interactive_math/blob/main/optimization/loss_function_landscapes.html) |
| [Ch.29](contents/en/chapter29/) Distributed | Parallel ML cartoon | [`parallel_computing_illustration.html`](https://github.com/nglelinh/interactive_math/blob/main/optimization/parallel_computing_illustration.html) |

Demos **not** tied to a named chapter (optional lab / seminar):

- [`Nelder-Mead.html`](https://github.com/nglelinh/interactive_math/blob/main/optimization/Nelder-Mead.html) — derivative-free search
- `lagrangian_fixed.html`, `lagrangian_kkt_conditions_backup.html`, `threejs_test.html` — drafts / backups; skip in lecture

Chapters 15–17, 19–25 (barrier, IPM, proximal Newton, ADMM, Frank–Wolfe, coordinate descent, MIP) have **no** matching `interactive_math` HTML yet.

## Remotion shorts

Short lecture clips rendered with Remotion use the filename pattern

```text
optimization--<topic>-vo.mp4
```

Examples of the `<topic>` slug (match the demo stem when possible):

```text
optimization--gradient-descent-vo.mp4
optimization--stochastic-gradient-vo.mp4
optimization--proximal-gradient-vo.mp4
optimization--kkt-conditions-vo.mp4
optimization--newtons-method-vo.mp4
optimization--quasi-newton-vo.mp4
optimization--loss-landscapes-vo.mp4
```

The `-vo` suffix marks the voice-over / student-facing encode. Keep the `optimization--` prefix so clips sort together and can be attached to the chapter landings above.

## Where links appear on the site

Chapter landings **05, 06, 07, 08, 09, 12, 14, 18, 26, 28, 29** include a short “Interactive demos” box that matches the rows above. This file remains the full map.
