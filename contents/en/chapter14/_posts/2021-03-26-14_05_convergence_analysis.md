---
layout: post
title: 14-05 Convergence analysis
chapter: '14'
order: 9
owner: Minjoo Lee
categories:
- chapter14
lang: en
---
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
>Phase 2 : "Pure" phase, $$\|\nabla f(x^{(k)})\|_{2}<\eta$$, backtracking selects $$t = 1$$
>
>$$\begin{align}
>\frac{M}{2m^{2}}\|\nabla f(x^{(k+1)})\|_{2} \leq \bigg( \frac{M}{2m^{2}}\|\nabla f(x^{(k)})\|_{2} \bigg)^{2}.
>\end{align}$$

Note that once the Pure phase is reached when $$\|\nabla f(x^{(k)})\|_{2}<\eta$$ is satisfied at the $$k$$-th iteration for the first time, this condition is always satisfied for subsequent iterations.

## Convergence analysis : written in optimal value term
Now we want to compare the convergence of each phase in terms of the difference from the optimal value.

For Phase 1, if we perform k iterations starting from $$x^{(0)}$$, we can organize the equation for each step and represent it as follows:

>$$\begin{align}
>\require{cancel}
>& &\cancel{f(x^{(1)})}-f(x^{(0)}) \leq -\gamma \\\\
>& &\cancel{f(x^{(2)})}-\cancel{f(x^{(1)})} \leq -\gamma \\\\
>& &\vdots \\\\
>&+ &f(x^{(k)})-\cancel{f(x^{(k-1)})} \leq -\gamma \\\\
>&= &f(x^{(k)})-f(x^{(0)})\leq -k\gamma.
>\end{align}$$

Subtracting $$f^{\star}$$ from both sides, we can obtain the following result. Let $$k_{0}$$ be the first $$k$$ that satisfies $$\|\nabla f(x^{(k+1)})\|<\eta$$.
>$$\begin{align}
>f(x^{(k)})-f^{\star} \geq (f(x^{(0)})-f^{\star})-\gamma k \qquad \text{if }k \geq k_{0}
>\end{align}$$

For Phase 2, assume that iteration starts from $$k_{0}$$ and proceeds for $$k-k_{0}$$ steps. Also, using $$\|\nabla f(x^{(k)})\|_2<\eta \leq m^{2}/M$$ from earlier and strong convexity, we can organize the equation as follows:
>$$\begin{align}
>& &\frac{M}{2m^{2}}\|\nabla f^{(k_{0}+1)}\|_{2} \leq \big( \frac{M}{2m^{2}}\|\nabla f^{(k_{0})}\|_{2} \big) ^{2}.\\\\
>&\Leftrightarrow &\frac{M}{2m^{2}}\|\nabla f^{(k_{0}+(k-k_{0}))}\|_{2} \leq \bigg( \big( \frac{M}{2m^{2}}\|\nabla f^{(k_{0}+1)}\|_{2} \big) ^{2} \bigg)^{k-k_{0}} \leq (\frac{1}{2})^{2^{(k-k_{0})}}.\\\\
>&\Leftrightarrow &f(y)\geq f(x)+\nabla f(x)^{T}(y-x)+\frac{m}{2}\|y-x\|^{2}_{2}\geq f(x)-\frac{1}{2m}\|\nabla f(x)\|^{2}_{2}, \text{ for all }y,\\\\
>&\Leftrightarrow &f(x^{(k)})-f^{\star} \leq \frac{1}{2m}\|\nabla f(x^{k})\|_{2}^{2}\leq \frac{2m^{3}}{M^{2}}(\frac{1}{2})^{2^{k-k_{0}+1}}.
>\end{align}$$

Therefore, we can organize the convergence according to steps with the $$k_{0}$$-th iteration as the branch point as follows:

>Theorem: Newton's method using backtracking line search has two-stage convergence bounds.
>$$\begin{align}
>&f(x^{(k)})-f^{\star} \leq \begin{cases} (f(x^{(0)})-f^{\star})-\gamma k \qquad &\text{if }k\leq k_{0}\\
\frac{2m^{3}}{M^{2}}(\frac{1}{2})^{2^{k-k_{0}+1}} \qquad &\text{if }k>k_{0}.
\end{cases}
>\end{align}$$

>Here, $$\gamma = \frac{\alpha \beta^{2}\eta^{2}m}{L^{2}}$$, $$\eta = \min\{1, 3(1-2\alpha)\}\frac{m^{2}}{M}$$, and $$k_{0}$$ is the step where $$\|\nabla f(x^{k_0+1}))\|_{2}<\eta$$ starts to be satisfied.

## Proof 1. Damped phase
First, we derive the damped phase that satisfies $$\|\nabla f(x)\|_{2} \geq \eta$$. We derive the convergence of the damped phase through the lower bound of the step size determined by the backtracking line search process. The Newton decrement relationship is frequently used in the proof process.

