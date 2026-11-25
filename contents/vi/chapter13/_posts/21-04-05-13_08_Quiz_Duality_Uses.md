---
layout: post
title: 13-08 Bài tập trắc nghiệm - Ứng Dụng và Tương Ứng của Tính Đối Ngẫu
chapter: '13'
order: 12
owner: GitHub Copilot
lang: vi
categories:
- chapter13
lesson_type: quiz
redirect_from:
  - /contents/vi/chapter13/13_07_Quiz_Duality_Uses/
---

Đọc hiểu công thức đối ngẫu là một chuyện, nhưng phản xạ nhanh trước những tình huống "bẫy" mới thực sự cho thấy bạn đã làm chủ Chương 13. Chẳng hạn: khi bài toán gốc không lồi chặt, việc cực tiểu hóa hàm Lagrange tại $$(u^\star, v^\star)$$ có chắc chắn trả về $$x^\star$$ không? Hay nếu biến đổi tương đương hàm đối ngẫu bằng cách lấy logarit, khoảng cách đối ngẫu tính từ hàm mới còn đáng tin nữa không?

Bộ câu hỏi trắc nghiệm này được thiết kế như một bài kiểm tra phản xạ toán học toàn diện cho toàn bộ Chương 13 — từ tiêu chí dừng, chuẩn đối ngẫu, hàm liên hợp, đối ngẫu Lasso đến nón đối ngẫu và đối ngẫu kép. Trước khi bước vào phần câu hỏi, hãy dành vài phút rà lại bản đồ bốn nhóm bẫy thường gặp nhất.

## Bản đồ kiến thức nền: Bốn nhóm phản xạ cốt lõi cần kiểm tra ở Chương 13

- **Duality gap và điều kiện khôi phục nghiệm:** Nhớ rõ khoảng cách đối ngẫu $$f(x) - g(u, v)$$ chỉ là chặn trên hợp lệ khi $$x$$ khả thi nguyên thủy và $$(u, v)$$ khả thi đối ngẫu; còn để khôi phục duy nhất $$x^\star$$ từ $$L(x, u^\star, v^\star)$$ ta cần thêm điều kiện lồi chặt (hoặc kiểm tra lại tính khả thi).
- **Cặp chuẩn đối ngẫu và liên hợp của chuẩn:** Thuộc lòng bảng tra cứu nhanh: $$\ell_p \leftrightarrow \ell_q$$ ($$1/p + 1/q = 1$$), chuẩn vết $$\leftrightarrow$$ chuẩn phổ, và liên hợp của bất kỳ chuẩn nào $$\|x\|$$ luôn là hàm chỉ thị của quả cầu đơn vị chuẩn đối ngẫu $$\|y\|_* \le 1$$.
- **Dịch chuyển toán tử tuyến tính và đối ngẫu Lasso:** Nhớ quy tắc tách biến $$z = Ax$$ khiến ma trận chuyển vị $$A^T$$ nhảy sang hàm liên hợp bên kia, còn Lasso có đối ngẫu là bài toán chiếu lên khối đa diện $$\|X^T u\|_\infty \le \lambda$$.
- **Nón đối ngẫu và đối ngẫu kép:** Phân biệt rõ nón tự đối ngẫu ($$\mathbb{R}_+^n, \mathcal{Q}_n, \mathbb{S}_+^n$$) với nón nhọn/tù tổng quát, và nhớ định lý $$(K^*)^* = K$$ chỉ đúng khi $$K$$ là nón lồi đóng.

### Khung giải thích (nên đọc chậm): Giải mẫu một tình huống bẫy trắc nghiệm về tính duy nhất khi khôi phục $$x^\star$$

**Tình huống:** Xét bài toán tuyến tính $$\min_{x \in \mathbb{R}} 0 \cdot x$$ với ràng buộc $$0 \le x \le 2$$ (hoặc $$\min_{x \in \mathbb{R}^2} x_1 + x_2$$ với $$x_1 + x_2 = 1, x_1 \ge 0, x_2 \ge 0$$). Giả sử ta đã có nghiệm đối ngẫu tối ưu $$v^\star = 1$$ cho bài toán thứ hai. Liệu mọi điểm cực tiểu của $$L(x, u^\star, v^\star)$$ có phải là $$x^\star$$ không?

1. **Lập hàm Lagrange:** Với ràng buộc $$-x_1 \le 0, -x_2 \le 0$$ (nhân tử $$u_1, u_2 \ge 0$$) và $$x_1 + x_2 - 1 = 0$$ (nhân tử $$v$$):
   $$L(x, u, v) = (1 - u_1 - v)x_1 + (1 - u_2 - v)x_2 + v.$$
2. **Tìm nghiệm đối ngẫu tối ưu:** Để $$\min_x L > -\infty$$ ta cần $$1 - u_1 - v = 0$$ và $$1 - u_2 - v = 0$$, nên $$v = 1 - u_1 \le 1$$. Cực đại $$g(u, v) = v$$ đạt tại $$v^\star = 1, u_1^\star = 0, u_2^\star = 0$$, cho $$g^\star = 1 = f^\star$$ (đối ngẫu mạnh thỏa mãn!).
3. **Thử khôi phục $$x$$ từ $$L(x, u^\star, v^\star)$$:**
   Thay $$u^\star = (0, 0), v^\star = 1$$ vào $$L$$, ta thu được $$L(x, u^\star, v^\star) \equiv 1$$ — một hằng số với **mọi** $$x \in \mathbb{R}^2$$!
