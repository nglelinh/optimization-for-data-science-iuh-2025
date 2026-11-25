---
layout: post
title: 05-02-03 Hồi Quy Tuyến Tính từ Góc Nhìn Thống Kê
chapter: '05'
order: 7
owner: AI Assistant
categories:
- chapter05
lang: vi
---

Khi học Bình phương tối thiểu ở bài trước, một câu hỏi đầy hoài nghi thường nảy ra: *tại sao lại tối thiểu hóa tổng **bình phương** sai số $$\sum (y_i - x_i^T \beta)^2$$ chứ không phải tổng trị tuyệt đối hay tổng lập phương?* Câu trả lời bất ngờ đến từ thống kê học: việc chọn chuẩn bình phương không hề là một sự tùy hứng hình học!

Nếu bạn giả định dữ liệu sinh ra bởi một quy luật tuyến tính cộng thêm nhiễu Gaussian độc lập $$\epsilon_i \sim \mathcal{N}(0, \sigma^2)$$, thì việc đi tìm bộ tham số $$\beta$$ làm cho dữ liệu quan sát được có xác suất xuất hiện cao nhất (**Ước lượng Hợp lý Tối đa — MLE**) sẽ dẫn ra **chính xác từng dấu phẩy** bài toán tối ưu lồi Bình phương tối thiểu! Bài học này bắc cây cầu giữa Tối ưu hóa Lồi và Thống kê Suy luận.

## Bản đồ kiến thức nền: Khi Tối ưu hóa Lồi gặp Thống kê Xác suất

Bốn trụ cột dưới đây kết nối hàm mất mát tối ưu với mô hình xác suất sinh dữ liệu:

- **Mô hình sinh dữ liệu Gaussian (Probabilistic Generative Model):** Giả định $$y_i = x_i^T \beta + \epsilon_i$$ với $$\epsilon_i \stackrel{\text{i.i.d.}}{\sim} \mathcal{N}(0, \sigma^2)$$ tương đương với phân phối có điều kiện $$y_i \mid x_i \sim \mathcal{N}(x_i^T \beta, \sigma^2)$$.
- **Hàm Hợp lý & Phép biến đổi Log-Likelihood:** Hàm hợp lý $$L(\beta) = \prod_{i=1}^n p(y_i \mid x_i; \beta)$$ là tích của nhiều hàm mũ — rất khó tối ưu trực tiếp và dễ tràn số dưới (underflow). Nhờ $$\log$$ là hàm đơn điệu tăng (Chương 04!), cực đại hóa $$L(\beta)$$ tương đương cực đại hóa $$\ell(\beta) = \sum_{i=1}^n \log p(y_i \mid x_i; \beta)$$, và cực tiểu hóa **Negative Log-Likelihood (NLL)** cho ngay bài toán lồi $$\frac{1}{2\sigma^2}\sum_{i=1}^n (y_i - x_i^T \beta)^2$$!
- **Phân phối nhiễu quyết định Hàm mất mát:** Đổi giả định nhiễu từ Gaussian sang **Laplace** ($$\exp(-|\epsilon|/b)$$) sẽ biến NLL thành hồi quy chuẩn $$\ell_1$$ (bền vững trước ngoại lai)! Còn thêm phân phối tiên nghiệm Gaussian lên $$\beta$$ (ước lượng MAP) sẽ sinh ra đúng hồi quy **Ridge ($$\ell_2$$)**, và tiên nghiệm Laplace sinh ra **Lasso ($$\ell_1$$)**!
- **Định lý Gauss–Markov & Độ bất định của ước lượng:** Không chỉ cho điểm tối ưu $$\hat{\beta}_{\text{MLE}}$$, góc nhìn thống kê còn cho ta ma trận hiệp phương sai $$\operatorname{Cov}(\hat{\beta}) = \sigma^2 (X^T X)^{-1}$$ để tính khoảng tin cậy và kiểm định giả thuyết.

### Khung giải thích (nên đọc chậm): Tính tay hàm Log-Likelihood và kiểm chứng MLE trùng khớp với OLS

