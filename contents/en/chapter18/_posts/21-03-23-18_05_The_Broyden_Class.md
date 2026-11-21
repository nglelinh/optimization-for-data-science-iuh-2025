---
layout: post
title: 18-05 The Broyden Class
chapter: '18'
order: 6
owner: Hooncheol Shin
categories:
- chapter18
lang: en
---

The Broyden class generalizes BFGS, DFP, and SR1 with the following formula.

* **Note:** $$B^+_{\text{BFGS}}$$ and $$B^+_{\text{DFP}}$$ are the $$B^+$$ computed by BFGS and DFP, respectively.

>$$
>B^+ = (1 - \phi)B^+_{\text{BFGS}} + \phi B^+_{\text{DFP}}, \text{ for } \phi \in \mathbb{R}.
>$$

Defining $$v$$ as $$\frac{y}{y^Ts} - \frac{Bs}{s^TBs}$$, the formula above becomes the formula below.

>$$
>B^+ = B - \frac{Bss^TB}{s^TBs} + \frac{yy^T}{y^Ts} + \phi(s^TBs)vv^T.
>$$

Observe:
* When $$\phi = 0$$, the update above is the same as BFGS.
* When $$\phi = 1$$, the update above is the same as DFP.
* When $$\phi = \frac{y^Ts}{y^Ts - s^TBs}$$, the update above is the same as SR1.

***Reference**: The case where the range of $$\phi$$ is restricted to $$[0, 1]$$ is called the restricted Broyden class [14].
