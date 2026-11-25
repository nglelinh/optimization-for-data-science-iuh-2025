---
layout: post
title: 14-11 Bài tập trắc nghiệm - Phương Pháp Newton
chapter: '14'
order: 19
owner: GitHub Copilot
lang: vi
categories:
- chapter14
lesson_type: quiz
redirect_from:
  - /contents/vi/chapter14/14_10_Quiz_Newton_Method/
---

Chương 14 chứa rất nhiều khái niệm sắc nét nhưng cũng dễ nhầm lẫn nếu chỉ đọc lướt: phương pháp Newton có vuông góc với đường đồng mức không? Vì sao Newton decrement $$\lambda(x)$$ lại bất biến affine trong khi $$\|\nabla f(x)\|_2$$ thì không? Điều kiện nào biến một hàm thành tự hài hòa, và vì sao cận hội tụ lại xuất hiện $$\log_2\log_2(1/\epsilon)$$?

Bộ câu hỏi trắc nghiệm này sẽ kiểm tra toàn diện phản xạ của bạn về tối ưu hóa bậc hai — từ công thức cơ bản, tính chất hình học, tìm kiếm đường backtracking, phân tích hai pha hội tụ, hàm tự hài hòa, đến Quasi-Newton. Hãy rà nhanh bản đồ bốn nhóm bẫy kinh điển trước khi bắt đầu chọn đáp án.

## Kiến thức cần nhớ: Bốn nhóm bẫy trắc nghiệm thường gặp ở Chương 14

