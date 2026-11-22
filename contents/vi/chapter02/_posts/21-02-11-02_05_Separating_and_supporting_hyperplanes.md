---
layout: post
title: 02-05 Siêu phẳng phân tách và hỗ trợ
chapter: '02'
order: 13
owner: Wontak Ryu
categories:
- chapter02
lang: vi
lesson_type: required
---

Phần này giới thiệu hai định lý cơ bản đặc trưng cho tập lồi: **định lý siêu phẳng phân tách** và **định lý siêu phẳng hỗ trợ**.

## Định lý siêu phẳng phân tách

Giả sử ta có hai tập lồi rời nhau (không giao nhau). Một cách tự nhiên để tách biệt chúng là đặt một đường thẳng hoặc mặt phẳng nằm giữa hai tập hợp. Ý tưởng này được ứng dụng rộng rãi trong các bài toán phân loại và được khẳng định chặt chẽ bởi **định lý siêu phẳng phân tách**.

Nếu $$C$$ và $$D$$ là hai tập lồi không rỗng và rời nhau, thì tồn tại $$a \ne 0$$ và $$b \in \mathbb{R}$$ sao cho $$a^T x \le b$$ với mọi $$x \in C$$ và $$a^T x \ge b$$ với mọi $$x \in D$$. Nói cách khác, hàm affine $$a^T x - b$$ không dương trên $$C$$ và không âm trên $$D$$. Siêu phẳng $$\{ x \mid a^T x = b\}$$ được gọi là **siêu phẳng phân tách** của $$C$$ và $$D$$.

Hình dưới đây minh họa một siêu phẳng phân tách hai tập lồi rời nhau $$C$$ và $$D$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.05_01_Seperating_hyperplan_theorem.png" alt="[Hình1] Định lý siêu phẳng phân tách [1]" width="70%">
  <figcaption style="text-align: center;">[Hình1] Định lý siêu phẳng phân tách [1]</figcaption>
</p>
</figure>

Chiều ngược lại của định lý không đúng: việc tồn tại siêu phẳng phân tách không đảm bảo hai tập hợp rời nhau. Chẳng hạn, với $$C = D = \{0\} \subseteq \mathbb{R}$$, siêu phẳng $$x = 0$$ vẫn thỏa mãn định nghĩa phân tách $$C$$ và $$D$$ dù hai tập này trùng nhau.

### Phân tách nghiêm ngặt

Nếu siêu phẳng phân tách thỏa mãn điều kiện mạnh hơn là $$a^T x < b$$ với mọi $$x \in C$$ và $$a^T x > b$$ với mọi $$x \in D$$, ta gọi đó là **phân tách nghiêm ngặt**. Hai tập lồi đóng rời nhau không phải lúc nào cũng có siêu phẳng phân tách nghiêm ngặt, nhưng điều kiện này vẫn được thỏa mãn trong nhiều trường hợp (ví dụ khi ít nhất một trong hai tập bị chặn).

## Định lý siêu phẳng hỗ trợ

**Định lý siêu phẳng hỗ trợ** khẳng định rằng với mọi tập lồi không rỗng $$C$$ và mọi điểm $$x_0$$ nằm trên biên **bd** $$C$$, luôn tồn tại ít nhất một siêu phẳng hỗ trợ cho $$C$$ tại $$x_0$$.

Cụ thể, cho $$x_0$$ là một điểm biên của $$C$$. Nếu tồn tại $$a \ne 0$$ sao cho $$a^T x \le a^T x_0$$ với mọi $$x \in C$$, thì siêu phẳng $$\{x \mid a^T x = a^T x_0 \}$$ được gọi là **siêu phẳng hỗ trợ** cho $$C$$ tại $$x_0$$.

*Lưu ý:* Biên của tập $$C$$ được định nghĩa là **bd** $$C = $$ **cl** $$C \setminus $$ **int** $$C$$, tức là bao đóng của $$C$$ trừ đi phần trong của nó.

Về mặt hình học, siêu phẳng hỗ trợ $$\{x \mid a^T x = a^T x_0\}$$ đi qua điểm biên $$x_0$$ và toàn bộ tập $$C$$ nằm trọn trong nửa không gian $$a^T x \le a^T x_0$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.05_02_Supporting_hyperplane_theorem.png" alt="[Hình 2] Siêu phẳng hỗ trợ [1]" width="70%">
  <figcaption style="text-align: center;">[Hình 2] Siêu phẳng hỗ trợ [1]</figcaption>
</p>
</figure>