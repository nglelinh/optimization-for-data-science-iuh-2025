---
layout: post
title: '17-02 Phương pháp điểm trong gốc-đối ngẫu'
chapter: '17'
order: 3
owner: Minjoo Lee
categories:
- chapter17
lang: vi
---

Tương tự phương pháp chắn, **phương pháp điểm trong gốc-đối ngẫu** cũng nhằm tính xấp xỉ các điểm dọc theo đường trung tâm. Tuy nhiên, giữa hai phương pháp có một số điểm khác biệt quan trọng.

## Khác biệt giữa phương pháp điểm trong gốc-đối ngẫu và phương pháp chắn
* Thông thường chỉ thực hiện **một bước Newton** ở mỗi vòng lặp (không cần vòng lặp trong riêng cho bước định tâm — centering).
* **Các điểm lặp không nhất thiết phải khả thi** trong quá trình chạy (thuật toán đưa điểm lặp tiến dần về miền khả thi kết hợp với tìm kiếm theo đường lui — backtracking line search).
* Thường **hiệu quả hơn** trong thực tế; đặc biệt dưới các điều kiện phù hợp, phương pháp đạt tốc độ hội tụ nhanh hơn hội tụ tuyến tính.
* Kém trực quan hơn một chút so với phương pháp chắn.
