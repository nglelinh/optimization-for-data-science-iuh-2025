---
layout: post
title: 14-05 Convergence analysis
chapter: '14'
order: 11
owner: Minjoo Lee
categories:
- chapter14
lang: en
---

Watch a plot of error versus iteration for damped Newton's method on a log scale and you will always see a dramatic elbow: first a steady straight ramp downward, then suddenly a vertical cliff where the error drops from $$10^{-2}$$ to $$10^{-15}$$ in four iterations. Classical convergence theory explains that exact two-act structure by splitting the algorithm into the **damped phase** (constant objective drop per step) and the **quadratically convergent pure phase** (unit steps, digits doubling).

## Background Knowledge Map: The Two-Phase Convergence Theorem

- **Pillar 1 — Three Smoothness Assumptions ($$m, L, M$$):** Strong convexity ($$mI \preceq \nabla^2 f(x)$$), gradient smoothness ($$\nabla^2 f(x) \preceq LI$$), and Hessian Lipschitz continuity ($$\|\nabla^2 f(x) - \nabla^2 f(y)\|_2 \le M\|x-y\|_2$$) control how faithfully the local quadratic tracks $$f$$.
- **Pillar 2 — Phase I (Damped Phase, $$\|\nabla f(x^{(k)})\|_2 \ge \eta$$):** Backtracking guarantees a fixed minimum drop $$f(x^{(k+1)}) - f(x^{(k)}) \le -\gamma$$ at every iteration, bounding the total number of damped steps by $$(f(x^{(0)}) - f^\star)/\gamma$$.
- **Pillar 3 — Phase II (Pure Quadratic Phase, $$\|\nabla f(x^{(k)})\|_2 < \eta$$):** Once the gradient norm crosses below $$\eta \le \frac{m^2}{M}$$, backtracking always accepts $$t = 1$$ and the gradient norm squares at each step: $$\frac{M}{2m^2}\|\nabla f(x^{(k+1)})\|_2 \le \left(\frac{M}{2m^2}\|\nabla f(x^{(k)})\|_2\right)^2$$.
- **Pillar 4 — Total Iteration Complexity:** Combining both phases yields at most $$\frac{f(x^{(0)}) - f^\star}{\gamma} + \log_2 \log_2(\epsilon_0/\epsilon)$$ iterations—notice that reaching $$10^{-12}$$ accuracy instead of $$10^{-6}$$ costs only **one** extra Newton step!

### Step-by-Step Worked Example (Read Slowly): Computing Phase-II Quadratic Contraction Numbers

Suppose a strongly convex function has $$m = 2$$ and Hessian Lipschitz constant $$M = 1$$, so the quadratic contraction constant is $$C = \frac{M}{2m^2} = \frac{1}{8} = 0.125$$, and the Phase-II threshold is $$\eta = \frac{m^2}{M} = 4$$ (we enter Phase II safely once $$C\|\nabla f(x^{(k)})\|_2 \le \frac{1}{2}$$, i.e., $$\|\nabla f(x^{(k)})\|_2 \le 4$$).

1. **Enter Phase II at $$\|\nabla f(x^{(0)})\|_2 = 2.0$$:**
   - Scaled gradient norm: $$e_0 = C\|\nabla f(x^{(0)})\|_2 = 0.125 \times 2.0 = 0.25 = \frac{1}{4}$$.
2. **Track the guaranteed upper bound $$e_{k+1} \le e_k^2$$:**
   - Step 1: $$e_1 \le (0.25)^2 = 0.0625 \implies \|\nabla f(x^{(1)})\|_2 \le 0.5$$.
   - Step 2: $$e_2 \le (0.0625)^2 \approx 3.91 \times 10^{-3} \implies \|\nabla f(x^{(2)})\|_2 \le 0.03125$$.
   - Step 3: $$e_3 \le (3.91 \times 10^{-3})^2 \approx 1.53 \times 10^{-5} \implies \|\nabla f(x^{(3)})\|_2 \le 1.22 \times 10^{-4}$$.
   - Step 4: $$e_4 \le (1.53 \times 10^{-5})^2 \approx 2.33 \times 10^{-10} \implies \|\nabla f(x^{(4)})\|_2 \le 1.86 \times 10^{-9}$$.
3. **Suboptimality bound via strong convexity ($$f(x) - f^\star \le \frac{1}{2m}\|\nabla f(x)\|_2^2$$):**
   - After just 4 pure Newton steps, $$f(x^{(4)}) - f^\star \le \frac{(1.86 \times 10^{-9})^2}{4} \approx 8.7 \times 10^{-19}$$—past double-precision machine epsilon!

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
    });
