---
layout: post
title: '02-08 Multiple-Choice Quiz - Convex Sets'
chapter: '02'
order: 18
owner: GitHub Copilot
lang: en
categories:
- chapter02
lesson_type: quiz
redirect_from:
  - /contents/en/chapter02/02_07_Quiz_Convex_Sets/
---

This multiple-choice quiz tests your understanding of affine sets, convex sets and important examples in convex geometry.

---

## 📚 Theory Review

Before starting the exercises, review the key concepts of this chapter:

### 📏 **Affine Sets**

**Definition:**
A set $$C$$ is affine if for all $$x_1, x_2 \in C$$ and $$\theta \in \mathbb{R}$$:
$$\theta x_1 + (1-\theta)x_2 \in C$$

**Affine combination:**
$$\sum_{i=1}^k \theta_i x_i$$ with $$\sum_{i=1}^k \theta_i = 1$$ (no requirement $$\theta_i \ge 0$$)

**Bao affine:**
$$\text{aff}(C) = \{\sum_{i=1}^k \theta_i x_i \mid x_i \in C, \sum_{i=1}^k \theta_i = 1\}$$

**Property:** An affine set = a translate of a linear subspace

### 🔵 **Convex Sets**

**Definition:**
A set $$C$$ is convex if for all $$x_1, x_2 \in C$$ and $$0 \le \theta \le 1$$:
$$\theta x_1 + (1-\theta)x_2 \in C$$

**Convex combination:**
$$\sum_{i=1}^k \theta_i x_i$$ with $$\sum_{i=1}^k \theta_i = 1, \theta_i \ge 0$$

**Convex hull:**
$$\text{conv}(C) = \{\sum_{i=1}^k \theta_i x_i \mid x_i \in C, \theta_i \ge 0, \sum_{i=1}^k \theta_i = 1\}$$

**Intuition:** No "dents" - the segment joining any 2 points lies in the set

### 🔺 **Cones and Convex Cones**

**Cone:**
A set $$C$$ is a cone if for all $$x \in C$$ and $$\theta \ge 0$$:
$$\theta x \in C$$

**Convex cone:**
Both a cone and convex. For $$x_1, x_2 \in C$$ and $$\theta_1, \theta_2 \ge 0$$:
$$\theta_1 x_1 + \theta_2 x_2 \in C$$

**Conic combination:**
$$\sum_{i=1}^k \theta_i x_i$$ with $$\theta_i \ge 0$$ (no requirement that the sum = 1)

### 📐 **Important Examples**

**Basic sets:**
- The empty set $$\emptyset$$: convex
- A single point $$\{x_0\}$$: convex
- Lines, line segments, rays: convex

**Hyperplane:**
$$\{x \mid a^T x = b\}$$ with $$a \neq 0$$ - affine and convex

**Halfspace:**
$$\{x \mid a^T x \le b\}$$ with $$a \neq 0$$ - convex

**Affine space:**
$$\{x \mid Ax = b\}$$ - affine and convex

**Euclidean ball:**
$$\{x \mid \lVert x - x_c \rVert_2 \le r\}$$ - convex

**Norm ball:**
$$\{x \mid \lVert x \rVert \le r\}$$ for any norm - convex

**Ellipsoid:**
$$\{x \mid (x-x_c)^T P^{-1} (x-x_c) \le 1\}$$ with $$P \succ 0$$ - convex

### ✂️ **Separating and Supporting Hyperplanes**

**Separating hyperplane theorem:**
If $$C$$ and $$D$$ are two disjoint convex sets, there exists a hyperplane $$\{x \mid a^T x = b\}$$ with $$a \neq 0$$ such that:
- $$a^T x \le b$$ for all $$x \in C$$
- $$a^T x \ge b$$ for all $$x \in D$$

**Supporting hyperplane theorem:**
For a convex set $$C$$ and a boundary point $$x_0 \in \text{bd}(C)$$, there exists a supporting hyperplane:
$$\{x \mid a^T x = a^T x_0\}$$ such that $$a^T x \le a^T x_0$$ for all $$x \in C$$

### 🔗 **Relations Between the Sets**

```
Affine sets ⊂ Convex sets
     ↓
Convex cones = Cones ∩ Convex sets (so Convex cones ⊂ Cones and Convex cones ⊂ Convex sets)
```

