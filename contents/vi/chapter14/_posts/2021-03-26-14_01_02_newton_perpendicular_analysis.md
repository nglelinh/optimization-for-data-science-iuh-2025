---
layout: post
title: 14-01-02 Phương Pháp Newton Có Di Chuyển Vuông Góc Với Đường Đồng Mức Hay Không?
chapter: '14'
order: 4
owner: AI Assistant
categories:
- chapter14
lang: vi
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center",
    tex2jax: {
        inlineMath: [['$', '$'], ['\\(', '\\)']],
        displayMath: [['$$', '$$'], ['\\[', '\\]']]
    }
});
</script>

<style>
.interactive-container {
    background: #f8f9fa;
    border: 1px solid #dee2e6;
    border-radius: 8px;
    padding: 20px;
    margin: 20px 0;
}

.controls {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
    margin-bottom: 20px;
    align-items: center;
}

.control-group {
    display: flex;
    flex-direction: column;
    gap: 5px;
}

.control-group label {
    font-weight: bold;
    font-size: 0.9em;
    color: #495057;
}

.control-group input[type="range"] {
    width: 150px;
}

.control-group input[type="number"] {
    width: 80px;
    padding: 4px;
    border: 1px solid #ced4da;
    border-radius: 4px;
}

button {
    background: #007bff;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 0.9em;
}

button:hover {
    background: #0056b3;
}

button:disabled {
    background: #6c757d;
    cursor: not-allowed;
}

#canvas {
    border: 1px solid #dee2e6;
    border-radius: 4px;
    display: block;
    margin: 0 auto;
}

.info-panel {
    background: #e9ecef;
    padding: 15px;
    border-radius: 4px;
    margin-top: 15px;
    font-family: monospace;
    font-size: 0.85em;
}

.legend {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-top: 10px;
    font-size: 0.9em;
}

.legend-item {
    display: flex;
    align-items: center;
    gap: 5px;
}

.legend-color {
    width: 20px;
    height: 3px;
    border-radius: 2px;
}

.comparison-table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
}

.comparison-table th,
.comparison-table td {
    border: 1px solid #dee2e6;
    padding: 12px;
    text-align: left;
}

.comparison-table th {
    background: #f8f9fa;
    font-weight: bold;
}

.math-explanation {
    background: #fff3cd;
    border: 1px solid #ffeaa7;
    border-radius: 4px;
    padding: 15px;
    margin: 15px 0;
}

.key-insight {
    background: #d1ecf1;
    border: 1px solid #bee5eb;
    border-radius: 4px;
    padding: 15px;
    margin: 15px 0;
}
</style>

Trong bài học này, chúng ta sẽ khám phá một câu hỏi quan trọng trong tối ưu hóa: **Phương pháp Newton có di chuyển vuông góc với đường đồng mức hay không?** Đây là một câu hỏi giúp chúng ta hiểu sâu hơn về sự khác biệt giữa Newton's method và gradient descent.

## 1. Trực Giác Cơ Bản

<div class="key-insight">
<strong>Câu trả lời ngắn gọn:</strong> <strong>KHÔNG</strong>, phương pháp Newton thường KHÔNG di chuyển vuông góc với đường đồng mức, khác với gradient descent.
</div>

### So sánh với Gradient Descent

- **Gradient Descent**: Luôn di chuyển theo hướng $$-\nabla f$$, vuông góc với đường đồng mức
- **Newton's Method**: Sử dụng thông tin bậc hai (Hessian) để "điều chỉnh" hướng di chuyển, không còn vuông góc trong không gian gốc

## 2. Giải Thích Toán Học

### Gradient Descent
Hướng di chuyển trong gradient descent:
$$\mathbf{d}_{GD} = -\nabla f(\mathbf{x})$$

Hướng này luôn vuông góc với đường đồng mức vì gradient là vector pháp tuyến của level curves.

