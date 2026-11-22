---
layout: post
title: 12 Điều Kiện KKT
chapter: '12'
order: 1
owner: Wontak Ryu
categories:
- chapter12
lang: vi
---

Khi bài toán nguyên thủy là bài toán lồi, các điều kiện Karush–Kuhn–Tucker (KKT) là **điều kiện đủ** để các điểm nguyên thủy và đối ngẫu đạt tối ưu với khoảng cách đối ngẫu bằng không. Bên cạnh đó, nếu hàm mục tiêu và các hàm ràng buộc của bài toán nguyên thủy khả vi và bài toán thỏa mãn tính đối ngẫu mạnh, thì mọi cặp nghiệm tối ưu nguyên thủy và đối ngẫu đều phải thỏa mãn các điều kiện KKT.

Các điều kiện KKT giữ vai trò quan trọng trong tối ưu hóa. Nhờ chúng, nhiều bài toán có cấu trúc đặc biệt có thể được giải bằng phương pháp giải tích, đồng thời nhiều thuật toán tối ưu hóa lồi cũng có thể được xem là các phương pháp đi tìm nghiệm của hệ điều kiện KKT [1]. Trong chương này, chúng ta sẽ tìm hiểu định nghĩa, tính chất của các điều kiện KKT và phân tích một số ví dụ minh họa.

*Ghi chú lịch sử:* Các điều kiện KKT ban đầu được Harold W. Kuhn và Albert W. Tucker công bố vào năm 1951 và khi đó được gọi là điều kiện KT (Kuhn–Tucker). Về sau, giới nghiên cứu phát hiện ra rằng các điều kiện cần tương tự đã được William Karush trình bày trong luận văn thạc sĩ năm 1939; từ đó tên của Karush được bổ sung và hệ điều kiện này mang tên KKT (Karush–Kuhn–Tucker) [3].

## Ứng dụng hiện đại (2022–2026)

Bài đọc tùy chọn đi kèm trình bày cách hệ KKT xuất hiện trong cvxpylayers và Theseus, các vector hỗ trợ của SVM, giá biên theo vị trí (LMP) trong thị trường điện và các ràng buộc công bằng đang chặt. Xem [12-07 Ứng dụng hiện đại của điều kiện KKT]({% multilang_post_url contents/chapter12/2026-09-16-12_07_modern_applications %}).