**Remember:**
- **Affine:** The line through 2 points ($$\theta \in \mathbb{R}$$)
- **Convex:** The segment joining 2 points ($$0 \le \theta \le 1$$)
- **Cone:** The ray from the origin through a point ($$\theta \ge 0$$)

### 🎯 **Operations that Preserve Convexity**

- **Intersection:** The intersection of convex sets is convex
- **Affine combination:** $$\alpha C + \beta D$$ is convex if $$C, D$$ are convex
- **Affine image:** $$f(C) = \{Ax + b \mid x \in C\}$$ is convex if $$C$$ is convex
- **Affine preimage:** $$f^{-1}(D) = \{x \mid Ax + b \in D\}$$ is convex if $$D$$ is convex

---

💡 **Tip:** Convex sets are the foundation of convex optimization. Most constraint sets in practice can be written as intersections of basic convex sets!

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>Multiple-Choice Quiz: Convex Sets</h2>
        <p>Choose the best answer for each question. The quiz focuses on the basic concepts of affine sets, convex sets and hyperplanes.</p>
        <div id="progress-bar">
            <div id="progress-fill"></div>
        </div>
        <p id="progress-text">Question 1/25</p>
    </div>

    <div id="quiz-questions">
        <!-- Question 1 -->
        <div class="question" id="q1">
            <h3>Question 1: A set $$C$$ is affine if:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) For all $$x_1, x_2 \in C$$ and $$0 \leq \theta \leq 1$$, we have $$\theta x_1 + (1-\theta)x_2 \in C$$</label>
                <label><input type="radio" name="q1" value="b"> B) For all $$x_1, x_2 \in C$$ and $$\theta \in \mathbb{R}$$, we have $$\theta x_1 + (1-\theta)x_2 \in C$$</label>
                <label><input type="radio" name="q1" value="c"> C) The set $$C$$ is closed</label>
                <label><input type="radio" name="q1" value="d"> D) The set $$C$$ has a boundary</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) For all $$x_1, x_2 \in C$$ and $$\theta \in \mathbb{R}$$, we have $$\theta x_1 + (1-\theta)x_2 \in C$$</strong><br>
                An affine set contains the entire line through any two of its points, with no restriction of $$\theta$$ to $$[0,1]$$.
            </div>
        </div>

        <!-- Question 2 -->
        <div class="question" id="q2" style="display: none;">
            <h3>Question 2: An affine combination of the points $$x_1, x_2, ..., x_k$$ has the form:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) $$\sum_{i=1}^k \theta_i x_i$$ with $$\theta_i \geq 0$$</label>
                <label><input type="radio" name="q2" value="b"> B) $$\sum_{i=1}^k \theta_i x_i$$ with $$\sum_{i=1}^k \theta_i = 1$$</label>
                <label><input type="radio" name="q2" value="c"> C) $$\sum_{i=1}^k \theta_i x_i$$ with $$\theta_i \geq 0$$ and $$\sum_{i=1}^k \theta_i = 1$$</label>
                <label><input type="radio" name="q2" value="d"> D) $$\sum_{i=1}^k x_i$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$\sum_{i=1}^k \theta_i x_i$$ with $$\sum_{i=1}^k \theta_i = 1$$</strong><br>
                An affine combination only requires the coefficients to sum to 1; it does not require them to be nonnegative (unlike a convex combination).
            </div>
        </div>

        <!-- Question 3 -->
        <div class="question" id="q3" style="display: none;">
            <h3>Question 3: If $$C$$ is an affine set and $$x_0 \in C$$, then $$V = C - x_0$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) An affine set</label>
                <label><input type="radio" name="q3" value="b"> B) A linear subspace</label>
                <label><input type="radio" name="q3" value="c"> C) A convex set</label>
                <label><input type="radio" name="q3" value="d"> D) A hyperplane</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) A linear subspace</strong><br>
                An affine set $$C$$ is the translate of a linear subspace $$V$$ by $$x_0$$. Hence $$V = C - x_0$$ is a subspace.
            </div>
        </div>

        <!-- Question 4 -->
        <div class="question" id="q4" style="display: none;">
            <h3>Question 4: A set $$C$$ is convex if:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) For all $$x_1, x_2 \in C$$ and $$\theta \in \mathbb{R}$$, we have $$\theta x_1 + (1-\theta)x_2 \in C$$</label>
                <label><input type="radio" name="q4" value="b"> B) For all $$x_1, x_2 \in C$$ and $$0 \leq \theta \leq 1$$, we have $$\theta x_1 + (1-\theta)x_2 \in C$$</label>
                <label><input type="radio" name="q4" value="c"> C) The set $$C$$ has no holes</label>
                <label><input type="radio" name="q4" value="d"> D) The set $$C$$ is a disk</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) For all $$x_1, x_2 \in C$$ and $$0 \leq \theta \leq 1$$, we have $$\theta x_1 + (1-\theta)x_2 \in C$$</strong><br>
                A convex set contains the segment joining any two of its points, with $$\theta$$ restricted to $$[0,1]$$.
            </div>
        </div>

        <!-- Question 5 -->
        <div class="question" id="q5" style="display: none;">
            <h3>Question 5: How does a convex combination differ from an affine combination?</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) The coefficients must sum to 1</label>
                <label><input type="radio" name="q5" value="b"> B) The coefficients must be nonnegative</label>
                <label><input type="radio" name="q5" value="c"> C) The number of points involved</label>
                <label><input type="radio" name="q5" value="d"> D) There is no difference</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) The coefficients must be nonnegative</strong><br>
                A convex combination requires $$\theta_i \geq 0$$ and $$\sum \theta_i = 1$$, whereas an affine combination only needs $$\sum \theta_i = 1$$.
            </div>
        </div>

        <!-- Question 6 -->
        <div class="question" id="q6" style="display: none;">
            <h3>Question 6: The hyperplane $$\{x : a^T x = b\}$$ with $$a \neq 0$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) Only a convex set</label>
                <label><input type="radio" name="q6" value="b"> B) Only an affine set</label>
                <label><input type="radio" name="q6" value="c"> C) Both a convex set and an affine set</label>
                <label><input type="radio" name="q6" value="d"> D) Neither a convex set nor an affine set</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: C) Both a convex set and an affine set</strong><br>
                A hyperplane satisfies both the convex-set and the affine-set definitions because it contains the entire line through any two of its points.
            </div>
        </div>

        <!-- Question 7 -->
        <div class="question" id="q7" style="display: none;">
            <h3>Question 7: The halfspace $$\{x : a^T x \leq b\}$$ with $$a \neq 0$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) Convex but not affine</label>
                <label><input type="radio" name="q7" value="b"> B) Affine but not convex</label>
                <label><input type="radio" name="q7" value="c"> C) Both a convex set and an affine set</label>
                <label><input type="radio" name="q7" value="d"> D) Neither a convex set nor an affine set</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Convex but not affine</strong><br>
                A halfspace is convex because it contains the segment joining any two of its points, but it is not affine because it does not contain entire lines.
            </div>
        </div>

        <!-- Question 8 -->
        <div class="question" id="q8" style="display: none;">
            <h3>Question 8: The Euclidean ball $$B(x_c, r) = \{x : \|x - x_c\|_2 \leq r\}$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) A convex set</label>
                <label><input type="radio" name="q8" value="b"> B) An affine set</label>
                <label><input type="radio" name="q8" value="c"> C) A hyperplane</label>
                <label><input type="radio" name="q8" value="d"> D) A halfspace</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) A convex set</strong><br>
                The Euclidean ball is convex because the segment joining any two points of the ball also lies in the ball.
            </div>
        </div>

        <!-- Question 9 -->
        <div class="question" id="q9" style="display: none;">
            <h3>Question 9: The ellipsoid $$\{x : (x-x_c)^T P^{-1} (x-x_c) \leq 1\}$$ with $$P \succ 0$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) A special case of the ball</label>
                <label><input type="radio" name="q9" value="b"> B) A convex set generalizing the ball</label>
                <label><input type="radio" name="q9" value="c"> C) Not a convex set</label>
                <label><input type="radio" name="q9" value="d"> D) Only defined in 2D</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) A convex set generalizing the ball</strong><br>
                The ellipsoid generalizes the Euclidean ball. When $$P = r^2 I$$, the ellipsoid becomes a ball.
            </div>
        </div>

        <!-- Question 10 -->
        <div class="question" id="q10" style="display: none;">
            <h3>Question 10: A polyhedron is defined as:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) An intersection of balls</label>
                <label><input type="radio" name="q10" value="b"> B) The solution set of finitely many linear inequalities and equalities</label>
                <label><input type="radio" name="q10" value="c"> C) A union of halfspaces</label>
                <label><input type="radio" name="q10" value="d"> D) A product of convex sets</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) The solution set of finitely many linear inequalities and equalities</strong><br>
                A polyhedron has the form $$\{x : a_i^T x \leq b_i, c_j^T x = d_j\}$$, the intersection of halfspaces and hyperplanes.
            </div>
        </div>

        <!-- Question 11 -->
        <div class="question" id="q11" style="display: none;">
            <h3>Question 11: A simplex in $$n$$-dimensional space is formed from:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) $$n$$ affinely independent points</label>
                <label><input type="radio" name="q11" value="b"> B) $$n+1$$ affinely independent points</label>
                <label><input type="radio" name="q11" value="c"> C) $$2n$$ points</label>
                <label><input type="radio" name="q11" value="d"> D) Infinitely many points</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$n+1$$ affinely independent points</strong><br>
                An $$n$$-dimensional simplex needs $$n+1$$ affinely independent points: a point (0D), a segment (1D), a triangle (2D), a tetrahedron (3D).
            </div>
        </div>

        <!-- Question 12 -->
        <div class="question" id="q12" style="display: none;">
            <h3>Question 12: The norm ball $$\{x : \|x - x_c\| \leq r\}$$ is convex:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) For every norm</label>
                <label><input type="radio" name="q12" value="b"> B) Only for the Euclidean norm</label>
                <label><input type="radio" name="q12" value="c"> C) Only for p-norms with $$p \geq 1$$</label>
                <label><input type="radio" name="q12" value="d"> D) Only when $$p = 2$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) For every norm</strong><br>
                The ball of every norm is convex: if $$\|x - x_c\| \leq r$$ and $$\|y - x_c\| \leq r$$, then by the triangle inequality and homogeneity, $$\|\theta x + (1-\theta)y - x_c\| \leq \theta r + (1-\theta) r = r$$. (For $$p < 1$$, $$\|\cdot\|_p$$ is not a norm and its "ball" is not convex.)
            </div>
        </div>

        <!-- Question 13 -->
        <div class="question" id="q13" style="display: none;">
            <h3>Question 13: The separating hyperplane theorem states that:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) Any two convex sets can be separated by a hyperplane</label>
                <label><input type="radio" name="q13" value="b"> B) Two disjoint convex sets can be separated by a hyperplane</label>
                <label><input type="radio" name="q13" value="c"> C) Every convex set has a supporting hyperplane</label>
                <label><input type="radio" name="q13" value="d"> D) A hyperplane always divides space into two equal parts</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Two disjoint convex sets can be separated by a hyperplane</strong><br>
                The separating hyperplane theorem applies to two disjoint (non-intersecting) convex sets, not to every pair of convex sets.
            </div>
        </div>

        <!-- Question 14 -->
        <div class="question" id="q14" style="display: none;">
            <h3>Question 14: A supporting hyperplane at a point $$x_0$$ on the boundary of a convex set $$C$$ satisfies:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) $$a^T x \geq a^T x_0$$ for all $$x \in C$$</label>
                <label><input type="radio" name="q14" value="b"> B) $$a^T x \leq a^T x_0$$ for all $$x \in C$$</label>
                <label><input type="radio" name="q14" value="c"> C) $$a^T x = a^T x_0$$ for all $$x \in C$$</label>
                <label><input type="radio" name="q14" value="d"> D) $$a^T x > a^T x_0$$ for all $$x \in C$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$a^T x \leq a^T x_0$$ for all $$x \in C$$</strong><br>
                The supporting hyperplane $$\{x : a^T x = a^T x_0\}$$ "supports" $$C$$ at $$x_0$$, with $$C$$ lying in the halfspace $$a^T x \leq a^T x_0$$.
            </div>
        </div>

        <!-- Question 15 -->
        <div class="question" id="q15" style="display: none;">
            <h3>Question 15: Strict separation of two sets $$C$$ and $$D$$ means:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) $$a^T x \leq b$$ for $$x \in C$$ and $$a^T x \geq b$$ for $$x \in D$$</label>
                <label><input type="radio" name="q15" value="b"> B) $$a^T x < b$$ for $$x \in C$$ and $$a^T x > b$$ for $$x \in D$$</label>
                <label><input type="radio" name="q15" value="c"> C) $$a^T x = b$$ for $$x \in C \cup D$$</label>
                <label><input type="radio" name="q15" value="d"> D) The distance between $$C$$ and $$D$$ is greater than 0</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) $$a^T x < b$$ for $$x \in C$$ and $$a^T x > b$$ for $$x \in D$$</strong><br>
                Strict separation requires strict inequalities (< and >), not just ≤ and ≥.
            </div>
        </div>

        <!-- Question 16 -->
        <div class="question" id="q16" style="display: none;">
            <h3>Question 16: The convex hull of a set $$S$$ is:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) The smallest convex set containing $$S$$</label>
                <label><input type="radio" name="q16" value="b"> B) The largest convex set contained in $$S$$</label>
                <label><input type="radio" name="q16" value="c"> C) The intersection of all convex sets containing $$S$$</label>
                <label><input type="radio" name="q16" value="d"> D) Both A and C are correct</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: D) Both A and C are correct</strong><br>
                The convex hull is both the smallest convex set containing $$S$$ and the intersection of all convex sets containing $$S$$. The two definitions are equivalent.
            </div>
        </div>

        <!-- Question 17 -->
        <div class="question" id="q17" style="display: none;">
            <h3>Question 17: A polytope is:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Any polyhedron</label>
                <label><input type="radio" name="q17" value="b"> B) A bounded polyhedron</label>
                <label><input type="radio" name="q17" value="c"> C) An unbounded polyhedron</label>
                <label><input type="radio" name="q17" value="d"> D) A polyhedron with infinitely many vertices</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) A bounded polyhedron</strong><br>
                Polytope is the special term for a bounded polyhedron.
            </div>
        </div>

        <!-- Question 18 -->
        <div class="question" id="q18" style="display: none;">
            <h3>Question 18: The probability simplex in $$\mathbb{R}^n$$ is defined as:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) $$\{x : x \geq 0, \sum x_i = 1\}$$</label>
                <label><input type="radio" name="q18" value="b"> B) $$\{x : x \geq 0, \sum x_i \leq 1\}$$</label>
                <label><input type="radio" name="q18" value="c"> C) $$\{x : \|x\| = 1\}$$</label>
                <label><input type="radio" name="q18" value="d"> D) $$\{x : \|x\| \leq 1\}$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$\{x : x \geq 0, \sum x_i = 1\}$$</strong><br>
                The probability simplex is the set of probability vectors: nonnegative components summing to 1.
            </div>
        </div>

        <!-- Question 19 -->
        <div class="question" id="q19" style="display: none;">
            <h3>Question 19: An affine set can be thought of as a union of:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) Many lines</label>
                <label><input type="radio" name="q19" value="b"> B) Many line segments</label>
                <label><input type="radio" name="q19" value="c"> C) Many rays</label>
                <label><input type="radio" name="q19" value="d"> D) Many isolated points</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Many lines</strong><br>
                An affine set is built from many lines, a convex set from many segments, and a cone from many rays.
            </div>
        </div>

        <!-- Question 20: Real-world applications -->
        <div class="question" id="q20" style="display: none;">
            <h3>Question 20: In optimization, separating hyperplanes are mainly used in:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Computing gradients</label>
                <label><input type="radio" name="q20" value="b"> B) Classification and machine learning</label>
                <label><input type="radio" name="q20" value="c"> C) Computing integrals</label>
                <label><input type="radio" name="q20" value="d"> D) Solving differential equations</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: B) Classification and machine learning</strong><br>
                Separating hyperplanes underlie many classification algorithms such as SVM, which are widely used in machine learning.
            </div>
        </div>

        <!-- Question 21 -->
        <div class="question" id="q21" style="display: none;">
            <h3>Question 21: Is the set $$S = \{(x,y) : x^2 + y^2 \leq 1\}$$ (the unit disk) convex?</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) Yes, because it satisfies the definition of a convex set</label>
                <label><input type="radio" name="q21" value="b"> B) No, because it has a curved boundary</label>
                <label><input type="radio" name="q21" value="c"> C) No, because it is not a polygon</label>
                <label><input type="radio" name="q21" value="d"> D) Convex only when the radius = 1</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Yes, because it satisfies the definition of a convex set</strong><br>
                A disk (and a ball) is always convex. The segment joining any two points of the disk lies entirely in the disk.
            </div>
        </div>

        <!-- Question 22 -->
        <div class="question" id="q22" style="display: none;">
            <h3>Question 22: Given three points $$A(0,0), B(2,0), C(1,2)$$, which of the following points is a convex combination of them?</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) $$(1,1)$$</label>
                <label><input type="radio" name="q22" value="b"> B) $$(3,1)$$</label>
                <label><input type="radio" name="q22" value="c"> C) $$(-1,0)$$</label>
                <label><input type="radio" name="q22" value="d"> D) $$(2,3)$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$(1,1)$$</strong><br>
                The convex combinations of three points form a triangle. The point $$(1,1)$$ lies in the triangle with vertices $$A, B, C$$.<br>
                We can write $$(1,1) = 0.25A + 0.25B + 0.5C$$ with nonnegative coefficients summing to 1.
            </div>
        </div>

        <!-- Question 23 -->
        <div class="question" id="q23" style="display: none;">
            <h3>Question 23: Which points does the hyperplane $$\{x : 2x_1 + 3x_2 = 6\}$$ in $$\mathbb{R}^2$$ pass through?</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) $$(0,2)$$ and $$(3,0)$$</label>
                <label><input type="radio" name="q23" value="b"> B) $$(1,1)$$ and $$(2,2)$$</label>
                <label><input type="radio" name="q23" value="c"> C) $$(0,0)$$ and $$(1,1)$$</label>
                <label><input type="radio" name="q23" value="d"> D) $$(2,3)$$ and $$(6,0)$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$(0,2)$$ and $$(3,0)$$</strong><br>
                Check: $$2(0) + 3(2) = 6$$ ✓ and $$2(3) + 3(0) = 6$$ ✓<br>
                This is the line crossing the $$y$$-axis at $$(0,2)$$ and the $$x$$-axis at $$(3,0)$$.
            </div>
        </div>

        <!-- Question 24 -->
        <div class="question" id="q24" style="display: none;">
            <h3>Question 24: Is the set $$K = \{(x,y) : x \geq 0, y \geq 0, y \leq x\}$$ a convex cone?</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) Yes, because it is closed under multiplication by positive scalars and under addition</label>
                <label><input type="radio" name="q24" value="b"> B) No, because it does not contain the origin</label>
                <label><input type="radio" name="q24" value="c"> C) No, because it is not symmetric</label>
                <label><input type="radio" name="q24" value="d"> D) It is only a cone, not convex</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) Yes, because it is closed under multiplication by positive scalars and under addition</strong><br>
                This set is the part of the first quadrant below the line $$y = x$$; it contains the origin and satisfies the definition of a convex cone.
            </div>
        </div>

        <!-- Question 25 -->
        <div class="question" id="q25" style="display: none;">
            <h3>Question 25: Given two convex sets $$C_1$$ and $$C_2$$, which of the following sets is always convex?</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) $$C_1 \cap C_2$$ (giao)</label>
                <label><input type="radio" name="q25" value="b"> B) $$C_1 \cup C_2$$ (union)</label>
                <label><input type="radio" name="q25" value="c"> C) $$C_1 \setminus C_2$$ (difference)</label>
                <label><input type="radio" name="q25" value="d"> D) $$C_1 \triangle C_2$$ (symmetric difference)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Correct answer: A) $$C_1 \cap C_2$$ (giao)</strong><br>
                The intersection of two convex sets is always convex. The union of two convex sets is not necessarily convex (e.g. two disjoint disks).
            </div>
        </div>
    </div>

    <div id="quiz-navigation">
        <button id="prev-btn" onclick="previousQuestion()" disabled>Previous</button>
        <button id="next-btn" onclick="nextQuestion()">Next</button>
        <button id="submit-btn" onclick="submitQuiz()" style="display: none;">Submit</button>
    </div>

    <div id="quiz-results" style="display: none;">
        <h3>Exercise Results</h3>
        <div id="score-display"></div>
        <div id="detailed-results"></div>
        <button onclick="restartQuiz()">Try again</button>
    </div>
