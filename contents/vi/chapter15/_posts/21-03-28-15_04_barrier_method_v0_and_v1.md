---
layout: post
title: '15-04 Phương pháp chắn v.0 và v.1'
chapter: "15"
order: 10
owner: "Minjoo Lee"
categories:
- chapter16
lang: vi
---

Sau khi biết công thức kỳ diệu $$f(x^*(t)) - f^* \le m/t$$, phản xạ tự nhiên đầu tiên của bất kỳ ai cũng sẽ là: *"Ồ, nếu tôi muốn sai số $$\epsilon = 10^{-6}$$ với $$m = 10$$ ràng buộc, sao tôi không chọn phắt ngay $$t = 10 / 10^{-6} = 10^7$$ rồi chạy Newton đúng 1 lần cho xong?!"*

Ý tưởng ngây thơ đó chính là **Phương pháp chắn v.0** — và trên thực tế nó **thất bại thảm hại**! Khi $$t = 10^7$$ quá lớn ngay từ đầu, hàm chắn gần như biến thành một vách đá dựng đứng với ma trận Hessian cực kỳ xấu (số điều kiện bùng nổ), khiến phương pháp Newton gần như đứng im hoặc mất hàng nghìn bước giảm chấn. Đó là lý do **Phương pháp chắn v.1** ra đời: khởi đầu với $$t^{(0)}$$ nhỏ (nơi địa hình tròn trịa, dễ đi), giải nhanh tới $$x^*(t^{(0)})$$, rồi tăng dần $$t \leftarrow \mu t$$ và dùng nghiệm cũ làm **điểm khởi tạo nóng (warm start)** cho vòng tiếp theo!

## Kiến thức cần nhớ: Sự đánh đổi khi chọn tham số $$\mu$$ trong Phương pháp chắn v.1

- **Tại sao v.0 thất bại còn v.1 thành công:** Ở v.0, điểm khởi tạo nằm rất xa $$x^*(m/\epsilon)$$ và địa hình bị méo gắt bởi $$t$$ khổng lồ. Ở v.1, nhờ tăng $$t$$ từng nấc nhân $$\mu$$, điểm $$x^*(t)$$ cũ luôn nằm rất gần điểm $$x^*(\mu t)$$ mới nên bước Newton định tâm chỉ mất khoảng 3–5 vòng lặp!
- **Cấu trúc hai vòng lặp của v.1:**
  - *Vòng ngoài (outer loop):* Kiểm tra $$m/t \le \epsilon$$; nếu chưa đạt, nhân $$t \leftarrow \mu t$$.
  - *Vòng trong (centering step):* Xuất phát từ $$x$$ hiện tại, chạy Newton để tìm $$x^*(t)$$.
- **Sự đánh đổi chọn $$\mu > 1$$:**
  - $$\mu$$ nhỏ (ví dụ $$\mu = 2$$): mỗi bước định tâm cực dễ (1–2 bước Newton), nhưng cần nhiều vòng ngoài.
  - $$\mu$$ lớn (ví dụ $$\mu = 100$$): ít vòng ngoài, nhưng mỗi vòng trong phải nhảy xa hơn nên tốn nhiều bước Newton hơn.
  - **Vùng ngọt thực tế:** $$\mu \in [10, 20]$$ thường cho tổng số bước Newton gần như tối ưu (thường chỉ 20–50 bước Newton tổng cộng cho mọi bài toán!).

### Giải thích: Tính tổng số vòng ngoài và ước lượng bước Newton cho các mức $$\mu$$ khác nhau

Giả sử một bài toán có $$m = 20$$ ràng buộc bất đẳng thức, khởi tạo $$t^{(0)} = 1$$, và ta cần độ chính xác $$\epsilon = 10^{-6}$$ (tức cần tăng $$t$$ từ $$1$$ đến $$t_{\text{end}} = \frac{m}{\epsilon} = 2 \times 10^7$$).

Số vòng lặp ngoài cần thiết là $$K = \left\lceil \frac{\log(t_{\text{end}} / t^{(0)})}{\log \mu} \right\rceil = \left\lceil \frac{\log(2 \times 10^7)}{\log \mu} \right\rceil$$ (chú ý $$\ln(2 \times 10^7) \approx 16.81$$):

1. **Với $$\mu = 2$$ (tăng chậm):**
   $$K = \lceil 16.81 / 0.693 \rceil = 25$$ vòng ngoài. Nếu mỗi vòng tốn trung bình 2 bước Newton → tổng $$\approx 50$$ bước Newton.
2. **Với $$\mu = 10$$ (vùng ngọt):**
   $$K = \lceil 16.81 / 2.303 \rceil = 8$$ vòng ngoài ($$t = 1, 10, 10^2, \dots, 10^8$$). Nếu mỗi vòng tốn trung bình 4 bước Newton → tổng $$\approx 32$$ bước Newton!
