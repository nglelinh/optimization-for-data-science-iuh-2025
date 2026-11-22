---
layout: post
title: 02-01-01 Đường thẳng, đoạn thẳng, tia
chapter: '02'
order: 3
owner: Wontak Ryu
categories:
- chapter02
lang: vi
---

Để định nghĩa tập affine, tập lồi và hình nón, trước hết ta xét ba đối tượng hình học cơ bản: đường thẳng, đoạn thẳng và tia.

Đường thẳng đi qua hai điểm kéo dài vô hạn về cả hai phía. Ngược lại, đoạn thẳng chỉ gồm các điểm nằm giữa hai điểm đó, còn tia xuất phát từ một điểm và kéo dài vô hạn theo một hướng đi qua điểm còn lại. Hình dưới đây minh họa đường thẳng và đoạn thẳng đi qua hai điểm $$x_1$$ và $$x_2$$. Tùy theo miền giá trị của tham số $$\theta$$, ta thu được biểu diễn tương ứng cho đường thẳng, đoạn thẳng hoặc tia.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.01_Line_Segment.png" alt="Line Segment" width="70%">
  <figcaption style="text-align: center;">$$\text{[Hình1] } x_1\text{ và } x_2 \text{ định nghĩa Đường thẳng và Đoạn thẳng [1]}$$</figcaption>
</p>
</figure>

*Lưu ý:* Khi lấy hai điểm thuộc một tập hợp để tạo thành đường thẳng, đoạn thẳng hoặc tia, việc các điểm tạo ra có luôn thuộc lại tập hợp đó hay không chính là tiêu chí để định nghĩa các loại tập hợp. (Ta cũng có thể định nghĩa tương tự bằng nhiều điểm thông qua tổ hợp affine, tổ hợp lồi hoặc tổ hợp nón; chi tiết sẽ được trình bày ở các mục tiếp theo.)

## Đường thẳng

**Đường thẳng** đi qua hai điểm $$x_1$$ và $$x_2$$ được định nghĩa là:
> $$y = \theta x_1 + (1 - \theta) x_2$$ với $$\theta \in \mathbb{R}$$

## Đoạn thẳng

**Đoạn thẳng** nối hai điểm $$x_1$$ và $$x_2$$ thu được khi giới hạn $$\theta$$ trong đoạn $$[0, 1]$$:
> $$y = \theta x_1 + (1 - \theta) x_2$$ với $$0 \le \theta \le 1$$

Ta cũng có thể viết lại dưới dạng:
> $$y = x_2 + \theta (x_1 - x_2)$$ với $$0 \le \theta \le 1$$

## Tia

**Tia** xuất phát từ $$x_2$$ và kéo dài vô hạn theo hướng đi qua $$x_1$$ được định nghĩa là:
> $$y = x_2 + \theta (x_1 - x_2)$$ với $$\theta \ge 0$$

Hoặc viết tương đương:
> $$y = \theta x_1 + (1 - \theta) x_2$$ với $$\theta \ge 0$$

Như vậy, miền giá trị của tham số $$\theta$$ lần lượt là $$\theta \in \mathbb{R}$$ đối với đường thẳng, $$0 \le \theta \le 1$$ đối với đoạn thẳng và $$\theta \ge 0$$ đối với tia. Các miền giá trị này sẽ xuất hiện lại tương ứng trong định nghĩa tập affine, tập lồi và hình nón ở các bài sau.
