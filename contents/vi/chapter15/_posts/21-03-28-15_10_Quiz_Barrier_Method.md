---
layout: post
title: 15-10 Bài tập trắc nghiệm - Phương Pháp Rào Cản
chapter: '15'
order: 16
owner: GitHub Copilot
lang: vi
categories:
- chapter15
lesson_type: quiz
redirect_from:
  - /contents/vi/chapter15/15_09_Quiz_Barrier_Method/
---

Phương pháp chắn kết nối rất nhiều chi tiết tinh tế từ cả Chương 13 (đối ngẫu) và Chương 14 (Newton & tự hài hòa): vì sao khoảng cách đối ngẫu lại bằng đúng $$m/t$$ chứ không phụ thuộc $$n$$? Vì sao v.0 bị hỏng còn v.1 lại chạy mượt? Tại sao chọn $$\mu$$ quá lớn hay quá nhỏ đều không tốt? Và tại sao Pha I chỉ cần dừng ngay khi $$s < 0$$?

Bộ câu hỏi trắc nghiệm này giúp bạn kiểm tra sắc bén toàn bộ chuỗi lập luận của Chương 15 — từ hàm chắn logarit, đường trung tâm, KKT nhiễu, khoảng cách dưới tối ưu, đến các phiên bản thuật toán v.0/v.1/v.2 và Pha I. Hãy lướt qua bốn điểm hay gài bẫy nhất trước khi vào bài.

## Kiến thức cần nhớ: Bốn điểm hay nhầm lẫn nhất trong trắc nghiệm Chương 15

- **$$m$$ là số ràng buộc bất đẳng thức, KHÔNG phải số chiều $$n$$ hay số ràng buộc đẳng thức:** Công thức $$f(x^*(t)) - f^* \le m/t$$ chỉ đếm số hàm bất đẳng thức $$h_i(x) \le 0$$ tạo nên hàm chắn $$\phi(x)$$ (ràng buộc đẳng thức $$Ax = b$$ không nằm trong $$\phi$$ nên không đóng góp vào $$m$$!).
- **Hàm mục tiêu chắn $$t f(x) + \phi(x)$$ vs. $$f(x) + \frac{1}{t}\phi(x)$$:** Hai dạng có cùng nghiệm $$x^*(t)$$, nhưng dạng $$t f(x) + \phi(x)$$ giữ nguyên tính tự hài hòa của $$\phi(x)$$ khi $$t$$ lớn.
- **Tâm giải tích ($$t \to 0$$) vs. Nghiệm tối ưu ($$t \to \infty$$):** Đầu $$t \to 0$$ là tâm giải tích (chỉ phụ thuộc hình học ràng buộc); đầu $$t \to \infty$$ mới là nghiệm tối ưu $$x^*$$.
- **Điều kiện dừng Pha I:** Không cần đợi Pha I hội tụ đến cực tiểu $$s^*$$; ngay khi tìm được bất kỳ cặp $$(x, s)$$ nào có $$s < 0$$ là $$x$$ đã khả thi chặt cho bài toán gốc (còn nếu $$s^* > 0$$ thì bài toán gốc vô nghiệm).

### Giải thích: Giải mẫu câu hỏi bẫy về số ràng buộc $$m$$ khi có cả ràng buộc đẳng thức

**Câu hỏi mẫu:** Một bài toán quy hoạch tuyến tính có $$n = 50$$ biến, $$p = 15$$ ràng buộc đẳng thức $$Ax = b$$, và $$m = 20$$ ràng buộc bất đẳng thức $$h_i(x) \le 0$$. Nếu điểm đường trung tâm $$x^*(t)$$ ứng với $$t = 100$$, chặn trên chắc chắn cho $$f(x^*(100)) - f^*$$ là bao nhiêu?

1. **Phân loại các ràng buộc:**
   - $$n = 50$$: số chiều biến $$x$$ — **không** xuất hiện trong công thức $$m/t$$.
   - $$p = 15$$: số ràng buộc đẳng thức $$Ax = b$$ — được giữ nguyên trực tiếp trong phương pháp Newton có ràng buộc đẳng thức, **không** đưa vào hàm chắn logarit!
   - $$m = 20$$: số ràng buộc bất đẳng thức — mỗi ràng buộc đóng góp đúng $$-\frac{1}{t}$$ vào hiệu $$g(u^*(t), v^*(t)) - f(x^*(t))$$.
2. **Tính khoảng cách dưới tối ưu:**
   $$f(x^*(100)) - f^* \le \frac{m}{t} = \frac{20}{100} = 0.2.$$
   (Nhiều bạn dễ nhầm lấy $$(20 + 15)/100 = 0.35$$ hoặc $$50/100 = 0.5$$ — hãy nhớ chỉ đếm các ràng buộc nằm trong hàm chắn $$\phi$$!).

---

## 📚 Ôn tập lý thuyết

Trước khi làm bài tập trắc nghiệm, hãy ôn lại các khái niệm chính của chương này:

### ⚡ **Phương pháp chắn (Barrier Method)**

#### **Bài toán tối ưu có ràng buộc bất đẳng thức**
$$\min_x f(x) \quad 	ext{s.t.} \quad h_i(x) \le 0, \quad Ax = b$$

với $$i = 1,\ldots,m$$.