### Newton's Method
Hướng di chuyển trong Newton's method:
$$\mathbf{d}_{Newton} = -[\nabla^2 f(\mathbf{x})]^{-1} \nabla f(\mathbf{x})$$

<div class="math-explanation">
<strong>Giải thích:</strong> Hessian $$\nabla^2 f$$ "biến đổi" không gian, làm cho hướng di chuyển không còn vuông góc với đường đồng mức trong tọa độ gốc. Newton tối ưu hóa theo "hướng dốc nhất" trong không gian được biến đổi bởi Hessian.
</div>

### Khi nào Newton vuông góc?
Chỉ khi Hessian là bội số của ma trận đơn vị: $$\nabla^2 f = cI$$ (với $$c$$ là hằng số), Newton trùng với GD và di chuyển vuông góc.

## 3. Minh Họa Tương Tác

<div class="interactive-container">
    <h4>So sánh Quỹ Đạo Newton vs Gradient Descent</h4>
    
    <div class="controls">
        <div class="control-group">
            <label for="a-param">Tham số a (độ cong theo x):</label>
            <input type="range" id="a-param" min="1" max="20" value="10" step="1">
            <input type="number" id="a-value" min="1" max="20" value="10" step="1">
        </div>
        
        <div class="control-group">
            <label for="b-param">Tham số b (độ cong theo y):</label>
            <input type="range" id="b-param" min="1" max="20" value="1" step="1">
            <input type="number" id="b-value" min="1" max="20" value="1" step="1">
        </div>
        
        <div class="control-group">
            <label for="start-x">Điểm bắt đầu x:</label>
            <input type="number" id="start-x" min="-3" max="3" value="2" step="0.1">
        </div>
        
        <div class="control-group">
            <label for="start-y">Điểm bắt đầu y:</label>
            <input type="number" id="start-y" min="-3" max="3" value="1.5" step="0.1">
        </div>
        
        <div class="control-group">
            <label for="learning-rate">Learning Rate (GD):</label>
            <input type="range" id="learning-rate" min="0.01" max="0.5" value="0.1" step="0.01">
            <input type="number" id="lr-value" min="0.01" max="0.5" value="0.1" step="0.01">
        </div>
        
        <button id="start-btn">Bắt đầu</button>
        <button id="step-btn">Từng bước</button>
        <button id="reset-btn">Đặt lại</button>
        <button id="toggle-contour">Ẩn/Hiện đường đồng mức</button>
    </div>
    
    <canvas id="canvas" width="600" height="500"></canvas>
    
    <div class="legend">
        <div class="legend-item">
            <div class="legend-color" style="background: #ff4444;"></div>
            <span>Gradient Descent (vuông góc với đường đồng mức)</span>
        </div>
        <div class="legend-item">
            <div class="legend-color" style="background: #4444ff;"></div>
            <span>Newton's Method (cắt qua đường đồng mức)</span>
        </div>
        <div class="legend-item">
            <div class="legend-color" style="background: #888888;"></div>
            <span>Đường đồng mức</span>
        </div>
    </div>
    
    <div id="info-panel" class="info-panel">
        Hàm mục tiêu: f(x,y) = (ax² + by²)/2<br>
        Nhấn "Bắt đầu" để xem so sánh quỹ đạo của hai phương pháp
    </div>
</div>

## 4. Phân Tích Chi Tiết

<table class="comparison-table">
    <thead>
        <tr>
            <th>Đặc điểm</th>
            <th>Gradient Descent</th>
            <th>Newton's Method</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>Hướng di chuyển</strong></td>
            <td>$$-\nabla f$$ (vuông góc với đường đồng mức)</td>
            <td>$$-H^{-1}\nabla f$$ (không vuông góc)</td>
        </tr>
        <tr>
            <td><strong>Thông tin sử dụng</strong></td>
            <td>Chỉ gradient (bậc 1)</td>
            <td>Gradient + Hessian (bậc 2)</td>
        </tr>
        <tr>
            <td><strong>Tốc độ hội tụ</strong></td>
            <td>Tuyến tính</td>
            <td>Bậc hai (gần optimum)</td>
        </tr>
        <tr>
            <td><strong>Xử lý ill-conditioning</strong></td>
            <td>Kém (zig-zag)</td>
            <td>Tốt (đi thẳng)</td>
        </tr>
        <tr>
            <td><strong>Chi phí tính toán</strong></td>
            <td>O(n) mỗi bước</td>
            <td>O(n³) mỗi bước</td>
        </tr>
    </tbody>