</div>

<style>
#quiz-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

#quiz-header {
    text-align: center;
    margin-bottom: 30px;
}

#progress-bar {
    width: 100%;
    height: 10px;
    background-color: #e0e0e0;
    border-radius: 5px;
    margin: 20px 0;
    overflow: hidden;
}

#progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #9C27B0, #673AB7);
    width: 5%;
    transition: width 0.3s ease;
}

.question {
    background: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 25px;
    margin-bottom: 20px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.question h3 {
    color: #333;
    margin-bottom: 20px;
    font-size: 1.1em;
    line-height: 1.4;
}

.options {
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.options label {
    display: flex;
    align-items: flex-start;
    padding: 12px;
    background: white;
    border: 2px solid #e0e0e0;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s ease;
    font-size: 1em;
    line-height: 1.4;
}

.options label:hover {
    border-color: #9C27B0;
    background-color: #f3e5f5;
}

.options input[type="radio"] {
    margin-right: 12px;
    margin-top: 2px;
    transform: scale(1.2);
    flex-shrink: 0;
}

.options label.selected {
    border-color: #9C27B0;
    background-color: #e8d5e8;
}

.explanation {
    margin-top: 20px;
    padding: 15px;
    background-color: #f3e5f5;
    border-left: 4px solid #9C27B0;
    border-radius: 4px;
    font-size: 0.95em;
    line-height: 1.5;
}

.explanation strong {
    color: #7B1FA2;
}

#quiz-navigation {
    text-align: center;
    margin: 30px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

#quiz-navigation button {
    background: #9C27B0;
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.2s ease;
}

#quiz-navigation button:hover:not(:disabled) {
    background: #7B1FA2;
}

