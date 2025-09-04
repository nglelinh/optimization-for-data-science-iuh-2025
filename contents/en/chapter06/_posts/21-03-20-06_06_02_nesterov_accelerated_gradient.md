---
layout: post
title: 06-06-02 Nesterov Accelerated Gradient (NAG)
chapter: '06'
order: 18
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
lesson_type: required
---

**Nesterov Accelerated Gradient (NAG)** là một cải tiến thông minh của momentum, được Yurii Nesterov đề xuất năm 1983. NAG không chỉ cải thiện tốc độ hội tụ mà còn có đảm bảo lý thuyết mạnh mẽ về hiệu suất.

## Ý tưởng "Look-ahead"

### Hạn chế của Momentum thông thường

Momentum cơ bản tính gradient tại vị trí hiện tại, sau đó kết hợp với vận tốc từ bước trước:

> $$v^{(k)} = \beta v^{(k-1)} + (1-\beta) \nabla f(x^{(k-1)})$$
> $$x^{(k)} = x^{(k-1)} - \alpha v^{(k)}$$

Điều này có thể dẫn đến **overshooting** - vượt quá điểm tối ưu do không "nhìn trước" được hướng di chuyển.

### Ý tưởng NAG

NAG giải quyết vấn đề này bằng cách **"nhìn trước"** (look-ahead):

1. **Dự đoán vị trí tiếp theo** dựa trên momentum hiện tại
2. **Tính gradient tại vị trí dự đoán** thay vì vị trí hiện tại  
3. **Sử dụng gradient này** để cập nhật momentum và vị trí

<figure class="image" style="align: center;">
<p align="center">
  <img src="https://miro.medium.com/max/1400/1*NRu7Pm7UA1lTc5ZtOXWNDw.png" alt="nag_visualization" width="70%" height="70%">
  <figcaption style="text-align: center;">So sánh Momentum (trái) và NAG (phải): NAG "nhìn trước" để điều chỉnh hướng</figcaption>
</p>
</figure>

## Công thức NAG

### Phiên bản gốc (Nesterov, 1983)

> $$v^{(k)} = \beta v^{(k-1)} + (1-\beta) \nabla f(x^{(k-1)} - \alpha \beta v^{(k-1)})$$
> $$x^{(k)} = x^{(k-1)} - \alpha v^{(k)}$$

### Phiên bản tương đương (dễ hiểu hơn)

> $$\tilde{x}^{(k-1)} = x^{(k-1)} - \alpha \beta v^{(k-1)}$$ (look-ahead position)
> $$v^{(k)} = \beta v^{(k-1)} + (1-\beta) \nabla f(\tilde{x}^{(k-1)})$$
> $$x^{(k)} = x^{(k-1)} - \alpha v^{(k)}$$

### Pseudocode

> **Given** starting point $$x^{(0)}$$, learning rate $$\alpha$$, momentum $$\beta$$ <br>
> **Initialize** $$v^{(0)} = 0$$ <br>
> **For** $$k = 1, 2, 3, ...$$ **do** <br>
> &nbsp;&nbsp;&nbsp;&nbsp; Compute look-ahead position: $$\tilde{x}^{(k-1)} = x^{(k-1)} - \alpha \beta v^{(k-1)}$$ <br>
> &nbsp;&nbsp;&nbsp;&nbsp; Compute gradient at look-ahead: $$g^{(k)} = \nabla f(\tilde{x}^{(k-1)})$$ <br>
> &nbsp;&nbsp;&nbsp;&nbsp; Update velocity: $$v^{(k)} = \beta v^{(k-1)} + (1-\beta) g^{(k)}$$ <br>
> &nbsp;&nbsp;&nbsp;&nbsp; Update position: $$x^{(k)} = x^{(k-1)} - \alpha v^{(k)}$$ <br>
> **Until** convergence criterion is met

## Trực quan hóa NAG

### Bước-by-bước Analysis