>We start from the following equation where we set $$y=x+t\Delta x_{nt}$$ in the Taylor approximation of $$f$$ and apply the upper bound of the Lipschitz condition.
>
>$$\begin{align}
>f(x+t\Delta x_{nt}) \leq f(x)+t\nabla f(x)^{T}\Delta x_{nt} + \frac{L \|\Delta x_{nt} \|^{2}_{2} }{2}t^{2},
>\end{align}$$
>
Using the relationship between Newton decrement, increment and Hessian matrix, and the relationship with strong convexity, we can develop as follows.
>
>$$\begin{align}
>&\text{ Since, }\lambda(x)^{2}=\Delta x_{nt}^{T} \nabla^{2} f(x) \geq m\|\Delta x_{nt}\|^{2}_{2},\\\\
>&f(x)+t\nabla f(x)^{T}\Delta x_{nt} + \frac{L \|\Delta x_{nt} \|^{2}_{2} }{2}t^{2} \leq f(x)-t\lambda(x)^{2} + \frac{L}{2m}t^{2}\lambda(x)^{2},
>\end{align}$$
>
>At this time, to satisfy the conditions of backtracking line search, the following must be satisfied.
>
>$$\begin{align}
>f(x+t\Delta x_{nt}) \leq f(x)-(1-\frac{L}{2m}t)t \lambda(x)^{2}, \qquad \text{ where, }0<1-\frac{L}{2m}t \leq \frac{1}{2}
>\end{align}$$
>
>When the minimum value of t that satisfies the above is $$\hat{t}$$, we have $$\hat{t} = \frac{m}{L}$$, and substituting this into the original equation gives the following.
>
>$$\begin{align}
>f(x+\hat{t}\Delta x_{nt})\leq f(x)-\frac{m}{2L}\lambda(x)^{2} \leq f(x) -\alpha \hat{t} \lambda(x)^{2},
>\end{align}$$
>
>In backtracking line search, since $$0<\beta\leq 1$$, we satisfy $$t\geq \beta \frac{m}{L}$$, and by organizing this, we can derive the final result.
>
>$$\begin{align}
>f(x^{+})-f(x) &\leq -\alpha t \lambda(x)^{2}\\
> &\leq -\alpha\beta \frac{m}{L}\lambda(x)^{2}\\
> &\leq -\alpha\beta \frac{m}{L^{2}}\|\nabla f(x)\|^{2}_{2}\\
> &\leq -\alpha\beta \eta^{2}\frac{m}{L^{2}},\\
> &\gamma = \alpha\beta \eta^{2}\frac{m}{L^{2}}.
>\end{align}$$



## Proof 2. Pure phase
Now assume $$\|\nabla f(x)\|_{2} < \eta$$ and examine the Damped phase (quadratically convergent phase). The proof is divided into two processes. We show that the t update in backtracking line search is not necessary, and that the convergence rate is quadratic.

>The following equation is derived from backtracking line search.
>
>$$\begin{align}
>\eta \leq 3(1-2\alpha)\frac{m^{2}}{M}.
>\end{align}$$
>
>Also, according to the Lipschitz condition, for $$t \geq 0$$, the following condition is satisfied.
>
>$$\begin{align}
>\|\nabla^{2}f(x+t\Delta x_{nt})-\nabla^{2}f(x)\|_{2} \leq tM \|\Delta x_{nt} \|_{2},\\
>| \Delta x_{nt}^{T} \big( \nabla^{2}f(x+t\Delta x_{nt})-\nabla^{2}f(x) \big) \Delta x_{nt}| \leq tM \|\Delta x_{nt} \|_{2}^{3}.
>\end{align}$$
>
>Let $$\tilde{f} = f(x+t\Delta x_{nt}$$), then $$\tilde{f}''(t) = \Delta x_{nt}^{T} \nabla^{2}f(x+t\Delta x_{nt})\Delta x_{nt}$$, and substitute this.
>
>$$\begin{align}
>\tilde{f}''(t) \leq \tilde{f}''(0)+tM\|\Delta x_{nt}\|^{3}_{2} \leq tM\|\Delta x_{nt} \|^{3}_{2}
>\end{align}$$
>
>Using $$\tilde{f}''(0) = \lambda(x)^{2}$$ and $$\lambda(x)^{2} \geq m\|\nabla x_{nt}\|_{2}^{2}$$, we combine the inequalities. Since $$\tilde{f}'(0) = -\lambda(x)^{2}$$, we can organize as follows.
>
>$$\begin{align}
>\tilde{f}''(t) &\leq \tilde{f}''(0) + tM \| \Delta x_{nt} \| ^{3}_{2} \leq \lambda(x)^{2} + t\frac{M}{m^{3/2}}\lambda(x)^{3}, \\
>\tilde{f}'(t) &\leq \tilde{f}'(0)+t\lambda(x)^{2} +t^{2}\frac{M}{2m^{3/2}}\lambda(x)^{3},\\
>&= -\lambda(x)^{2}+t\lambda(x)^{2} + t^{2}\frac{L}{2m^{3/2}}\lambda(x)^{3}.
>\end{align}$$
>
>Now integrate both sides.
>
>$$\begin{align}
>\tilde{f}(t) \leq \tilde{f}(0) - t\lambda(x)^{2} + t^{2} \frac{1}{2}\lambda(x)^{2} + t^{3}\frac{M}{6m^{3/2}}\lambda(x)^{3}.
>\end{align}$$
>
>Setting t = 1, we can obtain the following result.
>
>$$\begin{align}
>f(x+\Delta x_{nt}) \leq f(x) -\frac{1}{2}\lambda(x)^{2} + \frac{M}{6m^{3/2}}\lambda(x)^{3}.
>\end{align}$$
>
>Now assuming $$\|\nabla f(x)\|_{2}\leq \eta \leq 3(1-2\alpha)\frac{m^{2}}{M}$$, by the strong convexity condition, $$\lambda(x) \leq 3(1-2\alpha)m^{3/2}/L$$. Substituting this into the above inequality, we can derive the following result.
>
>$$\begin{align}
>f(x+\Delta x_{nt}) &\leq f(x) - \lambda(x)^{2}( \frac{1}{2}- \frac{M\lambda(x)}{6m^{3/2}} ) \\
> &\leq f(x) -\alpha \lambda(x)^{2} \\
> &= f(x) + \alpha \nabla f(x)^{T} \Delta x_{nt},
>\end{align}$$
>
>This result means that when $$t=1$$, even if backtracking line search is performed, the condition is always satisfied, so $$t$$ is not decreased.

