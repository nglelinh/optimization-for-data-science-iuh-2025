---
layout: post
title: '09-01 Proximal gradient descent'
chapter: '09'
order: 2
owner: Kyeongmin Woo
categories:
- chapter09
lang: en
---

When minimizing a smooth function $$g$$, gradient descent works because $$x - t\nabla g(x)$$ minimizes the local quadratic model $$g(x) + \nabla g(x)^\top(z - x) + \frac{1}{2t}\|z - x\|_2^2$$. The breakthrough idea behind **proximal gradient descent** is stunningly simple: when your objective is $$f(x) = g(x) + h(x)$$, keep that exact quadratic model for the smooth part $$g$$, leave the nonsmooth part $$h(z)$$ *untouched*, and minimize their sum! That single design choice births the proximal operator and unlocks exact sparsity in problems like Lasso via ISTA.

## Key ideas: From Quadratic Models to Soft-Thresholding (ISTA)

- **Pillar 1 — Partial Quadratic Majorization:** Replacing $$g(z)$$ by $$g(x) + \nabla g(x)^\top(z - x) + \frac{1}{2t}\|z - x\|_2^2$$ while keeping $$h(z)$$ exact yields the update $$x^+ = \arg\min_z \left\{\frac{1}{2t}\|z - (x - t\nabla g(x))\|_2^2 + h(z)\right\}$$.
- **Pillar 2 — The Proximal Mapping $$\operatorname{prox}_{t h}(y)$$:** Because $$\frac{1}{2t}\|z - y\|_2^2$$ is strictly convex, $$\operatorname{prox}_{t h}(y)$$ is always well-defined and unique for any closed proper convex $$h$$. Importantly, $$\operatorname{prox}_{t h}$$ depends *only* on $$h$$, never on the data matrix inside $$g$$.
- **Pillar 3 — Separability & Closed-Form Soft-Thresholding:** When $$h(x) = \lambda \|x\|_1 = \sum_{j=1}^p \lambda |x_j|$$, the proximal problem decouples into $$p$$ independent 1D problems whose exact solution is coordinatewise soft-thresholding $$[S_{\lambda t}(y)]_j = \operatorname{sign}(y_j)\max(|y_j| - \lambda t, 0)$$.
- **Pillar 4 — ISTA (Iterative Shrinkage-Thresholding Algorithm):** Applying proximal gradient descent to Lasso $$g(\beta) = \frac{1}{2}\|y - X\beta\|_2^2$$, $$h(\beta) = \lambda \|\beta\|_1$$ gives $$\beta^{(k)} = S_{\lambda t}(\beta^{(k-1)} + t X^\top (y - X\beta^{(k-1)}))$$, producing exact zeros on every iteration where $$|y_j| \le \lambda t$$.

### Worked example: One Full ISTA Iteration by Hand

Consider a 2-variable Lasso problem $$\min_{\beta \in \mathbb{R}^2} \frac{1}{2}\|y - X\beta\|_2^2 + \lambda \|\beta\|_1$$ with $$X = I_2$$ (the $$2\times 2$$ identity, so $$L = \|X\|_2^2 = 1$$), $$y = (3.0, -0.4)^\top$$, and $$\lambda = 1.0$$. Start at $$\beta^{(0)} = (1.0, 1.0)^\top$$ with step size $$t = 0.5 \le 1/L$$.

1. **Compute the smooth gradient $$\nabla g(\beta^{(0)}) = -X^\top(y - X\beta^{(0)})$$:**
   $$y - X\beta^{(0)} = \begin{pmatrix}3.0 \\ -0.4\end{pmatrix} - \begin{pmatrix}1.0 \\ 1.0\end{pmatrix} = \begin{pmatrix}2.0 \\ -1.4\end{pmatrix} \implies \nabla g(\beta^{(0)}) = \begin{pmatrix}-2.0 \\ 1.4\end{pmatrix}.$$
2. **Take the gradient step on $$g$$:**
   $$u = \beta^{(0)} - t\nabla g(\beta^{(0)}) = \begin{pmatrix}1.0 \\ 1.0\end{pmatrix} - 0.5\begin{pmatrix}-2.0 \\ 1.4\end{pmatrix} = \begin{pmatrix}2.0 \\ 0.3\end{pmatrix}.$$
