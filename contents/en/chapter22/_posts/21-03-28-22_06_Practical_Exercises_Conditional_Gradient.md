---
layout: post
title: '22-06 Practical Exercises - Conditional Gradient (Frank-Wolfe)'
chapter: '22'
order: 7
owner: GitHub Copilot
lang: en
categories:
- chapter22
lesson_type: required
redirect_from:
  - /contents/en/chapter22/22_05_Practical_Exercises_Conditional_Gradient/
---

Reading convergence proofs for Frank–Wolfe gives you the blueprint, but the real intuition clicks only when you compute the linear minimization oracle, duality gap, and away-step drop by hand and watch how dramatically the feasible geometry shapes the trajectory. This exercise set moves deliberately from basic 2D polytope iterations to projection-free nuclear-norm steps, exact line search, and away-step linear convergence—turning every theoretical theorem from Chapter 22 into muscle memory.

## Background Knowledge Map: Diagnostic Checklist for Solving Frank–Wolfe Problems

- **Identifying the LMO Closed Form:** Always check the geometry of $$C$$ first: on a polytope, test vertices; on an $$\ell_1$$ ball of radius $$t$$, pick $$-\operatorname{sign}(g_{i^\star}) t e_{i^\star}$$; on a trace-norm ball, compute only the leading singular vector pair $$(u_1, v_1)$$.
- **Monitoring the Duality Gap $$g_k$$:** At every step, compute $$g_k = \langle \nabla f(x_k), x_k - s_k \rangle \ge f(x_k) - f(x^\star)$$. If $$g_k = 0$$, $$x_k$$ is provably optimal—never waste extra iterations once $$g_k \le \varepsilon$$.
- **Choosing Step Sizes Wisely:** Open-loop $$\gamma_k = \frac{2}{k+2}$$ is parameter-free, whereas for quadratic objectives $$f(x) = \frac{1}{2}\|Ax - b\|_2^2$$, exact line search has the closed form $$\gamma_k = \operatorname{clip}_{[0,1]}\!\left(\frac{\langle \nabla f(x_k), x_k - s_k \rangle}{\|A(s_k - x_k)\|_2^2}\right)$$.
- **Diagnosing Zig-Zagging vs. Away Steps:** Whenever iterates bounce between two boundary vertices with shrinking step sizes, compare the forward gap $$\langle g_k, x_k - s_k \rangle$$ against the away gap $$\langle g_k, v_k - x_k \rangle$$ to decide whether to drop a stale vertex.

### Step-by-Step Worked Example (Read Slowly): Warm-Up Verification Before Exercise 1

Before tackling Exercise 1, let us trace a tiny 2D quadratic on the $$\ell_1$$ diamond $$C = \{x \in \mathbb{R}^2 : |x_1| + |x_2| \le 1\}$$ with $$f(x) = \frac{1}{2}\bigl((x_1 - 2)^2 + (x_2 - 1)^2\bigr)$$ starting at $$x_0 = (0, 0)^\top$$.

1. **Iteration 0 gradient:** $$\nabla f(x_0) = (-2, -1)^\top$$.
2. **LMO on the $$\ell_1$$ diamond:** $$\arg\min_{\|s\|_1 \le 1} (-2 s_1 - s_2)$$ picks $$s_0 = (1, 0)^\top$$ (value $$-2$$).
3. **Exact line search:** Direction $$d_0 = s_0 - x_0 = (1, 0)^\top$$, so
   $$\gamma_0 = \operatorname{clip}_{[0,1]}\!\left(\frac{-\langle (-2, -1), (1, 0) \rangle}{\|(1, 0)\|_2^2}\right) = \operatorname{clip}_{[0,1]}(2) = 1.$$
   Thus $$x_1 = (1, 0)^\top$$.
4. **Check optimality at $$x_1 = (1, 0)^\top$$:**
   - Gradient: $$\nabla f(x_1) = (1 - 2, 0 - 1)^\top = (-1, -1)^\top$$.
   - LMO: $$\min_{\|s\|_1 \le 1} (-s_1 - s_2) = -1$$, achieved at $$s_1 = (1, 0)^\top$$ or $$(0, 1)^\top$$.
   - Duality gap: $$g_1 = \langle (-1, -1), (1, 0) - (1, 0) \rangle = 0$$!
   A zero duality gap certifies that $$x_1 = (1, 0)^\top$$ is already the exact constrained minimizer on the $$\ell_1$$ ball—and notice how effortless the check was compared to writing KKT multipliers.

