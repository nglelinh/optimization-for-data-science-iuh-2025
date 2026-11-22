---
layout: post
title: 04-10 Bài tập trắc nghiệm - Cơ bản tối ưu hóa lồi
chapter: '04'
order: 11
owner: GitHub Copilot
lang: vi
categories:
- chapter04
lesson_type: quiz
redirect_from:
  - /contents/vi/chapter04/04_09_Quiz_Convex_Optimization_Basics/
---

Bài tập trắc nghiệm này kiểm tra hiểu biết của bạn về các khái niệm cơ bản trong tối ưu hóa lồi, bao gồm thuật ngữ, điều kiện tối ưu và các kỹ thuật biến đổi.

---

## 📚 Ôn tập lý thuyết

Trước khi làm bài tập, hãy ôn lại các khái niệm chính trong chương này:

### 🎯 **Bài Toán Tối Ưu Hóa Lồi**

**Dạng chuẩn:**
$$\begin{aligned}
&\min_{x \in D} &&f(x) \\
&\text{subject to} &&g_i(x) \le 0, \quad i = 1, \ldots, m \\
&&&h_j(x) = 0, \quad j = 1, \ldots, r
\end{aligned}$$

**Điều kiện lồi:**
- $$f, g_i$$ là hàm lồi
- $$h_j$$ là hàm affine: $$h_j(x) = a_j^T x + b_j$$
- $$D = \text{dom}(f) \cap \bigcap_{i=1}^m \text{dom}(g_i) \cap \bigcap_{j=1}^r \text{dom}(h_j)$$

### 📝 **Thuật Ngữ Cơ Bản**

**Các khái niệm quan trọng:**
- **Hàm mục tiêu:** $$f(x)$$ - hàm cần tối thiểu hóa
- **Ràng buộc bất đẳng thức:** $$g_i(x) \le 0$$
- **Ràng buộc đẳng thức:** $$h_j(x) = 0$$
- **Điểm khả thi:** $$x$$ thỏa mãn tất cả ràng buộc
- **Giá trị tối ưu:** $$f^* = \min\{f(x) \mid x \text{ khả thi}\}$$
- **Nghiệm tối ưu:** $$x^*$$ khả thi và $$f(x^*) = f^*$$
- **$$\epsilon$$-cận tối ưu (dưới tối ưu):** $$x$$ khả thi và $$f(x) \le f^* + \epsilon$$
- **Ràng buộc tích cực (hoạt động):** $$g_i(x^*) = 0$$ tại nghiệm tối ưu

**Tập khả thi:**
$$S = \{x \in D \mid g_i(x) \le 0, h_j(x) = 0\}$$

### 🔵 **Tính Chất Tập Nghiệm**

**Tính chất 1:** Tập nghiệm $$X_{\text{opt}}$$ của bài toán lồi là tập lồi

<div class="textbook-proof" markdown="1">
**Chứng minh:** Nếu $$x, y \in X_{\text{opt}}$$ và $$0 \le \theta \le 1$$:
- $$\theta x + (1-\theta)y$$ khả thi (do tính lồi của tập khả thi)
- $$f(\theta x + (1-\theta)y) \le \theta f(x) + (1-\theta)f(y) = f^*$$
</div>

**Tính chất 2:** Nếu $$f$$ lồi chặt thì nghiệm (nếu tồn tại) là duy nhất

### ✅ **Điều Kiện Tối Ưu**

**Điều kiện bậc nhất (hàm khả vi):**
Với bài toán $$\min_x f(x)$$ s.t. $$x \in C$$:
$$\nabla f(x^*)^T (y - x^*) \ge 0 \quad \forall y \in C$$

**Trường hợp không ràng buộc:** $$C = \mathbb{R}^n$$
$$\nabla f(x^*) = 0$$

**Điều kiện bậc hai (hàm khả vi hai lần):**
- **Điều kiện cần:** $$\nabla f(x^*) = 0$$ và $$\nabla^2 f(x^*) \succeq 0$$
- **Điều kiện đủ:** $$\nabla f(x^*) = 0$$ và $$\nabla^2 f(x^*) \succ 0$$