4. **Bài học rút ra:** Ngay cả điểm $$x = (-10, -10)$$ (hoàn toàn bất khả thi!) cũng cực tiểu hóa $$L(x, u^\star, v^\star)$$. Nguyên nhân: hàm mục tiêu tuyến tính **không lồi chặt**, nên cực tiểu của Lagrangian không duy nhất và ta bắt buộc phải lọc thêm các điều kiện khả thi nguyên thủy + bù yếu để tìm $$x^\star$$.

---

## 📚 Ôn tập lý thuyết

Trước khi làm bài tập trắc nghiệm, hãy ôn lại các khái niệm chính trong chương này:

### ⚡ **Hai ứng dụng chính của tính đối ngẫu**

**1. Khoảng cách đối ngẫu làm tiêu chí dừng:**
- **Khoảng cách đối ngẫu (duality gap):** $$f(x) - g(u,v)$$ với $$x$$ khả thi nguyên thủy và $$(u,v)$$ khả thi đối ngẫu.
- **Chặn trên sai số tối ưu:** $$f(x) - f^* \le f(x) - g(u,v)$$.
- **Kiểm tra tính tối ưu:** Nếu khoảng cách đối ngẫu bằng $$0$$ thì $$x$$ là nghiệm tối ưu.
- **Tiêu chí dừng thực tế:** Dừng thuật toán khi khoảng cách đối ngẫu nhỏ hơn ngưỡng $$\epsilon$$ cho trước.

**2. Giải bài toán nguyên thủy thông qua bài toán đối ngẫu:**
Khi có nghiệm đối ngẫu tối ưu $$(u^*, v^*)$$ và tính đối ngẫu mạnh thỏa mãn:
$$x^* = \arg\min_x L(x, u^*, v^*) = \arg\min_x \left\{ f(x) + \sum u_i^* h_i(x) + \sum v_j^* l_j(x) \right\}$$

Cách tiếp cận này đặc biệt hữu ích khi bài toán đối ngẫu dễ giải hơn bài toán nguyên thủy.

### 🔄 **Giải bài toán tách biến thông qua đối ngẫu**

**Bài toán nguyên thủy:** $$\min_x \sum_{i=1}^n f_i(x_i) \quad \text{s.t.} \quad a^T x = b$$

**Hàm đối ngẫu:**
$$g(v) = bv - \sum_{i=1}^n f_i^*(a_i v)$$

**Bài toán đối ngẫu:** $$\max_v bv - \sum_{i=1}^n f_i^*(a_i v)$$

**Khôi phục nghiệm nguyên thủy:** Khi đã có $$v^*$$ (và các $$f_i$$ lồi chặt, khả vi), giải độc lập từng phương trình $$\nabla f_i(x_i^*) = a_i v^*$$ theo từng tọa độ $$i$$.

**Ưu điểm:** Bài toán đối ngẫu chỉ còn một biến vô hướng $$v$$; các hàm liên hợp $$f_i^*$$ có thể tính song song và nhiều trường hợp có công thức dạng đóng.

### 📏 **Chuẩn đối ngẫu (Dual Norms)**

#### **Định nghĩa**
Với chuẩn $$\lVert x \rVert$$, **chuẩn đối ngẫu** $$\lVert z \rVert_*$$ được định nghĩa là:
$$\lVert z \rVert_* = \max_{\lVert x \rVert \le 1} z^T x$$

#### **Tính chất cơ bản**
- **Bất đẳng thức Cauchy–Schwarz tổng quát:** $$\lvert z^T x \rvert \le \lVert z \rVert_* \lVert x \rVert$$
- **Đối ngẫu kép:** $$\lVert x \rVert_{**} = \lVert x \rVert$$
- **Luôn là một chuẩn:** $$\lVert \cdot \rVert_*$$ là supremum của họ hàm tuyến tính nên luôn lồi và thỏa các tiên đề chuẩn.

#### **Các cặp chuẩn đối ngẫu quan trọng**
- **Chuẩn $$\ell_p$$:** $$(\lVert x \rVert_p)_* = \lVert x \rVert_q$$ với $$\frac{1}{p} + \frac{1}{q} = 1$$:
  - $$(\lVert x \rVert_1)_* = \lVert x \rVert_\infty$$
  - $$(\lVert x \rVert_2)_* = \lVert x \rVert_2$$
  - $$(\lVert x \rVert_\infty)_* = \lVert x \rVert_1$$
- **Chuẩn ma trận:** $$(\lVert X \rVert_{tr})_* = \lVert X \rVert_{op} = \sigma_1(X)$$ (giá trị kỳ dị lớn nhất).

#### **Biểu diễn chuẩn qua bài toán đối ngẫu**
Từ bài toán $$\min_y \lVert y \rVert \text{ s.t. } y = x$$, ta thu được bài toán đối ngẫu $$\max_{\lVert u \rVert_* \le 1} u^T x$$ và đẳng thức $$\lVert x \rVert = \max_{\lVert u \rVert_* \le 1} u^T x$$.

### 🎯 **Ví dụ: Đối ngẫu của bài toán LASSO**

