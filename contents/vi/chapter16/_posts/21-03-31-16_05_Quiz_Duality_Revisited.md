---
layout: post
title: 16-05 Bài tập trắc nghiệm - Tính Đối Ngẫu Tái Xét
chapter: '16'
order: 6
owner: GitHub Copilot
lang: vi
categories:
- chapter16
lesson_type: quiz
redirect_from:
  - /contents/vi/chapter16/16_04_Quiz_Duality_Revisited/
---

Chương 16 tổng hợp những khái niệm sắc nét nhất của toàn bộ lý thuyết đối ngẫu — từ biểu diễn minimax, điều kiện Slater tinh chỉnh, đối chiếu KKT với đường trung tâm LP, đến đối ngẫu Fenchel cho quy hoạch nón. Cũng chính vì tính cô đọng cao nên các câu hỏi trắc nghiệm chương này thường kiểm tra rất kỹ **các điều kiện biên**: khi nào không cần khả thi chặt? Dấu trừ trong đối ngẫu Fenchel nằm ở đâu? Liên hợp của hàm chỉ thị nón $$K$$ là $$I_{K^*}$$ hay $$I_{-K^*}$$?

Hãy dành hai phút rà lại bản đồ bốn điểm phân biệt dễ nhầm trước khi bước vào bộ câu hỏi trắc nghiệm.

## Kiến thức cần nhớ: Bốn điểm phân biệt sắc bén cho trắc nghiệm Chương 16

- **Slater gốc vs. Slater tinh chỉnh:** Slater gốc đòi mọi bất đẳng thức $$h_i(x) < 0$$; Slater tinh chỉnh **miễn** dấu chặt cho các ràng buộc tuyến tính/affine (chỉ cần $$\le 0$$), nên LP khả thi bị chặn luôn có đối ngẫu mạnh.
- **Điều kiện bù yếu KKT vs. Đường trung tâm:** Trong LP dạng chuẩn, KKT đòi $$x_i s_i = 0$$ (nằm trên biên), còn đường trung tâm đòi $$x_i s_i = \mu = 1/t > 0$$ (nằm trong miền trong, tổng khoảng cách đối ngẫu $$x^T s = n\mu$$).
- **Quy ước dấu trong Đối ngẫu Fenchel:** Với $$\min_x f(x) + g(Ax)$$, đối ngẫu Fenchel là $$\max_u -f^*(-A^T u) - g^*(u)$$ (hoặc $$\max_y -f^*(A^T y) - g^*(-y)$$). Luôn kiểm tra tính đối xứng: hai đối số của $$f^*$$ và $$g^*$$ phải ngược dấu nhau qua $$A^T$$!
- **Liên hợp của hàm chỉ thị nón:** Với nón $$K$$, $$I_K^*(z) = \sup_{x \in K} z^T x$$ bằng $$0$$ khi $$z^T x \le 0 \;\forall x \in K$$ (tức $$-z \in K^*$$) và $$+\infty$$ ngược lại — do đó $$I_K^*(z) = I_{-K^*}(z) = I_{K^*}(-z)$$!

### Giải thích: Giải mẫu câu hỏi bẫy về dấu trừ trong liên hợp của hàm chỉ thị nón $$I_K^*(z)$$

**Câu hỏi mẫu:** Cho nón không âm 1 chiều $$K = \mathbb{R}_+ = [0, +\infty)$$ (tự đối ngẫu: $$K^* = [0, +\infty)$$). Tính $$I_K^*(z)$$ tại $$z = 2$$ và $$z = -2$$ để tránh nhầm giữa $$I_{K^*}(z)$$ và $$I_{-K^*}(z)$$.

1. **Áp dụng định nghĩa hàm liên hợp:**
   $$I_K^*(z) = \sup_{x \ge 0} \bigl(z \cdot x - 0\bigr) = \sup_{x \ge 0} (zx).$$
2. **Thử $$z = 2 \in K^*$$:**
   Khi cho $$x \to +\infty$$, tích $$2x \to +\infty \implies I_K^*(2) = +\infty$$!
   (Nếu ai nhầm $$I_K^* = I_{K^*}$$ thì sẽ tưởng bằng $$0$$ — sai hoàn toàn!)
3. **Thử $$z = -2 \in -K^*$$:**
   Với mọi $$x \ge 0$$, tích $$-2x \le 0$$, và đạt cực đại bằng $$0$$ tại $$x = 0 \implies I_K^*(-2) = 0$$!
4. **Kết luận chắc chắn:** $$I_K^*(z) = 0 \iff z \in -K^* \iff -z \in K^*$$. Một phép thử 5 giây với số $$2$$ và $$-2$$ đủ để không bao giờ nhầm dấu trong các bài đối ngẫu nón!

---

## 📚 Ôn tập lý thuyết

Trước khi làm bài tập, hãy ôn lại các khái niệm chính trong chương này:

### ⚡ **Nhìn lại tính đối ngẫu (Duality Revisited)**

#### **Biểu diễn bài toán nguyên thủy – đối ngẫu qua hàm Lagrange**
**Bài toán nguyên thủy:**
$$\min_x f(x) \quad \text{s.t.} \quad h_i(x) \le 0, \quad l_j(x) = 0$$

**Hàm Lagrange:**
$$L(x,u,v) = f(x) + \sum_{i=1}^m u_i h_i(x) + \sum_{j=1}^r v_j l_j(x)$$

#### **Dạng viết lại nguyên thủy – đối ngẫu**
**Bài toán nguyên thủy:**
$$\min_x \max_{u \ge 0, v} L(x,u,v)$$

