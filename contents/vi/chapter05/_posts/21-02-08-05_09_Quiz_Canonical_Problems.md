---
layout: post
title: 05-07 Bài tập trắc nghiệm - Các bài toán tối ưu kinh điển
chapter: '05'
order: 11
owner: GitHub Copilot
lang: vi
categories:
- chapter05
lesson_type: quiz
---

Bài tập trắc nghiệm này kiểm tra hiểu biết của bạn về các bài toán tối ưu kinh điển, bao gồm quy hoạch tuyến tính, quy hoạch bậc hai, bình phương tối thiểu và hồi quy tuyến tính.

---

## 📚 Ôn tập lý thuyết

Trước khi làm bài tập, hãy ôn lại các khái niệm chính trong chương này:

### 📊 **Quy Hoạch Tuyến Tính (LP)**

**Dạng tổng quát:**
$$\begin{align}
&\min_{x} &&c^T x + d \\
&\text{s.t.} &&Gx \preceq h \\
&&&Ax = b
\end{align}$$

**Dạng chuẩn:**
$$\begin{align}
&\min_{x} &&c^T x \\
&\text{s.t.} &&Ax = b \\
&&&x \succeq 0
\end{align}$$

**Đặc điểm chính:**
- Hàm mục tiêu và ràng buộc đều **affine** (tuyến tính)
- Tập khả thi là **đa diện** (polyhedron)
- Nếu có nghiệm tối ưu (và đa diện có đỉnh), luôn tồn tại một nghiệm tối ưu tại **đỉnh** của đa diện
- Có thể giải hiệu quả bằng **thuật toán Simplex**

**Chuyển đổi về dạng chuẩn:**
1. Thêm biến slack: $$g_i(x) \le 0 \Rightarrow g_i(x) + s_i = 0, s_i \ge 0$$
2. Tách biến: $$x = x^+ - x^-$$ với $$x^+, x^- \ge 0$$

### 📈 **Quy Hoạch Bậc Hai (QP)**

**Dạng tổng quát:**
$$\begin{align}
&\min_{x} &&\frac{1}{2}x^T P x + q^T x + r \\
&\text{s.t.} &&Gx \preceq h \\
&&&Ax = b
\end{align}$$

**Điều kiện lồi:** $$P \in \mathbb{S}_+^n$$ (ma trận bán xác định dương)

**Kiểm tra $$P \succeq 0$$:**
- Tất cả eigenvalue $$\lambda_i \ge 0$$
- $$v^T P v \ge 0$$ với mọi $$v$$
- Với ma trận $$2 \times 2$$: $$a \ge 0, c \ge 0, ac \ge b^2$$

**Ví dụ ứng dụng:**
- **Tối ưu hóa danh mục:** $$\max \mu^T x - \frac{\gamma}{2}x^T P x$$
- **SVM:** $$\min \frac{1}{2}\lVert \beta \rVert_2^2 + C\sum \xi_i$$
- **Hồi quy Ridge:** $$\min \lVert Ax - b \rVert_2^2 + \lambda \lVert x \rVert_2^2$$

### 🎯 **Bình Phương Tối Thiểu**

**Bài toán cơ bản:**
$$\min_{x} \lVert Ax - b \rVert_2^2 = \min_{x} \sum_{i=1}^m (a_i^T x - b_i)^2$$

**Nghiệm dạng đóng (Normal Equation):**
$$x^* = (A^T A)^{-1} A^T b$$

**Điều kiện tồn tại nghiệm duy nhất:** $$A^T A$$ khả nghịch ($$A$$ có hạng cột đầy đủ)

**Hồi quy tuyến tính một biến:**
- Mô hình: $$y = mx + c$$
- Nghiệm: $$m = \frac{\sum(x_i - \bar{x})(y_i - \bar{y})}{\sum(x_i - \bar{x})^2}$$, $$c = \bar{y} - m\bar{x}$$