</table>

## 5. Ví Dụ Cụ Thể

Xét hàm $$f(x,y) = x^2 + 10y^2$$ với đường đồng mức là các ellipse dẹt.

**Tại điểm (1,1):**
- **Gradient**: $$\nabla f = (2, 20)$$ - vuông góc với ellipse
- **Hessian**: $$H = \begin{pmatrix} 2 & 0 \\ 0 & 20 \end{pmatrix}$$
- **Newton direction**: $$\mathbf{d} = -H^{-1}\nabla f = -\begin{pmatrix} 1/2 & 0 \\ 0 & 1/20 \end{pmatrix} \begin{pmatrix} 2 \\ 20 \end{pmatrix} = (-1, -1)$$

<div class="key-insight">
<strong>Quan sát:</strong> Gradient descent đi theo hướng (-2, -20) (vuông góc), trong khi Newton đi theo (-1, -1) (cắt chéo qua ellipse).
</div>

## 6. Tại Sao Điều Này Quan Trọng?

### Ưu điểm của Newton
1. **Xử lý ill-conditioning tốt**: Khi hàm có độ cong khác nhau theo các hướng khác nhau
2. **Hội tụ nhanh hơn**: Đặc biệt gần điểm tối ưu
3. **Bất biến affine**: Không phụ thuộc vào hệ tọa độ

### Nhược điểm
1. **Chi phí tính toán cao**: Cần tính và nghịch đảo Hessian
2. **Có thể không ổn định**: Nếu Hessian không positive definite
3. **Không phù hợp với dữ liệu lớn**: Do độ phức tạp O(n³)

## 7. Ứng Dụng Trong Machine Learning

Trong thực tế, các biến thể của Newton được sử dụng:
- **L-BFGS**: Xấp xỉ Hessian, tránh tính toán đầy đủ
- **Gauss-Newton**: Cho bài toán least squares
- **Levenberg-Marquardt**: Kết hợp ưu điểm của GD và Newton

<div class="math-explanation">
<strong>Kết luận:</strong> Newton's method không di chuyển vuông góc với đường đồng mức vì nó tối ưu hóa trong không gian được "biến đổi" bởi Hessian. Điều này cho phép nó hội tụ nhanh hơn nhưng với chi phí tính toán cao hơn.
</div>

<script>
class OptimizationVisualizer {
    constructor() {
        this.canvas = document.getElementById('canvas');
        this.ctx = this.canvas.getContext('2d');
        this.width = this.canvas.width;
        this.height = this.canvas.height;
        
        // Parameters
        this.a = 10;
        this.b = 1;
        this.startX = 2;
        this.startY = 1.5;
        this.learningRate = 0.1;
        
        // Visualization settings
        this.scale = 80;
        this.centerX = this.width / 2;
        this.centerY = this.height / 2;
        this.showContour = true;
        
        // Animation state
        this.isRunning = false;
        this.gdPath = [];
        this.newtonPath = [];
        this.currentStep = 0;
        this.maxSteps = 20;
        
        this.setupEventListeners();
        this.reset();
    }
    
