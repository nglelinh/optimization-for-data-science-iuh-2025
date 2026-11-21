---
layout: post
title: 05-02-04 Hồi quy Logistic
chapter: '05'
order: 8
owner: GitHub Copilot
categories:
- chapter05
lang: vi
lesson_type: required
---

# Hồi quy Logistic (Logistic Regression)

Hồi quy logistic là một trong những ứng dụng quan trọng nhất của tối ưu hóa lồi trong machine learning, được sử dụng rộng rãi cho các bài toán phân loại nhị phân.

## 🎯 Bài toán Phân loại Nhị phân

Khác với hồi quy tuyến tính dự đoán giá trị liên tục, **phân loại nhị phân** dự đoán xác suất một mẫu thuộc về một trong hai lớp.

**Ví dụ thực tế:**
- **Y tế**: Dự đoán bệnh nhân có mắc bệnh hay không (0: khỏe mạnh, 1: bệnh)
- **Marketing**: Khách hàng có mua sản phẩm hay không (0: không mua, 1: mua)
- **Tài chính**: Email có phải spam hay không (0: không spam, 1: spam)
- **Công nghệ**: Giao dịch có gian lận hay không (0: hợp lệ, 1: gian lận)

**Dữ liệu huấn luyện:**
- $$\{(\mathbf{x}_i, y_i)\}_{i=1}^n$$ với $$\mathbf{x}_i \in \mathbb{R}^p$$, $$y_i \in \{0, 1\}$$
- $$\mathbf{x}_i$$: vector đặc trưng (features)
- $$y_i$$: nhãn lớp (class label)

## 📊 Từ Linear Regression đến Logistic Regression

### Vấn đề với Linear Regression cho Phân loại

Nếu áp dụng hồi quy tuyến tính trực tiếp: $$\hat{y} = \mathbf{w}^T \mathbf{x} + b$$

**Vấn đề:**
- $$\hat{y}$$ có thể nhận giá trị bất kỳ: $$(-\infty, +\infty)$$
- Nhưng xác suất phải trong khoảng $$[0, 1]$$
- Không phù hợp với bản chất xác suất của phân loại

### Sigmoid Function - Cầu nối Quan trọng

**Hàm Sigmoid:**
$$\sigma(z) = \frac{1}{1 + e^{-z}}$$

**Tính chất quan trọng:**
- **Miền giá trị**: $$\sigma(z) \in (0, 1)$$ $$\forall z \in \mathbb{R}$$
- **Đơn điệu tăng**: $$\sigma'(z) > 0$$ $$\forall z$$
- **Đối xứng**: $$\sigma(-z) = 1 - \sigma(z)$$
- **Giới hạn**: $$\lim_{z \to -\infty} \sigma(z) = 0$$, $$\lim_{z \to +\infty} \sigma(z) = 1$$

**Đạo hàm đặc biệt:**
$$\sigma'(z) = \sigma(z)(1 - \sigma(z))$$


### Mô hình Logistic Regression

**Xác suất dự đoán:**
$$P(y = 1 | \mathbf{x}) = \sigma(\mathbf{w}^T \mathbf{x}) = \frac{1}{1 + e^{-\mathbf{w}^T \mathbf{x}}}$$

$$P(y = 0 | \mathbf{x}) = 1 - P(y = 1 | \mathbf{x}) = \frac{e^{-\mathbf{w}^T \mathbf{x}}}{1 + e^{-\mathbf{w}^T \mathbf{x}}}$$

**Quy tắc quyết định:**
$$\hat{y} = \begin{cases}
1 & \text{nếu } P(y = 1 | \mathbf{x}) \geq 0.5 \\
0 & \text{nếu } P(y = 1 | \mathbf{x}) < 0.5
\end{cases}$$

## 🧮 Hàm Mất mát Cross-Entropy

Trong logistic regression, chúng ta sử dụng **Cross-Entropy Loss** để đo lường sự khác biệt giữa dự đoán và thực tế:

$$J(\mathbf{w}) = -\sum_{i=1}^n \left[ y_i \log p_i + (1-y_i) \log (1-p_i) \right]$$

với $$p_i = \sigma(\mathbf{w}^T \mathbf{x}_i)$$ là xác suất dự đoán.

**Đặc điểm quan trọng:**
- **Phạt nặng dự đoán sai:** Khi dự đoán càng sai, loss càng lớn và không bị chặn trên
- **Smooth và convex:** Đảm bảo tối ưu hóa hiệu quả
- **Probabilistic:** Phù hợp với bản chất xác suất của bài toán

## 🔍 Chứng minh Tính Lồi

### Định lý: Hàm mất mát Logistic là lồi

**Chứng minh:**

**Bước 1:** Chứng minh $$-\log \sigma(z)$$ là lồi

$$-\log \sigma(z) = -\log \frac{1}{1 + e^{-z}} = \log(1 + e^{-z})$$

Đạo hàm bậc hai:
$$\frac{d^2}{dz^2} \log(1 + e^{-z}) = \frac{e^{-z}}{(1 + e^{-z})^2} = \sigma(z)(1 - \sigma(z)) > 0$$

⟹ $$-\log \sigma(z)$$ là lồi theo $$z$$

**Bước 2:** Chứng minh $$-\log(1 - \sigma(z))$$ là lồi

$$-\log(1 - \sigma(z)) = -\log \frac{e^{-z}}{1 + e^{-z}} = z + \log(1 + e^{-z})$$

Đạo hàm bậc hai:
$$\frac{d^2}{dz^2} [z + \log(1 + e^{-z})] = \frac{e^{-z}}{(1 + e^{-z})^2} > 0$$

⟹ $$-\log(1 - \sigma(z))$$ là lồi theo $$z$$

**Bước 3:** Kết luận

Vì $$z = \mathbf{w}^T \mathbf{x}_i$$ là affine theo $$\mathbf{w}$$, và tổng của các hàm lồi là lồi:

$$J(\mathbf{w}) = \sum_{i=1}^n \left[ -y_i \log \sigma(\mathbf{w}^T \mathbf{x}_i) - (1-y_i) \log (1 - \sigma(\mathbf{w}^T \mathbf{x}_i)) \right]$$

là **hàm lồi** theo $$\mathbf{w}$$.

## 📈 Gradient của Hàm Mất mát

**Gradient:**
$$\nabla_{\mathbf{w}} J(\mathbf{w}) = \sum_{i=1}^n (\sigma(\mathbf{w}^T \mathbf{x}_i) - y_i) \mathbf{x}_i = \mathbf{X}^T (\boldsymbol{\sigma} - \mathbf{y})$$

với:
- $$\mathbf{X} \in \mathbb{R}^{n \times p}$$: ma trận đặc trưng
- $$\boldsymbol{\sigma} = [\sigma(\mathbf{w}^T \mathbf{x}_1), ..., \sigma(\mathbf{w}^T \mathbf{x}_n)]^T$$
- $$\mathbf{y} = [y_1, ..., y_n]^T$$

**Hessian:**
$$\nabla^2_{\mathbf{w}} J(\mathbf{w}) = \mathbf{X}^T \mathbf{S} \mathbf{X}$$

với $$\mathbf{S} = \text{diag}(\sigma(\mathbf{w}^T \mathbf{x}_i)(1 - \sigma(\mathbf{w}^T \mathbf{x}_i)))$$

Vì $$\mathbf{S} \succ 0$$, ta có $$\nabla^2_{\mathbf{w}} J(\mathbf{w}) \succeq 0$$ ⟹ **hàm lồi**.

### 🎯 Ý nghĩa của Tính Lồi

**Tại sao tính lồi quan trọng?**

1. **Đảm bảo Global Optimum:**
   - Mọi **điểm cực tiểu địa phương đều là cực tiểu toàn cục** (tập nghiệm tối ưu là tập lồi)
   - Không có local minima "giả" như trong neural networks
   - Các thuật toán tối ưu đều hướng về nghiệm tối ưu toàn cục

2. **Gradient Descent hoạt động hiệu quả:**
   - **Luôn hội tụ** về nghiệm tối ưu (với learning rate phù hợp, khi nghiệm tối ưu tồn tại; với dữ liệu tách được tuyến tính hoàn toàn, nghiệm tối ưu nằm ở vô cực và $$\|\mathbf{w}\|$$ tăng mãi)
   - **Không bị kẹt** tại local minima
   - **Đơn giản và ổn định** - không cần kỹ thuật phức tạp

