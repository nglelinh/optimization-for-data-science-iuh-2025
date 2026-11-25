---
layout: post
title: '09-05-01 Phương pháp gradient gần kề tăng tốc'
chapter: '09'
order: 7
owner: Kyeongmin Woo
categories:
- chapter09
lang: vi
---

Năm 1983, khi Yurii Nesterov công bố phương pháp tăng tốc bậc nhất cho hàm trơn, cộng đồng tối ưu gần như không tin vào mắt mình — làm sao chỉ một phép ngoại suy tuyến tính miễn phí lại phá vỡ được rào cản $$O(1/k)$$ vốn thống trị suốt nhiều thập kỷ? Hơn hai mươi năm sau, câu hỏi mở rộng nó sang bài toán tổng hợp không trơn $$f(x) = g(x) + h(x)$$ đã được giải quyết trọn vẹn (đặc biệt qua công trình FISTA của Beck & Teboulle 2009 và chuỗi bài của Nesterov 2007), tạo ra **phương pháp gradient gần kề tăng tốc (Accelerated Proximal Gradient Method)**.

Hãy nhìn vào công thức cập nhật của bài học này: chỉ thêm đúng *một dòng* ngoại suy $$v = x^{(k-1)} + \frac{k-2}{k+1}(x^{(k-1)} - x^{(k-2)})$$ trước khi gọi bước prox quen thuộc! Chi phí tính toán mỗi vòng lặp gần như **bằng hệt** phương pháp không tăng tốc (vẫn chỉ 1 lần tính $$\nabla g$$ và 1 lần tính $$\operatorname{prox}_{t h}$$), nhưng tốc độ hội tụ nhảy vọt từ $$O(1/\epsilon)$$ lên $$O(1/\sqrt{\epsilon})$$.

## Bản đồ kiến thức nền: Ba trụ cột của công thức gradient gần kề tăng tốc

- **Chuỗi hai điểm (Điểm lặp $$x^{(k)}$$ và điểm ngoại suy $$v^{(k)}$$):** Ta duy trì điểm hợp lệ $$x^{(k)}$$ (luôn nằm trong miền của $$h$$ và giữ tính thưa) cùng điểm ngoại suy $$v^{(k)} = x^{(k-1)} + \frac{k-2}{k+1}(x^{(k-1)} - x^{(k-2)})$$. Bước gradient và prox được thực hiện từ $$v^{(k)}$$:
  $$x^{(k)} = \operatorname{prox}_{t_k h}\big(v^{(k)} - t_k \nabla g(v^{(k)})\big).$$
- **Quy luật tăng dần của trọng số quán tính $$\beta_k = \frac{k-2}{k+1}$$:** Ở bước đầu ($$k = 1, 2$$), hệ số bằng $$0$$ (khởi động êm như proximal gradient thường); khi $$k$$ lớn dần, $$\beta_k \approx 1 - \frac{3}{k}$$ tiến sát $$1$$. Chính con số $$3$$ trong $$1 - 3/k$$ gắn chặt với phương trình vi phân bậc hai giảm chấn $$\ddot{X} + \frac{3}{t}\dot{X} + \nabla g(X) = 0$$ (Su–Boyd–Candès 2014)!
- **Tính tương thích với bài toán Lasso và bài toán có ràng buộc:** Ngay cả khi $$v^{(k)}$$ tạm thời nhảy ra ngoài miền ràng buộc $$C$$ (hoặc tạm mất tính thưa do cộng hiệu hai vector), bước $$\operatorname{prox}_{t_k h}$$ ngay sau đó lập tức kéo $$x^{(k)}$$ quay về miền hợp lệ và khôi phục tính thưa!

### Khung giải thích (nên đọc chậm): Tính tay 3 vòng lặp đầu của Accelerated Proximal GD trên Lasso 1D

Xét bài toán Lasso 1D $$f(x) = \frac{1}{2}(x - 5)^2 + 1.0|x|$$ ($$g(x) = \frac{1}{2}(x-5)^2, L=1$$), dùng bước cố định nhỏ $$t = 0.5$$ để quan sát rõ tác dụng quán tính. Nghiệm tối ưu là $$x^* = 4$$. Khởi tạo $$x^{(0)} = x^{(-1)} = 0$$.

1. **Vòng $$k = 1$$ ($$\beta_1 = 0$$):**
   - $$v^{(1)} = x^{(0)} = 0$$.
   - $$x^{(1)} = S_{0.5}\big(0 - 0.5(0 - 5)\big) = S_{0.5}(2.5) = 2.0$$.
2. **Vòng $$k = 2$$ ($$\beta_2 = \frac{2-2}{2+1} = 0$$):**
   - $$v^{(2)} = x^{(1)} = 2.0$$.
   - $$x^{(2)} = S_{0.5}\big(2.0 - 0.5(2.0 - 5)\big) = S_{0.5}(3.5) = 3.0$$.
