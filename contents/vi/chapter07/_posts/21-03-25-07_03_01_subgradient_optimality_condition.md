---
layout: post
title: 07-03-01 Điều kiện tối ưu gradient dưới
chapter: '07'
order: 7
owner: Kyeongmin Woo
categories:
- chapter07
lang: vi
lesson_type: required
---

### Bổ đề

Với bất kỳ hàm $$f$$ nào, điều kiện $$x^*$$ là điểm cực tiểu toàn cục của $$f$$ tương đương với việc vector $$0$$ là một gradient dưới của $$f$$ tại $$x^*$$:

> $$
\begin{equation}
f(x^*) = \min_x f(x) \Longleftrightarrow 0 \in \partial f(x^*)
\end{equation}
$$

### Chứng minh
>
$$
\begin{align}
&f(x^*) = \min_x f(x)\\
\Longleftrightarrow &f(y) \geq f(x^*) \text{ với mọi } y\\
\Longleftrightarrow &f(y) \geq f(x^*) + 0^T(y-x^*)\\
\Longleftrightarrow &0 \in \partial f(x^*)
\end{align}
$$

Lưu ý rằng chứng minh trên không sử dụng giả thiết lồi của $$f$$, vì vậy điều kiện tối ưu này đúng ngay cả với các hàm không lồi.
