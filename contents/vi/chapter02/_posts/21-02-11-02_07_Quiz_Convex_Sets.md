---
layout: post
title: 02-07 Bài tập trắc nghiệm - Tập lồi
chapter: '02'
order: 12
owner: GitHub Copilot
lang: vi
categories:
- chapter02
lesson_type: quiz
---

Bài tập trắc nghiệm này kiểm tra hiểu biết của bạn về tập affine, tập lồi và các ví dụ quan trọng trong hình học lồi.

---

## 📚 Ôn tập lý thuyết

Trước khi làm bài tập, hãy ôn lại các khái niệm chính trong chương này:

### 📏 **Tập Affine**

**Định nghĩa:**
Tập $$C$$ là affine nếu với mọi $$x_1, x_2 \in C$$ và $$\theta \in \mathbb{R}$$:
$$\theta x_1 + (1-\theta)x_2 \in C$$

**Tổ hợp affine:**
$$\sum_{i=1}^k \theta_i x_i$$ với $$\sum_{i=1}^k \theta_i = 1$$ (không yêu cầu $$\theta_i \ge 0$$)

**Bao affine:**
$$\text{aff}(C) = \{\sum_{i=1}^k \theta_i x_i \mid x_i \in C, \sum_{i=1}^k \theta_i = 1\}$$

**Tính chất:** Tập affine = phép tịnh tiến của không gian con tuyến tính

### 🔵 **Tập Lồi**

**Định nghĩa:**
Tập $$C$$ là lồi nếu với mọi $$x_1, x_2 \in C$$ và $$0 \le \theta \le 1$$:
$$\theta x_1 + (1-\theta)x_2 \in C$$

**Tổ hợp lồi:**
$$\sum_{i=1}^k \theta_i x_i$$ với $$\sum_{i=1}^k \theta_i = 1, \theta_i \ge 0$$

**Bao lồi:**
$$\text{conv}(C) = \{\sum_{i=1}^k \theta_i x_i \mid x_i \in C, \theta_i \ge 0, \sum_{i=1}^k \theta_i = 1\}$$

**Trực quan:** Không có "vết lõm" - đoạn thẳng nối 2 điểm bất kỳ đều nằm trong tập

### 🔺 **Hình Nón và Hình Nón Lồi**

**Hình nón:**
Tập $$C$$ là nón nếu với mọi $$x \in C$$ và $$\theta \ge 0$$:
$$\theta x \in C$$

**Hình nón lồi:**
Vừa là nón vừa là lồi. Với $$x_1, x_2 \in C$$ và $$\theta_1, \theta_2 \ge 0$$:
$$\theta_1 x_1 + \theta_2 x_2 \in C$$

**Tổ hợp nón:**
$$\sum_{i=1}^k \theta_i x_i$$ với $$\theta_i \ge 0$$ (không yêu cầu tổng = 1)

### 📐 **Các Ví Dụ Quan Trọng**

**Tập hợp cơ bản:**
- Tập rỗng $$\emptyset$$: lồi
- Điểm đơn $$\{x_0\}$$: lồi
- Đường thẳng, đoạn thẳng, tia: lồi

**Siêu phẳng:**
$$\{x \mid a^T x = b\}$$ với $$a \neq 0$$ - là tập affine và lồi

**Nửa không gian:**
$$\{x \mid a^T x \le b\}$$ với $$a \neq 0$$ - là tập lồi

**Không gian affine:**
$$\{x \mid Ax = b\}$$ - là tập affine và lồi

**Hình cầu Euclidean:**
$$\{x \mid \lVert x - x_c \rVert_2 \le r\}$$ - là tập lồi

**Hình cầu chuẩn:**
$$\{x \mid \lVert x \rVert \le r\}$$ với chuẩn bất kỳ - là tập lồi

**Ellipsoid:**
$$\{x \mid (x-x_c)^T P^{-1} (x-x_c) \le 1\}$$ với $$P \succ 0$$ - là tập lồi

### ✂️ **Siêu Phẳng Phân Tách và Hỗ Trợ**

