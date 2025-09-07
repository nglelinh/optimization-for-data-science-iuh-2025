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

In this chapter, we will examine methods for solving problems using duality, including dual subgradient method, dual decomposition method, augmented Lagrangian method, and briefly introduce the concept of Alternating Direction Method of Multipliers (ADMM). 

First, we will briefly review the previously learned content on Proximal Newton method and Conjugate function. 

## Review: proximal Newton method  
Consider the following problem. 
>\begin{equation}
\min_x g(x) + h(x)
\end{equation}

Here, functions $$g$$ and $$h$$ are convex functions, where $$g$$ is twice differentiable and $$h$$ is simple.  

The Proximal Newton method starts with initial $$x^{(0)} \in \mathbb{R}^n$$ and finds the optimal vector direction that is good for both functions $$g$$ and $$h$$ as follows
>\begin{alignat}{1}
v^{(k)} & = \arg \min_v g({x^{(k-1)}})^T v +  \frac{1}{2} v^T \nabla^2 g(x^{(k-1)}) v + h(x^{(k-1)} + v) 
\end{alignat}

Using the direction found above, we update the next $$x^{(k)}$$ as follows.  
>\begin{equation}
x^{(k)} = x^{(k-1)} + t_k v^{(k)}, k=1,2,3,\dots 
\end{equation}

Here, $$t_k$$ is the step size determined by backtracking. 

We execute the above two processes iteratively. 

> * The above iteration is very expensive (computing $$v^{(k)}$$ is generally very difficult)
* However, under appropriate conditions, very few iterations are required to converge, and it has a convergence rate of local quadratic convergence 


## Review: conjugate function
For $$f: \mathbb{R}^n \to \mathbb{R}$$, the conjugate function is defined as follows.   
>\begin{equation}
f^*(y) = \max_x y^Tx - f(x)
\end{equation}

(1) The conjugate function can be written as follows, and this is a form that frequently appears in dual problems.  
>\begin{equation}
-f^{\ast}(y) = \min_x f(x) - y^Tx
\end{equation}

(2) If $$f$$ is closed and convex, then $$f^{**} = f$$. Also, 
>\begin{equation}
x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x) \Longleftrightarrow x \in \arg\min_z f(z) - y^Tz
\end{equation}
### Proof ###
first,, $$x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x)$$을 증명한다. 

### 1step : $$x \in \partial f^{\ast}(y) \Longleftarrow y \in \partial f(x)$$
>
$$y \in \partial f(x)$$를 let's assume. 그러면, $$x$$는 $$y^Tz - f(z)$$를 최대to, 하게 하는 $$z$$들의 set $$M_y$$ to, 속하게 된다, that is, $$x \in M_y$$. <br> however,, $$f^{\ast}(y)=   \max_z y^Tz - f(z)$$ 이고, $$\partial f^{\ast}(y)=\text{cl} \left( \text{conv} \left( \bigcup_{z \in M_y} \left\{ z \right\} \right) \right)$$. therefore,, $$x \in \partial f^{\ast}(y)$$

###  2step : $$x \in \partial f^{\ast}(y) \Longrightarrow y \in \partial f(x)$$
>
위at, 보인것and, 같이, if,, $$x \in  \partial f^{\ast}(y)$$ 이면, $$y \in \partial f^{\ast\ast}(x)$$. 여기서, $$f^{\ast\ast}(x)=f$$ 이므to, $$y \in \partial f(x)$$.  

위 1, 2 step를 through,, $$x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x)$$이 증명되었다. 
### 3step : $$x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x) \Longleftrightarrow x \in \arg\min_z f(z) - y^Tz$$
>
한편, $$y \in \partial f(x) \Longleftrightarrow x \in \arg\min_z f(z) - y^Tz$$은 subgradient의 정의from, 자명한 in fact,이다.  <br>
therefore,, 위 두 증명을 through,, $$x \in \partial f^{\ast}(y) \Longleftrightarrow y \in \partial f(x) \Longleftrightarrow x \in \arg\min_z f(z) - y^Tz$$임이 증명되었다.  


(3) if, $$f$$가 strictly convex이면,
> $$
> \begin{equation}
> \nabla f^{\ast}(y) = \arg\min_z f(z) - y^T z
> \end{equation}
> $$

### Proof

>$$f$$가 strictly convex이면, $$f(z)-y^Tz$$는 최소값을 갖는 유일한 $$z$$가 존재하며, 
>이것은 위 (2)to, about, 증명으from, $$\nabla f^{\ast}(y)$$이어야 한다. 

다시 말하면 $$f$$가 strictly convex이면  $$f^{\ast}$$의 subgradient는 1개이며 gradient가 된다. therefore,,  $$f^{\ast}$$는 differentiable한 function이다.