**Ý nghĩa Hessian:**
- $$\nabla^2 f(x^*) \succ 0$$: cực tiểu địa phương chặt
- $$\nabla^2 f(x^*) \prec 0$$: cực đại địa phương chặt
- $$\nabla^2 f(x^*)$$ bất định: điểm yên ngựa

### 🔄 **Biến Phụ (Slack Variables)**

**Mục đích:** Chuyển ràng buộc bất đẳng thức thành đẳng thức

**Biến đổi:**
$$g_i(x) \le 0 \quad \Rightarrow \quad g_i(x) + s_i = 0, \quad s_i \ge 0$$

**Bài toán gốc:**
$$\begin{aligned}
&\min_x &&f(x) \\
&\text{s.t.} &&g_i(x) \le 0
\end{aligned}$$

**Với biến phụ:**
$$\begin{aligned}
&\min_{x,s} &&f(x) \\
&\text{s.t.} &&g_i(x) + s_i = 0 \\
&&&s_i \ge 0
\end{aligned}$$

**Ý nghĩa:**
- $$s_i > 0$$: ràng buộc $$i$$ không tích cực (không hoạt động)
- $$s_i = 0$$: ràng buộc $$i$$ tích cực (chặt)

**Lưu ý:** Chỉ bảo toàn tính lồi khi $$g_i(x)$$ là hàm affine

### 🔧 **Nới Lỏng (Relaxation / Làm Giản)**

<div class="textbook-definition" markdown="1">
**Định nghĩa:** Thay thế tập khả thi $$C$$ bằng siêu tập $$\tilde{C} \supseteq C$$
</div>

**Bài toán gốc:** $$\min_x f(x)$$ s.t. $$x \in C$$
**Bài toán nới lỏng:** $$\min_x f(x)$$ s.t. $$x \in \tilde{C}$$

**Tính chất:** Giá trị tối ưu của bài toán nới lỏng $$\le$$ giá trị tối ưu gốc

**Ví dụ quan trọng:** Nới lỏng ràng buộc đẳng thức
$$h_j(x) = 0 \quad \Rightarrow \quad h_j(x) \le 0$$

**Ứng dụng:** Chuyển bài toán phi lồi thành lồi (khi $$h_j$$ lồi nhưng phi-affine)

### 🎲 **Các Kỹ Thuật Biến Đổi Khác**

**Loại bỏ ràng buộc đẳng thức:**
Nếu $$Ax = b$$ có nghiệm, có thể tham số hóa:
$$x = x_0 + Fz$$ với $$Ax_0 = b$$ và $$\text{range}(F) = \text{null}(A)$$

**Đổi biến:**
- Thay đổi biến để đơn giản hóa bài toán
- Bảo toàn tính lồi qua phép biến đổi affine

**Tách biến:**
- Tách bài toán lớn thành các bài toán con nhỏ hơn
- Sử dụng cấu trúc đặc biệt của bài toán

### 📊 **So Sánh Các Phương Pháp**

| Kỹ thuật | Mục đích | Ưu điểm | Nhược điểm |
|----------|----------|---------|------------|
| **Biến phụ** | Chuyển bất đẳng thức → đẳng thức | Đơn giản hóa thuật toán | Tăng số biến |
| **Nới lỏng (làm giản)** | Mở rộng tập khả thi | Chuyển phi lồi → lồi | Nghiệm có thể không khả thi với bài toán gốc |
| **Loại bỏ ràng buộc** | Giảm số ràng buộc | Giảm chiều bài toán | Yêu cầu phân tích đặc biệt |

### 🔍 **Nhận Biết Bài Toán Lồi**

**Checklist:**
- [ ] Hàm mục tiêu $$f$$ lồi?
- [ ] Ràng buộc bất đẳng thức $$g_i$$ lồi?
- [ ] Ràng buộc đẳng thức $$h_j$$ affine?
- [ ] Miền xác định $$D$$ lồi?

**Nếu tất cả ✓ → Bài toán tối ưu hóa lồi**

---

