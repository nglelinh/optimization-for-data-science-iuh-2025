---
layout: post
title: 06-06 Gradient descent with momentum
chapter: '06'
order: 15
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
lesson_type: required
---

<script src="https://d3js.org/d3.v7.min.js"></script>

## Vấn đề với Gradient Descent thuần túy

Hãy tưởng tượng bạn đang lăn một quả bóng xuống thung lũng. Gradient descent tiêu chuẩn giống như một quả bóng không có trí nhớ - tại mỗi bước, nó chỉ xem xét độ dốc hiện tại và di chuyển tương ứng. Điều này có thể dẫn đến một số vấn đề:

1. **Hội tụ chậm trong các khe hẹp**: Khi hàm có gradient dốc trong một số hướng và gradient thoải trong các hướng khác
2. **Dao động**: Thuật toán có thể dao động qua lại trên thung lũng thay vì tiến bộ ổn định
3. **Bị kẹt trong các cực tiểu địa phương kém**: Không có momentum, thuật toán có thể ổn định ở các nghiệm không tối ưu

**Câu hỏi**: Điều gì sẽ xảy ra nếu quả bóng của chúng ta có thể "nhớ" hướng trước đó và duy trì một chút vận tốc?

## Momentum: Thêm bộ nhớ vào Gradient Descent

Gradient descent với momentum được lấy cảm hứng từ vật lý - cụ thể là chuyển động của một quả bóng lăn xuống đồi với ma sát. Ý tưởng chính là tích lũy một vector vận tốc kết hợp gradient hiện tại với momentum trước đó.

### Thuật toán Momentum

**Quy tắc cập nhật:**
$$ \begin{align}
v^{(k)} &= \beta v^{(k-1)} + (1-\beta) \nabla f(x^{(k-1)}) \\
x^{(k)} &= x^{(k-1)} - t v^{(k)}
\end{align} $$

trong đó:
- $$v^{(k)}$$ là momentum (vận tốc) tại lần lặp $$k$$
- $$\beta \in [0,1)$$ là hệ số momentum (thường là 0.9 hoặc 0.99)
- $$t > 0$$ là tốc độ học
- $$v^{(0)} = 0$$ (vận tốc ban đầu bằng không)

### Công thức thay thế (kiểu Nesterov)

Một số triển khai sử dụng dạng hơi khác:
$$ \begin{align}
v^{(k)} &= \beta v^{(k-1)} + \nabla f(x^{(k-1)}) \\
x^{(k)} &= x^{(k-1)} - t v^{(k)}
\end{align} $$

**Ý tưởng chính**: Số hạng momentum $$v^{(k)}$$ là trung bình động có trọng số mũ của các gradient trong quá khứ.

## Hiểu hệ số Momentum $$\beta$$

Hệ số momentum $$\beta$$ kiểm soát thuật toán có bao nhiều "bộ nhớ":

- **$$\beta = 0$$**: Không có momentum, giảm về gradient descent tiêu chuẩn
- **$$\beta = 0.9$$**: Momentum trung bình, thường được sử dụng trong thực tế
- **$$\beta = 0.99$$**: Momentum cao, được sử dụng trong một số ứng dụng deep learning
- **$$\beta \to 1$$**: Momentum tối đa, nhưng có thể gây bất ổn

### Trung bình động có trọng số mũ

Momentum $$v^{(k)}$$ có thể được mở rộng là:
$$ v^{(k)} = (1-\beta) \sum_{i=0}^{k-1} \beta^i \nabla f(x^{(k-1-i)}) $$

Điều này cho thấy momentum cho trọng số giảm mũ cho các gradient cũ hơn.

## Interactive Visualization: Gradient Descent vs Momentum