**Định lý siêu phẳng phân tách:**
Nếu $$C$$ và $$D$$ là hai tập lồi rời rạc, tồn tại siêu phẳng $$\{x \mid a^T x = b\}$$ sao cho:
- $$a^T x \le b$$ với mọi $$x \in C$$
- $$a^T x \ge b$$ với mọi $$x \in D$$

**Định lý siêu phẳng hỗ trợ:**
Với tập lồi $$C$$ và điểm biên $$x_0 \in \text{bd}(C)$$, tồn tại siêu phẳng hỗ trợ:
$$\{x \mid a^T x = a^T x_0\}$$ sao cho $$a^T x \le a^T x_0$$ với mọi $$x \in C$$

### 🔗 **Mối Quan Hệ Giữa Các Tập**

```
Tập Affine ⊂ Tập Lồi
     ↓
Hình Nón ⊂ Hình Nón Lồi ⊂ Tập Lồi
```

**Ghi nhớ:**
- **Affine:** Đường thẳng qua 2 điểm ($$\theta \in \mathbb{R}$$)
- **Lồi:** Đoạn thẳng nối 2 điểm ($$0 \le \theta \le 1$$)  
- **Nón:** Tia từ gốc qua điểm ($$\theta \ge 0$$)

### 🎯 **Các Phép Toán Bảo Toàn Tính Lồi**

- **Giao:** Giao của các tập lồi là lồi
- **Tổ hợp affine:** $$\alpha C + \beta D$$ lồi nếu $$C, D$$ lồi
- **Ảnh affine:** $$f(C) = \{Ax + b \mid x \in C\}$$ lồi nếu $$C$$ lồi
- **Ảnh ngược affine:** $$f^{-1}(D) = \{x \mid Ax + b \in D\}$$ lồi nếu $$D$$ lồi

---

