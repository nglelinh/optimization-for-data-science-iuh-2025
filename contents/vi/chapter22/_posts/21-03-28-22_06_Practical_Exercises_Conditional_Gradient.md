---
layout: post
title: 22-5 Bài Tập Thực Hành - Conditional Gradient (Frank-Wolfe)
chapter: '22'
order: 6
owner: GitHub Copilot
lang: vi
categories:
- chapter22
lesson_type: required
---

# Bài Tập Thực Hành - Conditional Gradient (Frank-Wolfe)

Các bài tập được tham khảo từ Jaggi (2013) và Lacoste-Julien & Jaggi (2015).

---

## 📝 **Bài tập 1: Basic Frank-Wolfe**

$$\min_{x \in C} f(x)$$ với $$f(x) = \frac{1}{2}\|x\|^2$$, $$C = \{x : \|x\|_1 \leq 1\}$$.

**Yêu cầu:**  
a) Linear minimization oracle (LMO)  
b) Iterate từ $$x^{(0)} = 0$$  
c) Convergence rate

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) LMO:**

$$s^{(k)} = \arg\min_{s \in C} \langle \nabla f(x^{(k)}), s \rangle$$

$$= \arg\min_{\|s\|_1 \leq 1} \langle x^{(k)}, s \rangle$$

**Solution:** $$s_i = -\text{sign}(x_i^{(k)})$$ for $$i = \arg\max_j |x_j^{(k)}|$$

**b) Iteration:**

$$d^{(k)} = s^{(k)} - x^{(k)}$$

$$\gamma^{(k)} = \frac{2}{k+2}$$ (default step size)

$$x^{(k+1)} = x^{(k)} + \gamma^{(k)} d^{(k)} = (1 - \gamma^{(k)})x^{(k)} + \gamma^{(k)} s^{(k)}$$

**Iter 0:** $$x^{(0)} = 0$$, $$\nabla f = 0$$, $$s^{(0)}$$ arbitrary (say $$e_1$$)

$$x^{(1)} = \frac{2}{2}e_1 = e_1$$

**Iter 1:** $$\nabla f(e_1) = e_1$$, $$s^{(1)} = -e_1$$

$$x^{(2)} = \frac{1}{3}e_1 + \frac{2}{3}(-e_1) = -\frac{1}{3}e_1$$

**c) Convergence:**

$$f(x^{(k)}) - f^* \leq \frac{2LC_f}{k+2}$$

với $$L$$ Lipschitz constant của $$\nabla f$$, $$C_f$$ curvature constant.

**$$O(1/k)$$ convergence.**

</details>

---

## 📝 **Bài tập 2: Projection-Free**

So sánh Frank-Wolfe với Projected GD trên $$\ell_1$$ ball.

**Yêu cầu:**  
a) Complexity of projection $$\Pi_{\ell_1}(y)$$  
b) Complexity of LMO  
c) Khi nào FW better?

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Projection:**

$$\Pi_{\|·\|_1 \leq 1}(y) = \arg\min_{\|x\|_1 \leq 1} \|x - y\|^2$$

**Algorithm:** Soft-thresholding với adaptive threshold.

**Complexity:** $$O(n \log n)$$ (sorting)

**b) LMO:**

$$s = \arg\min_{\|s\|_1 \leq 1} \langle g, s \rangle = -\text{sign}(g_{\max}) e_{\max}$$

**Complexity:** $$O(n)$$ (find max)

**c) Advantage FW:**

- **Large $$n$$:** $$O(n)$$ << $$O(n \log n)$$
- **Sparse iterates:** $$x^{(k)}$$ convex combination of few atoms
- **No tuning:** step size $$\gamma = \frac{2}{k+2}$$ works

</details>

---

## 📝 **Bài tập 3: Line Search**

Thay $$\gamma = \frac{2}{k+2}$$ bằng exact line search.

**Yêu cầu:**  
a) $$\gamma^* = \arg\min_{\gamma \in [0,1]} f(x + \gamma d)$$  
b) For quadratic $$f(x) = \frac{1}{2}x^TQx - b^Tx$$  
c) Compare convergence

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Exact line search:**

