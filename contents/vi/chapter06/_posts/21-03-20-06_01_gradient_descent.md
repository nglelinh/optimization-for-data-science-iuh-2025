---
layout: post
title: 06-01 Gradient Descent
chapter: '06'
order: 2
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
lesson_type: required
---

Gradient descent là thuật toán cơ bản nhất để giải các bài toán tối ưu hóa lồi, khả vi và không ràng buộc:

> $$\min_x f(x),$$
> trong đó $$f$$ khả vi và $$dom(f) = \mathbb{R}^n$$.

Giá trị tối ưu được ký hiệu là $$f^* = \min_x f(x)$$ và điểm tối ưu tương ứng là $$x^*$$.

## Vai trò của Gradient Descent trong Khoa học Dữ liệu

Gradient descent là một trong những thuật toán nền tảng của học máy (machine learning), được sử dụng rộng rãi trong:

- **Huấn luyện mạng nơ-ron**: Thuật toán lan truyền ngược (backpropagation) kết hợp với gradient descent để cập nhật trọng số.
- **Hồi quy tuyến tính**: Tìm bộ hệ số tối ưu nhằm cực tiểu hóa sai số bình phương trung bình (MSE).
- **Hồi quy logistic**: Tối ưu hóa tham số cho bài toán phân loại.
- **Học sâu (Deep learning)**: Huấn luyện các mô hình lớn với hàng triệu tham số.
- **Hệ thống gợi ý**: Học biểu diễn sở thích người dùng và đặc trưng sản phẩm.

**Lưu ý**: Trong hầu hết các bài toán huấn luyện mô hình học máy, gradient descent hoặc các biến thể của nó đều đóng vai trò thuật toán tối ưu cốt lõi.

## Gradient Descent cho Hàm Một Biến

Đối với hàm một biến $$f: \mathbb{R} \to \mathbb{R}$$, gradient descent có dạng rất đơn giản. Gradient lúc này chính là đạo hàm bậc nhất, và quy tắc cập nhật được viết như sau:

> $$x^{(k)} = x^{(k-1)} - t f'(x^{(k-1)}), \quad k = 1, 2, 3, ...$$

trong đó $$f'(x)$$ là đạo hàm của $$f$$ tại điểm $$x$$.

### Diễn giải Hình học

Trong trường hợp một biến, đạo hàm $$f'(x)$$ là độ dốc của đường tiếp tuyến với đồ thị hàm số tại điểm $$x$$:
- Nếu $$f'(x) > 0$$, hàm số đang tăng tại $$x$$, nên ta di chuyển sang trái (trừ đi một đại lượng dương).
- Nếu $$f'(x) < 0$$, hàm số đang giảm tại $$x$$, nên ta di chuyển sang phải (trừ đi một đại lượng âm).
- Nếu $$f'(x) = 0$$, ta đã đạt tới điểm dừng (ứng viên cực tiểu).

### Tốc độ học $$t$$

Tốc độ học $$t$$ (còn gọi là kích thước bước) là siêu tham số quan trọng do người thiết kế thuật toán lựa chọn. Tham số này quyết định độ dài mỗi bước di chuyển theo hướng ngược chiều gradient.

**Ảnh hưởng của tốc độ học:**

- **Quá nhỏ ($$t \ll 1$$)**: Các bước cập nhật rất nhỏ, đòi hỏi nhiều lần lặp để tiến tới nghiệm tối ưu. Dù đảm bảo tính ổn định, cách chọn này có thể tốn kém về chi phí tính toán.
- **Quá lớn ($$t \gg 1$$)**: Thuật toán có thể nhảy vượt qua điểm cực tiểu, dẫn đến dao động quanh nghiệm tối ưu hoặc thậm chí phân kỳ ra xa nghiệm.
- **Phù hợp**: Thuật toán hội tụ nhanh và ổn định về nghiệm tối ưu.

