---
layout: post
title: 02 Tập Lồi
chapter: '02'
order: 0
owner: Wontak Ryu
categories:
- chapter02
lang: vi
---

Trong chương này, chúng ta sẽ nghiên cứu khái niệm về tập lồi, tạo nền tảng cho tối ưu hóa lồi.

### Bối cảnh
Tối ưu hóa lồi đề cập đến các kỹ thuật tìm cực đại hoặc cực tiểu bằng cách định nghĩa các bài toán sử dụng hàm lồi.
Tập lồi có liên quan chặt chẽ với hàm lồi theo hai cách chính:

* Hàm lồi được định nghĩa trên tập lồi. Miền xác định và miền giá trị của một hàm được định nghĩa như các tập lồi, và các tính chất chính của hàm lồi được xác định bởi những tập hợp này.
* Nếu bạn có thể biến đổi một bài toán tối ưu hóa thành bài toán liên quan đến hàm lồi, nó sẽ trở nên dễ giải hơn. Đôi khi, khó xác định liệu một bài toán có được định nghĩa bởi hàm lồi hay không. Trong những trường hợp như vậy, bạn có thể kiểm tra xem epigraph của hàm có phải là tập lồi hay không để xác định hàm có lồi không.

### Nội dung
Trong chương này, chúng ta sẽ đề cập đến định nghĩa và ví dụ về tập lồi, các tính chất chính của chúng, và các phép toán bảo toàn tính lồi.