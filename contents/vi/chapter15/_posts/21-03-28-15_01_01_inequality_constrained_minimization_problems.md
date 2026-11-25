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

Trước thế kỷ 20 cuối những năm 1980, nếu cần giải một bài toán quy hoạch tuyến tính có ràng buộc bất đẳng thức, hầu như mọi kỹ sư đều nghĩ ngay đến **thuật toán Đơn hình (Simplex)** — thuật toán "bò men theo từng cạnh và đỉnh" ở vỏ ngoài của khối đa diện khả thi. Simplex chạy rất nhanh trên nhiều bài toán thực tế, nhưng trong trường hợp xấu nhất (khối lập phương Klee–Minty), nó phải đi qua số đỉnh tăng theo hàm mũ!

**Phương pháp điểm trong (Interior-Point Method)** tạo ra một cuộc cách mạng tư duy ngược hoàn toàn: thay vì men theo các góc nhọn ở vỏ ngoài, nó **đâm xuyên qua phần ruột (miền trong)** của tập khả thi! Để làm được điều đó, bài học này bắt đầu bằng việc phát biểu chuẩn bài toán tối ưu lồi có cả ràng buộc đẳng thức lẫn bất đẳng thức và chuyển hóa nó sang bài toán chỉ có ràng buộc đẳng thức thông qua hàm chỉ thị.

## Kiến thức cần nhớ: Bối cảnh bài toán chuẩn và điều kiện cần của phương pháp điểm trong

- **Dạng chuẩn bài toán tối ưu lồi trơn:** $$\min_x f(x)$$ thỏa $$Ax = b$$ và $$h_i(x) \le 0$$ ($$i = 1, \dots, m$$), trong đó $$f, h_1, \dots, h_m$$ lồi và khả vi hai lần liên tục.
- **Điều kiện khả thi chặt (Slater's Condition):** Phải tồn tại ít nhất một điểm $$x$$ nằm hoàn toàn bên trong miền ràng buộc bất đẳng thức ($$h_i(x) < 0$$ với mọi $$i$$ và $$Ax = b$$). Điều này vừa đảm bảo miền trong khác rỗng cho phương pháp điểm trong, vừa đảm bảo **đối ngẫu mạnh** và tồn tại nghiệm KKT!
- **Hàm chỉ thị $$I_-(u)$$ như bước đệm khái niệm:** Viết lại ràng buộc $$h_i(x) \le 0$$ bằng cách cộng $$\sum I_-(h_i(x))$$ vào $$f(x)$$ xóa sạch ràng buộc bất đẳng thức về mặt hình thức, mở đường cho bước thay $$I_-$$ bằng hàm chắn trơn ở bài tiếp theo.

### Giải thích: Phân biệt miền khả thi, biên và miền trong chặt trên một đa giác nhỏ

Xét bài toán trên $$\mathbb{R}^2$$ với 3 ràng buộc bất đẳng thức:
$$h_1(x) = -x_1 \le 0, \qquad h_2(x) = -x_2 \le 0, \qquad h_3(x) = x_1 + x_2 - 2 \le 0.$$

1. **Kiểm tra điểm $$x_A = (0, 0)^T$$:**
   $$h_1(x_A) = 0, \quad h_2(x_A) = 0, \quad h_3(x_A) = -2 < 0.$$
   Điểm $$x_A$$ là **khả thi** (nằm trên góc biên tam giác), nên hàm chỉ thị $$\sum I_-(h_i(x_A)) = 0$$, nhưng **không khả thi chặt** (vì $$h_1 = h_2 = 0$$, nên $$\log(-h_1)$$ không xác định!).
2. **Kiểm tra điểm $$x_B = (0.5, 0.5)^T$$:**
   $$h_1(x_B) = -0.5 < 0, \quad h_2(x_B) = -0.5 < 0, \quad h_3(x_B) = -1 < 0.$$
   Điểm $$x_B$$ là **khả thi chặt** (nằm hoàn toàn trong ruột tam giác), chứng minh điều kiện Slater thỏa mãn và có thể dùng làm điểm xuất phát cho phương pháp điểm trong!
3. **Kiểm tra điểm $$x_C = (1.5, 1)^T$$:**
   $$h_3(x_C) = 0.5 > 0 \implies I_-(h_3(x_C)) = +\infty$$ — vi phạm ràng buộc, bị hàm chỉ thị loại bỏ ngay lập tức.

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
