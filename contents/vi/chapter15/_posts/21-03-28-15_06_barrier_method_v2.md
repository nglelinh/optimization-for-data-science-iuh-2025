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

Trong phiên bản trước, thuật toán yêu cầu giải chính xác bài toán chắn để nghiệm nằm đúng trên đường trung tâm. Tuy nhiên, đường trung tâm chỉ là phương tiện dẫn tới nghiệm tối ưu chứ không phải đích đến cuối cùng, nên trên thực tế ta không cần giải chính xác tuyệt đối ở từng bước định tâm.

### Thuật toán

Từ nhận xét đó, **phương pháp chắn v.2** chỉ giải xấp xỉ bài toán chắn ở mỗi bước: cụ thể, $$x^{(0)} \approx x^*(t)$$ ở bước 2 và $$x^{(k+1)} \approx x^*(t)$$ ở bước 3-2.

Cấu trúc thuật toán giữ nguyên như phương pháp chắn v.1:

1. Chọn $$t^{(0)} > 0$$ và đặt $$k := 0$$.
2. Tại $$t = t^{(0)}$$, giải xấp xỉ bài toán chắn để thu được $$x^{(0)} \approx x^*(t)$$.
3. Trong khi $$m/t > \epsilon$$:<br>
   3-1. Chọn $$t^{(k+1)} > t^{(k)}$$.<br>
   3-2. Khởi tạo phương pháp Newton bằng $$x^{(k)}$$ (warm start) và giải xấp xỉ bài toán chắn tại $$t = t^{(k+1)}$$ để thu được $$x^{(k+1)} \approx x^*(t)$$.<br>
   Kết thúc vòng lặp.<br>

Với phương pháp chắn v.2, hai câu hỏi trọng tâm cần đặt ra là:

* Mỗi bước giải xấp xỉ cần chính xác đến mức nào?
* Mỗi bước định tâm cần bao nhiêu bước Newton?

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_barrier_methodv2_04.png" alt="" width="70%" height="70%">
  <figcaption style="text-align: center;">[Hình 1] Phân tích số vòng lặp Newton và khoảng cách dưới tối ưu theo $$m$$ [1]</figcaption>
</p>
</figure>

Hình 1 cho thấy khi áp dụng phương pháp chắn cho bài toán có $$m$$ ràng buộc, tốc độ hội tụ vẫn là tuyến tính ngay cả khi $$m$$ rất lớn — tức số vòng lặp tăng theo thang logarit đối với $$m$$.

Nhìn từ góc độ khác, số bước Newton cần thiết để giảm khoảng cách đối ngẫu (duality gap) đi một hệ số $$10^4$$ chỉ tăng rất chậm theo $$m$$. Như thể hiện ở Hình 2, ngay cả khi $$m$$ tăng mạnh, mỗi bài toán vẫn chỉ cần khoảng 20–30 bước Newton (dù chi phí của bản thân mỗi bước Newton phụ thuộc đáng kể vào kích thước bài toán).

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_barrier_methodv2_05.png" alt="" width="70%" height="70%">
  <figcaption style="text-align: center;">[Hình 2] Phân tích số vòng lặp Newton khi $$m$$ tăng [1]</figcaption>
</p>
</figure>
