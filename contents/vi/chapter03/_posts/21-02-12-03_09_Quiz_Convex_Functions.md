---
layout: post
title: 03-09 Bài tập trắc nghiệm - Hàm lồi
chapter: '03'
order: 17
owner: GitHub Copilot
lang: vi
categories:
- chapter03
lesson_type: quiz
redirect_from:
  - /contents/vi/chapter03/03_08_Quiz_Convex_Functions/
---

Chương 03 là nơi tập trung nhiều câu hỏi "gài bẫy" kinh điển nhất trong các kỳ thi tối ưu hóa lồi: phân biệt lồi – lồi chặt – lồi mạnh, phân biệt hàm lồi với hàm giả lồi, nhớ đúng chiều quy tắc hợp thành $$h(g(x))$$, và tính nhanh hàm liên hợp Fenchel $$f^*(y)$$. Chỉ cần quên một điều kiện đơn điệu (như $$h$$ phải *không giảm*) là kết luận tính lồi có thể sai hoàn toàn!

Trước khi bước vào bộ câu hỏi trắc nghiệm, hãy quét nhanh 4 chốt kiểm tra và tự tay phân loại 3 hàm số mẫu ngay bên dưới.

## Kiến thức cần nhớ: Bốn chốt kiểm tra nhanh trước khi làm Quiz Chương 03

- **Chốt 1 — Phân cấp lồi:** Lồi mạnh ($$f'' \ge m > 0$$) $$\implies$$ Lồi chặt ($$f'' > 0$$) $$\implies$$ Lồi ($$f'' \ge 0$$) $$\implies$$ Giả lồi (mọi tập mức dưới lồi). Các chiều ngược lại đều **sai**!
- **Chốt 2 — Quy tắc hợp thành $$h(g(x))$$:** $$h$$ lồi + không giảm + $$g$$ lồi $$\implies$$ lồi; $$h$$ lồi + không tăng + $$g$$ lõm $$\implies$$ lồi.
- **Chốt 3 — Hàm liên hợp $$f^*(y)$$:** Luôn là hàm lồi với *mọi* $$f$$; liên hợp của $$\frac{1}{2}x^T Q x$$ ($$Q \succ 0$$) là $$\frac{1}{2}y^T Q^{-1} y$$; liên hợp của chuẩn $$\|x\|$$ là hàm chỉ thị của hình cầu đơn vị chuẩn đối ngẫu $$\|y\|_* \le 1$$!
- **Chốt 4 — Log-lõm và Log-lồi:** Mọi hàm log-lồi đều lồi, nhưng hàm log-lõm *chưa chắc* lõm (ví dụ mật độ Gauss hay $$x^2$$ trên $$x > 0$$).

### Giải thích: Phân loại nhanh 3 hàm bẫy kinh điển

Hãy kiểm tra tính lồi của 3 hàm sau:

1. **Hàm $$f(x) = -\sqrt{x}$$ trên $$x > 0$$:**
   - $$f'(x) = -\frac{1}{2}x^{-1/2}$$, $$f''(x) = +\frac{1}{4}x^{-3/2} > 0\ \forall x > 0$$.
   - Kết luận: **Hàm lồi chặt** (đừng nhầm dấu trừ mà tưởng là lõm!).
2. **Hàm $$g(x_1, x_2) = x_1 x_2$$ trên $$\mathbb{R}^2$$:**
   - Ma trận Hessian: $$\nabla^2 g = \begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}$$, có hai giá trị riêng $$\lambda_1 = +1$$ và $$\lambda_2 = -1$$.
   - Kết luận: **Không lồi, cũng không lõm** (mặt yên ngựa).
3. **Hàm $$h(x, y) = \frac{x^2}{y}$$ trên miền $$y > 0$$ (hàm quadratic-over-linear):**
   - Ma trận Hessian: $$\nabla^2 h(x, y) = \frac{2}{y^3}\begin{pmatrix}y^2 & -xy\\ -xy & x^2\end{pmatrix} = \frac{2}{y^3}\begin{pmatrix}y\\ -x\end{pmatrix}\begin{pmatrix}y & -x\end{pmatrix} \succeq 0$$.
   - Kết luận: **Hàm lồi** trên toàn nửa mặt phẳng $$y > 0$$ (cũng chính là hàm phối cảnh của $$x^2$$!).

---

Bài tập trắc nghiệm này kiểm tra hiểu biết của bạn về hàm lồi, các tính chất cơ bản, phép toán bảo toàn tính lồi và hàm liên hợp.

---

## 📚 Ôn tập lý thuyết

Trước khi làm bài tập, hãy ôn lại các khái niệm chính trong chương này:

### 📈 **Định nghĩa Hàm Lồi**

**Hàm lồi:**
Hàm $$f: \mathbb{R}^n \to \mathbb{R}$$ là lồi nếu:
1. $$\text{dom}(f)$$ là tập lồi
2. $$f(\theta x + (1-\theta)y) \le \theta f(x) + (1-\theta)f(y)$$
   với mọi $$x, y \in \text{dom}(f), 0 \le \theta \le 1$$

**Các loại hàm lồi:**
- **Lồi chặt:** $$f(\theta x + (1-\theta)y) < \theta f(x) + (1-\theta)f(y)$$ với $$x \neq y, 0 < \theta < 1$$
- **Lồi mạnh:** $$f - \frac{m}{2}\lVert x \rVert_2^2$$ lồi với $$m > 0$$
- **Hàm lõm:** $$f$$ lõm ⟺ $$-f$$ lồi