**Các chiến lược phổ biến để chọn tốc độ học:**
1. **Kích thước bước cố định**: Giữ nguyên một giá trị $$t$$ không đổi trong suốt quá trình tối ưu hóa.
2. **Tìm kiếm đường chính xác (exact line search)**: Tại mỗi bước lặp, chọn $$t$$ sao cho cực tiểu hóa $$f(x^{(k-1)} - t\nabla f(x^{(k-1)}))$$.
3. **Tìm kiếm đường lùi (backtracking line search)**: Bắt đầu với kích thước bước lớn rồi giảm dần cho đến khi đạt được mức giảm đủ lớn của hàm mục tiêu.
4. **Phương pháp thích ứng**: Tự động điều chỉnh tốc độ học dựa trên lịch sử cập nhật (ví dụ: Adam, RMSprop).

### Ví dụ: Hàm Bậc Hai

Xét hàm bậc hai $$f(x) = \frac{1}{2}(x - 2)^2 + 1$$ với đạo hàm $$f'(x) = x - 2$$.

Quy tắc cập nhật của gradient descent là:
> $$x^{(k)} = x^{(k-1)} - t(x^{(k-1)} - 2)$$

Bắt đầu từ $$x^{(0)} = 0$$ với kích thước bước $$t = 0.1$$:
> $$x^{(1)} = 0 - 0.1(0 - 2) = 0.2$$
> $$x^{(2)} = 0.2 - 0.1(0.2 - 2) = 0.38$$
> $$x^{(3)} = 0.38 - 0.1(0.38 - 2) = 0.542$$
> ...

Dãy lặp này hội tụ về $$x^* = 2$$, cũng là điểm cực tiểu toàn cục của hàm số.

### Lựa chọn Kích thước Bước

Việc chọn kích thước bước $$t$$ ảnh hưởng trực tiếp đến quá trình hội tụ:
- **Quá nhỏ**: Hội tụ rất chậm.
- **Quá lớn**: Có thể vượt quá cực tiểu và phân kỳ.
- **Tối ưu**: Với hàm bậc hai một biến $$f(x) = \frac{1}{2}ax^2 + bx + c$$ ($$a > 0$$), kích thước bước tối ưu là $$t = \frac{1}{a}$$, giúp đạt cực tiểu chỉ sau một bước.

### Trực quan Hóa Tương tác

<div id="single-var-gradient-descent" style="margin: 20px 0;">
    <div style="margin-bottom: 15px;">
        <label for="step-size-slider">Kích thước Bước (t): <span id="step-size-value">0.1</span></label><br>
        <input type="range" id="step-size-slider" min="0.01" max="0.5" step="0.01" value="0.1" style="width: 300px;">
    </div>
    
    <div style="margin-bottom: 15px;">
        <label for="start-point-slider">Điểm Bắt đầu: <span id="start-point-value">-3</span></label><br>
        <input type="range" id="start-point-slider" min="-5" max="5" step="0.1" value="-3" style="width: 300px;">
    </div>
    
    <div style="margin-bottom: 15px;">
        <button id="start-animation">Bắt đầu Animation</button>
        <button id="reset-animation">Reset</button>
        <button id="step-once">Một Bước</button>
    </div>
    
    <canvas id="gradient-canvas" width="600" height="400" style="border: 1px solid #ccc; display: block; margin: 0 auto;"></canvas>
    
    <div id="iteration-info" style="text-align: center; margin-top: 10px; font-family: monospace;">
Lần lặp: 0, x = -3.000, f(x) = 13.500, f'(x) = -5.000
    </div>
</div>

<script>
class SingleVarGradientDescent {
    constructor() {
        this.canvas = document.getElementById('gradient-canvas');
        this.ctx = this.canvas.getContext('2d');
        this.stepSizeSlider = document.getElementById('step-size-slider');
        this.startPointSlider = document.getElementById('start-point-slider');
        this.stepSizeValue = document.getElementById('step-size-value');
        this.startPointValue = document.getElementById('start-point-value');
        this.iterationInfo = document.getElementById('iteration-info');
        
        // Animation state
        this.isAnimating = false;
        this.currentX = -3;
        this.iteration = 0;
        this.history = [];
        this.animationId = null;
        
        // Function parameters: f(x) = 0.5 * (x - 2)^2 + 1
        this.a = 0.5;
        this.b = 2;
        this.c = 1;
        
        this.setupEventListeners();
        this.reset();
    }
    
