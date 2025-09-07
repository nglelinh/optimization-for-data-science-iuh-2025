---
layout: post
title: 02-05 Siêu phẳng phân tách và hỗ trợ
chapter: '02'
order: 11
owner: Wontak Ryu
categories:
- chapter02
lang: vi
lesson_type: required
---

Phần này giới thiệu hai định lý đặc trưng cho tập lồi: **định lý siêu phẳng phân tách** và **định lý siêu phẳng hỗ trợ**.

## Định lý siêu phẳng phân tách

Giả sử có một số tập lồi rời rạc không có giao điểm. Làm thế nào chúng ta có thể phân tách chúng? Cách đơn giản nhất là vẽ một đường thẳng giữa các tập hợp. Phương pháp này được sử dụng rộng rãi trong phân loại và được hỗ trợ bởi **định lý siêu phẳng phân tách**.

Nếu có hai tập lồi rời rạc $$C$$ và $$D$$, thì với $$x \in C$$, $$a^T x \le b$$ và với $$x \in D$$, $$a^T x \ge b$$ với một số $$a \ne 0$$ và $$b$$. Nói cách khác, hàm affine $$a^T x - b$$ không dương trên $$C$$ và không âm trên $$D$$. Siêu phẳng $$\{ x \mid a^T x = b\}$$ được gọi là **siêu phẳng phân tách** cho $$C$$ và $$D$$.

Hình dưới đây cho thấy một siêu phẳng phân tách chia hai tập lồi rời rạc $$C$$ và $$D$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.05_01_Seperating_hyperplan_theorem.png" alt="[Hình1] Định lý siêu phẳng phân tách [1]" width="70%">
  <figcaption style="text-align: center;">[Hình1] Định lý siêu phẳng phân tách [1]</figcaption>
</p>
</figure>

Điều ngược lại của định lý siêu phẳng phân tách không đúng. Tức là, sự tồn tại của một siêu phẳng phân tách không đảm bảo rằng các tập hợp là rời rạc. Ví dụ, nếu $$C = D = \{0\} \subseteq \mathbb{R}$$, thì $$x = 0$$ phân tách $$C$$ và $$D$$.

### Phân tách nghiêm ngặt

Nếu siêu phẳng phân tách thỏa mãn điều kiện mạnh hơn $$x \in C$$ suy ra $$a^T x < b$$ và $$x \in D$$ suy ra $$a^T x > b$$, điều này được gọi là **phân tách nghiêm ngặt**. Các tập lồi đóng rời rạc không phải lúc nào cũng yêu cầu phân tách nghiêm ngặt, nhưng trong nhiều trường hợp, điều kiện này được thỏa mãn.

## Định lý siêu phẳng hỗ trợ

**Định lý siêu phẳng hỗ trợ** phát biểu rằng với bất kỳ tập lồi không rỗng $$C$$ và bất kỳ điểm $$x_0$$ nào trên biên **bd** $$C$$, tồn tại một siêu phẳng hỗ trợ tại $$x_0$$.

Siêu phẳng hỗ trợ là gì? Giả sử $$x_0$$ là một điểm biên của $$C$$. Nếu với mọi $$x \in C$$, $$a^T x \le a^T x_0$$ ($$a \ne 0$$), thì siêu phẳng $$\{x \mid a^T x = a^T x_0 \}$$ là **siêu phẳng hỗ trợ** cho $$C$$ tại $$x_0$$.

[Lưu ý] Biên được định nghĩa là $$x_0 \in$$ **bd** $$C = $$ **cl** $$C$$ $$\setminus$$ **int** $$C$$, tức là bao đóng trừ đi phần trong.

Về mặt hình học, siêu phẳng hỗ trợ $$\{x \mid a^T x = a^T x_0\}$$ tiếp xúc với $$C$$ tại $$x_0$$ và nửa không gian $$a^T x \le a^T x_0$$ chứa $$C$$.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter02/02.05_02_Supporting_hyperplane_theorem.png" alt="[Hình 2] Siêu phẳng hỗ trợ [1]" width="70%">
  <figcaption style="text-align: center;">[Hình 2] Siêu phẳng hỗ trợ [1]</figcaption>
</p>
</figure>