3. **Lý thuyết tối ưu mạnh mẽ:**
   - Có thể chứng minh **tốc độ hội tụ**
   - Có thể **ước lượng sai số**
   - Có **điều kiện dừng** rõ ràng

### 🚀 Từ Tính Lồi đến Gradient Descent

**Vì hàm mất mát logistic là lồi và khả vi**, chúng ta có thể sử dụng **Gradient Descent** một cách tự tin:

**Thuật toán cơ bản:**
$$\mathbf{w}^{(k+1)} = \mathbf{w}^{(k)} - \alpha \nabla J(\mathbf{w}^{(k)})$$

với gradient:
$$\nabla J(\mathbf{w}) = \mathbf{X}^T (\boldsymbol{\sigma} - \mathbf{y})$$

**Đảm bảo hội tụ:**
- Chọn learning rate $$\alpha$$ phù hợp → **luôn hội tụ**
- Không cần lo lắng về local minima
- Có thể dự đoán được hành vi của thuật toán

**Kết nối với Chương 6:**
Trong **Chương 6 - Gradient Descent**, chúng ta sẽ học chi tiết:
- Cách chọn learning rate tối ưu
- Phân tích tốc độ hội tụ
- Các biến thể như Stochastic Gradient Descent
- **Logistic Regression sẽ là ví dụ chính** để minh họa các khái niệm này!

## 🔄 So sánh với Linear Regression

| Khía cạnh | Linear Regression | Logistic Regression |
|-----------|-------------------|---------------------|
| **Bài toán** | Hồi quy (regression) | Phân loại (classification) |
| **Đầu ra** | Giá trị liên tục | Xác suất $$\in [0,1]$$ |
| **Hàm kích hoạt** | Identity: $$f(z) = z$$ | Sigmoid: $$\sigma(z) = \frac{1}{1+e^{-z}}$$ |
| **Hàm mất mát** | MSE: $$\frac{1}{2n}\sum(y_i - \hat{y}_i)^2$$ | Cross-entropy: $$-\sum[y_i \log p_i + (1-y_i)\log(1-p_i)]$$ |
| **Nghiệm đóng** | Có (nếu $$\mathbf{X}^T\mathbf{X}$$ khả nghịch): $$\mathbf{w}^* = (\mathbf{X}^T\mathbf{X})^{-1}\mathbf{X}^T\mathbf{y}$$ | Không có |
| **Thuật toán** | Normal equation hoặc GD | Gradient Descent |
| **Tính lồi** | Lồi (quadratic) | Lồi (convex) |

## 💡 Ví dụ Minh họa: Dự đoán Spam Email

**Bài toán:** Phân loại email spam dựa trên số lượng từ khóa đáng ngờ.

**Dữ liệu:**
- $$x$$: số từ khóa spam trong email
- $$y$$: 1 nếu spam, 0 nếu không spam

**Mô hình:**
$$P(\text{spam} | x) = \sigma(w_0 + w_1 x) = \frac{1}{1 + e^{-(w_0 + w_1 x)}}$$

**Giải thích:**
- Nếu $$w_1 > 0$$: càng nhiều từ khóa spam, xác suất spam càng cao
- Điểm quyết định: $$x^* = -\frac{w_0}{w_1}$$ (khi $$P = 0.5$$)

## 🎛️ Interactive Visualization

<div id="logistic-regression-demo" style="margin: 20px 0;">
    <div style="display: flex; gap: 20px; margin-bottom: 20px;">
        <div style="flex: 1;">
            <h4>🎚️ Điều khiển Tham số</h4>
            <div style="margin: 10px 0;">
                <label for="w0-slider">Bias (w₀): <span id="w0-value">0</span></label>
                <input type="range" id="w0-slider" min="-5" max="5" step="0.1" value="0" style="width: 100%;">
            </div>
            <div style="margin: 10px 0;">
                <label for="w1-slider">Weight (w₁): <span id="w1-value">1</span></label>
                <input type="range" id="w1-slider" min="-3" max="3" step="0.1" value="1" style="width: 100%;">
            </div>
            <div style="margin: 10px 0;">
                <button id="add-data-btn" style="padding: 8px 16px; margin: 5px;">Thêm Dữ liệu</button>
                <button id="clear-data-btn" style="padding: 8px 16px; margin: 5px;">Xóa Dữ liệu</button>
                <button id="fit-model-btn" style="padding: 8px 16px; margin: 5px;">Fit Model</button>
            </div>
        </div>
        <div style="flex: 1;">
            <h4>📊 Thông tin Mô hình</h4>
            <div id="model-info">
                <p><strong>Phương trình:</strong> P(y=1|x) = σ(<span id="equation">0 + 1·x</span>)</p>
                <p><strong>Điểm quyết định:</strong> x = <span id="decision-boundary">0</span></p>
                <p><strong>Loss:</strong> <span id="current-loss">-</span></p>
                <p><strong>Accuracy:</strong> <span id="accuracy">-</span></p>
            </div>
        </div>
    </div>
    
    <div style="display: flex; gap: 20px;">
        <div style="flex: 1;">
            <h4>📈 Sigmoid Function</h4>
            <canvas id="sigmoid-canvas" width="400" height="300" style="border: 1px solid #ccc;"></canvas>
        </div>
        <div style="flex: 1;">
            <h4>🎯 Classification Results</h4>
            <canvas id="classification-canvas" width="400" height="300" style="border: 1px solid #ccc;"></canvas>
        </div>
    </div>
    
    <div style="margin-top: 20px;">
        <h4>📉 Loss Function Visualization</h4>
        <canvas id="loss-canvas" width="800" height="300" style="border: 1px solid #ccc;"></canvas>
    </div>
</div>

<script>
class LogisticRegressionDemo {
    constructor() {
        this.w0 = 0;
        this.w1 = 1;
        this.dataPoints = [];
        this.isAddingData = false;
        
        this.initializeCanvases();
        this.setupEventListeners();
        this.generateSampleData();
        this.updateVisualization();
    }
    
    initializeCanvases() {
        this.sigmoidCanvas = document.getElementById('sigmoid-canvas');
        this.sigmoidCtx = this.sigmoidCanvas.getContext('2d');
        
        this.classificationCanvas = document.getElementById('classification-canvas');
        this.classificationCtx = this.classificationCanvas.getContext('2d');
        
        this.lossCanvas = document.getElementById('loss-canvas');
        this.lossCtx = this.lossCanvas.getContext('2d');
    }
    
    setupEventListeners() {
        const w0Slider = document.getElementById('w0-slider');
        const w1Slider = document.getElementById('w1-slider');
        const addDataBtn = document.getElementById('add-data-btn');
        const clearDataBtn = document.getElementById('clear-data-btn');
        const fitModelBtn = document.getElementById('fit-model-btn');
        
        w0Slider.addEventListener('input', (e) => {
            this.w0 = parseFloat(e.target.value);
            document.getElementById('w0-value').textContent = this.w0.toFixed(1);
            this.updateVisualization();
        });
        
        w1Slider.addEventListener('input', (e) => {
            this.w1 = parseFloat(e.target.value);
            document.getElementById('w1-value').textContent = this.w1.toFixed(1);
            this.updateVisualization();
        });
        
        addDataBtn.addEventListener('click', () => {
            this.isAddingData = !this.isAddingData;
            addDataBtn.textContent = this.isAddingData ? 'Dừng Thêm' : 'Thêm Dữ liệu';
            addDataBtn.style.backgroundColor = this.isAddingData ? '#ff6b6b' : '';
        });
        
        clearDataBtn.addEventListener('click', () => {
            this.dataPoints = [];
            this.updateVisualization();
        });
        
        fitModelBtn.addEventListener('click', () => {
            this.fitModel();
        });
        
        // Click to add data points
        this.classificationCanvas.addEventListener('click', (e) => {
            if (this.isAddingData) {
                const rect = this.classificationCanvas.getBoundingClientRect();
                const x = (e.clientX - rect.left - 50) / 300 * 10 - 5; // Scale to [-5, 5]
                const y = e.clientY - rect.top > 150 ? 0 : 1; // Top half = class 1, bottom = class 0
                this.dataPoints.push({x, y});
                this.updateVisualization();
            }
        });
    }
    
