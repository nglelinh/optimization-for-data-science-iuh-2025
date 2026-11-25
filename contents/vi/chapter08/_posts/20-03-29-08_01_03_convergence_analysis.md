---
layout: post
title: '08-01-03 Phân tích hội tụ'
chapter: '08'
order: 5
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
lesson_type: required
---

Trong giải tích tối ưu, câu hỏi "thuật toán này có hội tụ không?" luôn đi kèm một câu hỏi sắc bén hơn: *"Hội tụ dưới giả thiết tối thiểu nào, và hội tụ tới đâu?"* Với gradient descent ở Chương 06, ta phải đòi hỏi $$\nabla f$$ liên tục Lipschitz (tức hàm phải đủ "mượt", độ cong không vô hạn). Nhưng với bài toán không trơn, $$\nabla f$$ thậm chí còn không tồn tại tại những điểm quan trọng nhất! Do đó, phương pháp subgradient hạ thấp đòi hỏi xuống một bậc hoàn toàn khác: chỉ cần chính hàm $$f$$ liên tục Lipschitz với hằng số $$G$$.

Cái giá của sự phóng khoáng về giả thiết thể hiện ngay trong kết quả định lý hội tụ: nếu giữ kích thước bước cố định $$t$$, sai số không tiến về $$0$$ mà dừng ở ngưỡng $$G^2 t / 2$$; chỉ khi cho kích thước bước giảm dần đúng chuẩn ($$\sum t_k = \infty, \sum t_k^2 < \infty$$), cả hai phần của phân số trong bất đẳng thức cơ bản mới đồng loạt triệt tiêu về $$0$$. Hiểu rõ cơ chế phân tách hai số hạng này sẽ giúp bạn chẩn đoán ngay vì sao một mô hình học máy đứng yên ở mức loss cố định khi dùng learning rate hằng số.

## Kiến thức cần nhớ: Bốn giả thiết và cơ chế hội tụ

- **Tính liên tục Lipschitz của hàm $$f$$ (thay vì của $$\nabla f$$):** Điều kiện $$|f(x) - f(y)| \le G\|x - y\|_2$$ tương đương với mọi subgradient đều bị chặn chuẩn: $$\|g\|_2 \le G$$ với mọi $$g \in \partial f(x)$$. Lưu ý rằng các hàm bậc hai như $$f(x) = x^2$$ không Lipschitz toàn cục trên $$\mathbb{R}$$, nhưng vẫn Lipschitz trên mọi miền bị chặn chứa quỹ đạo lặp.
- **Phân rã cận sai số thành hai thành phần:** Từ bất đẳng thức cơ bản với bước cố định $$t$$:
  $$f_{\text{best}}^{(k)} - f^* \le \underbrace{\frac{R^2}{2kt}}_{\text{sai số khởi điểm (giảm về } 0\text{)}} + \underbrace{\frac{G^2 t}{2}}_{\text{sàn dao động (không giảm)}}.$$
  Nhìn vào hai số hạng này, ta thấy ngay vì sao tăng $$k \to \infty$$ chỉ xóa được phần thứ nhất mà không xóa được phần thứ hai.
- **Định lý hội tụ cho bước giảm dần:** Khi $$\sum_{i=1}^k t_i \to \infty$$ (mẫu số ra vô cực) trong khi $$\sum_{i=1}^k t_i^2 \to C < \infty$$ (tử số bị chặn), phân số $$\frac{R^2 + G^2\sum_{i=1}^k t_i^2}{2\sum_{i=1}^k t_i}$$ bắt buộc tiến về $$0$$.
- **Khác biệt giữa hội tụ giá trị hàm và hội tụ điểm lặp:** Định lý khẳng định $$f_{\text{best}}^{(k)} \to f^*$$; còn bản thân dãy $$x^{(k)}$$ chỉ hội tụ về tập nghiệm $$X^*$$ khi có thêm giả thiết (chẳng hạn tập nghiệm bị chặn hoặc hàm lồi mạnh).

### Giải thích: Tính trực tiếp hai số hạng sai số cho bước cố định và bước $$t_k = 1/k$$

Giả sử một bài toán lồi không trơn có khoảng cách ban đầu $$R = 4$$ và hằng số Lipschitz $$G = 1$$.

1. **Trường hợp bước cố định $$t = 0.2$$:**
   Cận sai số tại bước $$k$$ là:
   $$f_{\text{best}}^{(k)} - f^* \le \frac{4^2}{2 \cdot k \cdot 0.2} + \frac{1^2 \cdot 0.2}{2} = \frac{40}{k} + 0.1.$$
   - Sau $$k = 40$$ bước: cận là $$1.0 + 0.1 = 1.1$$.
   - Sau $$k = 400$$ bước: cận là $$0.1 + 0.1 = 0.2$$.
   - Sau $$k = 40{,}000$$ bước: cận là $$0.001 + 0.1 = 0.101$$ — chạy thêm hàng chục nghìn bước cũng không phá nổi sàn $$0.1$$!
