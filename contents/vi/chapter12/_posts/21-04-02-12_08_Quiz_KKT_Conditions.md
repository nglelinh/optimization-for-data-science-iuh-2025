---
layout: post
title: 12-08 Bài tập trắc nghiệm - Điều Kiện KKT
chapter: '12'
order: 9
owner: GitHub Copilot
lang: vi
categories:
- chapter12
lesson_type: quiz
redirect_from:
  - /contents/vi/chapter12/12_07_Quiz_KKT_Conditions/
---

## 📚 Ôn tập lý thuyết

Trước khi làm bài tập trắc nghiệm, hãy ôn lại các khái niệm trọng tâm trong chương này:

### ⚡ **Điều kiện Karush–Kuhn–Tucker (KKT)**

#### **Bài toán tối ưu tổng quát**
$$\min_x f(x) \quad \text{s.t.} \quad h_i(x) \le 0, \quad l_j(x) = 0$$

với $$i = 1,\ldots,m$$ và $$j = 1,\ldots,r$$.

#### **Bốn điều kiện KKT**
Với bộ điểm $$(x^*, \lambda^*, \nu^*)$$:

1. **Điều kiện dừng (Stationarity):**
   $$0 \in \partial \left( f(x^*) + \sum_{i=1}^m \lambda_i^* h_i(x^*) + \sum_{j=1}^r \nu_j^* l_j(x^*) \right)$$

2. **Điều kiện bù yếu (Complementary slackness):**
   $$\lambda_i^* \cdot h_i(x^*) = 0 \quad \forall i$$

3. **Tính khả thi nguyên thủy (Primal feasibility):**
   $$h_i(x^*) \le 0, \quad l_j(x^*) = 0 \quad \forall i,j$$

4. **Tính khả thi đối ngẫu (Dual feasibility):**
   $$\lambda_i^* \ge 0 \quad \forall i$$

#### **Ý nghĩa của từng điều kiện**
- **Điều kiện dừng:** Gradient (hoặc dưới vi phân) của hàm Lagrangian theo $$x$$ bằng $$0$$ (chứa $$0$$).
- **Điều kiện bù yếu:** Với mỗi ràng buộc bất đẳng thức, hoặc ràng buộc đang chặt ($$h_i(x^*) = 0$$), hoặc nhân tử đối ngẫu bằng không ($$\lambda_i^* = 0$$).
- **Tính khả thi nguyên thủy:** Điểm $$x^*$$ thỏa mãn mọi ràng buộc của bài toán gốc.
- **Tính khả thi đối ngẫu:** Các nhân tử ứng với ràng buộc bất đẳng thức phải không âm.

### 📊 **Điều kiện đủ và điều kiện cần**

#### **Điều kiện đủ (Sufficiency)**
Nếu $$(x^*, \lambda^*, \nu^*)$$ thỏa mãn các điều kiện KKT và bài toán là **bài toán lồi**, thì đây là cặp nghiệm tối ưu nguyên thủy và đối ngẫu.

**Chứng minh ngắn:**
$$g(\lambda^*, \nu^*) = \min_x L(x, \lambda^*, \nu^*) = L(x^*, \lambda^*, \nu^*) = f(x^*)$$

Do đó $$g(\lambda^*, \nu^*) = f(x^*)$$, tức khoảng cách đối ngẫu bằng $$0$$ nên nghiệm đạt tối ưu toàn cục.

#### **Điều kiện cần (Necessity)**
Nếu $$(x^*, \lambda^*, \nu^*)$$ là cặp nghiệm tối ưu và bài toán thỏa mãn **tính đối ngẫu mạnh** (chẳng hạn thỏa điều kiện Slater), thì chúng bắt buộc thỏa mãn các điều kiện KKT.

#### **Tổng kết**
Đối với bài toán lồi có tính đối ngẫu mạnh:
$$x^*, \lambda^*, \nu^* \text{ tối ưu} \Leftrightarrow x^*, \lambda^*, \nu^* \text{ thỏa mãn các điều kiện KKT}$$

### 🔄 **Ví dụ: Quy hoạch bậc hai với ràng buộc đẳng thức**

#### **Bài toán**
$$\min_x \frac{1}{2}x^T P x + q^T x + r \quad \text{s.t.} \quad Ax = b$$

với $$P \in \mathbb{S}_+^n$$ (ma trận nửa xác định dương).

#### **Điều kiện KKT**
- **Điều kiện dừng:** $$Px^* + q + A^T \nu^* = 0$$
- **Khả thi nguyên thủy:** $$Ax^* = b$$
- **Bù yếu và khả thi đối ngẫu:** Không xuất hiện vì không có ràng buộc bất đẳng thức.

#### **Hệ ma trận KKT**
$$\begin{bmatrix} P & A^T \\ A & 0 \end{bmatrix} \begin{bmatrix} x^* \\ \nu^* \end{bmatrix} = \begin{bmatrix} -q \\ b \end{bmatrix}$$

**Ý nghĩa:** Hệ phương trình này cũng chính là hệ tính **bước Newton** trong bài toán tối ưu có ràng buộc đẳng thức.

### 🌊 **Ví dụ: Thuật toán Water-Filling**

#### **Bài toán**
$$\min_x -\sum_{i=1}^n \log(\alpha_i + x_i) \quad \text{s.t.} \quad x \succeq 0, \quad \mathbf{1}^T x = 1$$

với $$\alpha_i > 0$$.

#### **Điều kiện KKT**
- **Điều kiện dừng:** $$-\frac{1}{\alpha_i + x_i^*} - \lambda_i^* + \nu^* = 0$$
- **Bù yếu:** $$\lambda_i^* x_i^* = 0$$
- **Khả thi nguyên thủy:** $$x^* \succeq 0, \mathbf{1}^T x^* = 1$$
- **Khả thi đối ngẫu:** $$\lambda^* \succeq 0$$

