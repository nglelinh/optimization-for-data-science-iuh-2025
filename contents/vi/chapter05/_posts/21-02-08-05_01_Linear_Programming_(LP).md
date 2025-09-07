---
layout: post
title: 05-01 Quy Hoạch Tuyến Tính (LP)
chapter: '05'
order: 2
owner: Hooncheol Shin
categories:
- chapter05
lang: vi
lesson_type: required
---

<script src="https://d3js.org/d3.v7.min.js"></script>
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>

Quy hoạch tuyến tính (LP) là một trong những kỹ thuật tối ưu hóa cơ bản và được sử dụng rộng rãi nhất trong toán học, kinh tế học và kỹ thuật. Hãy tưởng tượng bạn là một quản lý nhà máy đang cố gắng tối đa hóa lợi nhuận trong khi phải đối phó với các tài nguyên hạn chế - đây chính xác là loại bài toán mà LP được thiết kế để giải quyết!

### Điều gì làm cho một bài toán "Tuyến tính"?

Một bài toán là tuyến tính khi:
- **Hàm mục tiêu** (thứ bạn muốn tối ưu hóa) có mối quan hệ đường thẳng
- Tất cả **ràng buộc** (giới hạn) cũng có mối quan hệ đường thẳng
- Không có biến nào được nhân với nhau (không có các số hạng $$x_1 \cdot x_2$$)
- Không có biến nào xuất hiện trong số mũ hoặc dưới căn bậc hai

### Ví dụ Đơn giản: Bài toán của Nông dân

Hãy bắt đầu với một ví dụ trực quan. Một nông dân có 100 mẫu đất và muốn trồng ngô và lúa mì để tối đa hóa lợi nhuận:

- **Ngô**: Lợi nhuận $300 mỗi mẫu, cần 2 giờ lao động mỗi mẫu
- **Lúa mì**: Lợi nhuận $200 mỗi mẫu, cần 1 giờ lao động mỗi mẫu  
- **Lao động có sẵn**: Tổng cộng 150 giờ

**Câu hỏi**: Nông dân nên trồng bao nhiêu mẫu mỗi loại cây trồng?

<div id="farmer-problem-viz" style="margin: 20px 0;"></div>

<div class="content-box exercise-box">
<strong>Bài tập Tương tác:</strong> Sử dụng các thanh trượt bên dưới để khám phá các tổ hợp khác nhau của ngô và lúa mì. Quan sát cách lợi nhuận thay đổi và liệu các ràng buộc có được thỏa mãn hay không!

<div style="margin: 10px 0;">
  <label for="corn-acres">Số mẫu ngô: <span id="corn-value">50</span></label><br>
  <input type="range" id="corn-acres" min="0" max="100" value="50" style="width: 300px;">
</div>

<div style="margin: 10px 0;">
  <label for="wheat-acres">Số mẫu lúa mì: <span id="wheat-value">50</span></label><br>
  <input type="range" id="wheat-acres" min="0" max="100" value="50" style="width: 300px;">
</div>

<div id="farmer-results" style="margin-top: 15px; font-family: monospace;">
  <div>Tổng diện tích sử dụng: <span id="land-used">100</span> / 100 mẫu</div>
  <div>Tổng lao động sử dụng: <span id="labor-used">150</span> / 150 giờ</div>
  <div>Tổng lợi nhuận: $<span id="total-profit">25000</span></div>
  <div id="feasibility-status" style="font-weight: bold; color: green;">✓ Nghiệm khả thi</div>
</div>
</div>

Bây giờ hãy chính thức hóa trực giác này. Nếu cả hàm mục tiêu và các hàm ràng buộc đều là affine, bài toán tối ưu được gọi là *chương trình tuyến tính* (LP). Chương trình tuyến tính tổng quát được phát biểu như sau:

### LP Tổng quát

>$$ \begin{align}
>    &\text{minimize}_{x} &&{c^T x + d} \\\\
>    &\text{subject to } &&{Gx \preceq h}\\\\
>    & &&{Ax = b},\\\\
>    &\text{where } &&G \in \mathbb{R}^{m \times n} \text{ and } A \in \mathbb{R}^{p \times n}.
>\end{align} $$

* Hằng số $$+d$$ trong hàm mục tiêu không ảnh hưởng đến quá trình tối ưu hóa hoặc kết quả và có thể bỏ qua.
* Nếu bạn muốn tối đa hóa $$c^T x + d$$ dưới cùng các ràng buộc, bạn có thể tương đương tối thiểu hóa $$-c^T x - d$$.
* Bài toán trên tìm nghiệm tối ưu $$x^*$$ của hàm affine $$c^T x + d$$ trên một tập khả thi đa diện.

### Giải thích Hình học