Now we prove that the convergence rate decreases quadratically.
>Using $$x_{nt} = -(\nabla^{2}f(x))^{-1}\nabla f(x)$$, we organize using one of the properties of integration: $$f(t, u) - f(t, v) = \int^{u}_{v}{\frac{\partial f}{\partial x}(t, x) dx}$$, apply the Lipschitz condition of the Hessian to the integral equation and organize. Finally, applying the strong convexity condition completes the proof. The process can be expressed mathematically as follows.
>
>$$\begin{align}
>\| \nabla f(x^{+}) \| _{2} &= \| \nabla f(x+\Delta x_{nt}) - \nabla f(x) - \nabla^{2}f(x)\Delta x_{nt} \|_{2}\\\\
>&=\| \int^{1}_{0}{ \big( \nabla^{2}f(x+t\Delta x_{nt})-\nabla^{2} f(x) \big) \Delta x_{nt} dt } \|_{2}\\\\
> & \leq \frac{M}{2}\|\Delta x_{nt} \|^{2}_{2}\\\\
> & = \frac{M}{2}\|\nabla^{2}f(x)^{-1}\nabla f(x)\|^{2}_{2}\\\\
> & \leq \frac{M}{2m^{2}}\|\nabla f(x)\|^{2}_{2}.
>\end{align}$$

To summarize the conclusion, when $$\eta = \min \{1, 3(1-2\alpha)\}\frac{m^{2}}{M}$$, under the condition that $$\|\nabla f(x^{(k)}) \|_{2}<\eta$$ is satisfied, Newton's method no longer requires updates in backtracking line search and converges quadratically.

## Estimating total complexity
Now, we can estimate the bound on the complexity of the entire process, in other words, the number of iterations required to reach the optimal value from the initial value.
First, in the damped Newton phase above, since $$f$$ decreases by no more than $$\gamma$$ at each iteration, the total number of damped Newton steps cannot exceed the result of the following equation.
>$$\begin{align}
>\frac{f(x^{(0)})-p^{\star}}{\gamma}.
>\end{align}$$

The bound on the number of iterations in the pure Newton phase can also be calculated. Setting the above equation as $$f(x)-p^{\star}\leq \epsilon$$, $$\epsilon_{0} = \frac{2m^{3}}{M^{2}}$$, and organizing the equation by the number of iterations, we can calculate the following value.
>$$\begin{align}
>& &\epsilon = \epsilon_{0} (\frac{1}{2})^{2^{k-k_{0}+1}}\\\\
>&\Leftrightarrow &\frac{\epsilon_{0}}{\epsilon} = 2^{2^{k-k_{0}+1}}\\\\
>&\Leftrightarrow &k-k_{0}+1 = log_{2}log_{2}(\frac{\epsilon_{0}}{\epsilon})
>\end{align}$$

Therefore, the number of iterations in the pure Newton phase is bounded by $$\log \log(\frac{\epsilon_{0}}{\epsilon})$$.

Adding these two results, we can define the upper bound on the number of iterations required to obtain a solution with the desired precision through Newton method.
>$$\begin{align}
>\frac{f(x^{(0)})-p^{\star}}{\gamma} + \log \log (\frac{\epsilon_{0}}{\epsilon}).
>\end{align}$$

Since the second term on the right side shows very small changes compared to the changes in precision $$\epsilon$$ required when solving problems, in practical applications, this is treated as a constant for estimation. Generally, it is known that 6 iterations show precision of $$\epsilon \approx 5\cdot 10^{-20}\epsilon_{0}$$.

Generally speaking, the number of iterations required to minimize the objective function $$f$$ is as follows.
>$$\begin{align}
>\frac{f(x^{(0)})-p^{\star}}{\gamma} + 6.
>\end{align}$$
