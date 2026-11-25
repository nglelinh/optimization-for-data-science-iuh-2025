---
layout: post
title: "10-08 Bài tập trắc nghiệm - Tính Đối Ngẫu trong Quy Hoạch Tuyến Tính"
chapter: "10"
order: 9
owner: "GitHub Copilot"
lang: vi
categories:
  - chapter10
lesson_type: quiz
redirect_from:
  - /contents/vi/chapter10/10_06_Quiz_LP_Duality/
---

Đối ngẫu trong quy hoạch tuyến tính có một điểm rất dễ gây "xoắn não" khi làm bài kiểm tra: chỉ cần nhầm một dấu trừ, lộn chiều bất đẳng thức $$\le$$ thành $$\ge$$, hoặc quên điều kiện dấu của biến đối ngẫu cho ràng buộc đẳng thức là cả bài toán đối ngẫu lập tức sai lệch hoàn toàn! Ngoài ra, các câu hỏi khái niệm về 4 tổ hợp trạng thái Primal–Dual (nhất là trường hợp *cả hai đều vô nghiệm*) cũng là cái bẫy kinh điển mà rất nhiều người học mắc phải.

Trước khi bắt tay vào bộ câu hỏi trắc nghiệm Chương 10 dưới đây, hãy điểm qua bản đồ bốn cụm kiến thức cốt lõi và kiểm chứng bốn phép thử ngắn để chắc tay trước mọi câu hỏi bẫy dấu và lý thuyết.

## Kiến thức cần nhớ: Bốn cụm kiến thức trọng tâm cho bài trắc nghiệm Chương 10

- **Bảng chuyển đổi Primal $$\leftrightarrow$$ Dual (S-O-B / quy tắc dấu):** Với Primal dạng $$\min$$: ràng buộc `=` $$\leftrightarrow$$ biến đối ngẫu tự do; ràng buộc `\ge` $$\leftrightarrow$$ biến đối ngẫu `\ge 0`; ràng buộc `\le` $$\leftrightarrow$$ biến đối ngẫu `\le 0` (hoặc đặt biến $$v \ge 0$$ rồi đổi dấu trước $$h^T v$$).
- **Đối ngẫu yếu, đối ngẫu mạnh và 4 trạng thái khả dĩ:** Luôn có $$d \le p$$ (với Primal $$\min$$, Dual $$\max$$). Nếu Primal không bị chặn dưới $$\Rightarrow$$ Dual chắc chắn vô nghiệm; nhưng ngược lại Primal vô nghiệm có thể dẫn tới Dual không bị chặn **hoặc** Dual cũng vô nghiệm!
- **Điều kiện bù (Complementary Slackness):** Tại cặp nghiệm tối ưu $$(x^*, u^*)$$, mọi ràng buộc bất đẳng thức gốc còn "lỏng" ($$a_i^T x^* < b_i$$) bắt buộc có biến đối ngẫu $$u_i^* = 0$$; và mọi biến đối ngẫu dương ($$u_i^* > 0$$) bắt buộc kéo theo ràng buộc gốc tương ứng phải chặt ($$a_i^T x^* = b_i$$).
- **Hai ứng dụng kinh điển — Max Flow/Min Cut và Matrix Games:** Ghi nhớ rằng lát cắt cực tiểu là đối ngẫu của luồng cực đại, và định lý minimax $$\min_x \max_y x^T P y = \max_y \min_x x^T P y$$ là hệ quả trực tiếp của đối ngẫu mạnh LP.

### Giải thích: Bốn phép thử số nhanh né bẫy trắc nghiệm Chương 10

1. **Bẫy 1 — Kiểm tra đối ngẫu yếu nhanh:** Một bài toán Primal $$\min$$ có nghiệm khả thi đạt $$p = 12$$, bài toán Dual $$\max$$ có nghiệm khả thi đạt $$d = 10$$. Ta kết luận được gì về $$p^*$$?
   Chắc chắn $$10 \le d^* = p^* \le 12$$ (giá trị tối ưu nằm trong đoạn $$[10, 12]$$; nếu có cặp nào đạt $$d = 12$$ thì lập tức kết luận tối ưu!).