#quiz-navigation button:disabled {
    background: #cccccc;
    cursor: not-allowed;
}

#quiz-results {
    text-align: center;
    padding: 30px;
    background: #f3e5f5;
    border-radius: 8px;
    border: 2px solid #9C27B0;
}

#score-display {
    font-size: 1.5em;
    font-weight: bold;
    margin: 20px 0;
    color: #7B1FA2;
}

#detailed-results {
    text-align: left;
    margin: 20px 0;
    max-height: 400px;
    overflow-y: auto;
}

.result-item {
    padding: 10px;
    margin: 5px 0;
    border-radius: 4px;
    border-left: 4px solid;
}

.result-item.correct {
    background-color: #e8f5e8;
    border-left-color: #4CAF50;
}

.result-item.incorrect {
    background-color: #ffebee;
    border-left-color: #f44336;
}

@media (max-width: 600px) {
    #quiz-container {
        padding: 10px;
    }
    
    .question {
        padding: 15px;
    }
    
    #quiz-navigation {
        flex-direction: column;
        gap: 10px;
    }
    
    #quiz-navigation button {
        width: 100%;
    }
}
</style>

<script>
let currentQuestion = 1;
const totalQuestions = 25;
let userAnswers = {};
let quizSubmitted = false;

// Correct answer for each question
const correctAnswers = {
    q1: 'b', q2: 'b', q3: 'b', q4: 'b', q5: 'b',
    q6: 'c', q7: 'a', q8: 'a', q9: 'b', q10: 'b',
    q11: 'b', q12: 'a', q13: 'b', q14: 'b', q15: 'b',
    q16: 'd', q17: 'b', q18: 'a', q19: 'a', q20: 'b',
    q21: 'a', q22: 'a', q23: 'a', q24: 'a', q25: 'a'
};