Xét mô hình 1 tham số không hệ số chặn $$y_i = \beta x_i + \epsilon_i$$ với $$\epsilon_i \sim \mathcal{N}(0, \sigma^2 = 4)$$ trên 2 quan sát: $$(x_1, y_1) = (1, 2)$$ và $$(x_2, y_2) = (2, 5)$$.

1. **Bước 1 — Viết hàm mật độ hợp lý:**
   $$L(\beta) = \frac{1}{\sqrt{2\pi \cdot 4}} \exp\left(-\frac{(2 - \beta)^2}{8}\right) \cdot \frac{1}{\sqrt{2\pi \cdot 4}} \exp\left(-\frac{(5 - 2\beta)^2}{8}\right).$$
2. **Bước 2 — Lấy âm logarit (Negative Log-Likelihood):**
   $$-\ell(\beta) = \log(8\pi) + \frac{1}{8}\Big[(2 - \beta)^2 + (5 - 2\beta)^2\Big].$$
   Hằng số $$\log(8\pi)$$ và hệ số dương $$\frac{1}{8}$$ không ảnh hưởng đến vị trí cực tiểu!
3. **Bước 3 — Cực tiểu hóa phần bình phương sai số:**
   $$S(\beta) = (2 - \beta)^2 + (5 - 2\beta)^2 = (4 - 4\beta + \beta^2) + (25 - 20\beta + 4\beta^2) = 5\beta^2 - 24\beta + 29.$$
   Đạo hàm: $$S'(\beta) = 10\beta - 24 = 0 \implies \hat{\beta}_{\text{MLE}} = 2.4$$.
4. **Bước 4 — Tính phương sai ước lượng:**
   Vì $$X^T X = 1^2 + 2^2 = 5$$ và $$\sigma^2 = 4$$, ta có $$\operatorname{Var}(\hat{\beta}_{\text{MLE}}) = \frac{\sigma^2}{X^T X} = \frac{4}{5} = 0.8$$ (độ lệch chuẩn $$\approx 0.894$$). Góc nhìn thống kê cho ta không chỉ con số $$2.4$$, mà cả thước đo mức độ tin cậy của nó!

---

## Hồi Quy Tuyến Tính từ Góc Nhìn Thống Kê

Trong bài học này, chúng ta khám phá hồi quy tuyến tính từ góc nhìn xác suất và thống kê, cho thấy việc cực tiểu hóa sai số bình phương trung bình (MSE) không chỉ có ý nghĩa trực quan mà còn có cơ sở lý thuyết chặt chẽ thông qua ước lượng hợp lý cực đại (Maximum Likelihood Estimation - MLE).

### 1. Diễn Giải Xác Suất của Hồi Quy Tuyến Tính

Dưới góc nhìn xác suất, nghiệm của bài toán hồi quy tuyến tính thu được từ việc cực tiểu hóa MSE có thể được lý giải trực tiếp bằng mô hình nhiễu thống kê.

Thật vậy, chúng ta giả định biến mục tiêu và biến đầu vào liên hệ với nhau qua phương trình:

$$y_i = \mathbf{w}^\top \mathbf{x}_i + \epsilon_i$$

trong đó $$\epsilon_i$$ biểu diễn sai số ngẫu nhiên (những yếu tố không được mô hình giải thích). Theo các giả thiết Gauss–Markov cổ điển, sai số ngẫu nhiên thỏa mãn:

#### Giả thiết 1: Sai số có kỳ vọng bằng 0
Các sai số $$\epsilon_i$$ là đại lượng ngẫu nhiên có kỳ vọng bằng 0:

$$\mathbb{E}(\epsilon_i) = 0$$

#### Giả thiết 2: Các sai số không tương quan
Các sai số ngẫu nhiên không có sự tương quan:

$$\mathbb{E}(\epsilon_i \epsilon_j) = 0, \quad \forall i \neq j$$

#### Giả thiết 3: Phương sai đồng nhất (Homoscedasticity)
Phương sai của sai số ngẫu nhiên là bất biến:

$$\text{Var}(\epsilon_i) = \sigma^2$$

#### Giả thiết 4: Sai số không tương quan với biến đầu vào
Sai số ngẫu nhiên $$\epsilon_i$$ và biến đầu vào $$\mathbf{x}_i$$ không tương quan với nhau:

