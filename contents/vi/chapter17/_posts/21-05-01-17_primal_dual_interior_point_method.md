---
layout: post
title: '17 Phương pháp điểm trong gốc-đối ngẫu'
chapter: '17'
order: 1
owner: Minjoo Lee
categories:
- chapter17
lang: vi
---

Trong chương này, chúng ta tìm hiểu **phương pháp điểm trong gốc-đối ngẫu (Primal-Dual Interior-Point Method)** — phương pháp cải thiện hiệu năng bằng cách rút gọn bước định tâm (centering) của phương pháp chắn xuống chỉ còn một bước Newton ở mỗi vòng lặp.

**Phương pháp điểm trong gốc-đối ngẫu** nới lỏng yêu cầu phải giữ nghiệm luôn khả thi trong bước định tâm, đồng thời áp dụng phiên bản tìm nghiệm (root-finding) của phương pháp Newton để tuyến tính hóa hệ phương trình phi tuyến. Nhờ đó, thuật toán thường hội tụ nhanh hơn và đạt độ chính xác cao hơn so với phương pháp chắn.

## Tài liệu tham khảo và đọc thêm
* S. Boyd and L. Vandenberghe (2004), “Convex optimization,” Chapter 11
* S. Wright (1997), “Primal-dual interior-point methods,” Chapters 5 and 6
* J. Renegar (2001), “A mathematical view of interior-point methods”
* Y. Nesterov and M. Todd (1998), “Primal-dual interior-point methods for self-scaled cones.” SIAM J. Optim.