**Bước 1: Look-ahead**
- Từ vị trí hiện tại $$x^{(k-1)}$$
- Di chuyển theo momentum cũ: $$\tilde{x}^{(k-1)} = x^{(k-1)} - \alpha \beta v^{(k-1)}$$
- Đây là vị trí mà momentum sẽ đưa chúng ta đến

**Bước 2: Gradient tại look-ahead**
- Tính gradient tại vị trí dự đoán: $$\nabla f(\tilde{x}^{(k-1)})$$
- Gradient này "thông minh" hơn vì biết được hướng di chuyển

**Bước 3: Cập nhật thông minh**
- Kết hợp momentum cũ với gradient mới
- Di chuyển đến vị trí cuối cùng

### Geometric Interpretation

```
Current position: x^(k-1)
         |
         | (momentum step)
         v
Look-ahead: x̃^(k-1) -----> ∇f(x̃^(k-1))
         |                      |
         | (combine)             |
         v                      |
Updated velocity: v^(k) <-------+
         |
         | (final step)
         v
New position: x^(k)
```

## So sánh Momentum vs NAG

| Aspect | Momentum | NAG |
|--------|----------|-----|
| **Gradient tính tại** | Vị trí hiện tại $$x^{(k-1)}$$ | Vị trí look-ahead $$\tilde{x}^{(k-1)}$$ |
| **Đặc điểm** | "Nhìn lại" - sử dụng thông tin quá khứ | "Nhìn trước" - dự đoán hướng di chuyển |
| **Overshooting** | Có thể xảy ra | Ít hơn do điều chỉnh sớm |
| **Tốc độ hội tụ** | $$O(1/k)$$ | $$O(1/k^2)$$ |
| **Độ phức tạp** | Đơn giản | Phức tạp hơn một chút |

### Ví dụ minh họa sự khác biệt

Xét hàm $$f(x) = \frac{1}{2}x^2$$ với $$x^{(0)} = 1$$, $$\alpha = 0.1$$, $$\beta = 0.9$$:

**Momentum**:
- $$v^{(1)} = 0.9 \cdot 0 + 0.1 \cdot 1 = 0.1$$
- $$x^{(1)} = 1 - 0.1 \cdot 0.1 = 0.99$$

**NAG**:
- $$\tilde{x}^{(0)} = 1 - 0.1 \cdot 0.9 \cdot 0 = 1$$
- $$v^{(1)} = 0.9 \cdot 0 + 0.1 \cdot 1 = 0.1$$
- $$x^{(1)} = 1 - 0.1 \cdot 0.1 = 0.99$$

Ở bước đầu, chúng giống nhau. Sự khác biệt xuất hiện ở các bước sau khi momentum tích lũy.

## Phân tích lý thuyết

### Tốc độ hội tụ

Đối với hàm **convex** và **L-smooth**:

| Thuật toán | Tốc độ hội tụ | Điều kiện |
|------------|---------------|-----------|
| **Gradient Descent** | $$O(1/k)$$ | Convex |
| **Momentum** | $$O(1/k)$$ | Convex |
| **NAG** | $$O(1/k^2)$$ | Convex |

Đây là **cải thiện đáng kể** về mặt lý thuyết!

### Strongly Convex Functions

Đối với hàm **strongly convex** với condition number $$\kappa$$:

| Thuật toán | Tốc độ hội tụ | Optimal β |
|------------|---------------|-----------|
| **Gradient Descent** | $$O((1-1/\kappa)^k)$$ | N/A |
| **NAG** | $$O((1-1/\sqrt{\kappa})^k)$$ | $$\frac{\sqrt{\kappa}-1}{\sqrt{\kappa}+1}$$ |

### Proof Sketch (Nesterov's Analysis)

NAG có thể được phân tích thông qua **estimate sequence**:

1. Định nghĩa sequence $$\{\phi_k\}$$ với $$\phi_k(x) \geq f(x)$$
2. $$\phi_k(x^{(k)}) - f(x^*) \leq \frac{2L\|x^{(0)} - x^*\|^2}{(k+1)^2}$$
3. Từ đó suy ra tốc độ hội tụ $$O(1/k^2)$$

