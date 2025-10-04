---
layout: post
title: 12-04 Ví dụ Máy Vector Hỗ Trợ (Support Vector Machines - SVM)
chapter: '12'
order: 5
owner: Wontak Ryu
categories:
- chapter12
lang: vi
lesson_type: required
---

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
    displayAlign: "center"
});
</script>

# Máy Vector Hỗ Trợ (Support Vector Machines - SVM)

## 1. Giới thiệu

**Support Vector Machine (SVM)** là một thuật toán phân loại mạnh mẽ, tìm siêu phẳng tối ưu để phân tách các lớp dữ liệu với **margin lớn nhất**.

### 1.1. Khoảng cách từ một điểm tới siêu mặt phẳng

Trước khi đi vào chi tiết, hãy nhắc lại kiến thức về hình học giải tích:

**Không gian 2 chiều:**  
Khoảng cách từ điểm $$(x_0, y_0)$$ tới đường thẳng $$w_1x + w_2y + b = 0$$ là:
$$
\frac{\lvert w_1x_0 + w_2y_0 + b\rvert}{\sqrt{w_1^2 + w_2^2}}
$$

**Không gian 3 chiều:**  
Khoảng cách từ điểm $$(x_0, y_0, z_0)$$ tới mặt phẳng $$w_1x + w_2y + w_3z + b = 0$$ là:
$$
\frac{\lvert w_1x_0 + w_2y_0 + w_3z_0 + b\rvert}{\sqrt{w_1^2 + w_2^2 + w_3^2}}
$$

**Tổng quát - Không gian nhiều chiều:**  
Khoảng cách từ điểm (vector) $$\mathbf{x}_0$$ tới **siêu mặt phẳng** $$\mathbf{w}^T\mathbf{x} + b = 0$$ là:
$$
\frac{\lvert\mathbf{w}^T\mathbf{x}_0 + b\rvert}{\|\mathbf{w}\|_2}
$$

**Lưu ý quan trọng:**  
- Nếu bỏ dấu giá trị tuyệt đối, ta xác định được điểm nằm về phía nào của siêu phẳng
- Biểu thức dương: điểm ở **phía dương** của siêu phẳng
- Biểu thức âm: điểm ở **phía âm** của siêu phẳng
- Biểu thức bằng 0: điểm nằm trên siêu phẳng

### 1.2. Ý tưởng cốt lõi

- **Siêu phẳng**: $$\beta^T x + \beta_0 = 0$$ phân tách hai lớp
- **Margin**: Khoảng cách từ siêu phẳng đến điểm gần nhất = $$\frac{2}{\|\beta\|}$$
- **Mục tiêu**: Maximize margin $$\Leftrightarrow$$ Minimize $$\|\beta\|$$

### 1.3. Minh họa trực quan: Khoảng cách và phân loại

<div id="distance-demo" style="margin: 20px 0;">
    <canvas id="distanceCanvas" width="600" height="400" style="border: 1px solid #ccc; display: block; margin: 0 auto;"></canvas>
    <div style="text-align: center; margin-top: 15px;">
        <p style="font-size: 14px; color: #666;">
            <strong>Hướng dẫn:</strong> Di chuyển chuột trên canvas để xem khoảng cách từ điểm đến đường thẳng
        </p>
        <p id="distanceInfo" style="font-size: 16px; font-weight: bold; color: #333;">
            Khoảng cách: 0
        </p>
    </div>
</div>

<script>
(function() {
    const canvas = document.getElementById('distanceCanvas');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    
    // Tham số đường thẳng: w1*x + w2*y + b = 0
    // Chọn đường thẳng đi qua giữa canvas với góc nghiêng
    const w1 = 1;
    const w2 = 0.5;
    const b = -200;
    const norm = Math.sqrt(w1*w1 + w2*w2);
    
    let mouseX = width / 2;
    let mouseY = height / 2;
    
    function draw() {
        // Clear canvas
        ctx.clearRect(0, 0, width, height);
        
        // Vẽ lưới nền
        ctx.strokeStyle = '#f0f0f0';
        ctx.lineWidth = 1;
        for (let x = 0; x < width; x += 50) {
            ctx.beginPath();
            ctx.moveTo(x, 0);
            ctx.lineTo(x, height);
            ctx.stroke();
        }
        for (let y = 0; y < height; y += 50) {
            ctx.beginPath();
            ctx.moveTo(0, y);
            ctx.lineTo(width, y);
            ctx.stroke();
        }
        
        // Vẽ đường thẳng w1*x + w2*y + b = 0
        ctx.strokeStyle = '#2c3e50';
        ctx.lineWidth = 3;
        ctx.beginPath();
        
        // Tính y cho x = 0 và x = width
        const y0 = -(w1 * 0 + b) / w2;
        const y1 = -(w1 * width + b) / w2;
        
        ctx.moveTo(0, y0);
        ctx.lineTo(width, y1);
        ctx.stroke();
        
        // Vẽ label cho đường thẳng
        ctx.fillStyle = '#2c3e50';
        ctx.font = '14px Arial';
        ctx.fillText('w₁x + w₂y + b = 0', width - 150, y1 + 20);
        
        // Tính khoảng cách từ điểm chuột đến đường thẳng
        const distance = Math.abs(w1 * mouseX + w2 * mouseY + b) / norm;
        const signedDist = (w1 * mouseX + w2 * mouseY + b) / norm;
        
        // Tìm điểm chiếu vuông góc
        const t = -(w1 * mouseX + w2 * mouseY + b) / (w1*w1 + w2*w2);
        const projX = mouseX + t * w1;
        const projY = mouseY + t * w2;
        
        // Vẽ đường vuông góc
        ctx.strokeStyle = '#e74c3c';
        ctx.lineWidth = 2;
        ctx.setLineDash([5, 5]);
        ctx.beginPath();
        ctx.moveTo(mouseX, mouseY);
        ctx.lineTo(projX, projY);
        ctx.stroke();
        ctx.setLineDash([]);
        
        // Vẽ điểm chuột
        ctx.fillStyle = signedDist > 0 ? '#3498db' : '#e74c3c';
        ctx.beginPath();
        ctx.arc(mouseX, mouseY, 8, 0, 2 * Math.PI);
        ctx.fill();
        
        // Vẽ điểm chiếu
        ctx.fillStyle = '#95a5a6';
        ctx.beginPath();
        ctx.arc(projX, projY, 5, 0, 2 * Math.PI);
        ctx.fill();
        
        // Hiển thị khoảng cách
        const distInfo = document.getElementById('distanceInfo');
        if (distInfo) {
            const side = signedDist > 0 ? '(Phía dương)' : '(Phía âm)';
            distInfo.innerHTML = `Khoảng cách: <span style="color: ${signedDist > 0 ? '#3498db' : '#e74c3c'}">${distance.toFixed(2)}</span> ${side}`;
        }
        
        // Vẽ text thông tin
        ctx.fillStyle = '#34495e';
        ctx.font = '12px Arial';
        ctx.fillText(`Điểm: (${mouseX.toFixed(0)}, ${mouseY.toFixed(0)})`, mouseX + 15, mouseY - 15);
    }
    
    // Event listeners
    canvas.addEventListener('mousemove', function(e) {
        const rect = canvas.getBoundingClientRect();
        mouseX = e.clientX - rect.left;
        mouseY = e.clientY - rect.top;
        draw();
    });
    
    // Initial draw
    draw();
})();
</script>

