---
layout: post
title: "10-06 Bài tập trắc nghiệm - Tính Đối Ngẫu trong Quy Hoạch Tuyến Tính"
chapter: "10"
order: 7
owner: "GitHub Copilot"
lang: vi
categories:
  - chapter10
lesson_type: quiz
---

## Ôn tập lý thuyết

Trước khi làm bài tập, hãy ôn lại các khái niệm chính trong chương này:

### **Tính Đối Ngẫu trong Linear Programming (LP Duality)**

#### **Ý tưởng cơ bản**
Tính đối ngẫu trong LP xuất phát từ việc tìm **cận dưới** cho giá trị tối ưu của bài toán nguyên thủy (primal).

**Nguyên lý:** Nếu có thể biểu diễn hàm mục tiêu như **tổ hợp tuyến tính** của các ràng buộc, ta có thể tìm được cận dưới.

#### **Từ ví dụ đơn giản đến tổng quát**

**Ví dụ 1:** Ràng buộc chứa hàm mục tiêu
$$\min_{x,y} x + y \quad \text{s.t.} \quad x + y \ge 2, \quad x,y \ge 0$$

**Cận dưới hiển nhiên:** $$B = 2$$

**Ví dụ 2:** Biểu diễn hàm mục tiêu qua tổ hợp tuyến tính
$$\min_{x,y} x + 3y \quad \text{s.t.} \quad x + y \ge 2, \quad x,y \ge 0$$

**Tổ hợp tuyến tính:**
$$1 \cdot (x + y) + 0 \cdot x + 2 \cdot y = x + 3y \ge 2$$

**Cận dưới:** $$B = 2$$

### 📏 **Xây Dựng Bài Toán Đối Ngẫu**

#### **Bài toán nguyên thủy tổng quát**
$$\min_x c^T x \quad \text{s.t.} \quad Ax = b, \quad Gx \le h$$

#### **Phương pháp xây dựng đối ngẫu**
1. **Định nghĩa biến đối ngẫu:** $$u$$ (cho ràng buộc đẳng thức), $$v \ge 0$$ (cho ràng buộc bất đẳng thức)
2. **Tạo tổ hợp tuyến tính:** $$u^T(Ax - b) + v^T(Gx - h) \le 0$$
3. **Sắp xếp để tách hàm mục tiêu:** $$(-A^T u - G^T v)^T x \ge -b^T u - h^T v$$
4. **Điều kiện khớp:** $$c = -A^T u - G^T v$$

#### **Bài toán đối ngẫu**
$$\max_{u,v} -b^T u - h^T v \quad \text{s.t.} \quad c = -A^T u - G^T v, \quad v \ge 0$$

### 🔄 **Quy Tắc Chuyển Đổi Primal-Dual**

| **Primal** | **Dual** |
|------------|----------|
| $$\min$$ | $$\max$$ |
| $$Ax = b$$ | $$u$$ không ràng buộc |
| $$Gx \le h$$ | $$v \ge 0$$ |
| $$x \ge 0$$ | Ràng buộc bất đẳng thức trong dual |
| $$x$$ không ràng buộc | Ràng buộc đẳng thức trong dual |

#### **Ví dụ chuyển đổi**
**Primal:**
$$\min_{x,y} px + qy \quad \text{s.t.} \quad x \ge 0, \quad y \le 1, \quad 3x + y = 2$$

**Dual:**
$$\max_{a,b,c} 2c - b \quad \text{s.t.} \quad a + 3c = p, \quad -b + c = q, \quad a,b \ge 0$$

### 🌊 **Ví Dụ: Max Flow - Min Cut**

#### **Bài toán Max Flow**
Tìm luồng tối đa từ nguồn $$s$$ đến đích $$t$$ trong đồ thị có hướng.

$$\max \sum_{(s,j) \in E} f_{sj} \quad \text{s.t.} \begin{cases}
f_{ij} \ge 0, \quad f_{ij} \le c_{ij} & \forall (i,j) \in E \\
\sum_{(i,k) \in E} f_{ik} = \sum_{(k,j) \in E} f_{kj} & \forall k \in V \setminus \{s,t\}
\end{cases}$$

#### **Bài toán Min Cut**
Tìm cắt có công suất tối thiểu phân tách $$s$$ và $$t$$.

$$\min \sum_{(i,j) \in E} b_{ij} c_{ij} \quad \text{s.t.} \begin{cases}
b_{ij} \ge x_i - x_j & \forall (i,j) \in E \\
x_i, b_{ij} \in \{0,1\} & \forall i,j \\
x_s = 1, x_t = 0
\end{cases}$$

