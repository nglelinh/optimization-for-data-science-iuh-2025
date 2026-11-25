---
layout: post
title: 03-05 Hàm log-lõm và log-lồi
chapter: '03'
order: 13
owner: Minjoo Lee
categories:
- chapter03
lang: vi
---

Hãy nhìn vào đường cong hình chuông của phân phối chuẩn Gauss $$p(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}$$: nó cong xuống quanh đỉnh $$x = 0$$ nhưng lại cong lên ở hai phần đuôi $$|x| > 1$$, tức nó **không lồi cũng không lõm**! Thế nhưng chỉ cần đeo "chiếc kính logarit" vào, $$\log p(x) = -\frac{1}{2}x^2 - \frac{1}{2}\log(2\pi)$$ lập tức biến thành một parabol **lõm chặt** hoàn hảo! Đó chính là sức mạnh của **hàm log-lõm** và **hàm log-lồi** — chiếc cầu nối trực tiếp giữa xác suất thống kê với tối ưu hóa lồi.

Bài học này trình bày định nghĩa, điều kiện đạo hàm cấp hai và hàng loạt tính chất bảo toàn tuyệt đẹp (như phép nhân, tích phân và tích chập!) của họ hàm log-lõm / log-lồi.

## Kiến thức cần nhớ: Bốn tính chất của Log-lõm và Log-lồi

- **Định nghĩa:** Với hàm dương $$f(x) > 0$$ trên miền lồi, $$f$$ là **log-lõm** nếu $$\log f$$ lõm (tương đương $$f(\theta x + (1-\theta)y) \ge f(x)^\theta f(y)^{1-\theta}$$); $$f$$ là **log-lồi** nếu $$\log f$$ lồi (và mọi hàm log-lồi đều tự động là hàm lồi!).
- **Điều kiện bậc hai (một biến):** $$f$$ log-lõm $$\iff f(x) f''(x) \le [f'(x)]^2$$; $$f$$ log-lồi $$\iff f(x) f''(x) \ge [f'(x)]^2$$.
- **Phép toán bảo toàn khác hẳn hàm lồi thường:**
  - **Tích** của hai hàm log-lõm là log-lõm (vì $$\log(fg) = \log f + \log g$$); **tổng** của hai hàm log-lồi là log-lồi (nhưng tổng hai hàm log-lõm thì *chưa chắc* log-lõm!).
  - **Định lý Prékopa (phép tích phân và tích chập):** Tích phân biên theo một biến của hàm mật độ log-lõm vẫn là log-lõm — nhờ đó **hàm phân phối tích lũy (CDF)** $$\Phi(x) = \int_{-\infty}^x p(t)\,dt$$ của phân phối chuẩn cũng là hàm log-lõm!
- **Ứng dụng trong MLE và bài toán ràng buộc xác suất:** Giúp chuyển các ràng buộc dạng $$\mathbb{P}(a^T x \le b) \ge \eta$$ thành ràng buộc lồi giải được bằng phần mềm.

### Giải thích: Phân loại 3 hàm quen thuộc theo bậc thang Lồi / Log-lõm / Log-lồi

Hãy kiểm tra bằng đạo hàm bậc hai của $$f$$ và $$\ln f$$ trên từng hàm:

1. **Hàm Gauss $$f(x) = e^{-x^2/2}$$ trên $$\mathbb{R}$$:**
   - $$f''(x) = (x^2 - 1)e^{-x^2/2}$$ đổi dấu tại $$x = \pm 1 \implies$$ không lồi, không lõm.
   - Nhưng $$\ln f(x) = -\frac{1}{2}x^2 \implies (\ln f)''(x) = -1 < 0 \implies$$ **log-lõm chặt**!
2. **Hàm $$g(x) = x^2$$ trên $$x > 0$$ (cẩn thận nhầm lẫn!):**
   - $$g''(x) = 2 > 0 \implies g$$ là **hàm lồi chặt**.
   - Nhưng $$\ln g(x) = 2\ln x \implies (\ln g)''(x) = -\frac{2}{x^2} < 0 \implies g$$ lại là **hàm log-lõm**! (Một hàm hoàn toàn có thể *vừa lồi vừa log-lõm*!)
3. **Hàm $$h(x) = e^{x^2}$$ trên $$\mathbb{R}$$:**
   - $$\ln h(x) = x^2 \implies (\ln h)''(x) = 2 > 0 \implies$$ **log-lồi** (và tự động là hàm lồi!).

---

Phần này giới thiệu các hàm log-lõm và log-lồi — hai lớp hàm quan trọng trong xác suất, thống kê và tối ưu hóa.

## Định nghĩa

### Hàm lõm logarithm (log-lõm)
Một hàm $$f : \mathbb{R}^n \rightarrow \mathbb{R}$$ thỏa mãn $$f(x) > 0$$ với mọi $$x \in \text{dom}f$$ được gọi là **lõm logarithm** (hay **log-lõm**) nếu $$\log f$$ là hàm lõm:
> $$f$$ là log-lõm với $$f(x) > 0$$ cho mọi $$x \in \text{dom}f$$ khi và chỉ khi:<br>
>$$f(\theta x + (1 - \theta) y) \geq f(x)^\theta f(y)^{1-\theta}$$ với mọi $$x, y \in \text{dom}f$$ và $$0 \leq \theta \leq 1$$.