    generateSampleData() {
        // Generate some sample data
        const sampleData = [
            {x: -3, y: 0}, {x: -2.5, y: 0}, {x: -2, y: 0}, {x: -1.5, y: 0},
            {x: -1, y: 0}, {x: -0.5, y: 0}, {x: 0, y: 0}, {x: 0.5, y: 1},
            {x: 1, y: 1}, {x: 1.5, y: 1}, {x: 2, y: 1}, {x: 2.5, y: 1}, {x: 3, y: 1}
        ];
        
        // Add some noise
        this.dataPoints = sampleData.map(point => ({
            x: point.x + (Math.random() - 0.5) * 0.5,
            y: Math.random() < 0.1 ? 1 - point.y : point.y // 10% label noise
        }));
    }
    
    sigmoid(z) {
        return 1 / (1 + Math.exp(-z));
    }
    
    predict(x) {
        return this.sigmoid(this.w0 + this.w1 * x);
    }
    
    calculateLoss() {
        if (this.dataPoints.length === 0) return 0;
        
        let loss = 0;
        for (const point of this.dataPoints) {
            const p = this.predict(point.x);
            const epsilon = 1e-15; // Prevent log(0)
            const clampedP = Math.max(epsilon, Math.min(1 - epsilon, p));
            loss += -point.y * Math.log(clampedP) - (1 - point.y) * Math.log(1 - clampedP);
        }
        return loss / this.dataPoints.length;
    }
    
    calculateAccuracy() {
        if (this.dataPoints.length === 0) return 0;
        
        let correct = 0;
        for (const point of this.dataPoints) {
            const prediction = this.predict(point.x) >= 0.5 ? 1 : 0;
            if (prediction === point.y) correct++;
        }
        return correct / this.dataPoints.length;
    }
    
    fitModel() {
        if (this.dataPoints.length === 0) return;
        
        // Simple gradient descent
        const learningRate = 0.1;
        const iterations = 1000;
        
        for (let iter = 0; iter < iterations; iter++) {
            let gradW0 = 0, gradW1 = 0;
            
            for (const point of this.dataPoints) {
                const p = this.predict(point.x);
                const error = p - point.y;
                gradW0 += error;
                gradW1 += error * point.x;
            }
            
            gradW0 /= this.dataPoints.length;
            gradW1 /= this.dataPoints.length;
            
            this.w0 -= learningRate * gradW0;
            this.w1 -= learningRate * gradW1;
        }
        
        // Update sliders
        document.getElementById('w0-slider').value = this.w0;
        document.getElementById('w1-slider').value = this.w1;
        document.getElementById('w0-value').textContent = this.w0.toFixed(1);
        document.getElementById('w1-value').textContent = this.w1.toFixed(1);
        
        this.updateVisualization();
    }
    
    drawSigmoid() {
        const ctx = this.sigmoidCtx;
        const canvas = this.sigmoidCanvas;
        
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Draw axes
        ctx.strokeStyle = '#ccc';
        ctx.lineWidth = 1;
        
        // X-axis
        ctx.beginPath();
        ctx.moveTo(50, canvas.height - 50);
        ctx.lineTo(canvas.width - 20, canvas.height - 50);
        ctx.stroke();
        
        // Y-axis
        ctx.beginPath();
        ctx.moveTo(50, 20);
        ctx.lineTo(50, canvas.height - 50);
        ctx.stroke();
        
        // Draw sigmoid curve
        ctx.strokeStyle = '#2196F3';
        ctx.lineWidth = 2;
        ctx.beginPath();
        
        for (let i = 0; i <= 300; i++) {
            const x = (i / 300) * 10 - 5; // x from -5 to 5
            const z = this.w0 + this.w1 * x;
            const y = this.sigmoid(z);
            
            const canvasX = 50 + (x + 5) / 10 * 300;
            const canvasY = canvas.height - 50 - y * 200;
            
            if (i === 0) {
                ctx.moveTo(canvasX, canvasY);
            } else {
                ctx.lineTo(canvasX, canvasY);
            }
        }
        ctx.stroke();
        
        // Draw decision boundary
        if (this.w1 !== 0) {
            const decisionX = -this.w0 / this.w1;
            if (decisionX >= -5 && decisionX <= 5) {
                const canvasX = 50 + (decisionX + 5) / 10 * 300;
                ctx.strokeStyle = '#ff6b6b';
                ctx.lineWidth = 2;
                ctx.setLineDash([5, 5]);
                ctx.beginPath();
                ctx.moveTo(canvasX, 20);
                ctx.lineTo(canvasX, canvas.height - 50);
                ctx.stroke();
                ctx.setLineDash([]);
            }
        }
        
        // Labels
        ctx.fillStyle = '#333';
        ctx.font = '12px Arial';
        ctx.fillText('P(y=1|x)', 10, 30);
        ctx.fillText('x', canvas.width - 15, canvas.height - 30);
        ctx.fillText('0', 45, canvas.height - 30);
        ctx.fillText('1', 45, 25);
        ctx.fillText('0.5', 35, canvas.height - 150);
    }
    
    drawClassification() {
        const ctx = this.classificationCtx;
        const canvas = this.classificationCanvas;
        
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Draw background regions
        ctx.fillStyle = 'rgba(255, 107, 107, 0.1)'; // Red for class 0
        ctx.fillRect(50, canvas.height/2, 300, canvas.height/2 - 50);
        
        ctx.fillStyle = 'rgba(76, 175, 80, 0.1)'; // Green for class 1
        ctx.fillRect(50, 20, 300, canvas.height/2 - 20);
        
        // Draw axes
        ctx.strokeStyle = '#ccc';
        ctx.lineWidth = 1;
        
        // X-axis
        ctx.beginPath();
        ctx.moveTo(50, canvas.height - 50);
        ctx.lineTo(350, canvas.height - 50);
        ctx.stroke();
        
        // Y-axis (class separator)
        ctx.beginPath();
        ctx.moveTo(50, canvas.height/2);
        ctx.lineTo(350, canvas.height/2);
        ctx.stroke();
        
        // Draw data points
        for (const point of this.dataPoints) {
            const canvasX = 50 + (point.x + 5) / 10 * 300;
            const canvasY = point.y === 1 ? canvas.height/4 : 3*canvas.height/4;
            
            ctx.fillStyle = point.y === 1 ? '#4CAF50' : '#f44336';
            ctx.beginPath();
            ctx.arc(canvasX, canvasY, 5, 0, 2 * Math.PI);
            ctx.fill();
        }
        
        // Draw decision boundary
        if (this.w1 !== 0) {
            const decisionX = -this.w0 / this.w1;
            if (decisionX >= -5 && decisionX <= 5) {
                const canvasX = 50 + (decisionX + 5) / 10 * 300;
                ctx.strokeStyle = '#2196F3';
                ctx.lineWidth = 3;
                ctx.beginPath();
                ctx.moveTo(canvasX, 20);
                ctx.lineTo(canvasX, canvas.height - 50);
                ctx.stroke();
            }
        }
        
        // Labels
        ctx.fillStyle = '#333';
        ctx.font = '12px Arial';
        ctx.fillText('Class 1', 10, 40);
        ctx.fillText('Class 0', 10, canvas.height - 60);
        ctx.fillText('x', 360, canvas.height - 30);
    }
    