💡 **Lưu ý:** Trong tối ưu hóa lồi, mọi cực tiểu địa phương đều là cực tiểu toàn cục, giúp các thuật toán giải bài toán đạt độ tin cậy cao.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>Bài tập trắc nghiệm: Cơ bản tối ưu hóa lồi</h2>
        <p>Chọn đáp án đúng nhất cho mỗi câu hỏi. Bài tập tập trung vào các khái niệm cơ bản và thực tế trong tối ưu hóa lồi.</p>
        <div id="progress-bar">
            <div id="progress-fill"></div>
        </div>
        <p id="progress-text">Câu hỏi 1/25</p>
    </div>

    <div id="quiz-questions">
        <!-- Câu hỏi 1: Định nghĩa bài toán tối ưu hóa lồi -->
        <div class="question" id="q1">
            <h3>Câu 1: Trong bài toán tối ưu hóa lồi, hàm ràng buộc đẳng thức $$h_j(x) = 0$$ phải là:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) Hàm lồi</label>
                <label><input type="radio" name="q1" value="b"> B) Hàm lõm</label>
                <label><input type="radio" name="q1" value="c"> C) Hàm affine</label>
                <label><input type="radio" name="q1" value="d"> D) Hàm bất kỳ</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) Hàm affine</strong><br>
                Trong bài toán tối ưu hóa lồi, các hàm ràng buộc đẳng thức $$h_j(x) = 0$$ phải là hàm affine để đảm bảo tập khả thi là tập lồi.
            </div>
        </div>

        <!-- Câu hỏi 2: Điểm khả thi -->
        <div class="question" id="q2" style="display: none;">
            <h3>Câu 2: Điểm $$x$$ được gọi là khả thi nếu:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) $$x \in D$$ và $$g_i(x) \leq 0$$ với mọi $$i$$</label>
                <label><input type="radio" name="q2" value="b"> B) $$x \in D$$, $$g_i(x) \leq 0$$ với mọi $$i$$, và $$h_j(x) = 0$$ với mọi $$j$$</label>
                <label><input type="radio" name="q2" value="c"> C) Chỉ cần $$f(x)$$ xác định</label>
                <label><input type="radio" name="q2" value="d"> D) $$x$$ là nghiệm tối ưu</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$x \in D$$, $$g_i(x) \leq 0$$ với mọi $$i$$, và $$h_j(x) = 0$$ với mọi $$j$$</strong><br>
                Điểm khả thi phải thỏa mãn tất cả các điều kiện: nằm trong miền xác định và thỏa mãn tất cả ràng buộc.
            </div>
        </div>

        <!-- Câu hỏi 3: Ràng buộc hoạt động -->
        <div class="question" id="q3" style="display: none;">
            <h3>Câu 3: Ràng buộc $$g_i(x) \leq 0$$ được gọi là "hoạt động" tại $$x$$ khi:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) $$g_i(x) < 0$$</label>
                <label><input type="radio" name="q3" value="b"> B) $$g_i(x) = 0$$</label>
                <label><input type="radio" name="q3" value="c"> C) $$g_i(x) > 0$$</label>
                <label><input type="radio" name="q3" value="d"> D) $$g_i(x) \leq -1$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$g_i(x) = 0$$</strong><br>
                Ràng buộc hoạt động có nghĩa là nó được thỏa mãn với đẳng thức, tức là $$g_i(x) = 0$$.
            </div>
        </div>

        <!-- Câu hỏi 4: Điểm ε-dưới tối ưu -->
        <div class="question" id="q4" style="display: none;">
            <h3>Câu 4: Điểm $$x$$ được gọi là $$\epsilon$$-dưới tối ưu nếu:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) $$f(x) = f^* + \epsilon$$</label>
                <label><input type="radio" name="q4" value="b"> B) $$f(x) \leq f^* + \epsilon$$</label>
                <label><input type="radio" name="q4" value="c"> C) $$f(x) \geq f^* - \epsilon$$</label>
                <label><input type="radio" name="q4" value="d"> D) $$|f(x) - f^*| \leq \epsilon$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$f(x) \leq f^* + \epsilon$$</strong><br>
                Điểm $$\epsilon$$-dưới tối ưu có giá trị hàm mục tiêu không vượt quá giá trị tối ưu cộng với $$\epsilon$$.
            </div>
        </div>

        <!-- Câu hỏi 5: Tính chất tập nghiệm -->
        <div class="question" id="q5" style="display: none;">
            <h3>Câu 5: Tập nghiệm $$X_{opt}$$ của bài toán tối ưu hóa lồi có tính chất:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) Luôn là tập lồi</label>
                <label><input type="radio" name="q5" value="b"> B) Có thể không lồi</label>
                <label><input type="radio" name="q5" value="c"> C) Luôn chứa duy nhất một điểm</label>
                <label><input type="radio" name="q5" value="d"> D) Luôn là tập rỗng</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Luôn là tập lồi</strong><br>
                Tập nghiệm của bài toán tối ưu hóa lồi luôn là tập lồi, đây là một tính chất quan trọng.
            </div>
        </div>

        <!-- Câu hỏi 6: Nghiệm duy nhất -->
        <div class="question" id="q6" style="display: none;">
            <h3>Câu 6: Bài toán tối ưu hóa lồi có nghiệm duy nhất khi:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) Hàm mục tiêu $$f$$ là lồi</label>
                <label><input type="radio" name="q6" value="b"> B) Hàm mục tiêu $$f$$ là lồi chặt</label>
                <label><input type="radio" name="q6" value="c"> C) Tập khả thi bị chặn</label>
                <label><input type="radio" name="q6" value="d"> D) Có ràng buộc đẳng thức</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Hàm mục tiêu $$f$$ là lồi chặt</strong><br>
                Khi hàm mục tiêu là lồi chặt, nghiệm tối ưu (nếu tồn tại) là duy nhất vì không có đoạn phẳng nào trên đồ thị.
            </div>
        </div>

        <!-- Câu hỏi 7: Điều kiện tối ưu bậc nhất -->
        <div class="question" id="q7" style="display: none;">
            <h3>Câu 7: Với bài toán $$\min_x f(x)$$ s.t. $$x \in C$$, điều kiện tối ưu bậc nhất là:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) $$\nabla f(x) = 0$$</label>
                <label><input type="radio" name="q7" value="b"> B) $$\nabla f(x)^T(y-x) \geq 0$$ với mọi $$y \in C$$</label>
                <label><input type="radio" name="q7" value="c"> C) $$\nabla f(x)^T(y-x) \leq 0$$ với mọi $$y \in C$$</label>
                <label><input type="radio" name="q7" value="d"> D) $$f(x) \leq f(y)$$ với mọi $$y \in C$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$\nabla f(x)^T(y-x) \geq 0$$ với mọi $$y \in C$$</strong><br>
                Điều kiện bậc nhất cho tính tối ưu yêu cầu không có hướng khả thi nào là hướng giảm: $$-\nabla f(x)$$ không được chỉ vào trong tập khả thi.
            </div>
        </div>

        <!-- Câu hỏi 8: Trường hợp không ràng buộc -->
        <div class="question" id="q8" style="display: none;">
            <h3>Câu 8: Với bài toán không ràng buộc $$\min_x f(x)$$ ($$C = \mathbb{R}^n$$), điều kiện tối ưu là:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) $$\nabla f(x) = 0$$</label>
                <label><input type="radio" name="q8" value="b"> B) $$\nabla^2 f(x) \succ 0$$</label>
                <label><input type="radio" name="q8" value="c"> C) $$f(x) = 0$$</label>
                <label><input type="radio" name="q8" value="d"> D) $$x = 0$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\nabla f(x) = 0$$</strong><br>
                Với bài toán không ràng buộc, điều kiện tối ưu bậc nhất trở thành $$\nabla f(x) = 0$$.
            </div>
        </div>

        <!-- Câu hỏi 9: Ma trận Hessian -->
        <div class="question" id="q9" style="display: none;">
            <h3>Câu 9: Ma trận Hessian $$\nabla^2 f(x)$$ cung cấp thông tin về:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) Độ dốc của hàm</label>
                <label><input type="radio" name="q9" value="b"> B) Độ cong của hàm</label>
                <label><input type="radio" name="q9" value="c"> C) Giá trị của hàm</label>
                <label><input type="radio" name="q9" value="d"> D) Miền xác định của hàm</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Độ cong của hàm</strong><br>
                Ma trận Hessian chứa các đạo hàm bậc hai, cung cấp thông tin về độ cong của hàm tại một điểm.
            </div>
        </div>

        <!-- Câu hỏi 10: Điều kiện bậc hai đủ -->
        <div class="question" id="q10" style="display: none;">
            <h3>Câu 10: Điều kiện đủ cho cực tiểu địa phương chặt là:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) $$\nabla f(x) = 0$$ và $$\nabla^2 f(x) \succeq 0$$</label>
                <label><input type="radio" name="q10" value="b"> B) $$\nabla f(x) = 0$$ và $$\nabla^2 f(x) \succ 0$$</label>
                <label><input type="radio" name="q10" value="c"> C) Chỉ cần $$\nabla f(x) = 0$$</label>
                <label><input type="radio" name="q10" value="d"> D) $$\nabla^2 f(x) \prec 0$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$\nabla f(x) = 0$$ và $$\nabla^2 f(x) \succ 0$$</strong><br>
                Điều kiện đủ cho cực tiểu địa phương chặt yêu cầu gradient bằng 0 và Hessian xác định dương.
            </div>
        </div>

        <!-- Câu hỏi 11: Biến phụ -->
        <div class="question" id="q11" style="display: none;">
            <h3>Câu 11: Biến phụ $$s_i$$ được giới thiệu để:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) Chuyển ràng buộc bất đẳng thức thành đẳng thức</label>
                <label><input type="radio" name="q11" value="b"> B) Chuyển ràng buộc đẳng thức thành bất đẳng thức</label>
                <label><input type="radio" name="q11" value="c"> C) Tăng số biến trong bài toán</label>
                <label><input type="radio" name="q11" value="d"> D) Giảm độ phức tạp tính toán</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Chuyển ràng buộc bất đẳng thức thành đẳng thức</strong><br>
                Biến phụ được sử dụng để biến đổi $$g_i(x) \leq 0$$ thành $$g_i(x) + s_i = 0$$ với $$s_i \geq 0$$.
            </div>
        </div>

        <!-- Câu hỏi 12: Ý nghĩa biến phụ -->
        <div class="question" id="q12" style="display: none;">
            <h3>Câu 12: Khi $$s_i > 0$$ tại nghiệm tối ưu, điều này có nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) Ràng buộc $$g_i(x) \leq 0$$ hoạt động</label>
                <label><input type="radio" name="q12" value="b"> B) Ràng buộc $$g_i(x) \leq 0$$ không hoạt động</label>
                <label><input type="radio" name="q12" value="c"> C) Bài toán không khả thi</label>
                <label><input type="radio" name="q12" value="d"> D) Nghiệm không tối ưu</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Ràng buộc $$g_i(x) \leq 0$$ không hoạt động</strong><br>
                Khi $$s_i > 0$$, ta có $$g_i(x) = -s_i < 0$$, nghĩa là ràng buộc không hoạt động (có "khoảng trống").
            </div>
        </div>

        <!-- Câu hỏi 13: Bảo toàn tính lồi với biến phụ -->
        <div class="question" id="q13" style="display: none;">
            <h3>Câu 13: Biến đổi biến phụ bảo toàn tính lồi khi:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) $$g_i(x)$$ là hàm lồi bất kỳ</label>
                <label><input type="radio" name="q13" value="b"> B) $$g_i(x)$$ là hàm affine</label>
                <label><input type="radio" name="q13" value="c"> C) $$g_i(x)$$ là hàm lõm</label>
                <label><input type="radio" name="q13" value="d"> D) Luôn bảo toàn tính lồi</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$g_i(x)$$ là hàm affine</strong><br>
                Biến đổi biến phụ chỉ bảo toàn tính lồi khi $$g_i(x)$$ là hàm affine. Với hàm phi tuyến, có thể phá hủy tính lồi.
            </div>
        </div>

        <!-- Câu hỏi 14: Làm giản (Relaxation) -->
        <div class="question" id="q14" style="display: none;">
            <h3>Câu 14: Kỹ thuật làm giản thay đổi tập miền $$C$$ thành $$\tilde{C}$$ sao cho:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) $$\tilde{C} \subseteq C$$</label>
                <label><input type="radio" name="q14" value="b"> B) $$\tilde{C} \supseteq C$$</label>
                <label><input type="radio" name="q14" value="c"> C) $$\tilde{C} = C$$</label>
                <label><input type="radio" name="q14" value="d"> D) $$\tilde{C} \cap C = \emptyset$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$\tilde{C} \supseteq C$$</strong><br>
                Làm giản mở rộng tập miền khả thi, tức là $$\tilde{C}$$ chứa $$C$$ như một tập con.
            </div>
        </div>

        <!-- Câu hỏi 15: Giá trị tối ưu sau làm giản -->
        <div class="question" id="q15" style="display: none;">
            <h3>Câu 15: Sau khi làm giản, giá trị tối ưu $$\tilde{f}^*$$ so với giá trị gốc $$f^*$$:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) $$\tilde{f}^* \geq f^*$$</label>
                <label><input type="radio" name="q15" value="b"> B) $$\tilde{f}^* \leq f^*$$</label>
                <label><input type="radio" name="q15" value="c"> C) $$\tilde{f}^* = f^*$$</label>
                <label><input type="radio" name="q15" value="d"> D) Không có mối quan hệ cố định</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$\tilde{f}^* \leq f^*$$</strong><br>
                Vì tối ưu hóa trên tập miền lớn hơn, giá trị tối ưu sau làm giản không thể lớn hơn giá trị gốc.
            </div>
        </div>

        <!-- Câu hỏi 16: Làm giản ràng buộc đẳng thức -->
        <div class="question" id="q16" style="display: none;">
            <h3>Câu 16: Làm giản ràng buộc đẳng thức $$h_j(x) = 0$$ thành:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) $$h_j(x) \geq 0$$</label>
                <label><input type="radio" name="q16" value="b"> B) $$h_j(x) \leq 0$$</label>
                <label><input type="radio" name="q16" value="c"> C) $$|h_j(x)| \leq \epsilon$$</label>
                <label><input type="radio" name="q16" value="d"> D) Loại bỏ ràng buộc</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$h_j(x) \leq 0$$</strong><br>
                Khi $$h_j(x)$$ là hàm lồi phi-affine, có thể làm giản $$h_j(x) = 0$$ thành $$h_j(x) \leq 0$$.
            </div>
        </div>

        <!-- Câu hỏi 17: Tập khả thi -->
        <div class="question" id="q17" style="display: none;">
            <h3>Câu 17: Tập khả thi của bài toán tối ưu hóa lồi có tính chất:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Luôn là tập lồi</label>
                <label><input type="radio" name="q17" value="b"> B) Có thể không lồi</label>
                <label><input type="radio" name="q17" value="c"> C) Luôn bị chặn</label>
                <label><input type="radio" name="q17" value="d"> D) Luôn không rỗng</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Luôn là tập lồi</strong><br>
                Trong bài toán tối ưu hóa lồi, tập khả thi luôn là tập lồi do các ràng buộc lồi và affine.
            </div>
        </div>

        <!-- Câu hỏi 18: Polytope -->
        <div class="question" id="q18" style="display: none;">
            <h3>Câu 18: Trong quy hoạch tuyến tính, tập khả thi bị chặn được gọi là:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) Polyhedron</label>
                <label><input type="radio" name="q18" value="b"> B) Polytope</label>
                <label><input type="radio" name="q18" value="c"> C) Simplex</label>
                <label><input type="radio" name="q18" value="d"> D) Ellipsoid</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Polytope</strong><br>
                Polytope là tập khả thi bị chặn trong quy hoạch tuyến tính, trong khi polyhedron có thể không bị chặn.
            </div>
        </div>

        <!-- Câu hỏi 19: Nghiệm tại đỉnh -->
        <div class="question" id="q19" style="display: none;">
            <h3>Câu 19: Trong quy hoạch tuyến tính, nếu nghiệm tối ưu tồn tại, nó có thể được tìm thấy tại:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) Điểm bất kỳ trong tập khả thi</label>
                <label><input type="radio" name="q19" value="b"> B) Tâm của tập khả thi</label>
                <label><input type="radio" name="q19" value="c"> C) Một trong các đỉnh của tập khả thi</label>
                <label><input type="radio" name="q19" value="d"> D) Biên của tập khả thi</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) Một trong các đỉnh của tập khả thi</strong><br>
                Đây là cơ sở cho thuật toán Simplex: nghiệm tối ưu của LP luôn có thể tìm thấy tại một đỉnh.
            </div>
        </div>

        <!-- Câu hỏi 20: Ưu điểm tối ưu hóa lồi -->
        <div class="question" id="q20" style="display: none;">
            <h3>Câu 20: Ưu điểm chính của bài toán tối ưu hóa lồi là:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Luôn có nghiệm duy nhất</label>
                <label><input type="radio" name="q20" value="b"> B) Mọi cực tiểu địa phương đều là cực tiểu toàn cục</label>
                <label><input type="radio" name="q20" value="c"> C) Tính toán nhanh hơn</label>
                <label><input type="radio" name="q20" value="d"> D) Không cần điều kiện tối ưu</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Mọi cực tiểu địa phương đều là cực tiểu toàn cục</strong><br>
                Đây là tính chất quan trọng nhất của tối ưu hóa lồi, đảm bảo không có vấn đề "mắc kẹt" tại cực tiểu địa phương.
            </div>
        </div>
        <!-- Câu hỏi 21: Thực hành -->
        <div class="question" id="q21" style="display: none;">
            <h3>Câu 21: Trong bài toán tối ưu lồi, điều kiện KKT là:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) Đủ cho tối ưu, và cũng cần thiết khi điều kiện Slater thỏa mãn</label>
                <label><input type="radio" name="q21" value="b"> B) Chỉ cần thiết</label>
                <label><input type="radio" name="q21" value="c"> C) Chỉ đủ</label>
                <label><input type="radio" name="q21" value="d"> D) Không liên quan</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Đủ cho tối ưu, và cũng cần thiết khi điều kiện Slater thỏa mãn</strong><br>
                Đối với bài toán tối ưu lồi, điều kiện KKT luôn đủ cho tối ưu toàn cục; chúng cũng cần thiết khi có điều kiện chính quy như Slater (khi đó đối ngẫu mạnh đúng). Không có Slater, nghiệm tối ưu có thể không thỏa KKT (ví dụ $$\min x$$ với $$x^2 \leq 0$$).
            </div>
        </div>

        <!-- Câu hỏi 22: Thực hành -->
        <div class="question" id="q22" style="display: none;">
            <h3>Câu 22: Bài toán $$\min x^2 + y^2$$ với $$x + y \geq 1$$ có nghiệm là:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) $$x = 0.5, y = 0.5$$</label>
                <label><input type="radio" name="q22" value="b"> B) $$x = 1, y = 0$$</label>
                <label><input type="radio" name="q22" value="c"> C) $$x = 0, y = 1$$</label>
                <label><input type="radio" name="q22" value="d"> D) Không có nghiệm</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$x = 0.5, y = 0.5$$</strong><br>
                Sử dụng phương pháp Lagrange với ràng buộc tích cực $$x + y = 1$$, ta được $$x = y = 0.5$$.
            </div>
        </div>

        <!-- Câu hỏi 23: Thực hành -->
        <div class="question" id="q23" style="display: none;">
            <h3>Câu 23: Hàm Lagrange của bài toán $$\min f(x)$$ với $$g(x) \leq 0$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) $$L(x,\lambda) = f(x) + \lambda g(x)$$</label>
                <label><input type="radio" name="q23" value="b"> B) $$L(x,\lambda) = f(x) - \lambda g(x)$$</label>
                <label><input type="radio" name="q23" value="c"> C) $$L(x,\lambda) = f(x) + \lambda^2 g(x)$$</label>
                <label><input type="radio" name="q23" value="d"> D) $$L(x,\lambda) = f(x) \cdot \lambda g(x)$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$L(x,\lambda) = f(x) + \lambda g(x)$$</strong><br>
                Hàm Lagrange chuẩn có dạng $$L(x,\lambda) = f(x) + \lambda g(x)$$ với $$\lambda \geq 0$$.
            </div>
        </div>

        <!-- Câu hỏi 24: Thực hành -->
        <div class="question" id="q24" style="display: none;">
            <h3>Câu 24: Điều kiện bù lỏng (complementary slackness) trong KKT là:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) $$\lambda_i g_i(x) = 0$$</label>
                <label><input type="radio" name="q24" value="b"> B) $$\lambda_i + g_i(x) = 0$$</label>
                <label><input type="radio" name="q24" value="c"> C) $$\lambda_i - g_i(x) = 0$$</label>
                <label><input type="radio" name="q24" value="d"> D) $$\lambda_i \cdot g_i(x) = 1$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\lambda_i g_i(x) = 0$$</strong><br>
                Điều kiện bù lỏng $$\lambda_i g_i(x) = 0$$ đảm bảo rằng với mỗi ràng buộc, hoặc ràng buộc đó tích cực ($$g_i(x) = 0$$) hoặc nhân tử Lagrange tương ứng bằng 0 ($$\lambda_i = 0$$).
            </div>
        </div>

        <!-- Câu hỏi 25: Thực hành -->
        <div class="question" id="q25" style="display: none;">
            <h3>Câu 25: Trong bài toán QP: $$\min \frac{1}{2}x^T P x + q^T x$$, ma trận $$P$$ phải:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) Nửa xác định dương</label>
                <label><input type="radio" name="q25" value="b"> B) Xác định dương</label>
                <label><input type="radio" name="q25" value="c"> C) Đối xứng</label>
                <label><input type="radio" name="q25" value="d"> D) Cả A và C</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Cả A và C</strong><br>
                Để bài toán QP là lồi, ma trận $$P$$ phải nửa xác định dương và đối xứng.
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
    background: linear-gradient(90deg, #E91E63, #9C27B0);
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
    border-color: #E91E63;
    background-color: #fce4ec;
}

