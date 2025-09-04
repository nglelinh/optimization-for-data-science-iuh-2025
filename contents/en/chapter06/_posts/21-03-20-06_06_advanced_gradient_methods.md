---
layout: post
title: 06-06 Các thuật toán tối ưu Gradient Descent
chapter: '06'
order: 16
owner: Kyeongmin Woo
categories:
- chapter06
lang: en
lesson_type: required
---

Gradient descent cơ bản có thể gặp phải một số vấn đề trong thực tế, đặc biệt là tốc độ hội tụ chậm và dao động quanh điểm tối ưu. Để khắc phục những hạn chế này, các nhà nghiên cứu đã phát triển nhiều biến thể cải tiến của gradient descent.

## Tổng quan về các thuật toán tối ưu

### Vấn đề của Gradient Descent cơ bản

**Standard Gradient Descent** có công thức đơn giản:
> $$x^{(k)} = x^{(k-1)} - \alpha \nabla f(x^{(k-1)})$$

Tuy nhiên, nó gặp phải những hạn chế sau:

1. **Tốc độ hội tụ chậm**: Đặc biệt với hàm có condition number cao
2. **Dao động "zigzag"**: Trong các thung lũng hẹp hoặc khi gradient thay đổi hướng thường xuyên  
3. **Khó vượt qua local minima**: Thiếu "quán tính" để vượt qua các điểm cực tiểu địa phương
4. **Sensitivity với learning rate**: Quá nhỏ → chậm, quá lớn → diverge

### Ý tưởng cải tiến chính

Để khắc phục những vấn đề trên, hai hướng tiếp cận chính được phát triển:

**1. Momentum (Polyak, 1964)**
- Thêm "quán tính" từ các bước trước đó
- Tích lũy vận tốc theo hướng nhất quán
- Làm mượt dao động theo hướng không nhất quán

**2. Acceleration (Nesterov, 1983)**  
- "Nhìn trước" để dự đoán hướng di chuyển
- Cải thiện tốc độ hội tụ từ $$O(1/k)$$ lên $$O(1/k^2)$$
- Giảm overshoot gần điểm tối ưu

## Roadmap của chương này

Chúng ta sẽ tìm hiểu chi tiết hai thuật toán quan trọng nhất:

### [6.6.1 Momentum]({{ site.baseurl }}/contents/en/chapter06/06_06_01_momentum)
- **Ý tưởng**: Sử dụng "quán tính" từ vật lý
- **Công thức**: $$v^{(k)} = \beta v^{(k-1)} + (1-\beta) \nabla f(x^{(k-1)})$$
- **Ưu điểm**: Tăng tốc hội tụ, giảm dao động, vượt local minima
- **Ứng dụng**: Deep learning, computer vision, NLP

### [6.6.2 Nesterov Accelerated Gradient (NAG)]({{ site.baseurl }}/contents/en/chapter06/06_06_02_nesterov_accelerated_gradient)
- **Ý tưởng**: "Look-ahead" để tính gradient tại vị trí dự đoán
- **Công thức**: $$v^{(k)} = \beta v^{(k-1)} + (1-\beta) \nabla f(\tilde{x}^{(k-1)})$$
- **Ưu điểm**: Tốc độ hội tụ $$O(1/k^2)$$, ít overshoot
- **Lý thuyết**: Optimal convergence rate cho smooth convex functions

## So sánh tổng quan

| Thuật toán | Tốc độ hội tụ | Độ phức tạp | Memory | Stability | Use case |
|------------|---------------|-------------|---------|-----------|----------|
| **Standard GD** | $$O(1/k)$$ | Thấp | Thấp | Cao | Simple problems |
| **Momentum** | $$O(1/k)$$ | Trung bình | Thấp | Trung bình | Most practical problems |
| **NAG** | $$O(1/k^2)$$ | Cao | Thấp | Trung bình | When speed is critical |

## Interactive Overview Demo

<div id="overview-comparison" style="margin: 20px 0;">
    <div style="margin-bottom: 15px;">
        <label for="overview-function">Function Type:</label>
        <select id="overview-function" style="margin-left: 10px;">
            <option value="quadratic">Quadratic (Convex)</option>
            <option value="rosenbrock">Rosenbrock (Non-convex)</option>
            <option value="beale">Beale (Non-convex)</option>
        </select>
    </div>
    
    <div style="margin-bottom: 15px;">
        <button id="start-overview">Start All Methods</button>
        <button id="reset-overview">Reset</button>
        <button id="step-overview">Single Step</button>
    </div>
    
    <canvas id="overview-canvas" width="600" height="400" style="border: 1px solid #ccc; display: block; margin: 0 auto;"></canvas>
    
    <div id="overview-info" style="text-align: center; margin-top: 10px; font-family: monospace;">
        <div style="color: #FF5722;">● Standard GD - Iteration: 0, Loss: 12.500</div>
        <div style="color: #FF9800;">● Momentum - Iteration: 0, Loss: 12.500</div>
        <div style="color: #4CAF50;">● NAG - Iteration: 0, Loss: 12.500</div>
    </div>
