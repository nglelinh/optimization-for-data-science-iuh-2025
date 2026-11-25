---
layout: post
title: 22-04 Properties and variants
chapter: '22'
order: 5
owner: YoungJae Choung
categories:
- chapter22
lang: en
---

Anyone who runs vanilla Frank–Wolfe on a smooth strongly convex objective whose optimum lies on the boundary of a polytope soon notices a frustrating behavior: the iterates zig-zag wildly back and forth between the active vertices, stalling at a slow $$O(1/k)$$ crawl even though the problem is strongly convex. Why? Because classical Frank–Wolfe can only move *toward* vertices, never *away* from bad vertices already carrying weight in the convex combination. Introducing **away steps** (Wolfe 1970; analyzed by Lacoste-Julien & Jaggi 2013–2015) cures the zig-zagging completely and restores linear convergence $$O(\exp(-ck))$$ over polytopes.

## Background Knowledge Map: Curing Zig-Zagging and Unlocking Linear Rates

- **Exact Line Search and Fully Corrective Variants:** Replacing $$\gamma_k = \frac{2}{k+1}$$ with exact line search $$\gamma_k = \arg\min_{\gamma \in [0,1]} f(x^{(k-1)} + \gamma(s^{(k-1)} - x^{(k-1)}))$$ guarantees monotonic descent, while fully corrective Frank–Wolfe re-optimizes $$f$$ over the entire convex hull of discovered atoms at each step.
- **Away-Step Direction and Active Set:** Maintaining $$x^{(k-1)} = \sum_{v \in S} \alpha_v v$$, we compute both the forward atom $$s_{\text{FW}} = \arg\min_{v \in C} \langle \nabla f(x), v \rangle$$ and the worst active atom $$v_{\text{away}} = \arg\max_{v \in S} \langle \nabla f(x), v \rangle$$. Stepping along $$x - v_{\text{away}}$$ sheds weight from outdated vertices.
- **Pyramidal Width and Linear Convergence:** Over a polytope $$C = \operatorname{conv}(\mathcal{A})$$, strong convexity plus smoothness is not enough for plain FW to converge linearly when $$x^\star$$ is on a face. Away-Step FW achieves global linear convergence $$h_{k} \le (1 - \rho)^k h_0$$ governed by the polytope’s geometric **pyramidal width**.
- **Path Following for Regularization Paths:** By coupling Frank–Wolfe with warm starts across increasing norm-ball radii $$t_1 < t_2 < \dots$$, one can trace an entire regularization path at controlled suboptimality tolerance $$\varepsilon$$ in far fewer iterations than solving each $$t$$ from scratch.

### Step-by-Step Worked Example (Read Slowly): Why an Away Step Beats a Forward Step

Consider minimizing $$f(x) = \frac{1}{2}\|x - c\|_2^2$$ with $$c = (0.5, 0.5, 0)^\top$$ over the 3-simplex $$\Delta_3 = \operatorname{conv}\{e_1, e_2, e_3\}$$. The true optimum is $$x^\star = (0.5, 0.5, 0)^\top$$ on the face $$\operatorname{conv}\{e_1, e_2\}$$. Suppose our current iterate is $$x = (0.4, 0.4, 0.2)^\top$$, with active set $$S = \{e_1, e_2, e_3\}$$ and weights $$\alpha = (0.4, 0.4, 0.2)$$.

1. **Compute the gradient at $$x$$:**
   $$g = \nabla f(x) = x - c = (-0.1,\ -0.1,\ +0.2)^\top.$$
2. **Evaluate the Forward (FW) direction:**
   - The smallest coordinate of $$g$$ is $$-0.1$$ (tied at $$e_1, e_2$$). Pick $$s_{\text{FW}} = e_1 = (1, 0, 0)^\top$$.
   - Forward direction: $$d_{\text{FW}} = e_1 - x = (0.6, -0.4, -0.2)^\top$$.
   - Directional improvement (negative inner product): $$-\langle g, d_{\text{FW}} \rangle = -(-0.06 + 0.04 - 0.04) = 0.06$$.
