---
layout: post
title: 03-01-02 Ví dụ về hàm lồi
chapter: '03'
order: 4
owner: Minjoo Lee
categories:
- chapter03
lang: vi
---

Khi xây dựng mô hình tối ưu trong thực tế — từ hồi quy bình phương tối thiểu, phạt điều chuẩn chuẩn $$\ell_1/\ell_2$$, hàm mất mát logistic, đến bài toán gán nhãn bằng hàm log-sum-exp — bạn sẽ bắt gặp đi bắt gặp lại cùng một nhóm khoảng một chục "hàm lồi nguyên tử". Thuộc lòng bảng tuần hoàn các hàm lồi nguyên tử này (cùng miền xác định của chúng!) là bí quyết để bạn nhận diện ngay một bài toán tối ưu lồi chỉ bằng mắt thường.

Bài học này tổng hợp đầy đủ các ví dụ hàm lồi một biến, đa biến, chuẩn, hàm bậc hai và hàm chỉ thị của tập lồi.

## Bản đồ kiến thức nền: Bảng tuần hoàn các hàm lồi nguyên tử

- **Hàm một biến cốt lõi:** $$e^{ax}$$ (mọi $$a$$), $$x^p$$ trên $$\mathbb{R}_{++}$$ (lồi khi $$p \ge 1$$ hoặc $$p \le 0$$; lõm khi $$0 \le p \le 1$$), $$-\log x$$ và $$x\log x$$ trên $$\mathbb{R}_{++}$$ (âm entropy).
- **Hàm affine và hàm bậc hai:** Mọi hàm affine $$a^T x + b$$ vừa lồi vừa lõm; hàm bậc hai $$\frac{1}{2}x^T P x + q^T x + r$$ lồi khi và chỉ khi $$P \succeq 0$$ (bao gồm hàm mất mát bình phương tối thiểu $$\|Ax - b\|_2^2$$ vì $$A^T A \succeq 0$$ luôn đúng!).
- **Mọi chuẩn và hàm log-sum-exp:** Bất kỳ chuẩn nào $$\|x\|$$ đều lồi nhờ bất đẳng thức tam giác; hàm $$\operatorname{lse}(x) = \log(\sum e^{x_i})$$ là xấp xỉ trơn, lồi của hàm $$\max_i x_i$$.
- **Hàm chỉ thị (Indicator Function $$I_C(x)$$):** Bằng $$0$$ nếu $$x \in C$$ và $$+\infty$$ nếu $$x \notin C$$. Hàm $$I_C$$ lồi khi và chỉ khi $$C$$ là tập lồi — cho phép nhúng mọi ràng buộc $$x \in C$$ vào thẳng hàm mục tiêu $$\min_x f(x) + I_C(x)$$!

### Khung giải thích (nên đọc chậm): Kiểm chứng tính lồi và độ sát của hàm Log-Sum-Exp với $$\max$$

Xét hàm log-sum-exp 2 biến $$f(x_1, x_2) = \ln(e^{x_1} + e^{x_2})$$ — nền tảng của hàm mất mát Softmax / Cross-Entropy trong học sâu:

1. **Tính giá trị tại hai điểm đối xứng $$x = (0, 2)$$ và $$y = (2, 0)$$:**
   $$f(0, 2) = f(2, 0) = \ln(e^0 + e^2) = \ln(1 + 7.389) = \ln(8.389) \approx 2.127.$$
2. **Kiểm tra bất đẳng thức Jensen tại trung điểm $$z = (1, 1)$$:**
   $$f(1, 1) = \ln(e^1 + e^1) = \ln(2e) = 1 + \ln 2 \approx 1.693.$$
   Rõ ràng $$1.693 \le 0.5(2.127) + 0.5(2.127) = 2.127$$ — bất đẳng thức lồi thỏa mãn chặt!
3. **Kiểm tra kẹp chặt với hàm $$\max(x_1, x_2)$$:**
   Với mọi $$x \in \mathbb{R}^n$$, luôn có $$\max_i x_i \le \ln\sum_{i=1}^n e^{x_i} \le \max_i x_i + \ln n$$.
   Tại $$x = (0, 2)$$ ($$n = 2,\ \ln 2 \approx 0.693$$): $$\max(0, 2) = 2 \le 2.127 \le 2 + 0.693 = 2.693$$ — log-sum-exp chính là phiên bản "mài tròn góc nhọn" lồi tuyệt đẹp của hàm $$\max$$!

---

Phần này điểm qua các ví dụ điển hình về hàm lồi, gồm:

* Hàm mũ
* Hàm lũy thừa
* Hàm affine
* Hàm bậc hai
* Hàm mất mát bình phương tối thiểu
* Chuẩn
* Hàm chỉ thị
* Hàm hỗ trợ
* Hàm max

## Hàm một biến

