---
layout: post
title: 01-06 Bài tập trắc nghiệm - Bài toán tối ưu hóa
chapter: '01'
order: 7
owner: GitHub Copilot
lang: vi
categories:
- chapter01
lesson_type: quiz
redirect_from:
  - /contents/vi/chapter01/01_05_Quiz_Optimization_Problems/
---

Sai lầm phổ biến nhất của người mới học tối ưu hóa lồi không phải là tính đạo hàm sai, mà là **nhận diện nhầm bài toán lồi với bài toán không lồi** ngay từ dòng đề bài đầu tiên. Chỉ cần một dấu bất đẳng thức bị đảo ngược ($$\ge$$ thay vì $$\le$$ trên một hàm lồi), hay một ràng buộc đẳng thức bậc hai như $$x_1^2 + x_2^2 = 1$$, toàn bộ tính lồi của miền khả thi lập tức biến mất.

Bộ trắc nghiệm này kiểm tra phản xạ phân loại bài toán tối ưu của bạn. Trước khi bắt đầu, hãy ôn nhanh 3 tiêu chí vàng và tự tay kiểm tra 3 ví dụ "bẫy" kinh điển ngay sau đây.

## Bản đồ kiến thức nền: Ba chốt kiểm tra nhanh bài toán tối ưu hóa lồi

- **Chốt 1 — Hàm mục tiêu $$f_0(x)$$:** Nếu bài toán là $$\min f_0$$ thì $$f_0$$ phải lồi; nếu là $$\max f_0$$ thì $$f_0$$ phải lõm (tức $$-f_0$$ lồi).
- **Chốt 2 — Ràng buộc bất đẳng thức $$g_i(x) \le 0$$:** Mỗi $$g_i$$ phải là hàm lồi (nếu đề viết $$u(x) \ge 0$$ thì $$u$$ phải là hàm lõm để $$-u(x) \le 0$$ lồi).
- **Chốt 3 — Ràng buộc đẳng thức $$h_j(x) = 0$$:** Bắt buộc phải là hàm affine $$a_j^T x + b_j = 0$$; mọi đẳng thức phi tuyến (trừ trường hợp đặc biệt rút gọn được) đều phá vỡ tính lồi của miền khả thi.

### Khung giải thích (nên đọc chậm): Phân loại 3 bài toán thoạt nhìn rất giống nhau

Hãy kiểm tra tính lồi của ba bài toán trên $$\mathbb{R}^2$$:

1. **Bài toán A:** $$\min 2x_1 - x_2$$ thỏa mãn $$x_1 + 2x_2 \le 4$$.
   - Hàm mục tiêu tuyến tính (lồi), ràng buộc $$x_1 + 2x_2 - 4 \le 0$$ là hàm affine (lồi).
   - Kết luận: **Quy hoạch tuyến tính (LP)** $$\subset$$ bài toán tối ưu hóa lồi.
2. **Bài toán B:** $$\min x_1^2 + x_2^2$$ thỏa mãn $$x_1^2 + x_2^2 \ge 1$$.
   - Hàm mục tiêu lồi, nhưng ràng buộc là $$g(x) = 1 - (x_1^2 + x_2^2) \le 0$$ — hàm $$g$$ là hàm **lõm**, không phải hàm lồi!
   - Phản ví dụ trực tiếp: $$x = (1, 0)$$ và $$y = (-1, 0)$$ đều khả thi ($$1 \ge 1$$), nhưng trung điểm $$\frac{1}{2}(x + y) = (0, 0)$$ có $$0^2 + 0^2 = 0 < 1$$ (nằm ngoài miền khả thi!).
   - Kết luận: **Không lồi**.
3. **Bài toán C:** $$\min x_1^2 + x_2^2$$ thỏa mãn $$x_1^2 + x_2^2 \le 1$$.
   - Đảo dấu bất đẳng thức thành $$x_1^2 + x_2^2 - 1 \le 0$$ biến miền khả thi thành hình tròn đặc (tập lồi).
   - Kết luận: **Bài toán tối ưu hóa lồi** (cụ thể là QCQP lồi), đạt cực tiểu duy nhất tại $$x^* = (0, 0)$$.

---

Bài tập trắc nghiệm này giúp bạn kiểm tra mức độ nắm vững các khái niệm cơ bản về bài toán tối ưu hóa và tối ưu hóa lồi.

