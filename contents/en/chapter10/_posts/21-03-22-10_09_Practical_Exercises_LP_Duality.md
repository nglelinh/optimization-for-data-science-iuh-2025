---
layout: post
title: '10-09 Practical Exercises - Duality in Linear Programming'
chapter: "10"
order: 10
owner: "GitHub Copilot"
lang: en
categories:
  - chapter10
lesson_type: required
redirect_from:
  - /contents/en/chapter10/10_07_Practical_Exercises_LP_Duality/
---

The following exercises are adapted from Boyd & Vandenberghe (2004), Bertsimas & Tsitsiklis (1997), and Dantzig (1963), and help students master the concepts of duality in LP.

---

## **Part I: Constructing Dual Problems**

### **Exercise 1: Basic LP Forms (Boyd & Vandenberghe, Ex. 5.1)**

For each of the following LPs, construct the dual problem and explain the meaning of the dual variables.

**a) Standard form:**

$$
\begin{align}
\min_{x} \quad & 3x_1 + 5x_2 + 2x_3 \\
\text{s.t.} \quad & x_1 + 2x_2 + x_3 = 4 \\
& 2x_1 + x_2 + 3x_3 = 5 \\
& x_1, x_2, x_3 \geq 0
\end{align}
$$

**b) Inequality form:**

$$
\begin{align}
\min_{x} \quad & 2x_1 + 4x_2 \\
\text{s.t.} \quad & x_1 + x_2 \geq 3 \\
& 2x_1 + x_2 \geq 5 \\
& x_1, x_2 \geq 0
\end{align}
$$

**c) Mixed form:**

$$
\begin{align}
\min_{x} \quad & x_1 + 2x_2 + 3x_3 \\
\text{s.t.} \quad & x_1 + x_2 = 2 \\
& x_2 + x_3 \leq 3 \\
& x_1 + x_3 \geq 1 \\
& x_1, x_2, x_3 \geq 0
\end{align}
$$

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**Part a) Standard form:**

**Rule:** For a min problem with equality constraints and variables $$\geq 0$$:
- Each equality constraint → a free (unrestricted-sign) dual variable  
- Each variable $$\geq 0$$ → a dual constraint $$\leq$$

**Dual problem:**

$$
\begin{align}
\max_{u} \quad & 4u_1 + 5u_2 \\
\text{s.t.} \quad & u_1 + 2u_2 \leq 3 \\
& 2u_1 + u_2 \leq 5 \\
& u_1 + 3u_2 \leq 2 \\
& u_1, u_2 \in \mathbb{R}
\end{align}
$$

**Interpretation:**
- $$u_1, u_2$$: shadow prices of constraints 1 and 2 (marginal value of increasing the RHS)
- Unrestricted in sign because the primal constraints are equalities
- Each primal variable produces one dual constraint

---

**Part b) Inequality form:**

**Rule:** Min with $$\geq$$ and $$x \geq 0$$:
- A $$\geq$$ constraint → a dual variable $$\geq 0$$
- A variable $$\geq 0$$ → a dual constraint $$\leq$$

**Dual problem:**

$$
\begin{align}
\max_{u} \quad & 3u_1 + 5u_2 \\
\text{s.t.} \quad & u_1 + 2u_2 \leq 2 \\
& u_1 + u_2 \leq 4 \\
& u_1, u_2 \geq 0
\end{align}
$$

---

**Part c) Mixed form:**

**Analysis:**
- Constraint 1 ($$=$$): dual variable $$u_1 \in \mathbb{R}$$
- Constraint 2 ($$\leq$$): dual variable $$u_2 \leq 0$$  
- Constraint 3 ($$\geq$$): dual variable $$u_3 \geq 0$$

**Dual problem:**

$$
\begin{align}
\max_{u} \quad & 2u_1 + 3u_2 + u_3 \\
\text{s.t.} \quad & u_1 + u_3 \leq 1 \\
& u_1 + u_2 \leq 2 \\
& u_2 + u_3 \leq 3 \\
& u_1 \in \mathbb{R}, \quad u_2 \leq 0, \quad u_3 \geq 0
\end{align}
$$

