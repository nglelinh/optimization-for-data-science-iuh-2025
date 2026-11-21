---
layout: post
title: '17-03 Một chút lịch sử'
chapter: '17'
order: 7
owner: Minjoo Lee
categories:
- chapter17
lang: vi
---

Nhìn chung, các bộ giải LP hiện đại hàng đầu sử dụng cả phương pháp đơn hình (Simplex) và phương pháp điểm trong.

* Dantzig (thập niên 1940): Phương pháp đơn hình, phương pháp đầu tiên giải LP dạng tổng quát, thu được nghiệm chính xác sau một số hữu hạn bước. Cho đến nay nó vẫn là một trong những thuật toán nổi tiếng và được nghiên cứu nhiều nhất cho LP.

* Klee và Minty (1972): Một bài toán LP "bệnh lý" với $$n$$ biến và $$2n$$ ràng buộc. Giải bằng phương pháp đơn hình cần $$2^n$$ vòng lặp.

* Khachiyan (1979): Thuật toán thời gian đa thức cho LP dựa trên phương pháp ellipsoid của Nemirovski và Yudin (1976); về mặt lý thuyết rất mạnh nhưng trong thực tế thì không.

* Karmarkar (1984): Phương pháp LP điểm trong thời gian đa thức khá hiệu quả và trở thành một nghiên cứu đột phá. (Bằng sáng chế Hoa Kỳ 4,744,026, hết hạn năm 2006).

* Renegar (1988): Thuật toán điểm trong dựa trên Newton cho LP. Nó có độ phức tạp tính toán tốt nhất về mặt lý thuyết cho đến khi có nghiên cứu mới nhất của Lee–Sidford.