2. **Trường hợp bước giảm dần $$t_i = 1/i$$:**
   Ta biết tổng điều hòa $$H_k = \sum_{i=1}^k \frac{1}{i} \approx \ln k + 0.577$$, còn $$\sum_{i=1}^k \frac{1}{i^2} < \frac{\pi^2}{6} \approx 1.645$$.
   - Tử số luôn nhỏ hơn $$R^2 + G^2 \cdot 1.645 = 16 + 1.645 = 17.645$$ với mọi $$k$$.
   - Mẫu số $$2 H_k$$ tăng mãi ra vô cực: tại $$k = 100$$, $$2 H_{100} \approx 10.37 \implies \text{cận} \approx 1.70$$; tại $$k = 10^6$$, $$2 H_{10^6} \approx 28.79 \implies \text{cận} \approx 0.61$$.
   - Khi $$k \to \infty$$, cận tiến về đúng $$0$$, không còn sàn sai số — nhưng đổi lại tốc độ co của $$\ln k$$ rất chậm, gợi ý vì sao bài tiếp theo ta cần tìm quy tắc bước tối ưu theo số vòng lặp $$k$$!

Trong gradient descent, ta giả thiết $$\nabla f$$ liên tục Lipschitz; còn trong phương pháp subgradient, ta giả thiết chính hàm $$f$$ liên tục Lipschitz (xem thêm định lý hội tụ của gradient descent tại [06-03-01]({% multilang_post_url contents/chapter06/21-03-20-06_03_01_convergence_analysis_and_proof %})).

Giả sử $$f$$ là hàm lồi với $$\text{dom } f = \mathbb{R}^n$$ và thỏa mãn điều kiện Lipschitz:

>\begin{align}
> | f(x) - f(y) | \le G \lVert x - y \rVert_2 \text{ với mọi } x, y
\end{align}

Dưới các giả thiết này, ta có hai kết quả hội tụ tương ứng với kích thước bước cố định và kích thước bước giảm dần.

## Định lý hội tụ cho kích thước bước cố định

Với kích thước bước cố định $$t_k = t$$:
>\begin{align}
> \lim_{k\to\infty} f(x^{(k)}_{best}) \le f^* + \frac{G^{2}t}{2}
\end{align}

## Định lý hội tụ cho kích thước bước giảm dần

Với kích thước bước giảm dần thỏa mãn điều kiện chuẩn:

>\begin{align}
\lim_{k\to\infty}f(x^{(k)}_{best}) = f^*
\end{align}

## Chứng minh

### Trường hợp kích thước bước cố định

Với kích thước bước cố định, ta có $$\sum_{i=1}^{k}t_{i} = kt$$ và $$\sum_{i=1}^{k}t_{i}^{2} = kt^2$$. Thay vào bất đẳng thức cơ bản:

>$$\begin{align}
& f_{best}^{(k)} - f^* \le \frac{R^{2}+G^{2}\sum_{i=1}^{k}t_{i}^{2}}{2\sum_{i=1}^{k}t_{i}} = \frac{R^{2}+G^{2}k t^{2}}{2kt}  = \frac{R^{2}}{2tk} + \frac{G^{2}t}{2} \\
& \lim_{k→\infty}(f^{(k)}_{best} - f^*) \le 0 + \frac{G^{2}t}{2} = \frac{G^{2}t}{2} \\
& \lim_{k→\infty}(f^{(k)}_{best}) \le f^* + \frac{G^{2}t}{2}
\end{align}
$$

### Trường hợp kích thước bước giảm dần

Chứng minh sử dụng hai điều kiện (1) và (2) của dãy kích thước bước giảm dần:

>$$
\begin{align}
\text{(1)} \sum_{i=1}^{\infty} t_i = \infty, \quad \text{(2)}  \sum_{i=1}^{\infty} t_i^{2} = \beta < \infty
\end{align}
$$

Thay vào bất đẳng thức cơ bản và cho $$k \to \infty$$:

>$$
\begin{align}
& f_{best}^{(k)} - f^* \le \frac{R^{2}+G^{2}\sum_{i=1}^{k}t_{i}^{2}}{2\sum_{i=1}^{k}t_{i}} \\
& \lim_{k→\infty}(f^{(k)}_{best} - f^* ) \le \frac{R^{2}+G^{2}\beta}{2\infty} = 0 \\
& \lim_{k→\infty}(f^{(k)}_{best}) =  f^* \\
\end{align}
$$