💡 **Mẹo:** Tập lồi là nền tảng của tối ưu hóa lồi. Hầu hết các tập ràng buộc trong thực tế đều có thể biểu diễn bằng giao của các tập lồi cơ bản!

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>Bài tập trắc nghiệm: Tập lồi</h2>
        <p>Chọn đáp án đúng nhất cho mỗi câu hỏi. Bài tập tập trung vào các khái niệm cơ bản về tập affine, tập lồi và siêu phẳng.</p>
        <div id="progress-bar">
            <div id="progress-fill"></div>
        </div>
        <p id="progress-text">Câu hỏi 1/25</p>
    </div>

    <div id="quiz-questions">
        <!-- Câu hỏi 1: Định nghĩa tập affine -->
        <div class="question" id="q1">
            <h3>Câu 1: Tập $$C$$ là tập affine nếu:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) Với mọi $$x_1, x_2 \in C$$ và $$0 \leq \theta \leq 1$$, ta có $$\theta x_1 + (1-\theta)x_2 \in C$$</label>
                <label><input type="radio" name="q1" value="b"> B) Với mọi $$x_1, x_2 \in C$$ và $$\theta \in \mathbb{R}$$, ta có $$\theta x_1 + (1-\theta)x_2 \in C$$</label>
                <label><input type="radio" name="q1" value="c"> C) Tập $$C$$ là tập đóng</label>
                <label><input type="radio" name="q1" value="d"> D) Tập $$C$$ có biên giới</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Với mọi $$x_1, x_2 \in C$$ và $$\theta \in \mathbb{R}$$, ta có $$\theta x_1 + (1-\theta)x_2 \in C$$</strong><br>
                Tập affine chứa toàn bộ đường thẳng đi qua bất kỳ hai điểm nào trong tập, không giới hạn $$\theta$$ trong khoảng $$[0,1]$$.
            </div>
        </div>

        <!-- Câu hỏi 2: Tổ hợp affine -->
        <div class="question" id="q2" style="display: none;">
            <h3>Câu 2: Tổ hợp affine của các điểm $$x_1, x_2, ..., x_k$$ có dạng:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) $$\sum_{i=1}^k \theta_i x_i$$ với $$\theta_i \geq 0$$</label>
                <label><input type="radio" name="q2" value="b"> B) $$\sum_{i=1}^k \theta_i x_i$$ với $$\sum_{i=1}^k \theta_i = 1$$</label>
                <label><input type="radio" name="q2" value="c"> C) $$\sum_{i=1}^k \theta_i x_i$$ với $$\theta_i \geq 0$$ và $$\sum_{i=1}^k \theta_i = 1$$</label>
                <label><input type="radio" name="q2" value="d"> D) $$\sum_{i=1}^k x_i$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$\sum_{i=1}^k \theta_i x_i$$ với $$\sum_{i=1}^k \theta_i = 1$$</strong><br>
                Tổ hợp affine chỉ yêu cầu tổng các hệ số bằng 1, không yêu cầu các hệ số không âm (khác với tổ hợp lồi).
            </div>
        </div>

        <!-- Câu hỏi 3: Mối quan hệ tập affine và không gian con -->
        <div class="question" id="q3" style="display: none;">
            <h3>Câu 3: Nếu $$C$$ là tập affine và $$x_0 \in C$$, thì $$V = C - x_0$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) Tập affine</label>
                <label><input type="radio" name="q3" value="b"> B) Không gian con tuyến tính</label>
                <label><input type="radio" name="q3" value="c"> C) Tập lồi</label>
                <label><input type="radio" name="q3" value="d"> D) Siêu phẳng</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Không gian con tuyến tính</strong><br>
                Tập affine $$C$$ là phép tịnh tiến của không gian con tuyến tính $$V$$ bởi $$x_0$$. Do đó $$V = C - x_0$$ là không gian con.
            </div>
        </div>

        <!-- Câu hỏi 4: Định nghĩa tập lồi -->
        <div class="question" id="q4" style="display: none;">
            <h3>Câu 4: Tập $$C$$ là tập lồi nếu:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) Với mọi $$x_1, x_2 \in C$$ và $$\theta \in \mathbb{R}$$, ta có $$\theta x_1 + (1-\theta)x_2 \in C$$</label>
                <label><input type="radio" name="q4" value="b"> B) Với mọi $$x_1, x_2 \in C$$ và $$0 \leq \theta \leq 1$$, ta có $$\theta x_1 + (1-\theta)x_2 \in C$$</label>
                <label><input type="radio" name="q4" value="c"> C) Tập $$C$$ không có lỗ hổng</label>
                <label><input type="radio" name="q4" value="d"> D) Tập $$C$$ là hình tròn</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Với mọi $$x_1, x_2 \in C$$ và $$0 \leq \theta \leq 1$$, ta có $$\theta x_1 + (1-\theta)x_2 \in C$$</strong><br>
                Tập lồi chứa đoạn thẳng nối bất kỳ hai điểm nào trong tập, với $$\theta$$ giới hạn trong $$[0,1]$$.
            </div>
        </div>

        <!-- Câu hỏi 5: Tổ hợp lồi -->
        <div class="question" id="q5" style="display: none;">
            <h3>Câu 5: Tổ hợp lồi khác với tổ hợp affine ở điểm nào?</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) Tổng các hệ số phải bằng 1</label>
                <label><input type="radio" name="q5" value="b"> B) Các hệ số phải không âm</label>
                <label><input type="radio" name="q5" value="c"> C) Số lượng điểm tham gia</label>
                <label><input type="radio" name="q5" value="d"> D) Không có sự khác biệt</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Các hệ số phải không âm</strong><br>
                Tổ hợp lồi yêu cầu $$\theta_i \geq 0$$ và $$\sum \theta_i = 1$$, trong khi tổ hợp affine chỉ cần $$\sum \theta_i = 1$$.
            </div>
        </div>

        <!-- Câu hỏi 6: Siêu phẳng -->
        <div class="question" id="q6" style="display: none;">
            <h3>Câu 6: Siêu phẳng $$\{x : a^T x = b\}$$ với $$a \neq 0$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) Chỉ là tập lồi</label>
                <label><input type="radio" name="q6" value="b"> B) Chỉ là tập affine</label>
                <label><input type="radio" name="q6" value="c"> C) Vừa là tập lồi vừa là tập affine</label>
                <label><input type="radio" name="q6" value="d"> D) Không phải tập lồi cũng không phải tập affine</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) Vừa là tập lồi vừa là tập affine</strong><br>
                Siêu phẳng thỏa mãn cả định nghĩa tập lồi và tập affine vì nó chứa toàn bộ đường thẳng đi qua bất kỳ hai điểm nào.
            </div>
        </div>

        <!-- Câu hỏi 7: Nửa không gian -->
        <div class="question" id="q7" style="display: none;">
            <h3>Câu 7: Nửa không gian $$\{x : a^T x \leq b\}$$ với $$a \neq 0$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) Tập lồi nhưng không phải tập affine</label>
                <label><input type="radio" name="q7" value="b"> B) Tập affine nhưng không phải tập lồi</label>
                <label><input type="radio" name="q7" value="c"> C) Vừa là tập lồi vừa là tập affine</label>
                <label><input type="radio" name="q7" value="d"> D) Không phải tập lồi cũng không phải tập affine</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Tập lồi nhưng không phải tập affine</strong><br>
                Nửa không gian là tập lồi vì chứa đoạn thẳng nối hai điểm bất kỳ, nhưng không phải tập affine vì không chứa toàn bộ đường thẳng.
            </div>
        </div>

        <!-- Câu hỏi 8: Hình cầu Euclidean -->
        <div class="question" id="q8" style="display: none;">
            <h3>Câu 8: Hình cầu Euclidean $$B(x_c, r) = \{x : \|x - x_c\|_2 \leq r\}$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) Tập lồi</label>
                <label><input type="radio" name="q8" value="b"> B) Tập affine</label>
                <label><input type="radio" name="q8" value="c"> C) Siêu phẳng</label>
                <label><input type="radio" name="q8" value="d"> D) Nửa không gian</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Tập lồi</strong><br>
                Hình cầu Euclidean là tập lồi vì đoạn thẳng nối hai điểm bất kỳ trong hình cầu cũng nằm trong hình cầu.
            </div>
        </div>

        <!-- Câu hỏi 9: Ellipsoid -->
        <div class="question" id="q9" style="display: none;">
            <h3>Câu 9: Ellipsoid $$\{x : (x-x_c)^T P^{-1} (x-x_c) \leq 1\}$$ với $$P \succ 0$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) Trường hợp đặc biệt của hình cầu</label>
                <label><input type="radio" name="q9" value="b"> B) Tập lồi tổng quát hóa hình cầu</label>
                <label><input type="radio" name="q9" value="c"> C) Không phải tập lồi</label>
                <label><input type="radio" name="q9" value="d"> D) Chỉ tồn tại trong 2D</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Tập lồi tổng quát hóa hình cầu</strong><br>
                Ellipsoid là tổng quát hóa của hình cầu Euclidean. Khi $$P = r^2 I$$, ellipsoid trở thành hình cầu.
            </div>
        </div>

        <!-- Câu hỏi 10: Đa diện -->
        <div class="question" id="q10" style="display: none;">
            <h3>Câu 10: Đa diện được định nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) Giao của các hình cầu</label>
                <label><input type="radio" name="q10" value="b"> B) Giao của các bất đẳng thức và đẳng thức tuyến tính</label>
                <label><input type="radio" name="q10" value="c"> C) Hợp của các nửa không gian</label>
                <label><input type="radio" name="q10" value="d"> D) Tích của các tập lồi</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Giao của các bất đẳng thức và đẳng thức tuyến tính</strong><br>
                Đa diện có dạng $$\{x : a_i^T x \leq b_i, c_j^T x = d_j\}$$, là giao của các nửa không gian và siêu phẳng.
            </div>
        </div>

        <!-- Câu hỏi 11: Đơn hình -->
        <div class="question" id="q11" style="display: none;">
            <h3>Câu 11: Đơn hình trong không gian $$n$$ chiều được tạo từ:</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) $$n$$ điểm độc lập affine</label>
                <label><input type="radio" name="q11" value="b"> B) $$n+1$$ điểm độc lập affine</label>
                <label><input type="radio" name="q11" value="c"> C) $$2n$$ điểm</label>
                <label><input type="radio" name="q11" value="d"> D) Vô hạn điểm</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$n+1$$ điểm độc lập affine</strong><br>
                Đơn hình trong không gian $$n$$ chiều cần $$n+1$$ điểm độc lập affine: điểm (0D), đoạn thẳng (1D), tam giác (2D), tứ diện (3D).
            </div>
        </div>

        <!-- Câu hỏi 12: Hình cầu chuẩn -->
        <div class="question" id="q12" style="display: none;">
            <h3>Câu 12: Hình cầu chuẩn $$\{x : \|x - x_c\| \leq r\}$$ là tập lồi khi:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) Với mọi chuẩn</label>
                <label><input type="radio" name="q12" value="b"> B) Chỉ với chuẩn Euclidean</label>
                <label><input type="radio" name="q12" value="c"> C) Với p-chuẩn khi $$p \geq 1$$</label>
                <label><input type="radio" name="q12" value="d"> D) Chỉ khi $$p = 2$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) Với p-chuẩn khi $$p \geq 1$$</strong><br>
                Hình cầu chuẩn là tập lồi khi sử dụng p-chuẩn với $$p \geq 1$$. Điều kiện $$p \geq 1$$ đảm bảo tính lồi của chuẩn.
            </div>
        </div>

        <!-- Câu hỏi 13: Định lý siêu phẳng phân tách -->
        <div class="question" id="q13" style="display: none;">
            <h3>Câu 13: Định lý siêu phẳng phân tách phát biểu rằng:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) Hai tập lồi bất kỳ đều có thể phân tách bằng siêu phẳng</label>
                <label><input type="radio" name="q13" value="b"> B) Hai tập lồi rời rạc có thể phân tách bằng siêu phẳng</label>
                <label><input type="radio" name="q13" value="c"> C) Mọi tập lồi đều có siêu phẳng hỗ trợ</label>
                <label><input type="radio" name="q13" value="d"> D) Siêu phẳng luôn chia không gian thành hai phần bằng nhau</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Hai tập lồi rời rạc có thể phân tách bằng siêu phẳng</strong><br>
                Định lý siêu phẳng phân tách áp dụng cho hai tập lồi rời rạc (không giao nhau), không phải cho mọi cặp tập lồi.
            </div>
        </div>

        <!-- Câu hỏi 14: Siêu phẳng hỗ trợ -->
        <div class="question" id="q14" style="display: none;">
            <h3>Câu 14: Siêu phẳng hỗ trợ tại điểm $$x_0$$ trên biên của tập lồi $$C$$ thỏa mãn:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) $$a^T x \geq a^T x_0$$ với mọi $$x \in C$$</label>
                <label><input type="radio" name="q14" value="b"> B) $$a^T x \leq a^T x_0$$ với mọi $$x \in C$$</label>
                <label><input type="radio" name="q14" value="c"> C) $$a^T x = a^T x_0$$ với mọi $$x \in C$$</label>
                <label><input type="radio" name="q14" value="d"> D) $$a^T x > a^T x_0$$ với mọi $$x \in C$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$a^T x \leq a^T x_0$$ với mọi $$x \in C$$</strong><br>
                Siêu phẳng hỗ trợ $$\{x : a^T x = a^T x_0\}$$ "hỗ trợ" tập $$C$$ tại $$x_0$$, với $$C$$ nằm trong nửa không gian $$a^T x \leq a^T x_0$$.
            </div>
        </div>

        <!-- Câu hỏi 15: Phân tách nghiêm ngặt -->
        <div class="question" id="q15" style="display: none;">
            <h3>Câu 15: Phân tách nghiêm ngặt giữa hai tập $$C$$ và $$D$$ có nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) $$a^T x \leq b$$ với $$x \in C$$ và $$a^T x \geq b$$ với $$x \in D$$</label>
                <label><input type="radio" name="q15" value="b"> B) $$a^T x < b$$ với $$x \in C$$ và $$a^T x > b$$ với $$x \in D$$</label>
                <label><input type="radio" name="q15" value="c"> C) $$a^T x = b$$ với $$x \in C \cup D$$</label>
                <label><input type="radio" name="q15" value="d"> D) Khoảng cách giữa $$C$$ và $$D$$ lớn hơn 0</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$a^T x < b$$ với $$x \in C$$ và $$a^T x > b$$ với $$x \in D$$</strong><br>
                Phân tách nghiêm ngặt yêu cầu bất đẳng thức nghiêm ngặt (< và >), không chỉ ≤ và ≥.
            </div>
        </div>

        <!-- Câu hỏi 16: Bao lồi -->
        <div class="question" id="q16" style="display: none;">
            <h3>Câu 16: Bao lồi của tập $$S$$ là:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) Tập lồi nhỏ nhất chứa $$S$$</label>
                <label><input type="radio" name="q16" value="b"> B) Tập lồi lớn nhất trong $$S$$</label>
                <label><input type="radio" name="q16" value="c"> C) Giao của tất cả tập lồi chứa $$S$$</label>
                <label><input type="radio" name="q16" value="d"> D) Cả A và C đều đúng</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Cả A và C đều đúng</strong><br>
                Bao lồi vừa là tập lồi nhỏ nhất chứa $$S$$, vừa là giao của tất cả các tập lồi chứa $$S$$. Hai định nghĩa này tương đương.
            </div>
        </div>

        <!-- Câu hỏi 17: Polytope -->
        <div class="question" id="q17" style="display: none;">
            <h3>Câu 17: Polytope là:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Đa diện bất kỳ</label>
                <label><input type="radio" name="q17" value="b"> B) Đa diện bị chặn</label>
                <label><input type="radio" name="q17" value="c"> C) Đa diện không bị chặn</label>
                <label><input type="radio" name="q17" value="d"> D) Đa diện có vô hạn đỉnh</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Đa diện bị chặn</strong><br>
                Polytope là thuật ngữ đặc biệt dành cho đa diện bị chặn (bounded polyhedron).
            </div>
        </div>

        <!-- Câu hỏi 18: Đơn hình xác suất -->
        <div class="question" id="q18" style="display: none;">
            <h3>Câu 18: Đơn hình xác suất trong $$\mathbb{R}^n$$ được định nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) $$\{x : x \geq 0, \sum x_i = 1\}$$</label>
                <label><input type="radio" name="q18" value="b"> B) $$\{x : x \geq 0, \sum x_i \leq 1\}$$</label>
                <label><input type="radio" name="q18" value="c"> C) $$\{x : \|x\| = 1\}$$</label>
                <label><input type="radio" name="q18" value="d"> D) $$\{x : \|x\| \leq 1\}$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\{x : x \geq 0, \sum x_i = 1\}$$</strong><br>
                Đơn hình xác suất là tập hợp các vector xác suất: các thành phần không âm và tổng bằng 1.
            </div>
        </div>

        <!-- Câu hỏi 19: Tính chất hình học -->
        <div class="question" id="q19" style="display: none;">
            <h3>Câu 19: Tập affine có thể được hiểu như tập hợp của:</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) Nhiều đường thẳng</label>
                <label><input type="radio" name="q19" value="b"> B) Nhiều đoạn thẳng</label>
                <label><input type="radio" name="q19" value="c"> C) Nhiều tia</label>
                <label><input type="radio" name="q19" value="d"> D) Nhiều điểm rời rạc</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Nhiều đường thẳng</strong><br>
                Tập affine được hình thành bằng cách tập hợp nhiều đường thẳng, tập lồi bằng nhiều đoạn thẳng, và hình nón bằng nhiều tia.
            </div>
        </div>

        <!-- Câu hỏi 20: Ứng dụng thực tế -->
        <div class="question" id="q20" style="display: none;">
            <h3>Câu 20: Trong tối ưu hóa, siêu phẳng phân tách được sử dụng chủ yếu trong:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Tính toán gradient</label>
                <label><input type="radio" name="q20" value="b"> B) Phân loại và machine learning</label>
                <label><input type="radio" name="q20" value="c"> C) Tính tích phân</label>
                <label><input type="radio" name="q20" value="d"> D) Giải phương trình vi phân</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Phân loại và machine learning</strong><br>
                Siêu phẳng phân tách là cơ sở cho nhiều thuật toán phân loại như SVM, được sử dụng rộng rãi trong machine learning.
            </div>
        </div>

        <!-- Câu hỏi 21: Kiểm tra tập lồi thực tế -->
        <div class="question" id="q21" style="display: none;">
            <h3>Câu 21: Tập $$S = \{(x,y) : x^2 + y^2 \leq 1\}$$ (hình tròn đơn vị) có phải là tập lồi không?</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) Có, vì thỏa mãn định nghĩa tập lồi</label>
                <label><input type="radio" name="q21" value="b"> B) Không, vì có biên cong</label>
                <label><input type="radio" name="q21" value="c"> C) Không, vì không phải đa giác</label>
                <label><input type="radio" name="q21" value="d"> D) Chỉ lồi khi bán kính = 1</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Có, vì thỏa mãn định nghĩa tập lồi</strong><br>
                Hình tròn (và hình cầu) luôn là tập lồi. Đoạn thẳng nối hai điểm bất kỳ trong hình tròn đều nằm hoàn toàn trong hình tròn.
            </div>
        </div>

        <!-- Câu hỏi 22: Tổ hợp lồi thực hành -->
        <div class="question" id="q22" style="display: none;">
            <h3>Câu 22: Cho ba điểm $$A(0,0), B(2,0), C(1,2)$$. Điểm nào sau đây thuộc tổ hợp lồi của chúng?</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) $$(1,1)$$</label>
                <label><input type="radio" name="q22" value="b"> B) $$(3,1)$$</label>
                <label><input type="radio" name="q22" value="c"> C) $$(-1,0)$$</label>
                <label><input type="radio" name="q22" value="d"> D) $$(2,3)$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$(1,1)$$</strong><br>
                Tổ hợp lồi của ba điểm tạo thành tam giác. Điểm $$(1,1)$$ nằm trong tam giác với đỉnh $$A, B, C$$.<br>
                Có thể viết $$(1,1) = 0.25A + 0.25B + 0.5C$$ với các hệ số không âm và tổng bằng 1.
            </div>
        </div>

        <!-- Câu hỏi 23: Siêu phẳng thực tế -->
        <div class="question" id="q23" style="display: none;">
            <h3>Câu 23: Siêu phẳng $$\{x : 2x_1 + 3x_2 = 6\}$$ trong $$\mathbb{R}^2$$ đi qua điểm nào?</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) $$(0,2)$$ và $$(3,0)$$</label>
                <label><input type="radio" name="q23" value="b"> B) $$(1,1)$$ và $$(2,2)$$</label>
                <label><input type="radio" name="q23" value="c"> C) $$(0,0)$$ và $$(1,1)$$</label>
                <label><input type="radio" name="q23" value="d"> D) $$(2,3)$$ và $$(6,0)$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$(0,2)$$ và $$(3,0)$$</strong><br>
                Kiểm tra: $$2(0) + 3(2) = 6$$ ✓ và $$2(3) + 3(0) = 6$$ ✓<br>
                Đây là đường thẳng cắt trục $$y$$ tại $$(0,2)$$ và trục $$x$$ tại $$(3,0)$$.
            </div>
        </div>

        <!-- Câu hỏi 24: Nón lồi -->
        <div class="question" id="q24" style="display: none;">
            <h3>Câu 24: Tập $$K = \{(x,y) : x \geq 0, y \geq 0, y \leq x\}$$ có phải là nón lồi không?</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) Có, vì đóng dưới phép nhân với số dương và cộng</label>
                <label><input type="radio" name="q24" value="b"> B) Không, vì không chứa gốc tọa độ</label>
                <label><input type="radio" name="q24" value="c"> C) Không, vì không đối xứng</label>
                <label><input type="radio" name="q24" value="d"> D) Chỉ là nón, không lồi</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Có, vì đóng dưới phép nhân với số dương và cộng</strong><br>
                Tập này là góc phần tư thứ nhất dưới đường $$y = x$$, chứa gốc tọa độ và thỏa mãn định nghĩa nón lồi.
            </div>
        </div>

        <!-- Câu hỏi 25: Phép toán bảo toàn tính lồi -->
        <div class="question" id="q25" style="display: none;">
            <h3>Câu 25: Cho hai tập lồi $$C_1$$ và $$C_2$$. Tập nào sau đây chắc chắn là lồi?</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) $$C_1 \cap C_2$$ (giao)</label>
                <label><input type="radio" name="q25" value="b"> B) $$C_1 \cup C_2$$ (hợp)</label>
                <label><input type="radio" name="q25" value="c"> C) $$C_1 \setminus C_2$$ (hiệu)</label>
                <label><input type="radio" name="q25" value="d"> D) $$C_1 \triangle C_2$$ (hiệu đối xứng)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$C_1 \cap C_2$$ (giao)</strong><br>
                Giao của hai tập lồi luôn là tập lồi. Hợp của hai tập lồi không nhất thiết lồi (ví dụ: hai hình tròn rời nhau).
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
    background: linear-gradient(90deg, #9C27B0, #673AB7);
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
    border-color: #9C27B0;
    background-color: #f3e5f5;
}