**Mối quan hệ:** Lồi mạnh ⟹ Lồi chặt ⟹ Lồi

### 🔢 **Các Ví Dụ Quan Trọng**

**Hàm một biến:**
- Hàm mũ: $$e^{ax}$$ lồi với mọi $$a \in \mathbb{R}$$
- Hàm lũy thừa: $$x^a$$ lồi trên $$\mathbb{R}_{++}$$ khi $$a \ge 1$$ hoặc $$a \le 0$$
- Hàm lũy thừa: $$x^a$$ lõm trên $$\mathbb{R}_{++}$$ khi $$0 \le a \le 1$$

**Hàm nhiều biến:**
- Hàm affine: $$a^T x + b$$ vừa lồi vừa lõm
- Hàm bậc hai: $$\frac{1}{2}x^T P x + q^T x + r$$ lồi khi $$P \succeq 0$$
- Chuẩn: $$\lVert x \rVert_p$$ lồi với mọi $$p \ge 1$$
- Hàm mất mát bình phương: $$\lVert Ax - b \rVert_2^2$$ luôn lồi

**Hàm đặc biệt:**
- Hàm chỉ thị: $$I_C(x) = \begin{cases} 0 & x \in C \\ +\infty & x \notin C \end{cases}$$ lồi nếu $$C$$ lồi
- Hàm hỗ trợ: $$I_C^*(x) = \sup_{y \in C} x^T y$$ luôn lồi
- Hàm max: $$\max\{f_1(x), \ldots, f_m(x)\}$$ lồi nếu $$f_i$$ lồi

### 🔍 **Tính Chất Đặc Trưng**

**Đặc trưng epigraph:**
$$f$$ lồi ⟺ $$\text{epi}(f) = \{(x,t) \mid x \in \text{dom}(f), f(x) \le t\}$$ là tập lồi

**Tập mức dưới:**
Nếu $$f$$ lồi thì $$\{x \mid f(x) \le \alpha\}$$ lồi với mọi $$\alpha$$

**Đặc trưng bậc nhất (hàm khả vi):**
$$f$$ lồi ⟺ $$f(y) \ge f(x) + \nabla f(x)^T (y-x)$$ với mọi $$x,y$$
(Hàm nằm trên đường tiếp tuyến)

**Đặc trưng bậc hai (hàm khả vi hai lần):**
$$f$$ lồi ⟺ $$\nabla^2 f(x) \succeq 0$$ với mọi $$x$$ (Hessian nửa xác định dương, với $$\text{dom}(f)$$ lồi)

### 🔄 **Phép Toán Bảo Toàn Tính Lồi**

**Tổ hợp tuyến tính:**
- $$\alpha f$$ lồi nếu $$f$$ lồi và $$\alpha \ge 0$$
- $$f_1 + f_2$$ lồi nếu $$f_1, f_2$$ lồi
- $$\sum_{i=1}^m \alpha_i f_i$$ lồi nếu $$f_i$$ lồi và $$\alpha_i \ge 0$$

**Hợp thành affine:**
$$f(Ax + b)$$ lồi nếu $$f$$ lồi

**Hợp thành tổng quát:** $$h(g(x))$$ lồi nếu:
- $$g$$ lồi, $$h$$ lồi và không giảm
- $$g$$ lõm, $$h$$ lồi và không tăng

**Maximum theo điểm:**
- $$\max\{f_1(x), f_2(x)\}$$ lồi nếu $$f_1, f_2$$ lồi
- $$\sup_{y \in A} f(x,y)$$ lồi theo $$x$$ nếu $$f(x,y)$$ lồi theo $$x$$ với mọi $$y$$

**Phép biến đổi phối cảnh:**
$$g(x,t) = tf(\frac{x}{t})$$ lồi nếu $$f$$ lồi và $$t > 0$$

### ⭐ **Hàm Liên Hợp (Conjugate)**

<div class="textbook-definition" markdown="1">
**Định nghĩa:**
$$f^*(y) = \sup_{x \in \text{dom}(f)} \{y^T x - f(x)\}$$
</div>

**Tính chất quan trọng:**
- $$f^*$$ luôn lồi (dù $$f$$ có lồi hay không)
- Bất đẳng thức Fenchel: $$f(x) + f^*(y) \ge x^T y$$
- Nếu $$f$$ đóng và lồi: $$f^{**} = f$$

**Các ví dụ:**
- $$f(x) = \frac{1}{2}x^T Q x \Rightarrow f^*(y) = \frac{1}{2}y^T Q^{-1} y$$ ($$Q \succ 0$$)
- $$f(x) = \lvert x \rvert \Rightarrow f^*(y) = \begin{cases} 0 & \lvert y \rvert \le 1 \\ +\infty & \lvert y \rvert > 1 \end{cases}$$
- $$f(x) = e^x \Rightarrow f^*(y) = \begin{cases} y \log y - y & y > 0 \\ 0 & y = 0 \\ +\infty & y < 0 \end{cases}$$

### 📊 **Bất Đẳng Thức Jensen**

**Dạng tổng quát:**
Nếu $$f$$ lồi và $$\sum_{i=1}^n w_i = 1, w_i \ge 0$$:
$$f\left(\sum_{i=1}^n w_i x_i\right) \le \sum_{i=1}^n w_i f(x_i)$$

**Dạng xác suất:**
Nếu $$X$$ là biến ngẫu nhiên: $$f(E[X]) \le E[f(X)]$$