#### **Mối quan hệ đối ngẫu**
**Dual của Max Flow = LP relaxation của Min Cut**

$$\text{Max Flow Value} \le \text{Dual LP} = \text{LP Relaxed Min Cut} \le \text{Min Cut Capacity}$$

**Định lý Max-Flow Min-Cut:** Cả ba giá trị đều bằng nhau!

### **Lagrangian Approach**

#### **Hàm Lagrangian**
Cho bài toán tối ưu tổng quát:
$$\min_x f(x) \quad \text{s.t.} \quad Ax = b, \quad Gx \le h$$

**Hàm Lagrangian:**
$$L(x,u,v) = f(x) + u^T(Ax - b) + v^T(Gx - h)$$

#### **Dual function**
$$g(u,v) = \min_x L(x,u,v)$$

**Tính chất:** $$g(u,v) \le f^*$$ với mọi $$v \ge 0$$ (weak duality)

#### **Bài toán đối ngẫu Lagrangian**
$$\max_{u,v} g(u,v) \quad \text{s.t.} \quad v \ge 0$$

#### **Cho LP:**
$$g(u,v) = \min_x (c + A^T u + G^T v)^T x - b^T u - h^T v$$

$$= \begin{cases}
-b^T u - h^T v & \text{if } c + A^T u + G^T v = 0 \\
-\infty & \text{otherwise}
\end{cases}$$

**Kết quả:** Giống dual LP truyền thống!

### 🎮 **Matrix Games**

#### **Thiết lập game**
- **Hai người chơi:** J (hàng) và R (cột)
- **Ma trận payout:** $$P$$ (J trả cho R)
- **Mixed strategies:** $$x$$ (J), $$y$$ (R)
- **Expected payout:** $$x^T P y$$

#### **Quan điểm của J (minimizer)**
R được biết trước strategy của J, nên J muốn minimize expected payout trong trường hợp xấu nhất:
$$\min_x \max_{i=1,\ldots,n} (P^T x)_i \quad \text{s.t.} \quad x \ge 0, \quad \mathbf{1}^T x = 1$$

**Reformulation:**
$$\min_{x,t} t \quad \text{s.t.} \quad x \ge 0, \quad \mathbf{1}^T x = 1, \quad P^T x \preceq t \mathbf{1}$$

#### **Quan điểm của R (maximizer)**
J được biết trước strategy của R, nên R muốn maximize expected payout trong trường hợp xấu nhất:
$$\max_y \min_{j=1,\ldots,m} (Py)_j \quad \text{s.t.} \quad y \ge 0, \quad \mathbf{1}^T y = 1$$

**Reformulation:**
$$\max_{y,v} v \quad \text{s.t.} \quad y \ge 0, \quad \mathbf{1}^T y = 1, \quad Py \succeq v \mathbf{1}$$

#### **Von Neumann's Minimax Theorem**
Hai bài toán trên là **primal-dual** của nhau và có cùng giá trị tối ưu:
$$\min_x \max_y x^T P y = \max_y \min_x x^T P y$$

**Lý do:** $$x^T P y$$ song tuyến tính (lồi theo $$x$$, lõm theo $$y$$) và các simplex là compact, lồi; hơn nữa đây là một cặp LP đối ngẫu nên strong duality luôn đúng.

### **Weak vs Strong Duality**

#### **Weak Duality**
**Luôn đúng:** Giá trị dual ≤ Giá trị primal
$$\max_{u,v} g(u,v) \le \min_x f(x)$$

**Duality gap:** $$f^* - g^* \ge 0$$

#### **Strong Duality**
**Điều kiện đặc biệt:** Giá trị dual = Giá trị primal
$$\max_{u,v} g(u,v) = \min_x f(x)$$

**Duality gap:** $$f^* - g^* = 0$$

#### **Khi nào Strong Duality xảy ra trong LP:**
- **Slater's condition:** Tồn tại điểm strictly feasible
- **Cho LP:** Nếu một trong primal hoặc dual khả thi thì strong duality xảy ra
- **Trường hợp ngoại lệ:** Cả primal và dual đều infeasible

### 🔄 **Các Dạng Chuẩn của LP**

#### **Standard form**
$$\min c^T x \quad \text{s.t.} \quad Ax = b, \quad x \ge 0$$

**Dual:**
$$\max b^T u \quad \text{s.t.} \quad A^T u \le c$$

#### **Inequality form**
$$\min c^T x \quad \text{s.t.} \quad Ax \le b$$