Sức mạnh của quy hoạch tuyến tính trở nên rõ ràng khi chúng ta trực quan hóa nó theo hình học. Mỗi ràng buộc định nghĩa một nửa không gian, và vùng khả thi là giao của tất cả các nửa không gian này - tạo thành một **đa diện**.

<div class="content-box insight-box">
<strong>Thông tin quan trọng:</strong> Nghiệm tối ưu của một chương trình tuyến tính luôn xuất hiện tại một <strong>đỉnh</strong> (góc) của vùng khả thi! Đây là lý do tại sao phương pháp simplex hoạt động bằng cách di chuyển từ đỉnh này sang đỉnh khác.
</div>

<div id="geometric-lp-viz" style="margin: 20px 0; text-align: center;"></div>

<figure class="image" style="align: center;">
<p align="center">
  <img src="{{ site.baseurl  }}/img/chapter_img/chapter05/05_01_geometric_interpretation_of_LP.png" alt="[Fig1] Giải thích hình học của LP [1]" width="70%">
  <figcaption style="text-align: center;">[Fig1] Giải thích hình học truyền thống của LP [1]</figcaption>
</p>
</figure>

## LP ở Dạng chuẩn

Tại sao chúng ta cần một dạng chuẩn? Nhiều thuật toán LP (như phương pháp simplex) được thiết kế để làm việc với một định dạng cụ thể. Việc chuyển đổi về dạng chuẩn cho phép chúng ta sử dụng các thuật toán mạnh mẽ này một cách nhất quán.

### LP dạng chuẩn
>$$ \begin{align}
>    &\text{minimize}_{x} &&{c^T x + d} \\\\
>    &\text{subject to } &&{A x = b} \\\\
>    & &&{x \succeq 0}.
>\end{align} $$

**Đặc điểm chính của dạng chuẩn:**
- **Mục tiêu**: Luôn là tối thiểu hóa (các bài toán tối đa hóa được chuyển đổi bằng cách lấy âm)
- **Ràng buộc**: Chỉ có ràng buộc đẳng thức (bất đẳng thức được chuyển đổi sử dụng biến slack)
- **Biến**: Tất cả các biến phải không âm

<div class="content-box insight-box">
<strong>Tại sao Dạng chuẩn?</strong> 
<ul>
<li><strong>Hiệu quả thuật toán:</strong> Phương pháp Simplex làm việc trực tiếp trên dạng chuẩn</li>
<li><strong>Phân tích lý thuyết:</strong> Dễ dàng hơn để chứng minh các điều kiện tối ưu</li>
<li><strong>Triển khai phần mềm:</strong> Hầu hết các bộ giải LP mong đợi đầu vào dạng chuẩn</li>
</ul>
</div>

Tất cả các LP tổng quát đều có thể được chuyển đổi về dạng chuẩn sử dụng các bước sau:

### Chuyển đổi LP về dạng chuẩn
**Bước 1.** Sử dụng biến slack $$s$$ để chuyển đổi ràng buộc bất đẳng thức thành ràng buộc đẳng thức:
> $$ \begin{align}
>     &\text{minimize}_{x, s} &&{c^T x + d} \\\\
>     &\text{subject to } &&{Gx + s = h} \\\\
>     & &&{Ax = b},\\\\
>     & &&{s \succeq 0}.
> \end{align} $$

**Bước 2.** Thay thế mỗi biến $$x$$ bằng hai biến không âm:
$$ x = x^{+}  - x^{-} $$, trong đó $$ x^{+} \text{, } x^{-} \succeq 0 $$.

> $$ \begin{align}
>     &\text{minimize}_{x^{+}, x^{-}, s} &&{c^Tx^{+} - c^Tx^{-} + d} \\\\
>     &\text{subject to } &&{Gx^{+} - Gx^{-} + s = h} \\\\
>     & &&{Ax^{+} - Ax^{-} = b},\\\\
>     & &&{s \succeq 0}\\\\
>     & &&{x^{+} \succeq 0}, {x^{-} \succeq 0}.
> \end{align} $$

**Bước 3.** Định nghĩa $$ \tilde{x} $$, $$ \tilde{c} $$, $$ \tilde{b} $$, và $$ \tilde{A} $$ như sau:

> $$\tilde{x} =
> \begin{bmatrix}
> x^{+} \\\\
> x^{-} \\\\
> s
> \end{bmatrix}, 
> \tilde{c} =
> \begin{bmatrix}
> c \\\\
> -c \\\\
> 0
> \end{bmatrix},
> \tilde{b} =
> \begin{bmatrix}
> h \\\\
> b
> \end{bmatrix}
> $$, 
> $$
> \tilde{A} =
> \begin{bmatrix}
> G & -G & I\\\\
> A & -A & O
> \end{bmatrix}
> $$