3. **Evaluate the Away-Step direction:**
   - Among active vertices $$S = \{e_1, e_2, e_3\}$$, the largest inner product $$\langle g, v \rangle$$ is at $$v_{\text{away}} = e_3$$ (value $$+0.2$$).
   - Away direction: $$d_{\text{away}} = x - e_3 = (0.4, 0.4, -0.8)^\top$$.
   - Directional improvement: $$-\langle g, d_{\text{away}} \rangle = -(-0.04 - 0.04 - 0.16) = 0.24$$.
4. **Compare and execute the Away Step:** Since $$0.24 > 0.06$$, Away-Step FW chooses $$d_{\text{away}}$$ with maximum feasible step $$\gamma_{\max} = \frac{\alpha_{e_3}}{1 - \alpha_{e_3}} = \frac{0.2}{0.8} = 0.25$$.
   - Exact line search gives $$\gamma^\star = \frac{0.24}{\|d_{\text{away}}\|_2^2} = \frac{0.24}{0.16 + 0.16 + 0.64} = \frac{0.24}{0.96} = 0.25 = \gamma_{\max}$$.
   - Update: $$x_{\text{new}} = x + 0.25(0.4, 0.4, -0.8)^\top = (0.5, 0.5, 0)^\top = x^\star$$!
   In a **single** drop step, Away-Step FW completely removes the spurious vertex $$e_3$$ and hits the exact optimum $$x^\star$$, whereas standard FW would have zig-zagged toward $$e_1$$ and $$e_2$$ for dozens of steps.

## Some variants
Let's look at some variant conditional gradient methods:<br>
• **Line search**: Instead of fixing $$γk=2/(k+1),k=1,2,3,...$$, we use exact line search for the step size at each $$k = 1, 2, 3, . . .$$.
> $$γ_k = \arg\min_{γ∈[0,1]} f\Bigl( x^{(k−1)} + γ\bigl(s^{(k−1)} − x^{(k−1)} \bigr) \Bigr)$$

Backtracking can also be used.

• **Fully corrective**: Direct update according to the following equation.
> $$x^{(k)} = \arg\min_y f(y) \: \text{ subject to } y ∈ conv\{ x^{(0)}, s^{(0)}, . . . s^{(k−1)} \}$$

This method can achieve much better progress, but the cost is high. 

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter22/away_steps.png" alt="[Fig 3] Away step motivation [3]">
  <figcaption style="text-align: center;">[Fig 3] Away step motivation [3]</figcaption>
</p>
</figure>
<br>


## Another variant: away steps
For a faster solution, let's look at the minimization problem in [Fig 3]. Here, the optimal solution is (0,0). The conditional descent method becomes difficult to move from the initial point (0,1). However, due to away step movement, conditional gradient descent not only moves to promising points but also moves away from unpromising points.



Let's assume a convex hull $$C = conv(A)$$ for atoms set $$A$$

We can explicitly represent $$x∈C$$ as a convex combination of elements belonging to $$A$$.
> $$x = \sum_{a∈A} λ_a(x)a$$

Conditional gradient with away steps: \\
$$\text{1. choose } x^{(0)} = a^{(0)} ∈ A$$ \\
$$\text{2. for } k = 1, 2, 3, . . .$$ \\
$$\qquad s^{(k−1)} ∈ \arg\min_{a∈A} ∇f(x^{(k−1)})^Ta,$$
$$\qquad a^{(k−1)} ∈ \arg\max_{a∈A, λa(x(k−1))>0} ∇f(x^{(k−1)})^Ta$$
$$\qquad \text{choose } v = s^{(k−1)} − x^{(k−1)} or \quad v = x^{(k−1)} − a^{(k−1)}$$
$$\qquad x^{(k)} = x^{(k−1)} + γ_kv$$ \\
$$\text{3. end for}$$