</script>

So far, we have examined pure Newton's method, which only has local convergence properties, and damped Newton's method (Newton's method with backtracking line search), which applies backtracking line search to ensure global convergence when convex.

In this chapter, we analyze the convergence rate of damped Newton's method. For damped Newton's method, we examine convergence bounds divided into two phases: the phase where backtracking is applied (damped phase: slow progress) and the locally convergent phase where backtracking is no longer needed (pure phase: quadratic convergence).

## Conditions of $$f$$ for convergence analysis
Assume that $$f$$ is convex, twice differentiable, has $$dom(f)=\mathbb{R}^{n}$$, and satisfies the following three conditions:

1. $$\nabla f$$ is Lipschitz continuous with parameter L.
>$$\begin{align}
>\|\nabla f(x) - \nabla f(y)\|_{2} \leq L\|x-y\|_{2} \quad \forall x,y.
>\end{align}$$

2. $$f$$ is strongly convex with parameter m. (Relationship between upper bound $$L$$ and Lipschitz continuous: [source](https://xingyuzhou.org/blog/notes/strong-convexity), [this book: 06-03-05]({% multilang_post_url contents/chapter06/21-03-20-06_03_05_look_at_the_conditions_and_practicalities %}))
>$$\begin{align}
>mI\preceq\nabla^{2}f(x)\preceq LI.
>\end{align}$$
3. $$\nabla^{2} f$$ is Lipschitz continuous with parameter M.
>$$\begin{align}
>\|\nabla^{2}f(x)-\nabla^{2}f(y)\|_{2} \leq M\|x-y\|_{2} \quad \forall x,y.
>\end{align}$$

## Convergence analysis
If the above three conditions are satisfied, for $$\eta, \gamma$$ satisfying $$0<\eta \leq m^{2}/M$$ and $$\gamma>0$$, the convergence for each phase can be obtained as follows:

>Phase I : "Damped" phase, $$\|\nabla f(x^{(k)})\|_{2} \geq \eta$$,
>
>$$\begin{align}
>f(x^{(k+1)})-f(x^{(k)}) \leq -\gamma
>\end{align}$$
>
>Phase II : "Pure" phase, $$\|\nabla f(x^{(k)})\|_{2}<\eta$$, backtracking selects $$t = 1$$
>
>$$\begin{align}
>\frac{M}{2m^{2}}\|\nabla f(x^{(k+1)})\|_{2} \leq \bigg( \frac{M}{2m^{2}}\|\nabla f(x^{(k)})\|_{2} \bigg)^{2}.
>\end{align}$$

Note that once the Pure phase is reached when $$\|\nabla f(x^{(k)})\|_{2}<\eta$$ is satisfied at the $$k$$-th iteration for the first time, this condition is always satisfied for subsequent iterations.

## Convergence analysis : written in optimal value term
Now we want to compare the convergence of each phase in terms of the difference from the optimal value.

For Phase I, if we perform $$k$$ iterations starting from $$x^{(0)}$$, we can organize the equation for each step and represent it as follows:

>$$\begin{align}
>\require{cancel}
>& &\cancel{f(x^{(1)})}-f(x^{(0)}) \leq -\gamma \\\\
>& &\cancel{f(x^{(2)})}-\cancel{f(x^{(1)})} \leq -\gamma \\\\
>& &\vdots \\\\
>&+ &f(x^{(k)})-\cancel{f(x^{(k-1)})} \leq -\gamma \\\\
>&= &f(x^{(k)})-f(x^{(0)})\leq -k\gamma.
>\end{align}$$

Subtracting $$f^{\star}$$ from both sides, we obtain the following result. Let $$k_{0}$$ be the first $$k$$ that satisfies $$\|\nabla f(x^{(k)})\|_{2}<\eta$$ (the iterations $$k \le k_0$$ belong to the damped phase).
>$$\begin{align}
>f(x^{(k)})-f^{\star} \leq (f(x^{(0)})-f^{\star})-\gamma k \qquad \text{if }k \leq k_{0}
>\end{align}$$

For Phase II, assume that the iteration starts from $$k_{0}$$ and proceeds for $$k-k_{0}$$ steps. Also, using $$\|\nabla f(x^{(k_0)})\|_2<\eta \leq m^{2}/M$$ from above and strong convexity, we can organize the equation as follows (set $$a_k = \frac{M}{2m^{2}}\|\nabla f(x^{(k)})\|_{2}$$, so that $$a_{k_0} \leq \frac{1}{2}$$):
>$$\begin{align}
>& &a_{k+1} \leq a_{k}^{2}\\\\
>&\Rightarrow &a_{k} \leq a_{k_0}^{2^{k-k_{0}}} \leq \Big(\frac{1}{2}\Big)^{2^{k-k_{0}}}\\\\
>&\Rightarrow &\|\nabla f(x^{(k)})\|_{2} \leq \frac{2m^{2}}{M}\Big(\frac{1}{2}\Big)^{2^{k-k_{0}}}.
>\end{align}$$

From strong convexity, $$f(y)\geq f(x)+\nabla f(x)^{T}(y-x)+\frac{m}{2}\|y-x\|^{2}_{2}\geq f(x)-\frac{1}{2m}\|\nabla f(x)\|^{2}_{2}$$ for all $$y$$, so
>$$\begin{align}
>f(x^{(k)})-f^{\star} \leq \frac{1}{2m}\|\nabla f(x^{(k)})\|_{2}^{2}\leq \frac{2m^{3}}{M^{2}}\Big(\frac{1}{2}\Big)^{2^{k-k_{0}+1}}.
>\end{align}$$

Therefore, we can summarize the convergence according to steps, with the $$k_{0}$$-th iteration as the branch point, as follows:

>Theorem: Newton's method using backtracking line search has two-stage convergence bounds.
>$$\begin{align}
>&f(x^{(k)})-f^{\star} \leq \begin{cases} (f(x^{(0)})-f^{\star})-\gamma k \qquad &\text{if }k\leq k_{0}\\\\
\frac{2m^{3}}{M^{2}}(\frac{1}{2})^{2^{k-k_{0}+1}} \qquad &\text{if }k>k_{0}.
\end{cases}
>\end{align}$$

>Here, $$\gamma = \frac{\alpha \beta \eta^{2}m}{L^{2}}$$, $$\eta = \min\{1, 3(1-2\alpha)\}\frac{m^{2}}{M}$$, and $$k_{0}$$ is the step where the condition $$\|\nabla f(x^{(k_0)})\|_{2}<\eta$$ starts to be satisfied.

## Proof 1. Damped phase
First, we derive the damped phase that satisfies $$\|\nabla f(x)\|_{2} \geq \eta$$. We derive the convergence of the damped phase through the lower bound of the step size determined by the backtracking line search process. The Newton decrement relationship is frequently used in the proof.

>We start from the following inequality, where we set $$y=x+t\Delta x_{nt}$$ in the Taylor approximation of $$f$$ and apply the upper bound from the Lipschitz condition.
>
>$$\begin{align}
>f(x+t\Delta x_{nt}) \leq f(x)+t\nabla f(x)^{T}\Delta x_{nt} + \frac{L \|\Delta x_{nt} \|^{2}_{2} }{2}t^{2},
>\end{align}$$
>
Using the relationship between the Newton decrement, the Newton step and the Hessian matrix, together with strong convexity, we can develop this as follows.
>
>$$\begin{align}
>&\text{Since }\lambda(x)^{2}=\Delta x_{nt}^{T} \nabla^{2} f(x) \Delta x_{nt} \geq m\|\Delta x_{nt}\|^{2}_{2}\text{ and }\nabla f(x)^{T}\Delta x_{nt} = -\lambda(x)^{2},\\\\
>&f(x)+t\nabla f(x)^{T}\Delta x_{nt} + \frac{L \|\Delta x_{nt} \|^{2}_{2} }{2}t^{2} \leq f(x)-t\lambda(x)^{2} + \frac{L}{2m}t^{2}\lambda(x)^{2},
>\end{align}$$
>
>To satisfy the backtracking line search condition, we consider $$t$$ satisfying the following inequality.
>
>$$\begin{align}
>f(x+t\Delta x_{nt}) \leq f(x)-(1-\frac{L}{2m}t)t \lambda(x)^{2}, \qquad \text{ where }0<1-\frac{L}{2m}t \leq \frac{1}{2}
>\end{align}$$
>
>Let $$\hat{t}$$ be the largest $$t$$ satisfying the above; then $$\hat{t} = \frac{m}{L}$$, and substituting it into the original inequality gives
>
>$$\begin{align}
>f(x+\hat{t}\Delta x_{nt})\leq f(x)-\frac{m}{2L}\lambda(x)^{2} \leq f(x) -\alpha \hat{t} \lambda(x)^{2},
>\end{align}$$
>
>(the last inequality holds because $$\alpha < 1/2$$). Since $$0<\beta\leq 1$$ in backtracking line search, we have $$t\geq \beta \frac{m}{L}$$, and rearranging we obtain the final result.
>
>$$\begin{align}
>f(x^{+})-f(x) &\leq -\alpha t \lambda(x)^{2}\\\\
> &\leq -\alpha\beta \frac{m}{L}\lambda(x)^{2}\\\\
> &\leq -\alpha\beta \frac{m}{L^{2}}\|\nabla f(x)\|^{2}_{2}\\\\
> &\leq -\alpha\beta \eta^{2}\frac{m}{L^{2}},\\\\
> &\gamma = \alpha\beta \eta^{2}\frac{m}{L^{2}}.
>\end{align}$$

(In the third step we used $$\lambda(x)^{2} = \nabla f(x)^{T}\nabla^{2}f(x)^{-1}\nabla f(x) \geq \|\nabla f(x)\|_2^2 / L$$.)

## Proof 2. Pure phase
Now assume $$\|\nabla f(x)\|_{2} < \eta$$ and consider the pure phase (the quadratically convergent phase). The proof has two parts: we show that the update of $$t$$ in backtracking line search is not necessary, and that the convergence rate is quadratic.

>From backtracking line search, we have the following inequality.
>
>$$\begin{align}
>\eta \leq 3(1-2\alpha)\frac{m^{2}}{M}.
>\end{align}$$
>
>Also, by the Lipschitz condition, for $$t \geq 0$$ the following conditions hold.
>
>$$\begin{align}
>\|\nabla^{2}f(x+t\Delta x_{nt})-\nabla^{2}f(x)\|_{2} \leq tM \|\Delta x_{nt} \|_{2},\\\\
>| \Delta x_{nt}^{T} \big( \nabla^{2}f(x+t\Delta x_{nt})-\nabla^{2}f(x) \big) \Delta x_{nt}| \leq tM \|\Delta x_{nt} \|_{2}^{3}.
>\end{align}$$
>
>Let $$\tilde{f}(t) = f(x+t\Delta x_{nt})$$; then $$\tilde{f}''(t) = \Delta x_{nt}^{T} \nabla^{2}f(x+t\Delta x_{nt})\Delta x_{nt}$$, and substituting this gives
>
>$$\begin{align}
>\tilde{f}''(t) \leq \tilde{f}''(0)+tM\|\Delta x_{nt}\|^{3}_{2}
>\end{align}$$
>
>Using $$\tilde{f}''(0) = \lambda(x)^{2}$$ and $$\lambda(x)^{2} \geq m\|\Delta x_{nt}\|_{2}^{2}$$ (so $$\|\Delta x_{nt}\|_2^3 \le \lambda(x)^3/m^{3/2}$$), we combine the inequalities. Since $$\tilde{f}'(0) = -\lambda(x)^{2}$$, we can organize as follows.
>
>$$\begin{align}
>\tilde{f}''(t) &\leq \lambda(x)^{2} + t\frac{M}{m^{3/2}}\lambda(x)^{3}, \\\\
>\tilde{f}'(t) &\leq \tilde{f}'(0)+t\lambda(x)^{2} +t^{2}\frac{M}{2m^{3/2}}\lambda(x)^{3}\\\\
>&= -\lambda(x)^{2}+t\lambda(x)^{2} + t^{2}\frac{M}{2m^{3/2}}\lambda(x)^{3}.
>\end{align}$$
>
>Now integrate both sides.
>
>$$\begin{align}
>\tilde{f}(t) \leq \tilde{f}(0) - t\lambda(x)^{2} + t^{2} \frac{1}{2}\lambda(x)^{2} + t^{3}\frac{M}{6m^{3/2}}\lambda(x)^{3}.
>\end{align}$$
>
>Setting $$t = 1$$, we obtain the following result.
>
>$$\begin{align}
>f(x+\Delta x_{nt}) \leq f(x) -\frac{1}{2}\lambda(x)^{2} + \frac{M}{6m^{3/2}}\lambda(x)^{3}.
>\end{align}$$
>
>Now assume $$\|\nabla f(x)\|_{2}\leq \eta \leq 3(1-2\alpha)\frac{m^{2}}{M}$$. By strong convexity, $$\lambda(x) \leq \|\nabla f(x)\|_{2}/m^{1/2} \leq 3(1-2\alpha)m^{3/2}/M$$. Substituting this into the inequality above, we get
>
>$$\begin{align}
>f(x+\Delta x_{nt}) &\leq f(x) - \lambda(x)^{2}( \frac{1}{2}- \frac{M\lambda(x)}{6m^{3/2}} ) \\\\
> &\leq f(x) -\alpha \lambda(x)^{2} \\\\
> &= f(x) + \alpha \nabla f(x)^{T} \Delta x_{nt},
>\end{align}$$
>
>This means that for $$t=1$$ the backtracking line search condition is always satisfied, so $$t$$ is not decreased.

Now we prove that the convergence rate is quadratic.
>Use $$\Delta x_{nt} = -(\nabla^{2}f(x))^{-1}\nabla f(x)$$ and the integral identity $$\nabla f(x+\Delta x_{nt}) - \nabla f(x) = \int^{1}_{0}{\nabla^{2}f(x+t\Delta x_{nt})\Delta x_{nt}\, dt}$$, apply the Lipschitz condition of the Hessian to the integral and organize. Finally, applying the strong convexity condition completes the proof. The process is written out as follows.
>
>$$\begin{align}
>\| \nabla f(x^{+}) \| _{2} &= \| \nabla f(x+\Delta x_{nt}) - \nabla f(x) - \nabla^{2}f(x)\Delta x_{nt} \|_{2}\\\\
>&=\| \int^{1}_{0}{ \big( \nabla^{2}f(x+t\Delta x_{nt})-\nabla^{2} f(x) \big) \Delta x_{nt} dt } \|_{2}\\\\
> & \leq \frac{M}{2}\|\Delta x_{nt} \|^{2}_{2}\\\\
> & = \frac{M}{2}\|\nabla^{2}f(x)^{-1}\nabla f(x)\|^{2}_{2}\\\\
> & \leq \frac{M}{2m^{2}}\|\nabla f(x)\|^{2}_{2}.
>\end{align}$$

To summarize: when $$\eta = \min \{1, 3(1-2\alpha)\}\frac{m^{2}}{M}$$ and $$\|\nabla f(x^{(k)}) \|_{2}<\eta$$, Newton's method no longer needs updates in backtracking line search and converges quadratically.

## Estimating total complexity
Now we can estimate the bound on the complexity of the entire process, in other words, the number of iterations required to go from the initial value to the optimal value.
First, in the damped Newton phase above, $$f$$ decreases by at least $$\gamma$$ at each iteration, so the total number of damped Newton steps cannot exceed the value of the following expression.
>$$\begin{align}
>\frac{f(x^{(0)})-p^{\star}}{\gamma}.
>\end{align}$$

The bound on the number of iterations in the pure Newton phase can also be calculated. Set $$f(x)-p^{\star}\leq \epsilon$$ and $$\epsilon_{0} = \frac{2m^{3}}{M^{2}}$$ in the formula above and solve for the number of iterations to obtain the following.
>$$\begin{align}
>& &\epsilon = \epsilon_{0} (\frac{1}{2})^{2^{k-k_{0}+1}}\\\\
>&\Leftrightarrow &\frac{\epsilon_{0}}{\epsilon} = 2^{2^{k-k_{0}+1}}\\\\
>&\Leftrightarrow &k-k_{0}+1 = \log_{2}\log_{2}(\frac{\epsilon_{0}}{\epsilon})
>\end{align}$$

Therefore, the number of iterations in the pure Newton phase is bounded by $$\log \log(\frac{\epsilon_{0}}{\epsilon})$$.

Adding these two results, we obtain an upper bound on the number of iterations required to reach a solution of the desired precision with Newton's method.
>$$\begin{align}
>\frac{f(x^{(0)})-p^{\star}}{\gamma} + \log_2 \log_2 (\frac{\epsilon_{0}}{\epsilon}).
>\end{align}$$

Compared with the change in the required precision $$\epsilon$$, the second term on the right side changes very little, so in practice it is treated as a constant when estimating. It is generally known that 6 iterations give a precision of $$\epsilon \approx 5\cdot 10^{-20}\epsilon_{0}$$.

In general, the number of iterations required to minimize the objective function $$f$$ is
>$$\begin{align}
>\frac{f(x^{(0)})-p^{\star}}{\gamma} + 6.
>\end{align}$$