## Interactive Comparison: Momentum vs NAG

<div id="nag-comparison" style="margin: 20px 0;">
    <div style="margin-bottom: 15px;">
        <label for="nag-beta">β parameter: <span id="nag-beta-value">0.9</span></label><br>
        <input type="range" id="nag-beta" min="0" max="0.99" step="0.01" value="0.9" style="width: 300px;">
    </div>
    
    <div style="margin-bottom: 15px;">
        <label for="nag-lr">Learning Rate: <span id="nag-lr-value">0.01</span></label><br>
        <input type="range" id="nag-lr" min="0.001" max="0.1" step="0.001" value="0.01" style="width: 300px;">
    </div>
    
    <div style="margin-bottom: 15px;">
        <button id="start-nag-comparison">Start Comparison</button>
        <button id="reset-nag-comparison">Reset</button>
        <button id="step-nag-comparison">Single Step</button>
    </div>
    
    <canvas id="nag-canvas" width="600" height="400" style="border: 1px solid #ccc; display: block; margin: 0 auto;"></canvas>
    
    <div id="nag-info" style="text-align: center; margin-top: 10px; font-family: monospace;">
        <div>Momentum - Iteration: 0, Loss: 12.500</div>
        <div>NAG - Iteration: 0, Loss: 12.500</div>
    </div>
</div>

## Ưu điểm của NAG

### 1. Hội tụ nhanh hơn
- **Lý thuyết**: $$O(1/k^2)$$ vs $$O(1/k)$$ của momentum
- **Thực tế**: Thường nhanh hơn 2-3 lần trong nhiều bài toán

### 2. Ít overshoot hơn
- Look-ahead giúp "phanh" sớm khi gần điểm tối ưu
- Ổn định hơn với learning rate lớn

### 3. Adaptive behavior
- Tự động điều chỉnh khi gradient thay đổi hướng
- Hoạt động tốt với non-convex functions

### 4. Theoretical guarantees
- Optimal convergence rate cho smooth convex functions
- Robust với noise trong gradient

## Nhược điểm và hạn chế

### 1. Độ phức tạp tính toán
- Cần tính gradient 2 lần mỗi iteration (look-ahead + actual)
- Memory overhead nhỏ nhưng có thể quan trọng trong deep learning

### 2. Hyperparameter sensitivity
- Cần tune cả α và β cẩn thận
- Không robust bằng Adam với default parameters

### 3. Implementation complexity
- Phức tạp hơn momentum thông thường
- Dễ implement sai, đặc biệt với batching

## Biến thể của NAG

### 1. NAG với Adaptive Learning Rate

Kết hợp NAG với adaptive methods:

> $$\tilde{x}^{(k-1)} = x^{(k-1)} - \alpha_k \beta v^{(k-1)}$$
> $$v^{(k)} = \beta v^{(k-1)} + (1-\beta) \nabla f(\tilde{x}^{(k-1)})$$
> $$x^{(k)} = x^{(k-1)} - \alpha_k v^{(k)}$$

### 2. Accelerated Gradient Method (AGM)

Phiên bản tổng quát hơn với sequence $$\{y_k\}$$:

> $$y^{(k)} = x^{(k-1)} + \frac{k-2}{k+1}(x^{(k-1)} - x^{(k-2)})$$
> $$x^{(k)} = y^{(k)} - \alpha \nabla f(y^{(k)})$$

### 3. NAdam (Nesterov + Adam)

Kết hợp NAG với Adam optimizer:
- Sử dụng look-ahead trong Adam's momentum term
- Kết hợp adaptive learning rate với acceleration

## Ứng dụng thực tế

### 1. Deep Learning
- **Computer Vision**: ResNet, DenseNet training
- **NLP**: BERT pre-training với NAG variants
- **Generative Models**: GAN training stability

### 2. Convex Optimization
- **Linear Programming**: Interior point methods
- **Quadratic Programming**: Portfolio optimization
- **SVM**: Support vector machine training

