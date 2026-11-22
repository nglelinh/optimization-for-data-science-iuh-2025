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

Trong [Chương 1](/chapter01/2021/01/07/optimization_problems/), ta đã biết một bài toán tối ưu hóa lồi dạng chuẩn được định nghĩa như sau:

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter05/05_00_optimization_problem.png" alt="[Fig1] Bài toán tối ưu lồi ở dạng chuẩn [3]" width="70%">
  <figcaption style="text-align: center;">[Fig1] Bài toán tối ưu lồi ở dạng chuẩn [3]</figcaption>
</p>
</figure>

* Miền xác định là tập lồi.
* Hàm mục tiêu $$ f $$ và các hàm ràng buộc bất đẳng thức $$ g_i $$ là các hàm lồi.
* Các hàm ràng buộc đẳng thức $$ h_j $$ là các hàm affine.

Tùy vào cấu trúc của hàm mục tiêu và các hàm ràng buộc, các bài toán tối ưu hóa lồi được phân loại thành nhiều lớp chuẩn khác nhau. Chương này trình bày sáu lớp bài toán tiêu biểu:

- Quy hoạch tuyến tính (Linear Programming - LP)
- Quy hoạch bậc hai (Quadratic Programming - QP)
- Quy hoạch bậc hai có ràng buộc bậc hai (Quadratically Constrained Quadratic Programming - QCQP)
- Quy hoạch nón bậc hai (Second-Order Cone Programming - SOCP)
- Quy hoạch nửa xác định (Semidefinite Programming - SDP)
- Quy hoạch nón (Conic Programming - CP)

Sáu lớp bài toán này tạo thành một hệ thống phân cấp bao hàm, với mức độ tổng quát tăng dần từ trái sang phải:

$$ LP \subseteq QP \subseteq QCQP \subseteq SOCP \subseteq SDP \subseteq CP $$
<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter05/05_00_canonical_problems.jpeg" alt="[Fig2] Các Bài Toán Chuẩn" width="90%">
  <figcaption style="text-align: center;">[Fig2] Các Bài Toán Chuẩn</figcaption>
</p>
</figure>

Sau phần phân loại và bài thực hành DCP/CVXPY, bài tùy chọn [05-08 Ứng dụng và phát triển gần đây]({% multilang_post_url contents/chapter05/2026-09-16-05_08_Applications_Recent %}) giới thiệu các ứng dụng hiện đại gắn với những dạng chuẩn này, bao gồm bộ giải Clarabel, bài toán QP tối ưu hóa danh mục đầu tư, nới lỏng SDP trong kiểm chứng mạng nơ-ron và khôi phục thưa bằng khai triển thuật toán.