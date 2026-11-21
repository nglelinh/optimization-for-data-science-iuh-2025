---
layout: post
title: 29-04 Modern federated applications
chapter: '29'
order: 5
owner: Nguyen Le Linh
categories:
- chapter29
lang: en
lesson_type: optional
---


Lessons 29-01 to 29-03 already own data-parallel SGD, **FedAvg**, and the ADMM contrast. This optional note is the 2020–2026 *application* layer: what to do when clients are non-IID (FedProx, SCAFFOLD), how adaptive server steps enter (FedOpt), and where the methods actually run (cross-silo healthcare). It does not re-derive the FedAvg three-step loop.

## 1. FedProx: a proximal leash on local drift

Li, Sahu, Zaheer, Sanjabi, Talwalkar, and Smith, *Federated Optimization in Heterogeneous Networks*, MLSys 2020, [proceedings.mlsys.org](https://proceedings.mlsys.org/paper_files/paper/2020/hash/1f5fe83998a09396ebe6477d9475ba0c-Abstract.html), replace the local objective $$F_c(w)$$ by

$$
F_c(w)+\frac{\mu}{2}\|w-w_t\|_2^2.
$$

That is a proximal term toward the broadcast global model — the same *idea* as an augmented-Lagrangian penalty, without a dual variable. FedProx is the first paper to read after FedAvg when client systems drop out and local data are non-IID. It is **not** ADMM (no dual ascent, no residual certificate); Chapter 29-03 already made that distinction. Use $$\mu>0$$ as a robustness knob, not as a proof that you have consensus.

## 2. SCAFFOLD: control variates for client drift

Karimireddy, Kale, Mohri, Reddi, Stich, and Suresh, *SCAFFOLD: Stochastic Controlled Averaging for Federated Learning*, ICML 2020, [PMLR v119](https://proceedings.mlr.press/v119/karimireddy20a.html), keep a *control variate* on the server and on each client so that local SGD is corrected by an estimate of the client-gradient bias $$(\nabla F_c-\nabla F)$$. Communication per round grows by one extra vector; the payoff is a rate that does not explode with the number of local steps $$E$$. If FedAvg is “hope the average of drifted models is fine,” SCAFFOLD is “subtract the estimated drift.” Variance-reduction students (26-05) will recognize the move.

## 3. FedOpt / FedAdam: the server is allowed to be Adam

Reddi, Charles, Zaheer, Garrett, Rush, Konečný, Kumar, and McMahan, *Adaptive Federated Optimization*, ICLR 2021, [OpenReview](https://openreview.net/forum?id=LkFG3lB13U5), treat the *pseudo-gradient* $$w_t-\bar w_{t+1}$$ (the averaged client delta) as an observation and apply Adam / Yogi / Adagrad **on the server**. Clients can stay on SGD; the adaptive preconditioner lives where memory is cheap. Combined with FedAvg-style local steps this is often called FedAdam. It is the Chapter 26 optimizer, lifted one level up the hierarchy — a useful exam question: *who* holds $$\hat m,\hat v$$?

## 4. Healthcare: the application that made FL mandatory

Cross-silo medical imaging and EHR prediction are why federated methods left the mobile-keyboard paper. Guan, Yap, Bozoki, and Liu, *Federated learning for medical image analysis: A survey*, *Pattern Recognition* 151:110424, 2024, [doi:10.1016/j.patcog.2024.110424](https://doi.org/10.1016/j.patcog.2024.110424), is the imaging map (tumour segmentation, chest X-rays, missing modalities). Nguyen et al., *Federated Learning for Smart Healthcare: A Survey*, *ACM Comput. Surv.* 55(3), 2022, and the 2025 CSBJ review (250+ papers, 2019–2024, [doi:10.1016/j.csbj.2025.06.009](https://doi.org/10.1016/j.csbj.2025.06.009)) catalogue system architecture, horizontal vs vertical partition, and which aggregator (FedAvg / FedProx / SCAFFOLD / FedAdam) deployments actually used. The optimization lesson is sober: FedAvg is still the default *implementation*; FedProx and SCAFFOLD are the default *answers* when a hospital’s class balance does not match another’s; formal privacy (DP-SGD, secure aggregation) is a different course, as 29-02 already warned.

| Method | Extra idea | Extra communication | When to try |
|--------|------------|---------------------|-------------|
| FedAvg (29-02) | average weights after $$E$$ local steps | one model / round | baseline, IID-ish |
| FedProx | proximal $$\mu$$ toward $$w_t$$ | same as FedAvg | dropouts, mild non-IID |
| SCAFFOLD | client/server control variates | $$+1$$ vector / client | strong client drift |
| FedAdam | Adam on the server pseudo-gradient | same as FedAvg (+ server state) | adaptive server, cheap clients |
| FedADMM (21-08) | dual residuals | same order | when you want a primal-dual certificate |

**Exercise.** Reuse the 3-client, one-class-each MNIST (or 2-D Gaussian) split from 29-02. Run $$E=5$$ local steps with (i) FedAvg, (ii) FedProx at two $$\mu$$, (iii) a *cartoon* SCAFFOLD that subtracts a running mean of each client’s gradient from the local step. Plot global test accuracy versus rounds, not versus local steps. Write four sentences on which method shrinks the oscillation you saw in 29-02.

## Sources

- H. B. McMahan et al., AISTATS 2017 — FedAvg (already required).
- T. Li et al., MLSys 2020 — FedProx.
- S. P. Karimireddy et al., ICML 2020 — SCAFFOLD.
- S. Reddi et al., ICLR 2021 — FedOpt / FedAdam.
- H. Guan et al., *Pattern Recognition* 151:110424, 2024 — medical imaging FL.
- D. C. Nguyen et al., *ACM Comput. Surv.* 55(3), 2022 — smart-healthcare FL.
- CSBJ 2025 survey, [doi:10.1016/j.csbj.2025.06.009](https://doi.org/10.1016/j.csbj.2025.06.009) — 2019–2024 system review.