**Bước 4.** Thế $$ \tilde{x} $$, $$ \tilde{c} $$, $$ \tilde{b} $$, và $$ \tilde{A} $$ vào bài toán từ Bước 2:

> $$ \begin{align}
>     &\text{minimize}_{\tilde{x}} &&{\tilde{c}^T \tilde{x} + d} \\\\
>     &\text{subject to} &&{\tilde{A} \tilde{x} = \tilde{b}} \\\\
>     & &&{\tilde{x} \succeq 0}.
> \end{align} $$

### Ví dụ - Chương trình chế độ ăn uống

Bài toán chế độ ăn uống là một ứng dụng kinh điển của quy hoạch tuyến tính, lần đầu tiên được nghiên cứu trong Thế chiến thứ hai để tìm cách nuôi dưỡng binh sĩ một cách kinh tế nhất trong khi vẫn đáp ứng các yêu cầu dinh dưỡng.

**Thiết lập bài toán:** Tìm sự kết hợp thức ăn rẻ nhất đáp ứng tất cả các yêu cầu dinh dưỡng.

> $$ \begin{align}
>     &\text{minimize}_{x} &&{c^T x} \\\\
>     &\text{subject to } &&{Dx \succeq d} \\\\
>     & &&{x \succeq 0}.
> \end{align} $$

**Biến và Tham số:**
* $$ c_j $$: Chi phí trên mỗi đơn vị thức phẩm j ($/đơn vị)
* $$ d_i $$: Lượng tiêu thụ tối thiểu khuyến nghị cho chất dinh dưỡng i (đơn vị/ngày)
* $$ D_{ij} $$: Lượng chất dinh dưỡng i trong thức phẩm j (đơn vị chất dinh dưỡng trên đơn vị thức phẩm)
* $$ x_j $$: Lượng thức phẩm j trong chế độ ăn uống (đơn vị/ngày)

<div class="content-box exercise-box">
<strong>Bộ Tối ưu hóa Chế độ ăn uống Tương tác:</strong> Hãy giải một bài toán chế độ ăn uống đơn giản với 3 loại thức phẩm và 2 chất dinh dưỡng!

<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 15px; margin: 15px 0;">
  <div style="text-align: center;">
    <strong>Bánh mì</strong><br>
    Chi phí: $2/ổ<br>
    Protein: 4g/ổ<br>
    Calories: 200/ổ
  </div>
  <div style="text-align: center;">
    <strong>Sữa</strong><br>
    Chi phí: $3/lít<br>
    Protein: 8g/lít<br>
    Calories: 150/lít
  </div>
  <div style="text-align: center;">
    <strong>Thịt</strong><br>
    Chi phí: $8/kg<br>
    Protein: 20g/kg<br>
    Calories: 300/kg
  </div>
</div>

<div style="margin: 15px 0;">
  <strong>Yêu cầu:</strong>
  <div>Protein tối thiểu: <input type="number" id="min-protein" value="20" min="10" max="50" style="width: 60px;"> gram/ngày</div>
  <div>Calories tối thiểu: <input type="number" id="min-calories" value="800" min="500" max="1500" style="width: 80px;"> calories/ngày</div>
</div>

<button id="solve-diet" style="background-color: #4CAF50; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Giải Bài toán Chế độ ăn uống</button>

<div id="diet-results" style="margin-top: 15px; font-family: monospace; background-color: #f9f9f9; padding: 10px; border-radius: 4px;">
  <div>Nhấp "Giải Bài toán Chế độ ăn uống" để xem nghiệm tối ưu!</div>
</div>
</div>

<div class="content-box insight-box">
<strong>Ứng dụng thực tế:</strong>
<ul>
<li><strong>Hậu cần quân sự:</strong> Nuôi quân đội một cách hiệu quả về chi phí</li>
<li><strong>Lập kế hoạch bữa ăn bệnh viện:</strong> Đáp ứng yêu cầu chế độ ăn uống của bệnh nhân</li>
<li><strong>Tối ưu hóa thức ăn gia súc:</strong> Dinh dưỡng gia súc với chi phí tối thiểu</li>
<li><strong>Chương trình bữa trưa học đường:</strong> Bữa ăn bổ dưỡng trong phạm vi ngân sách</li>
</ul>
</div>

## Thuật toán Simplex

**Thuật toán Simplex**, được phát triển bởi George Dantzig năm 1947, là một trong những thuật toán quan trọng nhất trong lịch sử tối ưu hóa. Nó đã cách mạng hóa quy hoạch tuyến tính bằng cách cung cấp một phương pháp hiệu quả để giải các bài toán LP một cách hệ thống.

### Tại sao Simplex hoạt động: Định lý Cơ bản

