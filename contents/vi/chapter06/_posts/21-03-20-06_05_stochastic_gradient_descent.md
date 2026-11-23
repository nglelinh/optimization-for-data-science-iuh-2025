---
layout: post
title: 06-05 Stochastic gradient descent
chapter: '06'
order: 17
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
lesson_type: required
---

<script src="../../../public/js/script.js"></script>
<script src="https://d3js.org/d3.v7.min.js"></script>

## Động lực: Thách thức của Dữ liệu Lớn

Hãy hình dung bài toán huấn luyện một mô hình học máy trên hàng triệu điểm dữ liệu. Gradient descent truyền thống yêu cầu tính gradient trên **toàn bộ** tập dữ liệu trước khi thực hiện một bước cập nhật duy nhất. Cách làm này nhanh chóng trở nên tốn kém cả về thời gian tính toán lẫn bộ nhớ khi quy mô dữ liệu lớn.

**Câu hỏi đặt ra**: Liệu ta có thể cập nhật tham số dần dần bằng cách chỉ xét một điểm dữ liệu tại mỗi bước hay không?

## Nền tảng Toán học

Xét bài toán cực tiểu hóa tổng của nhiều hàm thành phần:

$$ \begin{equation}
\min_x f(x) = \min_x \sum_{i=1}^m f_i(x)
\end{equation} $$

**Ý nghĩa thực tế**: Trong học máy, $$f_i(x)$$ thường là hàm mất mát trên mẫu huấn luyện thứ $$i$$, còn $$x$$ là vector tham số của mô hình.

### Batch Gradient Descent (Phương pháp Toàn tập)

Gradient của tổng bằng tổng các gradient thành phần:
$$\nabla f(x) = \nabla \sum_{i=1}^m f_i(x) = \sum_{i=1}^m \nabla f_i(x)$$

Quy tắc cập nhật của batch gradient descent là:
$$ \begin{equation}
x^{(k)} = x^{(k-1)} - t_k \cdot \sum_{i=1}^{m} \nabla f_i (x^{(k-1)}), \quad k=1,2,3,\dots
\end{equation} $$

**Chi phí tính toán**: $$O(m)$$ lần tính gradient trên mỗi bước lặp, trong đó $$m$$ là số hàm thành phần (hoặc số mẫu dữ liệu).

## Stochastic Gradient Descent: Giải pháp Thay thế Hiệu quả

**Ý tưởng cốt lõi**: Thay vì tính gradient của toàn bộ $$m$$ hàm thành phần, Stochastic Gradient Descent (SGD) chỉ sử dụng **một** hàm tại mỗi lần lặp:

$$ \begin{equation}
x^{(k)} = x^{(k-1)} - t_k \cdot \nabla f_{i_k} (x^{(k-1)}), \quad i_k \in \{1,2,\dots,m\}
\end{equation} $$

**Chi phí tính toán**: Chỉ $$O(1)$$ lần tính gradient cho mỗi lần lặp, giảm đáng kể chi phí trên mỗi bước cập nhật.

### Trực quan hóa Tương tác: So sánh GD và SGD theo Từng Bước

