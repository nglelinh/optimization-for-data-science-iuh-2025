---
layout: post
title: 03-03 The conjugate function
chapter: '03'
order: 7
owner: Minjoo Lee
categories:
- chapter03
lang: en
lesson_type: required
---

Instead of describing a smooth curve by its height $$f(x)$$ at each position $$x$$, you can describe the exact same curve by the vertical intercept of every tangent line of slope $$y$$. That slope-indexed re-encoding is the **Fenchel conjugate** $$f^*(y) = \sup_x (y^T x - f(x))$$. It is one of the deepest ideas in all of optimization: it automatically converts primal constraints into dual objectives, links smoothness of $$f$$ to strong convexity of $$f^*$$, and powers Moreau's decomposition for proximal algorithms.

## Key ideas: Intuition and Power of the Fenchel Conjugate

- **Geometric Meaning (Maximum Vertical Gap):** For a fixed slope $$y$$, $$f^*(y) = \sup_x (y^T x - f(x))$$ finds the maximum amount by which the linear function $$y^T x$$ rises above $$f(x)$$—i.e., the negative $$y$$-intercept of the supporting hyperplane with slope $$y$$.
- **Always Convex:** Because $$f^*(y)$$ is a pointwise supremum of affine functions of $$y$$, $$f^*$$ is *always* convex and closed—even when the original function $$f$$ is nonconvex!
- **Fenchel–Young Inequality:** Directly from the supremum definition, $$f(x) + f^*(y) \ge y^T x$$ for all $$x, y$$, with equality if and only if $$y \in \partial f(x)$$ (tangent slope matches $$y$$).
- **Biconjugate ($$f^{**} = f$$):** For any closed proper convex function, taking the conjugate twice recovers $$f$$ identically; for a nonconvex $$f$$, $$f^{**}$$ produces its tightest convex envelope!

### Worked example: Conjugate of a Quadratic and Fenchel–Young Check

Compute the Fenchel conjugate of $$f(x) = \frac{1}{2}a x^2$$ (where $$a > 0$$) and verify Fenchel's inequality numerically.

1. **Maximize $$g(x) = yx - \frac{1}{2}a x^2$$ over $$x \in \mathbb{R}$$:**
   $$g'(x) = y - ax = 0 \implies x^* = \frac{y}{a}.$$
   Since $$g''(x) = -a < 0$$, $$x^* = y/a$$ is the unique global maximizer.
2. **Substitute $$x^*$$ back into $$g(x)$$:**
   $$f^*(y) = y\left(\frac{y}{a}\right) - \frac{1}{2}a\left(\frac{y}{a}\right)^2 = \frac{y^2}{a} - \frac{y^2}{2a} = \frac{y^2}{2a}.$$
   Notice the duality of curvature: large curvature $$a$$ in $$f$$ becomes small curvature $$1/a$$ in $$f^*$$!
3. **Numerical check of Fenchel's inequality ($$a = 4, x = 2$$):**
   - With $$y = 6 \neq f'(2) = 8$$: $$f(2) + f^*(6) = 8 + \frac{36}{8} = 12.5 > 12 = xy$$ (strict inequality).
   - With $$y = f'(2) = 8$$: $$f(2) + f^*(8) = 8 + \frac{64}{8} = 16 = 2 \cdot 8 = xy$$ (exact equality!).

This section introduces the conjugate function (also known as the convex conjugate or Fenchel conjugate), a fundamental concept in convex analysis and duality theory that provides a powerful tool for transforming optimization problems.

## Definition and Mathematical Foundation

For a function $$f: \mathbb{R}^n \to \mathbb{R}$$, the **conjugate function** $$f^*: \mathbb{R}^n \to \mathbb{R}$$ is defined as:

$$f^*(y) = \sup_{x \in \text{dom}(f)} \{y^T x - f(x)\}$$

where $$\sup$$ denotes the supremum (least upper bound) over all $$x$$ in the domain of $$f$$.

### Geometric Interpretation

The conjugate function has a beautiful geometric interpretation:
- $$f^*(y)$$ represents the **maximum gap** between the linear function $$y^T x$$ and the original function $$f(x)$$
- Geometrically, it measures how much the hyperplane with slope $$y$$ can be "lifted above" the graph of $$f$$
- The conjugate transforms the function from the "primal space" to the "dual space" of slopes

### Why is it Important?

The conjugate function is used to:
1. Transform optimization problems into their corresponding **dual problems**
2. Provide analytical tools for **duality theory** (covered in Chapter 11)
3. Enable direct substitution in **Lagrange Duality** without explicit differentiation
4. Establish connections between primal and dual optimal solutions

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/conjugate_function.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1] Conjugate function [2]</figcaption>
</p>
</figure>

### giải thích trực giác nhé:

1. Ý tưởng về hàm tuyến tính và tính lồi

Một hàm tuyến tính (dạng 
𝑦
↦
⟨
𝑦
,
𝑥
⟩
−
𝑓
(
𝑥
)
y↦⟨y,x⟩−f(x)) luôn vừa lồi vừa lõm.

Nếu ta lấy supremum (giá trị lớn nhất) của nhiều hàm tuyến tính, kết quả sẽ là một bao trên của các hàm này.

2. Sup của hàm tuyến tính tạo ra mặt cong lồi

Hãy tưởng tượng trong 2D:

Mỗi hàm tuyến tính là một đường thẳng.

Nếu ta lấy supremum của tất cả các đường thẳng này, ta sẽ “nâng” một lớp màng cao su bao phủ phía trên các đường.

Kết quả bề mặt này không thể bị lõm xuống, mà luôn lồi ra ngoài.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter03/conjugate_function_2" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Fig1] Conjugate function [2]</figcaption>
</p>
</figure>

