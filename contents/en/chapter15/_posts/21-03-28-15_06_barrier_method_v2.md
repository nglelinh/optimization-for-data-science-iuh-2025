---
layout: post
title: 15-06 Barrier method v.2
chapter: '15'
order: '12'
owner: Minjoo Lee
categories:
- chapter15
lang: en
---

Here is a practical secret of every real interior-point solver: *nobody actually cares about the central path for its own sake!* The central path is merely a highway leading to $$x^\star$$. Spending 12 Newton steps to compute $$x^*(t^{(k)})$$ to 15 decimal places when you are immediately going to bump $$t$$ up by a factor of 10 anyway is pure wasted work. **Barrier Method v.2** replaces exact centering with *approximate* centering—stopping Newton as soon as $$\lambda(x)$$ is moderately small—and achieves the exact same accuracy in a fraction of the total Newton steps!

## Key ideas: Inexact Centering & Total Newton Complexity

- **Pillar 1 — Central Path as "Means to an End":** Intermediate iterates $$x^{(k)} \approx x^*(t^{(k)})$$ only need to stay inside Newton's local neighborhood of the central path—not sit on it to machine precision.
- **Pillar 2 — Stopping Criterion for Inner Newton Steps:** Using the Newton decrement $$\frac{1}{2}\lambda_t(x)^2 \le \epsilon_{\text{inner}}$$ (or $$\lambda_t(x) \le \eta$$) cleanly terminates each approximate centering step without wasted iterations.
- **Pillar 3 — Total Newton Complexity via Self-Concordance:** Combining the outer loop with Nesterov–Nemirovskii's self-concordance bound proves that total Newton steps grow only as $$O\left(\sqrt{m}\log\left(\frac{m}{t^{(0)}\epsilon}\right)\right)$$ in theory—and roughly 20–40 total steps *independent of $$m$$* in practice!
- **Pillar 4 — Bottleneck Shifts to Linear Algebra:** Because total Newton iterations barely change from $$m = 100$$ to $$m = 100{,}000$$, the true runtime of modern IPMs is governed almost entirely by the sparse KKT factorization cost per Newton step.

### Worked example: Comparing Exact vs. Inexact Centering Work

Suppose a barrier solve requires $$8$$ outer iterations ($$\mu = 10$$) from $$t = 1$$ to $$t = 10^8$$. At each outer step, after bumping $$t \leftarrow 10t$$, suppose the warm-started iterate has Newton decrement $$\lambda \approx 0.4$$, and each pure Newton step squares $$\lambda$$ roughly as $$\lambda_{j+1} \approx \lambda_j^2$$.

1. **Barrier Method v.1 (Exact centering to $$\lambda \le 10^{-10}$$ at every outer step):**
   - $$\lambda: 0.4 \to 0.16 \to 0.0256 \to 6.6 \times 10^{-4} \to 4.3 \times 10^{-7} \to 1.8 \times 10^{-13}$$ (5 Newton steps per outer loop).
   - Total Newton steps: $$8 \times 5 = 40$$ steps.
2. **Barrier Method v.2 (Inexact centering to $$\lambda \le 0.2$$ on intermediate loops, exact only on the final loop):**
   - Intermediate loops (7 loops): $$\lambda: 0.4 \to 0.16 \le 0.2$$ (**1–2 Newton steps** per loop!).
   - Final loop (1 loop): 5 Newton steps to polish $$x^\star$$ to $$10^{-13}$$.
   - Total Newton steps: $$7 \times 2 + 5 = 19$$ steps—**cutting runtime in half** with zero loss in final precision!

In the previous algorithm, we generated solutions along the central path, but in reality, the central path is just a means to reach the optimal solution ("means to an end"). Therefore, it is not necessary to solve the problem exactly.

### Algorithm

For this reason, Barrier method v.2 solves the barrier problem approximately. However, in step 2, $$x^{(0)} \approx x^*(t)$$ and in step 3-2, $$x^{(k+1)} \approx x^*(t)$$ are now approximations.

The steps of the algorithm are the same as those in Barrier method v.1.

1. Choose $$t^{(0)} > 0$$ and set $$k := 0$$.
2. At $$t = t^{(0)}$$, solve the barrier problem to obtain $$x^{(0)} \approx x^*(t)$$.
3. While $$m/t > \epsilon$$<br>
   3-1. Choose $$t^{(k+1)} > t^{(k)}$$.<br>
   3-2. Initialize Newton's method with $$x^{(k)}$$ (warm start)<br>
        At $$t = t^{(k+1)}$$, solve the barrier problem to obtain $$x^{(k+1)} \approx x^*(t)$$.<br>
   end while<br>

In Barrier method v.2, the following two issues are very important:

* How close should each approximation be?
* How many Newton steps are needed at each centering step?

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_barrier_methodv2_04.png" alt="" width="70%" height="70%">
  <figcaption style="text-align: center;">[Fig 1] Analysis of Newton iterations and suboptimality gap with respect to m [1]</figcaption>
</p>
</figure>

In the following figure, you can see that when the barrier method is applied to a problem with $$m$$ constraints, linear convergence occurs even as $$m$$ becomes large. That is, it has a log scale with respect to $$m$$.

From a different perspective, the Newton steps needed (to reduce the initial suboptimal gap (duality gap) of $$10^4$$) increase slowly with respect to $$m$$. Looking at the figure below, even when $$m$$ increases significantly, about 20-30 Newton steps are needed for each centering step. However, one Newton step varies greatly depending on the size of the problem.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_barrier_methodv2_05.png" alt="" width="70%" height="70%">
  <figcaption style="text-align: center;">[Fig 2] Analysis of the number of Newton iterations as m increases [1]</figcaption>
</p>
</figure>