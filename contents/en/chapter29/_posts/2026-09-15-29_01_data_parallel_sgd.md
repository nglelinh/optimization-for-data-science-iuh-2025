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

Scale a training job from 1 GPU to 64 GPUs using synchronous **Data-Parallel SGD**, and something remarkably clean happens: if every worker computes a local minibatch gradient of size $$b$$ and averages them via an AllReduce collective, the resulting parameter update is mathematically *indistinguishable* from running single-GPU SGD with global batch size $$B = P \cdot b$$. The real engineering and optimization subtleties lie in what happens as $$P$$ grows huge: variance shrinks by $$1/P$$, learning rates must scale carefully, and eventually you hit the critical batch size where adding more GPUs yields diminishing returns.

## Background Knowledge Map: Mathematics and Scaling Laws of Data-Parallel SGD

- **Exact Equivalence to Large-Batch SGD:** With $$P$$ workers each drawing $$b$$ i.i.d. samples, the averaged gradient $$g_k = \frac{1}{P}\sum_{p=1}^P g_k^{(p)}$$ is unbiased for $$\nabla F(w_k)$$ with variance $$\frac{\sigma^2}{Pb}$$—identical to a single worker with batch size $$B = Pb$$.
- **Ring AllReduce Bandwidth Scaling:** Instead of funneling all $$P$$ gradients through one bottleneck parameter server ($$O(Pd)$$ traffic at the server), Ring AllReduce passes chunks around a logical ring so every worker sends and receives only $$2\frac{P-1}{P}d \approx 2d$$ bytes—independent of $$P$$!
- **Linear Scaling Rule & Warmup:** When multiplying global batch size by $$P$$, multiplying the learning rate by $$P$$ (or $$\sqrt{P}$$ under Adam) keeps the noise-to-signal ratio balanced, paired with gradual warmup during early unstable epochs.
- **Synchronous Stragglers vs. Asynchronous Stale Gradients:** Synchronous AllReduce waits for the slowest worker each step; asynchronous SGD eliminates straggler waits but injects delayed ("stale") gradients $$\nabla f(w_{k-\tau})$$, which degrade convergence unless delay $$\tau$$ is tightly bounded.

### Step-by-Step Worked Example (Read Slowly): Computing Global Variance Reduction and Ring AllReduce Traffic

Suppose a single GPU trains with batch size $$b = 32$$, per-sample gradient variance $$\sigma^2 = 64$$, and model size $$d = 25\text{M}$$ float32 weights ($$100\text{ MB}$$). We scale synchronously to $$P = 8$$ GPUs.

1. **Single-GPU gradient variance:**
   $$\operatorname{Var}(g_{\text{1 GPU}}) = \frac{\sigma^2}{b} = \frac{64}{32} = 2.0.$$
2. **8-GPU synchronous data-parallel variance (global batch $$B = 8 \times 32 = 256$$):**
   $$\operatorname{Var}(g_{\text{8 GPUs}}) = \frac{\sigma^2}{P b} = \frac{64}{256} = 0.25$$ (an exact **8× variance reduction**!).
3. **Compare communication volume per step (Parameter Server vs. Ring AllReduce):**
   - **Central Parameter Server:** The server must receive $$8 \times 100\text{ MB} = 800\text{ MB}$$ and broadcast $$800\text{ MB}$$ = **1,600 MB** through one link!
   - **Ring AllReduce:** Each GPU sends $$2\frac{P-1}{P}(100\text{ MB}) = 2 \cdot \frac{7}{8}(100\text{ MB}) = 175\text{ MB}$$—nearly **10× less** bottleneck bandwidth, and capped below $$200\text{ MB}$$ even if you scale to $$P = 1024$$ GPUs!

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
