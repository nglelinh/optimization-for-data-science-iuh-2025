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

* **Note:** $$B^+_{\text{BFGS}}$$and, $$B^+_{\text{DFP}}$$는 각각 BFGSand, DFPby, 유도되는 $$B^+$$다.

>$$
>B^+ = (1 - \phi)B^+_{\text{BFGS}} + \phi B^+_{\text{DFP}}, \text{ for } \phi \in \mathbb{R}.
>$$

$$v$$를 $$\frac{y}{y^Ts} - \frac{Bs}{s^TBs}$$to, 정의하면 위 공식은 아래and, 같이 정리된다.

>$$
>B^+ = B - \frac{Bss^TB}{s^TBs} + \frac{yy^T}{y^Ts} + \phi(s^TBs)vv^T.
>$$

Observe:

* $$\phi =0$$일when,, 위 update는 BFGSand, 동일solution진다.
* $$\phi =1$$일when,, 위 update는 DFPand, 동일solution진다.
* $$\phi = \frac{y^Ts}{y^Ts - s^TBs}$$일when,, 위 update는 SR1and, 동일solution진다.

***reference**: $$\phi$$의 범위를 $$[0,1]$$to, 제한한 특수한 case,를 restricted Broyden class라 부른다 [14]. 