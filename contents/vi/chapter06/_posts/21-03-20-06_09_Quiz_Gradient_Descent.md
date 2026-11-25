---
layout: post
title: 06-09 Bài tập trắc nghiệm - Gradient Descent
chapter: '06'
order: 21
owner: GitHub Copilot
lang: vi
categories:
- chapter06
lesson_type: quiz
redirect_from:
  - /contents/vi/chapter06/06_08_Quiz_Gradient_Descent/
---

Chương 06 là chương dài và giàu kỹ thuật nhất từ đầu khóa học đến nay: từ cận trên bậc hai, điều kiện Armijo, tốc độ $$O(1/k)$$ vs. $$O(c^k)$$, cận dưới Nesterov, cho đến SGD, Momentum, Gradient Boosting và Điều chuẩn. Khi quá nhiều định lý đứng cạnh nhau, não bộ rất dễ trộn lẫn các giả thiết — ví dụ nhầm lẫn điều kiện cần của hội tụ tuyến tính, hay nhầm giữa bước cố định an toàn $$1/L$$ và ngưỡng ổn định $$2/L$$.

Bộ bài tập trắc nghiệm này là bài kiểm tra tổng lực giúp bạn khóa chặt mọi định lý, công thức và trực giác hình học của Chương 06 trước khi sang thế giới không khả vi của Chương 07!

## Bản đồ kiến thức nền: Bảng tra nhanh 4 điểm dễ nhầm nhất của Chương 06

Hãy rà soát nhanh bốn phân biệt cốt lõi trước khi trả lời các câu hỏi trắc nghiệm:

- **Tốc độ hội tụ theo lớp hàm (với GD chuẩn):**
  - Lồi + $$L$$-trơn: $$O(1/k)$$ (cần $$O(1/\epsilon)$$ bước).
  - Lồi mạnh $$m$$ + $$L$$-trơn: hội tụ tuyến tính $$O\big((1 - m/L)^k\big)$$ (cần $$O(\kappa \log(1/\epsilon))$$ bước).
  - Tăng tốc Nesterov: cải thiện thành $$O(1/k^2)$$ (lồi trơn) và $$O(\sqrt{\kappa} \log(1/\epsilon))$$ (lồi mạnh).
- **Bước an toàn vs. Ngưỡng phân kỳ (trên hàm bậc hai $$L$$-trơn):** $$t \le 1/L$$ đảm bảo giảm đơn điệu theo Bổ đề Giảm; $$1/L < t < 2/L$$ vẫn hội tụ nhưng có dao động; $$t \ge 2/L$$ không hội tụ / phân kỳ!
- **SGD vs. Batch GD:** SGD có chi phí mỗi bước $$O(p)$$ (độc lập với $$N$$) thay vì $$O(Np)$$, nhưng với bước cố định chỉ hội tụ vào vùng lân cận nghiệm; muốn hội tụ chính xác về $$x^\star$$ cần giảm bước theo điều kiện Robbins–Monro ($$\sum t_k = \infty, \sum t_k^2 < \infty$$).
- **Exact Line Search:** Hai bước liên tiếp luôn trực giao ($$\nabla f(x_{k+1})^T \nabla f(x_k) = 0$$), nên vẫn có thể đi zíc-zắc chậm trên thung lũng hẹp có $$\kappa$$ lớn!

### Khung giải thích (nên đọc chậm): Chẩn đoán nhanh một câu hỏi trắc nghiệm điển hình về số vòng lặp

**Câu hỏi mẫu:** *Hàm $$f$$ lồi mạnh với $$m = 2$$ và gradient Lipschitz $$L = 20$$. Nếu dùng Gradient Descent bước cố định $$t = 1/L$$, sau mỗi bước lặp sai số $$f(x^{(k)}) - f^\star$$ giảm đi ít nhất bao nhiêu phần trăm?*

1. **Bước 1 — Áp dụng công thức hội tụ tuyến tính:**
   $$f(x^{(k+1)}) - f^\star \le (1 - mt)\big(f(x^{(k)}) - f^\star\big).$$
2. **Bước 2 — Thay số $$m = 2,\; t = 1/L = 1/20 = 0.05$$:**
   $$1 - mt = 1 - 2(0.05) = 1 - 0.1 = 0.9.$$
3. **Bước 3 — Đọc kết quả chính xác:** Sai số sau bước mới bằng tối đa $$90\%$$ sai số cũ — tức là **giảm ít nhất $$10\%$$** sau mỗi vòng lặp! (Mẹo nhanh: với $$t = 1/L$$, tỷ lệ giảm mỗi bước luôn là $$1/\kappa = m/L$$!)

---

## 📚 Ôn tập Lý thuyết

Trước khi làm bài tập, hãy ôn lại các khái niệm chính trong chương này:

### 🎯 **Gradient Descent Cơ bản**

**Bài toán tối ưu:**
$$\min_x f(x), \quad f 	ext{ khả vi và } 	ext{dom}(f) = \mathbb{R}^n$$

**Quy tắc cập nhật:**
$$x^{(k)} = x^{(k-1)} - t 
abla f(x^{(k-1)}), \quad k = 1, 2, 3, \ldots$$