## Fundamental Properties

The conjugate function has several remarkable properties that make it a powerful analytical tool:

### 1. Convexity Property
- **$$f^*$$ is always convex**, regardless of whether $$f$$ is convex or not
- This is because $$f^*(y)$$ is the pointwise supremum of affine functions $$y^T x - f(x)$$
- The supremum of any collection of convex (affine) functions is convex

### 2. Fenchel's Inequality
For any $$x$$ and $$y$$:
$$f(x) + f^*(y) \geq x^T y$$

This fundamental inequality establishes a lower bound relationship between a function and its conjugate.

### 3. Conjugate of Conjugate (Biconjugate)
- In general: $$f^{**} \leq f$$ (the biconjugate is a lower bound)
- **If $$f$$ is closed and convex**: $$f^{**} = f$$ (perfect recovery)
- This property is crucial for duality theory

### 4. Subdifferential Relationship
If $$f$$ is closed and convex, then for any $$x, y$$:
$$y \in \partial f(x) \iff x \in \partial f^*(y) \iff f(x) + f^*(y) = x^T y$$

This establishes a beautiful symmetry between primal and dual spaces.

## Detailed Examples

### Example 1: Negative Logarithm
Consider $$f(x) = -\log x$$ for $$x > 0$$.

**Step-by-step calculation:**
$$f^*(y) = \sup_{x>0} \{xy + \log x\}$$

To find the supremum, we differentiate with respect to $$x$$:
$$\frac{d}{dx}(xy + \log x) = y + \frac{1}{x} = 0$$

This gives us $$x^* = -\frac{1}{y}$$ (valid only when $$y < 0$$).

**Result:**
$$f^*(y) = \begin{cases}
-1 - \log(-y), & \text{if } y < 0 \\
+\infty, & \text{if } y \geq 0
\end{cases}$$

### Example 2: Quadratic Function
Consider $$f(x) = \frac{1}{2}x^T Q x$$ where $$Q \succ 0$$ (positive definite).

**Step-by-step calculation:**
$$f^*(y) = \sup_{x} \{y^T x - \frac{1}{2}x^T Q x\}$$

Taking the gradient and setting it to zero:
$$\nabla_x (y^T x - \frac{1}{2}x^T Q x) = y - Qx = 0$$

This gives us $$x^* = Q^{-1}y$$.

Substituting back:
$$f^*(y) = y^T Q^{-1} y - \frac{1}{2}(Q^{-1}y)^T Q (Q^{-1}y) = \frac{1}{2}y^T Q^{-1} y$$

### Example 3: Absolute Value (1D case)
Consider $$f(x) = \lvert x \rvert$$ for $$x \in \mathbb{R}$$.

$$f^*(y) = \sup_{x} \{yx - \lvert x \rvert\}$$

**Analysis by cases:**
- If $$\lvert y \rvert \leq 1$$: The supremum is finite and equals 0
- If $$\lvert y \rvert > 1$$: The supremum is $$+\infty$$

**Result:**
$$f^*(y) = \begin{cases}
0, & \text{if } \lvert y \rvert \leq 1 \\
+\infty, & \text{if } \lvert y \rvert > 1
\end{cases}$$

This is the **indicator function** of the interval $$[-1, 1]$$.

### Example 4: Exponential Function
Consider $$f(x) = e^x$$ for $$x \in \mathbb{R}$$.

$$f^*(y) = \sup_{x} \{yx - e^x\}$$

Setting the derivative to zero: $$y - e^x = 0$$, so $$x^* = \log y$$ (valid for $$y > 0$$).

**Result:**
$$f^*(y) = \begin{cases}
y \log y - y, & \text{if } y > 0 \\
0, & \text{if } y = 0 \\
+\infty, & \text{if } y < 0
\end{cases}$$

## Applications in Optimization

The conjugate function plays a crucial role in:

1. **Lagrange Duality**: Converting primal problems to dual problems
2. **Fenchel Duality**: A general framework for convex optimization duality
3. **Proximal Operators**: Used in modern optimization algorithms
4. **Variational Analysis**: Studying optimization problems through conjugate pairs

These applications will be explored in detail in Chapters 11 and 13.

## Interactive Visualization

To better understand how conjugate functions work, explore our interactive visualization:

<div style="text-align: center; margin: 20px 0;">
    <a href="../conjugate_function_interactive.html" target="_blank" 
       style="display: inline-block; padding: 12px 24px; background-color: #3498db; color: white; text-decoration: none; border-radius: 6px; font-weight: bold; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
        🎯 Launch Interactive Conjugate Function Explorer
    </a>
</div>

The interactive tool allows you to:
- **Visualize different function types** and their conjugates side-by-side
- **Adjust parameters** to see how they affect the conjugate
- **Explore tangent lines** to understand the geometric interpretation
- **Compare multiple examples** with detailed mathematical explanations

## Summary and Key Takeaways

The conjugate function is a powerful mathematical tool that:

1. **Transforms functions** from primal to dual space through the operation $$f^*(y) = \sup_x \{y^T x - f(x)\}$$
2. **Always produces convex functions**, regardless of the original function's convexity
3. **Establishes fundamental inequalities** like Fenchel's inequality: $$f(x) + f^*(y) \geq x^T y$$
4. **Enables duality theory** by connecting primal and dual optimization problems
5. **Provides analytical tools** for solving complex optimization problems

Understanding conjugate functions is essential for:
- **Convex optimization theory** and algorithm development
- **Lagrange duality** and dual problem formulation  
- **Modern optimization methods** like proximal algorithms
- **Variational analysis** and mathematical economics

The geometric intuition of "maximum gap between linear and nonlinear functions" provides a visual understanding that complements the analytical definition, making this abstract concept more accessible to learners.