---

💡 **Mẹo:** Hàm lồi có tính chất "cong lên" - đoạn thẳng nối hai điểm bất kỳ trên đồ thị luôn nằm phía trên (hoặc trùng với) đồ thị, giúp việc tối ưu hóa trở nên thuận lợi hơn.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>Bài tập trắc nghiệm: Hàm lồi</h2>
        <p>Chọn đáp án đúng nhất cho mỗi câu hỏi. Bài tập tập trung vào các khái niệm cơ bản về hàm lồi và các phép toán liên quan.</p>
        <div id="progress-bar">
            <div id="progress-fill"></div>
        </div>
        <p id="progress-text">Câu hỏi 1/25</p>
    </div>

    <div id="quiz-questions">
        <!-- Câu hỏi 1: Định nghĩa hàm lồi -->
        <div class="question" id="q1">
            <h3>Câu 1: Hàm $$f: \mathbb{R}^n \to \mathbb{R}$$ là lồi nếu:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) Miền xác định là tập lồi và $$f(\theta x + (1-\theta)y) \leq \theta f(x) + (1-\theta)f(y)$$</label>
                <label><input type="radio" name="q1" value="b"> B) Chỉ cần $$f(\theta x + (1-\theta)y) \leq \theta f(x) + (1-\theta)f(y)$$</label>
                <label><input type="radio" name="q1" value="c"> C) Miền xác định là tập lồi và hàm khả vi</label>
                <label><input type="radio" name="q1" value="d"> D) Hàm liên tục trên miền xác định</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Miền xác định là tập lồi và $$f(\theta x + (1-\theta)y) \leq \theta f(x) + (1-\theta)f(y)$$</strong><br>
                Định nghĩa hàm lồi yêu cầu cả hai điều kiện: miền xác định phải là tập lồi và bất đẳng thức Jensen phải thỏa mãn với $$0 \leq \theta \leq 1$$.
            </div>
        </div>

        <!-- Câu hỏi 2: Hàm lồi chặt -->
        <div class="question" id="q2" style="display: none;">
            <h3>Câu 2: Hàm lồi chặt khác với hàm lồi ở điểm nào?</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) Sử dụng bất đẳng thức nghiêm ngặt $$<$$ thay vì $$\leq$$</label>
                <label><input type="radio" name="q2" value="b"> B) Chỉ áp dụng cho $$0 < \theta < 1$$ và $$x \neq y$$</label>
                <label><input type="radio" name="q2" value="c"> C) Cả A và B đều đúng</label>
                <label><input type="radio" name="q2" value="d"> D) Không có sự khác biệt</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) Cả A và B đều đúng</strong><br>
                Hàm lồi chặt yêu cầu $$f(\theta x + (1-\theta)y) < \theta f(x) + (1-\theta)f(y)$$ với $$0 < \theta < 1$$ và $$x \neq y$$.
            </div>
        </div>

        <!-- Câu hỏi 3: Mối quan hệ giữa các loại hàm lồi -->
        <div class="question" id="q3" style="display: none;">
            <h3>Câu 3: Mối quan hệ giữa các loại hàm lồi là:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) Lồi mạnh ⇒ Lồi chặt ⇒ Lồi</label>
                <label><input type="radio" name="q3" value="b"> B) Lồi ⇒ Lồi chặt ⇒ Lồi mạnh</label>
                <label><input type="radio" name="q3" value="c"> C) Lồi chặt ⇒ Lồi mạnh ⇒ Lồi</label>
                <label><input type="radio" name="q3" value="d"> D) Tất cả đều tương đương</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Lồi mạnh ⇒ Lồi chặt ⇒ Lồi</strong><br>
                Đây là thứ tự từ mạnh nhất đến yếu nhất: lồi mạnh là điều kiện mạnh nhất, sau đó đến lồi chặt, và cuối cùng là lồi.
            </div>
        </div>

        <!-- Câu hỏi 4: Hàm affine -->
        <div class="question" id="q4" style="display: none;">
            <h3>Câu 4: Hàm affine $$f(x) = a^T x + b$$ có tính chất:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) Chỉ lồi</label>
                <label><input type="radio" name="q4" value="b"> B) Chỉ lõm</label>
                <label><input type="radio" name="q4" value="c"> C) Vừa lồi vừa lõm</label>
                <label><input type="radio" name="q4" value="d"> D) Không lồi cũng không lõm</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) Vừa lồi vừa lõm</strong><br>
                Hàm affine thỏa mãn $$f(\theta x + (1-\theta)y) = \theta f(x) + (1-\theta)f(y)$$ (đẳng thức), nên vừa lồi vừa lõm.
            </div>
        </div>

        <!-- Câu hỏi 5: Hàm mũ -->
        <div class="question" id="q5" style="display: none;">
            <h3>Câu 5: Hàm $$f(x) = e^{ax}$$ với $$a \in \mathbb{R}$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) Lồi với mọi $$a$$</label>
                <label><input type="radio" name="q5" value="b"> B) Lồi chỉ khi $$a > 0$$</label>
                <label><input type="radio" name="q5" value="c"> C) Lõm với mọi $$a$$</label>
                <label><input type="radio" name="q5" value="d"> D) Phụ thuộc vào dấu của $$a$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Lồi với mọi $$a$$</strong><br>
                Hàm mũ $$e^{ax}$$ là hàm lồi với mọi giá trị thực của $$a$$, bao gồm cả $$a$$ âm, bằng 0 và dương.
            </div>
        </div>

        <!-- Câu hỏi 6: Hàm lũy thừa -->
        <div class="question" id="q6" style="display: none;">
            <h3>Câu 6: Trên $$\mathbb{R}_{++}$$, hàm $$f(x) = x^a$$ là lồi khi:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) $$a \geq 1$$ hoặc $$a \leq 0$$</label>
                <label><input type="radio" name="q6" value="b"> B) $$0 \leq a \leq 1$$</label>
                <label><input type="radio" name="q6" value="c"> C) $$a > 0$$</label>
                <label><input type="radio" name="q6" value="d"> D) Với mọi $$a$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$a \geq 1$$ hoặc $$a \leq 0$$</strong><br>
                Hàm $$x^a$$ lồi trên $$\mathbb{R}_{++}$$ khi $$a \geq 1$$ hoặc $$a \leq 0$$, và lõm khi $$0 \leq a \leq 1$$.
            </div>
        </div>

        <!-- Câu hỏi 7: Hàm bậc hai -->
        <div class="question" id="q7" style="display: none;">
            <h3>Câu 7: Hàm bậc hai $$f(x) = \frac{1}{2}x^T P x + q^T x + r$$ là lồi khi:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) $$P$$ là ma trận xác định dương</label>
                <label><input type="radio" name="q7" value="b"> B) $$P$$ là ma trận nửa xác định dương</label>
                <label><input type="radio" name="q7" value="c"> C) $$P$$ là ma trận đối xứng</label>
                <label><input type="radio" name="q7" value="d"> D) $$P$$ là ma trận khả nghịch</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$P$$ là ma trận nửa xác định dương</strong><br>
                Hàm bậc hai lồi khi ma trận Hessian $$P$$ là nửa xác định dương ($$P \succeq 0$$).
            </div>
        </div>

        <!-- Câu hỏi 8: Chuẩn -->
        <div class="question" id="q8" style="display: none;">
            <h3>Câu 8: Tất cả các chuẩn trên $$\mathbb{R}^n$$ đều:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) Lồi</label>
                <label><input type="radio" name="q8" value="b"> B) Lõm</label>
                <label><input type="radio" name="q8" value="c"> C) Vừa lồi vừa lõm</label>
                <label><input type="radio" name="q8" value="d"> D) Phụ thuộc vào loại chuẩn</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Lồi</strong><br>
                Theo định nghĩa, tất cả các chuẩn đều thỏa mãn bất đẳng thức tam giác, dẫn đến tính lồi.
            </div>
        </div>

        <!-- Câu hỏi 9: Tổng trọng số không âm -->
        <div class="question" id="q9" style="display: none;">
            <h3>Câu 9: Nếu $$f_1, f_2, ..., f_n$$ là các hàm lồi, thì $$\sum_{i=1}^n \alpha_i f_i$$ lồi khi:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) $$\alpha_i \geq 0$$ với mọi $$i$$</label>
                <label><input type="radio" name="q9" value="b"> B) $$\sum_{i=1}^n \alpha_i = 1$$</label>
                <label><input type="radio" name="q9" value="c"> C) $$\alpha_i > 0$$ với mọi $$i$$</label>
                <label><input type="radio" name="q9" value="d"> D) Với mọi $$\alpha_i \in \mathbb{R}$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\alpha_i \geq 0$$ với mọi $$i$$</strong><br>
                Tổng trọng số không âm của các hàm lồi vẫn là hàm lồi. Không cần điều kiện $$\sum \alpha_i = 1$$.
            </div>
        </div>

        <!-- Câu hỏi 10: Hợp thành affine -->
        <div class="question" id="q10" style="display: none;">
            <h3>Câu 10: Nếu $$f$$ là hàm lồi, thì $$g(x) = f(Ax + b)$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) Luôn lồi</label>
                <label><input type="radio" name="q10" value="b"> B) Lồi chỉ khi $$A$$ khả nghịch</label>
                <label><input type="radio" name="q10" value="c"> C) Lồi chỉ khi $$A$$ là ma trận vuông</label>
                <label><input type="radio" name="q10" value="d"> D) Không nhất thiết lồi</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Luôn lồi</strong><br>
                Hợp thành của hàm lồi với hàm affine luôn bảo toàn tính lồi, với mọi ma trận $$A$$ và vector $$b$$.
            </div>
        </div>

        <!-- Câu hỏi 11: Hợp thành tổng quát -->
        <div class="question" id="q11" style="display: none;">
            <h3>Câu 11: Cho $$g$$ lồi và $$h$$ lồi không giảm. Hàm $$f(x) = h(g(x))$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) Lồi</label>
                <label><input type="radio" name="q11" value="b"> B) Lõm</label>
                <label><input type="radio" name="q11" value="c"> C) Không xác định được</label>
                <label><input type="radio" name="q11" value="d"> D) Vừa lồi vừa lõm</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Lồi</strong><br>
                Khi $$g$$ lồi, $$h$$ lồi và không giảm, thì hàm hợp thành $$h(g(x))$$ là lồi.
            </div>
        </div>

        <!-- Câu hỏi 12: Maximum theo điểm -->
        <div class="question" id="q12" style="display: none;">
            <h3>Câu 12: Nếu $$f_1, f_2$$ là các hàm lồi, thì $$f(x) = \max\{f_1(x), f_2(x)\}$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) Lồi</label>
                <label><input type="radio" name="q12" value="b"> B) Lõm</label>
                <label><input type="radio" name="q12" value="c"> C) Không lồi cũng không lõm</label>
                <label><input type="radio" name="q12" value="d"> D) Phụ thuộc vào $$f_1, f_2$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Lồi</strong><br>
                Maximum theo điểm của các hàm lồi luôn là hàm lồi. Đây là một tính chất quan trọng bảo toàn tính lồi.
            </div>
        </div>

        <!-- Câu hỏi 13: Hàm liên hợp -->
        <div class="question" id="q13" style="display: none;">
            <h3>Câu 13: Hàm liên hợp $$f^*(y) = \sup_x \{y^T x - f(x)\}$$ có tính chất:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) Luôn lồi, bất kể $$f$$ có lồi hay không</label>
                <label><input type="radio" name="q13" value="b"> B) Lồi chỉ khi $$f$$ lồi</label>
                <label><input type="radio" name="q13" value="c"> C) Có cùng tính lồi với $$f$$</label>
                <label><input type="radio" name="q13" value="d"> D) Luôn lõm</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Luôn lồi, bất kể $$f$$ có lồi hay không</strong><br>
                Hàm liên hợp luôn lồi vì nó là supremum của các hàm affine $$y^T x - f(x)$$.
            </div>
        </div>

        <!-- Câu hỏi 14: Bất đẳng thức Fenchel -->
        <div class="question" id="q14" style="display: none;">
            <h3>Câu 14: Bất đẳng thức Fenchel phát biểu rằng:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) $$f(x) + f^*(y) \geq x^T y$$</label>
                <label><input type="radio" name="q14" value="b"> B) $$f(x) + f^*(y) \leq x^T y$$</label>
                <label><input type="radio" name="q14" value="c"> C) $$f(x) \cdot f^*(y) \geq x^T y$$</label>
                <label><input type="radio" name="q14" value="d"> D) $$f(x) = f^*(y) + x^T y$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f(x) + f^*(y) \geq x^T y$$</strong><br>
                Bất đẳng thức Fenchel là một bất đẳng thức cơ bản trong lý thuyết hàm liên hợp.
            </div>
        </div>

        <!-- Câu hỏi 15: Liên hợp kép -->
        <div class="question" id="q15" style="display: none;">
            <h3>Câu 15: Với hàm $$f$$ đóng và lồi, liên hợp kép $$f^{**}$$ thỏa mãn:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) $$f^{**} = f$$</label>
                <label><input type="radio" name="q15" value="b"> B) $$f^{**} \leq f$$</label>
                <label><input type="radio" name="q15" value="c"> C) $$f^{**} \geq f$$</label>
                <label><input type="radio" name="q15" value="d"> D) Không có mối quan hệ cố định</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f^{**} = f$$</strong><br>
                Với hàm đóng và lồi, liên hợp kép bằng chính hàm gốc. Đây là định lý Fenchel-Moreau.
            </div>
        </div>

        <!-- Câu hỏi 16: Ví dụ hàm liên hợp -->
        <div class="question" id="q16" style="display: none;">
            <h3>Câu 16: Liên hợp của hàm $$f(x) = |x|$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) Hàm chỉ thị của $$[-1,1]$$</label>
                <label><input type="radio" name="q16" value="b"> B) $$|y|$$</label>
                <label><input type="radio" name="q16" value="c"> C) $$y^2/2$$</label>
                <label><input type="radio" name="q16" value="d"> D) $$\log|y|$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Hàm chỉ thị của $$[-1,1]$$</strong><br>
                Liên hợp của $$|x|$$ là $$f^*(y) = 0$$ nếu $$|y| \leq 1$$ và $$+\infty$$ nếu $$|y| > 1$$.
            </div>
        </div>

        <!-- Câu hỏi 17: Hàm chỉ thị -->
        <div class="question" id="q17" style="display: none;">
            <h3>Câu 17: Hàm chỉ thị $$I_C(x)$$ của tập lồi $$C$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Lồi</label>
                <label><input type="radio" name="q17" value="b"> B) Lõm</label>
                <label><input type="radio" name="q17" value="c"> C) Không lồi cũng không lõm</label>
                <label><input type="radio" name="q17" value="d"> D) Phụ thuộc vào tập $$C$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Lồi</strong><br>
                Hàm chỉ thị của tập lồi luôn là hàm lồi: $$I_C(x) = 0$$ nếu $$x \in C$$, $$+\infty$$ nếu $$x \notin C$$.
            </div>
        </div>

        <!-- Câu hỏi 18: Hàm hỗ trợ -->
        <div class="question" id="q18" style="display: none;">
            <h3>Câu 18: Hàm hỗ trợ $$S_C(x) = \sup_{y \in C} x^T y$$ của tập $$C$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) Lồi bất kể $$C$$ có lồi hay không</label>
                <label><input type="radio" name="q18" value="b"> B) Lồi chỉ khi $$C$$ lồi</label>
                <label><input type="radio" name="q18" value="c"> C) Lõm bất kể $$C$$ có lồi hay không</label>
                <label><input type="radio" name="q18" value="d"> D) Có cùng tính lồi với $$C$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Lồi bất kể $$C$$ có lồi hay không</strong><br>
                Hàm hỗ trợ luôn lồi vì nó là supremum của các hàm tuyến tính $$x^T y$$.
            </div>
        </div>

        <!-- Câu hỏi 19: Hàm mất mát bình phương -->
        <div class="question" id="q19" style="display: none;">
            <h3>Câu 19: Hàm $$f(x) = \|Ax - b\|_2^2$$ với ma trận $$A$$ bất kỳ là:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) Luôn lồi</label>
                <label><input type="radio" name="q19" value="b"> B) Lồi chỉ khi $$A$$ vuông</label>
                <label><input type="radio" name="q19" value="c"> C) Lồi chỉ khi $$A$$ khả nghịch</label>
                <label><input type="radio" name="q19" value="d"> D) Không nhất thiết lồi</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Luôn lồi</strong><br>
                Vì $$A^T A$$ luôn nửa xác định dương với mọi ma trận $$A$$, nên $$\|Ax - b\|_2^2$$ luôn lồi.
            </div>
        </div>

        <!-- Câu hỏi 20: Ứng dụng -->
        <div class="question" id="q20" style="display: none;">
            <h3>Câu 20: Tại sao việc nhận biết hàm lồi quan trọng trong tối ưu hóa?</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Mọi cực tiểu địa phương đều là cực tiểu toàn cục</label>
                <label><input type="radio" name="q20" value="b"> B) Có nhiều thuật toán hiệu quả</label>
                <label><input type="radio" name="q20" value="c"> C) Lý thuyết đối ngẫu áp dụng được</label>
                <label><input type="radio" name="q20" value="d"> D) Tất cả các lý do trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các lý do trên</strong><br>
                Hàm lồi có nhiều tính chất tốt: mọi cực tiểu địa phương đều là cực tiểu toàn cục, có nhiều thuật toán giải hiệu quả và áp dụng được lý thuyết đối ngẫu.
            </div>
        </div>
        <!-- Câu hỏi 21: Thực hành -->
        <div class="question" id="q21" style="display: none;">
            <h3>Câu 21: Cho hàm $$f(x) = e^x$$. Hàm này có lồi không?</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) Có, vì $$f''(x) = e^x > 0$$</label>
                <label><input type="radio" name="q21" value="b"> B) Không, vì tăng quá nhanh</label>
                <label><input type="radio" name="q21" value="c"> C) Chỉ lồi trên $$(0, \infty)$$</label>
                <label><input type="radio" name="q21" value="d"> D) Không xác định được</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Có, vì $$f''(x) = e^x > 0$$</strong><br>
                $$f'(x) = e^x$$, $$f''(x) = e^x > 0$$ với mọi $$x$$, nên hàm lồi trên toàn bộ $$\mathbb{R}$$.
            </div>
        </div>

        <!-- Câu hỏi 22: Thực hành -->
        <div class="question" id="q22" style="display: none;">
            <h3>Câu 22: Hàm $$g(x) = \max\{x, 0\}$$ (ReLU) có phải là hàm lồi không?</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) Có, theo định nghĩa hàm lồi</label>
                <label><input type="radio" name="q22" value="b"> B) Không, vì không khả vi tại $$x = 0$$</label>
                <label><input type="radio" name="q22" value="c"> C) Chỉ lồi trên $$[0, \infty)$$</label>
                <label><input type="radio" name="q22" value="d"> D) Không, vì có góc nhọn</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Có, theo định nghĩa hàm lồi</strong><br>
                Hàm ReLU thỏa mãn định nghĩa hàm lồi. Tính không khả vi tại một điểm không ảnh hưởng đến tính lồi.
            </div>
        </div>

        <!-- Câu hỏi 23: Thực hành -->
        <div class="question" id="q23" style="display: none;">
            <h3>Câu 23: Cho $$f(x,y) = x^2 + y^2$$. Ma trận Hessian của $$f$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) $$\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$$</label>
                <label><input type="radio" name="q23" value="b"> B) $$\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$$</label>
                <label><input type="radio" name="q23" value="c"> C) $$\begin{pmatrix} 2x & 0 \\ 0 & 2y \end{pmatrix}$$</label>
                <label><input type="radio" name="q23" value="d"> D) $$\begin{pmatrix} x & y \\ y & x \end{pmatrix}$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$$</strong><br>
                $$\frac{\partial^2 f}{\partial x^2} = 2$$, $$\frac{\partial^2 f}{\partial y^2} = 2$$, $$\frac{\partial^2 f}{\partial x \partial y} = 0$$
            </div>
        </div>

        <!-- Câu hỏi 24: Thực hành -->
        <div class="question" id="q24" style="display: none;">
            <h3>Câu 24: Tổng của hai hàm lồi $$f$$ và $$g$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) Luôn lồi</label>
                <label><input type="radio" name="q24" value="b"> B) Có thể lồi hoặc không</label>
                <label><input type="radio" name="q24" value="c"> C) Luôn lõm</label>
                <label><input type="radio" name="q24" value="d"> D) Phụ thuộc vào miền xác định</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Luôn lồi</strong><br>
                Tổng của hai hàm lồi luôn là hàm lồi. Đây là một trong những phép toán bảo toàn tính lồi.
            </div>
        </div>

        <!-- Câu hỏi 25: Thực hành -->
        <div class="question" id="q25" style="display: none;">
            <h3>Câu 25: Hàm $$h(x) = |x|^p$$ với $$p \geq 1$$ có tính chất gì?</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) Lồi trên $$\mathbb{R}$$</label>
                <label><input type="radio" name="q25" value="b"> B) Lõm trên $$\mathbb{R}$$</label>
                <label><input type="radio" name="q25" value="c"> C) Lồi chỉ khi $$p = 2$$</label>
                <label><input type="radio" name="q25" value="d"> D) Không lồi không lõm</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Lồi trên $$\mathbb{R}$$</strong><br>
                Với $$p \geq 1$$, hàm $$|x|^p$$ là lồi trên toàn bộ $$\mathbb{R}$$. Đây là một ví dụ quan trọng của hàm lồi.
            </div>
        </div>

    </div>

    <div id="quiz-navigation">
        <button id="prev-btn" onclick="previousQuestion()" disabled>Câu trước</button>
        <button id="next-btn" onclick="nextQuestion()">Câu tiếp</button>
        <button id="submit-btn" onclick="submitQuiz()" style="display: none;">Nộp bài</button>
    </div>

    <div id="quiz-results" style="display: none;">
        <h3>Kết quả bài tập</h3>
        <div id="score-display"></div>
        <div id="detailed-results"></div>
        <button onclick="restartQuiz()">Làm lại</button>
    </div>