</div>

## Lịch sử phát triển

### Timeline của các thuật toán optimization

- **1847**: Cauchy - Gradient descent đầu tiên
- **1964**: Polyak - Heavy ball method (Momentum)
- **1983**: Nesterov - Accelerated gradient method
- **1987**: Nesterov - Optimal complexity theory
- **2011**: AdaGrad - Adaptive learning rates
- **2014**: Adam - Adaptive moments
- **2017**: AMSGrad - Fix Adam's convergence issues

### Breakthrough insights

**Polyak's contribution (1964)**:
- Ý tưởng sử dụng history của gradient
- Analogy với heavy ball trong vật lý
- First practical acceleration method

**Nesterov's contribution (1983)**:
- Look-ahead strategy
- Theoretical optimal rate $$O(1/k^2)$$
- Estimate sequence technique

## Khi nào sử dụng thuật toán nào?

### Decision Tree

```
Bài toán optimization
├── Convex function?
│   ├── Yes → Strongly convex?
│   │   ├── Yes → NAG (optimal rate)
│   │   └── No → Momentum hoặc NAG
│   └── No → Non-convex
│       ├── Deep learning → Adam/AdamW
│       ├── Few parameters → NAG
│       └── Many local minima → Momentum
└── Computational budget?
    ├── Limited → Standard GD
    ├── Moderate → Momentum  
    └── High → NAG hoặc Adam
```

### Practical Guidelines

**Chọn Standard GD khi**:
- Bài toán đơn giản, well-conditioned
- Cần implementation đơn giản nhất
- Debugging hoặc baseline

**Chọn Momentum khi**:
- Hầu hết các bài toán thực tế
- Deep learning với SGD
- Cần balance giữa speed và stability

**Chọn NAG khi**:
- Cần tốc độ hội tụ nhanh nhất
- Hàm smooth và well-behaved
- Có computational resources

## Tài liệu tham khảo chính

1. **Polyak, B. T.** (1964). Some methods of speeding up the convergence of iteration methods. USSR Computational Mathematics and Mathematical Physics.

2. **Nesterov, Y.** (1983). A method of solving a convex programming problem with convergence rate O(1/k²). Soviet Mathematics Doklady.

3. **Sutskever, I., et al.** (2013). On the importance of initialization and momentum in deep learning. ICML.

4. **Ruder, S.** (2016). An overview of gradient descent optimization algorithms. arXiv:1609.04747.

---

## Tiếp theo

Hãy khám phá chi tiết từng thuật toán:

1. **[Momentum →]({{ site.baseurl }}/contents/en/chapter06/06_06_01_momentum)**: Tìm hiểu cách "quán tính" cải thiện gradient descent

2. **[Nesterov Accelerated Gradient →]({{ site.baseurl }}/contents/en/chapter06/06_06_02_nesterov_accelerated_gradient)**: Khám phá thuật toán "look-ahead" với tốc độ hội tụ optimal

<script>
class OverviewComparison {
    constructor() {
        this.canvas = document.getElementById('overview-canvas');
        this.ctx = this.canvas.getContext('2d');
        
        // Controls
        this.functionSelect = document.getElementById('overview-function');
        this.overviewInfo = document.getElementById('overview-info');
        
        // State
        this.isAnimating = false;
        this.iteration = 0;
        
        // Initialize
        this.reset();
        this.setupEventListeners();
    }
    
    setupEventListeners() {
        this.functionSelect.addEventListener('change', () => {
            this.reset();
        });
        
        document.getElementById('start-overview').addEventListener('click', () => {
            this.startAnimation();
        });
        
        document.getElementById('reset-overview').addEventListener('click', () => {
            this.reset();
        });
        
        document.getElementById('step-overview').addEventListener('click', () => {
            this.singleStep();
        });
    }
    
