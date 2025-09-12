---
layout: post
title: '08-01-04 Tốc độ hội tụ'
chapter: '08'
order: 6
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

Tốc độ hội tụ mô tả cách số lần lặp cần thiết để đạt đến một điểm $$\epsilon$$-dưới tối ưu phụ thuộc vào $$\epsilon$$, sử dụng [ký hiệu Big-O](https://en.wikipedia.org/wiki/Big_O_notation). Ví dụ, nếu $$\epsilon = 10^{-2}$$ và tốc độ hội tụ là $$O(1/\epsilon)$$, thì cần khoảng $$1/10^{-2}=10^2$$ lần lặp.

Hãy sử dụng [08-01-02 Bất đẳng thức cơ bản]({% multilang_post_url contents/chapter08/20-03-29-08_01_02_basic_inequality %}) để suy ra tốc độ hội tụ cho phương pháp subgradient với kích thước bước cố định.

>$$Nhắc lại:$$
>\begin{align}
> f^{k}_{best} - f^{*} \quad \le \quad \frac{R^{2}}{2kt} + \frac{G^{2}t}{2}
\end{align}

Giả sử $$\epsilon$$ thỏa mãn $$\frac{R^{2}}{2kt} \le \frac{\epsilon}{2}$$ và $$\frac{G^{2}t}{2} \le \frac{\epsilon}{2}$$ (trong đó $$\epsilon$$ là khoảng cách dưới tối ưu, $$G$$ là hằng số Lipschitz, và $$R$$ là khoảng cách giữa điểm khởi đầu và điểm tối ưu). Khi đó $$ \frac{R^{2}}{2kt} + \frac{G^{2}t}{2} \le \epsilon$$. Nếu $$\frac{G^{2}t}{2} \le \frac{\epsilon}{2}$$, thì $$t \le \frac{\epsilon}{G^{2}}$$, và $$\frac{R^{2}}{2kt} \le \frac{\epsilon}{2}$$ dẫn đến $$\frac{R^2G^2}{\epsilon^2} \le k$$. Điều này có nghĩa là số lần lặp cần thiết ít nhất là $$\frac{R^2G^2}{\epsilon^2}$$ để đạt được $$f^{k}_{best} - f^{*} \le \epsilon$$.

Tốc độ hội tụ của thuật toán này là $$O(1/\epsilon^2)$$, có nghĩa là nó cần nhiều lần lặp hơn đáng kể so với phương pháp gradient descent, có tốc độ $$O(1/\epsilon)$$.