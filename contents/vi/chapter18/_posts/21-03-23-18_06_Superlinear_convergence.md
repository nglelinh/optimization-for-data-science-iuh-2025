---
layout: post
title: 18-06 Superlinear convergence
chapter: '18'
order: 7
owner: Hooncheol Shin
categories:
- chapter18
lang: en
---

### Assumption1: 
> The Hessian matrix $$G$$ is Lipschitz continuous at $$x^∗$$, that is, 
> $$\| G(x) − G(x^∗)  \le L \| x − x^∗ \|,$$
> for all $$x$$ near $$x^∗$$, where $$L$$ is a positive constant.

### Assumption2: Wolfe conditions
> Assume $$t$$ is chosen (via backtracking) so that
> $$ f(x + tp) \le f(x) + \alpha_1 t \nabla f(x)^T p$$
> and
> $$ \nabla f(x + tp)^T p \ge \alpha_2 \nabla f(x)^T p$$
> for $$0 < \alpha_1 < \alpha_2 < 1.$$

* The first condition of Wolfe conditions ensures that too large a $$t$$ is not selected.
* The second condition of Wolfe conditions ensures that too small a $$t$$ is not selected.

DFP and BFGS show superlinear convergence under the above two assumptions. (reference: [Rate of convergence in Wikipedia](https://en.wikipedia.org/wiki/Rate_of_convergence))
>$$
>\lim_{k \rightarrow \infty} \frac{ \| x^{k+1} - x^\ast \| }{ \| x^k - x^\ast \| } = 0.
>$$





## Theorem (Dennis-Moré)

다음은 Quasi-Newton method의 search direction이 Newton direction을 충분히 잘 approximation하고 있을when,, solutionwith, convergence하는 processat, step length가 Wolfe conditions를 만족함을 보인다. Superlinear convergence를 보이기 for, search direction이 만족solution야하는 condition,이라고도 할 수 있다 [14].

>$$f$$가 두 번 미분 가능하고 $$x^k \rightarrow x^\ast$$ s.t. $$\nabla f(x^\ast) = 0$$이며 $$\nabla^2 f(x^\ast)$$가 positive definite이라고 let's assume. 
>
>$$\lim_{k \rightarrow \infty} \frac{\| \nabla f(x^k) + \nabla^2 f(x^k) p^k \| }{\| p^k \|} = 0.$$
>
>if, search direction $$p^k$$가 위 condition,을 만족하면, 다음 두 가지 항목을 만족하는 $$k_0$$가 존재한다.
> 
> 1. $$k \ge k_0$$about, step length $$t_k=1$$은 Wolfe conditions를 만족한다.
> 2. if, $$k \ge k_0$$about, $$t_k = 1$$이면 $$x^k \rightarrow x^\ast$$는 superlinear convergence를 보인다.
 