/**
 * Update the progress bar and show the current question
 */
function updateProgress() {
    const progressFill = document.getElementById('progress-fill');
    const progressText = document.getElementById('progress-text');
    
    const percentage = (currentQuestion / totalQuestions) * 100;
    progressFill.style.width = percentage + '%';
    progressText.textContent = `Question ${currentQuestion}/${totalQuestions}`;
}

/**
 * Show a question by its number
 */
function showQuestion(questionNum) {
    // Hide all questions
    for (let i = 1; i <= totalQuestions; i++) {
        document.getElementById(`q${i}`).style.display = 'none';
    }
    
    // Show the current question
    document.getElementById(`q${questionNum}`).style.display = 'block';
    
    // Update the state of the navigation buttons
    document.getElementById('prev-btn').disabled = (questionNum === 1);
    document.getElementById('next-btn').style.display = (questionNum === totalQuestions) ? 'none' : 'inline-block';
    document.getElementById('submit-btn').style.display = (questionNum === totalQuestions) ? 'inline-block' : 'none';
    
    updateProgress();
}

/**
 * Go to the next question
 */
function nextQuestion() {
    if (currentQuestion < totalQuestions) {
        currentQuestion++;
        showQuestion(currentQuestion);
    }
}

/**
 * Go back to the previous question
 */