</details>

---

### **Exercise 2: Production Planning (Boyd & Vandenberghe, Ex. 5.2)**

A factory produces 2 products A and B:

| Product | Profit (thousand VND) | Labor (hours) | Machine (hours) |
|----------|------------------------|----------------|---------------|
| A        | 40                     | 2              | 1             |
| B        | 30                     | 1              | 2             |

Resources: 100 labor hours, 80 machine hours.

**Tasks:**  
a) Formulate the LP that maximizes profit    
b) Construct the dual problem    
c) Explain the economic meaning of the dual variables    
d) If one more labor hour is available, what is the maximum increase in profit?

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**a) Primal problem:**

Let $$x_1, x_2$$ be the quantities of products A and B.

$$
\begin{align}
\max_{x} \quad & 40x_1 + 30x_2 \\
\text{s.t.} \quad & 2x_1 + x_2 \leq 100 \quad \text{(Labor)} \\
& x_1 + 2x_2 \leq 80 \quad \text{(Machine)} \\
& x_1, x_2 \geq 0
\end{align}
$$

**b) Dual problem:**

Convert to a min problem: $$\min -40x_1 - 30x_2$$

$$
\begin{align}
\min_{u} \quad & 100u_1 + 80u_2 \\
\text{s.t.} \quad & 2u_1 + u_2 \geq 40 \\
& u_1 + 2u_2 \geq 30 \\
& u_1, u_2 \geq 0
\end{align}
$$

**c) Economic meaning:**

- $$u_1$$: **Shadow price of labor** - the marginal value of one more labor hour
- $$u_2$$: **Shadow price of machine time** - the marginal value of one more machine hour

Dual constraints:
- $$2u_1 + u_2 \geq 40$$: the value of the resources used to make 1 unit of product A must be $$\geq$$ its profit
- $$u_1 + 2u_2 \geq 30$$: similarly for product B

**d) Profit increase:**

To answer, solve the system of active dual constraints: $$2u_1 + u_2 = 40$$, $$u_1 + 2u_2 = 30$$ → $$u_1^* = 50/3 \approx 16.67$$, $$u_2^* = 20/3 \approx 6.67$$ thousand VND/hour (check: primal $$x^* = (40, 20)$$ gives $$40 \cdot 40 + 30 \cdot 20 = 2200$$ = dual $$100 \cdot \frac{50}{3} + 80 \cdot \frac{20}{3} = 2200$$ ✓).

→ One more labor hour increases profit by about **16.67 thousand VND** ($$50/3$$).

</details>

---

### **Exercise 3: Portfolio Optimization (Boyd & Vandenberghe, Ex. 5.3)**

An investor has 1000 million VND to invest in 3 assets with the following expected returns:

| Asset | Return (%) | Risk (standard deviation) |
|---------|---------------|-------------------------|
| Stocks| 15            | 20                      |
| Bonds| 8           | 5                       |
| Cash| 3             | 0                       |

Requirements: a return of at least 10% and a total risk of at most 12%.

**Tasks:**  
a) Formulate the LP that minimizes risk  
b) Construct the dual problem  
c) Explain the meaning of the dual variables

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**a) Primal problem:**

Let $$x_1, x_2, x_3$$ be the fractions invested in stocks, bonds, and cash.

$$
\begin{align}
\min_{x} \quad & 20x_1 + 5x_2 \\
\text{s.t.} \quad & x_1 + x_2 + x_3 = 1 \quad \text{(Total capital)} \\
& 15x_1 + 8x_2 + 3x_3 \geq 10 \quad \text{(Return)} \\
& x_1, x_2, x_3 \geq 0
\end{align}
$$

**b) Dual problem:**

