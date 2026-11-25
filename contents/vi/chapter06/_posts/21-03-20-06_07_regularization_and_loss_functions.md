---
layout: post
title: 06-07 Điều Chuẩn và Hàm Mất Mát
chapter: '06'
order: 19
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
---

Một mô hình học máy đạt sai số bằng $$0$$ trên tập huấn luyện có phải là mô hình tốt nhất không? Hoàn toàn ngược lại: nó có thể đang **học thuộc lòng cả nhiễu ngẫu nhiên** (quá khớp — overfitting) và sụp đổ thảm hại khi gặp dữ liệu mới! Để dạy mô hình biết "tổng quát hóa", tối ưu hóa học máy kết hợp hai thành phần như hai đĩa cân: **Hàm mất mát (Loss Function)** đo độ khớp với dữ liệu, và **Số hạng Điều chuẩn (Regularization)** phạt độ phức tạp của trọng số.

Điều kỳ diệu là cả hai lựa chọn đó đều mang ý nghĩa sâu sắc dưới lăng kính tối ưu hóa lồi: thêm Ridge ($$\ell_2$$) lập tức biến bài toán thành **lồi mạnh** (nghiệm duy nhất, hội tụ tuyến tính); thêm Lasso ($$\ell_1$$) tạo ra các **góc nhọn trên trục tọa độ** tự động ép trọng số thừa về đúng $$0$$ (chọn đặc trưng thưa); còn đổi hàm mất mát từ MSE sang Huber hay Hinge giúp mô hình miễn nhiễm với dữ liệu ngoại lai!

## Bản đồ kiến thức nền: Hình học của Điều chuẩn và Hàm mất mát

Bốn trụ cột dưới đây giúp bạn chọn đúng hàm mục tiêu cho mọi bài toán học máy:

- **Điều chuẩn $$\ell_2$$ (Ridge) — Độ trơn & Lồi mạnh:** Cộng $$\frac{\lambda}{2}\|w\|_2^2$$ vào hàm mất mát. Hình học: miền ràng buộc $$\|w\|_2 \le r$$ là hình cầu trơn, co đều mọi trọng số về gần 0 nhưng hiếm khi bằng 0 tuyệt đối. Lợi ích tối ưu: đảm bảo $$X^T X + \lambda I \succ 0$$ luôn khả nghịch và cải thiện chỉ số điều kiện $$\kappa$$!
- **Điều chuẩn $$\ell_1$$ (Lasso) — Tính thưa (Sparsity):** Cộng $$\lambda \|w\|_1$$. Hình học: miền ràng buộc $$\|w\|_1 \le r$$ là khối bát diện (hình thoi trong 2D) có các **đỉnh nhọn nằm đúng trên các trục tọa độ**, nên đường đồng mức elip rất dễ chạm đúng đỉnh và triệt tiêu hoàn toàn các biến vô ích! (Nhưng hàm không khả vi tại 0 — mở đường sang Chương 07: Subgradient!)
- **Elastic Net (Kết hợp $$\ell_1 + \ell_2$$):** Cộng $$\lambda_1 \|w\|_1 + \frac{\lambda_2}{2}\|w\|_2^2$$ để vừa giữ tính thưa của Lasso, vừa có tính lồi mạnh và xử lý tốt nhóm đặc trưng tương quan cao như Ridge.
- **Lựa chọn Hàm mất mát theo bản chất nhiễu & tác vụ:** Hồi quy chuẩn dùng **MSE** (trơn, nhạy ngoại lai), dữ liệu nhiều ngoại lai dùng **MAE** hoặc **Huber Loss** (bậc hai quanh 0, tuyến tính ở xa); phân loại dùng **Log-Loss** (xác suất trơn) hoặc **Hinge Loss** (biên lớn của SVM).

### Khung giải thích (nên đọc chậm): So sánh trực tiếp nghiệm OLS, Ridge và Lasso trên bài toán 1 chiều

Xét bài toán cực tiểu hóa 1 biến với dữ liệu chuẩn hóa $$y = 3$$ (tức nghiệm không điều chuẩn là $$w_{\text{OLS}} = 3$$) và hệ số điều chuẩn $$\lambda = 1$$:

1. **OLS (Không điều chuẩn):**
   $$\min_w \; \frac{1}{2}(w - 3)^2 \implies w_{\text{OLS}}^\star = 3.$$
2. **Ridge ($$\ell_2$$):**
   $$\min_w \; \frac{1}{2}(w - 3)^2 + \frac{1}{2}(1)w^2 = w^2 - 3w + 4.5.$$
   Đạo hàm $$2w - 3 = 0 \implies w_{\text{Ridge}}^\star = \frac{3}{1 + 1} = 1.5$$.
   (Tỷ lệ co đều: $$w_{\text{Ridge}} = \frac{y}{1 + \lambda}$$ — chỉ bằng $$0$$ khi $$y = 0$$!)
3. **Lasso ($$\ell_1$$):**
   $$\min_w \; \frac{1}{2}(w - 3)^2 + 1 \cdot |w|.$$
   Với $$w > 0$$, đạo hàm $$w - 3 + 1 = 0 \implies w_{\text{Lasso}}^\star = 3 - 1 = 2$$ (dịch về 0 đúng $$\lambda = 1$$ đơn vị).
   Bây giờ thử với một đặc trưng yếu có $$y = 0.7 < \lambda = 1$$:
   - Ridge vẫn cho $$w_{\text{Ridge}}^\star = \frac{0.7}{2} = 0.35 \neq 0$$.
   - Lasso ép **chính xác về $$w_{\text{Lasso}}^\star = 0$$** (ngưỡng mềm: $$\operatorname{sign}(y)\max(|y| - \lambda, 0) = 0$$)! Đó là lý do Lasso tự động loại bỏ đặc trưng nhiễu!

---

<script src="../../../public/js/script.js"></script>
<script src="https://d3js.org/d3.v7.min.js"></script>

## Giới thiệu: Vấn đề Quá khớp (Overfitting) trong Học máy

Trong học máy, một thách thức phổ biến là hiện tượng **quá khớp (overfitting)** — khi mô hình khớp quá sát vào nhiễu của dữ liệu huấn luyện, dẫn đến khả năng tổng quát hóa kém trên dữ liệu mới. **Điều chuẩn (regularization)** là kỹ thuật nền tảng giúp kiểm soát độ phức tạp của mô hình và giảm thiểu quá khớp.

### Vì sao cần Điều chuẩn?

Xét bài toán hồi quy tuyến tính cơ bản:
$$\min_{\mathbf{w}} rac{1}{2n} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2$$

**Vấn đề**: Khi số lượng đặc trưng lớn hoặc số mẫu ít, mô hình có thể đạt sai số huấn luyện gần bằng 0 nhưng lại cho sai số lớn trên dữ liệu kiểm tra.

**Giải pháp**: Bổ sung một **số hạng điều chuẩn (regularization term)** để phạt các trọng số có độ lớn quá cao:
$$\min_{\mathbf{w}} rac{1}{2n} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2 + \lambda R(\mathbf{w})$$

trong đó:
- $$\lambda > 0$$ là **tham số điều chuẩn** (kiểm soát mức độ phạt).
- $$R(\mathbf{w})$$ là **hàm điều chuẩn**.

## Hồi quy Ridge (Điều chuẩn L2)

### Định nghĩa Toán học

Hồi quy Ridge sử dụng bình phương chuẩn L2 làm số hạng điều chuẩn:

$$\min_{\mathbf{w}} rac{1}{2n} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2 + rac{\lambda}{2} \|\mathbf{w}\|_2^2$$

**Các thành phần của hàm mục tiêu:**
- **Hàm mất mát**: $$rac{1}{2n} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2$$ đo độ lệch giữa giá trị dự đoán và giá trị thực.
- **Số hạng điều chuẩn**: $$rac{\lambda}{2} \|\mathbf{w}\|_2^2 = rac{\lambda}{2} \sum_{j=1}^p w_j^2$$ phạt các trọng số có độ lớn cao.
- **Cường độ điều chuẩn**: $$\lambda$$ điều chỉnh sự đánh đổi giữa độ khớp dữ liệu và độ nhỏ của trọng số.

### Nghiệm Giải tích

Hồi quy Ridge có nghiệm dạng đóng:
$$\mathbf{w}^* = (\mathbf{X}^T\mathbf{X} + n\lambda \mathbf{I})^{-1} \mathbf{X}^T \mathbf{y}$$
(Nếu bỏ hệ số $$rac{1}{n}$$ ở hàm mất mát, nghiệm có dạng gọn là $$\mathbf{w}^* = (\mathbf{X}^T\mathbf{X} + \lambda \mathbf{I})^{-1} \mathbf{X}^T \mathbf{y}$$.)

**Ưu điểm của nghiệm này:**
- Ma trận $$(\mathbf{X}^T\mathbf{X} + n\lambda \mathbf{I})$$ luôn khả nghịch với mọi $$\lambda > 0$$.
- Khắc phục hiệu quả hiện tượng đa cộng tuyến (multicollinearity).
- Tính toán trực tiếp được bằng các thuật toán đại số tuyến tính chuẩn.