<div id="gd-sgd-comparison" style="margin: 20px 0;">
    <!-- Parameter Controls -->
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; margin-bottom: 15px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; background-color: #f9f9f9;">
        <div>
            <label for="learning-rate">Tốc độ học: </label>
            <input type="range" id="learning-rate" min="0.01" max="0.5" step="0.01" value="0.1">
            <span id="lr-value">0.1</span>
        </div>
        <div>
            <label for="num-functions">Số hàm thành phần (m): </label>
            <input type="range" id="num-functions" min="3" max="10" step="1" value="5">
            <span id="m-value">5</span>
        </div>
        <div>
            <label for="animation-speed">Tốc độ hoạt ảnh: </label>
            <input type="range" id="animation-speed" min="1" max="10" step="1" value="5">
            <span id="speed-value">5</span>
        </div>
    </div>
    
    <!-- Execution Mode Selection -->
    <div style="margin-bottom: 15px; padding: 10px; border: 1px solid #ddd; border-radius: 5px; background-color: #f0f8ff;">
        <h4 style="margin: 0 0 10px 0;">Chế độ chạy:</h4>
        <div style="display: flex; gap: 15px;">
            <label><input type="radio" name="exec-mode" value="auto" checked> Tự động chạy</label>
            <label><input type="radio" name="exec-mode" value="manual"> Chạy từng bước</label>
        </div>
    </div>
    
    <!-- Control Buttons -->
    <div style="display: flex; gap: 10px; margin-bottom: 15px; flex-wrap: wrap;">
        <button id="start-gd" style="background-color: #4CAF50; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Chạy Gradient Descent</button>
        <button id="start-sgd" style="background-color: #FF9800; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Chạy SGD</button>
        <button id="pause-resume" style="background-color: #2196F3; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;" disabled>Tạm dừng</button>
        <button id="step-forward" style="background-color: #9C27B0; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;" disabled>Bước tiếp</button>
        <button id="reset-demo" style="background-color: #f44336; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Đặt lại</button>
    </div>
    
    <!-- Algorithm Status -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 15px;">
        <div style="padding: 10px; border: 1px solid #4CAF50; border-radius: 5px; background-color: #f1f8e9;">
            <h4 style="margin: 0 0 5px 0; color: #4CAF50;">Trạng thái Gradient Descent</h4>
            <p id="gd-detailed-info" style="margin: 0; font-size: 14px;">Sẵn sàng</p>
        </div>
        <div style="padding: 10px; border: 1px solid #FF9800; border-radius: 5px; background-color: #fff8e1;">
            <h4 style="margin: 0 0 5px 0; color: #FF9800;">Trạng thái SGD</h4>
            <p id="sgd-detailed-info" style="margin: 0; font-size: 14px;">Sẵn sàng</p>
        </div>
    </div>
    
    <!-- Visualization Plots -->
    <div style="display: flex; gap: 20px; justify-content: center;">
        <div style="text-align: center;">
            <h4>Gradient Descent (toàn bộ dữ liệu)</h4>
            <svg id="gd-plot" width="350" height="350" style="border: 1px solid #ddd;"></svg>
            <div style="margin-top: 10px; padding: 8px; background-color: #f5f5f5; border-radius: 4px;">
                <p id="gd-info" style="margin: 0; font-weight: bold;">Số vòng lặp: 0, Chi phí: 0</p>
                <p id="gd-gradient-info" style="margin: 5px 0 0 0; font-size: 12px; color: #666;">Gradient: [0, 0]</p>
            </div>
        </div>
        <div style="text-align: center;">
            <h4>Gradient Descent ngẫu nhiên (SGD)</h4>
            <svg id="sgd-plot" width="350" height="350" style="border: 1px solid #ddd;"></svg>
            <div style="margin-top: 10px; padding: 8px; background-color: #f5f5f5; border-radius: 4px;">
                <p id="sgd-info" style="margin: 0; font-weight: bold;">Số vòng lặp: 0, Chi phí: 0</p>
                <p id="sgd-gradient-info" style="margin: 5px 0 0 0; font-size: 12px; color: #666;">Hàm được chọn: -, Gradient: [0, 0]</p>
            </div>
        </div>
    </div>
    
    <!-- Progress Visualization -->
    <div style="margin-top: 20px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; background-color: #fafafa;">
        <h4>Quá trình hội tụ</h4>
        <div style="display: flex; gap: 20px;">
            <div style="flex: 1;">
                <p><strong>Tiến trình GD:</strong></p>
                <div style="width: 100%; background-color: #e0e0e0; border-radius: 10px; height: 20px;">
                    <div id="gd-progress" style="width: 0%; background-color: #4CAF50; height: 100%; border-radius: 10px; transition: width 0.3s;"></div>
                </div>
            </div>
            <div style="flex: 1;">
                <p><strong>Tiến trình SGD:</strong></p>
                <div style="width: 100%; background-color: #e0e0e0; border-radius: 10px; height: 20px;">
                    <div id="sgd-progress" style="width: 0%; background-color: #FF9800; height: 100%; border-radius: 10px; transition: width 0.3s;"></div>
                </div>
            </div>
        </div>
    </div>
</div>

### Các Chiến lược Chọn Mẫu trong SGD

Chỉ số hàm $$i_k$$ có thể được lựa chọn theo hai quy tắc phổ biến:

#### 1. Quy tắc Tuần hoàn (Cyclic Rule)
**Thứ tự**: $$i_k = 1,2,\dots,m, 1,2,\dots,m, \ldots$$
- **Ưu điểm**: Có tính tất định, đảm bảo mọi hàm thành phần đều được duyệt qua đều đặn.
- **Nhược điểm**: Có thể chịu ảnh hưởng của chu kỳ lặp cố định nếu thứ tự dữ liệu có quy luật.

#### 2. Quy tắc Ngẫu nhiên (Randomized Rule)
**Thứ tự**: Chọn $$i_k$$ ngẫu nhiên đều từ $$\{1,2,\dots,m\}$$.
- **Ưu điểm**: Tránh chu kỳ cố định và có đảm bảo lý thuyết về hội tụ tốt hơn.
- **Nhược điểm**: Trong ngắn hạn, một số hàm thành phần có thể được chọn nhiều lần hơn các hàm khác.

**Trong thực tế**: Quy tắc ngẫu nhiên (hoặc xáo trộn ngẫu nhiên tập dữ liệu ở đầu mỗi epoch) được ưu tiên sử dụng vì mang lại tính chất hội tụ tốt hơn.

## Phân tích Hội tụ: Lý thuyết và Thực tế

### So sánh Công thức Cập nhật

**Batch GD (một epoch)**:
$$x^{(k+1)} = x^{(k)} - t_k \cdot \sum_{i=1}^{m} \nabla f_i (x^{(k)})$$

