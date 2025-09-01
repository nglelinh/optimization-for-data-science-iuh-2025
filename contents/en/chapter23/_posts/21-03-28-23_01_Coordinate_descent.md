---
layout: post
title: 23-01 Coordinate Descent
chapter: '23'
order: 2
owner: YoungJae Choung
categories:
- chapter23
lang: en
---

In this chapter, coordinate descent라 불리는 굉장히 간단하고 효율적이면서도 확장성이 뛰어난 method을 소개한다. 우선 몇 가지 간단한 문답with, 내용을 시작solution보도록 하겠다.

**Q1. function $$f: \mathbb{R}^n \rightarrow \mathbb{R}$$가 convex이고 미분 가능할 when,, 각 coordinateaxisabout, $$f$$를 minimization시킨 지점이 $$x$$라 한다면 이 $$x$$는 global minimizer인가?**

**A1: 그렇다. $$\nabla f(x) = 0$$이므to, $$x$$는 $$f$$to, about, global minimizer이다.**

위 질문은 $$e_i = (0, \dots, 1, \dots, 0) \in \mathbb{R}^n$$가 $$i$$번째 표준 기저vector(standard basis vector)일when,, 모든 $$\delta, i$$about, $$f(x + \delta e_i) \ge f(x)$$를 만족하는지 묻는 것and,도 같다. that is,, $$x$$at, 어느 coordinateaxis directionwith, 움직이더라도 $$f$$를 더 작게 할 수 없다는 것이므to, 모든 axisdirectionto, about, 편미분은 0이 된다.

$$
\nabla f(x) = \big( \frac{\partial f}{\partial x_1}(x), \dots, \frac{\partial f}{\partial x_n}(x) \big) = (0, \dots, 0) = 0
$$

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter23/smooth_function.png" alt="[Fig1] Smooth convex function f [3]">
  <figcaption style="text-align: center;">$$[Fig1] \; Smooth \; convex \; function \; f \; [3]$$ </figcaption>
</p>
</figure>


<br/>

**Q2. 그렇다면 $$f: \mathbb{R}^n \rightarrow \mathbb{R}$$가 convex이지만 '미분 불가능한' function일when,, 각 coordinateaxisabout, $$f$$를 minimization시킨 지점 $$x$$는 always, global minimizer인가?**

**A2: 아니다. 이 case,to,는 $$x$$가 $$f$$to, about, global minimizer라고 단언할 수 없다. (반례: 아래 Fig2)** 

아래 반례의 우측 등고선을 보면 표시된 지점이 global minimum이 아님to,도 불구하고 어느 coordinateaxis directionwith, 이동하더라도 $$f$$를 더 작게할 수 없음을 알 수 있다. ($$f$$를 더 작게 만들기 for,서는 등고선 안쪽with, 이동 가능solution야 한다.) 이 positionat,는 coordinateaxisand, 평행한 두 개의 접선 내부to, 등고선의 안쪽 모든 영역이 포함되기 because,이다. 반면 $$f$$가 미분 가능한 convex function인 case,to,는 등고선의 어느 지점at,도 단 하나만의 접선만이 존재하므to, 이런 현image이 발생하지 않는다.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter23/non-smooth_function.png" alt="[Fig2] Counterexample: Non-smooth convex function f [3]">
  <figcaption style="text-align: center;">$$[Fig2] \; Counterexample: Non \, smooth \; convex \; function \; f \; [3]$$ </figcaption>
</p>
</figure>
<br/>

**Q3. $$f$$를 미분 가능한 convex function $$g$$and, convex function $$h$$의 sumwith, 표현할 수 있을when,, 각 coordinateaxisabout, $$f$$를 minimization시킨 지점 $$x$$는 always, global minimizer인가? (that is,, $$f(x) = g(x) + \sum_{i=1}^{n} h_i(x_i)$$)**

**A3. 그렇다. 임의의(any) $$y$$about, 다음을 만족하기 because,이다. **
$$\begin{align}
f(y) - f(x) &\ge \nabla g(x)^T (y-x) + \sum_{i=1}^{n} \big[ h_i(y_i) - h_i(x_i) \big] \\\\
&= \sum_{i=1}^{n} \big[ \underbrace{\nabla_i g(x) (y_i - x_i) + h_i(y_i) - h_i(x_i)}_{\ge 0} \big] \ge 0
\end{align}$$

**증명:**

