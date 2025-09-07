---
layout: post
title: 05 Các Bài Toán Chuẩn
chapter: '05'
order: 1
owner: Hooncheol Shin
categories:
- chapter05
lang: vi
---

# Các Bài Toán Chuẩn

Trong [Chương 1](/chapter01/2021/01/07/optimization_problems/), chúng ta đã học rằng một bài toán tối ưu lồi được định nghĩa như sau:

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter05/05_00_optimization_problem.png" alt="[Fig1] Bài toán tối ưu lồi ở dạng chuẩn [3]" width="70%">
  <figcaption style="text-align: center;">[Fig1] Bài toán tối ưu lồi ở dạng chuẩn [3]</figcaption>
</p>
</figure>

* Tập miền xác định là lồi
* Hàm mục tiêu $$ f $$ và hàm ràng buộc bất đẳng thức $$ g_i $$ là lồi
* Hàm ràng buộc đẳng thức $$ h_j $$ là affine

Tùy thuộc vào loại hàm mục tiêu và hàm ràng buộc, các bài toán tối ưu được phân loại thành nhiều danh mục khác nhau. Trong chương này, chúng ta sẽ tìm hiểu về sáu lớp con chính:

- Quy hoạch tuyến tính (Linear Programming - LP)
- Quy hoạch bậc hai (Quadratic Programming - QP)
- Quy hoạch bậc hai với ràng buộc bậc hai (Quadratically Constrained Quadratic Programming - QCQP)
- Quy hoạch nón bậc hai (Second-Order Cone Programming - SOCP)
- Quy hoạch bán xác định (Semidefinite Programming - SDP)
- Quy hoạch nón (Conic Programming - CP)

Các bài toán này có mối quan hệ bao hàm như sau và trở nên tổng quát hơn khi di chuyển xuống dưới trong danh sách:

$$ LP \subseteq QP \subseteq QCQP \subseteq SOCP \subseteq SDP \subseteq CP $$
<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter05/05_00_canonical_problems.jpeg" alt="[Fig2] Các Bài Toán Chuẩn" width="90%">
  <figcaption style="text-align: center;">[Fig2] Các Bài Toán Chuẩn</figcaption>
</p>
</figure>