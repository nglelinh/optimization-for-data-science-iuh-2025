---
layout: post
title: '15-04 Phương pháp chắn v.0 và v.1'
chapter: "15"
order: 10
owner: "Minjoo Lee"
categories:
- chapter16
lang: vi
---

## Phương pháp chắn v.0
**Phương pháp chắn v.0** chọn $$t = m/\epsilon$$ với $$\epsilon > 0$$ và giải bài toán chắn sau để thu được $$f(x^*(t)) - f(x^*) \le \epsilon $$.
>
$$\begin{align}
 &\min_{x} \ && tf(x) + \phi(x) \\
 &\text{subject to } \ && Ax = b \\
\end{align}$$

Ở đây, $$m$$ là số ràng buộc và $$t$$ là một bội của $$1/\epsilon$$, nên khi $$\epsilon$$ càng nhỏ thì $$t$$ càng rất lớn, và cuối cùng ta đến cuối đường trung tâm, khiến bài toán tương đương với bài toán ban đầu. Do đó, cách này có thể rất chậm và khó giải.

Vì vậy, một cách tiếp cận tốt hơn là đi theo đường trung tâm để tìm nghiệm, dẫn đến định nghĩa **phương pháp chắn v.1**.

## Phương pháp chắn v.1
**Phương pháp chắn v.1** là phương pháp tăng dần giá trị $$t$$ và giải bài toán chắn sau nhiều lần.
>
$$\begin{align}
 &\min_{x} \ && tf(x) + \phi(x) \\
 &\text{subject to } \ && Ax = b \\
\end{align}$$

### Thuật toán
Thuật toán có thể được mô tả như sau.

1. Chọn $$t^{(0)} > 0$$ và đặt $$k := 0$$.
2. Tại $$t = t^{(0)}$$, giải bài toán chắn để thu được $$x^{(0)} = x^*(t)$$.
3. Trong khi $$m/t > \epsilon$$ <br>
  3-1. Chọn $$t^{(k+1)} > t^{(k)}$$. <br>
  3-2. Khởi tạo phương pháp Newton với $$x^{(k)}$$. (khởi động ấm, warm start)<br>
        Tại $$t = t^{(k+1)}$$, giải bài toán chắn để thu được $$x^{(k+1)} = x^*(t)$$.<br>
  kết thúc vòng lặp<br>

### Nhận xét
* **Cách cập nhật thường dùng**: $$t^{(k+1)} = \mu t^{(k)}$$, ($$\mu > 1$$)
* **Khởi động ấm (warm start)**: Ở bước 3-2, nghiệm của bước trước được dùng làm giá trị khởi tạo cho bước sau, cách này gọi là warm start.
* **Bước centering**: Các bước 2 và 3-2 của thuật toán, tức là giải bài toán chắn, được gọi là các bước centering (hay vòng lặp ngoài).

### Những điều cần cân nhắc
Khi chọn $$\mu$$ và $$t^{(0)}$$, cần cân nhắc các đánh đổi sau.
##### Chọn $$\mu$$
* Nếu $$\mu$$ quá nhỏ, số vòng lặp ngoài tăng lên. (Trong trường hợp này warm start có ích.)<br>
* Nếu $$\mu$$ quá lớn, phương pháp Newton cần nhiều vòng lặp để hội tụ ở mỗi bước centering.

##### Chọn giá trị khởi tạo của thuật toán
* Nếu $$t^{(0)}$$ quá nhỏ, số vòng lặp ngoài tăng lên.<br>
* Nếu $$t^{(0)}$$ quá lớn, bài toán trở thành giống v.0. Do đó, phương pháp Newton cần nhiều vòng lặp để tìm $$x^{(0)}$$ ở bước centering đầu tiên.

May mắn là hiệu năng của phương pháp chắn thực tế rất ổn định đối với việc chọn $$\mu$$ và $$t^{(0)}$$. Hơn nữa, khoảng giá trị phù hợp của các tham số này thay đổi tùy theo kích thước bài toán.

## Ví dụ LP nhỏ
Hình dưới đây cho thấy hiệu năng khi chạy một bài toán LP có n=50 chiều và m=100 ràng buộc bất đẳng thức bằng phương pháp chắn. Có thể thấy khi $$\mu = 2$$ thì số vòng lặp ngoài tăng lên, và khi $$\mu=150$$ thì số bước centering tăng tương đối so với khi $$\mu=50$$.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_barrier_method_03.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] Ví dụ LP nhỏ [3]</figcaption>
</p>
</figure>