#### **Nghiệm giải tích**
$$x_i^* = \max\left\{0, \frac{1}{\nu^*} - \alpha_i\right\}$$

với $$\nu^*$$ xác định duy nhất từ phương trình $$\sum_{i=1}^n \max\left\{0, \frac{1}{\nu^*} - \alpha_i\right\} = 1$$.

#### **Diễn giải trực quan**
- $$\alpha_i$$: Độ cao đáy của kênh thứ $$i$$.
- $$\frac{1}{\nu^*}$$: Mực nước chung.
- $$x_i^*$$: Lượng nước (công suất) phân bổ cho kênh thứ $$i$$ sao cho tổng lượng nước bằng $$1$$.

### 🎯 **Ví dụ: Máy vector hỗ trợ (SVM)**

#### **Bài toán nguyên thủy**
$$\min_{\beta,\beta_0,\xi} \frac{1}{2}\|\beta\|_2^2 + C\sum_{i=1}^n \xi_i$$
$$\text{s.t.} \quad \xi_i \ge 0, \quad y_i(x_i^T\beta + \beta_0) \ge 1 - \xi_i$$

#### **Điều kiện KKT**
- **Điều kiện dừng:**
  - $$\beta^* = \sum_{i=1}^n w_i^* y_i x_i$$
  - $$\sum_{i=1}^n w_i^* y_i = 0$$
  - $$w^* = C\mathbf{1} - v^*$$

- **Điều kiện bù yếu:**
  - $$v_i^* \xi_i^* = 0$$
  - $$w_i^* (1 - \xi_i^* - y_i(x_i^T\beta^* + \beta_0^*)) = 0$$

#### **Các vector hỗ trợ**
Điểm $$i$$ là vector hỗ trợ khi và chỉ khi $$w_i^* > 0$$, gồm hai nhóm:
- **Trên biên lề:** $$\xi_i^* = 0$$, $$w_i^* \in (0, C]$$
- **Bên trong lề hoặc phân loại sai:** $$\xi_i^* > 0$$, $$w_i^* = C$$

#### **Hệ quả thực hành**
- **Tính thưa:** Chỉ các vector hỗ trợ mới có $$w_i^* > 0$$ và tham gia vào biểu thức siêu phẳng.
- **Tính diễn giải:** Các điều kiện KKT giải thích rõ vai trò của từng điểm dữ liệu trong nghiệm SVM.

### 🔄 **Dạng ràng buộc và dạng Lagrange**

#### **Dạng ràng buộc (C)**
$$\min_x f(x) \quad \text{s.t.} \quad h(x) \le t$$

#### **Dạng Lagrange (L)**
$$\min_x f(x) + \lambda h(x)$$

#### **Điều kiện tương đương**
1. **(C) → (L):** Nếu (C) thỏa điều kiện Slater (đối ngẫu mạnh), tồn tại $$\lambda^* \ge 0$$ sao cho nghiệm của (C) cũng là nghiệm của (L).
2. **(L) → (C):** Nếu $$x^*$$ là nghiệm của (L), thì $$x^*$$ cũng là nghiệm của (C) khi đặt $$t = h(x^*)$$.

#### **Tương đương tại biên**
Khi $$h(x) \ge 0$$ (như chuẩn), $$t = 0$$ và $$\lambda = \infty$$, cả hai dạng đều áp đặt cùng một ràng buộc $$h(x) = 0$$.

### 🛠️ **Kỹ thuật thực hành**

#### **Quy trình kiểm tra điều kiện KKT**
1. Kiểm tra điều kiện dừng: $$\nabla_x L(x^*, \lambda^*, \nu^*) = 0$$ (hoặc $$0 \in \partial_x L$$).
2. Kiểm tra điều kiện bù yếu: $$\lambda_i^* h_i(x^*) = 0$$ với mọi $$i$$.
3. Kiểm tra tính khả thi nguyên thủy và đối ngẫu.
4. Kết luận tối ưu: nếu bài toán lồi và thỏa KKT thì điểm đó là nghiệm tối ưu toàn cục.

#### **Chiến lược giải bài toán giải tích**
1. Viết đầy đủ hệ điều kiện KKT cho bài toán.
2. Dùng điều kiện bù yếu để xét các trường hợp tập ràng buộc tích cực.
3. Giải hệ phương trình từ điều kiện dừng và các ràng buộc đang chặt.
4. Kiểm tra lại toàn bộ điều kiện khả thi để loại nghiệm ngoại lai.

#### **Ứng dụng trong thuật toán số**
- **Phương pháp tập tích cực (Active set):** Xác định dần tập ràng buộc chặt qua từng bước lặp.
- **Phương pháp điểm trong (Interior point):** Bám theo đường trung tâm thỏa mãn hệ KKT đã làm trơn.
- **Phương pháp nguyên thủy–đối ngẫu:** Cập nhật đồng thời biến nguyên thủy và biến đối ngẫu.

### 💡 **Ví dụ minh họa**

#### **Bài toán đơn giản**
$$\min_x x^2 + y^2 \quad \text{s.t.} \quad x + y = 1, \quad x \ge 0$$

**Điều kiện KKT:**
- **Điều kiện dừng:** $$2x^* - \lambda^* + \nu^* = 0$$, $$2y^* + \nu^* = 0$$
- **Bù yếu:** $$\lambda^* x^* = 0$$
- **Khả thi nguyên thủy:** $$x^* + y^* = 1$$, $$x^* \ge 0$$
- **Khả thi đối ngẫu:** $$\lambda^* \ge 0$$

