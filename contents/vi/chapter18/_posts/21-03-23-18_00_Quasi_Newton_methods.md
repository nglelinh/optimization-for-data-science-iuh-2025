---
layout: post
title: 18-00 Phương pháp Quasi-Newton
chapter: '18'
order: 1
owner: Hooncheol Shin
categories:
- chapter18
lang: vi
---

Vào giữa thập niên 1950, máy tính điện tử vẫn chạy bằng đèn chân không và thường xuyên sập nguồn sau vài giờ hoạt động. Nhà vật lý William Davidon khi giải bài toán tối ưu nhiều chiều tại Phòng thí nghiệm Quốc gia Argonne đã bị đẩy vào thế bí: phương pháp hạ gradient thì quá chậm (máy sập trước khi hội tụ), còn phương pháp Newton thì đòi hỏi tính và nghịch đảo ma trận Hessian cỡ $$n \times n$$ quá sức chịu đựng của máy tính. Trong cái khó ló cái khôn, ông nảy ra một ý tưởng thiên tài: **chỉ cần nhìn cách gradient thay đổi sau mỗi bước đi, ta có thể tự "học" dần độ cong của hàm mà không bao giờ phải tính đạo hàm bậc hai!** Đó là sự ra đời của họ phương pháp Quasi-Newton.

## Bản đồ kiến thức nền: Bốn trụ cột của tối ưu hóa Quasi-Newton

Để nắm trọn bức tranh của Chương 18, hãy nhìn cách phương pháp Quasi-Newton đứng đúng ở "điểm ngọt" giữa phương pháp bậc nhất và phương pháp bậc hai:

- **Chi phí tính toán theo kích thước bài toán (Complexity Trade-off):** Hạ gradient chỉ tốn $$O(n)$$ mỗi bước nhưng hội tụ tuyến tính chậm chạp khi số điều kiện xấu; Newton hội tụ bậc hai nhưng tốn $$O(n^3)$$ để giải hệ tuyến tính Hessian; Quasi-Newton tốn $$O(n^2)$$ (và L-BFGS chỉ tốn $$O(mn)$$) nhưng vẫn đạt hội tụ siêu tuyến tính.
- **Phương trình Secant (Secant Equation):** Thay vì đo độ cong tại một điểm bằng đạo hàm bậc hai, ta buộc ma trận xấp xỉ $$B_{k+1}$$ khớp đúng với biến thiên gradient $$y_k = \nabla f(x_{k+1}) - \nabla f(x_k)$$ dọc theo bước đi $$s_k = x_{k+1} - x_k$$, tức $$B_{k+1} s_k = y_k$$.
- **Cập nhật hạng thấp bảo toàn cấu trúc (Low-Rank Updates):** Để ma trận xấp xỉ luôn đối xứng, xác định dương (đảm bảo hướng đi luôn là hướng giảm) và không phải tính lại từ đầu, các công thức SR1, DFP, BFGS chỉ cộng thêm một ma trận hiệu chỉnh hạng 1 hoặc hạng 2.
- **Nghịch đảo trực tiếp nhờ công thức Sherman–Morrison–Woodbury:** Thay vì cập nhật $$B_k$$ rồi giải hệ tuyến tính $$O(n^3)$$, ta cập nhật trực tiếp ma trận nghịch đảo $$H_k \approx (\nabla^2 f)^{-1}$$ chỉ bằng vài phép nhân vector–ma trận tốn $$O(n^2)$$.

### Khung giải thích (nên đọc chậm): So sánh chi phí $$O(n^3)$$ vs $$O(n^2)$$ và một bước cát tuyến 1 chiều

Hãy cảm nhận hai ưu điểm của Quasi-Newton bằng hai phép tính nhỏ:

1. **Chênh lệch chi phí khi $$n = 10{,}000$$ biến:**
   - **Newton chính xác:** Phân tích Cholesky ma trận Hessian dày đặc tốn cỡ $$\frac{1}{3}n^3 \approx 3.3 \times 10^{11}$$ phép tính mỗi vòng lặp — và riêng việc lưu trữ ma trận $$10^4 \times 10^4$$ số thực 64-bit đã ngốn $$800\text{ MB}$$ RAM.
   - **BFGS:** Mỗi vòng lặp chỉ cần vài phép nhân ma trận–vector tốn $$O(n^2) \approx 10^8$$ phép tính (nhanh hơn **hơn 3.000 lần** so với Newton!).
   - **L-BFGS (với $$m = 10$$ cặp lịch sử):** Chỉ tốn $$O(mn) \approx 10^5$$ phép tính và dưới $$2\text{ MB}$$ RAM.
