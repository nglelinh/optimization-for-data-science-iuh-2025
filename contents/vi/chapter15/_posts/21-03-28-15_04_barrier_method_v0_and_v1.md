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
**Phương pháp chắn v.0** chọn trực tiếp $$t = m/\epsilon$$ với độ chính xác mong muốn $$\epsilon > 0$$, rồi giải một lần bài toán chắn sau để đảm bảo $$f(x^*(t)) - f(x^*) \le \epsilon$$:
>
$$\begin{align}
 &\min_{x} \ && tf(x) + \phi(x) \\
 &\text{subject to } \ && Ax = b \\
\end{align}$$

Tuy nhiên, vì $$t = m/\epsilon$$ tăng rất lớn khi $$\epsilon$$ nhỏ, bài toán tương ứng nằm sát cuối đường trung tâm và gần như quay về độ khó của bài toán gốc trên biên, khiến phương pháp Newton hội tụ chậm và khó giải.

Để khắc phục, thay vì đặt $$t$$ lớn ngay từ đầu, ta tăng dần $$t$$ để bám theo đường trung tâm. Cách tiếp cận này được gọi là **phương pháp chắn v.1**.

## Phương pháp chắn v.1
**Phương pháp chắn v.1** tăng dần tham số $$t$$ qua nhiều bước và giải chuỗi bài toán chắn sau:
>
$$\begin{align}
 &\min_{x} \ && tf(x) + \phi(x) \\
 &\text{subject to } \ && Ax = b \\
\end{align}$$

### Thuật toán
Các bước của thuật toán như sau:

1. Chọn $$t^{(0)} > 0$$ và đặt $$k := 0$$.
2. Tại $$t = t^{(0)}$$, giải bài toán chắn để thu được $$x^{(0)} = x^*(t)$$.
3. Trong khi $$m/t > \epsilon$$:<br>
  3-1. Chọn $$t^{(k+1)} > t^{(k)}$$.<br>
  3-2. Khởi tạo phương pháp Newton bằng $$x^{(k)}$$ (khởi động ấm — warm start) và giải bài toán chắn tại $$t = t^{(k+1)}$$ để thu được $$x^{(k+1)} = x^*(t)$$.<br>
  Kết thúc vòng lặp.<br>

### Nhận xét
* **Quy tắc cập nhật thường dùng**: $$t^{(k+1)} = \mu t^{(k)}$$ với $$\mu > 1$$.
* **Khởi động ấm (warm start)**: Ở bước 3-2, nghiệm của vòng lặp trước được dùng làm điểm khởi tạo cho vòng lặp tiếp theo.
* **Bước định tâm (centering step)**: Bước 2 và bước 3-2 (giải bài toán chắn ứng với một giá trị $$t$$ cố định) được gọi là các bước định tâm hay vòng lặp ngoài.

### Lựa chọn tham số
Khi chọn $$\mu$$ và $$t^{(0)}$$, cần cân nhắc các đánh đổi sau:

##### Chọn $$\mu$$
* Nếu $$\mu$$ quá nhỏ, số vòng lặp ngoài tăng lên (dù khởi động ấm giúp mỗi bước giải nhanh hơn).<br>
* Nếu $$\mu$$ quá lớn, điểm khởi tạo nằm xa điểm đường trung tâm mới nên phương pháp Newton cần nhiều vòng lặp hơn ở mỗi bước định tâm.

##### Chọn $$t^{(0)}$$
* Nếu $$t^{(0)}$$ quá nhỏ, số vòng lặp ngoài tăng lên.<br>
* Nếu $$t^{(0)}$$ quá lớn, bài toán ban đầu trở nên khó giải tương tự phương pháp chắn v.0, làm tăng số bước Newton ở bước định tâm đầu tiên.

Trong thực tế, hiệu năng của phương pháp chắn khá ổn định trước sự thay đổi của $$\mu$$ và $$t^{(0)}$$, trong đó khoảng giá trị phù hợp phụ thuộc vào kích thước bài toán.

## Ví dụ LP cỡ nhỏ
Hình dưới đây minh họa hiệu năng của phương pháp chắn trên một bài toán quy hoạch tuyến tính (LP) với $$n = 50$$ biến và $$m = 100$$ ràng buộc bất đẳng thức. Khi $$\mu = 2$$, số vòng lặp ngoài tăng lên; còn khi $$\mu = 150$$, số bước định tâm và bước Newton có sự đánh đổi rõ rệt so với mức $$\mu = 50$$.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_barrier_method_03.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] Ví dụ LP cỡ nhỏ [3]</figcaption>
</p>
</figure>
