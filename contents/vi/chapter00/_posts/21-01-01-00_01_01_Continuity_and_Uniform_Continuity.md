---
layout: post
title: 00-01-01 Tính liên tục và Tính liên tục đều
chapter: '00'
order: 3
owner: GitHub Copilot
lang: vi
categories:
- chapter00
lesson_type: required
---

Thoạt nghe, phân biệt giữa *liên tục*, *liên tục đều* và *liên tục Lipschitz* có vẻ là trò chơi tỉ mỉ của giới giải tích thuần túy với các ký hiệu $$\epsilon$$–$$\delta$$. Thế nhưng trong tối ưu hóa, sự khác biệt đó lại quyết định trực tiếp việc một thuật toán có hội tụ ổn định hay bị "nổ" giá trị khi bước nhảy không phù hợp: một hàm chỉ liên tục thôi vẫn có thể có độ dốc dựng đứng vô hạn ở đâu đó, khiến bước nhảy cố định làm thuật toán văng khỏi quỹ đạo.

Bài học này giúp bạn nhìn thấu bậc thang chặt chẽ dần từ liên tục điểm đến liên tục đều và liên tục Lipschitz — khái niệm xuất hiện trong hầu hết mọi định lý hội tụ của tối ưu hóa hiện đại.

## Kiến thức cần nhớ: Từ liên tục cục bộ đến kiểm soát tốc độ biến thiên toàn cục

- **Tính liên tục tại điểm (Pointwise Continuity):** Đảm bảo không có bước nhảy đứt gãy tại $$x_0$$; tuy nhiên bán kính an toàn $$\delta$$ có thể phải thu nhỏ tùy ý khi $$x_0$$ thay đổi vị trí.
- **Tính liên tục đều (Uniform Continuity):** Nâng chuẩn lên mức toàn cục: tồn tại **một** $$\delta(\epsilon)$$ duy nhất dùng chung cho mọi điểm trên miền xét. Trên tập compact (đóng và bị chặn), định lý Heine–Cantor bảo đảm mọi hàm liên tục tự động liên tục đều.
- **Tính liên tục Lipschitz (Lipschitz Continuity):** Đặt một "trần tốc độ" tuyến tính rõ ràng: $$|f(x) - f(y)| \le L\|x - y\|$$. Hằng số $$L$$ chính là cận trên toàn cục của độ dốc, cho phép tính trước số vòng lặp cần thiết để đạt sai số $$\epsilon$$.
- **Chuỗi bao hàm trong tối ưu hóa:** $$\text{Lipschitz} \subset \text{Liên tục đều} \subset \text{Liên tục}$$. Trong nhiều bài toán học máy, ta cần $$L$$-Lipschitz cho bản thân hàm $$f$$ (với hàm không trơn như ReLU, Hinge loss) hoặc cho gradient $$\nabla f$$ (gọi là tính trơn $$L$$-smooth).

### Giải thích: Vì sao $$f(x) = x^2$$ Lipschitz trên $$[0, 3]$$ nhưng không liên tục đều trên $$\mathbb{R}$$?

Hãy tự kiểm chứng bằng tay trên hàm quen thuộc $$f(x) = x^2$$:

1. **Trên đoạn đóng $$[0, 3]$$ (Lipschitz với $$L = 6$$):** Với mọi $$x, y \in [0, 3]$$, ta phân tích:
   $$|f(x) - f(y)| = |x^2 - y^2| = |x + y|\cdot |x - y| \le (3 + 3)|x - y| = 6|x - y|.$$
   Vậy $$f$$ liên tục Lipschitz với hằng số $$L = 6$$, kéo theo liên tục đều trên $$[0, 3]$$.
2. **Trên toàn trục thực $$\mathbb{R}$$ (mất tính liên tục đều):** Chọn hai dãy điểm càng lúc càng sát nhau: $$x_n = n$$ và $$y_n = n + \frac{1}{n}$$.
   - Khoảng cách đầu vào: $$|y_n - x_n| = \frac{1}{n} \to 0$$ khi $$n \to \infty$$ (chẳng hạn tại $$n = 100$$, hai điểm chỉ cách nhau $$0.01$$).
   - Độ lệch đầu ra:
     $$|f(y_n) - f(x_n)| = \left(n + \frac{1}{n}\right)^2 - n^2 = 2 + \frac{1}{n^2} > 2.$$
   Dù $$x_n$$ và $$y_n$$ gần nhau tới mức nào, đầu ra vẫn cách nhau hơn $$2$$ đơn vị! Không tồn tại một $$\delta$$ chung cho $$\epsilon = 1$$ trên toàn $$\mathbb{R}$$, nên $$x^2$$ **không** liên tục đều trên $$\mathbb{R}$$ — đó cũng là lý do các định lý hội tụ thường đòi hỏi chặn miền làm việc hoặc giả thiết gradient Lipschitz.