</div>

<style>
#quiz-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

#quiz-header {
    text-align: center;
    margin-bottom: 30px;
}

#progress-bar {
    width: 100%;
    height: 10px;
    background-color: #e0e0e0;
    border-radius: 5px;
    margin: 20px 0;
    overflow: hidden;
}

#progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #00BCD4, #009688);
    width: 5%;
    transition: width 0.3s ease;
}

.question {
    background: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 25px;
    margin-bottom: 20px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.question h3 {
    color: #333;
    margin-bottom: 20px;
    font-size: 1.1em;
    line-height: 1.4;
}

.options {
    display: flex;
    flex-direction: column;
    gap: 12px;
}

.options label {
    display: flex;
    align-items: flex-start;
    padding: 12px;
    background: white;
    border: 2px solid #e0e0e0;
    border-radius: 6px;
    cursor: pointer;
    transition: all 0.2s ease;
    font-size: 1em;
    line-height: 1.4;
}

.options label:hover {
    border-color: #00BCD4;
    background-color: #e0f2f1;
}

.options input[type="radio"] {
    margin-right: 12px;
    margin-top: 2px;
    transform: scale(1.2);
    flex-shrink: 0;
}

.options label.selected {
    border-color: #00BCD4;
    background-color: #b2dfdb;
}

.explanation {
    margin-top: 20px;
    padding: 15px;
    background-color: #e0f2f1;
    border-left: 4px solid #00BCD4;
    border-radius: 4px;
    font-size: 0.95em;
    line-height: 1.5;
}

.explanation strong {
    color: #00695C;
}

#quiz-navigation {
    text-align: center;
    margin: 30px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

#quiz-navigation button {
    background: #00BCD4;
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.2s ease;
}