2. **Trực giác 1 chiều trên hàm $$f(x) = \frac{1}{4}x^4 - x$$** (nghiệm tối ưu $$x^\star = 1$$, gradient $$f'(x) = x^3 - 1$$):
   - Khởi tạo tại $$x_0 = 2$$ ($$f'(2) = 7$$) và bước tới $$x_1 = 1.5$$ ($$f'(1.5) = 2.375$$).
   - Không cần tính đạo hàm bậc hai $$f''(x) = 3x^2$$, ta đo độ cong trung bình qua tỉ số cát tuyến:
     $$B_1 = \frac{f'(1.5) - f'(2)}{1.5 - 2} = \frac{2.375 - 7}{-0.5} = 9.25.$$
   - Bước Quasi-Newton tiếp theo là $$x_2 = x_1 - \frac{f'(x_1)}{B_1} = 1.5 - \frac{2.375}{9.25} \approx 1.2432$$ — tiến rất nhanh về $$x^\star = 1$$ mà chưa hề đụng tới đạo hàm bậc hai!

---

Vào giữa thập niên 1950, nhà vật lý W.C. Davidon khi làm việc tại Phòng thí nghiệm Quốc gia Argonne đã giải các bài toán tối ưu có khối lượng tính toán lớn bằng phương pháp hạ theo tọa độ (coordinate descent). Do máy tính thời đó thiếu ổn định và thường xuyên gặp sự cố trước khi phép tính hoàn tất, Davidon tìm cách tăng tốc độ hội tụ. Kết quả là thuật toán Quasi-Newton đầu tiên ra đời, mở ra bước tiến quan trọng cho tối ưu phi tuyến và kéo theo hàng loạt công trình nghiên cứu trong hai thập kỷ sau đó.

Trớ trêu thay, [nghiên cứu của Davidon](http://www.math.mcgill.ca/dstephens/680/Papers/Davidon91.pdf) khi ấy không được chấp nhận đăng và chỉ lưu hành dưới dạng báo cáo kỹ thuật suốt hơn 30 năm, trước khi chính thức được xuất bản trong [số đầu tiên của SIAM Journal on Optimization](https://epubs.siam.org/toc/sjope8/1/1) vào năm 1991.

Các phương pháp Quasi-Newton chỉ cần tính gradient của hàm mục tiêu ở mỗi vòng lặp. Nhờ đó, chi phí tính toán thấp hơn nhiều so với phương pháp Newton (vốn đòi hỏi đạo hàm bậc hai), đồng thời vẫn đạt tốc độ hội tụ siêu tuyến tính (superlinear convergence) [14].

## Động lực của phương pháp Quasi-Newton

Xét bài toán tối ưu trơn không ràng buộc:
> $$
> \min_x \: f(x), \\\\
> \text{trong đó } f \text{ khả vi hai lần, và } \operatorname{dom} f = \mathbb{R}^n.
> $$

Công thức cập nhật $$x$$ của phương pháp hạ gradient (Gradient Descent) và phương pháp Newton cho bài toán trên lần lượt là:
>**Phương pháp Gradient descent:**
>$$
>x^+ = x - t \nabla f(x)
>$$

>**Phương pháp Newton:**
>$$
>x^+ = x - t \nabla^2 f(x)^{-1} \nabla f(x)
>$$

Phương pháp Newton có ưu điểm là đạt tốc độ hội tụ bậc hai ($$O(\log \log (1/\epsilon))$$), nhưng gặp trở ngại lớn về chi phí tính toán ở hai bước sau:

* **Tính và lưu trữ ma trận Hessian $$\nabla^2 f(x)$$:** Việc tính và lưu trữ Hessian đòi hỏi bộ nhớ $$O(n^2)$$, không phù hợp khi làm việc với các bài toán có số chiều lớn (tham khảo: [Ma trận Hessian](https://en.wikipedia.org/wiki/Hessian_matrix#Use_in_optimization) trên Wikipedia).
* **Giải hệ phương trình $$\nabla^2 f(x) p = -\nabla f(x)$$:** Chi phí giải hệ tuyến tính (hoặc nghịch đảo Hessian) lên tới $$O(n^3)$$ ở mỗi bước (tham khảo: [Độ phức tạp tính toán của Đại số Ma trận](https://en.wikipedia.org/wiki/Computational_complexity_of_mathematical_operations#Matrix_algebra) trên Wikipedia).

Phương pháp Quasi-Newton khắc phục điều này bằng cách dùng một ma trận xấp xỉ $$B$$ thay cho $$\nabla^2 f(x)$$:
>**Phương pháp Quasi-Newton:**
>$$
>x^+ = x + tp \\\\
>\text{trong đó } Bp = -\nabla f(x).
>$$

Ở đây, ma trận $$B$$ cần dễ cập nhật và cho phép giải nhanh hệ phương trình $$Bp = g$$.

## Thuật toán Quasi-Newton
Khung thuật toán Quasi-Newton tổng quát gồm các bước:

* Chọn điểm khởi tạo $$x^0$$ và ma trận $$B^0$$ ban đầu.
* Với $$k = 0, 1, \dots$$:
    * Giải hệ $$B^k p^k = - \nabla f(x^k)$$.
    * Chọn độ dài bước $$t_k$$ và đặt $$x^{k+1} = x^{k} + t_k p^k$$.
    * Cập nhật $$B^k$$ thành $$B^{k+1}$$.
* Kết thúc khi đạt điều kiện dừng.

Điểm cốt lõi của lớp phương pháp này là cách cập nhật $$B$$ qua từng vòng lặp để ngày càng xấp xỉ tốt hơn độ cong của hàm mục tiêu quanh nghiệm tối ưu. Cách xây dựng $$B^+$$ từ $$B$$ sẽ là nội dung trọng tâm xuyên suốt chương này. (**Lưu ý:** Để trình bày gọn gàng, chúng ta dùng song song hai cặp ký hiệu $$B^{k+1}, B^k$$ và $$B^+, B$$.)