>$$F_i(x_i) = g(x_i ; x_{-i}) + h_i(x_i)$$ 라고 하자. ($$g(x_i ; x_{-i})$$ 는 $$x$$의 $$i$$번째 element만을 variableto, 보고, remainder는 고정된 값with, 본다는 의미이다.)
>
> $$
> \begin{align}
> & \: 0 \in \partial F_i (x_i) \\\\
> \Leftrightarrow & \: 0 \in \{ \nabla_i g(x) \} + \partial h_i(x_i)\\\\
> \Leftrightarrow & \: - \nabla_i g(x) \in \partial h_i(x\_i)
> \end{align}
> $$

[Subgradient의 정의]({% multilang_post_url contents/chapter07/21-03-25-07_01_subgradient %})by,,

> $$
> \begin{align}
> & h_i(y_i) \ge h_i(x_i) - \nabla_i g(x) (y_i - x_i)\\\\
> \Leftrightarrow & \nabla_i g(x) (y_i - x_i) + h_i(y_i) - h_i(x_i) \ge 0.
> \end{align}
> $$

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter23/separable_non-smooth.png" alt="[Fig3] Convex function f with separable non-smooth parts [3]">
  <figcaption style="text-align: center;">$$[Fig3] \; Convex \; function \; f \; with \; separable \; non \,smooth \; parts \; [3]$$ </figcaption>
</p>
</figure>
<br/>

## Conclusion

$$f(x) = g(x) + \sum_{i=1}^{n} h_i(x_i)$$ with $$g$$ convex, differentiable and $$h_i$$ convexto, about, minimizer는 **coordinate descent**를 using, 찾을 수 있다. Coordinate descent는 다음의 cycle을 iteration하는 것이다. (적당한 초기값 $$x^{(0)}$$가 설정되었다고 가정한다.)

>**Coordinate Descent:** <br/>
>$$\:$$ For $$k = 1,2,3,\dots$$,
>
>$$
>\begin{align}
>x_1^{(k)} &\in \text{arg}\min_{x_1} \: f(x_1, x_2^{(k-1)}, x_3^{(k-1)}, \dots, x_n^{(k-1)})\\\\
>x_2^{(k)} &\in \text{arg}\min_{x_2} \: f(x_1^{(k)}, x_2, x_3^{(k-1)}, \dots, x_n^{(k-1)})\\\\
>x_3^{(k)} &\in \text{arg}\min_{x_3} \: f(x_1^{(k)}, x_2^{(k)}, x_3, \dots, x_n^{(k-1)})\\\\
>& \dots\\\\
>x_n^{(k)} &\in \text{arg}\min_{x_n} \: f(x_1^{(k)}, x_2^{(k)}, x_3^{(k)}, \dots, x_n)
>\end{align}
>$$

#### Notes:

* $$x_{i+1}^{(k)}, \dots, x_{n}^{(k)}$$를 구하는 processat,는 $$k$$번째 cycleat, 새to, 구한 $$x_i^{(k)}$$를 사용한다.
* Cycleat,의 coordinateaxis 순서는 임의to, 지정solution도 무관하다.
* 두 개 이image의 coordinateaxis을 묶어서 블록with, 처리할 수도 있다.

앞서 소개한 coordinate descent는 exact coordinatewise minimizationto, solution당한다. 다른 방식with,는 gradient를 이용한 inexact coordinatewise minimization이 있다. ($$f$$가 미분 가능한 convex function라고 가정)

>**Coordinate Descent (inexact coordinatewise minimization):** <br/>
>$$\:$$ For $$k = 1,2,3,\dots$$,
>
>$$
>\begin{align}
>x_1^{(k)} &= x_1^{(k-1)} - t_{k,1} \cdot \nabla_1 f(x_1^{(k-1)}, x_2^{(k-1)}, x_3^{(k-1)}, \dots, x_n^{(k-1)})\\\\
>x_2^{(k)} &= x_2^{(k-1)} - t_{k,2} \cdot \nabla_2 f(x_1^{(k)}, x_2^{(k-1)}, x_3^{(k-1)}, \dots, x_n^{(k-1)})\\\\
>x_3^{(k)} &= x_3^{(k-1)} - t_{k,3} \cdot \nabla_3 f(x_1^{(k)}, x_2^{(k)}, x_3^{(k-1)}, \dots, x_n^{(k-1)})\\\\
>& \dots\\\\
>x_n^{(k)} &= x_n^{(k-1)} - t_{k,n} \cdot \nabla_n f(x_1^{(k)}, x_2^{(k)}, x_3^{(k)}, \dots, x_n^{(k-1)})
>\end{align}
>$$