---

## 📚 Ôn tập lý thuyết

Trước khi làm bài tập, hãy điểm lại các khái niệm chính trong chương này:

### 🎯 **Bài toán tối ưu hóa tổng quát**

**Dạng chuẩn:**
$$egin{align*} 
&\min_{x\in D}\ &&f(x) \
&	ext{với điều kiện} && g_i(x) \le 0,\ i = 1, ..., m \
&&& h_j(x) = 0,\ j = 1,\ ..., r
\end{align*}$$

**Các thành phần:**
- $$x \in \mathbb{R}^n$$: biến tối ưu hóa (biến quyết định).
- $$f(x)$$: hàm mục tiêu (objective function) hoặc hàm chi phí.
- $$g_i(x) \le 0$$: ràng buộc bất đẳng thức (inequality constraints).
- $$h_j(x) = 0$$: ràng buộc đẳng thức (equality constraints).
- $$x^*$$: nghiệm tối ưu (optimal solution).

**Miền xác định chung:**
$$D = 	ext{dom}(f) \cap igcap_{i=1}^m 	ext{dom}(g_i) \cap igcap_{j=1}^r 	ext{dom}(h_j)$$

### 🔵 **Tập lồi (Convex Sets)**

<div class="textbook-definition" markdown="1">
**Định nghĩa:**
Tập $$C$$ là tập lồi nếu với mọi $$x_1, x_2 \in C$$ và $$0 \le 	heta \le 1$$:
$$	heta x_1 + (1-	heta)x_2 \in C$$
</div>

**Đoạn thẳng:** $$x = 	heta x_1 + (1 - 	heta) x_2$$ với $$0 \le 	heta \le 1$$

**Tổ hợp lồi:** 
$$x = \sum_{i=1}^k 	heta_i x_i$$ với $$\sum_{i=1}^k 	heta_i = 1, 	heta_i \ge 0$$

### 📈 **Hàm lồi (Convex Functions)**

<div class="textbook-definition" markdown="1">
**Định nghĩa:**
Hàm $$f: \mathbb{R}^n 
ightarrow \mathbb{R}$$ là hàm lồi nếu:
1. $$	ext{dom}(f)$$ là tập lồi.
2. $$f(	heta x + (1 - 	heta)y) \le 	heta f(x) + (1-	heta)f(y)$$
   với mọi $$x, y \in 	ext{dom}(f), 0 \le 	heta \le 1$$.
</div>

**Biểu đồ trên (Epigraph):**
$$	ext{epi } f = \{(x, t) \in \mathbb{R}^{n+1} \mid x \in 	ext{dom } f, f(x) \le t\}$$

**Tính chất quan trọng:** $$f$$ lồi ⟺ $$	ext{epi } f$$ là tập lồi.

### 🏆 **Bài toán tối ưu hóa lồi**

<div class="textbook-definition" markdown="1">
**Định nghĩa:**
Bài toán tối ưu hóa là bài toán lồi khi:
- Hàm mục tiêu $$f$$ là hàm lồi.
- Các hàm ràng buộc bất đẳng thức $$g_i$$ là hàm lồi.
- Các hàm ràng buộc đẳng thức $$h_j$$ là hàm affine: $$h_j(x) = a_j^T x + b_j$$.
</div>

**Tính chất cốt lõi:** 
> Mọi cực tiểu địa phương của bài toán tối ưu hóa lồi đều là cực tiểu toàn cục.

**Hàm affine:** $$f(x) = Ax + b$$ (hàm tuyến tính cộng với một hằng số).

### 🔄 **Hàm lõm và hàm lồi**

**Hàm lõm:** $$f$$ lõm ⟺ $$-f$$ lồi
$$f(	heta x + (1 - 	heta)y) \ge 	heta f(x) + (1-	heta)f(y)$$

**Chuyển đổi:** Cực đại hóa hàm lõm $$f$$ tương đương cực tiểu hóa hàm lồi $$-f$$.

### 🎯 **Mục tiêu khóa học**

1. **Nhận biết:** xác định khi nào một bài toán là tối ưu hóa lồi.
2. **Mô hình hóa:** chuyển bài toán thực tế thành bài toán tối ưu hóa lồi.
3. **Lựa chọn:** chọn thuật toán phù hợp nhất cho từng lớp bài toán.