    setupEventListeners() {
        // Parameter controls
        const aParam = document.getElementById('a-param');
        const aValue = document.getElementById('a-value');
        const bParam = document.getElementById('b-param');
        const bValue = document.getElementById('b-value');
        const lrParam = document.getElementById('learning-rate');
        const lrValue = document.getElementById('lr-value');
        
        // Sync sliders with number inputs
        aParam.addEventListener('input', (e) => {
            this.a = parseFloat(e.target.value);
            aValue.value = this.a;
            this.reset();
        });
        
        aValue.addEventListener('input', (e) => {
            this.a = parseFloat(e.target.value);
            aParam.value = this.a;
            this.reset();
        });
        
        bParam.addEventListener('input', (e) => {
            this.b = parseFloat(e.target.value);
            bValue.value = this.b;
            this.reset();
        });
        
        bValue.addEventListener('input', (e) => {
            this.b = parseFloat(e.target.value);
            bParam.value = this.b;
            this.reset();
        });
        
        lrParam.addEventListener('input', (e) => {
            this.learningRate = parseFloat(e.target.value);
            lrValue.value = this.learningRate;
        });
        
        lrValue.addEventListener('input', (e) => {
            this.learningRate = parseFloat(e.target.value);
            lrParam.value = this.learningRate;
        });
        
        // Start position controls
        document.getElementById('start-x').addEventListener('input', (e) => {
            this.startX = parseFloat(e.target.value);
            this.reset();
        });
        
        document.getElementById('start-y').addEventListener('input', (e) => {
            this.startY = parseFloat(e.target.value);
            this.reset();
        });
        
        // Buttons
        document.getElementById('start-btn').addEventListener('click', () => this.startAnimation());
        document.getElementById('step-btn').addEventListener('click', () => this.stepAnimation());
        document.getElementById('reset-btn').addEventListener('click', () => this.reset());
        document.getElementById('toggle-contour').addEventListener('click', () => this.toggleContour());
    }
    
    // Objective function: f(x,y) = (ax² + by²)/2
    f(x, y) {
        return (this.a * x * x + this.b * y * y) / 2;
    }
    
    // Gradient: ∇f = (ax, by)
    gradient(x, y) {
        return [this.a * x, this.b * y];
    }
    
    // Hessian: H = [[a, 0], [0, b]]
    hessian(x, y) {
        return [[this.a, 0], [0, this.b]];
    }
    
    // Matrix inverse for 2x2
    inverse2x2(matrix) {
        const [[a, b], [c, d]] = matrix;
        const det = a * d - b * c;
        if (Math.abs(det) < 1e-10) return null;
        return [[d/det, -b/det], [-c/det, a/det]];
    }
    
    // Matrix-vector multiplication
    matVecMul(matrix, vector) {
        const [x, y] = vector;
        return [
            matrix[0][0] * x + matrix[0][1] * y,
            matrix[1][0] * x + matrix[1][1] * y
        ];
    }
    
    // Gradient descent step
    gradientDescentStep(x, y) {
        const [gx, gy] = this.gradient(x, y);
        return [
            x - this.learningRate * gx,
            y - this.learningRate * gy
        ];
    }
    
    // Newton method step
    newtonStep(x, y) {
        const [gx, gy] = this.gradient(x, y);
        const H = this.hessian(x, y);
        const Hinv = this.inverse2x2(H);
        
        if (!Hinv) return [x, y]; // Fallback if Hessian is singular
        
        const [dx, dy] = this.matVecMul(Hinv, [gx, gy]);
        return [x - dx, y - dy];
    }
    
    // Convert world coordinates to canvas coordinates
    worldToCanvas(x, y) {
        return [
            this.centerX + x * this.scale,
            this.centerY - y * this.scale
        ];
    }
    
    // Convert canvas coordinates to world coordinates
    canvasToWorld(canvasX, canvasY) {
        return [
            (canvasX - this.centerX) / this.scale,
            -(canvasY - this.centerY) / this.scale
        ];
    }
    
