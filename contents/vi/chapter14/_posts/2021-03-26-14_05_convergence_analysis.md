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
Newton decrement, 증분과 hessian matrix와의 관계와 Strong convexity의 관계를 이용하여 다음과 같이 전개할 수 있다.
>
>$$\begin{align}
>&\text{ Since, }\lambda(x)^{2}=\Delta x_{nt}^{T} \nabla^{2} f(x) \geq m\|\Delta x_{nt}\|^{2}_{2},\\\\
>&f(x)+t\nabla f(x)^{T}\Delta x_{nt} + \frac{L \|\Delta x_{nt} \|^{2}_{2} }{2}t^{2} \leq f(x)-t\lambda(x)^{2} + \frac{L}{2m}t^{2}\lambda(x)^{2},
>\end{align}$$
>
>이 때, backtracking line search의 조건을 만족하기 위해서는 아래를 만족해야 한다.
>
>$$\begin{align}
>f(x+t\Delta x_{nt}) \leq f(x)-(1-\frac{L}{2m}t)t \lambda(x)^{2}, \qquad \text{ where, }0<1-\frac{L}{2m}t \leq \frac{1}{2}
>\end{align}$$
>
>위를 만족하는 t의 최소값을 $$\hat{t}$$라 할 때, $$\hat{t} = \frac{m}{L}$$이 되고, 이를 원 식에 대입하면 다음과 같다.
>
>$$\begin{align}
>f(x+\hat{t}\Delta x_{nt})\leq f(x)-\frac{m}{2L}\lambda(x)^{2} \leq f(x) -\alpha \hat{t} \lambda(x)^{2},
>\end{align}$$
>
>backtracking line search에서 $$0<\beta\leq 1$$이므로, $$t\geq \beta \frac{m}{L}$$를 만족하고, 이를 정리하여 최종 결과를 유도할 수 있다.
>
>$$\begin{align}
>f(x^{+})-f(x) &\leq -\alpha t \lambda(x)^{2}\\
> &\leq -\alpha\beta \frac{m}{L}\lambda(x)^{2}\\
> &\leq -\alpha\beta \frac{m}{L^{2}}\|\nabla f(x)\|^{2}_{2}\\
> &\leq -\alpha\beta \eta^{2}\frac{m}{L^{2}},\\
> &\gamma = \alpha\beta \eta^{2}\frac{m}{L^{2}}.
>\end{align}$$



## Proof 2. Pure phase
이제 $$\|\nabla f(x)\|_{2} < \eta$$일 때를 가정하고, Damped phase(quadratically convergent phase)를 살펴본다. 증명은 두가지 과정으로 나뉜다. backtracking line search의 t 업데이트가 필요하지 않음을 보이고, 수렴속도가 quadratic함을 보이게 된다.

>Backtracking line search로 부터 다음과 같은 식이 유도된다.
>
>$$\begin{align}
>\eta \leq 3(1-2\alpha)\frac{m^{2}}{M}.
>\end{align}$$
>
>또한, Lipschitz condition에 따라 $$t \geq 0$$에 대하여, 다음 조건을 만족한다.
>
>$$\begin{align}
>\|\nabla^{2}f(x+t\Delta x_{nt})-\nabla^{2}f(x)\|_{2} \leq tM \|\Delta x_{nt} \|_{2},\\
>| \Delta x_{nt}^{T} \big( \nabla^{2}f(x+t\Delta x_{nt})-\nabla^{2}f(x) \big) \Delta x_{nt}| \leq tM \|\Delta x_{nt} \|_{2}^{3}.
>\end{align}$$
>
>$$\tilde{f} = f(x+t\Delta x_{nt}$$)라 두면, $$\tilde{f}''(t) = \Delta x_{nt}^{T} \nabla^{2}f(x+t\Delta x_{nt})\Delta x_{nt}$$이고, 이를 대입한다.
>
>$$\begin{align}
>\tilde{f}''(t) \leq \tilde{f}''(0)+tM\|\Delta x_{nt}\|^{3}_{2} \leq tM\|\Delta x_{nt} \|^{3}_{2}
>\end{align}$$
>
>$$\tilde{f}''(0) = \lambda(x)^{2}$$이고, $$\lambda(x)^{2} \geq m\|\nabla x_{nt}\|_{2}^{2}$$ 임을 이용하고, 부등식을 합친다. $$\tilde{f}'(0) = -\lambda(x)^{2}$$이므로 다음과 같이 정리할 수 있다.
>
>$$\begin{align}
>\tilde{f}''(t) &\leq \tilde{f}''(0) + tM \| \Delta x_{nt} \| ^{3}_{2} \leq \lambda(x)^{2} + t\frac{M}{m^{3/2}}\lambda(x)^{3}, \\
>\tilde{f}'(t) &\leq \tilde{f}'(0)+t\lambda(x)^{2} +t^{2}\frac{M}{2m^{3/2}}\lambda(x)^{3},\\
>&= -\lambda(x)^{2}+t\lambda(x)^{2} + t^{2}\frac{L}{2m^{3/2}}\lambda(x)^{3}.
>\end{align}$$
>
>이제 양변을 적분한다.
>
>$$\begin{align}
>\tilde{f}(t) \leq \tilde{f}(0) - t\lambda(x)^{2} + t^{2} \frac{1}{2}\lambda(x)^{2} + t^{3}\frac{M}{6m^{3/2}}\lambda(x)^{3}.
>\end{align}$$
>
>t = 1로 두면, 아래와 같은 결과를 얻을 수 있다.
>
>$$\begin{align}
>f(x+\Delta x_{nt}) \leq f(x) -\frac{1}{2}\lambda(x)^{2} + \frac{M}{6m^{3/2}}\lambda(x)^{3}.
>\end{align}$$
>
>이제 $$\|\nabla f(x)\|_{2}\leq \eta \leq 3(1-2\alpha)\frac{m^{2}}{M}$$이라 가정하면, strong convexity 조건에 의해 $$\lambda(x) \leq 3(1-2\alpha)m^{3/2}/L$$이다. 이를 위에 부등식에 대입하면 아래와 같은 결과를 유도할 수 있다.
>
>$$\begin{align}
>f(x+\Delta x_{nt}) &\leq f(x) - \lambda(x)^{2}( \frac{1}{2}- \frac{M\lambda(x)}{6m^{3/2}} ) \\
> &\leq f(x) -\alpha \lambda(x)^{2} \\
> &= f(x) + \alpha \nabla f(x)^{T} \Delta x_{nt},
>\end{align}$$
>
>이 결과는 $$t=1$$일때 backtracking line search를 수행하더라도 항상 조건을 만족하기 때문에, $$t$$를 감소시키지 않음을 의미한다.