<div id="momentum-comparison" style="margin: 20px 0;">
    <!-- Parameter Controls -->
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; margin-bottom: 15px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; background-color: #f9f9f9;">
        <div>
            <label for="momentum-lr">Learning Rate: </label>
            <input type="range" id="momentum-lr" min="0.01" max="0.3" step="0.01" value="0.1">
            <span id="momentum-lr-value">0.1</span>
        </div>
        <div>
            <label for="momentum-beta">Momentum (β): </label>
            <input type="range" id="momentum-beta" min="0" max="0.99" step="0.01" value="0.9">
            <span id="momentum-beta-value">0.9</span>
        </div>
        <div>
            <label for="momentum-speed">Animation Speed: </label>
            <input type="range" id="momentum-speed" min="1" max="10" step="1" value="5">
            <span id="momentum-speed-value">5</span>
        </div>
    </div>
    
    <!-- Control Buttons -->
    <div style="display: flex; gap: 10px; margin-bottom: 15px; flex-wrap: wrap;">
        <button id="start-vanilla-gd" style="background-color: #4CAF50; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Start Vanilla GD</button>
        <button id="start-momentum-gd" style="background-color: #FF9800; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Start Momentum GD</button>
        <button id="start-both" style="background-color: #2196F3; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Compare Both</button>
        <button id="reset-momentum" style="background-color: #f44336; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Reset</button>
    </div>
    
    <!-- Visualization Canvas -->
    <div id="momentum-canvas" style="border: 1px solid #ccc; border-radius: 5px; background-color: white; position: relative; overflow: hidden;">
        <svg width="800" height="500" id="momentum-svg"></svg>
    </div>
    
    <!-- Algorithm Status -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 15px;">
        <div style="padding: 10px; border: 1px solid #4CAF50; border-radius: 5px; background-color: #f1f8e9;">
            <h4 style="margin: 0 0 5px 0; color: #4CAF50;">Vanilla Gradient Descent</h4>
            <p id="vanilla-gd-info" style="margin: 0; font-size: 14px;">Ready to start</p>
        </div>
        <div style="padding: 10px; border: 1px solid #FF9800; border-radius: 5px; background-color: #fff8e1;">
            <h4 style="margin: 0 0 5px 0; color: #FF9800;">Momentum Gradient Descent</h4>
            <p id="momentum-gd-info" style="margin: 0; font-size: 14px;">Ready to start</p>
        </div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    // Momentum visualization implementation
    const svg = d3.select("#momentum-svg");
    const width = 800, height = 500;
    const margin = {top: 20, right: 20, bottom: 40, left: 40};
    
    // Function to optimize: f(x,y) = 0.5*x^2 + 5*y^2 (elongated bowl)
    function f(x, y) {
        return 0.5 * x * x + 5 * y * y;
    }
    
    function gradient(x, y) {
        return [x, 10 * y];
    }
    
    // Scale setup
    const xScale = d3.scaleLinear()
        .domain([-6, 6])
        .range([margin.left, width - margin.right]);
    
    const yScale = d3.scaleLinear()
        .domain([-3, 3])
        .range([height - margin.bottom, margin.top]);
    
    // Create contour plot
    function createContours() {
        // Create a simple grid-based contour visualization
        const gridSize = 20;
        const contourLevels = [1, 4, 9, 16, 25, 36, 49];
        
        svg.selectAll(".contour").remove();
        
        // Draw contour ellipses for the function f(x,y) = 0.5*x^2 + 5*y^2
        contourLevels.forEach(level => {
            // For f(x,y) = 0.5*x^2 + 5*y^2 = level
            // This is an ellipse: x^2/(2*level) + y^2/(level/5) = 1
            const a = Math.sqrt(2 * level); // semi-major axis in x direction
            const b = Math.sqrt(level / 5); // semi-minor axis in y direction
            
            if (a <= 6 && b <= 3) { // Only draw if within our domain
                svg.append("ellipse")
                    .attr("class", "contour")
                    .attr("cx", xScale(0))
                    .attr("cy", yScale(0))
                    .attr("rx", xScale(a) - xScale(0))
                    .attr("ry", yScale(0) - yScale(b))
                    .attr("fill", "none")
                    .attr("stroke", "#ddd")
                    .attr("stroke-width", 1)
                    .attr("opacity", 0.6);
            }
        });
    }
    
    createContours();
    
    // Add global minimum marker
    svg.append("circle")
        .attr("cx", xScale(0))
        .attr("cy", yScale(0))
        .attr("r", 8)
        .attr("fill", "red")
        .attr("stroke", "white")
        .attr("stroke-width", 2)
        .attr("opacity", 0.8);
    
    svg.append("text")
        .attr("x", xScale(0))
        .attr("y", yScale(0) - 15)
        .attr("text-anchor", "middle")
        .attr("font-size", "12px")
        .attr("font-weight", "bold")
        .attr("fill", "red")
        .text("Global Minimum");
    
    // Add axes
    svg.append("g")
        .attr("transform", `translate(0,${height - margin.bottom})`)
        .call(d3.axisBottom(xScale));
    
    svg.append("g")
        .attr("transform", `translate(${margin.left},0)`)
        .call(d3.axisLeft(yScale));
    
    // Add axis labels
    svg.append("text")
        .attr("x", width / 2)
        .attr("y", height - 5)
        .attr("text-anchor", "middle")
        .attr("font-size", "14px")
        .text("x");
    
    svg.append("text")
        .attr("x", 15)
        .attr("y", height / 2)
        .attr("text-anchor", "middle")
        .attr("font-size", "14px")
        .attr("transform", `rotate(-90, 15, ${height / 2})`)
        .text("y");
    
    // Add title
    svg.append("text")
        .attr("x", width / 2)
        .attr("y", 15)
        .attr("text-anchor", "middle")
        .attr("font-size", "16px")
        .attr("font-weight", "bold")
        .text("f(x,y) = 0.5x² + 5y² - Optimization Paths Comparison");
    
    // Variables for animation
    let vanillaPath = [], momentumPath = [];
    let vanillaRunning = false, momentumRunning = false;
    let vanillaInterval, momentumInterval;
    
    // Algorithm implementations
    function runVanillaGD() {
        const lr = parseFloat(document.getElementById('momentum-lr').value);
        let x = -4, y = 2; // Starting point
        let iteration = 0;
        const maxIterations = 500;
        vanillaPath = [{x: x, y: y}];
        vanillaRunning = true;
        
        vanillaInterval = setInterval(() => {
            const grad = gradient(x, y);
            x -= lr * grad[0];
            y -= lr * grad[1];
            vanillaPath.push({x: x, y: y});
            iteration++;
            
            updateVisualization();
            updateStatus();
            
            // Stop if converged or max iterations reached
            if ((Math.abs(grad[0]) < 0.01 && Math.abs(grad[1]) < 0.01) || iteration >= maxIterations) {
                clearInterval(vanillaInterval);
                vanillaRunning = false;
            }
        }, 1000 / parseFloat(document.getElementById('momentum-speed').value));
    }
    
    function runMomentumGD() {
        const lr = parseFloat(document.getElementById('momentum-lr').value);
        const beta = parseFloat(document.getElementById('momentum-beta').value);
        let x = -4, y = 2; // Starting point
        let vx = 0, vy = 0; // Initial velocity
        let iteration = 0;
        const maxIterations = 500;
        momentumPath = [{x: x, y: y}];
        momentumRunning = true;
        
        momentumInterval = setInterval(() => {
            const grad = gradient(x, y);
            vx = beta * vx + (1 - beta) * grad[0];
            vy = beta * vy + (1 - beta) * grad[1];
            x -= lr * vx;
            y -= lr * vy;
            momentumPath.push({x: x, y: y});
            iteration++;
            
            updateVisualization();
            updateStatus();
            
            // Stop if converged or max iterations reached
            if ((Math.abs(grad[0]) < 0.01 && Math.abs(grad[1]) < 0.01) || iteration >= maxIterations) {
                clearInterval(momentumInterval);
                momentumRunning = false;
            }
        }, 1000 / parseFloat(document.getElementById('momentum-speed').value));
    }
    
    function updateVisualization() {
        // Remove existing paths
        svg.selectAll(".vanilla-path").remove();
        svg.selectAll(".momentum-path").remove();
        svg.selectAll(".vanilla-point").remove();
        svg.selectAll(".momentum-point").remove();
        
        // Draw vanilla GD path
        if (vanillaPath.length > 1) {
            const line = d3.line()
                .x(d => xScale(d.x))
                .y(d => yScale(d.y));
            
            svg.append("path")
                .datum(vanillaPath)
                .attr("class", "vanilla-path")
                .attr("d", line)
                .attr("fill", "none")
                .attr("stroke", "#4CAF50")
                .attr("stroke-width", 2);
            
            // Current point
            const current = vanillaPath[vanillaPath.length - 1];
            svg.append("circle")
                .attr("class", "vanilla-point")
                .attr("cx", xScale(current.x))
                .attr("cy", yScale(current.y))
                .attr("r", 5)
                .attr("fill", "#4CAF50");
        }
        
        // Draw momentum GD path
        if (momentumPath.length > 1) {
            const line = d3.line()
                .x(d => xScale(d.x))
                .y(d => yScale(d.y));
            
            svg.append("path")
                .datum(momentumPath)
                .attr("class", "momentum-path")
                .attr("d", line)
                .attr("fill", "none")
                .attr("stroke", "#FF9800")
                .attr("stroke-width", 2);
            
            // Current point
            const current = momentumPath[momentumPath.length - 1];
            svg.append("circle")
                .attr("class", "momentum-point")
                .attr("cx", xScale(current.x))
                .attr("cy", yScale(current.y))
                .attr("r", 5)
                .attr("fill", "#FF9800");
        }
    }
    
    function updateStatus() {
        // Update vanilla GD status
        if (vanillaPath.length > 0) {
            const current = vanillaPath[vanillaPath.length - 1];
            const fValue = f(current.x, current.y);
            document.getElementById('vanilla-gd-info').innerHTML = 
                `Iteration: ${vanillaPath.length - 1}<br>Position: (${current.x.toFixed(3)}, ${current.y.toFixed(3)})<br>f(x,y): ${fValue.toFixed(4)}`;
        }
        
        // Update momentum GD status
        if (momentumPath.length > 0) {
            const current = momentumPath[momentumPath.length - 1];
            const fValue = f(current.x, current.y);
            document.getElementById('momentum-gd-info').innerHTML = 
                `Iteration: ${momentumPath.length - 1}<br>Position: (${current.x.toFixed(3)}, ${current.y.toFixed(3)})<br>f(x,y): ${fValue.toFixed(4)}`;
        }
    }
    
    // Event listeners
    document.getElementById('start-vanilla-gd').addEventListener('click', () => {
        if (!vanillaRunning) {
            vanillaRunning = true;
            runVanillaGD();
        }
    });
    
    document.getElementById('start-momentum-gd').addEventListener('click', () => {
        if (!momentumRunning) {
            momentumRunning = true;
            runMomentumGD();
        }
    });
    
    document.getElementById('start-both').addEventListener('click', () => {
        if (!vanillaRunning && !momentumRunning) {
            vanillaRunning = true;
            momentumRunning = true;
            runVanillaGD();
            runMomentumGD();
        }
    });
    
    document.getElementById('reset-momentum').addEventListener('click', () => {
        clearInterval(vanillaInterval);
        clearInterval(momentumInterval);
        vanillaRunning = false;
        momentumRunning = false;
        vanillaPath = [];
        momentumPath = [];
        updateVisualization();
        document.getElementById('vanilla-gd-info').innerHTML = 'Ready to start';
        document.getElementById('momentum-gd-info').innerHTML = 'Ready to start';
    });
    
    // Update display values
    document.getElementById('momentum-lr').addEventListener('input', function() {
        document.getElementById('momentum-lr-value').textContent = this.value;
    });
    
    document.getElementById('momentum-beta').addEventListener('input', function() {
        document.getElementById('momentum-beta-value').textContent = this.value;
    });
    
    document.getElementById('momentum-speed').addEventListener('input', function() {
        document.getElementById('momentum-speed-value').textContent = this.value;
    });
});
</script>

