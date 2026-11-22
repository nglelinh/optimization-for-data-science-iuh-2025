---
layout: post
title: 09-10 Bài tập trắc nghiệm - Phương Pháp Proximal Gradient
chapter: '09'
order: 12
owner: GitHub Copilot
lang: vi
categories:
- chapter09
lesson_type: quiz
---

## 📚 Ôn tập lý thuyết

Trước khi làm bài tập, hãy ôn lại các khái niệm chính trong chương này:

### ⚡ **Phương Pháp Gradient Gần Kề (Proximal Gradient)**

#### **Bài toán tổng hợp (Composite)**
Xét hàm mục tiêu có thể phân tách thành hai phần:
$$f(x) = g(x) + h(x)$$

trong đó:
- $$g(x)$$: hàm lồi, khả vi, $$\text{dom}(g) = \mathbb{R}^n$$.
- $$h(x)$$: hàm lồi, có thể không khả vi.

#### **Ý tưởng chính**
- **Xấp xỉ $$g$$:** Dùng khai triển Taylor bậc hai với ma trận Hessian thay bằng $$\frac{1}{t}I$$.
- **Giữ nguyên $$h$$:** Không xấp xỉ phần không khả vi.
- **Kết hợp tối ưu:** Tìm điểm cực tiểu của tổng hàm xấp xỉ bậc hai và $$h$$.

#### **Thuật toán cơ bản**
$$x^{(k)} = \text{prox}_{t_k}(x^{(k-1)} - t_k \nabla g(x^{(k-1)}))$$

với **ánh xạ gần kề (proximal mapping):**
$$\text{prox}_t(x) = \underset{z}{\arg\min} \left\{ \frac{1}{2t} \lVert x - z \rVert_2^2 + h(z) \right\}$$

#### **Diễn giải trực quan**
1. **Bước gradient:** $$x - t\nabla g(x)$$ (một bước gradient descent trên $$g$$).
2. **Điều chỉnh gần kề:** Tìm điểm vừa gần kết quả bước gradient, vừa làm nhỏ $$h$$.
3. **Cân bằng:** Tham số $$t$$ điều tiết giữa việc bám theo bước gradient và việc làm nhỏ $$h$$.

### 📏 **Ánh Xạ Gần Kề (Proximal Mapping)**

#### **Định nghĩa**
$$\text{prox}_t(x) = \underset{z}{\arg\min} \left\{ \frac{1}{2t} \lVert x - z \rVert_2^2 + h(z) \right\}$$

#### **Tính chất quan trọng**
- **Chỉ phụ thuộc vào $$h$$:** Độc lập với hàm $$g$$.
- **Có dạng đóng:** Tính được trực tiếp cho nhiều hàm $$h$$ phổ biến.
- **Đơn trị:** Nghiệm tồn tại duy nhất do tính lồi chặt của bài toán con.
- **Không giãn (Non-expansive):** $$\lVert \text{prox}_t(x) - \text{prox}_t(y) \rVert \le \lVert x - y \rVert$$.

#### **Các ví dụ tiêu biểu**

**1. Chuẩn L1 (LASSO):**
$$h(x) = \lambda \lVert x \rVert_1 \Rightarrow \text{prox}_t(x) = S_{\lambda t}(x)$$

**Toán tử ngưỡng mềm (Soft-thresholding):**
$$[S_{\lambda t}(x)]_i = \begin{cases}
x_i - \lambda t & \text{nếu } x_i > \lambda t \\
0 & \text{nếu } |x_i| \le \lambda t \\
x_i + \lambda t & \text{nếu } x_i < -\lambda t
\end{cases}$$

**2. Hàm chỉ thị (Phép chiếu):**
$$h(x) = I_C(x) \Rightarrow \text{prox}_t(x) = P_C(x)$$

**3. Chuẩn L2:**
$$h(x) = \lambda \lVert x \rVert_2 \Rightarrow \text{prox}_t(x) = \max\left\{0, 1 - \frac{\lambda t}{\lVert x \rVert_2}\right\} x$$

### 📊 **Phân Tích Hội Tụ**

#### **Giả thiết**
- $$g$$ lồi, khả vi với $$\nabla g$$ liên tục Lipschitz (hằng số $$L$$).
- $$h$$ lồi và $$\text{prox}_t$$ tính được.

#### **Định lý hội tụ**
Với kích thước bước cố định $$t \le 1/L$$:
$$f(x^{(k)}) - f^* \le \frac{\lVert x^{(0)} - x^* \rVert_2^2}{2tk}$$

**Ý nghĩa:**
- **Tốc độ hội tụ:** $$O(1/k)$$ (cùng bậc với gradient descent).
- **Điều kiện kích thước bước:** $$t \le 1/L$$ (tương tự gradient descent).
- **Hiệu quả:** Tương đương gradient descent xét theo số bước lặp.

#### **Tìm kiếm đường thẳng lùi (Backtracking line search)**
**Điều kiện kiểm tra:**
$$g(x - tG_t(x)) > g(x) - t\nabla g(x)^T G_t(x) + \frac{t}{2} \lVert G_t(x) \rVert_2^2$$