**Phân tích trường hợp:**
- **Trường hợp 1:** $$x^* > 0 \implies \lambda^* = 0 \implies x^* = y^* = 1/2$$, $$\nu^* = -1$$ (thỏa mãn).
- **Trường hợp 2:** $$x^* = 0 \implies y^* = 1 \implies \nu^* = -2 \implies \lambda^* = -2 < 0$$ (vi phạm tính khả thi đối ngẫu, loại).

**Nghiệm tối ưu:** $$x^* = 1/2, y^* = 1/2$$, $$\nu^* = -1$$, $$\lambda^* = 0$$.

### 🎯 **Kết nối với các chương khác và ứng dụng**

- **Liên hệ lý thuyết:** Chương 11 cung cấp lý thuyết đối ngẫu tổng quát làm nền tảng cho KKT; Chương 10 là trường hợp riêng cho quy hoạch tuyến tính; Chương 04 xét điều kiện tối ưu bậc nhất không ràng buộc.
- **Lưu ý khi áp dụng:** Cần kiểm tra điều kiện chuẩn ràng buộc (LICQ, MFCQ hoặc Slater) khi dùng KKT như điều kiện cần; không nhầm lẫn rằng ràng buộc tích cực luôn có $$\lambda_i > 0$$ (vẫn có thể có $$\lambda_i = 0$$); với bài toán không lồi, KKT chỉ là điều kiện cần chứ không đủ.
- **Ứng dụng phổ biến:** Học máy (SVM, điều chuẩn, ràng buộc công bằng), kỹ thuật (điều khiển tối ưu, xử lý tín hiệu, tối ưu kết cấu), kinh tế–tài chính (tối ưu danh mục đầu tư, phân bổ nguồn lực) và vận trù học (luồng mạng, lập kế hoạch sản xuất).

---

<style>
/* Sửa lỗi alignment cho MathJax inline math */
.MathJax {
    vertical-align: baseline !important;
}

mjx-container[jax="CHTML"][display="false"] {
    vertical-align: baseline !important;
    display: inline !important;
}

/* Đảm bảo các label trong quiz có alignment tốt */
.options label {
    display: flex;
    align-items: center;
    margin: 8px 0;
    padding: 8px;
    border-radius: 4px;
    transition: background-color 0.2s;
}

.options label:hover {
    background-color: #f0f0f0;
}

.options input[type="radio"] {
    margin-right: 8px;
    flex-shrink: 0;
}

/* Styling cho quiz container */
#quiz-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.question {
    background: #f8f9fa;
    border-left: 4px solid #007bff;
    padding: 20px;
    margin: 20px 0;
    border-radius: 8px;
}

.question h3 {
    color: #2c3e50;
    margin-bottom: 15px;
}

.explanation {
    background: #e8f5e8;
    border: 1px solid #28a745;
    padding: 15px;
    margin-top: 15px;
    border-radius: 6px;
}

.quiz-controls {
    text-align: center;
    margin: 30px 0;
}

.quiz-controls button {
    background: #007bff;
    color: white;
    border: none;
    padding: 12px 24px;
    margin: 0 10px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 16px;
    transition: background-color 0.3s;
}

.quiz-controls button:hover {
    background: #0056b3;
}

.quiz-controls button:disabled {
    background: #6c757d;
    cursor: not-allowed;
}

.progress-bar {
    width: 100%;
    height: 8px;
    background: #e9ecef;
    border-radius: 4px;
    margin: 20px 0;
    overflow: hidden;
}

