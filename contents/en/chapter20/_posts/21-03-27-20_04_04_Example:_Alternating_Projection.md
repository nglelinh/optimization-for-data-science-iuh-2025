---
layout: post
title: 20-04-04 Example - Alternating Projection
chapter: '20'
order: 12
owner: Hooncheol Shin
categories:
- chapter20
lang: en
---

Convex set $$C,D \in \mathbb{R}^n$$의 intersection의 한 점을 찾는 problem를 고려solution 보자.  
>\begin{equation}
\min_x I_C(x) + I_D(x)    
\end{equation}

위 problem를 ADMM형태to, 바꾸기 for,, 아래and, 같이 표현한다. 
> $$
> \begin{equation}
> \min_{x,z} I_C(x) + I_D(x) \quad \text{subject to} \quad x - z = 0   
> \end{equation}
> $$

각 ADMM cycle은 두개의 projection을 포함한다. 
> $$
> \begin{alignat}{1}
> x^{(k)} & = \arg\min_x P_C \left( z^{(k-1)} - w^{(k-1)} \right) \\
> z^{(k)} & = \arg\min_z P_D \left( x^{(k)} + w^{(k-1)} \right) \\
> w^{(k)} & = w^{(k-1)} + x^{(k)} + z^{(k)}
> \end{alignat}
> $$

위의 식at, $$x^{(k)}$$는 as follows: 도출된 것이다.

> $$
> \begin{alignat}{1}
> x^{(k)} & = \arg\min_x I_C(x) + \frac{\rho}{2} \lVert x - z^{(k-1)} + w^{(k-1)} \rVert_2^2 \\
> & = \arg\min_x P_C \left( z^{(k-1)} - w^{(k-1)} \right) \\
> \end{alignat}
> $$

위의 식at, $$z^{(k)}$$는 as follows: 도출된 것이다.

> $$
> \begin{alignat}{1}
> z^{(k)} & = \arg\min_x I_D(z) + \frac{\rho}{2} \lVert x^{(k-1)} - z + w^{(k-1)} \rVert_2^2 \\
> & = \arg\min_z P_D \left( x^{(k)} + w^{(k-1)} \right) \\
> \end{alignat}
> $$

위 method은 기존 alternating projection methodand, 비슷but, 더 효율적이다.  