$$
\begin{align}
\max_{u} \quad & u_1 + 10u_2 \\
\text{s.t.} \quad & u_1 + 15u_2 \leq 20 \\
& u_1 + 8u_2 \leq 5 \\
& u_1 + 3u_2 \leq 0 \\
& u_1 \in \mathbb{R}, \quad u_2 \geq 0
\end{align}
$$

**c) Meaning:**

- $$u_1$$: the marginal value of capital - how much the risk decreases if there is 1% more capital
- $$u_2$$: the value of relaxing the return constraint - the trade-off between return and risk

**Solution:** only stocks and bonds are needed: $$15x_1 + 8(1-x_1) = 10 \Rightarrow x_1 = 2/7$$, so $$x^* = (2/7, 5/7, 0)$$ with risk $$20(2/7) + 5(5/7) = 65/7 \approx 9.29\% \leq 12\%$$ ✓ (the maximum-risk constraint of 12% is not active). Dual solution: $$u_1^* = -85/7$$, $$u_2^* = 15/7 \approx 2.14$$ (dual value $$-85/7 + 150/7 = 65/7$$ ✓), meaning that raising the required return by 1% increases the risk by about 2.14%.

</details>

---

## **Part II: Weak and Strong Duality**

### **Exercise 4: Weak Duality (Boyd & Vandenberghe, Ex. 5.5)**

Consider the problem:

$$
\begin{align}
\text{(P)} \quad \min_{x} \quad & 2x_1 + 3x_2 \\
\text{s.t.} \quad & x_1 + x_2 \geq 4 \\
& 2x_1 + x_2 \geq 6 \\
& x_1, x_2 \geq 0
\end{align}
$$

**a)** Construct the dual problem (D)    
**b)** Let $$x = (3, 1)$$. Check feasibility and find a feasible solution $$u$$ of (D)    
**c)** Check $$c^Tx \geq b^Tu$$ (weak duality)    
**d)** Prove that $$x^* = (4, 0)$$ is an optimal solution

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**a) The dual problem:**

$$
\begin{align}
\text{(D)} \quad \max_{u} \quad & 4u_1 + 6u_2 \\
\text{s.t.} \quad & u_1 + 2u_2 \leq 2 \\
& u_1 + u_2 \leq 3 \\
& u_1, u_2 \geq 0
\end{align}
$$

**b) Check $$x = (3, 1)$$:**

Primal feasibility:
- $$3 + 1 = 4 \geq 4$$ ✓
- $$2(3) + 1 = 7 \geq 6$$ ✓  
- $$x \geq 0$$ ✓

Primal value: $$f(x) = 2(3) + 3(1) = 9$$

Try $$u = (0, 1)$$:
- $$0 + 2(1) = 2 \leq 2$$ ✓
- $$0 + 1 = 1 \leq 3$$ ✓
- Dual value: $$g(u) = 4(0) + 6(1) = 6$$

**c) Weak duality:**

$$
c^Tx = 9 \geq 6 = b^Tu
$$

✓ Satisfied!

**d) Prove that $$x^* = (4, 0)$$ is optimal:**

Check feasibility:
- $$4 + 0 = 4 \geq 4$$ ✓ (active)
- $$2(4) + 0 = 8 \geq 6$$ ✓ (inactive, slack = 2)

Value: $$f(x^*) = 2(4) + 3(0) = 8$$

Find $$u^*$$ satisfying complementary slackness: constraint 2 is inactive so $$u_2^* = 0$$; $$x_1^* > 0$$ so dual constraint 1 is active: $$u_1^* + 2u_2^* = 2 \Rightarrow u_1^* = 2$$.

Check dual feasibility: $$u_1^* + u_2^* = 2 \leq 3$$ ✓ (inactive, consistent with $$x_2^* = 0$$). Dual value: $$g(u^*) = 4(2) + 6(0) = 8 = f(x^*)$$ ✓