    drawLoss() {
        const ctx = this.lossCtx;
        const canvas = this.lossCanvas;
        
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        if (this.dataPoints.length === 0) return;
        
        // Draw axes
        ctx.strokeStyle = '#ccc';
        ctx.lineWidth = 1;
        
        // X-axis
        ctx.beginPath();
        ctx.moveTo(50, canvas.height - 50);
        ctx.lineTo(canvas.width - 20, canvas.height - 50);
        ctx.stroke();
        
        // Y-axis
        ctx.beginPath();
        ctx.moveTo(50, 20);
        ctx.lineTo(50, canvas.height - 50);
        ctx.stroke();
        
        // Calculate loss surface
        const originalW0 = this.w0;
        const originalW1 = this.w1;
        
        const w0Range = [-3, 3];
        const w1Range = [-2, 2];
        const resolution = 50;
        
        let minLoss = Infinity;
        let maxLoss = -Infinity;
        const lossData = [];
        
        for (let i = 0; i <= resolution; i++) {
            lossData[i] = [];
            for (let j = 0; j <= resolution; j++) {
                this.w0 = w0Range[0] + (w0Range[1] - w0Range[0]) * i / resolution;
                this.w1 = w1Range[0] + (w1Range[1] - w1Range[0]) * j / resolution;
                const loss = this.calculateLoss();
                lossData[i][j] = loss;
                minLoss = Math.min(minLoss, loss);
                maxLoss = Math.max(maxLoss, loss);
            }
        }
        
        // Draw contour lines
        const numContours = 10;
        for (let c = 0; c < numContours; c++) {
            const level = minLoss + (maxLoss - minLoss) * c / numContours;
            ctx.strokeStyle = `hsl(${240 - c * 20}, 70%, 60%)`;
            ctx.lineWidth = 1;
            
            // Simple contour drawing (could be improved)
            for (let i = 0; i < resolution; i++) {
                for (let j = 0; j < resolution; j++) {
                    if (Math.abs(lossData[i][j] - level) < (maxLoss - minLoss) / numContours / 2) {
                        const x = 50 + i / resolution * (canvas.width - 70);
                        const y = canvas.height - 50 - j / resolution * (canvas.height - 70);
                        ctx.fillRect(x, y, 2, 2);
                    }
                }
            }
        }
        
        // Mark current position
        this.w0 = originalW0;
        this.w1 = originalW1;
        
        const currentX = 50 + (this.w0 - w0Range[0]) / (w0Range[1] - w0Range[0]) * (canvas.width - 70);
        const currentY = canvas.height - 50 - (this.w1 - w1Range[0]) / (w1Range[1] - w1Range[0]) * (canvas.height - 70);
        
        ctx.fillStyle = '#ff6b6b';
        ctx.beginPath();
        ctx.arc(currentX, currentY, 6, 0, 2 * Math.PI);
        ctx.fill();
        
        // Labels
        ctx.fillStyle = '#333';
        ctx.font = '12px Arial';
        ctx.fillText('w₁', 10, canvas.height - 30);
        ctx.fillText('w₀', canvas.width - 20, canvas.height - 30);
    }
    
    updateVisualization() {
        this.drawSigmoid();
        this.drawClassification();
        this.drawLoss();
        
        // Update info panel
        const equation = `${this.w0.toFixed(1)} + ${this.w1.toFixed(1)}·x`;
        document.getElementById('equation').textContent = equation;
        
        const decisionBoundary = this.w1 !== 0 ? (-this.w0 / this.w1).toFixed(2) : '∞';
        document.getElementById('decision-boundary').textContent = decisionBoundary;
        
        const loss = this.calculateLoss();
        document.getElementById('current-loss').textContent = loss.toFixed(3);
        
        const accuracy = this.calculateAccuracy();
        document.getElementById('accuracy').textContent = (accuracy * 100).toFixed(1) + '%';
    }
}

// Initialize demo when page loads
document.addEventListener('DOMContentLoaded', () => {
    new LogisticRegressionDemo();
});
</script>

<style>
#logistic-regression-demo {
    font-family: Arial, sans-serif;
    max-width: 1000px;
    margin: 0 auto;
}

#logistic-regression-demo canvas {
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

#logistic-regression-demo input[type="range"] {
    width: 100%;
    margin: 5px 0;
}

#logistic-regression-demo button {
    background-color: #2196F3;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
}

#logistic-regression-demo button:hover {
    background-color: #1976D2;
}

#model-info {
    background-color: #f5f5f5;
    padding: 15px;
    border-radius: 4px;
    font-size: 14px;
}

#model-info p {
    margin: 5px 0;
}
</style>


---

💡 **Bài tập thực hành:** Hãy thử thay đổi các tham số trong visualization trên để hiểu rõ hơn về cách logistic regression hoạt động!

---

## 📖 Đọc thêm: Các Link Functions thay thế cho Sigmoid

*Phần này dành cho những bạn muốn tìm hiểu sâu hơn về lý do chọn sigmoid function, tại sao sử dụng cross-entropy loss, và các lựa chọn thay thế trong generalized linear models.*

## 🧮 Tại sao Cross-Entropy là Hàm Mất mát?

### 🎯 Mục tiêu: Tìm trọng số tốt nhất

**Câu hỏi cốt lõi:** Làm thế nào để tìm trọng số $$\mathbf{w}$$ sao cho mô hình dự đoán chính xác nhất?

**Ý tưởng:** Chọn $$\mathbf{w}$$ sao cho **xác suất quan sát được dữ liệu thực tế là cao nhất**.

### 🔍 Từ Xác suất đến Cross-Entropy

#### **Bước 1: Mô hình hóa xác suất**

Với mỗi mẫu dữ liệu $$(\mathbf{x}_i, y_i)$$, mô hình dự đoán:
- Nếu $$y_i = 1$$: xác suất là $$p_i = \sigma(\mathbf{w}^T \mathbf{x}_i)$$
- Nếu $$y_i = 0$$: xác suất là $$1 - p_i = 1 - \sigma(\mathbf{w}^T \mathbf{x}_i)$$

#### **Bước 2: Likelihood - "Khả năng xảy ra"**

**Câu hỏi:** Với trọng số $$\mathbf{w}$$ hiện tại, khả năng quan sát được toàn bộ dữ liệu là bao nhiều?

**Trả lời:** Nhân xác suất của tất cả các mẫu:
$$\text{Likelihood} = p_1^{y_1} \cdot (1-p_1)^{1-y_1} \times p_2^{y_2} \cdot (1-p_2)^{1-y_2} \times \ldots$$

#### **Bước 3: Maximum Likelihood Principle**

**Nguyên lý:** Chọn $$\mathbf{w}$$ để **tối đa hóa likelihood** = chọn $$\mathbf{w}$$ làm cho dữ liệu quan sát được có khả năng xảy ra cao nhất.

**Vấn đề thực tế:** Likelihood là tích của nhiều số nhỏ → khó tính toán và không ổn định.

#### **Bước 4: Log-Likelihood**

**Giải pháp:** Lấy logarithm để chuyển tích thành tổng:
$$\log(\text{Likelihood}) = \sum_{i=1}^n \left[ y_i \log p_i + (1-y_i) \log (1-p_i) \right]$$

**Lợi ích:**
- Tính toán ổn định hơn
- Tối đa hóa log-likelihood = tối đa hóa likelihood

#### **Bước 5: Cross-Entropy Loss**

**Chuyển đổi cuối cùng:** Tối đa hóa = Tối thiểu hóa âm của nó

$$J(\mathbf{w}) = -\log(\text{Likelihood}) = -\sum_{i=1}^n \left[ y_i \log p_i + (1-y_i) \log (1-p_i) \right]$$

**Đây chính là Cross-Entropy Loss!**

### 💡 Tại sao Cross-Entropy "Hợp lý"?

#### **1. Phạt nặng dự đoán sai**

**Ví dụ minh họa:**
- **Trường hợp 1:** $$y = 1$$ (thực tế), $$p = 0.9$$ (dự đoán)
  - Loss = $$-1 \times \log(0.9) = 0.105$$ (thấp - tốt!)

- **Trường hợp 2:** $$y = 1$$ (thực tế), $$p = 0.1$$ (dự đoán)  
  - Loss = $$-1 \times \log(0.1) = 2.303$$ (cao - tệ!)

**Kết luận:** Dự đoán càng sai, loss càng lớn, và **không bị chặn trên** (tăng xấp xỉ tuyến tính theo mức sai khi $$p \to 0$$).

#### **2. Khuyến khích dự đoán tự tin**

Cross-entropy "thưởng" cho những dự đoán tự tin và đúng:
- $$p = 0.99$$ khi $$y = 1$$ → loss rất thấp
- $$p = 0.51$$ khi $$y = 1$$ → loss vẫn cao (mặc dù đúng)

#### **3. Smooth và khả vi**

Khác với accuracy (0-1 loss), cross-entropy:
- **Smooth**: Có đạo hàm mọi nơi
- **Convex**: Đảm bảo tối ưu toàn cục
- **Informative gradient**: Gradient lớn khi dự đoán sai

### 🔄 So sánh với các Loss khác