3. **Với $$\mu = 1000$$ (tăng quá gắt):**
   $$K = \lceil 16.81 / 6.908 \rceil = 3$$ vòng ngoài, nhưng mỗi lần nhảy $$t$$ gấp 1000 lần làm điểm khởi tạo xa đường trung tâm, mỗi vòng trong có thể tốn 25–40 bước Newton → tổng $$\approx 90\text{–}120$$ bước Newton!

---

## Phương pháp chắn v.0
**Phương pháp chắn v.0** chọn trực tiếp $$t = m/\epsilon$$ với độ chính xác mong muốn $$\epsilon > 0$$, rồi giải một lần bài toán chắn sau để đảm bảo $$f(x^*(t)) - f(x^*) \le \epsilon$$:
>
$$\begin{align}
 &\min_{x} \ && tf(x) + \phi(x) \\
 &\text{subject to } \ && Ax = b \\
\end{align}$$

Tuy nhiên, vì $$t = m/\epsilon$$ tăng rất lớn khi $$\epsilon$$ nhỏ, bài toán tương ứng nằm sát cuối đường trung tâm và gần như quay về độ khó của bài toán gốc trên biên, khiến phương pháp Newton hội tụ chậm và khó giải.

Để khắc phục, thay vì đặt $$t$$ lớn ngay từ đầu, ta tăng dần $$t$$ để bám theo đường trung tâm. Cách tiếp cận này được gọi là **phương pháp chắn v.1**.

## Phương pháp chắn v.1
**Phương pháp chắn v.1** tăng dần tham số $$t$$ qua nhiều bước và giải chuỗi bài toán chắn sau:
>
$$\begin{align}
 &\min_{x} \ && tf(x) + \phi(x) \\
 &\text{subject to } \ && Ax = b \\
\end{align}$$

### Thuật toán
Các bước của thuật toán như sau:

1. Chọn $$t^{(0)} > 0$$ và đặt $$k := 0$$.
2. Tại $$t = t^{(0)}$$, giải bài toán chắn để thu được $$x^{(0)} = x^*(t)$$.
3. Trong khi $$m/t > \epsilon$$:<br>
  3-1. Chọn $$t^{(k+1)} > t^{(k)}$$.<br>
  3-2. Khởi tạo phương pháp Newton bằng $$x^{(k)}$$ (khởi động ấm — warm start) và giải bài toán chắn tại $$t = t^{(k+1)}$$ để thu được $$x^{(k+1)} = x^*(t)$$.<br>
  Kết thúc vòng lặp.<br>

### Nhận xét
* **Quy tắc cập nhật thường dùng**: $$t^{(k+1)} = \mu t^{(k)}$$ với $$\mu > 1$$.
* **Khởi động ấm (warm start)**: Ở bước 3-2, nghiệm của vòng lặp trước được dùng làm điểm khởi tạo cho vòng lặp tiếp theo.
* **Bước định tâm (centering step)**: Bước 2 và bước 3-2 (giải bài toán chắn ứng với một giá trị $$t$$ cố định) được gọi là các bước định tâm hay vòng lặp ngoài.

### Lựa chọn tham số
Khi chọn $$\mu$$ và $$t^{(0)}$$, cần cân nhắc các đánh đổi sau:

##### Chọn $$\mu$$
* Nếu $$\mu$$ quá nhỏ, số vòng lặp ngoài tăng lên (dù khởi động ấm giúp mỗi bước giải nhanh hơn).<br>
* Nếu $$\mu$$ quá lớn, điểm khởi tạo nằm xa điểm đường trung tâm mới nên phương pháp Newton cần nhiều vòng lặp hơn ở mỗi bước định tâm.

##### Chọn $$t^{(0)}$$
* Nếu $$t^{(0)}$$ quá nhỏ, số vòng lặp ngoài tăng lên.<br>
* Nếu $$t^{(0)}$$ quá lớn, bài toán ban đầu trở nên khó giải tương tự phương pháp chắn v.0, làm tăng số bước Newton ở bước định tâm đầu tiên.

Trong thực tế, hiệu năng của phương pháp chắn khá ổn định trước sự thay đổi của $$\mu$$ và $$t^{(0)}$$, trong đó khoảng giá trị phù hợp phụ thuộc vào kích thước bài toán.

## Ví dụ LP cỡ nhỏ
Hình dưới đây minh họa hiệu năng của phương pháp chắn trên một bài toán quy hoạch tuyến tính (LP) với $$n = 50$$ biến và $$m = 100$$ ràng buộc bất đẳng thức. Khi $$\mu = 2$$, số vòng lặp ngoài tăng lên; còn khi $$\mu = 150$$, số bước định tâm và bước Newton có sự đánh đổi rõ rệt so với mức $$\mu = 50$$.

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_barrier_method_03.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">[Hình 1] Ví dụ LP cỡ nhỏ [3]</figcaption>
</p>
</figure>