**Conclusion:** $$x^* = (4, 0)$$ is optimal (by weak duality, every feasible $$x$$ has $$f(x) \geq g(u^*) = 8$$). Note that $$(2,2)$$ is feasible but $$f = 10 > 8$$, so it is not optimal; $$x = (3,1)$$ gives $$f = 9$$.

</details>

---

### **Exercise 5: Strong Duality (Boyd & Vandenberghe, Ex. 5.6)**

Cho:

$$
\begin{align}
\text{(P)} \quad \min_{x} \quad & x_1 + 2x_2 + x_3 \\
\text{s.t.} \quad & x_1 + x_2 = 3 \\
& x_2 + x_3 = 2 \\
& x_1, x_2, x_3 \geq 0
\end{align}
$$

**a)** Find the optimal solution algebraically    
**b)** Construct and solve the dual problem    
**c)** Compute the duality gap    
**d)** Explain why strong duality holds

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**a) Solve the primal:**

From the constraints: $$x_1 = 3 - x_2$$, $$x_3 = 2 - x_2$$

Substitute into the objective:

$$
f = (3 - x_2) + 2x_2 + (2 - x_2) = 5
$$

The objective **does not depend on $$x_2$$**! Optimal value: $$f^* = 5$$

Condition: $$0 \leq x_2 \leq 2$$ (from $$x_3 \geq 0$$)

Example solution: $$x^* = (2, 1, 1)$$

**b) Dual:**

$$
\begin{align}
\max_{u} \quad & 3u_1 + 2u_2 \\
\text{s.t.} \quad & u_1 \leq 1 \\
& u_1 + u_2 \leq 2 \\
& u_2 \leq 1 \\
& u_1, u_2 \in \mathbb{R}
\end{align}
$$

Maximize: choose $$u_1 = 1$$, $$u_2 = 1$$

Check: $$1 \leq 1$$ ✓, $$1 + 1 = 2 \leq 2$$ ✓, $$1 \leq 1$$ ✓

Value: $$g^* = 3(1) + 2(1) = 5$$

**c) Duality gap:**

$$
\text{Gap} = f^* - g^* = 5 - 5 = 0
$$

Strong duality holds! ✓

**d) Explanation:**

In LP, strong duality holds when one of the two problems has a finite optimal solution (then the other one also has an optimal solution and the two values are equal):
- If the primal is unbounded then the dual is infeasible (and vice versa)
- Both problems can be infeasible at the same time

The Slater condition is automatically satisfied for a feasible LP.

</details>

---

## **Part III: Complementary Slackness**

### **Exercise 6: Applying CS (Bertsimas & Tsitsiklis, Ex. 4.3)**

Consider the problem and the following pairs of solutions:

$$
\begin{align}
\text{(P)} \quad \min_{x} \quad & 3x_1 + 2x_2 \\
\text{s.t.} \quad & x_1 + x_2 \geq 4 \\
& 2x_1 + x_2 \geq 6 \\
& x_1, x_2 \geq 0
\end{align}
$$

**Pairs of solutions:**  
1. $$x = (2, 2)$$, $$u = (1, 1)$$  
2. $$x = (3, 1)$$, $$u = (0, 3/2)$$  
3. $$x = (0, 6)$$, $$u = (0, 2)$$

**Tasks:** Check which pair is optimal using complementary slackness.

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**Dual:**

$$
\begin{align}
\max_{u} \quad & 4u_1 + 6u_2 \\
\text{s.t.} \quad & u_1 + 2u_2 \leq 3 \\
& u_1 + u_2 \leq 2 \\
& u_1, u_2 \geq 0
\end{align}
$$

**Complementary slackness conditions:**
1. $$u_1 \cdot [x_1 + x_2 - 4] = 0$$
2. $$u_2 \cdot [2x_1 + x_2 - 6] = 0$$
3. $$x_1 \cdot [u_1 + 2u_2 - 3] = 0$$
4. $$x_2 \cdot [u_1 + u_2 - 2] = 0$$

---

