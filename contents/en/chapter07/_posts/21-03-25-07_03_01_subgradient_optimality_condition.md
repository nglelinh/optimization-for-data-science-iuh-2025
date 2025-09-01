---
layout: post
title: 07-03-01 Subgradient Optimality Condition
chapter: '07'
order: 7
owner: Kyeongmin Woo
categories:
- chapter07
lang: en
---


### Lemma

For any function $$f$$, the condition that $$x^*$$ is a minimizer of $$f$$ and that $$0$$ is a subgradient at $$x^*$$ are equivalent:

> $$
\begin{equation}
f(x^*) = \min_x f(x) \Longleftrightarrow 0 \in \partial f(x^*)
\end{equation}
$$

### Proof
>
$$
\begin{align}
&f(x^*) = \min_x f(x)\\
\Longleftrightarrow &f(y) \geq f(x^*) \text{ for all } y\\
\Longleftrightarrow &f(y) \geq f(x^*) + 0^T(y-x^*)\\
\Longleftrightarrow &0 \in \partial f(x^*)
\end{align}
$$

Note that convexity of $$f$$ is not used in this proof, so this optimality condition applies even to non-convex functions.