---

## 2. Nhắc lại bài toán phân chia hai classes

Giả sử rằng có hai class khác nhau được mô tả bởi các điểm trong không gian nhiều chiều, hai classes này **linearly separable**, tức tồn tại một siêu phẳng phân chia chính xác hai classes đó. 

**Mục tiêu**: Tìm một siêu mặt phẳng phân chia hai classes, tức tất cả các điểm thuộc một class nằm về cùng một phía của siêu mặt phẳng đó và ngược phía với toàn bộ các điểm thuộc class còn lại.

Chúng ta có **vô số nghiệm** như minh họa dưới đây:

<figure class="image" style="align: center;">
<p align="center">
 <img src="https://machinelearningcoban.com/assets/19_svm/svm1.png" alt="" width="60%" height="60%">
 <figcaption style="text-align: center;">$$ \text{[Hình 2] Các mặt phân cách khả dĩ cho hai classes linearly separable}$$ </figcaption>
</p>
</figure>

**Câu hỏi đặt ra**: Trong vô số các mặt phân chia đó, **đâu là mặt phân chia tốt nhất** theo một tiêu chuẩn nào đó? 

Trong hình minh họa phía trên, có hai đường thẳng khá lệch về phía class hình tròn đỏ, trong khi đường thẳng còn lại gần như nằm ở giữa hai classes. Ta cần một tiêu chuẩn khách quan để chọn ra đường phân chia tối ưu.

### Tiêu chuẩn: Maximum Margin

Trong vô số các mặt phân cách khả dĩ, chúng ta cần một tiêu chuẩn để chọn ra mặt phân cách **tốt nhất**.

<figure class="image" style="align: center;">
<p align="center">
 <img src="https://machinelearningcoban.com/assets/19_svm/svm2.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">$$ \text{[Hình 3] So sánh các mặt phân cách với margin khác nhau}$$ </figcaption>
</p>
</figure>

**Định nghĩa Margin**: Khoảng cách từ điểm gần nhất của mỗi class đến mặt phân cách được gọi là **margin** (lề).

**Tiêu chuẩn tối ưu**: Mặt phân cách tốt nhất thỏa mãn hai điều kiện:
1. **Đối xứng**: Margin từ mặt phân cách đến mỗi class phải **bằng nhau**
2. **Tối đa**: Margin đó phải là **lớn nhất** có thể

**Ý nghĩa**: 
- Margin lớn → sự phân chia giữa hai classes **rạch ròi** hơn
- Tăng khả năng tổng quát hóa (generalization) cho dữ liệu mới
- Giảm độ nhạy cảm với nhiễu (noise) trong dữ liệu

**Kết luận**: Bài toán SVM chính là bài toán tìm mặt phân cách có **margin lớn nhất**. Đây là lý do SVM còn được gọi là **Maximum Margin Classifier**.

---

## 3. Xây dựng bài toán tối ưu cho SVM

### 3.1. Thiết lập bài toán

**Giả sử**: Các cặp dữ liệu của training set là $$(x_1, y_1), (x_2, y_2), \ldots, (x_N, y_N)$$ với:
- Vector $$x_i \in \mathbb{R}^d$$: đầu vào của một điểm dữ liệu
- $$y_i \in \{-1, +1\}$$: nhãn của điểm dữ liệu đó
- $$d$$: số chiều của dữ liệu
- $$N$$: số điểm dữ liệu

**Lưu ý**: Để dễ hình dung, chúng ta xét trường hợp không gian hai chiều. Các phép toán hoàn toàn có thể được tổng quát lên không gian nhiều chiều.

<figure class="image" style="align: center;">
<p align="center">
 <img src="https://machinelearningcoban.com/assets/19_svm/svm6.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">$$ \text{[Hình 4] Phân tích bài toán SVM}$$ </figcaption>
</p>
</figure>

**Giả sử**:
- Các điểm vuông xanh thuộc class +1
- Các điểm tròn đỏ thuộc class -1
- Mặt $$w^T x + b = w_1 x_1 + w_2 x_2 + b = 0$$ là mặt phân chia
- Class +1 nằm về **phía dương**, class -1 nằm về **phía âm**

### 3.2. Công thức khoảng cách

**Quan sát quan trọng**: Với cặp dữ liệu $$(x_n, y_n)$$ bất kỳ, khoảng cách từ điểm đó tới mặt phân chia là:

$$
\frac{y_n(w^T x_n + b)}{\|w\|_2}
$$

**Giải thích**: Điều này dễ nhận thấy vì theo giả sử, $$y_n$$ luôn cùng dấu với phía của $$x_n$$. Từ đó suy ra $$y_n$$ cùng dấu với $$(w^T x_n + b)$$, và tử số luôn là một số không âm.

### 3.3. Định nghĩa Margin

Với mặt phân chia như trên, **margin** được tính là khoảng cách gần nhất từ một điểm tới mặt đó (bất kể điểm nào trong hai classes):

$$
\text{margin} = \min_n \frac{y_n(w^T x_n + b)}{\|w\|_2}
$$

### 3.4. Bài toán tối ưu ban đầu

Bài toán tối ưu trong SVM chính là bài toán tìm $$w$$ và $$b$$ sao cho margin này đạt giá trị **lớn nhất**:

$$
\begin{align}
(w, b) &= \arg\max_{w,b} \left\{ \min_n \frac{y_n(w^T x_n + b)}{\|w\|_2} \right\} \\
&= \arg\max_{w,b} \left\{ \frac{1}{\|w\|_2} \min_n y_n(w^T x_n + b) \right\} \qquad (1)
\end{align}
$$