    // Different objective functions
    getFunctionAndGradient() {
        const funcType = this.functionSelect.value;
        
        switch(funcType) {
            case 'quadratic':
                return {
                    f: (x, y) => 0.5 * (10 * x * x + y * y),
                    grad: (x, y) => [10 * x, y],
                    name: 'Quadratic'
                };
            case 'rosenbrock':
                return {
                    f: (x, y) => (1 - x) * (1 - x) + 100 * (y - x * x) * (y - x * x),
                    grad: (x, y) => [
                        -2 * (1 - x) - 400 * x * (y - x * x),
                        200 * (y - x * x)
                    ],
                    name: 'Rosenbrock'
                };
            case 'beale':
                return {
                    f: (x, y) => {
                        const t1 = 1.5 - x + x * y;
                        const t2 = 2.25 - x + x * y * y;
                        const t3 = 2.625 - x + x * y * y * y;
                        return t1 * t1 + t2 * t2 + t3 * t3;
                    },
                    grad: (x, y) => {
                        const t1 = 1.5 - x + x * y;
                        const t2 = 2.25 - x + x * y * y;
                        const t3 = 2.625 - x + x * y * y * y;
                        
                        const dx = 2 * t1 * (-1 + y) + 2 * t2 * (-1 + y * y) + 2 * t3 * (-1 + y * y * y);
                        const dy = 2 * t1 * x + 2 * t2 * x * 2 * y + 2 * t3 * x * 3 * y * y;
                        
                        return [dx, dy];
                    },
                    name: 'Beale'
                };
            default:
                return this.getFunctionAndGradient.call(this, 'quadratic');
        }
    }
    
    // Coordinate transformations
    toCanvas(x, y) {
        const centerX = this.canvas.width / 2;
        const centerY = this.canvas.height / 2;
        const scale = this.functionSelect.value === 'quadratic' ? 50 : 100;
        return [centerX + x * scale, centerY - y * scale];
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
        
        // Starting positions based on function type
        const startPos = this.functionSelect.value === 'quadratic' ? [2, 2] : [-1, 1];
        
        // Standard GD
        this.gdPos = [...startPos];
        this.gdPath = [startPos];
        
        // Momentum
        this.momentumPos = [...startPos];
        this.momentumVel = [0, 0];
        this.momentumPath = [startPos];
        
        // NAG
        this.nagPos = [...startPos];
        this.nagVel = [0, 0];
        this.nagPath = [startPos];
        
        this.draw();
    }
    
    singleStep() {
        const {f, grad} = this.getFunctionAndGradient();
        const lr = 0.001; // Small learning rate for stability
        const beta = 0.9;
        
        // Standard Gradient Descent
        const gdGrad = grad(this.gdPos[0], this.gdPos[1]);
        this.gdPos[0] -= lr * gdGrad[0];
        this.gdPos[1] -= lr * gdGrad[1];
        this.gdPath.push([...this.gdPos]);
        
        // Momentum
        const momentumGrad = grad(this.momentumPos[0], this.momentumPos[1]);
        this.momentumVel[0] = beta * this.momentumVel[0] + (1 - beta) * momentumGrad[0];
        this.momentumVel[1] = beta * this.momentumVel[1] + (1 - beta) * momentumGrad[1];
        this.momentumPos[0] -= lr * this.momentumVel[0];
        this.momentumPos[1] -= lr * this.momentumVel[1];
        this.momentumPath.push([...this.momentumPos]);
        
        // NAG
        const lookAheadX = this.nagPos[0] - lr * beta * this.nagVel[0];
        const lookAheadY = this.nagPos[1] - lr * beta * this.nagVel[1];
        const nagGrad = grad(lookAheadX, lookAheadY);
        this.nagVel[0] = beta * this.nagVel[0] + (1 - beta) * nagGrad[0];
        this.nagVel[1] = beta * this.nagVel[1] + (1 - beta) * nagGrad[1];
        this.nagPos[0] -= lr * this.nagVel[0];
        this.nagPos[1] -= lr * this.nagVel[1];
        this.nagPath.push([...this.nagPos]);
        
        this.iteration++;
        this.draw();
    }
    
    draw() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        
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
        
        // Draw paths
        this.drawPath(this.gdPath, '#FF5722', 2);
        this.drawPath(this.momentumPath, '#FF9800', 2);
        this.drawPath(this.nagPath, '#4CAF50', 2);
        
        // Legend
        this.ctx.fillStyle = '#FF5722';
        this.ctx.fillRect(10, 10, 15, 10);
        this.ctx.fillStyle = '#000';
        this.ctx.font = '12px Arial';
        this.ctx.fillText('Standard GD', 30, 20);
        
        this.ctx.fillStyle = '#FF9800';
        this.ctx.fillRect(10, 30, 15, 10);
        this.ctx.fillStyle = '#000';
        this.ctx.fillText('Momentum', 30, 40);
        
