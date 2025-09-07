---
layout: post
title: 06-05 Stochastic gradient descent
chapter: '06'
order: 15
owner: Kyeongmin Woo
categories:
- chapter06
lang: vi
lesson_type: required
---

<script src="../../../public/js/script.js"></script>
<script src="https://d3js.org/d3.v7.min.js"></script>

## Động lực: Thử thách của Big Data

Hãy tưởng tượng bạn đang huấn luyện một mô hình machine learning trên hàng triệu điểm dữ liệu. Gradient descent truyền thống yêu cầu tính toán gradient cho **tất cả** các điểm dữ liệu trước khi thực hiện một lần cập nhật duy nhất. Điều này trở nên tốn kém về mặt tính toán và tiêu tốn bộ nhớ đối với các tập dữ liệu lớn.

**Câu hỏi**: Điều gì sẽ xảy ra nếu chúng ta có thể tiến bộ bằng cách chỉ xem xét một điểm dữ liệu tại một thời điểm?

## Nền tảng Toán học

Xem xét bài toán tối ưu hóa để tối thiểu hóa một tổng các hàm:

$$ \begin{equation}
\min_x f(x) = \min_x \sum_{i=1}^m f_i(x)
\end{equation} $$

**Diễn giải thực tế**: Trong machine learning, $$f_i(x)$$ thường đại diện cho mất mát trên ví dụ huấn luyện thứ $$i$$, trong đó $$x$$ là các tham số mô hình.

### Batch Gradient Descent (Phương pháp Truyền thống)

Gradient của tổng bằng tổng các gradient:
$$\nabla f(x) = \nabla \sum_{i=1}^m f_i(x) = \sum_{i=1}^m \nabla f_i(x)$$

Quy tắc cập nhật trở thành:
$$ \begin{equation}
x^{(k)} = x^{(k-1)} - t_k \cdot \sum_{i=1}^{m} \nabla f_i (x^{(k-1)}), \,  k=1,2,3,\dots
\end{equation} $$

**Chi phí tính toán**: $$O(m)$$ lần đánh giá gradient mỗi lần lặp, trong đó $$m$$ là số lượng hàm (hoặc điểm dữ liệu).

## Stochastic Gradient Descent: Giải pháp thay thế hiệu quả

**Ý tưởng chính**: Thay vì tính toán gradient cho tất cả $$m$$ hàm, SGD chỉ sử dụng **một** hàm tại mỗi lần lặp.

$$ \begin{equation}
x^{(k)} = x^{(k-1)} - t_k \cdot \nabla f_{i_k} (x^{(k-1)}), \quad i_k \in \{1,2,\dots,m\}
\end{equation} $$

**Chi phí tính toán**: $$O(1)$$ lần đánh giá gradient mỗi lần lặp - một cải thiện to lớn!

### Interactive Visualization: GD vs SGD with Step Control