### Minh họa Hiệu ứng Điều chuẩn Ridge

<div id="ridge-effect-demo" style="margin: 20px 0;">
    <div style="margin-bottom: 15px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; background-color: #f9f9f9;">
        <h4>Điều khiển Ridge Regularization</h4>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px;">
            <div>
                <label for="ridge-lambda">Lambda (λ): </label>
                <input type="range" id="ridge-lambda" min="0" max="10" step="0.1" value="1">
                <span id="ridge-lambda-value">1.0</span>
            </div>
            <div>
                <label for="ridge-noise">Noise Level: </label>
                <input type="range" id="ridge-noise" min="0" max="0.5" step="0.05" value="0.1">
                <span id="ridge-noise-value">0.1</span>
            </div>
            <div>
                <label for="ridge-features">Number of Features: </label>
                <input type="range" id="ridge-features" min="5" max="20" step="1" value="10">
                <span id="ridge-features-value">10</span>
            </div>
        </div>
        <div style="margin-top: 10px;">
            <button id="ridge-regenerate" style="background-color: #4CAF50; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Tạo dữ liệu mới</button>
        </div>
    </div>
    
    <div style="display: flex; gap: 20px; justify-content: center;">
        <div style="text-align: center;">
            <h4>Coefficients Path</h4>
            <svg id="ridge-coefficients" width="400" height="300" style="border: 1px solid #ddd;"></svg>
            <div style="margin-top: 10px; padding: 8px; background-color: #f5f5f5; border-radius: 4px;">
                <p id="ridge-coeff-info" style="margin: 0; font-size: 12px;">L2 Norm của coefficients: 0</p>
            </div>
        </div>
        <div style="text-align: center;">
            <h4>Training vs Validation Error</h4>
            <svg id="ridge-error" width="400" height="300" style="border: 1px solid #ddd;"></svg>
            <div style="margin-top: 10px; padding: 8px; background-color: #f5f5f5; border-radius: 4px;">
                <p id="ridge-error-info" style="margin: 0; font-size: 12px;">Optimal λ: 0</p>
            </div>
        </div>
    </div>
</div>

## Ví dụ Thực tế: Cực tiểu hóa Hàm Bậc hai

Để thấy rõ tác động toán học của điều chuẩn, ta xét bài toán cực tiểu hóa hàm bậc hai — cấu trúc nền tảng của nhiều mô hình học máy và tài chính định lượng.

### Bài toán: Tối ưu hóa Danh mục Đầu tư có Điều chuẩn

Xét bài toán tối ưu hóa danh mục đầu tư:

$$\min_{\mathbf{w}} rac{1}{2} \mathbf{w}^T \mathbf{Q} \mathbf{w} - \mathbf{\mu}^T \mathbf{w} + rac{\lambda}{2} \|\mathbf{w}\|_2^2$$

trong đó:
- $$\mathbf{w} \in \mathbb{R}^n$$: vector trọng số đầu tư cho $$n$$ tài sản.
- $$\mathbf{Q} \in \mathbb{R}^{n 	imes n}$$: ma trận hiệp phương sai (đo rủi ro).
- $$\mathbf{\mu} \in \mathbb{R}^n$$: vector lợi suất kỳ vọng.
- $$\lambda > 0$$: tham số điều chuẩn (phản ánh mức độ ngại rủi ro hoặc ổn định hóa trọng số).

### Phân tích Toán học

#### 1. Gradient của Hàm Mục tiêu

$$
abla f(\mathbf{w}) = \mathbf{Q}\mathbf{w} - \mathbf{\mu} + \lambda \mathbf{w} = (\mathbf{Q} + \lambda \mathbf{I})\mathbf{w} - \mathbf{\mu}$$

#### 2. Ma trận Hessian

$$
abla^2 f(\mathbf{w}) = \mathbf{Q} + \lambda \mathbf{I}$$

**Nhận xét quan trọng**:
- Khi $$\lambda > 0$$ và $$\mathbf{Q}$$ nửa xác định dương, ma trận Hessian $$\mathbf{Q} + \lambda \mathbf{I}$$ luôn xác định dương.
- Hàm mục tiêu trở nên lồi mạnh.
- Nghiệm tối ưu tồn tại và là duy nhất.

#### 3. Nghiệm Tối ưu

Đặt gradient bằng 0:
$$(\mathbf{Q} + \lambda \mathbf{I})\mathbf{w}^* = \mathbf{\mu}$$

$$\mathbf{w}^* = (\mathbf{Q} + \lambda \mathbf{I})^{-1} \mathbf{\mu}$$

### Minh họa Tương tác cho Hàm Bậc hai

<div id="quadratic-function-demo" style="margin: 20px 0;">
    <div style="margin-bottom: 15px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; background-color: #f9f9f9;">
        <h4>Quadratic Function Parameters</h4>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px;">
            <div>
                <label for="quad-lambda">Regularization λ: </label>
                <input type="range" id="quad-lambda" min="0" max="5" step="0.1" value="1">
                <span id="quad-lambda-value">1.0</span>
            </div>
            <div>
                <label for="quad-condition">Condition Number: </label>
                <input type="range" id="quad-condition" min="1" max="50" step="1" value="10">
                <span id="quad-condition-value">10</span>
            </div>
            <div>
                <label for="quad-dimension">Dimension: </label>
                <input type="range" id="quad-dimension" min="2" max="5" step="1" value="2">
                <span id="quad-dimension-value">2</span>
            </div>
        </div>
        <div style="margin-top: 10px;">
            <button id="quad-optimize" style="background-color: #4CAF50; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Run Optimization</button>
            <button id="quad-reset" style="background-color: #f44336; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Reset</button>
        </div>
    </div>
    
    <div style="display: flex; gap: 20px; justify-content: center;">
        <div style="text-align: center;">
            <h4>2D Contour Plot</h4>
            <svg id="quadratic-contour" width="400" height="400" style="border: 1px solid #ddd;"></svg>
            <div style="margin-top: 10px; padding: 8px; background-color: #f5f5f5; border-radius: 4px;">
                <p id="quad-contour-info" style="margin: 0; font-size: 12px;">Click to set starting point</p>
            </div>
        </div>
        <div style="text-align: center;">
            <h4>Convergence Analysis</h4>
            <svg id="quadratic-convergence" width="400" height="300" style="border: 1px solid #ddd;"></svg>
            <div style="margin-top: 10px; padding: 8px; background-color: #f5f5f5; border-radius: 4px;">
                <p id="quad-convergence-info" style="margin: 0; font-size: 12px;">Convergence rate: -</p>
            </div>
        </div>
    </div>
    
    <div style="margin-top: 20px;">
        <h4>Eigenvalue Analysis</h4>
        <div style="display: flex; gap: 20px; justify-content: center;">
            <div style="text-align: center;">
                <h5>Original Matrix Q</h5>
                <svg id="eigenvalue-original" width="300" height="200" style="border: 1px solid #ddd;"></svg>
            </div>
            <div style="text-align: center;">
                <h5>Regularized Matrix Q + λI</h5>
                <svg id="eigenvalue-regularized" width="300" height="200" style="border: 1px solid #ddd;"></svg>
            </div>
        </div>
        <div style="margin-top: 10px; padding: 10px; background-color: #e3f2fd; border-radius: 4px;">
            <p id="eigenvalue-analysis" style="margin: 0; font-size: 14px;">
                <strong>Analysis:</strong> Regularization improves condition number from ∞ to finite value
            </p>
        </div>
    </div>
</div>

### Gradient Descent trên Hàm Bậc hai

Với hàm mục tiêu bậc hai có điều chuẩn, bước lặp gradient descent có dạng:

$$\mathbf{w}^{(k+1)} = \mathbf{w}^{(k)} - lpha [(\mathbf{Q} + \lambda \mathbf{I})\mathbf{w}^{(k)} - \mathbf{\mu}]$$

#### Phân tích Tốc độ Hội tụ

- **Phân rã trị riêng**: $$\mathbf{Q} + \lambda \mathbf{I} = \mathbf{V} \mathbf{\Lambda} \mathbf{V}^T$$
- **Hệ số co**: $$
ho = \max_i \left|1 - lpha \lambda_i
ight|$$, trong đó $$\lambda_i$$ là các trị riêng của $$\mathbf{Q} + \lambda \mathbf{I}$$.
- **Kích thước bước tối ưu**: $$lpha^* = rac{2}{\lambda_{\min} + \lambda_{\max}}$$.
- **Hệ số hội tụ tối ưu**: $$
ho^* = rac{\kappa - 1}{\kappa + 1}$$, trong đó $$\kappa = rac{\lambda_{\max}}{\lambda_{\min}}$$ là chỉ số điều kiện.

### Ảnh hưởng của Điều chuẩn lên Tốc độ Hội tụ