### 🛠️ **Các thuật toán chính**

- **Gradient Descent:** phương pháp bậc nhất.
- **Phương pháp Newton:** phương pháp bậc hai.
- **Proximal Gradient:** dành cho hàm mục tiêu có phần không khả vi.
- **ADMM:** phù hợp với bài toán có cấu trúc tách được.
- **Coordinate Descent:** tối ưu hóa luân phiên theo từng tọa độ/khối biến.

---

💡 **Gợi ý:** Tối ưu hóa lồi có một tính chất rất thuận lợi: không có cực tiểu địa phương tách biệt với cực tiểu toàn cục — mọi cực tiểu địa phương đều là cực tiểu toàn cục.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>Bài tập trắc nghiệm: Bài toán tối ưu hóa</h2>
        <p>Chọn đáp án đúng nhất cho mỗi câu hỏi. Bạn sẽ nhận được kết quả ngay sau khi hoàn thành.</p>
        <div id="progress-bar">
            <div id="progress-fill"></div>
        </div>
        <p id="progress-text">Câu hỏi 1/25</p>
    </div>

    <div id="quiz-questions">
        <!-- Câu hỏi 1: Định nghĩa bài toán tối ưu hóa -->
        <div class="question" id="q1">
            <h3>Câu 1: Trong dạng chuẩn của bài toán tối ưu hóa, $$f(x)$$ được gọi là:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) Hàm ràng buộc</label>
                <label><input type="radio" name="q1" value="b"> B) Hàm mục tiêu</label>
                <label><input type="radio" name="q1" value="c"> C) Biến tối ưu hóa</label>
                <label><input type="radio" name="q1" value="d"> D) Miền khả thi</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Hàm mục tiêu</strong><br>
                Trong bài toán tối ưu hóa $$\min_{x\in D} f(x)$$, hàm $$f(x)$$ là hàm mục tiêu (objective function) hoặc hàm chi phí (cost function) mà chúng ta muốn tối thiểu hóa.
            </div>
        </div>

        <!-- Câu hỏi 2: Ràng buộc tường minh vs ngầm -->
        <div class="question" id="q2" style="display: none;">
            <h3>Câu 2: Cho bài toán $$\min \log(x)$$. Ràng buộc $$x > 0$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) Ràng buộc tường minh</label>
                <label><input type="radio" name="q2" value="b"> B) Ràng buộc ngầm</label>
                <label><input type="radio" name="q2" value="c"> C) Ràng buộc đẳng thức</label>
                <label><input type="radio" name="q2" value="d"> D) Không phải ràng buộc</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Ràng buộc ngầm</strong><br>
                Ràng buộc $$x > 0$$ phát sinh từ miền xác định của hàm $$\log(x)$$, không được chỉ định trực tiếp trong bài toán, nên được gọi là ràng buộc ngầm.
            </div>
        </div>

        <!-- Câu hỏi 3: Định nghĩa tập lồi -->
        <div class="question" id="q3" style="display: none;">
            <h3>Câu 3: Một tập $$C$$ được gọi là lồi nếu:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) Với mọi $$x_1, x_2 \in C$$ và $$0 \leq \theta \leq 1$$, ta có $$\theta x_1 + (1-\theta)x_2 \in C$$</label>
                <label><input type="radio" name="q3" value="b"> B) Tập $$C$$ là hình tròn</label>
                <label><input type="radio" name="q3" value="c"> C) Tập $$C$$ không có lỗ hổng</label>
                <label><input type="radio" name="q3" value="d"> D) Tập $$C$$ là tập đóng</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Với mọi $$x_1, x_2 \in C$$ và $$0 \leq \theta \leq 1$$, ta có $$\theta x_1 + (1-\theta)x_2 \in C$$</strong><br>
                Định nghĩa tập lồi: đoạn thẳng nối bất kỳ hai điểm nào trong tập đều nằm hoàn toàn trong tập đó.
            </div>
        </div>

        <!-- Câu hỏi 4: Hàm lồi -->
        <div class="question" id="q4" style="display: none;">
            <h3>Câu 4: Hàm $$f$$ là lồi nếu:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) $$f(\theta x + (1-\theta)y) \geq \theta f(x) + (1-\theta)f(y)$$</label>
                <label><input type="radio" name="q4" value="b"> B) $$f(\theta x + (1-\theta)y) \leq \theta f(x) + (1-\theta)f(y)$$</label>
                <label><input type="radio" name="q4" value="c"> C) $$f(\theta x + (1-\theta)y) = \theta f(x) + (1-\theta)f(y)$$</label>
                <label><input type="radio" name="q4" value="d"> D) $$f$$ là hàm tuyến tính</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$f(\theta x + (1-\theta)y) \leq \theta f(x) + (1-\theta)f(y)$$</strong><br>
                Định nghĩa hàm lồi: đoạn thẳng nối hai điểm bất kỳ trên đồ thị nằm phía trên đồ thị của hàm số.
            </div>
        </div>

        <!-- Câu hỏi 5: Hàm lõm -->
        <div class="question" id="q5" style="display: none;">
            <h3>Câu 5: Nếu $$f$$ là hàm lõm, thì $$-f$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) Hàm lõm</label>
                <label><input type="radio" name="q5" value="b"> B) Hàm lồi</label>
                <label><input type="radio" name="q5" value="c"> C) Hàm tuyến tính</label>
                <label><input type="radio" name="q5" value="d"> D) Không xác định được</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Hàm lồi</strong><br>
                Theo định nghĩa, hàm $$f$$ là lõm khi và chỉ khi $$-f$$ là lồi. Đây là cách chuyển đổi bài toán tối đa hóa hàm lõm thành tối thiểu hóa hàm lồi.
            </div>
        </div>

        <!-- Câu hỏi 6: Epigraph -->
        <div class="question" id="q6" style="display: none;">
            <h3>Câu 6: Epigraph của hàm $$f$$ được định nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) $$\{(x,t) : x \in \text{dom } f, f(x) \geq t\}$$</label>
                <label><input type="radio" name="q6" value="b"> B) $$\{(x,t) : x \in \text{dom } f, f(x) \leq t\}$$</label>
                <label><input type="radio" name="q6" value="c"> C) $$\{(x,t) : x \in \text{dom } f, f(x) = t\}$$</label>
                <label><input type="radio" name="q6" value="d"> D) $$\{x : x \in \text{dom } f\}$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$\{(x,t) : x \in \text{dom } f, f(x) \leq t\}$$</strong><br>
                Epigraph là tập hợp các điểm nằm phía trên đồ thị của hàm số. "Epi" có nghĩa là "phía trên".
            </div>
        </div>

        <!-- Câu hỏi 7: Mối quan hệ hàm lồi và tập lồi -->
        <div class="question" id="q7" style="display: none;">
            <h3>Câu 7: Hàm $$f$$ là lồi khi và chỉ khi:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) Miền xác định của $$f$$ là tập lồi</label>
                <label><input type="radio" name="q7" value="b"> B) Epigraph của $$f$$ là tập lồi</label>
                <label><input type="radio" name="q7" value="c"> C) Đồ thị của $$f$$ là tập lồi</label>
                <label><input type="radio" name="q7" value="d"> D) Hypograph của $$f$$ là tập lồi</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Epigraph của $$f$$ là tập lồi</strong><br>
                Đây là mối quan hệ quan trọng kết nối định nghĩa hàm lồi và tập lồi: hàm lồi ⟺ epigraph là tập lồi.
            </div>
        </div>

        <!-- Câu hỏi 8: Tính chất tối ưu địa phương -->
        <div class="question" id="q8" style="display: none;">
            <h3>Câu 8: Đối với hàm lồi, điểm tối ưu địa phương:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) Luôn là điểm tối ưu toàn cục</label>
                <label><input type="radio" name="q8" value="b"> B) Có thể không phải là điểm tối ưu toàn cục</label>
                <label><input type="radio" name="q8" value="c"> C) Không tồn tại</label>
                <label><input type="radio" name="q8" value="d"> D) Chỉ tồn tại duy nhất một điểm</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Luôn là điểm tối ưu toàn cục</strong><br>
                Đây là tính chất quan trọng của hàm lồi: mọi điểm tối ưu địa phương đều là tối ưu toàn cục, làm cho việc tìm nghiệm dễ dàng hơn.
            </div>
        </div>

        <!-- Câu hỏi 9: Tổ hợp lồi -->
        <div class="question" id="q9" style="display: none;">
            <h3>Câu 9: Tổ hợp lồi của các điểm $$x_1, x_2, ..., x_k$$ có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) $$\sum_{i=1}^k \theta_i x_i$$ với $$\theta_i \geq 0$$</label>
                <label><input type="radio" name="q9" value="b"> B) $$\sum_{i=1}^k \theta_i x_i$$ với $$\sum_{i=1}^k \theta_i = 1$$</label>
                <label><input type="radio" name="q9" value="c"> C) $$\sum_{i=1}^k \theta_i x_i$$ với $$\theta_i \geq 0$$ và $$\sum_{i=1}^k \theta_i = 1$$</label>
                <label><input type="radio" name="q9" value="d"> D) $$\sum_{i=1}^k x_i$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) $$\sum_{i=1}^k \theta_i x_i$$ với $$\theta_i \geq 0$$ và $$\sum_{i=1}^k \theta_i = 1$$</strong><br>
                Tổ hợp lồi yêu cầu các hệ số không âm và tổng bằng 1, tạo ra "trung bình có trọng số" của các điểm.
            </div>
        </div>

        <!-- Câu hỏi 10: Bài toán tối ưu hóa lồi -->
        <div class="question" id="q10" style="display: none;">
            <h3>Câu 10: Trong bài toán tối ưu hóa lồi, các hàm ràng buộc đẳng thức $$h_j(x) = 0$$ phải là:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) Hàm lồi</label>
                <label><input type="radio" name="q10" value="b"> B) Hàm lõm</label>
                <label><input type="radio" name="q10" value="c"> C) Hàm affine</label>
                <label><input type="radio" name="q10" value="d"> D) Hàm bất kỳ</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) Hàm affine</strong><br>
                Trong bài toán tối ưu hóa lồi, các ràng buộc đẳng thức phải là hàm affine: $$h_j(x) = a_j^T x + b_j$$.
            </div>
        </div>

        <!-- Câu hỏi 11: Hàm affine -->
        <div class="question" id="q11" style="display: none;">
            <h3>Câu 11: Hàm affine có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) $$e^{a^T x} + b$$</label>
                <label><input type="radio" name="q11" value="b"> B) $$ax^2 + bx + c$$</label>
                <label><input type="radio" name="q11" value="c"> C) $$a^T x + b$$</label>
                <label><input type="radio" name="q11" value="d"> D) $$\|x\|^2$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) $$a^T x + b$$</strong><br>
                Hàm affine là hàm tuyến tính cộng với một hằng số, có dạng tổng quát $$a^T x + b$$ trong không gian nhiều chiều.
            </div>
        </div>

        <!-- Câu hỏi 12: Ví dụ tập lồi -->
        <div class="question" id="q12" style="display: none;">
            <h3>Câu 12: Tập nào sau đây là tập lồi?</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) Hình tròn</label>
                <label><input type="radio" name="q12" value="b"> B) Hình vuông</label>
                <label><input type="radio" name="q12" value="c"> C) Nửa không gian</label>
                <label><input type="radio" name="q12" value="d"> D) Tất cả các đáp án trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các đáp án trên</strong><br>
                Hình tròn, hình vuông và nửa không gian đều là các ví dụ của tập lồi vì đoạn thẳng nối hai điểm bất kỳ trong tập đều nằm hoàn toàn trong tập.
            </div>
        </div>

        <!-- Câu hỏi 13: Ví dụ hàm lồi -->
        <div class="question" id="q13" style="display: none;">
            <h3>Câu 13: Hàm nào sau đây là hàm lồi?</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) $$f(x) = x^2$$</label>
                <label><input type="radio" name="q13" value="b"> B) $$f(x) = |x|$$</label>
                <label><input type="radio" name="q13" value="c"> C) $$f(x) = e^x$$</label>
                <label><input type="radio" name="q13" value="d"> D) Tất cả các đáp án trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các đáp án trên</strong><br>
                $$x^2$$ (parabol), $$|x|$$ (hàm trị tuyệt đối), và $$e^x$$ (hàm mũ) đều là các ví dụ cơ bản của hàm lồi.
            </div>
        </div>

        <!-- Câu hỏi 14: Ứng dụng trong machine learning -->
        <div class="question" id="q14" style="display: none;">
            <h3>Câu 14: Trong machine learning, bài toán nào sau đây thường được giải bằng tối ưu hóa lồi?</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) Huấn luyện mạng nơ-ron</label>
                <label><input type="radio" name="q14" value="b"> B) Hồi quy tuyến tính</label>
                <label><input type="radio" name="q14" value="c"> C) Lựa chọn đặc trưng bằng Lasso (phạt chuẩn $$\ell_1$$)</label>
                <label><input type="radio" name="q14" value="d"> D) Cả B và C</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Cả B và C</strong><br>
                Hồi quy tuyến tính và lựa chọn đặc trưng bằng Lasso (nới lỏng lồi của bài toán chọn tập con) dẫn đến bài toán tối ưu hóa lồi. Huấn luyện mạng nơ-ron thường là bài toán không lồi.
            </div>
        </div>

        <!-- Câu hỏi 15: Miền khả thi -->
        <div class="question" id="q15" style="display: none;">
            <h3>Câu 15: Miền khả thi của bài toán tối ưu hóa là:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) Tập hợp tất cả các biến</label>
                <label><input type="radio" name="q15" value="b"> B) Tập hợp các điểm thỏa mãn tất cả ràng buộc</label>
                <label><input type="radio" name="q15" value="c"> C) Miền xác định của hàm mục tiêu</label>
                <label><input type="radio" name="q15" value="d"> D) Tập hợp các nghiệm tối ưu</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Tập hợp các điểm thỏa mãn tất cả ràng buộc</strong><br>
                Miền khả thi (feasible region) là tập hợp tất cả các điểm $$x$$ thỏa mãn các ràng buộc $$g_i(x) \leq 0$$ và $$h_j(x) = 0$$.
            </div>
        </div>

        <!-- Câu hỏi 16: Thuật toán Simplex -->
        <div class="question" id="q16" style="display: none;">
            <h3>Câu 16: Thuật toán Simplex được phát triển bởi ai và vào năm nào?</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) George Dantzig, 1947</label>
                <label><input type="radio" name="q16" value="b"> B) John von Neumann, 1944</label>
                <label><input type="radio" name="q16" value="c"> C) Leonid Kantorovich, 1939</label>
                <label><input type="radio" name="q16" value="d"> D) Narendra Karmarkar, 1984</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) George Dantzig, 1947</strong><br>
                George Dantzig phát triển thuật toán Simplex vào năm 1947, tạo ra cuộc cách mạng trong lĩnh vực tối ưu hóa thực tế.
            </div>
        </div>

        <!-- Câu hỏi 17: Total variation denoising -->
        <div class="question" id="q17" style="display: none;">
            <h3>Câu 17: Trong bài toán khử nhiễu total variation, số hạng $$\sum_{(i,j) \in E} |\theta_i - \theta_j|$$ có tác dụng:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Tăng nhiễu</label>
                <label><input type="radio" name="q17" value="b"> B) Làm mịn ảnh</label>
                <label><input type="radio" name="q17" value="c"> C) Tăng độ tương phản</label>
                <label><input type="radio" name="q17" value="d"> D) Giảm kích thước ảnh</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Làm mịn ảnh</strong><br>
                Số hạng total variation penalty khuyến khích sự thay đổi nhỏ giữa các pixel lân cận, tạo hiệu ứng làm mịn ảnh.
            </div>
        </div>

        <!-- Câu hỏi 18: Ràng buộc bất đẳng thức -->
        <div class="question" id="q18" style="display: none;">
            <h3>Câu 18: Trong bài toán tối ưu hóa lồi, các hàm ràng buộc bất đẳng thức $$g_i(x) \leq 0$$ phải là:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) Hàm lồi</label>
                <label><input type="radio" name="q18" value="b"> B) Hàm lõm</label>
                <label><input type="radio" name="q18" value="c"> C) Hàm tuyến tính</label>
                <label><input type="radio" name="q18" value="d"> D) Hàm bất kỳ</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Hàm lồi</strong><br>
                Trong bài toán tối ưu hóa lồi, các hàm ràng buộc bất đẳng thức $$g_i(x) \leq 0$$ phải là hàm lồi để đảm bảo miền khả thi là tập lồi.
            </div>
        </div>

        <!-- Câu hỏi 19: Ưu điểm của tối ưu hóa lồi -->
        <div class="question" id="q19" style="display: none;">
            <h3>Câu 19: Ưu điểm chính của bài toán tối ưu hóa lồi so với bài toán không lồi là:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) Có nhiều nghiệm hơn</label>
                <label><input type="radio" name="q19" value="b"> B) Không có cực tiểu địa phương (ngoài cực tiểu toàn cục)</label>
                <label><input type="radio" name="q19" value="c"> C) Tính toán nhanh hơn</label>
                <label><input type="radio" name="q19" value="d"> D) Ứng dụng rộng hơn</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Không có cực tiểu địa phương (ngoài cực tiểu toàn cục)</strong><br>
                Ưu điểm chính của tối ưu hóa lồi là mọi cực tiểu địa phương đều là cực tiểu toàn cục, tránh được vấn đề "mắc kẹt" tại cực tiểu địa phương.
            </div>
        </div>

        <!-- Câu hỏi 20: Ứng dụng thực tế -->
        <div class="question" id="q20" style="display: none;">
            <h3>Câu 20: Lĩnh vực nào sau đây KHÔNG phải là ứng dụng chính của tối ưu hóa lồi?</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Xử lý tín hiệu</label>
                <label><input type="radio" name="q20" value="b"> B) Thiết kế mạch</label>
                <label><input type="radio" name="q20" value="c"> C) Trò chơi điện tử</label>
                <label><input type="radio" name="q20" value="d"> D) Tài chính</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) Trò chơi điện tử</strong><br>
                Mặc dù tối ưu hóa có thể được sử dụng trong trò chơi điện tử, nhưng xử lý tín hiệu, thiết kế mạch và tài chính là những ứng dụng chính và truyền thống hơn của tối ưu hóa lồi.
            </div>
        </div>

        <!-- Câu hỏi 21: Bài toán tối ưu hóa thực tế -->
        <div class="question" id="q21" style="display: none;">
            <h3>Câu 21: Cho bài toán tối thiểu hóa $$f(x) = x^2 + 4x + 3$$. Giá trị tối ưu là:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) $$-1$$</label>
                <label><input type="radio" name="q21" value="b"> B) $$0$$</label>
                <label><input type="radio" name="q21" value="c"> C) $$3$$</label>
                <label><input type="radio" name="q21" value="d"> D) $$-2$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$-1$$</strong><br>
                $$f'(x) = 2x + 4 = 0 \Rightarrow x = -2$$<br>
                $$f(-2) = (-2)^2 + 4(-2) + 3 = 4 - 8 + 3 = -1$$
            </div>
        </div>

        <!-- Câu hỏi 22: Kiểm tra tính lồi -->
        <div class="question" id="q22" style="display: none;">
            <h3>Câu 22: Hàm $$f(x) = |x|$$ có phải là hàm lồi không?</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) Có, vì $$f''(x) \geq 0$$ mọi nơi</label>
                <label><input type="radio" name="q22" value="b"> B) Có, theo định nghĩa hàm lồi</label>
                <label><input type="radio" name="q22" value="c"> C) Không, vì không khả vi tại $$x = 0$$</label>
                <label><input type="radio" name="q22" value="d"> D) Không, vì đồ thị có góc nhọn</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Có, theo định nghĩa hàm lồi</strong><br>
                Hàm $$|x|$$ thỏa mãn $$|tx + (1-t)y| \leq t|x| + (1-t)|y|$$ với mọi $$t \in [0,1]$$. Tính không khả vi tại một điểm không ảnh hưởng đến tính lồi.
            </div>
        </div>

        <!-- Câu hỏi 23: Ràng buộc trong thực tế -->
        <div class="question" id="q23" style="display: none;">
            <h3>Câu 23: Trong bài toán phân bổ ngân sách với $$x_1 + x_2 + x_3 = 100$$ và $$x_i \geq 0$$, có bao nhiêu ràng buộc?</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) 1 ràng buộc đẳng thức, 3 ràng buộc bất đẳng thức</label>
                <label><input type="radio" name="q23" value="b"> B) 4 ràng buộc đẳng thức</label>
                <label><input type="radio" name="q23" value="c"> C) 3 ràng buộc bất đẳng thức</label>
                <label><input type="radio" name="q23" value="d"> D) 1 ràng buộc đẳng thức</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) 1 ràng buộc đẳng thức, 3 ràng buộc bất đẳng thức</strong><br>
                Có 1 ràng buộc đẳng thức $$x_1 + x_2 + x_3 = 100$$ và 3 ràng buộc bất đẳng thức $$x_1 \geq 0, x_2 \geq 0, x_3 \geq 0$$.
            </div>
        </div>

        <!-- Câu hỏi 24: Miền khả thi -->
        <div class="question" id="q24" style="display: none;">
            <h3>Câu 24: Miền khả thi của bài toán $$\min x^2 + y^2$$ với $$x + y = 1, x \geq 0, y \geq 0$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) Đoạn thẳng từ $$(0,1)$$ đến $$(1,0)$$</label>
                <label><input type="radio" name="q24" value="b"> B) Tam giác với đỉnh $$(0,0), (0,1), (1,0)$$</label>
                <label><input type="radio" name="q24" value="c"> C) Đường tròn đơn vị</label>
                <label><input type="radio" name="q24" value="d"> D) Toàn bộ mặt phẳng</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Đoạn thẳng từ $$(0,1)$$ đến $$(1,0)$$</strong><br>
                Ràng buộc $$x + y = 1$$ tạo ra đường thẳng, kết hợp với $$x \geq 0, y \geq 0$$ cho ta đoạn thẳng trong góc phần tư thứ nhất.
            </div>
        </div>

        <!-- Câu hỏi 25: Tối ưu hóa có ràng buộc -->
        <div class="question" id="q25" style="display: none;">
            <h3>Câu 25: Nghiệm của bài toán $$\min x^2 + y^2$$ với ràng buộc $$x + y = 1$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) $$x = 0.5, y = 0.5$$</label>
                <label><input type="radio" name="q25" value="b"> B) $$x = 1, y = 0$$</label>
                <label><input type="radio" name="q25" value="c"> C) $$x = 0, y = 1$$</label>
                <label><input type="radio" name="q25" value="d"> D) $$x = 1, y = 1$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$x = 0.5, y = 0.5$$</strong><br>
                Sử dụng phương pháp Lagrange hoặc thế $$y = 1-x$$ vào hàm mục tiêu:<br>
                $$\min x^2 + (1-x)^2 = 2x^2 - 2x + 1$$<br>
                $$\frac{d}{dx}(2x^2 - 2x + 1) = 4x - 2 = 0 \Rightarrow x = 0.5, y = 0.5$$
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
    background-color: #ffe8e0;
}