---

Bài học này giới thiệu các khái niệm cơ bản về tính liên tục, tính liên tục đều và tính liên tục Lipschitz — những công cụ nền tảng giúp phân tích hành vi của hàm số trong tối ưu hóa.

---

## Tính liên tục và tính liên tục đều

**Tính liên tục** và **tính liên tục đều** là các khái niệm cơ bản mô tả mức độ ổn định của hàm số khi biến đầu vào thay đổi nhỏ. Dù có liên hệ chặt chẽ, hai khái niệm này mang bản chất khác nhau, trong đó tính liên tục đều là điều kiện mạnh hơn so với tính liên tục thông thường.

### Định nghĩa tính liên tục

Một hàm số $$f: A \to \mathbb{R}$$ được gọi là **liên tục tại điểm** $$c \in A$$ nếu với mọi số thực dương $$\varepsilon > 0$$, tồn tại một số thực dương $$\delta > 0$$ sao cho với mọi $$x \in A$$, nếu

$$\lvert x - c \rvert < \delta$$

thì

$$\lvert f(x) - f(c) \rvert < \varepsilon.$$

Về mặt trực quan, với mọi ngưỡng sai số $$\varepsilon$$ cho trước ở đầu ra $$f(x)$$, ta luôn tìm được một lân cận đủ nhỏ quanh $$c$$ (có độ rộng $$2\delta$$) sao cho mọi giá trị $$x$$ trong lân cận đó đều có ảnh $$f(x)$$ nằm trong khoảng $$\varepsilon$$ quanh $$f(c)$$. Điểm quan trọng cần lưu ý là giá trị $$\delta$$ nói chung không chỉ phụ thuộc vào $$\varepsilon$$ mà còn phụ thuộc vào vị trí của điểm $$c$$.

Một hàm số được gọi là **liên tục trên tập hợp** $$A$$ nếu nó liên tục tại mọi điểm $$c \in A$$.

**Ví dụ về các hàm liên tục** gồm mọi đa thức (chẳng hạn $$f(x) = x^2 + 3x - 1$$), các hàm lượng giác như $$\sin(x)$$, $$\cos(x)$$ và hàm mũ $$e^x$$ trên miền xác định tương ứng của chúng.

### Định nghĩa tính liên tục đều

**Tính liên tục đều** đặt ra một điều kiện chặt chẽ hơn. Một hàm số $$f: A \to \mathbb{R}$$ được gọi là **liên tục đều trên tập hợp** $$A$$ nếu với mọi số thực dương $$\varepsilon > 0$$, tồn tại một số thực dương $$\delta > 0$$ sao cho với mọi $$x, y \in A$$, nếu

$$\lvert x - y \rvert < \delta$$

thì

$$\lvert f(x) - f(y) \rvert < \varepsilon.$$

**Điểm khác biệt cốt lõi** so với tính liên tục tại điểm nằm ở thứ tự của các lượng từ: đối với tính liên tục **đều**, $$\delta$$ chỉ phụ thuộc vào $$\varepsilon$$ và dùng chung cho mọi cặp điểm $$x, y$$ trên toàn miền xác định $$A$$.

### Định nghĩa tính liên tục Lipschitz

**Tính liên tục Lipschitz** đưa ra một điều kiện định lượng cụ thể hơn cho tính liên tục. Một hàm số $$f: A \to \mathbb{R}$$ được gọi là **liên tục Lipschitz** (hoặc **$$L$$-Lipschitz**) trên tập hợp $$A$$ nếu tồn tại hằng số $$L \geq 0$$ sao cho với mọi $$x, y \in A$$:

$$\lvert f(x) - f(y) \rvert \leq L \lvert x - y \rvert.$$

Hằng số $$L$$ nhỏ nhất thỏa mãn bất đẳng thức trên được gọi là **hằng số Lipschitz** của $$f$$.

