---
layout: post
title: 22-04 Properties and variants
chapter: '22'
order: 5
owner: YoungJae Choung
categories:
- chapter22
lang: en
---

## Some variants
일부 변종 conditional gradient method들을 let's look at:<br>
• **Line search**: $$γk=2/(k+1),k=1,2,3,...$$를 고정하는 instead of, 각 $$k = 1, 2, 3, . . .$$ 스텝 사이즈to, about, exact line search를 사용한다.
> $$γ_k = \arg\min_{γ∈[0,1]} f\Bigl( x^{(k−1)} + γ\bigl(s^{(k−1)} − x^{(k−1)} \bigr) \Bigr)$$

and, 백트레킹을 사용 할 수도 있다.

• **Fully corrective**: 아래 식according to, 직접 업데이트 한다.
> $$x^{(k)} = \arg\min_y f(y) \: \text{ subject to } y ∈ conv\{ x^{(0)}, s^{(0)}, . . . s^{(k−1)} \}$$

이 방식은 훨씬 더 나은 진전을 이룰 수 있지만, Cost가 높다. 

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter22/away_steps.png" alt="[Fig 3] Away step motivation [3]">
  <figcaption style="text-align: center;">[Fig 3] Away step motivation [3]</figcaption>
</p>
</figure>
<br>


## Another variant: away steps
좀 더 빠른 이solution를 for,,  [Fig 3]의 minimization problem를 살펴 보자. 여기서 최적 solution는 (0,0)이다. and, conditional descent method은 초기 점 (0,1) because of, 움직이기 어렵게 된다. however, away step 이동due to, Conditional gradient descent는 가능성 있는 지점with, 이동 할 뿐만 아니라 가능성이 없는 지점at, 벗어나게 된다.



atoms $$A$$ setto, about, Convex hull $$C = conv(A)$$를 가정solution 보자

$$A$$to, 속한 element의 convex combinationwith, $$x∈C$$를 명시적with, 나타낼 수 있다.
> $$x = \sum_{a∈A} λ_a(x)a$$

Away stepsat,의 Conditional gradient: \\
$$\text{1. choose } x^{(0)} = a^{(0)} ∈ A$$ \\
$$\text{2. for } k = 1, 2, 3, . . .$$ \\
$$\qquad s^{(k−1)} ∈ \arg\min_{a∈A} ∇f(x^{(k−1)})^Ta,$$
$$\qquad a^{(k−1)} ∈ \arg\max_{a∈A, λa(x(k−1))>0} ∇f(x^{(k−1)})^Ta$$
$$\qquad \text{choose } v = s^{(k−1)} − x^{(k−1)} or \quad v = x^{(k−1)} − a^{(k−1)}$$
$$\qquad x^{(k)} = x^{(k−1)} + γ_kv$$ \\
$$\text{3. end for}$$


## Linear convergence
다음의 제약 condition,이 없는 problem를 고려solution 보자.
> $$\min_x f(x) \: \text{ subject to } x ∈ \mathbb{R}^n$$

여기서 $$f$$ is µ-strongly convex이고 $$∇f$$ 는 L-Lipschitz이다.

$$t_k = 1/L$$ about,서 gradient descent $$x^{(k+1)} = x^{(k)} − t_k∇f(x^{(k)})$$를 iteration하면서, 다음을 만족시킨다.
> $$f(x^{(k)}) − f^{\star} ≤ \Bigl( 1 −\frac{µ}{L} \Bigr)^k \bigl( f(x^{(0)}) − f^{\star} \bigr)$$

이제 아래의 제약 condition,이 있는 problem도 고려solution 보자.
> $$\min_x f(x) \: \text{ subject to } x ∈ conv(A) ⊆ \mathbb{R}^n$$

### [Theorem (Lacoste-Julien & Jaggi 2013)]
$$f$$가 µ-strongly convex이고, $$∇f$$는 L-Lipschitz 하며 $$A ⊆ \mathbb{R}^n$$는 유한 이라고 가정할 when,

적절한 $$γ_k$$about,, conditional gradient algorithmby, 생성 된 iteration 스텝은 다음을 always, 만족한다. 
> $$f(x^{(k)}) − f^{\star} ≤ (1 − r)^{k/2}(f(x^{(0)}) − f^{\star}) \text { for } r = \frac{µ}{L}·\frac{Φ(A)^2}{4\text{diam}(A)^2}$$
> $$\text{where }Φ(A) = \min_{F ∈faces(conv(A))} dist(F, conv(A \ F))$$
 
if, polytope가 평면이면, $$Φ$$는 작고 algorithm은 천천히 convergence한다.


## Path following
다음 주어진 norm constrained problem를 let's look at 
> $$\min_x f(x) \: \text{ subject to } \| x \| ≤ t$$

Frank-Wolfe algorithm은  **path following**to, 사용할 수 있다. 다시말solution, (대략적인) 솔루션 경to, $$\hat{x}(t), t ≥ 0$$를 생성할 수 있다는 의미 이다.

$$t_0 = 0$$and, $$x^{\star}(0) = 0$$at, 시작하여 parameter $$\epsilon, m > 0$$을 수정한 다음 $$k=1,2,3,...$$about, iteration한다.

* $$t_k = t_{k−1} + \frac{(1 − 1/m)\epsilon}{\| ∇f(\hat{x}(t_k−1))\|\_{∗}}$$를 computation하고, 모든 $$t ∈ (t_{k−1}, t_k)$$about, $$\hat{x}(t) = \hat{x}(t_{k−1})$$를 설정한다.

* $$t = t_k$$ at, Frank-Wolfe를 executing, $$\hat{x}(t_k)$$를 computation하고 duality gap이 $$≤ \frac{\epsilon}{m}$$ 인 case, 종료 한다.

이것은 기존의 strategy을 단순화 시킨 method이다. [Giesen et al. (2012)]

이 **path following** strategy을 through,, 방문하는 모든 $t$about, 다음을 보장할 수 있다.
> $$f(\hat{x}(t)) − f(x^{\star}(t)) ≤ \epsilon$$

that is,, 모든 $$t$$about,서 $$\epsilon$$by, 균일하게 경계가 정solution진 suboptimality gap의 경to,를 생성한다.

아래의 수식at, 보듯 Frank-Wolfe duality gap을 as follows: 재정의 할 수 있다.
> $$g_t(x) = \max_{\|s\|≤1} ∇f(x)^T(x − s) = ∇f(x)^Tx + t\|∇f(x)\|_{∗}$$

이것은$t$to, about, 선형 function이다. therefore, $$g_t(x) ≤ = \frac{\epsilon}{m}$$이면, 다음 수식by,서 $$t^+ = t + (1 − 1/m)\epsilon/\|∇f(x)\|_{∗}$$to, $$t$$를 증가 시킬 수 있다.

> $$g_t+ (x) = ∇f(x)^Tx + t\|∇f(x)\|_{∗} + \epsilon − \epsilon/m ≤ \epsilon$$

that is,, duality gap은 동일한 $$x$$about, $$t$$and, $$t^+$$ 사이at, $$≤ \epsilon$$to, 유지된다.