## Linear convergence
Let's consider the following unconstrained problem.
> $$\min_x f(x) \: \text{ subject to } x ∈ \mathbb{R}^n$$

Here, $$f$$ is µ-strongly convex and $$∇f$$ is L-Lipschitz.

By iterating gradient descent $$x^{(k+1)} = x^{(k)} − t_k∇f(x^{(k)})$$ with $$t_k = 1/L$$, the following is satisfied.
> $$f(x^{(k)}) − f^{\star} ≤ \Bigl( 1 −\frac{µ}{L} \Bigr)^k \bigl( f(x^{(0)}) − f^{\star} \bigr)$$

Now let's also consider the following constrained problem.
> $$\min_x f(x) \: \text{ subject to } x ∈ conv(A) ⊆ \mathbb{R}^n$$

### [Theorem (Lacoste-Julien & Jaggi 2013)]
Assume that $$f$$ is µ-strongly convex, $$∇f$$ is L-Lipschitz, and $$A ⊆ \mathbb{R}^n$$ is finite.

With appropriate $$γ_k$$, the iteration steps generated by the conditional gradient algorithm always satisfy the following. 
> $$f(x^{(k)}) − f^{\star} ≤ (1 − r)^{k/2}(f(x^{(0)}) − f^{\star}) \text { for } r = \frac{µ}{L}·\frac{Φ(A)^2}{4\text{diam}(A)^2}$$
> $$\text{where }Φ(A) = \min_{F ∈faces(conv(A))} dist(F, conv(A \ F))$$
 
If the polytope is planar, $$Φ$$ is small and the algorithm converges slowly.


## Path following
Let's look at the following given norm constrained problem 
> $$\min_x f(x) \: \text{ subject to } \| x \| ≤ t$$

The Frank-Wolfe algorithm can be used for **path following**. In other words, it means that it can generate a (approximate) solution path $$\hat{x}(t), t ≥ 0$$.

Starting with $$t_0 = 0$$ and $$x^{\star}(0) = 0$$, fix parameters $$\epsilon, m > 0$$ and then iterate for $$k=1,2,3,...$$.

* Compute $$t_k = t_{k−1} + \frac{(1 − 1/m)\epsilon}{\| ∇f(\hat{x}(t_k−1))\|\_{∗}}$$ and set $$\hat{x}(t) = \hat{x}(t_{k−1})$$ for all $$t ∈ (t_{k−1}, t_k)$$.

* At $$t = t_k$$, execute Frank-Wolfe to compute $$\hat{x}(t_k)$$ and terminate when the duality gap is $$≤ \frac{\epsilon}{m}$$.

This is a method that simplifies existing strategies. [Giesen et al. (2012)]

Through this **path following** strategy, we can guarantee the following for all visited $t$:
> $$f(\hat{x}(t)) − f(x^{\star}(t)) ≤ \epsilon$$

That is, it generates a case of suboptimality gap that is uniformly bounded by $$\epsilon$$ for all $$t$$.

As shown in the equation below, the Frank-Wolfe duality gap can be redefined as follows:
> $$g_t(x) = \max_{\|s\|≤1} ∇f(x)^T(x − s) = ∇f(x)^Tx + t\|∇f(x)\|_{∗}$$

This is a linear function with respect to $t$. Therefore, if $$g_t(x) ≤ \frac{\epsilon}{m}$$, we can increase $$t$$ to $$t^+ = t + (1 − 1/m)\epsilon/\|∇f(x)\|_{∗}$$ using the following equation.

> $$g_t+ (x) = ∇f(x)^Tx + t\|∇f(x)\|_{∗} + \epsilon − \epsilon/m ≤ \epsilon$$

That is, the duality gap is maintained at $$≤ \epsilon$$ between $$t$$ and $$t^+$$ for the same $$x$$.