2. **Bẫy 2 — Ví dụ cả Primal lẫn Dual đều vô nghiệm:**
   Xét Primal: $$\min x_1 - x_2$$ s.t. $$x_1 - x_2 \ge 1$$ và $$-x_1 + x_2 \ge 1$$ (hai ràng buộc mâu thuẫn nhau nên Primal vô nghiệm!).
   Dual: $$\max u_1 + u_2$$ s.t. $$u_1 - u_2 = 1$$, $$-u_1 + u_2 = -1$$? Nếu đổi hàm mục tiêu Primal thành $$x_1 + x_2$$ thì Dual đòi $$u_1 - u_2 = 1$$ và $$-u_1 + u_2 = 1$$ (vô nghiệm nốt!). Vậy cả hai cùng vô nghiệm là **hoàn toàn có thể xảy ra**!
3. **Bẫy 3 — Đọc nhanh biến đối ngẫu từ điều kiện bù:**
   Giả sử tại nghiệm tối ưu $$x^* = (2, 1)$$, ràng buộc $$x_1 + 2x_2 \le 10$$ có vế trái $$2 + 2 = 4 < 10$$ (còn dư $$6$$ đơn vị). Không cần giải bài toán đối ngẫu, ta biết ngay giá bóng tương ứng $$v^* = 0$$!
4. **Bẫy 4 — Giá trị trò chơi ma trận đối xứng:** Với ma trận chi trả phản đối xứng $$P^T = -P$$ (như Oẳn Tù Tì), giá trị trò chơi $$v^*$$ luôn bằng đúng $$0$$ vì hai người chơi có vai trò hoàn toàn bình đẳng.

## Ôn tập lý thuyết

Trước khi làm bài tập, hãy ôn lại các khái niệm chính trong chương này:

### Tính đối ngẫu trong quy hoạch tuyến tính (LP Duality)

#### Ý tưởng cơ bản
Tính đối ngẫu trong LP xuất phát từ bài toán tìm **cận dưới** cho giá trị tối ưu của bài toán gốc (primal).

**Nguyên lý:** Nếu biểu diễn được hàm mục tiêu dưới dạng **tổ hợp tuyến tính** (với hệ số phù hợp) của các ràng buộc, ta thu được một cận dưới cho bài toán gốc.

#### Từ ví dụ đơn giản đến tổng quát

**Ví dụ 1:** Ràng buộc chứa trực tiếp hàm mục tiêu
$$\min_{x,y} x + y \quad \text{s.t.} \quad x + y \ge 2, \quad x,y \ge 0$$

**Cận dưới trực tiếp:** $$B = 2$$

**Ví dụ 2:** Biểu diễn hàm mục tiêu qua tổ hợp tuyến tính của các ràng buộc
$$\min_{x,y} x + 3y \quad \text{s.t.} \quad x + y \ge 2, \quad x,y \ge 0$$

**Tổ hợp tuyến tính:**
$$1 \cdot (x + y) + 0 \cdot x + 2 \cdot y = x + 3y \ge 2$$

**Cận dưới:** $$B = 2$$

### 📏 Xây dựng bài toán đối ngẫu

#### Bài toán gốc tổng quát
$$\min_x c^T x \quad \text{s.t.} \quad Ax = b, \quad Gx \le h$$

#### Các bước xây dựng bài toán đối ngẫu
1. **Định nghĩa biến đối ngẫu:** $$u$$ (cho ràng buộc đẳng thức), $$v \ge 0$$ (cho ràng buộc bất đẳng thức).
2. **Lập tổ hợp tuyến tính:** $$u^T(Ax - b) + v^T(Gx - h) \le 0$$.
3. **Biến đổi để tách hàm mục tiêu:** $$(-A^T u - G^T v)^T x \ge -b^T u - h^T v$$.
4. **Điều kiện khớp hệ số:** $$c = -A^T u - G^T v$$.

#### Bài toán đối ngẫu
$$\max_{u,v} -b^T u - h^T v \quad \text{s.t.} \quad c = -A^T u - G^T v, \quad v \ge 0$$

### 🔄 Quy tắc chuyển đổi gốc – đối ngẫu

| **Bài toán gốc (Primal)** | **Bài toán đối ngẫu (Dual)** |
|---------------------------|------------------------------|
| $$\min$$ | $$\max$$ |
| $$Ax = b$$ | $$u$$ không ràng buộc dấu |
| $$Gx \le h$$ | $$v \ge 0$$ |
| $$x \ge 0$$ | Ràng buộc bất đẳng thức trong bài toán đối ngẫu |
| $$x$$ không ràng buộc dấu | Ràng buộc đẳng thức trong bài toán đối ngẫu |

