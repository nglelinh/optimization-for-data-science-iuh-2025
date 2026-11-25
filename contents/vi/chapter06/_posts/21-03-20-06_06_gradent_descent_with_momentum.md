---
layout: post
title: 06-06 Gradient descent with momentum
chapter: '06'
order: 18
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
lesson_type: required
---

Hãy hình dung một hòn bi thép nặng lăn xuống một khe núi hẹp và dài: ở hai vách núi dốc đứng bên trái–phải, lực kéo đổi chiều liên tục nên tự triệt tiêu lẫn nhau; còn dọc theo lòng khe thoai thoải đi xuống đáy, gia tốc tích tụ liên tục làm hòn bi lao vút về phía trước! Gradient Descent thuần túy giống như một người đi bộ "mất trí nhớ" — sau mỗi bước lại dừng hẳn về vận tốc 0 rồi mới tính lại hướng; còn **Momentum (Động lượng / Heavy Ball của Polyak, 1964)** trao cho thuật toán chính **quán tính vật lý** của hòn bi thép ấy!

Kết quả là một sự tăng tốc ngoạn mục: trên các hàm lồi mạnh có chỉ số điều kiện xấu $$\kappa = L/m$$, Momentum rút gọn số vòng lặp từ $$O(\kappa \log(1/\epsilon))$$ xuống còn $$O(\sqrt{\kappa} \log(1/\epsilon))$$ — hoàn toàn tương đương bước nhảy của tăng tốc Nesterov trên hàm bậc hai!

## Kiến thức cần nhớ: Vật lý và Đại số của Phương pháp Momentum

Ba trụ cột dưới đây giải mã trọn vẹn cách hệ số quán tính $$\beta$$ điều khiển quỹ đạo hội tụ:

- **Phương trình Động lượng & Trung bình trượt lũy thừa (EMA):** Quy tắc cập nhật:
  $$v_{k+1} = \beta v_k + \nabla f(x_k), \qquad x_{k+1} = x_k - \alpha v_{k+1}.$$
  Khai triển đệ quy cho thấy $$v_{k+1} = \sum_{j=0}^k \beta^{k-j} \nabla f(x_j)$$: vận tốc hiện tại là tổng trọng số suy giảm theo hàm mũ của toàn bộ lịch sử gradient!
- **Cơ chế "Triệt tiêu dao động – Khuếch đại hướng ổn định":**
  - Theo phương thung lũng dài (gradient cùng dấu liên tục $$g$$): vận tốc tích tụ lên đến $$\frac{g}{1 - \beta}$$ — với $$\beta = 0.9$$, tốc độ tiến dọc thung lũng được khuếch đại gấp **10 lần**!
  - Theo phương vách dốc (gradient đổi dấu $$+g, -g, +g, -g$$): các số hạng ngược dấu triệt tiêu nhau, dập tắt hiện tượng zíc-zắc!
- **Tham số tối ưu cho hàm bậc hai:** Với hàm bậc hai có trị riêng nằm trong $$[m, L]$$, cặp tham số tối ưu của Polyak là:
  $$\alpha^\star = \left(\frac{2}{\sqrt{L} + \sqrt{m}}\right)^2, \qquad \beta^\star = \left(\frac{\sqrt{L} - \sqrt{m}}{\sqrt{L} + \sqrt{m}}\right)^2 = \left(\frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1}\right)^2,$$
  đạt hệ số co mỗi bước là $$\frac{\sqrt{\kappa} - 1}{\sqrt{\kappa} + 1}$$!

### Giải thích: Chạy tay 3 bước Momentum vs. GD thường trên thung lũng hẹp

Xét hàm $$f(x_1, x_2) = \frac{1}{2}(x_1^2 + 9x_2^2)$$ ($$m = 1,\; L = 9,\; \kappa = 9$$).
- Với **GD thường** dùng bước tối ưu $$t^\star = \frac{2}{9+1} = 0.2$$, hệ số co là $$\frac{9-1}{9+1} = 0.8$$.
- Với **Momentum Polyak**, tính ngay tham số tối ưu:
  $$\alpha^\star = \left(\frac{2}{3 + 1}\right)^2 = 0.25, \qquad \beta^\star = \left(\frac{3 - 1}{3 + 1}\right)^2 = 0.25.$$
  Hệ số co lý thuyết giảm từ $$0.8$$ xuống còn $$\frac{\sqrt{9} - 1}{\sqrt{9} + 1} = 0.5$$!

