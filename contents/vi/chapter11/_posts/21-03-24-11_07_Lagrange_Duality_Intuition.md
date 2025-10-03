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

<div id="lagrangian-visualization" style="margin: 20px 0; padding: 20px; background: #f8f9fa; border-radius: 10px;">
    <canvas id="lagrangianCanvas" width="900" height="500" style="border: 2px solid #dee2e6; display: block; margin: 0 auto; background: white; border-radius: 5px;"></canvas>
    <div style="text-align: center; margin: 15px 0;">
        <div style="display: inline-block; padding: 10px 20px; background: white; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <label style="font-size: 18px; font-weight: bold;">λ = <span id="lambdaValue" style="color: #007bff;">0.0</span></label><br>
            <input type="range" id="lambdaSlider" min="0" max="4" step="0.05" value="0" style="width: 400px; margin-top: 10px;">
            <div style="margin-top: 10px; font-size: 14px; color: #666;">
                <span>Kéo thanh trượt để thay đổi hệ số Lagrange</span>
            </div>
        </div>
    </div>
    <div id="lagrangianInfo" style="text-align: center; margin-top: 15px; padding: 10px; background: white; border-radius: 5px;">
        <p style="margin: 5px 0; font-size: 16px;"><strong>Giá trị dual:</strong> <span id="dualValue" style="color: #28a745; font-weight: bold;">g(0) = 0</span></p>
        <p style="margin: 5px 0; font-size: 14px; color: #666;"><span id="lowerBoundInfo">Cận dưới của bài toán</span></p>
    </div>
</div>