#### Ví dụ chuyển đổi
**Bài toán gốc:**
$$\min_{x,y} px + qy \quad \text{s.t.} \quad x \ge 0, \quad y \le 1, \quad 3x + y = 2$$

**Bài toán đối ngẫu:**
$$\max_{a,b,c} 2c - b \quad \text{s.t.} \quad a + 3c = p, \quad -b + c = q, \quad a,b \ge 0$$

### 🌊 Ví dụ: Luồng cực đại – lát cắt cực tiểu

#### Bài toán luồng cực đại (Max Flow)
Tìm luồng lớn nhất từ nguồn $$s$$ đến đích $$t$$ trong đồ thị có hướng:

$$\max \sum_{(s,j) \in E} f_{sj} \quad \text{s.t.} \begin{cases}
f_{ij} \ge 0, \quad f_{ij} \le c_{ij} & \forall (i,j) \in E \\
\sum_{(i,k) \in E} f_{ik} = \sum_{(k,j) \in E} f_{kj} & \forall k \in V \setminus \{s,t\}
\end{cases}$$

#### Bài toán lát cắt cực tiểu (Min Cut)
Tìm lát cắt có dung lượng nhỏ nhất phân tách $$s$$ và $$t$$:

$$\min \sum_{(i,j) \in E} b_{ij} c_{ij} \quad \text{s.t.} \begin{cases}
b_{ij} \ge x_i - x_j & \forall (i,j) \in E \\
x_i, b_{ij} \in \{0,1\} & \forall i,j \\
x_s = 1, x_t = 0
\end{cases}$$

#### Mối quan hệ đối ngẫu
**Đối ngẫu của luồng cực đại = Bản nới lỏng LP của lát cắt cực tiểu**

$$\text{Max Flow Value} \le \text{Dual LP} = \text{LP Relaxed Min Cut} \le \text{Min Cut Capacity}$$

**Định lý luồng cực đại – lát cắt cực tiểu:** Cả ba giá trị trên đều bằng nhau.

### Cách tiếp cận Lagrangian

#### Hàm Lagrangian
Với bài toán tối ưu tổng quát:
$$\min_x f(x) \quad \text{s.t.} \quad Ax = b, \quad Gx \le h$$

**Hàm Lagrangian:**
$$L(x,u,v) = f(x) + u^T(Ax - b) + v^T(Gx - h)$$

#### Hàm đối ngẫu
$$g(u,v) = \min_x L(x,u,v)$$

**Tính chất:** $$g(u,v) \le f^*$$ với mọi $$v \ge 0$$ (đối ngẫu yếu).

#### Bài toán đối ngẫu Lagrangian
$$\max_{u,v} g(u,v) \quad \text{s.t.} \quad v \ge 0$$

#### Áp dụng cho LP
$$g(u,v) = \min_x (c + A^T u + G^T v)^T x - b^T u - h^T v$$

$$= \begin{cases}
-b^T u - h^T v & \text{if } c + A^T u + G^T v = 0 \\
-\infty & \text{otherwise}
\end{cases}$$

**Kết quả:** Trùng khớp với bài toán LP đối ngẫu xây dựng theo tổ hợp tuyến tính.

### 🎮 Trò chơi ma trận

#### Thiết lập trò chơi
- **Hai người chơi:** $$J$$ (chọn hàng) và $$R$$ (chọn cột).
- **Ma trận chi trả:** $$P$$ (khoản tiền $$J$$ trả cho $$R$$).
- **Chiến lược hỗn hợp:** phân phối xác suất $$x$$ (của $$J$$) và $$y$$ (của $$R$$).
- **Chi trả kỳ vọng:** $$x^T P y$$.

#### Góc nhìn của J (người cực tiểu hóa)
Khi $$R$$ biết trước chiến lược của $$J$$, $$J$$ muốn cực tiểu hóa chi trả kỳ vọng trong trường hợp xấu nhất:
$$\min_x \max_{i=1,\ldots,n} (P^T x)_i \quad \text{s.t.} \quad x \ge 0, \quad \mathbf{1}^T x = 1$$

**Dạng LP tương đương:**
$$\min_{x,t} t \quad \text{s.t.} \quad x \ge 0, \quad \mathbf{1}^T x = 1, \quad P^T x \preceq t \mathbf{1}$$

#### Góc nhìn của R (người cực đại hóa)
Khi $$J$$ biết trước chiến lược của $$R$$, $$R$$ muốn cực đại hóa chi trả kỳ vọng trong trường hợp xấu nhất:
$$\max_y \min_{j=1,\ldots,m} (Py)_j \quad \text{s.t.} \quad y \ge 0, \quad \mathbf{1}^T y = 1$$

