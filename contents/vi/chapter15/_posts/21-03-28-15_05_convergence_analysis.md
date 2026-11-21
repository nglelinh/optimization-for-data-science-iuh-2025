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

Giả sử bước centering trong phương pháp chắn được giải chính xác, ta thu được các kết quả hội tụ sau.

## Định lý hội tụ
Sau $$k$$ bước centering, **phương pháp chắn** thỏa mãn bất đẳng thức sau. (Ở đây $$k$$ là số vòng lặp ngoài.)
>$$\begin{align}
f(x^{(k)}) - f^{*} \le  \frac{m}{\mu^k t^{(0)}}
\end{align}$$

Nghĩa là, để đạt độ chính xác mong muốn $$\epsilon$$ bằng phương pháp chắn, bạn cần số bước centering sau đây, cộng thêm một bước centering đầu tiên.

>$$\begin{align}
\frac{log(m/(t^{(0)}\epsilon))}{\log \mu} + 1
\end{align}$$

Do đó, ta thấy sự hội tụ là tuyến tính, với $$O(\log 1/\epsilon )$$.

Phương pháp Newton hội tụ bậc hai với $$O(\log \log 1/\epsilon ) $$, nhưng trong trường hợp này bài toán rất khó, nên hội tụ tuyến tính không phải là kết quả tệ.

Định nghĩa về hội tụ tuyến tính và hội tụ bậc hai có thể xem trên Wiki.<br>
* Tham khảo: [Rate of convergence](https://en.wikipedia.org/wiki/Rate_of_convergence)
