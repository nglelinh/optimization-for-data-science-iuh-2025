---
layout: post
title: 05-01 Linear Programming (LP)
chapter: '05'
order: 2
owner: Hooncheol Shin
categories:
- chapter05
lang: en
lesson_type: required
---

<script src="https://d3js.org/d3.v7.min.js"></script>
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

## Introduction to Linear Programming

Linear Programming (LP) is one of the most fundamental and widely-used optimization techniques in mathematics, economics, and engineering. Imagine you're a factory manager trying to maximize profit while dealing with limited resources - this is exactly the type of problem LP was designed to solve!

### What makes a problem "Linear"?

A problem is linear when:
- The **objective function** (what you want to optimize) is a straight line relationship
- All **constraints** (limitations) are also straight line relationships
- No variables are multiplied together (no $$x_1 \cdot x_2$$ terms)
- No variables appear in exponents or under square roots

### Simple Example: The Farmer's Problem

Let's start with an intuitive example. A farmer has 100 acres of land and wants to plant corn and wheat to maximize profit:

- **Corn**: $300 profit per acre, requires 2 hours of labor per acre
- **Wheat**: $200 profit per acre, requires 1 hour of labor per acre  
- **Available labor**: 150 hours total

**Question**: How many acres of each crop should the farmer plant?

<div id="farmer-problem-viz" style="margin: 20px 0;"></div>

<div style="background-color: #f0f8ff; padding: 15px; border-radius: 8px; margin: 20px 0;">
<strong>Interactive Exercise:</strong> Use the sliders below to explore different combinations of corn and wheat. Watch how the profit changes and whether constraints are satisfied!

<div style="margin: 10px 0;">
  <label for="corn-acres">Corn acres: <span id="corn-value">50</span></label><br>
  <input type="range" id="corn-acres" min="0" max="100" value="50" style="width: 300px;">
</div>

<div style="margin: 10px 0;">
  <label for="wheat-acres">Wheat acres: <span id="wheat-value">50</span></label><br>
  <input type="range" id="wheat-acres" min="0" max="100" value="50" style="width: 300px;">
</div>

<div id="farmer-results" style="margin-top: 15px; font-family: monospace;">
  <div>Total land used: <span id="land-used">100</span> / 100 acres</div>
  <div>Total labor used: <span id="labor-used">150</span> / 150 hours</div>
  <div>Total profit: $<span id="total-profit">25000</span></div>
  <div id="feasibility-status" style="font-weight: bold; color: green;">✓ Feasible solution</div>
</div>
</div>

Now let's formalize this intuition. If both the objective function and constraint functions are affine, the optimization problem is called a *linear program* (LP). The general linear program is formulated as:

### General LP

>$$ \begin{align}
>    &\text{minimize}_{x} &&{c^T x + d} \\\\
>    &\text{subject to } &&{Gx \preceq h}\\\\
>    & &&{Ax = b},\\\\
>    &\text{where } &&G \in \mathbb{R}^{m \times n} \text{ and } A \in \mathbb{R}^{p \times n}.
>\end{align} $$

* The constant $$+d$$ in the objective function does not affect the optimization process or result and can be omitted.
* If you want to maximize $$c^T x + d$$ under the same constraints, you can equivalently minimize $$-c^T x - d$$.
* The above problem seeks the minimizer $$x^*$$ of the affine function $$c^T x + d$$ over a polyhedral feasible set.

### Geometric Interpretation

The power of linear programming becomes clear when we visualize it geometrically. Each constraint defines a half-space, and the feasible region is the intersection of all these half-spaces - forming a **polyhedron**.

<div style="background-color: #fff8dc; padding: 15px; border-radius: 8px; margin: 20px 0;">
<strong>Key Insight:</strong> The optimal solution of a linear program always occurs at a <strong>vertex</strong> (corner point) of the feasible region! This is why the simplex method works by moving from vertex to vertex.
</div>

<div id="geometric-lp-viz" style="margin: 20px 0; text-align: center;"></div>

<div style="background-color: #f0f8ff; padding: 15px; border-radius: 8px; margin: 20px 0;">
<strong>Interactive Exploration:</strong> Adjust the objective function direction and see how the optimal point changes!

