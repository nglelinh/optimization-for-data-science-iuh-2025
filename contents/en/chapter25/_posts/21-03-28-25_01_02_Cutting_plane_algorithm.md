---
layout: post
title: 25-01-02 Cutting plane algorithm
chapter: '25'
order: '4'
owner: YoungJae Choung
categories:
- chapter25
lang: en
---

Once you know that the convex hull $$\operatorname{conv}(S)$$ is a polyhedron, a natural algorithm leaps off the page: start with the initial LP relaxation $$P^{(0)}$$, solve it to obtain $$x^{(k)}$$, and if $$x^{(k)}$$ is fractional, ask a **separation oracle** for a valid inequality $$\pi^\top x \le \pi_0$$ that cuts off $$x^{(k)}$$. Append that inequality to form $$P^{(k+1)} \subsetneq P^{(k)}$$ and repeat. This iterative tightening loop is the pure Cutting Plane Algorithm—the conceptual engine behind both Gomory cuts and outer-approximation methods in convex optimization.

## Key ideas: Valid Inequalities, Separation, and the Cutting-Plane Loop

- **Valid Inequality Criterion:** An inequality $$\pi^\top x \le \pi_0$$ is valid for $$S = P \cap \mathbb{Z}^n$$ if $$\pi^\top x \le \pi_0$$ holds for every $$x \in S$$. Adding valid inequalities never removes any feasible integer point.
- **The Separation Problem:** Given a fractional point $$x^\star \in P \setminus \operatorname{conv}(S)$$, the separation problem asks for a valid inequality $$(\pi, \pi_0)$$ such that $$\pi^\top x^\star > \pi_0$$. By the Hyperplane Separation Theorem, such an inequality always exists!
- **Monotonic Relaxation Tightening:** Because $$S \subseteq P^{(k+1)} \subseteq P^{(k)}$$, the sequence of LP relaxation values $$z^{(0)}, z^{(1)}, z^{(2)}, \dots$$ moves monotonically toward the true integer optimum $$z_{\text{IP}}^\star$$ (non-decreasing for minimization, non-increasing for maximization).
- **Dual Simplex Re-Optimization:** After adding a single cut that violates the previous LP optimum $$x^{(k)}$$, the previous basis remains *dual feasible*—allowing the dual simplex method to re-optimize $$P^{(k+1)}$$ in just a handful of pivots instead of solving from scratch.

### Worked example: Two Iterations of the Cutting-Plane Loop

Maximize $$z = 2 x_1 + 3 x_2$$ over $$x_1, x_2 \in \mathbb{Z}_{\ge 0}$$ subject to $$P^{(0)} = \{x \ge 0 : x_1 + 2 x_2 \le 3,\ 2 x_1 + x_2 \le 3\}$$.

1. **Iteration 0 (Solve LP on $$P^{(0)}$$):**
   - Intersecting the two lines gives $$x^{(0)} = (1, 1)$$? Wait: $$1 + 2(1) = 3$$ and $$2(1) + 1 = 3$$, so $$(1,1)$$ is already integer! Let us shift the RHS to $$3.5$$ and $$2.5$$: $$P^{(0)} = \{x \ge 0 : x_1 + 2 x_2 \le 3.5,\ 2 x_1 + x_2 \le 2.5\}$$.
   - Intersecting gives $$3x_2 = 4.5 \implies x_2 = 1.5,\ x_1 = 0.5$$, so $$x^{(0)} = (0.5, 1.5)$$ with $$z^{(0)} = 2(0.5) + 3(1.5) = 5.5$$. (Fractional!)
2. **Generate Cut 1:** From $$x_1 + 2x_2 \le 3.5$$ and integrality of $$x_1, x_2$$, the left-hand side is an integer, so
   $$x_1 + 2 x_2 \le \lfloor 3.5 \rfloor = 3.$$
   Check separation: $$0.5 + 2(1.5) = 3.5 > 3$$ (cuts off $$x^{(0)}$$!).
3. **Iteration 1 (Solve LP on $$P^{(1)} = P^{(0)} \cap \{x_1 + 2x_2 \le 3\}$$):**
   - Intersecting $$x_1 + 2x_2 = 3$$ with $$2x_1 + x_2 = 2.5$$ gives $$3x_2 = 3.5 \implies x_2 = 7/6,\ x_1 = 2/3$$, with $$z^{(1)} = 2(2/3) + 3(7/6) = 29/6 \approx 4.833 < 5.5$$. (Still fractional!)