.options input[type="radio"] {
    margin-right: 12px;
    margin-top: 2px;
    transform: scale(1.2);
    flex-shrink: 0;
}

.options label.selected {
    border-color: #E91E63;
    background-color: #f8bbd9;
}

.explanation {
    margin-top: 20px;
    padding: 15px;
    background-color: #fce4ec;
    border-left: 4px solid #E91E63;
    border-radius: 4px;
    font-size: 0.95em;
    line-height: 1.5;
}

.explanation strong {
    color: #AD1457;
}

#quiz-navigation {
    text-align: center;
    margin: 30px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

#quiz-navigation button {
    background: #E91E63;
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.2s ease;
}

#quiz-navigation button:hover:not(:disabled) {
    background: #C2185B;
}

#quiz-navigation button:disabled {
    background: #cccccc;
    cursor: not-allowed;
}

#quiz-results {
    text-align: center;
    padding: 30px;
    background: #fce4ec;
    border-radius: 8px;
    border: 2px solid #E91E63;
}

#score-display {
    font-size: 1.5em;
    font-weight: bold;
    margin: 20px 0;
    color: #AD1457;
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
    q1: 'c', q2: 'b', q3: 'b', q4: 'b', q5: 'a',
    q6: 'b', q7: 'b', q8: 'a', q9: 'b', q10: 'b',
    q11: 'a', q12: 'b', q13: 'b', q14: 'b', q15: 'b',
    q16: 'b', q17: 'a', q18: 'b', q19: 'c', q20: 'b'
,
    q21: 'a', q22: 'a', q23: 'a', q24: 'a', q25: 'd'};

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
            ${scorePercentage >= 80 ? '🎉 Xuất sắc! Bạn đã nắm vững cơ bản tối ưu hóa lồi!' : 
              scorePercentage >= 60 ? '👍 Khá tốt! Hãy ôn lại một số khái niệm cơ bản.' : 
              scorePercentage >= 40 ? '📚 Cần ôn tập thêm về thuật ngữ và điều kiện tối ưu.' : '💪 Hãy đọc lại lý thuyết cơ bản về tối ưu hóa lồi!'}
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