**Dạng LP tương đương:**
$$\max_{y,v} v \quad \text{s.t.} \quad y \ge 0, \quad \mathbf{1}^T y = 1, \quad Py \succeq v \mathbf{1}$$

#### Định lý minimax của von Neumann
Hai bài toán trên là cặp **gốc – đối ngẫu** của nhau và có cùng giá trị tối ưu:
$$\min_x \max_y x^T P y = \max_y \min_x x^T P y$$

**Lý do:** $$x^T P y$$ là hàm song tuyến tính (lồi theo $$x$$, lõm theo $$y$$) trên các đơn hình lồi compact; đồng thời đây là một cặp LP đối ngẫu khả thi nên tính đối ngẫu mạnh luôn đúng.

### Đối ngẫu yếu và đối ngẫu mạnh

#### Đối ngẫu yếu (Weak Duality)
**Luôn đúng:** giá trị đối ngẫu $$\le$$ giá trị gốc:
$$\max_{u,v} g(u,v) \le \min_x f(x)$$

**Khoảng cách đối ngẫu (Duality gap):** $$f^* - g^* \ge 0$$.

#### Đối ngẫu mạnh (Strong Duality)
**Đẳng thức:** giá trị đối ngẫu = giá trị gốc:
$$\max_{u,v} g(u,v) = \min_x f(x)$$

**Khoảng cách đối ngẫu:** $$f^* - g^* = 0$$.

#### Điều kiện đối ngẫu mạnh trong LP
- Nếu ít nhất một trong hai bài toán (gốc hoặc đối ngẫu) khả thi thì tính đối ngẫu mạnh luôn đúng.
- Trường hợp ngoại lệ duy nhất: cả hai bài toán đều vô nghiệm (infeasible).

### 🔄 Các dạng chuẩn của LP

#### Dạng chuẩn (Standard form)
$$\min c^T x \quad \text{s.t.} \quad Ax = b, \quad x \ge 0$$

**Đối ngẫu:**
$$\max b^T u \quad \text{s.t.} \quad A^T u \le c$$

#### Dạng bất đẳng thức (Inequality form)
$$\min c^T x \quad \text{s.t.} \quad Ax \le b$$

**Đối ngẫu:**
$$\max -b^T u \quad \text{s.t.} \quad A^T u = -c, \quad u \ge 0$$

#### Dạng tổng quát (General form)
$$\min c^T x \quad \text{s.t.} \quad Ax = b, \quad Gx \le h$$

**Đối ngẫu:**
$$\max -b^T u - h^T v \quad \text{s.t.} \quad -A^T u - G^T v = c, \quad v \ge 0$$

### 🛠️ Kỹ năng thực hành

#### Xây dựng bài toán đối ngẫu từ bài toán gốc
1. Xác định dạng bài toán (cực tiểu hay cực đại, loại ràng buộc).
2. Áp dụng bảng quy tắc chuyển đổi gốc – đối ngẫu.
3. Kiểm tra lại tính hợp lý bằng bất đẳng thức đối ngẫu yếu.
4. Xác định điều kiện để đối ngẫu mạnh thỏa mãn.

#### Ý nghĩa kinh tế
- **Biến gốc:** mức sản xuất hoặc phương án phân bổ nguồn lực.
- **Biến đối ngẫu:** giá bóng (shadow prices), phản ánh giá trị biên của từng ràng buộc nguồn lực.
- **Khoảng cách đối ngẫu:** độ chênh lệch giữa giá trị mục tiêu gốc và đối ngẫu.

#### Một số ứng dụng tiêu biểu
- **Luồng trên mạng:** định tuyến mạng, vận tải.
- **Lý thuyết trò chơi:** chiến lược hỗn hợp, thiết kế đấu giá.
- **Kinh tế học:** cân bằng thị trường, phân bổ tài nguyên.
- **Học máy:** dạng đối ngẫu của máy vector hỗ trợ (SVM).

### Ví dụ minh họa

#### Bài toán đơn giản
**Bài toán gốc:**
$$\min 2x_1 + 3x_2 \quad \text{s.t.} \quad x_1 + x_2 \ge 1, \quad x_1, x_2 \ge 0$$

**Bài toán đối ngẫu:**
$$\max u \quad \text{s.t.} \quad u \le 2, \quad u \le 3, \quad u \ge 0$$