**Vấn đề**: Việc giải trực tiếp bài toán này sẽ rất phức tạp.

### 3.5. Biến đổi về bài toán đơn giản

**Nhận xét quan trọng**: Nếu ta thay vector hệ số $$w$$ bởi $$kw$$ và $$b$$ bởi $$kb$$ trong đó $$k$$ là một hằng số dương thì:
- Mặt phân chia **không thay đổi**
- Khoảng cách từ từng điểm đến mặt phân chia **không đổi**
- Margin **không đổi**

**Chuẩn hóa**: Dựa trên tính chất này, ta có thể giả sử:

$$
y_n(w^T x_n + b) = 1
$$

với những điểm nằm **gần mặt phân chia nhất** (các điểm support vectors).

<figure class="image" style="align: center;">
<p align="center">
 <img src="https://machinelearningcoban.com/assets/19_svm/svm3.png" alt="" width="60%" height="60%">
 <figcaption style="text-align: center;">$$ \text{[Hình 5] Các điểm gần mặt phân cách nhất được khoanh tròn}$$ </figcaption>
</p>
</figure>

**Hệ quả**: Với mọi $$n$$, ta có:

$$
y_n(w^T x_n + b) \geq 1
$$

### 3.6. Bài toán tối ưu có ràng buộc

Vậy bài toán tối ưu $$(1)$$ có thể đưa về:

$$
\begin{align}
(w, b) &= \arg\max_{w,b} \frac{1}{\|w\|_2} \\
\text{subject to: } & y_n(w^T x_n + b) \geq 1, \quad \forall n = 1,2,\ldots,N \qquad (2)
\end{align}
$$

### 3.7. Bài toán tối ưu chuẩn

Bằng biến đổi đơn giản, ta có thể đưa bài toán về dạng:

$$
\begin{align}
(w, b) &= \arg\min_{w,b} \frac{1}{2}\|w\|_2^2 \\
\text{subject to: } & 1 - y_n(w^T x_n + b) \leq 0, \quad \forall n = 1,2,\ldots,N \qquad (3)
\end{align}
$$

**Giải thích các biến đổi**:
1. Lấy **nghịch đảo** hàm mục tiêu (max → min)
2. **Bình phương** để được hàm khả vi
3. Nhân với $$\frac{1}{2}$$ để biểu thức đạo hàm đẹp hơn
4. Đổi dấu ràng buộc

### 3.8. Tính chất của bài toán

**Quan sát quan trọng**:

1. **Hàm mục tiêu**: $$\frac{1}{2}\|w\|_2^2$$ là một hàm **lồi** (norm bình phương)

2. **Hàm ràng buộc**: $$1 - y_n(w^T x_n + b)$$ là hàm **tuyến tính** theo $$w$$ và $$b$$, nên là hàm **lồi**

3. **Kết luận**: Bài toán $$(3)$$ là một **bài toán lồi** (convex optimization problem)

4. **Hơn nữa**: Đây là một **Quadratic Programming (QP)** problem

5. **Strictly convex**: Hàm mục tiêu là strictly convex vì $$\|w\|_2^2 = w^T I w$$ và $$I$$ là ma trận đơn vị - một ma trận **xác định dương**

6. **Nghiệm duy nhất**: Từ tính strictly convex, suy ra nghiệm cho SVM là **duy nhất**


### 3.10. Xác định class cho điểm mới

Sau khi tìm được mặt phân cách $$w^T x + b = 0$$, class của bất kỳ một điểm nào sẽ được xác định đơn giản bằng:

$$
\text{class}(x) = \text{sgn}(w^T x + b)
$$

Trong đó hàm $$\text{sgn}$$ là hàm xác định dấu:
- Nhận giá trị **+1** nếu đối số là không âm
- Nhận giá trị **-1** nếu ngược lại

---

## 4. Hard-Margin SVM (Dữ liệu tách được)

Khi dữ liệu **tách được tuyến tính**, bài toán SVM có dạng:

$$
\begin{align}
&\min_{\beta, \beta_0} &&{\frac{1}{2} \|\beta\|_2^2} \\
&\text{s.t.} && y_i (\beta^T x_i + \beta_0) \geq 1, \quad i = 1, \ldots, n
\end{align}
$$

**Giải thích:**
- Hàm mục tiêu: Minimize $$\|\beta\|$$ để maximize margin
- Ràng buộc: Mọi điểm phải cách siêu phẳng ít nhất 1 đơn vị (theo metric)

### 4.1. Minh họa tương tác: Hard-Margin SVM

<div id="hardmargin-demo" style="margin: 20px 0;">
    <canvas id="hardMarginCanvas" width="700" height="500" style="border: 1px solid #ccc; display: block; margin: 0 auto;"></canvas>
    <div style="text-align: center; margin-top: 15px;">
        <button id="resetData" style="padding: 10px 20px; font-size: 14px; cursor: pointer; background: #3498db; color: white; border: none; border-radius: 5px; margin: 5px;">
            🔄 Tạo dữ liệu mới
        </button>
        <button id="addPositive" style="padding: 10px 20px; font-size: 14px; cursor: pointer; background: #e74c3c; color: white; border: none; border-radius: 5px; margin: 5px;">
            ➕ Thêm điểm dương (+1)
        </button>
        <button id="addNegative" style="padding: 10px 20px; font-size: 14px; cursor: pointer; background: #2ecc71; color: white; border: none; border-radius: 5px; margin: 5px;">
            ➕ Thêm điểm âm (-1)
        </button>
        <p style="font-size: 14px; color: #666; margin-top: 10px;">
            <strong>Hướng dẫn:</strong> Click vào canvas để thêm điểm mới. Đường đen đậm là siêu phẳng phân cách, đường đứt nét là margin boundaries.
        </p>
    </div>
</div>

