---
layout: post
title: 14-06 Tự hài hòa (Self concordance)
chapter: '14'
order: 10
owner: Minjoo Lee
categories:
- chapter14
lang: vi
---
Trong phân tích hội tụ trước đây của phương pháp Newton, có hai vấn đề chính. [1]

Thứ nhất, trong các bài toán thực tế, rất khó tìm hằng số Lipschitz L, các cận dưới và trên của tính lồi mạnh m, M, v.v., được bao gồm trong các công thức. Vì điều này, trong khi chúng ta có thể quan sát sự hội tụ và tốc độ hội tụ, việc phân tích cần bao nhiêu bước Newton trong thực tế là gần như bất khả thi.

Thứ hai, mặc dù bản thân phương pháp Newton là bất biến affine, nhưng phân tích hội tụ của phương pháp Newton không bất biến affine. Đối với các hàm tổng quát, giá trị của hằng số Lipschitz hoặc các cận tính lồi mạnh thay đổi tùy thuộc vào phép biến đổi tọa độ.

Do đó, trong chương này, chúng ta giới thiệu các hàm tự hài hòa, giải quyết hai vấn đề trên.

Các hàm tự hài hòa quan trọng và có ý nghĩa vì ba lý do chính:

1. Các hàm rào cản logarit được sử dụng trong các phương pháp điểm nội là các hàm tự hài hòa.
2. Trong phân tích phương pháp Newton cho các hàm tự hài hòa, các số hạng liên quan đến hằng số không xuất hiện.
3. Tính tự hài hòa là bất biến affine. Tức là, số lần lặp Newton cần thiết không phụ thuộc vào các phép biến đổi affine của hệ tọa độ.