**Mã giả:**
1. **Cho điểm khởi tạo** $$x \in 	ext{dom}(f)$$
2. **Lặp lại:**
   - Xác định hướng giảm: $$\Delta x = -
abla f(x)$$
   - Tìm kiếm đường: chọn kích thước bước $$t > 0$$
   - Cập nhật: $$x = x + t \Delta x$$
3. **Cho đến khi** tiêu chuẩn dừng được thỏa mãn

**Diễn giải hình học:**
- Gradient $$
abla f(x)$$ chỉ hướng tăng dốc nhất.
- Gradient âm $$-
abla f(x)$$ chỉ hướng giảm dốc nhất.
- Tại điểm cực tiểu không ràng buộc: $$
abla f(x^*) = 0$$.

### 📏 **Cách Chọn Kích thước Bước**

#### **1. Kích thước bước cố định**
$$t = 	ext{const} > 0$$

- **Ưu điểm:** Đơn giản, chi phí mỗi bước thấp.
- **Nhược điểm:** Khó chọn trước giá trị phù hợp cho mọi bài toán.

#### **2. Tìm kiếm đường lùi (Backtracking Line Search)**
**Điều kiện Armijo:**
$$f(x + t\Delta x) \le f(x) + lpha t 
abla f(x)^T \Delta x$$

**Thuật toán:**
- Khởi tạo $$t = t_0$$.
- Nếu điều kiện Armijo chưa thỏa mãn: giảm $$t := eta t$$ (với $$0 < eta < 1$$).
- Lặp lại cho đến khi điều kiện được đáp ứng.

**Tham số thường dùng:** $$lpha = 0.01 \div 0.3$$, $$eta = 0.1 \div 0.8$$.

#### **3. Tìm kiếm đường chính xác (Exact Line Search)**
$$t^* = rg\min_{t > 0} f(x + t\Delta x)$$

- **Ưu điểm:** Tối ưu theo hướng hiện tại.
- **Nhược điểm:** Tốn kém về tính toán với hàm phi tuyến tổng quát.

### 📊 **Phân tích Hội tụ**

#### **Điều kiện Lipschitz**
Gradient $$
abla f$$ liên tục Lipschitz với hằng số $$L > 0$$:
$$\lVert 
abla f(x) - 
abla f(y) 
Vert_2 \le L \lVert x - y 
Vert_2$$

#### **Định lý hội tụ cho hàm lồi**
Với kích thước bước cố định $$t \le rac{1}{L}$$:
$$f(x^{(k)}) - f^* \le rac{\lVert x^{(0)} - x^* 
Vert_2^2}{2tk}$$

**Tốc độ hội tụ:** $$O(1/k)$$ — hội tụ dưới tuyến tính (sublinear).

#### **Định lý hội tụ cho hàm lồi mạnh**
Nếu $$f$$ lồi mạnh với hằng số $$m > 0$$:
$$f(x^{(k)}) - f^* \le \left(1 - rac{m}{L}
ight)^k \left(f(x^{(0)}) - f^*
ight) \quad (t = 1/L)$$

**Tốc độ hội tụ:** $$O(
ho^k)$$ với $$
ho < 1$$ — hội tụ tuyến tính (linear).

#### **Chỉ số điều kiện**
$$\kappa = rac{L}{m}$$ — tỉ số giữa hằng số Lipschitz và hằng số lồi mạnh:
- $$\kappa$$ nhỏ: hội tụ nhanh.
- $$\kappa$$ lớn: hội tụ chậm (bài toán điều kiện xấu).

### 🎲 **Stochastic Gradient Descent (SGD)**

#### **Bài toán tổng**
$$\min_x f(x) = \min_x \sum_{i=1}^m f_i(x)$$

#### **Batch Gradient Descent**
$$x^{(k)} = x^{(k-1)} - t_k \sum_{i=1}^m 
abla f_i(x^{(k-1)})$$
**Chi phí:** $$O(m)$$ lần tính gradient trên mỗi bước lặp.

#### **Stochastic Gradient Descent**
$$x^{(k)} = x^{(k-1)} - t_k 
abla f_{i_k}(x^{(k-1)})$$
**Chi phí:** $$O(1)$$ lần tính gradient trên mỗi bước lặp.

#### **Chiến lược chọn chỉ số**
- **Quy tắc tuần hoàn:** $$i_k = 1, 2, \ldots, m, 1, 2, \ldots$$
- **Quy tắc ngẫu nhiên:** Chọn $$i_k$$ ngẫu nhiên đều từ $$\{1, 2, \ldots, m\}$$.

#### **Mini-batch SGD**
$$x^{(k)} = x^{(k-1)} - t_k rac{1}{b} \sum_{i \in \mathcal{B}_k} 
abla f_i(x^{(k-1)})$$
trong đó $$\mathcal{B}_k$$ là mini-batch gồm $$b$$ mẫu.

### ⚡ **Gradient Descent có Momentum**

#### **Momentum cổ điển**
$$egin{align}
v^{(k)} &= eta v^{(k-1)} + 
abla f(x^{(k-1)}) \
x^{(k)} &= x^{(k-1)} - t v^{(k)}
\end{align}$$