**SGD (một epoch với quy tắc tuần hoàn, kích thước bước cố định $$t_k$$ trong epoch)**:
$$x^{(k+m)} = x^{(k)} - t_k \cdot \sum_{i=1}^{m} \nabla f_i (x^{(k+i-1)})$$

### Phân tích Quy tắc Tuần hoàn của SGD

Hãy xem xét chi tiết điều gì diễn ra trong một epoch hoàn chỉnh của SGD theo quy tắc tuần hoàn.

**Epoch là gì?** Một epoch tương ứng với việc thuật toán duyệt qua toàn bộ $$m$$ hàm thành phần đúng một lần.

**Trình tự cập nhật trong một epoch:**
- Xuất phát tại điểm $$x^{(k)}$$.
- **Bước 1**: Dùng $$f_1$$, tính $$\nabla f_1(x^{(k)})$$, cập nhật sang $$x^{(k+1)}$$.
- **Bước 2**: Dùng $$f_2$$, tính $$\nabla f_2(x^{(k+1)})$$, cập nhật sang $$x^{(k+2)}$$.
- **Bước 3**: Dùng $$f_3$$, tính $$\nabla f_3(x^{(k+2)})$$, cập nhật sang $$x^{(k+3)}$$.
- ...
- **Bước $$m$$**: Dùng $$f_m$$, tính $$\nabla f_m(x^{(k+m-1)})$$, cập nhật sang $$x^{(k+m)}$$.

**Các bước cập nhật riêng lẻ:**
$$\begin{align}
x^{(k+1)} &= x^{(k)} - t_k \nabla f_1(x^{(k)}) \\
x^{(k+2)} &= x^{(k+1)} - t_k \nabla f_2(x^{(k+1)}) \\
x^{(k+3)} &= x^{(k+2)} - t_k \nabla f_3(x^{(k+2)}) \\
&\vdots \\
x^{(k+m)} &= x^{(k+m-1)} - t_k \nabla f_m(x^{(k+m-1)})
\end{align}$$

**Gộp các bước cập nhật:**
Thay thế liên tiếp các biểu thức trên, ta thu được:
$$x^{(k+m)} = x^{(k)} - t_k \left[ \nabla f_1(x^{(k)}) + \nabla f_2(x^{(k+1)}) + \cdots + \nabla f_m(x^{(k+m-1)}) \right]$$

Viết gọn lại:
$$x^{(k+m)} = x^{(k)} - t_k \cdot \sum_{i=1}^{m} \nabla f_i (x^{(k+i-1)})$$

**Điểm cốt lõi:** Mỗi gradient $$\nabla f_i$$ được tính tại một vị trí **khác nhau** $$x^{(k+i-1)}$$, thay vì cùng tính tại điểm đầu $$x^{(k)}$$.

**Độ lệch giữa hướng cập nhật của SGD và Batch GD**:
$$\sum_{i=1}^{m}[ \nabla f_i (x^{(k+i-1)}) - \nabla f_i (x^{(k)})]$$

Biểu thức này đo mức độ sai lệch của quỹ đạo SGD so với bước cập nhật của batch GD. Nếu các hàm thành phần biến thiên chậm cục bộ (gradient liên tục Lipschitz), độ lệch này nhỏ và SGD hành xử gần với batch GD.

### Ví dụ Cụ thể với $$m = 3$$ Hàm Thành phần

Xét trường hợp $$m = 3$$ để thấy rõ sự khác biệt.

**Điểm xuất phát:** $$x^{(k)} = [1, 2]$$

**Hàm cụ thể (để kiểm tra bằng số):** khớp đường thẳng $$y \approx w s + c$$ qua ba điểm $$(s_i, y_i) = (0, 1), (1, 3), (2, 2)$$. Với $$x = [w, c]$$, đặt
$$f_i(x) = \tfrac{1}{2}(w s_i + c - y_i)^2, \qquad \nabla f_i(x) = (w s_i + c - y_i)\,[s_i, 1].$$
Tại $$x^{(k)} = [1, 2]$$: $$\nabla f_1 = [0, 1]$$, $$\nabla f_2 = [0, 0]$$, $$\nabla f_3 = [4, 2]$$ và $$f(x^{(k)}) = 2.5$$. Nghiệm tối ưu là $$x^\star = [0.5, 1.5]$$ với $$f(x^\star) = 0.75$$.

**Quá trình SGD theo quy tắc tuần hoàn:**
1. **Dùng $$f_1$$**: Tính $$\nabla f_1(x^{(k)}) = \nabla f_1([1,2])$$, cập nhật:
   $$x^{(k+1)} = x^{(k)} - t_k \nabla f_1(x^{(k)}) = [1,2] - t_k \nabla f_1([1,2])$$
2. **Dùng $$f_2$$**: Tính $$\nabla f_2(x^{(k+1)})$$ tại vị trí **mới**, cập nhật:
   $$x^{(k+2)} = x^{(k+1)} - t_k \nabla f_2(x^{(k+1)})$$