<script>
(function() {
    // Wait for DOM to be ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initLagrangianViz);
    } else {
        initLagrangianViz();
    }
    
    function initLagrangianViz() {
    const canvas = document.getElementById('lagrangianCanvas');
        if (!canvas) return;
        
    const ctx = canvas.getContext('2d');
    const slider = document.getElementById('lambdaSlider');
    const valueSpan = document.getElementById('lambdaValue');
        const dualValueSpan = document.getElementById('dualValue');
        const lowerBoundInfo = document.getElementById('lowerBoundInfo');
        
        // Animation state
        let animationFrame = null;
        
        function drawGrid(centerX, centerY, scale) {
            ctx.strokeStyle = '#e9ecef';
            ctx.lineWidth = 1;
            ctx.setLineDash([2, 2]);
            
            // Vertical grid lines
            for (let x = -8; x <= 8; x++) {
                if (x === 0) continue;
                const screenX = centerX + x * scale;
                ctx.beginPath();
                ctx.moveTo(screenX, 0);
                ctx.lineTo(screenX, canvas.height);
                ctx.stroke();
            }
            
            // Horizontal grid lines
            for (let y = -4; y <= 4; y++) {
                if (y === 0) continue;
                const screenY = centerY - y * scale;
                ctx.beginPath();
                ctx.moveTo(0, screenY);
                ctx.lineTo(canvas.width, screenY);
                ctx.stroke();
            }
            
            ctx.setLineDash([]);
        }
        
        function drawAxes(centerX, centerY, scale) {
            // Draw axes
            ctx.strokeStyle = '#495057';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(0, centerY);
            ctx.lineTo(canvas.width, centerY);
            ctx.moveTo(centerX, 0);
            ctx.lineTo(centerX, canvas.height);
            ctx.stroke();
            
            // Draw axis labels
            ctx.fillStyle = '#495057';
            ctx.font = 'bold 14px Arial';
            ctx.textAlign = 'center';
            
            // X-axis labels
            for (let x = -8; x <= 8; x += 2) {
                if (x === 0) continue;
                const screenX = centerX + x * scale;
                ctx.fillText(x.toString(), screenX, centerY + 20);
            }
            
            // Y-axis labels
            ctx.textAlign = 'right';
            for (let y = -4; y <= 4; y += 2) {
                if (y === 0) continue;
                const screenY = centerY - y * scale;
                ctx.fillText(y.toString(), centerX - 10, screenY + 5);
            }
            
            // Axis names
            ctx.font = 'bold 16px Arial';
            ctx.textAlign = 'center';
            ctx.fillText('x', canvas.width - 20, centerY - 10);
            ctx.textAlign = 'left';
            ctx.fillText('y', centerX + 10, 20);
        }
    
    function drawVisualization() {
        const lambda = parseFloat(slider.value);
            valueSpan.textContent = lambda.toFixed(2);
        
        // Clear canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Set up coordinate system
        const centerX = canvas.width / 2;
            const centerY = canvas.height * 0.6;
        const scale = 50;
            
            // Draw grid
            drawGrid(centerX, centerY, scale);
        
        // Draw axes
            drawAxes(centerX, centerY, scale);
        
        // Draw original function f(x) = x^2
            ctx.strokeStyle = '#212529';
            ctx.lineWidth = 3;
        ctx.beginPath();
        let first = true;
            for (let x = -8; x <= 8; x += 0.05) {
                const y = x * x;
            const screenX = centerX + x * scale;
                const screenY = centerY - y * scale / 4;
                if (screenY >= 0 && screenY <= canvas.height && screenX >= 0 && screenX <= canvas.width) {
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
            if (lambda > 0.01) {
                ctx.strokeStyle = '#007bff';
                ctx.lineWidth = 3;
            ctx.beginPath();
            first = true;
                for (let x = -8; x <= 8; x += 0.05) {
                const lagrangian = x * x + lambda * (x - 1);
                const screenX = centerX + x * scale;
                const screenY = centerY - lagrangian * scale / 4;
                    if (screenY >= -50 && screenY <= canvas.height + 50 && screenX >= 0 && screenX <= canvas.width) {
                    if (first) {
                        ctx.moveTo(screenX, screenY);
                        first = false;
                    } else {
                        ctx.lineTo(screenX, screenY);
                    }
                }
            }
            ctx.stroke();
            
                // Calculate minimum point
            const minX = -lambda / 2;
            const minY = -lambda * lambda / 4 - lambda;
            const screenMinX = centerX + minX * scale;
            const screenMinY = centerY - minY * scale / 4;
            
                // Draw vertical line from minimum to x-axis
            if (screenMinY >= 0 && screenMinY <= canvas.height) {
                    ctx.strokeStyle = '#007bff';
                    ctx.lineWidth = 1;
                    ctx.setLineDash([3, 3]);
                ctx.beginPath();
                    ctx.moveTo(screenMinX, screenMinY);
                    ctx.lineTo(screenMinX, centerY);
                    ctx.stroke();
                    ctx.setLineDash([]);
                    
                    // Mark minimum point with glow effect
                    ctx.shadowBlur = 10;
                    ctx.shadowColor = '#007bff';
                    ctx.fillStyle = '#007bff';
                    ctx.beginPath();
                    ctx.arc(screenMinX, screenMinY, 7, 0, 2 * Math.PI);
                ctx.fill();
                    ctx.shadowBlur = 0;
                    
                    // Add label for minimum
                    ctx.fillStyle = '#007bff';
                    ctx.font = 'bold 13px Arial';
                    ctx.textAlign = 'center';
                    ctx.fillText(`x* = ${minX.toFixed(2)}`, screenMinX, centerY + 35);
                    ctx.fillText(`g(λ) = ${minY.toFixed(2)}`, screenMinX, screenMinY - 15);
                }
                
                // Update dual value display
                dualValueSpan.textContent = `g(${lambda.toFixed(2)}) = ${minY.toFixed(3)}`;
                
                // Update lower bound info
                if (minY <= 1) {
                    lowerBoundInfo.textContent = `✓ g(λ) = ${minY.toFixed(3)} ≤ p* = 1 (cận dưới hợp lệ)`;
                    lowerBoundInfo.style.color = '#28a745';
                } else {
                    lowerBoundInfo.textContent = `⚠ Cận dưới không chặt`;
                    lowerBoundInfo.style.color = '#ffc107';
                }
            } else {
                dualValueSpan.textContent = 'g(0) = 0';
                lowerBoundInfo.textContent = 'Kéo thanh trượt để thấy hàm Lagrangian';
                lowerBoundInfo.style.color = '#666';
        }
        
        // Draw constraint boundary x = 1
            ctx.strokeStyle = '#dc3545';
            ctx.lineWidth = 3;
            ctx.setLineDash([8, 4]);
        ctx.beginPath();
        ctx.moveTo(centerX + scale, 0);
        ctx.lineTo(centerX + scale, canvas.height);
        ctx.stroke();
        ctx.setLineDash([]);
        
            // Mark optimal point (x=1, f(1)=1)
            const optX = 1;
            const optY = 1;
            const screenOptX = centerX + optX * scale;
            const screenOptY = centerY - optY * scale / 4;
            
            ctx.shadowBlur = 15;
            ctx.shadowColor = '#dc3545';
            ctx.fillStyle = '#dc3545';
        ctx.beginPath();
            ctx.arc(screenOptX, screenOptY, 8, 0, 2 * Math.PI);
        ctx.fill();
            ctx.shadowBlur = 0;
            
            // Draw legend box
            const legendX = 20;
            const legendY = 20;
            const legendWidth = 250;
            const legendHeight = 115;
            
            ctx.fillStyle = 'rgba(255, 255, 255, 0.95)';
            ctx.strokeStyle = '#dee2e6';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.roundRect(legendX, legendY, legendWidth, legendHeight, 5);
            ctx.fill();
            ctx.stroke();
            
            // Legend content
            let yPos = legendY + 25;
            ctx.textAlign = 'left';
            
            // Original function
            ctx.strokeStyle = '#212529';
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.moveTo(legendX + 10, yPos);
            ctx.lineTo(legendX + 40, yPos);
            ctx.stroke();
            ctx.fillStyle = '#212529';
        ctx.font = '14px Arial';
            ctx.fillText('f(x) = x²', legendX + 50, yPos + 5);
            
            yPos += 25;
            
            // Lagrangian
            if (lambda > 0.01) {
                ctx.strokeStyle = '#007bff';
                ctx.lineWidth = 3;
                ctx.beginPath();
                ctx.moveTo(legendX + 10, yPos);
                ctx.lineTo(legendX + 40, yPos);
                ctx.stroke();
                ctx.fillStyle = '#007bff';
                ctx.fillText(`L(x,λ) = x² + λ(x-1)`, legendX + 50, yPos + 5);
                yPos += 25;
            }
            
            // Constraint
            ctx.strokeStyle = '#dc3545';
            ctx.lineWidth = 3;
            ctx.setLineDash([8, 4]);
            ctx.beginPath();
            ctx.moveTo(legendX + 10, yPos);
            ctx.lineTo(legendX + 40, yPos);
            ctx.stroke();
            ctx.setLineDash([]);
            ctx.fillStyle = '#dc3545';
            ctx.fillText('Ràng buộc: x ≤ 1', legendX + 50, yPos + 5);
            
            yPos += 25;
            
            // Optimal point
            ctx.fillStyle = '#dc3545';
            ctx.beginPath();
            ctx.arc(legendX + 25, yPos, 6, 0, 2 * Math.PI);
            ctx.fill();
            ctx.fillStyle = '#dc3545';
            ctx.fillText('Nghiệm tối ưu: p* = 1', legendX + 50, yPos + 5);
        }
        
        // Debounce function for smoother performance
        let debounceTimer;
        function debouncedDraw() {
            clearTimeout(debounceTimer);
            debounceTimer = setTimeout(drawVisualization, 10);
        }
        
        slider.addEventListener('input', debouncedDraw);
    drawVisualization();
    }
})();
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

<div id="dual-function-visualization" style="margin: 20px 0; padding: 20px; background: #f8f9fa; border-radius: 10px;">
    <canvas id="dualCanvas" width="800" height="450" style="border: 2px solid #dee2e6; display: block; margin: 0 auto; background: white; border-radius: 5px;"></canvas>
    <div style="text-align: center; margin-top: 15px;">
        <button id="animateSupremum" style="padding: 10px 25px; font-size: 16px; background: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
            ▶ Chạy Animation
        </button>
        <button id="resetSupremum" style="padding: 10px 25px; font-size: 16px; background: #6c757d; color: white; border: none; border-radius: 5px; cursor: pointer; margin-left: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.2);">
            🔄 Reset
        </button>
    </div>
    <div style="margin-top: 15px; padding: 15px; background: white; border-radius: 5px; border-left: 4px solid #007bff;">
        <p style="margin: 0; font-size: 14px; color: #666;">
            <strong>Giải thích:</strong> Hàm dual -g(λ) là supremum theo từng điểm của tập các hàm affine, 
            do đó nó là hàm lồi. Điều này có nghĩa là bài toán dual luôn lồi, bất kể bài toán gốc có lồi hay không.
        </p>
    </div>
</div>

<script>
(function() {
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initDualViz);
    } else {
        initDualViz();
    }
    
    function initDualViz() {
    const canvas = document.getElementById('dualCanvas');
        if (!canvas) return;
        
    const ctx = canvas.getContext('2d');
        const animateBtn = document.getElementById('animateSupremum');
        const resetBtn = document.getElementById('resetSupremum');
        
        let animationProgress = 0;
        let isAnimating = false;
        let animationId = null;
        
        const affineFunctions = [
            { a: -2, b: 3.5, color: '#ff6b6b', label: 'f₁' },
            { a: -1, b: 3, color: '#4ecdc4', label: 'f₂' },
            { a: 0, b: 2.5, color: '#45b7d1', label: 'f₃' },
            { a: 1, b: 2, color: '#96ceb4', label: 'f₄' },
            { a: 2, b: 1.5, color: '#ffeaa7', label: 'f₅' }
        ];
        
        function drawDualVisualization(progress = 1) {
        // Clear canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Set up coordinate system
            const margin = 80;
            const centerX = margin;
            const centerY = canvas.height - margin;
            const scaleX = (canvas.width - margin - 40) / 5;
            const scaleY = 60;
            
            // Draw grid
            ctx.strokeStyle = '#e9ecef';
        ctx.lineWidth = 1;
            ctx.setLineDash([2, 2]);
            for (let i = 0; i <= 5; i++) {
                const x = centerX + i * scaleX;
                ctx.beginPath();
                ctx.moveTo(x, 0);
                ctx.lineTo(x, centerY);
                ctx.stroke();
            }
            for (let i = -2; i <= 4; i++) {
                const y = centerY - i * scaleY;
                ctx.beginPath();
                ctx.moveTo(centerX, y);
                ctx.lineTo(canvas.width - 20, y);
                ctx.stroke();
            }
            ctx.setLineDash([]);
            
            // Draw axes
            ctx.strokeStyle = '#495057';
            ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(centerX, 0);
            ctx.lineTo(centerX, centerY);
            ctx.moveTo(centerX, centerY);
            ctx.lineTo(canvas.width - 20, centerY);
        ctx.stroke();
        
            // Draw axis labels
            ctx.fillStyle = '#495057';
            ctx.font = 'bold 14px Arial';
            ctx.textAlign = 'center';
            
            // X-axis labels
            for (let i = 0; i <= 5; i++) {
                const x = centerX + i * scaleX;
                ctx.fillText(i.toString(), x, centerY + 25);
            }
            
            // Y-axis labels
            ctx.textAlign = 'right';
            for (let i = -2; i <= 4; i++) {
                const y = centerY - i * scaleY;
                ctx.fillText(i.toString(), centerX - 10, y + 5);
            }
            
            // Axis names
            ctx.fillStyle = '#212529';
            ctx.font = 'bold 18px Arial';
            ctx.textAlign = 'center';
            ctx.fillText('λ', canvas.width - 10, centerY + 25);
            ctx.textAlign = 'left';
            ctx.fillText('-g(λ)', centerX - 50, 20);
            
            // Draw affine functions with animation
            const numFunctionsToShow = Math.ceil(progress * affineFunctions.length);
            
            for (let i = 0; i < numFunctionsToShow; i++) {
                const func = affineFunctions[i];
                const alpha = (i < numFunctionsToShow - 1) ? 1 : (progress * affineFunctions.length - i);
                
                ctx.strokeStyle = func.color;
                ctx.globalAlpha = alpha;
                ctx.lineWidth = 2;
            ctx.beginPath();
            
                let first = true;
                for (let lambda = 0; lambda <= 5; lambda += 0.05) {
                    const y = func.a * lambda + func.b;
                const screenX = centerX + lambda * scaleX;
                const screenY = centerY - y * scaleY;
                
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
                
                // Draw function label
                const labelX = centerX + 4.5 * scaleX;
                const labelY = centerY - (func.a * 4.5 + func.b) * scaleY;
                if (labelY >= 0 && labelY <= canvas.height) {
                    ctx.fillStyle = func.color;
                    ctx.font = 'bold 14px Arial';
                    ctx.textAlign = 'left';
                    ctx.fillText(func.label, labelX + 10, labelY + 5);
                }
            }
            
            ctx.globalAlpha = 1;
            
            // Draw pointwise supremum (envelope) if animation is complete
            if (progress >= 0.9) {
                const envelopeAlpha = (progress - 0.9) / 0.1;
                ctx.globalAlpha = envelopeAlpha;
                
                ctx.strokeStyle = '#dc3545';
                ctx.lineWidth = 4;
                ctx.shadowBlur = 10;
                ctx.shadowColor = '#dc3545';
        ctx.beginPath();
        
                let first = true;
                const supremumPoints = [];
                
                for (let lambda = 0; lambda <= 5; lambda += 0.02) {
            let maxY = -Infinity;
                    for (const func of affineFunctions) {
                        const y = func.a * lambda + func.b;
                maxY = Math.max(maxY, y);
            }
                    
                    supremumPoints.push({ lambda, y: maxY });
            
            const screenX = centerX + lambda * scaleX;
            const screenY = centerY - maxY * scaleY;
            
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
                ctx.shadowBlur = 0;
                
                // Highlight some key points on the envelope
                if (envelopeAlpha > 0.5) {
                    const keyLambdas = [0.5, 1.5, 2.5, 3.5, 4.5];
                    for (const lambda of keyLambdas) {
                        let maxY = -Infinity;
                        for (const func of affineFunctions) {
                            const y = func.a * lambda + func.b;
                            maxY = Math.max(maxY, y);
                        }
                        
                        const screenX = centerX + lambda * scaleX;
                        const screenY = centerY - maxY * scaleY;
                        
                        if (screenY >= 0 && screenY <= canvas.height) {
                            ctx.fillStyle = '#dc3545';
                            ctx.beginPath();
                            ctx.arc(screenX, screenY, 5, 0, 2 * Math.PI);
                            ctx.fill();
                        }
                    }
                }
                
                ctx.globalAlpha = 1;
                
                // Add annotation
                ctx.fillStyle = '#dc3545';
                ctx.font = 'bold 16px Arial';
                ctx.textAlign = 'left';
                ctx.fillText('Supremum theo từng điểm', 200, 30);
        ctx.font = '14px Arial';
                ctx.fillText('(Đường bao lồi)', 200, 50);
            }
            
            // Draw legend
            const legendX = canvas.width - 180;
            const legendY = 80;
            const legendWidth = 160;
            const legendHeight = 80;
            
            ctx.fillStyle = 'rgba(255, 255, 255, 0.95)';
            ctx.strokeStyle = '#dee2e6';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.roundRect(legendX, legendY, legendWidth, legendHeight, 5);
            ctx.fill();
            ctx.stroke();
            
            // Legend title
            ctx.fillStyle = '#212529';
            ctx.font = 'bold 14px Arial';
            ctx.textAlign = 'center';
            ctx.fillText('Hàm Affine', legendX + legendWidth/2, legendY + 20);
            
            // Legend items
            ctx.font = '12px Arial';
            ctx.textAlign = 'left';
            for (let i = 0; i < Math.min(3, numFunctionsToShow); i++) {
                const func = affineFunctions[i];
                const yPos = legendY + 40 + i * 15;
                
                ctx.strokeStyle = func.color;
                ctx.lineWidth = 2;
                ctx.beginPath();
                ctx.moveTo(legendX + 10, yPos);
                ctx.lineTo(legendX + 30, yPos);
                ctx.stroke();
                
                ctx.fillStyle = '#495057';
                ctx.fillText(`${func.a}λ + ${func.b}`, legendX + 35, yPos + 4);
            }
        }
        
        function animate() {
            if (!isAnimating) return;
            
            animationProgress += 0.008;
            if (animationProgress >= 1) {
                animationProgress = 1;
                isAnimating = false;
                animateBtn.innerHTML = '▶ Chạy Lại';
                animateBtn.style.background = '#28a745';
            }
            
            drawDualVisualization(animationProgress);
            
            if (isAnimating) {
                animationId = requestAnimationFrame(animate);
            }
        }
        
        animateBtn.addEventListener('click', function() {
            if (animationProgress >= 1) {
                animationProgress = 0;
            }
            
            if (isAnimating) {
                isAnimating = false;
                if (animationId) cancelAnimationFrame(animationId);
                animateBtn.innerHTML = '▶ Tiếp Tục';
                animateBtn.style.background = '#007bff';
            } else {
                isAnimating = true;
                animateBtn.innerHTML = '⏸ Tạm Dừng';
                animateBtn.style.background = '#ffc107';
                animate();
            }
        });
        
        resetBtn.addEventListener('click', function() {
            isAnimating = false;
            if (animationId) cancelAnimationFrame(animationId);
            animationProgress = 0;
            animateBtn.innerHTML = '▶ Chạy Animation';
            animateBtn.style.background = '#007bff';
            drawDualVisualization(0);
        });
        
        // Initial draw
        drawDualVisualization(1);
    }
})();
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

<div id="conjugate-visualization" style="margin: 20px 0; padding: 20px; background: #f8f9fa; border-radius: 10px;">
    <canvas id="conjugateCanvas" width="900" height="550" style="border: 2px solid #dee2e6; display: block; margin: 0 auto; background: white; border-radius: 5px;"></canvas>
    <div style="text-align: center; margin: 15px 0;">
        <div style="display: inline-block; padding: 10px 20px; background: white; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <label style="font-size: 18px; font-weight: bold;">Độ dốc λ = <span id="slopeValue" style="color: #6f42c1;">1.0</span></label><br>
            <input type="range" id="slopeSlider" min="-4" max="4" step="0.05" value="1" style="width: 400px; margin-top: 10px;">
            <div style="margin-top: 10px; font-size: 14px; color: #666;">
                <span>Thay đổi độ dốc của đường thẳng λx</span>
            </div>
        </div>
    </div>
    <div id="conjugateInfo" style="text-align: center; margin-top: 15px; padding: 15px; background: white; border-radius: 5px; border-left: 4px solid #6f42c1;">
        <p style="margin: 5px 0; font-size: 16px;"><strong>Hàm liên hợp:</strong> <span id="conjugateValue" style="color: #6f42c1; font-weight: bold;">f*(1.0) = 0.50</span></p>
        <p style="margin: 5px 0; font-size: 14px; color: #666;"><span id="conjugateExplanation">Khoảng cách lớn nhất giữa λx và f(x)</span></p>
    </div>
</div>

<script>
(function() {
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initConjugateViz);
    } else {
        initConjugateViz();
    }
    
    function initConjugateViz() {
    const canvas = document.getElementById('conjugateCanvas');
        if (!canvas) return;
        
    const ctx = canvas.getContext('2d');
    const slider = document.getElementById('slopeSlider');
    const valueSpan = document.getElementById('slopeValue');
        const conjugateValueSpan = document.getElementById('conjugateValue');
        const explanationSpan = document.getElementById('conjugateExplanation');
        
        function drawGrid(centerX, centerY, scale) {
            ctx.strokeStyle = '#f1f3f5';
            ctx.lineWidth = 1;
            ctx.setLineDash([2, 2]);
            
            // Vertical grid
            for (let x = -10; x <= 10; x++) {
                if (x === 0) continue;
                const screenX = centerX + x * scale;
                if (screenX >= 0 && screenX <= canvas.width) {
                    ctx.beginPath();
                    ctx.moveTo(screenX, 0);
                    ctx.lineTo(screenX, canvas.height);
                    ctx.stroke();
                }
            }
            
            // Horizontal grid
            for (let y = -5; y <= 15; y++) {
                if (y === 0) continue;
                const screenY = centerY - y * scale;
                if (screenY >= 0 && screenY <= canvas.height) {
                    ctx.beginPath();
                    ctx.moveTo(0, screenY);
                    ctx.lineTo(canvas.width, screenY);
                    ctx.stroke();
                }
            }
            
            ctx.setLineDash([]);
        }
        
        function drawAxes(centerX, centerY, scale) {
            // Axes
            ctx.strokeStyle = '#495057';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(0, centerY);
            ctx.lineTo(canvas.width, centerY);
            ctx.moveTo(centerX, 0);
            ctx.lineTo(centerX, canvas.height);
            ctx.stroke();
            
            // Axis labels
            ctx.fillStyle = '#495057';
            ctx.font = 'bold 13px Arial';
            ctx.textAlign = 'center';
            
            // X-axis
            for (let x = -10; x <= 10; x += 2) {
                if (x === 0) continue;
                const screenX = centerX + x * scale;
                if (screenX >= 0 && screenX <= canvas.width) {
                    ctx.fillText(x.toString(), screenX, centerY + 20);
                }
            }
            
            // Y-axis
            ctx.textAlign = 'right';
            for (let y = -4; y <= 14; y += 2) {
                if (y === 0) continue;
                const screenY = centerY - y * scale;
                if (screenY >= 0 && screenY <= canvas.height) {
                    ctx.fillText(y.toString(), centerX - 10, screenY + 5);
                }
            }
            
            // Axis names
            ctx.font = 'bold 16px Arial';
            ctx.textAlign = 'center';
            ctx.fillText('x', canvas.width - 20, centerY - 10);
            ctx.textAlign = 'left';
            ctx.fillText('y', centerX + 10, 20);
        }
    
    function drawConjugateVisualization() {
        const slope = parseFloat(slider.value);
            valueSpan.textContent = slope.toFixed(2);
        
        // Clear canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Set up coordinate system
        const centerX = canvas.width / 2;
            const centerY = canvas.height * 0.75;
            const scale = 35;
            
            // Draw grid
            drawGrid(centerX, centerY, scale);
        
        // Draw axes
            drawAxes(centerX, centerY, scale);
        
        // Draw function f(x) = x^2/2
            ctx.strokeStyle = '#20c997';
            ctx.lineWidth = 4;
            ctx.shadowBlur = 5;
            ctx.shadowColor = '#20c997';
        ctx.beginPath();
        let first = true;
            for (let x = -10; x <= 10; x += 0.05) {
            const y = x * x / 2;
            const screenX = centerX + x * scale;
            const screenY = centerY - y * scale;
                if (screenY >= -10 && screenY <= canvas.height && screenX >= 0 && screenX <= canvas.width) {
                if (first) {
                    ctx.moveTo(screenX, screenY);
                    first = false;
                } else {
                    ctx.lineTo(screenX, screenY);
                }
            }
        }
        ctx.stroke();
            ctx.shadowBlur = 0;
        
        // Draw line λx with given slope
            ctx.strokeStyle = '#6f42c1';
            ctx.lineWidth = 3;
        ctx.beginPath();
            first = true;
            for (let x = -10; x <= 10; x += 0.1) {
            const y = slope * x;
            const screenX = centerX + x * scale;
            const screenY = centerY - y * scale;
                if (screenY >= -10 && screenY <= canvas.height + 10 && screenX >= -10 && screenX <= canvas.width + 10) {
                    if (first) {
                    ctx.moveTo(screenX, screenY);
                        first = false;
                } else {
                    ctx.lineTo(screenX, screenY);
                }
            }
        }
        ctx.stroke();
        
        // Find and mark the point where λx - f(x) is maximized
        let maxDiff = -Infinity;
        let maxX = 0;
            for (let x = -10; x <= 10; x += 0.01) {
            const diff = slope * x - x * x / 2;
            if (diff > maxDiff) {
                maxDiff = diff;
                maxX = x;
            }
        }
        
            const conjugateValue = slope * slope / 2;
            
            // Draw tangent line at optimal point (parallel to λx)
            ctx.strokeStyle = '#fd7e14';
            ctx.lineWidth = 3;
            ctx.setLineDash([8, 4]);
            ctx.shadowBlur = 5;
            ctx.shadowColor = '#fd7e14';
            ctx.beginPath();
            first = true;
            for (let x = -10; x <= 10; x += 0.1) {
                const y = slope * x - conjugateValue;
            const screenX = centerX + x * scale;
            const screenY = centerY - y * scale;
                if (screenY >= -10 && screenY <= canvas.height + 10 && screenX >= -10 && screenX <= canvas.width + 10) {
                    if (first) {
                    ctx.moveTo(screenX, screenY);
                        first = false;
                } else {
                    ctx.lineTo(screenX, screenY);
                }
            }
        }
        ctx.stroke();
        ctx.setLineDash([]);
            ctx.shadowBlur = 0;
            
            // Mark tangent point on f(x)
            const tangentY = maxX * maxX / 2;
            const tangentScreenX = centerX + maxX * scale;
            const tangentScreenY = centerY - tangentY * scale;
            
            if (tangentScreenY >= 0 && tangentScreenY <= canvas.height) {
                // Draw vertical line to show the contact point
                ctx.strokeStyle = '#e63946';
                ctx.lineWidth = 2;
                ctx.setLineDash([3, 3]);
        ctx.beginPath();
                ctx.moveTo(tangentScreenX, tangentScreenY);
                ctx.lineTo(tangentScreenX, centerY);
                ctx.stroke();
                ctx.setLineDash([]);
                
                // Mark point with glow
                ctx.shadowBlur = 15;
                ctx.shadowColor = '#e63946';
                ctx.fillStyle = '#e63946';
                ctx.beginPath();
                ctx.arc(tangentScreenX, tangentScreenY, 8, 0, 2 * Math.PI);
        ctx.fill();
                ctx.shadowBlur = 0;
                
                // Label the contact point
                ctx.fillStyle = '#e63946';
                ctx.font = 'bold 14px Arial';
                ctx.textAlign = 'center';
                ctx.fillText(`x* = ${maxX.toFixed(2)}`, tangentScreenX, centerY + 35);
            }
            
            // Draw vertical distance visualization (f*(λ))
            if (Math.abs(maxX) <= 10 && tangentScreenY >= 0) {
                const lineY = slope * maxX;
                const lineScreenY = centerY - lineY * scale;
                
                if (lineScreenY >= 0 && lineScreenY <= canvas.height) {
                    // Draw vertical arrow showing the distance
                    ctx.strokeStyle = '#6f42c1';
                    ctx.fillStyle = '#6f42c1';
                    ctx.lineWidth = 3;
                    
                    // Draw arrow
                    const arrowX = tangentScreenX + 50;
                    ctx.beginPath();
                    ctx.moveTo(arrowX, tangentScreenY);
                    ctx.lineTo(arrowX, lineScreenY);
                    ctx.stroke();
                    
                    // Arrowheads
                    ctx.beginPath();
                    ctx.moveTo(arrowX - 5, tangentScreenY + 10);
                    ctx.lineTo(arrowX, tangentScreenY);
                    ctx.lineTo(arrowX + 5, tangentScreenY + 10);
                    ctx.fill();
                    
                    ctx.beginPath();
                    ctx.moveTo(arrowX - 5, lineScreenY - 10);
                    ctx.lineTo(arrowX, lineScreenY);
                    ctx.lineTo(arrowX + 5, lineScreenY - 10);
                    ctx.fill();
                    
                    // Label the distance
                    const midY = (tangentScreenY + lineScreenY) / 2;
                    ctx.font = 'bold 14px Arial';
                    ctx.textAlign = 'left';
                    ctx.fillText(`f*(λ) = ${conjugateValue.toFixed(2)}`, arrowX + 10, midY + 5);
                }
            }
            
            // Update info display
            conjugateValueSpan.textContent = `f*(${slope.toFixed(2)}) = ${conjugateValue.toFixed(3)}`;
            explanationSpan.textContent = `Tại x* = ${maxX.toFixed(2)}, khoảng cách λx - f(x) đạt cực đại = ${conjugateValue.toFixed(3)}`;
            
            // Draw legend box
            const legendX = 20;
            const legendY = 20;
            const legendWidth = 280;
            const legendHeight = 135;
            
            ctx.fillStyle = 'rgba(255, 255, 255, 0.95)';
            ctx.strokeStyle = '#dee2e6';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.roundRect(legendX, legendY, legendWidth, legendHeight, 5);
            ctx.fill();
            ctx.stroke();
            
            // Legend content
            let yPos = legendY + 25;
            ctx.textAlign = 'left';
            
            // f(x)
            ctx.strokeStyle = '#20c997';
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.moveTo(legendX + 10, yPos);
            ctx.lineTo(legendX + 45, yPos);
            ctx.stroke();
            ctx.fillStyle = '#20c997';
            ctx.font = '15px Arial';
            ctx.fillText('f(x) = x²/2', legendX + 55, yPos + 5);
            yPos += 28;
            
            // λx
            ctx.strokeStyle = '#6f42c1';
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.moveTo(legendX + 10, yPos);
            ctx.lineTo(legendX + 45, yPos);
            ctx.stroke();
            ctx.fillStyle = '#6f42c1';
            ctx.fillText(`λx (λ = ${slope.toFixed(2)})`, legendX + 55, yPos + 5);
            yPos += 28;
            
            // Tangent
            ctx.strokeStyle = '#fd7e14';
            ctx.lineWidth = 3;
            ctx.setLineDash([8, 4]);
            ctx.beginPath();
            ctx.moveTo(legendX + 10, yPos);
            ctx.lineTo(legendX + 45, yPos);
            ctx.stroke();
            ctx.setLineDash([]);
            ctx.fillStyle = '#fd7e14';
            ctx.fillText('Đường tiếp xúc', legendX + 55, yPos + 5);
            yPos += 28;
            
            // Contact point
            ctx.fillStyle = '#e63946';
            ctx.beginPath();
            ctx.arc(legendX + 27, yPos - 3, 6, 0, 2 * Math.PI);
            ctx.fill();
            ctx.fillStyle = '#e63946';
            ctx.fillText('Điểm tiếp xúc', legendX + 55, yPos + 2);
        }
        
        // Debounce for performance
        let debounceTimer;
        function debouncedDraw() {
            clearTimeout(debounceTimer);
            debounceTimer = setTimeout(drawConjugateVisualization, 5);
        }
        
        slider.addEventListener('input', debouncedDraw);
    drawConjugateVisualization();
    }
})();
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