**Bài toán đối ngẫu:**
$$\max_{u \ge 0, v} \min_x L(x,u,v)$$

#### **Cách hiểu theo hàm chỉ thị**
- **Bài toán nguyên thủy:** Phép lấy $$\max_{u \ge 0, v}$$ đóng vai trò như hàm chỉ thị, phạt vô hạn mọi điểm $$x$$ vi phạm ràng buộc.
- **Bài toán đối ngẫu:** Phép lấy $$\min_x$$ với $$(u, v)$$ cố định giúp nới lỏng miền ràng buộc.
- **Tính tương đương:** Dạng viết lại nguyên thủy tương đương với bài toán gốc trên tập khả thi.

### 🔄 **Tính đối ngẫu yếu và mạnh (Tinh chỉnh)**

#### **Định lý đối ngẫu yếu**
Bất đẳng thức sau luôn đúng (không phụ thuộc tính lồi): $$p \ge d$$ (giá trị tối ưu nguyên thủy luôn lớn hơn hoặc bằng giá trị tối ưu đối ngẫu).

<div class="textbook-proof" markdown="1">
**Chứng minh:** Từ bất đẳng thức minimax:
$$\min_x \max_{u \ge 0, v} L(x,u,v) \ge \max_{u \ge 0, v} \min_x L(x,u,v)$$
</div>

#### **Tính đối ngẫu mạnh (Điều kiện Slater tinh chỉnh)**
**Điều kiện:** Trên miền xác định $$D$$, giả sử $$f, h_1,\ldots,h_p$$ là các hàm lồi và $$h_{p+1},\ldots,h_m, l_1,\ldots,l_r$$ là các hàm affine.

**Nếu tồn tại $$\hat{x} \in \text{relint}(D)$$ thỏa mãn:**
- $$h_i(\hat{x}) < 0, \quad i = 1,\ldots,p$$ (bất đẳng thức ngặt cho ràng buộc không affine)
- $$h_i(\hat{x}) \le 0, \quad i = p+1,\ldots,m$$ (bất đẳng thức không ngặt cho ràng buộc affine)
- $$l_j(\hat{x}) = 0, \quad j = 1,\ldots,r$$ (ràng buộc đẳng thức)

**Thì:** $$p = d$$ (tính đối ngẫu mạnh được thỏa mãn).

### 📊 **Các ví dụ đối ngẫu tiêu biểu**

#### **1. Đối ngẫu quy hoạch tuyến tính (LP)**

**Bài toán nguyên thủy (dạng chuẩn):**
$$\min c^T x \quad \text{s.t.} \quad Ax = b, \quad x \ge 0$$

**Hàm Lagrange:**
$$L(x,s,y) = c^T x - s^T x + (b - Ax)^T y$$

**Điều kiện dừng:** $$\nabla_x L = c - s - A^T y = 0 \Rightarrow c = A^T y + s$$

**Bài toán đối ngẫu:**
$$\max b^T y \quad \text{s.t.} \quad A^T y + s = c, \quad s \ge 0$$

#### **2. Đối ngẫu quy hoạch bậc hai (QP)**

**Bài toán nguyên thủy:**
$$\min \frac{1}{2}x^T Q x + c^T x \quad \text{s.t.} \quad Ax = b, \quad x \ge 0$$

với $$Q$$ là ma trận đối xứng nửa xác định dương.

**Hàm Lagrange:**
$$L(x,s,y) = \frac{1}{2}x^T Q x + c^T x - s^T x + (b - Ax)^T y$$

**Điều kiện dừng:** $$Qx + c - s - A^T y = 0 \Rightarrow Qx = A^T y + s - c$$

**Bài toán đối ngẫu:**
$$\max b^T y - \frac{1}{2}x^T Q x \quad \text{s.t.} \quad Qx = A^T y + s - c, \quad s \ge 0$$

**Nhận xét:** Bài toán đối ngẫu của một bài toán QP cũng là một bài toán QP.

#### **3. Đối ngẫu của bài toán rào cản (Barrier)**

**Bài toán rào cản nguyên thủy cho LP:**
$$\min c^T x - \tau \sum_{i=1}^n \log(x_i) \quad \text{s.t.} \quad Ax = b$$

**Hàm Lagrange:**
$$L(x,y) = c^T x - \tau \sum_{i=1}^n \log(x_i) + (b - Ax)^T y$$

**Nghiệm tối ưu theo $$x$$:** $$x_i = \frac{\tau}{s_i}$$ với $$s = c - A^T y$$.

**Bài toán đối ngẫu:**
$$\max b^T y + \tau \sum_{i=1}^n \log(s_i) \quad \text{s.t.} \quad A^T y + s = c$$ (bỏ qua hằng số $$n\tau(1 - \log\tau)$$)

**Kết quả:** Đối ngẫu của bài toán rào cản trùng khớp với bài toán rào cản thiết lập cho bài toán đối ngẫu.

### 🎯 **So sánh điều kiện tối ưu**

#### **Điều kiện KKT của bài toán gốc**
$$\begin{align}
l_j(x^*) &= 0 \quad \forall j \\
u_i^*, -h_i(x^*) &\ge 0 \quad \forall i \\
u_i^* h_i(x^*) &= 0 \quad \forall i \\
\nabla f(x^*) + \sum u_i^* \nabla h_i(x^*) + \sum v_j^* \nabla l_j(x^*) &= 0
\end{align}$$