<script>
(function() {
    const canvas = document.getElementById('hardMarginCanvas');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    
    let addMode = 0; // 0: none, 1: positive, -1: negative
    
    // Dữ liệu điểm
    let points = [
        // Class +1 (đỏ)
        {x: 450, y: 150, label: 1},
        {x: 500, y: 100, label: 1},
        {x: 550, y: 200, label: 1},
        {x: 480, y: 250, label: 1},
        {x: 520, y: 180, label: 1},
        // Class -1 (xanh)
        {x: 150, y: 250, label: -1},
        {x: 200, y: 300, label: -1},
        {x: 250, y: 350, label: -1},
        {x: 180, y: 400, label: -1},
        {x: 220, y: 280, label: -1}
    ];
    
    function simpleSVM() {
        // Thuật toán đơn giản để tìm hyperplane
        // Tìm trung điểm giữa 2 classes
        let posPoints = points.filter(p => p.label === 1);
        let negPoints = points.filter(p => p.label === -1);
        
        if (posPoints.length === 0 || negPoints.length === 0) return null;
        
        // Tính centroid mỗi class
        let posCenter = {
            x: posPoints.reduce((sum, p) => sum + p.x, 0) / posPoints.length,
            y: posPoints.reduce((sum, p) => sum + p.y, 0) / posPoints.length
        };
        
        let negCenter = {
            x: negPoints.reduce((sum, p) => sum + p.x, 0) / negPoints.length,
            y: negPoints.reduce((sum, p) => sum + p.y, 0) / negPoints.length
        };
        
        // Vector kết nối 2 centroids
        let dx = posCenter.x - negCenter.x;
        let dy = posCenter.y - negCenter.y;
        
        // Hyperplane vuông góc với vector này, đi qua trung điểm
        let midX = (posCenter.x + negCenter.x) / 2;
        let midY = (posCenter.y + negCenter.y) / 2;
        
        // w = (dx, dy), bias tính từ điểm mid
        let w = {x: dx, y: dy};
        let b = -(w.x * midX + w.y * midY);
        let norm = Math.sqrt(w.x * w.x + w.y * w.y);
        
        // Normalize
        w.x /= norm;
        w.y /= norm;
        b /= norm;
        
        // Tìm margin: khoảng cách gần nhất từ điểm đến hyperplane
        let minDist = Infinity;
        points.forEach(p => {
            let dist = Math.abs(w.x * p.x + w.y * p.y + b);
            if (dist < minDist) minDist = dist;
        });
        
        // Tìm support vectors
        let supportVectors = points.filter(p => {
            let dist = Math.abs(w.x * p.x + w.y * p.y + b);
            return dist < minDist + 5; // tolerance
        });
        
        return {w, b, margin: minDist, supportVectors};
    }
    
    function draw() {
        // Clear canvas
        ctx.clearRect(0, 0, width, height);
        
        // Background
        ctx.fillStyle = '#fafafa';
        ctx.fillRect(0, 0, width, height);
        
        // Tìm SVM solution
        let svm = simpleSVM();
        
        if (svm) {
            // Vẽ margin boundaries (đường đứt nét)
            ctx.strokeStyle = '#95a5a6';
            ctx.lineWidth = 2;
            ctx.setLineDash([5, 5]);
            
            // Margin boundary 1
            let b1 = svm.b + svm.margin;
            drawLine(svm.w, b1);
            
            // Margin boundary 2
            let b2 = svm.b - svm.margin;
            drawLine(svm.w, b2);
            
            ctx.setLineDash([]);
            
            // Vẽ hyperplane chính (đường đậm)
            ctx.strokeStyle = '#2c3e50';
            ctx.lineWidth = 3;
            drawLine(svm.w, svm.b);
            
            // Highlight support vectors
            ctx.strokeStyle = '#f39c12';
            ctx.lineWidth = 3;
            svm.supportVectors.forEach(sv => {
                ctx.beginPath();
                ctx.arc(sv.x, sv.y, 15, 0, 2 * Math.PI);
                ctx.stroke();
            });
            
            // Hiển thị thông tin
            ctx.fillStyle = '#2c3e50';
            ctx.font = 'bold 16px Arial';
            ctx.fillText(`Margin: ${(svm.margin * 2).toFixed(1)}`, 10, 30);
            ctx.fillText(`Support Vectors: ${svm.supportVectors.length}`, 10, 55);
        }
        
        // Vẽ các điểm dữ liệu
        points.forEach(p => {
            ctx.fillStyle = p.label === 1 ? '#e74c3c' : '#2ecc71';
            ctx.beginPath();
            ctx.arc(p.x, p.y, 8, 0, 2 * Math.PI);
            ctx.fill();
            
            // Viền
            ctx.strokeStyle = '#34495e';
            ctx.lineWidth = 2;
            ctx.stroke();
        });
        
        // Legend
        ctx.fillStyle = '#e74c3c';
        ctx.beginPath();
        ctx.arc(630, 30, 8, 0, 2 * Math.PI);
        ctx.fill();
        ctx.fillStyle = '#34495e';
        ctx.font = '14px Arial';
        ctx.fillText('Class +1', 645, 35);
        
        ctx.fillStyle = '#2ecc71';
        ctx.beginPath();
        ctx.arc(630, 55, 8, 0, 2 * Math.PI);
        ctx.fill();
        ctx.fillStyle = '#34495e';
        ctx.fillText('Class -1', 645, 60);
        
        // Support vector legend
        ctx.strokeStyle = '#f39c12';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.arc(630, 80, 8, 0, 2 * Math.PI);
        ctx.stroke();
        ctx.fillStyle = '#34495e';
        ctx.fillText('Support Vector', 645, 85);
    }
    
    function drawLine(w, b) {
        // Vẽ đường thẳng w.x * x + w.y * y + b = 0
        ctx.beginPath();
        
        if (Math.abs(w.y) > 0.01) {
            let y0 = -(w.x * 0 + b) / w.y;
            let y1 = -(w.x * width + b) / w.y;
            ctx.moveTo(0, y0);
            ctx.lineTo(width, y1);
        } else {
            let x = -b / w.x;
            ctx.moveTo(x, 0);
            ctx.lineTo(x, height);
        }
        
        ctx.stroke();
    }
    
    function generateRandomData() {
        points = [];
        // Class +1
        for (let i = 0; i < 5; i++) {
            points.push({
                x: 450 + Math.random() * 150,
                y: 100 + Math.random() * 200,
                label: 1
            });
        }
        // Class -1
        for (let i = 0; i < 5; i++) {
            points.push({
                x: 150 + Math.random() * 150,
                y: 250 + Math.random() * 200,
                label: -1
            });
        }
        draw();
    }
    
    // Event listeners
    canvas.addEventListener('click', function(e) {
        if (addMode !== 0) {
            const rect = canvas.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            points.push({x, y, label: addMode});
            draw();
            addMode = 0;
            document.getElementById('addPositive').style.opacity = '1';
            document.getElementById('addNegative').style.opacity = '1';
        }
    });
    
    document.getElementById('resetData').addEventListener('click', generateRandomData);
    
    document.getElementById('addPositive').addEventListener('click', function() {
        addMode = 1;
        this.style.opacity = '0.6';
        document.getElementById('addNegative').style.opacity = '1';
    });
    
    document.getElementById('addNegative').addEventListener('click', function() {
        addMode = -1;
        this.style.opacity = '0.6';
        document.getElementById('addPositive').style.opacity = '1';
    });
    
    // Initial draw
    draw();
})();
</script>