## Ưu điểm của Momentum

### 1. **Hội tụ nhanh hơn**
Momentum giúp thuật toán tăng tốc trong các hướng nhất quán, dẫn đến hội tụ nhanh hơn đặc biệt trong:
- Các hàm có thung lũng hoặc khe hẹp
- Các bài toán có điều kiện kém (số điều kiện cao)
- Các hàm có nhiều cực tiểu địa phương

### 2. **Giảm dao động**
Trong các hướng mà gradient thường xuyên đổi dấu, momentum giúp làm mượt các dao động bằng cách lấy trung bình các gradient trong quá khứ.

### 3. **Thoát khỏi cực tiểu địa phương**
Momentum tích lũy có thể giúp thuật toán "lăn qua" các cực tiểu địa phương nhỏ và tiếp tục hướng tới các nghiệm tốt hơn.

## Các biến thể và mở rộng

### 1. **Nesterov Accelerated Gradient (NAG)**
Thay vì tính gradient tại vị trí hiện tại, NAG tính nó tại vị trí "nhìn trước":

$$ \begin{align}
v^{(k)} &= \beta v^{(k-1)} + \nabla f(x^{(k-1)} - \beta v^{(k-1)}) \\
x^{(k)} &= x^{(k-1)} - t v^{(k)}
\end{align} $$

