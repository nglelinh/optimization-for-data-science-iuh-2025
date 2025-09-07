---
layout: post
title: 02-01-01 Đường thẳng, đoạn thẳng, tia
chapter: '02'
order: 2
owner: Wontak Ryu
categories:
- chapter02
lang: vi
---

Để định nghĩa tập affine, tập lồi và hình nón, trước tiên hãy xem xét đường thẳng, đoạn thẳng và tia.

Đường thẳng là một đường thẳng vô hạn đi qua hai điểm theo cả hai hướng. Ngược lại, đoạn thẳng là một đường thẳng chỉ được xác định giữa hai điểm, và tia bắt đầu từ một điểm và kéo dài vô hạn theo một hướng qua điểm khác. Hình dưới đây cho thấy một đường thẳng và một đoạn thẳng. Tùy thuộc vào phạm vi của tham số $$\theta$$, bạn có thể tưởng tượng cách một đường thẳng, đoạn thẳng hoặc tia được định nghĩa.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter02/02.01_Line_Segment.png" alt="Line Segment" width="70%">
  <figcaption style="text-align: center;">$$\text{[Hình1] } x_1\text{ và } x_2 \text{ định nghĩa Đường thẳng và Đoạn thẳng [1]}$$</figcaption>
</p>
</figure>

[Tham khảo] Khi bạn sử dụng hai điểm được bao gồm trong một tập hợp để tạo ra một đường thẳng, đoạn thẳng hoặc tia, việc liệu những điểm này có được bao gồm trong tập hợp hay không quyết định định nghĩa của tập hợp. (Bạn cũng có thể định nghĩa tập hợp bằng cách sử dụng nhiều điểm và các tổ hợp affine, lồi hoặc nón của chúng. Chi tiết sẽ được giải thích trong các phần tiếp theo.)

## Đường thẳng

Một **Đường thẳng** đi qua hai điểm $$x_1$$ và $$x_2$$ được định nghĩa là:
> $$y = \theta x_1 + (1 - \theta) x_2$$ với $$\theta \in \mathbb{R}$$

## Đoạn thẳng

Một **Đoạn thẳng** được định nghĩa bằng cách giới hạn $$\theta$$ trong khoảng [0, 1]:
> $$y = \theta x_1 + (1 - \theta) x_2$$ với $$0 \le \theta \le 1$$

Hoặc bạn có thể biểu diễn nó như:
> $$y = x_2 + \theta (x_1 - x_2)$$ với $$0 \le \theta \le 1$$

## Tia

Một **Tia** bắt đầu từ một điểm và kéo dài vô hạn theo một hướng:
> $$y = x_2 + \theta (x_1 - x_2)$$ với $$\theta \ge 0$$

Hoặc tương đương:
> $$y = \theta x_1 + (1 - \theta) x_2$$ với $$\theta \ge 0$$



Bây giờ bạn có thể thấy rằng phạm vi của $$\theta$$ là $$\theta \in \mathbb{R}$$ cho đường thẳng, $$0 \le \theta \le 1$$ cho đoạn thẳng, và $$\theta \ge 0$$ cho tia. Hơn nữa, bạn sẽ thấy rằng các phạm vi của $$\theta$$ giống nhau trong các tập affine, tập lồi và tập nón mà chúng ta sẽ định nghĩa sau này.