<div id="gd-sgd-comparison" style="margin: 20px 0;">
    <!-- Parameter Controls -->
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 20px; margin-bottom: 15px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; background-color: #f9f9f9;">
        <div>
            <label for="learning-rate">Learning Rate: </label>
            <input type="range" id="learning-rate" min="0.01" max="0.5" step="0.01" value="0.1">
            <span id="lr-value">0.1</span>
        </div>
        <div>
            <label for="num-functions">Number of Functions (m): </label>
            <input type="range" id="num-functions" min="3" max="10" step="1" value="5">
            <span id="m-value">5</span>
        </div>
        <div>
            <label for="animation-speed">Animation Speed: </label>
            <input type="range" id="animation-speed" min="1" max="10" step="1" value="5">
            <span id="speed-value">5</span>
        </div>
    </div>
    
    <!-- Execution Mode Selection -->
    <div style="margin-bottom: 15px; padding: 10px; border: 1px solid #ddd; border-radius: 5px; background-color: #f0f8ff;">
        <h4 style="margin: 0 0 10px 0;">Execution Mode:</h4>
        <div style="display: flex; gap: 15px;">
            <label><input type="radio" name="exec-mode" value="auto" checked> Auto Run</label>
            <label><input type="radio" name="exec-mode" value="manual"> Manual Step-by-Step</label>
        </div>
    </div>
    
    <!-- Control Buttons -->
    <div style="display: flex; gap: 10px; margin-bottom: 15px; flex-wrap: wrap;">
        <button id="start-gd" style="background-color: #4CAF50; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Start Gradient Descent</button>
        <button id="start-sgd" style="background-color: #FF9800; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Start SGD</button>
        <button id="pause-resume" style="background-color: #2196F3; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;" disabled>Pause</button>
        <button id="step-forward" style="background-color: #9C27B0; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;" disabled>Step Forward</button>
        <button id="reset-demo" style="background-color: #f44336; color: white; border: none; padding: 8px 16px; border-radius: 4px; cursor: pointer;">Reset</button>
    </div>
    
    <!-- Algorithm Status -->
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 15px;">
        <div style="padding: 10px; border: 1px solid #4CAF50; border-radius: 5px; background-color: #f1f8e9;">
            <h4 style="margin: 0 0 5px 0; color: #4CAF50;">Gradient Descent Status</h4>
            <p id="gd-detailed-info" style="margin: 0; font-size: 14px;">Ready to start</p>
        </div>
        <div style="padding: 10px; border: 1px solid #FF9800; border-radius: 5px; background-color: #fff8e1;">
            <h4 style="margin: 0 0 5px 0; color: #FF9800;">SGD Status</h4>
            <p id="sgd-detailed-info" style="margin: 0; font-size: 14px;">Ready to start</p>
        </div>
    </div>
    
    <!-- Visualization Plots -->
    <div style="display: flex; gap: 20px; justify-content: center;">
        <div style="text-align: center;">
            <h4>Gradient Descent (Batch)</h4>
            <svg id="gd-plot" width="350" height="350" style="border: 1px solid #ddd;"></svg>
            <div style="margin-top: 10px; padding: 8px; background-color: #f5f5f5; border-radius: 4px;">
                <p id="gd-info" style="margin: 0; font-weight: bold;">Iterations: 0, Cost: 0</p>
                <p id="gd-gradient-info" style="margin: 5px 0 0 0; font-size: 12px; color: #666;">Gradient: [0, 0]</p>
            </div>
        </div>
        <div style="text-align: center;">
            <h4>Stochastic Gradient Descent</h4>
            <svg id="sgd-plot" width="350" height="350" style="border: 1px solid #ddd;"></svg>
            <div style="margin-top: 10px; padding: 8px; background-color: #f5f5f5; border-radius: 4px;">
                <p id="sgd-info" style="margin: 0; font-weight: bold;">Iterations: 0, Cost: 0</p>
                <p id="sgd-gradient-info" style="margin: 5px 0 0 0; font-size: 12px; color: #666;">Selected Function: -, Gradient: [0, 0]</p>
            </div>
        </div>
    </div>
    
    <!-- Progress Visualization -->
    <div style="margin-top: 20px; padding: 15px; border: 1px solid #ddd; border-radius: 5px; background-color: #fafafa;">
        <h4>Convergence Progress</h4>
        <div style="display: flex; gap: 20px;">
            <div style="flex: 1;">
                <p><strong>GD Progress:</strong></p>
                <div style="width: 100%; background-color: #e0e0e0; border-radius: 10px; height: 20px;">
                    <div id="gd-progress" style="width: 0%; background-color: #4CAF50; height: 100%; border-radius: 10px; transition: width 0.3s;"></div>
                </div>
            </div>
            <div style="flex: 1;">
                <p><strong>SGD Progress:</strong></p>
                <div style="width: 100%; background-color: #e0e0e0; border-radius: 10px; height: 20px;">
                    <div id="sgd-progress" style="width: 0%; background-color: #FF9800; height: 100%; border-radius: 10px; transition: width 0.3s;"></div>
                </div>
            </div>
        </div>
    </div>
</div>

### Các chiến lược lựa chọn cho SGD

Chỉ số hàm $$i_k$$ có thể được chọn bằng các chiến lược khác nhau:

#### 1. Quy tắc vòng tròn (Cyclic Rule)
**Mẫu**: $$i_k = 1,2,\dots,m, 1,2,\dots,m, \ldots$$
- **Ưu điểm**: Có tính quyết định, đảm bảo tất cả các hàm đều được thăm
- **Nhược điểm**: Có thể bị kẹt trong các mẫu tuần hoàn

