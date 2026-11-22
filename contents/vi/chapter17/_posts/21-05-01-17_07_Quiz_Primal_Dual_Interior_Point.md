---
layout: post
title: 17-07 Bài tập trắc nghiệm - Phương Pháp Điểm Trong Nguyên Thủy-Đối Ngẫu
chapter: '17'
order: 11
owner: GitHub Copilot
lang: vi
categories:
- chapter17
lesson_type: quiz
redirect_from:
  - /contents/vi/chapter17/17_06_Quiz_Primal_Dual_Interior_Point/
---

## 📚 Ôn tập lý thuyết

Trước khi làm bài tập, hãy ôn lại các khái niệm chính trong chương này:

### ⚡ **Phương pháp điểm trong gốc-đối ngẫu (Primal-Dual Interior-Point Method)**

#### **Động lực và so sánh với phương pháp chắn**
**Hạn chế của phương pháp chắn (Barrier Method):**
- **Nhiều bước Newton cho mỗi giá trị $$t$$:** Bước định tâm (centering) đòi hỏi nhiều vòng lặp trong.
- **Bắt buộc duy trì tính khả thi:** Luôn phải giữ $$Ax = b$$ và $$h_i(x) < 0$$.
- **Giải tuần tự:** Phải giải từng bài toán con rào cản kế tiếp nhau.

**Ưu điểm của phương pháp gốc-đối ngẫu:**
- **Một bước Newton mỗi vòng lặp:** Không cần giải chính xác bước định tâm ở mỗi giá trị $$\tau$$.
- **Cho phép khởi tạo không khả thi:** Không yêu cầu $$Ax^0 = b$$ ở điểm bắt đầu (trong dạng này vẫn cần $$h(x^0) < 0, u^0 > 0$$).
- **Cập nhật đồng thời:** Cập nhật cùng lúc cả biến gốc và biến đối ngẫu.
- **Hiệu năng thực tế tốt hơn:** Thường cần ít vòng lặp hơn và đạt độ chính xác cao hơn.

### 🎯 **Phương trình đường trung tâm**

#### **Điều kiện KKT gốc**
$$\begin{align}
\nabla f(x) + \nabla h(x)u + A^T v &= 0 \\
Uh(x) &= 0 \\
Ax &= b \\
u \ge 0, \quad -h(x) &\ge 0
\end{align}$$

#### **Điều kiện KKT bị nhiễu (Đường trung tâm)**
$$\begin{align}
\nabla f(x) + \nabla h(x)u + A^T v &= 0 \\
Uh(x) + \tau\mathbf{1} &= 0 \\
Ax - b &= 0 \\
u > 0, \quad -h(x) &> 0
\end{align}$$

**Điểm khác biệt chính:** Điều kiện bù chặt $$Uh(x) = 0$$ được thay bằng $$Uh(x) = -\tau\mathbf{1}$$, điều kiện không âm $$\ge 0$$ chuyển thành điểm trong ngặt $$> 0$$, với tham số $$\tau = 1/t$$ kiểm soát mức độ nhiễu. Nghiệm $$(x(\tau), u(\tau), v(\tau))$$ trên đường trung tâm có khoảng cách đối ngẫu đúng bằng:
$$f(x(\tau)) - \min_x L(x, u(\tau), v(\tau)) = m\tau = \frac{m}{t}$$

### 🔄 **Bước Newton cho đường trung tâm**

**Vector phần dư:**
$$r(x,u,v) = \begin{bmatrix}
\nabla f(x) + \nabla h(x)u + A^T v \\
Uh(x) + \tau\mathbf{1} \\
Ax - b
\end{bmatrix}$$

**Hệ phương trình Newton:**
$$\begin{bmatrix}
\nabla^2 f(x) + \sum u_i \nabla^2 h_i(x) & \nabla h(x) & A^T \\
U \nabla h(x)^T & H(x) & 0 \\
A & 0 & 0
\end{bmatrix}
\begin{bmatrix}
\Delta x \\
\Delta u \\
\Delta v
\end{bmatrix} = -r(x,u,v)$$

với $$H(x) = \text{diag}(h(x))$$ và $$U = \text{diag}(u)$$. Hệ tuyến tính này xác định đồng thời hướng cập nhật $$(\Delta x, \Delta u, \Delta v)$$ cho cả biến gốc lẫn biến đối ngẫu theo phiên bản tìm nghiệm (root-finding) của phương pháp Newton.

### 📊 **Các phần dư và khoảng cách đối ngẫu thay thế**