# Practical Exercises - Conditional Gradient (Frank-Wolfe)

The exercises are adapted from Jaggi (2013) and Lacoste-Julien & Jaggi (2015).

---

## 📝 **Exercise 1: Basic Frank-Wolfe**

$$\min_{x \in C} f(x)$$ with $$f(x) = \frac{1}{2}\|x\|^2$$, $$C = \{x : \|x\|_1 \leq 1\}$$.

**Tasks:**  
a) Linear minimization oracle (LMO)  
b) Iterate from $$x^{(0)} = 0$$  
c) Convergence rate

<details>
<summary><strong>💡 Solution</strong></summary>

**a) LMO:**

$$s^{(k)} = \arg\min_{s \in C} \langle \nabla f(x^{(k)}), s \rangle$$

$$= \arg\min_{\|s\|_1 \leq 1} \langle x^{(k)}, s \rangle$$

**Solution:** $$s = -\text{sign}(x_i^{(k)})\, e_i$$ for $$i = \arg\max_j |x_j^{(k)}|$$

**b) Iteration:**

$$d^{(k)} = s^{(k)} - x^{(k)}$$

$$\gamma^{(k)} = \frac{2}{k+2}$$ (default step size)

$$x^{(k+1)} = x^{(k)} + \gamma^{(k)} d^{(k)} = (1 - \gamma^{(k)})x^{(k)} + \gamma^{(k)} s^{(k)}$$

**Iter 0:** $$x^{(0)} = 0$$, $$\nabla f = 0$$, $$s^{(0)}$$ arbitrary (say $$e_1$$)

$$x^{(1)} = \frac{2}{2}e_1 = e_1$$

**Iter 1:** $$\nabla f(e_1) = e_1$$, $$s^{(1)} = -e_1$$, $$\gamma^{(1)} = \frac{2}{3}$$

$$x^{(2)} = \frac{1}{3}e_1 + \frac{2}{3}(-e_1) = -\frac{1}{3}e_1$$

**c) Convergence:**

$$f(x^{(k)}) - f^* \leq \frac{2C_f}{k+2}$$

where $$C_f$$ is the curvature constant of $$f$$ over $$C$$ (it satisfies $$C_f \leq L\,\text{diam}(C)^2$$ when $$\nabla f$$ is $$L$$-Lipschitz).

**$$O(1/k)$$ convergence.**

</details>

---

## 📝 **Exercise 2: Projection-Free**

Compare Frank-Wolfe with projected GD on the $$\ell_1$$ ball.

**Tasks:**  
a) Complexity of the projection $$\Pi_{\ell_1}(y)$$  
b) Complexity of the LMO  
c) When is FW better?

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Projection:**

$$\Pi_{\|·\|_1 \leq 1}(y) = \arg\min_{\|x\|_1 \leq 1} \|x - y\|^2$$

**Algorithm:** soft-thresholding with an adaptive threshold.

**Complexity:** $$O(n \log n)$$ (sorting)

**b) LMO:**

$$s = \arg\min_{\|s\|_1 \leq 1} \langle g, s \rangle = -\text{sign}(g_{i^*})\, e_{i^*}, \quad i^* = \arg\max_i |g_i|$$

**Complexity:** $$O(n)$$ (find the max)

**c) Advantage of FW:**

- **Large $$n$$:** $$O(n)$$ << $$O(n \log n)$$
- **Sparse iterates:** $$x^{(k)}$$ is a convex combination of few atoms
- **No tuning:** the step size $$\gamma = \frac{2}{k+2}$$ works

</details>

---

## 📝 **Exercise 3: Line Search**

Replace $$\gamma = \frac{2}{k+2}$$ by exact line search.

**Tasks:**  
a) $$\gamma^* = \arg\min_{\gamma \in [0,1]} f(x + \gamma d)$$  
b) For the quadratic $$f(x) = \frac{1}{2}x^TQx - b^Tx$$  
c) Compare the convergence

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Exact line search:**

