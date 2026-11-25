---
layout: post
title: '08-01-02 Bất đẳng thức cơ bản'
chapter: '08'
order: 4
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

Mọi định lý lớn về hội tụ trong chương này — từ bước cố định, bước giảm dần, cho tới tốc độ $$O(1/\epsilon^2)$$ và kích thước bước Polyak — đều mọc ra từ cùng một gốc rễ duy nhất: **bất đẳng thức cơ bản của phương pháp subgradient**. Thú vị hơn nữa, chứng minh của nó không hề cần đến công cụ giải tích cao cấp nào; nó chỉ dài đúng vài dòng đại số sơ cấp dựa trên hằng đẳng thức $$\|a - b\|_2^2 = \|a\|_2^2 - 2a^T b + \|b\|_2^2$$ và phép cộng dồn rút gọn (telescoping sum).

Điều kỳ diệu nằm ở góc nhìn "kế toán năng lượng": ở mỗi bước lặp $$i$$, lượng khoảng cách bình phương $$\|x^{(i)} - x^*\|_2^2$$ thay đổi bởi hai lực kéo ngược chiều nhau. Một bên là lực hút về nghiệm $$-2\alpha_i(f(x^{(i)}) - f^*)$$ kéo ta tiến lại gần $$x^*$$; bên kia là lực nhiễu bước đi $$+\alpha_i^2 \|g^{(i)}\|_2^2$$ sinh ra do ta bước thẳng theo subgradient. Khi cộng dồn qua $$k$$ bước, tất cả các số hạng trung gian tự triệt tiêu nhau như quân domino, để lại đúng một cân bằng hoàn hảo giữa khoảng cách ban đầu $$R^2$$ và tổng bình phương bước đi $$G^2 \sum \alpha_i^2$$.

## Kiến thức cần nhớ: Bốn mảnh ghép tạo nên bất đẳng thức cơ bản

Để không bao giờ phải học thuộc lòng công thức $$\frac{R^2 + G^2\sum \alpha_i^2}{2\sum \alpha_i}$$, hãy nhìn rõ bốn viên gạch xây nên nó:

- **Khai triển bình phương chuẩn Euclid:** Đẳng thức $$\|x^{(k+1)} - x^*\|_2^2 = \|x^{(k)} - x^*\|_2^2 - 2\alpha_k g^{(k)T}(x^{(k)} - x^*) + \alpha_k^2 \|g^{(k)}\|_2^2$$ là phương trình cân bằng ở từng bước, biến một bài toán phi tuyến thành tổng các số hạng dễ chặn.
- **Bất đẳng thức định nghĩa subgradient:** Từ $$f(x^*) \ge f(x^{(k)}) + g^{(k)T}(x^* - x^{(k)})$$, ta đổi vế để thay tích vô hướng $$g^{(k)T}(x^{(k)} - x^*)$$ bằng đại lượng ta thực sự quan tâm là khoảng cách hàm mục tiêu $$f(x^{(k)}) - f^*$$.
- **Giả thiết bị chặn $$R$$ và $$G$$:** Khoảng cách khởi điểm $$\|x^{(0)} - x^*\|_2 \le R$$ kiểm soát tử số ban đầu, còn tính Lipschitz $$\|g^{(i)}\|_2 \le G$$ chặn số hạng bậc hai $$\alpha_i^2 \|g^{(i)}\|_2^2 \le \alpha_i^2 G^2$$ để bước đi không bị nổ.
- **Tổng rút gọn (Telescoping Sum) và chặn dưới bởi $$f_{\text{best}}^k$$:** Khi cộng từ $$i=1$$ đến $$k$$, chuỗi $$\|x^{(i)} - x^*\|_2^2 - \|x^{(i+1)} - x^*\|_2^2$$ rút gọn còn $$\|x^{(1)} - x^*\|_2^2 - \|x^{(k+1)} - x^*\|_2^2 \le R^2$$. Sau đó dùng $$\sum \alpha_i (f(x^{(i)}) - f^*) \ge (f_{\text{best}}^k - f^*)\sum \alpha_i$$ để tách ra kỷ lục tốt nhất.

### Giải thích: Kiểm chứng từng số hạng của bất đẳng thức cơ bản bằng tay

Xét $$f(x) = |x|$$ ($$x^* = 0$$, $$f^* = 0$$, $$G = 1$$), bắt đầu tại $$x^{(0)} = 1.5$$ (nên $$R = 1.5$$, $$R^2 = 2.25$$) và dùng bước cố định $$\alpha_0 = \alpha_1 = 1$$ trong $$k = 2$$ bước.