**Pair 1: $$x = (2,2)$$, $$u = (1,1)$$**

Primal feasible:
- $$2 + 2 = 4 \geq 4$$ ✓ (active)
- $$4 + 2 = 6 \geq 6$$ ✓ (active)

Dual feasible:
- $$1 + 2 = 3 \leq 3$$ ✓ (active)
- $$1 + 1 = 2 \leq 2$$ ✓ (active)

Complementary slackness:
1. $$1 \cdot 0 = 0$$ ✓
2. $$1 \cdot 0 = 0$$ ✓
3. $$2 \cdot 0 = 0$$ ✓
4. $$2 \cdot 0 = 0$$ ✓

**Conclusion:** Pair 1 is optimal! ✓✓✓

Value: $$f = 3(2) + 2(2) = 10 = 4(1) + 6(1) = g$$ ✓

---

**Pair 2: $$x = (3,1)$$, $$u = (0, 3/2)$$**

Primal: $$3+1=4$$ ✓, $$6+1=7 > 6$$ (slack = 1)

Dual: $$0+3=3$$ ✓, $$0+3/2=3/2$$ ✓

CS 2: $$u_2 \cdot [7-6] = (3/2)(1) = 3/2 \neq 0$$ ✗

**Conclusion:** Not optimal!

---

**Pair 3: $$x = (0,6)$$, $$u = (0,2)$$**

Dual: $$0 + 4 = 4 \not\leq 3$$ ✗

**Conclusion:** The dual is infeasible!

</details>

---

### **Exercise 7: Shadow Prices (Bertsimas & Tsitsiklis, Ex. 4.7)**

The production problem has the optimal solution $$x^* = (40, 20)$$ with:
- Labor: $$2(40) + 20 = 100$$ (active)
- Machine: $$40 + 2(20) = 80$$ (active)

**a)** Compute the shadow price of each resource    
**b)** If one more labor hour can be bought for 12 thousand, is it worth buying?    
**c)** Sensitivity analysis when labor increases to 105 hours

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**a) Compute the shadow prices:**

Objective: $$\max 40x_1 + 30x_2$$

From complementary slackness (both constraints active, both variables positive):

$$
\begin{cases}
2u_1 + u_2 = 40 \\
u_1 + 2u_2 = 30
\end{cases}
$$

Solve the system:
- From (1): $$u_2 = 40 - 2u_1$$
- Substitute into (2): $$u_1 + 2(40 - 2u_1) = 30$$
- $$u_1 + 80 - 4u_1 = 30$$
- $$-3u_1 = -50$$
- $$u_1 = 50/3 \approx 16.67$$
- $$u_2 = 40 - 2(50/3) = 40 - 100/3 = 20/3 \approx 6.67$$

**Shadow prices:**
- Labor: $$u_1^* = 16.67$$ thousand VND/hour
- Machine: $$u_2^* = 6.67$$ thousand VND/hour

**b) Purchase decision:**

Purchase price: 12 thousand VND/hour    
Marginal value: $$u_1^* = 16.67$$ thousand VND/hour

$$12 < 16.67$$ → **Worth buying** (a gain of 4.67 thousand/hour)

**c) Sensitivity:**

Increasing labor by 5 hours:

$$
\Delta f \approx u_1^* \times 5 = 16.67 \times 5 = 83.35 \text{ thousand VND}
$$

Current profit: $$40(40) + 30(20) = 2200$$ thousand

New profit: $$2200 + 83.35 = 2283.35$$ thousand VND

*(Note: the shadow price is only exact within the sensitivity range)*

</details>

---

## **Part IV: Max Flow and Min Cut**

### **Exercise 8: Max Flow Problem (Bertsimas & Tsitsiklis, Ex. 7.2)**

Consider a network with the following capacities:

```
    s --10--> a --8--> t
    |        / \       ^
    8      5    3     10
    |    /        \    |
    v  /            \  |
    b ---------------> c
          10
```