**Dual:**
$$\max -b^T u \quad \text{s.t.} \quad A^T u = -c, \quad u \ge 0$$

#### **General form**
$$\min c^T x \quad \text{s.t.} \quad Ax = b, \quad Gx \le h$$

**Dual:**
$$\max -b^T u - h^T v \quad \text{s.t.} \quad -A^T u - G^T v = c, \quad v \ge 0$$

### 🛠️ **Kỹ Thuật Thực Hành**

#### **Xây dựng dual từ primal:**
1. **Xác định dạng bài toán:** Min hay max, ràng buộc đẳng thức hay bất đẳng thức
2. **Áp dụng quy tắc chuyển đổi:** Theo bảng primal-dual
3. **Kiểm tra tính đúng đắn:** Weak duality phải thỏa mãn
4. **Tìm điều kiện strong duality:** Slater's condition hoặc feasibility

#### **Giải thích ý nghĩa kinh tế:**
- **Primal variables:** Quyết định sản xuất, phân bổ tài nguyên
- **Dual variables:** Giá bóng (shadow prices), giá trị biên của ràng buộc
- **Duality gap:** Độ chênh lệch giữa cận trên và cận dưới

#### **Ứng dụng thực tế:**
- **Network flows:** Internet routing, transportation
- **Game theory:** Strategic decision making, auction design
- **Economics:** Market equilibrium, resource allocation
- **Machine learning:** SVM dual formulation

### **Ví Dụ Minh Họa**

#### **Bài toán đơn giản:**
**Primal:**
$$\min 2x_1 + 3x_2 \quad \text{s.t.} \quad x_1 + x_2 \ge 1, \quad x_1, x_2 \ge 0$$

**Dual:**
$$\max u \quad \text{s.t.} \quad u \le 2, \quad u \le 3, \quad u \ge 0$$

**Giải:**
- **Primal optimal:** $$x_1^* = 1, x_2^* = 0$$, $$f^* = 2$$
- **Dual optimal:** $$u^* = 2$$, $$g^* = 2$$
- **Strong duality:** $$f^* = g^* = 2$$

#### **Complementary slackness:**
- $$x_1^* > 0 \Rightarrow u^* = 2$$ (tight)
- $$x_2^* = 0 \Rightarrow u^* \le 3$$ (slack OK)
- $$u^* > 0 \Rightarrow x_1^* + x_2^* = 1$$ (ràng buộc primal tight)

### **Kết Nối Với Các Chương Khác**

#### **Từ chương trước:**
- **Chương 05:** LP như canonical problem
- **Chương 04:** Optimality conditions
- **Chương 03:** Convex functions và properties

#### **Tầm quan trọng của LP Duality:**
- **Nền tảng lý thuyết:** Cho general duality (Chương 11)
- **Computational:** Dual simplex, interior point methods
- **Economic interpretation:** Shadow prices, sensitivity analysis
- **Machine learning:** SVM, robust optimization

#### **Hướng phát triển:**
- **Chương 11:** General duality theory
- **Chương 12:** KKT conditions
- **Applications:** Constrained optimization, game theory

### **Ý Nghĩa Lý Thuyết**

#### **Duality như công cụ phân tích:**
- **Bounds:** Cận trên và cận dưới cho optimal value
- **Sensitivity:** Ảnh hưởng của thay đổi ràng buộc
- **Optimality:** Điều kiện cần và đủ cho optimal solution
- **Algorithms:** Dual-based methods (dual simplex, etc.)

#### **Geometric interpretation:**
- **Primal:** Tìm điểm trong feasible region
- **Dual:** Tìm hyperplane supporting optimal value
- **Strong duality:** Hyperplane touches feasible region

#### **Economic interpretation:**
- **Primal:** Direct resource allocation
- **Dual:** Price-based market mechanism
- **Equilibrium:** Primal-dual optimal solutions

### **Mẹo Thực Hành**

#### **Nhận biết khi nào dùng duality:**
1. **Primal khó giải:** Dual có thể đơn giản hơn
2. **Sensitivity analysis:** Dual variables cho shadow prices
3. **Bounds:** Dual cung cấp cận cho primal
4. **Algorithm design:** Primal-dual methods

#### **Common mistakes:**
- **Sai quy tắc chuyển đổi:** Nhầm min/max, ≤/≥
- **Quên điều kiện non-negativity:** Dual variables
- **Không kiểm tra feasibility:** Của cả primal và dual
- **Hiểu sai ý nghĩa:** Dual variables không phải primal variables