#quiz-navigation button:hover:not(:disabled) {
    background: #00ACC1;
}

#quiz-navigation button:disabled {
    background: #cccccc;
    cursor: not-allowed;
}

#quiz-results {
    text-align: center;
    padding: 30px;
    background: #e0f2f1;
    border-radius: 8px;
    border: 2px solid #00BCD4;
}

#score-display {
    font-size: 1.5em;
    font-weight: bold;
    margin: 20px 0;
    color: #00695C;
}

#detailed-results {
    text-align: left;
    margin: 20px 0;
    max-height: 400px;
    overflow-y: auto;
}

.result-item {
    padding: 10px;
    margin: 5px 0;
    border-radius: 4px;
    border-left: 4px solid;
}

.result-item.correct {
    background-color: #e8f5e8;
    border-left-color: #4CAF50;
}

.result-item.incorrect {
    background-color: #ffebee;
    border-left-color: #f44336;
}

@media (max-width: 600px) {
    #quiz-container {
        padding: 10px;
    }
    
    .question {
        padding: 15px;
    }
    
    #quiz-navigation {
        flex-direction: column;
        gap: 10px;
    }
    
    #quiz-navigation button {
        width: 100%;
    }
}
</style>

<script>
let currentQuestion = 1;
const totalQuestions = 25;
let userAnswers = {};
let quizSubmitted = false;