1. **Phần dư đối ngẫu:** $$r_{\text{dual}} = \nabla f(x) + \nabla h(x)u + A^T v$$ ($$r_{\text{dual}} = 0$$ ứng với khả thi đối ngẫu).
2. **Phần dư trung tâm:** $$r_{\text{cent}} = Uh(x) + \tau\mathbf{1}$$ (điều kiện bù chặt bị nhiễu với tham số $$\tau$$).
3. **Phần dư gốc:** $$r_{\text{prim}} = Ax - b$$ ($$r_{\text{prim}} = 0$$ ứng với khả thi gốc).

**Khoảng cách đối ngẫu thay thế (Surrogate duality gap):**
$$\eta = -h(x)^T u \quad \text{với} \quad h(x) \le 0, \ u \ge 0$$

Khi điểm lặp đồng thời khả thi gốc và đối ngẫu ($$r_{\text{prim}} = 0, r_{\text{dual}} = 0$$), khoảng cách đối ngẫu thay thế trùng với khoảng cách đối ngẫu thực sự $$m\tau = m/t$$, với $$t = -\frac{m}{h(x)^T u}$$.

### 🔄 **Thuật toán gốc-đối ngẫu và tìm kiếm theo đường lui nhiều giai đoạn**

Đặt $$\tau(x,u) = -\frac{h(x)^T u}{m}$$, chọn $$\sigma \in (0,1)$$ ($$\sigma = 1/\mu$$) và khởi tạo $$(x^0, u^0, v^0)$$ với $$h(x^0) < 0, u^0 > 0$$. Ở mỗi vòng lặp $$k$$:
1. Đặt $$\tau = \sigma \tau(x^k, u^k)$$ và giải hệ Newton tìm $$(\Delta x, \Delta u, \Delta v)$$.
2. Tìm độ dài bước $$\theta_k$$ bằng **tìm kiếm theo đường lui nhiều giai đoạn (multi-stage backtracking line search)** với $$\alpha, \beta \in (0,1)$$ (thường $$\alpha = 0.01, \beta = 0.5$$):
   - **Giai đoạn 1 (khả thi đối ngẫu):** $$\theta_{\max} = \min\left\{1, \min\left\{-\frac{u_i}{\Delta u_i} : \Delta u_i < 0\right\}\right\}$$, rồi đặt $$\theta = 0.99\theta_{\max}$$.
   - **Giai đoạn 2 (khả thi gốc ngặt):** Giảm $$\theta = \beta\theta$$ cho đến khi $$h_i(x^+) < 0$$ với mọi $$i$$.
   - **Giai đoạn 3 (giảm chuẩn phần dư):** Tiếp tục giảm $$\theta = \beta\theta$$ cho đến khi $$\|r(x^+, u^+, v^+)\| \le (1 - \alpha\theta)\|r(x, u, v)\|$$.
3. Cập nhật $$(x^{k+1}, u^{k+1}, v^{k+1}) = (x^k, u^k, v^k) + \theta_k(\Delta x, \Delta u, \Delta v)$$.
4. Dừng khi $$-h(x)^T u \le \epsilon$$ và $$\lVert r_{\text{prim}} \rVert^2 + \lVert r_{\text{dual}} \rVert^2 \le \epsilon^2$$.

### 📈 **Trường hợp đặc biệt: LP và SDP**

#### **Quy hoạch tuyến tính (LP)**
- **Điều kiện đường trung tâm:** $$A^T y + s = c$$, $$Ax = b$$, $$XS\mathbf{1} = \tau\mathbf{1}$$, $$x, s > 0$$.
- **Hệ Newton:**
$$\begin{bmatrix}
0 & A^T & I \\
A & 0 & 0 \\
S & 0 & X
\end{bmatrix}
\begin{bmatrix}
\Delta x \\
\Delta y \\
\Delta s
\end{bmatrix} = -\begin{bmatrix}
A^T y + s - c \\
Ax - b \\
XS\mathbf{1} - \tau\mathbf{1}
\end{bmatrix}$$

#### **Quy hoạch bán xác định (SDP)**
- **Điều kiện đường trung tâm:** $$\mathcal{A}^*(y) + S = C$$, $$\mathcal{A}(X) = b$$, $$XS = \tau I$$, $$X, S \succ 0$$ (với tích vô hướng $$X \bullet S = \text{tr}(XS)$$).
- **Hệ Newton:**
$$\begin{bmatrix}
0 & \mathcal{A}^* & I \\
\mathcal{A} & 0 & 0 \\
S & 0 & X
\end{bmatrix}
\begin{bmatrix}
\Delta X \\
\Delta y \\
\Delta S
\end{bmatrix} = -\begin{bmatrix}
\mathcal{A}^*(y) + S - C \\
\mathcal{A}(X) - b \\
XS - \tau I
\end{bmatrix}$$

### 🔄 **So sánh phương pháp chắn và phương pháp gốc-đối ngẫu**