| Loss Function | Công thức | Ưu điểm | Nhược điểm |
|---------------|-----------|---------|------------|
| **Cross-Entropy** | $$-[y\log p + (1-y)\log(1-p)]$$ | Smooth, convex, principled | Sensitive to outliers |
| **Mean Squared Error** | $$(y - p)^2$$ | Simple, familiar | Not probabilistic |
| **0-1 Loss** | $$\mathbf{1}[y \neq \text{round}(p)]$$ | Direct accuracy | Non-differentiable |

### 🎯 Kết luận về Cross-Entropy

**Cross-Entropy không phải là lựa chọn tùy ý** - nó xuất phát tự nhiên từ:

1. **Nguyên lý Maximum Likelihood** - cách tốt nhất để fit mô hình xác suất
2. **Tính chất toán học tốt** - convex, smooth, differentiable  
3. **Ý nghĩa thực tế** - phạt nặng dự đoán sai, khuyến khích tự tin

**Đây là lý do tại sao cross-entropy là "gold standard" cho classification problems!**

## 🤔 Tại sao chọn Sigmoid Function?

### 1. **Yêu cầu Toán học cho Activation Function**

Để chuyển đổi từ $$\mathbb{R}$$ sang xác suất $$[0,1]$$, ta cần một hàm $$g: \mathbb{R} \to [0,1]$$ thỏa mãn:

**Yêu cầu bắt buộc:**
- ✅ **Monotonic**: $$g'(z) > 0$$ (đảm bảo thứ tự)
- ✅ **Bounded**: $$g(z) \in [0,1]$$ (xác suất hợp lệ)
- ✅ **Smooth**: Khả vi để tính gradient
- ✅ **Asymptotic**: $$\lim_{z \to -\infty} g(z) = 0$$, $$\lim_{z \to +\infty} g(z) = 1$$

**Yêu cầu mong muốn:**
- 🎯 **Simple derivative**: Đạo hàm dễ tính
- 🎯 **Probabilistic interpretation**: Có ý nghĩa xác suất
- 🎯 **Symmetric**: $$g(-z) = 1 - g(z)$$

### 2. **Nguồn gốc từ Odds và Logit**

**Odds (Tỷ số cược):**
$$\text{Odds} = \frac{P(y=1|x)}{P(y=0|x)} = \frac{P(y=1|x)}{1-P(y=1|x)}$$

**Log-odds (Logit):**
$$\text{logit}(p) = \log\left(\frac{p}{1-p}\right)$$

**Mô hình tuyến tính cho log-odds:**
$$\log\left(\frac{P(y=1|x)}{1-P(y=1|x)}\right) = \mathbf{w}^T \mathbf{x}$$

**Giải ngược để tìm P:**
$$\frac{P(y=1|x)}{1-P(y=1|x)} = e^{\mathbf{w}^T \mathbf{x}}$$

$$P(y=1|x) = (1-P(y=1|x)) \cdot e^{\mathbf{w}^T \mathbf{x}}$$

$$P(y=1|x) = e^{\mathbf{w}^T \mathbf{x}} - P(y=1|x) \cdot e^{\mathbf{w}^T \mathbf{x}}$$

$$P(y=1|x)(1 + e^{\mathbf{w}^T \mathbf{x}}) = e^{\mathbf{w}^T \mathbf{x}}$$

$$P(y=1|x) = \frac{e^{\mathbf{w}^T \mathbf{x}}}{1 + e^{\mathbf{w}^T \mathbf{x}}} = \frac{1}{1 + e^{-\mathbf{w}^T \mathbf{x}}} = \sigma(\mathbf{w}^T \mathbf{x})$$

⟹ **Sigmoid xuất hiện tự nhiên từ mô hình log-odds tuyến tính!**

### 3. **Ưu điểm Đặc biệt của Sigmoid**

#### **a) Đạo hàm Elegant**
$$\sigma'(z) = \sigma(z)(1 - \sigma(z))$$

**Lợi ích:**
- Không cần tính lại $$e^{-z}$$
- Gradient descent hiệu quả
- Backpropagation đơn giản

#### **b) Tính Đối xứng**
$$\sigma(-z) = 1 - \sigma(z)$$

**Ý nghĩa:** Nếu $$P(y=1|x) = 0.7$$ thì $$P(y=1|-x) = 0.3$$

#### **c) Giải thích Xác suất Tự nhiên**
- $$z = 0 \Rightarrow P = 0.5$$ (không thiên vị)
- $$z > 0 \Rightarrow P > 0.5$$ (thiên về class 1)
- $$z < 0 \Rightarrow P < 0.5$$ (thiên về class 0)

### 🔄 Tại sao cần các hàm thay thế?

Mặc dù sigmoid là lựa chọn phổ biến nhất, trong một số trường hợp đặc biệt, các link functions khác có thể phù hợp hơn:

- **Dữ liệu có tail behavior khác biệt**
- **Rare events hoặc imbalanced data**
- **Yêu cầu mô hình hóa đặc biệt**
- **Theoretical assumptions khác nhau**

### 1. **Tanh Function**

$$\tanh(z) = \frac{e^z - e^{-z}}{e^z + e^{-z}} = \frac{e^{2z} - 1}{e^{2z} + 1}$$

**Mối quan hệ với Sigmoid:**
$$\tanh(z) = 2\sigma(2z) - 1$$

**Đặc điểm:**
- ✅ **Miền giá trị**: $$(-1, 1)$$
- ✅ **Đối xứng qua gốc**: $$\tanh(-z) = -\tanh(z)$$
- ✅ **Đạo hàm**: $$\tanh'(z) = 1 - \tanh^2(z)$$

**Chuyển đổi về xác suất:** $$p = \frac{\tanh(z) + 1}{2}$$

**Ứng dụng:** Neural networks (hidden layers), khi cần output centered around 0

### 2. **Probit Function (Inverse Normal CDF)**

$$\Phi^{-1}(p) = z \Leftrightarrow p = \Phi(z) = \int_{-\infty}^z \frac{1}{\sqrt{2\pi}} e^{-t^2/2} dt$$

**Đặc điểm:**
- ✅ **Miền giá trị**: $$(0, 1)$$
- ✅ **Đối xứng**: $$\Phi(-z) = 1 - \Phi(z)$$
- ❌ **Không có dạng đóng**: Cần tính tích phân số

**So sánh với Sigmoid:**
- **Sigmoid**: đuôi exponential decay $$\sim e^{-|z|}$$
- **Probit**: đuôi Gaussian decay $$\sim e^{-z^2/2}$$ (nhanh hơn)

**Ứng dụng:** 
- Econometrics (probit regression)
- Khi dữ liệu có phân phối gần Gaussian
- Threshold models

### 3. **Gumbel (Log-log) Function**

$$F(z) = e^{-e^{-z}}$$

**Đặc điểm:**
- ✅ **Miền giá trị**: $$(0, 1)$$
- ❌ **Không đối xứng**: Right-skewed
- **CDF của Gumbel distribution**

**Ứng dụng:**
- Extreme value theory
- Survival analysis
- Modeling maximum values

### 4. **Complementary Log-log**

$$F(z) = 1 - e^{-e^z}$$

**Đặc điểm:**
- ✅ **Miền giá trị**: $$(0, 1)$$
- ❌ **Không đối xứng**: Left-skewed
- **Complement của Gumbel**

**Ứng dụng:**
- **Rare events modeling** (y=1 hiếm)
- Survival analysis (hazard modeling)
- Time-to-event data
- Poisson regression với binary outcomes

### 5. **Cauchit Function**

$$F(z) = \frac{1}{2} + \frac{1}{\pi} \arctan(z)$$

**Đặc điểm:**
- ✅ **Miền giá trị**: $$(0, 1)$$
- ✅ **Đối xứng**: $$F(-z) = 1 - F(z)$$
- **Heavy tails**: Slower decay than sigmoid/probit

**Ứng dụng:**
- Robust regression (outlier-resistant)
- Heavy-tailed error distributions
- Financial modeling

## 📊 Interactive Comparison Tool