**a)** Write the max flow problem as an LP    
**b)** Find a feasible flow    
**c)** Find a cut and compute its capacity    
**d)** Verify: flow value $$\leq$$ cut capacity

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**a) Max Flow LP:**

Variables: $$f_{ij}$$ is the flow on arc $$(i,j)$$

$$
\begin{align}
\max \quad & f_{sa} + f_{sb} \\
\text{s.t.} \quad & f_{sa} - f_{ab} - f_{at} - f_{ac} = 0 \quad \text{(node a)} \\
& f_{sb} + f_{ab} - f_{bc} = 0 \quad \text{(node b)} \\
& f_{ac} + f_{bc} - f_{ct} = 0 \quad \text{(node c)} \\
& 0 \leq f_{sa} \leq 10, \quad 0 \leq f_{sb} \leq 8 \\
& 0 \leq f_{at} \leq 8, \quad 0 \leq f_{ab} \leq 5 \\
& 0 \leq f_{ac} \leq 3, \quad 0 \leq f_{bc} \leq 10 \\
& 0 \leq f_{ct} \leq 10
\end{align}
$$

**b) Feasible flow:**

Try:
- $$f_{sa} = 10$$, $$f_{sb} = 8$$
- $$f_{at} = 8$$, $$f_{ab} = 0$$, $$f_{ac} = 2$$
- $$f_{bc} = 8$$, $$f_{ct} = 10$$

Check conservation:
- Node a: $$10 - 0 - 8 - 2 = 0$$ ✓
- Node b: $$8 + 0 - 8 = 0$$ ✓
- Node c: $$2 + 8 - 10 = 0$$ ✓

Flow value: $$|f| = 10 + 8 = 18$$

**c) Cut:**

Cut $$S = \{s\}$$, $$T = \{a,b,c,t\}$$:

Arcs from $$S$$ to $$T$$:
- $$(s,a)$$: capacity 10
- $$(s,b)$$: capacity 8

Capacity: $$C(S,T) = 10 + 8 = 18$$

**d) Verification:**

Flow value = 18 = cut capacity

By the Max-Flow Min-Cut theorem: this is a maximum flow and a minimum cut! ✓

</details>

---

## **Part V: Matrix Games**

### **Exercise 9: Zero-Sum Game (Dantzig, Ex. 8.1)**

Payoff matrix (from the row player's perspective):

$$
P = \begin{bmatrix}
3 & -1 & 2 \\
1 & 4 & -2 \\
0 & 2 & 3
\end{bmatrix}
$$

**a)** Check for a pure Nash equilibrium    
**b)** Write the LP for the mixed strategy (row player)    
**c)** Write the dual LP (column player)    
**d)** Explain the value of the game

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**a) Pure Nash equilibrium:**

Find the minimum of each row:
- Row 1: $$\min\{3, -1, 2\} = -1$$
- Row 2: $$\min\{1, 4, -2\} = -2$$
- Row 3: $$\min\{0, 2, 3\} = 0$$

Maxmin: $$\max\{-1, -2, 0\} = 0$$ (row 3)

Find the maximum of each column:
- Column 1: $$\max\{3, 1, 0\} = 3$$
- Column 2: $$\max\{-1, 4, 2\} = 4$$
- Column 3: $$\max\{2, -2, 3\} = 3$$

Minmax: $$\min\{3, 4, 3\} = 3$$

$$\text{Maxmin} \neq \text{Minmax}$$ → **There is no pure Nash equilibrium**

**b) LP for the row player:**

Maximize guaranteed payoff $$v$$:

$$
\begin{align}
\max_{x, v} \quad & v \\
\text{s.t.} \quad & 3x_1 + x_2 + 0x_3 \geq v \\
& -x_1 + 4x_2 + 2x_3 \geq v \\
& 2x_1 - 2x_2 + 3x_3 \geq v \\
& x_1 + x_2 + x_3 = 1 \\
& x_1, x_2, x_3 \geq 0
\end{align}
$$