#### **Debugging tips:**
- **Verify weak duality:** $$g^* \le f^*$$ luôn đúng
- **Check complementary slackness:** Tại optimal solutions
- **Geometric intuition:** Visualize trong 2D khi có thể
- **Economic meaning:** Dual variables như prices

---

💡 **Mẹo:** LP Duality là nền tảng cho toàn bộ duality theory trong optimization. Hiểu rõ LP duality sẽ giúp bạn nắm vững các khái niệm duality nâng cao hơn!

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

Bài tập trắc nghiệm này kiểm tra hiểu biết của bạn về tính đối ngẫu trong quy hoạch tuyến tính (LP duality), weak/strong duality, complementary slackness, max flow-min cut theorem và matrix games.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>🔄 Quiz: Tính Đối Ngẫu trong Quy Hoạch Tuyến Tính</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 5%"></div>
        </div>
        <div class="score-display" id="score-display">Câu hỏi: <span id="current-q">1</span> / <span id="total-q">20</span></div>
    </div>

    <div id="quiz-content">
        <!-- Câu hỏi 1: Primal LP form -->
        <div class="question" id="q1" style="display: block;">
            <h3>Câu 1: Cho bài toán LP primal: $$\min c^T x$$ s.t. $$Ax = b, Gx \leq h$$. Bài toán dual có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) $$\max -b^T u - h^T v$$ s.t. $$-A^T u - G^T v = c, v \geq 0$$</label>
                <label><input type="radio" name="q1" value="b"> B) $$\min -b^T u - h^T v$$ s.t. $$-A^T u - G^T v = c, v \geq 0$$</label>
                <label><input type="radio" name="q1" value="c"> C) $$\max -b^T u - h^T v$$ s.t. $$-A^T u - G^T v = c, v \leq 0$$</label>
                <label><input type="radio" name="q1" value="d"> D) $$\max c^T x$$ s.t. $$Ax \geq b, Gx = h$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\max -b^T u - h^T v$$ s.t. $$-A^T u - G^T v = c, v \geq 0$$</strong><br>
                Dual của minimization problem là maximization problem. Biến dual $$u$$ cho equality constraint không có ràng buộc dấu, $$v$$ cho inequality constraint phải non-negative. Từ Lagrangian $$L = c^Tx + u^T(Ax-b) + v^T(Gx-h)$$, cực tiểu theo $$x$$ hữu hạn khi và chỉ khi $$c + A^Tu + G^Tv = 0$$, khi đó $$g(u,v) = -b^Tu - h^Tv$$.
            </div>
        </div>

        <!-- Câu hỏi 2: Weak duality -->
        <div class="question" id="q2" style="display: none;">
            <h3>Câu 2: Weak duality theorem phát biểu rằng:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) Giá trị optimal của primal bằng giá trị optimal của dual</label>
                <label><input type="radio" name="q2" value="b"> B) Giá trị optimal của primal luôn lớn hơn hoặc bằng giá trị optimal của dual</label>
                <label><input type="radio" name="q2" value="c"> C) Giá trị optimal của primal luôn nhỏ hơn giá trị optimal của dual</label>
                <label><input type="radio" name="q2" value="d"> D) Primal và dual không thể cùng có nghiệm optimal</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Giá trị optimal của primal luôn lớn hơn hoặc bằng giá trị optimal của dual</strong><br>
                Weak duality: $$p^* \geq d^*$$ trong đó $$p^*$$ là giá trị optimal của primal (minimization) và $$d^*$$ là giá trị optimal của dual (maximization).
            </div>
        </div>

        <!-- Câu hỏi 3: Strong duality -->
        <div class="question" id="q3" style="display: none;">
            <h3>Câu 3: Strong duality xảy ra khi:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) $$p^* < d^*$$</label>
                <label><input type="radio" name="q3" value="b"> B) $$p^* = d^*$$</label>
                <label><input type="radio" name="q3" value="c"> C) $$p^* > d^*$$</label>
                <label><input type="radio" name="q3" value="d"> D) Primal không có nghiệm</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$p^* = d^*$$</strong><br>
                Strong duality có nghĩa là không có duality gap: giá trị optimal của primal bằng giá trị optimal của dual.
            </div>
        </div>

        <!-- Câu hỏi 4: Complementary slackness -->
        <div class="question" id="q4" style="display: none;">
            <h3>Câu 4: Với cặp LP $$\min c^T x$$ s.t. $$Ax \geq b, x \geq 0$$ và $$\max b^T y$$ s.t. $$A^T y \leq c, y \geq 0$$, complementary slackness phát biểu rằng:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) $$x_i > 0 \Rightarrow (A^T y)_i = c_i$$ và $$y_j > 0 \Rightarrow (Ax)_j = b_j$$</label>
                <label><input type="radio" name="q4" value="b"> B) $$x_i = 0$$ và $$y_j = 0$$ với mọi $$i, j$$</label>
                <label><input type="radio" name="q4" value="c"> C) Primal và dual cùng feasible</label>
                <label><input type="radio" name="q4" value="d"> D) $$Ax \geq b$$ và $$x \geq 0$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$x_i > 0 \Rightarrow (A^T y)_i = c_i$$ và $$y_j > 0 \Rightarrow (Ax)_j = b_j$$</strong><br>
                Complementary slackness: nếu primal variable dương thì dual constraint tight, nếu dual variable dương thì primal constraint tight.
            </div>
        </div>

        <!-- Câu hỏi 5: Duality gap -->
        <div class="question" id="q5" style="display: none;">
            <h3>Câu 5: Duality gap được định nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) $$d^* - p^*$$</label>
                <label><input type="radio" name="q5" value="b"> B) $$p^* - d^*$$</label>
                <label><input type="radio" name="q5" value="c"> C) $$p^* + d^*$$</label>
                <label><input type="radio" name="q5" value="d"> D) $$|p^* - d^*|$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$p^* - d^*$$</strong><br>
                Duality gap là hiệu số giữa giá trị optimal của primal và dual. Do weak duality, gap này luôn non-negative.
            </div>
        </div>

        <!-- Câu hỏi 6: Standard form LP dual -->
        <div class="question" id="q6" style="display: none;">
            <h3>Câu 6: Cho LP ở dạng chuẩn: $$\min c^T x$$ s.t. $$Ax = b, x \geq 0$$. Bài toán dual là:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) $$\max b^T y$$ s.t. $$A^T y \leq c$$</label>
                <label><input type="radio" name="q6" value="b"> B) $$\max b^T y$$ s.t. $$A^T y = c$$</label>
                <label><input type="radio" name="q6" value="c"> C) $$\min b^T y$$ s.t. $$A^T y \geq c$$</label>
                <label><input type="radio" name="q6" value="d"> D) $$\max b^T y$$ s.t. $$A^T y \geq c$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\max b^T y$$ s.t. $$A^T y \leq c$$</strong><br>
                Dual của standard form LP: biến dual $$y$$ không có ràng buộc dấu vì primal có equality constraints.
            </div>
        </div>

        <!-- Câu hỏi 7: Max flow problem -->
        <div class="question" id="q7" style="display: none;">
            <h3>Câu 7: Trong bài toán max flow, mục tiêu là:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) Tối thiểu hóa tổng capacity của các cạnh</label>
                <label><input type="radio" name="q7" value="b"> B) Tối đa hóa luồng từ source đến sink</label>
                <label><input type="radio" name="q7" value="c"> C) Tối thiểu hóa số cạnh trong đường đi</label>
                <label><input type="radio" name="q7" value="d"> D) Tối đa hóa số đỉnh được ghé thăm</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Tối đa hóa luồng từ source đến sink</strong><br>
                Max flow problem tìm luồng lớn nhất có thể gửi từ source node đến sink node thông qua network.
            </div>
        </div>

        <!-- Câu hỏi 8: Min cut problem -->
        <div class="question" id="q8" style="display: none;">
            <h3>Câu 8: Min cut problem tìm:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) Tập cạnh có tổng capacity nhỏ nhất để ngắt kết nối source và sink</label>
                <label><input type="radio" name="q8" value="b"> B) Đường đi ngắn nhất từ source đến sink</label>
                <label><input type="radio" name="q8" value="c"> C) Số cạnh tối thiểu để kết nối tất cả đỉnh</label>
                <label><input type="radio" name="q8" value="d"> D) Cây khung nhỏ nhất của đồ thị</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Tập cạnh có tổng capacity nhỏ nhất để ngắt kết nối source và sink</strong><br>
                Min cut tìm partition của đỉnh thành hai tập sao cho tổng capacity của cạnh giữa hai tập là nhỏ nhất.
            </div>
        </div>

        <!-- Câu hỏi 9: Max flow min cut theorem -->
        <div class="question" id="q9" style="display: none;">
            <h3>Câu 9: Max flow-min cut theorem phát biểu rằng:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) Giá trị max flow bằng capacity của min cut</label>
                <label><input type="radio" name="q9" value="b"> B) Max flow luôn nhỏ hơn min cut</label>
                <label><input type="radio" name="q9" value="c"> C) Min cut luôn nhỏ hơn max flow</label>
                <label><input type="radio" name="q9" value="d"> D) Max flow và min cut không liên quan</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Giá trị max flow bằng capacity của min cut</strong><br>
                Đây là một ví dụ kinh điển của strong duality: max flow problem và min cut problem là dual của nhau.
            </div>
        </div>

        <!-- Câu hỏi 10: Matrix games -->
        <div class="question" id="q10" style="display: none;">
            <h3>Câu 10: Trong matrix game với payout matrix $$P$$, player J muốn:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) Tối đa hóa expected payout</label>
                <label><input type="radio" name="q10" value="b"> B) Tối thiểu hóa maximum loss (minimax)</label>
                <label><input type="radio" name="q10" value="c"> C) Tối đa hóa minimum gain</label>
                <label><input type="radio" name="q10" value="d"> D) Tối thiểu hóa expected payout</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Tối thiểu hóa maximum loss (minimax)</strong><br>
                Player J (row player) muốn minimize maximum possible loss, tức là tìm mixed strategy để minimize worst-case payout.
            </div>
        </div>

        <!-- Câu hỏi 11: Feasible region -->
        <div class="question" id="q11" style="display: none;">
            <h3>Câu 11: Nếu primal LP có feasible region rỗng, thì dual LP:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) Cũng có feasible region rỗng</label>
                <label><input type="radio" name="q11" value="b"> B) Có thể unbounded hoặc infeasible</label>
                <label><input type="radio" name="q11" value="c"> C) Luôn có nghiệm optimal</label>
                <label><input type="radio" name="q11" value="d"> D) Luôn unbounded</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Có thể unbounded hoặc infeasible</strong><br>
                Khi primal infeasible, dual có thể unbounded (nếu dual feasible) hoặc cũng infeasible.
            </div>
        </div>

        <!-- Câu hỏi 12: Economic interpretation -->
        <div class="question" id="q12" style="display: none;">
            <h3>Câu 12: Trong kinh tế học, dual variables thường được hiểu là:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) Shadow prices (giá bóng)</label>
                <label><input type="radio" name="q12" value="b"> B) Production quantities</label>
                <label><input type="radio" name="q12" value="c"> C) Market demands</label>
                <label><input type="radio" name="q12" value="d"> D) Cost coefficients</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Shadow prices (giá bóng)</strong><br>
                Dual variables biểu thị marginal value của resources, tức là giá trị gia tăng khi tăng resource constraint một đơn vị.
            </div>
        </div>

        <!-- Câu hỏi 13: Dual of dual -->
        <div class="question" id="q13" style="display: none;">
            <h3>Câu 13: Dual của dual problem là:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) Một bài toán hoàn toàn khác</label>
                <label><input type="radio" name="q13" value="b"> B) Primal problem ban đầu</label>
                <label><input type="radio" name="q13" value="c"> C) Không tồn tại</label>
                <label><input type="radio" name="q13" value="d"> D) Bằng dual problem</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Primal problem ban đầu</strong><br>
                Tính chất đối xứng: dual của dual chính là primal problem ban đầu (có thể cần chuyển đổi dạng).
            </div>
        </div>

        <!-- Câu hỏi 14: LP duality conditions -->
        <div class="question" id="q14" style="display: none;">
            <h3>Câu 14: Để có strong duality trong LP, điều kiện cần là:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) Cả primal và dual đều có nghiệm optimal</label>
                <label><input type="radio" name="q14" value="b"> B) Primal hoặc dual có interior point (Slater condition)</label>
                <label><input type="radio" name="q14" value="c"> C) Feasible region là bounded</label>
                <label><input type="radio" name="q14" value="d"> D) Không cần điều kiện gì, LP luôn có strong duality</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Không cần điều kiện gì, LP luôn có strong duality</strong><br>
                Linear programs luôn thỏa mãn strong duality (hoặc cả hai infeasible) do tính chất đặc biệt của linear constraints.
            </div>
        </div>

        <!-- Câu hỏi 15: Primal-dual algorithm -->
        <div class="question" id="q15" style="display: none;">
            <h3>Câu 15: Primal-dual algorithms giải LP bằng cách:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) Chỉ giải primal problem</label>
                <label><input type="radio" name="q15" value="b"> B) Chỉ giải dual problem</label>
                <label><input type="radio" name="q15" value="c"> C) Đồng thời cập nhật cả primal và dual variables</label>
                <label><input type="radio" name="q15" value="d"> D) Giải tuần tự primal rồi dual</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) Đồng thời cập nhật cả primal và dual variables</strong><br>
                Primal-dual methods maintain và cập nhật cả primal và dual solutions, sử dụng duality để guide convergence.
            </div>
        </div>

        <!-- Câu hỏi 16: Sensitivity analysis -->
        <div class="question" id="q16" style="display: none;">
            <h3>Câu 16: Dual optimal solution cung cấp thông tin về:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) Sensitivity của objective value đối với thay đổi constraints</label>
                <label><input type="radio" name="q16" value="b"> B) Số lượng iterations cần thiết</label>
                <label><input type="radio" name="q16" value="c"> C) Complexity của algorithm</label>
                <label><input type="radio" name="q16" value="d"> D) Condition number của matrix</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Sensitivity của objective value đối với thay đổi constraints</strong><br>
                Dual variables cho biết objective value thay đổi bao nhiêu khi right-hand side của constraints thay đổi.
            </div>
        </div>

        <!-- Câu hỏi 17: Game theory equilibrium -->
        <div class="question" id="q17" style="display: none;">
            <h3>Câu 17: Nash equilibrium trong matrix game tương ứng với:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Primal optimal solution</label>
                <label><input type="radio" name="q17" value="b"> B) Dual optimal solution</label>
                <label><input type="radio" name="q17" value="c"> C) Cặp primal-dual optimal solutions</label>
                <label><input type="radio" name="q17" value="d"> D) Feasible solution bất kỳ</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) Cặp primal-dual optimal solutions</strong><br>
                Nash equilibrium mixed strategies tương ứng với optimal solutions của cặp primal-dual LP problems.
            </div>
        </div>

        <!-- Câu hỏi 18: Unbounded LP -->
        <div class="question" id="q18" style="display: none;">
            <h3>Câu 18: Nếu primal LP unbounded below, thì dual LP:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) Cũng unbounded</label>
                <label><input type="radio" name="q18" value="b"> B) Infeasible</label>
                <label><input type="radio" name="q18" value="c"> C) Có nghiệm optimal</label>
                <label><input type="radio" name="q18" value="d"> D) Bounded</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Infeasible</strong><br>
                Nếu primal (minimization) unbounded below, thì dual (maximization) phải infeasible theo weak duality.
            </div>
        </div>

        <!-- Câu hỏi 19: Flow conservation -->
        <div class="question" id="q19" style="display: none;">
            <h3>Câu 19: Trong max flow problem, flow conservation constraint yêu cầu:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) Tổng flow vào mỗi node bằng tổng flow ra (trừ source/sink)</label>
                <label><input type="radio" name="q19" value="b"> B) Flow trên mỗi cạnh không vượt quá capacity</label>
                <label><input type="radio" name="q19" value="c"> C) Flow phải non-negative</label>
                <label><input type="radio" name="q19" value="d"> D) Tất cả các điều kiện trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Tổng flow vào mỗi node bằng tổng flow ra (trừ source/sink)</strong><br>
                Flow conservation: $$\sum_{i} f_{ij} = \sum_{k} f_{jk}$$ tại mỗi intermediate node $$j$$.
            </div>
        </div>

        <!-- Câu hỏi 20: LP duality applications -->
        <div class="question" id="q20" style="display: none;">
            <h3>Câu 20: LP duality có ứng dụng trong:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Kinh tế học (resource allocation)</label>
                <label><input type="radio" name="q20" value="b"> B) Network flows và transportation</label>
                <label><input type="radio" name="q20" value="c"> C) Game theory và decision making</label>
                <label><input type="radio" name="q20" value="d"> D) Tất cả các lĩnh vực trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các lĩnh vực trên</strong><br>
                LP duality có ứng dụng rộng rãi: economics (shadow prices), networks (max flow-min cut), game theory (minimax), và nhiều lĩnh vực khác.
            </div>
        </div>
        <!-- Câu hỏi 21: Thực hành -->
        <div class="question" id="q21" style="display: none;">
            <h3>Câu 21: Bài toán đối ngẫu của LP $$\min c^T x$$ với $$Ax \geq b, x \geq 0$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) $$\max b^T y$$ với $$A^T y \leq c, y \geq 0$$</label>
                <label><input type="radio" name="q21" value="b"> B) $$\max b^T y$$ với $$A^T y \geq c, y \geq 0$$</label>
                <label><input type="radio" name="q21" value="c"> C) $$\min b^T y$$ với $$A^T y \leq c, y \geq 0$$</label>
                <label><input type="radio" name="q21" value="d"> D) $$\max c^T y$$ với $$A^T y \leq b, y \geq 0$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\max b^T y$$ với $$A^T y \leq c, y \geq 0$$</strong><br>
                Bài toán đối ngẫu của LP có dạng $$\max b^T y$$ với $$A^T y \leq c, y \geq 0$$.
            </div>
        </div>

        <!-- Câu hỏi 22: Thực hành -->
        <div class="question" id="q22" style="display: none;">
            <h3>Câu 22: Định lý đối ngẫu mạnh trong LP khẳng định:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) $$c^T x^* = b^T y^*$$</label>
                <label><input type="radio" name="q22" value="b"> B) $$c^T x^* \leq b^T y^*$$</label>
                <label><input type="radio" name="q22" value="c"> C) $$c^T x^* \geq b^T y^*$$</label>
                <label><input type="radio" name="q22" value="d"> D) Không có mối quan hệ</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$c^T x^* = b^T y^*$$</strong><br>
                Khi cả primal và dual đều có nghiệm tối ưu, giá trị tối ưu của chúng bằng nhau.
            </div>
        </div>

        <!-- Câu hỏi 23: Thực hành -->
        <div class="question" id="q23" style="display: none;">
            <h3>Câu 23: Điều kiện bổ sung trong LP: nếu $$x_i > 0$$ thì:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) Ràng buộc dual tương ứng tích cực</label>
                <label><input type="radio" name="q23" value="b"> B) Ràng buộc dual tương ứng không tích cực</label>
                <label><input type="radio" name="q23" value="c"> C) $$y_i = 0$$</label>
                <label><input type="radio" name="q23" value="d"> D) $$y_i > 0$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Ràng buộc dual tương ứng tích cực</strong><br>
                Điều kiện bổ sung: nếu $$x_i > 0$$ thì ràng buộc dual $$\sum_j a_{ji}y_j = c_i$$ phải tích cực.
            </div>
        </div>

        <!-- Câu hỏi 24: Thực hành -->
        <div class="question" id="q24" style="display: none;">
            <h3>Câu 24: Duality gap trong LP bằng:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) $$c^T x - b^T y$$</label>
                <label><input type="radio" name="q24" value="b"> B) $$b^T y - c^T x$$</label>
                <label><input type="radio" name="q24" value="c"> C) $$|c^T x - b^T y|$$</label>
                <label><input type="radio" name="q24" value="d"> D) $$\max\{c^T x, b^T y\}$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$c^T x - b^T y$$</strong><br>
                Duality gap = giá trị primal - giá trị dual = $$c^T x - b^T y \geq 0$$.
            </div>
        </div>

        <!-- Câu hỏi 25: Thực hành -->
        <div class="question" id="q25" style="display: none;">
            <h3>Câu 25: Cho LP: $$\min 2x_1 + 3x_2$$ với $$x_1 + x_2 \geq 1, x_1, x_2 \geq 0$$. Bài toán dual là:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) $$\max y$$ với $$y \leq 2, y \leq 3, y \geq 0$$</label>
                <label><input type="radio" name="q25" value="b"> B) $$\max y$$ với $$y \geq 2, y \geq 3, y \geq 0$$</label>
                <label><input type="radio" name="q25" value="c"> C) $$\min y$$ với $$y \leq 2, y \leq 3, y \geq 0$$</label>
                <label><input type="radio" name="q25" value="d"> D) $$\max 2y + 3y$$ với $$y \geq 1$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\max y$$ với $$y \leq 2, y \leq 3, y \geq 0$$</strong><br>
                Dual: $$\max y$$ với $$y \leq 2$$ (từ $$x_1 \geq 0$$), $$y \leq 3$$ (từ $$x_2 \geq 0$$), $$y \geq 0$$.
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
    q1: 'a', q2: 'b', q3: 'b', q4: 'a', q5: 'b',
    q6: 'a', q7: 'b', q8: 'a', q9: 'a', q10: 'b',
    q11: 'b', q12: 'a', q13: 'b', q14: 'd', q15: 'c',
    q16: 'a', q17: 'c', q18: 'b', q19: 'a', q20: 'd'
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
        message = '🌟 Xuất sắc! Bạn đã nắm vững LP duality theory!';
    } else if (percentage >= 80) {
        message = '👍 Rất tốt! Bạn hiểu tốt về primal-dual relationships.';
    } else if (percentage >= 70) {
        message = '📚 Khá ổn! Hãy xem lại complementary slackness và applications.';
    } else if (percentage >= 60) {
        message = '💪 Cần cải thiện! Ôn lại weak/strong duality và formulations.';
    } else {
        message = '📖 Hãy học lại từ đầu về LP duality nhé!';
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