$$\text{Cov}(\mathbf{x}_i, \epsilon_i) = 0, \quad \forall i = 1, \dots, n$$

### 2. Phân Phối Gaussian của Sai Số

Nếu giả định thêm rằng các sai số ngẫu nhiên $$\epsilon_i$$ độc lập và tuân theo phân phối Gaussian (phân phối chuẩn) với kỳ vọng bằng 0 và phương sai $$\sigma^2$$, ký hiệu $$\epsilon_i \sim \mathcal{N}(0, \sigma^2)$$, thì hàm mật độ xác suất tại mỗi điểm $$\epsilon_i$$ là:

$$p(\epsilon_i) = \frac{1}{\sqrt{2\pi \sigma^2}} \exp \left( -\frac{\epsilon_i^2}{2\sigma^2} \right)$$

Thay $$\epsilon_i = y_i - \mathbf{w}^\top \mathbf{x}_i$$ vào hàm mật độ xác suất, ta thu được:

$$p(y_i \mid \mathbf{x}_i; \mathbf{w}) = \frac{1}{\sqrt{2\pi \sigma^2}} \exp \left( -\frac{(y_i - \mathbf{w}^\top \mathbf{x}_i)^2}{2\sigma^2} \right)$$

Ký hiệu $$p(y_i \mid \mathbf{x}_i; \mathbf{w})$$ biểu diễn mật độ xác suất có điều kiện của $$y_i$$ khi biết $$\mathbf{x}_i$$, được tham số hóa bởi $$\mathbf{w}$$. Vì $$\mathbf{w}$$ là tham số cố định chứ không phải biến ngẫu nhiên điều kiện, ta dùng dấu `;` thay vì dấu `,`.

### 3. Ước Lượng Hợp Lý Tối Đa

Khi cố định dữ liệu quan sát và xét biểu thức trên như một hàm theo tham số $$\mathbf{w}$$, ta thu được hàm hợp lý (likelihood):

$$L(\mathbf{w}) = L(\mathbf{w}; \mathbf{X}, \mathbf{y}) = p(\mathbf{y} \mid \mathbf{X}; \mathbf{w})$$

Vì các sai số Gaussian không tương quan nên chúng độc lập với nhau; do đó mật độ đồng thời của tập dữ liệu bằng tích mật độ của từng mẫu:

$$\begin{align}
L(\mathbf{w}) &= \prod_{i=1}^{n} p(y_i \mid \mathbf{x}_i; \mathbf{w}) \\
&= \prod_{i=1}^{n} \frac{1}{\sqrt{2\pi \sigma^2}} \exp \left( -\frac{\epsilon_i^2}{2\sigma^2} \right)
\end{align}$$

Hàm hợp lý đo mức độ phù hợp của tham số $$\mathbf{w}$$ với dữ liệu quan sát $$(\mathbf{X}, \mathbf{y})$$. Theo nguyên lý ước lượng hợp lý cực đại (MLE), ta chọn $$\mathbf{w}$$ làm cực đại hóa $$L(\mathbf{w})$$.

### 4. Tối Ưu Hóa Log-Likelihood

Lấy logarit hai vế để đơn giản hóa bài toán tối ưu:

$$\begin{align}
\hat{\mathbf{w}} &= \arg \max \log L(\mathbf{w}) \\
&= \arg \max \log \left[ \prod_{i=1}^{n} \frac{1}{\sqrt{2\pi \sigma^2}} \exp \left( -\frac{\epsilon_i^2}{2\sigma^2} \right) \right] \\
&= \arg \max \sum_{i=1}^{n} \log \left[ \frac{1}{\sqrt{2\pi \sigma^2}} \exp \left( -\frac{\epsilon_i^2}{2\sigma^2} \right) \right] \\
&= \arg \max \sum_{i=1}^{n} \left[ -\frac{\epsilon_i^2}{2\sigma^2} - \log \sqrt{2\pi \sigma^2} \right] \\
&= \arg \max \left[ -\frac{1}{2\sigma^2} \sum_{i=1}^{n} \epsilon_i^2 - n \log \sqrt{2\pi \sigma^2} \right]
\end{align}$$