3. **Dùng $$f_3$$**: Tính $$\nabla f_3(x^{(k+2)})$$ tại vị trí **mới nhất**, cập nhật:
   $$x^{(k+3)} = x^{(k+2)} - t_k \nabla f_3(x^{(k+2)})$$

**Kết quả SGD sau một epoch:**
$$x^{(k+3)} = x^{(k)} - t_k[\nabla f_1(x^{(k)}) + \nabla f_2(x^{(k+1)}) + \nabla f_3(x^{(k+2)})]$$

**So sánh với Batch GD:**
$$x^{(k+1)} = x^{(k)} - t_k[\nabla f_1(x^{(k)}) + \nabla f_2(x^{(k)}) + \nabla f_3(x^{(k)})]$$

**Với các hàm cụ thể ở trên và $$t_k = 0.15$$:**

| Phương pháp | Bước | Gradient dùng | Điểm mới | $$f$$ |
|-------------|------|---------------|----------|-------|
| Batch GD | 1 | $$[4, 3]$$ (tổng tại $$[1, 2]$$) | $$[0.4, 1.55]$$ | 0.76375 |
| SGD | 1 | $$\nabla f_1([1, 2]) = [0, 1]$$ | $$[1, 1.85]$$ | 2.08375 |
| SGD | 2 | $$\nabla f_2([1, 1.85]) = [-0.15, -0.15]$$ | $$[1.0225, 1.8725]$$ | 2.2245 |
| SGD | 3 | $$\nabla f_3([1.0225, 1.8725]) = [3.835, 1.9175]$$ | $$[0.44725, 1.584875]$$ | 0.7543 |

Tổng các gradient SGD đã dùng là $$[3.685, 2.7675]$$ thay vì $$[4, 3]$$. Hiệu $$[-0.315, -0.2325]$$ chính là độ lệch ở công thức trên. Để ý rằng bước 2 làm $$f$$ *tăng*: gradient của một hàm $$f_i$$ không phải lúc nào cũng là hướng giảm của cả tổng.

**Sự khác biệt then chốt:**
- **Batch GD**: Toàn bộ gradient được tính tại **cùng một điểm** $$x^{(k)}$$.
- **SGD**: Mỗi gradient được tính tại một điểm **cập nhật liên tiếp** dọc theo quỹ đạo tối ưu.

Vì vậy, SGD thường giảm mất mát rất nhanh ở giai đoạn đầu nhưng dao động nhiều hơn khi tiến gần tới điểm cực tiểu.

### Tính chất Hội tụ

<div id="convergence-analysis" style="margin: 20px 0;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
        <div style="border: 1px solid #ddd; padding: 15px; border-radius: 5px;">
            <h4>Batch Gradient Descent</h4>
            <ul>
                <li><strong>Hướng di chuyển</strong>: Luôn theo hướng giảm dốc nhất chính xác</li>
                <li><strong>Hội tụ</strong>: Mượt mà, giảm đơn điệu</li>
                <li><strong>Tốc độ</strong>: Chậm hơn trên mỗi epoch, nhưng ổn định</li>
                <li><strong>Bộ nhớ</strong>: Cần nạp toàn bộ tập dữ liệu để tính gradient đầy đủ</li>
            </ul>
        </div>
        <div style="border: 1px solid #ddd; padding: 15px; border-radius: 5px;">
            <h4>Gradient Descent ngẫu nhiên (SGD)</h4>
            <ul>
                <li><strong>Hướng di chuyển</strong>: Có nhiễu, xấp xỉ hướng giảm</li>
                <li><strong>Hội tụ</strong>: Có dao động, nhưng tiến triển nhanh ở giai đoạn đầu</li>
                <li><strong>Tốc độ</strong>: Nhanh hơn rõ rệt trên mỗi epoch với tập dữ liệu lớn</li>
                <li><strong>Bộ nhớ</strong>: Chỉ cần xử lý từng mẫu một</li>
            </ul>
        </div>
    </div>
</div>

### Đảm bảo Lý thuyết

**Điều kiện liên tục Lipschitz**: Nếu mỗi $$\nabla f_i(x)$$ liên tục Lipschitz với hằng số $$L$$:
$$\|\nabla f_i(x) - \nabla f_i(y)\| \leq L \|x - y\|$$

thì SGD hội tụ về cùng nghiệm tối ưu với batch GD khi tốc độ học thỏa mãn các điều kiện giảm dần phù hợp.

**Quan sát thực tế**:
- SGD hoạt động hiệu quả trong **giai đoạn đầu** (khi còn ở xa nghiệm tối ưu).
- SGD gặp khó khăn hơn trong **giai đoạn tinh chỉnh** (khi ở gần nghiệm tối ưu) do nhiễu gradient.

## Mini-Batch Gradient Descent: Dung hòa Hai Phương pháp

Một phương án trung gian giữa batch GD và SGD là sử dụng các **mini-batch** kích thước $$b$$:

$$x^{(k)} = x^{(k-1)} - t_k \cdot \frac{1}{b} \sum_{i \in \mathcal{B}_k} \nabla f_i (x^{(k-1)})$$

