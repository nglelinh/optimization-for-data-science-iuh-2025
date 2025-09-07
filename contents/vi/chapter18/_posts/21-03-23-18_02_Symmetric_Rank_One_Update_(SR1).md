---
layout: post
title: 18-02 Symmetric Rank-One Update (SR1)
chapter: '18'
order: 3
owner: Hooncheol Shin
categories:
- chapter18
lang: en
---

The SR1 update is a method that updates $$B$$ with a rank-1 symmetric matrix so that $$B^+$$ maintains symmetry and continues to satisfy the secant equation. If a rank-1 symmetric matrix is decomposed as a product of $$a \in \left\{-1, 1\right\}$$ and $$u \in \mathbb{R^n}$$, the update form would be as follows.

>$$B^+ = B + auu^T.$$

## Key Observation
$$a$$ and $$u$$ must be chosen so that $$B^+$$ satisfies the secant equation. Thus, let's substitute the update form introduced above into the secant equation $$y = B^+s$$.

>$$y = B^+s \Rightarrow y = Bs + (au^Ts)u. \quad \text{--- (1)}$$

Since $$(au^Ts)$$ is a scalar, $$u$$ can also be expressed as a product of $$y-Bs$$ and an arbitrary scalar $$\delta$$ $$\big( u = \delta(y - Bs) \big)$$. Let's substitute $$u$$ in (1) with $$\delta(y - Bs)$$.

>$$y-Bs = a\delta^2 \big[ s^T(y - Bs) \big] (y -Bs),$$

The parameters $$\delta$$ and $$a$$ that satisfy the above equation are as follows.

>$$a = \text{sign} \big[ s^T (y - Bs) \big], \quad \delta = \pm | s^T(y-Bs) |^{-1/2}. \quad \text{--- (2)}$$

## The Only SR1 Updating Formula
Using the information obtained from the key observation, we can derive the unique form of SR1 update ([14] section 6.2). <br/>
$$\big( u = \delta (y - Bs)$$ and substituting (2) into $$B^+ = B + auu^T$$. $$\big)$$

>$$
>B^+ = B + \frac{(y-Bs)(y-Bs)^T}{(y-Bs)^Ts}.
>$$
>

## The Update Formula for the Inverse Hessian Approximation

To find $$x^+$$, we need to compute $$B^{-1}$$.

>$$x^+ = x + tp = x - tB^{-1}\nabla f(x)$$

If we can update $$B^{-1}$$ instead of $$B$$, wouldn't we be able to reduce the cost of computing $$B^{-1}$$ every time?

Using the [Sherman–Morrison formula](https://en.wikipedia.org/wiki/Sherman%E2%80%93Morrison_formula), we can see through the derivation process that $$B^{-1}$$ can also be updated in the same form. ($$H = B^{-1}$$)

>$$
>H^+ = H + \frac{(s-Hy)(s-Hy)^T}{(s-Hy)^Ty}.
>$$

## Shortcomings of SR1

SR1 has the advantage of being very simple, but it has two critical shortcomings.

1. The update can fail when $$(y-Bs)^Ts$$ approaches 0.
2. It cannot maintain the positive definiteness of $$B$$ and $$H$$.

The following sections introduce methods that complement the shortcomings of SR1. 