Vì $$\sigma^2$$ và $$2\pi$$ là các hằng số dương, việc cực đại hóa hàm log-likelihood tương đương với cực tiểu hóa tổng bình phương phần dư:

$$\sum_{i=1}^{n} \epsilon_i^2 = \sum_{i=1}^{n} (y_i - \mathbf{w}^\top \mathbf{x}_i)^2$$

Điều này tương đương với việc tối thiểu hóa hàm MSE:

$$\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

### 5. Chứng Minh Lý Thuyết

Như vậy, dưới giả định sai số phân phối chuẩn độc lập đồng nhất, bài toán bình phương tối thiểu tương đương với ước lượng hợp lý cực đại. Ngoài ra, theo định lý Gauss–Markov, chỉ cần các giả thiết Gauss–Markov được thỏa mãn (kể cả không cần giả định chuẩn), ước lượng OLS đã là ước lượng tuyến tính không chệch tốt nhất (BLUE). Giả định phân phối chuẩn cho phép xây dựng thêm các khoảng tin cậy và kiểm định ý nghĩa thống kê (p-value) cho các hệ số.

<div id="mle-demo" style="border: 2px solid #ddd; padding: 20px; margin: 20px 0; border-radius: 10px; background-color: #f9f9f9;">
    <h4 style="text-align: center; color: #333;">Trực Quan Hóa Ước Lượng Hợp Lý Tối Đa</h4>
    
    <div style="display: flex; flex-wrap: wrap; gap: 20px; align-items: flex-start;">
        <!-- Canvas for visualization -->
        <div style="flex: 1; min-width: 400px;">
            <canvas id="mleCanvas" width="400" height="300" style="border: 1px solid #ccc; background: white;"></canvas>
            <p style="font-size: 12px; color: #666; margin-top: 5px;">
                <strong>Trực quan hóa:</strong> Các chấm xanh là điểm dữ liệu, đường đỏ là đường khớp, và các đường cong thể hiện phân phối Gaussian của sai số.
            </p>
        </div>
        
        <!-- Controls -->
        <div style="flex: 1; min-width: 250px;">
            <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h5 style="margin-top: 0; color: #444;">Tham Số</h5>
                
                <div style="margin-bottom: 15px;">
                    <label for="noise-slider" style="display: block; margin-bottom: 5px; font-weight: bold;">Mức Nhiễu (σ): <span id="noise-value">0.5</span></label>
                    <input type="range" id="noise-slider" min="0.1" max="2" step="0.1" value="0.5" style="width: 100%;">
                </div>
                
                <div style="margin-bottom: 15px;">
                    <label for="slope-slider" style="display: block; margin-bottom: 5px; font-weight: bold;">Hệ Số Góc Thực: <span id="true-slope-value">1.0</span></label>
                    <input type="range" id="slope-slider" min="-2" max="3" step="0.1" value="1.0" style="width: 100%;">
                </div>
                
                <div style="margin-bottom: 15px;">
                    <label for="intercept-slider" style="display: block; margin-bottom: 5px; font-weight: bold;">Hệ Số Chặn Thực: <span id="true-intercept-value">0.0</span></label>
                    <input type="range" id="intercept-slider" min="-2" max="2" step="0.1" value="0.0" style="width: 100%;">
                </div>
                
                <button id="generate-data" style="width: 100%; padding: 10px; background: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; margin-bottom: 10px;">Tạo Dữ Liệu Mới</button>
                
                <div id="mle-results" style="font-family: monospace; font-size: 12px; line-height: 1.4; background: #f8f9fa; padding: 10px; border-radius: 4px;">
                    <div><strong>Ước Lượng MLE:</strong></div>
                    <div>Hệ số góc: <span id="mle-slope">0.000</span></div>
                    <div>Hệ số chặn: <span id="mle-intercept">0.000</span></div>
                    <div>Log-Likelihood: <span id="log-likelihood">0.000</span></div>
                </div>
            </div>
        </div>
    </div>
</div>

### 6. Huấn Luyện Mô Hình Hồi Quy Tuyến Tính trên Sklearn