        this.ctx.fillStyle = '#4CAF50';
        this.ctx.fillRect(10, 50, 15, 10);
        this.ctx.fillStyle = '#000';
        this.ctx.fillText('NAG', 30, 60);
        
        // Update info
        const {f} = this.getFunctionAndGradient();
        const gdLoss = f(this.gdPos[0], this.gdPos[1]);
        const momentumLoss = f(this.momentumPos[0], this.momentumPos[1]);
        const nagLoss = f(this.nagPos[0], this.nagPos[1]);
        
        this.overviewInfo.innerHTML = 
            `<div style="color: #FF5722;">● Standard GD - Iteration: ${this.iteration}, Loss: ${gdLoss.toFixed(3)}</div>` +
            `<div style="color: #FF9800;">● Momentum - Iteration: ${this.iteration}, Loss: ${momentumLoss.toFixed(3)}</div>` +
            `<div style="color: #4CAF50;">● NAG - Iteration: ${this.iteration}, Loss: ${nagLoss.toFixed(3)}</div>`;
    }
    
    startAnimation() {
        if (this.isAnimating) {
            this.isAnimating = false;
            document.getElementById('start-overview').textContent = 'Start All Methods';
            return;
        }
        
        this.isAnimating = true;
        document.getElementById('start-overview').textContent = 'Stop Animation';
        
        const animate = () => {
            if (!this.isAnimating) return;
            
            if (this.iteration < 500) {
                this.singleStep();
                setTimeout(animate, 50);
            } else {
                this.isAnimating = false;
                document.getElementById('start-overview').textContent = 'Start All Methods';
            }
        };
        
        animate();
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    if (document.getElementById('overview-canvas')) {
        new OverviewComparison();
    }
});
</script>
> $$x^{(k)} = x^{(k-1)} - \alpha v^{(k)}$$

Trong đó:
- $$\beta \in [0,1)$$ là **hệ số momentum** (thường $$\beta = 0.9$$)
- $$\alpha > 0$$ là **learning rate**
- $$v^{(0)} = 0$$ (khởi tạo vận tốc bằng 0)

### Phân tích toán học

Momentum có thể được viết dưới dạng tổng trọng số của các gradient trước đó:

> $$v^{(k)} = (1-\beta) \sum_{i=0}^{k-1} \beta^i \nabla f(x^{(k-1-i)})$$

Điều này cho thấy:
- Gradient gần đây có trọng số cao hơn
- Các gradient cũ vẫn có ảnh hưởng nhưng giảm dần theo hàm mũ
- Khi $$\beta \to 1$$, thuật toán "nhớ" lâu hơn các gradient trước đó

### Ưu điểm của Momentum

1. **Tăng tốc hội tụ**: Trong các hướng có gradient nhất quán, momentum tích lũy vận tốc
2. **Giảm dao động**: Trong các hướng có gradient dao động, momentum làm mượt chuyển động
3. **Vượt qua local minima**: Quán tính giúp vượt qua các điểm cực tiểu địa phương nông

### Ví dụ minh họa

Xét hàm $$f(x,y) = \frac{1}{2}(10x^2 + y^2)$$ - một ellipse với tỷ lệ khung hình 10:1.

**Gradient descent thông thường**:
- Dao động mạnh theo hướng x (gradient lớn)
- Tiến chậm theo hướng y (gradient nhỏ)
- Tạo ra quỹ đạo "zigzag"

**Momentum**:
- Tích lũy vận tốc theo hướng y (hướng đúng)
- Làm mượt dao động theo hướng x
- Quỹ đạo mượt mà hơn và hội tụ nhanh hơn

### Interactive Visualization: Momentum vs Standard Gradient Descent

<div id="momentum-comparison" style="margin: 20px 0;">
    <div style="margin-bottom: 15px;">
        <label for="momentum-beta">Momentum β: <span id="momentum-beta-value">0.9</span></label><br>
        <input type="range" id="momentum-beta" min="0" max="0.99" step="0.01" value="0.9" style="width: 300px;">
    </div>
    
    <div style="margin-bottom: 15px;">
        <label for="learning-rate">Learning Rate α: <span id="learning-rate-value">0.01</span></label><br>
        <input type="range" id="learning-rate" min="0.001" max="0.1" step="0.001" value="0.01" style="width: 300px;">
    </div>
    
    <div style="margin-bottom: 15px;">
        <button id="start-comparison">Start Comparison</button>
        <button id="reset-comparison">Reset</button>
        <button id="step-comparison">Single Step</button>
    </div>
    
    <canvas id="momentum-canvas" width="600" height="400" style="border: 1px solid #ccc; display: block; margin: 0 auto;"></canvas>
    
    <div id="comparison-info" style="text-align: center; margin-top: 10px; font-family: monospace;">
        <div>Standard GD - Iteration: 0, Loss: 12.500</div>
        <div>Momentum - Iteration: 0, Loss: 12.500</div>
    </div>