với $$G_t(x) = \frac{x - \text{prox}_t(x - t\nabla g(x))}{t}$$.

**Lưu ý:** Điều kiện lùi chỉ đánh giá trên phần trơn $$g$$, không đánh giá trên toàn bộ $$f$$.

### 🎯 **Ví Dụ: ISTA (Iterative Soft-Thresholding Algorithm)**

#### **Bài toán LASSO**
$$\min_\beta \frac{1}{2} \lVert y - X\beta \rVert_2^2 + \lambda \lVert \beta \rVert_1$$

**Phân tách:**
- $$g(\beta) = \frac{1}{2} \lVert y - X\beta \rVert_2^2$$ (khả vi).
- $$h(\beta) = \lambda \lVert \beta \rVert_1$$ (không khả vi).

#### **Gradient của $$g$$**
$$\nabla g(\beta) = -X^T(y - X\beta) = X^T(X\beta - y)$$

#### **Bước cập nhật ISTA**
$$\beta^{(k)} = S_{\lambda t}(\beta^{(k-1)} + tX^T(y - X\beta^{(k-1)}))$$

**Ưu điểm:** Công thức đơn giản và hội tụ nhanh hơn nhiều so với phương pháp subgradient.

### 🎯 **Ví Dụ: Hoàn Thiện Ma Trận (Matrix Completion)**

#### **Bài toán**
$$\min_B \frac{1}{2} \sum_{(i,j) \in \Omega} (Y_{ij} - B_{ij})^2 + \lambda \lVert B \rVert_{tr}$$

**Phân tách:**
- $$g(B) = \frac{1}{2} \lVert P_\Omega(Y) - P_\Omega(B) \rVert_F^2$$ (khả vi).
- $$h(B) = \lambda \lVert B \rVert_{tr}$$ (chuẩn vết, không khả vi).

#### **Toán tử chiếu**
$$[P_\Omega(B)]_{ij} = \begin{cases}
B_{ij} & \text{nếu } (i,j) \in \Omega \\
0 & \text{trường hợp khác}
\end{cases}$$

#### **Gradient của $$g$$**
$$\nabla g(B) = -(P_\Omega(Y) - P_\Omega(B))$$

#### **Ánh xạ gần kề cho chuẩn vết**
$$\text{prox}_t(B) = S_{\lambda t}(B)$$ (ngưỡng mềm ma trận).

Nếu $$B = U\Sigma V^T$$ (phân tích SVD), thì:
$$S_{\lambda t}(B) = U\Sigma_{\lambda t} V^T$$

với $$(\Sigma_{\lambda t})_{ii} = \max\{\Sigma_{ii} - \lambda t, 0\}$$.

#### **Thuật toán Soft-Impute**
$$B^{(k)} = S_{\lambda}(P_\Omega(Y) + P_\Omega^\perp(B^{(k-1)}))$$

### 🔄 **Các Trường Hợp Đặc Biệt**

Phương pháp gradient gần kề là **khuôn khổ tổng quát** bao gồm:

#### **1. Gradient Descent**
$$h = 0 \Rightarrow \text{prox}_t(x) = x$$
$$x^{(k)} = x^{(k-1)} - t\nabla g(x^{(k-1)})$$

#### **2. Gradient Descent có chiếu (Projected Gradient Descent)**
$$h = I_C \Rightarrow \text{prox}_t(x) = P_C(x)$$
$$x^{(k)} = P_C(x^{(k-1)} - t\nabla g(x^{(k-1)}))$$

#### **3. Thuật toán tối ưu gần kề (PMA)**
$$g = 0 \Rightarrow x^{(k)} = \text{prox}_t(x^{(k-1)})$$

### ⚡ **Gradient Gần Kề Tăng Tốc (FISTA)**

#### **Ý tưởng**
Bổ sung **động lượng** để nâng tốc độ hội tụ từ $$O(1/k)$$ lên $$O(1/k^2)$$.

#### **Thuật toán**
$$v = x^{(k-1)} + \frac{k-2}{k+1}(x^{(k-1)} - x^{(k-2)})$$
$$x^{(k)} = \text{prox}_{t_k}(v - t_k \nabla g(v))$$

#### **Trọng số động lượng**
$$\frac{k-2}{k+1} \to 1$$ khi $$k \to \infty$$.

#### **Đặc điểm**
- **Tốc độ hội tụ:** $$O(1/k^2)$$ — tối ưu trong lớp các phương pháp bậc nhất.
- **Không đơn điệu:** Giá trị hàm mục tiêu có thể tăng tạm thời ("gợn sóng Nesterov").
- **Hiệu quả:** Cải thiện rõ rệt trên các bài toán có số điều kiện lớn.

#### **FISTA cho LASSO**
Giảm đáng kể số bước lặp so với cả ISTA và phương pháp subgradient.

### 🔄 **So Sánh Các Phương Pháp**

| Phương pháp | Điều kiện | Tốc độ hội tụ | Ứng dụng |
|-------------|-----------|---------------|----------|
| **Gradient Descent** | $$f$$ khả vi | $$O(1/k)$$ | Tối ưu hàm trơn |
| **Subgradient** | $$f$$ lồi | $$O(1/\sqrt{k})$$ | Hàm không trơn tổng quát |
| **Gradient gần kề** | $$f = g + h$$, $$g$$ trơn | $$O(1/k)$$ | Bài toán tổng hợp |
| **Gradient gần kề tăng tốc** | $$f = g + h$$, $$g$$ trơn | $$O(1/k^2)$$ | Bài toán tổng hợp cần hội tụ nhanh |