#### **Khó khăn khi tối ưu trực tiếp trên biên**
- **Ràng buộc chặt và không chặt:** Khó xác định trước ràng buộc nào là tích cực (active) tại nghiệm.
- **Chi phí khảo sát biên:** Phương pháp tập tích cực có thể tốn chi phí cao khi số ràng buộc $$m$$ lớn.
- **Không khả vi:** Hàm chỉ thị $$I_C(x)$$ không khả vi trên biên nên không áp dụng trực tiếp được phương pháp Newton.

#### **Ý tưởng của phương pháp điểm trong**
Giải bài toán từ **phần trong** của miền khả thi thay vì lần theo biên:
- Tránh bài toán tổ hợp xác định tập ràng buộc tích cực.
- Thay hàm chỉ thị bằng hàm chắn trơn, khả vi hai lần.
- Chuyển bài toán về chuỗi bài toán chỉ còn ràng buộc đẳng thức để giải bằng phương pháp Newton.

### 🚧 **Hàm chắn logarit (Logarithmic Barrier Function)**

#### **Xấp xỉ hàm chỉ thị**
**Hàm chỉ thị gốc:** $$I_C(x) = egin{cases} 0 & 	ext{if } x \in C \ \infty & 	ext{otherwise} \end{cases}$$

**Hàm chắn logarit:** $$\phi(x) = -\sum_{i=1}^m \log(-h_i(x))$$

#### **Tính chất của hàm chắn logarit**
- **Miền xác định:** $$\{x : h_i(x) < 0 \quad orall i\}$$ (miền khả thi chặt).
- **Tính trơn:** Khả vi hai lần trên phần trong miền khả thi.
- **Hiệu ứng chắn:** $$\phi(x) 	o \infty$$ khi $$x$$ tiến sát biên.
- **Tính tự hài hòa:** Khi các $$h_i$$ là hàm affine hoặc bậc hai lồi, $$\phi$$ là hàm tự hài hòa, cho phép phân tích hội tụ bất biến affine của phương pháp Newton.

#### **Bài toán chắn**
**Bài toán gốc:** $$\min f(x)$$ thỏa mãn $$h_i(x) \le 0, Ax = b$$.

**Bài toán chắn tương ứng (với tham số chắn $$t > 0$$):**
$$\min_x tf(x) + \phi(x) \quad 	ext{s.t.} \quad Ax = b$$

#### **Vai trò của tham số $$t$$**
- **$$t$$ nhỏ:** Hàm chắn chi phối, đẩy nghiệm vào sâu bên trong miền khả thi.
- **$$t$$ lớn:** Hàm mục tiêu gốc $$f(x)$$ chi phối mạnh hơn.
- **Khi $$t 	o \infty$$:** Bài toán chắn hội tụ về bài toán gốc.

### 🛤️ **Đường trung tâm (Central Path)**

#### **Định nghĩa**
**Đường trung tâm:** $$\{x^*(t) : t > 0\}$$, trong đó $$x^*(t) = rg\min_x \{tf(x) + \phi(x) : Ax = b\}$$.

#### **Tính chất**
- Tạo thành một đường cong trơn trong $$\mathbb{R}^n$$.
- Hội tụ về nghiệm tối ưu gốc: $$x^*(t) 	o x^*$$ khi $$t 	o \infty$$.
- Mọi điểm $$x^*(t)$$ đều khả thi chặt.
- Với mỗi $$t > 0$$, điểm $$x^*(t)$$ là duy nhất dưới điều kiện lồi chặt.

### 📊 **Điều kiện KKT nhiễu và diễn giải**

#### **Điều kiện KKT của bài toán chắn**
Cho bài toán $$\min tf(x) + \phi(x)$$ thỏa mãn $$Ax = b$$:
- **Điều kiện dừng:** $$t
abla f(x^*(t)) + 
abla \phi(x^*(t)) + A^T 
u^*(t) = 0$$
- **Khả thi nguyên thủy:** $$Ax^*(t) = b$$

#### **Điều kiện KKT của bài toán gốc**
Cho bài toán $$\min f(x)$$ thỏa mãn $$h_i(x) \le 0, Ax = b$$:
- **Điều kiện dừng:** $$
abla f(x^*) + \sum_{i=1}^m \lambda_i^* 
abla h_i(x^*) + A^T 
u^* = 0$$
- **Độ lệch bù:** $$\lambda_i^* h_i(x^*) = 0$$
- **Khả thi đối ngẫu:** $$\lambda_i^* \ge 0$$
- **Khả thi nguyên thủy:** $$h_i(x^*) \le 0, Ax^* = b$$

#### **Mối liên hệ**
Từ $$
abla \phi(x) = -\sum_{i=1}^m rac{1}{h_i(x)} 
abla h_i(x)$$, đặt $$\lambda_i^*(t) = -rac{1}{th_i(x^*(t))}$$ ta thu được **điều kiện KKT nhiễu** với $$\lambda_i^*(t) h_i(x^*(t)) = -rac{1}{t}$$.

### 📈 **Khoảng cách dưới tối ưu (Suboptimality Gap)**

#### **Định lý**
$$f(x^*(t)) - f^* \le rac{m}{t}$$

**Ý tưởng chứng minh:**
1. Xây dựng điểm khả thi đối ngẫu từ nghiệm trên đường trung tâm.
2. Áp dụng đối ngẫu yếu: $$f(x^*(t)) - f^* \le 	ext{duality gap}$$.
3. Khoảng cách đối ngẫu tại $$x^*(t)$$ đúng bằng $$rac{m}{t}$$.