Hãy chạy tay từ $$x_0 = (1, 1)^T,\; v_0 = (0, 0)^T$$ với $$x_{k+1} = x_k - 0.25 \nabla f(x_k) + 0.25(x_k - x_{k-1})$$:
1. **Bước 1:** $$g_0 = (1, 9)^T \implies x_1 = (1, 1)^T - 0.25(1, 9)^T = (0.75,\; -1.25)^T$$.
2. **Bước 2:** $$g_1 = (0.75,\; -11.25)^T$$, độ dịch trước $$x_1 - x_0 = (-0.25,\; -2.25)^T$$.
   - $$x_{2,1} = 0.75 - 0.25(0.75) + 0.25(-0.25) = 0.50$$ (trong khi GD thường mới ở $$0.8^2 = 0.64$$!).
   - $$x_{2,2} = -1.25 - 0.25(-11.25) + 0.25(-2.25) = -1.25 + 2.8125 - 0.5625 = 1.00$$ (đang hãm dao động mạnh).
3. **Bước 3:** $$g_2 = (0.50,\; 9.0)^T$$, $$x_2 - x_1 = (-0.25,\; 2.25)^T$$.
   - $$x_{3,1} = 0.50 - 0.25(0.50) + 0.25(-0.25) = 0.3125$$ (so với GD thường $$0.8^3 = 0.512$$!).
   - $$x_{3,2} = 1.00 - 0.25(9.0) + 0.25(2.25) = -0.6875$$.
   Chỉ sau vài bước, quán tính đã kéo trục thoai thoải $$x_1$$ về đích nhanh vượt trội!

---

<script src="https://d3js.org/d3.v7.min.js"></script>

Hình minh họa trên trang này mô phỏng trường hợp toàn tập (full-batch) với hệ số momentum $$\beta$$ không đổi. Phân tích phổ theo phong cách Distill — bao gồm đa thức đặc trưng, giá trị $$\beta^\star$$ tối ưu, so sánh nhìn trước (look-ahead) với heavy ball, và lý do `nesterov=True` không tương đương FISTA — được trình bày trong bài hiện đại [26-02]({% multilang_post_url contents/chapter26/2026-09-15-26_02_momentum_and_nesterov %}); phiên bản gradient gần kề có lập lịch tham số nằm tại [09-05]({% multilang_post_url contents/chapter09/20-01-08-09_05_acceleration %}).

## Hạn chế của Gradient Descent Thuần túy

Hãy hình dung một quả bóng lăn xuống đáy thung lũng. Gradient descent tiêu chuẩn giống như một quả bóng không có quán tính: tại mỗi bước, nó chỉ dựa vào độ dốc tức thời để di chuyển. Điều này dẫn tới một số hạn chế:

1. **Hội tụ chậm trong các thung lũng hẹp**: Khi hàm số rất dốc theo một số phương nhưng lại rất thoải theo các phương khác.
2. **Dao động mạnh**: Quỹ đạo thường nảy qua lại giữa hai sườn thung lũng thay vì tiến thẳng về phía cực tiểu.
3. **Dễ dừng sớm tại cực tiểu cục bộ nông**: Thiếu quán tính khiến thuật toán khó vượt qua các vùng trũng cục bộ nhỏ.

**Câu hỏi đặt ra**: Điều gì xảy ra nếu ta cho thuật toán "ghi nhớ" hướng di chuyển trước đó và duy trì một phần vận tốc?

## Momentum: Bổ sung Quán tính cho Gradient Descent

Gradient descent có momentum lấy cảm hứng từ cơ học cổ điển — cụ thể là chuyển động của một vật lăn xuống dốc có lực cản ma sát. Ý tưởng cốt lõi là tích lũy một vector vận tốc kết hợp giữa hướng di chuyển trước đó và gradient hiện tại.

### Thuật toán Momentum

**Quy tắc cập nhật:**
$$ \begin{align}
v^{(k)} &= \beta v^{(k-1)} + (1-\beta) \nabla f(x^{(k-1)}) \\
x^{(k)} &= x^{(k-1)} - t v^{(k)}
\end{align} $$

