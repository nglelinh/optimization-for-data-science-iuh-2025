---
layout: post
title: '08-02-02 Hội tụ của các Phương pháp Ngẫu nhiên'
chapter: '08'
order: 13
owner: Kyeongmin Woo
categories:
- chapter08
lang: vi
---

Một câu hỏi rất tự nhiên sau khi thấy ví dụ chạy thử là: *nếu mỗi bước ta chỉ nhìn một phần nhỏ của hàm mục tiêu rồi bước theo hướng ồn ào của riêng nó, liệu thuật toán có bị kéo lạc mãi ra xa không?* Đáp án vừa quen vừa mới: cả biến thể tuần hoàn lẫn biến thể ngẫu nhiên đều hội tụ dưới đúng những quy tắc kích thước bước ta đã quen ở phần batch, nhưng **nghĩa của sự hội tụ** và **kích thước sàn sai số** có sự khác biệt tinh tế.

Với bước cố định $$t$$, ngay cả khi bạn đặt thuật toán ngay chính giữa nghiệm tối ưu $$x^*$$, nhiễu từ các thành phần $$f_i$$ khác nhau vẫn lập tức "đá" điểm lặp văng ra khỏi $$x^*$$, tạo nên một quỹ đạo dao động trong lân cận của nghiệm. Còn với bước giảm dần thỏa $$\sum t_k = \infty, \sum t_k^2 < \infty$$, biên độ của những cú đá ấy nhỏ dần về $$0$$, giúp giá trị hàm tốt nhất hội tụ về đúng $$f^*$$ (hội tụ tất định với bản tuần hoàn, và hội tụ theo kỳ vọng / hầu chắc chắn với bản ngẫu nhiên).

## Kiến thức cần nhớ: Ba trụ cột của lý thuyết hội tụ ngẫu nhiên

- **Hội tụ theo kỳ vọng và hầu chắc chắn (Expectation & Almost Sure Convergence):** Vì dãy $$x^{(k)}$$ là dãy biến ngẫu nhiên phụ thuộc vào chuỗi chỉ số rút thăm $$i_1, i_2, \dots$$, ta đánh giá $$\mathbb{E}[f_{\text{best}}^{(k)}] - f^* \to 0$$ (hoặc hội tụ hầu chắc chắn bằng bổ đề siêu martingale Robbins–Siegmund).
- **Nhiễu tại nghiệm tối ưu (Gradient Noise at Optimum):** Tại $$x^*$$, tổng subgradient bằng $$0$$ ($$\sum_{i=1}^m g_i(x^*) = 0$$), nhưng từng $$g_i(x^*)$$ nói chung **khác $$0$$**! Chính phương sai nội tại này tạo ra sàn sai số không thể xóa bỏ khi dùng bước cố định $$t$$.
- **Khác biệt giữa sàn sai số tuần hoàn và ngẫu nhiên:** Trong biến thể tuần hoàn, sai lệch có thể cộng dồn qua trọn một vòng $$m$$ mẫu (tạo hệ số lớn hơn theo $$m$$), trong khi bản ngẫu nhiên triệt tiêu sai số chéo nhờ tính độc lập giữa các bước, cho sàn sai số chặt hơn rõ rệt khi $$m$$ lớn.

### Giải thích: Minh họa vì sao bước cố định luôn bị "đá" khỏi nghiệm tối ưu

Xét bài toán gồm 2 hàm thành phần lồi trên $$\mathbb{R}$$:
$$f_1(x) = 2|x - 1|, \quad f_2(x) = |x + 1|, \quad f(x) = f_1(x) + f_2(x).$$
Kiểm tra tại $$x = 1$$: $$\partial f_1(1) = [-2, 2]$$ và $$\nabla f_2(1) = 1$$, nên $$\partial f(1) = [-1, 3] \ni 0$$. Vậy $$x^* = 1$$ là **nghiệm tối ưu duy nhất** với $$f^* = 0 + 2 = 2$$.

1. **Khởi đầu ngay tại nghiệm tối ưu $$x^{(0)} = x^* = 1$$ với bước cố định $$t = 0.5$$:**
   - Nếu bước 1 rút trúng $$i_1 = 2$$: dù $$x^{(0)}$$ đã tối ưu cho $$f$$, ta vẫn có $$g_2(1) = +1 \ne 0$$!
   - Thuật toán cập nhật: $$x^{(1)} = 1 - 0.5(1) = 0.5$$, khiến $$f(0.5) = 2(0.5) + 1.5 = 2.5 > f^* = 2$$!
   - Nếu bước 2 rút trúng $$i_2 = 1$$: $$g_1(0.5) = -2$$, cập nhật $$x^{(2)} = 0.5 - 0.5(-2) = 1.5$$, $$f(1.5) = 2(0.5) + 2.5 = 3.5$$!
2. **Thay bằng bước giảm dần $$t_k = 1/k$$:**
   Khi $$k = 100$$, cú "đá" từ $$f_2$$ chỉ còn dịch chuyển $$x$$ một lượng $$t_{100} \cdot 1 = 0.01$$, làm tăng $$f$$ tối đa $$0.03$$; khi $$k \to \infty$$, bán kính vùng dao động co về đúng $$0$$ và dãy hội tụ về $$f^* = 2$$.

Giả sử mỗi hàm thành phần $$f_i$$ ($$i = 1,...,m$$) là hàm lồi và liên tục Lipschitz với hằng số $$G$$.

Đối với phương pháp subgradient ngẫu nhiên, ta có hai kết quả hội tụ tương ứng với kích thước bước cố định và kích thước bước giảm dần:

- **Kích thước bước cố định** $$t_k = t$$ ($$k = 1, 2, 3, ...$$):

>$$\text{Đối với cả hai biến thể tuần hoàn và ngẫu nhiên với kích thước bước cố định, ta có:} \\
\begin{align}
\lim_{k\to\infty} f(x_{best}^{(k)}) \le f^{*} + 5m^{2}G^{2}t/2
\end{align}
$$

Trong đó, $$mG$$ là hằng số Lipschitz của hàm tổng $$\sum_{i=1}^{m} f_i$$.

- **Kích thước bước giảm dần**:

>$$\text{Đối với cả hai biến thể tuần hoàn và ngẫu nhiên với kích thước bước giảm dần, ta có:} \\
\begin{align}
\lim_{k\to\infty} f(x_{best}^{(k)}) = f^{*}
\end{align}
$$