    drawContourLines() {
        if (!this.showContour) return;
        
        this.ctx.strokeStyle = '#888888';
        this.ctx.lineWidth = 1;
        
        const levels = [0.5, 1, 2, 4, 8, 16];
        
        for (const level of levels) {
            this.ctx.beginPath();
            
            // Draw ellipse for level set f(x,y) = level
            // (ax² + by²)/2 = level => ax² + by² = 2*level
            // x²/(2*level/a) + y²/(2*level/b) = 1
            const radiusX = Math.sqrt(2 * level / this.a) * this.scale;
            const radiusY = Math.sqrt(2 * level / this.b) * this.scale;
            
            this.ctx.ellipse(this.centerX, this.centerY, radiusX, radiusY, 0, 0, 2 * Math.PI);
            this.ctx.stroke();
        }
    }
    
    drawPath(path, color, label) {
        if (path.length < 2) return;
        
        this.ctx.strokeStyle = color;
        this.ctx.lineWidth = 3;
        this.ctx.beginPath();
        
        const [startCanvasX, startCanvasY] = this.worldToCanvas(path[0][0], path[0][1]);
        this.ctx.moveTo(startCanvasX, startCanvasY);
        
        for (let i = 1; i < path.length; i++) {
            const [canvasX, canvasY] = this.worldToCanvas(path[i][0], path[i][1]);
            this.ctx.lineTo(canvasX, canvasY);
        }
        this.ctx.stroke();
        
        // Draw points
        this.ctx.fillStyle = color;
        for (let i = 0; i < path.length; i++) {
            const [canvasX, canvasY] = this.worldToCanvas(path[i][0], path[i][1]);
            this.ctx.beginPath();
            this.ctx.arc(canvasX, canvasY, i === 0 ? 6 : 4, 0, 2 * Math.PI);
            this.ctx.fill();
        }
        
        // Draw arrows for direction
        for (let i = 0; i < path.length - 1; i++) {
            const [x1, y1] = this.worldToCanvas(path[i][0], path[i][1]);
            const [x2, y2] = this.worldToCanvas(path[i+1][0], path[i+1][1]);
            this.drawArrow(x1, y1, x2, y2, color);
        }
    }
    
    drawArrow(x1, y1, x2, y2, color) {
        const dx = x2 - x1;
        const dy = y2 - y1;
        const length = Math.sqrt(dx * dx + dy * dy);
        
        if (length < 5) return;
        
        const angle = Math.atan2(dy, dx);
        const arrowLength = 10;
        const arrowAngle = Math.PI / 6;
        
        this.ctx.strokeStyle = color;
        this.ctx.lineWidth = 2;
        this.ctx.beginPath();
        
        // Arrow head
        const headX = x2 - arrowLength * Math.cos(angle - arrowAngle);
        const headY = y2 - arrowLength * Math.sin(angle - arrowAngle);
        this.ctx.moveTo(x2, y2);
        this.ctx.lineTo(headX, headY);
        
        const headX2 = x2 - arrowLength * Math.cos(angle + arrowAngle);
        const headY2 = y2 - arrowLength * Math.sin(angle + arrowAngle);
        this.ctx.moveTo(x2, y2);
        this.ctx.lineTo(headX2, headY2);
        
        this.ctx.stroke();
    }
    
    drawAxes() {
        this.ctx.strokeStyle = '#cccccc';
        this.ctx.lineWidth = 1;
        
        // X axis
        this.ctx.beginPath();
        this.ctx.moveTo(0, this.centerY);
        this.ctx.lineTo(this.width, this.centerY);
        this.ctx.stroke();
        
        // Y axis
        this.ctx.beginPath();
        this.ctx.moveTo(this.centerX, 0);
        this.ctx.lineTo(this.centerX, this.height);
        this.ctx.stroke();
        
        // Origin
        this.ctx.fillStyle = '#666666';
        this.ctx.beginPath();
        this.ctx.arc(this.centerX, this.centerY, 3, 0, 2 * Math.PI);
        this.ctx.fill();
    }
    
    draw() {
        // Clear canvas
        this.ctx.clearRect(0, 0, this.width, this.height);
        
        // Draw axes
        this.drawAxes();
        
        // Draw contour lines
        this.drawContourLines();
        
        // Draw paths
        this.drawPath(this.gdPath, '#ff4444', 'GD');
        this.drawPath(this.newtonPath, '#4444ff', 'Newton');
        
        // Update info panel
        this.updateInfoPanel();
    }
    