.progress-fill {
    height: 100%;
    background: linear-gradient(90deg, #007bff, #28a745);
    transition: width 0.3s ease;
}

.score-display {
    text-align: center;
    font-size: 18px;
    font-weight: bold;
    color: #2c3e50;
    margin: 20px 0;
}

.options label.selected {
    background-color: #e3f2fd;
    border: 2px solid #2196f3;
}

.final-score {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 30px;
    border-radius: 15px;
    text-align: center;
    margin: 30px 0;
}
</style>

Bài tập trắc nghiệm này kiểm tra mức độ nắm vững điều kiện Karush–Kuhn–Tucker (KKT) cùng các ví dụ ứng dụng như SVM, thuật toán water-filling, quy hoạch bậc hai và bài toán phạt L1.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>⚖️ Quiz: Điều Kiện KKT</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 5%"></div>
        </div>
        <div class="score-display" id="score-display">Câu hỏi: <span id="current-q">1</span> / <span id="total-q">20</span></div>
    </div>

    <div id="quiz-content">
        <!-- Câu hỏi 1: KKT conditions components -->
        <div class="question" id="q1" style="display: block;">
            <h3>Câu 1: Điều kiện KKT bao gồm những thành phần nào?</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) Chỉ stationarity và complementary slackness</label>
                <label><input type="radio" name="q1" value="b"> B) Stationarity, complementary slackness, primal feasibility, dual feasibility</label>
                <label><input type="radio" name="q1" value="c"> C) Chỉ primal và dual feasibility</label>
                <label><input type="radio" name="q1" value="d"> D) Chỉ stationarity</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Stationarity, complementary slackness, primal feasibility, dual feasibility</strong><br>
                Điều kiện KKT gồm 4 thành phần: (1) Điều kiện dừng (stationarity), (2) Điều kiện bù yếu (complementary slackness), (3) Tính khả thi nguyên thủy (primal feasibility) và (4) Tính khả thi đối ngẫu (dual feasibility).
            </div>
        </div>

        <!-- Câu hỏi 2: Stationarity condition -->
        <div class="question" id="q2" style="display: none;">
            <h3>Câu 2: Stationarity condition trong KKT có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) \(\nabla f(x^*) = 0\)</label>
                <label><input type="radio" name="q2" value="b"> B) \(\nabla f(x^*) + \sum \lambda_i \nabla h_i(x^*) + \sum \nu_j \nabla l_j(x^*) = 0\)</label>
                <label><input type="radio" name="q2" value="c"> C) \(\lambda_i h_i(x^*) = 0\)</label>
                <label><input type="radio" name="q2" value="d"> D) \(h_i(x^*) \leq 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$\nabla f(x^*) + \sum \lambda_i \nabla h_i(x^*) + \sum \nu_j \nabla l_j(x^*) = 0$$</strong><br>
                Điều kiện dừng yêu cầu gradient của hàm Lagrangian theo $$x$$ bằng 0, tức gradient của hàm mục tiêu cân bằng với tổ hợp tuyến tính các gradient của những ràng buộc.
            </div>
        </div>

        <!-- Câu hỏi 3: Complementary slackness -->
        <div class="question" id="q3" style="display: none;">
            <h3>Câu 3: Complementary slackness condition phát biểu rằng:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) \(\lambda_i h_i(x^*) = 0\) với mọi \(i\)</label>
                <label><input type="radio" name="q3" value="b"> B) \(\lambda_i = 0\) hoặc \(h_i(x^*) = 0\)</label>
                <label><input type="radio" name="q3" value="c"> C) Nếu \(h_i(x^*) < 0\) thì \(\lambda_i = 0\)</label>
                <label><input type="radio" name="q3" value="d"> D) Tất cả các điều trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các điều trên</strong><br>
                Điều kiện bù yếu có nhiều cách phát biểu tương đương: $$\lambda_i h_i(x^*) = 0$$, hoặc ít nhất một trong hai đại lượng $$\lambda_i$$ và $$h_i(x^*)$$ bằng 0, hay mọi ràng buộc không chặt đều có biến đối ngẫu bằng 0.
            </div>
        </div>

        <!-- Câu hỏi 4: KKT sufficiency -->
        <div class="question" id="q4" style="display: none;">
            <h3>Câu 4: KKT conditions là điều kiện đủ cho global optimality khi:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) Bài toán là convex</label>
                <label><input type="radio" name="q4" value="b"> B) Bài toán là non-convex</label>
                <label><input type="radio" name="q4" value="c"> C) Luôn luôn</label>
                <label><input type="radio" name="q4" value="d"> D) Không bao giờ</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Bài toán là convex</strong><br>
                Điều kiện KKT là điều kiện cần (khi có điều kiện chuẩn ràng buộc) cho mọi bài toán, nhưng chỉ là điều kiện đủ cho cực tiểu toàn cục khi bài toán là bài toán lồi.
            </div>
        </div>

        <!-- Câu hỏi 5: Active constraints -->
        <div class="question" id="q5" style="display: none;">
            <h3>Câu 5: Constraint \(h_i(x) \leq 0\) được gọi là active tại \(x^*\) khi:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) \(h_i(x^*) < 0\)</label>
                <label><input type="radio" name="q5" value="b"> B) \(h_i(x^*) = 0\)</label>
                <label><input type="radio" name="q5" value="c"> C) \(\lambda_i > 0\)</label>
                <label><input type="radio" name="q5" value="d"> D) \(\lambda_i = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$h_i(x^*) = 0$$</strong><br>
                Một ràng buộc bất đẳng thức được gọi là tích cực (active) khi nó đạt dấu bằng tại điểm tối ưu.
            </div>
        </div>

        <!-- Câu hỏi 6: Quadratic programming KKT -->
        <div class="question" id="q6" style="display: none;">
            <h3>Câu 6: Trong quadratic programming \(\min \frac{1}{2}x^T Q x + c^T x\) s.t. \(Ax = b\), stationarity condition là:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) \(Qx^* + c = 0\)</label>
                <label><input type="radio" name="q6" value="b"> B) \(Qx^* + c + A^T \nu^* = 0\)</label>
                <label><input type="radio" name="q6" value="c"> C) \(Ax^* = b\)</label>
                <label><input type="radio" name="q6" value="d"> D) \(\nu^* = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$Qx^* + c + A^T \nu^* = 0$$</strong><br>
                Stationarity: $$\nabla f(x^*) + A^T \nu^* = Qx^* + c + A^T \nu^* = 0$$.
            </div>
        </div>

        <!-- Câu hỏi 7: Water-filling problem -->
        <div class="question" id="q7" style="display: none;">
            <h3>Câu 7: Trong water-filling algorithm, bài toán tối ưu có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) \(\max \sum \log(\alpha_i + x_i)\) s.t. \(\sum x_i = P, x_i \geq 0\)</label>
                <label><input type="radio" name="q7" value="b"> B) \(\min \sum \log(\alpha_i + x_i)\) s.t. \(\sum x_i = P, x_i \geq 0\)</label>
                <label><input type="radio" name="q7" value="c"> C) \(\max \sum x_i^2\) s.t. \(\sum x_i = P\)</label>
                <label><input type="radio" name="q7" value="d"> D) \(\min \sum x_i^2\) s.t. \(\sum x_i = P\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\max \sum \log(\alpha_i + x_i)$$ s.t. $$\sum x_i = P, x_i \geq 0$$</strong><br>
                Thuật toán water-filling cực đại hóa tổng dung lượng logarit của các kênh dưới ràng buộc tổng công suất cố định và công suất không âm.
            </div>
        </div>

        <!-- Câu hỏi 8: Water-filling solution -->
        <div class="question" id="q8" style="display: none;">
            <h3>Câu 8: Nghiệm của water-filling algorithm có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) \(x_i^* = \max(0, \mu - \alpha_i)\)</label>
                <label><input type="radio" name="q8" value="b"> B) \(x_i^* = \max(0, \alpha_i - \mu)\)</label>
                <label><input type="radio" name="q8" value="c"> C) \(x_i^* = \mu - \alpha_i\)</label>
                <label><input type="radio" name="q8" value="d"> D) \(x_i^* = \alpha_i + \mu\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$x_i^* = \max(0, \mu - \alpha_i)$$</strong><br>
                Nghiệm water-filling phân bổ công suất $$\mu - \alpha_i$$ cho kênh $$i$$ nếu $$\mu > \alpha_i$$, ngược lại phân bổ bằng 0.
            </div>
        </div>

        <!-- Câu hỏi 9: SVM primal problem -->
        <div class="question" id="q9" style="display: none;">
            <h3>Câu 9: SVM primal problem có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) \(\min \frac{1}{2}\|w\|^2\) s.t. \(y_i(w^T x_i + b) \geq 1\)</label>
                <label><input type="radio" name="q9" value="b"> B) \(\max \frac{1}{2}\|w\|^2\) s.t. \(y_i(w^T x_i + b) \geq 1\)</label>
                <label><input type="radio" name="q9" value="c"> C) \(\min \sum \alpha_i\) s.t. \(\sum \alpha_i y_i = 0\)</label>
                <label><input type="radio" name="q9" value="d"> D) \(\max \sum \alpha_i\) s.t. \(\sum \alpha_i y_i = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\min \frac{1}{2}\|w\|^2$$ s.t. $$y_i(w^T x_i + b) \geq 1$$</strong><br>
                Bài toán SVM nguyên thủy cực tiểu hóa $$\frac{1}{2}\|w\|^2$$ (tương đương cực đại hóa độ rộng lề $$2/\|w\|$$) dưới các ràng buộc phân loại đúng.
            </div>
        </div>

        <!-- Câu hỏi 10: SVM dual problem -->
        <div class="question" id="q10" style="display: none;">
            <h3>Câu 10: SVM dual problem có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) \(\min \sum \alpha_i - \frac{1}{2}\sum \alpha_i \alpha_j y_i y_j x_i^T x_j\)</label>
                <label><input type="radio" name="q10" value="b"> B) \(\max \sum \alpha_i - \frac{1}{2}\sum \alpha_i \alpha_j y_i y_j x_i^T x_j\)</label>
                <label><input type="radio" name="q10" value="c"> C) \(\min \frac{1}{2}\|w\|^2 + C\sum \xi_i\)</label>
                <label><input type="radio" name="q10" value="d"> D) \(\max \frac{1}{2}\|w\|^2\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$\max \sum \alpha_i - \frac{1}{2}\sum \alpha_i \alpha_j y_i y_j x_i^T x_j$$</strong><br>
                Bài toán SVM đối ngẫu cực đại hóa hiệu giữa số hạng tuyến tính và số hạng bậc hai dưới ràng buộc $$\sum \alpha_i y_i = 0$$ và $$\alpha_i \geq 0$$.
            </div>
        </div>

        <!-- Câu hỏi 11: Support vectors -->
        <div class="question" id="q11" style="display: none;">
            <h3>Câu 11: Support vectors trong SVM là những điểm có:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) \(\alpha_i = 0\)</label>
                <label><input type="radio" name="q11" value="b"> B) \(\alpha_i > 0\)</label>
                <label><input type="radio" name="q11" value="c"> C) \(y_i(w^T x_i + b) > 1\)</label>
                <label><input type="radio" name="q11" value="d"> D) \(y_i(w^T x_i + b) < 1\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$\alpha_i > 0$$</strong><br>
                Các vector hỗ trợ có nhân tử đối ngẫu $$\alpha_i > 0$$ và (trong Hard-Margin SVM) nằm đúng trên biên lề: $$y_i(w^T x_i + b) = 1$$.
            </div>
        </div>

        <!-- Câu hỏi 12: LICQ condition -->
        <div class="question" id="q12" style="display: none;">
            <h3>Câu 12: Linear Independence Constraint Qualification (LICQ) yêu cầu:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) Tất cả constraints đều active</label>
                <label><input type="radio" name="q12" value="b"> B) Gradients của active constraints độc lập tuyến tính</label>
                <label><input type="radio" name="q12" value="c"> C) Tất cả constraints đều inactive</label>
                <label><input type="radio" name="q12" value="d"> D) Objective function khả vi</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Gradients của active constraints độc lập tuyến tính</strong><br>
                LICQ yêu cầu các gradient của những ràng buộc tích cực tại điểm tối ưu độc lập tuyến tính, qua đó đảm bảo điều kiện KKT là điều kiện cần.
            </div>
        </div>

        <!-- Câu hỏi 13: L1 penalized problem -->
        <div class="question" id="q13" style="display: none;">
            <h3>Câu 13: Trong L1 penalized problem \(\min f(x) + \lambda\|x\|_1\), điều kiện KKT cho thành phần \(x_i\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) \(\frac{\partial f}{\partial x_i} + \lambda \text{sign}(x_i) = 0\) nếu \(x_i \neq 0\)</label>
                <label><input type="radio" name="q13" value="b"> B) \(\frac{\partial f}{\partial x_i} + \lambda = 0\)</label>
                <label><input type="radio" name="q13" value="c"> C) \(\frac{\partial f}{\partial x_i} = 0\)</label>
                <label><input type="radio" name="q13" value="d"> D) \(x_i = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\frac{\partial f}{\partial x_i} + \lambda \text{sign}(x_i) = 0$$ nếu $$x_i \neq 0$$</strong><br>
                Khi $$x_i \neq 0$$, subgradient của $$|x_i|$$ là $$\text{sign}(x_i)$$. Khi $$x_i = 0$$, subgradient là $$[-1,1]$$.
            </div>
        </div>

        <!-- Câu hỏi 14: Uniqueness in L1 -->
        <div class="question" id="q14" style="display: none;">
            <h3>Câu 14: Trong L1 regularization, nghiệm duy nhất khi:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) \(f\) là strictly convex</label>
                <label><input type="radio" name="q14" value="b"> B) \(\lambda > 0\) bất kỳ</label>
                <label><input type="radio" name="q14" value="c"> C) Active set được xác định duy nhất</label>
                <label><input type="radio" name="q14" value="d"> D) Tất cả các điều trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f$$ là strictly convex</strong><br>
                Tính lồi chặt của $$f$$ đảm bảo bài toán có nghiệm duy nhất, ngay cả khi thành phần phạt L1 chỉ lồi chứ không lồi chặt.
            </div>
        </div>

        <!-- Câu hỏi 15: KKT matrix system -->
        <div class="question" id="q15" style="display: none;">
            <h3>Câu 15: Hệ phương trình KKT cho equality constrained QP có thể viết dưới dạng ma trận:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) \(\begin{bmatrix} Q & A^T \\ A & 0 \end{bmatrix} \begin{bmatrix} x \\ \nu \end{bmatrix} = \begin{bmatrix} -c \\ b \end{bmatrix}\)</label>
                <label><input type="radio" name="q15" value="b"> B) \(\begin{bmatrix} Q & A \\ A^T & 0 \end{bmatrix} \begin{bmatrix} x \\ \nu \end{bmatrix} = \begin{bmatrix} -c \\ b \end{bmatrix}\)</label>
                <label><input type="radio" name="q15" value="c"> C) \(Qx = -c\)</label>
                <label><input type="radio" name="q15" value="d"> D) \(Ax = b\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\begin{bmatrix} Q & A^T \\ A & 0 \end{bmatrix} \begin{bmatrix} x \\ \nu \end{bmatrix} = \begin{bmatrix} -c \\ b \end{bmatrix}$$</strong><br>
                KKT system kết hợp stationarity $$Qx + c + A^T\nu = 0$$ và feasibility $$Ax = b$$.
            </div>
        </div>

        <!-- Câu hỏi 16: Constraint qualification -->
        <div class="question" id="q16" style="display: none;">
            <h3>Câu 16: Constraint qualification cần thiết để:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) Đảm bảo KKT conditions sufficient</label>
                <label><input type="radio" name="q16" value="b"> B) Đảm bảo KKT conditions necessary</label>
                <label><input type="radio" name="q16" value="c"> C) Đảm bảo hàm mục tiêu khả vi</label>
                <label><input type="radio" name="q16" value="d"> D) Đảm bảo convexity</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Đảm bảo KKT conditions necessary</strong><br>
                Điều kiện chuẩn ràng buộc (như LICQ, MFCQ) đảm bảo điều kiện KKT là điều kiện cần cho cực tiểu địa phương.
            </div>
        </div>

        <!-- Câu hỏi 17: Second-order conditions -->
        <div class="question" id="q17" style="display: none;">
            <h3>Câu 17: Second-order sufficient condition yêu cầu Hessian của Lagrangian:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Positive definite trên toàn không gian</label>
                <label><input type="radio" name="q17" value="b"> B) Positive definite trên tangent space của active constraints</label>
                <label><input type="radio" name="q17" value="c"> C) Negative definite</label>
                <label><input type="radio" name="q17" value="d"> D) Singular</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Positive definite trên tangent space của active constraints</strong><br>
                Điều kiện đủ bậc hai (SOSC) yêu cầu ma trận Hessian của hàm Lagrangian xác định dương trên không gian tiếp tuyến của các ràng buộc tích cực, đảm bảo điểm đang xét là cực tiểu địa phương chặt.
            </div>
        </div>

        <!-- Câu hỏi 18: Penalty method connection -->
        <div class="question" id="q18" style="display: none;">
            <h3>Câu 18: Mối liên hệ giữa KKT multipliers và penalty methods:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) Ước lượng multiplier của penalty method hội tụ đến KKT multipliers</label>
                <label><input type="radio" name="q18" value="b"> B) Penalty parameters là giới hạn của KKT multipliers</label>
                <label><input type="radio" name="q18" value="c"> C) Không có mối liên hệ</label>
                <label><input type="radio" name="q18" value="d"> D) Chúng luôn bằng nhau</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Ước lượng multiplier của penalty method hội tụ đến KKT multipliers</strong><br>
                Khi tham số phạt tiến ra vô cùng, nghiệm của bài toán phạt hội tụ về nghiệm tối ưu gốc và các đại lượng ước lượng nhân tử hội tụ về nhân tử KKT.
            </div>
        </div>

        <!-- Câu hỏi 19: Sensitivity analysis -->
        <div class="question" id="q19" style="display: none;">
            <h3>Câu 19: KKT multipliers cung cấp thông tin về:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) Sensitivity của optimal value đối với thay đổi constraints</label>
                <label><input type="radio" name="q19" value="b"> B) Tốc độ hội tụ của algorithm</label>
                <label><input type="radio" name="q19" value="c"> C) Condition number của problem</label>
                <label><input type="radio" name="q19" value="d"> D) Số lượng iterations cần thiết</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Sensitivity của optimal value đối với thay đổi constraints</strong><br>
                Các nhân tử KKT đóng vai trò giá bóng (shadow price), phản ánh tốc độ thay đổi của giá trị tối ưu khi nới lỏng hoặc siết chặt các ràng buộc.
            </div>
        </div>

        <!-- Câu hỏi 20: Practical applications -->
        <div class="question" id="q20" style="display: none;">
            <h3>Câu 20: KKT conditions được ứng dụng trong:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Machine learning (SVM, neural networks)</label>
                <label><input type="radio" name="q20" value="b"> B) Signal processing (water-filling, beamforming)</label>
                <label><input type="radio" name="q20" value="c"> C) Economics (utility maximization, portfolio optimization)</label>
                <label><input type="radio" name="q20" value="d"> D) Tất cả các lĩnh vực trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các lĩnh vực trên</strong><br>
                Điều kiện KKT là công cụ nền tảng của tối ưu hóa có ràng buộc, được ứng dụng rộng rãi trong học máy, xử lý tín hiệu, kinh tế học và nhiều ngành kỹ thuật khác.
            </div>
        </div>
        <!-- Câu hỏi 21: Thực hành -->
        <div class="question" id="q21" style="display: none;">
            <h3>Câu 21: Điều kiện KKT bao gồm:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) Stationarity, primal feasibility, dual feasibility, complementary slackness</label>
                <label><input type="radio" name="q21" value="b"> B) Chỉ stationarity</label>
                <label><input type="radio" name="q21" value="c"> C) Chỉ feasibility</label>
                <label><input type="radio" name="q21" value="d"> D) Chỉ complementary slackness</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Stationarity, primal feasibility, dual feasibility, complementary slackness</strong><br>
                KKT gồm 4 điều kiện: $$\nabla f + \sum \lambda_i \nabla g_i + \sum \nu_j \nabla h_j = 0$$, $$g_i(x) \leq 0$$, $$\lambda_i \geq 0$$, $$\lambda_i g_i(x) = 0$$.
            </div>
        </div>

        <!-- Câu hỏi 22: Thực hành -->
        <div class="question" id="q22" style="display: none;">
            <h3>Câu 22: Điều kiện complementary slackness có nghĩa:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) $$\lambda_i g_i(x) = 0$$ cho mọi $$i$$</label>
                <label><input type="radio" name="q22" value="b"> B) $$\lambda_i + g_i(x) = 0$$</label>
                <label><input type="radio" name="q22" value="c"> C) $$\lambda_i = g_i(x)$$</label>
                <label><input type="radio" name="q22" value="d"> D) $$\lambda_i \cdot g_i(x) = 1$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\lambda_i g_i(x) = 0$$ cho mọi $$i$$</strong><br>
                Complementary slackness: hoặc $$\lambda_i = 0$$ hoặc $$g_i(x) = 0$$ (ràng buộc tích cực).
            </div>
        </div>

        <!-- Câu hỏi 23: Thực hành -->
        <div class="question" id="q23" style="display: none;">
            <h3>Câu 23: Cho bài toán $$\min x^2$$ với $$x \geq 1$$. Điều kiện KKT tại nghiệm $$x^* = 1$$:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) $$2x - \lambda = 0, \lambda \geq 0, \lambda(1-x) = 0$$</label>
                <label><input type="radio" name="q23" value="b"> B) $$2x = 0$$</label>
                <label><input type="radio" name="q23" value="c"> C) $$x = 1$$</label>
                <label><input type="radio" name="q23" value="d"> D) $$\lambda = 1$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$2x - \lambda = 0, \lambda \geq 0, \lambda(1-x) = 0$$</strong><br>
                Stationarity: $$2x - \lambda = 0$$. Tại $$x^* = 1$$: $$\lambda = 2$$, thỏa mãn complementary slackness.
            </div>
        </div>

        <!-- Câu hỏi 24: Thực hành -->
        <div class="question" id="q24" style="display: none;">
            <h3>Câu 24: LICQ (Linear Independence Constraint Qualification) yêu cầu:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) Gradient của các ràng buộc tích cực độc lập tuyến tính</label>
                <label><input type="radio" name="q24" value="b"> B) Tất cả ràng buộc tuyến tính</label>
                <label><input type="radio" name="q24" value="c"> C) Hàm mục tiêu tuyến tính</label>
                <label><input type="radio" name="q24" value="d"> D) Ma trận Hessian khả nghịch</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Gradient của các ràng buộc tích cực độc lập tuyến tính</strong><br>
                LICQ: các gradient $$\nabla g_i(x^*), \nabla h_j(x^*)$$ của ràng buộc tích cực phải độc lập tuyến tính.
            </div>
        </div>

        <!-- Câu hỏi 25: Thực hành -->
        <div class="question" id="q25" style="display: none;">
            <h3>Câu 25: Trong bài toán QP với KKT, ma trận hệ phương trình có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) $$\begin{pmatrix} H & A^T \\ A & 0 \end{pmatrix}$$</label>
                <label><input type="radio" name="q25" value="b"> B) $$\begin{pmatrix} H & 0 \\ 0 & A \end{pmatrix}$$</label>
                <label><input type="radio" name="q25" value="c"> C) $$H + A^T A$$</label>
                <label><input type="radio" name="q25" value="d"> D) $$H - A^T A$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\begin{pmatrix} H & A^T \\ A & 0 \end{pmatrix}$$</strong><br>
                Hệ KKT cho QP có dạng ma trận khối với Hessian $$H$$ và ma trận ràng buộc $$A$$.
            </div>
        </div>

    </div>

    <div class="quiz-controls">
        <button onclick="previousQuestion()" id="prev-btn" disabled>← Câu trước</button>
        <button onclick="nextQuestion()" id="next-btn">Câu tiếp →</button>
        <button onclick="submitQuiz()" id="submit-btn" style="display: none;">Nộp bài</button>
        <button onclick="resetQuiz()" id="reset-btn" style="display: none;">Làm lại</button>
    </div>

    <div id="final-result" style="display: none;" class="final-score">
        <h2>🎉 Hoàn thành Quiz!</h2>
        <p>Điểm số của bạn: <span id="final-score-text"></span></p>
        <p id="performance-message"></p>
    </div>
