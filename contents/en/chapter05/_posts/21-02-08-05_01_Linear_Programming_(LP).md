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

<div class="content-box exercise-box">
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

<div class="content-box insight-box">
<strong>Key Insight:</strong> The optimal solution of a linear program always occurs at a <strong>vertex</strong> (corner point) of the feasible region! This is why the simplex method works by moving from vertex to vertex.
</div>

<div id="geometric-lp-viz" style="margin: 20px 0; text-align: center;"></div>

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

<div class="content-box insight-box">
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

### Example - Diet program

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

<div class="content-box exercise-box">
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

<div class="content-box insight-box">
<strong>Real-world Applications:</strong>
<ul>
<li><strong>Military logistics:</strong> Feeding troops cost-effectively</li>
<li><strong>Hospital meal planning:</strong> Meeting patient dietary requirements</li>
<li><strong>Animal feed optimization:</strong> Livestock nutrition at minimum cost</li>
<li><strong>School lunch programs:</strong> Nutritious meals within budget constraints</li>
</ul>
</div>

## The Simplex Algorithm

The **Simplex Algorithm**, developed by George Dantzig in 1947, is one of the most important algorithms in optimization history. It revolutionized linear programming by providing an efficient method to solve LP problems systematically.

### Why Simplex Works: The Fundamental Theorem

<div class="content-box insight-box">
<strong>Fundamental Theorem of Linear Programming:</strong> If a linear program has an optimal solution, then there exists an optimal solution that occurs at a vertex (extreme point) of the feasible region.
</div>

This theorem is the key insight behind the Simplex algorithm. Instead of searching the entire feasible region (which could be infinite), we only need to check the finite number of vertices!

### How Simplex Works: The Strategy

The Simplex algorithm follows this elegant strategy:

1. **Start** at any vertex of the feasible region
2. **Check** if the current vertex is optimal  
3. **Move** to an adjacent vertex that improves the objective function
4. **Repeat** until no improvement is possible (optimal solution found)

### Simplex Algorithm Steps

Let's walk through the algorithm step by step using our standard form LP:

> $$ \begin{align}
>     &\text{minimize}_{x} &&{c^T x} \\\\
>     &\text{subject to } &&{A x = b} \\\\
>     & &&{x \succeq 0}.
> \end{align} $$

**Step 1: Initial Setup**
- Convert the LP to standard form (if not already)
- Find an initial basic feasible solution (vertex)
- Set up the simplex tableau

**Step 2: Optimality Test**
- Check if the current solution is optimal
- If all reduced costs are non-negative, we're done!

**Step 3: Choose Entering Variable**
- Select the variable with the most negative reduced cost
- This determines the direction to move

**Step 4: Choose Leaving Variable**  
- Use the minimum ratio test to avoid infeasibility
- This determines how far to move

**Step 5: Pivot Operation**
- Update the tableau using Gaussian elimination
- Move to the new vertex

**Step 6: Repeat**
- Go back to Step 2 until optimal

### Interactive Simplex Example

Let's solve a simple 2D problem step by step to see how Simplex works in practice:

<div class="content-box exercise-box">
<strong>Interactive Simplex Solver:</strong> Watch the algorithm move from vertex to vertex!

**Problem:**
$$\begin{align}
\text{maximize } & 3x_1 + 2x_2 \\
\text{subject to } & x_1 + x_2 \leq 4 \\
& 2x_1 + x_2 \leq 6 \\
& x_1, x_2 \geq 0
\end{align}$$

<div id="simplex-interactive" style="margin: 20px 0;"></div>

<div style="margin: 15px 0;">
  <button id="simplex-step" style="background-color: #2196F3; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; margin-right: 10px;">Next Step</button>
  <button id="simplex-reset" style="background-color: #f44336; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Reset</button>
</div>

<div id="simplex-status" style="margin-top: 15px; font-family: monospace; background-color: #f9f9f9; padding: 15px; border-radius: 4px;">
  <div><strong>Step 0:</strong> Starting at origin (0, 0)</div>
  <div>Current objective value: 0</div>
  <div>Click "Next Step" to begin the Simplex algorithm!</div>