trong đó:
- $$v^{(k)}$$ là vector momentum (vận tốc) tại lần lặp $$k$$.
- $$\beta \in [0,1)$$ là hệ số momentum (thường chọn $$0.9$$ hoặc $$0.99$$).
- $$t > 0$$ là tốc độ học.
- $$v^{(0)} = 0$$ (vận tốc khởi tạo bằng 0).

### Dạng công thức tương đương (không nhân hệ số $$1-\beta$$)

Một số cài đặt sử dụng dạng tương đương sau (khác ở hệ số tỉ lệ tốc độ học):
$$ \begin{align}
v^{(k)} &= \beta v^{(k-1)} + \nabla f(x^{(k-1)}) \\
x^{(k)} &= x^{(k-1)} - t v^{(k)}
\end{align} $$

**Ý nghĩa chính**: Ở cả hai dạng, $$v^{(k)}$$ là tổ hợp có trọng số mũ của các gradient trước đó: dạng đầu là trung bình trượt, dạng sau là tổng có trọng số. Cả hai vẫn là phương pháp heavy ball thông thường, không phải Nesterov.

## Ý nghĩa của Hệ số Momentum $$\beta$$

Hệ số $$\beta$$ kiểm soát mức độ "ghi nhớ" của thuật toán:

- **$$\beta = 0$$**: Không có momentum, thuật toán trở về gradient descent tiêu chuẩn.
- **$$\beta = 0.9$$**: Mức momentum trung bình, được sử dụng phổ biến trong thực tế.
- **$$\beta = 0.99$$**: Mức momentum cao, thường dùng trong một số bài toán học sâu có bề mặt mất mát trơn.
- **$$\beta \to 1$$**: Quán tính rất lớn, nhưng dễ gây mất ổn định nếu tốc độ học không đủ nhỏ.

### Trung bình Trượt có Trọng số Mũ

Khai triển đệ quy công thức momentum đầu tiên cho ta:
$$ v^{(k)} = (1-\beta) \sum_{i=0}^{k-1} \beta^i \nabla f(x^{(k-1-i)}) $$

Công thức này cho thấy trọng số của các gradient cũ giảm dần theo hàm mũ theo thời gian.

## Trực quan hóa Tương tác: Gradient Descent và Momentum

