---
layout: post
title: 17-03 Some history
chapter: '17'
order: 7
owner: Minjoo Lee
categories:
- chapter17
lang: en
---

For thirty years after George Dantzig invented the Simplex method in 1947, linear programming lived with an extraordinary paradox: in practice, Simplex solved industrial problems in a handful of pivots, yet nobody could prove it ran in polynomial time. In 1972, Klee and Minty shattered that hope by constructing a slightly squashed hypercube that forced Simplex to visit every single one of its $$2^n$$ corners. That shockwave triggered one of the most dramatic chapters in modern applied mathematics—from Khachiyan's front-page ellipsoid theorem to Karmarkar's interior-point revolution and today's near-linear-time LP algorithms.

## Key ideas: The Complexity Arc of Linear Programming

- **Boundary-Walking (Simplex) vs. Interior-Cutting (IPM):** Simplex moves along 1D edges of the feasible polytope from vertex to vertex; while typically requiring $$O(m)$$ pivots in practice, adversarial geometry (Klee–Minty cubes) induces exponential $$2^n$$ worst-case behavior.
- **Khachiyan's Ellipsoid Breakthrough (1979):** Proved for the first time that LP is in $$\mathbf{P}$$ by enclosing the feasible set in shrinking ellipsoids—a monumental theoretical triumph that remained too slow in practice due to $$O(n^2 \log(1/\epsilon))$$ iterations.
- **Karmarkar's Projective Interior-Point Method (1984):** Combined polynomial-time complexity with practical speed by cutting straight through the interior of the polytope, sparking the primal-dual path-following revolution.
- **Self-Concordance & Modern Complexity (Renegar 1988 to Lee–Sidford):** Renegar established the $$O(\sqrt{n}\log(1/\epsilon))$$ Newton iteration bound via path-following; Nesterov and Nemirovskii generalized it to all self-concordant cones (SOCP, SDP), and recent breakthroughs (Lee–Sidford, Cohen–Lee–Song) pushed total arithmetic complexity toward matrix-multiplication time $$O(n^\omega)$$.

### Worked example: The 2D Klee–Minty Cube vs. the Analytic Center

Consider the 2D Klee–Minty LP with distortion $$\epsilon = 1/4$$:
$$\max \; x_2 \quad \text{subject to} \quad 0 \le x_1 \le 1, \quad \frac{1}{4} x_1 \le x_2 \le 1 - \frac{1}{4} x_1.$$

1. **Identify all $$2^2 = 4$$ vertices of this slightly tilted square:**
   - $$v_0 = (0, 0)$$, objective $$0$$.
   - $$v_1 = (1, 0)$$ — wait: $$x_2 \ge \frac{1}{4} x_1$$ gives $$v_1 = (1, 1/4)$$, objective $$0.25$$.
   - $$v_2 = (1, 3/4)$$, objective $$0.75$$.
   - $$v_3 = (0, 1)$$, objective $$1.00$$ (global optimum).
2. **Trace Dantzig's steepest-reduced-cost Simplex path starting from $$v_0 = (0, 0)$$:**
   Along the tilted bottom edge from $$(0, 0)$$ to $$(1, 1/4)$$, $$x_2$$ increases; in the canonical Klee–Minty parameterization (where $$x_1$$ enters first under Dantzig's rule), Simplex walks the full Hamiltonian path:
   $$(0, 0) \;\longrightarrow\; \left(1, \tfrac{1}{4}\right) \;\longrightarrow\; \left(1, \tfrac{3}{4}\right) \;\longrightarrow\; (0, 1),$$
   visiting all $$4 = 2^2$$ vertices! In $$n$$ dimensions, the same recursive tilt forces $$2^n - 1$$ pivots (for $$n = 50$$, over $$10^{15}$$ pivots).
3. **Compare with the interior-point central path:**
   An interior-point method ignores the tilted boundary corners completely. Starting near the analytic center $$x_c \approx (0.5, 0.5)$$, its central path curves smoothly upward through the interior directly toward $$(0, 1)$$. Even in $$n = 50$$ dimensions, the iteration bound scales as $$O(\sqrt{n}\log(1/\epsilon))$$—roughly $$20\text{–}30$$ Newton steps instead of $$10^{15}$$ pivots.

Generally, modern state-of-the-art LP Solvers use both Simplex method and interior-point method.

* Dantzig (1940s): Simplex method, the first method to solve the general form of LP, obtaining exact solutions without iteration. It remains one of the best-known and most studied algorithms for LP to this day.

* Klee and Minty (1972): A pathological LP with $$n$$ variables and $$2n$$ constraints. Solving with the Simplex method requires $$2^n$$ iterations.

* Khachiyan (1979): A polynomial-time algorithm for LP based on the ellipsoid method of Nemirovski and Yudin (1976), which is theoretically strong but not so in practice.

* Karmarkar (1984): An interior-point polynomial-time LP method that is quite effective and became a breakthrough research. (US Patent 4,744,026, expired in 2006).

* Renegar (1988): Newton-based interior-point algorithm for LP. It had the theoretically best computational complexity until the latest research by Lee-Sidford emerged.