// Đáp án đúng cho từng câu hỏi
const correctAnswers = {
    q1: 'a', q2: 'c', q3: 'a', q4: 'c', q5: 'a',
    q6: 'a', q7: 'b', q8: 'a', q9: 'a', q10: 'a',
    q11: 'a', q12: 'a', q13: 'a', q14: 'a', q15: 'a',
    q16: 'a', q17: 'a', q18: 'a', q19: 'a', q20: 'd'
,
    q21: 'a', q22: 'a', q23: 'a', q24: 'a', q25: 'a'};

/**
 * Cập nhật thanh tiến trình và hiển thị câu hỏi hiện tại
 */
function updateProgress() {
    const progressFill = document.getElementById('progress-fill');
    const progressText = document.getElementById('progress-text');
    
    const percentage = (currentQuestion / totalQuestions) * 100;
    progressFill.style.width = percentage + '%';
    progressText.textContent = `Câu hỏi ${currentQuestion}/${totalQuestions}`;
}

/**
 * Hiển thị câu hỏi theo số thứ tự
 */
function showQuestion(questionNum) {
    // Ẩn tất cả câu hỏi
    for (let i = 1; i <= totalQuestions; i++) {
        document.getElementById(`q${i}`).style.display = 'none';
    }
    
    // Hiển thị câu hỏi hiện tại
    document.getElementById(`q${questionNum}`).style.display = 'block';
    
    // Cập nhật trạng thái nút điều hướng
    document.getElementById('prev-btn').disabled = (questionNum === 1);
    document.getElementById('next-btn').style.display = (questionNum === totalQuestions) ? 'none' : 'inline-block';
    document.getElementById('submit-btn').style.display = (questionNum === totalQuestions) ? 'inline-block' : 'none';
    
    updateProgress();
}