.explanation {
    margin-top: 20px;
    padding: 15px;
    background-color: #e8f4fd;
    border-left: 4px solid #2196F3;
    border-radius: 4px;
    font-size: 0.95em;
    line-height: 1.5;
}

.explanation strong {
    color: #1976D2;
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
    background: #e55a2b;
}

#quiz-navigation button:disabled {
    background: #cccccc;
    cursor: not-allowed;
}

#quiz-results {
    text-align: center;
    padding: 30px;
    background: #f0f8f0;
    border-radius: 8px;
    border: 2px solid #FF6B35;
}

#score-display {
    font-size: 1.5em;
    font-weight: bold;
    margin: 20px 0;
    color: #d84315;
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
    q1: 'b', q2: 'b', q3: 'a', q4: 'b', q5: 'b',
    q6: 'b', q7: 'b', q8: 'a', q9: 'c', q10: 'c',
    q11: 'c', q12: 'd', q13: 'd', q14: 'd', q15: 'b',
    q16: 'a', q17: 'b', q18: 'a', q19: 'b', q20: 'c',
    q21: 'a', q22: 'b', q23: 'a', q24: 'a', q25: 'a'
};

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
            ${scorePercentage >= 80 ? '🎉 Xuất sắc! Bạn đã nắm vững các khái niệm cơ bản!' : 
              scorePercentage >= 60 ? '👍 Khá tốt! Hãy ôn lại một số khái niệm.' : 
              scorePercentage >= 40 ? '📚 Cần ôn tập thêm về tối ưu hóa lồi.' : '💪 Hãy đọc lại lý thuyết và thử lại!'}
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