1. **Tính quỹ đạo thực tế:**
   - Tại $$x^{(0)} = 1.5$$: $$f(x^{(0)}) = 1.5$$, $$g^{(0)} = 1$$. Cập nhật $$x^{(1)} = 1.5 - 1(1) = 0.5$$.
   - Tại $$x^{(1)} = 0.5$$: $$f(x^{(1)}) = 0.5$$, $$g^{(1)} = 1$$. Cập nhật $$x^{(2)} = 0.5 - 1(1) = -0.5$$.
   - Kỷ lục tốt nhất sau hai điểm đã duyệt: $$f_{\text{best}} = \min(1.5, 0.5) = 0.5$$.
2. **Kiểm tra phương trình năng lượng ở từng bước:**
   - **Bước 0:** $$\|x^{(1)} - x^*\|^2 = 0.25$$, trong khi $$\|x^{(0)} - x^*\|^2 - 2\alpha_0(f(x^{(0)}) - f^*) + \alpha_0^2 \|g^{(0)}\|^2 = 2.25 - 2(1)(1.5) + 1(1) = 0.25$$ (khớp chính xác!).
   - **Bước 1:** $$\|x^{(2)} - x^*\|^2 = 0.25$$, trong khi $$0.25 - 2(1)(0.5) + 1(1) = 0.25$$ (khớp chính xác!).
3. **Cộng dồn hai bước và đối chiếu bất đẳng thức cơ bản:**
   - Cộng hai vế: $$2(1)(1.5 + 0.5) = 4 = 2.25 - 0.25 + 1^2(1 + 1) \le R^2 + G^2\sum \alpha_i^2 = 2.25 + 2 = 4.25$$.
   - Chia cho $$2\sum \alpha_i = 4$$:
     $$f_{\text{best}} - f^* = 0.5 \;\le\; \frac{1.5 + 0.5}{2} = 1.0 \;\le\; \frac{2.25 + 2}{4} = 1.0625.$$
   Mọi mắc xích — từ bình phương khoảng cách, tổng rút gọn đến cận trên cuối cùng — đều khớp từng con số thập phân!

Định lý hội tụ và tốc độ hội tụ của phương pháp subgradient đều được suy ra từ bất đẳng thức cơ bản dưới đây.

## Bất đẳng thức cơ bản

>$$
\begin{align}
f_{best}^{k} - f^* \quad \le \quad \frac{R^{2}+G^{2}\sum_{i=1}^{k}\alpha_{i}^{2}}{2\sum_{i=1}^{k}\alpha_{i}} 
\end{align}
$$

## Chứng minh

Nếu $$x^*$$ là một điểm tối ưu của hàm $$f$$, ta có khai triển bình phương khoảng cách:

>$$
\begin{alignat}{1}
 \Vert x^{(k+1)}-x^* \Vert _2^{2} & \quad = \quad  \Vert x^{(k)}-\alpha_k g^{(k)}-x^* \Vert _2^{2}  \\
                                   & \quad = \quad  \Vert (x^{(k)}-x^*)-\alpha_k g^{(k)} \Vert _2^{2}  \\
                                   & \quad = \quad  \Vert x^{(k)}-x^* \Vert _2^2 - 2 \alpha_k g^{(k)T}(x^{(k)}-x^*)+\alpha_k^2 \Vert g^{(k)} \Vert _2^2 \\
\end{alignat} $$

Theo định nghĩa của subgradient, ta có:

>$$
\begin{alignat}{1}
f(x^*) \ge f(x^{(k)}) + g^{(k)T}(x^*-x^{(k)}) & \quad \Longleftrightarrow \quad f(x^*)-f(x^{(k)}) \ge  g^{(k)T}(x^*-x^{(k)}) \\
                     & \quad  \Longleftrightarrow \quad f(x^{(k)}) - f(x^*) \le  g^{(k)T}(x^{(k)}-x^*) \\
                     & \quad \Longleftrightarrow \quad -2\alpha_{k}(f(x^{(k)}) - f(x^*)) \ge  -2\alpha_{k}(g^{(k)T}(x^{(k)}-x^*)) \\
                     & \quad \Longleftrightarrow \quad -2\alpha_{k}(g^{(k)T}(x^{(k)}-x^*)) \le -2\alpha_{k}(f(x^{(k)})-f(x^*)) \\
\end{alignat} $$

Thay bất đẳng thức này vào biểu thức khai triển ở trên và cộng dồn theo các bước lặp, ta thu được bất đẳng thức cơ bản đã phát biểu ở đầu bài.