#### **Nesterov Accelerated Gradient (NAG)**
$$egin{align}
v^{(k)} &= eta v^{(k-1)} + 
abla f(x^{(k-1)} - teta v^{(k-1)}) \
x^{(k)} &= x^{(k-1)} - t v^{(k)}
\end{align}$$

**Tham số thường dùng:** $$eta = 0.9$$.

**Ưu điểm:**
- Tăng tốc độ hội tụ dọc theo các hướng nhất quán.
- Giảm dao động cục bộ.
- Hạn chế ảnh hưởng của nhiễu gradient.

### 🔄 **So sánh Các Phương pháp**

| Phương pháp | Tốc độ/lần lặp | Bộ nhớ | Hội tụ | Ứng dụng phù hợp |
|-------------|----------------|--------|--------|------------------|
| **Batch GD** | Chậm | Cao | Ổn định | Tập dữ liệu nhỏ |
| **SGD** | Nhanh | Thấp | Có nhiễu | Tập dữ liệu lớn |
| **Mini-batch** | Trung bình | Trung bình | Cân bằng | Thực tế phổ biến |
| **Momentum** | Nhanh | Thấp | Tăng tốc | Học sâu (deep learning) |

### 🛠️ **Các Kỹ thuật Thực tế**

#### **Lập lịch tốc độ học (Learning Rate Scheduling)**
- **Giảm theo bậc (Step decay):** $$t_k = t_0 \cdot \gamma^{\lfloor k/s 
floor}$$
- **Giảm theo hàm mũ (Exponential decay):** $$t_k = t_0 \cdot e^{-\lambda k}$$
- **Giảm theo đa thức (Polynomial decay):** $$t_k = t_0 \cdot (1 + \lambda k)^{-p}$$

#### **Phương pháp thích ứng (Adaptive Methods)**
- **AdaGrad:** Điều chỉnh tốc độ học dựa trên tổng bình phương gradient quá khứ.
- **RMSprop:** Cải tiến AdaGrad bằng trung bình trượt có trọng số mũ.
- **Adam:** Kết hợp momentum và tốc độ học thích ứng.

#### **Điều chuẩn (Regularization)**
- **Điều chuẩn L1:** $$f(x) + \lambda \lVert x 
Vert_1$$
- **Điều chuẩn L2:** $$f(x) + rac{\lambda}{2} \lVert x 
Vert_2^2$$
- **Dropout:** Tắt ngẫu nhiên các nút trong mạng nơ-ron khi huấn luyện.

### 📈 **Ứng dụng Thực tế**

#### **Học máy (Machine Learning)**
- **Hồi quy tuyến tính:** $$\min_w \lVert Xw - y 
Vert_2^2$$
- **Hồi quy logistic:** $$\min_w \sum_i \log(1 + e^{-y_i w^T x_i})$$
- **Mạng nơ-ron:** Lan truyền ngược (backpropagation) kết hợp SGD.

#### **Học sâu (Deep Learning)**
- **Mạng tích chập (CNNs)**
- **Mạng hồi quy (RNNs)**
- **Mô hình Transformer**

#### **Các bài toán tối ưu hóa khác**
- **Tối ưu hóa danh mục đầu tư**
- **Xử lý tín hiệu**
- **Thị giác máy tính**

### 🔍 **Tiêu chí Dừng**

#### **Theo chuẩn gradient**
$$\lVert 
abla f(x^{(k)}) 
Vert_2 < \epsilon$$

#### **Theo độ thay đổi giá trị hàm**
$$|f(x^{(k)}) - f(x^{(k-1)})| < \epsilon$$

#### **Theo độ thay đổi tham số**
$$\lVert x^{(k)} - x^{(k-1)} 
Vert_2 < \epsilon$$

#### **Theo số lần lặp tối đa**
$$k > k_{\max}$$

### ⚠️ **Thách thức và Giải pháp**

#### **Các vấn đề thường gặp:**
- **Gradient tiêu biến / bùng nổ (Vanishing/exploding gradients):** Gradient quá nhỏ hoặc quá lớn qua nhiều tầng.
- **Điểm yên ngựa (Saddle points):** Xuất hiện phổ biến trong không gian nhiều chiều.
- **Cực tiểu cục bộ (Local minima):** Với các hàm mục tiêu không lồi.
- **Điều kiện xấu (Ill-conditioning):** Chỉ số điều kiện $$\kappa$$ lớn.

#### **Các giải pháp phổ biến:**
- **Cắt ngưỡng gradient (Gradient clipping):** Giới hạn chuẩn của gradient.
- **Chuẩn hóa theo lô (Batch normalization):** Ổn định phân phối đầu vào của từng tầng.
- **Kết nối tắt (Residual connections):** Giúp lan truyền gradient ổn định hơn trong mạng sâu.
- **Tiền điều kiện hóa (Preconditioning):** Biến đổi thang đo không gian tối ưu.

### 💡 **Kinh nghiệm Thực hành**

#### **Chọn tốc độ học:**
1. Bắt đầu thử từ $$t = 0.01$$.
2. Điều chỉnh tăng hoặc giảm theo lũy thừa của 10.
3. Theo dõi đường cong mất mát (loss curve).
4. Kết hợp lập lịch giảm tốc độ học.

