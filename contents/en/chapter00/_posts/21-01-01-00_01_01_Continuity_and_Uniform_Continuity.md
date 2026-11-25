---
layout: post
title: 00-01-01 Continuity and Uniform Continuity
chapter: '00'
order: 3
owner: GitHub Copilot
lang: en
categories:
- chapter00
lesson_type: required
---

Suppose you are calibrating a robotic arm's torque controller: if a tiny $$0.001$$-radian sensor jitter causes a sudden jump in predicted energy cost, no line-search algorithm can trust its own step sizes. Worse yet, even if a function is continuous at every individual point, its slope might blow up near the edge of the domain, forcing step sizes to shrink unpredictably. Distinguishing ordinary continuity, uniform continuity, and Lipschitz continuity is how analysts guarantee that a *single* global step size works across the entire optimization domain.

## Background Knowledge Map: The Hierarchy of Function Regularity

- **Pointwise Continuity:** Guarantees no sudden jumps at a fixed point $$c$$, but the allowable input tolerance $$\delta(\varepsilon, c)$$ may depend heavily on *where* $$c$$ sits in the domain.
- **Uniform Continuity:** Upgrades the guarantee so that one tolerance $$\delta(\varepsilon)$$ works simultaneously everywhere on the domain—automatically achieved by any continuous function on a compact set (Heine–Cantor theorem).
- **Lipschitz Continuity:** Enforces a uniform global bound $$|f(x) - f(y)| \le L\|x - y\|$$ on how fast outputs can change per unit input, directly controlling subgradient norms and convergence rates.
- **Strict Inclusion Hierarchy:** $$\text{Lipschitz Continuous} \subset \text{Uniformly Continuous} \subset \text{Continuous}$$—knowing which tier an objective occupies determines which convergence theorems apply.

### Step-by-Step Worked Example (Read Slowly): Why $$f(x) = x^2$$ Is Lipschitz on $$[0, 2]$$ but Not Uniformly Continuous on $$[0, \infty)$$

1. **Bounded domain $$[0, 2]$$ (Lipschitz proof):** For any $$x, y \in [0, 2]$$, factor the difference:
   $$|f(x) - f(y)| = |x^2 - y^2| = |x + y|\,|x - y|.$$
   Since $$0 \le x, y \le 2$$, we have $$|x + y| \le 4$$, so
   $$|f(x) - f(y)| \le 4|x - y|.$$
   Thus $$f$$ is Lipschitz continuous on $$[0, 2]$$ with Lipschitz constant $$L = 4$$ (and hence uniformly continuous with $$\delta = \varepsilon / 4$$).
2. **Unbounded domain $$[0, \infty)$$ (failure of uniform continuity):** Choose $$\varepsilon = 1$$ and test the sequences $$x_n = n$$ and $$y_n = n + \frac{1}{n}$$ for any integer $$n \ge 1$$.
   - Input separation: $$|y_n - x_n| = \frac{1}{n} \to 0$$ as $$n \to \infty$$ (smaller than any proposed $$\delta > 0$$ for large $$n$$).
   - Output separation:
     $$|y_n^2 - x_n^2| = \left(n^2 + 2 + \frac{1}{n^2}\right) - n^2 = 2 + \frac{1}{n^2} > 2 > \varepsilon.$$
   Because no single $$\delta > 0$$ can keep the output change below $$1$$ across all of $$[0, \infty)$$, $$x^2$$ is continuous everywhere yet fails to be uniformly continuous on $$[0, \infty)$$.

This lesson introduces the fundamental concepts of continuity and uniform continuity, which are essential for understanding the behavior of functions in optimization.

---

## Continuity and Uniform Continuity

**Continuity** and **Uniform Continuity** are fundamental concepts that describe the behavior of functions, particularly concerning their "smoothness" or "predictability." While closely related, they capture distinct properties, with uniform continuity being a stronger condition than mere continuity.

### Definition of Continuity

A function $$f: A \to \mathbb{R}$$ is said to be **continuous at a point** $$c \in A$$ if, for every positive real number $$\varepsilon > 0$$, there exists a positive real number $$\delta > 0$$ such that for all $$x \in A$$, if 

$$\lvert x - c \rvert < \delta$$

then 

$$\lvert f(x) - f(c) \rvert < \varepsilon$$ 

Intuitively, it means that for any desired level of precision $$\varepsilon$$ in the output $$f(x)$$, we can find a sufficiently small interval around $$c$$ (of width $$2\delta$$) such that all $$x$$ values within this interval map to $$f(x)$$ values within an $$\varepsilon$$-interval around $$f(c)$$. The crucial aspect here is that the choice of $$\delta$$ generally depends not only on $$\varepsilon$$ but also on the specific point $$c$$.

A function is **continuous on a set** $$A$$ if it is continuous at every point $$c \in A$$.

