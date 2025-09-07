---
layout: post
title: 06 Gradient Descent
chapter: '06'
order: 1
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

Trong chương này, chúng ta sẽ khám phá **Gradient Descent** (Thuật toán Gradient), một trong những phương pháp cơ bản và quan trọng nhất trong tối ưu hóa.

Trong các thuật toán tối ưu hóa, việc lựa chọn hướng tìm kiếm và kích thước bước là rất quan trọng đối với tốc độ hội tụ và sự thành công. Gradient descent di chuyển theo hướng của gradient âm. Kích thước bước có thể được cố định hoặc được chọn một cách thích ứng, và chúng ta sẽ thảo luận cả hai cách tiếp cận trong chương này.

Để gradient descent hội tụ, một số điều kiện tiên quyết phải được đáp ứng. Nếu những điều kiện này được thỏa mãn, chúng ta có thể phân tích gradient descent hội tụ nhanh như thế nào. Nếu tính lồi mạnh được thỏa mãn, sự hội tụ thậm chí còn nhanh hơn, và chúng ta sẽ xem xét tốc độ hội tụ trong những trường hợp như vậy.

Chúng ta cũng sẽ xem xét các ứng dụng của gradient descent, bao gồm gradient boosting và stochastic gradient descent.