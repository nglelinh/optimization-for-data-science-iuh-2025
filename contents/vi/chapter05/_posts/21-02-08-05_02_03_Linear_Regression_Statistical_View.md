---
layout: post
title: 05-02-03 Hồi Quy Tuyến Tính từ Góc Nhìn Thống Kê
chapter: '05'
order: 10
owner: AI Assistant
categories:
- chapter05
lang: vi
---

## Hồi Quy Tuyến Tính từ Góc Nhìn Thống Kê

Trong bài học này, chúng ta khám phá hồi quy tuyến tính từ góc nhìn xác suất và thống kê, chứng minh tại sao việc tối thiểu hóa tổng bình phương sai số (MSE) không chỉ trực quan mà còn được chứng minh lý thuyết thông qua ước lượng hợp lý tối đa.

### 1. Diễn Giải Xác Suất của Hồi Quy Tuyến Tính

Dưới góc nhìn xác suất, chúng ta có thể chứng minh rằng các ước lượng đạt được từ hồi quy tuyến tính dựa trên việc tối thiểu hóa tổng bình phương sai số từ hàm MSE là hoàn toàn tự nhiên và hợp lý.

Thật vậy, chúng ta giả định biến mục tiêu và biến đầu vào liên hệ với nhau qua phương trình:

$$y_i = \mathbf{w}^\top \mathbf{x}_i + \epsilon_i$$

trong đó $\epsilon_i$ đại diện cho sai số ngẫu nhiên mà bất kỳ phương trình nào cũng có. Đây là những yếu tố không thể giải thích bởi mô hình. Do ước lượng của chúng ta là không chệch, sai số ngẫu nhiên này được giả định thỏa mãn các tính chất theo giả thuyết của Gauss-Markov:

#### Giả Thuyết 1: Sai Số Có Kỳ Vọng Bằng Không
Các sai số $$\epsilon_i$$ là đại lượng ngẫu nhiên có kỳ vọng bằng 0:

$$\mathbb{E}(\epsilon_i) = 0$$

#### Giả Thuyết 2: Các Sai Số Không Tương Quan
Các sai số ngẫu nhiên không có sự tương quan:

$$\mathbb{E}(\epsilon_i \epsilon_j) = 0, \quad \forall i \neq j$$

#### Giả Thuyết 3: Phương Sai Đồng Nhất (Homoscedasticity)
Phương sai của sai số ngẫu nhiên là bất biến:

$$\text{Var}(\epsilon_i) = \sigma^2$$

#### Giả Thuyết 4: Độc Lập Giữa Sai Số và Đặc Trưng
Sai số ngẫu nhiên $\epsilon_i$ và các biến đầu vào $\mathbf{x}_i$ không có sự tương quan:

$$\text{Cov}(\mathbf{x}_i, \epsilon_i) = 0, \quad \forall i = 1, \dots, p$$

### 2. Phân Phối Gaussian của Sai Số

Dưới các giả thuyết này, các sai số ngẫu nhiên $\epsilon_i$ tạo thành một phân phối Gaussian (phân phối chuẩn) với trung bình bằng 0 và phương sai $\sigma^2$, ký hiệu là $\epsilon_i \sim \mathcal{N}(0, \sigma^2)$. Hàm mật độ xác suất tại mỗi điểm $\epsilon_i$ là:

$$p(\epsilon_i) = \frac{1}{\sqrt{2\pi \sigma^2}} \exp \left( -\frac{\epsilon_i^2}{2\sigma^2} \right)$$

Thay $\epsilon_i = y_i - \mathbf{w}^\top \mathbf{x}_i$ vào hàm mật độ xác suất, ta được:

$$p(y_i \mid \mathbf{x}_i; \mathbf{w}) = \frac{1}{\sqrt{2\pi \sigma^2}} \exp \left( -\frac{(y_i - \mathbf{w}^\top \mathbf{x}_i)^2}{2\sigma^2} \right)$$

Ký hiệu $p(y_i \mid \mathbf{x}_i; \mathbf{w})$ cho biết xác suất của $y_i$ tương ứng với $\mathbf{x}_i$, được tham số hóa bởi $\mathbf{w}$. Ở đây, $\mathbf{w}$ là đã biết và không được xem như điều kiện của $y_i$, do đó sử dụng dấu ; thay vì ,.