function previousQuestion() {
    if (currentQuestion > 1) {
        currentQuestion--;
        showQuestion(currentQuestion);
    }
}

/**
 * Store the user's answer
 */
function saveAnswer(questionId, answer) {
    userAnswers[questionId] = answer;
    
    // Update the UI to show the selected answer
    const labels = document.querySelectorAll(`#${questionId} .options label`);
    labels.forEach(label => {
        label.classList.remove('selected');
        if (label.querySelector('input').value === answer) {
            label.classList.add('selected');
        }
    });
}

/**
 * Submit and show the results
 */
function submitQuiz() {
    if (quizSubmitted) return;
    
    quizSubmitted = true;
    let correctCount = 0;
    let detailedResults = '';
    
    // Compute the score and build the detailed report
    for (let i = 1; i <= totalQuestions; i++) {
        const questionId = `q${i}`;
        const userAnswer = userAnswers[questionId];
        const correctAnswer = correctAnswers[questionId];
        const isCorrect = userAnswer === correctAnswer;
        
        if (isCorrect) correctCount++;
        
        // Show explanations for all questions
        const explanation = document.querySelector(`#${questionId} .explanation`);
        if (explanation) {
            explanation.style.display = 'block';
        }
        
        // Build the detailed report
        detailedResults += `
            <div class="result-item ${isCorrect ? 'correct' : 'incorrect'}">
                <strong>Question ${i}:</strong> ${isCorrect ? 'Correct' : 'Incorrect'}
                ${!isCorrect ? `<br><small>Your answer: ${userAnswer || 'Not answered'} | Correct answer: ${correctAnswer}</small>` : ''}
            </div>
        `;
    }
    
    // Show the results
    const scorePercentage = Math.round((correctCount / totalQuestions) * 100);
    document.getElementById('score-display').innerHTML = `
        <div>Score: ${correctCount}/${totalQuestions} (${scorePercentage}%)</div>
        <div style="margin-top: 10px; font-size: 0.9em;">
            ${scorePercentage >= 80 ? '🎉 Excellent! You have mastered convex geometry!' :
              scorePercentage >= 60 ? '👍 Pretty good! Review a few geometric concepts.' :
              scorePercentage >= 40 ? '📚 You need more review of convex sets and hyperplanes.' : '💪 Reread the theory of convex geometry!'}
        </div>
    `;
    
    document.getElementById('detailed-results').innerHTML = detailedResults;
    document.getElementById('quiz-results').style.display = 'block';
    document.getElementById('quiz-navigation').style.display = 'none';
    
    // Scroll to the results
    document.getElementById('quiz-results').scrollIntoView({ behavior: 'smooth' });
}