#### **Kiểm tra và gỡ lỗi:**
- Kiểm tra lại công thức tính gradient (so sánh với đạo hàm số).
- Trực quan hóa đường cong mất mát.
- Theo dõi chuẩn của gradient trong quá trình huấn luyện.
- Đánh giá định kỳ trên tập thẩm định (validation set).

#### **Tăng tốc huấn luyện:**
- Dùng mini-batch thay vì toàn tập.
- Huấn luyện song song hoặc phân tán.
- Tận dụng phần cứng tăng tốc (GPU).
- Huấn luyện với độ chính xác hỗn hợp (mixed precision).

---

💡 **Ghi chú:** Gradient descent là nền tảng của phần lớn thuật toán học máy hiện đại. Nắm vững các biến thể và kỹ thuật điều chỉnh sẽ giúp huấn luyện mô hình ổn định và hiệu quả hơn.

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
</style>

Bài tập trắc nghiệm này kiểm tra hiểu biết của bạn về thuật toán gradient descent và các biến thể, bao gồm lựa chọn kích thước bước, phân tích hội tụ, SGD và momentum.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>Bài tập trắc nghiệm: Gradient Descent</h2>
        <p>Chọn đáp án đúng nhất cho mỗi câu hỏi. Bài tập tập trung vào các khái niệm cơ bản và ứng dụng thực tế của gradient descent.</p>
        <div id="progress-bar">
            <div id="progress-fill"></div>
        </div>
        <p id="progress-text">Câu hỏi 1/25</p>
    </div>

    <div id="quiz-questions">
        <!-- Câu hỏi 1: Quy tắc cập nhật gradient descent -->
        <div class="question" id="q1">
            <h3>Câu 1: Quy tắc cập nhật cơ bản của gradient descent là:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) \(x^{(k)} = x^{(k-1)} + t \nabla f(x^{(k-1)})\)</label>
                <label><input type="radio" name="q1" value="b"> B) \(x^{(k)} = x^{(k-1)} - t \nabla f(x^{(k-1)})\)</label>
                <label><input type="radio" name="q1" value="c"> C) \(x^{(k)} = x^{(k-1)} - t \nabla^2 f(x^{(k-1)})\)</label>
                <label><input type="radio" name="q1" value="d"> D) \(x^{(k)} = x^{(k-1)} + t f(x^{(k-1)})\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$x^{(k)} = x^{(k-1)} - t \nabla f(x^{(k-1)})$$</strong><br>
                Gradient descent di chuyển theo hướng ngược với gradient để giảm giá trị hàm mục tiêu.
            </div>
        </div>

        <!-- Câu hỏi 2: Hướng giảm -->
        <div class="question" id="q2" style="display: none;">
            <h3>Câu 2: Hướng giảm trong gradient descent là:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) \(\Delta x = \nabla f(x)\)</label>
                <label><input type="radio" name="q2" value="b"> B) \(\Delta x = -\nabla f(x)\)</label>
                <label><input type="radio" name="q2" value="c"> C) \(\Delta x = \nabla^2 f(x)\)</label>
                <label><input type="radio" name="q2" value="d"> D) \(\Delta x = f(x)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$\Delta x = -\nabla f(x)$$</strong><br>
                Hướng giảm là âm của gradient, chỉ hướng giảm nhanh nhất của hàm số.
            </div>
        </div>

        <!-- Câu hỏi 3: Tác động của kích thước bước -->
        <div class="question" id="q3" style="display: none;">
            <h3>Câu 3: Nếu kích thước bước $$t$$ quá lớn, gradient descent có thể:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) Hội tụ nhanh hơn</label>
                <label><input type="radio" name="q3" value="b"> B) Vượt quá cực tiểu và phân kỳ</label>
                <label><input type="radio" name="q3" value="c"> C) Dừng lại ngay lập tức</label>
                <label><input type="radio" name="q3" value="d"> D) Tìm được nghiệm chính xác</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Vượt quá cực tiểu và phân kỳ</strong><br>
                Kích thước bước quá lớn có thể làm thuật toán dao động hoặc phân kỳ khỏi nghiệm tối ưu.
            </div>
        </div>

        <!-- Câu hỏi 4: Kích thước bước quá nhỏ -->
        <div class="question" id="q4" style="display: none;">
            <h3>Câu 4: Nếu kích thước bước $$t$$ quá nhỏ, gradient descent sẽ:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) Hội tụ rất chậm</label>
                <label><input type="radio" name="q4" value="b"> B) Phân kỳ</label>
                <label><input type="radio" name="q4" value="c"> C) Dao động</label>
                <label><input type="radio" name="q4" value="d"> D) Dừng ngay lập tức</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Hội tụ rất chậm</strong><br>
                Kích thước bước quá nhỏ làm thuật toán cập nhật rất chậm, cần nhiều lần lặp để hội tụ.
            </div>
        </div>

        <!-- Câu hỏi 5: Tìm kiếm đường lùi -->
        <div class="question" id="q5" style="display: none;">
            <h3>Câu 5: Tìm kiếm đường lùi (backtracking line search) hoạt động bằng cách:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) Tăng dần kích thước bước</label>
                <label><input type="radio" name="q5" value="b"> B) Bắt đầu với kích thước bước lớn và giảm dần</label>
                <label><input type="radio" name="q5" value="c"> C) Sử dụng kích thước bước cố định</label>
                <label><input type="radio" name="q5" value="d"> D) Tính toán đạo hàm bậc hai</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Bắt đầu với kích thước bước lớn và giảm dần</strong><br>
                Backtracking bắt đầu với bước lớn và giảm dần cho đến khi đạt được mức giảm đủ (điều kiện Armijo).
            </div>
        </div>

        <!-- Câu hỏi 6: Điều kiện Armijo -->
        <div class="question" id="q6" style="display: none;">
            <h3>Câu 6: Điều kiện Armijo trong backtracking yêu cầu:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) \(f(x + t\Delta x) \leq f(x)\)</label>
                <label><input type="radio" name="q6" value="b"> B) \(f(x + t\Delta x) \leq f(x) + \alpha t \nabla f(x)^T \Delta x\)</label>
                <label><input type="radio" name="q6" value="c"> C) \(f(x + t\Delta x) = f(x)\)</label>
                <label><input type="radio" name="q6" value="d"> D) \(\nabla f(x + t\Delta x) = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$f(x + t\Delta x) \leq f(x) + \alpha t \nabla f(x)^T \Delta x$$</strong><br>
                Điều kiện Armijo đảm bảo sự giảm đủ với tham số $$\alpha \in (0, 0.5)$$.
            </div>
        </div>

        <!-- Câu hỏi 7: Tìm kiếm đường chính xác -->
        <div class="question" id="q7" style="display: none;">
            <h3>Câu 7: Tìm kiếm đường chính xác (exact line search) tìm kích thước bước bằng cách:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) Sử dụng công thức cố định</label>
                <label><input type="radio" name="q7" value="b"> B) Tối thiểu hóa \(f(x - t \nabla f(x))\) theo \(t\)</label>
                <label><input type="radio" name="q7" value="c"> C) Chọn ngẫu nhiên</label>
                <label><input type="radio" name="q7" value="d"> D) Sử dụng đạo hàm bậc hai</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Tối thiểu hóa $$f(x - t \nabla f(x))$$ theo $$t$$</strong><br>
                Exact line search tìm kích thước bước tối ưu bằng cách giải bài toán tối ưu hóa một chiều.
            </div>
        </div>

        <!-- Câu hỏi 8: Điều kiện Lipschitz -->
        <div class="question" id="q8" style="display: none;">
            <h3>Câu 8: Điều kiện Lipschitz cho gradient có nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) \(\|\nabla f(x) - \nabla f(y)\| \leq L \|x - y\|\)</label>
                <label><input type="radio" name="q8" value="b"> B) \(\|f(x) - f(y)\| \leq L \|x - y\|\)</label>
                <label><input type="radio" name="q8" value="c"> C) \(\nabla f(x) = L\)</label>
                <label><input type="radio" name="q8" value="d"> D) \(f(x) \leq L\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\|\nabla f(x) - \nabla f(y)\| \leq L \|x - y\|$$</strong><br>
                Điều kiện Lipschitz đảm bảo gradient không thay đổi quá nhanh, quan trọng cho phân tích hội tụ.
            </div>
        </div>

        <!-- Câu hỏi 9: Tốc độ hội tụ gradient descent -->
        <div class="question" id="q9" style="display: none;">
            <h3>Câu 9: Với hàm lồi và gradient Lipschitz, gradient descent có tốc độ hội tụ:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) \(O(1/k^2)\)</label>
                <label><input type="radio" name="q9" value="b"> B) \(O(1/k)\)</label>
                <label><input type="radio" name="q9" value="c"> C) \(O(\log k)\)</label>
                <label><input type="radio" name="q9" value="d"> D) \(O(e^{-k})\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$O(1/k)$$</strong><br>
                Gradient descent có tốc độ hội tụ dưới tuyến tính (sublinear) $$O(1/k)$$ cho hàm lồi với gradient Lipschitz.
            </div>
        </div>

        <!-- Câu hỏi 10: SGD vs Batch GD -->
        <div class="question" id="q10" style="display: none;">
            <h3>Câu 10: Stochastic Gradient Descent (SGD) khác với Batch GD ở chỗ:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) SGD sử dụng tất cả dữ liệu mỗi lần cập nhật</label>
                <label><input type="radio" name="q10" value="b"> B) SGD chỉ sử dụng một mẫu dữ liệu mỗi lần cập nhật</label>
                <label><input type="radio" name="q10" value="c"> C) SGD không sử dụng gradient</label>
                <label><input type="radio" name="q10" value="d"> D) SGD luôn hội tụ nhanh hơn</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) SGD chỉ sử dụng một mẫu dữ liệu mỗi lần cập nhật</strong><br>
                SGD cập nhật tham số dựa trên gradient của một mẫu duy nhất thay vì toàn bộ tập dữ liệu.
            </div>
        </div>

        <!-- Câu hỏi 11: Ưu điểm của SGD -->
        <div class="question" id="q11" style="display: none;">
            <h3>Câu 11: Ưu điểm chính của SGD so với Batch GD là:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) Độ chính xác cao hơn</label>
                <label><input type="radio" name="q11" value="b"> B) Chi phí tính toán thấp hơn mỗi lần cập nhật</label>
                <label><input type="radio" name="q11" value="c"> C) Luôn hội tụ đến nghiệm tối ưu</label>
                <label><input type="radio" name="q11" value="d"> D) Không cần điều chỉnh tốc độ học</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Chi phí tính toán thấp hơn mỗi lần cập nhật</strong><br>
                SGD có độ phức tạp $$O(1)$$ mỗi lần cập nhật so với $$O(m)$$ của Batch GD, rất hiệu quả với tập dữ liệu lớn.
            </div>
        </div>

        <!-- Câu hỏi 12: Mini-batch GD -->
        <div class="question" id="q12" style="display: none;">
            <h3>Câu 12: Mini-batch Gradient Descent là sự kết hợp giữa:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) SGD và Newton method</label>
                <label><input type="radio" name="q12" value="b"> B) Batch GD và SGD</label>
                <label><input type="radio" name="q12" value="c"> C) Gradient descent và momentum</label>
                <label><input type="radio" name="q12" value="d"> D) Line search và fixed step</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Batch GD và SGD</strong><br>
                Mini-batch sử dụng một tập con nhỏ dữ liệu (thường 32-256 mẫu) để cân bằng giữa hiệu quả và ổn định.
            </div>
        </div>

        <!-- Câu hỏi 13: Quy tắc cập nhật momentum -->
        <div class="question" id="q13" style="display: none;">
            <h3>Câu 13: Quy tắc cập nhật của Gradient Descent với momentum là:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) \(v^{(k)} = \beta v^{(k-1)} + \nabla f(x^{(k-1)})\), \(x^{(k)} = x^{(k-1)} + t v^{(k)}\)</label>
                <label><input type="radio" name="q13" value="b"> B) \(v^{(k)} = \beta v^{(k-1)} + (1-\beta) \nabla f(x^{(k-1)})\), \(x^{(k)} = x^{(k-1)} - t v^{(k)}\)</label>
                <label><input type="radio" name="q13" value="c"> C) \(x^{(k)} = x^{(k-1)} - t \beta \nabla f(x^{(k-1)})\)</label>
                <label><input type="radio" name="q13" value="d"> D) \(x^{(k)} = \beta x^{(k-1)} - t \nabla f(x^{(k-1)})\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$v^{(k)} = \beta v^{(k-1)} + (1-\beta) \nabla f(x^{(k-1)})$$, $$x^{(k)} = x^{(k-1)} - t v^{(k)}$$</strong><br>
                Momentum tích lũy vận tốc với trung bình động có trọng số mũ của các gradient. (Dạng cổ điển $$v^{(k)} = \beta v^{(k-1)} + \nabla f(x^{(k-1)})$$, $$x^{(k)} = x^{(k-1)} - t v^{(k)}$$ cũng đúng, chỉ khác thang đo của $$t$$; phương án A sai vì đi theo hướng $$+v$$, tức là tăng hàm mục tiêu.)
            </div>
        </div>

        <!-- Câu hỏi 14: Hệ số momentum -->
        <div class="question" id="q14" style="display: none;">
            <h3>Câu 14: Hệ số momentum $$\beta$$ thường được chọn trong khoảng:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) [0.1, 0.3]</label>
                <label><input type="radio" name="q14" value="b"> B) [0.5, 0.7]</label>
                <label><input type="radio" name="q14" value="c"> C) [0.9, 0.99]</label>
                <label><input type="radio" name="q14" value="d"> D) [1.0, 1.5]</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) [0.9, 0.99]</strong><br>
                Hệ số momentum thường được chọn cao (0.9 hoặc 0.99) để duy trì "bộ nhớ" lâu dài của các gradient trước đó.
            </div>
        </div>

        <!-- Câu hỏi 15: Ưu điểm của momentum -->
        <div class="question" id="q15" style="display: none;">
            <h3>Câu 15: Momentum giúp gradient descent:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) Giảm dao động và tăng tốc hội tụ</label>
                <label><input type="radio" name="q15" value="b"> B) Tăng độ chính xác tính toán</label>
                <label><input type="radio" name="q15" value="c"> C) Giảm bộ nhớ sử dụng</label>
                <label><input type="radio" name="q15" value="d"> D) Loại bỏ hoàn toàn cực tiểu cục bộ</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Giảm dao động và tăng tốc hội tụ</strong><br>
                Momentum làm mượt quá trình tối ưu hóa, giảm dao động và giúp tăng tốc trong các hướng nhất quán.
            </div>
        </div>

        <!-- Câu hỏi 16: Nesterov Accelerated Gradient -->
        <div class="question" id="q16" style="display: none;">
            <h3>Câu 16: Nesterov Accelerated Gradient (NAG) khác với momentum thông thường ở chỗ:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) Sử dụng hệ số momentum khác</label>
                <label><input type="radio" name="q16" value="b"> B) Tính gradient tại vị trí "nhìn trước"</label>
                <label><input type="radio" name="q16" value="c"> C) Không sử dụng momentum</label>
                <label><input type="radio" name="q16" value="d"> D) Chỉ áp dụng cho hàm lồi</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Tính gradient tại vị trí "nhìn trước"</strong><br>
                NAG tính gradient tại $$x^{(k-1)} - t\beta v^{(k-1)}$$ thay vì $$x^{(k-1)}$$, cho phép "nhìn trước" hướng di chuyển.
            </div>
        </div>

        <!-- Câu hỏi 17: Ứng dụng gradient descent -->
        <div class="question" id="q17" style="display: none;">
            <h3>Câu 17: Gradient descent KHÔNG được sử dụng trực tiếp trong:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Huấn luyện neural networks</label>
                <label><input type="radio" name="q17" value="b"> B) Linear regression</label>
                <label><input type="radio" name="q17" value="c"> C) Logistic regression</label>
                <label><input type="radio" name="q17" value="d"> D) Integer programming</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Integer programming</strong><br>
                Integer programming là bài toán tối ưu rời rạc, không thể sử dụng gradient descent vì không có gradient.
            </div>
        </div>

        <!-- Câu hỏi 18: Điều kiện dừng -->
        <div class="question" id="q18" style="display: none;">
            <h3>Câu 18: Điều kiện dừng phổ biến cho gradient descent là:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) \(\|\nabla f(x)\| < \epsilon\)</label>
                <label><input type="radio" name="q18" value="b"> B) \(f(x) = 0\)</label>
                <label><input type="radio" name="q18" value="c"> C) \(x = 0\)</label>
                <label><input type="radio" name="q18" value="d"> D) \(t = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\|\nabla f(x)\| < \epsilon$$</strong><br>
                Thuật toán dừng khi độ lớn gradient nhỏ hơn ngưỡng $$\epsilon$$, cho thấy đã gần đạt cực tiểu.
            </div>
        </div>

        <!-- Câu hỏi 19: Hàm lồi mạnh -->
        <div class="question" id="q19" style="display: none;">
            <h3>Câu 19: Với hàm lồi mạnh, gradient descent có tốc độ hội tụ:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) \(O(1/k)\)</label>
                <label><input type="radio" name="q19" value="b"> B) \(O(1/k^2)\)</label>
                <label><input type="radio" name="q19" value="c"> C) \(O(\rho^k)\) với \(\rho < 1\) (linear)</label>
                <label><input type="radio" name="q19" value="d"> D) \(O(\log k)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) $$O(\rho^k)$$ với $$\rho < 1$$ (linear)</strong><br>
                Hàm lồi mạnh cho phép gradient descent đạt tốc độ hội tụ tuyến tính (geometric), nhanh hơn nhiều so với tốc độ dưới tuyến tính.
            </div>
        </div>

        <!-- Câu hỏi 20: Backpropagation -->
        <div class="question" id="q20" style="display: none;">
            <h3>Câu 20: Backpropagation trong neural networks về bản chất là:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Một thuật toán tối ưu hóa mới</label>
                <label><input type="radio" name="q20" value="b"> B) Cách hiệu quả để tính gradient cho gradient descent</label>
                <label><input type="radio" name="q20" value="c"> C) Thay thế cho gradient descent</label>
                <label><input type="radio" name="q20" value="d"> D) Chỉ áp dụng cho hàm tuyến tính</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Cách hiệu quả để tính gradient cho gradient descent</strong><br>
                Backpropagation sử dụng quy tắc dây chuyền (chain rule) để tính gradient hiệu quả trong mạng nơ-ron, sau đó dùng gradient descent để cập nhật trọng số.
            </div>
        </div>
        <!-- Câu hỏi 21: Thực hành -->
        <div class="question" id="q21" style="display: none;">
            <h3>Câu 21: Trong gradient descent, kích thước bước $$t = 0.01$$ có nghĩa là gì?</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) Di chuyển 1% theo hướng gradient</label>
                <label><input type="radio" name="q21" value="b"> B) Di chuyển theo hướng $$-\nabla f$$ một bước bằng 0.01 lần gradient (độ dài $$0.01\lVert\nabla f\rVert$$)</label>
                <label><input type="radio" name="q21" value="c"> C) Chia gradient cho 100</label>
                <label><input type="radio" name="q21" value="d"> D) Số lần lặp tối đa</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Di chuyển theo hướng $$-\nabla f$$ một bước bằng 0.01 lần gradient (độ dài $$0.01\lVert\nabla f\rVert$$)</strong><br>
                Kích thước bước $$t$$ xác định độ dài di chuyển theo hướng $$-\nabla f$$: $$x^{(k+1)} = x^{(k)} - t\nabla f(x^{(k)})$$.
            </div>
        </div>

        <!-- Câu hỏi 22: Thực hành -->
        <div class="question" id="q22" style="display: none;">
            <h3>Câu 22: Điều kiện Armijo trong line search kiểm tra:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) Giảm đủ của hàm mục tiêu</label>
                <label><input type="radio" name="q22" value="b"> B) Độ dốc của gradient</label>
                <label><input type="radio" name="q22" value="c"> C) Tính lồi của hàm</label>
                <label><input type="radio" name="q22" value="d"> D) Hội tụ của thuật toán</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Giảm đủ của hàm mục tiêu</strong><br>
                Điều kiện Armijo đảm bảo $$f(x + t\Delta x) \leq f(x) + c_1 t \nabla f(x)^T \Delta x$$ với $$c_1 \in (0,1)$$.
            </div>
        </div>

        <!-- Câu hỏi 23: Thực hành -->
        <div class="question" id="q23" style="display: none;">
            <h3>Câu 23: SGD khác với GD ở chỗ:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) Sử dụng toàn bộ dữ liệu</label>
                <label><input type="radio" name="q23" value="b"> B) Sử dụng một mẫu ngẫu nhiên</label>
                <label><input type="radio" name="q23" value="c"> C) Có kích thước bước cố định</label>
                <label><input type="radio" name="q23" value="d"> D) Luôn hội tụ nhanh hơn</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Sử dụng một mẫu ngẫu nhiên</strong><br>
                Stochastic Gradient Descent sử dụng một mẫu (hoặc mini-batch) ngẫu nhiên thay vì toàn bộ tập dữ liệu.
            </div>
        </div>

        <!-- Câu hỏi 24: Thực hành -->
        <div class="question" id="q24" style="display: none;">
            <h3>Câu 24: Momentum trong gradient descent giúp:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) Tăng tốc độ hội tụ</label>
                <label><input type="radio" name="q24" value="b"> B) Vượt qua cực tiểu cục bộ nông</label>
                <label><input type="radio" name="q24" value="c"> C) Giảm dao động</label>
                <label><input type="radio" name="q24" value="d"> D) Tất cả các lý do trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các lý do trên</strong><br>
                Momentum giúp tăng tốc hội tụ, giảm dao động và có thể vượt qua một số cực tiểu cục bộ nông.
            </div>
        </div>

        <!-- Câu hỏi 25: Thực hành -->
        <div class="question" id="q25" style="display: none;">
            <h3>Câu 25: Với hàm $$f(x) = x^2$$, gradient descent từ $$x_0 = 4$$ với $$t = 0.1$$ cho $$x_1 = ?$$</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) $$3.2$$</label>
                <label><input type="radio" name="q25" value="b"> B) $$4.8$$</label>
                <label><input type="radio" name="q25" value="c"> C) $$3.6$$</label>
                <label><input type="radio" name="q25" value="d"> D) $$2.4$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$3.2$$</strong><br>
                $$\nabla f(4) = 2 \cdot 4 = 8$$. $$x_1 = 4 - 0.1 \cdot 8 = 4 - 0.8 = 3.2$$.
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
    background: linear-gradient(90deg, #2196F3, #00BCD4);
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
    border-color: #2196F3;
    background-color: #e3f2fd;
}