<div id="regularization-convergence-demo" style="margin: 20px 0;">
    <div style="margin-bottom: 15px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; background-color: #fff3e0;">
        <h4>Convergence Rate Analysis</h4>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px;">
            <div>
                <label for="conv-lambda">Lambda: </label>
                <input type="range" id="conv-lambda" min="0.01" max="3" step="0.01" value="0.1">
                <span id="conv-lambda-value">0.1</span>
            </div>
            <div>
                <label for="conv-step-size">Step Size: </label>
                <input type="range" id="conv-step-size" min="0.01" max="0.5" step="0.01" value="0.1">
                <span id="conv-step-size-value">0.1</span>
            </div>
            <div>
                <button id="conv-optimal-step" style="background-color: #FF9800; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Optimal Step Size</button>
            </div>
        </div>
    </div>
    
    <div style="display: flex; gap: 20px; justify-content: center;">
        <div style="text-align: center;">
            <h4>Convergence Comparison</h4>
            <svg id="convergence-comparison" width="400" height="300" style="border: 1px solid #ddd;"></svg>
            <div style="margin-top: 10px; padding: 8px; background-color: #f5f5f5; border-radius: 4px;">
                <div style="display: flex; gap: 15px; justify-content: center; font-size: 12px;">
                    <span style="color: #1f77b4;">■ No Regularization</span>
                    <span style="color: #ff7f0e;">■ With Regularization</span>
                </div>
            </div>
        </div>
        <div style="text-align: center;">
            <h4>Condition Number vs λ</h4>
            <svg id="condition-number-plot" width="400" height="300" style="border: 1px solid #ddd;"></svg>
            <div style="margin-top: 10px; padding: 8px; background-color: #f5f5f5; border-radius: 4px;">
                <p id="condition-info" style="margin: 0; font-size: 12px;">Current κ: ∞</p>
            </div>
        </div>
    </div>
</div>

### Tình huống Minh họa: Bài toán Điều kiện Xấu

#### Vấn đề: Đa cộng tuyến trong Hồi quy Tuyến tính

Xét ma trận đặc trưng $$\mathbf{X}$$ có các cột gần như phụ thuộc tuyến tính:

$$\mathbf{X} = egin{bmatrix}
1 & 1 & 1.001 \
1 & 2 & 2.001 \
1 & 3 & 3.001 \
dots & dots & dots
\end{bmatrix}$$

**Hệ phương trình chuẩn (normal equations)**: $$\mathbf{X}^T\mathbf{X} \mathbf{w} = \mathbf{X}^T \mathbf{y}$$

**Vấn đề**: Ma trận $$\mathbf{X}^T\mathbf{X}$$ có chỉ số điều kiện rất lớn, gây mất ổn định số học khi nghịch đảo.

#### Giải pháp: Điều chuẩn Ridge

$$(\mathbf{X}^T\mathbf{X} + \lambda \mathbf{I}) \mathbf{w} = \mathbf{X}^T \mathbf{y}$$

**Tác dụng**:
- Giảm mạnh chỉ số điều kiện (chẳng hạn từ $$10^{12}$$ xuống $$10^2$$).
- Cải thiện rõ rệt độ ổn định số học.
- Đánh đổi hợp lý: chấp nhận tăng nhẹ độ chệch (bias) để giảm đáng kể phương sai (variance).

### Phân tích Thống kê

#### 1. Phân tích Độ chệch – Phương sai (Bias–Variance)

Đối với hồi quy Ridge:

$$	ext{MSE} = 	ext{Bias}^2 + 	ext{Variance} + 	ext{Noise}$$

- **Độ chệch (Bias)**: $$\mathbb{E}[\hat{\mathbf{w}}] - \mathbf{w}^* = -\lambda (\mathbf{X}^T\mathbf{X} + \lambda \mathbf{I})^{-1} \mathbf{w}^*$$
- **Phương sai (Variance)**: $$	ext{Var}[\hat{\mathbf{w}}] = \sigma^2 (\mathbf{X}^T\mathbf{X} + \lambda \mathbf{I})^{-1} \mathbf{X}^T\mathbf{X} (\mathbf{X}^T\mathbf{X} + \lambda \mathbf{I})^{-1}$$

#### 2. Bậc Tự do Hiệu dụng (Effective Degrees of Freedom)

$$	ext{df}(\lambda) = 	ext{tr}[\mathbf{X}(\mathbf{X}^T\mathbf{X} + \lambda \mathbf{I})^{-1}\mathbf{X}^T] = \sum_{i=1}^p rac{\sigma_i^2}{\sigma_i^2 + \lambda}$$

trong đó $$\sigma_i$$ là các giá trị kỳ dị của $$\mathbf{X}$$ (và $$\sigma_i^2$$ là các trị riêng của $$\mathbf{X}^T\mathbf{X}$$).

**Ý nghĩa**: Tăng $$\lambda$$ làm giảm bậc tự do hiệu dụng, qua đó thu hẹp độ phức tạp của mô hình.

### Cân nhắc về Tính toán

#### 1. Giải Trực tiếp so với Phương pháp Lặp

**Giải trực tiếp (phân rã Cholesky)**:
- Độ phức tạp: $$O(p^3)$$.
- Phù hợp khi số đặc trưng $$p < 10^4$$.
- Ổn định số học tốt nhờ số hạng điều chuẩn.

**Phương pháp lặp (Gradient descent)**:
- Độ phức tạp mỗi bước lặp: $$O(np)$$.
- Phù hợp khi số đặc trưng $$p$$ lớn.
- Tốc độ hội tụ phụ thuộc vào chỉ số điều kiện.

#### 2. Tiền điều kiện hóa (Preconditioning)

- **Tiền điều kiện Jacobi**: $$\mathbf{P} = 	ext{diag}(\mathbf{Q} + \lambda \mathbf{I})$$.
- **Hệ sau tiền điều kiện**: $$\mathbf{P}^{-1}(\mathbf{Q} + \lambda \mathbf{I})\mathbf{w} = \mathbf{P}^{-1}\mathbf{\mu}$$.
- **Lợi ích**: Cải thiện chỉ số điều kiện của hệ phương trình, giúp phương pháp lặp hội tụ nhanh hơn.

## Hồi quy Lasso (Điều chuẩn L1)

### Định nghĩa Toán học

Lasso (Least Absolute Shrinkage and Selection Operator) sử dụng chuẩn L1 làm số hạng điều chuẩn:

$$\min_{\mathbf{w}} rac{1}{2n} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2 + \lambda \|\mathbf{w}\|_1$$

trong đó $$\|\mathbf{w}\|_1 = \sum_{j=1}^p |w_j|$$.

### Đặc điểm Chính của Lasso

**1. Nghiệm thưa (Sparse Solutions):**
- Lasso có thể đưa nhiều hệ số về **chính xác bằng 0**.
- Tự động thực hiện **chọn lọc đặc trưng (feature selection)**.
- Tạo ra mô hình gọn nhẹ và dễ diễn giải hơn.

**2. Không có nghiệm dạng đóng tổng quát:**
- Cần giải bằng các thuật toán tối ưu lặp (như hạ tọa độ — coordinate descent, hoặc gradient gần kề — proximal gradient).
- Chi phí tối ưu thường phức tạp hơn hồi quy Ridge.

### So sánh Ridge và Lasso

<div id="ridge-lasso-comparison" style="margin: 20px 0;">
    <div style="margin-bottom: 15px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; background-color: #f0f8ff;">
        <h4>So sánh Ridge và Lasso Regularization</h4>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
            <div>
                <label for="comparison-lambda">Lambda (λ): </label>
                <input type="range" id="comparison-lambda" min="0" max="5" step="0.1" value="1">
                <span id="comparison-lambda-value">1.0</span>
            </div>
            <div>
                <label for="comparison-correlation">Feature Correlation: </label>
                <input type="range" id="comparison-correlation" min="0" max="0.9" step="0.1" value="0.5">
                <span id="comparison-correlation-value">0.5</span>
            </div>
        </div>
        <div style="margin-top: 10px;">
            <button id="comparison-update" style="background-color: #2196F3; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Cập nhật So sánh</button>
        </div>
    </div>
    
    <div style="display: flex; gap: 20px; justify-content: center;">
        <div style="text-align: center;">
            <h4>Ridge Coefficients</h4>
            <svg id="ridge-comparison" width="300" height="250" style="border: 1px solid #ddd;"></svg>
            <div style="margin-top: 5px; padding: 5px; background-color: #e8f5e8; border-radius: 4px;">
                <p style="margin: 0; font-size: 12px;">Shrinkage: Đều, không về 0</p>
            </div>
        </div>
        <div style="text-align: center;">
            <h4>Lasso Coefficients</h4>
            <svg id="lasso-comparison" width="300" height="250" style="border: 1px solid #ddd;"></svg>
            <div style="margin-top: 5px; padding: 5px; background-color: #fff3e0; border-radius: 4px;">
                <p style="margin: 0; font-size: 12px;">Sparsity: Một số về chính xác 0</p>
            </div>
        </div>
        <div style="text-align: center;">
            <h4>Regularization Geometry</h4>
            <svg id="regularization-geometry" width="300" height="250" style="border: 1px solid #ddd;"></svg>
            <div style="margin-top: 5px; padding: 5px; background-color: #f3e5f5; border-radius: 4px;">
                <p style="margin: 0; font-size: 12px;">L1: Diamond, L2: Circle</p>
            </div>
        </div>
    </div>
