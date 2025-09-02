---
layout: post
title: 00.03 Real Analysis And Set Theory
chapter: '00'
order: 4
owner: GitHub Copilot
lang: vi
categories:
- chapter00
---

**Các khái niệm chính:**

- Tập hợp, tập con $$A \subseteq B$$, hợp $$(A \cup B)$$, giao $$(A \cap B)$$
- Hàm số, miền xác định, tập giá trị
- Bất đẳng thức ($$\le$$, $$\ge$$, <, >)
- Tô-pô cơ bản của $$\mathbb{R}^n$$: tập mở, tập đóng, biên, nội
- Dãy số và giới hạn $$(\lim_{n \to \infty} x_n = L)$$
- Tính liên tục của hàm số

---
Một **tập mở** là khái niệm cơ bản trong tô-pô và giải tích, đặc trưng bởi tính chất **không chứa bất kỳ điểm biên nào của nó**.

Một tập $$S$$ trong $$\mathbb{R}^n$$ là **mở** nếu với mọi điểm $$x \in S$$, tồn tại một số thực dương $$\epsilon > 0$$ sao cho quả cầu mở $$B(x_{0}, \epsilon) = \{y \in X \mid d(x_{0}, y) < \epsilon\}$$ hoàn toàn nằm trong $$S$$.

Điều này có nghĩa là mỗi điểm trong tập mở đều được bao quanh bởi một "vùng đệm nhỏ" cũng thuộc tập đó. Ví dụ, trong $$\mathbb{R}^n$$, khoảng $$(a, b)$$ là tập mở vì với bất kỳ $$x \in (a, b)$$, ta có thể tìm được $$\epsilon$$ (ví dụ $$\epsilon = \min(x-a, b-x)$$) sao cho $$(x-\epsilon, x+\epsilon) \subset (a, b)$$.

<!-- Hình ảnh minh họa tập mở sẽ được thêm vào sau -->

---

Ngược lại, một **tập đóng** được định nghĩa là tập chứa tất cả các điểm biên của nó. Tương đương, trong **không gian tô-pô**, một tập $$S$$ là đóng nếu phần bù của nó $$\mathbb{R}^n \setminus S$$ là một **tập mở**.

Một đặc điểm quan trọng khác trong **không gian metric** là tập đóng chứa tất cả các điểm giới hạn của nó; nghĩa là, nếu một dãy điểm $$(x_n)$$ từ $$S$$ hội tụ về một điểm $$x$$, thì $$x$$ cũng phải thuộc $$S$$.

Ví dụ, khoảng đóng $$[a, b]$$ trong $$\mathbb{R}$$ là tập đóng, vì phần bù của nó $$(-\infty, a) \cup (b, \infty)$$ là tập mở, và bất kỳ dãy hội tụ nào trong $$[a,b]$$ đều có giới hạn nằm trong $$[a,b]$$.

---

**Biên** của một tập $$S$$, ký hiệu $$\partial S$$, bao gồm các điểm "nằm trên ranh giới" của tập. Một điểm $$x$$ là **điểm biên** của $$S$$ nếu mọi quả cầu mở tâm $$x$$ đều giao với cả $$S$$ và phần bù của nó $$S^c$$.

Một cách chính xác, $$\partial S = \bar{S} \setminus S^\circ$$, trong đó $$\bar{S}$$ là bao đóng của $$S$$ (tập đóng nhỏ nhất chứa $$S$$) và $$S^\circ$$ là nội của $$S$$.


---

A **compact set**(**tập hợp compact**) - in Euclidean spaces ($$\mathbb{R}^n$$), a set is compact if and only if it is both **closed and bounded**. 

Heine-Borel Theorem: A set is "bounded" if it can be contained within some sufficiently large open ball (i.e., $$\exists M > 0$$ such that $$S \subset B(0, M)$$). 

However, the more general and fundamental definition of compactness in a topological space is that every open cover of the set has a finite subcover. That is, if $$S \subset \bigcup_{\alpha \in A} U_\alpha$$ where each $$U_\alpha$$ is open, then there exists a finite subset $$F \subset A$$ such that $$S \subset \bigcup_{\alpha \in F} U_\alpha$$. This property is incredibly powerful, ensuring the existence of extrema for continuous functions (Extreme Value Theorem) and playing a vital role in many existence proofs.