/**
 * Restart the exercise
 */
function restartQuiz() {
    currentQuestion = 1;
    userAnswers = {};
    quizSubmitted = false;
    
    // Hide the results and show the navigation again
    document.getElementById('quiz-results').style.display = 'none';
    document.getElementById('quiz-navigation').style.display = 'flex';
    
    // Hide all explanations
    document.querySelectorAll('.explanation').forEach(exp => {
        exp.style.display = 'none';
    });
    
    // Clear all selections
    document.querySelectorAll('input[type="radio"]').forEach(input => {
        input.checked = false;
    });
    
    document.querySelectorAll('.options label').forEach(label => {
        label.classList.remove('selected');
    });
    
    // Show the first question
    showQuestion(1);
    
    // Scroll to the top
    document.getElementById('quiz-header').scrollIntoView({ behavior: 'smooth' });
}

// Initialize the exercise when the page loads
document.addEventListener('DOMContentLoaded', function() {
    showQuestion(1);
    
    // Add event listeners to all radio buttons
    document.querySelectorAll('input[type="radio"]').forEach(input => {
        input.addEventListener('change', function() {
            const questionId = this.name;
            const answer = this.value;
            saveAnswer(questionId, answer);
        });
    });
    
    // Render MathJax after the DOM has loaded
    if (window.MathJax && MathJax.startup && MathJax.startup.promise) {
        MathJax.startup.promise.then(() => MathJax.typesetPromise());
    }
});

// Handle keyboard shortcuts
document.addEventListener('keydown', function(event) {
    if (quizSubmitted) return;
    
    switch(event.key) {
        case 'ArrowLeft':
            if (currentQuestion > 1) previousQuestion();
            break;
        case 'ArrowRight':
            if (currentQuestion < totalQuestions) nextQuestion();
            break;
        case 'Enter':
            if (currentQuestion === totalQuestions) submitQuiz();
            break;
    }
});
</script>
