---
layout: post
title: 27-05 Bilevel optimization and hypergradients
chapter: '27'
order: 6
owner: Nguyen Le Linh
categories:
- chapter27
lang: en
lesson_type: optional
---

Tuning a learning rate or regularization strength $$\lambda$$ by grid search works for 2 hyperparameters, not 20,000. What if we could differentiate the *validation loss* directly with respect to $$\lambda$$ and run gradient descent on the hyperparameters themselves? That is **bilevel optimization**: an outer loop minimizes $$L_{\text{val}}(w^\star(\lambda), \lambda)$$ where the inner weights $$w^\star(\lambda) = \arg\min_w L_{\text{train}}(w, \lambda)$$ are themselves the output of an optimization problem! Computing the **hypergradient** $$\frac{d L_{\text{val}}}{d\lambda}$$ via unrolling or the Implicit Function Theorem (IFT) unifies hyperparameter optimization, MAML meta-learning, and data valuation.

## Background Knowledge Map: Bilevel Templates, Unrolling, and Implicit Differentiation

- **The Nested Bilevel Template:** Outer problem $$\min_\lambda F(\lambda) = L_{\text{val}}(w^\star(\lambda), \lambda)$$ subject to $$w^\star(\lambda) = \arg\min_w L_{\text{train}}(w, \lambda)$$. By the chain rule, $$\frac{d F}{d\lambda} = \frac{\partial L_{\text{val}}}{\partial \lambda} + \left(\frac{\partial w^\star}{\partial \lambda}\right)^\top \frac{\partial L_{\text{val}}}{\partial w}$$.
- **Method 1 — Unrolled Differentiation:** Replace $$w^\star(\lambda)$$ with $$K$$ steps of inner gradient descent $$w_K(\lambda)$$ and backpropagate through the entire $$K$$-step optimization loop. Simple to code in PyTorch/JAX, but memory scales as $$O(K \cdot d)$$ and gradients can vanish or explode for large $$K$$.
- **Method 2 — Implicit Function Theorem (IFT):** Differentiating the inner optimality condition $$\nabla_w L_{\text{train}}(w^\star(\lambda), \lambda) = 0$$ with respect to $$\lambda$$ gives the exact linear system $$\nabla_{ww}^2 L_{\text{train}} \cdot \frac{\partial w^\star}{\partial \lambda} = -\nabla_{w\lambda}^2 L_{\text{train}}$$. Using reverse-mode adjoints + conjugate gradients (or truncated Neumann series) solves for the hypergradient in $$O(d)$$ memory—independent of $$K$$!
- **Practical Trade-off:** Use unrolling when $$K$$ is tiny (e.g., 1–5 steps in MAML); use IFT when the inner solver runs hundreds of steps to near-convergence.

### Step-by-Step Worked Example (Read Slowly): Computing an Exact Hypergradient via IFT on Ridge Regression

Let $$L_{\text{train}}(w, \lambda) = \frac{1}{2}(w - 4)^2 + \frac{\lambda}{2} w^2$$ (1D ridge regression) and $$L_{\text{val}}(w) = \frac{1}{2}(w - 2)^2$$. Evaluate the hypergradient $$\frac{d L_{\text{val}}}{d\lambda}$$ at $$\lambda = 1$$.

1. **Solve the inner optimality condition $$\nabla_w L_{\text{train}}(w^\star, \lambda) = 0$$:**
   $$(w^\star - 4) + \lambda w^\star = 0 \implies w^\star(\lambda) = \frac{4}{1 + \lambda}.$$
   At $$\lambda = 1$$, $$w^\star(1) = \frac{4}{2} = 2$$? Let us make the validation target $$y_{\text{val}} = 3$$ so the hypergradient is nonzero: $$L_{\text{val}}(w) = \frac{1}{2}(w - 3)^2$$. Then at $$\lambda = 1$$, $$w^\star(1) = 2$$ and $$\frac{\partial L_{\text{val}}}{\partial w} = 2 - 3 = -1$$.
2. **Apply the Implicit Function Theorem (without differentiating the closed-form solution):**
   - Inner Hessian: $$\nabla_{ww}^2 L_{\text{train}} = 1 + \lambda = 2$$.
   - Mixed partial: $$\nabla_{w\lambda}^2 L_{\text{train}} = w^\star = 2$$.
   - IFT sensitivity: $$\frac{\partial w^\star}{\partial \lambda} = -(\nabla_{ww}^2 L_{\text{train}})^{-1} \nabla_{w\lambda}^2 L_{\text{train}} = -\frac{2}{2} = -1$$.
3. **Assemble the hypergradient:**
   $$\frac{d L_{\text{val}}}{d\lambda} = \frac{\partial L_{\text{val}}}{\partial w} \cdot \frac{\partial w^\star}{\partial \lambda} = (-1)(-1) = +1 > 0.$$
   Since the hypergradient is positive, gradient descent on $$\lambda$$ decreases $$\lambda$$—reducing shrinkage so $$w^\star$$ moves up from $$2$$ toward the validation target $$3$$!