4. **Generate Cut 2:** From $$2x_1 + x_2 \le 2.5$$ and integrality, $$2x_1 + x_2 \le \lfloor 2.5 \rfloor = 2$$.
   Check separation: $$2(2/3) + 7/6 = 2.5 > 2$$ (cuts off $$x^{(1)}$$!).
5. **Iteration 2 (Solve LP on $$P^{(2)}$$):** Intersecting $$x_1 + 2x_2 \le 3$$ and $$2x_1 + x_2 \le 2$$ over $$x \ge 0$$ achieves its maximum at the integer vertex $$x^{(2)} = (0, 1)$$? Wait: at $$(0, 1.5)$$ we violate $$x_2 \in \mathbb{Z}$$; at $$(1/3, 4/3)$$ we get $$z^{(2)} = 14/3 \approx 4.667$$; one final Chvátal–Gomory cut $$x_1 + x_2 \le 1$$ (from summing the two cuts: $$3x_1 + 3x_2 \le 5 \implies x_1 + x_2 \le \lfloor 5/3 \rfloor = 1$$) immediately produces the integer optimum $$x^\star = (0, 1)$$ with $$z^\star = 3$$!

In this section, we will examine the cutting plane algorithm that can solve integer linear programs.

## Valid Inequality

To define cutting planes, let's first look at what valid inequalities are. An inequality $$\pi^{T}x \le \pi_{0}$$ is said to be valid for set $$S$$ if it satisfies the following condition. That is, if a set $$S$$ is contained in the halfspace defined by the inequality $$\pi^{T}x \le \pi_{0}$$, then this inequality can be considered valid for $$S$$.

>$$\pi^{T}x \le \pi_{0} \text{ for all } x \in S$$

An inequality must be valid to become a cutting plane.

## Cutting plane algorithm

Now let's examine the cutting plane algorithm when we have the following integer programming problem:

>$$
>\begin{align}
>\min_{x} & \quad c^{T}x \\
>\text{subject to } & \quad x \in C \\
>& \quad x_j \in \mathbb{Z}, \quad j \in J \\
>\end{align}
>$$

where $$S := \text{conv} \left \{ x \in C : x_j \in \mathbb{Z}, j \in J \right \}$$.

### Cutting plane algorithm

In the following algorithm, we denote the Convex Problem as CP and the Integer Program as IP.

1. Set $$C_{0} := C$$ and compute $$x^{(0)} := \text{argmin}_{x} \left\{c^{T}x : x \in C_{0} \right\}$$
2. for $$k = 0, 1, ..$$
   - if $$x^{k}$$ is (IP) feasible, then $$x^{k}$$ is the optimal solution, so Stop
   - else
     - Find a valid inequality $$(\pi, \pi_{0})$$ for $$S$$ that cuts off $$x^{k}$$
     - $$C_{k+1} := C_{k} \cap \{ x : \pi^{T}x \le \pi_{0} \}$$
     - $$x^{(k+1)} := \text{argmin}_{x} \left\{c^{T}x : x \in C_{k+1} \right\}$$
   - end if
   - end for

Such valid inequalities are called **cutting planes** or **cuts**. Step 1 of the algorithm involves convex relaxation to solve the CP problem. At this time, the feasible set is $$C$$. In step 2 of the algorithm, if the obtained solution is feasible for IP, we consider this solution optimal. If it is not feasible, we find a valid inequality that separates the solution $$x^{k}$$ from the set $$S$$, thereby reducing the scope of $$C_{k}$$. Then, we redefine $$C_{k+1}$$ to solve the CP problem and iterate step 2 of the algorithm.

In the figure below, the polygon represents the set $$C$$, and the CP solution is represented by the black dot. In this case, a valid inequality cuts off the solution to reduce the scope of the set $$C$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_02_valid_inequality.png" alt="[Fig1] Valid Inequality">
  <figcaption style="text-align: center;">[Fig1] Valid Inequality [3]</figcaption>
</p>
</figure>

By continuously reducing the scope of the set $$C$$ in this way, we eventually meet the feasible set $$S$$, which is the convex hull of the IP problem, allowing us to find a solution that is feasible for IP.