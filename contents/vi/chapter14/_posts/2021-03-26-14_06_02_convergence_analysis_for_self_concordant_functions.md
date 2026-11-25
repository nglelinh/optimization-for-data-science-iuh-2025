---
layout: post
title: 14-06-02 Phân tích hội tụ cho các hàm tự hài hòa
chapter: '14'
order: 14
owner: Minjoo Lee
categories:
- chapter14
lang: vi
---

Đây chính là phần thưởng lớn nhất của khái niệm tự hài hòa: một định lý hội tụ **không còn bóng dáng của $$m, L, M$$**, không phụ thuộc số chiều $$n$$, không phụ thuộc số điều kiện của bài toán, và hoàn toàn bất biến affine!

Định lý Nesterov–Nemirovskii khẳng định rằng với mọi hàm tự hài hòa, phương pháp Newton có giảm chấn chỉ cần tối đa $$C(\alpha, \beta)\bigl(f(x^{(0)}) - f^\star\bigr) + \log_2\log_2(1/\epsilon)$$ vòng lặp. Toàn bộ độ phức tạp chỉ còn nằm ở đúng hai đại lượng mang ý nghĩa vật lý rõ ràng: khoảng cách hàm ban đầu $$f(x^{(0)}) - f^\star$$ và độ chính xác yêu cầu $$\epsilon$$.

## Kiến thức cần nhớ: Đọc hiểu định lý Nesterov–Nemirovskii

- **Cấu trúc hai số hạng quen thuộc nhưng sạch hằng số ẩn:**
  - Số hạng thứ nhất $$C(\alpha, \beta)(f(x^{(0)}) - f^\star)$$ đếm số bước ở giai đoạn giảm chấn, trong đó hằng số $$C(\alpha, \beta)$$ **chỉ phụ thuộc duy nhất vào hai tham số backtracking $$\alpha, \beta$$** mà bạn tự chọn!
  - Số hạng thứ hai $$\log_2\log_2(1/\epsilon)$$ đếm số bước ở giai đoạn hội tụ bậc hai (khi $$\lambda(x) < \eta$$, thường $$\eta = 1/4$$ hoặc $$0.25$$).
- **Chứng chỉ dừng trực tiếp từ Newton decrement:** Với hàm tự hài hòa, khi $$\lambda(x) \le 0.68$$ (hoặc $$\lambda(x) < 1$$), ta có chặn trên **tuyệt đối, không cần biết $$m$$**:
  $$f(x) - f^\star \le \lambda(x)^2 \quad (\text{khi } \lambda(x) \le 0.68).$$
- **Tại sao định lý này làm thay đổi ngành tối ưu:** Nhờ không chứa $$m, L, M$$, định lý cho phép chứng minh phương pháp điểm trong giải được LP, QP, SOCP và SDP trong thời gian đa thức được đảm bảo chặt chẽ.

### Giải thích: Tính cụ thể cận số vòng lặp với tham số backtracking chuẩn

Trong sách của Boyd & Vandenberghe (Chương 9.6), hằng số trong định lý hội tụ hàm tự hài hòa có thể viết tường minh là:
$$C(\alpha, \beta) = \frac{20 - 8\alpha}{\alpha\beta(1 - 2\alpha)^2} \quad \text{(hoặc cận chặt hơn cỡ } \frac{1}{\gamma}\text{ với } \gamma = \alpha\beta\frac{\eta^2}{1+\eta}\text{)}.$$

Hãy thử thay giá trị thực tế phổ biến $$\alpha = 0.2$$, $$\beta = 0.5$$ và ngưỡng chuyển pha $$\eta = 0.25$$ (từ lý thuyết tự hài hòa):

1. **Tính mức giảm tối thiểu $$\gamma$$ mỗi bước ở pha giảm chấn (khi $$\lambda(x) \ge \eta = 0.25$$):**
   $$\gamma = \alpha\beta \frac{\eta^2}{1 + \eta} = (0.2)(0.5)\frac{0.0625}{1.25} = 0.1 \times 0.05 = 0.005.$$
   Suy ra hằng số $$1/\gamma = 200$$ (cận lý thuyết trường hợp xấu nhất; thực tế thường nhanh hơn 10–20 lần).
2. **Tính cận số vòng lặp khi $$f(x^{(0)}) - f^\star = 1.5$$ và $$\epsilon = 10^{-10}$$:**
   - Pha giảm chấn: tối đa $$\frac{1.5}{0.005} = 300$$ bước (trong thực tế thường chỉ mất 3–8 bước).
   - Pha bậc hai: $$\log_2\log_2(10^{10}) \approx \log_2(33.2) \approx 5.05 \implies 6$$ bước.
3. **Điểm quan trọng nhất cần nhớ:** Nếu bạn nhân trục tọa độ lên $$1{,}000{,}000$$ lần (làm số điều kiện $$L/m$$ phình lên $$10^{12}$$), cận của Gradient Descent phình lên $$10^{12}$$ lần, còn cận tự hài hòa ở trên **không nhúc nhích dù chỉ 1 vòng lặp!**

---

Đối với các hàm tự hài hòa, kết quả phân tích hội tụ của phương pháp Newton có dạng:

>Định lý (Nesterov và Nemirovskii): Phương pháp Newton với tìm kiếm đường backtracking cần tối đa số vòng lặp sau để đạt được $$f(x^{(k)})-f^{\star}\leq \epsilon$$:
>\begin{align}
>C(\alpha, \beta)\big( f(x^{(0)})-f^{\star} \big) + \log\log{(1/\epsilon)},
>\end{align}
>trong đó $$C(\alpha, \beta)$$ là hằng số chỉ phụ thuộc vào hai tham số backtracking $$\alpha, \beta$$.

Chứng minh định lý này có cấu trúc tương tự phân tích hội tụ tổng quát của phương pháp Newton, nhưng khai thác các tính chất của hàm tự hài hòa để loại bỏ sự phụ thuộc vào các hằng số $$L, m, M$$ (xem [1], tr. 503).