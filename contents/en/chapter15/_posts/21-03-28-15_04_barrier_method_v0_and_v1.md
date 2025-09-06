---
layout: post
title: 15-04 Barrier method v.0 and v.1
chapter: "15"
order: 10
owner: "Minjoo Lee"
categories:
- chapter16
---

## Barrier method v.0
**Barrier method v.0** chooses $$t = m/\epsilon$$ for $$\epsilon > 0$$ and solves the following barrier problem to obtain $$f(x^*(t)) - f(x^*) \le \epsilon $$.
>
$$\begin{align}
 &\min_{x} \ && tf(x) + \phi(x) \\
 &\text{subject to } \ && Ax = b \\
\end{align}$$

Here, $$m$$ is the number of constraints and $$t$$ is a multiple of $$1/\epsilon$$, so as $$\epsilon$$ gets smaller, $$t$$ becomes very large, and eventually the end of the central path is reached, making the problem equivalent to the original problem. Therefore, this can be very slow and difficult to solve.

Thus, a better approach is to follow the central path to find the solution, which leads to the definition of **barrier method v.1**.

## Barrier method v.1
**Barrier method v.1** is a method that gradually increases the value of $$t$$ and solves the following barrier problem multiple times.
>
$$\begin{align}
 &\min_{x} \ && tf(x) + \phi(x) \\
 &\text{subject to } \ && Ax = b \\
\end{align}$$

### Algorithm
The algorithm can be described as follows.

1. Choose $$t^{(0)} > 0$$ and set $$k := 0$$.
2. At $$t = t^{(0)}$$, solve the barrier problem to obtain $$x^{(0)} = x^*(t)$$.
3. While $$m/t > \epsilon$$ <br>
  3-1. Choose $$t^{(k+1)} > t^{(k)}$$. <br>
  3-2. Initialize Newton's method with $$x^{(k)}$$. (warm start)<br>
        At $$t = t^{(k+1)}$$, solve the barrier problem to obtain $$x^{(k+1)} = x^*(t)$$.<br>
  end while<br>

### Comments
* **Common update method**: $$t^{(k+1)} = \mu t^{(k)}$$, ($$\mu > 1$$)
* **Warm start**: In step 3-2, the solution from the previous step is used as the initial value for the next step, which is called warm start.
* **Centering step**: Steps 2 and 3-2 in the algorithm, which solve the barrier problem, are called centering steps (or outer iterations).

### Considerations
In choosing $$\mu$$ and $$t^{(0)}$$, the following trade-offs must be considered.
##### Choice of $$\mu$$
* If $$\mu$$ is too small, the number of outer iterations increases. (In this case, warm start helps.)<br>
* If $$\mu$$ is too large, many iterations are required for Newton's method to converge in every centering step. 

##### Choice of initial algorithm value
* If $$t^{(0)}$$ is too small, the number of outer iterations increases.<br>
* If $$t^{(0)}$$ is too large, it becomes the same problem as v.0. Therefore, Newton's method requires many iterations to find $$x^{(0)}$$ in the first centering step. 

Fortunately, the performance of the actual barrier method is very robust to the choice of $$\mu$$ and $$t^{(0)}$$. Moreover, the appropriate range of these parameters varies depending on the problem size.

## Example of small LP
The following figure shows the performance when executing an LP problem with n=50 dimensions and m=100 inequality constraints using the barrier method. It can be confirmed that when $$\mu = 2$$, the outer iterations increase, and when $$\mu=150$$, the centering steps increase relatively compared to when $$\mu=50$$.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_barrier_method_03.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig 1] Example of small LP [3]</figcaption>
</p>
</figure>