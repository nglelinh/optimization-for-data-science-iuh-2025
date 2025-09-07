---
layout: post
title: 07-02 Vi phân dưới (Sub-differentials)
chapter: '07'
order: 3
owner: Kyeongmin Woo
categories:
- chapter07
lang: vi
lesson_type: required
---

Vi phân dưới $$\partial f(x)$$ của một hàm lồi $$f$$ tại điểm $$x$$ là tập hợp tất cả các gradient dưới tại $$x$$:

>
\begin{equation}
\partial f(x) = \{g \in \mathbb{R}^n | \text{g là gradient dưới của f tại x} \}
\end{equation}

Vi phân dưới có các tính chất sau:

- $$\partial f(x)$$ luôn là một tập lồi đóng, bất kể $$f$$ có lồi hay không.
- Nếu $$f$$ lồi, $$\partial f(x)$$ luôn chứa ít nhất một phần tử; nếu $$f$$ không lồi, nó có thể rỗng.
- Nếu $$f$$ khả vi và lồi tại $$x$$, thì $$\partial f(x) = \{\nabla f(x)\}$$.
- Nếu $$\partial f(x) = \{g\}$$, thì $$f$$ khả vi tại $$x$$ và $$\nabla f(x) = g$$.