**c) LP for the column player:**

Minimize max loss $$u$$:

$$
\begin{align}
\min_{y, u} \quad & u \\
\text{s.t.} \quad & 3y_1 - y_2 + 2y_3 \leq u \\
& y_1 + 4y_2 - 2y_3 \leq u \\
& 0y_1 + 2y_2 + 3y_3 \leq u \\
& y_1 + y_2 + y_3 = 1 \\
& y_1, y_2, y_3 \geq 0
\end{align}
$$

**d) Value of the game:**

Theo Von Neumann minimax theorem:

$$
v^* = \max_x \min_y x^T P y = \min_y \max_x x^T P y
$$

This value is the Nash equilibrium in mixed strategies.

**Experiment:** $$x = y = (1/3, 1/3, 1/3)$$

Expected payoff for each column:
- Column 1: $$(1/3)(3+1+0) = 4/3$$
- Column 2: $$(1/3)(-1+4+2) = 5/3$$
- Column 3: $$(1/3)(2-2+3) = 1$$

Min = 1, so $$v^* \geq 1$$.

**Optimal solution (solving the LP):** $$x^* = (3/8, 1/4, 3/8)$$, $$y^* = (17/40, 7/20, 9/40)$$, $$v^* = 11/8 = 1.375$$. Check: with $$x^*$$, the payoff of every column equals $$\frac{11}{8}$$ (column 1: $$\frac{9}{8}+\frac{2}{8}$$; column 2: $$-\frac{3}{8}+\frac{8}{8}+\frac{6}{8}$$; column 3: $$\frac{6}{8}-\frac{4}{8}+\frac{9}{8}$$). Note that $$\text{Maxmin} = 0 < v^* = 1.375 < \text{Minmax} = 3$$.

</details>

---

## **Part VI: Advanced Exercises from Boyd & Vandenberghe**

### **Exercise 10: Robust LP (Boyd & Vandenberghe, Ex. 5.11)**

Consider an LP with uncertain coefficients:

$$
\begin{align}
\min_{x} \quad & c^T x \\
\text{s.t.} \quad & a_i^T x \leq b_i, \quad i = 1, \ldots, m \\
& x \geq 0
\end{align}
$$

where $$a_i$$ may vary within an ellipsoid: $$\{a_i + P_i u : \|u\| \leq 1\}$$

**Tasks:**    
a) Write the equivalent robust problem    
b) Show that this is an SOCP (no longer a pure LP)    
c) Construct the dual problem

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**a) Robust formulation:**

The robust constraint requires:

$$
(a_i + P_i u)^T x \leq b_i, \quad \forall \|u\| \leq 1
$$

Equivalently:

$$
a_i^T x + \max_{\|u\| \leq 1} u^T P_i^T x \leq b_i
$$

Theo Cauchy-Schwarz:

$$
\max_{\|u\| \leq 1} u^T P_i^T x = \|P_i^T x\|
$$

Hence the robust constraint is:

$$
a_i^T x + \|P_i^T x\| \leq b_i
$$

**b) This is an SOCP, not an LP:**

The equivalent form is an SOCP (Second-Order Cone Program):

$$
\begin{align}
\min_{x} \quad & c^T x \\
\text{s.t.} \quad & a_i^T x + \|P_i^T x\| \leq b_i, \quad i = 1, \ldots, m \\
& x \geq 0
\end{align}
$$

If $$P_i = 0$$ (no uncertainty), we recover an ordinary LP.

**c) The dual problem:**

Using SOCP duality, the dual problem is rather complicated and is no longer a pure LP.

</details>

---

### **Exercise 11: Chebyshev Center (Boyd & Vandenberghe, Ex. 8.5)**

Find the point $$x_c$$ and the largest radius $$r$$ such that the ball $$\{x : \|x - x_c\| \leq r\}$$ lies inside the polyhedron $$\{x : a_i^T x \leq b_i, i = 1, \ldots, m\}$$.

