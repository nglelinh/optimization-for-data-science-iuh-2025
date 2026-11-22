---
layout: post
title: '15-05 Phân tích hội tụ'
chapter: "15"
order: 11
categories:
- chapter16
owner: "Minjoo Lee"
lang: vi
---

Giả sử mỗi bước định tâm (centering step) trong phương pháp chắn được giải chính xác, ta thu được kết quả hội tụ sau.

## Định lý hội tụ
Sau $$k$$ bước định tâm (vòng lặp ngoài), **phương pháp chắn** thỏa mãn bất đẳng thức:
>$$
>\begin{align}
>f(x^{(k)}) - f^{*} \le  \frac{m}{\mu^k t^{(0)}}
>\end{align}
>$$

Nghĩa là để đạt độ chính xác $$\epsilon$$, tổng số bước định tâm cần thiết (bao gồm bước định tâm đầu tiên) là:

>$$
>\begin{align}
>\frac{\log(m/(t^{(0)}\epsilon))}{\log \mu} + 1
>\end{align}
>$$

Như vậy, số vòng lặp ngoài có bậc độ phức tạp $$O(\log(1/\epsilon))$$, tương ứng tốc độ hội tụ tuyến tính.

So với tốc độ hội tụ bậc hai $$O(\log \log(1/\epsilon))$$ của phương pháp Newton không ràng buộc, hội tụ tuyến tính vẫn là kết quả tốt đối với lớp bài toán có ràng buộc bất đẳng thức vốn khó hơn nhiều.

Định nghĩa chi tiết về hội tụ tuyến tính và hội tụ bậc hai có thể tham khảo thêm trên Wikipedia:<br>
* Tham khảo: [Rate of convergence](https://en.wikipedia.org/wiki/Rate_of_convergence)