이제 우리는 수렴속도가 quadratic하게 줄어듬을 증명해본다.
>$$x_{nt} = -(\nabla^{2}f(x))^{-1}\nabla f(x)$$임을 이용한 뒤, 적분의 성질 중 하나인 $$f(t, u) - f(t, v) = \int^{u}_{v}{\frac{\partial f}{\partial x}(t, x) dx} $$를 이용하여 정리하고, Hessian의 Lipschitz 조건을 적분식에 적용하고 정리한다. 마지막으로 strong convexity 조건을 적용하면 증명이 완료된다. 과정을 수식으로 나타내면 아래와 같다.
>
>$$\begin{align}
>\| \nabla f(x^{+}) \| _{2} &= \| \nabla f(x+\Delta x_{nt}) - \nabla f(x) - \nabla^{2}f(x)\Delta x_{nt} \|_{2}\\\\
>&=\| \int^{1}_{0}{ \big( \nabla^{2}f(x+t\Delta x_{nt})-\nabla^{2} f(x) \big) \Delta x_{nt} dt } \|_{2}\\\\
> & \leq \frac{M}{2}\|\Delta x_{nt} \|^{2}_{2}\\\\
> & = \frac{M}{2}\|\nabla^{2}f(x)^{-1}\nabla f(x)\|^{2}_{2}\\\\
> & \leq \frac{M}{2m^{2}}\|\nabla f(x)\|^{2}_{2}.
>\end{align}$$

결론을 다시 정리하면, $$\eta = \min \{1, 3(1-2\alpha)\}\frac{m^{2}}{M}$$ 일 때, $$\|\nabla f(x^{(k)}) \|_{2}<\eta$$를 만족하는 조건에서는 Newton's method는 backtracing line search에서의 업데이트가 더이상 필요하지 않고, quadratic하게 converge 한다.

## Estimating total complexity
이제, 우리는 전체 과정에서의 complexity, 달리 말해 초기 값으로부터 최적값까지 도달하는데 걸리는 iteration 횟수에 대한 bound를 추정할 수 있다.
우선, 위의 damped Newton phase에서 $$f$$는 매 iteration마다 $$\gamma$$를 넘지 않는 선에서 값이 감소하므로, damped Newton step의 전체 step 수는 다음의 식의 결과값을 넘지 못한다.
>$$\begin{align}
>\frac{f(x^{(0)})-p^{\star}}{\gamma}.
>\end{align}$$

pure Newton phase에서의 iteration 횟수의 bound 또한 계산할 수 있다. 위의 식을 $$f(x)-p^{\star}\leq \epsilon$$, $$\epsilon_{0} = \frac{2m^{3}}{M^{2}}$$로 두고, iteration 횟수로 식을 정리하면 다음과 같은 값을 계산할 수 있다.
>$$\begin{align}
>& &\epsilon = \epsilon_{0} (\frac{1}{2})^{2^{k-k_{0}+1}}\\\\
>&\Leftrightarrow &\frac{\epsilon_{0}}{\epsilon} = 2^{2^{k-k_{0}+1}}\\\\
>&\Leftrightarrow &k-k_{0}+1 = log_{2}log_{2}(\frac{\epsilon_{0}}{\epsilon})
>\end{align}$$

따라서 pure Newton phase에서 iteration 횟수는 $$\log \log(\frac{\epsilon_{0}}{\epsilon})$$로 bound 된다.

이 두 결과를 더하면, Newton method를 통하여 원하는 정밀도의 해를 얻는데 필요한 iteration 횟수의 upper bound를 정의할 수 있다.
>$$\begin{align}
>\frac{f(x^{(0)})-p^{\star}}{\gamma} + \log \log (\frac{\epsilon_{0}}{\epsilon}).
>\end{align}$$

문제를 해결할때 요구되는 정밀도 $$\epsilon$$의 변화에 비해 우변의 두번째 항은 매우 작은 변화를 보이므로, 실제 응용에서는 이를 상수로 두고 추정을 하게 된다. 일반적으로 6번의 iteration은 $$\epsilon \approx 5\cdot 10^{-20}\epsilon_{0}$$의 정밀도를 보인다고 알려져 있다.

일반적으로 말해서, 목적함수 $$f$$를 최소화하는데 있어서 필요한 iteration 횟수는 다음과 같다.
>$$\begin{align}
>\frac{f(x^{(0)})-p^{\star}}{\gamma} + 6.
>\end{align}$$
