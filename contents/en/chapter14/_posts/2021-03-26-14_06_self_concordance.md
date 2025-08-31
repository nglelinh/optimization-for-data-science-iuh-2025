---
layout: post
title: 14-06 Self concordance
chapter: "14"
order: 10
owner: "Minjoo Lee"
---
In the previous convergence analysis of Newton's method, there are two major issues. [1]

First, in practical problems, it is difficult to find the Lipschitz constant L, the lower and upper bounds of strong convexity m, M, etc., which are included in the formulas. Because of this, while we can observe convergence and convergence rate, it is almost impossible to analyze how many Newton steps are needed in practice.

Second, although Newton's method itself is affine invariant, the convergence analysis of Newton's method is not affine invariant. For general functions, the values of the Lipschitz constant or strong convexity bounds change depending on the coordinate transformation.

Therefore, in this chapter, we introduce self-concordant functions, which address the above two issues.

Self-concordant functions are important and meaningful for three main reasons:

1. The log barrier functions used in interior-point methods are self-concordant functions.
2. In the analysis of Newton's method for self-concordant functions, terms involving constants do not appear.
3. Self-concordance is affine-invariant. That is, the number of Newton iterations required is independent of affine transformations of the coordinate system.