### 🛠️ **Kỹ Thuật Thực Hành**

#### **Khi nào nên dùng Gradient gần kề:**
- **Hàm tổng hợp:** $$f = g + h$$ với $$g$$ trơn, $$h$$ không trơn.
- **Bài toán chính quy hóa:** LASSO, elastic net, group LASSO.
- **Tối ưu có ràng buộc:** Gradient descent có chiếu.
- **Bài toán ma trận:** Hoàn thiện ma trận, phân tích thành phần chính bền vững (robust PCA).
- **Tối ưu thưa:** Chọn đặc trưng, cảm biến nén.

#### **Điều kiện triển khai hiệu quả:**
1. **Tính $$\nabla g$$:** Gradient của phần trơn phải tính được nhanh.
2. **Tính $$\text{prox}_t$$:** Có công thức giải tích hoặc bộ giải con hiệu quả.
3. **Hằng số Lipschitz $$L$$:** Giúp chọn kích thước bước ổn định.

#### **Gỡ lỗi và tinh chỉnh:**
- **Kiểm tra ánh xạ gần kề:** Xác minh công thức trên các ví dụ nhỏ.
- **Chọn kích thước bước:** Bước cố định ($$t = 1/L$$) hoặc tìm kiếm đường thẳng lùi.
- **Theo dõi hội tụ:** Quan sát $$f(x^{(k)})$$ qua các vòng lặp.
- **Tăng tốc:** Thử FISTA nếu phương pháp cơ bản hội tụ chậm.

### 📈 **Ứng Dụng Thực Tế**

#### **1. Học máy**
- **Hồi quy LASSO:** Chọn lọc đặc trưng.
- **Elastic Net:** Kết hợp chính quy hóa L1 và L2.
- **Group LASSO:** Tạo tính thưa theo nhóm biến.
- **Hồi quy Logistic thưa:** Phân loại kết hợp chọn đặc trưng.

#### **2. Xử lý tín hiệu**
- **Cảm biến nén (Compressed Sensing):** Khôi phục tín hiệu thưa.
- **Khử nhiễu ảnh:** Chính quy hóa biến phân toàn phần (Total Variation).
- **Hoàn thiện ma trận:** Lọc cộng tác, hệ thống gợi ý.

#### **3. Thị giác máy tính**
- **Phân đoạn ảnh:** Các phương pháp biến phân toàn phần.
- **Dòng quang học (Optical Flow):** Ước lượng chuyển động có chính quy hóa.
- **Tái tạo cấu trúc từ chuyển động:** Tối ưu thưa trong bundle adjustment.

#### **4. Thống kê**
- **Chọn biến:** Hồi quy nhiều chiều.
- **Thống kê bền vững:** Hàm mất mát Huber, hồi quy phân vị.
- **Mô hình đồ thị:** Ước lượng ma trận độ chính xác thưa.

### 💡 **Ví Dụ Minh Họa**

#### **Bài toán:** $$\min_x \frac{1}{2}(x-2)^2 + |x|$$

**Phân tách:**
- $$g(x) = \frac{1}{2}(x-2)^2$$, $$\nabla g(x) = x-2$$
- $$h(x) = |x|$$

**Ánh xạ gần kề:**
$$\text{prox}_t(x) = S_t(x) = \begin{cases}
x - t & \text{nếu } x > t \\
0 & \text{nếu } |x| \le t \\
x + t & \text{nếu } x < -t
\end{cases}$$

**Một bước gradient gần kề:**
1. Bước gradient: $$x - t(x-2) = (1-t)x + 2t$$.
2. Áp dụng ngưỡng mềm: $$\text{prox}_t((1-t)x + 2t)$$.

### 🎯 **Kết Nối Với Các Chương Khác**

#### **Từ các chương trước:**
- **Chương 08:** Phương pháp subgradient cho hàm không trơn.
- **Chương 07:** Gradient dưới và vi phân dưới.
- **Chương 06:** Gradient descent cho hàm trơn.

#### **Ưu điểm của Gradient gần kề:**
- **Nhanh hơn subgradient:** $$O(1/k)$$ so với $$O(1/\sqrt{k})$$.
- **Tổng quát hơn gradient descent:** Xử lý trực tiếp thành phần không trơn.
- **Có thể tăng tốc:** FISTA đạt tốc độ $$O(1/k^2)$$.

#### **Hướng mở rộng:**
- **ADMM:** Phương pháp nhân tử theo hướng luân phiên.
- **Phương pháp gốc–đối ngẫu:** Xử lý bài toán có ràng buộc phức tạp.
- **Biến thể ngẫu nhiên:** Phiên bản mini-batch và trực tuyến.

### 🌟 **Ý Nghĩa Lý Thuyết**

