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

Trong không gian 2D hay 3D, ai cũng vẽ được đường thẳng, đoạn thẳng và tia bằng thước kẻ. Nhưng khi bài toán tối ưu sống trong không gian 10.000 chiều — nơi không còn thước kẻ hay hình vẽ — ta cần một biểu diễn đại số thống nhất để "đi bộ" giữa hai phương án $$x_1$$ và $$x_2$$. Biểu diễn tham số $$x(\theta) = \theta x_1 + (1 - \theta)x_2$$ làm đúng điều đó: chỉ cần thay đổi miền của tham số thực $$\theta$$, ta lập tức thu được cả đường thẳng, đoạn thẳng lẫn tia.

Bài học ngắn nhưng nền tảng này đặt viên gạch ký hiệu đầu tiên cho toàn bộ hình học lồi của khóa học.

## Bản đồ kiến thức nền: Ba đối tượng sơ cấp qua một tham số $$\theta$$

- **Đường thẳng (Line):** $$x(\theta) = \theta x_1 + (1-\theta)x_2$$ với $$\theta \in \mathbb{R}$$ tự do — không bị chặn cả hai đầu, là khuôn mẫu của **tập affine**.
- **Đoạn thẳng (Line Segment):** Giới hạn $$0 \le \theta \le 1$$ — nối kín hai đầu mút $$x_1$$ (khi $$\theta = 1$$) và $$x_2$$ (khi $$\theta = 0$$), là khuôn mẫu của **tập lồi**.
- **Tia (Ray):** $$x(t) = x_0 + t v$$ với $$t \ge 0$$ ($$v \ne 0$$) — xuất phát từ điểm gốc $$x_0$$ và kéo dài vô hạn theo đúng một hướng $$v$$, là khuôn mẫu của **hình nón** và phân tích hướng vô hạn (recession directions) trong tối ưu hóa.

### Khung giải thích (nên đọc chậm): Định vị các điểm theo tham số $$\theta$$ giữa $$x_1 = (1, 2)$$ và $$x_2 = (5, 4)$$

Cho $$x_1 = (1, 2)^T$$ và $$x_2 = (5, 4)^T$$. Biểu diễn tham số là $$x(\theta) = \theta x_1 + (1 - \theta)x_2$$:

1. **Điểm trên đoạn thẳng ($$\theta = 0.25 \in [0, 1]$$):**
   $$x(0.25) = 0.25(1, 2) + 0.75(5, 4) = (0.25 + 3.75,\ 0.5 + 3.0) = (4, 3.5).$$
   Vì $$1 - \theta = 0.75$$ lớn hơn, điểm này nằm gần $$x_2$$ hơn gấp 3 lần so với $$x_1$$.
2. **Điểm trên đường thẳng nhưng ngoài đoạn thẳng ($$\theta = 1.5 \notin [0, 1]$$):**
   $$x(1.5) = 1.5(1, 2) - 0.5(5, 4) = (1.5 - 2.5,\ 3 - 2) = (-1, 1).$$
   Điểm này vượt quá đầu mút $$x_1$$ về phía trái.
3. **Điểm trên tia xuất phát từ $$x_1$$ đi qua $$x_2$$:** Đặt hướng $$v = x_2 - x_1 = (4, 2)^T$$ và $$x(t) = x_1 + t v$$ ($$t \ge 0$$). Với $$t = 2$$:
   $$x(2) = (1, 2) + 2(4, 2) = (9, 6).$$
   Nhờ cách viết này, ta dễ dàng kiểm tra một thuật toán tìm kiếm đường thẳng $$x^{(k+1)} = x^{(k)} + t d$$ đang đi dọc theo một tia hợp lệ.

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
