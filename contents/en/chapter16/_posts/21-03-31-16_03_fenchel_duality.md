---
layout: post
title: 16-03 Fenchel duality
chapter: '16'
order: 4
owner: Minjoo Lee
categories:
- chapter16
lang: en
---
<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

In [13-04 Conjugate function]({% multilang_post_url contents/chapter13/21-04-05-13_04_Conjugate_function %}), we learned how to derive dual problems using conjugate functions. Fenchel duality refers to dual problems derived from conjugate functions that have the following form:

$$
\max_{v} -f^*(A^Tv) - g^*(-v)
$$

Let's explore where this form of problem is derived from.

#### Primal problem

> $$
> \min_{x} \quad f(x) + g(Ax)
> $$

The given problem can be redefined with an added equality constraint.

#### Primal problem rewritten
>
$$
 \begin{align}
 &\min_{x,z} \        && f(x) + g(z)\\
 &\text{subject to} \ && Ax = z.
 \end{align}
 $$

Let's derive the dual problem of the redefined primal problem using conjugate functions. <br/>

* **Recall:** $$f^*(s) \doteq  \max_{x} \big( s^Tx - f(x) \big) = \min_{x} \big( f(x) - s^Tx \big)$$

<br/>
$$
\begin{align}
&\max_{v} \min_{x, z} \quad L(x,z,v)\\\\
= &\max_{v} \min_{x, z} \quad f(x) + g(z) + v^T (z - Ax) \\\\
= &\max_{v} \min_{x, z} \quad v^Tz + g(z) - (A^Tv)^Tx + f(x)\\\\
= &\max_{v} \quad  -f^*(A^Tv) - g^*(-v)\\\\
\end{align}
$$

#### Fenchel duality
> $$
> \max_{v} -f^*(A^Tv) - g^*(-v)
> $$

* **Nice Property:** If $$f, g$$ are convex and closed, the dual of the dual becomes the primal again. (Symmetric)

## Example: conic programming

#### Primal problem of CP in standard form
>$$
\begin{align}
    \mathop{\text{minimize}}_x &\quad c^Tx \\\\
    \text{subject to} &\quad Ax = b \\\\
    &\quad x \in K
\end{align}
$$

The above problem can be redefined using two functions $$f(x) = c^Tx + I_K(x)$$ and $$g(z) = I_{\{b\}}(z)$$.<br/>

* **Note:** $$\begin{equation}
    f(x) + g(Ax) = 
    \begin{cases}
      0, & \text{if}\ Ax=b, x \in K \\\\
      \infty, & \text{otherwise}
    \end{cases}
  \end{equation}$$

#### Primal problem of CP rewritten
> $$
> \begin{align}
> &\min_{x, z}       \ &&  f(x) + g(z)\\\
> &\text{subject to} \ && z  =Ax \\\
> \end{align}
> $$

#### Deriving dual problem of CP

Let's derive the dual problem from the redefined CP primal problem. First, expanding functions $$f$$ and $$g$$ gives us the following:
> $$
> \begin{align}
> & \min_{x, z} && \; c^Tx + I_K(x) + I_{\{b\}}(z)  \\\
> &\text{subject to} && \;  z   =Ax \\
> \end{align}
> $$

Let's expand the problem using conjugate functions from the definition of the dual problem.

> $$
> \begin{align}
> & \max_{y} \; \min_{x, z} \;  L(x, z, y) \\\
> = \; & \max_{y} \; \min_{x, z} \;  c^Tx + I_K(x) + I_{\{b\}}(z) + y^T(z-Ax) \\\
> = \; & \max_{y}  \;\min_{x, z} \; (c - A^Ty)^Tx  + I_K(x) \;+ \;  y^Tz + I_{\{b\}}(z) \\\
> = \; & \max_{y} \;  \min_{x, z} \; -( (A^Ty - c)^Tx  - I_K(x)) \;  - \; ( - y^Tz - I_{\{b\}}(z) ) \\\
> = \; & \max_{y} \; - I_K^*(A^Ty - c)  -  I_{\{b\}}^*(-y)  \\\
> = \; & \max_{y} \; - I_{-K^*}(A^Ty - c)  - I_{\{b\}}^*(-y)  \\
> \end{align}
> $$

$$I_{-K^*}(A^Ty - c)$$ can be expressed as a constraint.

> $$
> \begin{align}
> A^Ty - c & = -s, \; -s \in -K^* \\\
> \Leftrightarrow A^Ty + s & = c, \; s \in K^* \\\
> \end{align}
> $$

Since $$I_{\{b\}}^*(-y) = \max_{b} -b^Ty - I_{\{b\}}(b)$$, the problem can be organized as follows:
> $$
> \begin{align}
> &\max_{y, s} \ && -(-b^Ty - I_{\{b\}}(b)) \\\
> &\text{subject to} \ && y^TA + s = c \\\
> &  \; s \in K^* \\
> \end{align}
> $$

Since $$I_{\{b\}}(b) = 0$$, it can be removed from the problem.

#### Dual problem of CP

> $$
> \begin{align}
> &\max_{y, s} \ &&  \;  b^Ty  \\\
> &\text{subject to} \ && y^TA + s = c \\\
> &  \; s \in K^* \\
> \end{align}
> $$ 

* If either the primal problem or dual problem is strictly feasible, then strong duality is satisfied.
* If both the primal problem and dual problem are strictly feasible, then strong duality is satisfied and primal & dual optima exist.

## Example: semidefinite programming
Let's examine the forms of primal & dual problems for SDP and the primal & dual problems for SDP's barrier problem.

#### Primal problem of SDP
>$$
>\begin{align}
>    &\mathop{\text{minimize}}_{X} &&{tr(CX)} \\\\
>    &\text{subject to } &&{tr(A_iX) = b_i, \phantom{5} i=1,\dotsc,p} \\\\
>    & &&{X \succeq 0},\\\\
>\end{align}$$
>
> $$\text{where } C, A_1, \dotsc, A_p \in \mathbb{S}^n.$$

* **Recall:** $$tr(CX) = \sum_{i,j=1}^n C_{ij}X_{ij}$$
* **Note:** Unlike LP, SDP does not always satisfy strong duality.

#### Dual problem of SDP
>$$
>\begin{align}
>    &\mathop{\text{minimize}}_{y} &&{b^Ty} \\\\
>    &\text{subject to } &&{\sum_{i=1}^m y_i A_i + S = C} \\\\
>    & &&{S \succeq 0}.\\\\
>\end{align}
>$$

* **Note:** The positive semidefinite cone is a self-dual cone. ($$(\mathbb{S}_{+}^n)^* = \mathbb{S}_{+}^n$$)

#### Primal problem of Barrier problem for SDP
>$$
>\begin{align}
>    &\mathop{\text{minimize}}_{X} &&{tr(CX) - \tau \log \big( det(X) \big)} \\\\
>    &\text{subject to } &&{tr(A_iX) = b_i, \phantom{5} i=1,\dotsc,p} \\\\
>\end{align}$$
>
>$$\text{where } C, A_1, \dotsc, A_p \in \mathbb{S}^n.$$

#### Dual problem of Barrier problem for SDP
>$$
>\begin{align}
>    &\mathop{\text{minimize}}_{y, S} &&{b^Ty +  \tau \log \big( det(S) \big)} \\\\
>    &\text{subject to } &&{\sum_{i=1}^m y_i A_i + S = C}.
>\end{align}
>$$