**Examples of continuous functions** include all polynomials (e.g., $$f(x) = x^2 + 3x - 1$$), trigonometric functions like $$\sin(x)$$ and $$\cos(x)$$, and exponential functions $$e^x$$ on their respective domains. 

### Definition of Uniform Continuity

**Uniform Continuity**, on the other hand, imposes a more stringent condition. A function $$f: A \to \mathbb{R}$$ is said to be **uniformly continuous on a set** $$A$$ if, for every positive real number $$\varepsilon > 0$$, there exists a positive real number $$\delta > 0$$ such that for all $$x, y \in A$$, if 

$$\lvert x - y \rvert < \delta$$

then 

$$\lvert f(x) - f(y) \rvert < \varepsilon$$

The **key distinction** from point-wise continuity lies in the order of quantifiers: for **uniform** continuity, the $$\delta$$ depends *only* on $$\varepsilon$$ and is independent of the specific points $$x$$ and $$y$$ in the domain.

### Definition of Lipschitz Continuity

**Lipschitz Continuity** provides an even more specific and quantitative notion of continuity. A function $$f: A \to \mathbb{R}$$ is said to be **Lipschitz continuous** (or **L-Lipschitz**) on a set $$A$$ if there exists a constant $$L \geq 0$$ such that for all $$x, y \in A$$:

$$\lvert f(x) - f(y) \rvert \leq L \lvert x - y \rvert$$

The smallest such constant $$L$$ is called the **Lipschitz constant** or **Lipschitz modulus** of $$f$$.

**Key Properties of Lipschitz Continuity:**

1. **Bounded Rate of Change**: The Lipschitz condition ensures that the function cannot change faster than a linear rate determined by $$L$$.

2. **Uniform Continuity**: Every Lipschitz continuous function is uniformly continuous (choose $$\delta = \varepsilon/L$$ for $$L > 0$$).

3. **Almost Everywhere Differentiability**: Lipschitz continuous functions are differentiable almost everywhere, and where the derivative exists, $$\lvert f'(x) \rvert \leq L$$.

**Examples:**
- $$f(x) = \lvert x \rvert$$ is 1-Lipschitz on $$\mathbb{R}$$
- $$f(x) = \sin(x)$$ is 1-Lipschitz on $$\mathbb{R}$$ (since $$\lvert \cos(x) \rvert \leq 1$$)
- $$f(x) = x^2$$ is not Lipschitz on $$\mathbb{R}$$ but is Lipschitz on any bounded interval

### Key Differences and Hierarchy

The three types of continuity form a hierarchy of increasingly strong conditions:

**Continuity ⊆ Uniform Continuity ⊆ Lipschitz Continuity**

1. **Point-wise vs Global**: 
   - **Continuity**: Local property (checked at each point)
   - **Uniform Continuity**: Global property of the entire function
   - **Lipschitz Continuity**: Global property with quantitative bounds

2. **Choice of $$\delta$$**: 
   - **Continuity**: $$\delta$$ can depend on both $$\varepsilon$$ and the specific point $$c$$
   - **Uniform Continuity**: $$\delta$$ depends only on $$\varepsilon$$, working for all points simultaneously
   - **Lipschitz Continuity**: $$\delta = \varepsilon/L$$ provides explicit relationship

3. **Rate of Change Control**:
   - **Continuity**: No control over rate of change
   - **Uniform Continuity**: Ensures bounded variation over small intervals
   - **Lipschitz Continuity**: Provides explicit linear bound on rate of change

4. **Strength Relationships**: 
   - Every Lipschitz continuous function is uniformly continuous
   - Every uniformly continuous function is continuous
   - The converses are not generally true

### Detailed Examples and Comparisons

**Example 1: $$f(x) = x^2$$**
- **On $$\mathbb{R}$$**: Continuous but not uniformly continuous (rate of change $$\lvert f'(x) \rvert = 2\lvert x \rvert$$ is unbounded)
- **On $$[0,1]$$**: Continuous, uniformly continuous, and Lipschitz with $$L = 2$$

**Example 2: $$f(x) = \sin(x)$$**
- **On $$\mathbb{R}$$**: Continuous, uniformly continuous, and 1-Lipschitz (since $$\lvert \cos(x) \rvert \leq 1$$)

**Example 3: $$f(x) = \lvert x \rvert$$**
- **On $$\mathbb{R}$$**: Continuous, uniformly continuous, and 1-Lipschitz
- **Note**: Not differentiable at $$x = 0$$, but still Lipschitz

**Example 4: $$f(x) = \sqrt{x}$$**
- **On $$[0,1]$$**: Continuous and uniformly continuous, but not Lipschitz (derivative unbounded near $$x = 0$$)
- **On $$[a,1]$$ for $$a > 0$$**: Lipschitz with $$L = 1/(2\sqrt{a})$$