<div id="momentum-comparison" style="margin: 20px 0;">
    <!-- Parameter Controls -->
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; margin-bottom: 15px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; background-color: #f9f9f9;">
        <div>
            <label for="momentum-lr">Tốc độ học: </label>
            <input type="range" id="momentum-lr" min="0.01" max="0.3" step="0.01" value="0.1">
            <span id="momentum-lr-value">0.1</span>
        </div>
        <div>
            <label for="momentum-beta">Momentum (β): </label>
            <input type="range" id="momentum-beta" min="0" max="0.99" step="0.01" value="0.9">
            <span id="momentum-beta-value">0.9</span>
        </div>
        <div>
            <label for="momentum-speed">Tốc độ hoạt ảnh: </label>
            <input type="range" id="momentum-speed" min="1" max="10" step="1" value="5">
            <span id="momentum-speed-value">5</span>
        </div>
    </div>
    
    <!-- Control Buttons -->
    <div style="display: flex; gap: 10px; margin-bottom: 15px; flex-wrap: wrap;">
        <button id="start-vanilla-gd" style="background-color: #4CAF50; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Chạy GD thường</button>
        <button id="start-momentum-gd" style="background-color: #FF9800; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Chạy GD momentum</button>
        <button id="start-both" style="background-color: #2196F3; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">So sánh cả hai</button>
        <button id="reset-momentum" style="background-color: #f44336; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Đặt lại</button>
    </div>
    
    <!-- Visualization Canvas -->
    <div id="momentum-canvas" style="border: 1px solid #ccc; border-radius: 5px; background-color: white; position: relative; overflow: hidden;">
        <svg width="800" height="500" id="momentum-svg"></svg>
    </div>
    
    <!-- Algorithm Status -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 15px;">
        <div style="padding: 10px; border: 1px solid #4CAF50; border-radius: 5px; background-color: #f1f8e9;">
            <h4 style="margin: 0 0 5px 0; color: #4CAF50;">Gradient Descent thường</h4>
            <p id="vanilla-gd-info" style="margin: 0; font-size: 14px;">Sẵn sàng</p>
        </div>
        <div style="padding: 10px; border: 1px solid #FF9800; border-radius: 5px; background-color: #fff8e1;">
            <h4 style="margin: 0 0 5px 0; color: #FF9800;">Gradient Descent với momentum</h4>
            <p id="momentum-gd-info" style="margin: 0; font-size: 14px;">Sẵn sàng</p>
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
        .text("Cực tiểu toàn cục");
    
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
        .text("f(x,y) = 0.5x² + 5y² - So sánh đường đi tối ưu");
    
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
                `Vòng lặp: ${vanillaPath.length - 1}<br>Vị trí: (${current.x.toFixed(3)}, ${current.y.toFixed(3)})<br>f(x,y): ${fValue.toFixed(4)}`;
        }
        
        // Update momentum GD status
        if (momentumPath.length > 0) {
            const current = momentumPath[momentumPath.length - 1];
            const fValue = f(current.x, current.y);
            document.getElementById('momentum-gd-info').innerHTML = 
                `Vòng lặp: ${momentumPath.length - 1}<br>Vị trí: (${current.x.toFixed(3)}, ${current.y.toFixed(3)})<br>f(x,y): ${fValue.toFixed(4)}`;
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
        document.getElementById('vanilla-gd-info').innerHTML = 'Sẵn sàng';
        document.getElementById('momentum-gd-info').innerHTML = 'Sẵn sàng';
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
Momentum tích lũy vận tốc dọc theo các hướng có gradient nhất quán, nhờ đó đẩy nhanh quá trình hội tụ đặc biệt trên:
- Các hàm có thung lũng hoặc khe hẹp.
- Các bài toán có chỉ số điều kiện lớn.
- Các bề mặt hàm phức tạp có nhiều cực tiểu cục bộ.

### 2. **Giảm dao động**
Theo các phương mà gradient liên tục đổi dấu, việc lấy trung bình các gradient quá khứ giúp triệt tiêu bớt thành phần dao động qua lại.

### 3. **Khả năng vượt qua cực tiểu cục bộ nông**
Quán tính tích lũy giúp quỹ đạo có thể lăn qua các vùng trũng cục bộ nhỏ để tiếp tục hướng tới nghiệm tốt hơn.

## Các Biến thể và Mở rộng

### 1. **Nesterov Accelerated Gradient (NAG)**
Thay vì tính gradient tại vị trí hiện tại, NAG đánh giá gradient tại vị trí "nhìn trước" (look-ahead):

$$ \begin{align}
v^{(k)} &= \beta v^{(k-1)} + \nabla f(x^{(k-1)} - t \beta v^{(k-1)}) \\
x^{(k)} &= x^{(k-1)} - t v^{(k)}
\end{align} $$

**Trực giác**: Đánh giá độ dốc tại vị trí dự kiến mà bước momentum sắp đưa ta tới, từ đó điều chỉnh sớm hơn.

#### Hạn chế của Momentum Thông thường

Dù momentum giúp tăng tốc trên thung lũng hẹp, khi tiến gần đến điểm cực tiểu, quán tính tích lũy có thể khiến quỹ đạo vượt quá mục tiêu và cần thêm nhiều bước để giảm tốc.

#### Ý tưởng Cốt lõi của NAG

Ý tưởng của NAG là **dự đoán trước vị trí kế tiếp**: vì thành phần momentum sẽ dịch chuyển điểm lặp đi một đoạn $$-t\beta v^{(k-1)}$$, ta xấp xỉ vị trí sắp tới là $$x^{(k-1)} - t\beta v^{(k-1)}$$ rồi tính gradient ngay tại điểm nhìn trước đó để hiệu chỉnh bước đi.

#### So sánh Trực quan

- **Momentum thông thường**: Bước cập nhật kết hợp vector momentum từ bước trước và gradient tại **vị trí hiện tại**.
- **Nesterov momentum**: Bước cập nhật kết hợp vector momentum từ bước trước và gradient tại **vị trí nhìn trước** (nơi momentum dự kiến sẽ đưa tới).

Cơ chế nhìn trước này giúp NAG hiệu chỉnh kịp thời khi độ dốc đổi chiều, giảm hiện tượng vượt quá cực tiểu và thường hội tụ nhanh hơn.

### 2. **Adaptive Moment Estimation (Adam)**
Adam kết hợp momentum (mô-men bậc nhất) với tốc độ học thích ứng cho từng tham số (dựa trên mô-men bậc hai):

$$ \begin{align}
m^{(k)} &= \beta_1 m^{(k-1)} + (1-\beta_1) \nabla f(x^{(k-1)}) \\
v^{(k)} &= \beta_2 v^{(k-1)} + (1-\beta_2) (\nabla f(x^{(k-1)}))^2 \\
x^{(k)} &= x^{(k-1)} - t \frac{m^{(k)}}{\sqrt{v^{(k)}} + \epsilon}
\end{align} $$

## Kinh nghiệm Cài đặt Thực tế

### 1. **Chọn Hệ số Momentum**
- **Bắt đầu với $$\beta = 0.9$$**: Lựa chọn mặc định phù hợp cho đa số bài toán.
- **Tăng lên $$\beta = 0.99$$**: Khi bề mặt hàm mục tiêu rất trơn.
- **Giảm xuống $$\beta = 0.5\text{--}0.7$$**: Khi gradient có nhiều nhiễu hoặc hàm kém trơn.

### 2. **Điều chỉnh Tốc độ Học**
Khi dùng momentum (đặc biệt dạng không nhân $$1-\beta$$), cần cân nhắc giảm tốc độ học so với gradient descent thường vì momentum làm tăng kích thước bước hiệu dụng.

### 3. **Giai đoạn Khởi động (Warm-up)**
Có thể khởi đầu với hệ số momentum nhỏ rồi tăng dần để thuật toán tích lũy vận tốc ổn định hơn ở những vòng lặp đầu.

## Phân tích Toán học

### Tính chất Hội tụ

Đối với hàm lồi mạnh có gradient liên tục Lipschitz (và chọn tham số phù hợp trên lớp hàm bậc hai), gradient descent có momentum đạt được:
- **Hội tụ tuyến tính**: $$f(x^{(k)}) - f^* \leq C \rho^k$$ với một hằng số $$\rho < 1$$.
- **Cải thiện sự phụ thuộc vào chỉ số điều kiện**: Tốc độ phụ thuộc vào $$\sqrt{\kappa}$$ thay vì $$\kappa$$ như gradient descent chuẩn.

### Liên hệ với Phương pháp Quả cầu Nặng (Heavy Ball)

Gradient descent có momentum gắn chặt với phương trình vi phân chuyển động của quả cầu nặng có ma sát trong cơ học cổ điển:
$$mx'' + \gamma x' + \nabla f(x) = 0$$

Khi rời rạc hóa phương trình vi phân này theo thời gian, ta thu được quy tắc cập nhật momentum.

### Momentum và Nesterov trong khoảng 4 phút

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/momentum-nesterov_vi.mp4"></video>
</div>

Heavy ball và Nesterov trên thung lũng ½(w₁² + 100w₂²): đếm số bước, quét β, và trường hợp Nesterov phân kỳ khi η quá lớn.

## Tóm tắt So sánh

| Khía cạnh | Vanilla GD | Momentum GD |
|--------|------------|-------------|
| **Bộ nhớ** | Không | Có (trọng số giảm mũ) |
| **Hội tụ** | Có thể chậm | Thường nhanh hơn |
| **Dao động** | Dễ xảy ra hơn | Giảm đáng kể |
| **Cực tiểu cục bộ** | Dễ bị giữ lại | Có khả năng vượt qua tốt hơn |
| **Siêu tham số** | Tốc độ học | Tốc độ học + hệ số momentum |
| **Chi phí tính toán** | Thấp | Cao hơn không đáng kể |

## Những Điểm Chính

1. **Bổ sung quán tính**: Momentum lưu giữ thông tin về hướng cập nhật của các bước trước.
2. **Tăng tốc hội tụ**: Đặc biệt hữu ích trên các hàm có thung lũng hẹp hoặc chỉ số điều kiện lớn.
3. **Giảm dao động**: Làm mượt quỹ đạo zig-zag dọc theo các phương có độ cong lớn.
4. **Tính ứng dụng rộng**: Là nền tảng của nhiều bộ tối ưu hiện đại trong học máy và học sâu.
5. **Linh hoạt điều chỉnh**: Hệ số $$\beta$$ cho phép cân bằng giữa tốc độ tích lũy vận tốc và độ ổn định.

Tóm lại, momentum là một cải tiến đơn giản nhưng hiệu quả đối với gradient descent và vẫn giữ vai trò quan trọng trong các hệ thống tối ưu hóa hiện đại.
