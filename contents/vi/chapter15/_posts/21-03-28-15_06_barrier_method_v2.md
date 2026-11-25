---
layout: post
title: '15-06 Phương pháp chắn v.2'
chapter: '15'
order: 12
owner: Minjoo Lee
categories:
- chapter15
lang: vi
---

Ở phiên bản v.1, ta yêu cầu mỗi bước định tâm phải giải *chính xác tuyệt đối* bài toán $$\min t f(x) + \phi(x)$$ để điểm lặp nằm khít trên đường trung tâm $$x^*(t)$$. Nhưng hãy nghĩ lại một chút: **đường trung tâm đâu phải đích đến cuối cùng của chúng ta!** Điểm $$x^*(t)$$ ở các vòng đầu (khi $$t = 1$$ hay $$t = 10$$) chỉ là trạm trung chuyển tạm thời. Việc tiêu tốn thêm nhiều bước Newton để tìm $$x^*(10)$$ chính xác tới $$10^{-12}$$ rồi ngay lập tức vứt đi để tăng $$t \leftarrow 100$$ rõ ràng là một sự lãng phí!

**Phương pháp chắn v.2** khắc phục triệt để sự lãng phí ấy bằng một cải tiến thực dụng nhưng sâu sắc: ở mỗi vòng trong, ta **không giải chính xác tuyệt đối**, mà chỉ cần chạy Newton cho đến khi **đại lượng giảm Newton** thỏa $$\frac{1}{2}\lambda(x)^2 \le \epsilon_{\text{center}}$$ (hoặc thậm chí chỉ chạy 1 bước Newton — chiến lược *short-step*!), miễn là điểm lặp vẫn bám đủ gần đường trung tâm để bước tăng $$t$$ kế tiếp an toàn.

## Bản đồ kiến thức nền: Tư duy định tâm xấp xỉ (Inexact Centering) trong v.2

- **Tại sao không cần định tâm chính xác tuyệt đối:** Mục tiêu duy nhất của vòng trong là đưa $$x$$ vào vùng hội tụ bậc hai của bài toán chắn tại $$t$$ để làm bệ phóng cho $$\mu t$$. Khi Newton decrement $$\lambda(x)$$ đã nhỏ (ví dụ $$\lambda(x) \le 0.25$$), điểm $$x$$ đã ở sát $$x^*(t)$$ rồi!
- **Tiêu chí dừng vòng trong bằng Newton decrement:** Nhờ tính bất biến affine và ước lượng $$\frac{1}{2}\lambda(x)^2 \approx (tf(x)+\phi(x)) - (tf(x^*(t))+\phi(x^*(t)))$$, ta dừng vòng trong ngay khi $$\frac{1}{2}\lambda(x)^2 \le \epsilon_{\text{inner}}$$.
- **Điều chỉnh chứng chỉ dừng ở vòng cuối:** Vì $$x$$ chỉ nằm *gần* $$x^*(t)$$ chứ không trùng khít, sai số cuối cùng cần cộng thêm độ lệch định tâm nhỏ, hoặc chạy định tâm chính xác hơn chỉ ở đúng vòng ngoài cuối cùng khi $$m/t \le \epsilon$$.

### Khung giải thích (nên đọc chậm): So sánh chi phí giữa định tâm tuyệt đối (v.1) và định tâm vừa đủ (v.2)

Xét một bài toán chắn tại bước trung gian $$t = 10$$, trong đó Newton decrement giảm qua các bước Newton như sau (nhờ hội tụ bậc hai khi $$\lambda < 0.5$$):
- Sau bước 1: $$\lambda_1 = 0.80 \implies \frac{1}{2}\lambda_1^2 = 0.32$$.
- Sau bước 2: $$\lambda_2 = 0.25 \implies \frac{1}{2}\lambda_2^2 = 0.03125$$.
- Sau bước 3: $$\lambda_3 = 0.04 \implies \frac{1}{2}\lambda_3^2 = 0.0008$$.
- Sau bước 4: $$\lambda_4 = 0.001 \implies \frac{1}{2}\lambda_4^2 = 5 \times 10^{-7}$$.
- Sau bước 5: $$\lambda_5 = 10^{-6} \implies \frac{1}{2}\lambda_5^2 = 5 \times 10^{-13}$$.