#### **Ý nghĩa thực hành**
- Để đạt nghiệm chính xác $$\epsilon$$, chỉ cần $$t \ge rac{m}{\epsilon}$$.
- Đánh đổi: $$t$$ càng lớn thì xấp xỉ càng sát nhưng bài toán con càng khó giải.
- Tiêu chí dừng: $$rac{m}{t} < \epsilon$$.

### 🔄 **Các phiên bản thuật toán phương pháp chắn**

#### **Phương pháp chắn v.0 (giải trực tiếp một lần)**
Chọn trực tiếp $$t = rac{m}{\epsilon}$$ và giải $$\min tf(x) + \phi(x)$$ thỏa mãn $$Ax = b$$. Cách này kém hiệu quả vì với $$t$$ quá lớn, ma trận Hessian có số điều kiện rất xấu và phương pháp Newton hội tụ chậm.

#### **Phương pháp chắn v.1 (bám đường trung tâm)**
1. Chọn $$t^{(0)} > 0$$, đặt $$k = 0$$.
2. Giải bài toán chắn tại $$t^{(0)}$$ để thu được $$x^{(0)}$$.
3. **Trong khi** $$rac{m}{t^{(k)}} > \epsilon$$:
   - Cập nhật $$t^{(k+1)} = \mu t^{(k)}$$ (với $$\mu > 1$$).
   - **Khởi động ấm (warm start):** Dùng $$x^{(k)}$$ làm điểm khởi tạo cho phương pháp Newton.
   - Giải bài toán chắn tại $$t^{(k+1)}$$ để thu được $$x^{(k+1)}$$.
   - Tăng $$k \leftarrow k + 1$$.

#### **Các thành phần chính**
- **Bước định tâm (centering step):** Giải bài toán chắn cho một $$t$$ cố định (vòng lặp ngoài).
- **Bước Newton:** Các vòng lặp bên trong của mỗi bước định tâm.
- **Khởi động ấm:** Dùng nghiệm trước làm điểm xuất phát cho bước sau.

### ⚖️ **Đánh đổi khi chọn tham số**

- **Hệ số tăng $$\mu$$:** $$\mu$$ quá nhỏ làm tăng số vòng lặp ngoài; $$\mu$$ quá lớn làm tăng số bước Newton ở mỗi bước định tâm. Giá trị thường dùng là $$\mu = 10$$ đến $$50$$.
- **Tham số khởi tạo $$t^{(0)}$$:** $$t^{(0)}$$ quá nhỏ làm tăng số vòng lặp ngoài; $$t^{(0)}$$ quá lớn khiến bước định tâm đầu tiên khó giải.
- **Tính ổn định:** Trong thực tế, hiệu năng của phương pháp chắn khá bền vững trên một dải rộng của $$(\mu, t^{(0)})$$.

### 📊 **Phân tích hội tụ**

Giả sử mỗi bước định tâm được giải chính xác, sau $$k$$ vòng lặp ngoài ta có:
$$f(x^{(k)}) - f^* \le rac{m}{\mu^k t^{(0)}}$$

Số vòng lặp ngoài để đạt sai số $$\epsilon$$ là:
$$	ext{Số vòng lặp ngoài} = rac{\log(m/(t^{(0)}\epsilon))}{\log \mu} + 1$$

Bậc hội tụ là $$O(\log(1/\epsilon))$$ (hội tụ tuyến tính). So với gradient descent tổng quát ($$O(1/\epsilon)$$) và phương pháp Newton không ràng buộc ($$O(\log\log(1/\epsilon))$$), tốc độ tuyến tính là kết quả tốt cho bài toán có ràng buộc bất đẳng thức.

### 🎯 **Phương pháp tìm điểm khả thi (Phase I)**

Để bắt đầu phương pháp chắn, cần một điểm khả thi chặt thỏa mãn $$h_i(x) < 0 \;orall i$$ và $$Ax = b$$.

- **Cực tiểu hóa mức bất khả thi lớn nhất:** $$\min_{x,s} s \quad 	ext{s.t.} \quad h_i(x) \le s, \quad Ax = b$$. Nếu tìm được cặp khả thi có $$s < 0$$ thì $$x$$ là điểm khả thi chặt; nếu tối ưu $$s^* > 0$$ thì bài toán gốc vô nghiệm.
- **Tổng mức bất khả thi cho từng ràng buộc:** $$\min_{x,s} \mathbf{1}^T s \quad 	ext{s.t.} \quad h_i(x) \le s_i, \quad Ax = b, \quad s \succeq 0$$. Nghiệm tối ưu $$s^* = 0$$ tương đương bài toán gốc khả thi, đồng thời chỉ rõ ràng buộc nào bị vi phạm nếu bài toán vô nghiệm.

### 🛠️ **Chi tiết cài đặt và ví dụ LP**

#### **Gradient và Hessian của bài toán chắn**
- **Gradient:** $$
abla (tf + \phi) = t
abla f - \sum_{i=1}^m rac{1}{h_i(x)} 
abla h_i$$
- **Hessian:** $$
abla^2 (tf + \phi) = t
abla^2 f + \sum_{i=1}^m rac{1}{h_i^2(x)} 
abla h_i 
abla h_i^T - \sum_{i=1}^m rac{1}{h_i(x)} 
abla^2 h_i$$