/**
 * Chuyển đến câu hỏi tiếp theo
 */
function nextQuestion() {
    if (currentQuestion < totalQuestions) {
        currentQuestion++;
        showQuestion(currentQuestion);
    }
}

/**
 * Quay lại câu hỏi trước
 */
function previousQuestion() {
    if (currentQuestion > 1) {
        currentQuestion--;
        showQuestion(currentQuestion);
    }
}

/**
 * Lưu đáp án của người dùng
 */
function saveAnswer(questionId, answer) {
    userAnswers[questionId] = answer;
    
    // Cập nhật giao diện để hiển thị đáp án đã chọn
    const labels = document.querySelectorAll(`#${questionId} .options label`);
    labels.forEach(label => {
        label.classList.remove('selected');
        if (label.querySelector('input').value === answer) {
            label.classList.add('selected');
        }
    });
}

/**
 * Nộp bài và hiển thị kết quả
 */
function submitQuiz() {
    if (quizSubmitted) return;
    
    quizSubmitted = true;
    let correctCount = 0;
    let detailedResults = '';
    
    // Tính điểm và tạo báo cáo chi tiết
    for (let i = 1; i <= totalQuestions; i++) {
        const questionId = `q${i}`;
        const userAnswer = userAnswers[questionId];
        const correctAnswer = correctAnswers[questionId];
        const isCorrect = userAnswer === correctAnswer;
        
        if (isCorrect) correctCount++;
        
        // Hiển thị giải thích cho tất cả câu hỏi
        const explanation = document.querySelector(`#${questionId} .explanation`);
        if (explanation) {
            explanation.style.display = 'block';
        }
        
        // Tạo báo cáo chi tiết
        detailedResults += `
            <div class="result-item ${isCorrect ? 'correct' : 'incorrect'}">
                <strong>Câu ${i}:</strong> ${isCorrect ? 'Đúng' : 'Sai'}
                ${!isCorrect ? `<br><small>Đáp án của bạn: ${userAnswer || 'Chưa trả lời'} | Đáp án đúng: ${correctAnswer}</small>` : ''}
            </div>
        `;
    }
    
    // Hiển thị kết quả
    const scorePercentage = Math.round((correctCount / totalQuestions) * 100);
    document.getElementById('score-display').innerHTML = `
        <div>Điểm số: ${correctCount}/${totalQuestions} (${scorePercentage}%)</div>
        <div style="margin-top: 10px; font-size: 0.9em;">
            ${scorePercentage >= 80 ? '🎉 Xuất sắc! Bạn đã nắm vững lý thuyết hàm lồi!' : 
              scorePercentage >= 60 ? '👍 Khá tốt! Hãy ôn lại một số khái niệm về hàm lồi.' : 
              scorePercentage >= 40 ? '📚 Cần ôn tập thêm về định nghĩa và tính chất hàm lồi.' : '💪 Hãy đọc lại lý thuyết về hàm lồi và các phép toán!'}
        </div>
    `;
    
    document.getElementById('detailed-results').innerHTML = detailedResults;
    document.getElementById('quiz-results').style.display = 'block';
    document.getElementById('quiz-navigation').style.display = 'none';
    
    // Cuộn đến kết quả
    document.getElementById('quiz-results').scrollIntoView({ behavior: 'smooth' });
}

