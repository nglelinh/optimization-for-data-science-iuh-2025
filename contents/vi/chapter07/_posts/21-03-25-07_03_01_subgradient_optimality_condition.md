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

Đối với bất kỳ hàm $$f$$ nào, điều kiện $$x^*$$ là một điểm cực tiểu của $$f$$ và điều kiện vector $$0$$ là một gradient dưới tại $$x^*$$ là tương đương:

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

Lưu ý rằng tính lồi của $$f$$ không được sử dụng trong chứng minh này, nên điều kiện tối ưu này áp dụng ngay cả cho các hàm không lồi.