</div>

## 6.6.2 Nesterov Accelerated Gradient (NAG)

### Ý tưởng "Look-ahead"

Nesterov Accelerated Gradient (NAG) là một cải tiến thông minh của momentum, được Yurii Nesterov đề xuất năm 1983. Ý tưởng chính là **"nhìn trước"** (look-ahead):

Thay vì tính gradient tại vị trí hiện tại, NAG tính gradient tại vị trí mà momentum sẽ đưa chúng ta đến.

### Công thức NAG

> $$v^{(k)} = \beta v^{(k-1)} + (1-\beta) \nabla f(x^{(k-1)} - \alpha \beta v^{(k-1)})$$
> $$x^{(k)} = x^{(k-1)} - \alpha v^{(k)}$$

Hoặc có thể viết dưới dạng tương đương:

> $$v^{(k)} = \beta v^{(k-1)} + (1-\beta) \nabla f(\tilde{x}^{(k-1)})$$
> $$x^{(k)} = x^{(k-1)} - \alpha v^{(k)}$$

Trong đó $$\tilde{x}^{(k-1)} = x^{(k-1)} - \alpha \beta v^{(k-1)}$$ là **vị trí look-ahead**.

### Trực quan hóa NAG

1. **Bước 1**: Từ vị trí hiện tại $$x^{(k-1)}$$, di chuyển theo momentum cũ để có vị trí tạm thời $$\tilde{x}^{(k-1)}$$
2. **Bước 2**: Tính gradient tại vị trí tạm thời này: $$\nabla f(\tilde{x}^{(k-1)})$$
3. **Bước 3**: Cập nhật momentum và vị trí mới

### So sánh Momentum vs NAG

| Thuật toán | Gradient được tính tại | Đặc điểm |
|------------|------------------------|----------|
| **Momentum** | Vị trí hiện tại $$x^{(k-1)}$$ | "Nhìn lại" - sử dụng thông tin quá khứ |
| **NAG** | Vị trí look-ahead $$\tilde{x}^{(k-1)}$$ | "Nhìn trước" - dự đoán hướng di chuyển |

### Ưu điểm của NAG

1. **Hội tụ nhanh hơn**: NAG thường hội tụ nhanh hơn momentum thông thường
2. **Ít overshoot**: Khả năng "nhìn trước" giúp giảm hiện tượng vượt quá điểm tối ưu
3. **Lý thuyết mạnh**: Có đảm bảo lý thuyết về tốc độ hội tụ tốt hơn

### Phân tích lý thuyết

Đối với hàm convex và smooth, NAG có tốc độ hội tụ:
- **Gradient Descent**: $$O(1/k)$$
- **NAG**: $$O(1/k^2)$$

Đây là cải thiện đáng kể về mặt lý thuyết!

### Interactive Comparison: Momentum vs NAG

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

## Tổng kết và So sánh

### Bảng so sánh các thuật toán

| Thuật toán | Công thức cập nhật | Ưu điểm | Nhược điểm |
|------------|-------------------|---------|------------|
| **Standard GD** | $$x^{(k)} = x^{(k-1)} - \alpha \nabla f(x^{(k-1)})$$ | Đơn giản, ổn định | Chậm, dao động |
| **Momentum** | $$v^{(k)} = \beta v^{(k-1)} + (1-\beta) \nabla f(x^{(k-1)})$$ | Nhanh hơn, ít dao động | Có thể overshoot |
| **NAG** | $$v^{(k)} = \beta v^{(k-1)} + (1-\beta) \nabla f(\tilde{x}^{(k-1)})$$ | Nhanh nhất, ít overshoot | Phức tạp hơn |

### Khi nào sử dụng thuật toán nào?

- **Standard Gradient Descent**: Khi cần sự đơn giản và ổn định
- **Momentum**: Khi hàm mục tiêu có nhiều dao động hoặc thung lũng hẹp
- **NAG**: Khi cần tốc độ hội tụ nhanh nhất và có thể chấp nhận độ phức tạp cao hơn

### Hyperparameter tuning

**Momentum coefficient (β)**:
- $$\beta = 0.9$$: Giá trị phổ biến, cân bằng tốt
- $$\beta = 0.99$$: Momentum mạnh hơn, phù hợp với bài toán khó
- $$\beta = 0.5$$: Momentum nhẹ, phù hợp khi gradient ổn định