#### **Điều kiện KKT bị nhiễu (bài toán rào cản)**
$$\begin{align}
l_j(x^*(t)) &= 0 \quad \forall j \\
u_i(t), -h_i(x^*(t)) &> 0 \quad \forall i \\
u_i(t) h_i(x^*(t)) &= -\tau \quad \forall i \\
\nabla f(x^*(t)) + \sum u_i(t) \nabla h_i(x^*(t)) + \sum \hat{v}_j^* \nabla l_j(x^*(t)) &= 0
\end{align}$$

với $$\tau = \frac{1}{t}$$, $$u_i(t) = -\frac{1}{t h_i(x^*(t))}$$, $$\hat{v} = \frac{1}{t}v$$.

#### **Điểm khác biệt chính:**
- **Điều kiện bù chặt:** Chuyển từ $$= 0$$ sang $$= -\tau$$.
- **Tính khả thi:** Chuyển từ $$\ge 0$$ sang $$> 0$$ (điểm trong ngặt).
- **Ý nghĩa:** Khi $$\tau \to 0$$, nghiệm trên đường trung tâm tiến về nghiệm KKT chính xác của bài toán gốc.

### 📈 **Trường hợp đặc biệt: Quy hoạch tuyến tính (LP)**

#### **Điều kiện tối ưu nguyên thủy – đối ngẫu**
$$\begin{align}
A^T y^* + s^* &= c \\
Ax^* &= b \\
X S \mathbf{1} &= 0 \\
x^*, s^* &\ge 0
\end{align}$$

với $$X = \text{diag}(x^*)$$, $$S = \text{diag}(s^*)$$.

#### **Điều kiện của bài toán rào cản**
$$\begin{align}
A^T y^* + s^* &= c \\
Ax^* &= b \\
X S \mathbf{1} &= \tau \mathbf{1} \\
x^*, s^* &> 0
\end{align}$$

#### **Ý nghĩa về mặt thuật toán:**
- **Phương pháp đơn hình (Simplex nguyên thủy):** Duy trì điều kiện 2, 3 và $$x \ge 0$$, đồng thời tiến dần tới điều kiện 1 với $$s \ge 0$$ (khả thi đối ngẫu).
- **Phương pháp điểm trong (Interior-Point):** Duy trì điều kiện 4 ($$x, s > 0$$) và tiến dần tới các điều kiện 1, 2, 3.
- **Đường trung tâm:** Phương trình $$XS\mathbf{1} = \tau\mathbf{1}$$ xác định quỹ đạo trơn trong miền trong dẫn tới nghiệm tối ưu.

### 🔗 **Tính đối ngẫu Fenchel**

#### **Dạng bài toán tổng hợp**
**Nguyên thủy:** $$\min_x f(x) + g(Ax)$$

**Viết lại:** $$\min_{x,z} f(x) + g(z) \quad \text{s.t.} \quad Ax = z$$

#### **Cách tiếp cận qua hàm liên hợp**
**Hàm Lagrange:**
$$L(x,z,v) = f(x) + g(z) + v^T(z - Ax)$$

**Hàm đối ngẫu:**
$$\begin{align}
g(v) &= \min_{x,z} L(x,z,v) \\
&= \min_x [f(x) - (A^T v)^T x] + \min_z [g(z) + v^T z] \\
&= -f^*(A^T v) - g^*(-v)
\end{align}$$

#### **Bài toán đối ngẫu Fenchel**
$$\max_v -f^*(A^T v) - g^*(-v)$$

**Tính đối xứng:** Nếu $$f, g$$ là các hàm lồi và đóng, thì bài toán đối ngẫu của bài toán đối ngẫu quay về chính bài toán nguyên thủy.

### 🎯 **Ứng dụng trong quy hoạch nón (Conic Programming)**

#### **Bài toán quy hoạch nón dạng chuẩn**
$$\min c^T x \quad \text{s.t.} \quad Ax = b, \quad x \in K$$

#### **Biểu diễn Fenchel**
- $$f(x) = c^T x + I_K(x)$$
- $$g(z) = I_{\{b\}}(z)$$
- $$\min f(x) + g(Ax)$$

#### **Bài toán đối ngẫu nón**
$$\max b^T y \quad \text{s.t.} \quad A^T y + s = c, \quad s \in K^*$$

**Điều kiện đối ngẫu mạnh:**
- Bài toán nguyên thủy khả thi ngặt **hoặc** bài toán đối ngẫu khả thi ngặt (với giá trị tối ưu hữu hạn) $$\Longrightarrow$$ đối ngẫu mạnh thỏa mãn.
- Cả hai cùng khả thi ngặt $$\Longrightarrow$$ đối ngẫu mạnh thỏa mãn và cả hai đều đạt nghiệm tối ưu.

### 📊 **Quy hoạch bán xác định (SDP)**

**SDP nguyên thủy:**
$$\min \text{tr}(CX) \quad \text{s.t.} \quad \text{tr}(A_i X) = b_i, \quad X \succeq 0$$

**SDP đối ngẫu:**
$$\max b^T y \quad \text{s.t.} \quad \sum y_i A_i + S = C, \quad S \succeq 0$$

**Tính tự đối ngẫu của nón PSD:** $$(\mathbb{S}_+^n)^* = \mathbb{S}_+^n$$.

**Bài toán rào cản cho SDP:**
- **Nguyên thủy:** $$\min \text{tr}(CX) - \tau \log(\det(X)) \quad \text{s.t.} \quad \text{tr}(A_i X) = b_i$$
- **Đối ngẫu:** $$\max b^T y + \tau \log(\det(S)) \quad \text{s.t.} \quad \sum y_i A_i + S = C$$

