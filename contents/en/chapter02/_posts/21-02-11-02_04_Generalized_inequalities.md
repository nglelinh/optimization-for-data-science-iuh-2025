---
layout: post
title: 02-04 Generalized inequalities
chapter: '02'
order: 10
owner: Wontak Ryu
categories:
- chapter02
lang: en
---

In one-dimensional real space $$\mathbb{R}$$, given two numbers 1 and 2, we can say 2 is greater than 1. But in $$n$$-dimensional real space $$\mathbb{R}^n$$, given two points $$x_1$$ and $$x_2$$, can we say which is greater? This is not straightforward.

This section introduces **generalized inequalities** for comparing order between two points in $$\mathbb{R}^n$$, and also discusses the concepts of minimum and minimal elements of a set.

## Proper cone

A convex cone $$K \subseteq \mathbb{R}^n$$ is called a **proper cone** if it satisfies:

* K is closed (includes its boundary).
* K is solid (its interior is nonempty).
* K is pointed (does not contain any line) (i.e., $$x \in K, -x \in K \implies x = 0$$).

If a pointed & closed convex cone is defined in a subspace of dimension $$n-1$$ or less, its interior is empty, since it cannot contain an open ball in $$n$$ dimensions. Thus, it is not solid and cannot be a proper cone. For example, a 2D pie-shaped pointed & closed convex cone in $$\mathbb{R}^3$$ is not a proper cone.

See *[Wikipedia: Interior (topology)](https://en.wikipedia.org/wiki/Interior_(topology))* for the definition of interior.

## Generalized inequality

Using a proper cone, we can define a partial ordering in $$\mathbb{R}^n$$ called a **generalized inequality**. It has properties similar to the standard ordering in $$\mathbb{R}$$:

> $$x \preceq_{K} y \iff y − x \in K$$

Similarly, strict partial ordering is defined as:

> $$x \prec_{K} y \iff y − x \in $$ **int** $$K$$

If $$K = \mathbb{R}_{+}$$, then $$\preceq_{K}$$ is the usual $$\le$$ in $$\mathbb{R}$$.

#### Properties of generalized inequalities

Generalized inequality $$\preceq_{K}$$ satisfies:

* **Preserved under addition**: if $$x \preceq_{K} y$$ and $$u \preceq_{K} v$$, then $$ x+u \preceq_{K} y +v$$.
* **Transitive**: if $$x \preceq_{K} y$$ and $$y \preceq_{K} z$$ then $$x \preceq_{K}  z$$.
* **Preserved under nonnegative scaling**: if $$x \preceq_{K} y$$ and $$α \ge 0$$ then $$αx \preceq_{K} αy$$.
* **Reflexive**: $$x \preceq_{K} x$$.
* **Antisymmetric**: if $$x \preceq_{K} y$$ and $$y \preceq_{K} x$$, then $$x = y$$.
* **Preserved under limits**: if $$x_i \preceq_{K}  y_i$$ for $$i = 1, 2, ..., x_i \to x$$ and $$y_i \to y$$ as $$i \to ∞$$, then $$x \preceq_{K} y$$.

Strict generalized inequalities have corresponding properties.

## Minimum and minimal elements

$$\mathbb{R}$$의 ordering과 $$\mathbb{R}^n$$의 generalized ordering의 가장 큰 차이는 **linear ordering**이다. $$\mathbb{R}$$에서는  $$x \lt y$$ 또는 $$x \gt y$$와 같이 두 점을 비교할 수 있지만  generalized inequality는 그렇지 못하다. 따라서, generalized inequality 문맥으로 maximum과 minimum 개념을 정의하는 것이 훨씬 더 복잡할 것으로 예상해 볼 수 있다.

#### Minimum elements

$$x \in S$$이 모든 $$y \in S$$에 대해 $$x \preceq_{K} y$$이면 $$x$$는 집합 $$S$$의 **minimum** element이다. 비슷한 방식으로  **maximum**도 정의할 수 있다. 어떤 집합에서 minimum이 존재한다면 unique하다. 즉, minimum은 오직 하나만 존재한다. 

어떤 점 $$x \in S$$가 $$S$$의 minimum이라면 $$S \subseteq x + K$$이다. 여기서 $$x + K$$의 의미는 ($$\preceq_{K}$$에 따라) 모든 점들은 $$x$$와 비교할 수 있으며 $$x$$와 같거나 크다는 의미이다.

#### Minimal elements

비슷한 개념으로 **minimal**이 있다. $$x \in S$$이 모든 $$y \in S$$에 대해 $$y \preceq_{K} x$$인 경우는 $$y=x$$인 경우뿐이라면 $$x$$는 집합 $$S$$의 **minimal** element이다. 비슷한 방식으로  **maximal**도 정의할 수 있다. 집합은 여러 개의 minimal element를 가질 수 있다.

어떤 점 $$x \in S$$가 $$S$$의 minimal이라면 $$(x - K) \cap S = \{x\}$$이다. 여기서 $$x - K$$의 의미는 ($$\preceq_{K}$$에 따라) 모든 점들은 $$x$$와 비교할 수 있으며 $$x$$와 작거나 같다는 의미이다.

$$K = R_{+}$$의 경우 minimal과 minimum은 동일하며 일반적인 minimum의 정의에 부합한다.

#### $$R^2_{+}$$ cone에서 minimum과 minimal

$$\mathbb{R}^2_{+}$$ cone $$K$$를 고려해 보자. Inequality $$x \preceq_{K} y$$는 y가 x보다 오른쪽 위에 있다는 의미이다.  $$x \in S$$일 때 $$x$$가 minimum이란 이야기는 $$S$$의 모든 점이 $$x$$보다 오른쪽 위에 있다는 의미이다. $$x$$가 minimal이란 이야기는 $$S$$에는 $$x$$의 왼쪽 아래에 있는 점이 없다는 의미이다.

아래 그림에서 $$S_1$$은 minimum $$x_1$$을 갖는다. 집합 $$x + K$$은 옅은 회색으로 표시되어 있으며 집합 $$S_1$$은 $$S_1 \subseteq x + K$$이기 때문에 $$x_1$$은  minimum이다. $$S_2$$은 minimal $$x_2$$을 갖는다. 집합 $$x - K$$은 옅은 회색으로 표시되어 있으며 집합 $$S_2$$은 $$(x - K) \cap S = \{x\}$$이기 때문에  $$x_2$$는 minimal이다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.06_01_Minimum_and_minimal.png" alt="[Fig1] Minimum and minimal elements [1]" width="70%">
  <figcaption style="text-align: center;">[Fig1] Minimum and minimal elements [1]</figcaption>
</p>
</figure>


