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

Giống như phương pháp chắn, **phương pháp điểm trong gốc-đối ngẫu** cũng nhằm tính (xấp xỉ) các điểm trên đường trung tâm. Tuy nhiên, hai phương pháp có một số điểm khác biệt.

## Khác biệt giữa phương pháp điểm trong gốc-đối ngẫu và phương pháp chắn
* Thông thường chỉ thực hiện **một bước Newton** mỗi vòng lặp. (Tức là không có vòng lặp bổ sung cho bước centering.)
* **Không nhất thiết phải khả thi**. (Đẩy về miền khả thi thông qua backtracking line search.)
* Thông thường **hiệu quả hơn**. Đặc biệt, trong điều kiện thích hợp nó cho hiệu năng vượt trội so với hội tụ tuyến tính.
* Hơi kém trực quan hơn so với phương pháp chắn.
