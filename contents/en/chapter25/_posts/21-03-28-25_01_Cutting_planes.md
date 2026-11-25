---
layout: post
title: 25-01 Cutting Planes
chapter: '25'
order: 2
owner: YoungJae Choung
categories:
- chapter25
lang: en
---

In 1954, George Dantzig, Ray Fulkerson, and Selmer Johnson solved a 49-city Traveling Salesman Problem to provable global optimality—a feat everyone thought was impossible—by iteratively solving LP relaxations and adding hand-crafted inequalities that sliced off fractional subtours. Four years later, Ralph Gomory stunned the field by proving that cutting planes could be generated *purely algebraically* for any integer linear program. Though pure cutting-plane methods struggled with numerical ill-conditioning in the 1960s, their fusion with Branch and Bound in the 1990s triggered a million-fold speedup in integer programming.

## Key ideas: Geometric Intuition and History of Cutting Planes

- **Geometric Picture of a Cut:** Imagine the integer feasible points $$S = P \cap \mathbb{Z}^n$$ as pegs hammered into a board, and the LP relaxation $$P$$ as a loose polygon wrapped around them. A cutting plane is a straight line sliced across $$P$$ that trims away empty space containing $$x_{\text{LP}}$$ without nicking a single peg.
- **Outer Approximation of the Convex Hull:** Rather than computing all exponentially many facets of $$\operatorname{conv}(S)$$ up front, cutting-plane methods generate inequalities lazily—only in the neighborhood of the current optimal LP face.
- **Why Pure Cutting Planes Stalled Historically:** Adding hundreds of algebraic cuts sequentially without branching creates dense, numerically unstable simplex tableaus and suffers from slow tailing-off convergence.
- **The 1990s Renaissance (Polyhedral Combinatorics + Branch-and-Cut):** Combining problem-specific facet-defining cuts (cover cuts, clique cuts, MIR cuts) with Gomory cuts inside a Branch-and-Bound tree resolved numerical stalling and birthed modern MIP solvers.

### Worked example: Slicing Away a Fractional Corner in 2D

Suppose the LP polytope is $$P = \{x \in \mathbb{R}_{\ge 0}^2 : 2 x_1 + x_2 \le 3,\ x_1 + 2 x_2 \le 3\}$$, and we maximize $$x_1 + x_2$$ over $$S = P \cap \mathbb{Z}^2$$.

1. **Find the LP relaxation optimum:** Solving $$2x_1 + x_2 = 3$$ and $$x_1 + 2x_2 = 3$$ gives $$x_{\text{LP}} = (1, 1)$$? Wait: check $$2(1)+1 = 3$$ and $$1+2(1) = 3$$—that’s already integer! Let us tighten the RHS to $$2$$: $$P = \{x \ge 0 : 2x_1 + x_2 \le 2,\ x_1 + 2x_2 \le 2\}$$.
   - Now solving $$2x_1 + x_2 = 2$$ and $$x_1 + 2x_2 = 2$$ gives the fractional LP optimum $$x_{\text{LP}} = (2/3, 2/3)^\top$$ with objective $$4/3$$.
2. **Enumerate the true integer points $$S = P \cap \mathbb{Z}^2$$:**
   - $$(0, 0)$$, $$(1, 0)$$, and $$(0, 1)$$ are feasible; $$(1, 1)$$ gives $$2(1) + 1 = 3 > 2$$ (infeasible!).
3. **Construct the facet-defining cutting plane:** Summing the two constraints gives $$3x_1 + 3x_2 \le 4 \implies x_1 + x_2 \le 4/3$$. Rounding down for integer $$x_1 + x_2$$ gives the valid cut:
   $$x_1 + x_2 \le 1.$$
4. **Verify:** Every point in $$S = \{(0,0), (1,0), (0,1)\}$$ satisfies $$x_1 + x_2 \le 1$$, while $$x_{\text{LP}} = (2/3, 2/3)$$ violates it ($$4/3 > 1$$). Adding this single cut trims $$P$$ down to the exact convex hull $$\operatorname{conv}(S)$$!

The cutting plane method is an approach that changes an integer linear program to a convex problem and finds a solution. If this solution is not included in the original feasible set, it uses cuts to progressively guide the newly obtained solution to be included in the original feasible set by cutting out the region where the solution exists. Here, a cut is a line (or hyperplane) that cuts the feasible set, also called a cutting plane.

## Concept of cutting plane
Conceptually, it can be thought of as a method that draws a line between the original feasible set and the feasible set to cut out regions that are not part of the original feasible set, as shown in the figure below. 

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_cutting_plane_concept.png" alt="[Fig1] Cutting Plane">
  <figcaption style="text-align: center;">[Fig1] Cutting Plane</figcaption>
</p>
</figure>

* Red region: feasible set of the original integer linear program
* Blue region: feasible set of the convex relaxation problem
* Green line: cutting plane (the cutting plane exists between the blue and red regions)

The detailed algorithm will be introduced again in the main text.


## A bit of history on cutting planes
It took a very long time for the cutting plane method to develop from theory to a practical method. 

In 1954, Dantzig, Fulkerson, and Johnson first proposed the cutting plane method to solve the TSP (traveling salesman problem), and in 1958, mathematician Gomory proposed a general cutting plane method that could solve arbitrary integer linear programs. However, for about 30 years after that, Gomory cuts remained buried in an impractical state for solving real problems.

In 1990, Sebastian Ceria at CMU successfully implemented the cutting plane method using the branch and bound algorithm, which is called branch and cut. Since then, cutting planes have become a core component of commercial optimization solvers.