3. **Apply soft-thresholding $$S_{\lambda t}(u)$$ with threshold $$\lambda t = 1.0 \cdot 0.5 = 0.5$$:**
   - Coordinate 1: $$|2.0| > 0.5 \implies \beta_1^{(1)} = 2.0 - 0.5 = 1.5$$.
   - Coordinate 2: $$|0.3| \le 0.5 \implies \beta_2^{(1)} = 0$$ (exact zero!).
4. **Verify progress:** The true minimizer for $$X = I_2$$ is $$\beta^\star = S_{\lambda}(y) = (2.0, 0)^\top$$. In just one step with $$t = 0.5$$, ISTA identified the exact active support ($$\beta_2 = 0$$) and moved $$\beta_1$$ halfway from $$1.0$$ to $$2.0$$! (With $$t = 1/L = 1$$, it hits $$\beta^\star = (2.0, 0)^\top$$ in a single step.)

# Proximal gradient descent

**Proximal gradient descent** is a method for finding the optimum by decomposing the objective function into a differentiable part and a non-differentiable part. In this section, we will look at how to define functions and find the optimum in proximal gradient descent.

## Decomposable functions
Suppose the objective function $$f$$ can be decomposed into two functions $$g$$ and $$h$$.

>$$f(x) = g(x) + h(x)$$

Here, the two functions $$g$$ and $$h$$ have the following properties:

* $$g$$ is convex and differentiable. (**dom**$$(g) = \mathbb{R}^n$$)
* $$h$$ is convex and non-differentiable.

If $$f$$ is differentiable, you can find the next position using gradient descent:

>$$x^+ = x - t \cdot \nabla f(x)$$

**[Note]** In gradient descent, the function $$f$$ is approximated near $$x$$ by a second-order Taylor expansion, and the Hessian $$\nabla^2 f(x)$$ is replaced by $$\frac{1}{2t} I$$. The minimum of this approximation is chosen as the next position. (See Chapter 6 Gradient descent for details)

> \begin{align}
x^+ = \underset{z}{\text{argmin}}  \underbrace{ f(x) + \nabla f(x)^T (z - x) + \frac{1}{2t} \parallel z - x \parallel_2 ^2}_{\tilde{f}_t(z)}
\end{align}

However, if $$f$$ is not differentiable, you cannot use gradient descent. But if $$f$$ is composed as $$f = g + h$$, can't we approximate the differentiable part $$g$$ with a quadratic?

This idea leads to **Proximal gradient descent**. In this method, you adjust to the best position that is close to the location predicted by gradient descent for $$g$$ and also makes the non-differentiable function $$h$$ small. This process can be expressed as follows:

>
$$ \begin{align}
x^+ & = \underset{z}{\text{argmin}}   \tilde{g}_t(z) + h(z) \\
& = \underset{z}{\text{argmin}} \ g(x) + \nabla g(x)^T (z - x) + \frac{1}{2t} \parallel z - x \parallel_2 ^2 + h(z) \\
& = \underset{z}{\text{argmin}}  \nabla g(x)^T (z - x) + \frac{1}{2t} \parallel z - x \parallel_2 ^2 + \frac{t}{2} \parallel \nabla g(x) \parallel_2 ^2  + h(z) \\
& = \underset{z}{\text{argmin}}  \frac{1}{2t} \left ( 2t \nabla g(x)^T (z - x) + \parallel z - x \parallel_2 ^2 + t^2 \parallel \nabla g(x) \parallel_2 ^2 \right )  + h(z) \\
& = \underset{z}{\text{argmin}}  \frac{1}{2t} \left ( \parallel z - x \parallel_2 ^2 + 2t \nabla g(x)^T (z - x) + t^2 \parallel \nabla g(x) \parallel_2 ^2 \right ) + h(z) \\
& = \underset{z}{\text{argmin}}   \frac{1}{2t} \parallel z - (x - t \nabla g(x) )\parallel_2 ^2 + h(z) \\
\end{align} $$

When moving from the 2nd to the 3rd line, the term $$g(x)$$ is removed as a constant term with respect to z, and the term $$\frac{t}{2} \parallel \nabla g(x)^T \parallel_2 ^2 $$ is added. In the final equation, the first term $$\frac{1}{2t} \parallel z - (x - t \nabla g(x) )\parallel_2 ^2$$ is the term that brings it closer to the gradient update position of $$g$$, and the second term $$h(z)$$ is the term that reduces $$h$$.