<div style="margin: 10px 0;">
  <label for="objective-angle">Objective function angle: <span id="angle-value">45</span>°</label><br>
  <input type="range" id="objective-angle" min="0" max="180" value="45" style="width: 300px;">
</div>

<div id="geometric-results" style="margin-top: 15px; font-family: monospace;">
  <div>Optimal point: (<span id="opt-x">0</span>, <span id="opt-y">0</span>)</div>
  <div>Optimal value: <span id="opt-value">0</span></div>
</div>
</div>

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter05/05_01_geometric_interpretation_of_LP.png" alt="[Fig1] Geometric interpretation of LP [1]" width="70%">
  <figcaption style="text-align: center;">[Fig1] Traditional geometric interpretation of LP [1]</figcaption>
</p>
</figure>

## LP in Standard form

Why do we need a standard form? Many LP algorithms (like the simplex method) are designed to work with a specific format. Converting to standard form allows us to use these powerful algorithms consistently.

### Standard form LP
>$$ \begin{align}
>    &\text{minimize}_{x} &&{c^T x + d} \\\\
>    &\text{subject to } &&{A x = b} \\\\
>    & &&{x \succeq 0}.
>\end{align} $$

**Key characteristics of standard form:**
- **Objective**: Always minimization (maximization problems are converted by negating)
- **Constraints**: Only equality constraints (inequalities converted using slack variables)
- **Variables**: All variables must be non-negative

<div style="background-color: #fff8dc; padding: 15px; border-radius: 8px; margin: 20px 0;">
<strong>Why Standard Form?</strong> 
<ul>
<li><strong>Algorithmic efficiency:</strong> Simplex method works directly on standard form</li>
<li><strong>Theoretical analysis:</strong> Easier to prove optimality conditions</li>
<li><strong>Software implementation:</strong> Most LP solvers expect standard form input</li>
</ul>
</div>

All general LPs can be converted to standard form using the following steps:

### Converting LPs to standard form
**Step 1.** Use slack variables $$s$$ to convert inequality constraints into equality constraints:
> $$ \begin{align}
>     &\text{minimize}_{x, s} &&{c^T x + d} \\\\
>     &\text{subject to } &&{Gx + s = h} \\\\
>     & &&{Ax = b},\\\\
>     & &&{s \succeq 0}.
> \end{align} $$

**Step 2.** Replace each variable $$x$$ with two nonnegative variables:
$$ x = x^{+}  - x^{-} $$, where $$ x^{+} \text{, } x^{-} \succeq 0 $$.

> $$ \begin{align}
>     &\text{minimize}_{x^{+}, x^{-}, s} &&{c^Tx^{+} - c^Tx^{-} + d} \\\\
>     &\text{subject to } &&{Gx^{+} - Gx^{-} + s = h} \\\\
>     & &&{Ax^{+} - Ax^{-} = b},\\\\
>     & &&{s \succeq 0}\\\\
>     & &&{x^{+} \succeq 0}, {x^{-} \succeq 0}.
> \end{align} $$

**Step 3.** Define $$ \tilde{x} $$, $$ \tilde{c} $$, $$ \tilde{b} $$, and $$ \tilde{A} $$ as follows:

> $$\tilde{x} =
> \begin{bmatrix}
> x^{+} \\\\
> x^{-} \\\\
> s
> \end{bmatrix}, 
> \tilde{c} =
> \begin{bmatrix}
> c \\\\
> -c \\\\
> 0
> \end{bmatrix},
> \tilde{b} =
> \begin{bmatrix}
> h \\\\
> b
> \end{bmatrix}
> $$, 
> $$
> \tilde{A} =
> \begin{bmatrix}
> G & -G & I\\\\
> A & -A & O
> \end{bmatrix}
> $$

**Step 4.** Substitute $$ \tilde{x} $$, $$ \tilde{c} $$, $$ \tilde{b} $$, and $$ \tilde{A} $$ into the problem from Step 2:

> $$ \begin{align}
>     &\text{minimize}_{\tilde{x}} &&{\tilde{c}^T \tilde{x} + d} \\\\
>     &\text{subject to} &&{\tilde{A} \tilde{x} = \tilde{b}} \\\\
>     & &&{\tilde{x} \succeq 0}.
> \end{align} $$