### 3. Ước Lượng Hợp Lý Tối Đa

Dưới góc độ xác suất, $p(y_i \mid \mathbf{x}_i; \mathbf{w})$ là hàm phụ thuộc vào dữ liệu đầu vào $\mathbf{x}_i$ khi đã biết trọng số $\mathbf{w}$. Khi xem xác suất dưới góc nhìn của một hàm theo $\mathbf{w}$, ta gọi đó là hàm hợp lý (likelihood):

$$L(\mathbf{w}) = L(\mathbf{w}; \mathbf{X}, \mathbf{y}) = p(\mathbf{y} \mid \mathbf{X}; \mathbf{w})$$

Theo điều kiện 2 của giả thuyết Gauss-Markov, các sai số là độc lập, nên xác suất đồng thời của dữ liệu bằng tích các mật độ xác suất của từng điểm dữ liệu:

$$\begin{align}
L(\mathbf{w}) &= \prod_{i=1}^{n} p(y_i \mid \mathbf{x}_i; \mathbf{w}) \\
&= \prod_{i=1}^{n} \frac{1}{\sqrt{2\pi \sigma^2}} \exp \left( -\frac{\epsilon_i^2}{2\sigma^2} \right)
\end{align}$$

Hàm hợp lý phản ánh mối quan hệ xác suất giữa $\mathbf{y}$ và $\mathbf{X}$. Để tìm $\mathbf{w}$ sao cho mối quan hệ này phù hợp nhất, theo ước lượng hợp lý tối đa (Maximum Likelihood Estimation), ta chọn $\mathbf{w}$ sao cho $L(\mathbf{w})$ lớn nhất.

### 4. Tối Ưu Hóa Log-Likelihood

Lấy logarit hai vế để đơn giản hóa bài toán tối ưu:

$$\begin{align}
\hat{\mathbf{w}} &= \arg \max \log L(\mathbf{w}) \\
&= \arg \max \log \left[ \prod_{i=1}^{n} \frac{1}{\sqrt{2\pi \sigma^2}} \exp \left( -\frac{\epsilon_i^2}{2\sigma^2} \right) \right] \\
&= \arg \max \sum_{i=1}^{n} \log \left[ \frac{1}{\sqrt{2\pi \sigma^2}} \exp \left( -\frac{\epsilon_i^2}{2\sigma^2} \right) \right] \\
&= \arg \max \sum_{i=1}^{n} \left[ -\frac{\epsilon_i^2}{2\sigma^2} - \log \sqrt{2\pi \sigma^2} \right] \\
&= \arg \max \left[ -\frac{1}{2\sigma^2} \sum_{i=1}^{n} \epsilon_i^2 - n \log \sqrt{2\pi \sigma^2} \right]
\end{align}$$

Vì $\sigma^2$ và $2\pi$ là hằng số, tối ưu hóa hàm trên tương đương với tối thiểu hóa:

$$\sum_{i=1}^{n} \epsilon_i^2 = \sum_{i=1}^{n} (y_i - \mathbf{w}^\top \mathbf{x}_i)^2$$

Điều này tương đương với việc tối thiểu hóa hàm MSE:

$$\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

### 5. Chứng Minh Lý Thuyết

Như vậy, dưới góc nhìn xác suất, ta đã chứng minh rằng hồi quy tuyến tính dựa trên tối thiểu hóa tổng bình phương sai số tương đương với tối ưu hóa hàm hợp lý. Khi các điều kiện của giả thuyết Gauss-Markov được thỏa mãn, ước lượng của chúng ta là ước lượng không chệch tốt nhất (best linear unbiased estimator - BLUE). Các giả thuyết về khoảng tin cậy của giá trị dự báo và đánh giá ý nghĩa của các trọng số thông qua P-value có thể được thực hiện dựa trên phân phối chuẩn.

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

Sklearn là một thư viện toàn diện của Python về khoa học dữ liệu, hỗ trợ huấn luyện hầu hết các mô hình học máy, xây dựng pipeline, chuẩn hóa dữ liệu, và thực hiện kiểm định chéo (cross-validation).

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

### Những Hiểu Biết Quan Trọng

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
