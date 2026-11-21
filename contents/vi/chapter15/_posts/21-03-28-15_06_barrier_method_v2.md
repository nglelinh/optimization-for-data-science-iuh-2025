---
layout: post
title: '15-06 Phương pháp chắn v.2'
chapter: '15'
order: 12
owner: Minjoo Lee
categories:
- chapter15
lang: vi
---

Ở thuật toán trước, chúng ta tạo ra các nghiệm nằm trên đường trung tâm, nhưng thực ra đường trung tâm chỉ là phương tiện để đi đến nghiệm tối ưu ("means to an end"). Do đó, không cần giải bài toán một cách chính xác.

### Thuật toán

Vì lý do này, phương pháp chắn v.2 giải bài toán chắn một cách xấp xỉ. Cụ thể, $$x^{(0)} \approx x^*(t)$$ ở bước 2 và $$x^{(k+1)} \approx x^*(t)$$ ở bước 3-2 giờ đây là các xấp xỉ.

Các bước của thuật toán giống như trong phương pháp chắn v.1.

1. Chọn $$t^{(0)} > 0$$ và đặt $$k := 0$$.
2. Tại $$t = t^{(0)}$$, giải bài toán chắn để thu được $$x^{(0)} \approx x^*(t)$$.
3. Trong khi $$m/t > \epsilon$$<br>
   3-1. Chọn $$t^{(k+1)} > t^{(k)}$$.<br>
   3-2. Khởi tạo phương pháp Newton với $$x^{(k)}$$ (warm start)<br>
        Tại $$t = t^{(k+1)}$$, giải bài toán chắn để thu được $$x^{(k+1)} \approx x^*(t)$$.<br>
   kết thúc vòng lặp<br>

Trong phương pháp chắn v.2, hai vấn đề sau đây rất quan trọng:

* Mỗi xấp xỉ cần gần đến mức nào?
* Mỗi bước centering cần bao nhiêu bước Newton?

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_barrier_methodv2_04.png" alt="" width="70%" height="70%">
  <figcaption style="text-align: center;">[Hình 1] Phân tích số vòng lặp Newton và khoảng cách dưới tối ưu theo $$m$$ [1]</figcaption>
</p>
</figure>

Trong hình trên, bạn có thể thấy khi áp dụng phương pháp chắn cho bài toán có $$m$$ ràng buộc, sự hội tụ vẫn là tuyến tính ngay cả khi $$m$$ rất lớn. Nghĩa là, nó có thang logarit theo $$m$$.

Nhìn từ một góc độ khác, số bước Newton cần thiết (để giảm khoảng cách dưới tối ưu ban đầu (duality gap) $$10^4$$) chỉ tăng chậm theo $$m$$. Quan sát hình dưới đây, ngay cả khi $$m$$ tăng đáng kể, mỗi bước centering chỉ cần khoảng 20–30 bước Newton. Tuy nhiên, chi phí của một bước Newton thay đổi rất nhiều tùy theo kích thước bài toán.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_barrier_methodv2_05.png" alt="" width="70%" height="70%">
  <figcaption style="text-align: center;">[Hình 2] Phân tích số vòng lặp Newton khi $$m$$ tăng [1]</figcaption>
</p>
</figure>
