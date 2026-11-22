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