**Tasks:**    
a) Write the optimization problem    
b) Show that this is an LP    
c) Solve for a specific polyhedron

<details markdown="1">
<summary><strong>Detailed solution</strong></summary>

**a) Formulation:**

The condition for the ball to lie inside the polyhedron:

$$
a_i^T x \leq b_i, \quad \forall x : \|x - x_c\| \leq r
$$

Equivalently:

$$
\max_{\|x - x_c\| \leq r} a_i^T x \leq b_i
$$

$$
a_i^T x_c + r\|a_i\| \leq b_i
$$

**The problem:**

$$
\begin{align}
\max_{x_c, r} \quad & r \\
\text{s.t.} \quad & a_i^T x_c + r\|a_i\| \leq b_i, \quad i = 1, \ldots, m
\end{align}
$$

**b) Proof that it is an LP:**

This is an LP in the variables $$(x_c, r)$$. The coefficients $$\|a_i\|$$ are constants.

**c) A concrete example:**

Given the polyhedron:
- $$x_1 + x_2 \leq 4$$
- $$x_1 - x_2 \leq 2$$
- $$-x_1 + x_2 \leq 2$$
- $$-x_1 - x_2 \leq 2$$

LP:

$$
\begin{align}
\max \quad & r \\
\text{s.t.} \quad & x_{c1} + x_{c2} + r\sqrt{2} \leq 4 \\
& x_{c1} - x_{c2} + r\sqrt{2} \leq 2 \\
& -x_{c1} + x_{c2} + r\sqrt{2} \leq 2 \\
& -x_{c1} - x_{c2} + r\sqrt{2} \leq 2
\end{align}
$$

Solving (by hand or with a solver): $$r\sqrt{2} = 2$$, i.e. $$r = \sqrt{2} \approx 1.414$$, with center $$x_c = (t, t)$$, $$0 \leq t \leq 1$$ (e.g. $$x_c = (0, 0)$$); the solution is not unique because constraint 1 is not active. Check with $$x_c = (0,0)$$: the left-hand sides of the 4 constraints equal $$2, 2, 2, 2$$, i.e. $$\leq 4, 2, 2, 2$$ ✓ (constraints 2, 3, 4 are active).

</details>

---

## **Summary and Strategy**

### **Constructing the dual:**
- Identify the problem type (min/max, constraints)
- Apply the corresponding primal-dual rules
- Number of dual variables = number of primal constraints
- Number of dual constraints = number of primal variables

### **Checking optimality:**
- Primal + Dual feasibility
- Complementary slackness: $$u_i(a_i^T x - b_i) = 0$$
- Compare values: $$f^* = g^*$$ (strong duality)

### **Shadow price:**
- Marginal value of a resource
- Only exact within the sensitivity range
- Slack > 0 → shadow price = 0

### **Max Flow - Min Cut:**
- Flow conservation at intermediate nodes
- Flow value $$\leq$$ cut capacity (weak duality)
- If equal → both are optimal (strong duality)

### **Matrix Games:**
- Check for a saddle point first
- If there is none, solve an LP for the mixed strategy
- Von Neumann minimax: $$\max_x \min_y = \min_y \max_x$$

---

## **References**

1. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Chapter 5: Duality.

2. **Bertsimas, D., & Tsitsiklis, J. N.** (1997). *Introduction to Linear Optimization*. Athena Scientific. Chapters 4, 7.

3. **Dantzig, G. B.** (1963). *Linear Programming and Extensions*. Princeton University Press. Chapters 5-8.

4. **Luenberger, D. G., & Ye, Y.** (2008). *Linear and Nonlinear Programming* (3rd ed.). Springer.

5. **Vanderbei, R. J.** (2020). *Linear Programming: Foundations and Extensions* (5th ed.). Springer.

---

**Note:** The exercises are arranged from basic to advanced and are drawn directly from classic textbooks. Practice them thoroughly to master duality in LP!
