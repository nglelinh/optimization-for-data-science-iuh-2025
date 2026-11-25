---
layout: post
title: 06-02 How to choose step sizes
chapter: '06'
order: 5
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
lesson_type: required
---

Giving an optimizer the steepest-descent direction without a good step-size rule is like handing a driver a steering wheel with no gas pedal or brake. Step too small and your run burns hours making microscopic progress; step too big and the iterates rocket out of the valley. Section 06-02 compares the three classical step-size strategies—fixed step sizes, backtracking line search, and exact line search—so you know when each one wins.

## Background Knowledge Map: Three Classical Step-Size Paradigms

1. **Fixed Step Size ($$t_k = t$$)**: Zero extra function evaluations per iteration and trivial to implement, provided you know (or can bound) the global smoothness constant $$L$$ so that $$t \le 1/L$$. Fails or crawls when curvature varies wildly across the domain.
2. **Backtracking (Armijo) Line Search**: Starts each iteration with an optimistic step $$t = 1$$ and shrinks $$t \leftarrow \beta t$$ (with $$\beta \in (0, 1)$$) until the sufficient-decrease test $$f(x - t\nabla f(x)) \le f(x) - \alpha t\|\nabla f(x)\|_2^2$$ passes. Adapts automatically to *local* curvature without ever needing to know $$L$$!
3. **Exact Line Search**: Solves the 1D subproblem $$t_k = \arg\min_{s \ge 0} f(x_k - s\nabla f(x_k))$$ at every step. Achieves the steepest single-step drop (and makes consecutive steps orthogonal), but is only economical when the 1D minimization has a closed form—most notably for quadratic objectives.
4. **Cost-per-Iteration vs. Iteration-Count Trade-Off**: Fixed steps have the cheapest iterations; exact line search takes the fewest iterations (on well-behaved quadratics); backtracking hits the practical sweet spot for general smooth convex objectives.

### Step-by-Step Worked Example (Read Slowly): Comparing All Three Rules on One Quadratic Step

Minimize $$f(x) = \frac{1}{2}(x_1^2 + 9x_2^2)$$ from $$x^{(0)} = (3, 1)$$, where $$\nabla f(x^{(0)}) = (3, 9)$$ and $$f(x^{(0)}) = \frac{1}{2}(9 + 9) = 9$$.

1. **Fixed step size ($$t = 1/L = 1/9$$)**:
   - $$x^{(1)}_{\mathrm{fixed}} = (3, 1) - \frac{1}{9}(3, 9) = (\tfrac{8}{3},\; 0)$$.
   - New objective: $$f = \frac{1}{2}\bigl(\tfrac{64}{9} + 0\bigr) = \frac{32}{9} \approx 3.556$$.
2. **Exact line search**: Minimize $$\phi(s) = f(3 - 3s,\; 1 - 9s) = \frac{1}{2}\bigl[(3 - 3s)^2 + 9(1 - 9s)^2\bigr]$$.
   - Differentiate: $$\phi'(s) = -3(3 - 3s) - 81(1 - 9s) = -90 + 738s = 0 \implies s^\star = \frac{90}{738} = \frac{5}{41} \approx 0.1220$$.
   - New point: $$x^{(1)}_{\mathrm{exact}} = (3 - \tfrac{15}{41},\; 1 - \tfrac{45}{41}) = (\tfrac{108}{41},\; -\tfrac{4}{41})$$, giving $$f = \frac{1}{2}\cdot\frac{11664 + 144}{1681} = \frac{5904}{1681} \approx 3.512$$ (slightly better than fixed $$1/9$$!).
3. **Backtracking line search ($$\alpha = 0.5, \beta = 0.5$$, starting from $$t = 1$$)**:
   - Target condition: $$f(x - t\nabla f) \le 9 - 0.5 t (3^2 + 9^2) = 9 - 45t$$.
   - $$t = 1$$: $$f(0, -8) = 288 > -36$$ (reject).
   - $$t = 0.5$$: $$f(1.5, -3.5) = 56.25 > -13.5$$ (reject).
   - $$t = 0.25$$: $$f(2.25, -1.25) = 9.5625 > -2.25$$ (reject).
   - $$t = 0.125$$: $$f(2.625, -0.125) = 3.5156 \le 9 - 5.625 = 3.375$$? Slightly above ($$3.5156 > 3.375$$), so shrink once more to $$t = 0.0625$$: $$f(2.8125, 0.4375) = 4.816 \le 9 - 2.8125 = 6.1875$$ (accept!). No knowledge of $$L = 9$$ was needed!

When performing gradient descent, the **step size** determines how the variable $$x$$ is updated and affects the speed and success of finding the optimal value. This section introduces three main methods for choosing the step size to help gradient descent find the optimum more quickly:

- Fixed step size
- Backtracking line search
- Exact line search