/**
 * Khởi động lại bài tập
 */
function restartQuiz() {
    currentQuestion = 1;
    userAnswers = {};
    quizSubmitted = false;
    
    // Ẩn kết quả và hiển thị lại điều hướng
    document.getElementById('quiz-results').style.display = 'none';
    document.getElementById('quiz-navigation').style.display = 'flex';
    
    // Ẩn tất cả giải thích
    document.querySelectorAll('.explanation').forEach(exp => {
        exp.style.display = 'none';
    });
    
    // Xóa tất cả lựa chọn
    document.querySelectorAll('input[type="radio"]').forEach(input => {
        input.checked = false;
    });
    
    document.querySelectorAll('.options label').forEach(label => {
        label.classList.remove('selected');
    });
    
    // Hiển thị câu hỏi đầu tiên
    showQuestion(1);
    
    // Cuộn lên đầu
    document.getElementById('quiz-header').scrollIntoView({ behavior: 'smooth' });
}

// Khởi tạo bài tập khi trang được tải
document.addEventListener('DOMContentLoaded', function() {
    showQuestion(1);
    
    // Thêm event listener cho tất cả radio button
    document.querySelectorAll('input[type="radio"]').forEach(input => {
        input.addEventListener('change', function() {
            const questionId = this.name;
            const answer = this.value;
            saveAnswer(questionId, answer);
        });
    });
    
    // Render MathJax sau khi DOM được tải
    if (window.MathJax && MathJax.startup && MathJax.startup.promise) {
        MathJax.startup.promise.then(() => MathJax.typesetPromise());
    }
});

// Xử lý phím tắt
document.addEventListener('keydown', function(event) {
    if (quizSubmitted) return;
    
    switch(event.key) {
        case 'ArrowLeft':
            if (currentQuestion > 1) previousQuestion();
            break;
        case 'ArrowRight':
            if (currentQuestion < totalQuestions) nextQuestion();
            break;
        case 'Enter':
            if (currentQuestion === totalQuestions) submitQuiz();
            break;
    }
});
</script>
