---
layout: post
title: 11-7 Trực Quan về Lagrange Duality
chapter: '11'
order: 8
owner: GitHub Copilot
lang: vi
categories:
- chapter11
---

# Trực Quan về Lagrange Duality

## 🔍 Bài toán tối ưu tổng quát

Giả sử chúng ta cần giải bài toán tối ưu:

$$\begin{align}
\min_x f(x) \\
\text{s.t. } h_i(x) \leq 0, \quad i=1,\ldots,m \\
\mathcal{D} = \text{dom } f \cap \bigcap_{i=1}^{m} \text{dom } h_i
\end{align}$$

*Lưu ý: Để đơn giản, chúng ta chỉ xét ràng buộc bất đẳng thức. Ràng buộc đẳng thức có thể được biểu diễn bằng hai ràng buộc bất đẳng thức.*

## 🎭 "Bí ẩn" của Dual

Theo quy trình chuẩn, chúng ta xây dựng hàm Lagrangian:

$$L(x, \lambda) = f(x) + \lambda^T h(x), \quad \lambda \succeq 0$$

Sau đó định nghĩa hàm dual "bí ẩn":

$$\begin{align}
g(\lambda) &= \inf_{x \in \mathcal{D}} L(x, \lambda) \\
&= \inf_{x \in \mathcal{D}} (f(x) + \lambda^T h(x))
\end{align}$$

*Lưu ý: Để tìm infimum, x vẫn trong miền $$\mathcal{D}$$, không phải trong vùng khả thi từ các ràng buộc.*

Cuối cùng, bằng cách giải bài toán dual:

$$\max_{\lambda} g(\lambda) \quad \text{s.t. } \lambda \succeq 0$$

Chúng ta có thể tìm được một cận dưới tốt cho bài toán nguyên thủy.

## 🤔 Tại sao cần hàm Lagrangian?

> **Câu hỏi:** Tại sao chúng ta cần xây dựng hàm Lagrangian này?
> 
> **Trả lời:** Vì vấn đề về **nhiễu động (perturbation)**

Chúng ta không thể giải bài toán nguyên thủy bằng cách đơn giản tính $$\frac{\partial f(x)}{\partial x} = 0$$ vì có vùng khả thi từ các ràng buộc. Một giải pháp khả thi là thêm các ràng buộc như các số hạng nhiễu động, sau đó ước lượng cận dưới tốt nhất.

### 💡 Ví dụ minh họa

Xét bài toán tối ưu:

$$\begin{align}
\min_x x^2 \\
\text{s.t. } x - 1 \leq 0 \\
\mathcal{D} = \mathbb{R}
\end{align}$$

Nghiệm tối ưu dễ đoán: $$p^* = 0$$ khi $$x = 0$$.

**Hàm Lagrangian:**
$$L(x, \lambda) = x^2 + \lambda(x - 1), \quad \lambda \geq 0$$

**Hàm dual:**
$$g(\lambda) = \inf_{x \in \mathcal{D}} (x^2 + \lambda(x - 1)), \quad \lambda \geq 0$$

Để tìm $$\inf_{x \in \mathcal{D}} (x^2 + \lambda(x - 1))$$, ta cần $$\frac{\partial L(x,\lambda)}{\partial x} = 0$$.

Do đó: $$2x + \lambda = 0 \Rightarrow x = -\frac{\lambda}{2}$$

Thay ngược lại vào hàm dual:
$$g(\lambda) = \frac{\lambda^2}{4} - \lambda \cdot \frac{\lambda}{2} - \lambda = -\frac{\lambda^2}{4} - \lambda, \quad \lambda \geq 0$$

**Bài toán dual:**
$$\max_{\lambda} g(\lambda) \quad \text{s.t. } \lambda \geq 0$$

Nghiệm dual: $$d^* = -1$$ với $$\lambda = -2$$ (nhưng $$\lambda \geq 0$$, nên $$d^* = 0$$ với $$\lambda = 0$$)