Scikit-learn (`sklearn`) là thư viện Python phổ biến cho học máy và khoa học dữ liệu, hỗ trợ huấn luyện hầu hết các mô hình học máy, xây dựng pipeline, chuẩn hóa dữ liệu, và thực hiện kiểm định chéo (cross-validation).

Trong phần này, chúng ta sẽ tìm hiểu cách huấn luyện mô hình hồi quy tuyến tính trên sklearn. Quay lại bài toán trước, nếu thêm thông tin về khoảng cách tới trung tâm:

$$\mathbf{x}_2 = [20, 18, 17, 16, 15, 14, 12, 10, 8, 7, 5, 2, 1]$$

khi đó bài toán trở thành hồi quy đa biến. Quy trình xây dựng và huấn luyện mô hình gồm các bước:

1. Thu thập dữ liệu
2. Làm sạch dữ liệu
3. Lựa chọn dữ liệu đầu vào
4. Chuẩn hóa dữ liệu
5. Phân chia tập huấn luyện/kiểm tra (train/test)
6. Huấn luyện và đánh giá mô hình

Ở bài toán này, chúng ta tập trung vào bước 6 để hiểu cách huấn luyện mô hình.

<div id="sklearn-demo" style="border: 2px solid #ddd; padding: 20px; margin: 20px 0; border-radius: 10px; background-color: #f9f9f9;">
    <h4 style="text-align: center; color: #333;">Ví Dụ Sklearn Hồi Quy Tuyến Tính</h4>
    
    <div style="display: flex; flex-wrap: wrap; gap: 20px; align-items: flex-start;">
        <!-- Code example -->
        <div style="flex: 1; min-width: 400px;">
            <pre style="background: #f8f9fa; padding: 15px; border-radius: 5px; overflow-x: auto; font-size: 12px;"><code id="sklearn-code">import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Dữ liệu mẫu: giá nhà
# Đặc trưng: [diện_tích, khoảng_cách_tới_trung_tâm]
X = np.array([
    [50, 20], [60, 18], [70, 17], [80, 16], [90, 15],
    [100, 14], [110, 12], [120, 10], [130, 8], [140, 7],
    [150, 5], [160, 2], [170, 1]
])

# Mục tiêu: giá (nghìn đô la)
y = np.array([150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510])

# Chia dữ liệu
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Tạo và huấn luyện mô hình
model = LinearRegression()
model.fit(X_train, y_train)

# Dự đoán
y_pred = model.predict(X_test)

# Đánh giá mô hình
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Hệ số: {model.coef_}")
print(f"Hệ số chặn: {model.intercept_}")
print(f"MSE: {mse:.2f}")
print(f"R²: {r2:.3f}")
</code></pre>
        </div>
        
        <!-- Interactive results -->
        <div style="flex: 1; min-width: 250px;">
            <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h5 style="margin-top: 0; color: #444;">Kết Quả Mô Hình</h5>
                
                <button id="run-sklearn" style="width: 100%; padding: 10px; background: #28a745; color: white; border: none; border-radius: 5px; cursor: pointer; margin-bottom: 15px;">Chạy Ví Dụ Sklearn</button>
                
                <div id="sklearn-results" style="font-family: monospace; font-size: 12px; line-height: 1.4; background: #f8f9fa; padding: 10px; border-radius: 4px;">
                    <div><strong>Tham Số Mô Hình:</strong></div>
                    <div>Hệ số diện tích: <span id="area-coeff">--</span></div>
                    <div>Hệ số khoảng cách: <span id="distance-coeff">--</span></div>
                    <div>Hệ số chặn: <span id="sklearn-intercept">--</span></div>
                    <div><strong>Hiệu Suất:</strong></div>
                    <div>MSE: <span id="sklearn-mse">--</span></div>
                    <div>R²: <span id="sklearn-r2">--</span></div>
                </div>
                
                <div style="margin-top: 15px;">
                    <h6 style="margin-bottom: 10px; color: #444;">Máy Tính Dự Đoán</h6>
                    <div style="margin-bottom: 10px;">
                        <label style="display: block; margin-bottom: 5px;">Diện tích (m²):</label>
                        <input type="number" id="pred-area" value="100" min="50" max="200" style="width: 100%; padding: 5px; border: 1px solid #ddd; border-radius: 3px;">
                    </div>
                    <div style="margin-bottom: 10px;">
                        <label style="display: block; margin-bottom: 5px;">Khoảng cách tới trung tâm (km):</label>
                        <input type="number" id="pred-distance" value="10" min="1" max="20" style="width: 100%; padding: 5px; border: 1px solid #ddd; border-radius: 3px;">
                    </div>
                    <button id="make-prediction" style="width: 100%; padding: 8px; background: #17a2b8; color: white; border: none; border-radius: 3px; cursor: pointer;">Dự Đoán Giá</button>
                    <div id="prediction-result" style="margin-top: 10px; padding: 10px; background: #e9ecef; border-radius: 3px; text-align: center; font-weight: bold;">
                        Giá Dự Đoán: --
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