**Các tính chất chính của tính liên tục Lipschitz:**

1. **Tốc độ thay đổi bị chặn**: điều kiện Lipschitz đảm bảo hàm số không thay đổi nhanh hơn tốc độ tuyến tính xác định bởi $$L$$.
2. **Suy ra tính liên tục đều**: mọi hàm liên tục Lipschitz đều liên tục đều (với $$L > 0$$, chỉ cần chọn $$\delta = \varepsilon / L$$).
3. **Khả vi hầu khắp nơi**: hàm liên tục Lipschitz khả vi hầu khắp nơi, và tại mọi điểm khả vi ta có $$\lvert f'(x) \rvert \leq L$$.

**Ví dụ:**
- $$f(x) = \lvert x \rvert$$ là $$1$$-Lipschitz trên $$\mathbb{R}$$.
- $$f(x) = \sin(x)$$ là $$1$$-Lipschitz trên $$\mathbb{R}$$ (vì $$\lvert \cos(x) \rvert \leq 1$$).
- $$f(x) = x^2$$ không liên tục Lipschitz trên $$\mathbb{R}$$, nhưng liên tục Lipschitz trên mọi khoảng bị chặn.

### Sự khác biệt chính và quan hệ bao hàm

Ba lớp hàm liên tục tạo thành một thứ bậc theo mức độ chặt chẽ của điều kiện:

**Liên tục Lipschitz ⊆ Liên tục đều ⊆ Liên tục**

1. **Tính chất cục bộ và tính chất toàn cục**:
   - **Tính liên tục**: tính chất cục bộ (kiểm tra riêng tại từng điểm).
   - **Tính liên tục đều**: tính chất toàn cục trên cả miền xác định.
   - **Tính liên tục Lipschitz**: tính chất toàn cục kèm theo cận định lượng tường minh.

2. **Cách chọn $$\delta$$**:
   - **Tính liên tục**: $$\delta$$ có thể phụ thuộc vào cả $$\varepsilon$$ lẫn điểm $$c$$.
   - **Tính liên tục đều**: $$\delta$$ chỉ phụ thuộc vào $$\varepsilon$$, áp dụng đồng thời cho mọi điểm trên miền xác định.
   - **Tính liên tục Lipschitz**: $$\delta = \varepsilon / L$$ cho công thức tường minh theo $$\varepsilon$$ và $$L$$.

3. **Kiểm soát tốc độ thay đổi**:
   - **Tính liên tục**: không kiểm soát tốc độ thay đổi.
   - **Tính liên tục đều**: đảm bảo độ biến thiên của hàm nhỏ trên các khoảng đủ nhỏ một cách đồng đều.
   - **Tính liên tục Lipschitz**: chặn tốc độ thay đổi bằng một cận tuyến tính cụ thể.

4. **Quan hệ kéo theo**:
   - Mọi hàm liên tục Lipschitz đều liên tục đều.
   - Mọi hàm liên tục đều đều liên tục.
   - Các chiều ngược lại nhìn chung không đúng.

### Ví dụ chi tiết và so sánh

**Ví dụ 1: $$f(x) = x^2$$**
- **Trên $$\mathbb{R}$$**: liên tục nhưng không liên tục đều (tốc độ thay đổi $$\lvert f'(x) \rvert = 2\lvert x \rvert$$ không bị chặn).
- **Trên $$[0,1]$$**: liên tục, liên tục đều và liên tục Lipschitz với $$L = 2$$.

**Ví dụ 2: $$f(x) = \sin(x)$$**
- **Trên $$\mathbb{R}$$**: liên tục, liên tục đều và $$1$$-Lipschitz (vì $$\lvert \cos(x) \rvert \leq 1$$).

**Ví dụ 3: $$f(x) = \lvert x \rvert$$**
- **Trên $$\mathbb{R}$$**: liên tục, liên tục đều và $$1$$-Lipschitz.
- **Lưu ý**: hàm không khả vi tại $$x = 0$$ nhưng vẫn liên tục Lipschitz.

**Ví dụ 4: $$f(x) = \sqrt{x}$$**
- **Trên $$[0,1]$$**: liên tục và liên tục đều, nhưng không liên tục Lipschitz (đạo hàm không bị chặn gần $$x = 0$$).
- **Trên $$[a,1]$$ với $$a > 0$$**: liên tục Lipschitz với $$L = 1/(2\sqrt{a})$$.
