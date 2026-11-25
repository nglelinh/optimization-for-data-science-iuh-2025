---
layout: post
title: 25 Mixed Integer Programming (part II)
chapter: '25'
order: 1
owner: YoungJae Choung
categories:
- chapter25
lang: en
---

Branch and Bound alone can still drown in an exponential tree when the initial LP relaxation sits far outside the true integer points. Chapter 25 introduces the second half of the modern MIP revolution: **cutting planes**. Instead of immediately splitting the feasible region in two, we slice away fractional corners of the LP polytope using valid linear inequalities that leave every single integer feasible point untouched. When cutting planes are embedded inside Branch and Bound—forming **Branch and Cut**—commercial solvers leap from solving 50-variable toys in the 1980s to solving million-variable statistical and engineering problems today.

## Key ideas: The Solver Half of Mixed Integer Programming

- **Convex Hull & Convexification:** Every bounded integer linear program has an equivalent LP over the convex hull $$\operatorname{conv}(S)$$ of its integer points. Cutting planes iteratively approximate $$\operatorname{conv}(S)$$ locally around the optimal fractional vertex.
- **Valid Inequalities & Separation:** A linear inequality $$\pi^\top x \le \pi_0$$ is *valid* if every integer feasible point satisfies it, and a *cutting plane* if the current fractional LP optimum violates it ($$\pi^\top x_{\text{LP}} > \pi_0$$).
- **Gomory Cuts & Branch-and-Cut Synergy:** Gomory’s fractional cuts generate valid cuts automatically from any fractional simplex tableau row—no problem-specific structure required. Embedding cuts at every node of Branch and Bound creates the modern Branch-and-Cut engine.
- **High-Dimensional Statistical MIPs:** Armed with warm starts from discrete first-order methods and Branch-and-Cut, exact $$\ell_0$$ Best Subset Selection and robust Least Quantile of Squares regression become practically solvable at modern data scales.

### Worked example: Seeing a Single Cutting Plane Eliminate Branching

Consider $$\max x_1 + x_2$$ subject to $$2 x_1 + 2 x_2 \le 5$$ and $$x_1, x_2 \in \mathbb{Z}_{\ge 0}$$.

1. **Solve the LP relaxation:** The maximum of $$x_1 + x_2$$ subject to $$x_1 + x_2 \le 2.5$$ is $$2.5$$ (achieved, e.g., at $$(2.5, 0)$$).
2. **Derive a valid cutting plane by integer rounding:** Divide $$2 x_1 + 2 x_2 \le 5$$ by $$2$$ to get $$x_1 + x_2 \le 2.5$$. Since $$x_1$$ and $$x_2$$ are integers, their sum $$x_1 + x_2$$ must be an integer, so we can round the right-hand side down:
   $$x_1 + x_2 \le \lfloor 2.5 \rfloor = 2.$$
3. **Check validity and separation:**
   - Every integer feasible point satisfies $$2(x_1 + x_2) \le 5 \implies x_1 + x_2 \le 2$$ (valid!).
   - The fractional LP optimum $$(2.5, 0)$$ has $$2.5 > 2$$ (strictly separated!).
4. **Re-solve the tightened LP:** Maximizing $$x_1 + x_2$$ subject to $$x_1 + x_2 \le 2$$ immediately hits an integer vertex such as $$(2, 0)$$ with optimal value $$2$$—closing the integrality gap completely at the root node with **zero** branching.

This chapter examines the cutting plane algorithm, which can be considered the most core algorithm in Integer Programming (IP), and the branch and cut algorithm, which is its practical implementation. 

We will also examine examples of Integer Programming such as best subset selection and Least mean squares.

## Reference
* Belotti, Kirches, Leyer, Linderoth, Luedke, and Mahajan (2012), "Mixed-integer nonlinear optimization"
* Bertsimas and Mazumder (2016), "Best subset selection via a modern optimization lens"
* Bertsimas, King, and Mazumder (2014), "Least quantile regression via modern optimization"
* Conforti, Cornuejols, and Zambelli (2014), "Integer programming"
* Wolsey (1998), "Integer programming"

## 2026 applications (optional)

Best-subset MIP is still the statistical poster child; the same big-$$M$$ / ReLU encoding now selects pixels for a trained net, *certifies* robustness, and grows optimal classification trees. Learning to pick Gomory-style cuts (2024) turns 25-01 into training data. Optional lesson: [25-03 Modern applications of MIP in data science]({% multilang_post_url contents/chapter25/2026-09-16-25_03_modern_applications %}).