#### 2. Quy tắc ngẫu nhiên (Randomized Rule)
**Mẫu**: $$i_k$$ được chọn ngẫu nhiên đều từ $$\{1,2,\dots,m\}$$
- **Ưu điểm**: Tránh các mẫu tuần hoàn, đảm bảo lý thuyết tốt hơn
- **Nhược điểm**: Một số hàm có thể được thăm thường xuyên hơn những hàm khác

**Trong thực tế**: Lựa chọn ngẫu nhiên được ưa chuộng hơn do có tính chất hội tụ tốt hơn và khả năng thoát khỏi các mẫu cục bộ.

## Phân tích hội tụ: Lý thuyết so với Thực tế

### So sánh Toán học

**Batch GD (một epoch)**: 
$$x^{(k+1)} = x^{(k)} - t_k \cdot \sum_{i=1}^{m} \nabla f_i (x^{(k)})$$

**SGD (một epoch với quy tắc vòng tròn)**:
$$x^{(k+m)} = x^{(k)} - t_k \cdot \sum_{i=1}^{m} \nabla f_i (x^{(k+i-1)})$$

### Hiểu công thức quy tắc vòng tròn SGD

Hãy phân tích công thức này từng bước để hiểu điều gì xảy ra trong một epoch hoàn chỉnh của SGD với quy tắc vòng tròn:

**Epoch là gì?** Một epoch có nghĩa là chúng ta đã xử lý tất cả $$m$$ hàm đúng một lần.

**Quy trình quy tắc vòng tròn:**
- Bắt đầu tại vị trí $$x^{(k)}$$
- **Bước 1**: Sử dụng hàm $$f_1$$, tính $$\nabla f_1(x^{(k)})$$, cập nhật thành $$x^{(k+1)}$$
- **Bước 2**: Sử dụng hàm $$f_2$$, tính $$\nabla f_2(x^{(k+1)})$$, cập nhật thành $$x^{(k+2)}$$
- **Bước 3**: Sử dụng hàm $$f_3$$, tính $$\nabla f_3(x^{(k+2)})$$, cập nhật thành $$x^{(k+3)}$$
- ...
- **Bước m**: Sử dụng hàm $$f_m$$, tính $$\nabla f_m(x^{(k+m-1)})$$, cập nhật thành $$x^{(k+m)}$$

**Các cập nhật SGD riêng lẻ:**
$$\begin{align}
x^{(k+1)} &= x^{(k)} - t_k \nabla f_1(x^{(k)}) \\
x^{(k+2)} &= x^{(k+1)} - t_k \nabla f_2(x^{(k+1)}) \\
x^{(k+3)} &= x^{(k+2)} - t_k \nabla f_3(x^{(k+2)}) \\
&\vdots \\
x^{(k+m)} &= x^{(k+m-1)} - t_k \nabla f_m(x^{(k+m-1)})
\end{align}$$

**Thu gọn các cập nhật:**
Nếu chúng ta thay thế đệ quy và thu thập tất cả các số hạng, chúng ta được:
$$x^{(k+m)} = x^{(k)} - t_k \left[ \nabla f_1(x^{(k)}) + \nabla f_2(x^{(k+1)}) + \cdots + \nabla f_m(x^{(k+m-1)}) \right]$$

This can be written compactly as:
$$x^{(k+m)} = x^{(k)} - t_k \cdot \sum_{i=1}^{m} \nabla f_i (x^{(k+i-1)})$$

**Ý tưởng chính:** Mỗi gradient $$\nabla f_i$$ được đánh giá tại một vị trí **khác nhau** $$x^{(k+i-1)}$$, không phải tại cùng vị trí bắt đầu $$x^{(k)}$$.

**Key difference in update directions**:
$$\sum_{i=1}^{m}[ \nabla f_i (x^{(k+i-1)}) - \nabla f_i (x^{(k)})]$$

This difference represents how much the SGD path deviates from what batch GD would do. If the functions don't change much locally (Lipschitz continuous gradients), this difference is small and SGD behaves similarly to batch GD.

### Concrete Example with m = 3 Functions

Let's illustrate with $$m = 3$$ functions to make this crystal clear:

**Starting position:** $$x^{(k)} = [1, 2]$$

**SGD Cyclic Rule Process:**
1. **Use $$f_1$$**: Compute $$\nabla f_1(x^{(k)}) = \nabla f_1([1,2])$$, update:
   $$x^{(k+1)} = x^{(k)} - t_k \nabla f_1(x^{(k)}) = [1,2] - t_k \nabla f_1([1,2])$$
   