**Trực quan**: "Nhìn trước khi nhảy" - kiểm tra gradient tại nơi momentum sẽ đưa bạn đến.

#### Vấn đề với Momentum thông thường

Mặc dù momentum giúp quả bóng vượt qua các cực tiểu địa phương, có một hạn chế mà chúng ta có thể quan sát: khi tiến gần đến mục tiêu, momentum vẫn mất khá nhiều thời gian trước khi dừng lại. Lý do chính xác là do vận tốc tích lũy.

#### Ý tưởng chính

Ý tưởng cơ bản là **dự đoán hướng tương lai** - về cơ bản là nhìn trước một bước! Cụ thể, nếu chúng ta sử dụng số hạng momentum $$\beta v^{(k-1)}$$ để cập nhật, chúng ta có thể xấp xỉ vị trí tiếp theo là $$x^{(k-1)} - \beta v^{(k-1)}$$ (chúng ta không bao gồm số hạng gradient ở đây vì chúng ta sẽ sử dụng nó trong bước cuối).

Thay vì sử dụng gradient tại vị trí hiện tại, NAG bước tiến về phía trước và sử dụng gradient tại vị trí dự kiến tiếp theo.

#### Visual Comparison

**With regular momentum**: The update is the sum of two vectors:
- Momentum vector (from previous step)
- Gradient at the current position