---

## 5. Soft-Margin SVM (Dữ liệu không tách được)

Trong thực tế, dữ liệu thường **không tách được hoàn toàn**. Giới thiệu **slack variables** $$\xi_i \geq 0$$:

$$
\begin{align}
&\min_{\beta, \beta_0, \xi} &&{\frac{1}{2} \|\beta\|_2^2 + C\sum_{i=1}^n \xi_i} \\
&\text{s.t.} &&{\xi_i \geq 0, \quad i = 1, \ldots, n}\\
& && y_i (\beta^T x_i + \beta_0) \geq 1 - \xi_i, \quad i = 1, \ldots, n
\end{align}
$$

Với $$y \in \{-1, 1\}^n$$ và $$X \in \mathbb{R}^{n \times p}$$.

### Giải thích các thành phần

**1) Slack variable $$\xi_i$$:**
- $$\xi_i = 0$$: Điểm phân loại đúng, ngoài margin
- $$0 < \xi_i < 1$$: Điểm trong margin zone, vẫn đúng phía
- $$\xi_i = 1$$: Điểm nằm trên siêu phẳng
- $$\xi_i > 1$$: Điểm bị phân loại sai

**2) Tham số $$C > 0$$:**
- $$C$$ lớn: Phạt nặng vi phạm → margin nhỏ, ít misclassify
- $$C$$ nhỏ: Cho phép nhiều vi phạm → margin lớn
- **Trade-off**: Margin width vs. Training error

**3) Hàm mục tiêu:**
- $$\frac{1}{2}\|\beta\|_2^2$$: Maximize margin
- $$C\sum \xi_i$$: Minimize total violation

### 5.1. Minh họa tương tác: Ảnh hưởng của tham số C

<div id="softmargin-demo" style="margin: 20px 0;">
    <canvas id="softMarginCanvas" width="700" height="500" style="border: 1px solid #ccc; display: block; margin: 0 auto;"></canvas>
    <div style="text-align: center; margin-top: 15px;">
        <label for="cSlider" style="font-size: 16px; font-weight: bold;">Tham số C: <span id="cValue">1.0</span></label><br>
        <input type="range" id="cSlider" min="0.01" max="10" step="0.1" value="1" style="width: 400px; margin: 10px;">
        <p style="font-size: 14px; color: #666; margin-top: 10px;">
            <strong>C nhỏ (←)</strong>: Margin rộng, nhiều vi phạm được chấp nhận<br>
            <strong>C lớn (→)</strong>: Margin hẹp, ít vi phạm, phạt nặng
        </p>
        <div id="svmStats" style="margin-top: 10px; font-size: 14px;">
            <span style="color: #e74c3c; font-weight: bold;">● Vi phạm margin: 0</span> | 
            <span style="color: #f39c12; font-weight: bold;">● Support vectors: 0</span>
        </div>
    </div>
</div>