</div>

<script>
let currentQuestion = 1;
const totalQuestions = 25;
let userAnswers = {};
let quizSubmitted = false;

// Đáp án đúng
const correctAnswers = {
    q1: 'b', q2: 'b', q3: 'd', q4: 'a', q5: 'b',
    q6: 'b', q7: 'a', q8: 'a', q9: 'a', q10: 'b',
    q11: 'b', q12: 'b', q13: 'a', q14: 'a', q15: 'a',
    q16: 'b', q17: 'b', q18: 'a', q19: 'a', q20: 'd'
,
    q21: 'a', q22: 'a', q23: 'a', q24: 'a', q25: 'a'};

function showQuestion(n) {
    // Ẩn tất cả câu hỏi
    for (let i = 1; i <= totalQuestions; i++) {
        document.getElementById(`q${i}`).style.display = 'none';
    }
    
    // Hiển thị câu hỏi hiện tại
    document.getElementById(`q${n}`).style.display = 'block';
    
    // Cập nhật progress bar
    const progress = (n / totalQuestions) * 100;
    document.getElementById('progress-fill').style.width = progress + '%';
    
    // Cập nhật số câu hỏi
    document.getElementById('current-q').textContent = n;
    
    // Cập nhật nút điều hướng
    document.getElementById('prev-btn').disabled = (n === 1);
    document.getElementById('next-btn').style.display = (n === totalQuestions) ? 'none' : 'inline-block';
    document.getElementById('submit-btn').style.display = (n === totalQuestions) ? 'inline-block' : 'none';
    
    currentQuestion = n;
}