### Các điểm chính cần ghi nhớ

1. **Nền Tảng Lý Thuyết**: Ước lượng hợp lý tối đa cung cấp nền tảng lý thuyết vững chắc cho việc tại sao chúng ta tối thiểu hóa sai số bình phương trong hồi quy tuyến tính.

2. **Giả Thuyết Gaussian**: Hiệu quả của hồi quy tuyến tính dựa trên các giả thuyết Gauss-Markov, đặc biệt là sai số được phân phối chuẩn.

3. **Ước Lượng Không Chệch Tốt Nhất**: Dưới điều kiện phù hợp, OLS cung cấp BLUE - ước lượng tuyến tính không chệch hiệu quả nhất.

4. **Triển Khai Thực Tế**: Các công cụ hiện đại như sklearn giúp dễ dàng triển khai các khái niệm lý thuyết này trong thực tế.

5. **Đánh Giá Mô Hình**: Hiểu nền tảng thống kê giúp đánh giá mô hình đúng cách sử dụng các chỉ số như R², khoảng tin cậy và p-values.

<script>
// MLE Visualization
class MLEVisualization {
    constructor() {
        this.canvas = document.getElementById('mleCanvas');
        this.ctx = this.canvas.getContext('2d');
        this.width = this.canvas.width;
        this.height = this.canvas.height;
        
        // Parameters
        this.trueSlope = 1.0;
        this.trueIntercept = 0.0;
        this.noiseLevel = 0.5;
        this.dataPoints = [];
        
        this.setupControls();
        this.generateData();
        this.draw();
    }
    
    setupControls() {
        const noiseSlider = document.getElementById('noise-slider');
        const slopeSlider = document.getElementById('slope-slider');
        const interceptSlider = document.getElementById('intercept-slider');
        const generateBtn = document.getElementById('generate-data');
        
        noiseSlider.addEventListener('input', (e) => {
            this.noiseLevel = parseFloat(e.target.value);
            document.getElementById('noise-value').textContent = this.noiseLevel.toFixed(1);
            this.generateData();
            this.draw();
        });
        
        slopeSlider.addEventListener('input', (e) => {
            this.trueSlope = parseFloat(e.target.value);
            document.getElementById('true-slope-value').textContent = this.trueSlope.toFixed(1);
            this.generateData();
            this.draw();
        });
        
        interceptSlider.addEventListener('input', (e) => {
            this.trueIntercept = parseFloat(e.target.value);
            document.getElementById('true-intercept-value').textContent = this.trueIntercept.toFixed(1);
            this.generateData();
            this.draw();
        });
        
        generateBtn.addEventListener('click', () => {
            this.generateData();
            this.draw();
        });
    }
    
    generateData() {
        this.dataPoints = [];
        const n = 20;
        
        for (let i = 0; i < n; i++) {
            const x = (i / (n - 1)) * 4 - 2; // x from -2 to 2
            const trueY = this.trueSlope * x + this.trueIntercept;
            const noise = (Math.random() - 0.5) * 2 * this.noiseLevel;
            const y = trueY + noise;
            
            this.dataPoints.push({ x, y, trueY });
        }
    }
    
