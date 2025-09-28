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

Khi bài toán nguyên thủy là lồi, các điều kiện Karush–Kuhn–Tucker (KKT) trở thành **điều kiện đủ** cho các điểm tối ưu nguyên thủy & đối ngẫu với độ lệch đối ngẫu bằng không. Ngoài ra, khi hàm mục tiêu và các hàm ràng buộc của bài toán nguyên thủy khả vi và thỏa mãn tính đối ngẫu mạnh, các điểm tối ưu nguyên thủy & đối ngẫu luôn thỏa mãn các điều kiện KKT. 

Các điều kiện KKT giữ một vị trí rất quan trọng trong tối ưu hóa. Những điều kiện này cho phép một số bài toán đặc biệt được giải một cách giải tích, và nhiều thuật toán tối ưu hóa lồi có thể được hiểu như các phương pháp để giải các điều kiện KKT [1]. Trong chương này, chúng ta sẽ tìm hiểu về định nghĩa và tính chất của các điều kiện KKT và xem xét một số ví dụ dựa trên chúng.

*Ghi chú bên lề*, các điều kiện KKT ban đầu được Harold W. Kuhn và Albert W. Tucker giới thiệu với thế giới vào năm 1951, và vào thời điểm đó chúng được gọi là điều kiện KT (Kuhn-Tucker). Sau đó, các học giả phát hiện ra rằng các điều kiện cần thiết cho bài toán này đã được William Karush đề cập trong luận văn thạc sĩ của ông vào năm 1939, và từ đó trở đi, tên của Karush được bao gồm và chúng được biết đến như các điều kiện KKT (Karush–Kuhn–Tucker) [3].