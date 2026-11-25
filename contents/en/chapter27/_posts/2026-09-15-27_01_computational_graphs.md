---
layout: post
title: 27-01 Computational graphs
chapter: '27'
order: 2
owner: Nguyen Le Linh
categories:
- chapter27
lang: en
lesson_type: required
---

Before an autodiff engine can compute a single derivative, it must first see your program not as lines of Python, but as a **computational graph**—a Directed Acyclic Graph (DAG) where every node is an intermediate tensor and every edge represents an elementary operation with a known local derivative. The moment a computation becomes a DAG, the multivariable chain rule turns into a pure graph-traversal algorithm: total derivatives are simply the sum of products of edge weights along every directed path from an input to an output!

## Key ideas: Graph Structure, Fan-Out, and Memory Trade-Offs

- **Nodes, Edges, and Topological Order:** Inputs sit at source nodes, intermediate variables $$v_1, \dots, v_K$$ are evaluated in topological order so every parent is computed before its children, and the scalar loss $$\ell$$ sits at the sink.
- **Multivariable Chain Rule as Path Summation:** If node $$x$$ influences output $$\ell$$ along multiple branches (fan-out), the total derivative $$\frac{\partial \ell}{\partial x}$$ is the **sum** of contributions across all outgoing edges: $$\sum_{c \in \text{children}(x)} \frac{\partial \ell}{\partial c}\frac{\partial c}{\partial x}$$.
- **Static vs. Dynamic Graphs (Define-and-Run vs. Define-by-Run):** Dynamic tape graphs (PyTorch eager mode) record operations on the fly—supporting native Python `if`/`for` control flow—while traced/compiled graphs (JAX `jit`, `torch.compile`) enable global kernel fusion and memory planning.
- **Activation Checkpointing:** Because reverse-mode AD needs intermediate forward values to evaluate local derivatives, memory scales with graph depth. Checkpointing discards selected intermediates and recomputes them during the backward pass, trading extra compute for $$O(\sqrt{L})$$ memory.

### Worked example: Unrolling a Fan-Out Function Into a DAG and Summing Paths

Consider $$f(x_1, x_2) = x_1 x_2 + \sin(x_1)$$ at $$(x_1, x_2) = (0, 3)$$. Notice $$x_1$$ fans out into **two** branches!

1. **Build the topological DAG evaluation trace:**
   - $$v_1 = x_1 = 0$$, $$v_2 = x_2 = 3$$.
   - $$v_3 = v_1 \cdot v_2 = 0 \cdot 3 = 0$$ (local partials: $$\frac{\partial v_3}{\partial v_1} = v_2 = 3$$, $$\frac{\partial v_3}{\partial v_2} = v_1 = 0$$).
   - $$v_4 = \sin(v_1) = \sin(0) = 0$$ (local partial: $$\frac{\partial v_4}{\partial v_1} = \cos(0) = 1$$).
   - $$v_5 = v_3 + v_4 = 0$$ (local partials: $$\frac{\partial v_5}{\partial v_3} = 1$$, $$\frac{\partial v_5}{\partial v_4} = 1$$).
2. **Compute $$\frac{\partial v_5}{\partial x_1}$$ by summing over all directed paths from $$v_1$$ to $$v_5$$:**
   - Path 1 ($$v_1 \to v_3 \to v_5$$): $$\frac{\partial v_5}{\partial v_3}\cdot\frac{\partial v_3}{\partial v_1} = 1 \cdot 3 = 3$$.
   - Path 2 ($$v_1 \to v_4 \to v_5$$): $$\frac{\partial v_5}{\partial v_4}\cdot\frac{\partial v_4}{\partial v_1} = 1 \cdot 1 = 1$$.
   - Sum of paths: $$\frac{\partial v_5}{\partial x_1} = 3 + 1 = 4$$!
3. **Verify analytically:** $$\frac{\partial}{\partial x_1}(x_1 x_2 + \sin x_1) = x_2 + \cos(x_1) = 3 + 1 = 4$$. Exact match!

A **computational graph** is a directed acyclic graph whose nodes are values and whose edges record elementary maps ($$+$$, $$\times$$, $$\exp$$, `matmul`, …). Parameters, inputs, and the scalar loss are just distinguished nodes.

Example. Logistic loss on one example with weights $$w\in\mathbb{R}^2$$:

$$
z = w_1 x_1 + w_2 x_2, \quad p=\sigma(z), \quad \ell = -y\log p -(1-y)\log(1-p).
$$

Nodes: $$x$$, $$w$$, $$z$$, $$p$$, $$\ell$$. The graph *is* the program. Changing a weight changes every downstream node; AD’s job is to push that sensitivity to $$\ell$$ or to pull the sensitivity of $$\ell$$ backward.

Two implementation styles:

- **Wengert tape / define-by-run** (PyTorch): the graph is recorded while the Python `forward` executes. Control flow is ordinary Python.
- **Define-then-run** (historical Theano, JAX `jit` traces): you first build or trace a static graph, then execute it many times.

For this course the distinction matters only so that you know why `y.backward()` needs a graph that still exists — calling `backward` twice without `retain_graph` frees the tape.

**Exercise.** Draw the graph for $$\ell=\|W_2\,\phi(W_1 x)-y\|_2^2$$ with one hidden layer. Count multiplies on the forward pass. That count will reappear as the cost of reverse mode.