</div>

### Diễn giải Hình học của Điều chuẩn

**Vì sao Lasso tạo ra nghiệm thưa:**

1. **Miền ràng buộc L1**: $$\|\mathbf{w}\|_1 \leq t$$ có dạng **hình thoi** trong không gian hai chiều (có các đỉnh nhọn nằm trên trục tọa độ).
2. **Miền ràng buộc L2**: $$\|\mathbf{w}\|_2 \leq t$$ có dạng **hình tròn** trơn.
3. **Điểm tiếp xúc với đường đồng mức hàm mất mát**:
   - Với L1, đường đồng mức elip rất dễ tiếp xúc tại các đỉnh nhọn trên trục tọa độ, khiến một số thành phần của $$\mathbf{w}$$ bằng 0.
   - Với L2, biên hình tròn trơn nên điểm tiếp xúc thường nằm ngoài các trục tọa độ (các hệ số đều co nhỏ nhưng hiếm khi bằng 0 tuyệt đối).

## Elastic Net: Kết hợp Ridge và Lasso

Elastic Net kết hợp đồng thời hai số hạng phạt L1 và L2:

$$\min_{\mathbf{w}} rac{1}{2n} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|_2^2 + \lambda \left[ lpha \|\mathbf{w}\|_1 + rac{1-lpha}{2} \|\mathbf{w}\|_2^2 
ight]$$

**Vai trò tham số trộn $$lpha \in [0, 1]$$:**
- $$lpha = 1$$: Trở về hồi quy Lasso thuần túy.
- $$lpha = 0$$: Trở về hồi quy Ridge thuần túy.
- $$0 < lpha < 1$$: Kết hợp cả hai cơ chế.

**Ưu điểm:**
- Kết hợp tính thưa của Lasso với độ ổn định của Ridge.
- Xử lý tốt các nhóm biến có tương quan cao.
- Hoạt động ổn định cả khi số đặc trưng vượt quá số mẫu ($$p > n$$).

## Các Hàm Mất mát trong Học máy

### 1. Hàm Mất mát cho Hồi quy

#### Sai số Bình phương Trung bình (MSE)
$$L_{MSE}(\mathbf{w}) = rac{1}{n} \sum_{i=1}^n (y_i - \mathbf{w}^T \mathbf{x}_i)^2$$

**Đặc điểm:**
- Trơn và khả vi tại mọi điểm.
- Nhạy cảm với các điểm ngoại lai (outliers) do bình phương sai số.
- Tạo thành bài toán tối ưu lồi.

#### Sai số Tuyệt đối Trung bình (MAE)
$$L_{MAE}(\mathbf{w}) = rac{1}{n} \sum_{i=1}^n |y_i - \mathbf{w}^T \mathbf{x}_i|$$

**Đặc điểm:**
- Bền vững hơn trước các điểm ngoại lai.
- Không khả vi tại điểm sai số bằng 0.
- Lồi nhưng cần phương pháp dưới gradient (subgradient) hoặc quy hoạch tuyến tính.

#### Hàm Mất mát Huber (Huber Loss)
$$L_{Huber}(\mathbf{w}) = rac{1}{n} \sum_{i=1}^n egin{cases}
rac{1}{2}(y_i - \mathbf{w}^T \mathbf{x}_i)^2 & 	ext{nếu } |y_i - \mathbf{w}^T \mathbf{x}_i| \leq \delta \
\delta |y_i - \mathbf{w}^T \mathbf{x}_i| - rac{1}{2}\delta^2 & 	ext{ngược lại}
\end{cases}$$

**Đặc điểm:**
- Kết hợp ưu điểm của MSE (với sai số nhỏ) và MAE (với sai số lớn).
- Vừa trơn (khả vi liên tục) vừa bền vững trước ngoại lai.
- Tham số $$\delta$$ kiểm soát ngưỡng chuyển tiếp giữa phần bậc hai và phần tuyến tính.

### 2. Hàm Mất mát cho Phân lớp

#### Hàm Mất mát Logistic (Cross-Entropy)
$$L_{logistic}(\mathbf{w}) = rac{1}{n} \sum_{i=1}^n \log(1 + \exp(-y_i \mathbf{w}^T \mathbf{x}_i))$$

#### Hàm Mất mát Hinge (SVM)
$$L_{hinge}(\mathbf{w}) = rac{1}{n} \sum_{i=1}^n \max(0, 1 - y_i \mathbf{w}^T \mathbf{x}_i)$$

### Minh họa Tương tác: So sánh Các Hàm Mất mát

<div id="loss-functions-demo" style="margin: 20px 0;">
    <div style="margin-bottom: 15px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; background-color: #f9f9f9;">
        <h4>So sánh các Loss Functions</h4>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px;">
            <div>
                <label for="loss-delta">Huber Delta (δ): </label>
                <input type="range" id="loss-delta" min="0.5" max="3" step="0.1" value="1">
                <span id="loss-delta-value">1.0</span>
            </div>
            <div>
                <label for="loss-range">Error Range: </label>
                <input type="range" id="loss-range" min="2" max="8" step="0.5" value="4">
                <span id="loss-range-value">4.0</span>
            </div>
            <div>
                <label>
                    <input type="checkbox" id="show-derivatives"> Show Derivatives
                </label>
            </div>
        </div>
    </div>
    
    <div style="display: flex; gap: 20px; justify-content: center;">
        <div style="text-align: center;">
            <h4>Regression Loss Functions</h4>
            <svg id="regression-losses" width="400" height="300" style="border: 1px solid #ddd;"></svg>
            <div style="margin-top: 10px; padding: 8px; background-color: #f5f5f5; border-radius: 4px;">
                <div style="display: flex; gap: 15px; justify-content: center; font-size: 12px;">
                    <span style="color: #1f77b4;">■ MSE</span>
                    <span style="color: #ff7f0e;">■ MAE</span>
                    <span style="color: #2ca02c;">■ Huber</span>
                </div>
            </div>
        </div>
        <div style="text-align: center;">
            <h4>Classification Loss Functions</h4>
            <svg id="classification-losses" width="400" height="300" style="border: 1px solid #ddd;"></svg>
            <div style="margin-top: 10px; padding: 8px; background-color: #f5f5f5; border-radius: 4px;">
                <div style="display: flex; gap: 15px; justify-content: center; font-size: 12px;">
                    <span style="color: #d62728;">■ Logistic</span>
                    <span style="color: #9467bd;">■ Hinge</span>
                    <span style="color: #8c564b;">■ 0-1 Loss</span>
                </div>
            </div>
        </div>
    </div>
</div>

## Đường Điều chuẩn (Regularization Path) và Chọn Mô hình

### Kiểm định Chéo (Cross-Validation) để Chọn $$\lambda$$

Giá trị $$\lambda$$ tối ưu thường được xác định bằng kiểm định chéo:

1. **Chia tập dữ liệu**: Tách thành các tập huấn luyện (training), thẩm định (validation) và kiểm tra (test).
2. **Tìm kiếm lưới (grid search)**: Khảo sát dãy giá trị $$\lambda$$ theo thang logarit.
3. **Đánh giá**: Tính sai số trên tập thẩm định cho từng giá trị $$\lambda$$.
4. **Lựa chọn**: Chọn $$\lambda$$ cho sai số thẩm định thấp nhất.

### Minh họa Đường Điều chuẩn

<div id="regularization-path-demo" style="margin: 20px 0;">
    <div style="margin-bottom: 15px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; background-color: #f0f8ff;">
        <h4>Regularization Path Analysis</h4>
        <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px;">
            <div>
                <label for="path-method">Method: </label>
                <select id="path-method">
                    <option value="ridge">Ridge</option>
                    <option value="lasso">Lasso</option>
                    <option value="elastic">Elastic Net</option>
                </select>
            </div>
            <div>
                <label for="path-alpha">Elastic Net α: </label>
                <input type="range" id="path-alpha" min="0" max="1" step="0.1" value="0.5">
                <span id="path-alpha-value">0.5</span>
            </div>
            <div>
                <button id="path-animate" style="background-color: #FF9800; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Animate Path</button>
            </div>
        </div>
    </div>
    
    <div style="display: flex; gap: 20px; justify-content: center;">
        <div style="text-align: center;">
            <h4>Coefficient Path</h4>
            <svg id="coefficient-path" width="400" height="300" style="border: 1px solid #ddd;"></svg>
            <div style="margin-top: 10px; padding: 8px; background-color: #f5f5f5; border-radius: 4px;">
                <p id="path-info" style="margin: 0; font-size: 12px;">Current λ: 0, Active features: 0</p>
            </div>
        </div>
        <div style="text-align: center;">
            <h4>Cross-Validation Curve</h4>
            <svg id="cv-curve" width="400" height="300" style="border: 1px solid #ddd;"></svg>
            <div style="margin-top: 10px; padding: 8px; background-color: #f5f5f5; border-radius: 4px;">
                <p id="cv-info" style="margin: 0; font-size: 12px;">Optimal λ: 0, CV Score: 0</p>
            </div>
        </div>
    </div>