    calculateMLE() {
        const n = this.dataPoints.length;
        let sumX = 0, sumY = 0, sumXY = 0, sumX2 = 0;
        
        for (const point of this.dataPoints) {
            sumX += point.x;
            sumY += point.y;
            sumXY += point.x * point.y;
            sumX2 += point.x * point.x;
        }
        
        const slope = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX * sumX);
        const intercept = (sumY - slope * sumX) / n;
        
        // Calculate log-likelihood
        let logLikelihood = 0;
        for (const point of this.dataPoints) {
            const predicted = slope * point.x + intercept;
            const error = point.y - predicted;
            logLikelihood -= 0.5 * Math.log(2 * Math.PI * this.noiseLevel * this.noiseLevel);
            logLikelihood -= (error * error) / (2 * this.noiseLevel * this.noiseLevel);
        }
        
        return { slope, intercept, logLikelihood };
    }
    
    draw() {
        this.ctx.clearRect(0, 0, this.width, this.height);
        
        const mle = this.calculateMLE();
        
        // Update display
        document.getElementById('mle-slope').textContent = mle.slope.toFixed(3);
        document.getElementById('mle-intercept').textContent = mle.intercept.toFixed(3);
        document.getElementById('log-likelihood').textContent = mle.logLikelihood.toFixed(2);
        
        // Transform coordinates
        const transform = (x, y) => ({
            x: (x + 2.5) * this.width / 5,
            y: this.height - (y + 2.5) * this.height / 5
        });
        
        // Draw axes
        this.ctx.strokeStyle = '#ddd';
        this.ctx.lineWidth = 1;
        this.ctx.beginPath();
        this.ctx.moveTo(0, this.height / 2);
        this.ctx.lineTo(this.width, this.height / 2);
        this.ctx.moveTo(this.width / 2, 0);
        this.ctx.lineTo(this.width / 2, this.height);
        this.ctx.stroke();
        
        // Draw fitted line
        this.ctx.strokeStyle = '#ff4444';
        this.ctx.lineWidth = 2;
        this.ctx.beginPath();
        const start = transform(-2, mle.slope * (-2) + mle.intercept);
        const end = transform(2, mle.slope * 2 + mle.intercept);
        this.ctx.moveTo(start.x, start.y);
        this.ctx.lineTo(end.x, end.y);
        this.ctx.stroke();
        
        // Draw data points and error distributions
        for (const point of this.dataPoints) {
            const pos = transform(point.x, point.y);
            
            // Draw Gaussian error distribution
            const predicted = mle.slope * point.x + mle.intercept;
            const errorCenter = transform(point.x, predicted);
            
            this.ctx.strokeStyle = '#cccccc';
            this.ctx.lineWidth = 1;
            this.ctx.beginPath();
            for (let i = 0; i <= 20; i++) {
                const t = i / 20;
                const gaussY = predicted + (t - 0.5) * 4 * this.noiseLevel;
                const gaussVal = Math.exp(-0.5 * Math.pow((gaussY - predicted) / this.noiseLevel, 2));
                const gaussPos = transform(point.x + gaussVal * 0.3, gaussY);
                
                if (i === 0) {
                    this.ctx.moveTo(gaussPos.x, gaussPos.y);
                } else {
                    this.ctx.lineTo(gaussPos.x, gaussPos.y);
                }
            }
            this.ctx.stroke();
            
            // Draw data point
            this.ctx.fillStyle = '#4444ff';
            this.ctx.beginPath();
            this.ctx.arc(pos.x, pos.y, 4, 0, 2 * Math.PI);
            this.ctx.fill();
            
            // Draw error line
            this.ctx.strokeStyle = '#888';
            this.ctx.lineWidth = 1;
            this.ctx.beginPath();
            this.ctx.moveTo(pos.x, pos.y);
            this.ctx.lineTo(errorCenter.x, errorCenter.y);
            this.ctx.stroke();
        }
    }
}

// Sklearn Demo
class SklearnDemo {
    constructor() {
        this.setupControls();
        this.model = null;
        this.data = this.generateSampleData();
    }
    