    setupEventListeners() {
        this.stepSizeSlider.addEventListener('input', (e) => {
            this.stepSizeValue.textContent = e.target.value;
        });
        
        this.startPointSlider.addEventListener('input', (e) => {
            this.startPointValue.textContent = e.target.value;
            if (!this.isAnimating) {
                this.reset();
            }
        });
        
        document.getElementById('start-animation').addEventListener('click', () => {
            this.startAnimation();
        });
        
        document.getElementById('reset-animation').addEventListener('click', () => {
            this.reset();
        });
        
        document.getElementById('step-once').addEventListener('click', () => {
            this.singleStep();
        });
    }
    
    // Function: f(x) = 0.5 * (x - 2)^2 + 1
    f(x) {
        return this.a * Math.pow(x - this.b, 2) + this.c;
    }
    
    // Derivative: f'(x) = (x - 2)
    fprime(x) {
        return 2 * this.a * (x - this.b);
    }
    
    // Convert x coordinate to canvas coordinate
    xToCanvas(x) {
        const xMin = -5, xMax = 5;
        return (x - xMin) / (xMax - xMin) * this.canvas.width;
    }
    
    // Convert y coordinate to canvas coordinate
    yToCanvas(y) {
        const yMin = 0, yMax = 15;
        return this.canvas.height - (y - yMin) / (yMax - yMin) * this.canvas.height;
    }
    
    // Convert canvas x to actual x
    canvasToX(canvasX) {
        const xMin = -5, xMax = 5;
        return xMin + (canvasX / this.canvas.width) * (xMax - xMin);
    }
    
    drawFunction() {
        this.ctx.strokeStyle = '#2196F3';
        this.ctx.lineWidth = 2;
        this.ctx.beginPath();
        
        for (let canvasX = 0; canvasX <= this.canvas.width; canvasX += 2) {
            const x = this.canvasToX(canvasX);
            const y = this.f(x);
            const canvasY = this.yToCanvas(y);
            
            if (canvasX === 0) {
                this.ctx.moveTo(canvasX, canvasY);
            } else {
                this.ctx.lineTo(canvasX, canvasY);
            }
        }
        this.ctx.stroke();
    }
    
    drawAxes() {
        this.ctx.strokeStyle = '#666';
        this.ctx.lineWidth = 1;
        
        // X-axis
        const yZero = this.yToCanvas(0);
        this.ctx.beginPath();
        this.ctx.moveTo(0, yZero);
        this.ctx.lineTo(this.canvas.width, yZero);
        this.ctx.stroke();
        
        // Y-axis
        const xZero = this.xToCanvas(0);
        this.ctx.beginPath();
        this.ctx.moveTo(xZero, 0);
        this.ctx.lineTo(xZero, this.canvas.height);
        this.ctx.stroke();
        
        // Labels
        this.ctx.fillStyle = '#666';
        this.ctx.font = '12px Arial';
        this.ctx.textAlign = 'center';
        
        // X-axis labels
        for (let x = -4; x <= 4; x += 2) {
            const canvasX = this.xToCanvas(x);
            this.ctx.fillText(x.toString(), canvasX, yZero + 15);
        }
        
        // Y-axis labels
        this.ctx.textAlign = 'right';
        for (let y = 2; y <= 14; y += 2) {
            const canvasY = this.yToCanvas(y);
            this.ctx.fillText(y.toString(), xZero - 5, canvasY + 4);
        }
    }
    
    drawCurrentPoint() {
        const canvasX = this.xToCanvas(this.currentX);
        const canvasY = this.yToCanvas(this.f(this.currentX));
        
        // Current point
        this.ctx.fillStyle = '#F44336';
        this.ctx.beginPath();
        this.ctx.arc(canvasX, canvasY, 6, 0, 2 * Math.PI);
        this.ctx.fill();
        
        // Tangent line
        const derivative = this.fprime(this.currentX);
        const tangentLength = 1;
        const x1 = this.currentX - tangentLength;
        const x2 = this.currentX + tangentLength;
        const y1 = this.f(this.currentX) + derivative * (x1 - this.currentX);
        const y2 = this.f(this.currentX) + derivative * (x2 - this.currentX);
        
        this.ctx.strokeStyle = '#FF9800';
        this.ctx.lineWidth = 2;
        this.ctx.beginPath();
        this.ctx.moveTo(this.xToCanvas(x1), this.yToCanvas(y1));
        this.ctx.lineTo(this.xToCanvas(x2), this.yToCanvas(y2));
        this.ctx.stroke();
    }
    