**With Nesterov momentum**: The update is the sum of two vectors:
- Momentum vector (from previous step)  
- Gradient at the **look-ahead** position (where momentum would take us)

This "look-ahead" approach allows NAG to make more informed corrections and often leads to faster convergence.

### 2. **Adaptive Moment Estimation (Adam)**
Adam combines momentum with adaptive learning rates for each parameter:

$$ \begin{align}
m^{(k)} &= \beta_1 m^{(k-1)} + (1-\beta_1) \nabla f(x^{(k-1)}) \\
v^{(k)} &= \beta_2 v^{(k-1)} + (1-\beta_2) (\nabla f(x^{(k-1)}))^2 \\
x^{(k)} &= x^{(k-1)} - t \frac{m^{(k)}}{\sqrt{v^{(k)}} + \epsilon}
\end{align} $$

## Practical Implementation Tips

### 1. **Choosing the Momentum Coefficient**
- **Start with $$\beta = 0.9$$**: A good default for most problems
- **Increase to $$\beta = 0.99$$**: For very smooth optimization landscapes
- **Decrease to $$\beta = 0.5-0.7$$**: For noisy or non-smooth functions

### 2. **Learning Rate Adjustment**
When using momentum, you may need to reduce the learning rate compared to vanilla gradient descent, as momentum amplifies the effective step size.

### 3. **Warm-up Period**
Consider starting with lower momentum and gradually increasing it, as momentum needs time to build up effective velocity.

## Mathematical Analysis

### Convergence Properties

For strongly convex functions with Lipschitz gradients, momentum gradient descent achieves:
- **Linear convergence**: $$f(x^{(k)}) - f^* \leq C \rho^k$$ for some $$\rho < 1$$
- **Improved condition number**: Effective condition number can be improved from $$\kappa$$ to $$\sqrt{\kappa}$$

### Heavy Ball Method Connection

Momentum gradient descent is closely related to the heavy ball method from classical mechanics:
$$mx'' + \gamma x' + \nabla f(x) = 0$$

This differential equation, when discretized, leads to the momentum update rules.

## Tóm tắt so sánh

| Khía cạnh | Vanilla GD | Momentum GD |
|--------|------------|-------------|
| **Bộ nhớ** | Không | Có (giảm mũ) |
| **Hội tụ** | Có thể chậm | Thường nhanh hơn |
| **Dao động** | Dễ xảy ra hơn | Giảm |
| **Cực tiểu địa phương** | Có thể bị kẹt | Thoát tốt hơn |
| **Siêu tham số** | Tốc độ học | Tốc độ học + momentum |
| **Chi phí tính toán** | Thấp | Hơi cao hơn |

## Những điểm chính

1. **Momentum thêm bộ nhớ**: Nó nhớ hướng của các bước trước đó
2. **Hội tụ nhanh hơn**: Đặc biệt hiệu quả cho các hàm có thung lũng hoặc khe hẹp
3. **Giảm dao động**: Làm mượt hành vi zigzag
4. **Được sử dụng rộng rãi**: Nền tảng cho nhiều thuật toán tối ưu hóa hiện đại
5. **Có thể điều chỉnh**: Hệ số momentum $$\beta$$ cho phép tinh chỉnh cho các bài toán khác nhau

**Kết luận**: Momentum là một cải tiến đơn giản nhưng mạnh mẽ cho gradient descent đã vượt qua thử thách của thời gian và vẫn có liên quan trong các ứng dụng machine learning hiện đại.
