---
layout: post
title: 06-03-06 Can we do better?
chapter: '06'
order: 15
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

Gradient descent đạt tốc độ hội tụ $$O(1/k)$$ (tương ứng cần $$O(1/\epsilon)$$ vòng lặp để đạt sai số $$\epsilon$$) đối với các hàm lồi, khả vi và có gradient liên tục Lipschitz. Câu hỏi đặt ra là liệu có phương pháp bậc nhất nào đạt tốc độ hội tụ nhanh hơn gradient descent hay không.

### Phương pháp Bậc nhất

Một phương pháp bậc nhất tạo ra điểm lặp $$x^{(k)}$$ sao cho $$x^{(k)}$$ nằm trong không gian tuyến tính sinh bởi các gradient đã tính từ điểm khởi tạo $$x^{(0)}$$ đến $$x^{(k-1)}$$:

> $$x^{(k)} \in x^{(0)} + $$ **span**$$\{\nabla f(x^{(0)}),\nabla f(x^{(1)}),...,\nabla f(x^{(k-1)})\}$$

### Định lý Nesterov

Định lý của Nesterov thiết lập một cận dưới cho tốc độ hội tụ tốt nhất có thể của mọi phương pháp bậc nhất.

> **Định lý Nesterov**: Với mọi $$k \le (n-1)/2$$ và mọi điểm xuất phát $$x^{(0)}$$, tồn tại một hàm lồi trơn $$f$$ có gradient $$L$$-Lipschitz sao cho mọi phương pháp bậc nhất đều thỏa mãn (với $$n$$ là số chiều):<br>
\begin{align}
f(x^{(k)}) - f^{\star} \ge \frac{3L \lVert x^{(0)} - x^{\star} \rVert_2^2}{32(k + 1)^2}
\end{align}

Vì cận dưới trong định lý Nesterov có $$k^2$$ ở mẫu số, tốc độ hội tụ tối ưu về mặt lý thuyết của lớp phương pháp bậc nhất là $$O(1/k^2)$$, tương ứng chỉ cần $$O(1/\sqrt{\epsilon})$$ vòng lặp. Các thuật toán tăng tốc đạt được cận này sẽ được trình bày chi tiết hơn ở các phần sau.