**Nghiệm:**
- Nghiệm tối ưu gốc: $$x_1^* = 1, x_2^* = 0$$, $$f^* = 2$$.
- Nghiệm tối ưu đối ngẫu: $$u^* = 2$$, $$g^* = 2$$.
- Đối ngẫu mạnh: $$f^* = g^* = 2$$.

#### Điều kiện bù (Complementary slackness)
- $$x_1^* > 0 \Rightarrow u^* = 2$$ (ràng buộc đối ngẫu chặt).
- $$x_2^* = 0 \Rightarrow u^* \le 3$$ (ràng buộc đối ngẫu được phép lỏng).
- $$u^* > 0 \Rightarrow x_1^* + x_2^* = 1$$ (ràng buộc gốc chặt).

### Kết nối với các chương khác

- **Các chương trước:** LP như bài toán chuẩn (Chương 05), điều kiện tối ưu (Chương 04), hàm lồi và tính chất (Chương 03).
- **Hướng phát triển:** Lý thuyết đối ngẫu tổng quát (Chương 11), điều kiện KKT (Chương 12), cùng các ứng dụng trong tối ưu có ràng buộc và lý thuyết trò chơi.

### Lưu ý khi làm bài

- **Lỗi thường gặp:** Nhầm chiều bất đẳng thức ($$\le / \ge$$) hoặc nhầm $$\min / \max$$ khi chuyển đổi; quên điều kiện dấu không âm của biến đối ngẫu; không kiểm tra tính khả thi của cả hai bài toán.
- **Cách tự kiểm tra:** Luôn kiểm tra bất đẳng thức đối ngẫu yếu $$g^* \le f^*$$, kiểm tra điều kiện bù tại nghiệm tối ưu, và đối chiếu ý nghĩa kinh tế của biến đối ngẫu.

---

💡 **Ghi chú:** Tính đối ngẫu LP là cơ sở trực tiếp cho lý thuyết đối ngẫu tổng quát ở Chương 11.

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