.options input[type="radio"] {
    margin-right: 12px;
    margin-top: 2px;
    transform: scale(1.2);
    flex-shrink: 0;
}

.options label.selected {
    border-color: #9C27B0;
    background-color: #e8d5e8;
}

.explanation {
    margin-top: 20px;
    padding: 15px;
    background-color: #f3e5f5;
    border-left: 4px solid #9C27B0;
    border-radius: 4px;
    font-size: 0.95em;
    line-height: 1.5;
}

.explanation strong {
    color: #7B1FA2;
}

#quiz-navigation {
    text-align: center;
    margin: 30px 0;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

#quiz-navigation button {
    background: #9C27B0;
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 6px;
    cursor: pointer;
    font-size: 1em;
    transition: background-color 0.2s ease;
}

#quiz-navigation button:hover:not(:disabled) {
    background: #7B1FA2;
}

#quiz-navigation button:disabled {
    background: #cccccc;
    cursor: not-allowed;
}

#quiz-results {
    text-align: center;
    padding: 30px;
    background: #f3e5f5;
    border-radius: 8px;
    border: 2px solid #9C27B0;
}

#score-display {
    font-size: 1.5em;
    font-weight: bold;
    margin: 20px 0;
    color: #7B1FA2;
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
    q1: 'b', q2: 'b', q3: 'b', q4: 'b', q5: 'b',
    q6: 'c', q7: 'a', q8: 'a', q9: 'b', q10: 'b',
    q11: 'b', q12: 'c', q13: 'b', q14: 'b', q15: 'b',
    q16: 'd', q17: 'b', q18: 'a', q19: 'a', q20: 'b',
    q21: 'a', q22: 'a', q23: 'a', q24: 'a', q25: 'a'
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
            ${scorePercentage >= 80 ? '🎉 Xuất sắc! Bạn đã nắm vững hình học lồi!' : 
              scorePercentage >= 60 ? '👍 Khá tốt! Hãy ôn lại một số khái niệm hình học.' : 
              scorePercentage >= 40 ? '📚 Cần ôn tập thêm về tập lồi và siêu phẳng.' : '💪 Hãy đọc lại lý thuyết về hình học lồi!'}
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
    if (window.MathJax) {
        MathJax.typesetPromise();
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
