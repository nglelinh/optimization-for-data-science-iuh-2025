---
layout: post
title: '15-01-01 Bài toán cực tiểu hóa có ràng buộc bất đẳng thức'
chapter: '15'
order: 3
owner: Minjoo Lee
categories:
- chapter15
lang: vi
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>
Hãy xét bài toán tối ưu lồi sau.
>
$$\begin{align}
&\min_{x}           && f(x) \\ 
&\text{subject to } && Ax = b \\
                    &&& h_{i}(x) \leq 0, i = 1, \dotsc, m
\end{align}$$

Trong các bài toán có ràng buộc bất đẳng thức như thế này, rất khó phân biệt ràng buộc chặt (binding) và ràng buộc không chặt (non-binding), đặc biệt là ở biên của miền khả thi. Ràng buộc chặt là các ràng buộc ảnh hưởng đến nghiệm.

Do đó, **phương pháp điểm trong (interior method)** là cách tiếp cận cố gắng giải bài toán từ bên trong miền khả thi chứ không phải ở biên.

## Bối cảnh của phương pháp điểm trong
**Phương pháp điểm trong** cho các bài toán tổng quát được Anthony V. Fiacco và Garth P. McCormick đề xuất vào những năm 1960. Vào thời điểm đó, nó bị lu mờ bởi các phương pháp phổ biến như quy hoạch toàn phương tuần tự (sequential quadratic programming) và phương pháp tập tích cực (active set method), và chỉ được chú ý trở lại vào những năm 1980.

Phương pháp tập tích cực là một lý thuyết để xác định ràng buộc nào ảnh hưởng đến kết quả tối ưu. Trong phương pháp tập tích cực, một ràng buộc được coi là tích cực (active) nếu nó bằng 0, và các ràng buộc như vậy được gọi là tập tích cực. Tuy nhiên, để tìm tập tích cực cần tính biên của miền khả thi, và khi số ràng buộc tăng lên thì chi phí tính toán cũng tăng theo.

Nhận ra những vấn đề này, phương pháp điểm trong được phát triển để giải bài toán từ bên trong thay vì từ biên. Ví dụ, trong LP, nếu có $$m$$ ràng buộc thì việc tính biên đòi hỏi $$O(m^2)$$ phép tính, nhưng với phương pháp điểm trong, ngay cả khi $$m$$ lớn, nghiệm vẫn có thể tìm được trong 20–30 bước Newton. Chi tiết hơn về hiệu năng sẽ được bàn ở phần sau.

* Tham khảo: [Interior point method](https://en.wikipedia.org/wiki/Interior-point_method)
* Tham khảo: [Active set method](https://en.wikipedia.org/wiki/Active_set_method)

## Rút gọn bài toán cực tiểu hóa có ràng buộc đẳng thức
Bài toán trên có thể được viết lại với $$C := \{x : h_i(x) \le 0, i = 1, \cdots , m \}$$. Các ràng buộc bất đẳng thức có thể được đưa vào hàm mục tiêu dưới dạng hàm chỉ thị (indicator function).

>$$\begin{align}
&\min_{x} \ && f(x) + I_C(x) \\
&\text{subject to }\  && Ax = b \\
\end{align}$$

Bằng cách này, bài toán được chuyển thành bài toán cực tiểu hóa có ràng buộc đẳng thức. Tuy nhiên, vì hàm chỉ thị vẫn bao gồm biên nên vẫn còn khó khăn về việc tính biên như ở bài toán ban đầu, và vì nó không khả vi nên khó áp dụng phương pháp Newton.

Điều gì xảy ra nếu ta xấp xỉ hàm chỉ thị $$I_C$$ bằng một **hàm chắn (barrier function)**? Khi đó biên sẽ không được bao gồm, và vì hàm chắn khả vi nên có thể áp dụng phương pháp Newton.

Phương pháp giải bài toán được định nghĩa lại bằng hàm chắn như vậy được gọi là phương pháp chắn (barrier method), sẽ được giới thiệu chi tiết ở phần tiếp theo.