$$\min_{\gamma \in [0,1]} f(x^{(k)} + \gamma d^{(k)})$$

**b) Quadratic:**

$$f(x + \gamma d) = \frac{1}{2}(x + \gamma d)^TQ(x + \gamma d) - b^T(x + \gamma d)$$

$$\frac{d}{d\gamma} = d^TQ(x + \gamma d) - b^Td = 0$$

$$\gamma^* = \frac{b^Td - x^TQd}{d^TQd} = \frac{-\nabla f(x)^T d}{d^TQd}$$

Clip to $$[0, 1]$$.

**c) Convergence:**

**Default $$\gamma = 2/(k+2)$$:** $$O(1/k)$$

**Exact line search:** $$O(1/k)$$ với better constants

**Adaptive:** Often empirically faster

</details>

---

## 📝 **Bài tập 4: Away-Step Frank-Wolfe**

Thêm "away steps" để escape slow convergence.

**Yêu cầu:**  
a) Identify active set $$\mathcal{S}^{(k)}$$  
b) Away direction $$d_A = x - v_A$$  
c) Choose between FW và away step

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Active set:**

$$x^{(k)} = \sum_{v \in \mathcal{S}^{(k)}} \alpha_v v$$ với $$\alpha_v > 0$$, $$\sum \alpha_v = 1$$

(Vertices với positive weights trong convex combination)

**b) Away vertex:**

$$v_A = \arg\max_{v \in \mathcal{S}^{(k)}} \langle \nabla f(x^{(k)}), v \rangle$$

$$d_A = x^{(k)} - v_A$$

**c) Choose step:**

$$g_{\text{FW}} = \langle \nabla f, s - x \rangle$$

$$g_{\text{away}} = \langle \nabla f, x - v_A \rangle$$

If $$g_{\text{FW}} < g_{\text{away}}$$: FW step

Else: away step with $$\gamma_{\max} = \alpha_{v_A}$$

**Result:** Faster convergence, removes redundant vertices

</details>

---

## 📝 **Bài tập 5: Applications**

**Yêu cầu:**  
a) Nuclear norm ball: $$\|X\|_* \leq \tau$$  
b) Matching polytope  
c) Probabilistic graphical models

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Nuclear norm:**

**LMO:** $$S = \arg\min_{\|S\|_* \leq \tau} \langle G, S \rangle$$

$$= -\tau u_1 v_1^T$$

với $$(u_1, v_1)$$ là top singular vectors của $$G$$.

**Complexity:** $$O(mn)$$ (top SVD) << $$O(m^2n)$$ (projection)

**b) Matching:**

**LMO:** Minimum weight perfect matching

**Complexity:** $$O(n^3)$$ (Hungarian algorithm)

**Projection:** Intractable!

**c) Graphical models:**

**LMO:** MAP inference

**Useful:** Even approximate LMO works (relaxed FW)

</details>

---

## 💡 **Tổng kết**

**Frank-Wolfe Advantages:**

| Aspect | Benefit |
|--------|---------|
| **Projection-free** | $$O(n)$$ LMO vs $$O(n \log n)$$ projection |
| **Sparse iterates** | Automatic sparsity (convex combos) |
| **Simple step size** | $$\gamma = 2/(k+2)$$ works |
| **Structured constraints** | LMO easier than projection |

**Limitations:**

- $$O(1/k)$$ convergence (slower than accelerated)
- Not strongly convex-adaptive
- Zigzagging near boundaries

**When to use:**

- Expensive projection
- Need sparse solutions
- Structured constraints (nuclear norm, matching)

---

## 📚 **Tài liệu Tham khảo**

1. Jaggi, M. (2013). "Revisiting Frank-Wolfe: Projection-Free Sparse Convex Optimization". *ICML*.
2. Lacoste-Julien, S., & Jaggi, M. (2015). "On the Global Linear Convergence of Frank-Wolfe". *NeurIPS*.