</div>

## Hướng dẫn Thực hành

### 1. Khi nào chọn Ridge hay Lasso?

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 20px 0;">
    <div style="border: 1px solid #4CAF50; padding: 15px; border-radius: 5px; background-color: #f1f8e9;">
        <h4 style="color: #4CAF50;">Nên dùng Ridge khi:</h4>
        <ul>
            <li>Phần lớn đặc trưng đều đóng góp thông tin</li>
            <li>Có hiện tượng đa cộng tuyến cao</li>
            <li>Ưu tiên tính ổn định của ước lượng</li>
            <li>Tập dữ liệu nhỏ nhưng nhiều đặc trưng</li>
            <li>Không cần loại bỏ đặc trưng tự động</li>
        </ul>
    </div>
    <div style="border: 1px solid #FF9800; padding: 15px; border-radius: 5px; background-color: #fff8e1;">
        <h4 style="color: #FF9800;">Nên dùng Lasso khi:</h4>
        <ul>
            <li>Cần chọn lọc đặc trưng tự động</li>
            <li>Nhiều đặc trưng thừa hoặc không liên quan</li>
            <li>Ưu tiên mô hình gọn nhẹ, dễ diễn giải</li>
            <li>Mong muốn nghiệm thưa</li>
            <li>Dữ liệu số chiều cao</li>
        </ul>
    </div>
</div>

### 2. Chiến lược Tinh chỉnh Siêu tham số

```python
# Mã giả tinh chỉnh tham số điều chuẩn
def tune_regularization(X_train, y_train, X_val, y_val):
    lambda_values = np.logspace(-4, 2, 50)  # Các giá trị cách đều theo thang log
    best_lambda = None
    best_score = float('inf')
    
    for lambda_val in lambda_values:
        model = fit_regularized_model(X_train, y_train, lambda_val)
        val_score = evaluate_model(model, X_val, y_val)
        
        if val_score < best_score:
            best_score = val_score
            best_lambda = lambda_val
    
    return best_lambda, best_score
```

### 3. Chuẩn hóa Đặc trưng (Feature Scaling)

**Lưu ý quan trọng**: Các phương pháp điều chuẩn rất nhạy cảm với thang đo của đặc trưng.

- **Ridge/Lasso**: Cần chuẩn hóa đặc trưng (standardization) trước khi huấn luyện.
- **Lý do**: Số hạng phạt phụ thuộc trực tiếp vào độ lớn của các hệ số $$w_j$$; nếu các đặc trưng có đơn vị đo chênh lệch lớn, mức phạt sẽ không công bằng giữa chúng.
- **Cách xử lý**: Đưa các đặc trưng về trung bình 0 và độ lệch chuẩn 1 trước khi áp dụng điều chuẩn.

## Tóm tắt

### Những Điểm Chính
1. **Điều chuẩn (Regularization)** giúp kiểm soát độ phức tạp mô hình và hạn chế quá khớp.
2. **Ridge (L2)** co nhỏ đồng đều các hệ số và tăng tính ổn định số học.
3. **Lasso (L1)** tạo ra nghiệm thưa và thực hiện chọn lọc đặc trưng tự động.
4. **Elastic Net** kết hợp ưu điểm của cả L1 và L2.
5. **Lựa chọn hàm mất mát** quyết định tính trơn và độ bền vững của mô hình trước nhiễu ngoại lai.
6. **Kiểm định chéo (Cross-validation)** là công cụ tiêu chuẩn để chọn siêu tham số $$\lambda$$.

### Quy trình Thực hành
1. **Tiền xử lý dữ liệu**: Chuẩn hóa thang đo các đặc trưng.
2. **Chọn phương pháp**: Dựa trên cấu trúc dữ liệu và mục tiêu bài toán.
3. **Tinh chỉnh siêu tham số**: Dùng kiểm định chéo trên lưới giá trị $$\lambda$$.
4. **Đánh giá mô hình**: Kiểm tra trên tập dữ liệu độc lập (test set).
5. **Phân tích kết quả**: Kiểm tra độ lớn và độ thưa của các hệ số học được.

Điều chuẩn là công cụ hiệu quả nhưng không thay thế được việc hiểu rõ dữ liệu và bản chất bài toán.