    drawHistory() {
        if (this.history.length < 2) return;
        
        this.ctx.strokeStyle = '#4CAF50';
        this.ctx.lineWidth = 2;
        this.ctx.setLineDash([5, 5]);
        this.ctx.beginPath();
        
        for (let i = 0; i < this.history.length; i++) {
            const x = this.history[i];
            const canvasX = this.xToCanvas(x);
            const canvasY = this.yToCanvas(this.f(x));
            
            if (i === 0) {
                this.ctx.moveTo(canvasX, canvasY);
            } else {
                this.ctx.lineTo(canvasX, canvasY);
            }
        }
        this.ctx.stroke();
        this.ctx.setLineDash([]);
        
        // Draw history points
        this.ctx.fillStyle = '#4CAF50';
        for (let i = 0; i < this.history.length - 1; i++) {
            const x = this.history[i];
            const canvasX = this.xToCanvas(x);
            const canvasY = this.yToCanvas(this.f(x));
            
            this.ctx.beginPath();
            this.ctx.arc(canvasX, canvasY, 3, 0, 2 * Math.PI);
            this.ctx.fill();
        }
    }
    
    draw() {
        // Clear canvas
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
        
        // Draw components
        this.drawAxes();
        this.drawFunction();
        this.drawHistory();
        this.drawCurrentPoint();
        
        // Update iteration info
        this.iterationInfo.textContent = 
            `Lần lặp: ${this.iteration}, x = ${this.currentX.toFixed(3)}, ` +
            `f(x) = ${this.f(this.currentX).toFixed(3)}, f'(x) = ${this.fprime(this.currentX).toFixed(3)}`;
    }
    
    singleStep() {
        if (Math.abs(this.fprime(this.currentX)) < 1e-6) {
            return; // Already at minimum
        }
        
        const stepSize = parseFloat(this.stepSizeSlider.value);
        const newX = this.currentX - stepSize * this.fprime(this.currentX);
        
        this.history.push(this.currentX);
        this.currentX = newX;
        this.iteration++;
        
        this.draw();
    }
    
    startAnimation() {
        if (this.isAnimating) {
            this.stopAnimation();
            return;
        }
        
        this.isAnimating = true;
        document.getElementById('start-animation').textContent = 'Dừng Animation';
        
        const animate = () => {
            if (!this.isAnimating) return;
            
            if (Math.abs(this.fprime(this.currentX)) > 1e-6 && this.iteration < 100) {
                this.singleStep();
                this.animationId = setTimeout(animate, 500);
            } else {
                this.stopAnimation();
            }
        };
        
        animate();
    }
    
    stopAnimation() {
        this.isAnimating = false;
        document.getElementById('start-animation').textContent = 'Bắt đầu Animation';
        if (this.animationId) {
            clearTimeout(this.animationId);
            this.animationId = null;
        }
    }
    
    reset() {
        this.stopAnimation();
        this.currentX = parseFloat(this.startPointSlider.value);
        this.iteration = 0;
        this.history = [];
        this.draw();
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    new SingleVarGradientDescent();
});
</script>

## Phương pháp Gradient Descent cho Hàm Nhiều Biến

Gradient descent bắt đầu từ một điểm khởi tạo $$x^{(0)} \in \mathbb{R}^n$$ và cập nhật lặp cho đến khi tiêu chuẩn dừng được thỏa mãn:
> $$x^{(k)} = x^{(k-1)} - t \nabla f(x^{(k-1)}), \quad k = 1, 2, 3, ..., \quad t > 0$$

Mã giả:
> **Cho điểm khởi tạo** $$x \in dom(f)$$ <br>
> **Lặp lại** <br>
> 1. Xác định hướng giảm $$\Delta x = -\nabla f(x)$$. <br>
> 2. Tìm kiếm đường (line search): chọn kích thước bước $$t > 0$$. <br>
> 3. Cập nhật $$x = x + t \Delta x$$. <br>
> **Cho đến khi** tiêu chuẩn dừng được thỏa mãn <br>