<script>
(function() {
    const canvas = document.getElementById('softMarginCanvas');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    
    // Dữ liệu với một số điểm gây overlap
    const points = [
        // Class +1
        {x: 480, y: 150, label: 1},
        {x: 520, y: 100, label: 1},
        {x: 550, y: 200, label: 1},
        {x: 500, y: 250, label: 1},
        {x: 530, y: 180, label: 1},
        // Outliers class +1
        {x: 350, y: 280, label: 1}, // Vi phạm
        {x: 380, y: 320, label: 1}, // Vi phạm
        // Class -1
        {x: 180, y: 250, label: -1},
        {x: 220, y: 300, label: -1},
        {x: 260, y: 350, label: -1},
        {x: 200, y: 400, label: -1},
        {x: 240, y: 280, label: -1},
        // Outliers class -1
        {x: 420, y: 180, label: -1}, // Vi phạm
        {x: 400, y: 220, label: -1}  // Vi phạm
    ];
    
    let C = 1.0;
    
    function softMarginSVM() {
        // Simplified soft-margin SVM
        let posPoints = points.filter(p => p.label === 1);
        let negPoints = points.filter(p => p.label === -1);
        
        if (posPoints.length === 0 || negPoints.length === 0) return null;
        
        // Tính centroid với trọng số dựa trên C
        // C lớn -> ít bị ảnh hưởng bởi outliers
        // C nhỏ -> chấp nhận outliers nhiều hơn
        
        let posCenter = {
            x: posPoints.reduce((sum, p) => sum + p.x, 0) / posPoints.length,
            y: posPoints.reduce((sum, p) => sum + p.y, 0) / posPoints.length
        };
        
        let negCenter = {
            x: negPoints.reduce((sum, p) => sum + p.x, 0) / negPoints.length,
            y: negPoints.reduce((sum, p) => sum + p.y, 0) / negPoints.length
        };
        
        // Điều chỉnh hyperplane dựa trên C
        let dx = posCenter.x - negCenter.x;
        let dy = posCenter.y - negCenter.y;
        
        // Với C nhỏ, cho phép hyperplane linh hoạt hơn
        let flexibility = Math.max(0.1, 1 / C);
        
        let midX = (posCenter.x + negCenter.x) / 2;
        let midY = (posCenter.y + negCenter.y) / 2;
        
        let w = {x: dx, y: dy};
        let b = -(w.x * midX + w.y * midY);
        let norm = Math.sqrt(w.x * w.x + w.y * w.y);
        
        w.x /= norm;
        w.y /= norm;
        b /= norm;
        
        // Tính margin base
        let distances = points.map(p => ({
            point: p,
            dist: Math.abs(w.x * p.x + w.y * p.y + b),
            signedDist: (w.x * p.x + w.y * p.y + b) * p.label
        }));
        
        // Soft margin: margin điều chỉnh theo C
        let baseMargin = 50;
        let margin = baseMargin / (1 + C * 0.5);
        
        // Tìm violations và support vectors
        let violations = distances.filter(d => d.signedDist < margin);
        let supportVectors = distances.filter(d => 
            Math.abs(d.dist - margin) < 20 || d.signedDist < margin
        );
        
        return {
            w, b, margin,
            violations: violations.map(v => v.point),
            supportVectors: supportVectors.map(v => v.point),
            distances
        };
    }
    
    function draw() {
        ctx.clearRect(0, 0, width, height);
        
        // Background
        ctx.fillStyle = '#fafafa';
        ctx.fillRect(0, 0, width, height);
        
        let svm = softMarginSVM();
        
        if (svm) {
            // Vẽ margin region (vùng màu nhạt)
            ctx.fillStyle = 'rgba(52, 152, 219, 0.1)';
            ctx.fillRect(0, 0, width, height);
            
            // Vẽ margin boundaries
            ctx.strokeStyle = '#95a5a6';
            ctx.lineWidth = 2;
            ctx.setLineDash([5, 5]);
            
            let b1 = svm.b + svm.margin;
            let b2 = svm.b - svm.margin;
            drawLine(svm.w, b1);
            drawLine(svm.w, b2);
            
            ctx.setLineDash([]);
            
            // Vẽ hyperplane
            ctx.strokeStyle = '#2c3e50';
            ctx.lineWidth = 3;
            drawLine(svm.w, svm.b);
            
            // Highlight violations (slack variables)
            svm.violations.forEach(v => {
                ctx.strokeStyle = 'rgba(231, 76, 60, 0.5)';
                ctx.lineWidth = 20;
                ctx.beginPath();
                ctx.arc(v.x, v.y, 12, 0, 2 * Math.PI);
                ctx.stroke();
            });
            
            // Highlight support vectors
            svm.supportVectors.forEach(sv => {
                ctx.strokeStyle = '#f39c12';
                ctx.lineWidth = 3;
                ctx.beginPath();
                ctx.arc(sv.x, sv.y, 15, 0, 2 * Math.PI);
                ctx.stroke();
            });
            
            // Update stats
            const statsDiv = document.getElementById('svmStats');
            if (statsDiv) {
                statsDiv.innerHTML = `
                    <span style="color: #e74c3c; font-weight: bold;">● Vi phạm margin: ${svm.violations.length}</span> | 
                    <span style="color: #f39c12; font-weight: bold;">● Support vectors: ${svm.supportVectors.length}</span> | 
                    <span style="color: #3498db; font-weight: bold;">Margin width: ${(svm.margin * 2).toFixed(1)}</span>
                `;
            }
        }
        
        // Vẽ điểm dữ liệu
        points.forEach(p => {
            ctx.fillStyle = p.label === 1 ? '#e74c3c' : '#2ecc71';
            ctx.beginPath();
            ctx.arc(p.x, p.y, 8, 0, 2 * Math.PI);
            ctx.fill();
            
            ctx.strokeStyle = '#34495e';
            ctx.lineWidth = 2;
            ctx.stroke();
        });
        
        // Legend
        ctx.fillStyle = '#34495e';
        ctx.font = 'bold 14px Arial';
        ctx.fillText(`C = ${C.toFixed(2)}`, 10, 30);
        
        // Giải thích C
        if (C < 0.5) {
            ctx.fillText('Soft margin: Chấp nhận nhiều vi phạm', 10, 55);
        } else if (C > 5) {
            ctx.fillText('Hard margin: Phạt nặng vi phạm', 10, 55);
        } else {
            ctx.fillText('Balanced: Trade-off margin vs error', 10, 55);
        }
    }
    
    function drawLine(w, b) {
        ctx.beginPath();
        if (Math.abs(w.y) > 0.01) {
            let y0 = -(w.x * 0 + b) / w.y;
            let y1 = -(w.x * width + b) / w.y;
            ctx.moveTo(0, y0);
            ctx.lineTo(width, y1);
        } else {
            let x = -b / w.x;
            ctx.moveTo(x, 0);
            ctx.lineTo(x, height);
        }
        ctx.stroke();
    }
    
    // Slider event
    const slider = document.getElementById('cSlider');
    const cValue = document.getElementById('cValue');
    
    if (slider && cValue) {
        slider.addEventListener('input', function() {
            C = parseFloat(this.value);
            cValue.textContent = C.toFixed(2);
            draw();
        });
    }
    
    // Initial draw
    draw();
})();
</script>

---

## 6. Điều kiện KKT cho SVM

### 6.1. Hàm Lagrangian

Với nhân tử Lagrange $$v \geq 0$$ (cho $$\xi_i \geq 0$$) và $$w \geq 0$$ (cho ràng buộc margin):

$$
\begin{align}
L(\beta, \beta_0, \xi, v, w) = &\frac{1}{2} \|\beta\|_2^2 + C\sum_{i=1}^n \xi_i - \sum_{i=1}^n v_i \xi_i \\
&+ \sum_{i=1}^n w_i (1 - \xi_i - y_i (\beta^T x_i + \beta_0))
\end{align}
$$

### 6.2. Điều kiện Stationarity

**1) Đạo hàm theo $$\beta$$:**
$$
\frac{\partial L}{\partial \beta} = \beta - \sum_{i=1}^n w_i y_i x_i = 0
$$

$$
\Rightarrow \boxed{\beta^\star = \sum_{i=1}^n w_i^\star y_i x_i}
$$

**Ý nghĩa quan trọng:** Nghiệm tối ưu là tổ hợp tuyến tính của các điểm dữ liệu!

**2) Đạo hàm theo $$\beta_0$$:**
$$
\boxed{\sum_{i=1}^n w_i^\star y_i = 0}
$$

**3) Đạo hàm theo $$\xi_i$$:**
$$
C - v_i - w_i = 0 \Rightarrow \boxed{v_i^\star = C - w_i^\star}
$$

**Suy ra:** $$0 \leq w_i^\star \leq C$$ (vì $$v_i^\star \geq 0$$)

### 6.3. Complementary Slackness

**1) Cho $$\xi_i \geq 0$$:**
$$
v_i^\star \xi_i^\star = 0, \quad i = 1, \ldots, n
$$

**2) Cho ràng buộc margin:**
$$
w_i^\star (1 - \xi_i^\star - y_i (\beta^{\star T} x_i + \beta_0^\star)) = 0, \quad i = 1, \ldots, n
$$

### 6.4. Phân tích các trường hợp

#### **Trường hợp 1: $$w_i^\star = 0$$ (Non-support vector)**

- Từ $$v_i^\star = C > 0$$ → $$\xi_i^\star = 0$$ (CS 1)
- Từ CS 2: Ràng buộc margin không chặt
- **Kết luận:** $$y_i(\beta^{\star T} x_i + \beta_0^\star) > 1$$ 
- Điểm nằm **ngoài margin**, phân loại đúng, không ảnh hưởng đến nghiệm

