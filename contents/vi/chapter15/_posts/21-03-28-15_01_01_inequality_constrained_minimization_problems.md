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

Xét bài toán tối ưu lồi sau:
>
$$\begin{align}
&\min_{x}           && f(x) \\ 
&\text{subject to } && Ax = b \\
                    &&& h_{i}(x) \leq 0, i = 1, \dotsc, m
\end{align}$$

Với các bài toán có ràng buộc bất đẳng thức, việc phân biệt ràng buộc chặt (binding — ràng buộc ảnh hưởng trực tiếp đến nghiệm tối ưu) và ràng buộc không chặt (non-binding) thường khó khăn, đặc biệt khi xét trên biên của miền khả thi.

Do đó, **phương pháp điểm trong (interior-point method)** tiếp cận bài toán bằng cách tìm nghiệm đi từ bên trong miền khả thi thay vì lần theo biên.

## Bối cảnh của phương pháp điểm trong
**Phương pháp điểm trong** cho các bài toán tối ưu tổng quát được Anthony V. Fiacco và Garth P. McCormick đề xuất vào những năm 1960. Thời điểm đó, cách tiếp cận này ít được chú ý hơn so với các phương pháp phổ biến như quy hoạch toàn phương tuần tự (sequential quadratic programming) hay phương pháp tập tích cực (active set method), và chỉ thực sự phát triển mạnh trở lại từ thập niên 1980.

Phương pháp tập tích cực tìm cách xác định tập các ràng buộc đang có giá trị bằng 0 tại nghiệm (gọi là tập tích cực). Tuy nhiên, việc xác định tập này đòi hỏi phải khảo sát biên của miền khả thi, nên chi phí tính toán tăng nhanh khi số lượng ràng buộc lớn.

Nhằm khắc phục hạn chế đó, phương pháp điểm trong giải bài toán ngay từ phần trong của miền khả thi. Chẳng hạn, với quy hoạch tuyến tính (LP) gồm $$m$$ ràng buộc, việc tính toán trên biên có thể tốn $$O(m^2)$$ phép tính, trong khi phương pháp điểm trong thường chỉ cần khoảng 20–30 bước Newton ngay cả khi $$m$$ lớn. Hiệu năng của phương pháp sẽ được phân tích chi tiết ở các mục sau.

* Tham khảo: [Interior point method](https://en.wikipedia.org/wiki/Interior-point_method)
* Tham khảo: [Active set method](https://en.wikipedia.org/wiki/Active_set_method)

## Đưa về bài toán cực tiểu hóa có ràng buộc đẳng thức
Đặt $$C := \{x : h_i(x) \le 0, i = 1, \cdots , m \}$$. Ta có thể đưa toàn bộ các ràng buộc bất đẳng thức vào hàm mục tiêu thông qua hàm chỉ thị (indicator function) $$I_C(x)$$:

>$$\begin{align}
&\min_{x} \ && f(x) + I_C(x) \\
&\text{subject to }\  && Ax = b \\
\end{align}$$

Dạng bài toán này chỉ còn ràng buộc đẳng thức. Tuy nhiên, vì hàm chỉ thị $$I_C$$ vẫn chứa biên của $$C$$ và không khả vi, khó khăn ở biên chưa được giải quyết và ta vẫn không thể áp dụng trực tiếp phương pháp Newton.

Nếu thay hàm chỉ thị $$I_C$$ bằng một **hàm chắn (barrier function)** trơn, miền xác định sẽ nằm hoàn toàn trong phần trong của $$C$$ (không chứa biên) và hàm mục tiêu trở nên khả vi hai lần, cho phép áp dụng phương pháp Newton.

Cách tiếp cận giải bài toán xấp xỉ bằng hàm chắn này được gọi là **phương pháp chắn (barrier method)**, sẽ được trình bày chi tiết ở mục tiếp theo.
