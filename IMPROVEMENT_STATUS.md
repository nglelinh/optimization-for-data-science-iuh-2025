---
layout: default
title: Improvement status
permalink: /IMPROVEMENT_STATUS/
---

# Improvement-list status (2026-09-18)

Authoritative gap list: the attached sprint document *Optimization for Data Science (IUH) — Improvement list* (2026-09-15). There is **no** in-repo copy of that file; this page is the short done-versus-remaining note.

Numbering below matches the list’s “Gaps vs famous 2026 Opt-for-ML courses” table.

## Already on `main` before this pass (do not redo)

| # | Gap | Where it landed |
|---|-----|-----------------|
| 1 | SGD / minibatch / Adam / AdamW first-class | Ch.26 (`26-01`, `26-03`, `26-04`) |
| 2 | Autodiff lecture | Ch.27 |
| 3 | Thin / empty EN stubs (Simplex, key overviews) | Ch.05 Simplex + earlier stub fills |
| 4 | README pointing at upstream COFA | Rewritten README; Ch.00 in the contents table |
| 5 | Nonconvex DL landscapes | Ch.28 |
| 8 | Federated / data-parallel SGD | Ch.29 |
| 10 | CVXPY / DCP modeling lab | Ch.05 `05-07` |
| 14 | Mac folder hygiene | `AGENTS.md` |
| 15 | 2026 refresh + modern track | Ch.26–29 + optional CS/DS apps per chapter |

## Closed in this pass

| # | Gap | What changed |
|---|-----|----------------|
| 6 | Momentum / Nesterov pedagogy (P1) | Distill-style rewrite of **26-02** (EN+VI): valley, characteristic polynomial, $$\beta^\star$$, look-ahead vs heavy ball, NumPy, theory≠practice. Deepened the **09-05** stub into the FISTA / Distill picture (not a rewrite of 09-05-01). Pointers from 06-06 and the Ch.09 overview. |
| 7 | Variance reduction only stub-level (P1) | **26-05** upgraded from a one-page survey to a proper SVRG / SAGA lesson (control variate, outer/inner loops, SAGA table, linear-rate sketch, sklearn `saga`, code). Pointers from Ch.08 (`08-00`, `08-02-04`). |
| 9 | Demo linking completeness (P1) | Interactive-demo boxes added on landings **05, 07, 08** (EN+VI). **06, 09, 12, 14, 18, 26, 28, 29** already had boxes. `INTERACTIVE_DEMOS.md` “Where links appear” updated. |
| 11 | PL condition / modern rate story (P2) | New optional **28-05** (EN+VI). Pointers from Ch.06 landing, `06-00`, `06-03-04`, Ch.28 landing, `28-00`, `28-03`. |
| 12 | Bilevel / hypergrad intro (P2) | New optional **27-05** (EN+VI): nested HPO / MAML template, unrolling vs implicit hypergradient. Pointers from Ch.27 landing and `27-00`. |
| 13 | SAM / Muon / Sophia seminar (P2) | **26-06** upgraded from thin further-reading / one-paragraph-each to a short optional seminar (explicit SAM two-step, Sophia clip update, Muon Newton–Schulz). Does **not** duplicate the Sophia-as-Newton apps post `14-10`. |

## Still out of scope (list + sprint)

- Full rewrite of Chapters 00–25 theory.
- Conformal prediction as a core opt module; offline RL.
- New `interactive_math` HTML for Ch.15–17, 19–25 (none exists upstream).

## Hygiene

- No `_site/` committed.
- Bibliography stays under `reference/` (sidebar chapter 99).
- New 2026 lessons use the existing front matter (`layout`, `title`, `chapter`, `order`, `lang`, `categories`, `lesson_type`).