</div>

<div id="simplex-tableau" style="margin-top: 15px; font-family: monospace; background-color: #f0f8ff; padding: 15px; border-radius: 4px;">
  <strong>Current Simplex Tableau:</strong>
  <div id="tableau-content" style="margin-top: 10px;">
    Click "Next Step" to see the tableau!
  </div>
</div>
</div>

### Why Simplex is Efficient

Despite having potentially exponential worst-case complexity, Simplex is remarkably efficient in practice:

<div class="content-box insight-box">
<strong>Simplex Efficiency:</strong>
<ul>
<li><strong>Average case:</strong> Typically visits only 2-3 times the number of constraints</li>
<li><strong>Practical problems:</strong> Often solves in polynomial time</li>
<li><strong>Warm starts:</strong> Can reuse previous solutions when problem changes slightly</li>
<li><strong>Degeneracy handling:</strong> Modern implementations handle degenerate cases well</li>
</ul>
</div>

### Simplex Variants and Modern Developments

**Revised Simplex Method:**
- More numerically stable
- Better for sparse matrices  
- Used in most commercial solvers

**Dual Simplex Method:**
- Starts with dual feasible solution
- Useful for sensitivity analysis
- Better for certain problem types

**Interior Point Methods:**
- Polynomial-time complexity guarantee
- Better for very large problems
- Complement rather than replace Simplex

### Impact and Applications

The Simplex algorithm has transformed numerous industries:

<div class="content-box insight-box">
<strong>Simplex Success Stories:</strong>
<ul>
<li><strong>Airlines:</strong> Crew scheduling, route optimization, fleet assignment</li>
<li><strong>Manufacturing:</strong> Production planning, supply chain optimization</li>
<li><strong>Finance:</strong> Portfolio optimization, risk management</li>
<li><strong>Telecommunications:</strong> Network flow optimization, bandwidth allocation</li>
<li><strong>Energy:</strong> Power grid optimization, resource allocation</li>
</ul>
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
    
    // ==================== SIMPLEX ALGORITHM VISUALIZATION ====================
    
    function initializeSimplexVisualization() {
        const stepButton = document.getElementById('simplex-step');
        const resetButton = document.getElementById('simplex-reset');
        const statusDiv = document.getElementById('simplex-status');
        const tableauDiv = document.getElementById('tableau-content');
        const interactiveDiv = document.getElementById('simplex-interactive');
        
        if (!stepButton || !resetButton || !statusDiv || !tableauDiv || !interactiveDiv) return;
        
        // Simplex algorithm state
        let currentStep = 0;
        let currentVertex = [0, 0]; // Starting at origin
        let isOptimal = false;
        
        // Problem: maximize 3x1 + 2x2 subject to x1 + x2 <= 4, 2x1 + x2 <= 6, x1,x2 >= 0
        // In standard form: minimize -3x1 - 2x2 subject to x1 + x2 + s1 = 4, 2x1 + x2 + s2 = 6
        
        const vertices = [
            [0, 0, 4, 6], // (x1, x2, s1, s2) - origin
            [0, 4, 0, 2], // (0, 4, 0, 2) - intersection with x1 + x2 = 4
            [2, 2, 0, 0], // (2, 2, 0, 0) - intersection of both constraints
            [3, 0, 1, 0]  // (3, 0, 1, 0) - intersection with 2x1 + x2 = 6
        ];
        
        const objectiveValues = [0, 8, 10, 9]; // 3x1 + 2x2 at each vertex
        const simplexPath = [0, 3, 2]; // Path: origin -> (3,0) -> (2,2) optimal
        
        function createVisualization() {
            const width = 400;
            const height = 300;
            const margin = {top: 20, right: 20, bottom: 40, left: 40};
            
            // Clear previous content
            interactiveDiv.innerHTML = '';
            
            const svg = d3.select('#simplex-interactive')
                .append('svg')
                .attr('width', width)
                .attr('height', height);
            
            // Scales
            const xScale = d3.scaleLinear()
                .domain([0, 4])
                .range([margin.left, width - margin.right]);
            
            const yScale = d3.scaleLinear()
                .domain([0, 6])
                .range([height - margin.bottom, margin.top]);
            
            // Draw feasible region
            const feasibleRegion = [
                [0, 0], [0, 4], [2, 2], [3, 0], [0, 0]
            ];
            
            svg.append('path')
                .datum(feasibleRegion)
                .attr('fill', 'lightblue')
                .attr('fill-opacity', 0.3)
                .attr('stroke', 'blue')
                .attr('stroke-width', 2)
                .attr('d', d3.line()
                    .x(d => xScale(d[0]))
                    .y(d => yScale(d[1]))
                );
            
            // Draw constraint lines
            // x1 + x2 = 4
            svg.append('line')
                .attr('x1', xScale(0))
                .attr('y1', yScale(4))
                .attr('x2', xScale(4))
                .attr('y2', yScale(0))
                .attr('stroke', 'red')
                .attr('stroke-width', 2)
                .attr('stroke-dasharray', '5,5');
            
            // 2x1 + x2 = 6
            svg.append('line')
                .attr('x1', xScale(0))
                .attr('y1', yScale(6))
                .attr('x2', xScale(3))
                .attr('y2', yScale(0))
                .attr('stroke', 'green')
                .attr('stroke-width', 2)
                .attr('stroke-dasharray', '5,5');
            
            // Draw vertices
            const vertexPoints = [[0,0], [0,4], [2,2], [3,0]];
            svg.selectAll('.vertex')
                .data(vertexPoints)
                .enter()
                .append('circle')
                .attr('class', 'vertex')
                .attr('cx', d => xScale(d[0]))
                .attr('cy', d => yScale(d[1]))
                .attr('r', 6)
                .attr('fill', 'orange')
                .attr('stroke', 'black')
                .attr('stroke-width', 2);
            
            // Current position indicator
            svg.append('circle')
                .attr('id', 'current-position')
                .attr('cx', xScale(currentVertex[0]))
                .attr('cy', yScale(currentVertex[1]))
                .attr('r', 8)
                .attr('fill', 'red')
                .attr('stroke', 'darkred')
                .attr('stroke-width', 3);
            
            // Axes
            svg.append('g')
                .attr('transform', `translate(0,${height - margin.bottom})`)
                .call(d3.axisBottom(xScale));
            
            svg.append('g')
                .attr('transform', `translate(${margin.left},0)`)
                .call(d3.axisLeft(yScale));
            
            // Axis labels
            svg.append('text')
                .attr('x', width / 2)
                .attr('y', height - 5)
                .attr('text-anchor', 'middle')
                .text('x₁');
            
            svg.append('text')
                .attr('transform', 'rotate(-90)')
                .attr('x', -height / 2)
                .attr('y', 15)
                .attr('text-anchor', 'middle')
                .text('x₂');
            
            // Legend
            const legend = svg.append('g')
                .attr('transform', `translate(${width - 150}, 30)`);
            
            legend.append('text')
                .attr('x', 0)
                .attr('y', 0)
                .text('Constraints:')
                .attr('font-weight', 'bold');
            
            legend.append('line')
                .attr('x1', 0)
                .attr('y1', 15)
                .attr('x2', 20)
                .attr('y2', 15)
                .attr('stroke', 'red')
                .attr('stroke-width', 2)
                .attr('stroke-dasharray', '5,5');
            
            legend.append('text')
                .attr('x', 25)
                .attr('y', 19)
                .text('x₁ + x₂ ≤ 4')
                .attr('font-size', '12px');
            
            legend.append('line')
                .attr('x1', 0)
                .attr('y1', 30)
                .attr('x2', 20)
                .attr('y2', 30)
                .attr('stroke', 'green')
                .attr('stroke-width', 2)
                .attr('stroke-dasharray', '5,5');
            
            legend.append('text')
                .attr('x', 25)
                .attr('y', 34)
                .text('2x₁ + x₂ ≤ 6')
                .attr('font-size', '12px');
        }
        
        function updateTableau(step) {
            let tableauHTML = '';
            
            switch(step) {
                case 0:
                    tableauHTML = `
                        <table style="border-collapse: collapse; margin: 10px 0;">
                            <tr style="background-color: #e0e0e0;">
                                <th style="border: 1px solid #ccc; padding: 8px;">Basic</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">x₁</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">x₂</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">s₁</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">s₂</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">RHS</th>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ccc; padding: 8px;">s₁</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">4</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ccc; padding: 8px;">s₂</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">2</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">6</td>
                            </tr>
                            <tr style="background-color: #fff2cc;">
                                <td style="border: 1px solid #ccc; padding: 8px;">z</td>
                                <td style="border: 1px solid #ccc; padding: 8px; color: red;"><strong>-3</strong></td>
                                <td style="border: 1px solid #ccc; padding: 8px; color: red;">-2</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                            </tr>
                        </table>
                        <div style="margin-top: 10px;">
                            <strong>Analysis:</strong> Most negative coefficient is -3 (x₁ column). x₁ enters the basis.
                        </div>
                    `;
                    break;
                case 1:
                    tableauHTML = `
                        <table style="border-collapse: collapse; margin: 10px 0;">
                            <tr style="background-color: #e0e0e0;">
                                <th style="border: 1px solid #ccc; padding: 8px;">Basic</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">x₁</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">x₂</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">s₁</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">s₂</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">RHS</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">Ratio</th>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ccc; padding: 8px;">s₁</td>
                                <td style="border: 1px solid #ccc; padding: 8px; background-color: #ffcccc;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">4</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">4/1 = 4</td>
                            </tr>
                            <tr style="background-color: #ccffcc;">
                                <td style="border: 1px solid #ccc; padding: 8px;">s₂</td>
                                <td style="border: 1px solid #ccc; padding: 8px; background-color: #ffcccc;"><strong>2</strong></td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">6</td>
                                <td style="border: 1px solid #ccc; padding: 8px;"><strong>6/2 = 3</strong></td>
                            </tr>
                            <tr style="background-color: #fff2cc;">
                                <td style="border: 1px solid #ccc; padding: 8px;">z</td>
                                <td style="border: 1px solid #ccc; padding: 8px; background-color: #ffcccc;">-3</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">-2</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">-</td>
                            </tr>
                        </table>
                        <div style="margin-top: 10px;">
                            <strong>Minimum ratio test:</strong> min{4/1, 6/2} = min{4, 3} = 3. s₂ leaves the basis.
                        </div>
                    `;
                    break;
                case 2:
                    tableauHTML = `
                        <table style="border-collapse: collapse; margin: 10px 0;">
                            <tr style="background-color: #e0e0e0;">
                                <th style="border: 1px solid #ccc; padding: 8px;">Basic</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">x₁</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">x₂</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">s₁</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">s₂</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">RHS</th>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ccc; padding: 8px;">s₁</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px; color: red;"><strong>0.5</strong></td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">-0.5</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ccc; padding: 8px;">x₁</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0.5</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0.5</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">3</td>
                            </tr>
                            <tr style="background-color: #fff2cc;">
                                <td style="border: 1px solid #ccc; padding: 8px;">z</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px; color: red;"><strong>-0.5</strong></td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1.5</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">9</td>
                            </tr>
                        </table>
                        <div style="margin-top: 10px;">
                            <strong>Current solution:</strong> x₁ = 3, x₂ = 0, objective = 9<br>
                            <strong>Analysis:</strong> x₂ has negative coefficient (-0.5), so x₂ enters the basis.
                        </div>
                    `;
                    break;
                case 3:
                    tableauHTML = `
                        <table style="border-collapse: collapse; margin: 10px 0;">
                            <tr style="background-color: #e0e0e0;">
                                <th style="border: 1px solid #ccc; padding: 8px;">Basic</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">x₁</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">x₂</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">s₁</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">s₂</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">RHS</th>
                            </tr>
                            <tr style="background-color: #ccffcc;">
                                <td style="border: 1px solid #ccc; padding: 8px;">x₂</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">2</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">-1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">2</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ccc; padding: 8px;">x₁</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">-1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">2</td>
                            </tr>
                            <tr style="background-color: #ccffcc;">
                                <td style="border: 1px solid #ccc; padding: 8px;">z</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">10</td>
                            </tr>
                        </table>
                        <div style="margin-top: 10px;">
                            <strong>OPTIMAL SOLUTION FOUND!</strong><br>
                            x₁ = 2, x₂ = 2, Maximum objective value = 10<br>
                            All coefficients in the objective row are non-negative.
                        </div>
                    `;
                    break;
            }
            
            tableauDiv.innerHTML = tableauHTML;
        }
        
        function updateStatus(step) {
            let statusHTML = '';
            
            switch(step) {
                case 0:
                    statusHTML = `
                        <div><strong>Step 0:</strong> Initial basic feasible solution</div>
                        <div>Current vertex: (0, 0)</div>
                        <div>Current objective value: 0</div>
                        <div>Basic variables: s₁ = 4, s₂ = 6</div>
                    `;
                    currentVertex = [0, 0];
                    break;
                case 1:
                    statusHTML = `
                        <div><strong>Step 1:</strong> Choose entering variable</div>
                        <div>Most negative coefficient: -3 (x₁ column)</div>
                        <div>x₁ enters the basis</div>
                        <div>Performing minimum ratio test...</div>
                    `;
                    break;
                case 2:
                    statusHTML = `
                        <div><strong>Step 2:</strong> First iteration complete</div>
                        <div>Current vertex: (3, 0)</div>
                        <div>Current objective value: 9</div>
                        <div>Basic variables: x₁ = 3, s₁ = 1</div>
                    `;
                    currentVertex = [3, 0];
                    break;
                case 3:
                    statusHTML = `
                        <div><strong>Step 3:</strong> OPTIMAL SOLUTION FOUND!</div>
                        <div>Current vertex: (2, 2)</div>
                        <div>Maximum objective value: 10</div>
                        <div>Basic variables: x₁ = 2, x₂ = 2</div>
                    `;
                    currentVertex = [2, 2];
                    isOptimal = true;
                    break;
            }
            
            statusDiv.innerHTML = statusHTML;
            
            // Update visualization
            const currentPos = d3.select('#current-position');
            if (currentPos.node()) {
                const xScale = d3.scaleLinear().domain([0, 4]).range([40, 360]);
                const yScale = d3.scaleLinear().domain([0, 6]).range([260, 40]);
                
                currentPos
                    .transition()
                    .duration(500)
                    .attr('cx', xScale(currentVertex[0]))
                    .attr('cy', yScale(currentVertex[1]));
            }
        }
        
        function nextStep() {
            if (currentStep < 3) {
                currentStep++;
                updateStatus(currentStep);
                updateTableau(currentStep);
                
                if (currentStep === 3) {
                    stepButton.textContent = 'Algorithm Complete!';
                    stepButton.disabled = true;
                    stepButton.style.backgroundColor = '#4CAF50';
                }
            }
        }
        
        function reset() {
            currentStep = 0;
            currentVertex = [0, 0];
            isOptimal = false;
            
            stepButton.textContent = 'Next Step';
            stepButton.disabled = false;
            stepButton.style.backgroundColor = '#2196F3';
            
            updateStatus(0);
            updateTableau(0);
            createVisualization();
        }
        
        // Event listeners
        stepButton.addEventListener('click', nextStep);
        resetButton.addEventListener('click', reset);
        
        // Initialize
        createVisualization();
        updateStatus(0);
        updateTableau(0);
    }
    
    // Initialize all interactive elements
    initializeFarmerProblem();
    initializeDietSolver();
    initializeSimplexVisualization();
    
    // Trigger MathJax re-rendering if needed
    if (window.MathJax) {
        MathJax.typesetPromise();
    }
});
</script>