<div id="lagrangian-visualization" style="margin: 20px 0;">
    <canvas id="lagrangianCanvas" width="800" height="400" style="border: 1px solid #ccc; display: block; margin: 0 auto;"></canvas>
    <div style="text-align: center; margin: 10px 0;">
        <label>λ = <span id="lambdaValue">0</span></label><br>
        <input type="range" id="lambdaSlider" min="0" max="4" step="0.1" value="0" style="width: 300px;">
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('lagrangianCanvas');
    const ctx = canvas.getContext('2d');
    const slider = document.getElementById('lambdaSlider');
    const valueSpan = document.getElementById('lambdaValue');
    
    function drawVisualization() {
        const lambda = parseFloat(slider.value);
        valueSpan.textContent = lambda.toFixed(1);
        
        // Clear canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Set up coordinate system
        const centerX = canvas.width / 2;
        const centerY = canvas.height / 2;
        const scale = 50;
        
        // Draw axes
        ctx.strokeStyle = '#ddd';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(0, centerY);
        ctx.lineTo(canvas.width, centerY);
        ctx.moveTo(centerX, 0);
        ctx.lineTo(centerX, canvas.height);
        ctx.stroke();
        
        // Draw original function f(x) = x^2
        ctx.strokeStyle = '#000';
        ctx.lineWidth = 2;
        ctx.beginPath();
        let first = true;
        for (let x = -4; x <= 4; x += 0.1) {
            const screenX = centerX + x * scale;
            const screenY = centerY - (x * x) * scale / 4;
            if (screenY >= 0 && screenY <= canvas.height) {
                if (first) {
                    ctx.moveTo(screenX, screenY);
                    first = false;
                } else {
                    ctx.lineTo(screenX, screenY);
                }
            }
        }
        ctx.stroke();
        
        // Draw Lagrangian L(x,λ) = x^2 + λ(x-1)
        if (lambda > 0) {
            ctx.strokeStyle = lambda < 2 ? '#0066cc' : '#00cc66';
            ctx.lineWidth = 2;
            ctx.beginPath();
            first = true;
            for (let x = -4; x <= 4; x += 0.1) {
                const lagrangian = x * x + lambda * (x - 1);
                const screenX = centerX + x * scale;
                const screenY = centerY - lagrangian * scale / 4;
                if (screenY >= 0 && screenY <= canvas.height) {
                    if (first) {
                        ctx.moveTo(screenX, screenY);
                        first = false;
                    } else {
                        ctx.lineTo(screenX, screenY);
                    }
                }
            }
            ctx.stroke();
            
            // Mark minimum point
            const minX = -lambda / 2;
            const minY = -lambda * lambda / 4 - lambda;
            const screenMinX = centerX + minX * scale;
            const screenMinY = centerY - minY * scale / 4;
            
            if (screenMinY >= 0 && screenMinY <= canvas.height) {
                ctx.fillStyle = lambda < 2 ? '#0066cc' : '#00cc66';
                ctx.beginPath();
                ctx.arc(screenMinX, screenMinY, 4, 0, 2 * Math.PI);
                ctx.fill();
            }
        }
        
        // Draw constraint boundary x = 1
        ctx.strokeStyle = '#ff6666';
        ctx.lineWidth = 2;
        ctx.setLineDash([5, 5]);
        ctx.beginPath();
        ctx.moveTo(centerX + scale, 0);
        ctx.lineTo(centerX + scale, canvas.height);
        ctx.stroke();
        ctx.setLineDash([]);
        
        // Mark optimal point
        ctx.fillStyle = '#ff0000';
        ctx.beginPath();
        ctx.arc(centerX + scale, centerY - scale / 4, 5, 0, 2 * Math.PI);
        ctx.fill();
        
        // Add labels
        ctx.fillStyle = '#000';
        ctx.font = '14px Arial';
        ctx.fillText('f(x) = x²', 20, 30);
        if (lambda > 0) {
            ctx.fillStyle = lambda < 2 ? '#0066cc' : '#00cc66';
            ctx.fillText(`L(x,${lambda}) = x² + ${lambda}(x-1)`, 20, 50);
        }
        ctx.fillStyle = '#ff0000';
        ctx.fillText('x = 1 (ràng buộc)', centerX + scale + 10, 30);
        ctx.fillText('p* = 1', centerX + scale + 10, centerY - scale / 4 - 10);
    }
    
    slider.addEventListener('input', drawVisualization);
    drawVisualization();
});
</script>

