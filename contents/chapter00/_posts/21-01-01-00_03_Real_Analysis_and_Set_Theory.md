---
layout: post
title: Real Analysis And Set Theory
chapter: "00"
order: 3
owner: "GitHub Copilot"
---

**Key Concepts:**

- Sets, subsets $$A \subseteq B$$, union $$(A \cup B)$$, intersection $$(A \cap B)$$
- Functions, domain, range
- Inequalities ($$\le$$, $$\ge$$, <, >)
- Basic topology of $$\mathbb{R}^n$$: open sets, closed sets, boundary, interior
- Sequences and limits $$(\lim_{n \to \infty} x_n = L)$$
- Continuity of functions

---
An **open set**(**tập mở**) is a fundamental concept in topology and analysis, characterized by the property that it **contains none of its boundary points**. 

A set $$S$$ in $$\mathbb{R}^n$$ is **open** if for every point $$x \in S$$, there exists a positive real number $$\epsilon > 0$$ such that the open ball $$B(x_{0}, \epsilon) = \{y \in X \mid d(x_{0}, y) < \epsilon\}$$ is entirely contained within $$S$$. 

This means every point in an open set is surrounded by a small "buffer zone" that also belongs to the set. For example, in $$\mathbb{R}^n$$, the interval $$(a, b)$$ is open because for any $$x \in (a, b)$$, we can find an $$\epsilon$$ (e.g., $$\epsilon = \min(x-a, b-x)$$) such that $$(x-\epsilon, x+\epsilon) \subset (a, b)$$.

<!-- Hình ảnh minh họa open set sẽ được thêm vào sau -->

---

Conversely, a **closed set** is defined as a set that contains all of its boundary points. Equivalently, in a **topological space**, a set $$S$$ is closed if its complement $$\mathbb{R}^n \setminus S$$ is an **open set**. 

Another crucial characterization in **metric spaces** is that a closed set contains all its limit points; that is, if a sequence of points $$(x_n)$$ from $$S$$ converges to a point $$x$$, then $$x$$ must also be in $$S$$. 

For instance, the closed interval $$[a, b]$$ in $$\mathbb{R}$$ is a closed set, as its complement $$(-\infty, a) \cup (b, \infty)$$ is open, and any convergent sequence within $$[a,b]$$ will have its limit within $$[a,b]$$.

---

The **boundary** of a set $$S$$, denoted $$\partial S$$, consists of points that are "on the edge" of the set. A point $$x$$ is a **boundary point** of $$S$$ if every open ball centered at $$x$$ intersects both $$S$$ and its complement $$S^c$$. 

Formally, $$\partial S = \bar{S} \setminus S^\circ$$, where $$\bar{S}$$ is the closure of $$S$$ (the smallest closed set containing $$S$$) and $$S^\circ$$ is the interior of $$S$$.

The **interior** of a set $$S$$, denoted $$S^\circ$$, includes all points strictly "inside" the set, excluding the boundary. A point $$x \in S$$ is an interior point if there exists an $$\epsilon > 0$$ such that the open ball $$B(x, \epsilon)$$ is entirely contained within $$S$$. The interior $$S^\circ$$ is always an open set, and it is the largest open set contained within $$S$$.

<!-- Hình ảnh minh họa boundary và interior sẽ được thêm vào sau -->

---

A **compact set**(**tập hợp compact**) - in Euclidean spaces ($$\mathbb{R}^n$$), a set is compact if and only if it is both **closed and bounded**. 

Heine-Borel Theorem: A set is "bounded" if it can be contained within some sufficiently large open ball (i.e., $$\exists M > 0$$ such that $$S \subset B(0, M)$$). 

However, the more general and fundamental definition of compactness in a topological space is that every open cover of the set has a finite subcover. That is, if $$S \subset \bigcup_{\alpha \in A} U_\alpha$$ where each $$U_\alpha$$ is open, then there exists a finite subset $$F \subset A$$ such that $$S \subset \bigcup_{\alpha \in F} U_\alpha$$. This property is incredibly powerful, ensuring the existence of extrema for continuous functions (Extreme Value Theorem) and playing a vital role in many existence proofs.