**Hồi quy tuyến tính nhiều biến:**
- Mô hình: $$y = X\beta$$
- Nghiệm: $$\beta^* = (X^T X)^{-1} X^T y$$

### 🔢 **Các Bài Toán Kinh Điển Khác**

**QCQP (Quadratically Constrained QP):**
$$\begin{align}
&\min &&\frac{1}{2}x^T P_0 x + q_0^T x \\
&\text{s.t.} &&\frac{1}{2}x^T P_i x + q_i^T x + r_i \le 0, \quad i = 1,\ldots,m
\end{align}$$

**SOCP (Second-Order Cone Programming):**
$$\begin{align}
&\min &&f^T x \\
&\text{s.t.} &&\lVert A_i x + b_i \rVert_2 \le c_i^T x + d_i, \quad i = 1,\ldots,m
\end{align}$$

**SDP (Semidefinite Programming):**
$$\begin{align}
&\min &&\text{tr}(CX) \\
&\text{s.t.} &&\text{tr}(A_i X) = b_i, \quad i = 1,\ldots,m \\
&&&X \succeq 0
\end{align}$$

### 🏗️ **Mối Quan Hệ Giữa Các Bài Toán**

```
LP ⊆ QP ⊆ QCQP ⊆ SDP
    ⊆ SOCP ⊆
```

**Giải thích:**
- **LP → QP:** Đặt $$P = 0$$ trong QP
- **QP → QCQP:** Ràng buộc tuyến tính là trường hợp đặc biệt của ràng buộc bậc hai
- **SOCP → SDP:** Nón bậc hai biểu diễn được bằng ràng buộc nửa xác định dương (LMI)
- **QCQP → SDP:** QCQP (lồi) có thể biểu diễn qua SDP với kỹ thuật Schur complement

### 🛠️ **Thuật Toán Giải**

**Linear Programming:**
- **Simplex Method:** Di chuyển từ đỉnh này sang đỉnh khác
- **Interior Point Methods:** Đi qua phần trong của tập khả thi
- **Dual Simplex:** Bắt đầu từ nghiệm dual khả thi

**Quadratic Programming:**
- **Active Set Methods:** Xác định ràng buộc hoạt động
- **Interior Point Methods:** Mở rộng từ LP
- **Gradient Projection:** Chiếu gradient lên tập khả thi

**Least Squares:**
- **Normal Equation:** Nghiệm trực tiếp $$x^* = (A^T A)^{-1} A^T b$$
- **QR Decomposition:** Ổn định số hơn
- **SVD:** Xử lý ma trận suy biến
- **Gradient Descent:** Cho bài toán lớn

### 📋 **Ứng Dụng Thực Tế**

**Linear Programming:**
- Tối ưu hóa sản xuất và phân phối
- Lập kế hoạch chế độ ăn uống
- Quản lý danh mục đầu tư
- Lịch trình nhân viên

**Quadratic Programming:**
- Tối ưu hóa danh mục Markowitz
- Support Vector Machines
- Model Predictive Control
- Image denoising

**Least Squares:**
- Hồi quy tuyến tính và phi tuyến
- Curve fitting và interpolation
- Signal processing
- Computer vision

### 🔍 **Nhận Biết Loại Bài Toán**

**Checklist:**
- [ ] Hàm mục tiêu tuyến tính? → **LP**
- [ ] Hàm mục tiêu bậc hai, ràng buộc tuyến tính? → **QP**
- [ ] Ràng buộc bậc hai? → **QCQP**
- [ ] Ràng buộc norm? → **SOCP**
- [ ] Ràng buộc ma trận? → **SDP**
- [ ] Không có ràng buộc, mục tiêu bình phương? → **Least Squares**

### ⚡ **Độ Phức Tạp Tính Toán**