**Hình 1:** *Hàm Lagrangian và hàm dual. Đường cong đen là bài toán gốc, đường cong xanh và xanh lá là bài toán gốc với nhiễu động. Chúng ta có thể thấy các giá trị của $$\inf_{x \in \mathcal{D}} L(x, \lambda)$$ (điểm yên ngựa trên đường cong xanh và xanh lá) luôn nhỏ hơn hoặc bằng nghiệm tối ưu $$p^*$$.*

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/chapter_img/lagrangian_function_example.png" alt="Lagrangian Function Example" style="max-width: 100%; height: auto;">
    <p><em>Nguồn: <a href="https://masszhou.github.io/2016/09/10/Lagrange-Duality/">Zhiliang Zhou's Blog</a></em></p>
</div>

## 🎯 Tại sao giải bài toán dual?

> **Câu hỏi:** Tại sao chúng ta chọn giải bài toán dual để ước lượng cận dưới? Có dễ hơn không?
> 
> **Trả lời:** **CÓ**. Nó dễ giải hơn.

Thực tế, hàm dual $$g(\lambda)$$ là **lõm (concave)**, hay nói cách khác $$-g(\lambda)$$ là **lồi (convex)**.

Từ phương trình (3), chúng ta biết $$-g(\lambda)$$ là supremum theo từng điểm của một tập các hàm affine theo $$\lambda$$, điều này có nghĩa $$-g(\lambda)$$ là lồi.

<div id="dual-function-visualization" style="margin: 20px 0;">
    <canvas id="dualCanvas" width="600" height="300" style="border: 1px solid #ccc; display: block; margin: 0 auto;"></canvas>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('dualCanvas');
    const ctx = canvas.getContext('2d');
    
    function drawDualVisualization() {
        // Clear canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Set up coordinate system
        const centerX = 50;
        const centerY = canvas.height - 50;
        const scaleX = 100;
        const scaleY = 50;
        
        // Draw axes
        ctx.strokeStyle = '#ddd';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(centerX, 0);
        ctx.lineTo(centerX, canvas.height);
        ctx.moveTo(0, centerY);
        ctx.lineTo(canvas.width, centerY);
        ctx.stroke();
        
        // Draw several affine functions
        const colors = ['#ff9999', '#99ff99', '#9999ff', '#ffff99', '#ff99ff'];
        for (let i = 0; i < 5; i++) {
            const a = -2 + i * 1;
            const b = 1 + i * 0.5;
            
            ctx.strokeStyle = colors[i];
            ctx.lineWidth = 1;
            ctx.beginPath();
            
            for (let lambda = 0; lambda <= 5; lambda += 0.1) {
                const y = a * lambda + b;
                const screenX = centerX + lambda * scaleX;
                const screenY = centerY - y * scaleY;
                
                if (lambda === 0) {
                    ctx.moveTo(screenX, screenY);
                } else {
                    ctx.lineTo(screenX, screenY);
                }
            }
            ctx.stroke();
        }
        
        // Draw pointwise supremum (envelope)
        ctx.strokeStyle = '#ff0000';
        ctx.lineWidth = 3;
        ctx.beginPath();
        
        for (let lambda = 0; lambda <= 5; lambda += 0.05) {
            let maxY = -Infinity;
            for (let i = 0; i < 5; i++) {
                const a = -2 + i * 1;
                const b = 1 + i * 0.5;
                const y = a * lambda + b;
                maxY = Math.max(maxY, y);
            }
            
            const screenX = centerX + lambda * scaleX;
            const screenY = centerY - maxY * scaleY;
            
            if (lambda === 0) {
                ctx.moveTo(screenX, screenY);
            } else {
                ctx.lineTo(screenX, screenY);
            }
        }
        ctx.stroke();
        
        // Add labels
        ctx.fillStyle = '#000';
        ctx.font = '14px Arial';
        ctx.fillText('λ', canvas.width - 30, centerY + 20);
        ctx.fillText('g(λ)', centerX - 30, 20);
        
        ctx.fillStyle = '#ff0000';
        ctx.fillText('Supremum theo từng điểm', 300, 30);
        ctx.fillText('(hàm lồi)', 300, 50);
    }
    
    drawDualVisualization();
});
</script>