* **Hàm mũ:** Với mọi số thực $$a$$, hàm $$e^{ax}$$ là hàm lồi trên $$\mathbb{R}$$.
> $$e^{ax}$$ là hàm lồi với mọi $$a \in \mathbb{R}$$

* **Hàm lũy thừa:** Với $$x \in \mathbb{R}_{++}$$ (tức $$x > 0$$) và $$a \in \mathbb{R}$$, tính lồi hay lõm của $$x^a$$ phụ thuộc vào giá trị của số mũ $$a$$:
> $$x^{a}$$ là hàm lồi trên $$\mathbb{R}_{++}$$ với mọi $$a \geq 1$$ hoặc $$a \leq 0$$
> $$x^{a}$$ là hàm lõm trên $$\mathbb{R}_{++}$$ với mọi $$0 \leq a \leq 1$$

## Hàm affine

Như đã nêu trong bài [03-01-01]({% multilang_post_url contents/chapter03/21-02-12-03_01_01_convex_functions_definition %}), mọi hàm affine đều vừa lồi vừa lõm.

* Trên $$\mathbb{R}$$ và $$\mathbb{R}^n$$:
> $$a^Tx + b$$ vừa lồi vừa lõm

* Trên $$\mathbb{R}^{m \times n}$$:
> $$\text{tr}(A^TX) + b = \sum_{i=1}^m\sum_{j=1}^n A_{ij}X_{ij} + b$$ vừa lồi vừa lõm

## Hàm bậc hai

Xét hàm bậc hai $$f(x)=\frac{1}{2}x^TPx+q^Tx+r$$, có gradient $$\nabla f(x)= Px+q$$ và ma trận Hessian $$\nabla^2f(x) = P$$. Nếu $$P$$ là ma trận nửa xác định dương ($$P \succeq 0$$) thì $$f(x)$$ là hàm lồi:
> $$f(x)=\frac{1}{2}x^TPx+q^Tx+r$$ là hàm lồi với $$P \in \mathbb{S}^n_+$$, $$q \in \mathbb{R}^n$$, $$r \in \mathbb{R}$$

**Hỏi: Tại sao $$f(x)$$ lồi khi $$P$$ là ma trận nửa xác định dương?**
**Đáp:** Đối với hàm bậc hai, ma trận Hessian $$\nabla^2 f(x) = P$$ phản ánh độ cong của hàm theo mọi phương. Khi $$P \succeq 0$$, độ cong theo mọi hướng đều không âm (đồ thị luôn hướng bề lõm lên trên), nên hàm là hàm lồi.

## Hàm mất mát bình phương tối thiểu

Với mọi ma trận $$A$$, ma trận $$A^TA$$ luôn nửa xác định dương, do đó hàm $$\left \| Ax - b \right \|_{2}^{2}$$ luôn là hàm lồi:

> $$f(x) = \| Ax - b \|_{2}^{2}$$ là hàm lồi với mọi $$A$$

## Chuẩn

Mọi chuẩn trên $$\mathbb{R}^n$$ đều là hàm lồi. Nếu $$f:\mathbb{R}^n \mapsto \mathbb{R}$$ là một chuẩn thì theo bất đẳng thức tam giác và tính thuần nhất bậc một, ta có:
>$$
\begin{aligned}
f(\theta x+(1-\theta)y) \le \theta f(x)+(1-\theta)f(y), \text{ với } 0 \le \theta \le 1, \text{ cho mọi } x,y \in \text{dom} f,
\end{aligned}
$$
>$$
\begin{aligned}
\|x\|_{p} = \left(\sum_{i=1}^{n} |x_i|^p\right)^{1/p} \text{ với } p \geq 1, \quad \|x\|_\infty = \max_{i=1,.., n} |x_i|\\
\end{aligned} 
$$

## Hàm chỉ thị

Với một **tập lồi** $$C$$ cho trước, hàm chỉ thị $$I_C$$ nhận giá trị $$0$$ với các điểm thuộc $$C$$ và $$+\infty$$ với các điểm ngoài $$C$$ là một hàm lồi:

>$$I_{C} (x) =
\begin{cases}
0, & x \in C\\
\infty, & x \notin C\\
\end{cases}
$$

## Hàm hỗ trợ

Xét một tập $$C$$ bất kỳ. Dù $$C$$ có lồi hay không, hàm hỗ trợ của $$C$$ luôn là hàm lồi:
> $$I_{C}^{*} (x) = \sup_{y\in C} x^Ty$$ là hàm lồi

Xem thêm [định nghĩa hàm hỗ trợ trên Wikipedia](https://en.wikipedia.org/wiki/Support_function).

## Hàm max

Giá trị lớn nhất theo từng điểm của một họ hữu hạn các hàm lồi là một hàm lồi; về mặt hình học, bao trên của các đồ thị hàm lồi vẫn là một hàm lồi. Đặc biệt:
> $$f(x) = \max \{x_1,..., x_n\}$$ là hàm lồi
