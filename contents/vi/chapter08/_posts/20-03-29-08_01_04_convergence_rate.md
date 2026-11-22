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

Tốc độ hội tụ mô tả số bước lặp cần thiết để đạt một điểm cận tối ưu với sai số $$\epsilon$$ theo độ lớn của $$\epsilon$$, biểu diễn qua [ký hiệu Big-O](https://en.wikipedia.org/wiki/Big_O_notation). Chẳng hạn, nếu $$\epsilon = 10^{-2}$$ và tốc độ hội tụ là $$O(1/\epsilon)$$, thuật toán cần khoảng $$1/10^{-2}=10^2$$ bước lặp.

Ta sử dụng [08-01-02 Bất đẳng thức cơ bản]({% multilang_post_url contents/chapter08/20-03-29-08_01_02_basic_inequality %}) để suy ra tốc độ hội tụ của phương pháp subgradient với kích thước bước cố định.

>$$Nhắc lại:$$
>\begin{align}
> f^{k}_{best} - f^{*} \quad \le \quad \frac{R^{2}}{2kt} + \frac{G^{2}t}{2}
\end{align}

Giả sử ta chọn $$t$$ và $$k$$ sao cho $$\frac{R^{2}}{2kt} \le \frac{\epsilon}{2}$$ và $$\frac{G^{2}t}{2} \le \frac{\epsilon}{2}$$ (trong đó $$\epsilon$$ là sai số cận tối ưu, $$G$$ là hằng số Lipschitz, và $$R$$ là khoảng cách từ điểm khởi tạo đến điểm tối ưu). Khi đó $$ \frac{R^{2}}{2kt} + \frac{G^{2}t}{2} \le \epsilon$$. Từ $$\frac{G^{2}t}{2} \le \frac{\epsilon}{2}$$ suy ra $$t \le \frac{\epsilon}{G^{2}}$$; kết hợp với $$\frac{R^{2}}{2kt} \le \frac{\epsilon}{2}$$ ta có $$k \ge \frac{R^2G^2}{\epsilon^2}$$. Như vậy, để bảo đảm $$f^{k}_{best} - f^{*} \le \epsilon$$, số bước lặp cần thiết có bậc $$\frac{R^2G^2}{\epsilon^2}$$.

Do đó, tốc độ hội tụ của phương pháp subgradient là $$O(1/\epsilon^2)$$, đòi hỏi nhiều bước lặp hơn đáng kể so với tốc độ $$O(1/\epsilon)$$ của gradient descent trên hàm trơn.