$$\min_{\gamma \in [0,1]} f(x^{(k)} + \gamma d^{(k)})$$

**b) Quadratic:**

$$f(x + \gamma d) = \frac{1}{2}(x + \gamma d)^TQ(x + \gamma d) - b^T(x + \gamma d)$$

$$\frac{d}{d\gamma} = d^TQ(x + \gamma d) - b^Td = 0$$

$$\gamma^* = \frac{b^Td - x^TQd}{d^TQd} = \frac{-\nabla f(x)^T d}{d^TQd}$$

Clip to $$[0, 1]$$.

**c) Convergence:**

**Default $$\gamma = 2/(k+2)$$:** $$O(1/k)$$

**Exact line search:** $$O(1/k)$$ with better constants

**Adaptive:** often faster empirically

</details>

---

## 📝 **Exercise 4: Away-Step Frank-Wolfe**

Add "away steps" to escape slow convergence.

**Tasks:**  
a) Identify the active set $$\mathcal{S}^{(k)}$$  
b) Away direction $$d_A = x - v_A$$  
c) Choose between the FW step and the away step

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Active set:**

$$x^{(k)} = \sum_{v \in \mathcal{S}^{(k)}} \alpha_v v$$ with $$\alpha_v > 0$$, $$\sum \alpha_v = 1$$

(The vertices with positive weights in the convex combination)

**b) Away vertex:**

$$v_A = \arg\max_{v \in \mathcal{S}^{(k)}} \langle \nabla f(x^{(k)}), v \rangle$$

$$d_A = x^{(k)} - v_A$$

**c) Choose the step:**

$$g_{\text{FW}} = \langle \nabla f, s - x \rangle$$

$$g_{\text{away}} = \langle \nabla f, x - v_A \rangle$$

If $$g_{\text{FW}} < g_{\text{away}}$$: FW step

Else: away step with $$\gamma_{\max} = \frac{\alpha_{v_A}}{1 - \alpha_{v_A}}$$

**Result:** faster convergence, removes redundant vertices

</details>

---

## 📝 **Exercise 5: Applications**

**Tasks:**  
a) Nuclear norm ball: $$\|X\|_* \leq \tau$$  
b) Matching polytope  
c) Probabilistic graphical models

<details>
<summary><strong>💡 Solution</strong></summary>

**a) Nuclear norm:**

**LMO:** $$S = \arg\min_{\|S\|_* \leq \tau} \langle G, S \rangle$$

$$= -\tau u_1 v_1^T$$

where $$(u_1, v_1)$$ are the top singular vectors of $$G$$.

**Complexity:** a top-singular-pair computation (cheap, e.g. power iteration, $$O(mn)$$ per iteration) << a full SVD (about $$O(m^2n)$$) for the projection

**b) Matching:**

**LMO:** minimum weight perfect matching

**Complexity:** $$O(n^3)$$ (Hungarian algorithm)

**Projection:** hard to compute!

**c) Graphical models:**

**LMO:** MAP inference

**Useful:** even an approximate LMO works (relaxed FW)

</details>

---

## 💡 **Summary**

**Frank-Wolfe Advantages:**

| Aspect | Benefit |
|--------|---------|
| **Projection-free** | $$O(n)$$ LMO vs $$O(n \log n)$$ projection |
| **Sparse iterates** | Automatic sparsity (convex combinations) |
| **Simple step size** | $$\gamma = 2/(k+2)$$ works |
| **Structured constraints** | LMO easier than projection |

**Limitations:**

- $$O(1/k)$$ convergence (slower than accelerated methods)
- Does not adapt to strong convexity
- Zigzagging near the boundary

**When to use:**

- Expensive projection
- Need sparse solutions
- Structured constraints (nuclear norm, matching)

---

## 📚 **References**

1. Jaggi, M. (2013). "Revisiting Frank-Wolfe: Projection-Free Sparse Convex Optimization". *ICML*.
2. Lacoste-Julien, S., & Jaggi, M. (2015). "On the Global Linear Convergence of Frank-Wolfe". *NeurIPS*.
