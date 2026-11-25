---
layout: post
title: 15-04 Barrier method v.0 and v.1
chapter: "15"
order: 10
owner: "Minjoo Lee"
categories:
- chapter16
lang: en
---

If $$t = m/\epsilon$$ guarantees $$\epsilon$$-accuracy in one shot, why not just set $$t = 10^8$$ right away and run Newton's method once (Barrier Method v.0)? Try it, and Newton's method chokes immediately: at $$t = 10^8$$, the barrier wall is razor-sharp, its Hessian is horribly ill-conditioned, and Newton's local quadratic basin shrinks to microscopic size. **Barrier Method v.1** solves this by *continuously walking* along the central path: multiply $$t$$ by $$\mu \in [10, 20]$$ and warm-start each centering step from the previous solution!

## Background Knowledge Map: One-Shot (v.0) vs. Path-Following (v.1)

- **Pillar 1 — Why One-Shot (v.0) Fails:** Setting $$t = m/\epsilon$$ directly creates an almost-discontinuous objective whose Hessian explodes near boundaries, forcing hundreds of painful damped Newton steps.
- **Pillar 2 — Geometric Progression ($$t^{(k+1)} = \mu t^{(k)}$$):** Multiplying $$t$$ by a moderate factor $$\mu > 1$$ shrinks the guaranteed duality gap $$m/t$$ exponentially fast—by a factor of $$\mu$$ on every outer iteration.
- **Pillar 3 — Warm-Starting Keeps Newton Close to the Basin:** Starting the centering step for $$\mu t$$ at $$x^*(t)$$ places the iterate close to $$x^*(\mu t)$$, requiring only a few Newton iterations to re-center.
- **Pillar 4 — The $$\mu$$ Trade-Off (Sweet Spot $$\mu \in [10, 20]$$):** Small $$\mu$$ (e.g., $$2$$) means cheap centering steps but many outer iterations; huge $$\mu$$ (e.g., $$150$$) means few outer iterations but expensive re-centering; moderate $$\mu \approx 10\text{–}20$$ minimizes *total* Newton steps.

### Step-by-Step Worked Example (Read Slowly): Counting Outer Iterations for Different Choices of $$\mu$$

Suppose a linear program has $$m = 100$$ inequality constraints, initial barrier parameter $$t^{(0)} = 1$$ (initial gap $$m/t^{(0)} = 100$$), and target accuracy $$\epsilon = 10^{-6}$$.

1. **Compute the required final $$t$$:** We stop once $$\frac{m}{t} \le \epsilon \implies t \ge \frac{100}{10^{-6}} = 10^8$$.
2. **Count outer centering steps $$k = \left\lceil \frac{\log(10^8)}{\log \mu} \right\rceil$$ across three choices of $$\mu$$:**
   - **$$\mu = 2$$ (too timid):** $$k = \lceil \log_2(10^8) \rceil = \lceil 26.57 \rceil = 27$$ outer iterations (plus 1 initial centering = 28).
   - **$$\mu = 10$$ (sweet spot):** $$k = \lceil \log_{10}(10^8) \rceil = 8$$ outer iterations ($$t = 1, 10, 10^2, \dots, 10^8$$)! If each centering takes ~4 Newton steps, total cost is only ~32 Newton steps.
   - **$$\mu = 100$$ (aggressive):** $$k = \lceil \log_{100}(10^8) \rceil = 4$$ outer iterations—half as many outer loops, *but* each jump is 10× steeper so each centering step may need 10–15 Newton steps (40–60 total).

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