| Bài toán | Độ phức tạp | Ghi chú |
|----------|-------------|---------|
| **LP** | Đa thức (interior point); Simplex nhanh trong thực tế | Simplex: tốt trung bình |
| **QP** | Đa thức | Interior point methods |
| **Least Squares** | $$O(n^3)$$ | Normal equation |
| **SOCP** | Đa thức | Tương tự SDP |
| **SDP** | Đa thức | Chậm hơn LP, QP |

---

💡 **Mẹo:** Luôn bắt đầu với bài toán đơn giản nhất có thể giải quyết vấn đề của bạn. LP nhanh hơn QP, QP nhanh hơn SDP!

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>Bài tập trắc nghiệm: Các bài toán tối ưu kinh điển</h2>
        <p>Chọn đáp án đúng nhất cho mỗi câu hỏi. Bài tập tập trung vào các khái niệm cơ bản và ứng dụng thực tế của LP, QP và bình phương tối thiểu.</p>
        <div id="progress-bar">
            <div id="progress-fill"></div>
        </div>
        <p id="progress-text">Câu hỏi 1/25</p>
    </div>

    <div id="quiz-questions">
        <!-- Câu hỏi 1: Định nghĩa LP -->
        <div class="question" id="q1">
            <h3>Câu 1: Quy hoạch tuyến tính (LP) có đặc điểm nào sau đây?</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) Hàm mục tiêu và ràng buộc đều là hàm tuyến tính</label>
                <label><input type="radio" name="q1" value="b"> B) Hàm mục tiêu là bậc hai, ràng buộc tuyến tính</label>
                <label><input type="radio" name="q1" value="c"> C) Hàm mục tiêu tuyến tính, ràng buộc phi tuyến</label>
                <label><input type="radio" name="q1" value="d"> D) Cả hàm mục tiêu và ràng buộc đều phi tuyến</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Hàm mục tiêu và ràng buộc đều là hàm tuyến tính</strong><br>
                Quy hoạch tuyến tính được định nghĩa bởi hàm mục tiêu tuyến tính và tất cả ràng buộc đều là tuyến tính (affine).
            </div>
        </div>

        <!-- Câu hỏi 2: Dạng chuẩn LP -->
        <div class="question" id="q2" style="display: none;">
            <h3>Câu 2: Dạng chuẩn của LP có đặc điểm:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) Tối đa hóa, ràng buộc bất đẳng thức, biến tự do</label>
                <label><input type="radio" name="q2" value="b"> B) Tối thiểu hóa, ràng buộc đẳng thức, biến không âm</label>
                <label><input type="radio" name="q2" value="c"> C) Tối đa hóa, ràng buộc đẳng thức, biến không âm</label>
                <label><input type="radio" name="q2" value="d"> D) Tối thiểu hóa, ràng buộc bất đẳng thức, biến tự do</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Tối thiểu hóa, ràng buộc đẳng thức, biến không âm</strong><br>
                Dạng chuẩn LP: minimize $$c^T x$$ subject to $$Ax = b$$, $$x \geq 0$$.
            </div>
        </div>

        <!-- Câu hỏi 3: Biến slack -->
        <div class="question" id="q3" style="display: none;">
            <h3>Câu 3: Biến slack được sử dụng để:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) Chuyển ràng buộc đẳng thức thành bất đẳng thức</label>
                <label><input type="radio" name="q3" value="b"> B) Chuyển ràng buộc bất đẳng thức thành đẳng thức</label>
                <label><input type="radio" name="q3" value="c"> C) Tăng số biến trong bài toán</label>
                <label><input type="radio" name="q3" value="d"> D) Giảm độ phức tạp tính toán</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Chuyển ràng buộc bất đẳng thức thành đẳng thức</strong><br>
                Biến slack chuyển $$Gx \leq h$$ thành $$Gx + s = h$$ với $$s \geq 0$$.
            </div>
        </div>

        <!-- Câu hỏi 4: Định lý cơ bản LP -->
        <div class="question" id="q4" style="display: none;">
            <h3>Câu 4: Định lý cơ bản của quy hoạch tuyến tính nói rằng:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) Nghiệm tối ưu luôn duy nhất</label>
                <label><input type="radio" name="q4" value="b"> B) Nếu LP có nghiệm tối ưu và vùng khả thi có đỉnh, thì luôn có một nghiệm tối ưu tại một đỉnh</label>
                <label><input type="radio" name="q4" value="c"> C) Vùng khả thi luôn bị chặn</label>
                <label><input type="radio" name="q4" value="d"> D) Hàm mục tiêu luôn có cực tiểu toàn cục</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Nếu LP có nghiệm tối ưu và vùng khả thi có đỉnh, thì luôn có một nghiệm tối ưu tại một đỉnh</strong><br>
                Đây là cơ sở cho thuật toán Simplex: nghiệm tối ưu của LP luôn có thể tìm thấy tại một đỉnh.
            </div>
        </div>

        <!-- Câu hỏi 5: Thuật toán Simplex -->
        <div class="question" id="q5" style="display: none;">
            <h3>Câu 5: Thuật toán Simplex hoạt động bằng cách:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) Tìm kiếm ngẫu nhiên trong vùng khả thi</label>
                <label><input type="radio" name="q5" value="b"> B) Di chuyển từ đỉnh này sang đỉnh khác để cải thiện hàm mục tiêu</label>
                <label><input type="radio" name="q5" value="c"> C) Sử dụng gradient descent</label>
                <label><input type="radio" name="q5" value="d"> D) Chia đôi vùng khả thi</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Di chuyển từ đỉnh này sang đỉnh khác để cải thiện hàm mục tiêu</strong><br>
                Simplex bắt đầu từ một đỉnh và di chuyển đến đỉnh kề cải thiện giá trị hàm mục tiêu.
            </div>
        </div>

        <!-- Câu hỏi 6: QP định nghĩa -->
        <div class="question" id="q6" style="display: none;">
            <h3>Câu 6: Quy hoạch bậc hai (QP) có hàm mục tiêu dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) $$c^T x$$</label>
                <label><input type="radio" name="q6" value="b"> B) $$\frac{1}{2}x^T P x + q^T x + r$$</label>
                <label><input type="radio" name="q6" value="c"> C) $$\|Ax - b\|_2$$</label>
                <label><input type="radio" name="q6" value="d"> D) $$x^T A x^T$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$\frac{1}{2}x^T P x + q^T x + r$$</strong><br>
                QP có hàm mục tiêu là hàm bậc hai lồi với ma trận $$P \in \mathbb{S}_+^n$$.
            </div>
        </div>

        <!-- Câu hỏi 7: Ma trận P trong QP -->
        <div class="question" id="q7" style="display: none;">
            <h3>Câu 7: Trong QP, ma trận $$P$$ phải thỏa mãn điều kiện:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) $$P$$ là ma trận đối xứng</label>
                <label><input type="radio" name="q7" value="b"> B) $$P$$ là ma trận bán xác định dương</label>
                <label><input type="radio" name="q7" value="c"> C) $$P$$ là ma trận khả nghịch</label>
                <label><input type="radio" name="q7" value="d"> D) $$P$$ là ma trận đường chéo</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$P$$ là ma trận bán xác định dương</strong><br>
                Điều kiện $$P \in \mathbb{S}_+^n$$ đảm bảo hàm mục tiêu là lồi.
            </div>
        </div>

        <!-- Câu hỏi 8: LP là trường hợp đặc biệt của QP -->
        <div class="question" id="q8" style="display: none;">
            <h3>Câu 8: LP là trường hợp đặc biệt của QP khi:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) $$P = I$$ (ma trận đơn vị)</label>
                <label><input type="radio" name="q8" value="b"> B) $$P = 0$$ (ma trận không)</label>
                <label><input type="radio" name="q8" value="c"> C) $$q = 0$$</label>
                <label><input type="radio" name="q8" value="d"> D) $$r = 0$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$P = 0$$ (ma trận không)</strong><br>
                Khi $$P = 0$$, hàm mục tiêu QP trở thành $$q^T x + r$$, đây chính là LP.
            </div>
        </div>

        <!-- Câu hỏi 9: Bài toán bình phương tối thiểu -->
        <div class="question" id="q9" style="display: none;">
            <h3>Câu 9: Bài toán bình phương tối thiểu tuyến tính có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) minimize $$\|Ax - b\|_1$$</label>
                <label><input type="radio" name="q9" value="b"> B) minimize $$\|Ax - b\|_2^2$$</label>
                <label><input type="radio" name="q9" value="c"> C) minimize $$\|Ax - b\|_\infty$$</label>
                <label><input type="radio" name="q9" value="d"> D) minimize $$x^T A x$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) minimize $$\|Ax - b\|_2^2$$</strong><br>
                Bài toán bình phương tối thiểu tối thiểu hóa tổng các sai số bình phương.
            </div>
        </div>

        <!-- Câu hỏi 10: Nghiệm phương trình chuẩn -->
        <div class="question" id="q10" style="display: none;">
            <h3>Câu 10: Nghiệm của bài toán bình phương tối thiểu được cho bởi:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) $$x^* = A^{-1}b$$</label>
                <label><input type="radio" name="q10" value="b"> B) $$x^* = (A^T A)^{-1} A^T b$$</label>
                <label><input type="radio" name="q10" value="c"> C) $$x^* = A^T (AA^T)^{-1} b$$</label>
                <label><input type="radio" name="q10" value="d"> D) $$x^* = A^T b$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$x^* = (A^T A)^{-1} A^T b$$</strong><br>
                Đây là nghiệm dạng đóng của phương trình chuẩn $$A^T A x = A^T b$$ (khi $$A$$ có hạng cột đầy đủ).
            </div>
        </div>

        <!-- Câu hỏi 11: Hồi quy tuyến tính đơn biến -->
        <div class="question" id="q11" style="display: none;">
            <h3>Câu 11: Trong hồi quy tuyến tính $$y = mx + c$$, hệ số góc $$m$$ được tính bằng:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) $$\frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}$$</label>
                <label><input type="radio" name="q11" value="b"> B) $$\frac{\sum (y_i - \bar{y})^2}{\sum (x_i - \bar{x})^2}$$</label>
                <label><input type="radio" name="q11" value="c"> C) $$\bar{y} - m\bar{x}$$</label>
                <label><input type="radio" name="q11" value="d"> D) $$\frac{\sum x_i y_i}{\sum x_i^2}$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}$$</strong><br>
                Đây là công thức chuẩn cho hệ số góc trong hồi quy tuyến tính đơn biến.
            </div>
        </div>

        <!-- Câu hỏi 12: Giả thuyết Gauss-Markov -->
        <div class="question" id="q12" style="display: none;">
            <h3>Câu 12: Giả thuyết Gauss-Markov không bao gồm:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) Sai số có kỳ vọng bằng 0</label>
                <label><input type="radio" name="q12" value="b"> B) Các sai số không tương quan</label>
                <label><input type="radio" name="q12" value="c"> C) Phương sai đồng nhất</label>
                <label><input type="radio" name="q12" value="d"> D) Sai số phân phối đều</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Sai số phân phối đều</strong><br>
                Giả thuyết Gauss-Markov chỉ yêu cầu sai số có kỳ vọng 0, không tương quan và có phương sai đồng nhất; nó không giả định phân phối cụ thể nào (không cần chuẩn, càng không cần đều). Giả định phân phối chuẩn chỉ cần thêm cho suy luận (kiểm định, khoảng tin cậy) hoặc để OLS trùng với MLE.
            </div>
        </div>

        <!-- Câu hỏi 13: Ước lượng hợp lý tối đa -->
        <div class="question" id="q13" style="display: none;">
            <h3>Câu 13: Ước lượng hợp lý tối đa (MLE) trong hồi quy tuyến tính tương đương với:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) Tối đa hóa log-likelihood</label>
                <label><input type="radio" name="q13" value="b"> B) Tối thiểu hóa tổng sai số bình phương</label>
                <label><input type="radio" name="q13" value="c"> C) Cả A và B</label>
                <label><input type="radio" name="q13" value="d"> D) Tối đa hóa R²</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) Cả A và B</strong><br>
                Dưới giả thuyết Gaussian, tối đa hóa log-likelihood tương đương với tối thiểu hóa MSE.
            </div>
        </div>

        <!-- Câu hỏi 14: Ứng dụng LP -->
        <div class="question" id="q14" style="display: none;">
            <h3>Câu 14: Bài toán chế độ ăn uống là ví dụ của:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) Quy hoạch tuyến tính</label>
                <label><input type="radio" name="q14" value="b"> B) Quy hoạch bậc hai</label>
                <label><input type="radio" name="q14" value="c"> C) Bình phương tối thiểu</label>
                <label><input type="radio" name="q14" value="d"> D) Quy hoạch phi tuyến</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Quy hoạch tuyến tính</strong><br>
                Bài toán chế độ ăn uống có hàm mục tiêu và ràng buộc đều tuyến tính.
            </div>
        </div>

        <!-- Câu hỏi 15: Ứng dụng QP -->
        <div class="question" id="q15" style="display: none;">
            <h3>Câu 15: Tối ưu hóa danh mục đầu tư là ví dụ của:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) Quy hoạch tuyến tính</label>
                <label><input type="radio" name="q15" value="b"> B) Quy hoạch bậc hai</label>
                <label><input type="radio" name="q15" value="c"> C) Bình phương tối thiểu</label>
                <label><input type="radio" name="q15" value="d"> D) Quy hoạch nguyên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Quy hoạch bậc hai</strong><br>
                Tối ưu hóa danh mục cân bằng lợi nhuận (tuyến tính) và rủi ro (bậc hai).
            </div>
        </div>

        <!-- Câu hỏi 16: Polytope -->
        <div class="question" id="q16" style="display: none;">
            <h3>Câu 16: Vùng khả thi của LP được gọi là:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) Ellipsoid</label>
                <label><input type="radio" name="q16" value="b"> B) Polytope (nếu bị chặn)</label>
                <label><input type="radio" name="q16" value="c"> C) Simplex</label>
                <label><input type="radio" name="q16" value="d"> D) Hyperplane</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Polytope (nếu bị chặn)</strong><br>
                Vùng khả thi của LP là giao của các nửa không gian, tạo thành polytope nếu bị chặn.
            </div>
        </div>

        <!-- Câu hỏi 17: Điều kiện tối ưu cho least squares -->
        <div class="question" id="q17" style="display: none;">
            <h3>Câu 17: Điều kiện tối ưu cho bài toán bình phương tối thiểu là:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) $$Ax = b$$</label>
                <label><input type="radio" name="q17" value="b"> B) $$A^T A x = A^T b$$</label>
                <label><input type="radio" name="q17" value="c"> C) $$A^T x = b$$</label>
                <label><input type="radio" name="q17" value="d"> D) $$x = 0$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$A^T A x = A^T b$$</strong><br>
                Đây là phương trình chuẩn, điều kiện cần và đủ cho bài toán bình phương tối thiểu.
            </div>
        </div>

        <!-- Câu hỏi 18: R² trong hồi quy -->
        <div class="question" id="q18" style="display: none;">
            <h3>Câu 18: Hệ số xác định R² đo lường:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) Sai số trung bình</label>
                <label><input type="radio" name="q18" value="b"> B) Tỷ lệ phương sai được giải thích bởi mô hình</label>
                <label><input type="radio" name="q18" value="c"> C) Độ lệch chuẩn</label>
                <label><input type="radio" name="q18" value="d"> D) Hệ số tương quan</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Tỷ lệ phương sai được giải thích bởi mô hình</strong><br>
                R² = 1 - (SSres/SStot) cho biết mô hình giải thích được bao nhiêu phần trăm biến thiên của dữ liệu.
            </div>
        </div>

        <!-- Câu hỏi 19: Độ phức tạp Simplex -->
        <div class="question" id="q19" style="display: none;">
            <h3>Câu 19: Độ phức tạp của thuật toán Simplex là:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) Đa thức</label>
                <label><input type="radio" name="q19" value="b"> B) Mũ trong trường hợp xấu nhất nhưng hiệu quả trong thực tế</label>
                <label><input type="radio" name="q19" value="c"> C) Logarithmic</label>
                <label><input type="radio" name="q19" value="d"> D) Hằng số</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Mũ trong trường hợp xấu nhất nhưng hiệu quả trong thực tế</strong><br>
                Simplex có độ phức tạp mũ trong trường hợp xấu nhất (ví dụ Klee-Minty) nhưng trong thực tế số vòng lặp thường chỉ khoảng 2-3 lần số ràng buộc.
            </div>
        </div>

        <!-- Câu hỏi 20: BLUE -->
        <div class="question" id="q20" style="display: none;">
            <h3>Câu 20: BLUE trong hồi quy tuyến tính có nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Best Linear Unbiased Estimator</label>
                <label><input type="radio" name="q20" value="b"> B) Basic Linear Uniform Estimation</label>
                <label><input type="radio" name="q20" value="c"> C) Bayesian Linear Update Equation</label>
                <label><input type="radio" name="q20" value="d"> D) Bounded Linear Uncertainty Estimate</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Best Linear Unbiased Estimator</strong><br>
                Dưới giả thuyết Gauss-Markov, OLS cho ước lượng tuyến tính không chệch tốt nhất.
            </div>
        </div>
        <!-- Câu hỏi 21: Thực hành -->
        <div class="question" id="q21" style="display: none;">
            <h3>Câu 21: Bài toán LP có dạng chuẩn là:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) $$\min c^T x$$ với $$Ax = b, x \geq 0$$</label>
                <label><input type="radio" name="q21" value="b"> B) $$\min c^T x$$ với $$Ax \leq b$$</label>
                <label><input type="radio" name="q21" value="c"> C) $$\max c^T x$$ với $$Ax \leq b$$</label>
                <label><input type="radio" name="q21" value="d"> D) $$\min c^T x$$ với $$Ax \geq b$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\min c^T x$$ với $$Ax = b, x \geq 0$$</strong><br>
                Dạng chuẩn của LP là tối thiểu hóa với ràng buộc đẳng thức và ràng buộc không âm.
            </div>
        </div>

        <!-- Câu hỏi 22: Thực hành -->
        <div class="question" id="q22" style="display: none;">
            <h3>Câu 22: Trong SOCP, ràng buộc nón có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) $$\|Ax + b\|_2 \leq c^T x + d$$</label>
                <label><input type="radio" name="q22" value="b"> B) $$\|Ax + b\|_1 \leq c^T x + d$$</label>
                <label><input type="radio" name="q22" value="c"> C) $$\|Ax + b\|_\infty \leq c^T x + d$$</label>
                <label><input type="radio" name="q22" value="d"> D) $$(Ax + b)^2 \leq c^T x + d$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\|Ax + b\|_2 \leq c^T x + d$$</strong><br>
                SOCP sử dụng ràng buộc nón bậc hai với chuẩn Euclid (L2).
            </div>
        </div>

        <!-- Câu hỏi 23: Thực hành -->
        <div class="question" id="q23" style="display: none;">
            <h3>Câu 23: Bài toán SDP có ràng buộc:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) Ma trận nửa xác định dương</label>
                <label><input type="radio" name="q23" value="b"> B) Ma trận đối xứng</label>
                <label><input type="radio" name="q23" value="c"> C) Ma trận tam giác</label>
                <label><input type="radio" name="q23" value="d"> D) Ma trận đường chéo</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Ma trận nửa xác định dương</strong><br>
                SDP có ràng buộc ma trận phải nửa xác định dương: $$X \succeq 0$$.
            </div>
        </div>

        <!-- Câu hỏi 24: Thực hành -->
        <div class="question" id="q24" style="display: none;">
            <h3>Câu 24: Bài toán phân bổ tài nguyên với 3 dự án và ngân sách 100 có thể mô hình hóa bằng:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) LP</label>
                <label><input type="radio" name="q24" value="b"> B) QP</label>
                <label><input type="radio" name="q24" value="c"> C) SOCP</label>
                <label><input type="radio" name="q24" value="d"> D) SDP</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) LP</strong><br>
                Bài toán phân bổ tài nguyên tuyến tính thường được mô hình hóa bằng Linear Programming.
            </div>
        </div>

        <!-- Câu hỏi 25: Thực hành -->
        <div class="question" id="q25" style="display: none;">
            <h3>Câu 25: Trong bài toán portfolio optimization, hàm mục tiêu thường là:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) Tối thiểu hóa rủi ro (phương sai)</label>
                <label><input type="radio" name="q25" value="b"> B) Tối đa hóa lợi nhuận</label>
                <label><input type="radio" name="q25" value="c"> C) Cân bằng rủi ro-lợi nhuận</label>
                <label><input type="radio" name="q25" value="d"> D) Tất cả các trường hợp trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các trường hợp trên</strong><br>
                Portfolio optimization có thể tối thiểu rủi ro, tối đa lợi nhuận, hoặc cân bằng cả hai (Markowitz model).
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
    background: linear-gradient(90deg, #FF6B35, #F7931E);
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
    border-color: #FF6B35;
    background-color: #fff5f0;
}

