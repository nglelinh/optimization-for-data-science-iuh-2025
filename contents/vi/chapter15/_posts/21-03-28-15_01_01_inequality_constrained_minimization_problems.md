---
layout: post
title: 15-01-01 Inequality constrained minimization problems
chapter: '15'
order: 3
owner: Minjoo Lee
categories:
- chapter15
lang: vi
---
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>
Let's consider the following convex optimization problem.
>
$$\begin{align}
&\min_{x}           && f(x) \\ 
&\text{subject to } && Ax = b \\
                    &&& h_{i}(x) \leq 0, i = 1, \dotsc, m
\end{align}$$

In problems that include inequalities like this, it is difficult to distinguish between binding and non-binding constraints, especially at the boundary of the feasible region. Binding constraints refer to the constraints that affect the solution.

Therefore, the **interior method** is an approach that tries to solve the problem from the interior of the feasible region, not at the boundary.

## Background of interior method
The **interior method** for general problems was proposed in the 1960s by Anthony V. Fiacco and Garth P. McCormick. At the time, it was overshadowed by popular methods like sequential quadratic programming and the active set method, and only gained attention in the 1980s.

The active set method is a theory for determining which constraints affect the optimization result. In the active set method, a constraint is considered active if it is zero, and such constraints are called the active set. However, to find the active set, you need to compute the boundary of the feasible region, and as the number of constraints increases, the computational cost increases.

Recognizing these issues, the interior point method was developed to solve problems from the interior rather than the boundary. For example, in LP, if there are $$m$$ constraints, calculating the boundary requires $$O(m^2)$$ computations, but with the interior method, even for large $$m$$, the solution can be found within 20–30 Newton steps. More details on performance will be discussed later.

* Reference: [Interior point method](https://en.wikipedia.org/wiki/Interior-point_method)
* Reference: [Active set method](https://en.wikipedia.org/wiki/Active_set_method)

## Reducing equality constrained minimization problem
The above problem can be rewritten as $$C := \{x : h_i(x) \le 0, i = 1, \cdots , m \}$$. Inequality constraints can be included in the objective function as an indicator function.

>$$\begin{align}
&\min_{x} \ && f(x) + I_C(x) \\
&\text{subject to }\  && Ax = b \\
\end{align}$$

이와 같이 문제를 equality constrained minimization problem으로 변환할 수 있다. 하지만, Indicator function의 경우 여전히 boundary를 포함하고 있기 때문에 원래 문제의 boundary 계산의 어려움을 여전히 갖고 있으며 differentiable하지 않기 때문에 newton's method를 적용하기는 어렵다.

indicator function $$I_C$$를 **barrier function**으로 근사하면 어떨까? 그럴 경우 boundary는 포함하지 않게 되며 differentiable하기 때문에 newton's method를 적용할 수 있게 된다. 

이와 같이 barrier function으로 재정의한 문제를 푸는 방법을 barrier method라고 하는데 다음 절에서 자세히 소개하고 있다.