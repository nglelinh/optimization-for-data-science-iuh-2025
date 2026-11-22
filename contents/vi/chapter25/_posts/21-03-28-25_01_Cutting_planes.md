---
layout: post
title: '25-01 Mặt phẳng cắt'
chapter: '25'
order: 2
owner: YoungJae Choung
categories:
- chapter25
lang: vi
---

Phương pháp mặt phẳng cắt (cutting plane) giải bài toán quy hoạch tuyến tính nguyên bằng cách xuất phát từ bài toán nới lỏng lồi. Nếu nghiệm tìm được chưa thuộc tập khả thi nguyên ban đầu, thuật toán bổ sung các bất đẳng thức tuyến tính — gọi là *lát cắt* (cut) hay *mặt phẳng cắt* — nhằm cắt bỏ vùng chứa nghiệm phân số đó mà không loại bỏ bất kỳ điểm nguyên khả thi nào, dần dẫn nghiệm hội tụ về tập khả thi ban đầu.

## Khái niệm mặt phẳng cắt

Về mặt hình học, mặt phẳng cắt tương ứng với một đường thẳng (hay siêu phẳng trong không gian nhiều chiều) ngăn cách nghiệm nới lỏng nằm ngoài miền nguyên khỏi tập khả thi nguyên ban đầu, như minh họa trong Hình 1.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_cutting_plane_concept.png" alt="[Hình 1] Mặt phẳng cắt">
  <figcaption style="text-align: center;">[Hình 1] Mặt phẳng cắt</figcaption>
</p>
</figure>

* Vùng đỏ: bao lồi của tập khả thi thuộc quy hoạch tuyến tính nguyên ban đầu.
* Vùng xanh: tập khả thi của bài toán nới lỏng lồi.
* Đường xanh lá: mặt phẳng cắt ngăn cách phần thừa của vùng xanh với vùng đỏ.

Thuật toán cụ thể sẽ được trình bày trong các mục tiếp theo.

## Đôi nét lịch sử về mặt phẳng cắt

Phương pháp mặt phẳng cắt trải qua chặng đường dài từ lý thuyết đến triển khai thực tế.

Năm 1954, Dantzig, Fulkerson và Johnson lần đầu áp dụng ý tưởng mặt phẳng cắt cho bài toán người bán hàng du lịch (TSP). Đến năm 1958, Ralph Gomory đề xuất phương pháp mặt phẳng cắt tổng quát cho mọi bài toán quy hoạch tuyến tính nguyên. Tuy nhiên, trong suốt khoảng 30 năm sau đó, các lát cắt Gomory vẫn ít được sử dụng trong thực tiễn do vấn đề ổn định số và tốc độ hội tụ chậm khi chạy độc lập.

Năm 1990, Sebastian Ceria (Đại học Carnegie Mellon) cùng các cộng sự đã kết hợp hiệu quả mặt phẳng cắt với thuật toán nhánh và cận, hình thành thuật toán **nhánh và cắt (branch and cut)**. Từ đó, mặt phẳng cắt trở thành một thành phần không thể thiếu trong hầu hết các bộ giải quy hoạch nguyên thương mại và mã nguồn mở.