#### **Bài toán LASSO nguyên thủy**
$$\min_\beta \frac{1}{2}\lVert y - X\beta \rVert_2^2 + \lambda \lVert \beta \rVert_1$$

#### **Đưa về dạng có ràng buộc**
$$\min_{\beta,z} \frac{1}{2}\lVert y - z \rVert_2^2 + \lambda \lVert \beta \rVert_1 \quad \text{s.t.} \quad z = X\beta$$

#### **Hàm Lagrangian và hàm đối ngẫu**
$$L(\beta,z,u) = \frac{1}{2}\lVert y - z \rVert_2^2 + \lambda \lVert \beta \rVert_1 + u^T(z - X\beta)$$

$$g(u) = \frac{1}{2}\lVert y \rVert_2^2 - \frac{1}{2}\lVert y - u \rVert_2^2 - I_{\{\lVert X^T u \rVert_\infty \le \lambda\}}(u)$$

#### **Bài toán LASSO đối ngẫu (dạng tương đương)**
$$\min_u \lVert y - u \rVert_2^2 \quad \text{s.t.} \quad \lVert X^T u \rVert_\infty \le \lambda$$

#### **Quan hệ nguyên thủy–đối ngẫu**
Điều kiện Slater được thỏa mãn nên có tính đối ngẫu mạnh, và nghiệm liên hệ bởi $$X\beta^* = y - u^*$$ (tức $$u^*$$ chính là phần dư).

### 🔗 **Hàm liên hợp và bài toán đối ngẫu**

#### **Hàm liên hợp**
$$f^*(u) = \sup_x \{u^T x - f(x)\} \iff -f^*(u) = \min_x \{f(x) - u^T x\}$$

#### **Bài toán tổng hai hàm**
Với bài toán $$\min_x f(x) + g(x)$$, viết lại thành $$\min_{x,z} f(x) + g(z) \text{ s.t. } x = z$$, ta thu được hàm đối ngẫu:
$$g(u) = \min_{x,z} f(x) + g(z) + u^T(z - x) = -f^*(u) - g^*(-u)$$

và bài toán đối ngẫu: $$\max_u -f^*(u) - g^*(-u)$$.

#### **Ví dụ áp dụng**
1. **Hàm chỉ thị:** $$\min_x f(x) + I_C(x) \Rightarrow \max_u -f^*(u) - I_C^*(-u)$$, với $$I_C^*$$ là hàm hỗ trợ của tập $$C$$.
2. **Thành phần chuẩn:** $$\min_x f(x) + \lVert x \rVert \Rightarrow \max_{\lVert u \rVert_* \le 1} -f^*(u)$$.

### 🔺 **Nón đối ngẫu (Dual Cones)**

#### **Định nghĩa**
Cho nón $$K \subseteq \mathbb{R}^n$$, **nón đối ngẫu** $$K^*$$ là:
$$K^* = \{y : y^T x \ge 0 \quad \forall x \in K\}$$

#### **Tính chất**
- $$K^*$$ luôn là nón lồi ngay cả khi $$K$$ không lồi.
- Nếu $$K$$ là nón lồi và đóng thì $$K^{**} = K$$.
- Về mặt hình học: $$y \in K^* \Leftrightarrow$$ nửa không gian $$\{x : y^T x \ge 0\}$$ chứa toàn bộ nón $$K$$.

#### **Các ví dụ quan trọng**
1. **Không gian con tuyến tính $$V$$:** $$V^* = V^\perp$$ (phần bù trực giao); ví dụ $$(\text{row}(A))^* = \text{null}(A)$$.
2. **Nón chuẩn:** Với $$K = \{(x,t) : \lVert x \rVert \le t\}$$, nón đối ngẫu là $$K^* = \{(y,s) : \lVert y \rVert_* \le s\}$$.
3. **Nón ma trận nửa xác định dương:** Tự đối ngẫu $$(\mathbb{S}_+^n)^* = \mathbb{S}_+^n$$, vì $$Y \succeq 0 \Leftrightarrow \text{tr}(YX) \ge 0 \; \forall X \succeq 0$$.

### 🎯 **Đối ngẫu trong quy hoạch nón (Conic Programming)**

- **Bài toán nguyên thủy:** $$\min_x f(x) \quad \text{s.t.} \quad Ax \in K$$
- **Bài toán đối ngẫu:** $$\max_u -f^*(A^T u) \quad \text{s.t.} \quad u \in K^*$$ (suy ra từ hàm hỗ trợ $$I_K^*(-u) = I_{K^*}(u)$$).
- **Ví dụ SOCP:** Bài toán $$\min c^T x \text{ s.t. } \lVert A_i x + b_i \rVert_2 \le c_i^T x + d_i$$ viết gọn thành $$Ax + b \in K$$ (với $$K$$ là tích các nón bậc hai) có đối ngẫu $$\max -b^T u \text{ s.t. } A^T u = c, u \in K^*$$.

### 💡 **Ví dụ minh họa**