#### **Toán tử gần kề như "gradient tổng quát":**
- **Gradient:** $$\nabla f(x)$$ cho hàm trơn.
- **Subgradient:** $$\partial f(x)$$ cho hàm không trơn.
- **Toán tử gần kề:** $$\text{prox}_t$$ cho bài toán tổng hợp.

#### **Bao Moreau (Moreau envelope):**
$$f_t(x) = \min_z \left\{ f(z) + \frac{1}{2t}\lVert x - z \rVert^2 \right\}$$

**Tính chất:** $$f_t$$ là hàm trơn với $$\nabla f_t(x) = \frac{x - \text{prox}_t(x)}{t}$$.

#### **Liên hệ với giải tích biến phân:**
- Gradient gần kề ↔ Tách xuôi–ngược (forward-backward splitting).
- Tăng tốc ↔ Các phương pháp có quán tính.
- Tốc độ hội tụ ↔ Lý thuyết độ phức tạp tối ưu.

### 💡 **Mẹo Thực Hành**

#### **Lựa chọn phương pháp phù hợp:**
1. **Hàm trơn:** Gradient descent.
2. **Hàm không trơn tổng quát:** Phương pháp subgradient.
3. **Hàm tổng hợp có prox dễ tính:** Phương pháp gradient gần kề.
4. **Cần hội tụ nhanh hơn:** FISTA.
5. **Có ràng buộc tập lồi:** Gradient descent có chiếu.

#### **Kinh nghiệm cài đặt:**
- **Vector hóa phép tính:** Tận dụng tính toán song song.
- **Khởi tạo ấm (Warm start):** Dùng nghiệm của tham số trước làm điểm khởi tạo.
- **Bước thích nghi:** Dùng tìm kiếm đường thẳng lùi khi không biết $$L$$.
- **Dừng sớm:** Theo dõi tiêu chuẩn hội tụ qua từng bước.

#### **Lỗi thường gặp:**
- **Sai công thức toán tử gần kề:** Cần kiểm tra kỹ ngưỡng và hệ số $$t$$.
- **Kích thước bước quá lớn:** Có thể gây phân kỳ.
- **Bỏ qua hằng số Lipschitz:** Ảnh hưởng trực tiếp đến điều kiện hội tụ.
- **Không chuẩn hóa dữ liệu:** Làm xấu số điều kiện và giảm ổn định số học.

---

💡 **Ghi chú:** Phương pháp gradient gần kề là cầu nối tự nhiên giữa tối ưu hàm trơn và tối ưu hàm không trơn, giữ vai trò trọng tâm trong học máy có chính quy hóa.

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