- **Hình học bước Newton vs. Gradient Descent:** Nhớ rằng hướng Newton **không** nhất thiết vuông góc đường đồng mức (trừ khi $$\nabla f(x)$$ là vectơ riêng của $$\nabla^2 f(x)$$), nhưng luôn tạo góc nhọn với $$-\nabla f(x)$$ miễn là $$\nabla^2 f(x) \succ 0$$.
- **Tính bất biến affine:** Cả bước cập nhật Newton, Newton decrement $$\lambda(x)$$, lẫn cận hội tụ của hàm tự hài hòa đều **bất biến affine**; ngược lại, Gradient Descent, $$\|\nabla f(x)\|_2$$ và các hằng số $$m, L, M$$ thì **không**.
- **Hội tụ cục bộ vs. toàn cục:** Newton thuần túy ($$t = 1$$) chỉ hội tụ **cục bộ** (có thể phân kỳ khi xa nghiệm); muốn hội tụ **toàn cục** trên hàm lồi phải ghép thêm tìm kiếm đường backtracking (Newton có giảm chấn).
- **Hàm tự hài hòa và độ phức tạp:** Kiểm tra đúng số mũ $$3/2$$ và hằng số $$2$$ ($$\vert f''' \vert \le 2(f'')^{3/2}$$), nhớ hàm $$-\log x$$ là tự hài hòa còn $$e^x$$ trên $$\mathbb{R}$$ thì không, và chi phí mỗi bước Newton đặc là $$O(n^3)$$ với bộ nhớ $$O(n^2)$$.

### Giải thích: Giải mẫu một câu hỏi bẫy về phép nhân vô hướng hàm tự hài hòa

**Câu hỏi mẫu:** Cho $$f(x) = -\log x$$ (đã biết là hàm tự hài hòa trên $$x > 0$$). Xét hai hàm mới $$g_1(x) = 4 f(x)$$ và $$g_2(x) = \frac{1}{4} f(x)$$. Hàm nào còn là hàm tự hài hòa?

1. **Nhắc lại điều kiện kiểm tra:** $$\vert h'''(x) \vert \le 2 (h''(x))^{3/2}$$.
2. **Kiểm tra $$g_1(x) = 4(-\log x)$$:**
   - $$g_1''(x) = \frac{4}{x^2}$$, $$\vert g_1'''(x) \vert = \frac{8}{x^3}$$.
   - Vế phải: $$2\left(\frac{4}{x^2}\right)^{3/2} = 2 \cdot \frac{8}{x^3} = \frac{16}{x^3} \ge \frac{8}{x^3} = \vert g_1'''(x) \vert$$. → **$$g_1$$ VẪN tự hài hòa!**
3. **Kiểm tra $$g_2(x) = \frac{1}{4}(-\log x)$$:**
   - $$g_2''(x) = \frac{1}{4x^2}$$, $$\vert g_2'''(x) \vert = \frac{1}{2x^3}$$.
   - Vế phải: $$2\left(\frac{1}{4x^2}\right)^{3/2} = 2 \cdot \frac{1}{8x^3} = \frac{1}{4x^3} < \frac{1}{2x^3} = \vert g_2'''(x) \vert$$. → **$$g_2$$ KHÔNG còn tự hài hòa!**
4. **Quy tắc nhớ nhanh cho phòng thi:** Nhân hàm tự hài hòa với $$c \ge 1$$ thì giữ nguyên tính tự hài hòa; nhân với $$0 < c < 1$$ có thể làm mất tính tự hài hòa!

---

## 📚 Ôn tập lý thuyết

Trước khi làm bài tập trắc nghiệm, hãy ôn lại các khái niệm chính của chương này:

### ⚡ **Phương pháp Newton (Newton Method)**

#### **Từ phương pháp bậc nhất đến bậc hai**
- **Phương pháp bậc nhất:** Gradient descent sử dụng đạo hàm bậc nhất $$
abla f(x)$$.
- **Phương pháp bậc hai:** Phương pháp Newton sử dụng thêm đạo hàm bậc hai $$
abla^2 f(x)$$ (ma trận Hessian).
- **Ý tưởng:** Thay vì xấp xỉ ma trận Hessian bằng $$rac{1}{t}I$$, ta tính trực tiếp $$
abla^2 f(x)$$.

#### **Bài toán**
$$\min_x f(x)$$ với $$f$$ lồi, khả vi hai lần và $$	ext{dom}(f) = \mathbb{R}^n$$.

#### **Công thức cập nhật Newton**
$$x^{(k)} = x^{(k-1)} - (
abla^2 f(x^{(k-1)}))^{-1} 
abla f(x^{(k-1)})$$

**So sánh với Gradient Descent:**
- **Gradient Descent:** $$x^{(k)} = x^{(k-1)} - t 
abla f(x^{(k-1)})$$
- **Newton:** $$x^{(k)} = x^{(k-1)} - (
abla^2 f(x^{(k-1)}))^{-1} 
abla f(x^{(k-1)})$$

### 🔍 **Diễn giải và tính chất**

#### **Diễn giải bước Newton**
**Hướng Newton:** $$\Delta x_{nt} = -(
abla^2 f(x))^{-1} 
abla f(x)$$

**Ý nghĩa hình học:**
- Cực tiểu hóa xấp xỉ bậc hai: $$f(x) + 
abla f(x)^T (y-x) + rac{1}{2}(y-x)^T 
abla^2 f(x) (y-x)$$
- Điểm cực tiểu: $$y^* = x - (
abla^2 f(x))^{-1} 
abla f(x)$$

#### **Liên hệ với bài toán tìm nghiệm**
Phương pháp Newton cho bài toán tối ưu tương đương với phương pháp Newton–Raphson giải phương trình $$
abla f(x) = 0$$.

**Newton–Raphson:** $$x^{(k)} = x^{(k-1)} - rac{g(x^{(k-1)})}{g'(x^{(k-1)})}$$

**Khi $$g(x) = 
abla f(x)$$:** $$x^{(k)} = x^{(k-1)} - (
abla^2 f(x^{(k-1)}))^{-1} 
abla f(x^{(k-1)})$$

#### **Tính bất biến affine**
**Tính chất:** Phương pháp Newton bất biến dưới các phép biến đổi affine khả nghịch của hệ tọa độ.

**Nếu:** $$g(y) = f(Ay + b)$$ với $$A$$ không suy biến,  
**Thì:** các bước Newton của $$g$$ và $$f$$ tương đương nhau qua phép biến đổi đó.

**Ý nghĩa:** Thuật toán không bị ảnh hưởng bởi số điều kiện của hệ tọa độ như gradient descent.

### 📐 **Đại lượng giảm Newton (Newton Decrement)**

#### **Định nghĩa**
$$\lambda(x) = (
abla f(x)^T (
abla^2 f(x))^{-1} 
abla f(x))^{1/2}$$

#### **Ý nghĩa**
1. **Chất lượng xấp xỉ bậc hai:** $$rac{1}{2}\lambda^2(x) = f(x) - \min_y \hat{f}(y)$$, trong đó $$\hat{f}(y)$$ là xấp xỉ bậc hai của $$f$$ tại $$x$$. Đại lượng $$rac{1}{2}\lambda^2(x)$$ là ước lượng cho khoảng cách tối ưu $$f(x) - f^*$$ (dựa trên xấp xỉ bậc hai, không phải cận trên chặt trong mọi trường hợp).
2. **Độ dài bước Newton:** $$\lambda(x) = \lVert \Delta x_{nt} 
Vert_{
abla^2 f(x)}$$ (theo chuẩn cảm sinh bởi ma trận Hessian).
3. **Khoảng cách Mahalanobis:** Đo độ lớn bước Newton tính từ điểm hiện tại trong hệ đo xác định bởi Hessian.

#### **Các biểu thức tương đương**
- $$\lambda(x) = (\Delta x_{nt}^T 
abla^2 f(x) \Delta x_{nt})^{1/2}$$
- $$
abla f(x)^T \Delta x_{nt} = -\lambda^2(x)$$

#### **Tính bất biến affine**
Đại lượng giảm Newton cũng bất biến affine: $$\lambda_g(y) = \lambda_f(x)$$.

### 🎯 **Phương pháp Newton có giảm chấn (Damped Newton Method)**

#### **Hạn chế của phương pháp Newton thuần túy**
- **Không đảm bảo hội tụ toàn cục:** Giá trị $$f(x^{(k)})$$ có thể tăng.
- **Chỉ hội tụ cục bộ:** Cần điểm khởi tạo đủ gần điểm tối ưu.

#### **Tìm kiếm đường backtracking**
**Thuật toán:**
1. Tính hướng Newton: $$v = -(
abla^2 f(x))^{-1} 
abla f(x)$$.
2. **Backtracking:** Với tham số $$0 < lpha \le 1/2$$, $$0 < eta < 1$$:
   ```
   t = 1
   while f(x + tv) > f(x) + α t ∇f(x)^T v:
       t = βt
   ```
3. **Cập nhật:** $$x^+ = x + tv$$.

#### **Điều kiện Armijo**
$$f(x + tv) \le f(x) + lpha t 
abla f(x)^T v$$

với $$
abla f(x)^T v = -\lambda^2(x) < 0$$.

### 📊 **Phân tích hội tụ**

#### **Các giả thiết**
1. **$$
abla f$$ liên tục Lipschitz:** $$\lVert 
abla f(x) - 
abla f(y) 
Vert_2 \le L \lVert x-y 
Vert_2$$
2. **Tính lồi mạnh:** $$mI \preceq 
abla^2 f(x) \preceq LI$$
3. **$$
abla^2 f$$ liên tục Lipschitz:** $$\lVert 
abla^2 f(x) - 
abla^2 f(y) 
Vert_2 \le M \lVert x-y 
Vert_2$$

#### **Hội tụ hai giai đoạn**
**Giai đoạn I — Giai đoạn giảm chấn (Damped phase):** $$\lVert 
abla f(x^{(k)}) 
Vert_2 \ge \eta$$
$$f(x^{(k+1)}) - f(x^{(k)}) \le -\gamma$$

**Giai đoạn II — Giai đoạn thuần túy (Pure phase):** $$\lVert 
abla f(x^{(k)}) 
Vert_2 < \eta$$
$$rac{M}{2m^2} \lVert 
abla f(x^{(k+1)}) 
Vert_2 \le \left(rac{M}{2m^2} \lVert 
abla f(x^{(k)}) 
Vert_2
ight)^2$$

#### **Tốc độ hội tụ**
**Giai đoạn I:** Giá trị hàm giảm ít nhất một lượng cố định $$\gamma$$ ở mỗi bước:
$$f(x^{(k)}) - f^* \le (f(x^{(0)}) - f^*) - \gamma k$$

**Giai đoạn II:** Hội tụ bậc hai:
$$f(x^{(k)}) - f^* \le rac{2m^3}{M^2}\left(rac{1}{2}
ight)^{2^{k-k_0+1}}$$

#### **Tổng độ phức tạp vòng lặp**
$$rac{f(x^{(0)}) - f^*}{\gamma} + \log\log\left(rac{\epsilon_0}{\epsilon}
ight)$$

**Ước lượng thực hành:** $$rac{f(x^{(0)}) - f^*}{\gamma} + 6$$.

### 🌟 **Hàm tự hài hòa (Self-Concordant Functions)**

#### **Động lực**
Phân tích hội tụ cổ điển có hai hạn chế:
1. **Khó xác định hằng số:** Các hằng số $$L, m, M$$ thường không biết trước trong thực tế.
2. **Không bất biến affine:** Cận hội tụ phụ thuộc vào hệ tọa độ.

#### **Định nghĩa**
Hàm $$f$$ là **tự hài hòa** nếu với trường hợp một biến:
$$|f'''(x)| \le 2(f''(x))^{3/2}$$

**Trường hợp nhiều biến:** $$\lvert D^3 f(x)[h,h,h] 
vert \le 2(h^T 
abla^2 f(x) h)^{3/2}$$.

#### **Tính chất chính**
1. **Bất biến affine:** Tính tự hài hòa được bảo toàn qua phép biến đổi affine.
2. **Không phụ thuộc hằng số $$L, m, M$$:** Phân tích hội tụ không cần các hằng số này.
3. **Liên hệ với hàm chắn:** Các hàm chắn logarit của ràng buộc affine là hàm tự hài hòa.

#### **Hội tụ với hàm tự hài hòa**
Phân tích chỉ dựa vào đại lượng giảm Newton $$\lambda(x)$$:
- **Giai đoạn giảm chấn:** $$\lambda(x) \ge \eta$$
- **Giai đoạn thuần túy:** $$\lambda(x) < \eta$$

### 🔄 **So sánh phương pháp Newton và Gradient Descent**

| Khía cạnh | Phương pháp Newton | Gradient Descent |
|--------|---------------|------------------|
| **Bộ nhớ** | $$O(n^2)$$ (lưu ma trận Hessian) | $$O(n)$$ (lưu vector gradient) |
| **Chi phí tính toán mỗi bước** | $$O(n^3)$$ (giải hệ tuyến tính) | $$O(n)$$ (phép toán vector) |
| **Tốc độ hội tụ** | Bậc hai (gần điểm tối ưu) | Tuyến tính |
| **Ảnh hưởng của số điều kiện** | Bất biến affine | Nhạy cảm với số điều kiện |
| **Độ ổn định số học** | Nhạy cảm hơn với sai số số học | Ổn định hơn |

#### **Ưu và nhược điểm của phương pháp Newton**
**Ưu điểm:**
- Hội tụ bậc hai khi gần điểm tối ưu.
- Bất biến affine, không phụ thuộc số điều kiện của hệ tọa độ.
- Cần ít vòng lặp, đặc biệt khi yêu cầu độ chính xác cao.

**Nhược điểm:**
- Chi phí mỗi bước cao: $$O(n^3)$$.
- Tốn bộ nhớ lưu trữ ma trận Hessian: $$O(n^2)$$.
- Nhạy cảm với sai số số học khi giải hệ với Hessian.

#### **Lựa chọn trong thực tế**
- **Số chiều $$n$$ nhỏ đến trung bình:** Phương pháp Newton thường hiệu quả hơn.
- **Số chiều $$n$$ lớn:** Nên dùng gradient descent hoặc các phương pháp quasi-Newton.
- **Cần độ chính xác cao hoặc bài toán có số điều kiện xấu:** Phương pháp Newton có lợi thế rõ rệt.

### 🛠️ **Lưu ý cài đặt**

#### **Tính bước Newton**
1. Lập ma trận Hessian $$H = 
abla^2 f(x)$$.
2. Giải hệ tuyến tính $$H \Delta x = -
abla f(x)$$.
3. Không tính nghịch đảo tường minh; dùng phân rã Cholesky, LU hoặc phương pháp gradient liên hợp (CG).

#### **Ổn định số học**
- Đảm bảo Hessian xác định dương (bổ sung điều chuẩn $$\epsilon I$$ nếu cần).
- Theo dõi số điều kiện $$\kappa(H)$$.
- Luôn dùng tìm kiếm đường backtracking để đảm bảo hội tụ toàn cục.

#### **Tiêu chí dừng**
1. Đại lượng giảm Newton: $$\lambda^2(x)/2 < \epsilon$$.
2. Chuẩn gradient: $$\lVert 
abla f(x) 
Vert_2 < \epsilon$$.
3. Độ giảm giá trị hàm: $$\lvert f(x^{(k)}) - f(x^{(k-1)}) 
vert < \epsilon$$.

### 🎯 **Trường hợp đặc biệt và mở rộng**

#### **Các phương pháp Quasi-Newton**
**Mục tiêu:** Tránh tính và phân rã ma trận Hessian chính xác.

**Công thức cập nhật BFGS:**
$$B_{k+1} = B_k + rac{y_k y_k^T}{y_k^T s_k} - rac{B_k s_k s_k^T B_k}{s_k^T B_k s_k}$$

với $$s_k = x_{k+1} - x_k$$ và $$y_k = 
abla f(x_{k+1}) - 
abla f(x_k)$$.

**L-BFGS:** Phiên bản bộ nhớ giới hạn cho các bài toán quy mô lớn.

#### **Phương pháp miền tin cậy (Trust Region)**
Thay thế tìm kiếm đường bằng bài toán con có ràng buộc bán kính $$\Delta$$:
$$\min_p f(x) + 
abla f(x)^T p + rac{1}{2}p^T 
abla^2 f(x) p \quad 	ext{với} \quad \lVert p 
Vert \le \Delta$$

### 💡 **Ví dụ minh họa**

#### **Hồi quy logistic**
- **Bài toán:** $$\min_eta \sum_{i=1}^n \log(1 + \exp(-y_i x_i^T eta))$$
- **Gradient:** $$
abla f(eta) = -\sum_{i=1}^n rac{y_i x_i}{1 + \exp(y_i x_i^T eta)}$$
- **Hessian:** $$
abla^2 f(eta) = \sum_{i=1}^n rac{\exp(y_i x_i^T eta)}{(1 + \exp(y_i x_i^T eta))^2} x_i x_i^T$$
- **Bước Newton:** Giải hệ $$
abla^2 f(eta) \Delta eta = -
abla f(eta)$$.

#### **Hàm bậc hai**
- **Bài toán:** $$f(x) = rac{1}{2}x^T Q x + b^T x + c$$ với $$Q \succ 0$$.
- **Bước Newton:** $$\Delta x = -Q^{-1}(Qx + b) = -(x + Q^{-1}b)$$.
- **Hội tụ trong 1 bước:** $$x^{(1)} = x^{(0)} - (x^{(0)} + Q^{-1}b) = -Q^{-1}b = x^*$$.

### 🎯 **Kết nối với các chương khác**

- **Từ các chương trước:** Gradient descent (Chương 06), điều kiện KKT (Chương 12) và ứng dụng đối ngẫu (Chương 13).
- **Hướng phát triển tiếp theo:** Phương pháp chắn (Chương 15), các phương pháp điểm trong, các phương pháp quasi-Newton (Chương 18) và phương pháp miền tin cậy.

### 💡 **Tóm tắt thực hành**

- **Nên dùng phương pháp Newton khi:** số chiều vừa phải (thường $$n \le 10^3$$), hàm mục tiêu trơn, cần độ chính xác cao hoặc bài toán có số điều kiện xấu.
- **Lỗi thường gặp:** Hessian suy biến tại điểm yên ngựa hoặc gần biên, chi phí tính đạo hàm bậc hai quá cao, điểm khởi tạo xa vùng hội tụ bậc hai, hoặc tính nghịch đảo ma trận tường minh gây khuếch đại sai số số học.
- **Các biến thể và lĩnh vực ứng dụng:** Newton điều chuẩn ($$H + \epsilon I$$), Levenberg–Marquardt, điều chuẩn bậc ba, Newton không chính xác (dùng CG), L-BFGS, Gauss–Newton, SQP, phương pháp điểm trong; ứng dụng trong hồi quy logistic, ước lượng hợp lý cực đại, mô hình tuyến tính tổng quát (IRLS), điều khiển tối ưu, xử lý tín hiệu và tối ưu danh mục đầu tư.

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

Bài tập trắc nghiệm này kiểm tra kiến thức về phương pháp Newton, bao gồm tối ưu bậc hai, phân tích hội tụ, tìm kiếm đường backtracking, hàm tự hài hòa và các phương pháp quasi-Newton.

---

<div id="quiz-container">
    <div id="quiz-header">
        <h2>🔢 Bài tập trắc nghiệm: Phương pháp Newton</h2>
        <div class="progress-bar">
            <div class="progress-fill" id="progress-fill" style="width: 4%"></div>
        </div>
        <div class="score-display" id="score-display">Câu hỏi: <span id="current-q">1</span> / <span id="total-q">25</span></div>
    </div>

    <div id="quiz-content">
        <!-- Câu hỏi 1: Newton method update -->
        <div class="question" id="q1" style="display: block;">
            <h3>Câu 1: Công thức cập nhật của phương pháp Newton thuần túy (không dùng tìm kiếm đường) là:</h3>
            <div class="options">
                <label><input type="radio" name="q1" value="a"> A) \(x^{(k+1)} = x^{(k)} - t_k 
abla f(x^{(k)})\)</label>
                <label><input type="radio" name="q1" value="b"> B) \(x^{(k+1)} = x^{(k)} - t_k [
abla^2 f(x^{(k)})]^{-1} 
abla f(x^{(k)})\)</label>
                <label><input type="radio" name="q1" value="c"> C) \(x^{(k+1)} = x^{(k)} - [
abla^2 f(x^{(k)})]^{-1} 
abla f(x^{(k)})\)</label>
                <label><input type="radio" name="q1" value="d"> D) \(x^{(k+1)} = x^{(k)} - 
abla^2 f(x^{(k)}) 
abla f(x^{(k)})\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) $$x^{(k+1)} = x^{(k)} - [
abla^2 f(x^{(k)})]^{-1} 
abla f(x^{(k)})$$</strong><br>
                Phương pháp Newton thuần túy dùng bước Newton đầy đủ với kích thước bước $$t = 1$$.
            </div>
        </div>

        <!-- Câu hỏi 2: Newton direction -->
        <div class="question" id="q2" style="display: none;">
            <h3>Câu 2: Hướng Newton \(\Delta x_{nt}\) được xác định bằng cách giải hệ phương trình:</h3>
            <div class="options">
                <label><input type="radio" name="q2" value="a"> A) \(
abla^2 f(x) \Delta x_{nt} = 
abla f(x)\)</label>
                <label><input type="radio" name="q2" value="b"> B) \(
abla^2 f(x) \Delta x_{nt} = -
abla f(x)\)</label>
                <label><input type="radio" name="q2" value="c"> C) \(
abla f(x) \Delta x_{nt} = -
abla^2 f(x)\)</label>
                <label><input type="radio" name="q2" value="d"> D) \(\Delta x_{nt} = -
abla f(x)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) $$
abla^2 f(x) \Delta x_{nt} = -
abla f(x)$$</strong><br>
                Hướng Newton được tìm bằng cách giải hệ phương trình tuyến tính với ma trận Hessian và vế phải là đối của gradient.
            </div>
        </div>

        <!-- Câu hỏi 3: Second-order method -->
        <div class="question" id="q3" style="display: none;">
            <h3>Câu 3: Phương pháp Newton được gọi là phương pháp bậc hai vì:</h3>
            <div class="options">
                <label><input type="radio" name="q3" value="a"> A) Sử dụng đạo hàm bậc hai (ma trận Hessian)</label>
                <label><input type="radio" name="q3" value="b"> B) Hội tụ trong 2 bước</label>
                <label><input type="radio" name="q3" value="c"> C) Cần 2 lần tính gradient</label>
                <label><input type="radio" name="q3" value="d"> D) Có tốc độ hội tụ bậc hai</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Sử dụng đạo hàm bậc hai (ma trận Hessian)</strong><br>
                Các phương pháp bậc hai sử dụng thông tin đạo hàm bậc hai (Hessian), khác với phương pháp bậc nhất chỉ dùng gradient.
            </div>
        </div>

        <!-- Câu hỏi 4: Convergence rate -->
        <div class="question" id="q4" style="display: none;">
            <h3>Câu 4: Tốc độ hội tụ cục bộ của phương pháp Newton là:</h3>
            <div class="options">
                <label><input type="radio" name="q4" value="a"> A) Tuyến tính (Linear)</label>
                <label><input type="radio" name="q4" value="b"> B) Siêu tuyến tính (Superlinear)</label>
                <label><input type="radio" name="q4" value="c"> C) Bậc hai (Quadratic)</label>
                <label><input type="radio" name="q4" value="d"> D) Bậc ba (Cubic)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) Bậc hai (Quadratic)</strong><br>
                Trong vùng lân cận điểm tối ưu, phương pháp Newton đạt hội tụ bậc hai: $$\lVert x^{(k+1)} - x^* 
Vert \leq C \lVert x^{(k)} - x^* 
Vert^2$$.
            </div>
        </div>

        <!-- Câu hỏi 5: Newton decrement -->
        <div class="question" id="q5" style="display: none;">
            <h3>Câu 5: Đại lượng giảm Newton (Newton decrement) \(\lambda(x)\) được định nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q5" value="a"> A) \(\lambda(x) = \sqrt{
abla f(x)^T [
abla^2 f(x)]^{-1} 
abla f(x)}\)</label>
                <label><input type="radio" name="q5" value="b"> B) \(\lambda(x) = 
abla f(x)^T [
abla^2 f(x)]^{-1} 
abla f(x)\)</label>
                <label><input type="radio" name="q5" value="c"> C) $$\lambda(x) = \lVert 
abla f(x) 
Vert$$</label>
                <label><input type="radio" name="q5" value="d"> D) $$\lambda(x) = \lVert 
abla^2 f(x) 
Vert$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$\lambda(x) = \sqrt{
abla f(x)^T [
abla^2 f(x)]^{-1} 
abla f(x)}$$</strong><br>
                Đại lượng giảm Newton là tiêu chí dừng tự nhiên và bất biến affine cho phương pháp Newton.
            </div>
        </div>

        <!-- Câu hỏi 6: Affine invariance -->
        <div class="question" id="q6" style="display: none;">
            <h3>Câu 6: Tính chất bất biến affine của phương pháp Newton có nghĩa là:</h3>
            <div class="options">
                <label><input type="radio" name="q6" value="a"> A) Quỹ đạo lặp không thay đổi dưới các phép biến đổi tọa độ affine khả nghịch</label>
                <label><input type="radio" name="q6" value="b"> B) Chỉ hoạt động với các hàm affine</label>
                <label><input type="radio" name="q6" value="c"> C) Yêu cầu phải có ràng buộc affine</label>
                <label><input type="radio" name="q6" value="d"> D) Chỉ đạt hội tụ tuyến tính</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Quỹ đạo lặp không thay đổi dưới các phép biến đổi tọa độ affine khả nghịch</strong><br>
                Phương pháp Newton không phụ thuộc hệ tọa độ: nếu biến đổi $$x \mapsto Ax + b$$ (với $$A$$ khả nghịch), các bước Newton biến đổi tương ứng theo đúng phép biến đổi đó.
            </div>
        </div>

        <!-- Câu hỏi 7: Backtracking line search -->
        <div class="question" id="q7" style="display: none;">
            <h3>Câu 7: Tìm kiếm đường backtracking trong phương pháp Newton sử dụng:</h3>
            <div class="options">
                <label><input type="radio" name="q7" value="a"> A) Điều kiện Armijo dọc theo hướng Newton</label>
                <label><input type="radio" name="q7" value="b"> B) Tìm kiếm đường chính xác (exact line search)</label>
                <label><input type="radio" name="q7" value="c"> C) Kích thước bước cố định</label>
                <label><input type="radio" name="q7" value="d"> D) Tìm kiếm tỷ lệ vàng (golden section search)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Điều kiện Armijo dọc theo hướng Newton</strong><br>
                Tìm kiếm đường backtracking kiểm tra điều kiện giảm đủ (Armijo): $$f(x + t\Delta x_{nt}) \leq f(x) + lpha t 
abla f(x)^T \Delta x_{nt}$$.
            </div>
        </div>

        <!-- Câu hỏi 8: When Newton method fails -->
        <div class="question" id="q8" style="display: none;">
            <h3>Câu 8: Phương pháp Newton thuần túy có thể gặp sự cố hoặc không hội tụ khi:</h3>
            <div class="options">
                <label><input type="radio" name="q8" value="a"> A) Ma trận Hessian không xác định dương</label>
                <label><input type="radio" name="q8" value="b"> B) Điểm khởi tạo ở quá xa điểm tối ưu</label>
                <label><input type="radio" name="q8" value="c"> C) Ma trận Hessian suy biến</label>
                <label><input type="radio" name="q8" value="d"> D) Tất cả các trường hợp trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các trường hợp trên</strong><br>
                Phương pháp Newton cần Hessian xác định dương để đảm bảo hướng giảm, không xác định khi Hessian suy biến, và có thể phân kỳ nếu xuất phát quá xa nghiệm.
            </div>
        </div>

        <!-- Câu hỏi 9: Self-concordant functions -->
        <div class="question" id="q9" style="display: none;">
            <h3>Câu 9: Lớp hàm tự hài hòa (self-concordant functions) quan trọng vì:</h3>
            <div class="options">
                <label><input type="radio" name="q9" value="a"> A) Phân tích hội tụ không phụ thuộc vào các hằng số $$L, m, M$$</label>
                <label><input type="radio" name="q9" value="b"> B) Phân tích hội tụ có tính bất biến affine</label>
                <label><input type="radio" name="q9" value="c"> C) Xuất hiện tự nhiên trong các hàm chắn của phương pháp điểm trong</label>
                <label><input type="radio" name="q9" value="d"> D) Tất cả các lý do trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các lý do trên</strong><br>
                Hàm tự hài hòa loại bỏ sự phụ thuộc vào các hằng số khó ước lượng, giữ nguyên tính bất biến affine trong phân tích hội tụ và là cơ sở lý thuyết cho các hàm chắn logarit.
            </div>
        </div>

        <!-- Câu hỏi 10: Self-concordance definition -->
        <div class="question" id="q10" style="display: none;">
            <h3>Câu 10: Hàm lồi \(f\) là hàm tự hài hòa nếu thỏa mãn:</h3>
            <div class="options">
                <label><input type="radio" name="q10" value="a"> A) \(|f'''(x)[h,h,h]| \leq 2(f''(x)[h,h])^{3/2}\)</label>
                <label><input type="radio" name="q10" value="b"> B) \(f''(x) \succ 0\)</label>
                <label><input type="radio" name="q10" value="c"> C) \(f\) là hàm lồi</label>
                <label><input type="radio" name="q10" value="d"> D) \(f\) là hàm trơn</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$|f'''(x)[h,h,h]| \leq 2(f''(x)[h,h])^{3/2}$$</strong><br>
                Điều kiện tự hài hòa chặn độ lớn đạo hàm bậc ba theo đạo hàm bậc hai dọc theo mọi hướng $$h$$.
            </div>
        </div>

        <!-- Câu hỏi 11: Quasi-Newton methods -->
        <div class="question" id="q11" style="display: none;">
            <h3>Câu 11: Các phương pháp quasi-Newton khác phương pháp Newton ở điểm nào?</h3>
            <div class="options">
                <label><input type="radio" name="q11" value="a"> A) Không cần tính ma trận Hessian chính xác</label>
                <label><input type="radio" name="q11" value="b"> B) Dùng ma trận xấp xỉ cho Hessian (hoặc nghịch đảo Hessian)</label>
                <label><input type="radio" name="q11" value="c"> C) Chi phí tính toán mỗi bước thấp hơn</label>
                <label><input type="radio" name="q11" value="d"> D) Tất cả các điểm trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các điểm trên</strong><br>
                Các phương pháp quasi-Newton xấp xỉ Hessian từ thông tin gradient để giảm chi phí tính toán mỗi vòng lặp.
            </div>
        </div>

        <!-- Câu hỏi 12: BFGS update -->
        <div class="question" id="q12" style="display: none;">
            <h3>Câu 12: Phương pháp BFGS (dạng thông dụng) trực tiếp cập nhật xấp xỉ của:</h3>
            <div class="options">
                <label><input type="radio" name="q12" value="a"> A) Chỉ đường chéo của ma trận Hessian</label>
                <label><input type="radio" name="q12" value="b"> B) Ma trận nghịch đảo của Hessian</label>
                <label><input type="radio" name="q12" value="c"> C) Vector gradient</label>
                <label><input type="radio" name="q12" value="d"> D) Giá trị hàm mục tiêu</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Ma trận nghịch đảo của Hessian</strong><br>
                Ở dạng thường dùng, BFGS cập nhật trực tiếp ma trận xấp xỉ $$H_k$$ của nghịch đảo Hessian để tránh giải hệ tuyến tính (cũng có dạng tương đương cập nhật xấp xỉ $$B_k$$ của chính Hessian).
            </div>
        </div>

        <!-- Câu hỏi 13: Computational complexity -->
        <div class="question" id="q13" style="display: none;">
            <h3>Câu 13: Chi phí tính toán tổng quát cho mỗi vòng lặp của phương pháp Newton (với $$n$$ biến) là:</h3>
            <div class="options">
                <label><input type="radio" name="q13" value="a"> A) \(O(n)\)</label>
                <label><input type="radio" name="q13" value="b"> B) \(O(n^2)\)</label>
                <label><input type="radio" name="q13" value="c"> C) \(O(n^3)\)</label>
                <label><input type="radio" name="q13" value="d"> D) \(O(n^4)\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: C) $$O(n^3)$$</strong><br>
                Phương pháp Newton cần lưu trữ $$O(n^2)$$ cho ma trận Hessian và tốn $$O(n^3)$$ phép tính để giải hệ tuyến tính $$H \Delta x = -g$$.
            </div>
        </div>

        <!-- Câu hỏi 14: Damped Newton method -->
        <div class="question" id="q14" style="display: none;">
            <h3>Câu 14: Phương pháp Newton có giảm chấn (damped Newton method) sử dụng:</h3>
            <div class="options">
                <label><input type="radio" name="q14" value="a"> A) Kích thước bước nhỏ cố định</label>
                <label><input type="radio" name="q14" value="b"> B) Tìm kiếm đường dọc theo hướng Newton</label>
                <label><input type="radio" name="q14" value="c"> C) Ma trận Hessian hiệu chỉnh cố định</label>
                <label><input type="radio" name="q14" value="d"> D) Hướng của gradient descent</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: B) Tìm kiếm đường dọc theo hướng Newton</strong><br>
                Phương pháp Newton có giảm chấn kết hợp hướng Newton với tìm kiếm đường backtracking để đảm bảo hội tụ toàn cục.
            </div>
        </div>

        <!-- Câu hỏi 15: Trust region vs line search -->
        <div class="question" id="q15" style="display: none;">
            <h3>Câu 15: Phương pháp Newton miền tin cậy (trust region) khác phương pháp Newton tìm kiếm đường ở chỗ:</h3>
            <div class="options">
                <label><input type="radio" name="q15" value="a"> A) Giới hạn độ dài bước đi trong một miền tin cậy</label>
                <label><input type="radio" name="q15" value="b"> B) Có thể thay đổi cả hướng bước đi thay vì chỉ thu nhỏ kích thước bước</label>
                <label><input type="radio" name="q15" value="c"> C) Chọn bước bằng cách giải bài toán con với ràng buộc $$\lVert p 
Vert \leq \Delta$$</label>
                <label><input type="radio" name="q15" value="d"> D) Tất cả các điểm trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các điểm trên</strong><br>
                Phương pháp miền tin cậy cực tiểu hóa mô hình bậc hai trong vùng bán kính $$\Delta$$, qua đó đồng thời kiểm soát cả độ dài lẫn hướng bước đi.
            </div>
        </div>

        <!-- Câu hỏi 16: Newton method for root finding -->
        <div class="question" id="q16" style="display: none;">
            <h3>Câu 16: Phương pháp Newton tìm nghiệm cho phương trình một biến \(g(x) = 0\) có công thức lặp:</h3>
            <div class="options">
                <label><input type="radio" name="q16" value="a"> A) \(x^{(k+1)} = x^{(k)} - rac{g(x^{(k)})}{g'(x^{(k)})}\)</label>
                <label><input type="radio" name="q16" value="b"> B) \(x^{(k+1)} = x^{(k)} - g(x^{(k)})\)</label>
                <label><input type="radio" name="q16" value="c"> C) \(x^{(k+1)} = x^{(k)} - g'(x^{(k)})\)</label>
                <label><input type="radio" name="q16" value="d"> D) \(x^{(k+1)} = x^{(k)} + rac{g(x^{(k)})}{g'(x^{(k)})}\)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$x^{(k+1)} = x^{(k)} - rac{g(x^{(k)})}{g'(x^{(k)})}$$</strong><br>
                Phương pháp Newton cho tối ưu hóa chính là áp dụng công thức tìm nghiệm này cho phương trình $$
abla f(x) = 0$$.
            </div>
        </div>

        <!-- Câu hỏi 17: Hessian modification -->
        <div class="question" id="q17" style="display: none;">
            <h3>Câu 17: Khi ma trận Hessian không xác định dương, ta có thể xử lý bằng cách:</h3>
            <div class="options">
                <label><input type="radio" name="q17" value="a"> A) Thêm điều chuẩn: \(H + \lambda I\)</label>
                <label><input type="radio" name="q17" value="b"> B) Điều chỉnh các giá trị riêng âm (lấy trị tuyệt đối hoặc cắt ngưỡng dương)</label>
                <label><input type="radio" name="q17" value="c"> C) Dùng phân rã Cholesky hiệu chỉnh (modified Cholesky)</label>
                <label><input type="radio" name="q17" value="d"> D) Tất cả các phương pháp trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các phương pháp trên</strong><br>
                Cả ba kỹ thuật (thêm điều chuẩn, hiệu chỉnh giá trị riêng, phân rã Cholesky hiệu chỉnh) đều giúp thu được ma trận xác định dương để đảm bảo hướng giảm.
            </div>
        </div>

        <!-- Câu hỏi 18: L-BFGS -->
        <div class="question" id="q18" style="display: none;">
            <h3>Câu 18: Ưu điểm của thuật toán L-BFGS (Limited-memory BFGS) là:</h3>
            <div class="options">
                <label><input type="radio" name="q18" value="a"> A) Yêu cầu bộ nhớ \(O(n)\) thay vì \(O(n^2)\)</label>
                <label><input type="radio" name="q18" value="b"> B) Phù hợp với các bài toán tối ưu quy mô lớn</label>
                <label><input type="radio" name="q18" value="c"> C) Không cần lưu trữ ma trận đầy đủ cỡ \(n 	imes n\)</label>
                <label><input type="radio" name="q18" value="d"> D) Tất cả các ưu điểm trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các ưu điểm trên</strong><br>
                L-BFGS chỉ lưu một số lượng nhỏ các cặp vector lịch sử (thường từ 5 đến 20 cặp) thay vì ma trận đầy đủ, nên rất phù hợp cho bài toán nhiều biến.
            </div>
        </div>

        <!-- Câu hỏi 19: Newton method applications -->
        <div class="question" id="q19" style="display: none;">
            <h3>Câu 19: Phương pháp Newton được ứng dụng trong lĩnh vực nào sau đây?</h3>
            <div class="options">
                <label><input type="radio" name="q19" value="a"> A) Các phương pháp điểm trong (interior-point methods)</label>
                <label><input type="radio" name="q19" value="b"> B) Huấn luyện mô hình học máy và mạng nơ-ron (các biến thể bậc hai)</label>
                <label><input type="radio" name="q19" value="c"> C) Ước lượng hợp lý cực đại (maximum likelihood estimation)</label>
                <label><input type="radio" name="q19" value="d"> D) Tất cả các ứng dụng trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các ứng dụng trên</strong><br>
                Phương pháp Newton và các biến thể của nó được dùng rộng rãi trong phương pháp điểm trong, học máy và ước lượng thống kê.
            </div>
        </div>

        <!-- Câu hỏi 20: Comparison with first-order methods -->
        <div class="question" id="q20" style="display: none;">
            <h3>Câu 20: So với các phương pháp bậc nhất, phương pháp Newton có đặc điểm:</h3>
            <div class="options">
                <label><input type="radio" name="q20" value="a"> A) Cần ít vòng lặp hơn nhưng chi phí mỗi vòng lặp cao hơn</label>
                <label><input type="radio" name="q20" value="b"> B) Hội tụ bậc hai (cục bộ) so với hội tụ tuyến tính</label>
                <label><input type="radio" name="q20" value="c"> C) Bất biến affine so với phụ thuộc hệ tọa độ</label>
                <label><input type="radio" name="q20" value="d"> D) Tất cả các đặc điểm trên</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: D) Tất cả các đặc điểm trên</strong><br>
                Phương pháp Newton đánh đổi chi phí mỗi bước cao hơn để đạt số vòng lặp ít hơn, hội tụ bậc hai gần nghiệm và tính bất biến affine.
            </div>
        </div>

        <!-- Câu hỏi 21: Thực hành -->
        <div class="question" id="q21" style="display: none;">
            <h3>Câu 21: Phương pháp Newton sử dụng thông tin nào của hàm mục tiêu?</h3>
            <div class="options">
                <label><input type="radio" name="q21" value="a"> A) Cả gradient và ma trận Hessian</label>
                <label><input type="radio" name="q21" value="b"> B) Chỉ gradient</label>
                <label><input type="radio" name="q21" value="c"> C) Chỉ ma trận Hessian</label>
                <label><input type="radio" name="q21" value="d"> D) Chỉ giá trị hàm số</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Cả gradient và ma trận Hessian</strong><br>
                Công thức cập nhật Newton: $$x^{(k+1)} = x^{(k)} - [
abla^2 f(x^{(k)})]^{-1} 
abla f(x^{(k)})$$.
            </div>
        </div>

        <!-- Câu hỏi 22: Thực hành -->
        <div class="question" id="q22" style="display: none;">
            <h3>Câu 22: Tốc độ hội tụ của phương pháp Newton gần điểm tối ưu là:</h3>
            <div class="options">
                <label><input type="radio" name="q22" value="a"> A) Bậc hai (Quadratic)</label>
                <label><input type="radio" name="q22" value="b"> B) Tuyến tính (Linear)</label>
                <label><input type="radio" name="q22" value="c"> C) Dưới tuyến tính (Sublinear)</label>
                <label><input type="radio" name="q22" value="d"> D) Bậc ba (Cubic)</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Bậc hai (Quadratic)</strong><br>
                Phương pháp Newton hội tụ bậc hai khi ở gần nghiệm với Hessian khả nghịch và liên tục Lipschitz.
            </div>
        </div>

        <!-- Câu hỏi 23: Thực hành -->
        <div class="question" id="q23" style="display: none;">
            <h3>Câu 23: Các phương pháp quasi-Newton khác phương pháp Newton ở chỗ:</h3>
            <div class="options">
                <label><input type="radio" name="q23" value="a"> A) Xấp xỉ ma trận Hessian thay vì tính chính xác</label>
                <label><input type="radio" name="q23" value="b"> B) Không dùng gradient</label>
                <label><input type="radio" name="q23" value="c"> C) Chỉ áp dụng cho hàm tuyến tính</label>
                <label><input type="radio" name="q23" value="d"> D) Luôn chậm hơn trong mọi bài toán</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Xấp xỉ ma trận Hessian thay vì tính chính xác</strong><br>
                Các phương pháp quasi-Newton (như BFGS, L-BFGS) xây dựng xấp xỉ Hessian từ thông tin gradient qua các bước lặp.
            </div>
        </div>

        <!-- Câu hỏi 24: Thực hành -->
        <div class="question" id="q24" style="display: none;">
            <h3>Câu 24: Công thức cập nhật BFGS (dạng thông dụng) cập nhật:</h3>
            <div class="options">
                <label><input type="radio" name="q24" value="a"> A) Ma trận xấp xỉ nghịch đảo Hessian</label>
                <label><input type="radio" name="q24" value="b"> B) Vector gradient</label>
                <label><input type="radio" name="q24" value="c"> C) Điểm lặp hiện tại</label>
                <label><input type="radio" name="q24" value="d"> D) Kích thước bước</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) Ma trận xấp xỉ nghịch đảo Hessian</strong><br>
                BFGS cập nhật ma trận xấp xỉ $$H_k pprox [
abla^2 f]^{-1}$$ dựa trên hiệu vị trí và hiệu gradient giữa hai bước liên tiếp.
            </div>
        </div>

        <!-- Câu hỏi 25: Thực hành -->
        <div class="question" id="q25" style="display: none;">
            <h3>Câu 25: Với hàm $$f(x) = x^2$$, một bước Newton xuất phát từ $$x_0 = 2$$ cho:</h3>
            <div class="options">
                <label><input type="radio" name="q25" value="a"> A) $$x_1 = 0$$</label>
                <label><input type="radio" name="q25" value="b"> B) $$x_1 = 1$$</label>
                <label><input type="radio" name="q25" value="c"> C) $$x_1 = -2$$</label>
                <label><input type="radio" name="q25" value="d"> D) $$x_1 = 2$$</label>
            </div>
            <div class="explanation" style="display: none;">
                <strong>Đáp án đúng: A) $$x_1 = 0$$</strong><br>
                Ta có $$
abla f(2) = 4$$ và $$
abla^2 f(2) = 2$$, nên $$x_1 = 2 - 4/2 = 0$$.
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
    q1: 'c', q2: 'b', q3: 'a', q4: 'c', q5: 'a',
    q6: 'a', q7: 'a', q8: 'd', q9: 'd', q10: 'a',
    q11: 'd', q12: 'b', q13: 'c', q14: 'b', q15: 'd',
    q16: 'a', q17: 'd', q18: 'd', q19: 'd', q20: 'd'
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
        message = '🌟 Xuất sắc! Bạn đã thành thạo Newton method và second-order optimization!';
    } else if (percentage >= 80) {
        message = '👍 Rất tốt! Bạn hiểu tốt về Newton method và convergence analysis.';
    } else if (percentage >= 70) {
        message = '📚 Khá ổn! Hãy xem lại self-concordance và quasi-Newton methods.';
    } else if (percentage >= 60) {
        message = '💪 Cần cải thiện! Ôn lại Newton direction và backtracking line search.';
    } else {
        message = '📖 Hãy học lại từ đầu về Newton method nhé!';
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