3. **Vòng $$k = 3$$ ($$\beta_3 = \frac{3-2}{3+1} = 0.25$$ — quán tính bắt đầu kích hoạt!):**
   - Ngoại suy: $$v^{(3)} = x^{(2)} + 0.25(x^{(2)} - x^{(1)}) = 3.0 + 0.25(3.0 - 2.0) = 3.25$$.
   - Bước gradient + prox tại $$v^{(3)} = 3.25$$:
     $$x^{(3)} = S_{0.5}\big(3.25 - 0.5(3.25 - 5)\big) = S_{0.5}(3.25 + 0.875) = S_{0.5}(4.125) = 3.625.$$
   - *So sánh với không tăng tốc (ISTA cùng $$t=0.5$$):* ISTA ở vòng 3 chỉ đạt $$S_{0.5}(3.0 + 1.0) = 3.500$$ (còn cách $$x^*=4$$ là $$0.5$$), trong khi bản tăng tốc đã tiến tới $$3.625$$ (chỉ còn cách $$0.375$$) ngay từ nhịp quán tính đầu tiên!

# Phương pháp gradient gần kề tăng tốc

Khi bổ sung kỹ thuật tăng tốc, phương pháp gradient gần kề đạt được tốc độ hội tụ tối ưu $$O(1/\sqrt{\epsilon})$$. Trong chuỗi nghiên cứu của mình, Nesterov đã đề xuất bốn phương pháp nổi tiếng, trong đó có ba phương pháp tăng tốc:

- 1983: Phương pháp tăng tốc đầu tiên cho các hàm trơn
- 1988: Một biến thể tăng tốc khác cho các hàm trơn
- 2005: Kỹ thuật làm trơn hàm không trơn kết hợp với phương pháp tăng tốc năm 1983
- 2007: Phương pháp tăng tốc cho các bài toán tối ưu tổng hợp

Dưới đây, chúng ta trình bày phương pháp của Beck và Teboulle (2008), mở rộng phương pháp Nesterov (1983) cho lớp hàm tổng hợp.

## Thuật toán gradient gần kề tăng tốc
Tương tự các bài trước, giả sử $$g$$ là hàm lồi khả vi và $$h$$ là hàm lồi. Xét bài toán:
> 
\begin{align}
\min_x g(x) + h(x)
\end{align}

**Phương pháp gradient gần kề tăng tốc** tận dụng hướng dịch chuyển của bước trước để tránh đổi hướng đột ngột ở bước tiếp theo. Nói cách khác, thuật toán bổ sung một thành phần động lượng tạo quán tính theo hướng tiến triển gần nhất.

Khởi tạo $$x^{(0)} = x^{(-1)} \in \mathbb{R}^n$$. Tại mỗi bước $$k = 1, 2, 3, \dots$$, ta tính điểm ngoại suy $$v$$ có xét đến động lượng, rồi áp dụng bước gradient gần kề tại $$v$$:

> $$
\begin{align}
v & = x^{(k-1)} + \frac{k-2}{k + 1}  (x^{(k-1)} −x^{(k-2)}) \\
x^{(k)} & = \text{prox}_{t_k} (v − t_k \nabla g(v)), k = 1,2,3,...  \\
\end{align} $$

- Ở bước đầu tiên ($$k = 1$$), vì $$x^{(0)} - x^{(-1)} = 0$$, điểm $$v$$ trùng với $$x^{(0)}$$ nên bước cập nhật giống hệt phương pháp gradient gần kề tiêu chuẩn.
- Từ các bước sau trở đi, $$v$$ được dịch thêm một lượng động lượng theo hướng $$x^{(k-1)} - x^{(k-2)}$$. Khi $$k$$ tăng, trọng số động lượng tăng dần và tiến về $$1$$.
- Khi $$h = 0$$, thuật toán trở về **phương pháp gradient tăng tốc (accelerated gradient method)**.

Hình dưới đây minh họa sự biến thiên của trọng số động lượng theo $$k$$. Ở các giá trị $$k$$ đầu tiên, trọng số có giá trị âm, nhưng tại $$k = 1$$ hiệu $$x^{(0)} - x^{(-1)} = 0$$ nên thành phần động lượng triệt tiêu và không gây ảnh hưởng. Khi $$k$$ tăng, trọng số tiến gần về $$1$$, giúp duy trì quán tính mạnh hơn và tăng tốc độ hội tụ.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter09/momentum_weight.png" width="80%" height="80%">
  <figcaption style="text-align: center;">[Hình 1] Trọng số động lượng [3]</figcaption>
</figure>

## Ví dụ trên bài toán Lasso
Khi áp dụng phương pháp gradient gần kề tăng tốc cho bài toán Lasso đã xét trước đó, đồ thị hội tụ dưới đây cho thấy tốc độ hội tụ vượt trội so với cả phương pháp subgradient và phương pháp gradient gần kề tiêu chuẩn.

Có thể quan sát một đoạn ở giữa đồ thị mà giá trị hàm mục tiêu tạm thời tăng lên — hiện tượng này được gọi là "gợn sóng Nesterov" (Nesterov ripples). Điều này cho thấy phương pháp gradient gần kề tăng tốc không đảm bảo giảm đơn điệu giá trị hàm mục tiêu ở mọi bước lặp.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter09/accelerated_proximal_gradient.png" width="80%" height="80%">
  <figcaption style="text-align: center;">[Hình 2] Gradient Gần kề Tăng tốc [3]</figcaption>
</figure>