Bài tập trắc nghiệm này kiểm tra kiến thức về tính đối ngẫu trong quy hoạch tuyến tính (LP), đối ngẫu yếu và mạnh, điều kiện bù, định lý luồng cực đại – lát cắt cực tiểu và trò chơi ma trận.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>🔄 Quiz: Tính Đối Ngẫu trong Quy Hoạch Tuyến Tính</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 5%"></div>
        </div>
        <div class="score-display" id="score-display">Câu hỏi: <span id="current-q">1</span> / <span id="total-q">25</span></div>
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
                Đối ngẫu của bài toán cực tiểu hóa là bài toán cực đại hóa. Biến đối ngẫu $$u$$ ứng với ràng buộc đẳng thức không bị ràng buộc dấu, còn $$v$$ ứng với ràng buộc bất đẳng thức phải không âm. Từ Lagrangian $$L = c^Tx + u^T(Ax-b) + v^T(Gx-h)$$, cực tiểu theo $$x$$ hữu hạn khi và chỉ khi $$c + A^Tu + G^Tv = 0$$, khi đó $$g(u,v) = -b^Tu - h^Tv$$.
            </div>
        </div>

        <!-- Câu hỏi 2: Weak duality -->
        <div class="question" id="q2" style="display: none;">
            <h3>Câu 2: Định lý đối ngẫu yếu (weak duality) phát biểu rằng:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) Giá trị tối ưu của bài toán gốc bằng giá trị tối ưu của bài toán đối ngẫu</label>
                <label><input type="radio" name="q2" value="b"> B) Giá trị tối ưu của bài toán gốc luôn lớn hơn hoặc bằng giá trị tối ưu của bài toán đối ngẫu</label>
                <label><input type="radio" name="q2" value="c"> C) Giá trị tối ưu của bài toán gốc luôn nhỏ hơn giá trị tối ưu của bài toán đối ngẫu</label>
                <label><input type="radio" name="q2" value="d"> D) Bài toán gốc và bài toán đối ngẫu không thể cùng có nghiệm tối ưu</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Giá trị tối ưu của bài toán gốc luôn lớn hơn hoặc bằng giá trị tối ưu của bài toán đối ngẫu</strong><br>
                Đối ngẫu yếu: $$p^* \geq d^*$$, trong đó $$p^*$$ là giá trị tối ưu của bài toán gốc (cực tiểu hóa) và $$d^*$$ là giá trị tối ưu của bài toán đối ngẫu (cực đại hóa).
            </div>
        </div>

        <!-- Câu hỏi 3: Strong duality -->
        <div class="question" id="q3" style="display: none;">
            <h3>Câu 3: Tính đối ngẫu mạnh (strong duality) xảy ra khi:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) $$p^* < d^*$$</label>
                <label><input type="radio" name="q3" value="b"> B) $$p^* = d^*$$</label>
                <label><input type="radio" name="q3" value="c"> C) $$p^* > d^*$$</label>
                <label><input type="radio" name="q3" value="d"> D) Primal không có nghiệm</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$p^* = d^*$$</strong><br>
                Đối ngẫu mạnh có nghĩa là khoảng cách đối ngẫu bằng 0: giá trị tối ưu của bài toán gốc bằng giá trị tối ưu của bài toán đối ngẫu.
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
                Điều kiện bù (complementary slackness): nếu biến gốc dương thì ràng buộc đối ngẫu tương ứng chặt, và nếu biến đối ngẫu dương thì ràng buộc gốc tương ứng chặt.
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
                Khoảng cách đối ngẫu là hiệu giữa giá trị tối ưu của bài toán gốc và bài toán đối ngẫu; theo đối ngẫu yếu, hiệu này luôn không âm.
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
                Đối ngẫu của LP dạng chuẩn: biến đối ngẫu $$y$$ không bị ràng buộc dấu vì bài toán gốc chỉ có ràng buộc đẳng thức.
            </div>
        </div>

        <!-- Câu hỏi 7: Max flow problem -->
        <div class="question" id="q7" style="display: none;">
            <h3>Câu 7: Trong bài toán max flow, mục tiêu là:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) Cực tiểu hóa tổng dung lượng của các cạnh</label>
                <label><input type="radio" name="q7" value="b"> B) Cực đại hóa luồng từ nguồn đến đích</label>
                <label><input type="radio" name="q7" value="c"> C) Cực tiểu hóa số cạnh trong đường đi</label>
                <label><input type="radio" name="q7" value="d"> D) Cực đại hóa số đỉnh được ghé thăm</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Cực đại hóa luồng từ nguồn đến đích</strong><br>
                Bài toán luồng cực đại tìm tổng lưu lượng lớn nhất có thể truyền từ đỉnh nguồn đến đỉnh đích qua mạng.
            </div>
        </div>

        <!-- Câu hỏi 8: Min cut problem -->
        <div class="question" id="q8" style="display: none;">
            <h3>Câu 8: Bài toán lát cắt cực tiểu (min cut) tìm:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) Tập cạnh có tổng dung lượng nhỏ nhất để tách rời nguồn và đích</label>
                <label><input type="radio" name="q8" value="b"> B) Đường đi ngắn nhất từ nguồn đến đích</label>
                <label><input type="radio" name="q8" value="c"> C) Số cạnh tối thiểu để kết nối tất cả đỉnh</label>
                <label><input type="radio" name="q8" value="d"> D) Cây khung nhỏ nhất của đồ thị</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Tập cạnh có tổng dung lượng nhỏ nhất để tách rời nguồn và đích</strong><br>
                Lát cắt cực tiểu tìm phân hoạch tập đỉnh thành hai tập chứa nguồn và đích sao cho tổng dung lượng các cạnh đi từ tập nguồn sang tập đích là nhỏ nhất.
            </div>
        </div>

        <!-- Câu hỏi 9: Max flow min cut theorem -->
        <div class="question" id="q9" style="display: none;">
            <h3>Câu 9: Định lý luồng cực đại – lát cắt cực tiểu phát biểu rằng:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) Giá trị luồng cực đại bằng dung lượng của lát cắt cực tiểu</label>
                <label><input type="radio" name="q9" value="b"> B) Max flow luôn nhỏ hơn min cut</label>
                <label><input type="radio" name="q9" value="c"> C) Min cut luôn nhỏ hơn max flow</label>
                <label><input type="radio" name="q9" value="d"> D) Max flow và min cut không liên quan</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Giá trị luồng cực đại bằng dung lượng của lát cắt cực tiểu</strong><br>
                Đây là một ví dụ kinh điển về tính đối ngẫu mạnh giữa bài toán luồng cực đại và lát cắt cực tiểu.
            </div>
        </div>

        <!-- Câu hỏi 10: Matrix games -->
        <div class="question" id="q10" style="display: none;">
            <h3>Câu 10: Trong trò chơi ma trận với ma trận chi trả $$P$$, người chơi J muốn:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) Cực đại hóa chi trả kỳ vọng</label>
                <label><input type="radio" name="q10" value="b"> B) Cực tiểu hóa mức lỗ tối đa (minimax)</label>
                <label><input type="radio" name="q10" value="c"> C) Cực đại hóa mức lãi tối thiểu</label>
                <label><input type="radio" name="q10" value="d"> D) Cực tiểu hóa chi trả kỳ vọng</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Cực tiểu hóa mức lỗ tối đa (minimax)</strong><br>
                Người chơi J (người chọn hàng) tìm chiến lược hỗn hợp để cực tiểu hóa mức chi trả xấu nhất có thể phải trả cho R.
            </div>
        </div>

        <!-- Câu hỏi 11: Feasible region -->
        <div class="question" id="q11" style="display: none;">
            <h3>Câu 11: Nếu LP gốc có miền khả thi rỗng (vô nghiệm), thì LP đối ngẫu:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) Cũng có miền khả thi rỗng</label>
                <label><input type="radio" name="q11" value="b"> B) Có thể không bị chặn (unbounded) hoặc vô nghiệm (infeasible)</label>
                <label><input type="radio" name="q11" value="c"> C) Luôn có nghiệm tối ưu</label>
                <label><input type="radio" name="q11" value="d"> D) Luôn không bị chặn</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Có thể không bị chặn (unbounded) hoặc vô nghiệm (infeasible)</strong><br>
                Khi bài toán gốc vô nghiệm, bài toán đối ngẫu có thể không bị chặn (nếu khả thi) hoặc cũng vô nghiệm.
            </div>
        </div>

        <!-- Câu hỏi 12: Economic interpretation -->
        <div class="question" id="q12" style="display: none;">
            <h3>Câu 12: Trong kinh tế học, các biến đối ngẫu thường được hiểu là:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) Giá bóng (shadow prices)</label>
                <label><input type="radio" name="q12" value="b"> B) Production quantities</label>
                <label><input type="radio" name="q12" value="c"> C) Market demands</label>
                <label><input type="radio" name="q12" value="d"> D) Cost coefficients</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Giá bóng (shadow prices)</strong><br>
                Biến đối ngẫu biểu thị giá trị biên của nguồn lực, tức mức thay đổi của hàm mục tiêu khi tăng thêm một đơn vị nguồn lực.
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
                Trong LP, nếu ít nhất một trong hai bài toán gốc hoặc đối ngẫu khả thi thì đối ngẫu mạnh luôn thỏa mãn mà không cần thêm điều kiện Slater; ngoại lệ duy nhất là khi cả hai bài toán đều vô nghiệm.
            </div>
        </div>

        <!-- Câu hỏi 15: Primal-dual algorithm -->
        <div class="question" id="q15" style="display: none;">
            <h3>Câu 15: Các thuật toán gốc – đối ngẫu (primal-dual) giải LP bằng cách:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) Chỉ giải primal problem</label>
                <label><input type="radio" name="q15" value="b"> B) Chỉ giải dual problem</label>
                <label><input type="radio" name="q15" value="c"> C) Đồng thời cập nhật cả biến gốc và biến đối ngẫu</label>
                <label><input type="radio" name="q15" value="d"> D) Giải tuần tự primal rồi dual</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) Đồng thời cập nhật cả biến gốc và biến đối ngẫu</strong><br>
                Các phương pháp gốc – đối ngẫu duy trì và cập nhật đồng thời cả nghiệm gốc lẫn nghiệm đối ngẫu, sử dụng khoảng cách đối ngẫu để kiểm soát hội tụ.
            </div>
        </div>

        <!-- Câu hỏi 16: Sensitivity analysis -->
        <div class="question" id="q16" style="display: none;">
            <h3>Câu 16: Nghiệm tối ưu đối ngẫu cung cấp thông tin về:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) Độ nhạy của giá trị mục tiêu đối với sự thay đổi của các ràng buộc</label>
                <label><input type="radio" name="q16" value="b"> B) Số lượng iterations cần thiết</label>
                <label><input type="radio" name="q16" value="c"> C) Complexity của algorithm</label>
                <label><input type="radio" name="q16" value="d"> D) Condition number của matrix</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Độ nhạy của giá trị mục tiêu đối với sự thay đổi của các ràng buộc</strong><br>
                Biến đối ngẫu cho biết giá trị tối ưu thay đổi như thế nào khi vế phải của các ràng buộc biến động.
            </div>
        </div>

        <!-- Câu hỏi 17: Game theory equilibrium -->
        <div class="question" id="q17" style="display: none;">
            <h3>Câu 17: Cân bằng Nash trong trò chơi ma trận tương ứng với:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Primal optimal solution</label>
                <label><input type="radio" name="q17" value="b"> B) Dual optimal solution</label>
                <label><input type="radio" name="q17" value="c"> C) Cặp nghiệm tối ưu của bài toán gốc và bài toán đối ngẫu</label>
                <label><input type="radio" name="q17" value="d"> D) Feasible solution bất kỳ</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) Cặp nghiệm tối ưu của bài toán gốc và bài toán đối ngẫu</strong><br>
                Cặp chiến lược hỗn hợp ở cân bằng Nash tương ứng với cặp nghiệm tối ưu của hai bài toán LP gốc – đối ngẫu.
            </div>
        </div>

        <!-- Câu hỏi 18: Unbounded LP -->
        <div class="question" id="q18" style="display: none;">
            <h3>Câu 18: Nếu LP gốc không bị chặn dưới (unbounded below), thì LP đối ngẫu:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) Cũng unbounded</label>
                <label><input type="radio" name="q18" value="b"> B) Infeasible</label>
                <label><input type="radio" name="q18" value="c"> C) Có nghiệm optimal</label>
                <label><input type="radio" name="q18" value="d"> D) Bounded</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Infeasible</strong><br>
                Nếu bài toán gốc (cực tiểu hóa) không bị chặn dưới, bài toán đối ngẫu (cực đại hóa) bắt buộc phải vô nghiệm theo định lý đối ngẫu yếu.
            </div>
        </div>

        <!-- Câu hỏi 19: Flow conservation -->
        <div class="question" id="q19" style="display: none;">
            <h3>Câu 19: Trong bài toán luồng cực đại, ràng buộc bảo toàn luồng yêu cầu:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) Tổng luồng vào mỗi nút bằng tổng luồng ra (trừ nguồn và đích)</label>
                <label><input type="radio" name="q19" value="b"> B) Luồng trên mỗi cạnh không vượt quá dung lượng</label>
                <label><input type="radio" name="q19" value="c"> C) Luồng phải không âm</label>
                <label><input type="radio" name="q19" value="d"> D) Tất cả các điều kiện trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Tổng luồng vào mỗi nút bằng tổng luồng ra (trừ nguồn và đích)</strong><br>
                Bảo toàn luồng: $$\sum_{i} f_{ij} = \sum_{k} f_{jk}$$ tại mọi nút trung gian $$j$$.
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
                Tính đối ngẫu LP được ứng dụng trong kinh tế học (giá bóng), mạng luồng (luồng cực đại – lát cắt cực tiểu), lý thuyết trò chơi (định lý minimax) và nhiều lĩnh vực khác.
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
            <h3>Câu 23: Theo điều kiện bù trong LP, nếu $$x_i > 0$$ thì:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) Ràng buộc đối ngẫu tương ứng chặt (active)</label>
                <label><input type="radio" name="q23" value="b"> B) Ràng buộc đối ngẫu tương ứng lỏng (inactive)</label>
                <label><input type="radio" name="q23" value="c"> C) $$y_i = 0$$</label>
                <label><input type="radio" name="q23" value="d"> D) $$y_i > 0$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Ràng buộc đối ngẫu tương ứng chặt (active)</strong><br>
                Điều kiện bù: nếu $$x_i > 0$$ thì ràng buộc đối ngẫu $$\sum_j a_{ji}y_j = c_i$$ phải xảy ra dấu bằng (chặt).
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
        message = '🌟 Xuất sắc! Bạn đã nắm vững lý thuyết đối ngẫu LP.';
    } else if (percentage >= 80) {
        message = '👍 Rất tốt! Bạn hiểu tốt mối quan hệ gốc – đối ngẫu.';
    } else if (percentage >= 70) {
        message = '📚 Khá ổn! Hãy xem lại điều kiện bù và các ứng dụng.';
    } else if (percentage >= 60) {
        message = '💪 Cần cải thiện! Ôn lại đối ngẫu yếu/mạnh và cách lập bài toán đối ngẫu.';
    } else {
        message = '📖 Hãy ôn lại từ đầu các khái niệm về đối ngẫu LP.';
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