#### **Ví dụ quy hoạch tuyến tính (LP)**
Với bài toán $$\min c^T x$$ thỏa mãn $$Ax = b, \; x \ge 0$$:
- **Bài toán chắn:** $$\min tc^T x - \sum_{i=1}^n \log x_i$$ thỏa mãn $$Ax = b$$.
- **Điều kiện KKT đường trung tâm:** $$tc + A^T 
u - X^{-1} e = 0, \quad Ax = b$$ (với $$X = 	ext{diag}(x)$$, $$e = (1,\ldots,1)^T$$), tương ứng độ lệch bù nhiễu $$x_i \lambda_i = rac{1}{t}$$.

### 🎯 **Kết nối và lưu ý thực hành**

- **Liên hệ kiến thức:** Phương pháp chắn kế thừa phương pháp Newton (Chương 14), điều kiện KKT (Chương 12) và lý thuyết đối ngẫu (Chương 11), đồng thời mở đường cho các phương pháp điểm trong nguyên thủy–đối ngẫu (primal-dual), nhúng đồng nhất và tối ưu nón (SOCP, SDP).
- **Lưu ý triển khai:** Luôn giữ điểm lặp khả thi chặt ($$h_i(x) < 0$$) thông qua backtracking line search; tận dụng khởi động ấm; theo dõi số điều kiện Hessian khi $$t$$ lớn; và thực hiện bước Phase I khi chưa có sẵn điểm khả thi chặt.
- **Ứng dụng:** Các bộ giải quy hoạch tuyến tính, bậc hai và nón (như CPLEX, Gurobi, MOSEK, Clarabel), tối ưu danh mục đầu tư, điều khiển tối ưu, thiết kế kỹ thuật và học máy.

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