### Ví dụ

Hình dưới đây minh họa gradient descent trên một hàm lồi. Trong trường hợp này, mọi cực tiểu cục bộ đều là cực tiểu toàn cục.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter06/06_01_gradientdescent1.png" alt="gradientdescent1" width="80%" height="80%">
  <figcaption style="text-align: center;">[Hình 1] Gradient descent trên hàm lồi [3]</figcaption>
</p>
</figure>

Hình tiếp theo minh họa gradient descent trên một hàm không lồi. Khi đó, điểm khởi tạo quyết định thuật toán sẽ hội tụ về cực tiểu cục bộ nào.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter06/06_01_gradientdescent2.png" alt="gradientdescent2" width="80%" height="80%">
  <figcaption style="text-align: center;">[Hình 2] Gradient descent trên hàm không lồi [3]</figcaption>
</p>
</figure>

## Diễn giải Gradient Descent

Gradient descent có thể được hiểu như quá trình chọn điểm tiếp theo bằng cách cực tiểu hóa một xấp xỉ bậc hai cục bộ của hàm mục tiêu.

Đối với hàm $$f$$, khai triển Taylor bậc hai quanh điểm $$x$$ có dạng:
>$$f(y) \approx f(x) + \nabla f(x)^T (y - x) + \frac{1}{2} (y - x)^T \nabla^2 f(x) (y - x)$$

Nếu ta xấp xỉ ma trận Hessian $$\nabla^2 f(x)$$ bằng $$\frac{1}{t}I$$, ta thu được:
>$$f(y) \approx f(x) + \nabla f(x)^T (y - x) + \frac{1}{2t} \|y - x\|_2^2$$
trong đó $$t$$ là kích thước bước.

Như vậy, gradient descent xấp xỉ hàm mục tiêu bằng một hàm bậc hai có ma trận Hessian đẳng hướng với mọi giá trị riêng đều bằng $$\frac{1}{t}$$. Biểu thức $$f(x) + \nabla f(x)^T (y - x)$$ là xấp xỉ tuyến tính của $$f$$ quanh $$x$$, còn $$\frac{1}{2t} \|y - x\|_2^2$$ đóng vai trò là số hạng gần kề (proximal term), kiểm soát khoảng cách giữa $$y$$ và $$x$$.

Điểm tiếp theo $$y = x^+$$ được chọn làm cực tiểu của hàm bậc hai xấp xỉ này. Đặt gradient theo $$y$$ bằng 0, ta thu được:

> $$x^+ = x - t \nabla f(x)$$

Trong hình minh họa bên dưới, chấm xanh biểu diễn vị trí hiện tại $$x$$ và chấm đỏ biểu diễn vị trí tiếp theo $$x^+$$. Đường cong phía dưới là hàm thực $$f$$, còn đường cong phía trên là hàm bậc hai xấp xỉ của $$f$$; chấm đỏ chính là điểm cực tiểu của hàm bậc hai xấp xỉ đó.

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl }}/img/chapter_img/chapter06/06_01_gradientdescent3.png" alt="gradientdescent3" width="80%" height="80%">
  <figcaption style="text-align: center;">$$ \text{[Hình 3] Thuật toán Gradient descent : chấm đỏ là } x^+ \text{ và chấm xanh là } x \text{ [3]} $$</figcaption>
</p>
</figure>

Khoảng cách từ vị trí mới $$y$$ tới vị trí hiện tại $$x$$ chịu ảnh hưởng trực tiếp bởi trọng số $$\frac{1}{2t}$$ của số hạng gần kề. Khi $$t$$ nhỏ, trọng số này lớn hơn, buộc thuật toán chỉ thực hiện các bước nhỏ quanh $$x$$. Quy tắc cập nhật này có thể viết gọn dưới dạng bài toán tối ưu:

> \begin{align}
x^+ = \underset{y}{\arg \min} \ f(x) + \nabla f(x)^T (y - x) + \frac{1}{2t} \parallel y - x \parallel_2^2
\end{align}