4. **Verify directly:** $$\frac{d}{d\lambda}\left[\frac{1}{2}\left(\frac{4}{1+\lambda} - 3\right)^2\right]\Big|_{\lambda=1} = (2 - 3)\cdot \frac{-4}{(1+1)^2} = (-1)(-1) = +1$$. Exact!

Chapters 26–27 trained a model by differentiating a *single* loss with respect to weights. A surprising amount of modern machine learning is a **nested** pair of optimizations: the weights are themselves the solution of an inner problem that depends on a hyperparameter, and we want to differentiate the *outer* objective through that solution. This optional lesson is one nested template — bilevel optimization and the **hypergradient** — at IUH depth. It is not a second autodiff lecture (27-01–27-03 already own JVP / VJP) and it is not a survey of every HPO library.

The map to keep is Chen, Chen, Jiang, Ye, Wang, Yang, Poor, and Wang, *A Whole New World, but How? A Survey of Bilevel Optimization and Applications*, [arXiv:2405.04996](https://arxiv.org/abs/2405.04996) (2024), together with the classical implicit-function viewpoint in Bengio, *Gradient-Based Optimization of Hyperparameters* (2000) and the modern deep-learning treatment of Franceschi, Frasconi, Salzo, Grazzi, and Pontil (ICML 2018).

## One nested template

A **bilevel** program is

$$
\begin{align}
\min_{\lambda}\quad & F\bigl(w^\star(\lambda),\lambda\bigr)\\
\text{s.t.}\quad & w^\star(\lambda)\in\arg\min_w\, L(w,\lambda).
\end{align}
$$

The **inner** problem is ordinary training: $$L$$ is the training loss, $$w$$ the weights, $$\lambda$$ a hyperparameter that *enters the inner problem* (a learning rate, a weight-decay, a validation-weighted data filter, the initialization of a few inner steps). The **outer** objective $$F$$ is usually a validation loss, a fairness constraint, or a meta-task. The object $$\nabla_\lambda F(w^\star(\lambda),\lambda)$$ is the **hypergradient**.

This is the same template under several course names:

- **Hyperparameter optimization (HPO).** $$\lambda$$ is weight decay or a step-size; $$F$$ is validation loss. Pedestrian grid search never differentiates through $$w^\star$$; a hypergradient method does.
- **Meta-learning / MAML.** Each “task” is an inner SGD of a few steps from a shared initialization $$\lambda$$; the outer loss is performance after those steps. Finn, Abbeel, and Levine (ICML 2017) is the algorithm; the mathematics is unrolled bilevel.
- **Dataset distillation / learning to optimize.** The inner solver is a few GD steps; the outer variables are synthetic data, or even the optimizer’s own hyperparameters.
- **Implicit layers.** An equilibrium $$w=\Phi(w,\lambda)$$ is an inner fixed point; Deep Equilibrium Models differentiate through it with a vector–Jacobian product (a cousin of 27-02 / 27-03).

If you can draw the nested pair and name which gradient is the hypergradient, you can read those papers without a new theory course.

## Two ways to get the hypergradient

**Unrolling.** Replace $$w^\star(\lambda)$$ by $$T$$ steps of a differentiable inner solver, $$w_{t+1}=w_t-\eta\nabla_w L(w_t,\lambda)$$, and backpropagate through the tape. Reverse mode (27-03) gives $$\nabla_\lambda F$$ at a cost linear in $$T$$ times the cost of one inner step — exactly the memory story of a long unrolled RNN. One-step unrolling ($$T=1$$) is already enough to *feel* the chain rule; MAML-style few-shot methods live at small $$T$$.

**Implicit differentiation.** If the inner problem is smooth and the Hessian $$H=\nabla_{ww}^2 L(w^\star,\lambda)$$ is invertible at the minimizer, the implicit function theorem says

$$
\frac{\mathrm{d}w^\star}{\mathrm{d}\lambda}
=-H^{-1}\nabla_{w\lambda}^2 L(w^\star,\lambda),
$$

so the hypergradient is

$$
\nabla_\lambda F
=\nabla_\lambda F\big|_{\text{explicit}}
-\bigl(\nabla_{w\lambda}^2 L\bigr)^\top H^{-1}\nabla_w F.
$$

You never form $$H^{-1}$$: you solve $$H\,v=\nabla_w F$$ by conjugate gradients (Hessian–vector products via forward-over-reverse AD, the mixed mode mentioned in 27-03) and then contract against the mixed partial. Lorraine, Vicol, and Duvenaud (ICML 2020, *Optimizing Millions of Hyperparameters by Implicit Differentiation*) is the scalable-HPO slogan built on that solve. The invertibility hypothesis is the price: at a true inner minimizer of a strongly convex $$L$$ it is honest; on a nonconvex net that you stopped early, unrolling is often the more honest model of what you actually computed.

Approximate implicit differentiation (truncated CG, Neumann series) sits between the two. Treat it as a seminar paper, not a second set of homework knobs.

<div class="content-box insight-box">
<strong>When to unroll, when to invert.</strong>
Short inner loop, nonconvex, or “the algorithm <em>is</em> the model” (MAML, learned optimizers): unroll.
Long inner loop, strongly convex inner problem, many hyperparameters (validation-weighted training, neural architecture with a convex inner solver): implicit / CG.
Never differentiate through a full AdamW pretrain of a language model by either route — use a proxy (a short fine-tune, a linear head, a subset) or do not claim a hypergradient.
</div>

## A one-step unrolled learning-rate

The smallest honest example is a quadratic inner problem and a scalar step-size $$\lambda=\eta$$. One gradient step from $$w_0$$ gives $$w_1(\eta)=w_0-\eta\nabla L(w_0)$$. An outer loss $$F(w_1)=\tfrac12\|w_1-w_{\mathrm{val}}\|_2^2$$ then has an elementary hypergradient $$\mathrm{d}F/\mathrm{d}\eta$$ by the chain rule — no library required.

```python
import numpy as np

def one_step_hypergrad(A, b, w0, eta, w_val):
    """Inner: one GD step on 0.5 w^T A w - b^T w. Outer: 0.5 ||w1 - w_val||^2."""
    g = A @ w0 - b
    w1 = w0 - eta * g
    # d w1 / d eta = -g ; hypergrad = (w1 - w_val)^T dw1/deta
    hyper = (w1 - w_val) @ (-g)
    return w1, hyper

A = np.diag([1.0, 10.0])
b = np.array([1.0, 1.0])
w0 = np.zeros(2)
w_val = np.linalg.solve(A, b)          # pretend the val target is the minimizer
w1, dF = one_step_hypergrad(A, b, w0, eta=0.05, w_val=w_val)
print(w1, "hypergrad dF/deta", dF)
```

A negative hypergradient says “the validation loss would decrease if you *raised* $$\eta$$.” That is the entire HPO message, written without a tuner. Reverse-mode AD (PyTorch or JAX) does the same bookkeeping when $$T>1$$ or when $$L$$ is a net; you now know which tape you are asking it to play.

For a *true* inner minimizer of the same quadratic, implicit differentiation recovers $$\mathrm{d}w^\star/\mathrm{d}\lambda$$ for any hyperparameter that enters $$A$$ or $$b$$ (a ridge $$\lambda$$ is the usual classroom choice: $$L(w,\lambda)=\tfrac12\|Xw-y\|_2^2+\frac{\lambda}{2}\|w\|_2^2$$, outer loss on a validation split). The linear system is $$(X^\top X+\lambda I)v=\nabla_w F$$ — a ridge solve you already met in Chapter 05.

## What this course expects

You should be able to (i) write the nested pair for HPO and for one-step MAML, (ii) say why reverse mode on an unrolled inner loop *is* a hypergradient, (iii) write the implicit formula and name the Hessian solve, and (iv) refuse to unroll a full LLM pretrain. Chapter 26’s AdamW remains the inner *algorithm* for the models we actually train; this page is how a validation loss can talk back to a hyperparameter without a grid. Further reading, not assessed: Maclaurin, Duvenaud, and Adams (2015) on reversing SGD for HPO; Rajeswaran, Finn, Kakade, and Levine (ICML 2019) on implicit MAML; the 2024 Chen survey for the taxonomy.

**Exercise 1.** Derive $$\mathrm{d}w_1/\mathrm{d}\eta=- \nabla L(w_0)$$ for one GD step and the hypergradient of $$F(w_1)=\tfrac12\|w_1-w_{\mathrm{val}}\|_2^2$$. Then implement two steps ($$T=2$$) by hand and check against `torch.autograd` on the same quadratic.

**Exercise 2.** For ridge $$L(w,\lambda)=\tfrac12\|Xw-y\|_2^2+\frac{\lambda}{2}\|w\|_2^2$$ with a validation outer loss, write the implicit hypergradient and compute it by solving $$(X^\top X+\lambda I)v=\nabla_w F$$. Compare to differentiating a *single* GD step on the same $$L$$. When do the two numbers disagree, and which one matches “I actually ran $$T$$ steps”?

**Question.** Mixed-mode AD in 27-03 computes Hessian–vector products in time comparable to one gradient. Where, exactly, does that product appear in the implicit hypergradient — and why is that the reason Lorraine et al. can advertise “millions of hyperparameters”?

## Sources

- Y. Bengio, “Gradient-Based Optimization of Hyperparameters,” *Neural Computation*, 2000.
- L. Franceschi, P. Frasconi, S. Salzo, R. Grazzi, and M. Pontil, “Bilevel Programming for Hyperparameter Optimization and Meta-Learning,” ICML 2018.
- J. Lorraine, P. Vicol, and D. Duvenaud, “Optimizing Millions of Hyperparameters by Implicit Differentiation,” ICML 2020.
- C. Finn, P. Abbeel, and S. Levine, “Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks,” ICML 2017.
- C. Chen et al., “A Whole New World, but How?,” [arXiv:2405.04996](https://arxiv.org/abs/2405.04996), 2024.