**Learning rate (α)**:
- Thường nhỏ hơn so với standard GD do momentum tăng tốc
- Cần điều chỉnh cùng với β để tránh divergence

<script>
class AdvancedGradientComparison {
    constructor() {
        this.setupMomentumComparison();
        this.setupNAGComparison();
    }
    
    setupMomentumComparison() {
        this.momentumCanvas = document.getElementById('momentum-canvas');
        this.momentumCtx = this.momentumCanvas.getContext('2d');
        
        // Controls
        this.betaSlider = document.getElementById('momentum-beta');
        this.lrSlider = document.getElementById('learning-rate');
        this.betaValue = document.getElementById('momentum-beta-value');
        this.lrValue = document.getElementById('learning-rate-value');
        this.comparisonInfo = document.getElementById('comparison-info');
        
        // State
        this.isAnimating = false;
        this.iteration = 0;
        
        // Initialize positions
        this.resetMomentumComparison();
        
        // Event listeners
        this.betaSlider.addEventListener('input', (e) => {
            this.betaValue.textContent = e.target.value;
        });
        
        this.lrSlider.addEventListener('input', (e) => {
            this.lrValue.textContent = e.target.value;
        });
        
        document.getElementById('start-comparison').addEventListener('click', () => {
            this.startMomentumAnimation();
        });
        
        document.getElementById('reset-comparison').addEventListener('click', () => {
            this.resetMomentumComparison();
        });
        
        document.getElementById('step-comparison').addEventListener('click', () => {
            this.singleMomentumStep();
        });
    }
    