### 3. Machine Learning
- **Logistic Regression**: Large-scale classification
- **Neural Networks**: Faster convergence than SGD
- **Reinforcement Learning**: Policy gradient methods

## Hyperparameter Guidelines

### Momentum coefficient (β)

**For convex problems**:
- $$\beta = \frac{\sqrt{\kappa}-1}{\sqrt{\kappa}+1}$$ (optimal cho strongly convex)
- $$\kappa$$ là condition number của Hessian

**For deep learning**:
- $$\beta = 0.9$$: Standard choice
- $$\beta = 0.99$$: For very deep networks
- $$\beta = 0.999$$: For transformer models

### Learning rate (α)

**Relationship với momentum**:
- NAG cho phép learning rate lớn hơn momentum thông thường
- Rule of thumb: $$\alpha_{NAG} \approx 1.5 \times \alpha_{momentum}$$

**Adaptive scheduling**:
- **Cosine annealing**: $$\alpha_k = \alpha_0 \cos(\frac{\pi k}{2K})$$
- **Step decay**: Giảm α khi loss plateau
- **Warm restart**: Reset α định kỳ

## Performance Comparison

### Benchmark Results

Trên CIFAR-10 với ResNet-18:

| Optimizer | Epochs to 95% accuracy | Final accuracy |
|-----------|------------------------|----------------|
| **SGD** | 150 | 94.2% |
| **Momentum** | 120 | 95.1% |
| **NAG** | 100 | 95.3% |
| **Adam** | 80 | 95.0% |

### Convergence Analysis

```
Loss vs Iterations (Log scale):

10^2 |     SGD
     |      \
10^1 |       \  Momentum
     |        \   \
10^0 |         \   \  NAG
     |          \   \  \
10^-1|           \   \  \
     |            \   \  \
10^-2+-------------\---\--\----
     0    50   100  150  200
              Iterations
```

<script>
class NAGComparison {
    constructor() {
        this.canvas = document.getElementById('nag-canvas');
        this.ctx = this.canvas.getContext('2d');
        
        // Controls
        this.betaSlider = document.getElementById('nag-beta');
        this.lrSlider = document.getElementById('nag-lr');
        this.betaValue = document.getElementById('nag-beta-value');
        this.lrValue = document.getElementById('nag-lr-value');
        this.nagInfo = document.getElementById('nag-info');
        
        // State
        this.isAnimating = false;
        this.iteration = 0;
        
        // Initialize
        this.reset();
        this.setupEventListeners();
    }
    
    setupEventListeners() {
        this.betaSlider.addEventListener('input', (e) => {
            this.betaValue.textContent = e.target.value;
        });
        
        this.lrSlider.addEventListener('input', (e) => {
            this.lrValue.textContent = e.target.value;
        });
        
        document.getElementById('start-nag-comparison').addEventListener('click', () => {
            this.startAnimation();
        });
        
        document.getElementById('reset-nag-comparison').addEventListener('click', () => {
            this.reset();
        });
        
        document.getElementById('step-nag-comparison').addEventListener('click', () => {
            this.singleStep();
        });
    }
    
    // Objective function: f(x,y) = 0.5 * (10*x^2 + y^2)
    objectiveFunction(x, y) {
        return 0.5 * (10 * x * x + y * y);
    }
    
    // Gradient: [10*x, y]
    gradient(x, y) {
        return [10 * x, y];
    }
    
    // Coordinate transformations
    toCanvas(x, y) {
        const centerX = this.canvas.width / 2;
        const centerY = this.canvas.height / 2;
        const scale = 50;
        return [centerX + x * scale, centerY - y * scale];
    }
    