2. **Use $$f_2$$**: Compute $$\nabla f_2(x^{(k+1)})$$ at the **new** position, update:
   $$x^{(k+2)} = x^{(k+1)} - t_k \nabla f_2(x^{(k+1)})$$
   
3. **Use $$f_3$$**: Compute $$\nabla f_3(x^{(k+2)})$$ at the **newest** position, update:
   $$x^{(k+3)} = x^{(k+2)} - t_k \nabla f_3(x^{(k+2)})$$

**Final SGD result after one epoch:**
$$x^{(k+3)} = x^{(k)} - t_k[\nabla f_1(x^{(k)}) + \nabla f_2(x^{(k+1)}) + \nabla f_3(x^{(k+2)})]$$

**Compare with Batch GD:**
$$x^{(k+1)} = x^{(k)} - t_k[\nabla f_1(x^{(k)}) + \nabla f_2(x^{(k)}) + \nabla f_3(x^{(k)})]$$

**The crucial difference:** 
- **Batch GD**: All gradients evaluated at the **same** starting point $$x^{(k)}$$
- **SGD**: Each gradient evaluated at a **different** point along the optimization path

This is why SGD can make faster initial progress (it's already "exploring" the landscape) but can be noisier near the optimum.

### Convergence Properties

<div id="convergence-analysis" style="margin: 20px 0;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
        <div style="border: 1px solid #ddd; padding: 15px; border-radius: 5px;">
            <h4>Batch Gradient Descent</h4>
            <ul>
                <li><strong>Direction</strong>: Always in steepest descent direction</li>
                <li><strong>Convergence</strong>: Smooth, monotonic decrease</li>
                <li><strong>Speed</strong>: Slower per epoch, but stable</li>
                <li><strong>Memory</strong>: Requires full dataset in memory</li>
            </ul>
        </div>
        <div style="border: 1px solid #ddd; padding: 15px; border-radius: 5px;">
            <h4>Stochastic Gradient Descent</h4>
            <ul>
                <li><strong>Direction</strong>: Noisy, approximate descent direction</li>
                <li><strong>Convergence</strong>: Oscillatory, but faster initial progress</li>
                <li><strong>Speed</strong>: Faster per epoch, especially for large datasets</li>
                <li><strong>Memory</strong>: Processes one sample at a time</li>
            </ul>
        </div>
    </div>
</div>

### Theoretical Guarantees

**Lipschitz Continuity Condition**: If $$\nabla f_i(x)$$ is Lipschitz continuous with constant $$L$$:
$$\|\nabla f_i(x) - \nabla f_i(y)\| \leq L \|x - y\|$$

Then SGD converges to the same optimal solution as batch GD, provided the learning rate satisfies appropriate conditions.

**Practical Observation**: 
- SGD excels in the **exploration phase** (far from optimum)
- SGD struggles in the **exploitation phase** (near optimum) due to noise

## Mini-Batch Gradient Descent: The Best of Both Worlds

A compromise between batch GD and SGD uses **mini-batches** of size $$b$$:

$$x^{(k)} = x^{(k-1)} - t_k \cdot \frac{1}{b} \sum_{i \in \mathcal{B}_k} \nabla f_i (x^{(k-1)})$$

where $$\mathcal{B}_k$$ is a mini-batch of $$b$$ randomly selected indices.

<div id="minibatch-comparison" style="margin: 20px 0;">
    <h4>Comparison: Batch vs Mini-batch vs SGD</h4>
    <table style="width: 100%; border-collapse: collapse; margin: 15px 0;">
        <thead>
            <tr style="background-color: #f5f5f5;">
                <th style="border: 1px solid #ddd; padding: 10px;">Method</th>
                <th style="border: 1px solid #ddd; padding: 10px;">Batch Size</th>
                <th style="border: 1px solid #ddd; padding: 10px;">Computation/Update</th>
                <th style="border: 1px solid #ddd; padding: 10px;">Convergence</th>
                <th style="border: 1px solid #ddd; padding: 10px;">Memory Usage</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="border: 1px solid #ddd; padding: 10px;"><strong>Batch GD</strong></td>
                <td style="border: 1px solid #ddd; padding: 10px;">$$m$$ (full dataset)</td>
                <td style="border: 1px solid #ddd; padding: 10px;">$$O(m)$$</td>
                <td style="border: 1px solid #ddd; padding: 10px;">Smooth, stable</td>
                <td style="border: 1px solid #ddd; padding: 10px;">High</td>
            </tr>
            <tr>
                <td style="border: 1px solid #ddd; padding: 10px;"><strong>Mini-batch GD</strong></td>
                <td style="border: 1px solid #ddd; padding: 10px;">$$b$$ (typically 32-256)</td>
                <td style="border: 1px solid #ddd; padding: 10px;">$$O(b)$$</td>
                <td style="border: 1px solid #ddd; padding: 10px;">Balanced</td>
                <td style="border: 1px solid #ddd; padding: 10px;">Medium</td>
            </tr>
            <tr>
                <td style="border: 1px solid #ddd; padding: 10px;"><strong>SGD</strong></td>
                <td style="border: 1px solid #ddd; padding: 10px;">1</td>
                <td style="border: 1px solid #ddd; padding: 10px;">$$O(1)$$</td>
                <td style="border: 1px solid #ddd; padding: 10px;">Fast but noisy</td>
                <td style="border: 1px solid #ddd; padding: 10px;">Low</td>
            </tr>
        </tbody>
    </table>
</div>

## Những điểm chính và Hiểu biết thực tế

### Khi nào sử dụng SGD
1. **Tập dữ liệu lớn** (hàng triệu mẫu)
2. **Các tình huống học trực tuyến**
3. **Môi trường bộ nhớ hạn chế**
4. **Các giai đoạn huấn luyện đầu** để tiến bộ nhanh

### Khi nào sử dụng Batch GD
1. **Tập dữ liệu nhỏ đến trung bình**
2. **Yêu cầu độ chính xác cao**
3. **Cần hội tụ ổn định**
4. **Các giai đoạn tinh chỉnh cuối cùng**

### Thực hành tốt nhất
- **Lập lịch tốc độ học**: Bắt đầu cao, giảm dần theo thời gian
- **Xáo trộn**: Ngẫu nhiên hóa thứ tự dữ liệu mỗi epoch
- **Mini-batch**: Thường là lựa chọn thực tế tốt nhất
- **Momentum**: Giúp SGD vượt qua nhiễu và tăng tốc hội tụ

**Thực tế hiện đại**: Hầu hết các framework deep learning sử dụng mini-batch SGD với các optimizer tinh vi (Adam, RMSprop) tự động điều chỉnh tốc độ học.

<script>
document.addEventListener('DOMContentLoaded', function() {
    // Global variables for demos
    let gdData = [], sgdData = [];
    let gdPosition = [2, 2], sgdPosition = [2, 2];
    let isRunning = false;
    let isPaused = false;
    let isManualMode = false;
    let animationId;
    let currentAlgorithm = null; // 'gd' or 'sgd'
    let algorithmState = {
        gd: { iteration: 0, position: [2, 2], path: [], functions: [], totalCost: 0, gradient: [0, 0] },
        sgd: { iteration: 0, position: [2, 2], path: [], functions: [], totalCost: 0, gradient: [0, 0], selectedFunc: -1 }
    };
    
    // Initialize sliders
    const learningRateSlider = document.getElementById('learning-rate');
    const numFunctionsSlider = document.getElementById('num-functions');
    const animationSpeedSlider = document.getElementById('animation-speed');
    const lrValue = document.getElementById('lr-value');
    const mValue = document.getElementById('m-value');
    const speedValue = document.getElementById('speed-value');
    
    if (learningRateSlider) {
        learningRateSlider.addEventListener('input', function() {
            lrValue.textContent = this.value;
        });
    }
    
    if (numFunctionsSlider) {
        numFunctionsSlider.addEventListener('input', function() {
            mValue.textContent = this.value;
        });
    }
    
    if (animationSpeedSlider) {
        animationSpeedSlider.addEventListener('input', function() {
            speedValue.textContent = this.value;
        });
    }
    
    // Execution mode radio buttons
    const execModeRadios = document.querySelectorAll('input[name="exec-mode"]');
    execModeRadios.forEach(radio => {
        radio.addEventListener('change', function() {
            isManualMode = this.value === 'manual';
            updateControlButtons();
        });
    });
    
    // Simple quadratic functions for demonstration
    function createFunctions(m) {
        const functions = [];
        for (let i = 0; i < m; i++) {
            const centerX = (Math.random() - 0.5) * 4;
            const centerY = (Math.random() - 0.5) * 4;
            functions.push({
                center: [centerX, centerY],
                gradient: function(x, y) {
                    return [2 * (x - centerX), 2 * (y - centerY)];
                },
                value: function(x, y) {
                    return (x - centerX) ** 2 + (y - centerY) ** 2;
                }
            });
        }
        return functions;
    }
    
    // Setup SVG plots
    function setupPlot(svgId, width = 300, height = 300) {
        const svg = d3.select(`#${svgId}`);
        if (svg.empty()) return null;
        
        svg.selectAll("*").remove();
        
        const margin = {top: 20, right: 20, bottom: 30, left: 40};
        const plotWidth = width - margin.left - margin.right;
        const plotHeight = height - margin.top - margin.bottom;
        
        const xScale = d3.scaleLinear()
            .domain([-3, 3])
            .range([0, plotWidth]);
            
        const yScale = d3.scaleLinear()
            .domain([-3, 3])
            .range([plotHeight, 0]);
        
        const g = svg.append("g")
            .attr("transform", `translate(${margin.left},${margin.top})`);
        
        // Add axes
        g.append("g")
            .attr("transform", `translate(0,${plotHeight})`)
            .call(d3.axisBottom(xScale));
            
        g.append("g")
            .call(d3.axisLeft(yScale));
        
        // Add contour background
        const contourData = [];
        for (let i = 0; i < 20; i++) {
            for (let j = 0; j < 20; j++) {
                const x = -3 + (i / 19) * 6;
                const y = -3 + (j / 19) * 6;
                contourData.push({x, y, z: x*x + y*y});
            }
        }
        
        return {svg, g, xScale, yScale, plotWidth, plotHeight};
    }
    
    // Control button functions
    function updateControlButtons() {
        const pauseResumeBtn = document.getElementById('pause-resume');
        const stepForwardBtn = document.getElementById('step-forward');
        
        if (pauseResumeBtn) {
            pauseResumeBtn.disabled = !isRunning;
            pauseResumeBtn.textContent = isPaused ? 'Resume' : 'Pause';
        }
        
        if (stepForwardBtn) {
            stepForwardBtn.disabled = !isManualMode && !isPaused;
        }
    }
    
    // GD vs SGD Comparison Demo
    const startGDBtn = document.getElementById('start-gd');
    const startSGDBtn = document.getElementById('start-sgd');
    const pauseResumeBtn = document.getElementById('pause-resume');
    const stepForwardBtn = document.getElementById('step-forward');
    const resetBtn = document.getElementById('reset-demo');
    
    if (startGDBtn) {
        startGDBtn.addEventListener('click', function() {
            if (isRunning && currentAlgorithm === 'gd') return;
            initializeAlgorithm('gd');
            if (!isManualMode) {
                runAlgorithm('gd');
            }
        });
    }
    
    if (startSGDBtn) {
        startSGDBtn.addEventListener('click', function() {
            if (isRunning && currentAlgorithm === 'sgd') return;
            initializeAlgorithm('sgd');
            if (!isManualMode) {
                runAlgorithm('sgd');
            }
        });
    }
    
    if (pauseResumeBtn) {
        pauseResumeBtn.addEventListener('click', function() {
            if (isPaused) {
                isPaused = false;
                if (currentAlgorithm) {
                    runAlgorithm(currentAlgorithm);
                }
            } else {
                isPaused = true;
                if (animationId) {
                    cancelAnimationFrame(animationId);
                }
            }
            updateControlButtons();
        });
    }
    
    if (stepForwardBtn) {
        stepForwardBtn.addEventListener('click', function() {
            if (currentAlgorithm && (isManualMode || isPaused)) {
                performSingleStep(currentAlgorithm);
            }
        });
    }
    
    if (resetBtn) {
        resetBtn.addEventListener('click', function() {
            resetDemo();
        });
    }
    
    // Initialize algorithm state
    function initializeAlgorithm(algorithm) {
        const m = parseInt(numFunctionsSlider.value);
        const functions = createFunctions(m);
        
        algorithmState[algorithm] = {
            iteration: 0,
            position: [2, 2],
            path: [[2, 2]],
            functions: functions,
            totalCost: 0,
            gradient: [0, 0],
            selectedFunc: algorithm === 'sgd' ? -1 : undefined
        };
        
        currentAlgorithm = algorithm;
        isRunning = true;
        isPaused = false;
        
        // Setup plot
        const plotId = algorithm === 'gd' ? 'gd-plot' : 'sgd-plot';
        const plot = setupPlot(plotId, 350, 350);
        
        // Update status
        updateAlgorithmDisplay(algorithm);
        updateControlButtons();
        
        // Update detailed info
        const detailedInfoId = algorithm === 'gd' ? 'gd-detailed-info' : 'sgd-detailed-info';
        document.getElementById(detailedInfoId).textContent = 
            isManualMode ? 'Ready for manual stepping' : 'Running automatically...';
    }
    
    // Run algorithm in auto mode
    function runAlgorithm(algorithm) {
        if (isPaused || isManualMode) return;
        
        const speed = parseInt(animationSpeedSlider.value);
        const delay = 1100 - speed * 100; // Convert speed to delay (higher speed = lower delay)
        
        function step() {
            if (isPaused || !isRunning) return;
            
            const shouldContinue = performSingleStep(algorithm);
            
            if (shouldContinue && !isPaused) {
                setTimeout(() => {
                    animationId = requestAnimationFrame(step);
                }, delay);
            } else {
                isRunning = false;
                updateControlButtons();
                
                const detailedInfoId = algorithm === 'gd' ? 'gd-detailed-info' : 'sgd-detailed-info';
                document.getElementById(detailedInfoId).textContent = 'Converged!';
            }
        }
        
        step();
    }
    
    // Perform a single step of the algorithm
    function performSingleStep(algorithm) {
        const state = algorithmState[algorithm];
        const lr = parseFloat(learningRateSlider.value);
        
        if (algorithm === 'gd') {
            return performGDStep(state, lr);
        } else {
            return performSGDStep(state, lr);
        }
    }
    
    function performGDStep(state, lr) {
        // Compute full gradient (sum of all function gradients)
        let gradX = 0, gradY = 0;
        for (const func of state.functions) {
            const grad = func.gradient(state.position[0], state.position[1]);
            gradX += grad[0];
            gradY += grad[1];
        }
        
        // Average the gradients
        gradX /= state.functions.length;
        gradY /= state.functions.length;
        
        state.gradient = [gradX, gradY];
        
        // Update position
        state.position[0] -= lr * gradX;
        state.position[1] -= lr * gradY;
        state.path.push(state.position.slice());
        
        // Compute total cost
        state.totalCost = 0;
        for (const func of state.functions) {
            state.totalCost += func.value(state.position[0], state.position[1]);
        }
        state.totalCost /= state.functions.length;
        
        state.iteration++;
        
        // Update visualization
        updateAlgorithmDisplay('gd');
        
        // Check convergence
        const gradientMagnitude = Math.sqrt(gradX * gradX + gradY * gradY);
        return state.iteration < 100 && gradientMagnitude > 0.01;
    }
    
    function performSGDStep(state, lr) {
        // Select random function
        const funcIndex = Math.floor(Math.random() * state.functions.length);
        const func = state.functions[funcIndex];
        state.selectedFunc = funcIndex;
        
        // Compute gradient for selected function only
        const grad = func.gradient(state.position[0], state.position[1]);
        state.gradient = grad;
        
        // Update position
        state.position[0] -= lr * grad[0];
        state.position[1] -= lr * grad[1];
        state.path.push(state.position.slice());
        
        // Compute total cost
        state.totalCost = 0;
        for (const func of state.functions) {
            state.totalCost += func.value(state.position[0], state.position[1]);
        }
        state.totalCost /= state.functions.length;
        
        state.iteration++;
        
        // Update visualization
        updateAlgorithmDisplay('sgd');
        
        // Check convergence (SGD needs more iterations)
        return state.iteration < 300 && state.totalCost > 0.01;
    }
    
    function updateAlgorithmDisplay(algorithm) {
        const state = algorithmState[algorithm];
        const plotId = algorithm === 'gd' ? 'gd-plot' : 'sgd-plot';
        const color = algorithm === 'gd' ? 'steelblue' : 'orange';
        
        // Update path visualization
        const plot = {
            svg: d3.select(`#${plotId}`),
            g: d3.select(`#${plotId} g`),
            xScale: d3.scaleLinear().domain([-3, 3]).range([0, 270]),
            yScale: d3.scaleLinear().domain([-3, 3]).range([270, 0])
        };
        
        if (!plot.g.empty()) {
            updatePath(plot, state.path, color);
        }
        
        // Update info displays
        const infoId = algorithm === 'gd' ? 'gd-info' : 'sgd-info';
        const gradientInfoId = algorithm === 'gd' ? 'gd-gradient-info' : 'sgd-gradient-info';
        
        document.getElementById(infoId).textContent = 
            `Iterations: ${state.iteration}, Cost: ${state.totalCost.toFixed(4)}`;
        
        if (algorithm === 'gd') {
            document.getElementById(gradientInfoId).textContent = 
                `Gradient: [${state.gradient[0].toFixed(3)}, ${state.gradient[1].toFixed(3)}]`;
        } else {
            document.getElementById(gradientInfoId).textContent = 
                `Selected Function: f${state.selectedFunc + 1}, Gradient: [${state.gradient[0].toFixed(3)}, ${state.gradient[1].toFixed(3)}]`;
        }
        
        // Update progress bar
        const progressId = algorithm === 'gd' ? 'gd-progress' : 'sgd-progress';
        const maxIterations = algorithm === 'gd' ? 100 : 300;
        const progress = Math.min((state.iteration / maxIterations) * 100, 100);
        document.getElementById(progressId).style.width = `${progress}%`;
        
        // Update detailed status
        const detailedInfoId = algorithm === 'gd' ? 'gd-detailed-info' : 'sgd-detailed-info';
        const gradMagnitude = Math.sqrt(state.gradient[0] ** 2 + state.gradient[1] ** 2);
        document.getElementById(detailedInfoId).textContent = 
            `Step ${state.iteration}: Position [${state.position[0].toFixed(3)}, ${state.position[1].toFixed(3)}], |∇| = ${gradMagnitude.toFixed(4)}`;
    }
    
    function updatePath(plot, path, color) {
        const line = d3.line()
            .x(d => plot.xScale(d[0]))
            .y(d => plot.yScale(d[1]));
        
        plot.g.selectAll('.path').remove();
        plot.g.append('path')
            .datum(path)
            .attr('class', 'path')
            .attr('fill', 'none')
            .attr('stroke', color)
            .attr('stroke-width', 2)
            .attr('d', line);
        
        // Add current position
        const current = path[path.length - 1];
        plot.g.selectAll('.current-pos').remove();
        plot.g.append('circle')
            .attr('class', 'current-pos')
            .attr('cx', plot.xScale(current[0]))
            .attr('cy', plot.yScale(current[1]))
            .attr('r', 5)
            .attr('fill', color);
    }
    
    function resetDemo() {
        if (animationId) {
            cancelAnimationFrame(animationId);
        }
        
        isRunning = false;
        isPaused = false;
        currentAlgorithm = null;
        
        // Reset algorithm states
        algorithmState = {
            gd: { iteration: 0, position: [2, 2], path: [], functions: [], totalCost: 0, gradient: [0, 0] },
            sgd: { iteration: 0, position: [2, 2], path: [], functions: [], totalCost: 0, gradient: [0, 0], selectedFunc: -1 }
        };
        
        // Clear plots
        d3.select('#gd-plot').selectAll("*").remove();
        d3.select('#sgd-plot').selectAll("*").remove();
        
        // Reset info displays
        document.getElementById('gd-info').textContent = 'Iterations: 0, Cost: 0';
        document.getElementById('sgd-info').textContent = 'Iterations: 0, Cost: 0';
        document.getElementById('gd-gradient-info').textContent = 'Gradient: [0, 0]';
        document.getElementById('sgd-gradient-info').textContent = 'Selected Function: -, Gradient: [0, 0]';
        
        // Reset detailed info
        document.getElementById('gd-detailed-info').textContent = 'Ready to start';
        document.getElementById('sgd-detailed-info').textContent = 'Ready to start';
        
        // Reset progress bars
        document.getElementById('gd-progress').style.width = '0%';
        document.getElementById('sgd-progress').style.width = '0%';
        
        // Update control buttons
        updateControlButtons();
    }
    
});
</script>