.options input[type="radio"] {
    margin-right: 12px;
    margin-top: 2px;
    transform: scale(1.2);
    flex-shrink: 0;
}

.options label.selected {
    border-color: #FF6B35;
    background-color: #ffe5d6;
}

.explanation {
    margin-top: 20px;
    padding: 15px;
    background-color: #fff5f0;
    border-left: 4px solid #FF6B35;
    border-radius: 4px;
    font-size: 0.95em;
    line-height: 1.5;
}

.explanation strong {
    color: #D2691E;
}

#quiz-navigation {
    text-align: center;
    margin: 30px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

#quiz-navigation button {
    background: #FF6B35;
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.2s ease;
}

#quiz-navigation button:hover:not(:disabled) {
    background: #E55A2B;
}

#quiz-navigation button:disabled {
    background: #cccccc;
    cursor: not-allowed;
}

#quiz-results {
    text-align: center;
    padding: 30px;
    background: #fff5f0;
    border-radius: 8px;
    border: 2px solid #FF6B35;
}

#score-display {
    font-size: 1.5em;
    font-weight: bold;
    margin: 20px 0;
    color: #D2691E;
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
    q1: 'a', q2: 'b', q3: 'b', q4: 'b', q5: 'b',
    q6: 'b', q7: 'b', q8: 'b', q9: 'b', q10: 'b',
    q11: 'a', q12: 'd', q13: 'c', q14: 'a', q15: 'b',
    q16: 'b', q17: 'b', q18: 'b', q19: 'b', q20: 'a'
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
            ${scorePercentage >= 80 ? '🎉 Xuất sắc! Bạn đã nắm vững các bài toán tối ưu kinh điển!' : 
              scorePercentage >= 60 ? '👍 Khá tốt! Hãy ôn lại một số khái niệm về LP và QP.' : 
              scorePercentage >= 40 ? '📚 Cần ôn tập thêm về thuật toán Simplex và bình phương tối thiểu.' : '💪 Hãy đọc lại lý thuyết về các bài toán tối ưu cơ bản!'}
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
