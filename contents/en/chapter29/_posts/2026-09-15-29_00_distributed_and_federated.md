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
