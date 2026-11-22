---
layout: post
title: 28-03 Quá tham số
chapter: '28'
order: 4
owner: Nguyen Le Linh
categories:
- chapter28
lang: vi
lesson_type: required
---


Một mô hình được gọi là **quá tham số hóa (overparameterized)** khi số lượng tham số $$d$$ lớn hơn đáng kể so với số ràng buộc hiệu dụng từ dữ liệu huấn luyện (trường hợp kinh điển là $$d \gg n$$ để nội suy $$n$$ nhãn vô hướng). Khi đó, phương trình $$F(w)=0$$ (tức hàm mất mát huấn luyện xấp xỉ 0) có cả một **tập nghiệm rất lớn**. Quá trình huấn luyện không còn là bài toán “tìm cực tiểu duy nhất”, mà trở thành câu hỏi: *thuật toán tối ưu sẽ chọn nghiệm nội suy nào trong số đó?*

Đây chính là góc nhìn **thiên kiến ẩn (implicit bias)**. Trên bài toán bình phương tối thiểu thiếu xác định, gradient descent xuất phát từ gốc hội tụ về nghiệm nội suy có **chuẩn $$\ell_2$$ nhỏ nhất** trong không gian sinh bởi các đặc trưng; trên bài toán phân loại tuyến tính tách được, nó hội tụ theo hướng cực đại hóa lề (Soudry và cộng sự, cùng nhiều nghiên cứu nối tiếp). Dù mạng nơ-ron sâu là phi tuyến, nguyên lý cốt lõi vẫn giữ nguyên: **thuật toán tối ưu là một phần của thiên kiến quy nạp (inductive bias)**.

Quá tham số hóa cũng làm thay đổi hình học của $$F$$. Trong nhiều chế độ mô hình đặc trưng ngẫu nhiên và mạng đủ rộng, bề mặt hàm mất mát trở nên thuận lợi về mặt cục bộ: khi điểm lặp đã vào đủ gần, mọi điểm tới hạn mà SGD gặp đều nội suy dữ liệu huấn luyện, nên câu hỏi chính không còn là có bị kẹt ở điểm yên ngựa hay không mà là mô hình hội tụ tới *điểm nội suy nào*. Điều này giải thích vì sao nhận định “không lồi thì chắc chắn kẹt ở cực tiểu địa phương xấu” không phản ánh đúng thực tế của học sâu hiện đại.

**Điều kiện Polyak–Łojasiewicz (PL)** (giới thiệu ngắn gọn). Nếu hàm $$F$$ thỏa mãn:

$$
\tfrac12 \|\nabla F(w)\|_2^2 \ge \mu \bigl(F(w)-F^\star\bigr)
$$

với hằng số $$\mu>0$$, thì gradient descent vẫn đạt tốc độ hội tụ tuyến tính *mà không cần tính lồi*. Nhiều bài toán bình phương tối thiểu quá tham số hóa và một số chế độ mạng rộng thỏa điều kiện PL cục bộ. Bài tùy chọn [28-05]({% multilang_post_url contents/chapter28/2026-09-18-28_05_pl_condition %}) trình bày chi tiết cách kế thừa chứng minh Chương 06 cho bất đẳng thức này (Karimi, Nutini & Schmidt, [arXiv:1608.04636](https://arxiv.org/abs/1608.04636)).

**Bài tập.** Khớp $$n=20$$ điểm dữ liệu vô hướng bằng một đa thức bậc $$50$$ theo hai cách: (i) nghiệm chuẩn tối thiểu từ `numpy.linalg.lstsq` và (ii) gradient descent xuất phát từ hai điểm khởi tạo ngẫu nhiên khác nhau. So sánh sai số kiểm tra trên một hàm gốc trơn: cả hai đều đạt mất mát huấn luyện gần bằng 0 nhưng cho ra các nghiệm nội suy khác nhau.
