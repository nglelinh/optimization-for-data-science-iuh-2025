---
layout: post
title: 29-01 Data-parallel SGD
chapter: '29'
order: 2
owner: Nguyen Le Linh
categories:
- chapter29
lang: en
lesson_type: required
---


Suppose we partition the $$n$$ examples across $$P$$ workers, worker $$p$$ holding index set $$\mathcal{I}_p$$. A synchronous **data-parallel** step is

$$
g_k = \frac{1}{P}\sum_{p=1}^P g_k^{(p)}, \qquad
g_k^{(p)} = \frac{1}{B}\sum_{i\in\mathcal{B}_{k,p}} \nabla f_i(w_k),
$$

then $$w_{k+1}=w_k-\eta g_k$$. If the union of the minibatches $$\mathcal{B}_{k,p}$$ is a uniform sample, this is ordinary minibatch SGD with batch size $$PB$$. The *systems* content is how $$g_k$$ is formed: a **parameter server** sums incoming gradients, or an **all-reduce** (ring, tree, NCCL) averages them without a single bottleneck node.

**What is not magic.** Data parallelism does not change the mathematics of SGD if every worker uses the *same* $$w_k$$. It changes wall-clock per step and the largest feasible batch. An all-reduce of a 100-million-parameter vector is a bandwidth problem; that is why people discuss compression (quantize, sparsify) as an optional next lecture.

**Asynchronous** variants (Hogwild!-style) apply stale gradients. They can be faster on shared memory and harder to analyse. For this course, implement the synchronous picture first.

```python
# Pedagogical sketch — not a real distributed runtime
def data_parallel_step(workers_grads, eta, w):
    g = sum(workers_grads) / len(workers_grads)
    return w - eta * g
```

Open [parallel_computing_illustration.html](https://nglelinh.github.io/interactive_math/optimization/parallel_computing_illustration.html) for a cartoon of splitting work, then come back and write the all-reduce of $$g$$ on the board.

**Exercise.** If each worker’s batch is of size $$B=32$$ and $$P=8$$, what is the equivalent single-node batch? If you linearly scale $$\eta$$ with $$P$$, what can go wrong (hint: Chapter 26 schedules and the large-batch breakdown)?