Bài tập trắc nghiệm này kiểm tra kiến thức về phương pháp chắn (barrier method), bao gồm phương pháp điểm trong, hàm chắn logarit, đường trung tâm, phân tích hội tụ và các phương pháp tìm điểm khả thi.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>🚧 Bài tập trắc nghiệm: Phương pháp chắn và điểm trong</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 4%"></div>
        </div>
        <div class="score-display" id="score-display">Câu hỏi: <span id="current-q">1</span> / <span id="total-q">25</span></div>
    </div>

    <div id="quiz-content">
        <!-- Câu hỏi 1: Barrier method concept -->
        <div class="question" id="q1" style="display: block;">
            <h3>Câu 1: Phương pháp chắn (barrier method) xử lý các ràng buộc bất đẳng thức bằng cách:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) Chuyển trực tiếp thành ràng buộc đẳng thức</label>
                <label><input type="radio" name="q1" value="b"> B) Thêm hàm chắn vào hàm mục tiêu</label>
                <label><input type="radio" name="q1" value="c"> C) Loại bỏ các ràng buộc bất đẳng thức</label>
                <label><input type="radio" name="q1" value="d"> D) Dùng hàm phạt bên ngoài miền khả thi</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Thêm hàm chắn vào hàm mục tiêu</strong><br>
                Phương pháp chắn bổ sung hàm chắn vào hàm mục tiêu để giữ mọi điểm lặp nằm trong phần trong miền khả thi, tránh vi phạm ràng buộc.
            </div>
        </div>

        <!-- Câu hỏi 2: Log barrier function -->
        <div class="question" id="q2" style="display: none;">
            <h3>Câu 2: Hàm chắn logarit cho ràng buộc \(g_i(x) \leq 0\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) \(-\log(-g_i(x))\)</label>
                <label><input type="radio" name="q2" value="b"> B) \(\log(g_i(x))\)</label>
                <label><input type="radio" name="q2" value="c"> C) \(-\log(g_i(x))\)</label>
                <label><input type="radio" name="q2" value="d"> D) \(\log(-g_i(x))\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$-\log(-g_i(x))$$</strong><br>
                Hàm chắn logarit $$-\log(-g_i(x))$$ xác định khi $$g_i(x) < 0$$ và tiến tới $$+\infty$$ khi $$g_i(x) 	o 0^-$$ (tiến sát biên).
            </div>
        </div>

        <!-- Câu hỏi 3: Barrier problem -->
        <div class="question" id="q3" style="display: none;">
            <h3>Câu 3: Bài toán chắn (barrier problem) có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) \(\min tf(x) + \phi(x)\) thỏa mãn \(Ax = b\)</label>
                <label><input type="radio" name="q3" value="b"> B) \(\min f(x) + t\phi(x)\) thỏa mãn \(Ax = b\)</label>
                <label><input type="radio" name="q3" value="c"> C) \(\min f(x) - t\phi(x)\) thỏa mãn \(Ax = b\)</label>
                <label><input type="radio" name="q3" value="d"> D) \(\min f(x)\) thỏa mãn \(Ax = b, g(x) \leq 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\min tf(x) + \phi(x)$$ thỏa mãn $$Ax = b$$</strong><br>
                Với tham số $$t > 0$$, khi $$t 	o \infty$$ nghiệm của bài toán chắn hội tụ về nghiệm của bài toán gốc.
            </div>
        </div>

        <!-- Câu hỏi 4: Central path -->
        <div class="question" id="q4" style="display: none;">
            <h3>Câu 4: Đường trung tâm (central path) là:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) Tập hợp \(\{x^*(t) | t > 0\}\) với \(x^*(t)\) là nghiệm của bài toán chắn</label>
                <label><input type="radio" name="q4" value="b"> B) Đoạn thẳng nối điểm khởi tạo với điểm tối ưu</label>
                <label><input type="radio" name="q4" value="c"> C) Tâm hình học của miền khả thi</label>
                <label><input type="radio" name="q4" value="d"> D) Quỹ đạo của gradient descent</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Tập hợp $$\{x^*(t) | t > 0\}$$ với $$x^*(t)$$ là nghiệm của bài toán chắn</strong><br>
                Đường trung tâm là quỹ đạo nghiệm tối ưu $$x^*(t)$$ của bài toán chắn khi tham số $$t$$ biến thiên từ $$0$$ đến $$\infty$$.
            </div>
        </div>

        <!-- Câu hỏi 5: Central path properties -->
        <div class="question" id="q5" style="display: none;">
            <h3>Câu 5: Khi \(t 	o \infty\), đường trung tâm có tính chất:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) Hội tụ về nghiệm tối ưu của bài toán gốc</label>
                <label><input type="radio" name="q5" value="b"> B) Phân kỳ</label>
                <label><input type="radio" name="q5" value="c"> C) Dao động không hội tụ</label>
                <label><input type="radio" name="q5" value="d"> D) Tiến tới một điểm bất kỳ trên biên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Hội tụ về nghiệm tối ưu của bài toán gốc</strong><br>
                Khi $$t 	o \infty$$, trọng số tương đối $$rac{1}{t}$$ của hàm chắn tiến về 0 nên $$x^*(t)$$ tiến về nghiệm tối ưu $$x^*$$ của bài toán gốc.
            </div>
        </div>

        <!-- Câu hỏi 6: KKT conditions for barrier -->
        <div class="question" id="q6" style="display: none;">
            <h3>Câu 6: Điều kiện dừng KKT của bài toán chắn tại \(x^*(t)\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) \(t
abla f(x) + \sum rac{1}{-g_i(x)} 
abla g_i(x) + A^T
u = 0\)</label>
                <label><input type="radio" name="q6" value="b"> B) \(
abla f(x) + \sum \lambda_i 
abla g_i(x) + A^T
u = 0\)</label>
                <label><input type="radio" name="q6" value="c"> C) \(t
abla f(x) = 0\)</label>
                <label><input type="radio" name="q6" value="d"> D) \(
abla f(x) = 0\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$t
abla f(x) + \sum rac{1}{-g_i(x)} 
abla g_i(x) + A^T
u = 0$$</strong><br>
                Từ điều kiện dừng $$t
abla f(x) + 
abla \phi(x) + A^T
u = 0$$ với $$
abla \phi(x) = \sum rac{1}{-g_i(x)} 
abla g_i(x)$$.
            </div>
        </div>

        <!-- Câu hỏi 7: Dual variables interpretation -->
        <div class="question" id="q7" style="display: none;">
            <h3>Câu 7: Biến đối ngẫu tương ứng với điểm đường trung tâm \(x^*(t)\) được xác định bởi:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) \(\lambda_i^*(t) = rac{1}{t(-g_i(x^*(t)))}\)</label>
                <label><input type="radio" name="q7" value="b"> B) \(\lambda_i^*(t) = t(-g_i(x^*(t)))\)</label>
                <label><input type="radio" name="q7" value="c"> C) \(\lambda_i^*(t) = -g_i(x^*(t))\)</label>
                <label><input type="radio" name="q7" value="d"> D) \(\lambda_i^*(t) = rac{1}{-g_i(x^*(t))}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\lambda_i^*(t) = rac{1}{t(-g_i(x^*(t)))}$$</strong><br>
                Biến đối ngẫu này luôn dương, khả thi đối ngẫu và hội tụ về biến đối ngẫu tối ưu khi $$t 	o \infty$$.
            </div>
        </div>

        <!-- Câu hỏi 8: Duality gap -->
        <div class="question" id="q8" style="display: none;">
            <h3>Câu 8: Khoảng cách đối ngẫu (duality gap) tại điểm đường trung tâm \(x^*(t)\) là:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) \(rac{m}{t}\) với \(m\) là số ràng buộc bất đẳng thức</label>
                <label><input type="radio" name="q8" value="b"> B) \(rac{1}{t}\)</label>
                <label><input type="radio" name="q8" value="c"> C) \(mt\)</label>
                <label><input type="radio" name="q8" value="d"> D) \(t\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$rac{m}{t}$$ với $$m$$ là số ràng buộc bất đẳng thức</strong><br>
                Khoảng cách đối ngẫu $$\eta = f(x^*(t)) - g(\lambda^*(t), 
u^*(t)) = rac{m}{t}$$, tiến về 0 khi tăng $$t$$.
            </div>
        </div>

        <!-- Câu hỏi 9: Barrier method algorithm -->
        <div class="question" id="q9" style="display: none;">
            <h3>Câu 9: Nguyên lý vận hành của thuật toán phương pháp chắn là:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) Tăng dần \(t\) theo dãy và giải bài toán chắn ứng với mỗi giá trị \(t\)</label>
                <label><input type="radio" name="q9" value="b"> B) Giảm dần \(t\) theo dãy</label>
                <label><input type="radio" name="q9" value="c"> C) Giữ \(t\) cố định trong suốt thuật toán</label>
                <label><input type="radio" name="q9" value="d"> D) Chọn \(t\) ngẫu nhiên ở mỗi bước</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Tăng dần $$t$$ theo dãy và giải bài toán chắn ứng với mỗi giá trị $$t$$</strong><br>
                Thuật toán bắt đầu từ $$t^{(0)}$$, giải bài toán chắn rồi cập nhật $$t^{(k+1)} = \mu t^{(k)}$$ với $$\mu > 1$$ cho đến khi $$m/t \le \epsilon$$.
            </div>
        </div>

        <!-- Câu hỏi 10: Centering step -->
        <div class="question" id="q10" style="display: none;">
            <h3>Câu 10: Bước định tâm (centering step) trong phương pháp chắn là:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) Giải bài toán chắn ứng với một giá trị \(t\) cố định bằng phương pháp Newton</label>
                <label><input type="radio" name="q10" value="b"> B) Tìm tâm hình học của miền khả thi</label>
                <label><input type="radio" name="q10" value="c"> C) Cập nhật tham số \(t\)</label>
                <label><input type="radio" name="q10" value="d"> D) Kiểm tra tính khả thi của nghiệm</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Giải bài toán chắn ứng với một giá trị $$t$$ cố định bằng phương pháp Newton</strong><br>
                Bước định tâm giải $$\min tf(x) + \phi(x)$$ thỏa mãn $$Ax = b$$ để tìm điểm $$x^*(t)$$ (hoặc xấp xỉ đủ tốt của nó) trên đường trung tâm.
            </div>
        </div>

        <!-- Câu hỏi 11: Self-concordance of log barrier -->
        <div class="question" id="q11" style="display: none;">
            <h3>Câu 11: Khi các \(g_i\) là hàm affine, hàm chắn logarit \(-\log(-g_i(x))\) có tính chất:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) Tự hài hòa (self-concordant)</label>
                <label><input type="radio" name="q11" value="b"> B) Lồi</label>
                <label><input type="radio" name="q11" value="c"> C) Trơn (khả vi vô hạn trên phần trong miền khả thi)</label>
                <label><input type="radio" name="q11" value="d"> D) Tất cả các tính chất trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các tính chất trên</strong><br>
                Khi $$g_i$$ là hàm affine, hàm chắn logarit vừa lồi, trơn, vừa tự hài hòa, giúp đảm bảo cận hội tụ lý thuyết cho phương pháp Newton. (Với $$g_i$$ lồi tổng quát, hàm chắn vẫn lồi và trơn nhưng không nhất thiết tự hài hòa.)
            </div>
        </div>

        <!-- Câu hỏi 12: Feasibility methods -->
        <div class="question" id="q12" style="display: none;">
            <h3>Câu 12: Bài toán Phase I cơ bản để tìm điểm xuất phát khả thi chặt có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) \(\min s\) thỏa mãn \(g_i(x) \leq s, Ax = b\)</label>
                <label><input type="radio" name="q12" value="b"> B) \(\min \|g(x)\|\)</label>
                <label><input type="radio" name="q12" value="c"> C) \(\min f(x)\)</label>
                <label><input type="radio" name="q12" value="d"> D) \(\min \|x\|\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\min s$$ thỏa mãn $$g_i(x) \leq s, Ax = b$$</strong><br>
                Phase I cực tiểu hóa biến phụ $$s$$. Nếu nghiệm tối ưu $$s^* < 0$$ thì tồn tại điểm khả thi chặt; nếu $$s^* > 0$$ thì bài toán gốc vô nghiệm.
            </div>
        </div>

        <!-- Câu hỏi 13: Convergence rate -->
        <div class="question" id="q13" style="display: none;">
            <h3>Câu 13: Số vòng lặp ngoài của phương pháp chắn để đạt độ chính xác \(\epsilon\) có bậc:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) \(O(\log(1/\epsilon))\)</label>
                <label><input type="radio" name="q13" value="b"> B) \(O(1/\epsilon)\)</label>
                <label><input type="radio" name="q13" value="c"> C) \(O(\sqrt{1/\epsilon})\)</label>
                <label><input type="radio" name="q13" value="d"> D) \(O(1/\epsilon^2)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$O(\log(1/\epsilon))$$</strong><br>
                Với quy tắc nhân $$t^{(k+1)} = \mu t^{(k)}$$, số vòng lặp ngoài để thu nhỏ khoảng cách đối ngẫu về dưới $$\epsilon$$ tăng theo $$O(\log(1/\epsilon))$$.
            </div>
        </div>

        <!-- Câu hỏi 14: Newton decrement in barrier -->
        <div class="question" id="q14" style="display: none;">
            <h3>Câu 14: Đại lượng giảm Newton (Newton decrement) trong phương pháp chắn được dùng để:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) Làm tiêu chí dừng cho bước định tâm</label>
                <label><input type="radio" name="q14" value="b"> B) Cập nhật trực tiếp tham số \(t\)</label>
                <label><input type="radio" name="q14" value="c"> C) Kiểm tra tính khả thi của ràng buộc</label>
                <label><input type="radio" name="q14" value="d"> D) Tính khoảng cách đối ngẫu \(m/t\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Làm tiêu chí dừng cho bước định tâm</strong><br>
                Điều kiện $$\lambda(x) \leq \eta$$ kiểm soát mức độ gần đường trung tâm trước khi tăng tham số $$t$$.
            </div>
        </div>

        <!-- Câu hỏi 15: Primal-dual methods -->
        <div class="question" id="q15" style="display: none;">
            <h3>Câu 15: Phương pháp điểm trong nguyên thủy–đối ngẫu (primal-dual) khác phương pháp chắn ở chỗ:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) Cập nhật đồng thời cả biến nguyên thủy và biến đối ngẫu</label>
                <label><input type="radio" name="q15" value="b"> B) Không liên quan đến đường trung tâm</label>
                <label><input type="radio" name="q15" value="c"> C) Chỉ áp dụng cho quy hoạch tuyến tính</label>
                <label><input type="radio" name="q15" value="d"> D) Không sử dụng phương pháp Newton</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Cập nhật đồng thời cả biến nguyên thủy và biến đối ngẫu</strong><br>
                Phương pháp nguyên thủy–đối ngẫu cập nhật trực tiếp bộ $$(x, \lambda, 
u)$$ cùng lúc thay vì chỉ giải tìm $$x$$ ở từng vòng lặp ngoài.
            </div>
        </div>

        <!-- Câu hỏi 16: Barrier parameter update -->
        <div class="question" id="q16" style="display: none;">
            <h3>Câu 16: Quy tắc cập nhật tham số chắn thường dùng trong thực hành là:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) \(t^{(k+1)} = \mu t^{(k)}\) với \(\mu = 10\)</label>
                <label><input type="radio" name="q16" value="b"> B) \(t^{(k+1)} = t^{(k)} + 1\)</label>
                <label><input type="radio" name="q16" value="c"> C) \(t^{(k+1)} = 2t^{(k)}\)</label>
                <label><input type="radio" name="q16" value="d"> D) \(t^{(k+1)} = (t^{(k)})^2\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$t^{(k+1)} = \mu t^{(k)}$$ với $$\mu = 10$$</strong><br>
                Giá trị $$\mu pprox 10$$ (hoặc trong khoảng 10–50) thường cân bằng tốt giữa số vòng lặp ngoài và số bước Newton trong mỗi bước định tâm.
            </div>
        </div>

        <!-- Câu hỏi 17: Barrier method advantages -->
        <div class="question" id="q17" style="display: none;">
            <h3>Câu 17: Ưu điểm của phương pháp chắn là:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Có độ phức tạp đa thức về mặt lý thuyết</label>
                <label><input type="radio" name="q17" value="b"> B) Tận dụng tốt khởi động ấm (warm start) giữa các bước định tâm</label>
                <label><input type="radio" name="q17" value="c"> C) Xử lý ràng buộc bất đẳng thức mà không cần xác định tập tích cực</label>
                <label><input type="radio" name="q17" value="d"> D) Tất cả các ưu điểm trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các ưu điểm trên</strong><br>
                Phương pháp chắn có độ phức tạp đa thức, tận dụng khởi động ấm hiệu quả và xử lý tự nhiên số lượng lớn ràng buộc bất đẳng thức.
            </div>
        </div>

        <!-- Câu hỏi 18: Linear programming barrier -->
        <div class="question" id="q18" style="display: none;">
            <h3>Câu 18: Cho bài toán LP: \(\min c^Tx\) thỏa mãn \(Ax = b, x \geq 0\). Hàm chắn logarit tương ứng là:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) \(-\sum_{i=1}^n \log x_i\)</label>
                <label><input type="radio" name="q18" value="b"> B) \(\sum_{i=1}^n \log x_i\)</label>
                <label><input type="radio" name="q18" value="c"> C) \(-\sum_{i=1}^n x_i\)</label>
                <label><input type="radio" name="q18" value="d"> D) \(\sum_{i=1}^n x_i^2\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$-\sum_{i=1}^n \log x_i$$</strong><br>
                Với các ràng buộc $$-x_i \leq 0$$ (tức $$x_i \geq 0$$), hàm chắn logarit là $$-\sum_{i=1}^n \log x_i$$, giữ chặt $$x_i > 0$$.
            </div>
        </div>

        <!-- Câu hỏi 19: Barrier method vs penalty method -->
        <div class="question" id="q19" style="display: none;">
            <h3>Câu 19: Phương pháp chắn (barrier) khác phương pháp phạt (penalty) ở điểm nào?</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) Phương pháp chắn luôn giữ các điểm lặp bên trong miền khả thi</label>
                <label><input type="radio" name="q19" value="b"> B) Phương pháp phạt cho phép các điểm lặp vi phạm ràng buộc trong quá trình tối ưu</label>
                <label><input type="radio" name="q19" value="c"> C) Phương pháp chắn đòi hỏi điểm khởi tạo khả thi chặt</label>
                <label><input type="radio" name="q19" value="d"> D) Tất cả các điểm trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các điểm trên</strong><br>
                Phương pháp chắn duy trì tính khả thi chặt ở mọi bước và cần điểm khởi tạo khả thi chặt, trái ngược với phương pháp phạt tiếp cận nghiệm từ bên ngoài miền khả thi.
            </div>
        </div>

        <!-- Câu hỏi 20: Applications -->
        <div class="question" id="q20" style="display: none;">
            <h3>Câu 20: Các phương pháp điểm trong được ứng dụng trong:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Các bộ giải quy hoạch tuyến tính (LP)</label>
                <label><input type="radio" name="q20" value="b"> B) Quy hoạch nửa xác định (SDP)</label>
                <label><input type="radio" name="q20" value="c"> C) Các thư viện tối ưu lồi hiện đại</label>
                <label><input type="radio" name="q20" value="d"> D) Tất cả các ứng dụng trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các ứng dụng trên</strong><br>
                Phương pháp điểm trong là thuật toán nền tảng của nhiều bộ giải như CPLEX, Gurobi, CVX, MOSEK và Clarabel.
            </div>
        </div>

        <!-- Câu hỏi 21: Thực hành -->
        <div class="question" id="q21" style="display: none;">
            <h3>Câu 21: Phương pháp chắn biến đổi bài toán có ràng buộc bất đẳng thức thành:</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) Chuỗi bài toán không có ràng buộc bất đẳng thức (không ràng buộc hoặc chỉ có ràng buộc đẳng thức)</label>
                <label><input type="radio" name="q21" value="b"> B) Một bài toán tuyến tính duy nhất</label>
                <label><input type="radio" name="q21" value="c"> C) Một bài toán QP không tham số</label>
                <label><input type="radio" name="q21" value="d"> D) Một bài toán SDP</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Chuỗi bài toán không có ràng buộc bất đẳng thức</strong><br>
                Phương pháp chắn giải chuỗi bài toán $$\min t f(x) + \phi(x)$$ (tương đương $$\min f(x) + rac{1}{t}\phi(x)$$) với $$t 	o \infty$$.
            </div>
        </div>

        <!-- Câu hỏi 22: Thực hành -->
        <div class="question" id="q22" style="display: none;">
            <h3>Câu 22: Hàm chắn logarit cho hệ ràng buộc $$g_i(x) \leq 0$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) $$-\sum \log(-g_i(x))$$</label>
                <label><input type="radio" name="q22" value="b"> B) $$\sum \log(g_i(x))$$</label>
                <label><input type="radio" name="q22" value="c"> C) $$\sum g_i(x)^2$$</label>
                <label><input type="radio" name="q22" value="d"> D) $$\sum |g_i(x)|$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$-\sum \log(-g_i(x))$$</strong><br>
                Hàm chắn logarit được định nghĩa là $$\phi(x) = -\sum_{i=1}^m \log(-g_i(x))$$ trên miền $$g_i(x) < 0$$.
            </div>
        </div>

        <!-- Câu hỏi 23: Thực hành -->
        <div class="question" id="q23" style="display: none;">
            <h3>Câu 23: Đường trung tâm trong phương pháp chắn là:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) Tập nghiệm của hệ $$t
