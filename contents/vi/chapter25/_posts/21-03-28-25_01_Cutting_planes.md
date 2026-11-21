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

Phương pháp mặt phẳng cắt (cutting plane) là cách tiếp cận biến một quy hoạch tuyến tính nguyên thành một bài toán lồi rồi tìm nghiệm. Nếu nghiệm này không thuộc tập khả thi ban đầu, nó dùng các lát cắt (cut) để cắt bỏ vùng chứa nghiệm, từng bước dẫn nghiệm mới thu được vào tập khả thi ban đầu. Ở đây, lát cắt là một đường thẳng (hoặc siêu phẳng) cắt tập khả thi, còn gọi là mặt phẳng cắt.

## Khái niệm mặt phẳng cắt
Về mặt khái niệm, có thể xem đây là phương pháp kẻ một đường giữa tập khả thi ban đầu và tập khả thi đã nới lỏng để cắt bỏ các vùng không thuộc tập khả thi ban đầu, như hình dưới.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter25/25_01_cutting_plane_concept.png" alt="[Hình 1] Mặt phẳng cắt">
  <figcaption style="text-align: center;">[Hình 1] Mặt phẳng cắt</figcaption>
</p>
</figure>

* Vùng đỏ: tập khả thi của quy hoạch tuyến tính nguyên ban đầu
* Vùng xanh: tập khả thi của bài toán nới lỏng lồi
* Đường xanh lá: mặt phẳng cắt (mặt phẳng cắt nằm giữa vùng xanh và vùng đỏ)

Thuật toán chi tiết sẽ được giới thiệu lại ở phần chính.


## Đôi nét lịch sử về mặt phẳng cắt
Phương pháp mặt phẳng cắt mất rất nhiều thời gian để phát triển từ lý thuyết thành một phương pháp thực tế.

Năm 1954, Dantzig, Fulkerson và Johnson lần đầu đề xuất phương pháp mặt phẳng cắt để giải bài toán TSP (người bán hàng du lịch), và năm 1958, nhà toán học Gomory đề xuất phương pháp mặt phẳng cắt tổng quát có thể giải quy hoạch tuyến tính nguyên bất kỳ. Tuy nhiên, trong khoảng 30 năm sau đó, các lát cắt Gomory vẫn bị bỏ quên trong trạng thái không thực dụng để giải các bài toán thực tế.

Năm 1990, Sebastian Ceria tại CMU đã cài đặt thành công phương pháp mặt phẳng cắt kết hợp với thuật toán nhánh và cận, gọi là nhánh và cắt (branch and cut). Từ đó, mặt phẳng cắt trở thành thành phần cốt lõi của các bộ giải tối ưu thương mại.