<script>
document.addEventListener('DOMContentLoaded', function() {
    // Quadratic Function Demo
    initializeQuadraticFunctionDemo();
    
    // Regularization Convergence Demo
    initializeRegularizationConvergenceDemo();
    
    // Ridge Effect Demo
    initializeRidgeEffectDemo();
    
    // Ridge vs Lasso Comparison
    initializeRidgeLassoComparison();
    
    // Loss Functions Demo
    initializeLossFunctionsDemo();
    
    // Regularization Path Demo
    initializeRegularizationPathDemo();
    
    function initializeRidgeEffectDemo() {
        const lambdaSlider = document.getElementById('ridge-lambda');
        const noiseSlider = document.getElementById('ridge-noise');
        const featuresSlider = document.getElementById('ridge-features');
        const regenerateBtn = document.getElementById('ridge-regenerate');
        
        let currentData = generateRidgeData();
        
        function generateRidgeData() {
            const n = 50; // samples
            const p = parseInt(featuresSlider.value); // features
            const noise = parseFloat(noiseSlider.value);
            
            // Generate true coefficients (sparse)
            const trueCoeffs = Array(p).fill(0).map((_, i) => 
                i < 3 ? (Math.random() - 0.5) * 4 : 0
            );
            
            // Generate X matrix
            const X = Array(n).fill().map(() => 
                Array(p).fill().map(() => Math.random() * 2 - 1)
            );
            
            // Generate y with noise
            const y = X.map(row => 
                row.reduce((sum, x, i) => sum + x * trueCoeffs[i], 0) + 
                (Math.random() - 0.5) * noise * 2
            );
            
            return { X, y, trueCoeffs, n, p };
        }
        
        function updateRidgeDemo() {
            const lambda = parseFloat(lambdaSlider.value);
            document.getElementById('ridge-lambda-value').textContent = lambda.toFixed(1);
            
            // Compute Ridge coefficients for different lambda values
            const lambdaRange = Array(50).fill().map((_, i) => i * 0.2);
            const coeffPaths = computeRidgeCoefficients(currentData, lambdaRange);
            
            // Update visualizations
            updateRidgeCoefficientsPlot(coeffPaths, lambdaRange, lambda);
            updateRidgeErrorPlot(currentData, lambdaRange);
        }
        
        function computeRidgeCoefficients(data, lambdaRange) {
            const { X, y, p } = data;
            const paths = Array(p).fill().map(() => []);
            
            lambdaRange.forEach(lambda => {
                const coeffs = solveRidge(X, y, lambda);
                coeffs.forEach((coeff, i) => paths[i].push(coeff));
            });
            
            return paths;
        }
        
        function solveRidge(X, y, lambda) {
            // Simplified Ridge solution: w = (X'X + λI)^(-1) X'y
            const p = X[0].length;
            const n = X.length;
            
            // Compute X'X
            const XtX = Array(p).fill().map(() => Array(p).fill(0));
            for (let i = 0; i < p; i++) {
                for (let j = 0; j < p; j++) {
                    for (let k = 0; k < n; k++) {
                        XtX[i][j] += X[k][i] * X[k][j];
                    }
                }
            }
            
            // Add λI
            for (let i = 0; i < p; i++) {
                XtX[i][i] += lambda;
            }
            
            // Compute X'y
            const Xty = Array(p).fill(0);
            for (let i = 0; i < p; i++) {
                for (let k = 0; k < n; k++) {
                    Xty[i] += X[k][i] * y[k];
                }
            }
            
            // Solve linear system (simplified - using pseudo-inverse)
            return solveLinearSystem(XtX, Xty);
        }
        
        function solveLinearSystem(A, b) {
            // Simplified solution using Gaussian elimination
            const n = A.length;
            const coeffs = Array(n).fill(0);
            
            // For demo purposes, use a simplified approach
            for (let i = 0; i < n; i++) {
                coeffs[i] = b[i] / (A[i][i] + 1e-10);
            }
            
            return coeffs;
        }
        
        function updateRidgeCoefficientsPlot(coeffPaths, lambdaRange, currentLambda) {
            const svg = d3.select('#ridge-coefficients');
            svg.selectAll('*').remove();
            
            const margin = {top: 20, right: 20, bottom: 40, left: 50};
            const width = 400 - margin.left - margin.right;
            const height = 300 - margin.top - margin.bottom;
            
            const g = svg.append('g')
                .attr('transform', `translate(${margin.left},${margin.top})`);
            
            // Scales
            const xScale = d3.scaleLinear()
                .domain(d3.extent(lambdaRange))
                .range([0, width]);
            
            const allCoeffs = coeffPaths.flat();
            const yScale = d3.scaleLinear()
                .domain(d3.extent(allCoeffs))
                .nice()
                .range([height, 0]);
            
            // Axes
            g.append('g')
                .attr('transform', `translate(0,${height})`)
                .call(d3.axisBottom(xScale));
            
            g.append('g')
                .call(d3.axisLeft(yScale));
            
            // Axis labels
            g.append('text')
                .attr('transform', `translate(${width/2},${height + 35})`)
                .style('text-anchor', 'middle')
                .text('Lambda (λ)');
            
            g.append('text')
                .attr('transform', 'rotate(-90)')
                .attr('y', 0 - margin.left)
                .attr('x', 0 - height/2)
                .attr('dy', '1em')
                .style('text-anchor', 'middle')
                .text('Coefficient Value');
            
            // Line generator
            const line = d3.line()
                .x((d, i) => xScale(lambdaRange[i]))
                .y(d => yScale(d));
            
            // Draw coefficient paths
            const colors = d3.schemeCategory10;
            coeffPaths.forEach((path, i) => {
                g.append('path')
                    .datum(path)
                    .attr('fill', 'none')
                    .attr('stroke', colors[i % colors.length])
                    .attr('stroke-width', 2)
                    .attr('d', line);
            });
            
            // Current lambda line
            g.append('line')
                .attr('x1', xScale(currentLambda))
                .attr('x2', xScale(currentLambda))
                .attr('y1', 0)
                .attr('y2', height)
                .attr('stroke', 'red')
                .attr('stroke-width', 2)
                .attr('stroke-dasharray', '5,5');
            
            // Update info
            const currentIndex = Math.round(currentLambda / 0.2);
            const currentCoeffs = coeffPaths.map(path => path[currentIndex] || 0);
            const l2Norm = Math.sqrt(currentCoeffs.reduce((sum, c) => sum + c*c, 0));
            document.getElementById('ridge-coeff-info').textContent = 
                `L2 Norm của coefficients: ${l2Norm.toFixed(3)}`;
        }
        
        function updateRidgeErrorPlot(data, lambdaRange) {
            // Simplified error computation for demo
            const svg = d3.select('#ridge-error');
            svg.selectAll('*').remove();
            
            const margin = {top: 20, right: 20, bottom: 40, left: 50};
            const width = 400 - margin.left - margin.right;
            const height = 300 - margin.top - margin.bottom;
            
            const g = svg.append('g')
                .attr('transform', `translate(${margin.left},${margin.top})`);
            
            // Generate synthetic error curves
            const trainErrors = lambdaRange.map(lambda => 
                0.1 + 0.5 * lambda + Math.random() * 0.1
            );
            const valErrors = lambdaRange.map(lambda => 
                0.3 + 0.2 * Math.abs(lambda - 2) + Math.random() * 0.1
            );
            
            // Scales
            const xScale = d3.scaleLinear()
                .domain(d3.extent(lambdaRange))
                .range([0, width]);
            
            const yScale = d3.scaleLinear()
                .domain([0, Math.max(...trainErrors, ...valErrors)])
                .nice()
                .range([height, 0]);
            
            // Axes
            g.append('g')
                .attr('transform', `translate(0,${height})`)
                .call(d3.axisBottom(xScale));
            
            g.append('g')
                .call(d3.axisLeft(yScale));
            
            // Axis labels
            g.append('text')
                .attr('transform', `translate(${width/2},${height + 35})`)
                .style('text-anchor', 'middle')
                .text('Lambda (λ)');
            
            g.append('text')
                .attr('transform', 'rotate(-90)')
                .attr('y', 0 - margin.left)
                .attr('x', 0 - height/2)
                .attr('dy', '1em')
                .style('text-anchor', 'middle')
                .text('Error');
            
            // Line generator
            const line = d3.line()
                .x((d, i) => xScale(lambdaRange[i]))
                .y(d => yScale(d));
            
            // Draw error curves
            g.append('path')
                .datum(trainErrors)
                .attr('fill', 'none')
                .attr('stroke', 'blue')
                .attr('stroke-width', 2)
                .attr('d', line);
            
            g.append('path')
                .datum(valErrors)
                .attr('fill', 'none')
                .attr('stroke', 'red')
                .attr('stroke-width', 2)
                .attr('d', line);
            
            // Legend
            const legend = g.append('g')
                .attr('transform', `translate(${width - 100}, 20)`);
            
            legend.append('line')
                .attr('x1', 0).attr('x2', 20)
                .attr('y1', 0).attr('y2', 0)
                .attr('stroke', 'blue').attr('stroke-width', 2);
            legend.append('text')
                .attr('x', 25).attr('y', 5)
                .text('Training');
            
            legend.append('line')
                .attr('x1', 0).attr('x2', 20)
                .attr('y1', 15).attr('y2', 15)
                .attr('stroke', 'red').attr('stroke-width', 2);
            legend.append('text')
                .attr('x', 25).attr('y', 20)
                .text('Validation');
            
            // Find optimal lambda
            const optimalIndex = valErrors.indexOf(Math.min(...valErrors));
            const optimalLambda = lambdaRange[optimalIndex];
            document.getElementById('ridge-error-info').textContent = 
                `Optimal λ: ${optimalLambda.toFixed(2)}`;
        }
        
        // Event listeners
        lambdaSlider.addEventListener('input', updateRidgeDemo);
        noiseSlider.addEventListener('input', function() {
            document.getElementById('ridge-noise-value').textContent = this.value;
        });
        featuresSlider.addEventListener('input', function() {
            document.getElementById('ridge-features-value').textContent = this.value;
        });
        
        regenerateBtn.addEventListener('click', function() {
            currentData = generateRidgeData();
            updateRidgeDemo();
        });
        
        // Initial update
        updateRidgeDemo();
    }
    
    function initializeRidgeLassoComparison() {
        const lambdaSlider = document.getElementById('comparison-lambda');
        const correlationSlider = document.getElementById('comparison-correlation');
        const updateBtn = document.getElementById('comparison-update');
        
        function updateComparison() {
            const lambda = parseFloat(lambdaSlider.value);
            const correlation = parseFloat(correlationSlider.value);
            
            document.getElementById('comparison-lambda-value').textContent = lambda.toFixed(1);
            document.getElementById('comparison-correlation-value').textContent = correlation.toFixed(1);
            
            // Generate synthetic data with controlled correlation
            const p = 8; // features
            const trueCoeffs = [2, -1.5, 1, 0.5, -0.8, 0, 0, 0];
            
            // Compute Ridge and Lasso coefficients
            const ridgeCoeffs = computeRidgeCoeffs(trueCoeffs, lambda, correlation);
            const lassoCoeffs = computeLassoCoeffs(trueCoeffs, lambda, correlation);
            
            // Update visualizations
            updateComparisonPlot('ridge-comparison', ridgeCoeffs, 'Ridge');
            updateComparisonPlot('lasso-comparison', lassoCoeffs, 'Lasso');
            updateGeometryPlot(lambda);
        }
        
        function computeRidgeCoeffs(trueCoeffs, lambda, correlation) {
            // Simplified Ridge shrinkage
            const shrinkageFactor = 1 / (1 + lambda);
            return trueCoeffs.map(coeff => coeff * shrinkageFactor);
        }
        
        function computeLassoCoeffs(trueCoeffs, lambda, correlation) {
            // Simplified Lasso soft thresholding
            return trueCoeffs.map(coeff => {
                const absCoeff = Math.abs(coeff);
                if (absCoeff <= lambda) return 0;
                return Math.sign(coeff) * (absCoeff - lambda);
            });
        }
        
        function updateComparisonPlot(svgId, coeffs, title) {
            const svg = d3.select(`#${svgId}`);
            svg.selectAll('*').remove();
            
            const margin = {top: 20, right: 20, bottom: 40, left: 40};
            const width = 300 - margin.left - margin.right;
            const height = 250 - margin.top - margin.bottom;
            
            const g = svg.append('g')
                .attr('transform', `translate(${margin.left},${margin.top})`);
            
            // Scales
            const xScale = d3.scaleBand()
                .domain(coeffs.map((_, i) => `w${i+1}`))
                .range([0, width])
                .padding(0.1);
            
            const yScale = d3.scaleLinear()
                .domain(d3.extent(coeffs))
                .nice()
                .range([height, 0]);
            
            // Axes
            g.append('g')
                .attr('transform', `translate(0,${height})`)
                .call(d3.axisBottom(xScale));
            
            g.append('g')
                .call(d3.axisLeft(yScale));
            
            // Bars
            const color = title === 'Ridge' ? '#4CAF50' : '#FF9800';
            g.selectAll('.bar')
                .data(coeffs)
                .enter().append('rect')
                .attr('class', 'bar')
                .attr('x', (d, i) => xScale(`w${i+1}`))
                .attr('width', xScale.bandwidth())
                .attr('y', d => d >= 0 ? yScale(d) : yScale(0))
                .attr('height', d => Math.abs(yScale(d) - yScale(0)))
                .attr('fill', color);
            
            // Zero line
            g.append('line')
                .attr('x1', 0)
                .attr('x2', width)
                .attr('y1', yScale(0))
                .attr('y2', yScale(0))
                .attr('stroke', 'black')
                .attr('stroke-width', 1);
        }
        
        function updateGeometryPlot(lambda) {
            const svg = d3.select('#regularization-geometry');
            svg.selectAll('*').remove();
            
            const margin = {top: 20, right: 20, bottom: 40, left: 40};
            const width = 300 - margin.left - margin.right;
            const height = 250 - margin.top - margin.bottom;
            
            const g = svg.append('g')
                .attr('transform', `translate(${margin.left},${margin.top})`);
            
            const centerX = width / 2;
            const centerY = height / 2;
            const radius = Math.min(width, height) / 3;
            
            // L2 constraint (circle)
            g.append('circle')
                .attr('cx', centerX)
                .attr('cy', centerY)
                .attr('r', radius)
                .attr('fill', 'none')
                .attr('stroke', '#4CAF50')
                .attr('stroke-width', 3)
                .attr('opacity', 0.7);
            
            // L1 constraint (diamond)
            const diamondPoints = [
                [centerX, centerY - radius],
                [centerX + radius, centerY],
                [centerX, centerY + radius],
                [centerX - radius, centerY]
            ];
            
            const line = d3.line()
                .x(d => d[0])
                .y(d => d[1]);
            
            g.append('path')
                .datum([...diamondPoints, diamondPoints[0]])
                .attr('d', line)
                .attr('fill', 'none')
                .attr('stroke', '#FF9800')
                .attr('stroke-width', 3)
                .attr('opacity', 0.7);
            
            // Contour lines (ellipses)
            for (let i = 1; i <= 3; i++) {
                g.append('ellipse')
                    .attr('cx', centerX + 20)
                    .attr('cy', centerY - 10)
                    .attr('rx', i * 15)
                    .attr('ry', i * 25)
                    .attr('fill', 'none')
                    .attr('stroke', '#666')
                    .attr('stroke-width', 1)
                    .attr('stroke-dasharray', '3,3')
                    .attr('opacity', 0.5);
            }
            
            // Labels
            g.append('text')
                .attr('x', centerX + radius + 10)
                .attr('y', centerY + 5)
                .text('L2')
                .attr('fill', '#4CAF50')
                .attr('font-weight', 'bold');
            
            g.append('text')
                .attr('x', centerX + radius/Math.sqrt(2) + 5)
                .attr('y', centerY - radius/Math.sqrt(2) - 5)
                .text('L1')
                .attr('fill', '#FF9800')
                .attr('font-weight', 'bold');
        }
        
        // Event listeners
        lambdaSlider.addEventListener('input', updateComparison);
        correlationSlider.addEventListener('input', updateComparison);
        updateBtn.addEventListener('click', updateComparison);
        
        // Initial update
        updateComparison();
    }
    
    function initializeLossFunctionsDemo() {
        const deltaSlider = document.getElementById('loss-delta');
        const rangeSlider = document.getElementById('loss-range');
        const derivativesCheckbox = document.getElementById('show-derivatives');
        
        function updateLossFunctions() {
            const delta = parseFloat(deltaSlider.value);
            const range = parseFloat(rangeSlider.value);
            const showDerivatives = derivativesCheckbox.checked;
            
            document.getElementById('loss-delta-value').textContent = delta.toFixed(1);
            document.getElementById('loss-range-value').textContent = range.toFixed(1);
            
            updateRegressionLosses(delta, range, showDerivatives);
            updateClassificationLosses(range, showDerivatives);
        }
        
        function updateRegressionLosses(delta, range, showDerivatives) {
            const svg = d3.select('#regression-losses');
            svg.selectAll('*').remove();
            
            const margin = {top: 20, right: 20, bottom: 40, left: 50};
            const width = 400 - margin.left - margin.right;
            const height = 300 - margin.top - margin.bottom;
            
            const g = svg.append('g')
                .attr('transform', `translate(${margin.left},${margin.top})`);
            
            // Generate error values
            const errors = d3.range(-range, range, 0.1);
            
            // Loss functions
            const mseLoss = errors.map(e => 0.5 * e * e);
            const maeLoss = errors.map(e => Math.abs(e));
            const huberLoss = errors.map(e => 
                Math.abs(e) <= delta ? 0.5 * e * e : delta * Math.abs(e) - 0.5 * delta * delta
            );
            
            // Scales
            const xScale = d3.scaleLinear()
                .domain([-range, range])
                .range([0, width]);
            
            const maxLoss = Math.max(...mseLoss, ...maeLoss, ...huberLoss);
            const yScale = d3.scaleLinear()
                .domain([0, maxLoss])
                .nice()
                .range([height, 0]);
            
            // Axes
            g.append('g')
                .attr('transform', `translate(0,${height})`)
                .call(d3.axisBottom(xScale));
            
            g.append('g')
                .call(d3.axisLeft(yScale));
            
            // Axis labels
            g.append('text')
                .attr('transform', `translate(${width/2},${height + 35})`)
                .style('text-anchor', 'middle')
                .text('Prediction Error');
            
            g.append('text')
                .attr('transform', 'rotate(-90)')
                .attr('y', 0 - margin.left)
                .attr('x', 0 - height/2)
                .attr('dy', '1em')
                .style('text-anchor', 'middle')
                .text('Loss');
            
            // Line generator
            const line = d3.line()
                .x((d, i) => xScale(errors[i]))
                .y(d => yScale(d));
            
            // Draw loss functions
            const colors = ['#1f77b4', '#ff7f0e', '#2ca02c'];
            const losses = [mseLoss, maeLoss, huberLoss];
            const names = ['MSE', 'MAE', 'Huber'];
            
            losses.forEach((loss, i) => {
                g.append('path')
                    .datum(loss)
                    .attr('fill', 'none')
                    .attr('stroke', colors[i])
                    .attr('stroke-width', 3)
                    .attr('d', line);
            });
            
            // Legend
            const legend = g.append('g')
                .attr('transform', `translate(${width - 80}, 20)`);
            
            names.forEach((name, i) => {
                legend.append('line')
                    .attr('x1', 0).attr('x2', 20)
                    .attr('y1', i * 20).attr('y2', i * 20)
                    .attr('stroke', colors[i]).attr('stroke-width', 3);
                legend.append('text')
                    .attr('x', 25).attr('y', i * 20 + 5)
                    .text(name);
            });
        }
        
        function updateClassificationLosses(range, showDerivatives) {
            const svg = d3.select('#classification-losses');
            svg.selectAll('*').remove();
            
            const margin = {top: 20, right: 20, bottom: 40, left: 50};
            const width = 400 - margin.left - margin.right;
            const height = 300 - margin.top - margin.bottom;
            
            const g = svg.append('g')
                .attr('transform', `translate(${margin.left},${margin.top})`);
            
            // Generate margin values (y * f(x))
            const margins = d3.range(-range, range, 0.1);
            
            // Loss functions
            const logisticLoss = margins.map(m => Math.log(1 + Math.exp(-m)));
            const hingeLoss = margins.map(m => Math.max(0, 1 - m));
            const zeroOneLoss = margins.map(m => m <= 0 ? 1 : 0);
            
            // Scales
            const xScale = d3.scaleLinear()
                .domain([-range, range])
                .range([0, width]);
            
            const maxLoss = Math.max(...logisticLoss, ...hingeLoss, ...zeroOneLoss);
            const yScale = d3.scaleLinear()
                .domain([0, maxLoss])
                .nice()
                .range([height, 0]);
            
            // Axes
            g.append('g')
                .attr('transform', `translate(0,${height})`)
                .call(d3.axisBottom(xScale));
            
            g.append('g')
                .call(d3.axisLeft(yScale));
            
            // Axis labels
            g.append('text')
                .attr('transform', `translate(${width/2},${height + 35})`)
                .style('text-anchor', 'middle')
                .text('Margin (y × f(x))');
            
            g.append('text')
                .attr('transform', 'rotate(-90)')
                .attr('y', 0 - margin.left)
                .attr('x', 0 - height/2)
                .attr('dy', '1em')
                .style('text-anchor', 'middle')
                .text('Loss');
            
            // Line generator
            const line = d3.line()
                .x((d, i) => xScale(margins[i]))
                .y(d => yScale(d));
            
            // Draw loss functions
            const colors = ['#d62728', '#9467bd', '#8c564b'];
            const losses = [logisticLoss, hingeLoss, zeroOneLoss];
            const names = ['Logistic', 'Hinge', '0-1 Loss'];
            
            losses.forEach((loss, i) => {
                g.append('path')
                    .datum(loss)
                    .attr('fill', 'none')
                    .attr('stroke', colors[i])
                    .attr('stroke-width', 3)
                    .attr('d', line);
            });
            
            // Legend
            const legend = g.append('g')
                .attr('transform', `translate(${width - 80}, 20)`);
            
            names.forEach((name, i) => {
                legend.append('line')
                    .attr('x1', 0).attr('x2', 20)
                    .attr('y1', i * 20).attr('y2', i * 20)
                    .attr('stroke', colors[i]).attr('stroke-width', 3);
                legend.append('text')
                    .attr('x', 25).attr('y', i * 20 + 5)
                    .text(name);
            });
        }
        
        // Event listeners
        deltaSlider.addEventListener('input', updateLossFunctions);
        rangeSlider.addEventListener('input', updateLossFunctions);
        derivativesCheckbox.addEventListener('change', updateLossFunctions);
        
        // Initial update
        updateLossFunctions();
    }
    
    function initializeRegularizationPathDemo() {
        const methodSelect = document.getElementById('path-method');
        const alphaSlider = document.getElementById('path-alpha');
        const animateBtn = document.getElementById('path-animate');
        
        let isAnimating = false;
        let animationId = null;
        
        function updateRegularizationPath() {
            const method = methodSelect.value;
            const alpha = parseFloat(alphaSlider.value);
            
            document.getElementById('path-alpha-value').textContent = alpha.toFixed(1);
            
            // Generate regularization path
            const lambdaRange = d3.range(0, 5, 0.1);
            const coeffPaths = generateRegularizationPath(method, alpha, lambdaRange);
            
            updateCoefficientPathPlot(coeffPaths, lambdaRange, method);
            updateCVCurvePlot(lambdaRange, method);
        }
        
        function generateRegularizationPath(method, alpha, lambdaRange) {
            const p = 6; // features
            const trueCoeffs = [2, -1.5, 1, 0.5, -0.8, 0.3];
            
            const paths = Array(p).fill().map(() => []);
            
            lambdaRange.forEach(lambda => {
                let coeffs;
                if (method === 'ridge') {
                    coeffs = trueCoeffs.map(c => c / (1 + lambda));
                } else if (method === 'lasso') {
                    coeffs = trueCoeffs.map(c => {
                        const abs_c = Math.abs(c);
                        return abs_c > lambda ? Math.sign(c) * (abs_c - lambda) : 0;
                    });
                } else { // elastic net
                    coeffs = trueCoeffs.map(c => {
                        const abs_c = Math.abs(c);
                        const l1_part = abs_c > alpha * lambda ? Math.sign(c) * (abs_c - alpha * lambda) : 0;
                        return l1_part / (1 + (1 - alpha) * lambda);
                    });
                }
                
                coeffs.forEach((coeff, i) => paths[i].push(coeff));
            });
            
            return paths;
        }
        
        function updateCoefficientPathPlot(coeffPaths, lambdaRange, method) {
            const svg = d3.select('#coefficient-path');
            svg.selectAll('*').remove();
            
            const margin = {top: 20, right: 20, bottom: 40, left: 50};
            const width = 400 - margin.left - margin.right;
            const height = 300 - margin.top - margin.bottom;
            
            const g = svg.append('g')
                .attr('transform', `translate(${margin.left},${margin.top})`);
            
            // Scales
            const xScale = d3.scaleLinear()
                .domain(d3.extent(lambdaRange))
                .range([0, width]);
            
            const allCoeffs = coeffPaths.flat();
            const yScale = d3.scaleLinear()
                .domain(d3.extent(allCoeffs))
                .nice()
                .range([height, 0]);
            
            // Axes
            g.append('g')
                .attr('transform', `translate(0,${height})`)
                .call(d3.axisBottom(xScale));
            
            g.append('g')
                .call(d3.axisLeft(yScale));
            
            // Axis labels
            g.append('text')
                .attr('transform', `translate(${width/2},${height + 35})`)
                .style('text-anchor', 'middle')
                .text('Lambda (λ)');
            
            g.append('text')
                .attr('transform', 'rotate(-90)')
                .attr('y', 0 - margin.left)
                .attr('x', 0 - height/2)
                .attr('dy', '1em')
                .style('text-anchor', 'middle')
                .text('Coefficient Value');
            
            // Line generator
            const line = d3.line()
                .x((d, i) => xScale(lambdaRange[i]))
                .y(d => yScale(d));
            
            // Draw coefficient paths
            const colors = d3.schemeCategory10;
            coeffPaths.forEach((path, i) => {
                g.append('path')
                    .datum(path)
                    .attr('fill', 'none')
                    .attr('stroke', colors[i % colors.length])
                    .attr('stroke-width', 2)
                    .attr('d', line);
                
                // Add feature label at the end
                const lastValue = path[path.length - 1];
                if (Math.abs(lastValue) > 0.01) {
                    g.append('text')
                        .attr('x', width + 5)
                        .attr('y', yScale(lastValue) + 3)
                        .attr('font-size', '10px')
                        .text(`f${i+1}`);
                }
            });
            
            // Update info
            const currentLambda = 1.0; // example
            const activeFeatures = coeffPaths.filter(path => Math.abs(path[Math.floor(currentLambda * 10)]) > 0.01).length;
            document.getElementById('path-info').textContent = 
                `Current λ: ${currentLambda.toFixed(1)}, Active features: ${activeFeatures}`;
        }
        
        function updateCVCurvePlot(lambdaRange, method) {
            const svg = d3.select('#cv-curve');
            svg.selectAll('*').remove();
            
            const margin = {top: 20, right: 20, bottom: 40, left: 50};
            const width = 400 - margin.left - margin.right;
            const height = 300 - margin.top - margin.bottom;
            
            const g = svg.append('g')
                .attr('transform', `translate(${margin.left},${margin.top})`);
            
            // Generate synthetic CV scores
            const cvScores = lambdaRange.map(lambda => {
                const base = 0.2 + 0.1 * Math.abs(lambda - 1.5);
                return base + (Math.random() - 0.5) * 0.05;
            });
            
            // Scales
            const xScale = d3.scaleLinear()
                .domain(d3.extent(lambdaRange))
                .range([0, width]);
            
            const yScale = d3.scaleLinear()
                .domain(d3.extent(cvScores))
                .nice()
                .range([height, 0]);
            
            // Axes
            g.append('g')
                .attr('transform', `translate(0,${height})`)
                .call(d3.axisBottom(xScale));
            
            g.append('g')
                .call(d3.axisLeft(yScale));
            
            // Axis labels
            g.append('text')
                .attr('transform', `translate(${width/2},${height + 35})`)
                .style('text-anchor', 'middle')
                .text('Lambda (λ)');
            
            g.append('text')
                .attr('transform', 'rotate(-90)')
                .attr('y', 0 - margin.left)
                .attr('x', 0 - height/2)
                .attr('dy', '1em')
                .style('text-anchor', 'middle')
                .text('CV Score');
            
            // Line generator
            const line = d3.line()
                .x((d, i) => xScale(lambdaRange[i]))
                .y(d => yScale(d));
            
            // Draw CV curve
            g.append('path')
                .datum(cvScores)
                .attr('fill', 'none')
                .attr('stroke', '#2196F3')
                .attr('stroke-width', 3)
                .attr('d', line);
            
            // Find and mark optimal lambda
            const minIndex = cvScores.indexOf(Math.min(...cvScores));
            const optimalLambda = lambdaRange[minIndex];
            
            g.append('circle')
                .attr('cx', xScale(optimalLambda))
                .attr('cy', yScale(cvScores[minIndex]))
                .attr('r', 5)
                .attr('fill', 'red');
            
            // Update info
            document.getElementById('cv-info').textContent = 
                `Optimal λ: ${optimalLambda.toFixed(2)}, CV Score: ${cvScores[minIndex].toFixed(3)}`;
        }
        
        function animatePath() {
            if (isAnimating) {
                // Stop animation
                isAnimating = false;
                if (animationId) clearInterval(animationId);
                animateBtn.textContent = 'Animate Path';
                return;
            }
            
            // Start animation
            isAnimating = true;
            animateBtn.textContent = 'Stop Animation';
            
            const lambdaRange = d3.range(0, 5, 0.1);
            let currentIndex = 0;
            
            animationId = setInterval(() => {
                if (currentIndex >= lambdaRange.length) {
                    currentIndex = 0;
                }
                
                // Update visualization for current lambda
                const currentLambda = lambdaRange[currentIndex];
                // Add animation logic here
                
                currentIndex++;
            }, 100);
        }
        
        // Event listeners
        methodSelect.addEventListener('change', updateRegularizationPath);
        alphaSlider.addEventListener('input', updateRegularizationPath);
        animateBtn.addEventListener('click', animatePath);
        
        // Initial update
        updateRegularizationPath();
    }
});
</script>