**Hình 2:** *Supremum theo từng điểm của tập các hàm affine là hàm lồi*

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/chapter_img/pointwise_supremum_convex.png" alt="Pointwise Supremum of Affine Functions" style="max-width: 100%; height: auto;">
    <p><em>Nguồn: <a href="https://masszhou.github.io/2016/09/10/Lagrange-Duality/">Zhiliang Zhou's Blog</a></em></p>
</div>

Hình 2 cho thấy một tập các hàm affine, đường đỏ đại diện cho supremum theo từng điểm. Rõ ràng trong hình này đường đỏ là một hàm lồi. Chúng ta biết rằng đối với hàm và tập lồi, việc giải cực trị toàn cục là dễ dàng. Bất kể $$f(x)$$ có lồi hay không, hàm dual của nó luôn lõm, đây là một tính chất thuận tiện.

## 🔗 Kết nối với hàm liên hợp (Conjugate Function)

Khi các ràng buộc trong phương trình (1) là tuyến tính, hàm dual thường trông giống với hàm liên hợp.

### 📐 Hàm liên hợp

Hàm liên hợp của $$f(x)$$ được định nghĩa là:

$$f^*(λ) = \sup_x (λ^T x - f(x))$$

<div id="conjugate-visualization" style="margin: 20px 0;">
    <canvas id="conjugateCanvas" width="600" height="400" style="border: 1px solid #ccc; display: block; margin: 0 auto;"></canvas>
    <div style="text-align: center; margin: 10px 0;">
        <label>Độ dốc λ = <span id="slopeValue">1</span></label><br>
        <input type="range" id="slopeSlider" min="-3" max="3" step="0.1" value="1" style="width: 300px;">
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('conjugateCanvas');
    const ctx = canvas.getContext('2d');
    const slider = document.getElementById('slopeSlider');
    const valueSpan = document.getElementById('slopeValue');
    
    function drawConjugateVisualization() {
        const slope = parseFloat(slider.value);
        valueSpan.textContent = slope.toFixed(1);
        
        // Clear canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Set up coordinate system
        const centerX = canvas.width / 2;
        const centerY = canvas.height * 0.7;
        const scale = 30;
        
        // Draw axes
        ctx.strokeStyle = '#ddd';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(0, centerY);
        ctx.lineTo(canvas.width, centerY);
        ctx.moveTo(centerX, 0);
        ctx.lineTo(centerX, canvas.height);
        ctx.stroke();
        
        // Draw function f(x) = x^2/2
        ctx.strokeStyle = '#00cc00';
        ctx.lineWidth = 3;
        ctx.beginPath();
        let first = true;
        for (let x = -8; x <= 8; x += 0.1) {
            const y = x * x / 2;
            const screenX = centerX + x * scale;
            const screenY = centerY - y * scale;
            if (screenY >= 0 && screenY <= canvas.height) {
                if (first) {
                    ctx.moveTo(screenX, screenY);
                    first = false;
                } else {
                    ctx.lineTo(screenX, screenY);
                }
            }
        }
        ctx.stroke();
        
        // Draw line λx with given slope
        ctx.strokeStyle = '#000';
        ctx.lineWidth = 2;
        ctx.beginPath();
        for (let x = -8; x <= 8; x += 0.1) {
            const y = slope * x;
            const screenX = centerX + x * scale;
            const screenY = centerY - y * scale;
            if (screenY >= 0 && screenY <= canvas.height && screenX >= 0 && screenX <= canvas.width) {
                if (x === -8) {
                    ctx.moveTo(screenX, screenY);
                } else {
                    ctx.lineTo(screenX, screenY);
                }
            }
        }
        ctx.stroke();
        
        // Find and mark the point where λx - f(x) is maximized
        let maxDiff = -Infinity;
        let maxX = 0;
        for (let x = -8; x <= 8; x += 0.01) {
            const diff = slope * x - x * x / 2;
            if (diff > maxDiff) {
                maxDiff = diff;
                maxX = x;
            }
        }
        
        // Draw tangent line at optimal point
        ctx.strokeStyle = '#ff6600';
        ctx.lineWidth = 2;
        ctx.setLineDash([5, 5]);
        ctx.beginPath();
        const tangentY = maxX * maxX / 2;
        const tangentScreenX = centerX + maxX * scale;
        const tangentScreenY = centerY - tangentY * scale;
        
        // Draw tangent line
        for (let x = -8; x <= 8; x += 0.1) {
            const y = slope * x - slope * slope / 2;
            const screenX = centerX + x * scale;
            const screenY = centerY - y * scale;
            if (screenY >= 0 && screenY <= canvas.height && screenX >= 0 && screenX <= canvas.width) {
                if (x === -8) {
                    ctx.moveTo(screenX, screenY);
                } else {
                    ctx.lineTo(screenX, screenY);
                }
            }
        }
        ctx.stroke();
        ctx.setLineDash([]);
        
        // Mark optimal point
        ctx.fillStyle = '#ff0000';
        ctx.beginPath();
        ctx.arc(tangentScreenX, tangentScreenY, 5, 0, 2 * Math.PI);
        ctx.fill();
        
        // Add labels
        ctx.fillStyle = '#00cc00';
        ctx.font = '16px Arial';
        ctx.fillText('f(x) = x²/2', 20, 30);
        
        ctx.fillStyle = '#000';
        ctx.fillText(`λx (λ = ${slope.toFixed(1)})`, 20, 55);
        
        ctx.fillStyle = '#ff6600';
        ctx.fillText('Đường tiếp tuyến', 20, 80);
        
        ctx.fillStyle = '#ff0000';
        ctx.fillText(`f*(λ) = ${(slope * slope / 2).toFixed(2)}`, 20, 105);
    }
    
    slider.addEventListener('input', drawConjugateVisualization);
    drawConjugateVisualization();
});
</script>