    generateSampleData() {
        return {
            X: [
                [50, 20], [60, 18], [70, 17], [80, 16], [90, 15],
                [100, 14], [110, 12], [120, 10], [130, 8], [140, 7],
                [150, 5], [160, 2], [170, 1]
            ],
            y: [150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510]
        };
    }
    
    setupControls() {
        const runBtn = document.getElementById('run-sklearn');
        const predBtn = document.getElementById('make-prediction');
        
        runBtn.addEventListener('click', () => this.runSklearnExample());
        predBtn.addEventListener('click', () => this.makePrediction());
    }
    
    runSklearnExample() {
        // Simulate sklearn linear regression
        const { X, y } = this.data;
        
        // Calculate means
        const meanX1 = X.reduce((sum, row) => sum + row[0], 0) / X.length;
        const meanX2 = X.reduce((sum, row) => sum + row[1], 0) / X.length;
        const meanY = y.reduce((sum, val) => sum + val, 0) / y.length;
        
        // Calculate coefficients using normal equation
        let sumX1X1 = 0, sumX2X2 = 0, sumX1X2 = 0;
        let sumX1Y = 0, sumX2Y = 0;
        
        for (let i = 0; i < X.length; i++) {
            const x1 = X[i][0] - meanX1;
            const x2 = X[i][1] - meanX2;
            const yVal = y[i] - meanY;
            
            sumX1X1 += x1 * x1;
            sumX2X2 += x2 * x2;
            sumX1X2 += x1 * x2;
            sumX1Y += x1 * yVal;
            sumX2Y += x2 * yVal;
        }
        
        // Solve 2x2 system
        const det = sumX1X1 * sumX2X2 - sumX1X2 * sumX1X2;
        const coeff1 = (sumX2X2 * sumX1Y - sumX1X2 * sumX2Y) / det;
        const coeff2 = (sumX1X1 * sumX2Y - sumX1X2 * sumX1Y) / det;
        const intercept = meanY - coeff1 * meanX1 - coeff2 * meanX2;
        
        // Calculate MSE and R²
        let mse = 0, tss = 0;
        for (let i = 0; i < X.length; i++) {
            const predicted = coeff1 * X[i][0] + coeff2 * X[i][1] + intercept;
            const error = y[i] - predicted;
            mse += error * error;
            tss += (y[i] - meanY) * (y[i] - meanY);
        }
        mse /= X.length;
        const r2 = 1 - (mse * X.length) / tss;
        
        this.model = { coeff1, coeff2, intercept };
        
        // Update display
        document.getElementById('area-coeff').textContent = coeff1.toFixed(3);
        document.getElementById('distance-coeff').textContent = coeff2.toFixed(3);
        document.getElementById('sklearn-intercept').textContent = intercept.toFixed(3);
        document.getElementById('sklearn-mse').textContent = mse.toFixed(2);
        document.getElementById('sklearn-r2').textContent = r2.toFixed(3);
    }
    
    makePrediction() {
        if (!this.model) {
            alert('Vui lòng chạy ví dụ sklearn trước!');
            return;
        }
        
        const area = parseFloat(document.getElementById('pred-area').value);
        const distance = parseFloat(document.getElementById('pred-distance').value);
        
        const prediction = this.model.coeff1 * area + this.model.coeff2 * distance + this.model.intercept;
        
        document.getElementById('prediction-result').innerHTML = 
            `Giá Dự Đoán: <strong>$${prediction.toFixed(0)}k</strong>`;
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    new MLEVisualization();
    new SklearnDemo();
});
</script>

<style>
#mle-demo canvas {
    border-radius: 5px;
}

#sklearn-demo pre {
    max-height: 400px;
    overflow-y: auto;
}

.demo-container {
    margin: 20px 0;
}

input[type="range"] {
    -webkit-appearance: none;
    appearance: none;
    height: 5px;
    background: #ddd;
    outline: none;
    border-radius: 5px;
}

input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 15px;
    height: 15px;
    background: #007bff;
    cursor: pointer;
    border-radius: 50%;
}

input[type="range"]::-moz-range-thumb {
    width: 15px;
    height: 15px;
    background: #007bff;
    cursor: pointer;
    border-radius: 50%;
    border: none;
}
</style>