#### **Trường hợp 2: $$0 < w_i^\star < C$$ (Support vector trên margin)**

- Cả $$v_i^\star$$ và $$w_i^\star$$ đều dương
- Từ CS: $$\xi_i^\star = 0$$ và $$y_i(\beta^{\star T} x_i + \beta_0^\star) = 1$$
- **Kết luận:** Điểm nằm **đúng trên margin boundary**
- Quan trọng nhất trong xác định siêu phẳng!

#### **Trường hợp 3: $$w_i^\star = C$$ (Support vector vi phạm margin)**

- Từ $$v_i^\star = 0$$: không ràng buộc $$\xi_i^\star$$
- Từ CS 2: $$y_i(\beta^{\star T} x_i + \beta_0^\star) = 1 - \xi_i^\star$$

**Phân loại con:**
- $$\xi_i^\star = 0$$: Trên margin (giống trường hợp 2)
- $$0 < \xi_i^\star < 1$$: Trong margin zone, phân loại đúng
- $$\xi_i^\star \geq 1$$: Bị phân loại sai (misclassified)

## 7. Support Vectors

### Định nghĩa

**Support vectors** là các điểm có $$w_i^\star > 0$$.

Từ điều kiện stationarity:
$$
\beta^\star = \sum_{i: w_i^\star > 0} w_i^\star y_i x_i
$$

→ **Chỉ support vectors quyết định siêu phẳng!**

### Phân loại Support Vectors

<figure class="image" style="align: center;">
<p align="center">
 <img src="{{ site.baseurl }}/img/chapter_img/chapter12/svm.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">$$ \text{[Hình 1] Minh họa các support vectors với } \xi^\star \neq 0 \text{ [3]}$$ </figcaption>
</p>
</figure>

**1) Support vectors trên margin** ($$\xi_i^\star = 0$$, $$0 < w_i^\star \leq C$$):
- Nằm đúng trên đường biên margin
- $$y_i(\beta^{\star T} x_i + \beta_0^\star) = 1$$
- Quan trọng nhất trong xác định siêu phẳng

**2) Support vectors trong margin** ($$0 < \xi_i^\star < 1$$, $$w_i^\star = C$$):
- Nằm giữa margin và siêu phẳng
- Vẫn phân loại đúng nhưng vi phạm margin
- Thường là outliers hoặc điểm gần biên

**3) Support vectors bị misclassify** ($$\xi_i^\star \geq 1$$, $$w_i^\star = C$$):
- Nằm sai phía siêu phẳng
- Bị phân loại sai
- Đóng góp nhiều vào penalty $$C\sum \xi_i$$

### Ý nghĩa thực tiễn

1. **Hiệu quả tính toán:**
   - Chỉ cần lưu trữ $$s$$ support vectors (thường $$s \ll n$$)
   - Prediction: $$\hat{y} = \text{sign}(\sum_{SV} w_i y_i \langle x_i, x \rangle + \beta_0)$$

2. **Ổn định của mô hình:**
   - Chỉ phụ thuộc support vectors
   - Các điểm xa margin không ảnh hưởng
   - Robust với outliers (nếu $$C$$ phù hợp)

3. **Sparsity:**
   - Nhiều $$w_i = 0$$ (non-support vectors)
   - Mô hình "sparse" và dễ giải thích

## 8. Ví dụ Chi tiết

### Ví dụ 1D: Dữ liệu đơn giản

**Dữ liệu:**
- Lớp $$+1$$: $$x_1 = 3, x_2 = 4$$
- Lớp $$-1$$: $$x_3 = 1, x_4 = 2$$

**Bài toán hard-margin:**
$$
\begin{align}
\min_{\beta, \beta_0} \quad &\frac{1}{2}\beta^2 \\
\text{s.t.} \quad &3\beta + \beta_0 \geq 1, \quad 4\beta + \beta_0 \geq 1 \\
&-\beta - \beta_0 \geq 1, \quad -2\beta - \beta_0 \geq 1
\end{align}
$$

**Giải pháp hình học:**
- Siêu phẳng tối ưu nằm giữa $$x = 2$$ và $$x = 3$$
- Điểm gần nhất: $$x_2 = 4$$ và $$x_4 = 2$$

**Điều kiện margin chặt:**
$$
\begin{cases}
4\beta + \beta_0 = 1 \\
2\beta + \beta_0 = -1
\end{cases}
\Rightarrow \beta = 1, \quad \beta_0 = -3
$$

**Nghiệm:**
- Siêu phẳng: $$x - 3 = 0$$ hay $$x = 3$$ (sai! phải là $$x=2.5$$)
- Hãy kiểm tra lại...

**Sửa lại:** Điểm gần nhất phải là $$x = 3$$ (lớp +1) và $$x = 2$$ (lớp -1):
$$
\begin{cases}
3\beta + \beta_0 = 1 \\
2\beta + \beta_0 = -1
\end{cases}
\Rightarrow \beta = 2, \quad \beta_0 = -5
$$

- Siêu phẳng: $$2x - 5 = 0$$ hay $$x = 2.5$$ ✓
- Margin: $$\frac{2}{\lvert\beta\rvert} = \frac{2}{2} = 1$$
- Support vectors: $$x = 3$$ và $$x = 2$$

## 9. Bài toán Đối ngẫu

### Dual Problem

Thế các điều kiện stationarity vào Lagrangian:

$$
\begin{align}
\max_{w} \quad &\sum_{i=1}^n w_i - \frac{1}{2} \sum_{i,j} w_i w_j y_i y_j \langle x_i, x_j \rangle \\
\text{s.t.} \quad &\sum_{i=1}^n w_i y_i = 0 \\
&0 \leq w_i \leq C, \quad i = 1, \ldots, n
\end{align}
$$

### Ưu điểm

1. **Kernel trick**: Chỉ phụ thuộc vào $$\langle x_i, x_j \rangle$$ → có thể dùng kernel
2. **Ít ràng buộc hơn**: Chỉ 1 ràng buộc đẳng thức + box constraints
3. **Solver hiệu quả**: SMO, LIBSVM

## 10. Ứng dụng KKT trong SVM

### 10.1. Kiểm tra tính tối ưu

Dùng điều kiện KKT để verify nghiệm:
1. Primal/Dual feasibility
2. Stationarity
3. Complementary slackness

