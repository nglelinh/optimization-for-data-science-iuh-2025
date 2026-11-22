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

Nhìn chung, các bộ giải quy hoạch tuyến tính (LP) hiện đại hàng đầu đều kết hợp cả phương pháp đơn hình (Simplex) và phương pháp điểm trong.

* Dantzig (thập niên 1940): Phương pháp đơn hình — phương pháp đầu tiên giải LP dạng tổng quát và tìm được nghiệm chính xác sau một số hữu hạn bước. Đến nay, đây vẫn là một trong những thuật toán nổi tiếng và được nghiên cứu nhiều nhất cho LP.

* Klee và Minty (1972): Xây dựng một lớp bài toán LP "bệnh lý" (Klee–Minty cube) gồm $$n$$ biến và $$2n$$ ràng buộc, khiến phương pháp đơn hình cần tới $$2^n$$ vòng lặp trong trường hợp xấu nhất.

* Khachiyan (1979): Đề xuất thuật toán thời gian đa thức đầu tiên cho LP dựa trên phương pháp ellipsoid của Nemirovski và Yudin (1976); kết quả này có ý nghĩa lý thuyết lớn nhưng không hiệu quả trong thực tế.

* Karmarkar (1984): Đề xuất phương pháp điểm trong thời gian đa thức cho LP có hiệu năng thực tế tốt, tạo bước ngoặt lớn cho lĩnh vực tối ưu hóa (Bằng sáng chế Hoa Kỳ 4,744,026, hết hạn năm 2006).

* Renegar (1988): Phát triển thuật toán điểm trong dựa trên phương pháp Newton cho LP, đạt độ phức tạp tính toán lý thuyết tốt nhất cho đến khi có các cải tiến gần đây hơn của Lee–Sidford.