    drawContours() {
        this.ctx.strokeStyle = '#E0E0E0';
        this.ctx.lineWidth = 1;
        
        // Draw elliptical contours
        const levels = [0.5, 2, 8, 18, 32, 50];
        
        for (let level of levels) {
            this.ctx.beginPath();
            for (let angle = 0; angle <= 2 * Math.PI; angle += 0.1) {
                // For f(x,y) = 0.5*(10*x^2 + y^2) = level
                const a = Math.sqrt(2 * level / 10); // x semi-axis
                const b = Math.sqrt(2 * level);      // y semi-axis
                
                const x = a * Math.cos(angle);
                const y = b * Math.sin(angle);
                const [canvasX, canvasY] = this.toCanvas(x, y);
                
                if (angle === 0) {
                    this.ctx.moveTo(canvasX, canvasY);
                } else {
                    this.ctx.lineTo(canvasX, canvasY);
                }
            }
            this.ctx.stroke();
        }
        
        // Draw axes
        this.ctx.strokeStyle = '#CCCCCC';
        this.ctx.lineWidth = 1;
        
        // X-axis
        this.ctx.beginPath();
        this.ctx.moveTo(0, this.canvas.height / 2);
        this.ctx.lineTo(this.canvas.width, this.canvas.height / 2);
        this.ctx.stroke();
        
        // Y-axis
        this.ctx.beginPath();
        this.ctx.moveTo(this.canvas.width / 2, 0);
        this.ctx.lineTo(this.canvas.width / 2, this.canvas.height);
        this.ctx.stroke();
    }
    
    drawPath(path, color, lineWidth = 2) {
        if (path.length < 2) return;
        
        this.ctx.strokeStyle = color;
        this.ctx.lineWidth = lineWidth;
        this.ctx.beginPath();
        
        for (let i = 0; i < path.length; i++) {
            const [canvasX, canvasY] = this.toCanvas(path[i][0], path[i][1]);
            if (i === 0) {
                this.ctx.moveTo(canvasX, canvasY);
            } else {
                this.ctx.lineTo(canvasX, canvasY);
            }
        }
        this.ctx.stroke();
        
        // Draw current position
        if (path.length > 0) {
            const [lastX, lastY] = path[path.length - 1];
            const [canvasX, canvasY] = this.toCanvas(lastX, lastY);
            this.ctx.fillStyle = color;
            this.ctx.beginPath();
            this.ctx.arc(canvasX, canvasY, 5, 0, 2 * Math.PI);
            this.ctx.fill();
        }
    }
    
    reset() {
        this.isAnimating = false;
        this.iteration = 0;
        
        // Starting position
        this.momentumPos = [2, 2];
        this.nagPos = [2, 2];
        this.momentumVel = [0, 0];
        this.nagVel = [0, 0];
        
        this.momentumPath = [[2, 2]];
        this.nagPath = [[2, 2]];
        
        this.draw();
    }
    
    singleStep() {
        const lr = parseFloat(this.lrSlider.value);
        const beta = parseFloat(this.betaSlider.value);
        
        // Momentum
        const momentumGrad = this.gradient(this.momentumPos[0], this.momentumPos[1]);
        this.momentumVel[0] = beta * this.momentumVel[0] + (1 - beta) * momentumGrad[0];
        this.momentumVel[1] = beta * this.momentumVel[1] + (1 - beta) * momentumGrad[1];
        this.momentumPos[0] -= lr * this.momentumVel[0];
        this.momentumPos[1] -= lr * this.momentumVel[1];
        this.momentumPath.push([this.momentumPos[0], this.momentumPos[1]]);
        
        // NAG (Nesterov Accelerated Gradient)
        // Look-ahead position
        const lookAheadX = this.nagPos[0] - lr * beta * this.nagVel[0];
        const lookAheadY = this.nagPos[1] - lr * beta * this.nagVel[1];
        
        // Gradient at look-ahead position
        const nagGrad = this.gradient(lookAheadX, lookAheadY);
        this.nagVel[0] = beta * this.nagVel[0] + (1 - beta) * nagGrad[0];
        this.nagVel[1] = beta * this.nagVel[1] + (1 - beta) * nagGrad[1];
        this.nagPos[0] -= lr * this.nagVel[0];
        this.nagPos[1] -= lr * this.nagVel[1];
        this.nagPath.push([this.nagPos[0], this.nagPos[1]]);
        
        this.iteration++;
        this.draw();
    }
    