    updateInfoPanel() {
        const panel = document.getElementById('info-panel');
        const gdCurrent = this.gdPath.length > 0 ? this.gdPath[this.gdPath.length - 1] : [this.startX, this.startY];
        const newtonCurrent = this.newtonPath.length > 0 ? this.newtonPath[this.newtonPath.length - 1] : [this.startX, this.startY];
        
        const gdValue = this.f(gdCurrent[0], gdCurrent[1]);
        const newtonValue = this.f(newtonCurrent[0], newtonCurrent[1]);
        
        panel.innerHTML = `
            Hàm mục tiêu: f(x,y) = (${this.a}x² + ${this.b}y²)/2<br>
            Bước hiện tại: ${this.currentStep}<br>
            GD - Vị trí: (${gdCurrent[0].toFixed(3)}, ${gdCurrent[1].toFixed(3)}), f = ${gdValue.toFixed(4)}<br>
            Newton - Vị trí: (${newtonCurrent[0].toFixed(3)}, ${newtonCurrent[1].toFixed(3)}), f = ${newtonValue.toFixed(4)}
        `;
    }
    
    reset() {
        this.isRunning = false;
        this.gdPath = [[this.startX, this.startY]];
        this.newtonPath = [[this.startX, this.startY]];
        this.currentStep = 0;
        
        document.getElementById('start-btn').disabled = false;
        document.getElementById('step-btn').disabled = false;
        
        this.draw();
    }
    
    stepAnimation() {
        if (this.currentStep >= this.maxSteps) return;
        
        // Gradient descent step
        const gdCurrent = this.gdPath[this.gdPath.length - 1];
        const gdNext = this.gradientDescentStep(gdCurrent[0], gdCurrent[1]);
        this.gdPath.push(gdNext);
        
        // Newton step
        const newtonCurrent = this.newtonPath[this.newtonPath.length - 1];
        const newtonNext = this.newtonStep(newtonCurrent[0], newtonCurrent[1]);
        this.newtonPath.push(newtonNext);
        
        this.currentStep++;
        this.draw();
        
        // Check convergence
        const gdConverged = Math.abs(gdNext[0]) < 0.01 && Math.abs(gdNext[1]) < 0.01;
        const newtonConverged = Math.abs(newtonNext[0]) < 0.01 && Math.abs(newtonNext[1]) < 0.01;
        
        if (gdConverged && newtonConverged || this.currentStep >= this.maxSteps) {
            this.isRunning = false;
            document.getElementById('start-btn').disabled = false;
            document.getElementById('step-btn').disabled = true;
        }
    }
    
    startAnimation() {
        if (this.isRunning) return;
        
        this.isRunning = true;
        document.getElementById('start-btn').disabled = true;
        document.getElementById('step-btn').disabled = true;
        
        const animate = () => {
            if (!this.isRunning) return;
            
            this.stepAnimation();
            
            if (this.isRunning && this.currentStep < this.maxSteps) {
                setTimeout(animate, 500);
            } else {
                this.isRunning = false;
                document.getElementById('start-btn').disabled = false;
                document.getElementById('step-btn').disabled = false;
            }
        };
        
        animate();
    }
    
    toggleContour() {
        this.showContour = !this.showContour;
        this.draw();
    }
}

// Initialize when page loads
document.addEventListener('DOMContentLoaded', () => {
    new OptimizationVisualizer();
});
</script>

## Tài liệu tham khảo

1. Boyd, S., & Vandenberghe, L. (2004). *Convex optimization*. Cambridge University Press.
2. Nocedal, J., & Wright, S. J. (2006). *Numerical optimization* (2nd ed.). Springer.
3. Nesterov, Y. (2003). *Introductory lectures on convex optimization: A basic course*. Springer.
4. Bertsekas, D. P. (1999). *Nonlinear programming* (2nd ed.). Athena Scientific.