| **Tiêu chí** | **Phương pháp chắn (Barrier)** | **Phương pháp gốc-đối ngẫu (Primal-Dual)** |
|------------|-------------------|------------------------|
| **Số bước Newton** | Nhiều bước cho mỗi pha định tâm | Một bước ở mỗi vòng lặp |
| **Tính khả thi trung gian** | Phải luôn duy trì khả thi | Cho phép khởi tạo không khả thi ($$Ax^0 \neq b$$) |
| **Biến cập nhật** | Chỉ biến gốc | Cập nhật đồng thời cả gốc và đối ngẫu |
| **Tốc độ hội tụ** | Tuyến tính (vòng ngoài) | Thường đạt siêu tuyến tính dưới điều kiện thích hợp |
| **Độ phức tạp (LP)** | Đa thức | $$O(\sqrt{n}\log(1/\epsilon))$$ vòng lặp, tổng $$O(n^{3.5}\log(1/\epsilon))$$ |

### 🛠️ **Lưu ý thực hành và mở rộng**

- **Dự báo – hiệu chỉnh Mehrotra (Predictor-Corrector):** Kết hợp bước dự báo affine ($$\mu = 0$$) để giảm nhanh khoảng cách đối ngẫu với bước hiệu chỉnh dùng tham số $$\sigma$$ thích nghi để giữ gần đường trung tâm.
- **Nhúng đồng nhất tự đối ngẫu (Homogeneous self-dual):** Cho phép phát hiện đồng thời tính không khả thi và không bị chặn mà không cần điểm khởi tạo khả thi.
- **Giải hệ tuyến tính:** Sử dụng phân rã ma trận thưa (chẳng hạn phân rã LDL thưa cho hệ khối đối xứng rút gọn), theo dõi số điều kiện và điều chuẩn khi cần.

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

