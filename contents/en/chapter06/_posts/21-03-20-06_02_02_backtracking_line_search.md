---
layout: post
title: 06-02-02 Backtracking line search
chapter: '06'
order: 7
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
---

In real-world optimization, you almost never know the global Lipschitz constant $$L$$ in advance—and even when you do, $$L$$ reflects the *worst* curvature anywhere in $$\mathbb{R}^n$$, forcing tiny steps even across flat plateaus. Backtracking line search (Armijo's rule) solves both problems in five lines of code: try a bold step first, check if the objective dropped by a fair fraction of the linear prediction, and geometrically shrink the step until it passes.

## Key ideas: Inside Armijo Backtracking Line Search

1. **The Sufficient-Decrease (Armijo) Condition**: Given parameters $$\alpha \in (0, 0.5]$$ and $$\beta \in (0, 1)$$, we accept step size $$t$$ when
   $$f(x - t\nabla f(x)) \le f(x) - \alpha t \|\nabla f(x)\|_2^2.$$
   Geometrically, the point $$(t, f(x - t\nabla f(x)))$$ must lie below a shallower secant line of slope $$-\alpha\|\nabla f(x)\|_2^2$$ drawn from $$(0, f(x))$$.
2. **Why Simply Requiring $$f(x^+) < f(x)$$ Fails**: Merely demanding strict decrease allows tiny steps that stall far from the minimum (or huge steps that barely drop $$f$$). The $$\alpha t\|\nabla f(x)\|_2^2$$ margin guarantees progress proportional to both the step size and the squared gradient norm.
3. **Guaranteed Finite Termination**: Because $$f(x - t\nabla f(x)) \le f(x) - t(1 - \frac{Lt}{2})\|\nabla f(x)\|_2^2$$ for $$L$$-smooth functions, any $$t \le \frac{2(1-\alpha)}{L}$$ (in particular $$t \le 1/L$$ when $$\alpha \le 0.5$$) automatically satisfies Armijo! Hence backtracking stops with $$t \ge \min(t_0, \beta/L)$$ in at most $$O(\log(L))$$ evaluations.
4. **Typical Hyperparameter Choices**: In practice, $$\alpha \in [0.01, 0.3]$$ (very permissive so large steps are accepted) and $$\beta \in [0.5, 0.8]$$ (halving or gently shrinking $$t$$) work reliably across convex and smooth nonconvex objectives.

### Worked example: Tracing Every Backtracking Trial on $$f(x) = x^4 - 4x$$

Run one iteration of Armijo backtracking on $$f(x) = x^4 - 4x$$ starting at $$x = 0$$, with initial step $$t = 1$$, $$\alpha = 0.25$$, and $$\beta = 0.5$$.

1. **Evaluate $$f(x)$$ and $$f'(x)$$ at $$x = 0$$**:
   - $$f(0) = 0$$, and $$f'(x) = 4x^3 - 4 \implies f'(0) = -4$$.
   - Descent direction is $$-f'(0) = +4$$, and $$\|f'(0)\|_2^2 = 16$$.
   - Armijo threshold for any candidate $$t$$:
     $$f(0 + 4t) \le 0 - 0.25 \cdot t \cdot 16 = -4t.$$
2. **Trial 1 ($$t = 1$$)**:
   - Candidate point: $$x_{\mathrm{try}} = 4$$, where $$f(4) = 4^4 - 4(4) = 256 - 16 = 240$$.
   - Threshold: $$-4(1) = -4$$. Since $$240 > -4$$, **reject** and shrink $$t \leftarrow 0.5$$.
3. **Trial 2 ($$t = 0.5$$)**:
   - Candidate point: $$x_{\mathrm{try}} = 2$$, where $$f(2) = 16 - 8 = 8$$.
   - Threshold: $$-4(0.5) = -2$$. Since $$8 > -2$$, **reject** and shrink $$t \leftarrow 0.25$$.
4. **Trial 3 ($$t = 0.25$$)**:
   - Candidate point: $$x_{\mathrm{try}} = 1$$, where $$f(1) = 1 - 4 = -3$$.
   - Threshold: $$-4(0.25) = -1$$. Since $$-3 \le -1$$, **ACCEPT!**
   - Notice $$x = 1$$ happens to be the exact global minimizer of $$x^4 - 4x$$ (where $$f'(1) = 0$$), reached in one adaptive iteration without ever knowing a global Lipschitz constant!

## Introduction: The Step Size Problem

In gradient descent, we use the update rule:
$$x_{k+1} = x_k - t_k \nabla f(x_k)$$

where:
- $$x_k$$ is our current position at iteration $$k$$
- $$\nabla f(x_k)$$ is the gradient (tells us the direction of steepest ascent)
- $$t_k > 0$$ is the **step size** (how far we move in that direction)

### Why Do We Need Adaptive Step Sizes?

**The Problem with Fixed Step Sizes:**
- If $$t_k$$ is too small → we make slow progress (many tiny steps)
- If $$t_k$$ is too large → we might overshoot the minimum or even diverge
- A fixed step size can't adapt to different regions of the function

**The Solution:** Use an **adaptive step size** that automatically adjusts based on the function's behavior. One of the most popular methods is **backtracking line search**.

## What is Backtracking Line Search?

**The Core Idea:** Start with a large step size and progressively make it smaller until we find a "good enough" step.

Think of it like this:
1. **Try a big step** - Maybe we can make fast progress!
2. **Check if it's too big** - Did we overshoot or not improve enough?
3. **If yes, backtrack** - Make the step smaller and try again
4. **Repeat until satisfied** - Stop when we find an acceptable step

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter06/06_02_02_Backtracking_Line_Search.png" alt="backtrackinglinesearch1" width="100%" height="100%">
  <figcaption style="text-align: center;">[Fig1] Backtracking Line Search: The red line shows the "acceptance threshold" - if our function value (blue curve) goes below this line, we accept the step size [3]</figcaption>
</p>
</figure>

### The Mathematical Condition

We accept a step size $$t$$ if it provides **sufficient decrease** in the function value:

$$f(x - t \nabla f(x)) \leq f(x) - \alpha t \|\nabla f(x)\|_2^2$$

where:
- **Left side:** The actual function value after taking the step
- **Right side:** The current function value minus a threshold for "sufficient decrease"
- $$\alpha \in (0, 0.5]$$ is a parameter that controls how much decrease we require (typically $$\alpha = 0.5$$)

**Intuition:** The right side represents a linear approximation of how much the function *should* decrease. If the actual decrease (left side) is at least this much, we accept the step.

## The Backtracking Line Search Algorithm

### Parameters
- $$\alpha \in (0, 0.5]$$: Controls how much decrease we require (typically $$\alpha = 0.5$$)
- $$\beta \in (0, 1)$$: Controls how much we shrink the step size when backtracking (typically $$\beta = 0.8$$ or $$\beta = 0.9$$)

### Algorithm Steps

**Input:** Current point $$x$$, gradient $$\nabla f(x)$$
**Output:** Good step size $$t$$

1. **Initialize:** Set $$t = 1$$ (start with a full step)

2. **Check the condition:** While the sufficient decrease condition is NOT satisfied:
   $$f(x - t \nabla f(x)) > f(x) - \alpha t \|\nabla f(x)\|_2^2$$

3. **Backtrack:** Set $$t = \beta \cdot t$$ (shrink the step size)

4. **Update:** Use the final $$t$$ to update: $$x^+ = x - t \nabla f(x)$$

### Step-by-Step Example

Let's say we're at point $$x$$ with gradient $$\nabla f(x)$$:

1. **Try $$t = 1$$:** Check if $$f(x - 1 \cdot \nabla f(x)) \leq f(x) - \alpha \|\nabla f(x)\|_2^2$$
   - If YES → Accept $$t = 1$$
   - If NO → Continue to step 2

2. **Try $$t = 0.8$$:** Check if $$f(x - 0.8 \nabla f(x)) \leq f(x) - 0.8\alpha \|\nabla f(x)\|_2^2$$
   - If YES → Accept $$t = 0.8$$
   - If NO → Continue to step 3

3. **Try $$t = 0.64$$:** Check if $$f(x - 0.64 \nabla f(x)) \leq f(x) - 0.64\alpha \|\nabla f(x)\|_2^2$$
   - And so on...

## Why Does This Work? The Mathematical Intuition

### The Sufficient Decrease Condition Explained

The condition $$f(x - t \nabla f(x)) \leq f(x) - \alpha t \|\nabla f(x)\|_2^2$$ can be understood as:

**Left side:** $$f(x - t \nabla f(x))$$ = The actual function value after taking the step

**Right side:** $$f(x) - \alpha t \|\nabla f(x)\|_2^2$$ = Current value minus expected decrease

The expected decrease $$\alpha t \|\nabla f(x)\|_2^2$$ comes from the **linear approximation**:
$$f(x - t \nabla f(x)) \approx f(x) - t \|\nabla f(x)\|_2^2$$

We require the actual decrease to be at least a fraction $$\alpha$$ of this predicted decrease.

### Why This Guarantees Progress

1. **Prevents tiny steps:** The condition ensures we don't accept arbitrarily small step sizes
2. **Prevents overshooting:** If we overshoot, the function value won't decrease enough
3. **Balances speed and stability:** We get reasonably large steps while maintaining convergence

### Performance Comparison

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter06/06_02_02_Convergence.png" alt="backtrackinglinesearch1" width="70%" height="70%">
  <figcaption style="text-align: center;">[Fig2] Convergence comparison: Backtracking line search (adaptive) vs Fixed step size. Notice how the adaptive method converges much faster! [3]</figcaption>
</p>
</figure>

## Practical Example: Minimizing a Quadratic Function

Let's work through a detailed example to see backtracking line search in action!

### Example 1: Simple Quadratic (Lucky Case)

**Problem:** Minimize $$f(x) = \frac{1}{2}x^2$$ starting from $$x_0 = 4$$

**Setup:** 
- Parameters: $$\alpha = 0.5$$, $$\beta = 0.8$$
- Gradient: $$\nabla f(x) = x$$
- Optimal solution: $$x^* = 0$$

**Iteration 1:**
- Current: $$x = 4$$, $$\nabla f(x) = 4$$, $$f(x) = 8$$
- Try $$t = 1$$: 
  - New point: $$x - t\nabla f(x) = 4 - 1 \cdot 4 = 0$$
  - Function value: $$f(0) = 0$$
- **Check sufficient decrease:** $$f(0) \leq f(4) - \alpha t \|\nabla f(4)\|^2$$
  - Left side: $$0$$
  - Right side: $$8 - 0.5 \cdot 1 \cdot 16 = 0$$
  - $$0 \leq 0$$ ✓ (Accept $$t = 1$$)
- Update: $$x_1 = 0$$ 

**Result:** We reached the optimum in one step! This is because the quadratic function is "well-behaved."

### Example 2: A Non-Convex Function

**Problem:** Minimize $$f(x) = x^2 + 10\sin(x)$$ starting from $$x_0 = 3$$

This function is not convex. It has a local minimum near $$x \approx 3.84$$ and its global minimum near $$x \approx -1.31$$. Let's see what backtracking does here.

**Setup:**
- Parameters: $$\alpha = 0.3$$, $$\beta = 0.7$$
- Gradient: $$\nabla f(x) = 2x + 10\cos(x)$$

**Iteration 1:**
- Current: $$x = 3$$, $$\nabla f(3) = 6 + 10\cos(3) \approx -3.900$$, $$\vert\nabla f(3)\vert^2 \approx 15.21$$, $$f(3) = 9 + 10\sin(3) \approx 10.41$$
- The gradient is negative, so the step $$-t\nabla f(x)$$ moves to the right.

| Try | $$t$$ | $$x - t\nabla f(x)$$ | $$f(x - t\nabla f(x))$$ | $$f(x) - \alpha t \vert\nabla f(x)\vert^2$$ | Accept? |
|-----|-------|----------------------|--------------------------|----------------------------------------------|---------|
| 1 | 1 | 6.900 | 53.39 | 5.85 | ✗ |
| 2 | 0.7 | 5.730 | 27.58 | 7.22 | ✗ |
| 3 | 0.49 | 4.911 | 14.31 | 8.18 | ✗ |
| 4 | 0.343 | 4.338 | 9.51 | 8.85 | ✗ |
| 5 | 0.2401 | 3.936 | 8.36 | 9.32 | ✓ |

After 4 backtracking steps we accept $$t = 0.2401$$ and move to $$x_1 \approx 3.936$$, with $$f(x_1) \approx 8.36$$.

**Iteration 2:**
- Current: $$x_1 \approx 3.936$$, $$\nabla f(x_1) \approx 0.868$$ (now positive, so we step to the left).
- The trials $$t = 1, 0.7, 0.49, 0.343, 0.2401, 0.168$$ are all rejected. The step $$t = 0.7^6 \approx 0.1176$$ is accepted, which gives $$x_2 \approx 3.834$$, $$f(x_2) \approx 8.3156$$.

**Next iterations:** the gradient drops quickly: $$\vert\nabla f(x_3)\vert \approx 3 \times 10^{-4}$$ and $$\vert\nabla f(x_4)\vert \approx 3 \times 10^{-6}$$. The method converges to $$x \approx 3.8375$$ with $$f \approx 8.3156$$.

**Result:** Backtracking always gives a decrease in $$f$$, but on a non-convex function it only finds the **local** minimum near the starting point. The global minimum $$f(-1.3064) \approx -7.946$$ is on the other side of a hill, and gradient descent from $$x_0 = 3$$ never gets there.

### Example 3: A Smooth Convex Function

**Problem:** Minimize $$f(x) = x^2 + 0.1x^4$$ starting from $$x_0 = 2$$

**Setup:**
- Parameters: $$\alpha = 0.5$$, $$\beta = 0.8$$
- Gradient: $$\nabla f(x) = 2x + 0.4x^3$$
- At $$x = 2$$: $$\nabla f(2) = 4 + 3.2 = 7.2$$, $$\vert\nabla f(2)\vert^2 = 51.84$$, $$f(2) = 4 + 1.6 = 5.6$$

**Iteration 1:**

| Try | $$t$$ | $$2 - 7.2\,t$$ | $$f(2 - 7.2\,t)$$ | $$5.6 - 0.5 \cdot 51.84\, t$$ | Accept? |
|-----|-------|----------------|--------------------|-------------------------------|---------|
| 1 | 1 | -5.200 | 100.16 | -20.32 | ✗ |
| 2 | 0.8 | -3.760 | 34.12 | -15.14 | ✗ |
| 3 | 0.64 | -2.608 | 11.43 | -10.99 | ✗ |
| 4 | 0.512 | -1.686 | 3.653 | -7.671 | ✗ |
| 5 | 0.4096 | -0.949 | 0.982 | -5.017 | ✗ |
| 6 | 0.3277 | -0.359 | 0.131 | -2.893 | ✗ |
| 7 | 0.2621 | 0.113 | 0.0127 | -1.195 | ✗ |
| 8 | 0.2097 | 0.490 | 0.246 | 0.164 | ✗ |
| 9 | 0.1678 | 0.792 | 0.667 | 1.251 | ✓ **Accept!** |

**Result:** After 8 backtracking steps, we accept $$t = 0.8^8 \approx 0.168$$ and update to $$x_1 \approx 0.792$$.

Note that some rejected steps (for example $$t = 0.2621$$, which lands at $$x \approx 0.113$$) give a much smaller $$f$$ than the accepted one. They are rejected because the right-hand side is negative there, and $$f \ge 0$$ everywhere. With $$\alpha = 0.5$$, the condition demands a large decrease, so it only accepts small enough steps.

### Key Insights from These Examples

1. **Simple functions** (like pure quadratics) may converge in one step
2. **Complex functions** require multiple backtracking steps to find safe step sizes
3. **The algorithm is robust** - it automatically finds appropriate step sizes without manual tuning
4. **Each backtracking iteration** makes the step size smaller by factor $$\beta$$
5. **The sufficient decrease condition** prevents both overshooting and accepting tiny progress

### Why This Beats Fixed Step Sizes

Let's see a head-to-head comparison! We'll minimize $$f(x) = x^2 - 2x + 5$$ starting from $$x_0 = 4$$.

**Function details:**
- Gradient: $$\nabla f(x) = 2x - 2$$
- Optimal solution: $$x^* = 1$$ with $$f(x^*) = 4$$
- Starting point: $$x_0 = 4$$, $$f(x_0) = 13$$

## Comparison: Fixed Step Size vs Backtracking Line Search

### Method 1: Fixed Small Step Size ($$t = 0.1$$)

Here $$x_{k+1} - 1 = 0.8\,(x_k - 1)$$, so the error shrinks by only 20% per step.

| Iteration | $$x_k$$ | $$\nabla f(x_k)$$ | $$x_{k+1} = x_k - 0.1 \nabla f(x_k)$$ | $$f(x_{k+1})$$ |
|-----------|---------|-------------------|---------------------------------------|----------------|
| 0 | 4.0 | 6.0 | 3.4 | 9.76 |
| 1 | 3.4 | 4.8 | 2.92 | 7.6864 |
| 2 | 2.92 | 3.84 | 2.536 | 6.359296 |
| 3 | 2.536 | 3.072 | 2.2288 | 5.509949 |
| 4 | 2.2288 | 2.4576 | 1.98304 | 4.966368 |
| 5 | 1.98304 | 1.96608 | 1.786432 | 4.618475 |
| ... | ... | ... | ... | ... |
| 20 | 1.034588 | 0.069175 | 1.027670 | 4.000766 |
| ... | ... | ... | ... | ... |
| **50** | **1.000043** | **0.000086** | **1.000034** | **4.000000001** |

**Result:** It does converge, but slowly: it needs 36 iterations to reach $$\vert x_k - 1\vert < 10^{-3}$$ and 67 iterations to reach $$\vert x_k - 1\vert < 10^{-6}$$.

### Method 2: Fixed Large Step Size ($$t = 1.5$$)

| Iteration | $$x_k$$ | $$\nabla f(x_k)$$ | $$x_{k+1} = x_k - 1.5 \nabla f(x_k)$$ | $$f(x_{k+1})$$ |
|-----------|---------|-------------------|---------------------------------------|----------------|
| 0 | 4.0 | 6.0 | -5.0 | 40 |
| 1 | -5.0 | -12.0 | 13.0 | 148 |
| 2 | 13.0 | 24.0 | -23.0 | 580 |
| 3 | -23.0 | -48.0 | 49.0 | 2308 |
| 4 | 49.0 | 96.0 | -95.0 | 9220 |

**Result:** Diverges! Here $$x_{k+1} - 1 = -2\,(x_k - 1)$$, so the error doubles and changes sign at every step.

### Method 3: Fixed Medium Step Size ($$t = 0.5$$)

| Iteration | $$x_k$$ | $$\nabla f(x_k)$$ | $$x_{k+1} = x_k - 0.5 \nabla f(x_k)$$ | $$f(x_{k+1})$$ |
|-----------|---------|-------------------|---------------------------------------|----------------|
| 0 | 4.0 | 6.0 | 1.0 | 4.0 |
| 1 | 1.0 | 0.0 | 1.0 | 4.0 |

**Result:** Lucky guess! It reaches the optimum in one step, because $$t = 0.5 = 1/f''(x)$$ is exactly the Newton step for this quadratic. For another function, $$t = 0.5$$ could be too small or too large.

### Method 4: Backtracking Line Search ($$\alpha = 0.5$$, $$\beta = 0.8$$)

**Iteration 1:**
- Current: $$x = 4$$, $$\nabla f(x) = 6$$, $$\vert\nabla f(x)\vert^2 = 36$$, $$f(x) = 13$$
- Try $$t = 1$$: $$x - t\nabla f(x) = 4 - 6 = -2$$, $$f(-2) = 13$$
- Check: $$13 \leq 13 - 0.5 \cdot 1 \cdot 36 = -5$$ ✗ (Too big!)
- Try $$t = 0.8$$: $$x - t\nabla f(x) = 4 - 4.8 = -0.8$$, $$f(-0.8) = 7.24$$
- Check: $$7.24 \leq 13 - 0.5 \cdot 0.8 \cdot 36 = -1.4$$ ✗ (Still too big!)
- Try $$t = 0.64$$: $$x - t\nabla f(x) = 4 - 3.84 = 0.16$$, $$f(0.16) = 4.7056$$
- Check: $$4.7056 \leq 13 - 0.5 \cdot 0.64 \cdot 36 = 1.48$$ ✗ (Still too big!)
- Try $$t = 0.512$$: $$x - t\nabla f(x) = 4 - 3.072 = 0.928$$, $$f(0.928) = 4.005184$$
- Check: $$4.005184 \leq 13 - 0.5 \cdot 0.512 \cdot 36 = 3.784$$ ✗ (Rejected, even though $$x = 0.928$$ is close to the optimum!)
- Try $$t = 0.4096$$: $$x - t\nabla f(x) = 4 - 2.4576 = 1.5424$$, $$f(1.5424) \approx 4.2942$$
- Check: $$4.2942 \leq 13 - 0.5 \cdot 0.4096 \cdot 36 = 5.6272$$ ✓ **Accept!**
- Update: $$x_1 = 1.5424$$

**Why is $$t = 0.512$$ rejected?** For this function, $$f(x - tg) = f(x) - t g^2 + t^2 g^2$$ with $$g = \nabla f(x)$$. The condition $$f(x - tg) \leq f(x) - 0.5\, t g^2$$ is then the same as $$t \leq 0.5$$. So at every iteration, the trials $$1, 0.8, 0.64, 0.512$$ are rejected and $$t = 0.4096$$ is accepted.

**Iteration 2:**
- Current: $$x = 1.5424$$, $$\nabla f(x) = 1.0848$$, $$f(x) \approx 4.2942$$
- Again $$t = 1, 0.8, 0.64, 0.512$$ are rejected, and $$t = 0.4096$$ is accepted.
- Update: $$x_2 = 1.5424 - 0.4096 \cdot 1.0848 \approx 1.0981$$

**Next iterations:** each iteration multiplies the error by $$\vert 1 - 2 \cdot 0.4096\vert = 0.1808$$:

| Iteration $$k$$ | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|-----------------|---|---|---|---|---|---|---|---|---|
| $$x_k$$ | 1.5424 | 1.0981 | 1.0177 | 1.0032 | 1.00058 | 1.000105 | 1.000019 | 1.0000034 | 1.0000006 |

**Result:** Backtracking reaches $$\vert x_k - 1\vert < 10^{-3}$$ after 5 iterations and $$\vert x_k - 1\vert < 10^{-6}$$ after **9 iterations**, using 45 function evaluations in total (5 trials per iteration). It needs no tuning, while the fixed step $$t = 0.1$$ needs 67 iterations for the same accuracy.

## Performance Summary

| Method | Iterations to $$\vert x_k - 1\vert < 10^{-6}$$ | Comments |
|--------|-------------------------------------------------|----------|
| Fixed Small ($$t = 0.1$$) | 67 | Safe but slow |
| Fixed Large ($$t = 1.5$$) | ∞ | Diverges |
| Fixed Medium ($$t = 0.5$$) | 1 | Lucky guess only! |
| **Backtracking** | **9** (45 function evaluations) | **Robust, no tuning** |

## Key Insights

1. **Fixed small steps:** Safe but painfully slow
2. **Fixed large steps:** Fast when they work, catastrophic when they don't
3. **Fixed "perfect" steps:** Impossible to find without knowing the answer
4. **Backtracking:** Automatically finds good step sizes, robust across different functions

### The Real Power: Robustness Across Functions

The magic of backtracking line search is that it works well for ANY function:

- **Gentle functions:** Takes appropriately large steps for fast progress
- **Steep functions:** Automatically reduces step size to prevent overshooting  
- **Varying functions:** Adapts step size throughout the optimization process
- **Unknown functions:** No need to guess the "right" step size beforehand

**Bottom line:** Backtracking line search gives you the speed of large steps when safe, and the stability of small steps when necessary - automatically!

## Advantages and Practical Considerations

### Advantages:
1. **Automatic adaptation:** No need to manually tune step sizes
2. **Convergence guarantees:** Theoretical guarantees for convex functions
3. **Simple implementation:** Easy to code and understand
4. **Robust:** Works well across different types of problems

### Practical Tips:
- **Typical parameter values:** $$\alpha = 0.5$$, $$\beta = 0.8$$ or $$\beta = 0.9$$
- **Computational cost:** Each backtracking step requires one function evaluation
- **When to use:** Especially useful when the function's "landscape" varies significantly

## Summary

**Backtracking line search** solves the fundamental problem of choosing good step sizes in gradient descent:

1. **Start optimistic:** Try a large step size ($$t = 1$$)
2. **Test rigorously:** Check if the step provides sufficient decrease
3. **Adapt intelligently:** If not, shrink the step size and try again
4. **Guarantee progress:** The mathematical condition ensures we always make meaningful progress

This simple yet powerful technique transforms gradient descent from a method that requires careful tuning into a robust, adaptive algorithm that works well out of the box.

**Next time** you implement gradient descent, consider adding backtracking line search - your algorithm will converge faster and be much more reliable!

### Backtracking and exact line search in about 3 minutes

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/line-search_en.mp4"></video>
</div>

Fixed steps that are too small or too large, the Armijo condition and the shrinks t ← βt, compared with exact search on the lesson's examples.