#### **Cực tiểu hóa chuẩn $$\ell_2$$ có ràng buộc tuyến tính**
- **Bài toán nguyên thủy:** $$\min_x \lVert x \rVert_2 \quad \text{s.t.} \quad Ax = b$$
- **Bài toán đối ngẫu:** $$\max_{\lVert A^T u \rVert_2 \le 1} b^T u$$ (suy từ hàm Lagrangian $$L(x, u) = \lVert x \rVert_2 + u^T(b - Ax)$$).
- **Diễn giải:** Tìm $$u$$ thỏa $$\lVert A^T u \rVert_2 \le 1$$ để cực đại hóa $$b^T u$$; khi hệ $$Ax = b$$ khả thi, giá trị tối ưu bằng chuẩn nhỏ nhất $$\lVert x^* \rVert_2$$ của nghiệm chuẩn cực tiểu $$x^* = A^+ b$$.

#### **Cực tiểu hóa chuẩn $$\ell_1$$ có ràng buộc tuyến tính**
- **Bài toán nguyên thủy:** $$\min_x \lVert x \rVert_1 \quad \text{s.t.} \quad Ax = b$$
- **Bài toán đối ngẫu:** $$\max_{\lVert A^T u \rVert_\infty \le 1} b^T u$$
- **Diễn giải hình học:** Tìm $$u$$ thuộc đa diện khả thi đối ngẫu $$\{u : \lVert A^T u \rVert_\infty \le 1\}$$ sao cho tích vô hướng $$b^T u$$ đạt cực đại.

### 🛠️ **Lưu ý thực hành và ứng dụng**

- **Khi nào nên giải bài toán đối ngẫu:** Khi bài toán đối ngẫu có ít biến hơn, cấu trúc ràng buộc đơn giản hơn, tách biến tốt cho tính toán song song, hoặc khi cần theo dõi khoảng cách đối ngẫu làm tiêu chí dừng.
- **Các lỗi cần tránh:** Bỏ qua điều kiện chuẩn ràng buộc đảm bảo đối ngẫu mạnh, đánh giá sai sai số số học của khoảng cách đối ngẫu, hoặc chuẩn hóa tỷ lệ biến chưa phù hợp.
- **Ứng dụng thực tế:** Học máy (SVM, LASSO, hoàn thiện ma trận với chuẩn hạt nhân), xử lý tín hiệu (cảm biến nén với chuẩn $$\ell_1$$, khử nhiễu ảnh tổng biến phân), vận trù học (luồng cực đại–lát cắt cực tiểu, phân bổ tài nguyên) và tài chính (tối ưu danh mục đầu tư, quản trị rủi ro).

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