**Hình 3:** *Hàm liên hợp. Đường cong xanh lá là $$f(x)$$, đường thẳng đen là $$λ^T x$$, các vector (có dấu) giữa $$λ^T x$$ và $$f(x)$$ là $$λ^T x - f(x)$$. Vậy hàm liên hợp $$f^*(λ)$$ là về khoảng cách lớn nhất giữa đường thẳng $$λ^T x$$ và $$f(x)$$.*

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/chapter_img/conjugate_function_geometric.png" alt="Conjugate Function Geometric Interpretation" style="max-width: 100%; height: auto;">
    <p><em>Nguồn: <a href="https://masszhou.github.io/2016/09/10/Lagrange-Duality/">Zhiliang Zhou's Blog</a></em></p>
</div>

### 🔄 Khi ràng buộc là tuyến tính

Khi các ràng buộc là tuyến tính, bài toán tối ưu có dạng:

$$\min_x f(x) \quad \text{s.t. } Ax \preceq b$$

Hàm dual Lagrange là:

$$\begin{align}
g(λ) &= \inf_x (f(x) + λ^T(Ax - b)) \quad \text{với } λ \succeq 0 \\
&= -\sup_x (-λ^T A x - f(x)) - λ^T b \\
&= -f^*(-λ^T A) - λ^T b \quad \text{theo phương trình (9)}
\end{align}$$

Trực quan, vì $$-λ^T b$$ là số hạng tuyến tính, các giá trị cực trị chỉ bị ảnh hưởng bởi miền, vì vậy nếu chúng ta tập trung vào số hạng $$-f^*(-λ^T A)$$, việc giải $$\max_λ g(λ)$$ có nghĩa là giải $$\min f^*(-λ^T A)$$.

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/chapter_img/conjugate_minimum_example.png" alt="Minimum of Conjugate Function" style="max-width: 100%; height: auto;">
    <p><em>Hình 4: Minimum của hàm liên hợp - Nguồn: <a href="https://masszhou.github.io/2016/09/10/Lagrange-Duality/">Zhiliang Zhou's Blog</a></em></p>
</div>