abla f + 
abla \phi + A^T
u = 0$$ (cùng $$Ax = b$$) theo $$t > 0$$</label>
                <label><input type="radio" name="q23" value="b"> B) Đường thẳng đi qua nghiệm tối ưu</label>
                <label><input type="radio" name="q23" value="c"> C) Biên của miền khả thi</label>
                <label><input type="radio" name="q23" value="d"> D) Quỹ đạo của gradient descent</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Tập nghiệm của hệ $$t
abla f + 
abla \phi + A^T
u = 0$$ (cùng $$Ax = b$$) theo $$t > 0$$</strong><br>
                Mỗi điểm $$x^*(t)$$ trên đường trung tâm thỏa mãn điều kiện tối ưu $$t
abla f(x) + 
abla \phi(x) + A^T
u = 0$$ và $$Ax = b$$.
            </div>
        </div>

        <!-- Câu hỏi 24: Thực hành -->
        <div class="question" id="q24" style="display: none;">
            <h3>Câu 24: Khi $$t 	o \infty$$ trong phương pháp chắn:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) Nghiệm $$x^*(t)$$ tiến đến nghiệm tối ưu của bài toán gốc</label>
                <label><input type="radio" name="q24" value="b"> B) Nghiệm phân kỳ</label>
                <label><input type="radio" name="q24" value="c"> C) Hàm chắn luôn bằng 0</label>
                <label><input type="radio" name="q24" value="d"> D) Bài toán mất nghiệm</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Nghiệm $$x^*(t)$$ tiến đến nghiệm tối ưu của bài toán gốc</strong><br>
                Khi $$t 	o \infty$$, khoảng cách dưới tối ưu $$m/t 	o 0$$ nên nghiệm bài toán chắn hội tụ về nghiệm bài toán gốc.
            </div>
        </div>

        <!-- Câu hỏi 25: Thực hành -->
        <div class="question" id="q25" style="display: none;">
            <h3>Câu 25: Với ràng buộc $$x > 0$$, đạo hàm của hàm chắn $$-\log x$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) $$-1/x$$</label>
                <label><input type="radio" name="q25" value="b"> B) $$1/x$$</label>
                <label><input type="radio" name="q25" value="c"> C) $$-x$$</label>
                <label><input type="radio" name="q25" value="d"> D) $$\log x$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$-1/x$$</strong><br>
                Ta có $$rac{d}{dx}(-\log x) = -rac{1}{x}$$.
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
        <h2>🎉 Hoàn thành bài tập trắc nghiệm!</h2>
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
    q1: 'b', q2: 'a', q3: 'a', q4: 'a', q5: 'a',
    q6: 'a', q7: 'a', q8: 'a', q9: 'a', q10: 'a',
    q11: 'd', q12: 'a', q13: 'a', q14: 'a', q15: 'a',
    q16: 'a', q17: 'd', q18: 'a', q19: 'd', q20: 'd'
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
        message = '🌟 Xuất sắc! Bạn đã thành thạo barrier method và interior point optimization!';
    } else if (percentage >= 80) {
        message = '👍 Rất tốt! Bạn hiểu tốt về central path và convergence analysis.';
    } else if (percentage >= 70) {
        message = '📚 Khá ổn! Hãy xem lại log barrier function và duality gap.';
    } else if (percentage >= 60) {
        message = '💪 Cần cải thiện! Ôn lại barrier problem và KKT conditions.';
    } else {
        message = '📖 Hãy học lại từ đầu về interior point methods nhé!';
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