Bài tập trắc nghiệm này kiểm tra kiến thức về phương pháp điểm trong gốc-đối ngẫu, bao gồm phương trình đường trung tâm, hệ Newton, phần dư, khoảng cách đối ngẫu thay thế và quy hoạch bán xác định (SDP).

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>⚡ Bài tập trắc nghiệm: Phương pháp điểm trong gốc-đối ngẫu</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 4%"></div>
        </div>
        <div class="score-display" id="score-display">Câu hỏi: <span id="current-q">1</span> / <span id="total-q">25</span></div>
    </div>

    <div id="quiz-content">
        <!-- Câu hỏi 1: Primal-dual vs barrier method -->
        <div class="question" id="q1" style="display: block;">
            <h3>Câu 1: Phương pháp điểm trong gốc-đối ngẫu khác phương pháp chắn ở điểm nào?</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) Cập nhật đồng thời cả biến gốc và biến đối ngẫu</label>
                <label><input type="radio" name="q1" value="b"> B) Chỉ thực hiện một bước Newton ở mỗi vòng lặp</label>
                <label><input type="radio" name="q1" value="c"> C) Không yêu cầu điểm khởi tạo phải thỏa mãn ràng buộc đẳng thức khả thi</label>
                <label><input type="radio" name="q1" value="d"> D) Tất cả các điểm trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các điểm trên</strong><br>
                Phương pháp gốc-đối ngẫu cập nhật đồng thời biến gốc và đối ngẫu, thường chỉ cần một bước Newton mỗi vòng lặp và cho phép khởi tạo không khả thi ($$Ax^0 \neq b$$).
            </div>
        </div>

        <!-- Câu hỏi 2: Central path equations -->
        <div class="question" id="q2" style="display: none;">
            <h3>Câu 2: Hệ phương trình đường trung tâm cho bài toán có ràng buộc bất đẳng thức $$g_i(x) \leq 0$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) $$\nabla f(x) + \sum \lambda_i \nabla g_i(x) = 0, \ \lambda_i g_i(x) = -\frac{1}{t}$$</label>
                <label><input type="radio" name="q2" value="b"> B) $$\nabla f(x) + \sum \lambda_i \nabla g_i(x) = 0, \ \lambda_i g_i(x) = 0$$</label>
                <label><input type="radio" name="q2" value="c"> C) $$\nabla f(x) = 0, \ g_i(x) = 0$$</label>
                <label><input type="radio" name="q2" value="d"> D) $$\lambda_i = \frac{1}{t}, \ g_i(x) = -1$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\nabla f(x) + \sum \lambda_i \nabla g_i(x) = 0, \ \lambda_i g_i(x) = -\frac{1}{t}$$</strong><br>
                Phương trình đường trung tâm gồm điều kiện dừng và điều kiện bù chặt bị nhiễu theo tham số $$t$$ (hay $$\tau = 1/t$$).
            </div>
        </div>

        <!-- Câu hỏi 3: Newton system -->
        <div class="question" id="q3" style="display: none;">
            <h3>Câu 3: Hệ phương trình Newton trong phương pháp gốc-đối ngẫu được giải để tìm đại lượng nào?</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) $$(\Delta x, \Delta \lambda, \Delta \nu)$$ — hướng cập nhật cho cả biến gốc và biến đối ngẫu</label>
                <label><input type="radio" name="q3" value="b"> B) Chỉ $$\Delta x$$ — hướng cập nhật biến gốc</label>
                <label><input type="radio" name="q3" value="c"> C) Chỉ $$\Delta \lambda$$ — hướng cập nhật biến đối ngẫu</label>
                <label><input type="radio" name="q3" value="d"> D) Tham số $$t$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$(\Delta x, \Delta \lambda, \Delta \nu)$$ — hướng cập nhật cho cả biến gốc và biến đối ngẫu</strong><br>
                Hệ Newton giải đồng thời hướng cập nhật biến gốc $$\Delta x$$ và các hướng cập nhật biến đối ngẫu $$\Delta \lambda, \Delta \nu$$.
            </div>
        </div>

        <!-- Câu hỏi 4: Surrogate duality gap -->
        <div class="question" id="q4" style="display: none;">
            <h3>Câu 4: Khoảng cách đối ngẫu thay thế (surrogate duality gap) trong phương pháp gốc-đối ngẫu là:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) $$\eta = -\sum_{i=1}^m \lambda_i g_i(x)$$</label>
                <label><input type="radio" name="q4" value="b"> B) \(\eta = f(x) - g(\lambda, \nu)\)</label>
                <label><input type="radio" name="q4" value="c"> C) \(\eta = \|\nabla f(x)\|\)</label>
                <label><input type="radio" name="q4" value="d"> D) \(\eta = \sum_{i=1}^m |\lambda_i|\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\eta = -\sum_{i=1}^m \lambda_i g_i(x)$$</strong><br>
                Khoảng cách đối ngẫu thay thế ước lượng độ chênh lệch đối ngẫu trực tiếp từ điểm gốc-đối ngẫu hiện tại mà không cần đánh giá hàm đối ngẫu hay yêu cầu điểm lặp khả thi.
            </div>
        </div>

        <!-- Câu hỏi 5: Residuals -->
        <div class="question" id="q5" style="display: none;">
            <h3>Câu 5: Ba thành phần phần dư (residuals) trong phương pháp gốc-đối ngẫu gồm:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) Phần dư đối ngẫu, phần dư gốc và phần dư trung tâm</label>
                <label><input type="radio" name="q5" value="b"> B) Chỉ phần dư đối ngẫu</label>
                <label><input type="radio" name="q5" value="c"> C) Chỉ phần dư gốc</label>
                <label><input type="radio" name="q5" value="d"> D) Chỉ phần dư trung tâm</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Phần dư đối ngẫu, phần dư gốc và phần dư trung tâm</strong><br>
                Ba thành phần phần dư tương ứng với điều kiện dừng (đối ngẫu), điều kiện khả thi đẳng thức (gốc) và điều kiện bù chặt bị nhiễu (trung tâm).
            </div>
        </div>

        <!-- Câu hỏi 6: Predictor-corrector -->
        <div class="question" id="q6" style="display: none;">
            <h3>Câu 6: Trong phương pháp dự báo – hiệu chỉnh (predictor-corrector):</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) Bước dự báo giảm khoảng cách đối ngẫu, bước hiệu chỉnh cải thiện độ gần đường trung tâm</label>
                <label><input type="radio" name="q6" value="b"> B) Bước dự báo tăng tính khả thi, bước hiệu chỉnh giảm khoảng cách đối ngẫu</label>
                <label><input type="radio" name="q6" value="c"> C) Chỉ có bước dự báo</label>
                <label><input type="radio" name="q6" value="d"> D) Chỉ có bước hiệu chỉnh</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Bước dự báo giảm khoảng cách đối ngẫu, bước hiệu chỉnh cải thiện độ gần đường trung tâm</strong><br>
                Bước dự báo (affine) tiến mạnh về phía nghiệm tối ưu để giảm khoảng cách đối ngẫu, còn bước hiệu chỉnh kéo điểm lặp trở lại gần đường trung tâm.
            </div>
        </div>

        <!-- Câu hỏi 7: Mehrotra's algorithm -->
        <div class="question" id="q7" style="display: none;">
            <h3>Câu 7: Thuật toán dự báo – hiệu chỉnh Mehrotra là:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) Thuật toán gốc-đối ngẫu thực tế với tham số định tâm thích nghi</label>
                <label><input type="radio" name="q7" value="b"> B) Phương pháp Newton thuần túy</label>
                <label><input type="radio" name="q7" value="c"> C) Biến thể của phương pháp chắn thuần gốc</label>
                <label><input type="radio" name="q7" value="d"> D) Phương pháp bậc nhất</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Thuật toán gốc-đối ngẫu thực tế với tham số định tâm thích nghi</strong><br>
                Thuật toán Mehrotra là biến thể gốc-đối ngẫu được sử dụng rộng rãi nhờ cách chọn tham số định tâm $$\sigma$$ thích nghi dựa trên chất lượng bước dự báo.
            </div>
        </div>

        <!-- Câu hỏi 8: Infeasible start -->
        <div class="question" id="q8" style="display: none;">
            <h3>Câu 8: Phương pháp gốc-đối ngẫu có thể bắt đầu từ điểm không khả thi nhờ:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) Tìm kiếm theo đường lui (backtracking line search) làm giảm chuẩn phần dư về 0</label>
                <label><input type="radio" name="q8" value="b"> B) Bỏ qua các ràng buộc khả thi</label>
                <label><input type="radio" name="q8" value="c"> C) Chiếu trực tiếp lên tập khả thi ở mỗi bước</label>
                <label><input type="radio" name="q8" value="d"> D) Không thể bắt đầu từ điểm không khả thi</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Tìm kiếm theo đường lui (backtracking line search) làm giảm chuẩn phần dư về 0</strong><br>
                Tìm kiếm theo đường lui nhiều giai đoạn vừa giữ điểm lặp trong miền $$h(x) < 0, u > 0$$ vừa đảm bảo chuẩn phần dư tổng hợp (gồm cả phần dư khả thi) giảm dần về $$0$$.
            </div>
        </div>

        <!-- Câu hỏi 9: SDP primal problem -->
        <div class="question" id="q9" style="display: none;">
            <h3>Câu 9: Bài toán gốc của quy hoạch bán xác định (SDP) có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) \(\min C \bullet X\) thỏa mãn \(A_i \bullet X = b_i, \ X \succeq 0\)</label>
                <label><input type="radio" name="q9" value="b"> B) \(\min c^T x\) thỏa mãn \(Ax = b, \ x \geq 0\)</label>
                <label><input type="radio" name="q9" value="c"> C) \(\min \frac{1}{2}x^T Q x\) thỏa mãn \(Ax \leq b\)</label>
                <label><input type="radio" name="q9" value="d"> D) \(\min f(x)\) thỏa mãn \(g_i(x) \leq 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\min C \bullet X$$ thỏa mãn $$A_i \bullet X = b_i, \ X \succeq 0$$</strong><br>
                SDP cực tiểu hóa hàm tuyến tính trên biến ma trận đối xứng với các ràng buộc đẳng thức tuyến tính và ràng buộc nửa xác định dương $$X \succeq 0$$.
            </div>
        </div>

        <!-- Câu hỏi 10: SDP dual -->
        <div class="question" id="q10" style="display: none;">
            <h3>Câu 10: Bài toán đối ngẫu của SDP có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) \(\max b^T y\) thỏa mãn \(\sum y_i A_i + S = C, \ S \succeq 0\)</label>
                <label><input type="radio" name="q10" value="b"> B) \(\min b^T y\) thỏa mãn \(A^T y \leq c\)</label>
                <label><input type="radio" name="q10" value="c"> C) \(\max c^T z\) thỏa mãn \(A^T z = b\)</label>
                <label><input type="radio" name="q10" value="d"> D) \(\min \|y\|^2\) thỏa mãn \(Ay = b\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\max b^T y$$ thỏa mãn $$\sum y_i A_i + S = C, \ S \succeq 0$$</strong><br>
                Bài toán đối ngẫu của SDP cực đại hóa $$b^T y$$ với ma trận bù đối ngẫu nửa xác định dương $$S \succeq 0$$.
            </div>
        </div>

        <!-- Câu hỏi 11: SDP complementary slackness -->
        <div class="question" id="q11" style="display: none;">
            <h3>Câu 11: Điều kiện bù chặt trong SDP là:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) \(X \bullet S = 0\) (tức \(\text{tr}(XS) = 0\))</label>
                <label><input type="radio" name="q11" value="b"> B) \(X \bullet S = 1\)</label>
                <label><input type="radio" name="q11" value="c"> C) \(X + S = 0\)</label>
                <label><input type="radio" name="q11" value="d"> D) \(\|X - S\| = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$X \bullet S = 0$$ (tức $$\text{tr}(XS) = 0$$)</strong><br>
                Điều kiện bù chặt của SDP yêu cầu tích vô hướng vết giữa ma trận gốc và ma trận đối ngẫu bằng $$0$$ (với $$X, S \succeq 0$$, điều này tương đương với $$XS = 0$$).
            </div>
        </div>

        <!-- Câu hỏi 12: Central path for SDP -->
        <div class="question" id="q12" style="display: none;">
            <h3>Câu 12: Điều kiện đường trung tâm cho SDP là:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) \(XS = \frac{1}{t}I\)</label>
                <label><input type="radio" name="q12" value="b"> B) \(X \bullet S = \frac{n}{t}\)</label>
                <label><input type="radio" name="q12" value="c"> C) \(XS = 0\)</label>
                <label><input type="radio" name="q12" value="d"> D) \(X = S\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$XS = \frac{1}{t}I$$</strong><br>
                Trên đường trung tâm của SDP, tích ma trận $$XS$$ bằng bội số của ma trận đơn vị: $$XS = \tau I = \frac{1}{t}I$$.
            </div>
        </div>

        <!-- Câu hỏi 13: Newton direction for SDP -->
        <div class="question" id="q13" style="display: none;">
            <h3>Câu 13: Hướng Newton trong phương pháp gốc-đối ngẫu cho SDP được tìm bằng cách giải:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) Hệ phương trình tuyến tính hóa theo \((\Delta X, \Delta y, \Delta S)\)</label>
                <label><input type="radio" name="q13" value="b"> B) Chỉ theo \(\Delta X\)</label>
                <label><input type="radio" name="q13" value="c"> C) Chỉ theo \(\Delta S\)</label>
                <label><input type="radio" name="q13" value="d"> D) Bài toán phân rã trị riêng</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Hệ phương trình tuyến tính hóa theo $$(\Delta X, \Delta y, \Delta S)$$</strong><br>
                Hệ Newton cho SDP giải đồng thời bước cập nhật ma trận gốc $$\Delta X$$, vector đối ngẫu $$\Delta y$$ và ma trận đối ngẫu $$\Delta S$$.
            </div>
        </div>

        <!-- Câu hỏi 14: Polynomial complexity -->
        <div class="question" id="q14" style="display: none;">
            <h3>Câu 14: Độ phức tạp tính toán trong trường hợp xấu nhất của phương pháp điểm trong gốc-đối ngẫu là:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) Thời gian đa thức (polynomial-time)</label>
                <label><input type="radio" name="q14" value="b"> B) Thời gian hàm mũ (exponential-time)</label>
                <label><input type="radio" name="q14" value="c"> C) Thuộc lớp NP-hard</label>
                <label><input type="radio" name="q14" value="d"> D) Không có đảm bảo lý thuyết</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Thời gian đa thức (polynomial-time)</strong><br>
                Các phương pháp điểm trong có độ phức tạp thời gian đa thức trong trường hợp xấu nhất cho LP, SOCP và SDP.
            </div>
        </div>

        <!-- Câu hỏi 15: Warm start -->
        <div class="question" id="q15" style="display: none;">
            <h3>Câu 15: Khởi động ấm (warm start) trong phương pháp gốc-đối ngẫu có nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) Khởi tạo từ nghiệm của một bài toán tương tự đã giải trước đó</label>
                <label><input type="radio" name="q15" value="b"> B) Luôn bắt đầu từ gốc tọa độ</label>
                <label><input type="radio" name="q15" value="c"> C) Bắt đầu từ một điểm ngẫu nhiên</label>
                <label><input type="radio" name="q15" value="d"> D) Bắt đầu từ biên của tập khả thi</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Khởi tạo từ nghiệm của một bài toán tương tự đã giải trước đó</strong><br>
                Khởi động ấm tận dụng nghiệm của bài toán liên quan làm điểm khởi đầu nhằm rút ngắn số vòng lặp hội tụ.
            </div>
        </div>

        <!-- Câu hỏi 16: Homogeneous self-dual -->
        <div class="question" id="q16" style="display: none;">
            <h3>Câu 16: Dạng nhúng đồng nhất tự đối ngẫu (homogeneous self-dual) có ưu điểm nào sau đây?</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) Phát hiện được cả trường hợp bài toán không khả thi và không bị chặn</label>
                <label><input type="radio" name="q16" value="b"> B) Không cần tìm điểm khởi tạo khả thi</label>
                <label><input type="radio" name="q16" value="c"> C) Xử lý thống nhất mọi trạng thái nghiệm trong cùng một khuôn khổ</label>
                <label><input type="radio" name="q16" value="d"> D) Tất cả các ưu điểm trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các ưu điểm trên</strong><br>
                Dạng đồng nhất tự đối ngẫu xử lý thống nhất cả ba trường hợp (có nghiệm tối ưu, không khả thi, không bị chặn) mà không cần pha tìm điểm khả thi ban đầu.
            </div>
        </div>

        <!-- Câu hỏi 17: Centering parameter -->
        <div class="question" id="q17" style="display: none;">
            <h3>Câu 17: Tham số định tâm (centering parameter) \(\sigma\) trong phương pháp gốc-đối ngẫu có vai trò:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Cân bằng giữa việc bám sát đường trung tâm và tốc độ tiến về nghiệm tối ưu</label>
                <label><input type="radio" name="q17" value="b"> B) Luôn được cố định bằng 0</label>
                <label><input type="radio" name="q17" value="c"> C) Luôn được cố định bằng 1</label>
                <label><input type="radio" name="q17" value="d"> D) Không ảnh hưởng đến thuật toán</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Cân bằng giữa việc bám sát đường trung tâm và tốc độ tiến về nghiệm tối ưu</strong><br>
                Với $$\sigma \in [0, 1]$$, $$\sigma = 0$$ tương ứng với bước affine thuần túy (tiến nhanh nhất), còn $$\sigma = 1$$ tương ứng với bước định tâm thuần túy.
            </div>
        </div>

        <!-- Câu hỏi 18: Linear programming special case -->
        <div class="question" id="q18" style="display: none;">
            <h3>Câu 18: Với bài toán LP, phương pháp điểm trong gốc-đối ngẫu có đặc điểm nào sau đây?</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) Hệ phương trình Newton có cấu trúc tuyến tính thưa đơn giản</label>
                <label><input type="radio" name="q18" value="b"> B) Điều kiện bù chặt bị nhiễu có dạng \(x_i s_i = \frac{1}{t}\)</label>
                <label><input type="radio" name="q18" value="c"> C) Cho phép cài đặt với hiệu năng tính toán rất cao</label>
                <label><input type="radio" name="q18" value="d"> D) Tất cả các đặc điểm trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các đặc điểm trên</strong><br>
                LP là trường hợp đặc biệt có cấu trúc đơn giản, giúp phương pháp điểm trong gốc-đối ngẫu đạt hiệu quả rất cao trong thực tế.
            </div>
        </div>

        <!-- Câu hỏi 19: Convergence rate -->
        <div class="question" id="q19" style="display: none;">
            <h3>Câu 19: Tốc độ hội tụ của phương pháp điểm trong gốc-đối ngẫu là:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) Siêu tuyến tính dưới các điều kiện không suy biến phù hợp</label>
                <label><input type="radio" name="q19" value="b"> B) Luôn chỉ tuyến tính</label>
                <label><input type="radio" name="q19" value="c"> C) Luôn bậc hai ở mọi vòng lặp</label>
                <label><input type="radio" name="q19" value="d"> D) Dưới tuyến tính (sublinear)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Siêu tuyến tính dưới các điều kiện không suy biến phù hợp</strong><br>
                Dưới các giả thiết không suy biến thích hợp, phương pháp điểm trong gốc-đối ngẫu đạt tốc độ hội tụ siêu tuyến tính (thậm chí tiệm cận bậc hai).
            </div>
        </div>

        <!-- Câu hỏi 20: Modern applications -->
        <div class="question" id="q20" style="display: none;">
            <h3>Câu 20: Phương pháp điểm trong gốc-đối ngẫu được ứng dụng rộng rãi trong:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Các bộ giải tối ưu thương mại và mã nguồn mở</label>
                <label><input type="radio" name="q20" value="b"> B) Quy hoạch tuyến tính và quy hoạch bán xác định quy mô lớn</label>
                <label><input type="radio" name="q20" value="c"> C) Các bài toán tối ưu trong học máy</label>
                <label><input type="radio" name="q20" value="d"> D) Tất cả các ứng dụng trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các ứng dụng trên</strong><br>
                Phương pháp điểm trong gốc-đối ngẫu là thuật toán lõi của nhiều bộ giải hiện đại (như CPLEX, Gurobi, MOSEK, Clarabel) dùng trong công nghiệp và học máy.
            </div>
        </div>
        <!-- Câu hỏi 21: Thực hành -->
        <div class="question" id="q21" style="display: none;">
            <h3>Câu 21: Phương pháp điểm trong gốc-đối ngẫu kết hợp hai ý tưởng nền tảng nào?</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) Hàm chắn (đường trung tâm) và phương pháp Newton</label>
                <label><input type="radio" name="q21" value="b"> B) Hạ gradient và động lượng (momentum)</label>
                <label><input type="radio" name="q21" value="c"> C) Đơn hình gốc và đơn hình đối ngẫu</label>
                <label><input type="radio" name="q21" value="d"> D) SGD và Adam</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Hàm chắn (đường trung tâm) và phương pháp Newton</strong><br>
                Phương pháp điểm trong gốc-đối ngẫu dùng hệ KKT bị nhiễu từ hàm chắn kết hợp với phương pháp Newton để cập nhật đồng thời biến gốc và biến đối ngẫu.
            </div>
        </div>

        <!-- Câu hỏi 22: Thực hành -->
        <div class="question" id="q22" style="display: none;">
            <h3>Câu 22: Trong phương pháp điểm trong gốc-đối ngẫu, hệ phương trình Newton rút gọn (sau khi khử \(\Delta \lambda\)) có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) Ma trận khối đối xứng</label>
                <label><input type="radio" name="q22" value="b"> B) Ma trận tam giác</label>
                <label><input type="radio" name="q22" value="c"> C) Ma trận đường chéo</label>
                <label><input type="radio" name="q22" value="d"> D) Ma trận đơn vị</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Ma trận khối đối xứng</strong><br>
                Sau khi khử $$\Delta \lambda$$, hệ KKT trở thành hệ ma trận khối đối xứng (augmented system) thuận lợi cho phân rã LDL; hệ Newton đầy đủ ban đầu nhìn chung không đối xứng.
            </div>
        </div>

        <!-- Câu hỏi 23: Thực hành -->
        <div class="question" id="q23" style="display: none;">
            <h3>Câu 23: Cách tiếp cận dự báo – hiệu chỉnh (predictor-corrector) trong IPM thực hiện:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) Dự báo hướng tiến về nghiệm và hiệu chỉnh độ gần đường trung tâm</label>
                <label><input type="radio" name="q23" value="b"> B) Chỉ thực hiện bước dự báo</label>
                <label><input type="radio" name="q23" value="c"> C) Chỉ thực hiện bước hiệu chỉnh</label>
                <label><input type="radio" name="q23" value="d"> D) Không liên quan đến đường trung tâm</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Dự báo hướng tiến về nghiệm và hiệu chỉnh độ gần đường trung tâm</strong><br>
                Bước dự báo tìm hướng giảm nhanh khoảng cách đối ngẫu, còn bước hiệu chỉnh đảm bảo điểm lặp không lệch quá xa đường trung tâm.
            </div>
        </div>

        <!-- Câu hỏi 24: Thực hành -->
        <div class="question" id="q24" style="display: none;">
            <h3>Câu 24: Độ phức tạp tính toán tổng thể của phương pháp điểm trong cho LP là:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) $$O(n^{3.5} \log(1/\epsilon))$$</label>
                <label><input type="radio" name="q24" value="b"> B) $$O(2^n)$$</label>
                <label><input type="radio" name="q24" value="c"> C) $$O(n!)$$</label>
                <label><input type="radio" name="q24" value="d"> D) $$O(n \log n)$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$O(n^{3.5} \log(1/\epsilon))$$</strong><br>
                Thuật toán cần $$O(\sqrt{n}\log(1/\epsilon))$$ vòng lặp, mỗi vòng lặp tốn $$O(n^3)$$ phép toán phân rã ma trận, cho tổng độ phức tạp $$O(n^{3.5} \log(1/\epsilon))$$.
            </div>
        </div>

        <!-- Câu hỏi 25: Thực hành -->
        <div class="question" id="q25" style="display: none;">
            <h3>Câu 25: Thuật toán Mehrotra thuộc lớp thuật toán nào?</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) Phương pháp điểm trong gốc-đối ngẫu dự báo – hiệu chỉnh thực tế</label>
                <label><input type="radio" name="q25" value="b"> B) Phương pháp đơn hình (Simplex)</label>
                <label><input type="radio" name="q25" value="c"> C) Hạ gradient (Gradient descent)</label>
                <label><input type="radio" name="q25" value="d"> D) Nhánh và cận (Branch and bound)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Phương pháp điểm trong gốc-đối ngẫu dự báo – hiệu chỉnh thực tế</strong><br>
                Thuật toán dự báo – hiệu chỉnh của Mehrotra là một trong những cài đặt thực tế phổ biến nhất của phương pháp điểm trong gốc-đối ngẫu.
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
    q1: 'd', q2: 'a', q3: 'a', q4: 'a', q5: 'a',
    q6: 'a', q7: 'a', q8: 'a', q9: 'a', q10: 'a',
    q11: 'a', q12: 'a', q13: 'a', q14: 'a', q15: 'a',
    q16: 'd', q17: 'a', q18: 'd', q19: 'a', q20: 'd'
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
        message = '🌟 Xuất sắc! Bạn đã thành thạo primal-dual interior point methods!';
    } else if (percentage >= 80) {
        message = '👍 Rất tốt! Bạn hiểu tốt về central path và SDP.';
    } else if (percentage >= 70) {
        message = '📚 Khá ổn! Hãy xem lại Newton systems và residuals.';
    } else if (percentage >= 60) {
        message = '💪 Cần cải thiện! Ôn lại primal-dual algorithms và complementary slackness.';
    } else {
        message = '📖 Hãy học lại từ đầu về primal-dual methods nhé!';
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