function nextQuestion() {
    if (currentQuestion < totalQuestions) {
        showQuestion(currentQuestion + 1);
    }
}

function previousQuestion() {
    if (currentQuestion > 1) {
        showQuestion(currentQuestion - 1);
    }
}

function saveAnswer(questionId, answer) {
    userAnswers[questionId] = answer;
    
    // Highlight selected option
    const questionDiv = document.getElementById(questionId);
    const labels = questionDiv.querySelectorAll('.options label');
    labels.forEach(label => {
        label.classList.remove('selected');
        const input = label.querySelector('input[type="radio"]');
        if (input.checked) {
            label.classList.add('selected');
        }
    });
}

function calculateScore() {
    let correct = 0;
    for (let q in correctAnswers) {
        if (userAnswers[q] === correctAnswers[q]) {
            correct++;
        }
    }
    return correct;
}

function submitQuiz() {
    quizSubmitted = true;
    const score = calculateScore();
    const percentage = Math.round((score / totalQuestions) * 100);
    
    // Hiển thị tất cả giải thích
    for (let i = 1; i <= totalQuestions; i++) {
        const explanation = document.querySelector(`#q${i} .explanation`);
        explanation.style.display = 'block';
        
        // Highlight đáp án đúng và sai
        const questionDiv = document.getElementById(`q${i}`);
        const labels = questionDiv.querySelectorAll('.options label');
        labels.forEach(label => {
            const input = label.querySelector('input[type="radio"]');
            const value = input.value;
            
            if (value === correctAnswers[`q${i}`]) {
                label.style.backgroundColor = '#d4edda';
                label.style.border = '2px solid #28a745';
            } else if (value === userAnswers[`q${i}`] && value !== correctAnswers[`q${i}`]) {
                label.style.backgroundColor = '#f8d7da';
                label.style.border = '2px solid #dc3545';
            }
        });
    }
    
    // Hiển thị kết quả cuối
    document.getElementById('final-result').style.display = 'block';
    document.getElementById('final-score-text').textContent = `${score}/${totalQuestions} (${percentage}%)`;
    
    let message = '';
    if (percentage >= 90) {
        message = '🌟 Xuất sắc! Bạn đã thành thạo KKT conditions và applications!';
    } else if (percentage >= 80) {
        message = '👍 Rất tốt! Bạn hiểu tốt về optimality conditions và practical examples.';
    } else if (percentage >= 70) {
        message = '📚 Khá ổn! Hãy xem lại complementary slackness và constraint qualification.';
    } else if (percentage >= 60) {
        message = '💪 Cần cải thiện! Ôn lại KKT conditions và stationarity.';
    } else {
        message = '📖 Hãy học lại từ đầu về KKT theory nhé!';
    }
    
    document.getElementById('performance-message').textContent = message;
    
    // Ẩn nút submit, hiện nút reset
    document.getElementById('submit-btn').style.display = 'none';
    document.getElementById('reset-btn').style.display = 'inline-block';
    
    // Cuộn đến kết quả
    document.getElementById('final-result').scrollIntoView({ behavior: 'smooth' });
}

function resetQuiz() {
    // Reset trạng thái
    currentQuestion = 1;
    userAnswers = {};
    quizSubmitted = false;
    
    // Ẩn tất cả giải thích
    document.querySelectorAll('.explanation').forEach(exp => {
        exp.style.display = 'none';
    });
    
    // Reset style của labels
    document.querySelectorAll('.options label').forEach(label => {
        label.style.backgroundColor = '';
        label.style.border = '';
        label.classList.remove('selected');
    });
    
    // Uncheck tất cả radio buttons
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
    
    // Ẩn kết quả cuối và reset button
    document.getElementById('final-result').style.display = 'none';
    document.getElementById('reset-btn').style.display = 'none';
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
