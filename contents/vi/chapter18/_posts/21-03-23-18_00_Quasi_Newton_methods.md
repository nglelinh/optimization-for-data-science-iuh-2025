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

Vào giữa những năm 1950, nhà vật lý W.C. Davidon, người đang làm việc tại Phòng thí nghiệm Quốc gia Argonne, đã giải quyết các bài toán tối ưu với yêu cầu tính toán lớn bằng phương pháp coordinate descent. Không may, do sự bất ổn của máy tính vào thời điểm đó, hệ thống thường xuyên bị sập trước khi các tính toán có thể được hoàn thành, và bực bội với điều này, Davidon quyết định tìm các phương pháp có thể cải thiện tốc độ tính toán. Điều này dẫn đến sự ra đời của thuật toán Quasi-Newton đầu tiên. Đây trở thành chất xúc tác cho sự tiến bộ đáng kể trong tối ưu phi tuyến, và sau đó, nhiều nghiên cứu tiếp theo về phương pháp này đã xuất hiện trong 20 năm tiếp theo.

Một cách trớ trêu, [nghiên cứu của Davidon](http://www.math.mcgill.ca/dstephens/680/Papers/Davidon91.pdf) không được công bố vào thời điểm đó và vẫn là một báo cáo kỹ thuật trong hơn 30 năm. Nó cuối cùng đã được xuất bản trong [số đầu tiên của SIAM Journal on Optimization](https://epubs.siam.org/toc/sjope8/1/1) vào năm 1991.

Các phương pháp Quasi-Newton chỉ yêu cầu gradient của hàm mục tiêu tại mỗi vòng lặp. Điều này có gánh nặng tính toán ít hơn nhiều so với phương pháp Newton yêu cầu đạo hàm bậc hai, và hơn nữa còn cho thấy sự hội tụ siêu tuyến tính, khiến nó trở thành một phương pháp đủ hấp dẫn [14]. 

## Động lực cho phương pháp Quasi-Newton

Xét bài toán tối ưu trơn không ràng buộc sau:
> $$
> \min_x \: f(x), \\\\
> \text{trong đó } f \text{ khả vi hai lần, và } dom \; f = \mathbb{R}^n.
> $$

Các phương pháp cập nhật cho x trong phương pháp Gradient descent và phương pháp Newton cho bài toán trên như sau:
>**Phương pháp Gradient descent:**
>$$
>x^+ = x - t \nabla f(x)
>$$

>**Phương pháp Newton:**
>$$
>x^+ = x - t \nabla^2 f(x)^{-1} \nabla f(x)
>$$

Phương pháp Newton có ưu điểm là cho thấy tốc độ hội tụ bậc hai ($$O(\log \log 1/ \epsilon)$$), nhưng có vấn đề với chi phí tính toán cao đáng kể trong hai quá trình sau: 

* Tính toán Hessian $$\nabla^2 f(x)$$: Việc tính toán và lưu trữ ma trận Hessian yêu cầu bộ nhớ $$O(n^2)$$. Đây không phải là hiệu suất phù hợp để xử lý các hàm có chiều cao. (tham khảo: [Ma trận Hessian](https://en.wikipedia.org/wiki/Hessian_matrix#Use_in_optimization) trên Wikipedia)
* Giải phương trình $$\nabla^2 f(x) p = -\nabla f(x)$$: Để giải phương trình này, chúng ta phải tính ma trận nghịch đảo của Hessian $$\nabla^2 f(x)$$. (tham khảo: [Độ phức tạp tính toán của Đại số Ma trận](https://en.wikipedia.org/wiki/Computational_complexity_of_mathematical_operations#Matrix_algebra) trên Wikipedia)

Các phương pháp Quasi-Newton sử dụng một xấp xỉ $$B$$ thay vì $$\nabla^2 f(x)$$.
>**Phương pháp Quasi-Newton:**
>$$
>x^+ = x + tp \\\\
>\text{trong đó } Bp = -\nabla f(x).
>$$

Ở đây, B nên dễ tính toán, và cũng nên dễ giải phương trình $$Bp = g$$. 

## Thuật toán Quasi-Newton
Thuật toán Quasi-Newton như sau:

* Chọn $$x^0$$ và $$B^0$$ ban đầu
* Với $$k = 0, 1, \dots$$
    * Giải $$B^k p^k = - \nabla f(x^k)$$
    * Chọn $$t_k$$ và đặt $$x^{k+1} = x^{k} + t_k p^k$$
    * Cập nhật $$B^k$$ thành $$B^{k+1}$$
* Kết thúc

Một đặc điểm chính của phương pháp này là cập nhật $$B$$ để chúng ta có thể dần dần tiếp cận điểm tối ưu. Nghĩa là, phương pháp thu được bước tiếp theo $$B^+$$ từ $$B$$ sẽ là chủ đề thảo luận chính trong chương này. (**Lưu ý:** Để thuận tiện, chúng ta sẽ sử dụng hai ký hiệu $$B^{k+1}, B^k$$ và $$B^+, B$$ thay thế cho nhau.)