<div class="content-box insight-box">
<strong>Định lý Cơ bản của Quy hoạch Tuyến tính:</strong> Nếu một chương trình tuyến tính có nghiệm tối ưu, thì tồn tại một nghiệm tối ưu xuất hiện tại một đỉnh (cực điểm) của vùng khả thi.
</div>

Định lý này là thông tin quan trọng đằng sau thuật toán Simplex. Thay vì tìm kiếm toàn bộ vùng khả thi (có thể vô hạn), chúng ta chỉ cần kiểm tra số hữu hạn các đỉnh!

### How Simplex Works: The Strategy

The Simplex algorithm follows this elegant strategy:

1. **Start** at any vertex of the feasible region
2. **Check** if the current vertex is optimal  
3. **Move** to an adjacent vertex that improves the objective function
4. **Repeat** until no improvement is possible (optimal solution found)

### Simplex Algorithm Steps

Let's walk through the algorithm step by step using our standard form LP:

> $$ \begin{align}
>     &\text{minimize}_{x} &&{c^T x} \\\\
>     &\text{subject to } &&{A x = b} \\\\
>     & &&{x \succeq 0}.
> \end{align} $$

**Step 1: Initial Setup**
- Convert the LP to standard form (if not already)
- Find an initial basic feasible solution (vertex)
- Set up the simplex tableau

**Step 2: Optimality Test**
- Check if the current solution is optimal
- If all reduced costs are non-negative, we're done!

**Step 3: Choose Entering Variable**
- Select the variable with the most negative reduced cost
- This determines the direction to move

**Step 4: Choose Leaving Variable**  
- Use the minimum ratio test to avoid infeasibility
- This determines how far to move

**Step 5: Pivot Operation**
- Update the tableau using Gaussian elimination
- Move to the new vertex

**Step 6: Repeat**
- Go back to Step 2 until optimal

### Interactive Simplex Example

Let's solve a simple 2D problem step by step to see how Simplex works in practice:

<div class="content-box exercise-box">
<strong>Interactive Simplex Solver:</strong> Watch the algorithm move from vertex to vertex!

**Problem:**
$$\begin{align}
\text{maximize } & 3x_1 + 2x_2 \\
\text{subject to } & x_1 + x_2 \leq 4 \\
& 2x_1 + x_2 \leq 6 \\
& x_1, x_2 \geq 0
\end{align}$$

<div id="simplex-interactive" style="margin: 20px 0;"></div>

<div style="margin: 15px 0;">
  <button id="simplex-step" style="background-color: #2196F3; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; margin-right: 10px;">Next Step</button>
  <button id="simplex-reset" style="background-color: #f44336; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer;">Reset</button>
</div>

<div id="simplex-status" style="margin-top: 15px; font-family: monospace; background-color: #f9f9f9; padding: 15px; border-radius: 4px;">
  <div><strong>Step 0:</strong> Starting at origin (0, 0)</div>
  <div>Current objective value: 0</div>
  <div>Click "Next Step" to begin the Simplex algorithm!</div>
</div>

<div id="simplex-tableau" style="margin-top: 15px; font-family: monospace; background-color: #f0f8ff; padding: 15px; border-radius: 4px;">
  <strong>Current Simplex Tableau:</strong>
  <div id="tableau-content" style="margin-top: 10px;">
    Click "Next Step" to see the tableau!
  </div>
</div>
</div>

### Why Simplex is Efficient

Despite having potentially exponential worst-case complexity, Simplex is remarkably efficient in practice:

<div class="content-box insight-box">
<strong>Simplex Efficiency:</strong>
<ul>
<li><strong>Average case:</strong> Typically visits only 2-3 times the number of constraints</li>
<li><strong>Practical problems:</strong> Often solves in polynomial time</li>
<li><strong>Warm starts:</strong> Can reuse previous solutions when problem changes slightly</li>
<li><strong>Degeneracy handling:</strong> Modern implementations handle degenerate cases well</li>
</ul>
</div>

### Simplex Variants and Modern Developments

**Revised Simplex Method:**
- More numerically stable
- Better for sparse matrices  
- Used in most commercial solvers

**Dual Simplex Method:**
- Starts with dual feasible solution
- Useful for sensitivity analysis
- Better for certain problem types

**Interior Point Methods:**
- Polynomial-time complexity guarantee
- Better for very large problems
- Complement rather than replace Simplex

### Impact and Applications

The Simplex algorithm has transformed numerous industries:

<div class="content-box insight-box">
<strong>Simplex Success Stories:</strong>
<ul>
<li><strong>Airlines:</strong> Crew scheduling, route optimization, fleet assignment</li>
<li><strong>Manufacturing:</strong> Production planning, supply chain optimization</li>
<li><strong>Finance:</strong> Portfolio optimization, risk management</li>
<li><strong>Telecommunications:</strong> Network flow optimization, bandwidth allocation</li>
<li><strong>Energy:</strong> Power grid optimization, resource allocation</li>
</ul>
</div>

