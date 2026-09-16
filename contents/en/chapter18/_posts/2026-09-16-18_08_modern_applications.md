---
layout: post
title: 18-08 Modern applications of quasi-Newton methods (2022–2026)
chapter: '18'
order: 9
owner: Nguyen Le Linh
categories:
- chapter18
lang: en
lesson_type: optional
---

Quasi-Newton methods replace $$\nabla^2 f(x)$$ by a matrix $$B$$ that obeys the secant equation $$B^{+}s = y$$ and (for BFGS/L-BFGS) stays positive definite under the curvature condition $$y^\top s > 0$$. The 2022–2026 applications that still *look like this chapter* are not the LLM pre-trainers that estimate a diagonal Hessian (those belong with Newton / Sophia in Chapter 14). They are the codes that keep a short history of $$(s,y)$$ pairs — L-BFGS in scientific machine learning and in classical tabular models — and the structured preconditioners (Shampoo / SOAP) that are BFGS's Kronecker cousins.

## PINNs: Adam to get close, L-BFGS to finish

Physics-informed neural networks minimise a residual that contains differential operators. Those operators make the loss ill-conditioned: the Hessian's eigenvalue range tracks the spectrum of a discretised PDE, not the spectrum of a cross-entropy. Rathore, Lei, Frangella, Lu, and Udell (ICML 2024) compare Adam, L-BFGS, and **Adam+L-BFGS**, show that the combination dominates either method alone, and introduce NysNewton-CG as a further second-order refinement. The paper's theoretical contribution is the link between ill-conditioned differential operators and an ill-conditioned PINN Hessian — which is exactly why a secant method, which accumulates curvature along the trajectory, outperforms a diagonal adaptive method that never sees off-diagonal residual couplings.

The training recipe that papers actually ship is older than 2024 and still standard in 2026: run Adam until the residual is in a quadratic bowl, then switch to L-BFGS with a Wolfe line search. Urbán, Stefanou, Pons, et al. (2024, [arXiv:2405.04230](https://arxiv.org/abs/2405.04230)) state the same split and measure how much accuracy BFGS / L-BFGS add after the Adam prelude. This is Chapter 18 in a lab notebook: the two-loop recursion of 18-07, not a new optimiser.

## Self-scaled BFGS on PINNs, PIKANs, and DeepONets

Kiyani, Shukla, Urbán, Darbon, and Karniadakis (2025, [arXiv:2501.16371](https://arxiv.org/abs/2501.16371)) revisit the Broyden class you studied in 18-05. **Self-scaled BFGS** and **self-scaled Broyden** rescale the Hessian approximation using the most recent curvature pair, which is a classical safeguard (Oren–Luenberger) against the wild step-length variation of PDE residuals. On Burgers, Allen–Cahn, Kuramoto–Sivashinsky, and Ginzburg–Landau, and on physics-informed Kolmogorov–Arnold networks, they report orders-of-magnitude residual improvements *without* the adaptive loss weights that PINN papers usually need. The same updates help DeepONet training.

Read this as a live Broyden-class experiment: $$\phi=0$$ is BFGS, $$\phi=1$$ is DFP, and a self-scaled member is a data-dependent $$\phi$$ plus a scalar prefactor. The curvature condition $$y^\top s>0$$ is enforced by the line search; when it fails, the pair is skipped — the same skip that L-BFGS implementations have always used.

## L-BFGS-B as the quiet default in tabular ML

scikit-learn's `LogisticRegression(solver="lbfgs")` and its GLM family (`solver="lbfgs"`, the default next to `newton-cholesky`) call SciPy's **L-BFGS-B**: limited-memory BFGS with bound constraints. For $$n$$ in the tens of thousands and $$d$$ in the hundreds to low thousands, this is still the correct algorithm — cheaper than forming a Hessian, more accurate than SGD on a convex GLM, and warm-startable along a regularisation path. Hugging Face Trainer exposes `optim="lbfgs"` for the rare fine-tune that is small enough; the important cultural fact is the opposite of the Sophia story: *when the model fits in a CPU Hessian sketch of a few dozen vectors, quasi-Newton beats Adam*.

A five-line check:

```python
from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(solver="lbfgs", max_iter=200, C=1.0)
clf.fit(X, y)
print(clf.n_iter_)
```

Compare with `solver="newton-cholesky"` (Chapter 14) on a tall design and with `solver="saga"` on a wide one. You are choosing among Newton, L-BFGS, and a variance-reduced first-order method using only the dimensions $$n,d$$ and the constraint type.

## SOAP: Shampoo's eigenbasis as a structured quasi-Newton

Vyas, Morwani, Zhao, Kwun, Shapira, Brandfonbrener, Janson, and Kakade (ICLR 2025) introduce **SOAP** (*ShampoO with Adam in the Preconditioner's eigenbasis*). Shampoo (Gupta, Koren, Singer, 2018; the 2023–2024 large-scale revivals) maintains Kronecker-factored second-moment matrices and is a structured quasi-Newton / natural-gradient hybrid. SOAP proves that Shampoo with the square-root inverse is Adafactor run in Shampoo's eigenbasis, then *replaces* Adafactor by AdamW in that slowly moving basis. On 360M and 660M language models, in the large-batch regime, SOAP cuts iteration count by more than 40% and wall-clock by more than 35% versus AdamW, and by about 20% versus Shampoo.

This is not L-BFGS — there is no $$(s,y)$$ pair — but it is the same design thesis as DFP/BFGS: *estimate a positive-definite curvature, invert it cheaply, refresh it on a slower schedule than the gradient.* The extra hyperparameter is the eigendecomposition frequency, analogous to L-BFGS memory $$m$$. Place SOAP next to K-FAC (Chapter 14) in a seminar; place L-BFGS next to PINNs in a lab.

## Sources

- P. Rathore, W. Lei, Z. Frangella, L. Lu, M. Udell, “Challenges in Training PINNs: A Loss Landscape Perspective,” ICML 2024, PMLR 235.
- W. Urbán et al., “Unveiling the optimization process of Physics Informed Neural Networks,” 2024. [arXiv:2405.04230](https://arxiv.org/abs/2405.04230)
- E. Kiyani, K. Shukla, J. F. Urbán, J. Darbon, G. E. Karniadakis, “Optimizing the Optimizer for Physics-Informed Neural Networks and Kolmogorov-Arnold Networks,” 2025. [arXiv:2501.16371](https://arxiv.org/abs/2501.16371)
- N. Vyas et al., “SOAP: Improving and Stabilizing Shampoo using Adam,” ICLR 2025. [arXiv:2409.11321](https://arxiv.org/abs/2409.11321)
- SciPy `L-BFGS-B`; scikit-learn `LogisticRegression(solver="lbfgs")`.
