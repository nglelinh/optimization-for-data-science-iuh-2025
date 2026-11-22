---
layout: post
title: 14-06 Tự hài hòa (Self concordance)
chapter: '14'
order: 12
owner: Minjoo Lee
categories:
- chapter14
lang: vi
---
Phân tích hội tụ ở mục trước cho phương pháp Newton tồn tại hai hạn chế chính [1].

Thứ nhất, trong thực tế rất khó xác định các hằng số xuất hiện trong cận hội tụ như hằng số Lipschitz $$L$$ của gradient, tham số lồi mạnh $$m$$ hay hằng số Lipschitz $$M$$ của Hessian. Vì vậy, dù lý thuyết khẳng định tốc độ hội tụ, ta hầu như không thể tính trước số bước Newton cần thiết cho một bài toán cụ thể.

Thứ hai, bản thân phương pháp Newton bất biến affine, nhưng phân tích hội tụ cổ điển lại không bất biến affine. Với hàm tổng quát, các hằng số $$L, m, M$$ thay đổi theo phép biến đổi tọa độ.

Vì hai lý do trên, mục này giới thiệu lớp **hàm tự hài hòa (self-concordant functions)** nhằm khắc phục cả hai hạn chế.

Các hàm tự hài hòa có vai trò quan trọng vì ba lý do:

1. Các hàm chắn logarit dùng trong phương pháp điểm trong đều là hàm tự hài hòa (khi các ràng buộc bất đẳng thức là hàm affine hoặc bậc hai lồi).
2. Phân tích hội tụ của phương pháp Newton cho hàm tự hài hòa không phụ thuộc vào các hằng số khó ước lượng như $$L, m, M$$.
3. Tính tự hài hòa bất biến affine, nghĩa là cận số vòng lặp Newton không phụ thuộc vào phép biến đổi affine của hệ tọa độ.