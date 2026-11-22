---
layout: post
title: 13-06 Tinh tế đối ngẫu & Đối ngẫu kép
chapter: '13'
order: 10
owner: Wontak Ryu
categories:
- chapter13
lang: vi
---

## Một số lưu ý tinh tế về đối ngẫu

* Trong thực hành, ta thường biến đổi bài toán đối ngẫu sang một bài toán tối ưu tương đương gọn hơn và vẫn gọi đó là bài toán đối ngẫu. Khi tính đối ngẫu mạnh được thỏa mãn, nghiệm của bài toán đối ngẫu đã biến đổi vẫn có thể dùng để phân tích đặc trưng hoặc khôi phục nghiệm nguyên thủy.

#### Lưu ý
Giá trị mục tiêu tối ưu của bài toán đối ngẫu sau khi biến đổi (chẳng hạn bỏ hằng số hay đổi dấu) không nhất thiết bằng giá trị tối ưu của bài toán nguyên thủy.

* Một kỹ thuật phổ biến để xây dựng bài toán đối ngẫu cho bài toán không ràng buộc là đưa thêm các biến phụ và ràng buộc đẳng thức vào bài toán nguyên thủy. Cách biến đổi này không duy nhất; các cách đặt biến phụ khác nhau có thể dẫn tới những bài toán đối ngẫu khác nhau.

## Đối ngẫu kép

Xét bài toán cực tiểu hóa tổng quát với các ràng buộc tuyến tính:

> $$ \min_x f(x) \text{ với điều kiện } Ax \le b, \; Cx = d$$

Hàm Lagrangian tương ứng là:

> $$L(x,u,v) = f(x) + (A^Tu + C^Tv)^Tx - b^Tu - d^Tv$$

Từ đó, bài toán đối ngẫu có dạng:

> $$ \max_{u,v} -f^*(-A^Tu - C^Tv) - b^Tu - d^Tv \text{ với điều kiện } u \ge 0 $$

#### Nhắc lại tính chất

Nếu $$f$$ là hàm đóng và lồi, ta đã biết hàm liên hợp kép bằng chính hàm gốc ($$f^{**} = f$$), nên bài toán đối ngẫu của bài toán đối ngẫu chính là bài toán nguyên thủy.

Thực tế, tính chất này còn mở rộng vượt ra ngoài trường hợp ràng buộc tuyến tính. Xét bài toán tổng quát:

> $$ 
>\begin{align}
> & \min_x && f(x) \\
>&\text{ với điều kiện } && h_i(x) \le 0, \; i = 1,\dots,m \\
> &&&l_j(x) = 0, \; j = 1,\dots,r
>\end{align}$$

Nếu $$f$$ và các hàm $$h_1, \dots, h_m$$ đều đóng và lồi, còn $$l_1, \dots, l_r$$ là các hàm affine, thì đối ngẫu của đối ngẫu vẫn là bài toán nguyên thủy. Kết quả này được xây dựng từ góc nhìn lý thuyết hàm hai biến (xem thêm Chương 29 và Chương 30 trong sách của Rockafellar).