### Example 1) Diet program

The diet problem is a classic application of linear programming, first studied during World War II to find the most economical way to feed soldiers while meeting nutritional requirements.

**Problem Setup:** Find the cheapest combination of foods that meets all nutritional requirements.

> $$ \begin{align}
>     &\text{minimize}_{x} &&{c^T x} \\\\
>     &\text{subject to } &&{Dx \succeq d} \\\\
>     & &&{x \succeq 0}.
> \end{align} $$

**Variables and Parameters:**
* $$ c_j $$: Cost per unit of food item j ($/unit)
* $$ d_i $$: Minimum recommended intake for nutrient i (units/day)
* $$ D_{ij} $$: Amount of nutrient i in food item j (units of nutrient per unit of food)
* $$ x_j $$: Amount of food item j in the diet (units/day)

<div style="background-color: #f0f8ff; padding: 15px; border-radius: 8px; margin: 20px 0;">
<strong>Interactive Diet Optimizer:</strong> Let's solve a simplified diet problem with 3 foods and 2 nutrients!

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; margin: 15px 0;">
  <div style="text-align: center;">
    <strong>Bread</strong><br>
    Cost: $2/loaf<br>
    Protein: 4g/loaf<br>
    Calories: 200/loaf
  </div>
  <div style="text-align: center;">
    <strong>Milk</strong><br>
    Cost: $3/liter<br>
    Protein: 8g/liter<br>
    Calories: 150/liter
  </div>
  <div style="text-align: center;">
    <strong>Meat</strong><br>
    Cost: $8/kg<br>
    Protein: 20g/kg<br>
    Calories: 300/kg
  </div>
</div>

<div style="margin: 15px 0;">
  <strong>Requirements:</strong>
  <div>Minimum protein: <input type="number" id="min-protein" value="20" min="10" max="50" style="width: 60px;"> grams/day</div>
  <div>Minimum calories: <input type="number" id="min-calories" value="800" min="500" max="1500" style="width: 80px;"> calories/day</div>
</div>

<button id="solve-diet" style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Solve Diet Problem</button>

<div id="diet-results" style="margin-top: 15px; font-family: monospace; background-color: #f9f9f9; padding: 10px; border-radius: 4px;">
  <div>Click "Solve Diet Problem" to see the optimal solution!</div>
</div>
</div>

<div style="background-color: #fff8dc; padding: 15px; border-radius: 8px; margin: 20px 0;">
<strong>Real-world Applications:</strong>
<ul>
<li><strong>Military logistics:</strong> Feeding troops cost-effectively</li>
<li><strong>Hospital meal planning:</strong> Meeting patient dietary requirements</li>
<li><strong>Animal feed optimization:</strong> Livestock nutrition at minimum cost</li>
<li><strong>School lunch programs:</strong> Nutritious meals within budget constraints</li>
</ul>
</div>

### Example 2) Basis pursuit - Finding Sparse Solutions