trong đó $$\mathcal{B}_k$$ là tập con gồm $$b$$ chỉ số được chọn ngẫu nhiên.

**Tổng hay trung bình?** Ở trên, batch GD dùng **tổng** $$\sum_{i=1}^m \nabla f_i$$, tức gradient của $$f = \sum_i f_i$$. Công thức mini-batch dùng **trung bình** trên $$b$$ chỉ số. Đây là ước lượng không chệch của gradient trung bình $$\frac{1}{m}\sum_{i=1}^m \nabla f_i$$, cách viết quen thuộc trong học máy khi ta cực tiểu hóa mất mát trung bình. Hai cách viết chỉ khác nhau một hằng số, và hằng số này được gộp vào kích thước bước. Nếu muốn ước lượng tổng thì dùng $$\frac{m}{b}\sum_{i \in \mathcal{B}_k} \nabla f_i$$. Với $$b = m$$ và cách viết trung bình, mini-batch GD chính là batch GD với bước $$t_k/m$$.

<div id="minibatch-comparison" style="margin: 20px 0;">
    <h4>So sánh: Batch GD, Mini-batch GD và SGD</h4>
    <table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
        <thead>
            <tr style="background-color: #f5f5f5;">
                <th style="border: 1px solid #ddd; padding: 10px;">Phương pháp</th>
                <th style="border: 1px solid #ddd; padding: 10px;">Kích thước lô (Batch Size)</th>
                <th style="border: 1px solid #ddd; padding: 10px;">Chi phí / Cập nhật</th>
                <th style="border: 1px solid #ddd; padding: 10px;">Hành vi hội tụ</th>
                <th style="border: 1px solid #ddd; padding: 10px;">Mức dùng bộ nhớ</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="border: 1px solid #ddd; padding: 10px;"><strong>Batch GD</strong></td>
                <td style="border: 1px solid #ddd; padding: 10px;">$$m$$ (toàn bộ tập dữ liệu)</td>
                <td style="border: 1px solid #ddd; padding: 10px;">$$O(m)$$</td>
                <td style="border: 1px solid #ddd; padding: 10px;">Mượt, ổn định</td>
                <td style="border: 1px solid #ddd; padding: 10px;">Cao</td>
            </tr>
            <tr>
                <td style="border: 1px solid #ddd; padding: 10px;"><strong>Mini-batch GD</strong></td>
                <td style="border: 1px solid #ddd; padding: 10px;">$$b$$ (thường 32–256)</td>
                <td style="border: 1px solid #ddd; padding: 10px;">$$O(b)$$</td>
                <td style="border: 1px solid #ddd; padding: 10px;">Cân bằng</td>
                <td style="border: 1px solid #ddd; padding: 10px;">Trung bình</td>
            </tr>
            <tr>
                <td style="border: 1px solid #ddd; padding: 10px;"><strong>SGD</strong></td>
                <td style="border: 1px solid #ddd; padding: 10px;">1</td>
                <td style="border: 1px solid #ddd; padding: 10px;">$$O(1)$$</td>
                <td style="border: 1px solid #ddd; padding: 10px;">Nhanh nhưng nhiều nhiễu</td>
                <td style="border: 1px solid #ddd; padding: 10px;">Thấp</td>
            </tr>
        </tbody>
    </table>
</div>

## Tổng kết và Kinh nghiệm Thực hành

### Khi nào nên dùng SGD
1. **Tập dữ liệu lớn** (hàng triệu mẫu).
2. **Bài toán học trực tuyến (online learning)** khi dữ liệu đến theo luồng.
3. **Môi trường hạn chế bộ nhớ**.
4. **Giai đoạn huấn luyện đầu** cần giảm nhanh hàm mất mát.

### Khi nào nên dùng Batch GD
1. **Tập dữ liệu nhỏ đến trung bình**.
2. **Yêu cầu độ chính xác nghiệm cao**.
3. **Cần quỹ đạo hội tụ ổn định, không nhiễu**.
4. **Giai đoạn tinh chỉnh cuối** sau khi đã tiến gần nghiệm.

### Thực hành Khuyến nghị
- **Lập lịch tốc độ học**: Bắt đầu với bước lớn vừa phải rồi giảm dần theo thời gian.
- **Xáo trộn dữ liệu**: Đảo ngẫu nhiên thứ tự mẫu trước mỗi epoch.
- **Mini-batch**: Thường là lựa chọn thực tế tốt nhất nhờ tận dụng tính toán song song trên phần cứng.
- **Momentum**: Giúp SGD giảm dao động do nhiễu và tăng tốc hội tụ.

**Trong thực tế hiện đại**: Hầu hết các thư viện học sâu đều sử dụng mini-batch SGD kết hợp với các thuật toán tối ưu thích ứng (như Adam, RMSprop) để tự động điều chỉnh tốc độ học cho từng tham số.

