---
layout: post
title: 10 Duality in Linear Programs
chapter: '10'
order: 1
owner: Wontak Ryu
categories:
- chapter10
lang: en
---

Suppose a logistics team hands you a shipping schedule costing $4.2 million and claims it is the absolute cheapest plan possible. How could they *prove* to a skeptical CFO that no hidden route combination in a billion-variable network could shave off even $1? Checking every feasible plan is impossible, yet **Linear Programming (LP) duality** provides an astonishingly compact certificate: a set of nonnegative resource "shadow prices" whose weighted sum of constraints produces a mathematical lower bound equal to $4.2 million. Chapter 10 unpacks this primal–dual mirror world—from elementary lower bounds to max-flow/min-cut and von Neumann's minimax theorem.

## Key ideas: The Architecture of LP Duality

- **Pillar 1 — Primal Plans vs. Dual Certificates:** Every minimization LP (the *primal*) seeks the lowest-cost feasible decision $$x$$; its companion maximization LP (the *dual*) combines the primal constraints with multipliers $$(u, v)$$ to build the tightest possible lower bound $$B \le c^\top x$$.
- **Pillar 2 — Weak vs. Strong Duality:** Weak duality ($$d^\star \le p^\star$$) holds universally by construction of valid constraint combinations. For feasible, bounded LPs, **strong duality** ($$d^\star = p^\star$$) closes the gap completely, guaranteeing that an exact optimality certificate always exists.
- **Pillar 3 — Combinatorial & Game-Theoretic Dual Pairs:** LP duality unifies crown jewels across mathematics and computer science: the dual of maximum network flow is the minimum $$s\text{–}t$$ cut, and the dual of one player's minimax strategy in a zero-sum matrix game is the opponent's maximin strategy.
- **Pillar 4 — Perfect Symmetry (Involution):** Taking the dual of the dual LP recovers the original primal LP verbatim—meaning neither problem is inherently "primary"; they are two equivalent views of the same polyhedral geometry.

### Worked example: Certifying Optimality of a 2-Variable LP in Three Lines

Consider the primal LP: minimize $$x_1 + 2x_2$$ subject to $$x_1 + x_2 \ge 3$$, $$x_1 \ge 1$$, and $$x_2 \ge 0$$.

1. **Test a candidate primal solution:** Try $$x^\star = (3, 0)^\top$$.
   - Check feasibility: $$3 + 0 = 3 \ge 3$$, $$3 \ge 1$$, $$0 \ge 0$$ (all satisfied!).
   - Primal objective value: $$p = 1(3) + 2(0) = 3$$.
2. **Construct a lower bound directly from the constraints:**
   Notice that since $$x_2 \ge 0$$, adding $$1 \cdot (x_1 + x_2 \ge 3)$$ and $$1 \cdot (x_2 \ge 0)$$ gives:
   $$x_1 + 2x_2 = (x_1 + x_2) + x_2 \ge 3 + 0 = 3.$$
3. **Read off the certificate:** For *every* feasible $$(x_1, x_2)$$, the objective is at least $$3$$ (weak duality), and $$x^\star = (3, 0)^\top$$ achieves $$3$$ (strong duality). That single nonnegative combination of constraints proves global optimality without inspecting any other point in the feasible region!

Starting from this chapter, we will examine duality, which plays a significant role in optimization theory.
From an optimization perspective, duality can be simply described as the concept that a single optimization problem can be viewed from two perspectives: the primal problem and the dual problem.

In this chapter, we specifically explore duality in linear programs.
Rather than directly applying it to general convex problems, we will derive the dual problem from the primal problem by applying it to linear programs, and organize how the relationship between these two problems is established and what properties they have under specific conditions.

## Modern applications (2022–2026)

An optional companion lesson reads the same LP dual as a certificate in neural-network verification (α,β-CROWN), electricity LMPs, max-flow cuts, and Kantorovich optimal transport. See [10-07 Modern applications of LP duality]({% multilang_post_url contents/chapter10/2026-09-16-10_07_modern_applications %}). 