    setupNAGComparison() {
        this.nagCanvas = document.getElementById('nag-canvas');
        this.nagCtx = this.nagCanvas.getContext('2d');
        
        // Controls
        this.nagBetaSlider = document.getElementById('nag-beta');
        this.nagLrSlider = document.getElementById('nag-lr');
        this.nagBetaValue = document.getElementById('nag-beta-value');
        this.nagLrValue = document.getElementById('nag-lr-value');
        this.nagInfo = document.getElementById('nag-info');
        
        // State
        this.nagAnimating = false;
        this.nagIteration = 0;
        
        // Initialize positions
        this.resetNAGComparison();
        
        // Event listeners
        this.nagBetaSlider.addEventListener('input', (e) => {
            this.nagBetaValue.textContent = e.target.value;
        });
        
        this.nagLrSlider.addEventListener('input', (e) => {
            this.nagLrValue.textContent = e.target.value;
        });
        
        document.getElementById('start-nag-comparison').addEventListener('click', () => {
            this.startNAGAnimation();
        });
        
        document.getElementById('reset-nag-comparison').addEventListener('click', () => {
            this.resetNAGComparison();
        });
        
        document.getElementById('step-nag-comparison').addEventListener('click', () => {
            this.singleNAGStep();
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
    toCanvas(x, y, canvas) {
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const scale = 50;
        return [centerX + x * scale, centerY - y * scale];
    }
    
    fromCanvas(canvasX, canvasY, canvas) {
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const scale = 50;
        return [(canvasX - centerX) / scale, (centerY - canvasY) / scale];
    }
    
    drawContours(ctx, canvas) {
        ctx.strokeStyle = '#E0E0E0';
        ctx.lineWidth = 1;
        
        // Draw elliptical contours
        const levels = [0.5, 2, 8, 18, 32, 50];
        
        for (let level of levels) {
            ctx.beginPath();
            for (let angle = 0; angle <= 2 * Math.PI; angle += 0.1) {
                // For f(x,y) = 0.5*(10*x^2 + y^2) = level
                // Ellipse: x^2/(2*level/10) + y^2/(2*level) = 1
                const a = Math.sqrt(2 * level / 10); // x semi-axis
                const b = Math.sqrt(2 * level);      // y semi-axis
                
                const x = a * Math.cos(angle);
                const y = b * Math.sin(angle);
                const [canvasX, canvasY] = this.toCanvas(x, y, canvas);
                
                if (angle === 0) {
                    ctx.moveTo(canvasX, canvasY);
                } else {
                    ctx.lineTo(canvasX, canvasY);
                }
            }
            ctx.stroke();
        }
        
        // Draw axes
        ctx.strokeStyle = '#CCCCCC';
        ctx.lineWidth = 1;
        
        // X-axis
        ctx.beginPath();
        ctx.moveTo(0, canvas.height / 2);
        ctx.lineTo(canvas.width, canvas.height / 2);
        ctx.stroke();
        
        // Y-axis
        ctx.beginPath();
        ctx.moveTo(canvas.width / 2, 0);
        ctx.lineTo(canvas.width / 2, canvas.height);
        ctx.stroke();
    }
    
    drawPath(ctx, canvas, path, color, lineWidth = 2) {
        if (path.length < 2) return;
        
        ctx.strokeStyle = color;
        ctx.lineWidth = lineWidth;
        ctx.beginPath();
        
        for (let i = 0; i < path.length; i++) {
            const [canvasX, canvasY] = this.toCanvas(path[i][0], path[i][1], canvas);
            if (i === 0) {
                ctx.moveTo(canvasX, canvasY);
            } else {
                ctx.lineTo(canvasX, canvasY);
            }
        }
        ctx.stroke();
        
        // Draw current position
        if (path.length > 0) {
            const [lastX, lastY] = path[path.length - 1];
            const [canvasX, canvasY] = this.toCanvas(lastX, lastY, canvas);
            ctx.fillStyle = color;
            ctx.beginPath();
            ctx.arc(canvasX, canvasY, 5, 0, 2 * Math.PI);
            ctx.fill();
        }
    }
    
    resetMomentumComparison() {
        this.isAnimating = false;
        this.iteration = 0;
        
        // Starting position
        this.gdPos = [2, 2];
        this.momentumPos = [2, 2];
        this.momentumVel = [0, 0];
        
        this.gdPath = [[2, 2]];
        this.momentumPath = [[2, 2]];
        
        this.drawMomentumComparison();
    }
    
    resetNAGComparison() {
        this.nagAnimating = false;
        this.nagIteration = 0;
        
        // Starting position
        this.momentumPos2 = [2, 2];
        this.nagPos = [2, 2];
        this.momentumVel2 = [0, 0];
        this.nagVel = [0, 0];
        
        this.momentumPath2 = [[2, 2]];
        this.nagPath = [[2, 2]];
        
        this.drawNAGComparison();
    }
    
    singleMomentumStep() {
        const lr = parseFloat(this.lrSlider.value);
        const beta = parseFloat(this.betaSlider.value);
        
        // Standard Gradient Descent
        const gdGrad = this.gradient(this.gdPos[0], this.gdPos[1]);
        this.gdPos[0] -= lr * gdGrad[0];
        this.gdPos[1] -= lr * gdGrad[1];
        this.gdPath.push([this.gdPos[0], this.gdPos[1]]);
        
        // Momentum
        const momentumGrad = this.gradient(this.momentumPos[0], this.momentumPos[1]);
        this.momentumVel[0] = beta * this.momentumVel[0] + (1 - beta) * momentumGrad[0];
        this.momentumVel[1] = beta * this.momentumVel[1] + (1 - beta) * momentumGrad[1];
        this.momentumPos[0] -= lr * this.momentumVel[0];
        this.momentumPos[1] -= lr * this.momentumVel[1];
        this.momentumPath.push([this.momentumPos[0], this.momentumPos[1]]);
        
        this.iteration++;
        this.drawMomentumComparison();
    }
    
    singleNAGStep() {
        const lr = parseFloat(this.nagLrSlider.value);
        const beta = parseFloat(this.nagBetaSlider.value);
        
        // Momentum
        const momentumGrad = this.gradient(this.momentumPos2[0], this.momentumPos2[1]);
        this.momentumVel2[0] = beta * this.momentumVel2[0] + (1 - beta) * momentumGrad[0];
        this.momentumVel2[1] = beta * this.momentumVel2[1] + (1 - beta) * momentumGrad[1];
        this.momentumPos2[0] -= lr * this.momentumVel2[0];
        this.momentumPos2[1] -= lr * this.momentumVel2[1];
        this.momentumPath2.push([this.momentumPos2[0], this.momentumPos2[1]]);
        
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
        
        this.nagIteration++;
        this.drawNAGComparison();
    }
    
    drawMomentumComparison() {
        this.momentumCtx.clearRect(0, 0, this.momentumCanvas.width, this.momentumCanvas.height);
        
        this.drawContours(this.momentumCtx, this.momentumCanvas);
        this.drawPath(this.momentumCtx, this.momentumCanvas, this.gdPath, '#FF5722', 2);
        this.drawPath(this.momentumCtx, this.momentumCanvas, this.momentumPath, '#2196F3', 2);
        
        // Legend
        this.momentumCtx.fillStyle = '#FF5722';
        this.momentumCtx.fillRect(10, 10, 20, 10);
        this.momentumCtx.fillStyle = '#000';
        this.momentumCtx.font = '12px Arial';
        this.momentumCtx.fillText('Standard GD', 35, 20);
        
        this.momentumCtx.fillStyle = '#2196F3';
        this.momentumCtx.fillRect(10, 30, 20, 10);
        this.momentumCtx.fillStyle = '#000';
        this.momentumCtx.fillText('Momentum', 35, 40);
        
        // Update info
        const gdLoss = this.objectiveFunction(this.gdPos[0], this.gdPos[1]);
        const momentumLoss = this.objectiveFunction(this.momentumPos[0], this.momentumPos[1]);
        
        this.comparisonInfo.innerHTML = 
            `<div>Standard GD - Iteration: ${this.iteration}, Loss: ${gdLoss.toFixed(3)}</div>` +
            `<div>Momentum - Iteration: ${this.iteration}, Loss: ${momentumLoss.toFixed(3)}</div>`;
    }
    
    drawNAGComparison() {
        this.nagCtx.clearRect(0, 0, this.nagCanvas.width, this.nagCanvas.height);
        
        this.drawContours(this.nagCtx, this.nagCanvas);
        this.drawPath(this.nagCtx, this.nagCanvas, this.momentumPath2, '#FF9800', 2);
        this.drawPath(this.nagCtx, this.nagCanvas, this.nagPath, '#4CAF50', 2);
        
        // Legend
        this.nagCtx.fillStyle = '#FF9800';
        this.nagCtx.fillRect(10, 10, 20, 10);
        this.nagCtx.fillStyle = '#000';
        this.nagCtx.font = '12px Arial';
        this.nagCtx.fillText('Momentum', 35, 20);
        
        this.nagCtx.fillStyle = '#4CAF50';
        this.nagCtx.fillRect(10, 30, 20, 10);
        this.nagCtx.fillStyle = '#000';
        this.nagCtx.fillText('NAG', 35, 40);
        
        // Update info
        const momentumLoss = this.objectiveFunction(this.momentumPos2[0], this.momentumPos2[1]);
        const nagLoss = this.objectiveFunction(this.nagPos[0], this.nagPos[1]);
        
        this.nagInfo.innerHTML = 
            `<div>Momentum - Iteration: ${this.nagIteration}, Loss: ${momentumLoss.toFixed(3)}</div>` +
            `<div>NAG - Iteration: ${this.nagIteration}, Loss: ${nagLoss.toFixed(3)}</div>`;
    }
    
    startMomentumAnimation() {
        if (this.isAnimating) {
            this.isAnimating = false;
            document.getElementById('start-comparison').textContent = 'Start Comparison';
            return;
        }
        
        this.isAnimating = true;
        document.getElementById('start-comparison').textContent = 'Stop Comparison';
        
        const animate = () => {
            if (!this.isAnimating) return;
            
            const currentLoss = Math.min(
                this.objectiveFunction(this.gdPos[0], this.gdPos[1]),
                this.objectiveFunction(this.momentumPos[0], this.momentumPos[1])
            );
            
            if (currentLoss > 1e-4 && this.iteration < 200) {
                this.singleMomentumStep();
                setTimeout(animate, 100);
            } else {
                this.isAnimating = false;
                document.getElementById('start-comparison').textContent = 'Start Comparison';
            }
        };
        
        animate();
    }
    
    startNAGAnimation() {
        if (this.nagAnimating) {
            this.nagAnimating = false;
            document.getElementById('start-nag-comparison').textContent = 'Start Comparison';
            return;
        }
        
        this.nagAnimating = true;
        document.getElementById('start-nag-comparison').textContent = 'Stop Comparison';
        
        const animate = () => {
            if (!this.nagAnimating) return;
            
            const currentLoss = Math.min(
                this.objectiveFunction(this.momentumPos2[0], this.momentumPos2[1]),
                this.objectiveFunction(this.nagPos[0], this.nagPos[1])
            );
            
            if (currentLoss > 1e-4 && this.nagIteration < 200) {
                this.singleNAGStep();
                setTimeout(animate, 100);
            } else {
                this.nagAnimating = false;
                document.getElementById('start-nag-comparison').textContent = 'Start Comparison';
            }
        };
        
        animate();
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    new AdvancedGradientComparison();
});
</script>

## Tài liệu tham khảo

1. Nesterov, Y. (1983). A method of solving a convex programming problem with convergence rate O(1/k²). Soviet Mathematics Doklady, 27(2), 372-376.

2. Polyak, B. T. (1964). Some methods of speeding up the convergence of iteration methods. USSR Computational Mathematics and Mathematical Physics, 4(5), 1-17.

3. Sutskever, I., Martens, J., Dahl, G., & Hinton, G. (2013). On the importance of initialization and momentum in deep learning. International Conference on Machine Learning, 1139-1147.