1. **Cách làm của v.1 (đòi $$\frac{1}{2}\lambda^2 \le 10^{-10}$$ ở mọi vòng ngoài):** Tốn **5 bước Newton** ở ngay trạm trung gian $$t = 10$$.
2. **Cách làm của v.2 (chỉ cần $$\frac{1}{2}\lambda^2 \le 0.05$$ ở các vòng trung gian):** Dừng ngay sau **2 bước Newton** (khi $$\frac{1}{2}\lambda_2^2 = 0.03125 \le 0.05$$) và lập tức tăng $$t \leftarrow \mu t$$!
3. **Hiệu quả cộng dồn:** Qua 8 vòng ngoài, v.2 tiết kiệm hơn **50% số lần phân rã Cholesky** mà vẫn cập bến cùng một nghiệm cuối với độ chính xác $$10^{-8}$$!

---

Trong phiên bản trước, thuật toán yêu cầu giải chính xác bài toán chắn để nghiệm nằm đúng trên đường trung tâm. Tuy nhiên, đường trung tâm chỉ là phương tiện dẫn tới nghiệm tối ưu chứ không phải đích đến cuối cùng, nên trên thực tế ta không cần giải chính xác tuyệt đối ở từng bước định tâm.

### Thuật toán

Từ nhận xét đó, **phương pháp chắn v.2** chỉ giải xấp xỉ bài toán chắn ở mỗi bước: cụ thể, $$x^{(0)} \approx x^*(t)$$ ở bước 2 và $$x^{(k+1)} \approx x^*(t)$$ ở bước 3-2.

Cấu trúc thuật toán giữ nguyên như phương pháp chắn v.1:

1. Chọn $$t^{(0)} > 0$$ và đặt $$k := 0$$.
2. Tại $$t = t^{(0)}$$, giải xấp xỉ bài toán chắn để thu được $$x^{(0)} \approx x^*(t)$$.
3. Trong khi $$m/t > \epsilon$$:<br>
   3-1. Chọn $$t^{(k+1)} > t^{(k)}$$.<br>
   3-2. Khởi tạo phương pháp Newton bằng $$x^{(k)}$$ (warm start) và giải xấp xỉ bài toán chắn tại $$t = t^{(k+1)}$$ để thu được $$x^{(k+1)} \approx x^*(t)$$.<br>
   Kết thúc vòng lặp.<br>

Với phương pháp chắn v.2, hai câu hỏi trọng tâm cần đặt ra là:

* Mỗi bước giải xấp xỉ cần chính xác đến mức nào?
* Mỗi bước định tâm cần bao nhiêu bước Newton?

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_barrier_methodv2_04.png" alt="" width="70%" height="70%">
  <figcaption style="text-align: center;">[Hình 1] Phân tích số vòng lặp Newton và khoảng cách dưới tối ưu theo $$m$$ [1]</figcaption>
</p>
</figure>

Hình 1 cho thấy khi áp dụng phương pháp chắn cho bài toán có $$m$$ ràng buộc, tốc độ hội tụ vẫn là tuyến tính ngay cả khi $$m$$ rất lớn — tức số vòng lặp tăng theo thang logarit đối với $$m$$.

Nhìn từ góc độ khác, số bước Newton cần thiết để giảm khoảng cách đối ngẫu (duality gap) đi một hệ số $$10^4$$ chỉ tăng rất chậm theo $$m$$. Như thể hiện ở Hình 2, ngay cả khi $$m$$ tăng mạnh, mỗi bài toán vẫn chỉ cần khoảng 20–30 bước Newton (dù chi phí của bản thân mỗi bước Newton phụ thuộc đáng kể vào kích thước bài toán).

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter15/15_barrier_methodv2_05.png" alt="" width="70%" height="70%">
  <figcaption style="text-align: center;">[Hình 2] Phân tích số vòng lặp Newton khi $$m$$ tăng [1]</figcaption>
</p>
</figure>