## 💻 Ví dụ tương tác

Hãy xem một ví dụ cụ thể với bài toán:

$$\min x^2 \quad \text{s.t. } x \leq 1$$

<div id="complete-example" style="margin: 20px 0; padding: 20px; border: 1px solid #ddd; border-radius: 5px;">
    <h4>Minh họa hoàn chỉnh</h4>
    <canvas id="completeCanvas" width="800" height="500" style="border: 1px solid #ccc; display: block; margin: 0 auto;"></canvas>
    <div style="text-align: center; margin: 10px 0;">
        <button id="animateBtn" style="padding: 10px 20px; font-size: 16px;">Chạy Animation</button>
        <button id="resetBtn" style="padding: 10px 20px; font-size: 16px; margin-left: 10px;">Reset</button>
    </div>
    <div id="explanation" style="margin-top: 20px; font-size: 14px; line-height: 1.6;">
        <p><strong>Giải thích:</strong></p>
        <ul>
            <li><span style="color: #000; font-weight: bold;">Đường đen:</span> Hàm gốc f(x) = x²</li>
            <li><span style="color: #0066cc; font-weight: bold;">Đường xanh:</span> Hàm Lagrangian L(x,λ)</li>
            <li><span style="color: #ff6666; font-weight: bold;">Đường đỏ đứt:</span> Ràng buộc x ≤ 1</li>
            <li><span style="color: #ff0000; font-weight: bold;">Điểm đỏ:</span> Nghiệm tối ưu p* = 1</li>
            <li><span style="color: #0066cc; font-weight: bold;">Điểm xanh:</span> Minimum của Lagrangian (cung cấp cận dưới)</li>
        </ul>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const canvas = document.getElementById('completeCanvas');
    const ctx = canvas.getContext('2d');
    const animateBtn = document.getElementById('animateBtn');
    const resetBtn = document.getElementById('resetBtn');
    
    let animationId = null;
    let currentLambda = 0;
    let isAnimating = false;
    
    function drawCompleteExample(lambda) {
        // Clear canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Set up coordinate system
        const leftPanel = { x: 50, y: 50, width: 350, height: 300 };
        const rightPanel = { x: 450, y: 50, width: 300, height: 300 };
        
        // Left panel: Primal space
        drawPrimalSpace(leftPanel, lambda);
        
        // Right panel: Dual function
        drawDualSpace(rightPanel, lambda);
        
        // Add titles
        ctx.fillStyle = '#000';
        ctx.font = 'bold 16px Arial';
        ctx.fillText('Không gian Primal', leftPanel.x + 100, leftPanel.y - 20);
        ctx.fillText('Hàm Dual g(λ)', rightPanel.x + 80, rightPanel.y - 20);
        
        // Add current lambda value
        ctx.fillText(`λ hiện tại: ${lambda.toFixed(2)}`, 50, canvas.height - 30);
        
        // Calculate and display dual value
        const dualValue = -lambda * lambda / 4 - lambda;
        ctx.fillText(`g(λ) = ${dualValue.toFixed(3)}`, 250, canvas.height - 30);
    }
    
    function drawPrimalSpace(panel, lambda) {
        const centerX = panel.x + panel.width / 2;
        const centerY = panel.y + panel.height - 50;
        const scale = 40;
        
        // Draw axes
        ctx.strokeStyle = '#ddd';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(panel.x, centerY);
        ctx.lineTo(panel.x + panel.width, centerY);
        ctx.moveTo(centerX, panel.y);
        ctx.lineTo(centerX, panel.y + panel.height);
        ctx.stroke();
        
        // Draw original function f(x) = x^2
        ctx.strokeStyle = '#000';
        ctx.lineWidth = 3;
        ctx.beginPath();
        let first = true;
        for (let x = -3; x <= 3; x += 0.1) {
            const y = x * x;
            const screenX = centerX + x * scale;
            const screenY = centerY - y * scale / 2;
            if (screenY >= panel.y && screenY <= panel.y + panel.height) {
                if (first) {
                    ctx.moveTo(screenX, screenY);
                    first = false;
                } else {
                    ctx.lineTo(screenX, screenY);
                }
            }
        }
        ctx.stroke();
        
        // Draw Lagrangian if lambda > 0
        if (lambda > 0) {
            ctx.strokeStyle = '#0066cc';
            ctx.lineWidth = 2;
            ctx.beginPath();
            first = true;
            for (let x = -3; x <= 3; x += 0.1) {
                const lagrangian = x * x + lambda * (x - 1);
                const screenX = centerX + x * scale;
                const screenY = centerY - lagrangian * scale / 2;
                if (screenY >= panel.y && screenY <= panel.y + panel.height) {
                    if (first) {
                        ctx.moveTo(screenX, screenY);
                        first = false;
                    } else {
                        ctx.lineTo(screenX, screenY);
                    }
                }
            }
            ctx.stroke();
            
            // Mark minimum of Lagrangian
            const minX = -lambda / 2;
            const minY = -lambda * lambda / 4 - lambda;
            const screenMinX = centerX + minX * scale;
            const screenMinY = centerY - minY * scale / 2;
            
            if (screenMinY >= panel.y && screenMinY <= panel.y + panel.height) {
                ctx.fillStyle = '#0066cc';
                ctx.beginPath();
                ctx.arc(screenMinX, screenMinY, 5, 0, 2 * Math.PI);
                ctx.fill();
            }
        }
        
        // Draw constraint x = 1
        ctx.strokeStyle = '#ff6666';
        ctx.lineWidth = 2;
        ctx.setLineDash([5, 5]);
        ctx.beginPath();
        ctx.moveTo(centerX + scale, panel.y);
        ctx.lineTo(centerX + scale, panel.y + panel.height);
        ctx.stroke();
        ctx.setLineDash([]);
        
        // Mark optimal point
        ctx.fillStyle = '#ff0000';
        ctx.beginPath();
        ctx.arc(centerX + scale, centerY - scale / 2, 6, 0, 2 * Math.PI);
        ctx.fill();
        
        // Add labels
        ctx.fillStyle = '#000';
        ctx.font = '12px Arial';
        ctx.fillText('f(x) = x²', panel.x + 10, panel.y + 20);
        if (lambda > 0) {
            ctx.fillStyle = '#0066cc';
            ctx.fillText(`L(x,${lambda.toFixed(1)})`, panel.x + 10, panel.y + 35);
        }
    }
    
    function drawDualSpace(panel, currentLambda) {
        const centerX = panel.x + 20;
        const centerY = panel.y + panel.height - 50;
        const scaleX = 60;
        const scaleY = 40;
        
        // Draw axes
        ctx.strokeStyle = '#ddd';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(centerX, panel.y);
        ctx.lineTo(centerX, panel.y + panel.height);
        ctx.moveTo(centerX, centerY);
        ctx.lineTo(panel.x + panel.width, centerY);
        ctx.stroke();
        
        // Draw dual function g(λ) = -λ²/4 - λ
        ctx.strokeStyle = '#cc0000';
        ctx.lineWidth = 3;
        ctx.beginPath();
        let first = true;
        for (let lambda = 0; lambda <= 4; lambda += 0.05) {
            const g = -lambda * lambda / 4 - lambda;
            const screenX = centerX + lambda * scaleX;
            const screenY = centerY - g * scaleY;
            if (screenY >= panel.y && screenY <= panel.y + panel.height) {
                if (first) {
                    ctx.moveTo(screenX, screenY);
                    first = false;
                } else {
                    ctx.lineTo(screenX, screenY);
                }
            }
        }
        ctx.stroke();
        
        // Mark current point
        const currentG = -currentLambda * currentLambda / 4 - currentLambda;
        const currentScreenX = centerX + currentLambda * scaleX;
        const currentScreenY = centerY - currentG * scaleY;
        
        if (currentScreenY >= panel.y && currentScreenY <= panel.y + panel.height) {
            ctx.fillStyle = '#cc0000';
            ctx.beginPath();
            ctx.arc(currentScreenX, currentScreenY, 6, 0, 2 * Math.PI);
            ctx.fill();
        }
        
        // Add labels
        ctx.fillStyle = '#000';
        ctx.font = '12px Arial';
        ctx.fillText('λ', panel.x + panel.width - 20, centerY + 15);
        ctx.fillText('g(λ)', centerX - 15, panel.y + 15);
        
        // Add axis labels
        for (let i = 0; i <= 4; i++) {
            ctx.fillText(i.toString(), centerX + i * scaleX - 3, centerY + 15);
        }
    }
    
    function animate() {
        if (!isAnimating) return;
        
        currentLambda += 0.02;
        if (currentLambda > 4) {
            currentLambda = 0;
        }
        
        drawCompleteExample(currentLambda);
        animationId = requestAnimationFrame(animate);
    }
    
    animateBtn.addEventListener('click', function() {
        if (isAnimating) {
            isAnimating = false;
            if (animationId) {
                cancelAnimationFrame(animationId);
            }
            animateBtn.textContent = 'Chạy Animation';
        } else {
            isAnimating = true;
            animateBtn.textContent = 'Dừng Animation';
            animate();
        }
    });
    
    resetBtn.addEventListener('click', function() {
        isAnimating = false;
        if (animationId) {
            cancelAnimationFrame(animationId);
        }
        currentLambda = 0;
        animateBtn.textContent = 'Chạy Animation';
        drawCompleteExample(currentLambda);
    });
    
    // Initial draw
    drawCompleteExample(currentLambda);
});
</script>

