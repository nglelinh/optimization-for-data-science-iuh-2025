layout: post
title: 15-05 Convergence analysis
chapter: "15"
order: 11
owner: "Minjoo Lee"
Assuming the centering step in the barrier method is solved exactly, we can obtain the following convergence results.

## Convergence Theorem
After $$k$$ centering steps, the **barrier method** satisfies the following equation. (Here, $$k$$ is the number of outer iterations.)
>$$\begin{align}
f(x^{(k)}) - f^{*} \le  \frac{m}{\mu^k t^{(0)}}
\end{align}$$

That is, to reach the desired accuracy level $$\epsilon$$ with the barrier method, you need the following number of centering steps plus one for the first centering step.

>$$\begin{align}
\frac{log(m/(t^{(0)}\epsilon))}{\log \mu} + 1
\end{align}$$

Therefore, we see that the convergence is linear, with $$O(\log 1/\epsilon )$$.

Newton's method has quadratic convergence with $$O(\log \log 1/\epsilon ) $$, but in this case, the problem is very difficult, so linear convergence is not such a bad result.

For the definitions of linear and quadratic convergence, refer to the Wiki.<br>
* Reference: [Rate of convergence](https://en.wikipedia.org/wiki/Rate_of_convergence)