<script>
/**
 * Interactive Linear Programming Visualizations
 * Implements farmer problem, geometric interpretation, diet optimizer, and norm comparisons
 */

// Wait for DOM to be fully loaded
document.addEventListener('DOMContentLoaded', function() {
    
    // ==================== FARMER PROBLEM INTERACTIVE ====================
    
    function initializeFarmerProblem() {
        const cornSlider = document.getElementById('corn-acres');
        const wheatSlider = document.getElementById('wheat-acres');
        
        if (!cornSlider || !wheatSlider) return;
        
        function updateFarmerResults() {
            const corn = parseFloat(cornSlider.value);
            const wheat = parseFloat(wheatSlider.value);
            
            // Update display values
            document.getElementById('corn-value').textContent = corn;
            document.getElementById('wheat-value').textContent = wheat;
            
            // Calculate metrics
            const landUsed = corn + wheat;
            const laborUsed = corn * 2 + wheat * 1; // 2 hours per corn acre, 1 hour per wheat acre
            const profit = corn * 300 + wheat * 200; // $300 per corn acre, $200 per wheat acre
            
            // Update results
            document.getElementById('land-used').textContent = landUsed;
            document.getElementById('labor-used').textContent = laborUsed;
            document.getElementById('total-profit').textContent = profit;
            
            // Check feasibility
            const feasibilityStatus = document.getElementById('feasibility-status');
            if (landUsed <= 100 && laborUsed <= 150) {
                feasibilityStatus.textContent = '✓ Feasible solution';
                feasibilityStatus.style.color = 'green';
            } else {
                feasibilityStatus.textContent = '✗ Infeasible solution';
                feasibilityStatus.style.color = 'red';
            }
        }
        
        cornSlider.addEventListener('input', updateFarmerResults);
        wheatSlider.addEventListener('input', updateFarmerResults);
        
        // Initialize
        updateFarmerResults();
    }
    
    // ==================== DIET PROBLEM SOLVER ====================
    
    function initializeDietSolver() {
        const solveButton = document.getElementById('solve-diet');
        if (!solveButton) return;
        
        solveButton.addEventListener('click', function() {
            const minProtein = parseFloat(document.getElementById('min-protein').value);
            const minCalories = parseFloat(document.getElementById('min-calories').value);
            
            // Simple heuristic solver (in practice, would use simplex method)
            // Food data: [cost, protein, calories]
            const bread = [2, 4, 200];
            const milk = [3, 8, 150];
            const meat = [8, 20, 300];
            
            // Try different combinations and find minimum cost feasible solution
            let bestCost = Infinity;
            let bestSolution = null;
            
            for (let b = 0; b <= 20; b += 0.5) {
                for (let m = 0; m <= 10; m += 0.5) {
                    for (let mt = 0; mt <= 5; mt += 0.5) {
                        const protein = b * bread[1] + m * milk[1] + mt * meat[1];
                        const calories = b * bread[2] + m * milk[2] + mt * meat[2];
                        const cost = b * bread[0] + m * milk[0] + mt * meat[0];
                        
                        if (protein >= minProtein && calories >= minCalories && cost < bestCost) {
                            bestCost = cost;
                            bestSolution = [b, m, mt];
                        }
                    }
                }
            }
            
            const resultsDiv = document.getElementById('diet-results');
            if (bestSolution) {
                const [bread_amt, milk_amt, meat_amt] = bestSolution;
                const totalProtein = bread_amt * bread[1] + milk_amt * milk[1] + meat_amt * meat[1];
                const totalCalories = bread_amt * bread[2] + milk_amt * milk[2] + meat_amt * meat[2];
                
                resultsDiv.innerHTML = `
                    <div><strong>Optimal Diet Solution:</strong></div>
                    <div>Bread: ${bread_amt.toFixed(1)} loaves</div>
                    <div>Milk: ${milk_amt.toFixed(1)} liters</div>
                    <div>Meat: ${meat_amt.toFixed(1)} kg</div>
                    <div>---</div>
                    <div>Total cost: $${bestCost.toFixed(2)}</div>
                    <div>Total protein: ${totalProtein.toFixed(1)}g (required: ${minProtein}g)</div>
                    <div>Total calories: ${totalCalories.toFixed(0)} (required: ${minCalories})</div>
                `;
            } else {
                resultsDiv.innerHTML = '<div style="color: red;">No feasible solution found!</div>';
            }
        });
    }
    
    // ==================== SIMPLEX ALGORITHM VISUALIZATION ====================
    
    function initializeSimplexVisualization() {
        const stepButton = document.getElementById('simplex-step');
        const resetButton = document.getElementById('simplex-reset');
        const statusDiv = document.getElementById('simplex-status');
        const tableauDiv = document.getElementById('tableau-content');
        const interactiveDiv = document.getElementById('simplex-interactive');
        
        if (!stepButton || !resetButton || !statusDiv || !tableauDiv || !interactiveDiv) return;
        
        // Simplex algorithm state
        let currentStep = 0;
        let currentVertex = [0, 0]; // Starting at origin
        let isOptimal = false;
        
        // Problem: maximize 3x1 + 2x2 subject to x1 + x2 <= 4, 2x1 + x2 <= 6, x1,x2 >= 0
        // In standard form: minimize -3x1 - 2x2 subject to x1 + x2 + s1 = 4, 2x1 + x2 + s2 = 6
        
        const vertices = [
            [0, 0, 4, 6], // (x1, x2, s1, s2) - origin
            [0, 4, 0, 2], // (0, 4, 0, 2) - intersection with x1 + x2 = 4
            [2, 2, 0, 0], // (2, 2, 0, 0) - intersection of both constraints
            [3, 0, 1, 0]  // (3, 0, 1, 0) - intersection with 2x1 + x2 = 6
        ];
        
        const objectiveValues = [0, 8, 10, 9]; // 3x1 + 2x2 at each vertex
        const simplexPath = [0, 3, 2]; // Path: origin -> (3,0) -> (2,2) optimal
        
        function createVisualization() {
            const width = 400;
            const height = 300;
            const margin = {top: 20, right: 20, bottom: 40, left: 40};
            
            // Clear previous content
            interactiveDiv.innerHTML = '';
            
            const svg = d3.select('#simplex-interactive')
                .append('svg')
                .attr('width', width)
                .attr('height', height);
            
            // Scales
            const xScale = d3.scaleLinear()
                .domain([0, 4])
                .range([margin.left, width - margin.right]);
            
            const yScale = d3.scaleLinear()
                .domain([0, 6])
                .range([height - margin.bottom, margin.top]);
            
            // Draw feasible region
            const feasibleRegion = [
                [0, 0], [0, 4], [2, 2], [3, 0], [0, 0]
            ];
            
            svg.append('path')
                .datum(feasibleRegion)
                .attr('fill', 'lightblue')
                .attr('fill-opacity', 0.3)
                .attr('stroke', 'blue')
                .attr('stroke-width', 2)
                .attr('d', d3.line()
                    .x(d => xScale(d[0]))
                    .y(d => yScale(d[1]))
                );
            
            // Draw constraint lines
            // x1 + x2 = 4
            svg.append('line')
                .attr('x1', xScale(0))
                .attr('y1', yScale(4))
                .attr('x2', xScale(4))
                .attr('y2', yScale(0))
                .attr('stroke', 'red')
                .attr('stroke-width', 2)
                .attr('stroke-dasharray', '5,5');
            
            // 2x1 + x2 = 6
            svg.append('line')
                .attr('x1', xScale(0))
                .attr('y1', yScale(6))
                .attr('x2', xScale(3))
                .attr('y2', yScale(0))
                .attr('stroke', 'green')
                .attr('stroke-width', 2)
                .attr('stroke-dasharray', '5,5');
            
            // Draw vertices
            const vertexPoints = [[0,0], [0,4], [2,2], [3,0]];
            svg.selectAll('.vertex')
                .data(vertexPoints)
                .enter()
                .append('circle')
                .attr('class', 'vertex')
                .attr('cx', d => xScale(d[0]))
                .attr('cy', d => yScale(d[1]))
                .attr('r', 6)
                .attr('fill', 'orange')
                .attr('stroke', 'black')
                .attr('stroke-width', 2);
            
            // Current position indicator
            svg.append('circle')
                .attr('id', 'current-position')
                .attr('cx', xScale(currentVertex[0]))
                .attr('cy', yScale(currentVertex[1]))
                .attr('r', 8)
                .attr('fill', 'red')
                .attr('stroke', 'darkred')
                .attr('stroke-width', 3);
            
            // Axes
            svg.append('g')
                .attr('transform', `translate(0,${height - margin.bottom})`)
                .call(d3.axisBottom(xScale));
            
            svg.append('g')
                .attr('transform', `translate(${margin.left},0)`)
                .call(d3.axisLeft(yScale));
            
            // Axis labels
            svg.append('text')
                .attr('x', width / 2)
                .attr('y', height - 5)
                .attr('text-anchor', 'middle')
                .text('x₁');
            
            svg.append('text')
                .attr('transform', 'rotate(-90)')
                .attr('x', -height / 2)
                .attr('y', 15)
                .attr('text-anchor', 'middle')
                .text('x₂');
            
            // Legend
            const legend = svg.append('g')
                .attr('transform', `translate(${width - 150}, 30)`);
            
            legend.append('text')
                .attr('x', 0)
                .attr('y', 0)
                .text('Constraints:')
                .attr('font-weight', 'bold');
            
            legend.append('line')
                .attr('x1', 0)
                .attr('y1', 15)
                .attr('x2', 20)
                .attr('y2', 15)
                .attr('stroke', 'red')
                .attr('stroke-width', 2)
                .attr('stroke-dasharray', '5,5');
            
            legend.append('text')
                .attr('x', 25)
                .attr('y', 19)
                .text('x₁ + x₂ ≤ 4')
                .attr('font-size', '12px');
            
            legend.append('line')
                .attr('x1', 0)
                .attr('y1', 30)
                .attr('x2', 20)
                .attr('y2', 30)
                .attr('stroke', 'green')
                .attr('stroke-width', 2)
                .attr('stroke-dasharray', '5,5');
            
            legend.append('text')
                .attr('x', 25)
                .attr('y', 34)
                .text('2x₁ + x₂ ≤ 6')
                .attr('font-size', '12px');
        }
        
        function updateTableau(step) {
            let tableauHTML = '';
            
            switch(step) {
                case 0:
                    tableauHTML = `
                        <table style="border-collapse: collapse; margin: 10px 0;">
                            <tr style="background-color: #e0e0e0;">
                                <th style="border: 1px solid #ccc; padding: 8px;">Basic</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">x₁</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">x₂</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">s₁</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">s₂</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">RHS</th>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ccc; padding: 8px;">s₁</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">4</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ccc; padding: 8px;">s₂</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">2</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">6</td>
                            </tr>
                            <tr style="background-color: #fff2cc;">
                                <td style="border: 1px solid #ccc; padding: 8px;">z</td>
                                <td style="border: 1px solid #ccc; padding: 8px; color: red;"><strong>-3</strong></td>
                                <td style="border: 1px solid #ccc; padding: 8px; color: red;">-2</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                            </tr>
                        </table>
                        <div style="margin-top: 10px;">
                            <strong>Analysis:</strong> Most negative coefficient is -3 (x₁ column). x₁ enters the basis.
                        </div>
                    `;
                    break;
                case 1:
                    tableauHTML = `
                        <table style="border-collapse: collapse; margin: 10px 0;">
                            <tr style="background-color: #e0e0e0;">
                                <th style="border: 1px solid #ccc; padding: 8px;">Basic</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">x₁</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">x₂</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">s₁</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">s₂</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">RHS</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">Ratio</th>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ccc; padding: 8px;">s₁</td>
                                <td style="border: 1px solid #ccc; padding: 8px; background-color: #ffcccc;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">4</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">4/1 = 4</td>
                            </tr>
                            <tr style="background-color: #ccffcc;">
                                <td style="border: 1px solid #ccc; padding: 8px;">s₂</td>
                                <td style="border: 1px solid #ccc; padding: 8px; background-color: #ffcccc;"><strong>2</strong></td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">6</td>
                                <td style="border: 1px solid #ccc; padding: 8px;"><strong>6/2 = 3</strong></td>
                            </tr>
                            <tr style="background-color: #fff2cc;">
                                <td style="border: 1px solid #ccc; padding: 8px;">z</td>
                                <td style="border: 1px solid #ccc; padding: 8px; background-color: #ffcccc;">-3</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">-2</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">-</td>
                            </tr>
                        </table>
                        <div style="margin-top: 10px;">
                            <strong>Minimum ratio test:</strong> min{4/1, 6/2} = min{4, 3} = 3. s₂ leaves the basis.
                        </div>
                    `;
                    break;
                case 2:
                    tableauHTML = `
                        <table style="border-collapse: collapse; margin: 10px 0;">
                            <tr style="background-color: #e0e0e0;">
                                <th style="border: 1px solid #ccc; padding: 8px;">Basic</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">x₁</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">x₂</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">s₁</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">s₂</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">RHS</th>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ccc; padding: 8px;">s₁</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px; color: red;"><strong>0.5</strong></td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">-0.5</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ccc; padding: 8px;">x₁</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0.5</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0.5</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">3</td>
                            </tr>
                            <tr style="background-color: #fff2cc;">
                                <td style="border: 1px solid #ccc; padding: 8px;">z</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px; color: red;"><strong>-0.5</strong></td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1.5</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">9</td>
                            </tr>
                        </table>
                        <div style="margin-top: 10px;">
                            <strong>Current solution:</strong> x₁ = 3, x₂ = 0, objective = 9<br>
                            <strong>Analysis:</strong> x₂ has negative coefficient (-0.5), so x₂ enters the basis.
                        </div>
                    `;
                    break;
                case 3:
                    tableauHTML = `
                        <table style="border-collapse: collapse; margin: 10px 0;">
                            <tr style="background-color: #e0e0e0;">
                                <th style="border: 1px solid #ccc; padding: 8px;">Basic</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">x₁</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">x₂</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">s₁</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">s₂</th>
                                <th style="border: 1px solid #ccc; padding: 8px;">RHS</th>
                            </tr>
                            <tr style="background-color: #ccffcc;">
                                <td style="border: 1px solid #ccc; padding: 8px;">x₂</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">2</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">-1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">2</td>
                            </tr>
                            <tr>
                                <td style="border: 1px solid #ccc; padding: 8px;">x₁</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">-1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">2</td>
                            </tr>
                            <tr style="background-color: #ccffcc;">
                                <td style="border: 1px solid #ccc; padding: 8px;">z</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">0</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">1</td>
                                <td style="border: 1px solid #ccc; padding: 8px;">10</td>
                            </tr>
                        </table>
                        <div style="margin-top: 10px;">
                            <strong>OPTIMAL SOLUTION FOUND!</strong><br>
                            x₁ = 2, x₂ = 2, Maximum objective value = 10<br>
                            All coefficients in the objective row are non-negative.
                        </div>
                    `;
                    break;
            }
            
            tableauDiv.innerHTML = tableauHTML;
        }
        
        function updateStatus(step) {
            let statusHTML = '';
            
            switch(step) {
                case 0:
                    statusHTML = `
                        <div><strong>Step 0:</strong> Initial basic feasible solution</div>
                        <div>Current vertex: (0, 0)</div>
                        <div>Current objective value: 0</div>
                        <div>Basic variables: s₁ = 4, s₂ = 6</div>
                    `;
                    currentVertex = [0, 0];
                    break;
                case 1:
                    statusHTML = `
                        <div><strong>Step 1:</strong> Choose entering variable</div>
                        <div>Most negative coefficient: -3 (x₁ column)</div>
                        <div>x₁ enters the basis</div>
                        <div>Performing minimum ratio test...</div>
                    `;
                    break;
                case 2:
                    statusHTML = `
                        <div><strong>Step 2:</strong> First iteration complete</div>
                        <div>Current vertex: (3, 0)</div>
                        <div>Current objective value: 9</div>
                        <div>Basic variables: x₁ = 3, s₁ = 1</div>
                    `;
                    currentVertex = [3, 0];
                    break;
                case 3:
                    statusHTML = `
                        <div><strong>Step 3:</strong> OPTIMAL SOLUTION FOUND!</div>
                        <div>Current vertex: (2, 2)</div>
                        <div>Maximum objective value: 10</div>
                        <div>Basic variables: x₁ = 2, x₂ = 2</div>
                    `;
                    currentVertex = [2, 2];
                    isOptimal = true;
                    break;
            }
            
            statusDiv.innerHTML = statusHTML;
            
            // Update visualization
            const currentPos = d3.select('#current-position');
            if (currentPos.node()) {
                const xScale = d3.scaleLinear().domain([0, 4]).range([40, 360]);
                const yScale = d3.scaleLinear().domain([0, 6]).range([260, 40]);
                
                currentPos
                    .transition()
                    .duration(500)
                    .attr('cx', xScale(currentVertex[0]))
                    .attr('cy', yScale(currentVertex[1]));
            }
        }
        
        function nextStep() {
            if (currentStep < 3) {
                currentStep++;
                updateStatus(currentStep);
                updateTableau(currentStep);
                
                if (currentStep === 3) {
                    stepButton.textContent = 'Algorithm Complete!';
                    stepButton.disabled = true;
                    stepButton.style.backgroundColor = '#4CAF50';
                }
            }
        }
        
        function reset() {
            currentStep = 0;
            currentVertex = [0, 0];
            isOptimal = false;
            
            stepButton.textContent = 'Next Step';
            stepButton.disabled = false;
            stepButton.style.backgroundColor = '#2196F3';
            
            updateStatus(0);
            updateTableau(0);
            createVisualization();
        }
        
        // Event listeners
        stepButton.addEventListener('click', nextStep);
        resetButton.addEventListener('click', reset);
        
        // Initialize
        createVisualization();
        updateStatus(0);
        updateTableau(0);
    }
    
    // Initialize all interactive elements
    initializeFarmerProblem();
    initializeDietSolver();
    initializeSimplexVisualization();
    
    // Trigger MathJax re-rendering if needed
    if (window.MathJax) {
        MathJax.typesetPromise();
    }
});
</script>