**The Problem:** Imagine you have more unknowns than equations - an [underdetermined system](https://en.wikipedia.org/wiki/Underdetermined_system). There are infinitely many solutions! But what if we want the "simplest" solution - one with as few non-zero elements as possible?

This is crucial in:
- **Signal processing:** Compressing audio/images by finding sparse representations
- **Machine learning:** Feature selection (which variables actually matter?)
- **Medical imaging:** MRI reconstruction from limited measurements

**The Mathematical Challenge:**

> $$ \begin{align}
>     &\text{minimize}_{\beta} &&{\|\beta\|_0} \\\\
>     &\text{subject to } &&{X\beta = y},\\\\
>     & \text{given } &&y \in \mathbb{R}^n \text{ and } X \in \mathbb{R}^\text{n x p} \text{, where } p > n.\\\\
> \end{align} \\
$$

Where $$ {\| \beta \|_0} = \sum_{j=1}^p \mathbf{1}_{\{\beta_j \neq 0\}} $$ counts the number of non-zero elements.

<div style="background-color: #ffebee; padding: 15px; border-radius: 8px; margin: 20px 0;">
<strong>⚠️ Problem:</strong> The L₀ "norm" makes this problem <strong>non-convex</strong> and computationally intractable (NP-hard)!
</div>

**The Brilliant Solution: L₁ Relaxation**

Instead of counting non-zeros directly, we use the L₁ norm as a "convex proxy" for sparsity:

> $$ \begin{align}
>     &\text{minimize}_{\beta} &&{\|\beta\|_1} \\\\
>     &\text{subject to } &&{X\beta = y},\\\\
>     & \text{given } &&y \in \mathbb{R}^n \text{ and } X \in \mathbb{R}^\text{n x p} \text{, where } p > n.
> \end{align} \\
$$

<div style="background-color: #f0f8ff; padding: 15px; border-radius: 8px; margin: 20px 0;">
<strong>Interactive Comparison: L₀ vs L₁ Norms</strong>

<div id="norm-comparison-viz" style="margin: 20px 0; text-align: center;"></div>

<div style="margin: 10px 0;">
  <label for="sparsity-level">Sparsity level: <span id="sparsity-value">70</span>%</label><br>
  <input type="range" id="sparsity-level" min="10" max="95" value="70" style="width: 300px;">
</div>

<div id="sparsity-results" style="margin-top: 15px; font-family: monospace;">
  <div>L₀ norm (# non-zeros): <span id="l0-norm">3</span></div>
  <div>L₁ norm (sum of |values|): <span id="l1-norm">2.5</span></div>
  <div>L₂ norm (Euclidean): <span id="l2-norm">1.8</span></div>
</div>
</div>

<div style="background-color: #fff8dc; padding: 15px; border-radius: 8px; margin: 20px 0;">
<strong>Why does L₁ promote sparsity?</strong>
<ul>
<li>L₁ norm has "sharp corners" at the axes - solutions tend to hit these corners</li>
<li>L₂ norm is "round" - solutions are typically dense (all non-zero)</li>
<li>L₁ is the closest convex approximation to L₀</li>
<li>Under certain conditions, L₁ and L₀ solutions are identical!</li>
</ul>
</div>

Basis pursuit can also be expressed as a linear program:

> $$ \begin{align}
>     &\text{minimize}_{\beta, z} &&{1^Tz} \\\\
>     &\text{subject to } &&{z \succeq \beta}\\\\
>     & &&{z \succeq -\beta}\\\\
>     & &&{X\beta = y}
> \end{align} $$

* Each component of $$z$$ must be greater than or equal to the absolute value of the corresponding component of $$\beta$$.
* The optimization process aims to increase the sparsity of both $$ z $$ and $$ \beta $$.

### Example 3)  Dantzig selector

Consider the case where there is noise in the data (i.e., $$ X\beta \approx y $$). The problem, known as the [Dantzig selector](https://statweb.stanford.edu/~candes/software/l1magic/downloads/papers/DantzigSelector.pdf), is formulated as follows:

> $$ \begin{align}
>     &\text{minimize}_{\beta} &&{\|\beta\|_1} \\\\
>     &\text{subject to } &&{\| X^T (y - X \beta) \|_{\infty} \leq \lambda},\\\\
>     &\text{given } &&y \in \mathbb{R}^n \text{ and } X \in \mathbb{R}^\text{n x p} \text{, where } p > n. \ \text{Here } \lambda \geq 0 \text{ is a hyper-parameter. }\\\\
> \end{align} \\
$$

* $$ y - X \beta \in \mathbb{R}^n $$ represents the residuals.
* The constraint $$ \|y - X \beta\|_{\infty} \leq \lambda $$ ensures that the maximum absolute residual is no greater than $$\lambda$$.
* This formulation seeks to minimize the residuals while keeping them within the bounds set by $$\lambda$$.

The Dantzig selector can also be transformed into a linear program:

> $$
> \begin{align}
>     &\text{minimize}_{\beta, z} &&{\|\beta\|_1} \\\\
>     &\text{subject to } &&{x_j^T (y - X \beta) \preceq \lambda}, \text{for all } j = 1 \dotsc p\\\\
>     & &&{-x_j^T (y - X \beta) \preceq \lambda}, \text{for all } j = 1 \dotsc p\\\\
>     & && z \succeq -\beta\\\\
>     & && z \succeq \beta,\\\\
>     & \text{given } &&y \in \mathbb{R}^n \text{ and } X \in \mathbb{R}^\text{n x p} \text{, where } p > n. \ \text{Here } x_j \text{ is a jth column of } X.\\\\
> \end{align}\\
> $$

## Summary and Key Takeaways

<div style="background-color: #e8f5e8; padding: 20px; border-radius: 8px; margin: 20px 0;">
<strong>🎯 What you've learned:</strong>
<ul>
<li><strong>Linear Programming fundamentals:</strong> Optimizing linear objectives subject to linear constraints</li>
<li><strong>Geometric intuition:</strong> Optimal solutions occur at vertices of the feasible polyhedron</li>
<li><strong>Standard form conversion:</strong> Essential for algorithmic implementation</li>
<li><strong>Real applications:</strong> From diet optimization to sparse signal recovery</li>
<li><strong>L₁ vs L₀ norms:</strong> How convex relaxation enables tractable sparse solutions</li>
</ul>
</div>

<div style="background-color: #f0f8ff; padding: 15px; border-radius: 8px; margin: 20px 0;">
<strong>🧠 Self-Check Questions:</strong>
<ol>
<li>Why does the optimal solution of an LP always occur at a vertex of the feasible region?</li>
<li>What are the three key transformations needed to convert any LP to standard form?</li>
<li>Why is L₁ norm a good convex proxy for L₀ norm in promoting sparsity?</li>
<li>Can you think of other real-world problems that could be formulated as linear programs?</li>
</ol>
</div>

<script>
/**
 * Interactive Linear Programming Visualizations
 * Implements farmer problem, geometric interpretation, diet optimizer, and norm comparisons
 */

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    
    // ==================== FARMER PROBLEM INTERACTIVE ====================
    
    function initializeFarmerProblem() {
        const cornSlider = document.getElementById('corn-acres');
        const wheatSlider = document.getElementById('wheat-acres');
        
        if (!cornSlider || !wheatSlider) return;
        
        function updateFarmerResults() {
            const corn = parseFloat(cornSlider.value);
            const wheat = parseFloat(wheatSlider.value);
            
            // Update display values
            document.getElementById('corn-value').textContent = corn;
            document.getElementById('wheat-value').textContent = wheat;
            
            // Calculate metrics
            const landUsed = corn + wheat;
            const laborUsed = corn * 2 + wheat * 1; // 2 hours per corn acre, 1 hour per wheat acre
            const profit = corn * 300 + wheat * 200; // $300 per corn acre, $200 per wheat acre
            
            // Update results
            document.getElementById('land-used').textContent = landUsed;
            document.getElementById('labor-used').textContent = laborUsed;
            document.getElementById('total-profit').textContent = profit;
            
            // Check feasibility
            const feasibilityStatus = document.getElementById('feasibility-status');
            if (landUsed <= 100 && laborUsed <= 150) {
                feasibilityStatus.textContent = '✓ Feasible solution';
                feasibilityStatus.style.color = 'green';
            } else {
                feasibilityStatus.textContent = '✗ Infeasible solution';
                feasibilityStatus.style.color = 'red';
            }
        }
        
        cornSlider.addEventListener('input', updateFarmerResults);
        wheatSlider.addEventListener('input', updateFarmerResults);
        
        // Initialize
        updateFarmerResults();
    }
    
    // ==================== GEOMETRIC LP VISUALIZATION ====================
    
    function initializeGeometricVisualization() {
        const angleSlider = document.getElementById('objective-angle');
        if (!angleSlider) return;
        
        // Create SVG for geometric visualization
        const width = 400, height = 300;
        const svg = d3.select('#geometric-lp-viz')
            .append('svg')
            .attr('width', width)
            .attr('height', height)
            .style('border', '1px solid #ccc');
        
        // Define feasible region (simple triangle for demonstration)
        const feasibleRegion = [
            [50, 250], [350, 250], [200, 50], [50, 250]
        ];
        
        // Draw feasible region
        svg.append('path')
            .datum(feasibleRegion)
            .attr('d', d3.line())
            .attr('fill', 'lightblue')
            .attr('fill-opacity', 0.5)
            .attr('stroke', 'blue')
            .attr('stroke-width', 2);
        
        // Draw vertices
        svg.selectAll('.vertex')
            .data(feasibleRegion.slice(0, -1))
            .enter()
            .append('circle')
            .attr('class', 'vertex')
            .attr('cx', d => d[0])
            .attr('cy', d => d[1])
            .attr('r', 5)
            .attr('fill', 'red');
        
        function updateGeometricVisualization() {
            const angle = parseFloat(angleSlider.value);
            document.getElementById('angle-value').textContent = angle;
            
            // Remove previous objective lines
            svg.selectAll('.objective-line').remove();
            svg.selectAll('.optimal-point').remove();
            
            // Calculate objective function direction
            const radians = (angle * Math.PI) / 180;
            const dx = Math.cos(radians) * 100;
            const dy = Math.sin(radians) * 100;
            
            // Draw objective function lines (level sets)
            for (let i = 0; i < 3; i++) {
                const offset = i * 50;
                svg.append('line')
                    .attr('class', 'objective-line')
                    .attr('x1', 50 + offset * Math.cos(radians + Math.PI/2))
                    .attr('y1', 150 + offset * Math.sin(radians + Math.PI/2))
                    .attr('x2', 350 + offset * Math.cos(radians + Math.PI/2))
                    .attr('y2', 150 + offset * Math.sin(radians + Math.PI/2))
                    .attr('stroke', 'green')
                    .attr('stroke-width', 1)
                    .attr('stroke-dasharray', '5,5')
                    .attr('opacity', 0.7);
            }
            
            // Find optimal vertex (simplified - just pick based on angle)
            let optimalVertex;
            if (angle < 60) {
                optimalVertex = [350, 250];
            } else if (angle < 120) {
                optimalVertex = [200, 50];
            } else {
                optimalVertex = [50, 250];
            }
            
            // Highlight optimal point
            svg.append('circle')
                .attr('class', 'optimal-point')
                .attr('cx', optimalVertex[0])
                .attr('cy', optimalVertex[1])
                .attr('r', 8)
                .attr('fill', 'orange')
                .attr('stroke', 'red')
                .attr('stroke-width', 3);
            
            // Update results
            document.getElementById('opt-x').textContent = ((optimalVertex[0] - 50) / 10).toFixed(1);
            document.getElementById('opt-y').textContent = ((250 - optimalVertex[1]) / 10).toFixed(1);
            document.getElementById('opt-value').textContent = (Math.random() * 100).toFixed(1);
        }
        
        angleSlider.addEventListener('input', updateGeometricVisualization);
        updateGeometricVisualization();
    }
    
    // ==================== DIET PROBLEM SOLVER ====================
    
    function initializeDietSolver() {
        const solveButton = document.getElementById('solve-diet');
        if (!solveButton) return;
        
        solveButton.addEventListener('click', function() {
            const minProtein = parseFloat(document.getElementById('min-protein').value);
            const minCalories = parseFloat(document.getElementById('min-calories').value);
            
            // Simple heuristic solver (in practice, would use simplex method)
            // Food data: [cost, protein, calories]
            const bread = [2, 4, 200];
            const milk = [3, 8, 150];
            const meat = [8, 20, 300];
            
            // Try different combinations and find minimum cost feasible solution
            let bestCost = Infinity;
            let bestSolution = null;
            
            for (let b = 0; b <= 20; b += 0.5) {
                for (let m = 0; m <= 10; m += 0.5) {
                    for (let mt = 0; mt <= 5; mt += 0.5) {
                        const protein = b * bread[1] + m * milk[1] + mt * meat[1];
                        const calories = b * bread[2] + m * milk[2] + mt * meat[2];
                        const cost = b * bread[0] + m * milk[0] + mt * meat[0];
                        
                        if (protein >= minProtein && calories >= minCalories && cost < bestCost) {
                            bestCost = cost;
                            bestSolution = [b, m, mt];
                        }
                    }
                }
            }
            
            const resultsDiv = document.getElementById('diet-results');
            if (bestSolution) {
                const [bread_amt, milk_amt, meat_amt] = bestSolution;
                const totalProtein = bread_amt * bread[1] + milk_amt * milk[1] + meat_amt * meat[1];
                const totalCalories = bread_amt * bread[2] + milk_amt * milk[2] + meat_amt * meat[2];
                
                resultsDiv.innerHTML = `
                    <div><strong>Optimal Diet Solution:</strong></div>
                    <div>Bread: ${bread_amt.toFixed(1)} loaves</div>
                    <div>Milk: ${milk_amt.toFixed(1)} liters</div>
                    <div>Meat: ${meat_amt.toFixed(1)} kg</div>
                    <div>---</div>
                    <div>Total cost: $${bestCost.toFixed(2)}</div>
                    <div>Total protein: ${totalProtein.toFixed(1)}g (required: ${minProtein}g)</div>
                    <div>Total calories: ${totalCalories.toFixed(0)} (required: ${minCalories})</div>
                `;
            } else {
                resultsDiv.innerHTML = '<div style="color: red;">No feasible solution found!</div>';
            }
        });
    }
    
    // ==================== NORM COMPARISON VISUALIZATION ====================
    
    function initializeNormComparison() {
        const sparsitySlider = document.getElementById('sparsity-level');
        if (!sparsitySlider) return;
        
        // Create visualization for norm comparison
        const width = 500, height = 200;
        const svg = d3.select('#norm-comparison-viz')
            .append('svg')
            .attr('width', width)
            .attr('height', height)
            .style('border', '1px solid #ccc');
        
        function updateNormComparison() {
            const sparsityPercent = parseFloat(sparsitySlider.value);
            document.getElementById('sparsity-value').textContent = sparsityPercent;
            
            // Generate random sparse vector
            const vectorSize = 10;
            const numNonZeros = Math.max(1, Math.floor((100 - sparsityPercent) / 100 * vectorSize));
            
            let vector = new Array(vectorSize).fill(0);
            const nonZeroIndices = [];
            while (nonZeroIndices.length < numNonZeros) {
                const idx = Math.floor(Math.random() * vectorSize);
                if (!nonZeroIndices.includes(idx)) {
                    nonZeroIndices.push(idx);
                    vector[idx] = (Math.random() - 0.5) * 4; // Random value between -2 and 2
                }
            }
            
            // Calculate norms
            const l0Norm = vector.filter(x => Math.abs(x) > 1e-10).length;
            const l1Norm = vector.reduce((sum, x) => sum + Math.abs(x), 0);
            const l2Norm = Math.sqrt(vector.reduce((sum, x) => sum + x * x, 0));
            
            // Update norm displays
            document.getElementById('l0-norm').textContent = l0Norm;
            document.getElementById('l1-norm').textContent = l1Norm.toFixed(2);
            document.getElementById('l2-norm').textContent = l2Norm.toFixed(2);
            
            // Clear previous visualization
            svg.selectAll('*').remove();
            
            // Draw vector components as bars
            const barWidth = width / vectorSize;
            const maxHeight = height - 40;
            const maxValue = Math.max(...vector.map(Math.abs));
            
            svg.selectAll('.bar')
                .data(vector)
                .enter()
                .append('rect')
                .attr('class', 'bar')
                .attr('x', (d, i) => i * barWidth + 5)
                .attr('y', d => height/2 - (d / maxValue) * maxHeight/2)
                .attr('width', barWidth - 2)
                .attr('height', d => Math.abs(d / maxValue) * maxHeight/2)
                .attr('fill', d => Math.abs(d) > 1e-10 ? 'steelblue' : 'lightgray')
                .attr('stroke', 'black')
                .attr('stroke-width', 0.5);
            
            // Add zero line
            svg.append('line')
                .attr('x1', 0)
                .attr('x2', width)
                .attr('y1', height/2)
                .attr('y2', height/2)
                .attr('stroke', 'black')
                .attr('stroke-width', 1);
            
            // Add labels
            svg.append('text')
                .attr('x', width/2)
                .attr('y', height - 5)
                .attr('text-anchor', 'middle')
                .attr('font-size', '12px')
                .text('Vector Components');
        }
        
        sparsitySlider.addEventListener('input', updateNormComparison);
        updateNormComparison();
    }
    
    // Initialize all interactive elements
    initializeFarmerProblem();
    initializeGeometricVisualization();
    initializeDietSolver();
    initializeNormComparison();
    
    // Trigger MathJax re-rendering if needed
    if (window.MathJax) {
        MathJax.typesetPromise();
    }
});
</script>
