---
layout: post
title: '15-05 Phân tích hội tụ'
chapter: "15"
order: 11
categories:
- chapter16
owner: "Minjoo Lee"
lang: vi
---

Nhìn vào phương pháp chắn v.1 với hai vòng lặp lồng nhau (vòng ngoài tăng $$t$$, vòng trong chạy Newton), câu hỏi định lượng quan trọng nhất là: **cần bao nhiêu vòng ngoài để sai số giảm xuống dưới $$\epsilon$$?**

Kết quả phân tích hội tụ ở mục 15-05 gọn gàng đến bất ngờ: vì sau mỗi bước định tâm, $$t$$ tăng theo cấp số nhân $$t^{(k)} = \mu^k t^{(0)}$$, nên khoảng cách dưới tối ưu giảm theo cấp số nhân $$f(x^{(k)}) - f^* \le \frac{m}{\mu^k t^{(0)}}$$! Điều đó có nghĩa là **phương pháp chắn hội tụ tuyến tính (tốc độ cấp số nhân) theo số vòng ngoài**, và số vòng ngoài chỉ tăng theo hàm **logarit** của $$1/\epsilon$$!

## Bản đồ kiến thức nền: Giải phẫu định lý hội tụ vòng ngoài của Phương pháp chắn

- **Quy luật giảm sai số sau $$k$$ vòng ngoài:** Khi bắt đầu từ $$t^{(0)}$$ và nhân hệ số $$\mu > 1$$ mỗi vòng, ta có:
  $$f(x^{(k)}) - f^* \le \frac{m}{\mu^k t^{(0)}}.$$
- **Số vòng ngoài tối đa đạt độ chính xác $$\epsilon$$:** Giải bất phương trình $$\frac{m}{\mu^k t^{(0)}} \le \epsilon$$ cho ra ngay:
  $$k \ge \frac{\log\bigl(m / (\epsilon t^{(0)})\bigr)}{\log \mu}.$$
- **Góc nhìn "số bước để thêm 1 chữ số chính xác":** Nếu chọn $$\mu = 10$$, thì **cứ đúng 1 vòng ngoài**, khoảng cách đối ngẫu giảm đúng 10 lần — tức bạn mua thêm **1 chữ số thập phân chính xác** sau mỗi bước định tâm!
- **Ghép với độ phức tạp vòng trong:** Khi kết hợp với tính tự hài hòa của hàm chắn (mục 15-08), mỗi vòng trong chỉ tốn số bước Newton bị chặn bởi $$O(\sqrt{m})$$ (nếu chọn $$\mu = 1 + 1/\sqrt{m}$$), đem lại tổng độ phức tạp đa thức huyền thoại $$O\bigl(\sqrt{m}\log(m/(\epsilon t^{(0)}))\bigr)$$ bước Newton!

### Khung giải thích (nên đọc chậm): Tính trực tiếp số vòng ngoài và sai số từng bước với $$m = 50, \mu = 10$$

Xét một bài toán tối ưu lồi có $$m = 50$$ ràng buộc bất đẳng thức, khởi tạo $$t^{(0)} = 0.5$$, hệ số tăng $$\mu = 10$$, và yêu cầu sai số $$\epsilon = 10^{-5}$$.

1. **Tính sai số tối đa sau từng vòng ngoài $$k = 0, 1, 2, \dots$$:**
   - $$k = 0$$ ($$t^{(0)} = 0.5$$): $$f(x^{(0)}) - f^* \le \frac{50}{0.5} = 100$$.
   - $$k = 1$$ ($$t^{(1)} = 5$$): $$f(x^{(1)}) - f^* \le 10$$.
   - $$k = 2$$ ($$t^{(2)} = 50$$): $$f(x^{(2)}) - f^* \le 1$$.
   - $$k = 7$$ ($$t^{(7)} = 5 \times 10^6$$): $$f(x^{(7)}) - f^* \le \frac{50}{5 \times 10^6} = 10^{-5} = \epsilon$$!
2. **Kiểm tra lại bằng công thức logarit:**
   $$k = \frac{\log_{10}\bigl(50 / (10^{-5} \times 0.5)\bigr)}{\log_{10}(10)} = \log_{10}(10^7) = 7 \text{ vòng ngoài}.$$
   Chỉ cần **7 vòng định tâm**, sai số đã giảm **10 triệu lần** từ $$100$$ xuống $$10^{-5}$$!

---

Giả sử mỗi bước định tâm (centering step) trong phương pháp chắn được giải chính xác, ta thu được kết quả hội tụ sau.

## Định lý hội tụ
Sau $$k$$ bước định tâm (vòng lặp ngoài), **phương pháp chắn** thỏa mãn bất đẳng thức:
>$$
>\begin{align}
>f(x^{(k)}) - f^{*} \le  \frac{m}{\mu^k t^{(0)}}
>\end{align}
>$$

Nghĩa là để đạt độ chính xác $$\epsilon$$, tổng số bước định tâm cần thiết (bao gồm bước định tâm đầu tiên) là:

>$$
>\begin{align}
>\frac{\log(m/(t^{(0)}\epsilon))}{\log \mu} + 1
>\end{align}
>$$

Như vậy, số vòng lặp ngoài có bậc độ phức tạp $$O(\log(1/\epsilon))$$, tương ứng tốc độ hội tụ tuyến tính.

So với tốc độ hội tụ bậc hai $$O(\log \log(1/\epsilon))$$ của phương pháp Newton không ràng buộc, hội tụ tuyến tính vẫn là kết quả tốt đối với lớp bài toán có ràng buộc bất đẳng thức vốn khó hơn nhiều.

Định nghĩa chi tiết về hội tụ tuyến tính và hội tụ bậc hai có thể tham khảo thêm trên Wikipedia:<br>
* Tham khảo: [Rate of convergence](https://en.wikipedia.org/wiki/Rate_of_convergence)
