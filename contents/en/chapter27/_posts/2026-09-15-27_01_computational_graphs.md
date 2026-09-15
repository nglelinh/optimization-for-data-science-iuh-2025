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