## Proximal gradient descent
Proximal gradient descent starts from an initial point $$x^{(0)}$$ and iteratively applies the following update:

>$$x^{(k)} = \text{prox}_{t_k}(x^{(k-1)} - t_k \nabla g(x^{(k-1)}) )$$, $$k=1,2,3,...$$

Here, $$\text{prox}_{t}$$ is defined as the proximal mapping:

> \begin{align}
\text{prox}_{t}(x) = \underset{z}{\arg \min}  \frac{1}{2t} \parallel x - z \parallel_2^2 + h(z)
\end{align}

If we rewrite this in the update form we have seen so far, it becomes:

> \begin{align}
x^{(k)} = x^{(k-1)} - t_k \cdot G_{t_k}(x^{(k-1)}), \space \space \text{where} \space G_{t}(x) = \frac{x-\text{prox}_{t} (x - t \nabla g(x))}{t} \\
\end{align}

##  What good did this do?
What is the benefit of doing this? Could it be just changing the problem to another form of minimization problem?

The key point is that for most of the main $$h$$ functions, $$\text{prox}_{t}(\cdot)$$ can be computed analytically. In other words, it can be calculated as follows:

* The mapping function $$\text{prox}_{t}(\cdot)$$ depends only on $$h$$, not on $$g$$.
* The function $$g$$ can be very complex, but here we only need to compute the gradient $$\nabla g$$.

The convergence analysis will be done concerning the number of iterations of the algorithm. Note that in each iteration, computing $$\text{prox}_{t}(\cdot)$$ may vary in computational cost depending on $$h$$.

##  Example: ISTA
Let's look at an example of proximal gradient descent. In the previous chapter, the lasso criterion was defined as follows when $$y \in \mathbb{R}^n$$ and $$X \in \mathbb{R}^{n \times p}$$:

> \begin{align}
f(\beta) = \frac{1}{2} \parallel y - X\beta \parallel_2^2 + \lambda \parallel \beta \parallel_1 \\
\end{align}

Here, $$g(\beta) = \frac{1}{2} \parallel y - X\beta \parallel_2^2$$ and $$h(\beta) = \lambda \parallel \beta \parallel_1$$. In this case, the proximal mapping is defined as:

>
$$ \begin{align}
\text{prox}_{t}(\beta) & = \underset{z}{\text{argmin}}  \frac{1}{2t} \parallel \beta - z \parallel_2^2 + \lambda \parallel z \parallel_1 \\
& = S_{\lambda t}(\beta) \\
\end{align} $$

$$S_{\lambda t}(\beta)$$ is the soft-thresholding operator, defined as follows. (For more details, see Chapter 7 Subgradient)

> $$ \begin{align}
[S_{\lambda t}(\beta)]_i =
\begin{cases}
\beta_i - \lambda & \mbox{if } \beta_i \gt \lambda \\
0 & \mbox{if } \lambda \le \beta_i \le \lambda, i = 1, ..., n \\
\beta_i + \lambda & \mbox{if } \beta_i \lt -\lambda \\
\end{cases}
\\
\end{align} $$

Since the gradient of $$g$$ is $$\nabla g(\beta) = -X^{T} (y - X \beta)$$, the proximal gradient update is defined as:

>$$\beta^+ = S_{\lambda t}(\beta + tX^{T} (y - X \beta) )$$

This algorithm is a very simple algorithm called the **iterative soft-thresholding algorithm (ISTA)**. (Beck and Teboulle (2008), "A fast iterative shrinkage-thresholding algorithm for linear inverse problems")

In the following figure, you can clearly see the performance difference between the subgradient method and proximal gradient descent. In terms of the number of iterations, the performance of proximal gradient descent is comparable to that of gradient descent.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter09/09.01_01_ISTA.png" width="80%" height="80%">
  <figcaption style="text-align: center;">[Fig 1] Example of proximal gradient (ISTA) vs. subgradient method convergence rate [3]</figcaption>
</p>
</figure>

### Soft-thresholding: the prox of λ|x| and exact zeros (video)

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/prox-shrink_en.mp4"></video>
</div>

The prox of $$\lambda\|x\|_1$$ sends small entries to exactly zero and shrinks the others by $$\lambda$$: $$\operatorname{sign}(y)\max(|y|-\lambda,0)$$.

### Try it yourself: ISTA on a tiny lasso

<div class="opx-explainer" data-opx="ista" data-lang="en"></div>