<div id="link-functions-comparison" style="margin: 20px 0;">
    <div style="margin-bottom: 20px;">
        <h4>🎛️ Điều khiển Hiển thị</h4>
        <div style="display: flex; gap: 15px; flex-wrap: wrap;">
            <label><input type="checkbox" id="show-sigmoid" checked> Sigmoid</label>
            <label><input type="checkbox" id="show-tanh" checked> Tanh (scaled)</label>
            <label><input type="checkbox" id="show-probit" checked> Probit</label>
            <label><input type="checkbox" id="show-gumbel"> Gumbel</label>
            <label><input type="checkbox" id="show-cauchit"> Cauchit</label>
        </div>
    </div>
    
    <div style="display: flex; gap: 20px;">
        <div style="flex: 1;">
            <h4>📈 Link Functions Comparison</h4>
            <canvas id="link-functions-canvas" width="500" height="400" style="border: 1px solid #ccc;"></canvas>
        </div>
        <div style="flex: 1;">
            <h4>📊 Properties Comparison</h4>
            <div id="properties-table" style="font-size: 14px;">
                <table style="width: 100%; border-collapse: collapse;">
                    <thead>
                        <tr style="background-color: #f0f0f0;">
                            <th style="border: 1px solid #ccc; padding: 8px;">Function</th>
                            <th style="border: 1px solid #ccc; padding: 8px;">Symmetric</th>
                            <th style="border: 1px solid #ccc; padding: 8px;">Tail Behavior</th>
                            <th style="border: 1px solid #ccc; padding: 8px;">Computation</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td style="border: 1px solid #ccc; padding: 8px;"><strong>Sigmoid</strong></td>
                            <td style="border: 1px solid #ccc; padding: 8px;">✅ Yes</td>
                            <td style="border: 1px solid #ccc; padding: 8px;">Exponential</td>
                            <td style="border: 1px solid #ccc; padding: 8px;">⚡ Fast</td>
                        </tr>
                        <tr>
                            <td style="border: 1px solid #ccc; padding: 8px;"><strong>Tanh</strong></td>
                            <td style="border: 1px solid #ccc; padding: 8px;">✅ Yes</td>
                            <td style="border: 1px solid #ccc; padding: 8px;">Exponential</td>
                            <td style="border: 1px solid #ccc; padding: 8px;">⚡ Fast</td>
                        </tr>
                        <tr>
                            <td style="border: 1px solid #ccc; padding: 8px;"><strong>Probit</strong></td>
                            <td style="border: 1px solid #ccc; padding: 8px;">✅ Yes</td>
                            <td style="border: 1px solid #ccc; padding: 8px;">Gaussian</td>
                            <td style="border: 1px solid #ccc; padding: 8px;">🐌 Slow</td>
                        </tr>
                        <tr>
                            <td style="border: 1px solid #ccc; padding: 8px;"><strong>Gumbel</strong></td>
                            <td style="border: 1px solid #ccc; padding: 8px;">❌ No</td>
                            <td style="border: 1px solid #ccc; padding: 8px;">Right-skewed</td>
                            <td style="border: 1px solid #ccc; padding: 8px;">⚡ Fast</td>
                        </tr>
                        <tr>
                            <td style="border: 1px solid #ccc; padding: 8px;"><strong>Cauchit</strong></td>
                            <td style="border: 1px solid #ccc; padding: 8px;">✅ Yes</td>
                            <td style="border: 1px solid #ccc; padding: 8px;">Heavy tails</td>
                            <td style="border: 1px solid #ccc; padding: 8px;">⚡ Fast</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>

<script>
class LinkFunctionsComparison {
    constructor() {
        this.canvas = document.getElementById('link-functions-canvas');
        if (!this.canvas) return;
        this.ctx = this.canvas.getContext('2d');
        this.setupEventListeners();
        this.draw();
    }
    
    setupEventListeners() {
        const checkboxes = ['sigmoid', 'tanh', 'probit', 'gumbel', 'cauchit'];
        checkboxes.forEach(name => {
            const checkbox = document.getElementById(`show-${name}`);
            if (checkbox) {
                checkbox.addEventListener('change', () => {
                    this.draw();
                });
            }
        });
    }
    
    sigmoid(z) {
        return 1 / (1 + Math.exp(-z));
    }
    
    tanh_scaled(z) {
        return (Math.tanh(z) + 1) / 2; // Scale tanh from [-1,1] to [0,1]
    }
    
    // Approximation of probit function (inverse normal CDF)
    probit(z) {
        // Using rational approximation for normal CDF
        const a1 = 0.254829592;
        const a2 = -0.284496736;
        const a3 = 1.421413741;
        const a4 = -1.453152027;
        const a5 = 1.061405429;
        const p = 0.3275911;
        
        const sign = z < 0 ? -1 : 1;
        z = Math.abs(z) / Math.sqrt(2);
        
        const t = 1.0 / (1.0 + p * z);
        const y = 1.0 - (((((a5 * t + a4) * t) + a3) * t + a2) * t + a1) * t * Math.exp(-z * z);
        
        return 0.5 * (1.0 + sign * y);
    }
    
    gumbel(z) {
        return Math.exp(-Math.exp(-z));
    }
    
    cauchit(z) {
        return 0.5 + Math.atan(z) / Math.PI;
    }
    
    draw() {
        const ctx = this.ctx;
        const canvas = this.canvas;
        
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Draw axes
        ctx.strokeStyle = '#ccc';
        ctx.lineWidth = 1;
        
        // X-axis
        ctx.beginPath();
        ctx.moveTo(50, canvas.height - 50);
        ctx.lineTo(canvas.width - 20, canvas.height - 50);
        ctx.stroke();
        
        // Y-axis
        ctx.beginPath();
        ctx.moveTo(50, 20);
        ctx.lineTo(50, canvas.height - 50);
        ctx.stroke();
        
        // Grid lines
        ctx.strokeStyle = '#f0f0f0';
        ctx.lineWidth = 0.5;
        
        // Horizontal grid lines
        for (let i = 1; i <= 4; i++) {
            const y = 20 + (canvas.height - 70) * i / 5;
            ctx.beginPath();
            ctx.moveTo(50, y);
            ctx.lineTo(canvas.width - 20, y);
            ctx.stroke();
        }
        
        // Vertical grid lines
        for (let i = 1; i <= 9; i++) {
            const x = 50 + (canvas.width - 70) * i / 10;
            ctx.beginPath();
            ctx.moveTo(x, 20);
            ctx.lineTo(x, canvas.height - 50);
            ctx.stroke();
        }
        
        // Draw functions
        const functions = [
            { name: 'sigmoid', func: this.sigmoid, color: '#2196F3', label: 'Sigmoid' },
            { name: 'tanh', func: this.tanh_scaled, color: '#4CAF50', label: 'Tanh (scaled)' },
            { name: 'probit', func: this.probit, color: '#FF9800', label: 'Probit' },
            { name: 'gumbel', func: this.gumbel, color: '#9C27B0', label: 'Gumbel' },
            { name: 'cauchit', func: this.cauchit, color: '#F44336', label: 'Cauchit' }
        ];
        
        functions.forEach(({name, func, color, label}) => {
            const checkbox = document.getElementById(`show-${name}`);
            if (checkbox && checkbox.checked) {
                ctx.strokeStyle = color;
                ctx.lineWidth = 2;
                ctx.beginPath();
                
                for (let i = 0; i <= 400; i++) {
                    const z = (i / 400) * 10 - 5; // z from -5 to 5
                    let y;
                    
                    try {
                        y = func.call(this, z);
                        if (isNaN(y) || !isFinite(y)) continue;
                    } catch (e) {
                        continue;
                    }
                    
                    const canvasX = 50 + (z + 5) / 10 * (canvas.width - 70);
                    const canvasY = canvas.height - 50 - y * (canvas.height - 70);
                    
                    if (i === 0) {
                        ctx.moveTo(canvasX, canvasY);
                    } else {
                        ctx.lineTo(canvasX, canvasY);
                    }
                }
                ctx.stroke();
            }
        });
        
        // Draw legend
        let legendY = 30;
        functions.forEach(({name, color, label}) => {
            const checkbox = document.getElementById(`show-${name}`);
            if (checkbox && checkbox.checked) {
                ctx.strokeStyle = color;
                ctx.lineWidth = 3;
                ctx.beginPath();
                ctx.moveTo(canvas.width - 150, legendY);
                ctx.lineTo(canvas.width - 120, legendY);
                ctx.stroke();
                
                ctx.fillStyle = '#333';
                ctx.font = '12px Arial';
                ctx.fillText(label, canvas.width - 115, legendY + 4);
                
                legendY += 20;
            }
        });
        
        // Labels
        ctx.fillStyle = '#333';
        ctx.font = '12px Arial';
        ctx.fillText('z', canvas.width - 15, canvas.height - 30);
        ctx.fillText('P(y=1|z)', 10, 15);
        
        // Axis labels
        ctx.fillText('-5', 45, canvas.height - 30);
        ctx.fillText('0', 245, canvas.height - 30);
        ctx.fillText('5', 445, canvas.height - 30);
        ctx.fillText('0', 35, canvas.height - 45);
        ctx.fillText('0.5', 30, canvas.height/2 + 5);
        ctx.fillText('1', 35, 25);
    }
}