## 🎓 Kết luận

<div style="text-align: center; margin: 20px 0;">
    <img src="/img/chapter_img/lagrange_duality_framework.png" alt="Lagrange Duality Framework Overview" style="max-width: 100%; height: auto;">
    <p><em>Hình 5: Tổng quan về Framework Lagrange Duality - Nguồn: <a href="https://masszhou.github.io/2016/09/10/Lagrange-Duality/">Zhiliang Zhou's Blog</a></em></p>
</div>

Lagrange Duality cung cấp một cách tiếp cận mạnh mẽ để giải quyết các bài toán tối ưu phức tạp bằng cách:

1. **Chuyển đổi ràng buộc thành nhiễu động:** Hàm Lagrangian thêm các ràng buộc như penalty terms
2. **Tạo cận dưới:** Hàm dual luôn cung cấp lower bound cho bài toán gốc
3. **Đảm bảo tính lồi:** Bài toán dual luôn lồi, dễ giải hơn
4. **Kết nối với hình học:** Hàm liên hợp cung cấp góc nhìn hình học trực quan

### 🔍 Ý nghĩa thực tiễn

- **Thuật toán:** Nhiều thuật toán tối ưu hiện đại dựa trên duality
- **Phân tích độ nhạy:** Dual variables cho biết "giá" của việc thay đổi ràng buộc  
- **Kiểm tra tối ưu:** Duality gap giúp đánh giá chất lượng nghiệm
- **Thiết kế thuật toán:** Primal-dual methods kết hợp cả hai quan điểm

Lagrange Duality không chỉ là một công cụ toán học trừu tượng, mà là một framework mạnh mẽ giúp chúng ta hiểu sâu hơn về bản chất của các bài toán tối ưu và thiết kế các thuật toán hiệu quả để giải chúng.

## 🖼️ Ghi chú về hình ảnh

Các hình ảnh trong bài học này được lấy cảm hứng và tham khảo từ bài viết gốc của Zhiliang Zhou. Các visualization tương tác được tạo bằng JavaScript để bổ sung và làm rõ hơn các khái niệm được trình bày trong bài gốc.

## 📚 Tài liệu tham khảo

1. "Convex Optimization" - Stephen Boyd & Lieven Vandenberghe
2. [Intuition behind Lagrange Duality](https://masszhou.github.io/2016/09/10/Lagrange-Duality/) - Zhiliang Zhou's Blog
3. [Zhiliang's Blog and Notes](https://masszhou.github.io/) - Another External Brain Drive
4. Các chương trước trong khóa học về Linear Programming Duality và General Duality
5. Boyd, S., & Vandenberghe, L. (2004). Convex optimization. Cambridge University Press
6. Rockafellar, R. T. (1970). Convex analysis. Princeton University Press