**Lưu ý:** Khác với LP, bài toán SDP không phải lúc nào cũng thỏa mãn tính đối ngẫu mạnh.

### 🛠️ **Ý nghĩa thực hành và liên kết giữa các dạng đối ngẫu**

- **Lagrangian ↔ Fenchel:** Đối ngẫu Lagrange phù hợp cho bài toán có ràng buộc tổng quát; đối ngẫu Fenchel đặc biệt thuận tiện cho bài toán tổng hai hàm (có điều chuẩn hoặc toán tử tuyến tính).
- **Lựa chọn thuật toán:** Nếu bài toán đối ngẫu có cấu trúc đơn giản hơn, có thể giải trực tiếp bài toán đối ngẫu; với bài toán quy mô lớn có ràng buộc nón hoặc cần độ chính xác cao, phương pháp điểm trong nguyên thủy – đối ngẫu khai thác đồng thời cả hai phía và dùng khoảng cách đối ngẫu làm tiêu chí dừng.
- **Lưu ý cài đặt:** Cần kiểm tra điều kiện Slater để đảm bảo đối ngẫu mạnh, theo dõi số điều kiện và tận dụng nghiệm đối ngẫu cho khởi động ấm (warm start) hoặc phân tích độ nhạy (giá bóng).

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

Bài tập trắc nghiệm này kiểm tra kiến thức về tính đối ngẫu, bao gồm đối ngẫu Lagrange, điều kiện tối ưu KKT, đối ngẫu Fenchel và các tính chất liên quan.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>🔄 Bài tập trắc nghiệm: Tính đối ngẫu (Nhìn lại)</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 4%"></div>
        </div>
        <div class="score-display" id="score-display">Câu hỏi: <span id="current-q">1</span> / <span id="total-q">25</span></div>
    </div>

    <div id="quiz-content">
        <!-- Câu hỏi 1: Lagrangian definition -->
        <div class="question" id="q1" style="display: block;">
            <h3>Câu 1: Hàm Lagrange cho bài toán có ràng buộc \(h_i(x) \leq 0\) và \(l_j(x) = 0\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) \(L(x,u,v) = f(x) + \sum u_i h_i(x) + \sum v_j l_j(x)\)</label>
                <label><input type="radio" name="q1" value="b"> B) \(L(x,u,v) = f(x) - \sum u_i h_i(x) - \sum v_j l_j(x)\)</label>
                <label><input type="radio" name="q1" value="c"> C) \(L(x,u,v) = f(x) + \sum u_i h_i(x) - \sum v_j l_j(x)\)</label>
                <label><input type="radio" name="q1" value="d"> D) \(L(x,u,v) = f(x) - \sum u_i h_i(x) + \sum v_j l_j(x)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$L(x,u,v) = f(x) + \sum u_i h_i(x) + \sum v_j l_j(x)$$</strong><br>
                Đây là dạng chuẩn của hàm Lagrange với biến đối ngẫu $$u_i \geq 0$$ cho ràng buộc bất đẳng thức và $$v_j$$ tự do cho ràng buộc đẳng thức.
            </div>
        </div>

        <!-- Câu hỏi 2: Primal problem reformulation -->
        <div class="question" id="q2" style="display: none;">
            <h3>Câu 2: Bài toán nguyên thủy có thể được viết lại thành:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) \(\min_x \max_{u \geq 0, v} L(x,u,v)\)</label>
                <label><input type="radio" name="q2" value="b"> B) \(\max_x \min_{u \geq 0, v} L(x,u,v)\)</label>
                <label><input type="radio" name="q2" value="c"> C) \(\min_x \min_{u \geq 0, v} L(x,u,v)\)</label>
                <label><input type="radio" name="q2" value="d"> D) \(\max_x \max_{u \geq 0, v} L(x,u,v)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\min_x \max_{u \geq 0, v} L(x,u,v)$$</strong><br>
                Bài toán nguyên thủy cực tiểu hóa theo $$x$$ sau khi cực đại hóa hàm Lagrange theo các biến đối ngẫu để áp đặt các ràng buộc.
            </div>
        </div>

        <!-- Câu hỏi 3: Dual problem -->
        <div class="question" id="q3" style="display: none;">
            <h3>Câu 3: Bài toán đối ngẫu tương ứng là:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) \(\max_{u \geq 0, v} \min_x L(x,u,v)\)</label>
                <label><input type="radio" name="q3" value="b"> B) \(\min_{u \geq 0, v} \max_x L(x,u,v)\)</label>
                <label><input type="radio" name="q3" value="c"> C) \(\max_{u \geq 0, v} \max_x L(x,u,v)\)</label>
                <label><input type="radio" name="q3" value="d"> D) \(\min_{u \geq 0, v} \min_x L(x,u,v)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\max_{u \geq 0, v} \min_x L(x,u,v)$$</strong><br>
                Bài toán đối ngẫu cực đại hóa theo các biến đối ngẫu sau khi cực tiểu hóa hàm Lagrange theo biến nguyên thủy $$x$$.
            </div>
        </div>

        <!-- Câu hỏi 4: Dual function -->
        <div class="question" id="q4" style="display: none;">
            <h3>Câu 4: Hàm đối ngẫu \(g(u,v)\) được định nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) \(g(u,v) = \inf_x L(x,u,v)\)</label>
                <label><input type="radio" name="q4" value="b"> B) \(g(u,v) = \sup_x L(x,u,v)\)</label>
                <label><input type="radio" name="q4" value="c"> C) \(g(u,v) = L(x^*,u,v)\)</label>
                <label><input type="radio" name="q4" value="d"> D) \(g(u,v) = \nabla_x L(x,u,v)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$g(u,v) = \inf_x L(x,u,v)$$</strong><br>
                Hàm đối ngẫu là cận dưới đúng (infimum) của hàm Lagrange theo biến nguyên thủy, và luôn là hàm lõm theo các biến đối ngẫu.
            </div>
        </div>

        <!-- Câu hỏi 5: Strong duality condition -->
        <div class="question" id="q5" style="display: none;">
            <h3>Câu 5: Tính đối ngẫu mạnh xảy ra khi:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) \(p^* = d^*\) (giá trị tối ưu nguyên thủy bằng giá trị tối ưu đối ngẫu)</label>
                <label><input type="radio" name="q5" value="b"> B) \(p^* > d^*\)</label>
                <label><input type="radio" name="q5" value="c"> C) \(p^* < d^*\)</label>
                <label><input type="radio" name="q5" value="d"> D) Khoảng cách đối ngẫu bằng \(\infty\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$p^* = d^*$$ (giá trị tối ưu nguyên thủy bằng giá trị tối ưu đối ngẫu)</strong><br>
                Tính đối ngẫu mạnh đồng nghĩa với khoảng cách đối ngẫu bằng $$0$$, tức $$p^* = d^*$$.
            </div>
        </div>

        <!-- Câu hỏi 6: KKT stationarity -->
        <div class="question" id="q6" style="display: none;">
            <h3>Câu 6: Điều kiện dừng (stationarity) trong hệ KKT là:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) \(\nabla_x L(x^*,u^*,v^*) = 0\)</label>
                <label><input type="radio" name="q6" value="b"> B) \(h_i(x^*) \leq 0\)</label>
                <label><input type="radio" name="q6" value="c"> C) \(u_i^* \geq 0\)</label>
                <label><input type="radio" name="q6" value="d"> D) \(u_i^* h_i(x^*) = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\nabla_x L(x^*,u^*,v^*) = 0$$</strong><br>
                Điều kiện dừng yêu cầu gradient của hàm Lagrange theo biến nguyên thủy triệt tiêu tại điểm tối ưu.
            </div>
        </div>

        <!-- Câu hỏi 7: Complementary slackness -->
        <div class="question" id="q7" style="display: none;">
            <h3>Câu 7: Điều kiện bù chặt (complementary slackness) là:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) \(u_i^* h_i(x^*) = 0\) với mọi \(i\)</label>
                <label><input type="radio" name="q7" value="b"> B) \(u_i^* + h_i(x^*) = 0\)</label>
                <label><input type="radio" name="q7" value="c"> C) \(u_i^* h_i(x^*) \geq 0\)</label>
                <label><input type="radio" name="q7" value="d"> D) \(u_i^* = h_i(x^*)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$u_i^* h_i(x^*) = 0$$ với mọi $$i$$</strong><br>
                Điều kiện bù chặt cho biết biến đối ngẫu bằng $$0$$ nếu ràng buộc không tác dụng ($$h_i(x^*) < 0$$), và ràng buộc phải tác dụng ($$h_i(x^*) = 0$$) nếu biến đối ngẫu dương ($$u_i^* > 0$$).
            </div>
        </div>

        <!-- Câu hỏi 8: Fenchel conjugate -->
        <div class="question" id="q8" style="display: none;">
            <h3>Câu 8: Hàm liên hợp Fenchel của hàm \(f\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) \(f^*(y) = \sup_x (y^T x - f(x))\)</label>
                <label><input type="radio" name="q8" value="b"> B) \(f^*(y) = \inf_x (y^T x - f(x))\)</label>
                <label><input type="radio" name="q8" value="c"> C) \(f^*(y) = \sup_x (y^T x + f(x))\)</label>
                <label><input type="radio" name="q8" value="d"> D) \(f^*(y) = f(y)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f^*(y) = \sup_x (y^T x - f(x))$$</strong><br>
                Hàm liên hợp Fenchel là cận trên đúng (supremum) của hiệu giữa hàm tuyến tính $$y^Tx$$ và hàm gốc $$f(x)$$.
            </div>
        </div>

        <!-- Câu hỏi 9: Fenchel duality -->
        <div class="question" id="q9" style="display: none;">
            <h3>Câu 9: Bài toán đối ngẫu Fenchel của \(\min_x f(x) + g(Ax)\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) \(\max_v -f^*(A^T v) - g^*(-v)\)</label>
                <label><input type="radio" name="q9" value="b"> B) \(\min_v f^*(A^T v) + g^*(v)\)</label>
                <label><input type="radio" name="q9" value="c"> C) \(\max_v f^*(A^T v) - g^*(v)\)</label>
                <label><input type="radio" name="q9" value="d"> D) \(\min_v -f^*(A^T v) + g^*(-v)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\max_v -f^*(A^T v) - g^*(-v)$$</strong><br>
                Bài toán đối ngẫu Fenchel biểu diễn mục tiêu đối ngẫu trực tiếp qua hàm liên hợp của $$f$$ và $$g$$.
            </div>
        </div>

        <!-- Câu hỏi 10: Biconjugate -->
        <div class="question" id="q10" style="display: none;">
            <h3>Câu 10: Hàm song liên hợp (biconjugate) \(f^{**}\) của hàm lồi \(f\) thỏa mãn:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) \(f^{**} = f\) (nếu \(f\) lồi, chính thường và nửa liên tục dưới)</label>
                <label><input type="radio" name="q10" value="b"> B) \(f^{**} = -f\)</label>
                <label><input type="radio" name="q10" value="c"> C) \(f^{**} = f^2\)</label>
                <label><input type="radio" name="q10" value="d"> D) \(f^{**} = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f^{**} = f$$ (nếu $$f$$ lồi, chính thường và nửa liên tục dưới)</strong><br>
                Theo định lý Fenchel–Moreau, hàm song liên hợp của một hàm lồi chính thường, nửa liên tục dưới (đóng) chính là hàm ban đầu.
            </div>
        </div>

        <!-- Câu hỏi 11: Saddle point -->
        <div class="question" id="q11" style="display: none;">
            <h3>Câu 11: \((x^*, u^*, v^*)\) là điểm yên (saddle point) của hàm Lagrange nếu:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) \(L(x^*, u, v) \leq L(x^*, u^*, v^*) \leq L(x, u^*, v^*)\) với mọi \((x,u,v)\) khả thi</label>
                <label><input type="radio" name="q11" value="b"> B) \(L(x^*, u^*, v^*) = 0\)</label>
                <label><input type="radio" name="q11" value="c"> C) \(\nabla L(x^*, u^*, v^*) = 0\)</label>
                <label><input type="radio" name="q11" value="d"> D) \(L(x, u, v) = L(x^*, u^*, v^*)\) với mọi \((x,u,v)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$L(x^*, u, v) \leq L(x^*, u^*, v^*) \leq L(x, u^*, v^*)$$ với mọi $$(x,u,v)$$ khả thi</strong><br>
                Điểm yên đạt cực tiểu theo biến nguyên thủy $$x$$ và đạt cực đại theo các biến đối ngẫu $$(u, v)$$.
            </div>
        </div>

        <!-- Câu hỏi 12: Slater condition -->
        <div class="question" id="q12" style="display: none;">
            <h3>Câu 12: Với bài toán lồi, điều kiện Slater đảm bảo:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) Tính đối ngẫu mạnh được thỏa mãn</label>
                <label><input type="radio" name="q12" value="b"> B) Tính đối ngẫu yếu được thỏa mãn</label>
                <label><input type="radio" name="q12" value="c"> C) Khoảng cách đối ngẫu bằng 0</label>
                <label><input type="radio" name="q12" value="d"> D) Cả A và C</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Cả A và C</strong><br>
                Điều kiện Slater (tồn tại điểm khả thi ngặt) đảm bảo tính đối ngẫu mạnh, tức là không có khoảng cách đối ngẫu ($$p^* = d^*$$).
            </div>
        </div>

        <!-- Câu hỏi 13: Linear programming dual -->
        <div class="question" id="q13" style="display: none;">
            <h3>Câu 13: Bài toán đối ngẫu của LP \(\min c^T x\) thỏa mãn \(Ax = b, x \geq 0\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) \(\max b^T y\) thỏa mãn \(A^T y \leq c\)</label>
                <label><input type="radio" name="q13" value="b"> B) \(\min b^T y\) thỏa mãn \(A^T y \geq c\)</label>
                <label><input type="radio" name="q13" value="c"> C) \(\max c^T y\) thỏa mãn \(A^T y = b\)</label>
                <label><input type="radio" name="q13" value="d"> D) \(\min A^T y\) thỏa mãn \(b^T y \leq c\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\max b^T y$$ thỏa mãn $$A^T y \leq c$$</strong><br>
                Bài toán đối ngẫu chuẩn của LP có biến $$y$$ tự do và ràng buộc $$A^T y \leq c$$ (tương đương $$A^T y + s = c, s \geq 0$$).
            </div>
        </div>

        <!-- Câu hỏi 14: Quadratic programming dual -->
        <div class="question" id="q14" style="display: none;">
            <h3>Câu 14: Bài toán đối ngẫu của QP \(\min \frac{1}{2}x^T Q x + c^T x\) thỏa mãn \(Ax \leq b\) với \(Q \succ 0\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) \(\max -\frac{1}{2}(A^T u + c)^T Q^{-1} (A^T u + c) - b^T u\) thỏa mãn \(u \geq 0\)</label>
                <label><input type="radio" name="q14" value="b"> B) \(\min \frac{1}{2}u^T Q u - b^T u\) thỏa mãn \(u \geq 0\)</label>
                <label><input type="radio" name="q14" value="c"> C) \(\max b^T u\) thỏa mãn \(A^T u = c\)</label>
                <label><input type="radio" name="q14" value="d"> D) \(\min c^T u + b^T u\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\max -\frac{1}{2}(A^T u + c)^T Q^{-1} (A^T u + c) - b^T u$$ thỏa mãn $$u \geq 0$$</strong><br>
                Từ điều kiện dừng $$\nabla_x L = Qx + c + A^T u = 0 \Rightarrow x = -Q^{-1}(A^T u + c)$$, thay lại vào hàm Lagrange thu được bài toán đối ngẫu trên.
            </div>
        </div>

        <!-- Câu hỏi 15: Conjugate of quadratic -->
        <div class="question" id="q15" style="display: none;">
            <h3>Câu 15: Hàm liên hợp của \(f(x) = \frac{1}{2}x^T Q x\) với \(Q \succ 0\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) \(f^*(y) = \frac{1}{2}y^T Q^{-1} y\)</label>
                <label><input type="radio" name="q15" value="b"> B) \(f^*(y) = \frac{1}{2}y^T Q y\)</label>
                <label><input type="radio" name="q15" value="c"> C) \(f^*(y) = y^T Q^{-1} y\)</label>
                <label><input type="radio" name="q15" value="d"> D) \(f^*(y) = -\frac{1}{2}y^T Q^{-1} y\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f^*(y) = \frac{1}{2}y^T Q^{-1} y$$</strong><br>
                Hàm liên hợp của dạng toàn phương xác định dương thay ma trận $$Q$$ bằng nghịch đảo $$Q^{-1}$$ và giữ nguyên hệ số $$\frac{1}{2}$$.
            </div>
        </div>

        <!-- Câu hỏi 16: Moreau envelope -->
        <div class="question" id="q16" style="display: none;">
            <h3>Câu 16: Bao Moreau (Moreau envelope) của hàm \(f\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) \(M_\lambda f(x) = \inf_z \left( f(z) + \frac{1}{2\lambda}\|x-z\|^2 \right)\)</label>
                <label><input type="radio" name="q16" value="b"> B) \(M_\lambda f(x) = f(x) + \lambda\|x\|^2\)</label>
                <label><input type="radio" name="q16" value="c"> C) \(M_\lambda f(x) = \lambda f(x)\)</label>
                <label><input type="radio" name="q16" value="d"> D) \(M_\lambda f(x) = f(\lambda x)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$M_\lambda f(x) = \inf_z \left( f(z) + \frac{1}{2\lambda}\|x-z\|^2 \right)$$</strong><br>
                Bao Moreau là một xấp xỉ trơn của hàm $$f$$ thu được bằng phép chập infimal với hàm điều chuẩn bậc hai.
            </div>
        </div>

        <!-- Câu hỏi 17: Proximal operator -->
        <div class="question" id="q17" style="display: none;">
            <h3>Câu 17: Toán tử lân cận (proximal operator) liên hệ với bao Moreau như thế nào?</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) \(\text{prox}_{\lambda f}(x) = \arg\min_z \left( f(z) + \frac{1}{2\lambda}\|x-z\|^2 \right)\)</label>
                <label><input type="radio" name="q17" value="b"> B) \(\text{prox}_{\lambda f}(x) = \nabla M_\lambda f(x)\)</label>
                <label><input type="radio" name="q17" value="c"> C) \(\text{prox}_{\lambda f}(x) = M_\lambda f(x)\)</label>
                <label><input type="radio" name="q17" value="d"> D) \(\text{prox}_{\lambda f}(x) = x - \lambda \nabla f(x)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\text{prox}_{\lambda f}(x) = \arg\min_z \left( f(z) + \frac{1}{2\lambda}\|x-z\|^2 \right)$$</strong><br>
                Toán tử lân cận chính là điểm đạt cực tiểu (argmin) của bài toán tối ưu trong định nghĩa bao Moreau.
            </div>
        </div>

        <!-- Câu hỏi 18: Duality in SVM -->
        <div class="question" id="q18" style="display: none;">
            <h3>Câu 18: Trong SVM, bài toán đối ngẫu có ưu điểm nào sau đây?</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) Có thể áp dụng thủ thuật hạt nhân (kernel trick)</label>
                <label><input type="radio" name="q18" value="b"> B) Số biến phụ thuộc vào số điểm dữ liệu thay vì số chiều đặc trưng</label>
                <label><input type="radio" name="q18" value="c"> C) Là bài toán quy hoạch bậc hai với ràng buộc hộp đơn giản</label>
                <label><input type="radio" name="q18" value="d"> D) Tất cả các ưu điểm trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các ưu điểm trên</strong><br>
                Bài toán đối ngẫu của SVM cho phép dùng kernel trick, có ràng buộc đơn giản và đặc biệt hiệu quả khi không gian đặc trưng có số chiều lớn.
            </div>
        </div>

        <!-- Câu hỏi 19: Weak duality theorem -->
        <div class="question" id="q19" style="display: none;">
            <h3>Câu 19: Định lý đối ngẫu yếu khẳng định rằng:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) \(d^* \leq p^*\) luôn đúng</label>
                <label><input type="radio" name="q19" value="b"> B) \(d^* \geq p^*\) luôn đúng</label>
                <label><input type="radio" name="q19" value="c"> C) \(d^* = p^*\) luôn đúng</label>
                <label><input type="radio" name="q19" value="d"> D) Không có quan hệ giữa \(d^*\) và \(p^*\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$d^* \leq p^*$$ luôn đúng</strong><br>
                Theo đối ngẫu yếu, giá trị tối ưu đối ngẫu luôn là cận dưới của giá trị tối ưu nguyên thủy, bất kể bài toán có lồi hay không.
            </div>
        </div>

        <!-- Câu hỏi 20: Applications of duality -->
        <div class="question" id="q20" style="display: none;">
            <h3>Câu 20: Lý thuyết đối ngẫu được ứng dụng trong lĩnh vực nào sau đây?</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Phân tích độ nhạy (sensitivity analysis)</label>
                <label><input type="radio" name="q20" value="b"> B) Thiết kế thuật toán (các phương pháp đối ngẫu và nguyên thủy – đối ngẫu)</label>
                <label><input type="radio" name="q20" value="c"> C) Phân tích lý thuyết và thiết lập cận tối ưu</label>
                <label><input type="radio" name="q20" value="d"> D) Tất cả các ứng dụng trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các ứng dụng trên</strong><br>
                Lý thuyết đối ngẫu đóng vai trò nền tảng trong phân tích độ nhạy, thiết kế thuật toán, ước lượng cận dưới và diễn giải kinh tế (giá bóng).
            </div>
        </div>
        <!-- Câu hỏi 21: Thực hành -->
        <div class="question" id="q21" style="display: none;">
            <h3>Câu 21: Trong lý thuyết đối ngẫu, tính đối ngẫu mạnh xảy ra khi:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) Khoảng cách đối ngẫu bằng 0</label>
                <label><input type="radio" name="q21" value="b"> B) Bài toán nguyên thủy không khả thi</label>
                <label><input type="radio" name="q21" value="c"> C) Bài toán đối ngẫu không khả thi</label>
                <label><input type="radio" name="q21" value="d"> D) Cả hai bài toán đều không bị chặn</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Khoảng cách đối ngẫu bằng 0</strong><br>
                Tính đối ngẫu mạnh nghĩa là $$p^* = d^*$$, tức khoảng cách đối ngẫu $$p^* - d^* = 0$$.
            </div>
        </div>

        <!-- Câu hỏi 22: Thực hành -->
        <div class="question" id="q22" style="display: none;">
            <h3>Câu 22: Hàm liên hợp Fenchel của hàm $$f(x) = \frac{1}{2}x^2$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) $$f^*(y) = \frac{1}{2}y^2$$</label>
                <label><input type="radio" name="q22" value="b"> B) $$f^*(y) = y^2$$</label>
                <label><input type="radio" name="q22" value="c"> C) $$f^*(y) = \frac{1}{4}y^2$$</label>
                <label><input type="radio" name="q22" value="d"> D) $$f^*(y) = 2y^2$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f^*(y) = \frac{1}{2}y^2$$</strong><br>
                Hàm liên hợp Fenchel của $$\frac{1}{2}x^2$$ là $$\sup_x (yx - \frac{1}{2}x^2) = \frac{1}{2}y^2$$.
            </div>
        </div>

        <!-- Câu hỏi 23: Thực hành -->
        <div class="question" id="q23" style="display: none;">
            <h3>Câu 23: Định lý song đối ngẫu (biconjugate) khẳng định:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) $$f^{**} = f$$ nếu $$f$$ lồi, chính thường và đóng</label>
                <label><input type="radio" name="q23" value="b"> B) $$f^{**} = -f$$</label>
                <label><input type="radio" name="q23" value="c"> C) $$f^{**} = f^2$$</label>
                <label><input type="radio" name="q23" value="d"> D) $$f^{**}$$ không tồn tại</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f^{**} = f$$ nếu $$f$$ lồi, chính thường và đóng</strong><br>
                Với hàm lồi chính thường và đóng, lấy liên hợp hai lần sẽ quay trở về đúng hàm ban đầu.
            </div>
        </div>

        <!-- Câu hỏi 24: Thực hành -->
        <div class="question" id="q24" style="display: none;">
            <h3>Câu 24: Phân rã Moreau (Moreau decomposition) cho biết:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) $$x = \text{prox}_f(x) + \text{prox}_{f^*}(x)$$</label>
                <label><input type="radio" name="q24" value="b"> B) $$x = \text{prox}_f(x) - \text{prox}_{f^*}(x)$$</label>
                <label><input type="radio" name="q24" value="c"> C) $$x = \text{prox}_f(x) \cdot \text{prox}_{f^*}(x)$$</label>
                <label><input type="radio" name="q24" value="d"> D) Không có công thức tổng quát</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$x = \text{prox}_f(x) + \text{prox}_{f^*}(x)$$</strong><br>
                Phân rã Moreau cho thấy mọi điểm $$x$$ có thể được phân tách thành tổng ảnh qua toán tử lân cận của $$f$$ và của hàm liên hợp $$f^*$$.
            </div>
        </div>

        <!-- Câu hỏi 25: Thực hành -->
        <div class="question" id="q25" style="display: none;">
            <h3>Câu 25: Phép biến đổi Legendre (Legendre transform) liên quan trực tiếp đến:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) Hàm liên hợp Fenchel (Fenchel conjugate)</label>
                <label><input type="radio" name="q25" value="b"> B) Gradient</label>
                <label><input type="radio" name="q25" value="c"> C) Ma trận Hessian</label>
                <label><input type="radio" name="q25" value="d"> D) Trị riêng (eigenvalue)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Hàm liên hợp Fenchel (Fenchel conjugate)</strong><br>
                Phép biến đổi Legendre là trường hợp đặc biệt của hàm liên hợp Fenchel đối với các hàm lồi ngặt và khả vi.
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
    q1: 'a', q2: 'a', q3: 'a', q4: 'a', q5: 'a',
    q6: 'a', q7: 'a', q8: 'a', q9: 'a', q10: 'a',
    q11: 'a', q12: 'd', q13: 'a', q14: 'a', q15: 'a',
    q16: 'a', q17: 'a', q18: 'd', q19: 'a', q20: 'd'
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
        message = '🌟 Xuất sắc! Bạn đã thành thạo duality theory và advanced concepts!';
    } else if (percentage >= 80) {
        message = '👍 Rất tốt! Bạn hiểu tốt về Lagrangian và Fenchel duality.';
    } else if (percentage >= 70) {
        message = '📚 Khá ổn! Hãy xem lại KKT conditions và conjugate functions.';
    } else if (percentage >= 60) {
        message = '💪 Cần cải thiện! Ôn lại strong duality và optimality conditions.';
    } else {
        message = '📖 Hãy học lại từ đầu về duality theory nhé!';
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