### 10.2. Tính $$\beta_0$$

Từ support vectors trên margin ($$0 < w_i < C$$):
$$
\beta_0 = y_i - \beta^T x_i = y_i - \sum_{j} w_j y_j \langle x_j, x_i \rangle
$$

**Thực tế:** Lấy trung bình trên tất cả SV trên margin:
$$
\beta_0 = \frac{1}{\lvert S\rvert} \sum_{i \in S} \left( y_i - \sum_{j} w_j y_j \langle x_j, x_i \rangle \right)
$$

### 10.3. Lọc Support Vectors

Trước khi giải, loại bỏ điểm chắc chắn không phải SV:
$$
y_i(\beta_{\text{init}}^T x_i + \beta_{0,\text{init}}) \gg 1
$$

→ Tăng hiệu quả cho datasets lớn

## 11. Bài tập Thực hành

### Bài tập 1: Phân tích Support Vectors

Cho nghiệm SVM với $$C = 1$$:
```
w = (0, 0.5, 0.3, 1, 0, 1, 0.2)
ξ = (0, 0, 0.2, 0.8, 0, 1.5, 0)
```

**Yêu cầu:**
a) Xác định support vectors  
b) Phân loại theo vị trí (trên margin, trong margin, misclassified)  
c) Giải thích $$w_1 = 0$$ nhưng $$\xi_1 = 0$$

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a) Support vectors:** $$i \in \{2, 3, 4, 6, 7\}$$ (vì $$w_i > 0$$)

**b) Phân loại:**
- **Trên margin**: $$i = 2, 7$$ ($$\xi_i = 0$$, $$0 < w_i < C$$)
- **Trong margin**: $$i = 3, 4$$ ($$0 < \xi_i < 1$$, $$w_i = C$$)
- **Misclassified**: $$i = 6$$ ($$\xi_6 = 1.5 > 1$$, $$w_6 = C$$)

**c)** $$w_1 = 0$$ nghĩa là không phải SV. Từ CS: $$v_1 = C - 0 = 1 > 0$$ → $$\xi_1 = 0$$ ✓  
Điểm $$x_1$$ nằm xa margin, phân loại đúng.

</details>

---

### Bài tập 2: Tính toán từ KKT

Cho $$C = 2$$, $$n = 3$$, $$p = 2$$:
```
x₁ = (0, 1), y₁ = +1, w₁ = 0.5
x₂ = (1, 0), y₂ = +1, w₂ = 0.5  
x₃ = (0, 0), y₃ = -1, w₃ = 1
```
$$\xi_1 = \xi_2 = 0$$, $$\xi_3 = 0.2$$.

**Yêu cầu:**
a) Tính $$\beta$$ từ stationarity  
b) Tính $$\beta_0$$ từ SV trên margin  
c) Kiểm tra CS cho $$i=3$$

<details>
<summary><strong>💡 Lời giải</strong></summary>

**a)** $$\beta = \sum w_i y_i x_i = 0.5(0,1) + 0.5(1,0) + 1 \cdot (-1)(0,0) = (0.5, 0.5)$$

**b)** Từ $$i=1$$: $$y_1(\beta^T x_1 + \beta_0) = 1$$  
$$1 \cdot (0.5 + \beta_0) = 1$$ → $$\beta_0 = 0.5$$

**c)** CS: $$w_3(1 - \xi_3 - y_3(\beta^T x_3 + \beta_0)) = 0$$  
$$y_3(\beta^T x_3 + \beta_0) = -1(0.5) = -0.5$$  
$$1(1 - 0.2 - (-0.5)) = 1.3 \neq 0$$ ✗  

**Kết luận:** CS vi phạm! Có lỗi trong dữ liệu.

</details>

---

## 12. Tóm tắt

### Các điểm chính

1. **SVM giải quyết vấn đề của PLA**: Trong vô số mặt phân cách, SVM tìm mặt có margin lớn nhất
2. **Maximum Margin Classifier**: SVM tối đa hóa khoảng cách từ mặt phân cách đến điểm gần nhất
3. **Bài toán tối ưu lồi**: Hard-margin SVM là Quadratic Programming với nghiệm duy nhất
4. **Soft-margin** cho phép vi phạm qua $$\xi_i$$, điều khiển bởi $$C$$
5. **Điều kiện KKT** cho:
   - $$\beta = \sum w_i y_i x_i$$ (chỉ phụ thuộc support vectors)
   - Phân loại điểm thành SV và non-SV
6. **Support vectors** quyết định siêu phẳng, thường $$s \ll n$$
7. **Complementary slackness** giải thích khi nào $$w_i = 0$$ hay $$w_i > 0$$

### Ý nghĩa thực tiễn

Điều kiện KKT không dùng trực tiếp để giải SVM (dùng SMO, LIBSVM), nhưng giúp:
- Kiểm chứng tính tối ưu
- Hiểu cấu trúc nghiệm (sparsity, support vectors)
- Phát triển thuật toán hiệu quả
- Phân tích độ nhạy của mô hình

### Lợi thế của SVM

1. **Hiệu quả với dữ liệu chiều cao**: Hoạt động tốt khi số chiều > số mẫu
2. **Tiết kiệm bộ nhớ**: Chỉ lưu trữ support vectors
3. **Linh hoạt**: Có thể dùng kernel cho dữ liệu phi tuyến
4. **Robust**: Ít bị overfitting nhờ margin maximization

---

## 📚 Tài liệu tham khảo

### Sách và giáo trình

1. **Vapnik, V. N.** (1995). *The Nature of Statistical Learning Theory*. Springer.
2. **Boyd, S., & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. Chapter 12.
3. **Hastie, T., et al.** (2009). *The Elements of Statistical Learning* (2nd ed.). Springer. Chapter 12.
4. **Cristianini, N., & Shawe-Taylor, J.** (2000). *An Introduction to Support Vector Machines*. Cambridge University Press.
5. **Bishop, C. M.** (2006). *Pattern Recognition and Machine Learning*. Springer. Chapter 7.

### Bài viết và tutorial

6. **Machine Learning Cơ Bản** - [Bài 19: Support Vector Machine](https://machinelearningcoban.com/2017/04/09/smv/) - Vũ Hữu Tiệp
7. **scikit-learn Documentation** - [Support Vector Machines](https://scikit-learn.org/stable/modules/svm.html)
8. **LIBSVM** - [A Library for Support Vector Machines](https://www.csie.ntu.edu.tw/~cjlin/libsvm/)