<div id="complete-example" style="margin: 20px 0; padding: 25px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
    <h4 style="color: white; text-align: center; margin-bottom: 20px; font-size: 22px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">🎬 Minh họa Tổng hợp: Primal-Dual Relationship</h4>
    <canvas id="completeCanvas" width="1100" height="600" style="border: 3px solid white; display: block; margin: 0 auto; background: white; border-radius: 8px; box-shadow: 0 5px 15px rgba(0,0,0,0.3);"></canvas>
    <div style="text-align: center; margin: 20px 0;">
        <button id="animateBtn" style="padding: 12px 30px; font-size: 17px; background: #28a745; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; box-shadow: 0 4px 6px rgba(0,0,0,0.2); transition: all 0.3s;">
            ▶ Chạy Animation
        </button>
        <button id="resetBtn" style="padding: 12px 30px; font-size: 17px; background: #6c757d; color: white; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; margin-left: 15px; box-shadow: 0 4px 6px rgba(0,0,0,0.2); transition: all 0.3s;">
            🔄 Reset
        </button>
        <div style="margin-top: 15px; padding: 10px 20px; background: rgba(255,255,255,0.9); border-radius: 8px; display: inline-block;">
            <span style="font-size: 18px; font-weight: bold; color: #495057;">λ = <span id="currentLambdaDisplay" style="color: #007bff;">0.00</span></span>
            <span style="margin: 0 15px; color: #dee2e6;">|</span>
            <span style="font-size: 18px; font-weight: bold; color: #495057;">g(λ) = <span id="currentDualDisplay" style="color: #dc3545;">0.000</span></span>
    </div>
    </div>
    <div id="explanation" style="margin-top: 20px; padding: 20px; background: rgba(255,255,255,0.95); border-radius: 10px; box-shadow: 0 3px 10px rgba(0,0,0,0.2);">
        <p style="margin: 0 0 15px 0; font-size: 16px; font-weight: bold; color: #495057;">📖 Hướng dẫn đọc biểu đồ:</p>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 15px; font-size: 14px; line-height: 1.8;">
            <div style="padding: 10px; background: #f8f9fa; border-radius: 5px; border-left: 4px solid #212529;">
                <span style="color: #212529; font-weight: bold;">● Đường đen đậm:</span> Hàm mục tiêu f(x) = x²
            </div>
            <div style="padding: 10px; background: #f8f9fa; border-radius: 5px; border-left: 4px solid #007bff;">
                <span style="color: #007bff; font-weight: bold;">● Đường xanh dương:</span> Hàm Lagrangian L(x,λ)
            </div>
            <div style="padding: 10px; background: #f8f9fa; border-radius: 5px; border-left: 4px solid #dc3545;">
                <span style="color: #dc3545; font-weight: bold;">⊥ Đường đỏ đứt:</span> Ràng buộc x ≤ 1
            </div>
            <div style="padding: 10px; background: #f8f9fa; border-radius: 5px; border-left: 4px solid #ff0000;">
                <span style="color: #ff0000; font-weight: bold;">◉ Điểm đỏ lớn:</span> Nghiệm tối ưu p* = 1
            </div>
            <div style="padding: 10px; background: #f8f9fa; border-radius: 5px; border-left: 4px solid #007bff;">
                <span style="color: #007bff; font-weight: bold;">◉ Điểm xanh:</span> Min của L(x,λ) → g(λ)
            </div>
            <div style="padding: 10px; background: #f8f9fa; border-radius: 5px; border-left: 4px solid #28a745;">
                <span style="color: #28a745; font-weight: bold;">📊 Đường cong phải:</span> Hàm dual g(λ)
            </div>
        </div>
        <div style="margin-top: 15px; padding: 12px; background: #fff3cd; border-left: 4px solid #ffc107; border-radius: 5px;">
            <p style="margin: 0; color: #856404; font-size: 14px;">
                <strong>💡 Quan sát chính:</strong> Khi λ tăng, điểm minimum của Lagrangian (xanh) di chuyển sang trái, 
                và giá trị g(λ) giảm xuống (cận dưới chặt hơn). Giá trị lớn nhất của g(λ) cho ta nghiệm dual tốt nhất!
            </p>
        </div>
    </div>
