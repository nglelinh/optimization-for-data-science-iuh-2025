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

Nếu Chương 04 dạy bạn ngữ pháp chung của tối ưu hóa lồi, thì Chương 05 giống như việc bước vào bảo tàng những "kiến trúc kinh điển" đã định hình cả khoa học dữ liệu, tài chính và kỹ thuật hiện đại. Từ bài toán chia khẩu phần ăn thời Thế chiến II (LP), tối ưu danh mục đầu tư Markowitz đạt giải Nobel Kinh tế (QP), đến định vị vệ tinh và thiết kế ăng-ten (SOCP), hay nới lỏng đồ thị lượng tử và kiểm chứng mạng nơ-ron (SDP) — tất cả đều xếp thành một **hệ phân cấp lồng nhau tuyệt đẹp**:
$$\text{LP} \subset \text{QP} \subset \text{QCQP} \subset \text{SOCP} \subset \text{SDP} \subset \text{CP}.$$

Tại sao việc nhận diện đúng "họ" của bài toán lại quan trọng đến vậy? Bởi vì mỗi tầng cao hơn có sức biểu diễn mạnh hơn, nhưng chi phí giải cũng tăng theo: một bài LP hàng triệu biến có thể giải trong vài giây, trong khi một bài SDP vài nghìn biến đã đòi hỏi bộ nhớ khổng lồ. Biết xếp bài toán vào tầng **thấp nhất có thể** chính là dấu ấn của người làm tối ưu chuyên nghiệp.

## Kiến thức cần nhớ: Hệ phân cấp các bài toán tối ưu hóa chuẩn

Toàn bộ Chương 05 xoay quanh bốn trụ cột phân loại bài toán theo cấu trúc hàm mục tiêu và hình học nón ràng buộc:

- **Tầng Đa diện — LP & QP:** Tập khả thi là đa diện tạo bởi các bất đẳng thức tuyến tính $$Gx \le h$$. LP có hàm mục tiêu tuyến tính (nghiệm nằm ở đỉnh đa diện), còn QP có hàm mục tiêu bậc hai lồi (nghiệm có thể nằm trên mặt hoặc phần trong đa diện).
- **Tầng Nón Bậc Hai — QCQP & SOCP:** Khi ràng buộc có thêm chuẩn Euclidean $$\|Ax + b\|_2 \le c^T x + d$$ (nón hình nón kem / Lorentz cone), ta mô hình hóa được bài toán bền vững trước nhiễu ellipsoid, bài toán khoảng cách, và hồi quy có ràng buộc năng lượng.
- **Tầng Nón Ma trận — SDP & CP:** Khi biến quyết định là ma trận đối xứng nửa xác định dương $$X \succeq 0$$, ta mở khóa sức mạnh của bất đẳng thức ma trận tuyến tính (LMI) — nền tảng của lý thuyết điều khiển hiện đại, hoàn thiện ma trận và nới lỏng bài toán tổ hợp NP-khó.
- **Cầu nối Thực hành — Mô hình hóa DCP & Thống kê:** Các mô hình cốt lõi của học máy như Bình phương tối thiểu (Least Squares), Hồi quy tuyến tính, Hồi quy Logistic, Lasso và SVM đều là các trường hợp đặc biệt trong hệ phân cấp này, và ngôn ngữ DCP (CVXPY) tự động biên dịch chúng về đúng bộ giải nón tương ứng.

### Giải thích: Phân tầng cùng một bài toán khi thay đổi hàm mục tiêu và ràng buộc

Xét biến quyết định $$x = (x_1, x_2) \in \mathbb{R}^2$$ với ngân sách cơ bản $$x_1 + x_2 \le 4,\; x_1, x_2 \ge 0$$:

1. **Tầng LP:** $$\min \; (-2x_1 - 3x_2)$$ trên tam giác trên. Hàm mục tiêu tuyến tính, ràng buộc tuyến tính. Nghiệm nằm tại đỉnh $$(0, 4)$$ với $$f^\star = -12$$.
2. **Tầng QP:** Thêm phạt rủi ro bậc hai: $$\min \; (-2x_1 - 3x_2 + \frac{1}{2}(x_1^2 + x_2^2))$$. Gradient bằng 0 tại $$(2, 3)$$, vi phạm $$2 + 3 = 5 > 4$$. Chiếu lên cạnh $$x_1 + x_2 = 4$$: thay $$x_2 = 4 - x_1$$ cho $$\phi(x_1) = x_1^2 - 3x_1 - 4$$, cực tiểu tại $$x_1^\star = 1.5,\; x_2^\star = 2.5$$ (nằm giữa cạnh chứ không ở đỉnh!), $$f^\star = -6.25$$.
3. **Tầng SOCP / QCQP:** Thêm ràng buộc năng lượng tròn $$\sqrt{x_1^2 + x_2^2} \le 2$$ (tương đương $$x_1^2 + x_2^2 \le 4$$) với mục tiêu tuyến tính $$\min (-2x_1 - 3x_2)$$. Theo Cauchy-Schwarz, $$-2x_1 - 3x_2 \ge -\sqrt{2^2 + 3^2}\sqrt{x_1^2 + x_2^2} = -2\sqrt{13} \approx -7.211$$, đạt tại $$x^\star = \frac{2}{\sqrt{13}}(2, 3) \approx (1.109, 1.664)$$ (thỏa $$x_1 + x_2 \approx 2.773 \le 4$$).
4. **Bài học rút ra:** Chỉ cần nhìn bậc của hàm mục tiêu và loại nón của ràng buộc, bạn biết ngay tầng nhỏ nhất cần gọi bộ giải!

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