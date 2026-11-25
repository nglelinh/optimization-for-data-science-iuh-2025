---
layout: post
title: 29 Distributed and federated optimization
chapter: '29'
order: 1
owner: Nguyen Le Linh
categories:
- chapter29
lang: en
lesson_type: required
---

Modern optimization rarely happens on a single machine anymore—either the dataset and model are too massive for one GPU (forcing **data-parallel distributed training** across thousands of accelerators connected by InfiniBand), or the data itself cannot legally leave millions of phones and hospitals (forcing **federated learning** over slow, unreliable wireless links). Chapter 29 unifies these worlds by contrasting synchronous data-parallel SGD, communication-saving Federated Averaging (FedAvg), and Chapter 21’s consensus ADMM—showing how communication bandwidth, synchronization barriers, and non-IID data heterogeneity reshape optimization from the ground up.

## Background Knowledge Map: Distributed & Federated Optimization Landscape

- **The Communication Bottleneck:** On a cluster or across mobile devices, transmitting a $$d$$-dimensional gradient or model update over a network often takes $$10\times$$–$$1000\times$$ longer than computing a local gradient—making *communication rounds*, not FLOPs, the dominant resource.
- **Synchronous Data-Parallel SGD:** Partitions a giant minibatch across $$P$$ workers, averages gradients via AllReduce, and produces an update mathematically *identical* to single-machine large-batch SGD—limited mainly by stragglers and the critical batch size.
- **Federated Learning & Local Steps (FedAvg):** Keeps raw data strictly on-device, lets each sampled client run $$E$$ local SGD steps before sending weight deltas to a central server, trading communication frequency for **client drift** when client distributions are non-IID.
- **Dual Consensus (ADMM) vs. Primal Averaging (FedAvg):** Consensus ADMM uses dual variables to eliminate client drift completely on convex problems, whereas modern federated methods (FedProx, SCAFFOLD, FedAdam) adapt proximal leashes, control variates, and server-side adaptivity to nonconvex deep networks.

### Step-by-Step Worked Example (Read Slowly): Communication Cost of Data-Parallel SGD vs. Local-Step FedAvg

Suppose $$P = 10$$ clients each hold local data, the model has $$d = 10^6$$ float32 parameters ($$4\text{ MB}$$ per model), and we want every client to execute $$T = 100$$ local gradient steps.

1. **Synchronous Data-Parallel SGD (sync every $$E = 1$$ step):**
   - Number of communication rounds: $$100$$.
   - Each client uploads + downloads $$4\text{ MB} \times 2 = 8\text{ MB}$$ per round.
   - Total network traffic per client: $$100 \times 8\text{ MB} = 800\text{ MB}$$ (and $$8\text{ GB}$$ aggregate across 10 clients).
2. **FedAvg with $$E = 10$$ local steps per round:**
   - Number of communication rounds: $$100 / 10 = 10$$ rounds.
   - Total network traffic per client: $$10 \times 8\text{ MB} = 80\text{ MB}$$—an immediate **10× reduction** in communication cost!
3. **The trade-off:** When all 10 clients have IID data, those 10 rounds behave almost like Data-Parallel SGD; when clients have strongly skewed non-IID data, the 10 local steps pull each client toward its own local optimum before averaging—creating the client drift we analyze in Lessons 29-02 and 29-04.

# Distributed and federated optimization

Chapter 21 (ADMM) is the course’s first *distributed convex* workhorse: split a structured objective, pass dual variables, and obtain consensus. Deep learning rarely looks like that. The 2026 default is **data-parallel SGD**: each worker owns a shard of the data, computes a minibatch gradient, and a server (or an all-reduce) averages the gradients (or the weights).

**Federated learning** is the same idea with a social constraint: raw data must not leave the device. **FedAvg** (McMahan et al., AISTATS 2017) lets each client run several local SGD steps and averages *parameters* once per round. Communication, not flops, is the scarce resource.

This chapter is an introduction. We will not treat Byzantine robustness or gradient compression in depth (USC CSCI 599 week-12 territory). We *will* make the ADMM contrast sharp enough that you never call FedAvg “just ADMM.”

## Lessons

1. Data-parallel SGD and all-reduce
2. FedAvg
3. ADMM vs data-parallel / federated methods
4. Modern federated applications (optional) — FedProx, SCAFFOLD, FedAdam, healthcare

Primary reading: McMahan et al., *Communication-Efficient Learning of Deep Networks from Decentralized Data*, [PMLR v54](https://proceedings.mlr.press/v54/mcmahan17a.html). Revisit Boyd et al., *Distributed Optimization and Statistical Learning via ADMM*. The 2020–2026 application layer is [29-04]({% multilang_post_url contents/chapter29/2026-09-16-29_04_modern_federated %}).
