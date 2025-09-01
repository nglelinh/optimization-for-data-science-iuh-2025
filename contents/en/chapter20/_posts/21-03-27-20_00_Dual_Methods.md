---
layout: post
title: 20 Dual Methods
chapter: '20'
order: 1
owner: Hooncheol Shin
categories:
- chapter20
lang: en
---

본 장at,는 dual 을 using, problem를 solution결하는 methodwith,서,  dual subgradient method, dual decomposition method, augmented Lagrangian methodabout, knowing,보고, Alternating Direction Method of Multipliers (ADMM)의 개념을 간단히 knowing,본다. 

우선 앞at, 배운 내용 중 Proximal Newton method and, Conjugate function 내용을 간단히 복습한다. 

## Review: proximal Newton method  
다음의 problem가 있다. 
>\begin{equation}
\min_x g(x) + h(x)
\end{equation}

여기서, function $$g$$and, $$h$$는 convex function이며, $$g$$는 두번 미분 가능하고, $$h$$는 simple 하다고 가정한다.  

Proximal Newton method는 최초 $$x^{(0)} \in \mathbb{R}^n$$at, 시작되며, first, function $$g$$and, $$h$$to,게 모두 좋은 최적의 vector direction을 아래and, 같이 찾는다
>\begin{alignat}{1}
v^{(k)} & = \arg \min_v g({x^{(k-1)}})^T v +  \frac{1}{2} v^T \nabla^2 g(x^{(k-1)}) v + h(x^{(k-1)} + v) 
\end{alignat}

위at, finding,진 directionwith, 아래and, 같이 다음 $$x^{(k)}$$를 업데이트한다.  
>\begin{equation}
x^{(k)} = x^{(k-1)} + t_k v^{(k)}, k=1,2,3,\dots 
\end{equation}

여기서, $$t_k$$는 step sizeto,서 backtrackingwith, 결정된다. 

위 두 process을 iteration적with, 실행한다. 

> * 위 iteration(iteration)은 매우 비용이 많이 든다 ($$v^{(k)}$$를 computation하는 것이 generally, 매우 어렵다)
* however,, 적당한 condition,하at,는 converge하기to, 매우 적은 iteration이 요구되고, local quadratic convergence의 convergence 속도를 갖는다 


## Review: conjugate function ###
$$f: \mathbb{R}^n \to \mathbb{R}$$about,, conjugate function는 아래and, 같이 정의된다.   
>\begin{equation}
f^*(y) = \max_x y^Tx - f(x)
\end{equation}

(1) Conjugate function는 아래and, 같이 쓸 수 있으며, 이는 dual problemat, 자주 나타나는 형태이다.  
>\begin{equation}
-f^{\ast}(y) = \min_x f(x) - y^Tx
\end{equation}

(2) if, $$f$$가 closed하고 convex이면, $$f^{**} = f$$ 이다. also,, 
>\begin{equation}
x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x) \Longleftrightarrow x \in \arg\min_z f(z) - y^Tz
\end{equation}
#### Proof ####
first,, $$x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x)$$을 증명한다. 

#### 1step : $$x \in \partial f^{\ast}(y) \Longleftarrow y \in \partial f(x)$$
>
$$y \in \partial f(x)$$를 let's assume. 그러면, $$x$$는 $$y^Tz - f(z)$$를 최대to, 하게 하는 $$z$$들의 set $$M_y$$ to, 속하게 된다, that is, $$x \in M_y$$. <br> however,, $$f^{\ast}(y)=   \max_z y^Tz - f(z)$$ 이고, $$\partial f^{\ast}(y)=\text{cl} \left( \text{conv} \left( \bigcup_{z \in M_y} \left\{ z \right\} \right) \right)$$. therefore,, $$x \in \partial f^{\ast}(y)$$

####  2step : $$x \in \partial f^{\ast}(y) \Longrightarrow y \in \partial f(x)$$
>
위at, 보인것and, 같이, if,, $$x \in  \partial f^{\ast}(y)$$ 이면, $$y \in \partial f^{\ast\ast}(x)$$. 여기서, $$f^{\ast\ast}(x)=f$$ 이므to, $$y \in \partial f(x)$$.  

위 1, 2 step를 through,, $$x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x)$$이 증명되었다. 
#### 3step : $$x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x) \Longleftrightarrow x \in \arg\min_z f(z) - y^Tz$$
>
한편, $$y \in \partial f(x) \Longleftrightarrow x \in \arg\min_z f(z) - y^Tz$$은 subgradient의 정의from, 자명한 in fact,이다.  <br>
therefore,, 위 두 증명을 through,, $$x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x) \Longleftrightarrow x \in \arg\min_z f(z) - y^Tz$$임이 증명되었다.  


(3) if, $$f$$가 strictly convex이면,
> $$
> \begin{equation}
> \nabla f^{\ast}(y) = \arg\min_z f(z) - y^T z
> \end{equation}
> $$

#### Proof

>$$f$$가 strictly convex이면, $$f(z)-y^Tz$$는 최소값을 갖는 유일한 $$z$$가 존재하며, 
>이것은 위 (2)to, about, 증명으from, $$\nabla f^{\ast}(y)$$이어야 한다. 

다시 말하면 $$f$$가 strictly convex이면  $$f^{\ast}$$의 subgradient는 1개이며 gradient가 된다. therefore,,  $$f^{\ast}$$는 differentiable한 function이다.