Bài tập trắc nghiệm này kiểm tra kiến thức về các ứng dụng và tương ứng của tính đối ngẫu, gồm hàm liên hợp, chuẩn đối ngẫu, đối ngẫu LASSO, nón đối ngẫu và các tính chất đối ngẫu liên quan.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>🔄 Quiz: Ứng Dụng và Tương Ứng của Tính Đối Ngẫu</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 5%"></div>
        </div>
        <div class="score-display" id="score-display">Câu hỏi: <span id="current-q">1</span> / <span id="total-q">20</span></div>
    </div>

    <div id="quiz-content">
        <!-- Câu hỏi 1: Conjugate function definition -->
        <div class="question" id="q1" style="display: block;">
            <h3>Câu 1: Conjugate function $$f^*(y)$$ được định nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) $$f^*(y) = \max_x (y^T x - f(x))$$</label>
                <label><input type="radio" name="q1" value="b"> B) $$f^*(y) = \min_x (y^T x - f(x))$$</label>
                <label><input type="radio" name="q1" value="c"> C) $$f^*(y) = \max_x (y^T x + f(x))$$</label>
                <label><input type="radio" name="q1" value="d"> D) $$f^*(y) = f(y)$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f^*(y) = \max_x (y^T x - f(x))$$</strong><br>
                Hàm liên hợp (biến đổi Legendre–Fenchel) là giá trị supremum của hiệu giữa hàm tuyến tính $$y^T x$$ và $$f(x)$$.
            </div>
        </div>

        <!-- Câu hỏi 2: Conjugate properties -->
        <div class="question" id="q2" style="display: none;">
            <h3>Câu 2: Conjugate function $$f^*$$ có tính chất:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) Luôn convex</label>
                <label><input type="radio" name="q2" value="b"> B) Luôn concave</label>
                <label><input type="radio" name="q2" value="c"> C) Có cùng tính lồi với $$f$$</label>
                <label><input type="radio" name="q2" value="d"> D) Không xác định được</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Luôn convex</strong><br>
                Hàm liên hợp luôn lồi vì là supremum theo điểm của một họ các hàm affine, bất kể bản thân $$f$$ có lồi hay không.
            </div>
        </div>

        <!-- Câu hỏi 3: Double conjugate -->
        <div class="question" id="q3" style="display: none;">
            <h3>Câu 3: Nếu $$f$$ là convex và lower semicontinuous, thì $$f^{**}$$ bằng:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) $$f$$</label>
                <label><input type="radio" name="q3" value="b"> B) $$-f$$</label>
                <label><input type="radio" name="q3" value="c"> C) $$f^*$$</label>
                <label><input type="radio" name="q3" value="d"> D) $$0$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f$$</strong><br>
                Theo định lý Fenchel–Moreau, nếu $$f$$ là hàm lồi và nửa liên tục dưới (đóng) thì $$f^{**} = f$$.
            </div>
        </div>

        <!-- Câu hỏi 4: Dual norm definition -->
        <div class="question" id="q4" style="display: none;">
            <h3>Câu 4: Dual norm $$\lVert x \rVert_*$$ được định nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) $$\lVert x \rVert_* = \max_{\lVert z \rVert \leq 1} z^T x$$</label>
                <label><input type="radio" name="q4" value="b"> B) $$\lVert x \rVert_* = \min_{\lVert z \rVert \leq 1} z^T x$$</label>
                <label><input type="radio" name="q4" value="c"> C) $$\lVert x \rVert_* = \max_{\lVert z \rVert = 1} z^T x$$</label>
                <label><input type="radio" name="q4" value="d"> D) $$\lVert x \rVert_* = \lVert x \rVert$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\|x\|_* = \max_{\|z\| \leq 1} z^T x$$</strong><br>
                Chuẩn đối ngẫu là giá trị lớn nhất của tích vô hướng với các vector nằm trong quả cầu đơn vị của chuẩn gốc.
            </div>
        </div>

        <!-- Câu hỏi 5: Lp dual norm -->
        <div class="question" id="q5" style="display: none;">
            <h3>Câu 5: Dual norm của $$\ell_p$$ norm là:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) $$\ell_p$$ norm</label>
                <label><input type="radio" name="q5" value="b"> B) $$\ell_q$$ norm với $$1/p + 1/q = 1$$</label>
                <label><input type="radio" name="q5" value="c"> C) \(\ell_\infty\) norm</label>
                <label><input type="radio" name="q5" value="d"> D) \(\ell_1\) norm</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$\ell_q$$ norm với $$1/p + 1/q = 1$$</strong><br>
                Theo cặp liên hợp Hölder, chuẩn đối ngẫu của $$\ell_p$$ là $$\ell_q$$ với $$1/p + 1/q = 1$$; đặc biệt chuẩn đối ngẫu của $$\ell_1$$ là $$\ell_\infty$$.
            </div>
        </div>

        <!-- Câu hỏi 6: Holder inequality -->
        <div class="question" id="q6" style="display: none;">
            <h3>Câu 6: Hölder inequality có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) \(|x^T y| \leq \|x\|_p \|y\|_q\) với \(1/p + 1/q = 1\)</label>
                <label><input type="radio" name="q6" value="b"> B) \(|x^T y| \leq \|x\|_p \|y\|_p\)</label>
                <label><input type="radio" name="q6" value="c"> C) \(|x^T y| \geq \|x\|_p \|y\|_q\)</label>
                <label><input type="radio" name="q6" value="d"> D) \(\|x + y\|_p \leq \|x\|_p + \|y\|_p\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$|x^T y| \leq \|x\|_p \|y\|_q$$ với $$1/p + 1/q = 1$$</strong><br>
                Bất đẳng thức Hölder là dạng tổng quát của bất đẳng thức Cauchy–Schwarz, liên hệ tích vô hướng với cặp chuẩn đối ngẫu.
            </div>
        </div>

        <!-- Câu hỏi 7: Nuclear norm dual -->
        <div class="question" id="q7" style="display: none;">
            <h3>Câu 7: Dual norm của nuclear norm (trace norm) là:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) Frobenius norm</label>
                <label><input type="radio" name="q7" value="b"> B) Operator norm (spectral norm)</label>
                <label><input type="radio" name="q7" value="c"> C) Nuclear norm</label>
                <label><input type="radio" name="q7" value="d"> D) \(\ell_1\) norm của singular values</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Operator norm (spectral norm)</strong><br>
                Chuẩn đối ngẫu của chuẩn hạt nhân (nuclear/trace norm) $$\|X\|_* = \sum \sigma_i$$ là chuẩn toán tử $$\|X\|_{op} = \sigma_1$$ (giá trị kỳ dị lớn nhất).
            </div>
        </div>

        <!-- Câu hỏi 8: LASSO dual problem -->
        <div class="question" id="q8" style="display: none;">
            <h3>Câu 8: LASSO dual problem có constraint:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) \(\|A^T u\|_\infty \leq \lambda\)</label>
                <label><input type="radio" name="q8" value="b"> B) \(\|A^T u\|_1 \leq \lambda\)</label>
                <label><input type="radio" name="q8" value="c"> C) \(\|A^T u\|_2 \leq \lambda\)</label>
                <label><input type="radio" name="q8" value="d"> D) \(\|u\|_2 \leq \lambda\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\|A^T u\|_\infty \leq \lambda$$</strong><br>
                Bài toán LASSO đối ngẫu có ràng buộc $$\|A^T u\|_\infty \leq \lambda$$ vì chuẩn đối ngẫu của chuẩn $$\ell_1$$ là chuẩn $$\ell_\infty$$.
            </div>
        </div>

        <!-- Câu hỏi 9: Conjugate of quadratic -->
        <div class="question" id="q9" style="display: none;">
            <h3>Câu 9: Conjugate của \(f(x) = \frac{1}{2}x^T Q x\) với \(Q \succ 0\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) \(f^*(y) = \frac{1}{2}y^T Q^{-1} y\)</label>
                <label><input type="radio" name="q9" value="b"> B) \(f^*(y) = \frac{1}{2}y^T Q y\)</label>
                <label><input type="radio" name="q9" value="c"> C) \(f^*(y) = y^T Q^{-1} y\)</label>
                <label><input type="radio" name="q9" value="d"> D) \(f^*(y) = \frac{1}{2}y^T Q^{-2} y\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f^*(y) = \frac{1}{2}y^T Q^{-1} y$$</strong><br>
                Hàm liên hợp của dạng toàn phương $$\frac{1}{2}x^T Q x$$ (với $$Q \succ 0$$) là dạng toàn phương $$\frac{1}{2}y^T Q^{-1} y$$.
            </div>
        </div>

        <!-- Câu hỏi 10: Conjugate of indicator -->
        <div class="question" id="q10" style="display: none;">
            <h3>Câu 10: Conjugate của indicator function \(I_C(x)\) của tập lồi \(C\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) \(I_C^*(y) = \sup_{x \in C} y^T x\)</label>
                <label><input type="radio" name="q10" value="b"> B) \(I_C^*(y) = \inf_{x \in C} y^T x\)</label>
                <label><input type="radio" name="q10" value="c"> C) \(I_C^*(y) = I_C(y)\)</label>
                <label><input type="radio" name="q10" value="d"> D) \(I_C^*(y) = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$I_C^*(y) = \sup_{x \in C} y^T x$$</strong><br>
                Hàm liên hợp của hàm chỉ thị $$I_C$$ chính là hàm hỗ trợ (support function) của tập $$C$$.
            </div>
        </div>

        <!-- Câu hỏi 11: Dual cone definition -->
        <div class="question" id="q11" style="display: none;">
            <h3>Câu 11: Dual cone \(K^*\) của cone \(K\) được định nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) \(K^* = \{y : y^T x \geq 0 \text{ với mọi } x \in K\}\)</label>
                <label><input type="radio" name="q11" value="b"> B) \(K^* = \{y : y^T x \leq 0 \text{ với mọi } x \in K\}\)</label>
                <label><input type="radio" name="q11" value="c"> C) \(K^* = \{y : y^T x = 0 \text{ với mọi } x \in K\}\)</label>
                <label><input type="radio" name="q11" value="d"> D) \(K^* = K\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$K^* = \{y : y^T x \geq 0 \text{ với mọi } x \in K\}$$</strong><br>
                Nón đối ngẫu gồm tất cả các vector tạo góc không tù (tích vô hướng không âm) với mọi vector trong nón gốc.
            </div>
        </div>

        <!-- Câu hỏi 12: Self-dual cone -->
        <div class="question" id="q12" style="display: none;">
            <h3>Câu 12: Cone nào sau đây là self-dual?</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) Positive orthant \(\mathbb{R}_+^n\)</label>
                <label><input type="radio" name="q12" value="b"> B) Second-order cone (Lorentz cone)</label>
                <label><input type="radio" name="q12" value="c"> C) Positive semidefinite cone</label>
                <label><input type="radio" name="q12" value="d"> D) Tất cả các cone trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các cone trên</strong><br>
                Nón không âm $$\mathbb{R}_+^n$$, nón bậc hai và nón ma trận nửa xác định dương đều tự đối ngẫu ($$K^* = K$$).
            </div>
        </div>

        <!-- Câu hỏi 13: Conjugate of norm -->
        <div class="question" id="q13" style="display: none;">
            <h3>Câu 13: Conjugate của norm \(\|x\|\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) \(f^*(y) = I_{\{\|y\|_* \leq 1\}}(y)\)</label>
                <label><input type="radio" name="q13" value="b"> B) \(f^*(y) = \|y\|_*\)</label>
                <label><input type="radio" name="q13" value="c"> C) \(f^*(y) = \|y\|\)</label>
                <label><input type="radio" name="q13" value="d"> D) \(f^*(y) = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f^*(y) = I_{\{\|y\|_* \leq 1\}}(y)$$</strong><br>
                Hàm liên hợp của một chuẩn là hàm chỉ thị của quả cầu đơn vị ứng với chuẩn đối ngẫu.
            </div>
        </div>

        <!-- Câu hỏi 14: Fenchel duality -->
        <div class="question" id="q14" style="display: none;">
            <h3>Câu 14: Fenchel duality theorem áp dụng cho bài toán \(\min f(x) + g(Ax)\):</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) \(\min f(x) + g(Ax) = \max -f^*(-A^T y) - g^*(y)\)</label>
                <label><input type="radio" name="q14" value="b"> B) \(\min f(x) + g(Ax) = \max f^*(A^T y) + g^*(y)\)</label>
                <label><input type="radio" name="q14" value="c"> C) \(\min f(x) + g(Ax) = \min f^*(x) + g^*(Ax)\)</label>
                <label><input type="radio" name="q14" value="d"> D) Không có mối liên hệ</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\min f(x) + g(Ax) = \max -f^*(-A^T y) - g^*(y)$$</strong><br>
                Định lý đối ngẫu Fenchel liên kết bài toán nguyên thủy và bài toán đối ngẫu thông qua các hàm liên hợp.
            </div>
        </div>

        <!-- Câu hỏi 15: Legendre transform -->
        <div class="question" id="q15" style="display: none;">
            <h3>Câu 15: Legendre transform được sử dụng khi:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) \(f\) là convex và differentiable</label>
                <label><input type="radio" name="q15" value="b"> B) \(f\) là concave</label>
                <label><input type="radio" name="q15" value="c"> C) \(f\) là linear</label>
                <label><input type="radio" name="q15" value="d"> D) \(f\) là non-convex</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f$$ là convex và differentiable</strong><br>
                Biến đổi Legendre là trường hợp riêng của hàm liên hợp khi $$f$$ lồi và khả vi.
            </div>
        </div>

        <!-- Câu hỏi 16: Moreau envelope -->
        <div class="question" id="q16" style="display: none;">
            <h3>Câu 16: Moreau envelope \(M_\lambda f(x)\) liên quan đến:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) Proximal operator</label>
                <label><input type="radio" name="q16" value="b"> B) Conjugate function</label>
                <label><input type="radio" name="q16" value="c"> C) Smoothing của \(f\)</label>
                <label><input type="radio" name="q16" value="d"> D) Tất cả các điều trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các điều trên</strong><br>
                Bao Moreau liên hệ chặt với toán tử cận (proximal operator), hàm liên hợp và tạo ra xấp xỉ trơn cho hàm $$f$$.
            </div>
        </div>

        <!-- Câu hỏi 17: Convex conjugate inequality -->
        <div class="question" id="q17" style="display: none;">
            <h3>Câu 17: Fenchel-Young inequality phát biểu rằng:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) \(f(x) + f^*(y) \geq x^T y\)</label>
                <label><input type="radio" name="q17" value="b"> B) \(f(x) + f^*(y) \leq x^T y\)</label>
                <label><input type="radio" name="q17" value="c"> C) \(f(x) + f^*(y) = x^T y\)</label>
                <label><input type="radio" name="q17" value="d"> D) \(f(x) - f^*(y) \geq x^T y\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$f(x) + f^*(y) \geq x^T y$$</strong><br>
                Bất đẳng thức Fenchel–Young khẳng định $$f(x) + f^*(y) \geq x^T y$$, và dấu bằng xảy ra khi $$y \in \partial f(x)$$.
            </div>
        </div>

        <!-- Câu hỏi 18: Dual problem solving -->
        <div class="question" id="q18" style="display: none;">
            <h3>Câu 18: Khi nào nên giải dual problem thay vì primal?</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) Khi dual có ít variables hơn</label>
                <label><input type="radio" name="q18" value="b"> B) Khi dual có structure đơn giản hơn</label>
                <label><input type="radio" name="q18" value="c"> C) Khi có strong duality</label>
                <label><input type="radio" name="q18" value="d"> D) Tất cả các trường hợp trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các trường hợp trên</strong><br>
                Giải bài toán đối ngẫu có lợi khi số biến ít hơn, cấu trúc ràng buộc đơn giản hơn hoặc thuận tiện tính toán hơn, với điều kiện thỏa mãn tính đối ngẫu mạnh.
            </div>
        </div>

        <!-- Câu hỏi 19: Conjugate of max -->
        <div class="question" id="q19" style="display: none;">
            <h3>Câu 19: Conjugate của \(f(x) = \max\{f_1(x), f_2(x)\}\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) \(f^*(y) = \max\{f_1^*(y), f_2^*(y)\}\)</label>
                <label><input type="radio" name="q19" value="b"> B) \(f^*(y) = \min\{f_1^*(y), f_2^*(y)\}\)</label>
                <label><input type="radio" name="q19" value="c"> C) \(f^*(y) = f_1^*(y) + f_2^*(y)\)</label>
                <label><input type="radio" name="q19" value="d"> D) \(f^*(y) = \inf\{\lambda_1 f_1^*(y_1/\lambda_1) + \lambda_2 f_2^*(y_2/\lambda_2) : y_1 + y_2 = y,\ \lambda_1 + \lambda_2 = 1, \lambda_i \geq 0\}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) $$f^*(y) = \inf\{\lambda_1 f_1^*(y_1/\lambda_1) + \lambda_2 f_2^*(y_2/\lambda_2) : y_1 + y_2 = y,\ \lambda_1 + \lambda_2 = 1, \lambda_i \geq 0\}$$</strong><br>
                Với $$f_1, f_2$$ lồi, đóng: conjugate của max là bao lồi (convex hull) của $$\min\{f_1^*, f_2^*\}$$, chính là công thức D (dùng perspective). Đáp án B chỉ là $$\min\{f_1^*, f_2^*\}$$, nói chung không lồi nên không thể là một conjugate. Ví dụ: $$\max\{x, -x\} = |x|$$ có conjugate $$I_{[-1,1]}$$, trong khi $$\min\{I_{\{1\}}, I_{\{-1\}}\} = I_{\{-1,1\}}$$.
            </div>
        </div>

        <!-- Câu hỏi 20: Applications -->
        <div class="question" id="q20" style="display: none;">
            <h3>Câu 20: Conjugate duality được ứng dụng trong:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Machine learning (regularization, kernel methods)</label>
                <label><input type="radio" name="q20" value="b"> B) Signal processing (compressed sensing, denoising)</label>
                <label><input type="radio" name="q20" value="c"> C) Economics (utility theory, market equilibrium)</label>
                <label><input type="radio" name="q20" value="d"> D) Tất cả các lĩnh vực trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các lĩnh vực trên</strong><br>
                Đối ngẫu liên hợp được ứng dụng rộng rãi trong học máy (điều chuẩn), xử lý tín hiệu (biểu diễn thưa), kinh tế học (tối đa hóa độ thỏa dụng) và nhiều lĩnh vực khác.
            </div>
        </div>
        <!-- Câu hỏi 21: Thực hành -->
        <div class="question" id="q21" style="display: none;">
            <h3>Câu 21: Sensitivity analysis trong tối ưu hóa nghiên cứu:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) Thay đổi nghiệm khi tham số thay đổi</label>
                <label><input type="radio" name="q21" value="b"> B) Độ nhạy của thuật toán</label>
                <label><input type="radio" name="q21" value="c"> C) Tốc độ hội tụ</label>
                <label><input type="radio" name="q21" value="d"> D) Độ chính xác số</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Thay đổi nghiệm khi tham số thay đổi</strong><br>
                Phân tích độ nhạy nghiên cứu mức độ thay đổi của giá trị và nghiệm tối ưu khi các tham số của bài toán biến thiên.
            </div>
        </div>

        <!-- Câu hỏi 22: Thực hành -->
        <div class="question" id="q22" style="display: none;">
            <h3>Câu 22: Trong LP, shadow price của ràng buộc $$i$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) Giá trị của dual variable $$y_i^*$$</label>
                <label><input type="radio" name="q22" value="b"> B) Giá trị của primal variable</label>
                <label><input type="radio" name="q22" value="c"> C) Hệ số trong hàm mục tiêu</label>
                <label><input type="radio" name="q22" value="d"> D) Slack variable</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Giá trị của dual variable $$y_i^*$$</strong><br>
                Giá bóng (shadow price) chính là biến đối ngẫu tối ưu, phản ánh tốc độ thay đổi biên của giá trị tối ưu khi nới lỏng ràng buộc thêm một đơn vị.
            </div>
        </div>

        <!-- Câu hỏi 23: Thực hành -->
        <div class="question" id="q23" style="display: none;">
            <h3>Câu 23: Envelope theorem trong tối ưu hóa cho biết:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) $$\frac{\partial f^*(\theta)}{\partial \theta} = \frac{\partial L}{\partial \theta}$$</label>
                <label><input type="radio" name="q23" value="b"> B) $$\frac{\partial f^*}{\partial x} = 0$$</label>
                <label><input type="radio" name="q23" value="c"> C) $$\frac{\partial^2 f^*}{\partial \theta^2} = 0$$</label>
                <label><input type="radio" name="q23" value="d"> D) $$f^*(\theta) = \text{const}$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\frac{\partial f^*(\theta)}{\partial \theta} = \frac{\partial L}{\partial \theta}$$</strong><br>
                Định lý bao (envelope theorem) cho biết đạo hàm của hàm giá trị tối ưu theo tham số bằng đạo hàm riêng của hàm Lagrangian theo tham số đó tại điểm tối ưu.
            </div>
        </div>

        <!-- Câu hỏi 24: Thực hành -->
        <div class="question" id="q24" style="display: none;">
            <h3>Câu 24: Parametric programming nghiên cứu bài toán:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) $$\min f(x,\theta)$$ với $$g(x,\theta) \leq 0$$</label>
                <label><input type="radio" name="q24" value="b"> B) $$\min f(x)$$ với $$g(x) \leq \theta$$</label>
                <label><input type="radio" name="q24" value="c"> C) Cả A và B</label>
                <label><input type="radio" name="q24" value="d"> D) Không có tham số</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) Cả A và B</strong><br>
                Parametric programming xem xét bài toán tối ưu với tham số trong hàm mục tiêu và/hoặc ràng buộc.
            </div>
        </div>

        <!-- Câu hỏi 25: Thực hành -->
        <div class="question" id="q25" style="display: none;">
            <h3>Câu 25: Trong portfolio optimization, khi risk aversion tăng:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) Chọn portfolio ít rủi ro hơn</label>
                <label><input type="radio" name="q25" value="b"> B) Chọn portfolio rủi ro hơn</label>
                <label><input type="radio" name="q25" value="c"> C) Không thay đổi</label>
                <label><input type="radio" name="q25" value="d"> D) Tối đa hóa return</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Chọn portfolio ít rủi ro hơn</strong><br>
                Hệ số ngại rủi ro (risk aversion) càng cao thì danh mục đầu tư tối ưu càng ưu tiên phương sai (rủi ro) thấp hơn.
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
    q1: 'a', q2: 'a', q3: 'a', q4: 'a', q5: 'b',
    q6: 'a', q7: 'b', q8: 'a', q9: 'a', q10: 'a',
    q11: 'a', q12: 'd', q13: 'a', q14: 'a', q15: 'a',
    q16: 'd', q17: 'a', q18: 'd', q19: 'd', q20: 'd'
,
    q21: 'a', q22: 'a', q23: 'a', q24: 'c', q25: 'a'};

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
        message = '🌟 Xuất sắc! Bạn đã thành thạo advanced duality theory!';
    } else if (percentage >= 80) {
        message = '👍 Rất tốt! Bạn hiểu tốt về conjugate functions và dual norms.';
    } else if (percentage >= 70) {
        message = '📚 Khá ổn! Hãy xem lại conjugate properties và Fenchel duality.';
    } else if (percentage >= 60) {
        message = '💪 Cần cải thiện! Ôn lại conjugate functions và dual cones.';
    } else {
        message = '📖 Hãy học lại từ đầu về advanced duality concepts nhé!';
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