// Initialize comparison when page loads
document.addEventListener('DOMContentLoaded', () => {
    new LinkFunctionsComparison();
});
</script>

## 🎯 Hướng dẫn Lựa chọn Link Function

### **Sigmoid (Logistic)** - Lựa chọn Mặc định ⭐
**Sử dụng khi:**
- Bài toán phân loại nhị phân chuẩn
- Cần tốc độ tính toán cao
- Muốn giải thích odds ratio
- Dữ liệu cân bằng, không có outliers cực đoan

### **Probit** - Cho Dữ liệu Gaussian
**Sử dụng khi:**
- Dữ liệu có phân phối gần Gaussian
- Cần mô hình hóa threshold effects
- Quan tâm đến tail behavior chính xác
- Có thời gian tính toán (chậm hơn sigmoid)

### **Complementary Log-log** - Cho Rare Events
**Sử dụng khi:**
- Modeling rare events (y=1 hiếm)
- Survival analysis
- Time-to-event data
- Asymmetric data distribution

### **Cauchit** - Cho Heavy-tailed Data
**Sử dụng khi:**
- Dữ liệu có nhiều outliers
- Heavy-tailed distributions
- Robust modeling cần thiết

## 💡 Kết luận về Link Functions

### **Tại sao Sigmoid vẫn là lựa chọn tốt nhất?**

1. **🧮 Toán học Elegant:**
   - Đạo hàm đơn giản: $$\sigma'(z) = \sigma(z)(1-\sigma(z))$$
   - Tính toán nhanh, ổn định số học
   - Không cần tra bảng hay tính tích phân

2. **📊 Ý nghĩa Xác suất Tự nhiên:**
   - Xuất phát từ log-odds model
   - Giải thích trực quan (odds ratio)
   - Symmetric around 0.5

3. **⚡ Hiệu suất Tính toán:**
   - Chỉ cần một phép chia và exponential
   - Gradient descent hiệu quả
   - Phù hợp cho big data

4. **🔄 Tính Lồi Đảm bảo:**
   - Cross-entropy với sigmoid luôn lồi
   - Global optimum guaranteed
   - Thuật toán hội tụ ổn định

**Khuyến nghị:** Bắt đầu với sigmoid, chỉ chuyển sang link function khác khi có lý do cụ thể và đã thử nghiệm so sánh hiệu suất.

## 🔢 Mở rộng: Softmax Regression (Multi-class Classification)

*Logistic Regression chỉ xử lý được 2 lớp. Vậy làm thế nào để phân loại nhiều lớp?*

### 🎯 Từ Binary đến Multi-class

**Bài toán Multi-class Classification:**
- **Input**: $$\mathbf{x} \in \mathbb{R}^p$$
- **Output**: $$y \in \{1, 2, 3, ..., K\}$$ (K lớp)
- **Mục tiêu**: Dự đoán xác suất cho mỗi lớp

**Ví dụ thực tế:**
- **Nhận dạng chữ số**: 0, 1, 2, ..., 9 (10 lớp)
- **Phân loại email**: spam, promotion, social, primary (4 lớp)
- **Chẩn đoán bệnh**: khỏe mạnh, cảm lạnh, viêm họng, COVID (4 lớp)

### 🧮 Softmax Function

**Mở rộng từ Sigmoid:**
- **Sigmoid**: $$\sigma(z) = \frac{e^z}{1 + e^z}$$ (2 lớp)
- **Softmax**: $$\text{softmax}(\mathbf{z})_i = \frac{e^{z_i}}{\sum_{j=1}^K e^{z_j}}$$ (K lớp)

**Tính chất Softmax:**
- ✅ **Tổng bằng 1**: $$\sum_{i=1}^K \text{softmax}(\mathbf{z})_i = 1$$
- ✅ **Luôn dương**: $$\text{softmax}(\mathbf{z})_i > 0$$ $$\forall i$$
- ✅ **Monotonic**: Lớp có $$z_i$$ lớn hơn → xác suất cao hơn
- ✅ **Smooth**: Khả vi mọi nơi

### 🏗️ Mô hình Softmax Regression

**Tham số mô hình:**
- $$\mathbf{W} \in \mathbb{R}^{p \times K}$$: ma trận trọng số
- $$\mathbf{b} \in \mathbb{R}^K$$: bias vector

**Forward pass:**
$$\mathbf{z} = \mathbf{W}^T \mathbf{x} + \mathbf{b}$$

$$P(y = k | \mathbf{x}) = \frac{e^{z_k}}{\sum_{j=1}^K e^{z_j}}$$

**Dự đoán:**
$$\hat{y} = \arg\max_k P(y = k | \mathbf{x})$$

### 📊 Cross-Entropy Loss cho Multi-class

**One-hot encoding:**
- $$y = 2$$ (lớp 2) → $$\mathbf{y} = [0, 1, 0, 0]$$ (nếu K=4)

**Multi-class Cross-Entropy:**
$$J(\mathbf{W}) = -\sum_{i=1}^n \sum_{k=1}^K y_{i,k} \log p_{i,k}$$

với:
- $$y_{i,k}$$: one-hot encoding của sample $$i$$
- $$p_{i,k} = P(y = k | \mathbf{x}_i)$$: xác suất dự đoán

**Đặc điểm:**
- **Mở rộng tự nhiên** từ binary cross-entropy
- **Vẫn convex** → gradient descent hoạt động tốt
- **Phạt nặng dự đoán sai** như binary case

### 🔄 So sánh Binary vs Multi-class

| Khía cạnh | Binary Logistic | Softmax Regression |
|-----------|-----------------|-------------------|
| **Số lớp** | 2 | K ≥ 2 |
| **Activation** | Sigmoid | Softmax |
| **Tham số** | $$\mathbf{w} \in \mathbb{R}^p$$ | $$\mathbf{W} \in \mathbb{R}^{p \times K}$$ |
| **Output** | 1 xác suất | K xác suất |
| **Loss** | Binary cross-entropy | Multi-class cross-entropy |
| **Gradient** | $$\mathbf{X}^T(\boldsymbol{\sigma} - \mathbf{y})$$ | $$\mathbf{X}^T(\mathbf{P} - \mathbf{Y})$$ |

### 🎛️ Interactive Softmax Demo

<div id="softmax-demo" style="margin: 20px 0;">
    <div style="display: flex; gap: 20px; margin-bottom: 20px;">
        <div style="flex: 1;">
            <h4>🎚️ Điều khiển Logits</h4>
            <div style="margin: 10px 0;">
                <label for="z1-slider">z₁ (Class 1): <span id="z1-value">1.0</span></label>
                <input type="range" id="z1-slider" min="-3" max="3" step="0.1" value="1.0" style="width: 100%;">
            </div>
            <div style="margin: 10px 0;">
                <label for="z2-slider">z₂ (Class 2): <span id="z2-value">0.5</span></label>
                <input type="range" id="z2-slider" min="-3" max="3" step="0.1" value="0.5" style="width: 100%;">
            </div>
            <div style="margin: 10px 0;">
                <label for="z3-slider">z₃ (Class 3): <span id="z3-value">-0.5</span></label>
                <input type="range" id="z3-slider" min="-3" max="3" step="0.1" value="-0.5" style="width: 100%;">
            </div>
            <div style="margin: 10px 0;">
                <label for="z4-slider">z₄ (Class 4): <span id="z4-value">-1.0</span></label>
                <input type="range" id="z4-slider" min="-3" max="3" step="0.1" value="-1.0" style="width: 100%;">
            </div>
        </div>
        <div style="flex: 1;">
            <h4>📊 Softmax Probabilities</h4>
            <div id="probabilities-display" style="font-family: monospace; font-size: 14px;">
                <div>Class 1: <span id="p1">0.000</span></div>
                <div>Class 2: <span id="p2">0.000</span></div>
                <div>Class 3: <span id="p3">0.000</span></div>
                <div>Class 4: <span id="p4">0.000</span></div>
                <hr>
                <div><strong>Sum: <span id="sum">1.000</span></strong></div>
                <div><strong>Predicted: Class <span id="predicted">1</span></strong></div>
            </div>
        </div>
    </div>
    
    <div style="display: flex; gap: 20px;">
        <div style="flex: 1;">
            <h4>📈 Probability Bars</h4>
            <canvas id="prob-bars-canvas" width="400" height="300" style="border: 1px solid #ccc;"></canvas>
        </div>
        <div style="flex: 1;">
            <h4>🥧 Probability Pie Chart</h4>
            <canvas id="prob-pie-canvas" width="400" height="300" style="border: 1px solid #ccc;"></canvas>
        </div>
    </div>