.options input[type="radio"] {
    margin-right: 12px;
    margin-top: 2px;
    transform: scale(1.2);
    flex-shrink: 0;
}

.options label.selected {
    border-color: #2196F3;
    background-color: #bbdefb;
}

.explanation {
    margin-top: 20px;
    padding: 15px;
    background-color: #e3f2fd;
    border-left: 4px solid #2196F3;
    border-radius: 4px;
    font-size: 0.95em;
    line-height: 1.5;
}

.explanation strong {
    color: #1565C0;
}

#quiz-navigation {
    text-align: center;
    margin: 30px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

#quiz-navigation button {
    background: #2196F3;
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.2s ease;
}

#quiz-navigation button:hover:not(:disabled) {
    background: #1976D2;
}

#quiz-navigation button:disabled {
    background: #cccccc;
    cursor: not-allowed;
}

#quiz-results {
    text-align: center;
    padding: 30px;
    background: #e3f2fd;
    border-radius: 8px;
    border: 2px solid #2196F3;
}

#score-display {
    font-size: 1.5em;
    font-weight: bold;
    margin: 20px 0;
    color: #1565C0;
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
    q1: 'b', q2: 'b', q3: 'b', q4: 'a', q5: 'b',
    q6: 'b', q7: 'b', q8: 'a', q9: 'b', q10: 'b',
    q11: 'b', q12: 'b', q13: 'b', q14: 'c', q15: 'a',
    q16: 'b', q17: 'd', q18: 'a', q19: 'c', q20: 'b'
,
    q21: 'b', q22: 'a', q23: 'b', q24: 'd', q25: 'a'};

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
    
    // Re-render MathJax for the newly displayed question
    if (window.MathJax && MathJax.startup && MathJax.startup.promise) {
        MathJax.startup.promise.then(() => MathJax.typesetPromise([document.getElementById(`q${questionNum}`)]));
    }
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
            ${scorePercentage >= 80 ? '🎉 Xuất sắc! Bạn đã nắm vững gradient descent và các biến thể!' : 
              scorePercentage >= 60 ? '👍 Khá tốt! Hãy ôn lại một số khái niệm về SGD và momentum.' : 
              scorePercentage >= 40 ? '📚 Cần ôn tập thêm về thuật toán gradient descent.' : '💪 Hãy đọc lại lý thuyết về gradient descent từ đầu!'}
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