<script>
document.addEventListener('DOMContentLoaded', function() {
    // Global variables for demos
    let gdData = [], sgdData = [];
    let gdPosition = [2, 2], sgdPosition = [2, 2];
    let isRunning = false;
    let isPaused = false;
    let isManualMode = false;
    let animationId;
    let currentAlgorithm = null; // 'gd' or 'sgd'
    let algorithmState = {
        gd: { iteration: 0, position: [2, 2], path: [], functions: [], totalCost: 0, gradient: [0, 0] },
        sgd: { iteration: 0, position: [2, 2], path: [], functions: [], totalCost: 0, gradient: [0, 0], selectedFunc: -1 }
    };
    
    // Initialize sliders
    const learningRateSlider = document.getElementById('learning-rate');
    const numFunctionsSlider = document.getElementById('num-functions');
    const animationSpeedSlider = document.getElementById('animation-speed');
    const lrValue = document.getElementById('lr-value');
    const mValue = document.getElementById('m-value');
    const speedValue = document.getElementById('speed-value');
    
    if (learningRateSlider) {
        learningRateSlider.addEventListener('input', function() {
            lrValue.textContent = this.value;
        });
    }
    
    if (numFunctionsSlider) {
        numFunctionsSlider.addEventListener('input', function() {
            mValue.textContent = this.value;
        });
    }
    
    if (animationSpeedSlider) {
        animationSpeedSlider.addEventListener('input', function() {
            speedValue.textContent = this.value;
        });
    }
    
    // Execution mode radio buttons
    const execModeRadios = document.querySelectorAll('input[name="exec-mode"]');
    execModeRadios.forEach(radio => {
        radio.addEventListener('change', function() {
            isManualMode = this.value === 'manual';
            updateControlButtons();
        });
    });
    
    // Simple quadratic functions for demonstration
    function createFunctions(m) {
        const functions = [];
        for (let i = 0; i < m; i++) {
            const centerX = (Math.random() - 0.5) * 4;
            const centerY = (Math.random() - 0.5) * 4;
            functions.push({
                center: [centerX, centerY],
                gradient: function(x, y) {
                    return [2 * (x - centerX), 2 * (y - centerY)];
                },
                value: function(x, y) {
                    return (x - centerX) ** 2 + (y - centerY) ** 2;
                }
            });
        }
        return functions;
    }
    
    // Setup SVG plots
    function setupPlot(svgId, width = 300, height = 300) {
        const svg = d3.select(`#${svgId}`);
        if (svg.empty()) return null;
        
        svg.selectAll("*").remove();
        
        const margin = {top: 20, right: 20, bottom: 30, left: 40};
        const plotWidth = width - margin.left - margin.right;
        const plotHeight = height - margin.top - margin.bottom;
        
        const xScale = d3.scaleLinear()
            .domain([-3, 3])
            .range([0, plotWidth]);
            
        const yScale = d3.scaleLinear()
            .domain([-3, 3])
            .range([plotHeight, 0]);
        
        const g = svg.append("g")
            .attr("transform", `translate(${margin.left},${margin.top})`);
        
        // Add axes
        g.append("g")
            .attr("transform", `translate(0,${plotHeight})`)
            .call(d3.axisBottom(xScale));
            
        g.append("g")
            .call(d3.axisLeft(yScale));
        
        // Add contour background
        const contourData = [];
        for (let i = 0; i < 20; i++) {
            for (let j = 0; j < 20; j++) {
                const x = -3 + (i / 19) * 6;
                const y = -3 + (j / 19) * 6;
                contourData.push({x, y, z: x*x + y*y});
            }
        }
        
        return {svg, g, xScale, yScale, plotWidth, plotHeight};
    }
    
    // Control button functions
    function updateControlButtons() {
        const pauseResumeBtn = document.getElementById('pause-resume');
        const stepForwardBtn = document.getElementById('step-forward');
        
        if (pauseResumeBtn) {
            pauseResumeBtn.disabled = !isRunning;
            pauseResumeBtn.textContent = isPaused ? 'Tiếp tục' : 'Tạm dừng';
        }
        
        if (stepForwardBtn) {
            stepForwardBtn.disabled = !isManualMode && !isPaused;
        }
    }
    
    // GD vs SGD Comparison Demo
    const startGDBtn = document.getElementById('start-gd');
    const startSGDBtn = document.getElementById('start-sgd');
    const pauseResumeBtn = document.getElementById('pause-resume');
    const stepForwardBtn = document.getElementById('step-forward');
    const resetBtn = document.getElementById('reset-demo');
    
    if (startGDBtn) {
        startGDBtn.addEventListener('click', function() {
            if (isRunning && currentAlgorithm === 'gd') return;
            initializeAlgorithm('gd');
            if (!isManualMode) {
                runAlgorithm('gd');
            }
        });
    }
    
    if (startSGDBtn) {
        startSGDBtn.addEventListener('click', function() {
            if (isRunning && currentAlgorithm === 'sgd') return;
            initializeAlgorithm('sgd');
            if (!isManualMode) {
                runAlgorithm('sgd');
            }
        });
    }
    
    if (pauseResumeBtn) {
        pauseResumeBtn.addEventListener('click', function() {
            if (isPaused) {
                isPaused = false;
                if (currentAlgorithm) {
                    runAlgorithm(currentAlgorithm);
                }
            } else {
                isPaused = true;
                if (animationId) {
                    cancelAnimationFrame(animationId);
                }
            }
            updateControlButtons();
        });
    }
    
    if (stepForwardBtn) {
        stepForwardBtn.addEventListener('click', function() {
            if (currentAlgorithm && (isManualMode || isPaused)) {
                performSingleStep(currentAlgorithm);
            }
        });
    }
    
    if (resetBtn) {
        resetBtn.addEventListener('click', function() {
            resetDemo();
        });
    }
    
    // Initialize algorithm state
    function initializeAlgorithm(algorithm) {
        const m = parseInt(numFunctionsSlider.value);
        const functions = createFunctions(m);
        
        algorithmState[algorithm] = {
            iteration: 0,
            position: [2, 2],
            path: [[2, 2]],
            functions: functions,
            totalCost: 0,
            gradient: [0, 0],
            selectedFunc: algorithm === 'sgd' ? -1 : undefined
        };
        
        currentAlgorithm = algorithm;
        isRunning = true;
        isPaused = false;
        
        // Setup plot
        const plotId = algorithm === 'gd' ? 'gd-plot' : 'sgd-plot';
        const plot = setupPlot(plotId, 350, 350);
        
        // Update status
        updateAlgorithmDisplay(algorithm);
        updateControlButtons();
        
        // Update detailed info
        const detailedInfoId = algorithm === 'gd' ? 'gd-detailed-info' : 'sgd-detailed-info';
        document.getElementById(detailedInfoId).textContent = 
            isManualMode ? 'Sẵn sàng chạy từng bước' : 'Đang tự động chạy...';
    }
    
    // Run algorithm in auto mode
    function runAlgorithm(algorithm) {
        if (isPaused || isManualMode) return;
        
        const speed = parseInt(animationSpeedSlider.value);
        const delay = 1100 - speed * 100; // Convert speed to delay (higher speed = lower delay)
        
        function step() {
            if (isPaused || !isRunning) return;
            
            const shouldContinue = performSingleStep(algorithm);
            
            if (shouldContinue && !isPaused) {
                setTimeout(() => {
                    animationId = requestAnimationFrame(step);
                }, delay);
            } else {
                isRunning = false;
                updateControlButtons();
                
                const detailedInfoId = algorithm === 'gd' ? 'gd-detailed-info' : 'sgd-detailed-info';
                document.getElementById(detailedInfoId).textContent = 'Đã hội tụ!';
            }
        }
        
        step();
    }
    
    // Perform a single step of the algorithm
    function performSingleStep(algorithm) {
        const state = algorithmState[algorithm];
        const lr = parseFloat(learningRateSlider.value);
        
        if (algorithm === 'gd') {
            return performGDStep(state, lr);
        } else {
            return performSGDStep(state, lr);
        }
    }
    
    function performGDStep(state, lr) {
        // Compute full gradient (sum of all function gradients)
        let gradX = 0, gradY = 0;
        for (const func of state.functions) {
            const grad = func.gradient(state.position[0], state.position[1]);
            gradX += grad[0];
            gradY += grad[1];
        }
        
        // Average the gradients
        gradX /= state.functions.length;
        gradY /= state.functions.length;
        
        state.gradient = [gradX, gradY];
        
        // Update position
        state.position[0] -= lr * gradX;
        state.position[1] -= lr * gradY;
        state.path.push(state.position.slice());
        
        // Compute total cost
        state.totalCost = 0;
        for (const func of state.functions) {
            state.totalCost += func.value(state.position[0], state.position[1]);
        }
        state.totalCost /= state.functions.length;
        
        state.iteration++;
        
        // Update visualization
        updateAlgorithmDisplay('gd');
        
        // Check convergence
        const gradientMagnitude = Math.sqrt(gradX * gradX + gradY * gradY);
        return state.iteration < 100 && gradientMagnitude > 0.01;
    }
    
    function performSGDStep(state, lr) {
        // Select random function
        const funcIndex = Math.floor(Math.random() * state.functions.length);
        const func = state.functions[funcIndex];
        state.selectedFunc = funcIndex;
        
        // Compute gradient for selected function only
        const grad = func.gradient(state.position[0], state.position[1]);
        state.gradient = grad;
        
        // Update position
        state.position[0] -= lr * grad[0];
        state.position[1] -= lr * grad[1];
        state.path.push(state.position.slice());
        
        // Compute total cost
        state.totalCost = 0;
        for (const func of state.functions) {
            state.totalCost += func.value(state.position[0], state.position[1]);
        }
        state.totalCost /= state.functions.length;
        
        state.iteration++;
        
        // Update visualization
        updateAlgorithmDisplay('sgd');
        
        // Check convergence (SGD needs more iterations)
        return state.iteration < 300 && state.totalCost > 0.01;
    }
    
    function updateAlgorithmDisplay(algorithm) {
        const state = algorithmState[algorithm];
        const plotId = algorithm === 'gd' ? 'gd-plot' : 'sgd-plot';
        const color = algorithm === 'gd' ? 'steelblue' : 'orange';
        
        // Update path visualization
        const plot = {
            svg: d3.select(`#${plotId}`),
            g: d3.select(`#${plotId} g`),
            xScale: d3.scaleLinear().domain([-3, 3]).range([0, 270]),
            yScale: d3.scaleLinear().domain([-3, 3]).range([270, 0])
        };
        
        if (!plot.g.empty()) {
            updatePath(plot, state.path, color);
        }
        
        // Update info displays
        const infoId = algorithm === 'gd' ? 'gd-info' : 'sgd-info';
        const gradientInfoId = algorithm === 'gd' ? 'gd-gradient-info' : 'sgd-gradient-info';
        
        document.getElementById(infoId).textContent = 
            `Số vòng lặp: ${state.iteration}, Chi phí: ${state.totalCost.toFixed(4)}`;
        
        if (algorithm === 'gd') {
            document.getElementById(gradientInfoId).textContent = 
                `Gradient: [${state.gradient[0].toFixed(3)}, ${state.gradient[1].toFixed(3)}]`;
        } else {
            document.getElementById(gradientInfoId).textContent = 
                `Hàm được chọn: f${state.selectedFunc + 1}, Gradient: [${state.gradient[0].toFixed(3)}, ${state.gradient[1].toFixed(3)}]`;
        }
        
        // Update progress bar
        const progressId = algorithm === 'gd' ? 'gd-progress' : 'sgd-progress';
        const maxIterations = algorithm === 'gd' ? 100 : 300;
        const progress = Math.min((state.iteration / maxIterations) * 100, 100);
        document.getElementById(progressId).style.width = `${progress}%`;
        
        // Update detailed status
        const detailedInfoId = algorithm === 'gd' ? 'gd-detailed-info' : 'sgd-detailed-info';
        const gradMagnitude = Math.sqrt(state.gradient[0] ** 2 + state.gradient[1] ** 2);
        document.getElementById(detailedInfoId).textContent = 
            `Bước ${state.iteration}: Vị trí [${state.position[0].toFixed(3)}, ${state.position[1].toFixed(3)}], |∇| = ${gradMagnitude.toFixed(4)}`;
    }
    
    function updatePath(plot, path, color) {
        const line = d3.line()
            .x(d => plot.xScale(d[0]))
            .y(d => plot.yScale(d[1]));
        
        plot.g.selectAll('.path').remove();
        plot.g.append('path')
            .datum(path)
            .attr('class', 'path')
            .attr('fill', 'none')
            .attr('stroke', color)
            .attr('stroke-width', 2)
            .attr('d', line);
        
        // Add current position
        const current = path[path.length - 1];
        plot.g.selectAll('.current-pos').remove();
        plot.g.append('circle')
            .attr('class', 'current-pos')
            .attr('cx', plot.xScale(current[0]))
            .attr('cy', plot.yScale(current[1]))
            .attr('r', 5)
            .attr('fill', color);
    }
    
    function resetDemo() {
        if (animationId) {
            cancelAnimationFrame(animationId);
        }
        
        isRunning = false;
        isPaused = false;
        currentAlgorithm = null;
        
        // Reset algorithm states
        algorithmState = {
            gd: { iteration: 0, position: [2, 2], path: [], functions: [], totalCost: 0, gradient: [0, 0] },
            sgd: { iteration: 0, position: [2, 2], path: [], functions: [], totalCost: 0, gradient: [0, 0], selectedFunc: -1 }
        };
        
        // Clear plots
        d3.select('#gd-plot').selectAll("*").remove();
        d3.select('#sgd-plot').selectAll("*").remove();
        
        // Reset info displays
        document.getElementById('gd-info').textContent = 'Số vòng lặp: 0, Chi phí: 0';
        document.getElementById('sgd-info').textContent = 'Số vòng lặp: 0, Chi phí: 0';
        document.getElementById('gd-gradient-info').textContent = 'Gradient: [0, 0]';
        document.getElementById('sgd-gradient-info').textContent = 'Hàm được chọn: -, Gradient: [0, 0]';
        
        // Reset detailed info
        document.getElementById('gd-detailed-info').textContent = 'Sẵn sàng';
        document.getElementById('sgd-detailed-info').textContent = 'Sẵn sàng';
        
        // Reset progress bars
        document.getElementById('gd-progress').style.width = '0%';
        document.getElementById('sgd-progress').style.width = '0%';
        
        // Update control buttons
        updateControlButtons();
    }
    
});
</script>

### SGD và minibatch trong khoảng 3 phút

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/sgd-minibatch_vi.mp4"></video>
</div>

Ví dụ m = 3 điểm: một bước GD so với một epoch SGD, bước hằng so với bước giảm dần, rồi ảnh hưởng của kích thước batch.
