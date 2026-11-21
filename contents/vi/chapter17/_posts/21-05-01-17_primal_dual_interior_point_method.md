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

Trong chương này, chúng ta sẽ tìm hiểu **phương pháp điểm trong gốc-đối ngẫu (Primal-Dual Interior-Point Method)**, phương pháp cải thiện hiệu năng bằng cách rút gọn bước centering của phương pháp chắn đã học trước đó xuống chỉ còn một bước.

**Phương pháp điểm trong gốc-đối ngẫu** nới lỏng ràng buộc rằng bước centering phải khả thi, và dùng phiên bản tìm nghiệm của phương pháp Newton để xấp xỉ các phương trình phi tuyến bằng phương trình tuyến tính nhằm tìm nghiệm, nhờ đó nhanh hơn và chính xác hơn phương pháp chắn.

## Tài liệu tham khảo và đọc thêm
* S. Boyd and L. Vandenberghe (2004), “Convex optimization,” Chapter 11
* S. Wright (1997), “Primal-dual interior-point methods,” Chapters 5 and 6
* J. Renegar (2001), “A mathematical view of interior-point methods”
* Y. Nesterov and M. Todd (1998), “Primal-dual interior-point methods for self-scaled cones.” SIAM J. Optim.