### Hàm lồi logarithm (log-lồi)
Một hàm $$f : \mathbb{R}^n \mapsto \mathbb{R}$$ thỏa mãn $$f(x) > 0$$ với mọi $$x \in \text{dom}f$$ được gọi là **lồi logarithm** (hay **log-lồi**) nếu $$\log f$$ là hàm lồi. Do đó, $$f$$ là log-lồi khi và chỉ khi $$1/f$$ là log-lõm:
> $$f$$ là log-lồi với $$f(x) > 0$$ cho mọi $$x \in \text{dom}f$$ $$\Longleftrightarrow \frac{1}{f}$$ là log-lõm.

Trong một số bối cảnh, ta cho phép $$f$$ nhận giá trị bằng 0 với quy ước $$\log 0 = -\infty$$; khi đó $$f$$ vẫn được gọi là log-lõm nếu hàm giá trị thực mở rộng $$\log f$$ là hàm lõm.

**Vì hàm logarithm đơn điệu tăng, mọi hàm log-lồi đều là hàm giả lồi và mọi hàm log-lõm đều là hàm giả lõm.**

## Ví dụ

### Hàm affine
Hàm affine dương sau đây là hàm log-lõm:
>$$f(x) = a^Tx + b$$ trên $$\{x \mid a^Tx + b > 0\}$$

### Hàm lũy thừa
$$f(x) = x^a$$ trên $$\mathbb{R}_{++}$$ là hàm log-lồi khi $$a \leq 0$$ và là hàm log-lõm khi $$a \geq 0$$.

### Hàm mũ
$$f(x) = e^{ax}$$ vừa là hàm log-lồi vừa là hàm log-lõm.

### Hàm phân phối tích lũy của phân phối chuẩn (Gauss)
$$\Phi(x) = \frac{1}{ \sqrt{2 \pi } } \int_{-\infty}^x e^{-u^2/2} du$$ là hàm log-lõm.

### Hàm Gamma
$$\Gamma(x) = \int_0^\infty u^{x-1}e^{-u} du$$ là hàm log-lồi với $$x \geq 1$$ (thực tế đúng trên toàn bộ $$\mathbb{R}_{++}$$).

### Định thức
$$\det X$$ là hàm log-lõm trên $$\mathbb{S}^n_{++}$$.

### Tỉ số giữa định thức và vết
$$\det X / \text{tr} X$$ là hàm log-lõm trên $$\mathbb{S}^n_{++}$$.

<br>

## Tính chất

### Hàm log-lồi và log-lõm khả vi hai lần
Nếu $$f$$ khả vi hai lần trên miền lồi $$\text{dom} f$$ và $$f(x) > 0$$, ta có:
>$$\nabla^2 \log f(x) = \frac{1}{f(x)} \nabla^2 f(x) - \frac{1}{f(x)^2}\nabla f(x) \nabla f(x)^T$$

Do đó:<br>
$$f$$ là log-lồi $$\Longleftrightarrow$$ $$f(x) \nabla^2 f(x) \succeq \nabla f(x)\nabla f(x)^T$$ với mọi $$x \in \text{dom} f$$, và<br>
$$f$$ là log-lõm $$\Longleftrightarrow$$ $$f(x) \nabla^2 f(x) \preceq \nabla f(x)\nabla f(x)^T$$ với mọi $$x \in \text{dom} f$$.

<br>

### Phép nhân
Tính log-lồi và tính log-lõm được bảo toàn qua phép nhân và phép nhân với hằng số dương. Chẳng hạn, nếu $$f$$ và $$g$$ là log-lõm thì tích theo điểm $$h(x) = f(x)g(x)$$ cũng là log-lõm, vì $$\log h(x) = \log f(x) + \log g(x)$$ là tổng của hai hàm lõm.

### Phép cộng và tích phân của hàm log-lồi
Nhìn chung, tổng của hai hàm log-lõm không nhất thiết log-lõm; tuy nhiên tính log-lồi được bảo toàn qua phép cộng. Thật vậy, nếu $$f$$ và $$g$$ là các hàm log-lồi thì $$F = \log f$$ và $$G = \log g$$ đều lồi. Áp dụng quy tắc hợp thành vector cho hàm log-sum-exp (là hàm lồi và không giảm theo từng biến), ta thấy:

>$$\log(\exp F + \exp G) = \log(f + g)$$

là một hàm lồi, do đó $$f + g$$ là hàm log-lồi.

Tổng quát hóa sang dạng tích phân: nếu $$f(x, y)$$ là log-lồi theo $$x$$ với mọi $$y \in C$$, thì hàm $$g(x)$$ sau đây cũng là log-lồi:
>$$g(x) = \int_C f(x,y)\, dy$$

### Tích phân và tích chập của hàm log-lõm
Tính log-lõm cũng được bảo toàn khi lấy tích phân theo một nhóm biến: nếu $$f : \mathbb{R}^n \times \mathbb{R}^m \mapsto \mathbb{R}$$ là hàm log-lõm đồng thời theo $$(x, y)$$, thì hàm biên $$g(x)$$ là log-lõm theo $$x \in \mathbb{R}^n$$:
>$$f : \mathbb{R}^n \times \mathbb{R}^m \mapsto \mathbb{R}$$ là log-lõm $$\Longrightarrow$$ $$g(x) = \int f(x,y)\, dy$$ là log-lõm theo $$x \in \mathbb{R}^n$$.

Từ kết quả này suy ra mọi phân phối biên của một mật độ xác suất log-lõm đều là hàm log-lõm.<br>

Tính log-lõm cũng được bảo toàn qua phép tích chập: nếu $$f$$ và $$g$$ là các hàm log-lõm trên $$\mathbb{R}^n$$ thì tích chập của chúng cũng là hàm log-lõm:
>$$f, g$$ là log-lõm trên $$\mathbb{R}^n \Longrightarrow (f \ast g)(x) = \int f(x-y)g(y)\, dy$$ là log-lõm.<br>
