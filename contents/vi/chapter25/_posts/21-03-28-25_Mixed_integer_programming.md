---
layout: post
title: 25 Quy Hoạch Số Nguyên Hỗn Hợp (Phần II)
chapter: '25'
order: 1
owner: YoungJae Choung
categories:
- chapter25
lang: vi
---

Chương này trình bày thuật toán mặt phẳng cắt (cutting plane) — một trong những công cụ cốt lõi của quy hoạch nguyên (IP) — cùng thuật toán nhánh và cắt (branch and cut), là sự kết hợp được triển khai phổ biến nhất trong các bộ giải thực tế.

Tiếp theo, chương minh họa hai ví dụ mở rộng của quy hoạch nguyên hỗn hợp trong thống kê: chọn tập con tốt nhất (best subset selection) và hồi quy bình phương trung vị nhỏ nhất / hồi quy phân vị nhỏ nhất (least median of squares / least quantile regression).

## Tài liệu tham khảo

* Belotti, Kirches, Leyffer, Linderoth, Luedke, and Mahajan (2012), "Mixed-integer nonlinear optimization"
* Bertsimas and Mazumder (2016), "Best subset selection via a modern optimization lens"
* Bertsimas, King, and Mazumder (2014), "Least quantile regression via modern optimization"
* Conforti, Cornuejols, and Zambelli (2014), "Integer programming"
* Wolsey (1998), "Integer programming"

## Ứng dụng giai đoạn 2022–2026 (tùy chọn)

Bài toán chọn tập con tốt nhất bằng MIP vẫn là ví dụ tiêu biểu trong thống kê; cùng kỹ thuật mã hóa big-$$M$$ cho hàm kích hoạt ReLU hiện còn được dùng để chọn đặc trưng cho mạng nơ-ron đã huấn luyện, *chứng nhận* độ bền vững đối kháng và xây dựng cây phân loại tối ưu. Bên cạnh đó, các nghiên cứu năm 2024 về học quy tắc chọn mặt phẳng cắt kiểu Gomory biến chính quy trình ở mục 25-01 thành bài toán học máy. Đọc thêm tại bài tùy chọn: [25-03 Ứng dụng hiện đại của MIP trong khoa học dữ liệu]({% multilang_post_url contents/chapter25/2026-09-16-25_03_modern_applications %}).