Bài tập trắc nghiệm này kiểm tra hiểu biết của bạn về phương pháp gradient gần kề (proximal gradient method), proximal operator, composite optimization và acceleration methods như FISTA.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>🎯 Quiz: Phương Pháp Proximal Gradient</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 5%"></div>
        </div>
        <div class="score-display" id="score-display">Câu hỏi: <span id="current-q">1</span> / <span id="total-q">20</span></div>
    </div>

    <div id="quiz-content">
        <!-- Câu hỏi 1: Composite function form -->
        <div class="question" id="q1" style="display: block;">
            <h3>Câu 1: Proximal gradient method áp dụng cho bài toán có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) \(\min f(x)\) với \(f\) khả vi</label>
                <label><input type="radio" name="q1" value="b"> B) \(\min f(x) = g(x) + h(x)\) với \(g\) khả vi, \(h\) lồi</label>
                <label><input type="radio" name="q1" value="c"> C) \(\min f(x)\) với \(f\) không lồi</label>
                <label><input type="radio" name="q1" value="d"> D) \(\min f(x)\) với ràng buộc tuyến tính</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$\min f(x) = g(x) + h(x)$$ với $$g$$ khả vi, $$h$$ lồi</strong><br>
                Proximal gradient method được thiết kế cho composite optimization với $$g$$ khả vi và $$h$$ có thể không khả vi.
            </div>
        </div>

        <!-- Câu hỏi 2: Proximal operator definition -->
        <div class="question" id="q2" style="display: none;">
            <h3>Câu 2: Proximal operator của hàm \(h\) được định nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) \(\text{prox}_h(v) = \arg\min_x \{h(x) + \frac{1}{2}\|x - v\|^2\}\)</label>
                <label><input type="radio" name="q2" value="b"> B) \(\text{prox}_h(v) = \arg\min_x \{h(x) - \frac{1}{2}\|x - v\|^2\}\)</label>
                <label><input type="radio" name="q2" value="c"> C) \(\text{prox}_h(v) = \arg\min_x \{h(x) + \|x - v\|\}\)</label>
                <label><input type="radio" name="q2" value="d"> D) \(\text{prox}_h(v) = v - \nabla h(v)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\text{prox}_h(v) = \arg\min_x \{h(x) + \frac{1}{2}\|x - v\|^2\}$$</strong><br>
                Proximal operator cân bằng giữa việc giảm thiểu $$h(x)$$ và giữ $$x$$ gần với $$v$$.
            </div>
        </div>

        <!-- Câu hỏi 3: Proximal gradient update -->
        <div class="question" id="q3" style="display: none;">
            <h3>Câu 3: Công thức cập nhật của proximal gradient method là:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) \(x^{(k+1)} = x^{(k)} - t \nabla g(x^{(k)})\)</label>
                <label><input type="radio" name="q3" value="b"> B) \(x^{(k+1)} = \text{prox}_{th}(x^{(k)} - t \nabla g(x^{(k)}))\)</label>
                <label><input type="radio" name="q3" value="c"> C) \(x^{(k+1)} = \text{prox}_{tg}(x^{(k)} - t \nabla h(x^{(k)}))\)</label>
                <label><input type="radio" name="q3" value="d"> D) \(x^{(k+1)} = x^{(k)} - t(\nabla g(x^{(k)}) + \nabla h(x^{(k)}))\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$x^{(k+1)} = \text{prox}_{th}(x^{(k)} - t \nabla g(x^{(k)}))$$</strong><br>
                Thực hiện gradient step cho $$g$$ rồi áp dụng proximal operator cho $$h$$.
            </div>
        </div>

        <!-- Câu hỏi 4: Proximal operator of L1 norm -->
        <div class="question" id="q4" style="display: none;">
            <h3>Câu 4: Proximal operator của \(h(x) = \lambda\|x\|_1\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) \(\text{prox}_{\lambda\|\cdot\|_1}(v) = v - \lambda\)</label>
                <label><input type="radio" name="q4" value="b"> B) \(\text{prox}_{\lambda\|\cdot\|_1}(v) = \text{sign}(v) \max(|v| - \lambda, 0)\)</label>
                <label><input type="radio" name="q4" value="c"> C) \(\text{prox}_{\lambda\|\cdot\|_1}(v) = \frac{v}{1 + \lambda}\)</label>
                <label><input type="radio" name="q4" value="d"> D) \(\text{prox}_{\lambda\|\cdot\|_1}(v) = v\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$\text{prox}_{\lambda\|\cdot\|_1}(v) = \text{sign}(v) \max(|v| - \lambda, 0)$$</strong><br>
                Đây là soft thresholding operator, co các thành phần về phía 0 một lượng $$\lambda$$.
            </div>
        </div>

        <!-- Câu hỏi 5: Proximal operator of L2 norm squared -->
        <div class="question" id="q5" style="display: none;">
            <h3>Câu 5: Proximal operator của \(h(x) = \frac{\lambda}{2}\|x\|_2^2\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) \(\text{prox}_{\frac{\lambda}{2}\|\cdot\|_2^2}(v) = \frac{v}{1 + \lambda}\)</label>
                <label><input type="radio" name="q5" value="b"> B) \(\text{prox}_{\frac{\lambda}{2}\|\cdot\|_2^2}(v) = v - \lambda v\)</label>
                <label><input type="radio" name="q5" value="c"> C) \(\text{prox}_{\frac{\lambda}{2}\|\cdot\|_2^2}(v) = v\)</label>
                <label><input type="radio" name="q5" value="d"> D) \(\text{prox}_{\frac{\lambda}{2}\|\cdot\|_2^2}(v) = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\text{prox}_{\frac{\lambda}{2}\|\cdot\|_2^2}(v) = \frac{v}{1 + \lambda}$$</strong><br>
                Proximal operator của quadratic function có dạng shrinkage với hệ số $$\frac{1}{1 + \lambda}$$.
            </div>
        </div>

        <!-- Câu hỏi 6: Convergence rate -->
        <div class="question" id="q6" style="display: none;">
            <h3>Câu 6: Tốc độ hội tụ của proximal gradient method là:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) \(O(1/k^2)\)</label>
                <label><input type="radio" name="q6" value="b"> B) \(O(1/k)\)</label>
                <label><input type="radio" name="q6" value="c"> C) \(O(1/\sqrt{k})\)</label>
                <label><input type="radio" name="q6" value="d"> D) \(O(e^{-k})\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$O(1/k)$$</strong><br>
                Proximal gradient method có tốc độ hội tụ $$O(1/k)$$ giống như gradient descent cho hàm lồi.
            </div>
        </div>

        <!-- Câu hỏi 7: When to use proximal gradient -->
        <div class="question" id="q7" style="display: none;">
            <h3>Câu 7: Proximal gradient method thích hợp khi:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) Cả \(g\) và \(h\) đều khả vi</label>
                <label><input type="radio" name="q7" value="b"> B) \(g\) khả vi và proximal operator của \(h\) dễ tính</label>
                <label><input type="radio" name="q7" value="c"> C) Cả \(g\) và \(h\) đều không khả vi</label>
                <label><input type="radio" name="q7" value="d"> D) Hàm mục tiêu không lồi</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$g$$ khả vi và proximal operator của $$h$$ dễ tính</strong><br>
                Phương pháp này hiệu quả khi có thể tính gradient của $$g$$ và proximal operator của $$h$$ một cách dễ dàng.
            </div>
        </div>

        <!-- Câu hỏi 8: FISTA algorithm -->
        <div class="question" id="q8" style="display: none;">
            <h3>Câu 8: FISTA (Fast Iterative Shrinkage-Thresholding Algorithm) là:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) Phiên bản chậm của proximal gradient</label>
                <label><input type="radio" name="q8" value="b"> B) Phiên bản tăng tốc của proximal gradient với momentum</label>
                <label><input type="radio" name="q8" value="c"> C) Thuật toán cho bài toán không lồi</label>
                <label><input type="radio" name="q8" value="d"> D) Thuật toán chỉ cho L1 regularization</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Phiên bản tăng tốc của proximal gradient với momentum</strong><br>
                FISTA sử dụng momentum để đạt tốc độ hội tụ $$O(1/k^2)$$ thay vì $$O(1/k)$$.
            </div>
        </div>

        <!-- Câu hỏi 9: FISTA convergence rate -->
        <div class="question" id="q9" style="display: none;">
            <h3>Câu 9: Tốc độ hội tụ của FISTA là:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) \(O(1/k^2)\)</label>
                <label><input type="radio" name="q9" value="b"> B) \(O(1/k)\)</label>
                <label><input type="radio" name="q9" value="c"> C) \(O(1/\sqrt{k})\)</label>
                <label><input type="radio" name="q9" value="d"> D) \(O(e^{-k})\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$O(1/k^2)$$</strong><br>
                FISTA đạt tốc độ hội tụ optimal $$O(1/k^2)$$ cho first-order methods trên hàm lồi.
            </div>
        </div>

        <!-- Câu hỏi 10: FISTA momentum parameter -->
        <div class="question" id="q10" style="display: none;">
            <h3>Câu 10: Trong FISTA, tham số momentum \(t_k\) được cập nhật theo công thức:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) \(t_{k+1} = \frac{1 + \sqrt{1 + 4t_k^2}}{2}\)</label>
                <label><input type="radio" name="q10" value="b"> B) \(t_{k+1} = t_k + 1\)</label>
                <label><input type="radio" name="q10" value="c"> C) \(t_{k+1} = 0.9 t_k\)</label>
                <label><input type="radio" name="q10" value="d"> D) \(t_{k+1} = 1\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$t_{k+1} = \frac{1 + \sqrt{1 + 4t_k^2}}{2}$$</strong><br>
                Đây là công thức đặc biệt trong FISTA để đảm bảo tốc độ hội tụ optimal.
            </div>
        </div>

        <!-- Câu hỏi 11: Proximal operator properties -->
        <div class="question" id="q11" style="display: none;">
            <h3>Câu 11: Proximal operator có tính chất:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) Không làm tăng khoảng cách (non-expansive, với $$h$$ lồi)</label>
                <label><input type="radio" name="q11" value="b"> B) Tăng khoảng cách</label>
                <label><input type="radio" name="q11" value="c"> C) Không liên tục</label>
                <label><input type="radio" name="q11" value="d"> D) Chỉ áp dụng cho hàm khả vi</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Không làm tăng khoảng cách (non-expansive, với $$h$$ lồi)</strong><br>
                $$\|\text{prox}_h(u) - \text{prox}_h(v)\| \leq \|u - v\|$$ với mọi $$u, v$$, đây là tính chất quan trọng cho phân tích hội tụ.
            </div>
        </div>

        <!-- Câu hỏi 12: Lasso problem -->
        <div class="question" id="q12" style="display: none;">
            <h3>Câu 12: Bài toán Lasso \(\min \frac{1}{2}\|Ax - b\|_2^2 + \lambda\|x\|_1\) có thể giải bằng:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) Gradient descent</label>
                <label><input type="radio" name="q12" value="b"> B) Proximal gradient với \(g(x) = \frac{1}{2}\|Ax - b\|_2^2\), \(h(x) = \lambda\|x\|_1\)</label>
                <label><input type="radio" name="q12" value="c"> C) Newton method</label>
                <label><input type="radio" name="q12" value="d"> D) Không thể giải được</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Proximal gradient với $$g(x) = \frac{1}{2}\|Ax - b\|_2^2$$, $$h(x) = \lambda\|x\|_1$$</strong><br>
                Lasso là ví dụ điển hình của composite optimization với $$g$$ khả vi và $$h$$ không khả vi.
            </div>
        </div>

        <!-- Câu hỏi 13: Matrix completion -->
        <div class="question" id="q13" style="display: none;">
            <h3>Câu 13: Trong matrix completion, proximal operator của nuclear norm thực hiện:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) Hard thresholding trên singular values</label>
                <label><input type="radio" name="q13" value="b"> B) Soft thresholding trên singular values</label>
                <label><input type="radio" name="q13" value="c"> C) Không thay đổi ma trận</label>
                <label><input type="radio" name="q13" value="d"> D) Đặt tất cả phần tử bằng 0</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Soft thresholding trên singular values</strong><br>
                Proximal operator của nuclear norm $$\|X\|_*$$ thực hiện SVD và soft thresholding trên các singular values.
            </div>
        </div>

        <!-- Câu hỏi 14: Backtracking line search -->
        <div class="question" id="q14" style="display: none;">
            <h3>Câu 14: Trong proximal gradient method, có thể sử dụng backtracking line search không?</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) Không, vì hàm không khả vi</label>
                <label><input type="radio" name="q14" value="b"> B) Có, dựa trên điều kiện giảm đủ cho composite function</label>
                <label><input type="radio" name="q14" value="c"> C) Chỉ khi \(h = 0\)</label>
                <label><input type="radio" name="q14" value="d"> D) Chỉ cho FISTA</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Có, dựa trên điều kiện giảm đủ cho composite function</strong><br>
                Có thể sử dụng backtracking với điều kiện $$f(x^+) \leq Q_t(x^+, x)$$ trong đó $$Q_t$$ là quadratic upper bound.
            </div>
        </div>

        <!-- Câu hỏi 15: Proximal operator of indicator function -->
        <div class="question" id="q15" style="display: none;">
            <h3>Câu 15: Proximal operator của hàm chỉ thị \(I_C(x)\) của tập lồi \(C\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) \(\text{prox}_{I_C}(v) = v\)</label>
                <label><input type="radio" name="q15" value="b"> B) \(\text{prox}_{I_C}(v) = P_C(v)\) (projection onto \(C\))</label>
                <label><input type="radio" name="q15" value="c"> C) \(\text{prox}_{I_C}(v) = 0\)</label>
                <label><input type="radio" name="q15" value="d"> D) Không tồn tại</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$\text{prox}_{I_C}(v) = P_C(v)$$ (projection onto $$C$$)</strong><br>
                Proximal operator của hàm chỉ thị chính là phép chiếu lên tập ràng buộc.
            </div>
        </div>

        <!-- Câu hỏi 16: Composite gradient mapping -->
        <div class="question" id="q16" style="display: none;">
            <h3>Câu 16: Composite gradient mapping \(G_t(x)\) được định nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) \(G_t(x) = \nabla g(x)\)</label>
                <label><input type="radio" name="q16" value="b"> B) \(G_t(x) = \frac{1}{t}(x - \text{prox}_{th}(x - t\nabla g(x)))\)</label>
                <label><input type="radio" name="q16" value="c"> C) \(G_t(x) = \text{prox}_{th}(x)\)</label>
                <label><input type="radio" name="q16" value="d"> D) \(G_t(x) = x - t\nabla g(x)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$G_t(x) = \frac{1}{t}(x - \text{prox}_{th}(x - t\nabla g(x)))$$</strong><br>
                Composite gradient mapping tổng quát hóa gradient cho composite functions và được dùng trong điều kiện dừng.
            </div>
        </div>

        <!-- Câu hỏi 17: Acceleration always beneficial -->
        <div class="question" id="q17" style="display: none;">
            <h3>Câu 17: Acceleration (như FISTA) có luôn có lợi không?</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Luôn có lợi</label>
                <label><input type="radio" name="q17" value="b"> B) Không, có thể làm chậm hội tụ trong một số trường hợp</label>
                <label><input type="radio" name="q17" value="c"> C) Chỉ có lợi cho hàm quadratic</label>
                <label><input type="radio" name="q17" value="d"> D) Chỉ có lợi cho L1 regularization</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Không, có thể làm chậm hội tụ trong một số trường hợp</strong><br>
                Acceleration có thể gây dao động và chậm hội tụ, đặc biệt khi hàm có conditioning kém hoặc trong giai đoạn đầu.
            </div>
        </div>

        <!-- Câu hỏi 18: Proximal gradient vs subgradient -->
        <div class="question" id="q18" style="display: none;">
            <h3>Câu 18: So với subgradient method, proximal gradient method:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) Chậm hơn</label>
                <label><input type="radio" name="q18" value="b"> B) Nhanh hơn và ổn định hơn</label>
                <label><input type="radio" name="q18" value="c"> C) Chỉ áp dụng cho hàm khả vi</label>
                <label><input type="radio" name="q18" value="d"> D) Có cùng tốc độ hội tụ</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Nhanh hơn và ổn định hơn</strong><br>
                Proximal gradient có tốc độ $$O(1/k)$$ so với $$O(1/\sqrt{k})$$ của subgradient, và ít dao động hơn.
            </div>
        </div>

        <!-- Câu hỏi 19: Strongly convex case -->
        <div class="question" id="q19" style="display: none;">
            <h3>Câu 19: Khi \(g\) là strongly convex, proximal gradient method có tốc độ hội tụ:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) \(O(1/k)\)</label>
                <label><input type="radio" name="q19" value="b"> B) \(O(\rho^k)\) với \(\rho < 1\) (linear)</label>
                <label><input type="radio" name="q19" value="c"> C) \(O(1/k^2)\)</label>
                <label><input type="radio" name="q19" value="d"> D) \(O(1/\sqrt{k})\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$O(\rho^k)$$ với $$\rho < 1$$ (linear)</strong><br>
                Strong convexity của $$g$$ đảm bảo tốc độ hội tụ linear (geometric) cho proximal gradient method.
            </div>
        </div>

        <!-- Câu hỏi 20: Practical considerations -->
        <div class="question" id="q20" style="display: none;">
            <h3>Câu 20: Trong thực tế, để áp dụng proximal gradient method hiệu quả, cần:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Proximal operator của \(h\) phải có closed-form solution</label>
                <label><input type="radio" name="q20" value="b"> B) \(g\) phải có Lipschitz gradient</label>
                <label><input type="radio" name="q20" value="c"> C) Biết step size thích hợp</label>
                <label><input type="radio" name="q20" value="d"> D) Tất cả các điều kiện trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các điều kiện trên</strong><br>
                Để hiệu quả, cần proximal operator dễ tính, Lipschitz gradient cho $$g$$, và step size phù hợp.
            </div>
        </div>
        <!-- Câu hỏi 21: Thực hành -->
        <div class="question" id="q21" style="display: none;">
            <h3>Câu 21: Proximal operator của hàm $$f(x) = \lambda|x|$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) $$\text{prox}_f(x) = \text{sign}(x)\max\{|x|-\lambda, 0\}$$</label>
                <label><input type="radio" name="q21" value="b"> B) $$\text{prox}_f(x) = x - \lambda$$</label>
                <label><input type="radio" name="q21" value="c"> C) $$\text{prox}_f(x) = \lambda x$$</label>
                <label><input type="radio" name="q21" value="d"> D) $$\text{prox}_f(x) = |x|$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\text{prox}_f(x) = \text{sign}(x)\max\{|x|-\lambda, 0\}$$</strong><br>
                Đây là soft thresholding operator, một trong những proximal operator quan trọng nhất.
            </div>
        </div>

        <!-- Câu hỏi 22: Thực hành -->
        <div class="question" id="q22" style="display: none;">
            <h3>Câu 22: Proximal gradient method kết hợp:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) Gradient descent + proximal operator</label>
                <label><input type="radio" name="q22" value="b"> B) Newton method + gradient</label>
                <label><input type="radio" name="q22" value="c"> C) SGD + momentum</label>
                <label><input type="radio" name="q22" value="d"> D) Line search + Hessian</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Gradient descent + proximal operator</strong><br>
                Proximal gradient method: $$x^{(k+1)} = \text{prox}_{th}(x^{(k)} - t\nabla g(x^{(k)}))$$.
            </div>
        </div>

        <!-- Câu hỏi 23: Thực hành -->
        <div class="question" id="q23" style="display: none;">
            <h3>Câu 23: FISTA là thuật toán:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) Tăng tốc proximal gradient</label>
                <label><input type="radio" name="q23" value="b"> B) Newton method cải tiến</label>
                <label><input type="radio" name="q23" value="c"> C) Stochastic gradient descent</label>
                <label><input type="radio" name="q23" value="d"> D) Interior point method</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Tăng tốc proximal gradient</strong><br>
                FISTA (Fast Iterative Shrinkage-Thresholding Algorithm) là phiên bản tăng tốc của proximal gradient.
            </div>
        </div>

        <!-- Câu hỏi 24: Thực hành -->
        <div class="question" id="q24" style="display: none;">
            <h3>Câu 24: Bài toán LASSO có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) $$\min \frac{1}{2}\|Ax-b\|^2 + \lambda\|x\|_1$$</label>
                <label><input type="radio" name="q24" value="b"> B) $$\min \frac{1}{2}\|Ax-b\|^2 + \lambda\|x\|_2$$</label>
                <label><input type="radio" name="q24" value="c"> C) $$\min \|Ax-b\|_1 + \lambda\|x\|_2$$</label>
                <label><input type="radio" name="q24" value="d"> D) $$\min \|Ax-b\|_\infty + \lambda\|x\|_1$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\min \frac{1}{2}\|Ax-b\|^2 + \lambda\|x\|_1$$</strong><br>
                LASSO sử dụng regularization L1: $$\min \frac{1}{2}\|Ax-b\|^2 + \lambda\|x\|_1$$.
            </div>
        </div>

        <!-- Câu hỏi 25: Thực hành -->
        <div class="question" id="q25" style="display: none;">
            <h3>Câu 25: Với $$\text{prox}_{\lambda|\cdot|}(2)$$ và $$\lambda = 0.5$$, kết quả là:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) $$1.5$$</label>
                <label><input type="radio" name="q25" value="b"> B) $$2$$</label>
                <label><input type="radio" name="q25" value="c"> C) $$1$$</label>
                <label><input type="radio" name="q25" value="d"> D) $$0.5$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$1.5$$</strong><br>
                $$\text{prox}_{0.5|\cdot|}(2) = \text{sign}(2)\max\{|2|-0.5, 0\} = 1 \cdot 1.5 = 1.5$$.
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
    q1: 'b', q2: 'a', q3: 'b', q4: 'b', q5: 'a',
    q6: 'b', q7: 'b', q8: 'b', q9: 'a', q10: 'a',
    q11: 'a', q12: 'b', q13: 'b', q14: 'b', q15: 'b',
    q16: 'b', q17: 'b', q18: 'b', q19: 'b', q20: 'd'
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
        message = '🌟 Xuất sắc! Bạn đã thành thạo proximal gradient method!';
    } else if (percentage >= 80) {
        message = '👍 Rất tốt! Bạn hiểu tốt về proximal operators và FISTA.';
    } else if (percentage >= 70) {
        message = '📚 Khá ổn! Hãy xem lại proximal operators và acceleration.';
    } else if (percentage >= 60) {
        message = '💪 Cần cải thiện! Ôn lại composite optimization và proximal operators.';
    } else {
        message = '📖 Hãy học lại từ đầu về proximal gradient method nhé!';
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
