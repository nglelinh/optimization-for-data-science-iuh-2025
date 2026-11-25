---
layout: post
title: 07-02-01 Connection to a Convexity Geometry
chapter: '07'
order: 4
owner: Kyeongmin Woo
categories:
- chapter07
lang: en
---

At first, *constrained* optimization (staying inside a convex set $$C$$) and *nonsmooth unconstrained* optimization seem like two different worlds. A single brilliant trick from convex analysis unifies them completely: encode the constraint $$x \in C$$ as the **indicator function** $$I_C(x)$$ (which equals $$0$$ inside $$C$$ and $$+\infty$$ outside $$C$$). The moment you take the subdifferential of $$I_C(x)$$, pure geometry jumps off the page—$$\partial I_C(x)$$ is literally the **normal cone** $$N_C(x)$$!

## Background Knowledge Map: Indicator Functions and Normal Cones

1. **The Indicator Function $$I_C(x)$$**: Defined as $$I_C(x) = 0$$ for $$x \in C$$ and $$I_C(x) = +\infty$$ for $$x \notin C$$. It is convex if and only if $$C$$ is a convex set, and turns any constrained problem $$\min_{x \in C} f(x)$$ into the unconstrained problem $$\min_{x \in \mathbb{R}^n} \bigl(f(x) + I_C(x)\bigr)$$.
2. **Exact Identity $$\partial I_C(x) = N_C(x)$$**: For $$x \in C$$, $$g \in \partial I_C(x)$$ means $$I_C(y) \ge 0 + g^T(y - x)$$ for all $$y$$. For $$y \notin C$$ this holds automatically ($$+\infty \ge \text{finite}$$); for $$y \in C$$ it reduces to $$g^T(y - x) \le 0$$—the exact definition of the **normal cone** $$N_C(x)$$!
3. **Interior vs. Boundary Geometry**:
   - At an *interior* point $$x \in \operatorname{int}(C)$$, you can move in every direction inside $$C$$, forcing $$N_C(x) = \{0\}$$.
   - At a *boundary* point $$x \in \partial C$$, $$N_C(x)$$ is the outward-pointing cone of vectors forming an obtuse or right angle with every feasible direction $$y - x$$.
4. **Why This Connection Matters**: Adding $$I_C(x)$$ to $$f(x)$$ and applying $$0 \in \partial(f + I_C)(x^\star) = \partial f(x^\star) + N_C(x^\star)$$ immediately derives the first-order constrained optimality condition of Chapter 04 and powers Proximal Gradient Descent (where the prox of $$I_C$$ is Euclidean projection $$P_C$$!).

### Step-by-Step Worked Example (Read Slowly): Computing Normal Cones of the Unit Box $$C = [0, 1]^2$$

Let $$C = [0, 1] \times [0, 1]$$ be the unit square in $$\mathbb{R}^2$$. Compute $$\partial I_C(x) = N_C(x)$$ at three distinct points: an interior point, an edge midpoint, and a corner.

1. **Interior point $$x = (0.5, 0.5)$$**:
   - Small perturbations $$y = x \pm \epsilon e_1$$ and $$y = x \pm \epsilon e_2$$ all stay in $$C$$.
   - Requiring $$g^T(\pm \epsilon e_i) \le 0$$ forces $$g_1 = 0$$ and $$g_2 = 0$$. Thus $$N_C(0.5, 0.5) = \{(0, 0)\}$$.
2. **Right-edge midpoint $$x = (1, 0.5)$$**:
   - For any $$y \in [0, 1]^2$$, we have $$y_1 - 1 \le 0$$ while $$y_2 - 0.5$$ can be either positive or negative.
   - To ensure $$g_1(y_1 - 1) + g_2(y_2 - 0.5) \le 0$$ for all $$y \in C$$, we must have $$g_1 \ge 0$$ and $$g_2 = 0$$.
   - Thus $$N_C(1, 0.5) = \{(g_1, 0) : g_1 \ge 0\}$$ (the horizontal ray pointing straight out to the right).
3. **Top-right corner $$x = (1, 1)$$**:
   - For all $$y \in [0, 1]^2$$, both $$y_1 - 1 \le 0$$ and $$y_2 - 1 \le 0$$.
   - Hence $$g_1(y_1 - 1) + g_2(y_2 - 1) \le 0$$ holds for *all* $$g_1 \ge 0, g_2 \ge 0$$!
   - Thus $$N_C(1, 1) = \mathbb{R}^2_+$$ (the entire first quadrant, fanning out at $$90^\circ$$ from the corner).

For a convex set $$C \subseteq \mathbb{R}^n$$, consider the indicator function $$I_C: \mathbb{R}^n \to \mathbb{R}$$ defined as:

>
$$
I_C(x) = I\{x \in C \} =
\begin{cases}
0               &\text{if } x \in C \\
\infty         &\text{if } x \notin C 
\end{cases}
$$

The subdifferential of this function has the following geometric meaning:

### Lemma
For $$x \in C$$, the subdifferential $$\partial I_C(x)$$ coincides with the normal cone $$\mathcal{N}_C(x)$$ to the set $$C$$ at $$x$$:

>
\begin{equation}
\mathcal{N}_C(x) = \{g \in \mathbb{R}^n | g^Tx \geq g^Ty \text{  for all  } y \in C \}
\end{equation}

### Proof

By definition, the subgradient must satisfy:
>
\begin{equation}
I_C(y) \geq I_C(x) + g^T(y-x) \text{ for all } y
\end{equation}

Here, $$x \in C$$ and $$I_C(x)=0$$, so:
>
\begin{equation}
I_C(y) \geq g^T(y-x) \text{ for all } y
\end{equation}

First, for all $$y \in C$$, we have:
>
\begin{equation}
I_C(y) = 0 \geq g^T(y-x)
\end{equation}

Thus, the subgradient $$g$$ must satisfy $$g^Tx \geq g^Ty$$.

Second, for all $$y \notin C$$, $$I_C(y) = \infty$$, so the inequality holds for any value of $$g$$:
>
$$I_C(y)=\infty \geq g^T(y-x)$$

which is always true.

Since the subgradient must satisfy both conditions above, the subgradient for this function becomes:
>
$$\{g \in \mathbb{R}^n | g^Tx \geq g^Ty\}$$

This completes the proof. 

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter07/07_02_subgrad-5.png" alt="connection_to_convexity_geometry" width="80%" height="80%">
</p>
  <figcaption style="text-align: center;">[Fig 1] Normal cone [1]</figcaption>
</figure>