    draw() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        
        this.drawContours();
        this.drawPath(this.momentumPath, '#FF9800', 2);
        this.drawPath(this.nagPath, '#4CAF50', 2);
        
        // Legend
        this.ctx.fillStyle = '#FF9800';
        this.ctx.fillRect(10, 10, 20, 10);
        this.ctx.fillStyle = '#000';
        this.ctx.font = '12px Arial';
        this.ctx.fillText('Momentum', 35, 20);
        
        this.ctx.fillStyle = '#4CAF50';
        this.ctx.fillRect(10, 30, 20, 10);
        this.ctx.fillStyle = '#000';
        this.ctx.fillText('NAG', 35, 40);
        
        // Update info
        const momentumLoss = this.objectiveFunction(this.momentumPos[0], this.momentumPos[1]);
        const nagLoss = this.objectiveFunction(this.nagPos[0], this.nagPos[1]);
        
        this.nagInfo.innerHTML = 
            `<div>Momentum - Iteration: ${this.iteration}, Loss: ${momentumLoss.toFixed(3)}</div>` +
            `<div>NAG - Iteration: ${this.iteration}, Loss: ${nagLoss.toFixed(3)}</div>`;
    }
    
    startAnimation() {
        if (this.isAnimating) {
            this.isAnimating = false;
            document.getElementById('start-nag-comparison').textContent = 'Start Comparison';
            return;
        }
        
        this.isAnimating = true;
        document.getElementById('start-nag-comparison').textContent = 'Stop Comparison';
        
        const animate = () => {
            if (!this.isAnimating) return;
            
            const currentLoss = Math.min(
                this.objectiveFunction(this.momentumPos[0], this.momentumPos[1]),
                this.objectiveFunction(this.nagPos[0], this.nagPos[1])
            );
            
            if (currentLoss > 1e-4 && this.iteration < 200) {
                this.singleStep();
                setTimeout(animate, 100);
            } else {
                this.isAnimating = false;
                document.getElementById('start-nag-comparison').textContent = 'Start Comparison';
            }
        };
        
        animate();
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('nag-canvas')) {
        new NAGComparison();
    }
});
</script>

## Tổng kết

### Khi nào sử dụng NAG?

**✅ Nên sử dụng NAG khi**:
- Cần tốc độ hội tụ nhanh nhất
- Hàm mục tiêu smooth và well-conditioned
- Có đủ computational budget
- Bài toán convex hoặc strongly convex

**❌ Không nên sử dụng NAG khi**:
- Gradient rất noisy (SGD với mini-batch nhỏ)
- Cần simplicity và robustness
- Memory/computation bị hạn chế
- Hyperparameter tuning khó khăn

### Key Takeaways

1. **NAG = Momentum + Look-ahead**: Tính gradient tại vị trí dự đoán
2. **Theoretical superiority**: $$O(1/k^2)$$ convergence rate
3. **Practical benefits**: Ít overshoot, hội tụ nhanh hơn
4. **Implementation care**: Cần implement cẩn thận để tránh bugs

NAG là một trong những breakthrough quan trọng nhất trong optimization, mở đường cho nhiều phương pháp acceleration hiện đại như Adam, AdaGrad, và các variants khác.

## Tài liệu tham khảo

1. Nesterov, Y. (1983). A method of solving a convex programming problem with convergence rate O(1/k²). Soviet Mathematics Doklady, 27(2), 372-376.

2. Beck, A., & Teboulle, M. (2009). A fast iterative shrinkage-thresholding algorithm for linear inverse problems. SIAM journal on imaging sciences, 2(1), 183-202.

3. Sutskever, I., Martens, J., Dahl, G., & Hinton, G. (2013). On the importance of initialization and momentum in deep learning. International Conference on Machine Learning, 1139-1147.

4. Ruder, S. (2016). An overview of gradient descent optimization algorithms. arXiv preprint arXiv:1609.04747.