</div>

<script>
(function() {
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initCompleteViz);
    } else {
        initCompleteViz();
    }
    
    function initCompleteViz() {
    const canvas = document.getElementById('completeCanvas');
        if (!canvas) return;
        
    const ctx = canvas.getContext('2d');
    const animateBtn = document.getElementById('animateBtn');
    const resetBtn = document.getElementById('resetBtn');
        const lambdaDisplay = document.getElementById('currentLambdaDisplay');
        const dualDisplay = document.getElementById('currentDualDisplay');
    
    let animationId = null;
    let currentLambda = 0;
    let isAnimating = false;
    
    function drawCompleteExample(lambda) {
        // Clear canvas
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
            // Set up panels
            const leftPanel = { x: 60, y: 60, width: 500, height: 450 };
            const rightPanel = { x: 600, y: 60, width: 450, height: 450 };
            
            // Draw panel backgrounds
            ctx.fillStyle = '#f8f9fa';
            ctx.fillRect(leftPanel.x - 10, leftPanel.y - 10, leftPanel.width + 20, leftPanel.height + 20);
            ctx.fillRect(rightPanel.x - 10, rightPanel.y - 10, rightPanel.width + 20, rightPanel.height + 20);
            
            // Draw panels
            drawPrimalSpace(leftPanel, lambda);
        drawDualSpace(rightPanel, lambda);
        
            // Add panel titles
            ctx.fillStyle = '#212529';
            ctx.font = 'bold 20px Arial';
            ctx.textAlign = 'center';
            ctx.fillText('Không Gian Primal', leftPanel.x + leftPanel.width/2, leftPanel.y - 25);
            ctx.fillText('Không Gian Dual', rightPanel.x + rightPanel.width/2, rightPanel.y - 25);
            
            // Update displays
            lambdaDisplay.textContent = lambda.toFixed(2);
        const dualValue = -lambda * lambda / 4 - lambda;
            dualDisplay.textContent = dualValue.toFixed(3);
    }
    
    function drawPrimalSpace(panel, lambda) {
        const centerX = panel.x + panel.width / 2;
            const centerY = panel.y + panel.height - 70;
            const scale = 50;
        
            // Draw grid
            ctx.strokeStyle = '#e9ecef';
        ctx.lineWidth = 1;
            ctx.setLineDash([2, 2]);
            for (let x = -4; x <= 4; x++) {
                if (x === 0) continue;
                const screenX = centerX + x * scale;
                ctx.beginPath();
                ctx.moveTo(screenX, panel.y);
                ctx.lineTo(screenX, panel.y + panel.height);
                ctx.stroke();
            }
            for (let y = -2; y <= 6; y++) {
                if (y === 0) continue;
                const screenY = centerY - y * scale / 2;
                ctx.beginPath();
                ctx.moveTo(panel.x, screenY);
                ctx.lineTo(panel.x + panel.width, screenY);
                ctx.stroke();
            }
            ctx.setLineDash([]);
            
            // Draw axes
            ctx.strokeStyle = '#495057';
            ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(panel.x, centerY);
        ctx.lineTo(panel.x + panel.width, centerY);
        ctx.moveTo(centerX, panel.y);
        ctx.lineTo(centerX, panel.y + panel.height);
        ctx.stroke();
            
            // Axis labels
            ctx.fillStyle = '#495057';
            ctx.font = 'bold 13px Arial';
            ctx.textAlign = 'center';
            for (let x = -4; x <= 4; x += 2) {
                if (x === 0) continue;
                ctx.fillText(x.toString(), centerX + x * scale, centerY + 20);
            }
            ctx.font = 'bold 16px Arial';
            ctx.fillText('x', panel.x + panel.width - 15, centerY - 10);
            ctx.fillText('y', centerX + 15, panel.y + 20);
        
        // Draw original function f(x) = x^2
            ctx.strokeStyle = '#212529';
            ctx.lineWidth = 4;
            ctx.shadowBlur = 5;
            ctx.shadowColor = '#212529';
        ctx.beginPath();
        let first = true;
            for (let x = -4; x <= 4; x += 0.05) {
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
            ctx.shadowBlur = 0;
        
        // Draw Lagrangian if lambda > 0
            if (lambda > 0.01) {
                ctx.strokeStyle = '#007bff';
                ctx.lineWidth = 3;
                ctx.shadowBlur = 5;
                ctx.shadowColor = '#007bff';
            ctx.beginPath();
            first = true;
                for (let x = -4; x <= 4; x += 0.05) {
                const lagrangian = x * x + lambda * (x - 1);
                const screenX = centerX + x * scale;
                const screenY = centerY - lagrangian * scale / 2;
                    if (screenY >= panel.y - 20 && screenY <= panel.y + panel.height + 20) {
                    if (first) {
                        ctx.moveTo(screenX, screenY);
                        first = false;
                    } else {
                        ctx.lineTo(screenX, screenY);
                    }
                }
            }
            ctx.stroke();
                ctx.shadowBlur = 0;
            
            // Mark minimum of Lagrangian
            const minX = -lambda / 2;
            const minY = -lambda * lambda / 4 - lambda;
            const screenMinX = centerX + minX * scale;
            const screenMinY = centerY - minY * scale / 2;
            
            if (screenMinY >= panel.y && screenMinY <= panel.y + panel.height) {
                    // Vertical line to axis
                    ctx.strokeStyle = '#007bff';
                    ctx.lineWidth = 2;
                    ctx.setLineDash([3, 3]);
                ctx.beginPath();
                    ctx.moveTo(screenMinX, screenMinY);
                    ctx.lineTo(screenMinX, centerY);
                    ctx.stroke();
                    ctx.setLineDash([]);
                    
                    // Glow effect
                    ctx.shadowBlur = 15;
                    ctx.shadowColor = '#007bff';
                    ctx.fillStyle = '#007bff';
                    ctx.beginPath();
                    ctx.arc(screenMinX, screenMinY, 8, 0, 2 * Math.PI);
                ctx.fill();
                    ctx.shadowBlur = 0;
                    
                    // Label
                    ctx.fillStyle = '#007bff';
                    ctx.font = 'bold 13px Arial';
                    ctx.textAlign = 'center';
                    ctx.fillText(`x*=${minX.toFixed(2)}`, screenMinX, screenMinY - 15);
                    ctx.fillText(`g(λ)=${minY.toFixed(2)}`, screenMinX, centerY + 35);
            }
        }
        
        // Draw constraint x = 1
            ctx.strokeStyle = '#dc3545';
            ctx.lineWidth = 4;
            ctx.setLineDash([10, 5]);
            ctx.shadowBlur = 5;
            ctx.shadowColor = '#dc3545';
        ctx.beginPath();
        ctx.moveTo(centerX + scale, panel.y);
        ctx.lineTo(centerX + scale, panel.y + panel.height);
        ctx.stroke();
        ctx.setLineDash([]);
            ctx.shadowBlur = 0;
            
            // Shade feasible region
            ctx.fillStyle = 'rgba(220, 53, 69, 0.1)';
            ctx.fillRect(panel.x, panel.y, centerX + scale - panel.x, panel.height);
        
        // Mark optimal point
            ctx.shadowBlur = 20;
            ctx.shadowColor = '#ff0000';
        ctx.fillStyle = '#ff0000';
        ctx.beginPath();
            ctx.arc(centerX + scale, centerY - scale / 2, 10, 0, 2 * Math.PI);
        ctx.fill();
            ctx.shadowBlur = 0;
            
            // Label optimal
            ctx.fillStyle = '#ff0000';
            ctx.font = 'bold 14px Arial';
            ctx.textAlign = 'center';
            ctx.fillText('p* = 1', centerX + scale, centerY - scale / 2 - 20);
            
            // Legend
            const legendX = panel.x + 15;
            const legendY = panel.y + 15;
            ctx.fillStyle = 'rgba(255, 255, 255, 0.95)';
            ctx.strokeStyle = '#dee2e6';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.roundRect(legendX, legendY, 160, 90, 5);
            ctx.fill();
            ctx.stroke();
            
            ctx.font = '13px Arial';
            ctx.textAlign = 'left';
            let yPos = legendY + 20;
            
            ctx.strokeStyle = '#212529';
            ctx.lineWidth = 3;
            ctx.beginPath();
            ctx.moveTo(legendX + 10, yPos);
            ctx.lineTo(legendX + 35, yPos);
            ctx.stroke();
            ctx.fillStyle = '#212529';
            ctx.fillText('f(x) = x²', legendX + 45, yPos + 4);
            yPos += 22;
            
            if (lambda > 0.01) {
                ctx.strokeStyle = '#007bff';
                ctx.beginPath();
                ctx.moveTo(legendX + 10, yPos);
                ctx.lineTo(legendX + 35, yPos);
                ctx.stroke();
                ctx.fillStyle = '#007bff';
                ctx.fillText('L(x,λ)', legendX + 45, yPos + 4);
                yPos += 22;
            }
            
            ctx.strokeStyle = '#dc3545';
            ctx.setLineDash([8, 4]);
            ctx.beginPath();
            ctx.moveTo(legendX + 10, yPos);
            ctx.lineTo(legendX + 35, yPos);
            ctx.stroke();
            ctx.setLineDash([]);
            ctx.fillStyle = '#dc3545';
            ctx.fillText('x ≤ 1', legendX + 45, yPos + 4);
    }
    
    function drawDualSpace(panel, currentLambda) {
            const margin = 50;
            const centerX = panel.x + margin;
            const centerY = panel.y + panel.height - 70;
            const scaleX = (panel.width - margin - 30) / 4;
            const scaleY = 60;
            
            // Draw grid
            ctx.strokeStyle = '#e9ecef';
        ctx.lineWidth = 1;
            ctx.setLineDash([2, 2]);
            for (let i = 0; i <= 4; i++) {
                const x = centerX + i * scaleX;
                ctx.beginPath();
                ctx.moveTo(x, panel.y);
                ctx.lineTo(x, centerY);
                ctx.stroke();
            }
            for (let i = -5; i <= 1; i++) {
                const y = centerY + i * scaleY;
                ctx.beginPath();
                ctx.moveTo(centerX, y);
                ctx.lineTo(panel.x + panel.width - 20, y);
                ctx.stroke();
            }
            ctx.setLineDash([]);
            
            // Draw axes
            ctx.strokeStyle = '#495057';
            ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(centerX, panel.y);
            ctx.lineTo(centerX, centerY);
        ctx.moveTo(centerX, centerY);
            ctx.lineTo(panel.x + panel.width - 20, centerY);
        ctx.stroke();
            
            // Axis labels
            ctx.fillStyle = '#495057';
            ctx.font = 'bold 13px Arial';
            ctx.textAlign = 'center';
            for (let i = 0; i <= 4; i++) {
                ctx.fillText(i.toString(), centerX + i * scaleX, centerY + 20);
            }
            ctx.textAlign = 'right';
            for (let i = -5; i <= 0; i++) {
                ctx.fillText(i.toString(), centerX - 10, centerY + i * scaleY + 5);
            }
            
            ctx.font = 'bold 16px Arial';
            ctx.textAlign = 'center';
            ctx.fillText('λ', panel.x + panel.width - 10, centerY + 20);
            ctx.textAlign = 'left';
            ctx.fillText('g(λ)', centerX - 40, panel.y + 20);
        
        // Draw dual function g(λ) = -λ²/4 - λ
            ctx.strokeStyle = '#28a745';
            ctx.lineWidth = 4;
            ctx.shadowBlur = 5;
            ctx.shadowColor = '#28a745';
        ctx.beginPath();
        let first = true;
            for (let lambda = 0; lambda <= 4; lambda += 0.02) {
            const g = -lambda * lambda / 4 - lambda;
            const screenX = centerX + lambda * scaleX;
            const screenY = centerY - g * scaleY;
                if (screenY >= panel.y && screenY <= centerY + 10) {
                if (first) {
                    ctx.moveTo(screenX, screenY);
                    first = false;
                } else {
                    ctx.lineTo(screenX, screenY);
                }
            }
        }
        ctx.stroke();
            ctx.shadowBlur = 0;
            
            // Mark current point with trail effect
            if (currentLambda > 0) {
                // Draw trail
                ctx.strokeStyle = 'rgba(220, 53, 69, 0.3)';
                ctx.lineWidth = 2;
                ctx.setLineDash([5, 5]);
                ctx.beginPath();
                for (let lambda = 0; lambda <= currentLambda; lambda += 0.05) {
                    const g = -lambda * lambda / 4 - lambda;
                    const screenX = centerX + lambda * scaleX;
                    const screenY = centerY - g * scaleY;
                    if (lambda === 0) {
                        ctx.moveTo(screenX, screenY);
                    } else {
                        ctx.lineTo(screenX, screenY);
                    }
                }
                ctx.stroke();
                ctx.setLineDash([]);
            }
        
        // Mark current point
        const currentG = -currentLambda * currentLambda / 4 - currentLambda;
        const currentScreenX = centerX + currentLambda * scaleX;
        const currentScreenY = centerY - currentG * scaleY;
        
            if (currentScreenY >= panel.y && currentScreenY <= centerY) {
                // Vertical line
                ctx.strokeStyle = '#dc3545';
                ctx.lineWidth = 2;
                ctx.setLineDash([3, 3]);
            ctx.beginPath();
                ctx.moveTo(currentScreenX, currentScreenY);
                ctx.lineTo(currentScreenX, centerY);
                ctx.stroke();
                ctx.setLineDash([]);
                
                // Glow point
                ctx.shadowBlur = 20;
                ctx.shadowColor = '#dc3545';
                ctx.fillStyle = '#dc3545';
                ctx.beginPath();
                ctx.arc(currentScreenX, currentScreenY, 10, 0, 2 * Math.PI);
            ctx.fill();
                ctx.shadowBlur = 0;
            }
            
            // Show p* = 1 reference line
            ctx.strokeStyle = '#ff0000';
            ctx.lineWidth = 2;
            ctx.setLineDash([8, 4]);
            const pStarY = centerY - 1 * scaleY;
            ctx.beginPath();
            ctx.moveTo(centerX, pStarY);
            ctx.lineTo(panel.x + panel.width - 20, pStarY);
            ctx.stroke();
            ctx.setLineDash([]);
            
            ctx.fillStyle = '#ff0000';
            ctx.font = 'bold 13px Arial';
            ctx.textAlign = 'left';
            ctx.fillText('p* = 1', panel.x + panel.width - 70, pStarY - 5);
    }
    
    function animate() {
        if (!isAnimating) return;
        
            currentLambda += 0.015;
        if (currentLambda > 4) {
            currentLambda = 0;
        }
        
        drawCompleteExample(currentLambda);
        animationId = requestAnimationFrame(animate);
    }
    
    animateBtn.addEventListener('click', function() {
        if (isAnimating) {
            isAnimating = false;
                if (animationId) cancelAnimationFrame(animationId);
                animateBtn.innerHTML = '▶ Tiếp Tục';
                animateBtn.style.background = '#007bff';
        } else {
            isAnimating = true;
                animateBtn.innerHTML = '⏸ Tạm Dừng';
                animateBtn.style.background = '#ffc107';
            animate();
        }
    });
    
    resetBtn.addEventListener('click', function() {
        isAnimating = false;
            if (animationId) cancelAnimationFrame(animationId);
        currentLambda = 0;
            animateBtn.innerHTML = '▶ Chạy Animation';
            animateBtn.style.background = '#28a745';
        drawCompleteExample(currentLambda);
    });
    
    // Initial draw
    drawCompleteExample(currentLambda);
    }
})();
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