</div>

<script>
class SoftmaxDemo {
    constructor() {
        this.z = [1.0, 0.5, -0.5, -1.0];
        this.colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'];
        this.setupEventListeners();
        this.updateDisplay();
    }
    
    setupEventListeners() {
        for (let i = 1; i <= 4; i++) {
            const slider = document.getElementById(`z${i}-slider`);
            if (slider) {
                slider.addEventListener('input', (e) => {
                    this.z[i-1] = parseFloat(e.target.value);
                    document.getElementById(`z${i}-value`).textContent = this.z[i-1].toFixed(1);
                    this.updateDisplay();
                });
            }
        }
    }
    
    softmax(z) {
        const maxZ = Math.max(...z);
        const expZ = z.map(zi => Math.exp(zi - maxZ)); // Numerical stability
        const sumExpZ = expZ.reduce((sum, exp) => sum + exp, 0);
        return expZ.map(exp => exp / sumExpZ);
    }
    
    updateDisplay() {
        const probs = this.softmax(this.z);
        const sum = probs.reduce((s, p) => s + p, 0);
        const predicted = probs.indexOf(Math.max(...probs)) + 1;
        
        // Update probability display
        for (let i = 1; i <= 4; i++) {
            const elem = document.getElementById(`p${i}`);
            if (elem) {
                elem.textContent = probs[i-1].toFixed(3);
                elem.style.color = this.colors[i-1];
                elem.style.fontWeight = predicted === i ? 'bold' : 'normal';
            }
        }
        
        const sumElem = document.getElementById('sum');
        if (sumElem) sumElem.textContent = sum.toFixed(3);
        
        const predElem = document.getElementById('predicted');
        if (predElem) {
            predElem.textContent = predicted;
            predElem.style.color = this.colors[predicted-1];
        }
        
        this.drawBars(probs);
        this.drawPie(probs);
    }
    
    drawBars(probs) {
        const canvas = document.getElementById('prob-bars-canvas');
        if (!canvas) return;
        
        const ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        const barWidth = 60;
        const maxHeight = 200;
        const startX = 50;
        const startY = canvas.height - 50;
        
        // Draw axes
        ctx.strokeStyle = '#ccc';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(30, 30);
        ctx.lineTo(30, startY);
        ctx.lineTo(canvas.width - 20, startY);
        ctx.stroke();
        
        // Draw bars
        for (let i = 0; i < 4; i++) {
            const x = startX + i * (barWidth + 20);
            const height = probs[i] * maxHeight;
            
            ctx.fillStyle = this.colors[i];
            ctx.fillRect(x, startY - height, barWidth, height);
            
            // Labels
            ctx.fillStyle = '#333';
            ctx.font = '12px Arial';
            ctx.textAlign = 'center';
            ctx.fillText(`Class ${i+1}`, x + barWidth/2, startY + 20);
            ctx.fillText(probs[i].toFixed(3), x + barWidth/2, startY - height - 5);
        }
        
        // Y-axis labels
        ctx.textAlign = 'right';
        ctx.fillText('0.0', 25, startY + 5);
        ctx.fillText('0.5', 25, startY - maxHeight/2 + 5);
        ctx.fillText('1.0', 25, startY - maxHeight + 5);
    }
    
    drawPie(probs) {
        const canvas = document.getElementById('prob-pie-canvas');
        if (!canvas) return;
        
        const ctx = canvas.getContext('2d');
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const radius = 100;
        
        let currentAngle = -Math.PI / 2; // Start from top
        
        for (let i = 0; i < 4; i++) {
            const sliceAngle = probs[i] * 2 * Math.PI;
            
            // Draw slice
            ctx.beginPath();
            ctx.moveTo(centerX, centerY);
            ctx.arc(centerX, centerY, radius, currentAngle, currentAngle + sliceAngle);
            ctx.closePath();
            ctx.fillStyle = this.colors[i];
            ctx.fill();
            ctx.strokeStyle = '#fff';
            ctx.lineWidth = 2;
            ctx.stroke();
            
            // Draw label
            if (probs[i] > 0.05) { // Only show label if slice is big enough
                const labelAngle = currentAngle + sliceAngle / 2;
                const labelX = centerX + Math.cos(labelAngle) * radius * 0.7;
                const labelY = centerY + Math.sin(labelAngle) * radius * 0.7;
                
                ctx.fillStyle = '#fff';
                ctx.font = 'bold 12px Arial';
                ctx.textAlign = 'center';
                ctx.fillText(`${i+1}`, labelX, labelY + 4);
            }
            
            currentAngle += sliceAngle;
        }
        
        // Legend
        for (let i = 0; i < 4; i++) {
            const legendY = 20 + i * 20;
            ctx.fillStyle = this.colors[i];
            ctx.fillRect(20, legendY, 15, 15);
            ctx.fillStyle = '#333';
            ctx.font = '12px Arial';
            ctx.textAlign = 'left';
            ctx.fillText(`Class ${i+1}: ${(probs[i] * 100).toFixed(1)}%`, 40, legendY + 12);
        }
    }
}

// Initialize demo when page loads
document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('softmax-demo')) {
        new SoftmaxDemo();
    }
});
</script>

<style>
#softmax-demo {
    font-family: Arial, sans-serif;
    max-width: 1000px;
    margin: 0 auto;
}

#softmax-demo canvas {
    border-radius: 4px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

#softmax-demo input[type="range"] {
    width: 100%;
    margin: 5px 0;
}

#probabilities-display {
    background-color: #f5f5f5;
    padding: 15px;
    border-radius: 4px;
    line-height: 1.6;
}

#probabilities-display div {
    margin: 5px 0;
}
</style>

### 🎯 Ứng dụng Thực tế của Softmax

#### **1. Computer Vision**
- **Image Classification**: ImageNet (1000 lớp)
- **Object Detection**: COCO dataset (80 lớp)
- **Medical Imaging**: Phân loại X-ray, MRI

#### **2. Natural Language Processing**
- **Sentiment Analysis**: positive, negative, neutral
- **Language Detection**: English, Vietnamese, Chinese, ...
- **Text Classification**: news categories, spam detection

#### **3. Recommendation Systems**
- **Content Categories**: movies, music, books
- **User Preferences**: age groups, interests
- **Product Classification**: electronics, fashion, food

### 🔄 Kết nối với Deep Learning

**Softmax là building block quan trọng:**
- **Output layer** của neural networks
- **Attention mechanisms** trong Transformers
- **Policy networks** trong Reinforcement Learning

**Từ Logistic → Softmax → Neural Networks:**
1. **Logistic Regression**: Linear + Sigmoid
2. **Softmax Regression**: Linear + Softmax  
3. **Neural Networks**: Multiple layers + Softmax

### 💡 Tóm tắt Softmax Regression

**Ưu điểm:**
- ✅ **Mở rộng tự nhiên** từ binary classification
- ✅ **Probabilistic output** có ý nghĩa
- ✅ **Convex optimization** → đáng tin cậy
- ✅ **Efficient training** với gradient descent

**Nhược điểm:**
- ❌ **Linear decision boundaries** (như logistic)
- ❌ **Assumes linear separability**
- ❌ **May struggle** với complex patterns

**Khi nào sử dụng:**
- Multi-class classification problems
- Cần probabilistic outputs
- Baseline model trước khi thử complex methods
- Interpretability quan trọng

**Softmax Regression là bước đệm hoàn hảo** giữa simple logistic regression và complex neural networks!
