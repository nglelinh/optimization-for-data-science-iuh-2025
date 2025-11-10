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

## 1. Giới thiệu

**Support Vector Machine (SVM)** là một trong những thuật toán máy học cổ điển và mạnh mẽ nhất cho bài toán phân loại. Được phát triển bởi Vladimir Vapnik và cộng sự vào những năm 1990, SVM đã tạo nên một cuộc cách mạng trong lĩnh vực machine learning nhờ nền tảng toán học vững chắc và khả năng xử lý dữ liệu chiều cao một cách hiệu quả.

**Ý tưởng cốt lõi:** Hãy tưởng tượng bạn cần vẽ một đường thẳng để phân chia hai nhóm điểm trên mặt phẳng. Có vô số cách vẽ, nhưng đường nào là "tốt nhất"? SVM trả lời câu hỏi này bằng cách tìm **đường phân chia có khoảng cách lớn nhất** đến các điểm gần nhất của cả hai nhóm. Khoảng cách này được gọi là **margin (biên độ)**. Margin càng lớn, mô hình càng "tự tin" trong việc phân loại và có khả năng tổng quát hóa tốt hơn trên dữ liệu mới.

**Lộ trình bài học:** Chúng ta sẽ cùng nhau đi từ trực giác hình học đến công thức toán học một cách tự nhiên:
- Bắt đầu với **trực giác hình học**: Tại sao margin lớn lại quan trọng?
- Chuyển sang **công thức toán học**: Biểu diễn bài toán dưới dạng tối ưu lồi (Quadratic Programming)
- Khám phá **support vectors**: Những điểm dữ liệu "quyết định" siêu phẳng phân cách
- Mở rộng sang **Soft-Margin SVM**: Xử lý dữ liệu thực tế có nhiễu và không tách được hoàn toàn
- Nghiên cứu **bài toán đối ngẫu**: Cánh cửa dẫn đến kernel trick và các ứng dụng nâng cao

### 1.1. Kiến thức nền tảng: Khoảng cách từ điểm tới siêu phẳng

Trước khi bắt đầu, hãy ôn lại một công thức quan trọng từ hình học giải tích:

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

### 1.2. Ý tưởng cốt lõi - Ba khái niệm then chốt

Trước khi đi vào chi tiết, hãy nắm vững ba khái niệm nền tảng:

- **Siêu phẳng phân cách**: Trong không gian nhiều chiều, siêu phẳng $$\beta^T x + \beta_0 = 0$$ đóng vai trò như một "bức tường" chia không gian thành hai vùng, mỗi vùng chứa một lớp dữ liệu.

- **Margin (Biên độ)**: Đây là khoảng cách từ siêu phẳng đến điểm gần nhất trong mỗi lớp. Khi siêu phẳng nằm ở vị trí tối ưu, margin bằng $$\frac{2}{\|\beta\|}$$ (chúng ta sẽ chứng minh điều này sau).

- **Mục tiêu tối ưu**: Maximize margin $$\Leftrightarrow$$ Minimize $$\|\beta\|$$. Tại sao lại tương đương? Vì margin tỉ lệ nghịch với $$\|\beta\|$$, nên margin lớn nhất khi $$\|\beta\|$$ nhỏ nhất.

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

## 2. Bài toán phân chia hai lớp dữ liệu

Hãy bắt đầu với một tình huống đơn giản nhưng đầy thách thức: chúng ta có hai nhóm (lớp) điểm dữ liệu trong không gian nhiều chiều, và hai nhóm này **tách được tuyến tính** (linearly separable). Điều này có nghĩa là tồn tại ít nhất một siêu phẳng có thể phân chia hoàn toàn hai nhóm - tất cả điểm của nhóm A nằm về một phía, tất cả điểm của nhóm B nằm về phía đối diện.

**Nhiệm vụ của chúng ta:** Tìm một siêu phẳng phân chia sao cho không có điểm nào "đi lạc" - mỗi điểm phải nằm đúng phía của siêu phẳng tương ứng với nhãn của nó.

**Thách thức đầu tiên:** Nếu dữ liệu tách được tuyến tính, chúng ta có **vô số cách chọn** siêu phẳng phân chia! Minh họa dưới đây cho thấy ba đường thẳng khác nhau đều phân chia chính xác hai lớp:

<figure class="image" style="align: center;">
<p align="center">
 <img src="https://machinelearningcoban.com/assets/19_svm/svm1.png" alt="" width="60%" height="60%">
 <figcaption style="text-align: center;">$$ \text{[Hình 2] Các mặt phân cách khả dĩ cho hai classes linearly separable}$$ </figcaption>
</p>
</figure>

**Câu hỏi then chốt:** Trong vô số các mặt phân chia đều "đúng" về mặt phân loại, **đâu là mặt phân chia TỐT NHẤT**? 

Hãy quan sát kỹ hình minh họa phía trên. Bạn có nhận thấy gì không? Hai đường thẳng đầu tiên "lệch" khá nhiều về phía các điểm hình tròn đỏ - chúng dường như "sợ" các điểm hình vuông xanh và né tránh chúng. Trong khi đó, đường thẳng thứ ba nằm gần như chính giữa hai nhóm, tạo ra một "vùng an toàn" xung quanh nó.

Trực giác cho chúng ta biết: đường phân chia ở giữa sẽ "tự tin" và "robust" hơn khi gặp dữ liệu mới. Nhưng làm thế nào để biến trực giác này thành một công thức toán học cụ thể?

### 2.1. Tiêu chuẩn: Maximum Margin - Từ trực giác đến định lượng

SVM giải quyết vấn đề này bằng một ý tưởng cực kỳ tinh tế: sử dụng khái niệm **margin** (lề, biên độ) để định lượng mức độ "an toàn" của một đường phân chia.

<figure class="image" style="align: center;">
<p align="center">
 <img src="https://machinelearningcoban.com/assets/19_svm/svm2.png" alt="" width="70%" height="70%">
 <figcaption style="text-align: center;">$$ \text{[Hình 3] So sánh các mặt phân cách với margin khác nhau}$$ </figcaption>
</p>
</figure>

**Margin là gì?** Đơn giản nhất, margin là khoảng cách từ siêu phẳng phân cách đến **điểm gần nhất** của mỗi lớp dữ liệu. Hãy nghĩ về nó như "vùng đệm an toàn" xung quanh đường phân chia.

**Siêu phẳng tối ưu phải thỏa mãn hai nguyên tắc vàng:**

1. **Công bằng (Đối xứng)**: Khoảng cách từ siêu phẳng đến điểm gần nhất của lớp A phải **bằng** khoảng cách đến điểm gần nhất của lớp B. Không thiên vị lớp nào cả!

2. **Tối đa hóa an toàn**: Trong tất cả các siêu phẳng công bằng, chọn cái có margin **lớn nhất** - tức "vùng đệm" rộng nhất.

**Tại sao margin lớn lại quan trọng?** Ba lý do thực tiễn:

- **Khả năng tổng quát hóa**: Margin rộng giống như có "vùng dung sai" lớn. Khi có dữ liệu mới hơi lệch so với dữ liệu huấn luyện, mô hình vẫn phân loại đúng.
  
- **Độ tin cậy**: Điểm dữ liệu càng xa siêu phẳng, quyết định phân loại càng "tự tin". Margin lớn nghĩa là hầu hết điểm đều được phân loại với độ tin cậy cao.
  
- **Chống nhiễu**: Nếu có vài điểm bị nhiễu (đo đạc sai, outliers), margin lớn giúp mô hình ít bị ảnh hưởng.

**Kết luận quan trọng**: Bài toán SVM chính là bài toán tìm mặt phân cách có **margin lớn nhất**. Vì vậy, SVM còn được gọi là **Maximum Margin Classifier** - bộ phân loại margin cực đại.

---

## 3. Xây dựng bài toán tối ưu cho SVM

Chúng ta đã có trực giác rõ ràng: cần tìm siêu phẳng có margin lớn nhất. Giờ là lúc biến trực giác này thành **ngôn ngữ toán học chính xác** - một bài toán tối ưu mà máy tính có thể giải được. Hành trình này sẽ đưa chúng ta từ hình học trực quan đến một bài toán Quadratic Programming chuẩn.

### 3.1. Thiết lập ký hiệu

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

### 3.2. Công thức khoảng cách - Một mẹo toán học tinh tế

Với cặp dữ liệu $$(x_n, y_n)$$ bất kỳ, khoảng cách từ điểm $$x_n$$ tới siêu phẳng phân chia được tính bởi:

$$
\frac{y_n(w^T x_n + b)}{\|w\|_2}
$$

**Tại sao lại có $$y_n$$ ở tử số?** Đây là một mẹo thông minh! Nhớ lại rằng:
- Nếu $$x_n$$ thuộc lớp +1, nó nằm ở phía dương của siêu phẳng → $$w^T x_n + b > 0$$
- Nếu $$x_n$$ thuộc lớp -1, nó nằm ở phía âm của siêu phẳng → $$w^T x_n + b < 0$$

Vì theo giả sử mô hình phân loại đúng, $$y_n$$ luôn **cùng dấu** với $$(w^T x_n + b)$$. Do đó:
$$
y_n(w^T x_n + b) > 0 \quad \text{(luôn dương!)}
$$

Nhân với $$y_n$$ giúp ta **loại bỏ dấu giá trị tuyệt đối** trong công thức khoảng cách, làm cho các phép toán sau này đơn giản hơn rất nhiều!

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

### 3.5. Biến đổi về bài toán đơn giản - Thủ thuật chuẩn hóa

Trước khi tiếp tục, chúng ta cần một **quan sát quan trọng** giúp đơn giản hóa bài toán đáng kể.

**Tính bất định về tỷ lệ:** Giả sử ta có một siêu phẳng $$w^T x + b = 0$$. Nếu nhân cả $$w$$ và $$b$$ với cùng một hằng số dương $$k > 0$$, ta được siêu phẳng mới $$(kw)^T x + kb = 0$$. Điều kỳ diệu là:
- Mặt phân chia **vẫn là cùng một mặt** (vì phương trình vẫn cho cùng tập hợp các điểm thỏa mãn)
- Khoảng cách từ mỗi điểm đến mặt phân chia **không đổi** (phép chia cho $$\|kw\| = k\|w\|$$ triệt tiêu hệ số $$k$$)
- Do đó, margin cũng **không đổi**!

**Thủ thuật chuẩn hóa thông minh:** Vì tỷ lệ của $$w$$ và $$b$$ không quan trọng, ta có thể tự do chọn tỷ lệ sao cho tiện tính toán nhất. Cụ thể, ta sẽ **chuẩn hóa** sao cho với những điểm **gần siêu phẳng nhất** (sau này gọi là support vectors), ta có:

$$
y_n(w^T x_n + b) = 1
$$

Đây là một quy ước tuyệt vời vì nó biến margin thành công thức rất đẹp: $$\text{margin} = \frac{1}{\|w\|}$$.

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

### 3.9. Xác định class cho điểm mới

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

## 5. Soft-Margin SVM: Đối mặt với dữ liệu thực tế

Cho đến nay, chúng ta đã làm việc với một giả thiết lý tưởng: dữ liệu **hoàn toàn tách được tuyến tính**, không có điểm nào vi phạm margin. Đây là **Hard-Margin SVM** - một mô hình "cứng nhắc" không cho phép bất kỳ ngoại lệ nào.

Nhưng thực tế không hoàn hảo như vậy!

### 5.0. Khi lý thuyết gặp thực tiễn: Tại sao cần Slack Variables?

**Yêu cầu khắt khe của Hard-Margin SVM:**

Mọi điểm dữ liệu phải thỏa mãn:
$$
y_i (\beta^T x_i + \beta_0) \geq 1, \quad \forall i = 1,\ldots,n
$$

Điều này nghĩa là **TẤT CẢ** các điểm - không ngoại lệ - phải:
1. Được phân loại **hoàn toàn đúng** (nằm đúng phía của siêu phẳng)
2. Nằm **ngoài vùng margin** (cách siêu phẳng ít nhất 1 đơn vị chuẩn hóa)

**Ba tình huống phổ biến khiến Hard-Margin SVM "bó tay":**

**1) Dữ liệu không tách được tuyến tính (Linearly Non-separable):**
```
Class +1:  ○ ○ ○ ● ○     ← Có 1 điểm class -1 lọt vào
                          
Class -1:  ● ● ● ○ ●     ← Có 1 điểm class +1 lọt vào
```
→ **KHÔNG TỒN TẠI** siêu phẳng nào tách được hoàn toàn!

**2) Outliers (Điểm nhiễu):**
```
Class +1:  ○ ○ ○ ○
                      ●  ← Outlier duy nhất
Class -1:  ● ● ● ●
```
→ Outlier có thể **kéo lệch** siêu phẳng tối ưu, làm giảm margin!

**3) Overlap tự nhiên:**
- Trong nhiều bài toán thực tế (y tế, tài chính), hai class có **vùng chồng lấn** tự nhiên
- Không có ranh giới rõ ràng 100%

**Giải pháp tinh tế: Slack Variables (Biến nới lỏng) $$\xi_i$$**

Thay vì bắt buộc tất cả điểm phải tuân thủ nghiêm ngặt, chúng ta cho phép **nới lỏng có kiểm soát**:

$$
y_i (\beta^T x_i + \beta_0) \geq 1 - \xi_i, \quad \xi_i \geq 0
$$

**Diễn giải bằng ngôn ngữ đời thường:**

- Mỗi điểm dữ liệu có một **"quyền vi phạm"** riêng, được đo bằng $$\xi_i$$
- Nếu điểm $$i$$ là "outlier" hoặc gần biên quyết định, nó có thể sử dụng $$\xi_i > 0$$ để "xin phép" vi phạm margin
- Nhưng vi phạm **không miễn phí**! Điểm đó phải "trả giá" bằng cách đóng góp $$C \cdot \xi_i$$ vào hàm mục tiêu
- Tham số $$C$$ quyết định "mức phạt": $$C$$ lớn = phạt nặng = ít vi phạm được chấp nhận

**Tại sao đây là ý tưởng xuất sắc:**

- ✅ **Luôn có nghiệm**: Bài toán không bao giờ vô nghiệm (infeasible), vì ta luôn có thể chọn $$\xi_i$$ đủ lớn
- ✅ **Robust với outliers**: Vài điểm lạc không làm sụp đổ toàn bộ mô hình
- ✅ **Linh hoạt**: Xử lý được cả dữ liệu tách được và không tách được tuyến tính
- ✅ **Cân bằng thông minh**: Trade-off giữa "margin rộng" (tổng quát hóa tốt) và "ít lỗi huấn luyện" (độ chính xác cao)

### 5.1. Công thức toán học của Soft-Margin SVM

Dựa trên ý tưởng slack variable ở trên, ta có bài toán tối ưu hoàn chỉnh:

$$
\begin{align}
&\min_{\beta, \beta_0, \xi} &&{\frac{1}{2} \|\beta\|_2^2 + C\sum_{i=1}^n \xi_i} \\
&\text{s.t.} &&{\xi_i \geq 0, \quad i = 1, \ldots, n}\\
& && y_i (\beta^T x_i + \beta_0) \geq 1 - \xi_i, \quad i = 1, \ldots, n
\end{align}
$$

trong đó:
- $$\beta \in \mathbb{R}^p$$: vector trọng số của siêu phẳng
- $$\beta_0 \in \mathbb{R}$$: bias term
- $$\xi = (\xi_1, \ldots, \xi_n) \in \mathbb{R}^n$$: vector slack variables
- $$y \in \{-1, +1\}^n$$: vector nhãn
- $$X \in \mathbb{R}^{n \times p}$$: ma trận dữ liệu

### Giải thích chi tiết các thành phần

**1) Slack variable $$\xi_i$$ - Biến nới lỏng:**

Slack variable đo lường **mức độ vi phạm** của từng điểm dữ liệu. Giá trị của nó cho biết điểm đó nằm ở đâu:

- **$$\xi_i = 0$$**: Điểm **lý tưởng** 
  - Phân loại đúng
  - Nằm ngoài margin (ở phía đúng, cách siêu phẳng $$\geq 1$$ đơn vị)
  - Không vi phạm gì cả
  - Không bị phạt trong hàm mục tiêu

- **$$0 < \xi_i < 1$$**: Điểm **vi phạm margin nhẹ**
  - Vẫn phân loại **đúng** (nằm đúng phía của siêu phẳng)
  - Nhưng nằm **trong vùng margin** (quá gần siêu phẳng)
  - Vi phạm margin boundary
  - Thường là outliers hoặc điểm gần biên quyết định

- **$$\xi_i = 1$$**: Điểm **trên siêu phẳng**
  - Nằm chính xác trên đường phân cách $$\beta^T x_i + \beta_0 = 0$$
  - Không thể quyết định phân loại
  - Điểm giới hạn giữa đúng và sai

- **$$\xi_i > 1$$**: Điểm **bị phân loại sai**
  - Nằm **sai phía** siêu phẳng
  - Misclassified point
  - Bị phạt nặng trong hàm mục tiêu
  - Giá trị $$\xi_i$$ càng lớn, sai càng nghiêm trọng

**2) Tham số $$C > 0$$ - Hằng số điều khiển (Regularization parameter):**

$$C$$ quyết định **cân bằng** giữa hai mục tiêu mâu thuẫn:

- **Vai trò**: Trọng số phạt cho vi phạm margin
- **Ý nghĩa**: "Giá" phải trả khi vi phạm

**Ảnh hưởng của C:**

| Giá trị C | Margin | Vi phạm được chấp nhận | Khả năng tổng quát | Nguy cơ |
|-----------|--------|------------------------|-------------------|---------|
| **$$C$$ rất nhỏ** (→ 0) | Rộng | Nhiều | Tốt (generalize tốt) | Underfitting |
| **$$C$$ trung bình** | Cân bằng | Vừa phải | Tốt nhất | - |
| **$$C$$ rất lớn** (→ ∞) | Hẹp | Rất ít | Kém (fit data) | Overfitting |

**Giải thích chi tiết:**

- **$$C$$ nhỏ** (ví dụ: 0.01):
  - Phạt nhẹ cho vi phạm → chấp nhận nhiều $$\xi_i > 0$$
  - Ưu tiên **margin rộng** hơn là độ chính xác training
  - Mô hình **mềm dẻo**, robust với outliers
  - Có thể bị underfitting

- **$$C$$ lớn** (ví dụ: 100):
  - Phạt nặng cho vi phạm → cố gắng $$\xi_i \approx 0$$
  - Ưu tiên **độ chính xác training** hơn là margin rộng
  - Gần với Hard-Margin SVM
  - Có thể bị overfitting, nhạy cảm với outliers

**Công thức toán học:**

Khi $$C \to \infty$$:
$$
\min \frac{1}{2}\|\beta\|^2 + \underbrace{C\sum \xi_i}_{\text{phải } \approx 0} 
\Rightarrow \xi_i \to 0, \, \forall i
$$
→ Trở về Hard-Margin SVM!

**3) Hàm mục tiêu - Hai thành phần:**

$$
\underbrace{\frac{1}{2}\|\beta\|_2^2}_{\text{(1) Maximize margin}} + \underbrace{C\sum_{i=1}^n \xi_i}_{\text{(2) Minimize violations}}
$$

- **(1) Margin term**: $$\frac{1}{2}\|\beta\|_2^2$$
  - Minimize $$\|\beta\|$$ ⟺ Maximize margin width $$\frac{2}{\|\beta\|}$$
  - Muốn margin **càng rộng càng tốt**

- **(2) Loss term**: $$C\sum_{i=1}^n \xi_i$$
  - Tổng mức độ vi phạm của tất cả các điểm
  - Muốn vi phạm **càng ít càng tốt**
  - $$C$$ là trọng số cân bằng hai mục tiêu

### 5.2. Ví dụ số cụ thể về Slack Variable

Để hiểu rõ hơn cách slack variable hoạt động, xét một ví dụ đơn giản:

**Giả sử**: Ta có siêu phẳng đã tìm được: $$\beta = 1, \beta_0 = -2.5$$, tức $$x - 2.5 = 0$$ hay $$x = 2.5$$

**Dữ liệu và phân tích:**

| Điểm | $$x_i$$ | $$y_i$$ | $$y_i(\beta^T x_i + \beta_0)$$ | Ràng buộc | $$\xi_i$$ | Phân loại | Ghi chú |
|------|---------|---------|-------------------------------|-----------|-----------|-----------|---------|
| A | 4.0 | +1 | $$1(4-2.5)=1.5$$ | $$1.5 \geq 1$$ ✓ | **0** | Đúng | Ngoài margin, lý tưởng |
| B | 3.0 | +1 | $$1(3-2.5)=0.5$$ | $$0.5 \geq 1$$ ✗ | **0.5** | Đúng | Trong margin zone |
| C | 2.5 | +1 | $$1(2.5-2.5)=0$$ | $$0 \geq 1$$ ✗ | **1.0** | Biên | Trên siêu phẳng |
| D | 2.0 | +1 | $$1(2-2.5)=-0.5$$ | $$-0.5 \geq 1$$ ✗ | **1.5** | Sai | Bị misclassified |
| E | 1.0 | -1 | $$-1(1-2.5)=1.5$$ | $$1.5 \geq 1$$ ✓ | **0** | Đúng | Ngoài margin, lý tưởng |
| F | 2.0 | -1 | $$-1(2-2.5)=0.5$$ | $$0.5 \geq 1$$ ✗ | **0.5** | Đúng | Trong margin zone |

**Giải thích từng trường hợp:**

1. **Điểm A** ($$x=4, y=+1$$):
   - $$y(\beta^T x + \beta_0) = 1.5 \geq 1$$ → Thỏa ràng buộc!
   - $$\xi_A = 0$$ (không cần nới lỏng)
   - Điểm **lý tưởng**, đúng phía và xa siêu phẳng

2. **Điểm B** ($$x=3, y=+1$$):
   - $$y(\beta^T x + \beta_0) = 0.5 < 1$$ → Vi phạm!
   - Cần $$\xi_B = 0.5$$ để: $$0.5 \geq 1 - 0.5$$ ✓
   - Vẫn phân loại đúng nhưng quá gần siêu phẳng

3. **Điểm C** ($$x=2.5, y=+1$$):
   - Nằm chính xác trên siêu phẳng
   - $$\xi_C = 1.0$$ (ngưỡng giới hạn)

4. **Điểm D** ($$x=2, y=+1$$):
   - Nằm sai phía (bên âm) mặc dù nhãn là +1
   - $$\xi_D = 1.5 > 1$$ → Bị phân loại sai!
   - Đóng góp lớn vào penalty $$C \cdot \xi_D$$

**Tổng penalty:**
$$
\sum_{i=1}^n \xi_i = 0 + 0.5 + 1.0 + 1.5 + 0 + 0.5 = 3.5
$$

**Hàm mục tiêu:**
$$
\frac{1}{2}(1)^2 + C \cdot 3.5 = 0.5 + 3.5C
$$

- Nếu $$C = 1$$: Objective = $$0.5 + 3.5 = 4.0$$
- Nếu $$C = 10$$: Objective = $$0.5 + 35 = 35.5$$ (phạt nặng!)
- Nếu $$C = 0.1$$: Objective = $$0.5 + 0.35 = 0.85$$ (ít quan tâm đến vi phạm)

### 5.3. Minh họa tương tác: Ảnh hưởng của tham số C

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

## 5A. Hinge Loss: Loss Function của SVM

Sau khi hiểu bài toán tối ưu của SVM, chúng ta sẽ tìm hiểu một **góc nhìn khác** - nhìn SVM như một bài toán **minimizing loss function**, tương tự như các thuật toán machine learning khác.

### 5A.1. Từ ràng buộc đến Loss Function

**Nhìn lại Soft-Margin SVM:**

$$
\begin{align}
\min_{\beta, \beta_0, \xi} \quad &\frac{1}{2}\|\beta\|^2 + C\sum_{i=1}^n \xi_i \\
\text{s.t.} \quad &y_i(\beta^T x_i + \beta_0) \geq 1 - \xi_i \\
&\xi_i \geq 0, \quad i = 1, \ldots, n
\end{align}
$$

**Câu hỏi tự nhiên:** Có thể loại bỏ biến phụ $$\xi_i$$ và ràng buộc không?

**Trả lời:** Có! Từ ràng buộc $$\xi_i \geq 0$$ và $$y_i(\beta^T x_i + \beta_0) \geq 1 - \xi_i$$, ta có:

$$
\xi_i \geq \max\{0, 1 - y_i(\beta^T x_i + \beta_0)\}
$$

Để minimize hàm mục tiêu, ta chọn $$\xi_i$$ nhỏ nhất có thể:

$$
\xi_i = \max\{0, 1 - y_i(\beta^T x_i + \beta_0)\}
$$

**Kết quả:** Bài toán tương đương với:

$$
\min_{\beta, \beta_0} \quad \frac{1}{2}\|\beta\|^2 + C\sum_{i=1}^n \underbrace{\max\{0, 1 - y_i(\beta^T x_i + \beta_0)\}}_{\text{Hinge Loss } \ell(y_i, f(x_i))}
$$

Đây chính là **formulation với hinge loss**!

### 5A.2. Định nghĩa Hinge Loss

**Hinge Loss** cho một điểm dữ liệu $$(x_i, y_i)$$ với dự đoán $$f(x_i) = \beta^T x_i + \beta_0$$ được định nghĩa:

$$
\ell_{\text{hinge}}(y_i, f(x_i)) = \max\{0, 1 - y_i f(x_i)\}
$$

hoặc viết gọn hơn:

$$
\ell_{\text{hinge}}(y, f) = [1 - yf]_+ = \begin{cases}
0 & \text{nếu } yf \geq 1 \\
1 - yf & \text{nếu } yf < 1
\end{cases}
$$

với ký hiệu $$[\cdot]_+ = \max\{0, \cdot\}$$ (phần dương).

**Ý nghĩa của từng trường hợp:**

| $$yf(x)$$ | Diễn giải | Hinge Loss | Ý nghĩa |
|-----------|-----------|------------|---------|
| $$> 1$$ | Phân loại đúng, xa margin | $$0$$ | Không bị phạt, điểm lý tưởng |
| $$= 1$$ | Phân loại đúng, trên margin | $$0$$ | Biên giới, không phạt |
| $$0 < yf < 1$$ | Phân loại đúng, trong margin | $$1 - yf > 0$$ | Bị phạt vì vi phạm margin |
| $$yf = 0$$ | Trên siêu phẳng quyết định | $$1$$ | Phạt mức trung bình |
| $$yf < 0$$ | **Phân loại sai** | $$1 - yf > 1$$ | Phạt nặng, sai càng nhiều phạt càng nặng |

**Đồ thị Hinge Loss:**

```
Loss
  |
4 |           /
  |          /
3 |         /  
  |        /   
2 |       /    
  |      /     
1 |_____/      
  |            
0 |____________
  -2  -1  0  1  2  yf(x)
      ↑     ↑
    sai   đúng
```

### 5A.3. So sánh với các Loss Function khác

**1) Zero-One Loss (0-1 Loss):**

$$
\ell_{0-1}(y, f) = \mathbb{I}[yf < 0] = \begin{cases}
0 & \text{nếu phân loại đúng} \\
1 & \text{nếu phân loại sai}
\end{cases}
$$

- **Ý nghĩa**: Đếm số lỗi phân loại, đây là mục tiêu thực sự trong classification
- **Vấn đề**: Không khả vi, không lồi, NP-hard để tối ưu!

**2) Logistic Loss (Log Loss):**

$$
\ell_{\text{logistic}}(y, f) = \log(1 + e^{-yf})
$$

- **Dùng trong**: Logistic Regression
- **Đặc điểm**: Smooth (khả vi mọi nơi), lồi
- **So với hinge**: Không bao giờ bằng 0, luôn phạt (nhẹ) ngay cả khi đúng

**3) Exponential Loss:**

$$
\ell_{\text{exp}}(y, f) = e^{-yf}
$$

- **Dùng trong**: AdaBoost
- **Đặc điểm**: Phạt rất nặng với outliers

**4) Squared Hinge Loss:**

$$
\ell_{\text{squared}}(y, f) = [1 - yf]_+^2
$$

- **Đặc điểm**: Khả vi tại $$yf = 1$$, phạt nặng hơn hinge loss chuẩn

**Bảng so sánh trực quan:**

| Loss Function | Công thức | Lồi | Khả vi | Robust với outliers | Sparse solution |
|---------------|-----------|-----|--------|---------------------|-----------------|
| **0-1 Loss** | $$\mathbb{I}[yf<0]$$ | ❌ | ❌ | ✅ | - |
| **Hinge Loss** | $$[1-yf]_+$$ | ✅ | ⚠️ (subgradient) | ✅ | ✅ |
| **Logistic Loss** | $$\log(1+e^{-yf})$$ | ✅ | ✅ | ⚠️ | ❌ |
| **Exponential Loss** | $$e^{-yf}$$ | ✅ | ✅ | ❌ | ❌ |
| **Squared Hinge** | $$[1-yf]_+^2$$ | ✅ | ✅ | ⚠️ | ❌ |

**Tại sao Hinge Loss phù hợp với SVM?**

1. **Lồi**: Đảm bảo bài toán tối ưu có nghiệm duy nhất
2. **Margin-based**: Phạt cả điểm đúng nhưng gần margin (không như logistic chỉ quan tâm đúng/sai)
3. **Sparse**: Loss bằng 0 khi $$yf \geq 1$$ → Chỉ support vectors đóng góp
4. **Robust**: Phạt tuyến tính với outliers (không như exponential phạt quá nặng)

### 5A.4. Hinge Loss và Regularization

**Bài toán SVM với Hinge Loss:**

$$
\min_{\beta, \beta_0} \quad \underbrace{\frac{1}{2}\|\beta\|^2}_{\text{Regularization}} + C\sum_{i=1}^n \underbrace{[1 - y_i(\beta^T x_i + \beta_0)]_+}_{\text{Hinge Loss}}
$$

Đây là dạng **Regularized Empirical Risk Minimization**:

$$
\min_{\beta, \beta_0} \quad \underbrace{\frac{\lambda}{2}\|\beta\|^2}_{\text{Regularization}} + \underbrace{\frac{1}{n}\sum_{i=1}^n \ell(y_i, f(x_i))}_{\text{Empirical Risk}}
$$

với $$\lambda = \frac{1}{C \cdot n}$$.

**Hai vai trò:**

1. **$$\frac{1}{2}\|\beta\|^2$$**: 
   - Regularization term (Ridge regularization)
   - Prevent overfitting
   - Encourage large margin
   - Smooth solution

2. **$$\sum [1 - y_i f(x_i)]_+$$**:
   - Data fitting term
   - Minimize training error
   - Ensure correct classification

**Trade-off được điều khiển bởi $$C$$:**

$$
\begin{cases}
C \to 0: & \text{Ưu tiên regularization} \to \text{Large margin, simple model} \\
C \to \infty: & \text{Ưu tiên data fitting} \to \text{Small margin, fit data closely}
\end{cases}
$$

### 5A.5. Hinge Loss trong Deep Learning

Hinge loss không chỉ dùng cho SVM, nó còn xuất hiện trong:

**1) Multi-class Hinge Loss:**

$$
\ell_{\text{multiclass}}(y, f) = \sum_{j \neq y} [1 + f_j - f_y]_+
$$

- Dùng trong multi-class SVM
- $$f_j$$: score cho class $$j$$
- $$y$$: true class

**2) Triplet Loss (trong Metric Learning):**

$$
\ell_{\text{triplet}} = [\|f(a) - f(p)\|^2 - \|f(a) - f(n)\|^2 + \text{margin}]_+
$$

- $$a$$: anchor, $$p$$: positive, $$n$$: negative
- Dùng trong face recognition, siamese networks

**3) Ranking Loss:**

$$
\ell_{\text{rank}} = [1 - (f(x^+) - f(x^-))]_+
$$

- Dùng trong learning to rank, recommendation systems

### 5A.6. Subgradient và Optimization

**Vấn đề**: Hinge loss **không khả vi** tại $$yf = 1$$!

**Giải pháp**: Dùng **subgradient**

Tại điểm $$yf = 1$$, subgradient của $$[1 - yf]_+$$ là bất kỳ giá trị trong $$[-1, 0]$$.

**Subgradient của hinge loss:**

$$
\partial \ell_{\text{hinge}}(y, f) = \begin{cases}
\{0\} & \text{nếu } yf > 1 \\
[-1, 0] & \text{nếu } yf = 1 \\
\{-y\} & \text{nếu } yf < 1
\end{cases}
$$

**Gradient của bài toán SVM:**

$$
\nabla_\beta J(\beta) = \beta + C\sum_{i=1}^n \partial_\beta [1 - y_i(\beta^T x_i + \beta_0)]_+
$$

$$
= \beta - C\sum_{i: y_i f(x_i) < 1} y_i x_i
$$

Đây là cơ sở cho các thuật toán như **Subgradient Descent** và **Stochastic Gradient Descent** để train SVM.

### 5A.7. Kết nối với Soft-Margin SVM

**Ba formulation tương đương:**

**1) Constrained form (ban đầu):**
$$
\min \frac{1}{2}\|\beta\|^2 + C\sum \xi_i \quad \text{s.t. } y_i f(x_i) \geq 1 - \xi_i, \xi_i \geq 0
$$

**2) Unconstrained with Hinge Loss:**
$$
\min \frac{1}{2}\|\beta\|^2 + C\sum [1 - y_i f(x_i)]_+
$$

**3) Dual form:**
$$
\max \sum w_i - \frac{1}{2}\sum_{i,j} w_i w_j y_i y_j \langle x_i, x_j \rangle \quad \text{s.t. } 0 \leq w_i \leq C, \sum w_i y_i = 0
$$

Ba formulation này **hoàn toàn tương đương**, cho cùng một nghiệm tối ưu!

**Khi nào dùng formulation nào?**

| Formulation | Khi nào dùng | Solver | Ưu điểm |
|-------------|--------------|--------|---------|
| **Constrained** | Lý thuyết, phân tích KKT | QP solver | Dễ phân tích, rõ ràng về ràng buộc |
| **Hinge Loss** | Training với SGD | Subgradient descent | Nhanh, scalable, dễ implement |
| **Dual** | Kernel methods | SMO, LIBSVM | Kernel trick, sparse solution |

---

## 6. Bài toán Đối ngẫu (Dual Problem)

### 6.1. Tại sao cần Dual Problem? - Cánh cửa dẫn đến sức mạnh thực sự của SVM

Có vẻ như chúng ta đã có bài toán Soft-Margin SVM hoàn chỉnh ở dạng **primal** (gốc). Tại sao lại cần một "phiên bản đối ngẫu" (dual)?

Câu trả lời là: **Bài toán đối ngẫu mở ra những khả năng mà bài toán gốc không thể làm được!**

**Ba lý do then chốt khiến Dual Problem trở thành "ngôi sao" trong thực tế:**

1. **Kernel Trick - Phép màu của SVM**: 
   - Dual form chỉ phụ thuộc vào **tích vô hướng** $$\langle x_i, x_j \rangle$$ giữa các điểm dữ liệu
   - Ta có thể thay thế bằng **kernel function** $$K(x_i, x_j)$$ để ánh xạ ngầm lên không gian vô hạn chiều
   - Điều này cho phép SVM xử lý dữ liệu **phi tuyến phức tạp** mà không tăng độ phức tạp tính toán!

2. **Hiệu quả khi số chiều lớn**:
   - Primal: $$p + 1 + n$$ biến ($$p$$ có thể rất lớn, thậm chí vô hạn với kernel)
   - Dual: chỉ $$n$$ biến (số mẫu, thường nhỏ hơn nhiều)
   - Khi $$n \ll p$$ (ví dụ: phân loại văn bản, gene expression), dual nhanh hơn đáng kể

3. **Sparsity tự nhiên**:
   - Nghiệm dual có tính sparse: chỉ **support vectors** có $$w_i > 0$$
   - Phần lớn $$w_i = 0$$ → dự đoán nhanh, tiết kiệm bộ nhớ
   - Dễ hiểu: "Những điểm nào quyết định siêu phẳng?"

### 6.2. Xây dựng Dual Problem

**Bài toán Primal:**
$$
\begin{align}
\min_{\beta, \beta_0, \xi} \quad &\frac{1}{2}\|\beta\|^2 + C\sum_{i=1}^n \xi_i \\
\text{s.t.} \quad &y_i(\beta^T x_i + \beta_0) \geq 1 - \xi_i \\
&\xi_i \geq 0
\end{align}
$$

**Lagrangian:**
$$
L(\beta, \beta_0, \xi, w, v) = \frac{1}{2}\|\beta\|^2 + C\sum_{i=1}^n \xi_i - \sum_{i=1}^n w_i[y_i(\beta^T x_i + \beta_0) - 1 + \xi_i] - \sum_{i=1}^n v_i \xi_i
$$

trong đó $$w_i \geq 0, v_i \geq 0$$ là các Lagrange multipliers.

**Điều kiện KKT - Stationarity:**

Lấy đạo hàm theo các biến primal và cho bằng 0:

1. $$\frac{\partial L}{\partial \beta} = 0 \Rightarrow \beta = \sum_{i=1}^n w_i y_i x_i$$

2. $$\frac{\partial L}{\partial \beta_0} = 0 \Rightarrow \sum_{i=1}^n w_i y_i = 0$$

3. $$\frac{\partial L}{\partial \xi_i} = 0 \Rightarrow C - w_i - v_i = 0 \Rightarrow w_i \leq C$$

**Thế vào Lagrangian**, ta được **Dual Problem:**

$$
\begin{align}
\max_{w} \quad &\sum_{i=1}^n w_i - \frac{1}{2} \sum_{i,j=1}^n w_i w_j y_i y_j \langle x_i, x_j \rangle \\
\text{s.t.} \quad &\sum_{i=1}^n w_i y_i = 0 \\
&0 \leq w_i \leq C, \quad i = 1, \ldots, n
\end{align}
$$

**Hoặc dạng minimization:**
$$
\begin{align}
\min_{w} \quad &\frac{1}{2} \sum_{i,j=1}^n w_i w_j y_i y_j \langle x_i, x_j \rangle - \sum_{i=1}^n w_i \\
\text{s.t.} \quad &\sum_{i=1}^n w_i y_i = 0 \\
&0 \leq w_i \leq C, \quad i = 1, \ldots, n
\end{align}
$$

### 6.3. Ý nghĩa sâu sắc của Dual Variables - "Giá trị" của mỗi điểm dữ liệu

**Biến đối ngẫu $$w_i$$** (Lagrange multiplier) không chỉ là một con số trừu tượng - nó **"định giá"** tầm quan trọng của mỗi điểm dữ liệu trong việc quyết định siêu phẳng!

Hãy "đọc" ý nghĩa của $$w_i$$:

- **$$w_i = 0$$**: Điểm $$x_i$$ là **"người ngoài cuộc"**
  - Nằm xa margin, phân loại đúng và an toàn
  - **Không đóng góp gì** vào siêu phẳng: có thể xóa điểm này mà mô hình không đổi!
  - Chiếm đa số các điểm trong dataset

- **$$0 < w_i < C$$**: Điểm $$x_i$$ là **"support vector lý tưởng"**
  - Nằm **chính xác trên margin boundary** ($$\xi_i = 0$$)
  - Phân loại đúng, nhưng ở vị trí "nguy hiểm" nhất
  - Đây là những điểm **quan trọng nhất**, quyết định độ nghiêng và vị trí của siêu phẳng
  - Thường rất ít: chỉ 5-20% số điểm

- **$$w_i = C$$**: Điểm $$x_i$$ là **"support vector vấn đề"**
  - Vi phạm margin ($$\xi_i > 0$$): hoặc nằm trong margin, hoặc bị phân loại sai
  - "Đóng góp" vào siêu phẳng nhưng cũng **bị phạt** trong hàm mục tiêu
  - Thường là outliers, điểm nhiễu, hoặc điểm thuộc vùng chồng lấn giữa hai lớp

### 6.4. Tính $$\beta_0$$ từ nghiệm Dual

Sau khi giải dual problem và có $$w^\star$$, ta tính:

1. **$$\beta^\star$$** từ công thức: $$\beta^\star = \sum_{i=1}^n w_i^\star y_i x_i$$

2. **$$\beta_0^\star$$** từ support vector trên margin ($$0 < w_i^\star < C$$, $$\xi_i^\star = 0$$):
   $$
   \beta_0^\star = y_i - \beta^{\star T} x_i
   $$
   
   Trong thực tế, để robust hơn, ta lấy trung bình trên tất cả SV trên margin:
   $$
   \beta_0^\star = \frac{1}{|\mathcal{S}|} \sum_{i \in \mathcal{S}} (y_i - \beta^{\star T} x_i)
   $$
   với $$\mathcal{S} = \{i: 0 < w_i^\star < C\}$$

### 6.5. Ưu điểm của Dual Formulation

1. **Kernel trick**: Chỉ phụ thuộc vào $$\langle x_i, x_j \rangle$$ → có thể thay bằng $$K(x_i, x_j)$$
2. **Ít ràng buộc**: Chỉ 1 ràng buộc đẳng thức + box constraints
3. **Solver hiệu quả**: SMO (Sequential Minimal Optimization), LIBSVM
4. **Sparsity tự nhiên**: Chỉ support vectors có $$w_i > 0$$

---

## 7. Support Vectors: Những "trụ cột" của mô hình

Giờ đây chúng ta đến với **khái niệm trung tâm** mà SVM được đặt tên theo: **Support Vectors** (các vector hỗ trợ).

### Định nghĩa chính xác

**Support vectors** là tất cả các điểm dữ liệu có hệ số đối ngẫu khác không:
$$
\text{Support vectors} = \{x_i : w_i^\star > 0\}
$$

**Tại sao chúng quan trọng đến vậy?** Nhớ lại công thức từ điều kiện KKT stationarity:
$$
\beta^\star = \sum_{i: w_i^\star > 0} w_i^\star y_i x_i = \sum_{\text{support vectors}} w_i^\star y_i x_i
$$

**Phát hiện sửng sốt:** Siêu phẳng tối ưu **CHỈ phụ thuộc vào support vectors!**

- Tất cả điểm khác ($$w_i = 0$$) có thể bỏ đi mà mô hình không thay đổi
- Siêu phẳng "đứng trên vai" của một số ít điểm quan trọng
- Đây là lý do SVM có tính **sparse** tự nhiên

### Ba loại Support Vectors - Mỗi loại một vai trò

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

---

## 8. Kernel Methods: Từ tuyến tính đến phi tuyến

Cho đến giờ, chúng ta mới chỉ làm việc với **siêu phẳng tuyến tính** - một "đường thẳng" (hoặc mặt phẳng trong không gian nhiều chiều) để phân chia dữ liệu. Nhưng dữ liệu thực tế thường có **ranh giới phức tạp, phi tuyến**. Ví dụ: hai lớp dữ liệu phân bố theo hình tròn đồng tâm - không có đường thẳng nào tách được chúng!

Đây chính là lúc **Kernel Trick** - một trong những ý tưởng tinh tế và mạnh mẽ nhất trong machine learning - phát huy tác dụng.

### 8.0. Nhìn lại: Dual Problem và vai trò của tích vô hướng

Trước khi đi vào kernel, hãy nhìn lại **bài toán đối ngẫu** đã học ở Section 6:

$$
\min_{w} \frac{1}{2} \sum_{i,j=1}^n w_i w_j y_i y_j \underbrace{\langle x_i, x_j \rangle}_{\text{Tích vô hướng!}} - \sum_{i=1}^n w_i
$$

**Quan sát then chốt:** Bài toán dual **CHỈ phụ thuộc** vào tích vô hướng $$\langle x_i, x_j \rangle$$ giữa các cặp điểm dữ liệu, KHÔNG phụ thuộc trực tiếp vào $$x_i$$ hay $$x_j$$ riêng lẻ!

**Hệ quả quan trọng:** Nếu ta thay tích vô hướng $$\langle x_i, x_j \rangle$$ bằng một hàm khác $$K(x_i, x_j)$$, toàn bộ bài toán vẫn giải được, miễn là $$K$$ thỏa mãn một số điều kiện nhất định.

Đây chính là **cửa ngõ** dẫn đến kernel methods!

### 8.1. Linear Kernel: Điểm khởi đầu đơn giản nhất

Trước khi nghĩ đến những kernel phức tạp, hãy bắt đầu với trường hợp **đơn giản nhất**: chính tích vô hướng thông thường!

**Định nghĩa Linear Kernel:**

$$
K_{\text{linear}}(x, z) = \langle x, z \rangle = x^T z = \sum_{j=1}^d x_j z_j
$$

**Có vẻ quá đơn giản phải không?** Nhưng đây chính là ví dụ HOÀN HẢO để hiểu kernel!

**Tại sao Linear Kernel là một kernel?**

Câu hỏi: Có tồn tại ánh xạ $$\phi$$ sao cho $$K_{\text{linear}}(x, z) = \langle \phi(x), \phi(z) \rangle$$?

Câu trả lời: **CÓ!** Chọn ánh xạ đơn giản nhất:

$$
\phi(x) = x \quad \text{(ánh xạ đồng nhất - identity map)}
$$

Khi đó:

$$
K_{\text{linear}}(x, z) = \langle \phi(x), \phi(z) \rangle = \langle x, z \rangle = x^T z \quad \checkmark
$$

**Ý nghĩa:**

- Linear kernel = "KHÔNG ánh xạ gì cả", dữ liệu vẫn ở không gian gốc
- Siêu phẳng phân chia vẫn là **tuyến tính** trong không gian gốc
- Đây chính là SVM thông thường mà chúng ta đã học!

**Tại sao vẫn gọi nó là "kernel"?**

Vì nó thỏa mãn **điều kiện Mercer** (sẽ học sau):
- **Đối xứng**: $$K(x, z) = x^T z = z^T x = K(z, x)$$ ✓
- **Positive semi-definite**: Ma trận Gram $$\mathbf{K}_{ij} = x_i^T x_j$$ luôn PSD ✓

**Khi nào dùng Linear Kernel?**

1. **Baseline đầu tiên**: Luôn thử linear kernel trước!
2. **Dữ liệu chiều cao** ($$p \gg n$$): Như phân loại văn bản với hàng nghìn từ
3. **Dữ liệu đã tách được tuyến tính**: Không cần phi tuyến hóa
4. **Cần tốc độ**: Nhanh nhất, ít tham số nhất

**Ví dụ ứng dụng - Text Classification:**

Trong phân loại email spam/ham:
- Dữ liệu được biểu diễn bằng TF-IDF với 10,000 từ vựng → không gian 10,000 chiều
- Linear kernel thường hoạt động tốt vì dữ liệu văn bản thường tách được trong không gian TF-IDF
- Nhanh và hiệu quả, không cần phi tuyến hóa

**Bài toán dual với Linear Kernel:**

$$
\min_{w} \frac{1}{2} \sum_{i,j} w_i w_j y_i y_j \underbrace{K_{\text{linear}}(x_i, x_j)}_{= x_i^T x_j} - \sum_i w_i
$$

Giống hệt bài toán dual ban đầu! Linear kernel chỉ là "viết lại" tích vô hướng dưới dạng kernel.

**Kết luận quan trọng:**

> Linear kernel là **nền tảng** để hiểu các kernel khác. Nó cho thấy:
> 1. Kernel là một hàm $$K(x, z)$$ tính "độ giống nhau" giữa $$x$$ và $$z$$
> 2. Với linear kernel, "độ giống nhau" = tích vô hướng thông thường
> 3. Các kernel khác sẽ định nghĩa "độ giống nhau" theo cách khác, phức tạp hơn

Giờ chúng ta đã hiểu linear kernel, hãy xem điều gì xảy ra khi dữ liệu **không tách được tuyến tính**!

---

### 8.2. Động lực: Khi Linear Kernel không đủ

**Vấn đề cơ bản:** Nhiều bộ dữ liệu thực tế **không tách được tuyến tính** trong không gian gốc.

**Ví dụ kinh điển - Dữ liệu XOR:**

```
Class +1:  (+1, +1)  và  (-1, -1)  (hai góc chéo)
Class -1:  (+1, -1)  và  (-1, +1)  (hai góc chéo còn lại)
```

Không có đường thẳng nào có thể phân chia hai lớp này trong không gian 2D!

**Ý tưởng đột phá:** Nếu không tách được ở không gian hiện tại, hãy **ánh xạ lên không gian chiều cao hơn** - nơi dữ liệu có thể tách được!

### 8.3. Feature Mapping: Từ Linear đến Polynomial

**Bắt đầu với ví dụ đơn giản - Dữ liệu 1 chiều:**

Giả sử dữ liệu trên trục số:
```
Class +1: x = -2, x = +2  (hai đầu)
Class -1: x = 0           (ở giữa)
```

Không có điểm nào trên trục số (threshold) tách được hai class này!

**Giải pháp: Ánh xạ lên không gian 2 chiều**

Định nghĩa ánh xạ:
$$
\phi(x) = (x, x^2) \in \mathbb{R}^2
$$

Dữ liệu sau khi ánh xạ:
```
Class +1: φ(-2) = (-2, 4),  φ(+2) = (+2, 4)
Class -1: φ(0) = (0, 0)
```

Bây giờ trong không gian 2D $$(x, x^2)$$, ta có thể dùng đường thẳng $$x^2 = 2$$ để tách hai class!

**Kernel tương ứng:**

Với ánh xạ $$\phi(x) = (x, x^2)$$, kernel là:

$$
\begin{align}
K(x, z) &= \langle \phi(x), \phi(z) \rangle \\
&= \langle (x, x^2), (z, z^2) \rangle \\
&= xz + x^2z^2
\end{align}
$$

**Mở rộng: Polynomial Kernel tổng quát**

### 8.4. Feature Mapping tổng quát: Ánh xạ lên không gian mới

**Định nghĩa:** Ánh xạ đặc trưng (feature map) là một hàm $$\phi$$ biến đổi dữ liệu từ không gian gốc sang không gian mới:

$$
\phi: \mathbb{R}^d \to \mathcal{H}
$$

trong đó $$\mathcal{H}$$ là **không gian đặc trưng** (feature space), thường có số chiều cao hơn (thậm chí vô hạn!).

**Ví dụ cụ thể - Ánh xạ bậc 2 cho $$\mathbb{R}^2$$:**

Với $$x = (x_1, x_2) \in \mathbb{R}^2$$, định nghĩa:

$$
\phi(x) = (x_1^2, \sqrt{2}x_1x_2, x_2^2, \sqrt{2}x_1, \sqrt{2}x_2, 1) \in \mathbb{R}^6
$$

Bây giờ $$x$$ được biểu diễn bằng **6 chiều** thay vì 2 chiều! Trong không gian mới này, nhiều dữ liệu phi tuyến trở nên tách được tuyến tính.

**Bài toán SVM trong không gian mới:**

Thay vì giải:
$$
\min_{w} \frac{1}{2} \sum_{i,j} w_i w_j y_i y_j \langle x_i, x_j \rangle - \sum_i w_i
$$

Ta giải trong không gian đặc trưng:
$$
\min_{w} \frac{1}{2} \sum_{i,j} w_i w_j y_i y_j \langle \phi(x_i), \phi(x_j) \rangle - \sum_i w_i
$$

**Vấn đề lớn:** Nếu $$\phi(x)$$ có số chiều rất cao (ví dụ: 1000 chiều), việc tính toán $$\langle \phi(x_i), \phi(x_j) \rangle$$ sẽ **cực kỳ tốn kém**!

### 8.5. Kernel Trick: Phép màu không cần ánh xạ tường minh

Đây là **bước đột phá** biến kernel methods từ ý tưởng đẹp thành công cụ thực tiễn!

**Ý tưởng thiên tài:** Thay vì tính $$\phi(x)$$ rồi tính tích vô hướng, ta tìm một **hàm kernel** $$K$$ sao cho:

$$
K(x_i, x_j) = \langle \phi(x_i), \phi(x_j) \rangle
$$

mà **KHÔNG cần tính $$\phi(x)$$ tường minh**!

**Tại sao đây là phép màu?**

- Tính $$K(x_i, x_j)$$ trực tiếp trong không gian gốc: **$$O(d)$$ - rất nhanh!**
- Tránh tính $$\phi(x_i)$$ và $$\phi(x_j)$$ trong không gian chiều cao: tiết kiệm tài nguyên khổng lồ
- Thậm chí ánh xạ lên **không gian vô hạn chiều** mà vẫn tính toán được!

**Ví dụ minh họa - Polynomial Kernel bậc 2:**

Với ánh xạ $$\phi(x) = (x_1^2, \sqrt{2}x_1x_2, x_2^2, \sqrt{2}x_1, \sqrt{2}x_2, 1)$$, ta có:

$$
\begin{align}
\langle \phi(x), \phi(z) \rangle &= x_1^2 z_1^2 + 2x_1x_2z_1z_2 + x_2^2z_2^2 + 2x_1z_1 + 2x_2z_2 + 1 \\
&= (x_1z_1 + x_2z_2)^2 + 2(x_1z_1 + x_2z_2) + 1 \\
&= (\langle x, z \rangle + 1)^2
\end{align}
$$

Vậy thay vì tính 6 phép nhân trong $$\mathbb{R}^6$$, ta chỉ cần:

$$
K(x, z) = (\langle x, z \rangle + 1)^2
$$

**2 phép tính trong $$\mathbb{R}^2$$** - Nhanh gấp nhiều lần!

**So sánh chi phí tính toán:**

| Phương pháp | Các bước | Độ phức tạp |
|-------------|----------|-------------|
| **Cách 1: Tính tường minh** | 1. Tính $$\phi(x)$$ (6 chiều)<br>2. Tính $$\phi(z)$$ (6 chiều)<br>3. Tính tích vô hướng (6 phép nhân) | $$O(6 + 6 + 6) = O(18)$$ |
| **Cách 2: Kernel trick** | 1. Tính $$\langle x, z \rangle$$ (2 phép nhân)<br>2. Tính $$(\cdot + 1)^2$$ (1 phép cộng, 1 phép mũ) | $$O(2 + 2) = O(4)$$ |

Nhanh hơn **4.5 lần**! Và đây chỉ với ánh xạ bậc 2 trong $$\mathbb{R}^2$$. Với dữ liệu chiều cao và bậc lớn hơn, lợi ích còn lớn hơn rất nhiều!

**Ví dụ thực tế với dữ liệu chiều cao:**

Với polynomial kernel bậc 3 trong không gian 100 chiều:
- **Số chiều sau ánh xạ tường minh**: $$C(100+3, 3) \approx 176,851$$ chiều!
- **Chi phí tính toán tường minh**: Phải tính và lưu trữ vector 176,851 chiều
- **Chi phí với kernel trick**: Chỉ cần tính $$(\langle x, z \rangle + 1)^3$$ - vài phép toán đơn giản
- **Kết quả**: Kernel trick nhanh hơn **hàng trăm lần**!

**Kết luận về Kernel Trick:**

1. **Tiết kiệm tính toán khổng lồ**: Không cần tính $$\phi(x)$$ tường minh
2. **Cho phép không gian vô hạn chiều**: RBF kernel ánh xạ lên $$\mathbb{R}^\infty$$ nhưng vẫn tính được!
3. **Elegant và powerful**: Đơn giản nhưng mạnh mẽ

> **Kernel trick** là lý do SVM có thể xử lý dữ liệu phi tuyến phức tạp mà vẫn hiệu quả về mặt tính toán!

### 8.6. Các Kernel phổ biến và ứng dụng

Giờ chúng ta đã hiểu kernel trick, hãy xem các kernel phổ biến nhất trong thực tế:

**1) Linear Kernel (Kernel tuyến tính):**

$$
K(x, z) = \langle x, z \rangle = x^T z
$$

- **Khi nào dùng:** Dữ liệu đã tách được tuyến tính, hoặc số chiều rất cao ($$p \gg n$$)
- **Ưu điểm:** Nhanh nhất, ít tham số, tránh overfitting
- **Ví dụ:** Phân loại văn bản (bag-of-words với hàng nghìn từ vựng)

**2) Polynomial Kernel (Kernel đa thức):**

$$
K(x, z) = (\langle x, z \rangle + c)^q
$$

với $$q$$ là bậc đa thức, $$c \geq 0$$ là hằng số.

- **Khi nào dùng:** Ranh giới quyết định là đa thức bậc thấp ($$q = 2, 3$$)
- **Ưu điểm:** Linh hoạt, mô hình hóa tương tác giữa các features
- **Nhược điểm:** Khó tune tham số $$q$$ và $$c$$, dễ overfitting với $$q$$ lớn
- **Ví dụ:** Nhận dạng chữ viết tay, xử lý ảnh

**3) RBF (Radial Basis Function) Kernel - Kernel Gauss:**

$$
K(x, z) = \exp\left(-\frac{\|x - z\|^2}{2\sigma^2}\right) = \exp(-\gamma \|x - z\|^2)
$$

với $$\gamma = \frac{1}{2\sigma^2} > 0$$ là tham số bandwidth.

- **Khi nào dùng:** **Default choice** cho hầu hết bài toán - rất linh hoạt!
- **Ưu điểm:** 
  - Ánh xạ lên **không gian vô hạn chiều**
  - Có thể xấp xỉ mọi hàm liên tục (universal approximator)
  - Chỉ có 1 tham số $$\gamma$$ cần tune
- **Nhược điểm:** Dễ overfit nếu $$\gamma$$ quá lớn
- **Ví dụ:** Nhận dạng khuôn mặt, phân loại gene expression

**4) Sigmoid Kernel:**

$$
K(x, z) = \tanh(\alpha \langle x, z \rangle + c)
$$

- **Khi nào dùng:** Mô phỏng neural network với một hidden layer
- **Lưu ý:** Không phải lúc nào cũng positive definite (không đảm bảo hội tụ)
- **Ví dụ:** Một số bài toán nhị phân đơn giản

**Tổng kết so sánh 4 kernel:**

| Kernel | Linear | Polynomial | RBF | Sigmoid |
|--------|--------|------------|-----|---------|
| **Công thức** | $$x^Tz$$ | $$(\langle x,z\rangle + c)^q$$ | $$\exp(-\gamma\\|x-z\\|^2)$$ | $$\tanh(\alpha\langle x,z\rangle+c)$$ |
| **Tham số** | 0 | 2 ($$q, c$$) | 1 ($$\gamma$$) | 2 ($$\alpha, c$$) |
| **Không gian** | $$\mathbb{R}^d$$ | $$\mathbb{R}^{C(d+q,q)}$$ | $$\mathbb{R}^\infty$$ | - |
| **Dễ tune** | ✅ Rất dễ | ⚠️ Khó | ✅ Dễ | ❌ Rất khó |
| **Tốc độ** | ⚡ Nhanh nhất | ⚡ Nhanh | 🐌 Trung bình | 🐌 Trung bình |
| **Khi nào dùng** | Baseline | Tương tác bậc thấp | **Default** | Hiếm khi |

### 8.7. Điều kiện hợp lệ của Kernel - Mercer's Theorem

**Câu hỏi quan trọng:** Không phải hàm nào cũng có thể làm kernel! Điều kiện nào đảm bảo $$K$$ là một kernel hợp lệ?

**Định lý Mercer (Mercer's Theorem):**

Một hàm $$K: \mathcal{X} \times \mathcal{X} \to \mathbb{R}$$ là một kernel hợp lệ (valid kernel) nếu và chỉ nếu nó là **symmetric positive semi-definite**, tức là:

1. **Đối xứng:** $$K(x, z) = K(z, x), \quad \forall x, z$$

2. **Positive semi-definite:** Với mọi $$n$$ điểm $$\{x_1, \ldots, x_n\}$$ và mọi $$a_1, \ldots, a_n \in \mathbb{R}$$:
   $$
   \sum_{i=1}^n \sum_{j=1}^n a_i a_j K(x_i, x_j) \geq 0
   $$
   
   Hay tương đương: Ma trận Gram $$\mathbf{K}$$ với $$K_{ij} = K(x_i, x_j)$$ là **positive semi-definite**.

**Ý nghĩa thực tiễn:**

- Nếu $$K$$ thỏa điều kiện Mercer → Tồn tại $$\phi$$ sao cho $$K(x, z) = \langle \phi(x), \phi(z) \rangle$$
- Bài toán tối ưu SVM là **convex** và có nghiệm duy nhất
- Nếu $$K$$ vi phạm điều kiện → Bài toán có thể không hội tụ!

**Kiểm tra trong thực tế:**

- Các kernel chuẩn (linear, polynomial, RBF) đều thỏa Mercer
- Nếu tự định nghĩa kernel mới, cần kiểm tra tính positive definite của ma trận $$\mathbf{K}$$

### 8.8. Xây dựng Kernel mới từ Kernel cũ

**Tính chất đóng (Closure properties):** Nếu $$K_1$$ và $$K_2$$ là kernel hợp lệ, thì các phép toán sau cũng cho kernel hợp lệ:

1. **Tổng:** $$K(x, z) = K_1(x, z) + K_2(x, z)$$

2. **Nhân với hằng số dương:** $$K(x, z) = c \cdot K_1(x, z), \quad c > 0$$

3. **Tích:** $$K(x, z) = K_1(x, z) \cdot K_2(x, z)$$

4. **Hàm của kernel:** $$K(x, z) = f(K_1(x, z))$$ với $$f$$ là hàm positive-preserving

5. **Tensor product:** $$K(x, z) = K_1(x_1, z_1) \cdot K_2(x_2, z_2)$$ với $$x = (x_1, x_2)$$

**Ví dụ ứng dụng:**

Kết hợp RBF với Linear để có cả tính tuyến tính và phi tuyến:

$$
K(x, z) = \underbrace{\alpha \langle x, z \rangle}_{\text{Linear}} + \underbrace{\beta \exp(-\gamma \|x - z\|^2)}_{\text{RBF}}, \quad \alpha, \beta > 0
$$

### 8.9. Kernel SVM trong thực tế

**Công thức dự đoán với Kernel:**

Sau khi huấn luyện, dự đoán cho điểm mới $$x$$:

$$
f(x) = \text{sign}\left(\sum_{i \in SV} w_i^\star y_i K(x, x_i) + \beta_0^\star\right)
$$

**Lưu ý quan trọng:**

- Chỉ cần tính $$K(x, x_i)$$ với **support vectors** (rất ít so với toàn bộ dữ liệu)
- Không cần biết $$\phi(x)$$ là gì - chỉ cần $$K$$!
- Tốc độ dự đoán: $$O(\#SV \cdot d)$$ với $$d$$ là chiều dữ liệu gốc

**Lựa chọn kernel trong thực tế:**

| Tình huống | Kernel đề xuất | Lý do |
|------------|----------------|-------|
| **Baseline / không biết gì** | Linear | Nhanh, ít overfit, baseline tốt |
| **Dữ liệu phi tuyến** | RBF | Linh hoạt, universal approximator |
| **Số chiều cao ($$p \gg n$$)** | Linear | Tránh overfit trong không gian chiều cao |
| **Feature engineering sẵn** | Linear | Đã có features tốt rồi |
| **Tương tác bậc thấp** | Polynomial ($$q=2,3$$) | Model hóa tương tác rõ ràng |
| **Computational budget thấp** | Linear | Nhanh nhất |

**Quy trình thực hành:**

1. **Bắt đầu với Linear SVM**: Baseline nhanh
2. **Thử RBF SVM**: Nếu Linear không tốt
3. **Grid search cho $$C$$ và $$\gamma$$**: Tune hyperparameters
4. **Cross-validation**: Đánh giá độ tổng quát

### 8.10. Minh họa tương tác: So sánh các Kernel

<div id="kernel-demo" style="margin: 20px 0;">
    <canvas id="kernelCanvas" width="800" height="500" style="border: 1px solid #ccc; display: block; margin: 0 auto;"></canvas>
    <div style="text-align: center; margin-top: 15px;">
        <label for="kernelSelect" style="font-size: 16px; font-weight: bold; margin-right: 10px;">Chọn Kernel:</label>
        <select id="kernelSelect" style="padding: 8px; font-size: 14px; border-radius: 5px; border: 1px solid #ccc;">
            <option value="linear">Linear Kernel</option>
            <option value="poly2">Polynomial (degree 2)</option>
            <option value="poly3">Polynomial (degree 3)</option>
            <option value="rbf" selected>RBF/Gaussian</option>
        </select>
        <div style="margin-top: 15px;" id="rbfGammaControl">
            <label for="gammaSlider" style="font-size: 14px;">Gamma (RBF): <span id="gammaValue">0.5</span></label><br>
            <input type="range" id="gammaSlider" min="0.1" max="5" step="0.1" value="0.5" style="width: 300px; margin-top: 5px;">
        </div>
        <p style="font-size: 14px; color: #666; margin-top: 10px;">
            Dữ liệu phi tuyến (XOR-like pattern). Quan sát ranh giới quyết định với từng kernel.
        </p>
    </div>
</div>

<script>
(function() {
    const canvas = document.getElementById('kernelCanvas');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    
    // Dữ liệu XOR-like pattern
    const points = [
        // Class +1 (đỏ) - hai góc đối diện
        {x: 200, y: 150, label: 1}, {x: 220, y: 130, label: 1}, {x: 180, y: 170, label: 1},
        {x: 600, y: 350, label: 1}, {x: 620, y: 330, label: 1}, {x: 580, y: 370, label: 1},
        {x: 210, y: 160, label: 1}, {x: 590, y: 340, label: 1},
        
        // Class -1 (xanh) - hai góc đối diện còn lại
        {x: 600, y: 150, label: -1}, {x: 620, y: 130, label: -1}, {x: 580, y: 170, label: -1},
        {x: 200, y: 350, label: -1}, {x: 220, y: 330, label: -1}, {x: 180, y: 370, label: -1},
        {x: 610, y: 160, label: -1}, {x: 190, y: 340, label: -1}
    ];
    
    let currentKernel = 'rbf';
    let gamma = 0.5;
    
    // Kernel functions
    function kernel(x1, x2, type) {
        const dx = x1.x - x2.x;
        const dy = x1.y - x2.y;
        const dot = x1.x * x2.x + x1.y * x2.y;
        
        switch(type) {
            case 'linear':
                return dot;
            case 'poly2':
                return Math.pow(dot / 10000 + 1, 2);
            case 'poly3':
                return Math.pow(dot / 10000 + 1, 3);
            case 'rbf':
                return Math.exp(-gamma * (dx*dx + dy*dy) / 10000);
            default:
                return dot;
        }
    }
    
    // Simplified prediction
    function predict(testPoint) {
        let sum = 0;
        points.forEach(p => {
            const k = kernel(testPoint, p, currentKernel);
            sum += p.label * k;
        });
        return sum;
    }
    
    function draw() {
        ctx.clearRect(0, 0, width, height);
        
        // Vẽ background với decision boundary
        const gridSize = 5;
        for (let x = 0; x < width; x += gridSize) {
            for (let y = 0; y < height; y += gridSize) {
                const pred = predict({x, y});
                const alpha = Math.min(Math.abs(pred) * 0.02, 0.3);
                ctx.fillStyle = pred > 0 ? `rgba(231, 76, 60, ${alpha})` : `rgba(46, 204, 113, ${alpha})`;
                ctx.fillRect(x, y, gridSize, gridSize);
            }
        }
        
        // Vẽ decision boundary (đường contour pred = 0)
        ctx.strokeStyle = '#2c3e50';
        ctx.lineWidth = 3;
        ctx.beginPath();
        let firstPoint = true;
        
        for (let y = 50; y < height - 50; y += 2) {
            for (let x = 50; x < width - 50; x += 2) {
                const pred = predict({x, y});
                const predRight = predict({x: x+2, y});
                const predDown = predict({x, y: y+2});
                
                // Tìm zero crossing
                if (Math.sign(pred) !== Math.sign(predRight) || Math.sign(pred) !== Math.sign(predDown)) {
                    if (firstPoint) {
                        ctx.moveTo(x, y);
                        firstPoint = false;
                    } else {
                        ctx.lineTo(x, y);
                    }
                }
            }
        }
        ctx.stroke();
        
        // Vẽ data points
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
        ctx.font = 'bold 16px Arial';
        ctx.fillText(`Kernel: ${currentKernel.toUpperCase()}`, 20, 30);
        
        if (currentKernel === 'rbf') {
            ctx.fillText(`γ = ${gamma.toFixed(2)}`, 20, 55);
        }
    }
    
    // Event listeners
    const kernelSelect = document.getElementById('kernelSelect');
    const gammaSlider = document.getElementById('gammaSlider');
    const gammaValue = document.getElementById('gammaValue');
    const gammaControl = document.getElementById('rbfGammaControl');
    
    if (kernelSelect) {
        kernelSelect.addEventListener('change', function() {
            currentKernel = this.value;
            gammaControl.style.display = currentKernel === 'rbf' ? 'block' : 'none';
            draw();
        });
    }
    
    if (gammaSlider && gammaValue) {
        gammaSlider.addEventListener('input', function() {
            gamma = parseFloat(this.value);
            gammaValue.textContent = gamma.toFixed(2);
            draw();
        });
    }
    
    // Initial draw
    draw();
})();
</script>

### 8.11. Ưu và nhược điểm của Kernel Methods

**✅ Ưu điểm vượt trội:**

1. **Không gian vô hạn chiều**: RBF kernel ánh xạ lên không gian vô hạn chiều mà vẫn tính toán nhanh
2. **Không cần feature engineering**: Kernel tự động tạo features phi tuyến
3. **Lý thuyết vững chắc**: Mercer's theorem đảm bảo tính chất toán học
4. **Linh hoạt**: Có thể thiết kế kernel riêng cho từng domain (string kernel, graph kernel, ...)
5. **Hiệu quả với dữ liệu nhỏ/trung bình**: SVM+kernel hoạt động tốt với $$n < 10^5$$

**❌ Nhược điểm cần lưu ý:**

1. **Khó tune hyperparameters**: $$C$$, $$\gamma$$, ... cần grid search tốn thời gian
2. **Training chậm với dữ liệu lớn**: Độ phức tạp $$O(n^2)$$ đến $$O(n^3)$$ cho $$n$$ lớn
3. **Lưu trữ support vectors**: Cần lưu tất cả SV để dự đoán (có thể nhiều với dữ liệu phức tạp)
4. **Black box**: Khó interpret hơn linear model
5. **Không có probability estimate tự nhiên**: Cần Platt scaling để có xác suất

**So sánh với Neural Networks:**

| Tiêu chí | Kernel SVM | Neural Networks |
|----------|------------|-----------------|
| **Dữ liệu nhỏ ($$n < 10^4$$)** | ✅ Tốt hơn | Có thể overfit |
| **Dữ liệu lớn ($$n > 10^6$$)** | ❌ Chậm | ✅ Tốt hơn |
| **Interpretability** | Trung bình (SV) | ❌ Khó |
| **Hyperparameter tuning** | ❌ Khó | ❌ Rất khó |
| **Training time** | $$O(n^2)$$-$$O(n^3)$$ | Phụ thuộc kiến trúc |
| **Lý thuyết** | ✅ Vững chắc | Đang phát triển |

---

## 9. Ví dụ Chi tiết

### Ví dụ 1D: Dữ liệu đơn giản

**Dữ liệu:**
- Lớp $$+1$$: $$x_1 = 3, x_2 = 4$$
- Lớp $$-1$$: $$x_3 = 1, x_4 = 2$$

<div id="svm1d-demo" style="margin: 20px 0;">
    <canvas id="svm1dCanvas" width="700" height="300" style="border: 1px solid #ccc; display: block; margin: 0 auto;"></canvas>
    <div style="text-align: center; margin-top: 15px;">
        <div style="background: #f8f9fa; padding: 15px; border-radius: 8px; display: inline-block;">
            <p style="margin: 5px; font-size: 14px;"><strong>Nghiệm tối ưu:</strong></p>
            <p style="margin: 5px; font-size: 14px;">Siêu phẳng: $$x = 2.5$$</p>
            <p style="margin: 5px; font-size: 14px;">$$\beta = 2, \quad \beta_0 = -5$$</p>
            <p style="margin: 5px; font-size: 14px;">Margin width: $$\frac{2}{\lvert\beta\rvert} = 1$$</p>
            <p style="margin: 5px; font-size: 14px; color: #f39c12;"><strong>Support Vectors:</strong> $$x = 2$$ và $$x = 3$$</p>
        </div>
    </div>
</div>

<script>
(function() {
    const canvas = document.getElementById('svm1dCanvas');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    
    // Dữ liệu
    const points = [
        {x: 3, label: 1, name: 'x₁'},
        {x: 4, label: 1, name: 'x₂'},
        {x: 1, label: -1, name: 'x₃'},
        {x: 2, label: -1, name: 'x₄'}
    ];
    
    // Nghiệm: β = 2, β₀ = -5
    // Hyperplane: 2x - 5 = 0 => x = 2.5
    const hyperplane = 2.5;
    const margin = 0.5; // margin = 1/β = 1/2
    
    // Scaling cho visualization
    const scale = 100;
    const offsetX = 150;
    const centerY = height / 2;
    
    function xToScreen(x) {
        return offsetX + x * scale;
    }
    
    function draw() {
        // Clear
        ctx.clearRect(0, 0, width, height);
        
        // Background
        ctx.fillStyle = '#fafafa';
        ctx.fillRect(0, 0, width, height);
        
        // Vẽ trục x
        ctx.strokeStyle = '#34495e';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(50, centerY);
        ctx.lineTo(width - 50, centerY);
        ctx.stroke();
        
        // Vẽ mũi tên trục x
        ctx.beginPath();
        ctx.moveTo(width - 50, centerY);
        ctx.lineTo(width - 60, centerY - 5);
        ctx.lineTo(width - 60, centerY + 5);
        ctx.closePath();
        ctx.fillStyle = '#34495e';
        ctx.fill();
        
        // Vẽ các điểm trên trục
        for (let i = 0; i <= 5; i++) {
            const x = xToScreen(i);
            ctx.strokeStyle = '#95a5a6';
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(x, centerY - 5);
            ctx.lineTo(x, centerY + 5);
            ctx.stroke();
            
            ctx.fillStyle = '#7f8c8d';
            ctx.font = '12px Arial';
            ctx.textAlign = 'center';
            ctx.fillText(i.toString(), x, centerY + 20);
        }
        
        // Vẽ margin boundaries (đường đứt nét)
        ctx.strokeStyle = '#95a5a6';
        ctx.lineWidth = 2;
        ctx.setLineDash([5, 5]);
        
        // Left margin boundary (x = 2)
        const leftMargin = xToScreen(hyperplane - margin);
        ctx.beginPath();
        ctx.moveTo(leftMargin, 50);
        ctx.lineTo(leftMargin, height - 50);
        ctx.stroke();
        
        // Right margin boundary (x = 3)
        const rightMargin = xToScreen(hyperplane + margin);
        ctx.beginPath();
        ctx.moveTo(rightMargin, 50);
        ctx.lineTo(rightMargin, height - 50);
        ctx.stroke();
        
        ctx.setLineDash([]);
        
        // Vẽ margin zone (vùng màu nhạt)
        ctx.fillStyle = 'rgba(52, 152, 219, 0.1)';
        ctx.fillRect(leftMargin, 50, rightMargin - leftMargin, height - 100);
        
        // Vẽ hyperplane (đường đậm)
        const hyperX = xToScreen(hyperplane);
        ctx.strokeStyle = '#2c3e50';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(hyperX, 50);
        ctx.lineTo(hyperX, height - 50);
        ctx.stroke();
        
        // Label cho hyperplane
        ctx.fillStyle = '#2c3e50';
        ctx.font = 'bold 14px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('x = 2.5', hyperX, 40);
        ctx.font = '12px Arial';
        ctx.fillText('Siêu phẳng', hyperX, 25);
        
        // Labels cho margins
        ctx.fillStyle = '#7f8c8d';
        ctx.font = '12px Arial';
        ctx.fillText('x = 2', leftMargin, height - 35);
        ctx.fillText('x = 3', rightMargin, height - 35);
        
        // Vẽ data points
        points.forEach(p => {
            const x = xToScreen(p.x);
            
            // Điểm
            ctx.fillStyle = p.label === 1 ? '#e74c3c' : '#2ecc71';
            ctx.beginPath();
            ctx.arc(x, centerY, 12, 0, 2 * Math.PI);
            ctx.fill();
            
            // Viền
            ctx.strokeStyle = '#34495e';
            ctx.lineWidth = 2;
            ctx.stroke();
            
            // Highlight support vectors
            if (p.x === 2 || p.x === 3) {
                ctx.strokeStyle = '#f39c12';
                ctx.lineWidth = 4;
                ctx.beginPath();
                ctx.arc(x, centerY, 18, 0, 2 * Math.PI);
                ctx.stroke();
            }
            
            // Label điểm
            ctx.fillStyle = '#34495e';
            ctx.font = 'bold 14px Arial';
            ctx.textAlign = 'center';
            ctx.fillText(p.name, x, centerY - 30);
            
            // Hiển thị class
            ctx.font = '12px Arial';
            const classLabel = p.label === 1 ? 'y = +1' : 'y = -1';
            ctx.fillStyle = p.label === 1 ? '#e74c3c' : '#2ecc71';
            ctx.fillText(classLabel, x, centerY + 40);
        });
        
        // Vẽ khoảng cách margin (mũi tên hai chiều)
        const arrowY = 80;
        ctx.strokeStyle = '#3498db';
        ctx.lineWidth = 2;
        
        // Đường kẻ
        ctx.beginPath();
        ctx.moveTo(leftMargin, arrowY);
        ctx.lineTo(hyperX, arrowY);
        ctx.stroke();
        
        ctx.beginPath();
        ctx.moveTo(hyperX, arrowY);
        ctx.lineTo(rightMargin, arrowY);
        ctx.stroke();
        
        // Mũi tên trái
        ctx.beginPath();
        ctx.moveTo(leftMargin + 5, arrowY - 5);
        ctx.lineTo(leftMargin, arrowY);
        ctx.lineTo(leftMargin + 5, arrowY + 5);
        ctx.stroke();
        
        // Mũi tên phải
        ctx.beginPath();
        ctx.moveTo(rightMargin - 5, arrowY - 5);
        ctx.lineTo(rightMargin, arrowY);
        ctx.lineTo(rightMargin - 5, arrowY + 5);
        ctx.stroke();
        
        // Label margin
        ctx.fillStyle = '#3498db';
        ctx.font = 'bold 12px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('margin = 0.5', (leftMargin + hyperX) / 2, arrowY - 10);
        ctx.fillText('margin = 0.5', (hyperX + rightMargin) / 2, arrowY - 10);
        
        // Legend
        const legendX = width - 180;
        const legendY = 100;
        
        // Class +1
        ctx.fillStyle = '#e74c3c';
        ctx.beginPath();
        ctx.arc(legendX, legendY, 8, 0, 2 * Math.PI);
        ctx.fill();
        ctx.strokeStyle = '#34495e';
        ctx.lineWidth = 2;
        ctx.stroke();
        ctx.fillStyle = '#34495e';
        ctx.font = '12px Arial';
        ctx.textAlign = 'left';
        ctx.fillText('Class +1', legendX + 15, legendY + 4);
        
        // Class -1
        ctx.fillStyle = '#2ecc71';
        ctx.beginPath();
        ctx.arc(legendX, legendY + 25, 8, 0, 2 * Math.PI);
        ctx.fill();
        ctx.strokeStyle = '#34495e';
        ctx.lineWidth = 2;
        ctx.stroke();
        ctx.fillStyle = '#34495e';
        ctx.fillText('Class -1', legendX + 15, legendY + 29);
        
        // Support Vector
        ctx.strokeStyle = '#f39c12';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.arc(legendX, legendY + 50, 8, 0, 2 * Math.PI);
        ctx.stroke();
        ctx.fillStyle = '#34495e';
        ctx.fillText('Support Vector', legendX + 15, legendY + 54);
    }
    
    // Initial draw
    draw();
})();
</script>

**Bài toán hard-margin:**
$$
\begin{align}
\min_{\beta, \beta_0} \quad &\frac{1}{2}\beta^2 \\
\text{s.t.} \quad &3\beta + \beta_0 \geq 1, \quad 4\beta + \beta_0 \geq 1 \\
&-\beta - \beta_0 \geq 1, \quad -2\beta - \beta_0 \geq 1
\end{align}
$$

**Phân tích nghiệm:**

Support vectors là các điểm gần nhất với siêu phẳng: $$x = 3$$ (lớp +1) và $$x = 2$$ (lớp -1).

**Điều kiện margin chặt:**
$$
\begin{cases}
3\beta + \beta_0 = 1 \\
2\beta + \beta_0 = -1
\end{cases}
\Rightarrow \beta = 2, \quad \beta_0 = -5
$$

**Kết quả:**
- Siêu phẳng: $$2x - 5 = 0$$ hay $$x = 2.5$$ ✓
- Margin width: $$\frac{2}{\lvert\beta\rvert} = \frac{2}{2} = 1$$
- Support vectors: $$x = 2$$ và $$x = 3$$
- Các điểm $$x = 1$$ và $$x = 4$$ không phải support vectors vì chúng nằm xa margin hơn

---

## 9. Bài tập Thực hành

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

## 10. Tóm tắt: Nhìn lại hành trình chinh phục SVM

### 10.1. Từ trực giác hình học đến toán học chặt chẽ

Chúng ta vừa hoàn thành một hành trình đầy thú vị, đi từ **câu hỏi tự nhiên** đến **công cụ toán học mạnh mẽ**:

**🔹 Xuất phát điểm (Trực giác):** 
"Trong vô số đường phân chia, đường nào là *tốt nhất*?" → Câu hỏi đơn giản nhưng sâu sắc

**🔹 Bước 1 (Định lượng):** 
Margin = "vùng an toàn" xung quanh đường phân chia → Công cụ đo lường chất lượng khách quan

**🔹 Bước 2 (Toán học hóa):** 
Maximize margin ⇔ Quadratic Programming → Bài toán tối ưu lồi, nghiệm duy nhất, giải được hiệu quả

**🔹 Bước 3 (Đối mặt thực tế):** 
Hard-Margin → Soft-Margin với slack variables → Xử lý nhiễu, outliers, dữ liệu không tách được

**🔹 Bước 3A (Góc nhìn Loss Function):**
Constrained optimization → Hinge Loss → Kết nối với machine learning, subgradient descent

**🔹 Bước 4 (Mở rộng sức mạnh):** 
Primal → Dual Problem → Cánh cửa đến kernel trick và không gian vô hạn chiều

**🔹 Bước 5 (Phi tuyến hóa):**
Linear boundary → Kernel Methods → Xử lý ranh giới quyết định phức tạp, phi tuyến

**🔹 Đích đến:** 
Một framework hoàn chỉnh, vừa có nền tảng lý thuyết vững chắc, vừa mạnh mẽ trong thực tiễn, từ tuyến tính đến phi tuyến, từ optimization đến machine learning

### 10.2. Các khái niệm then chốt

| Khái niệm | Công thức | Ý nghĩa |
|-----------|-----------|---------|
| **Margin** | $$\frac{2}{\|\beta\|}$$ | Khoảng cách giữa 2 margin boundaries |
| **Hard-Margin** | $$y_i(\beta^T x_i + \beta_0) \geq 1$$ | Tất cả điểm phải phân loại đúng |
| **Soft-Margin** | $$y_i(\beta^T x_i + \beta_0) \geq 1 - \xi_i$$ | Cho phép vi phạm có kiểm soát |
| **Support Vectors** | $$w_i > 0$$ | Các điểm quyết định siêu phẳng |
| **Tham số C** | $$C \sum \xi_i$$ | Trọng số phạt vi phạm margin |
| **Hinge Loss** | $$[1 - yf]_+ = \max\\{0, 1-yf\\}$$ | Loss function của SVM, lồi và sparse |
| **Kernel Function** | $$K(x, z) = \langle \phi(x), \phi(z) \rangle$$ | Ánh xạ ngầm lên không gian đặc trưng |
| **RBF Kernel** | $$K(x, z) = \exp(-\gamma \\|x - z\\|^2)$$ | Kernel phổ biến nhất, linh hoạt |

### 10.3. Ba biến thể của SVM

1. **Hard-Margin SVM** (Dữ liệu tách được hoàn toàn)
   - Nghiệm tồn tại ⟺ dữ liệu linearly separable
   - Margin lớn nhất, không cho phép vi phạm
   - Nhạy cảm với outliers

2. **Soft-Margin SVM** (Dữ liệu thực tế)
   - Luôn có nghiệm
   - Trade-off: margin rộng vs. vi phạm ít (điều khiển bởi $$C$$)
   - Robust với nhiễu

3. **Kernel SVM** (Dữ liệu phi tuyến)
   - Sử dụng dual formulation
   - Ánh xạ ngầm lên không gian chiều cao
   - Không tăng độ phức tạp tính toán

### 10.4. Kernel Methods: Chìa khóa cho phi tuyến

**Kernel Trick** là bước đột phá quan trọng nhất của SVM, biến nó từ một classifier tuyến tính thành một công cụ mạnh mẽ cho dữ liệu phi tuyến.

**Ý tưởng cốt lõi:**

$$
K(x, z) = \langle \phi(x), \phi(z) \rangle
$$

- **Không cần tính $$\phi(x)$$ tường minh**: Tính trực tiếp $$K(x, z)$$ trong không gian gốc
- **Không gian vô hạn chiều**: RBF kernel ánh xạ lên $$\mathbb{R}^\infty$$ mà vẫn tính được!
- **Độ phức tạp không đổi**: $$O(d)$$ thay vì $$O(\text{dim}(\phi))$$

**Bốn kernel phổ biến nhất:**

| Kernel | Công thức | Khi nào dùng | Hyperparameters |
|--------|-----------|--------------|------------------|
| **Linear** | $$\langle x, z \rangle$$ | Baseline, dữ liệu chiều cao | Không |
| **Polynomial** | $$(\langle x, z \rangle + c)^q$$ | Tương tác bậc thấp | $$q, c$$ |
| **RBF/Gaussian** | $$\exp(-\gamma \\|x - z\\|^2)$$ | **Default choice**, rất linh hoạt | $$\gamma$$ |
| **Sigmoid** | $$\tanh(\alpha \langle x, z \rangle + c)$$ | Giống neural net | $$\alpha, c$$ |

**Định lý Mercer - Điều kiện hợp lệ:**

Kernel $$K$$ hợp lệ ⟺ Ma trận Gram $$\mathbf{K}$$ là **symmetric positive semi-definite**

- Đảm bảo: Bài toán SVM là convex, có nghiệm duy nhất
- Tất cả kernel chuẩn đều thỏa mãn
- Có thể xây dựng kernel mới từ kernel cũ (tổng, tích, ...)

**Lựa chọn kernel trong thực tế:**

1. **Bắt đầu với Linear SVM**: Nhanh, baseline tốt
2. **Nếu không đủ → RBF SVM**: Linh hoạt, universal approximator
3. **Grid search $$C$$ và $$\gamma$$**: Cross-validation để tune
4. **Polynomial kernel**: Chỉ khi biết rõ tương tác bậc thấp

### 10.5. Vai trò của Support Vectors

**Support vectors** là "xương sống" của SVM:

- Chỉ **support vectors** (điểm có $$w_i > 0$$) quyết định siêu phẳng
- Thường rất ít: $$|\{i: w_i > 0\}| \ll n$$
- Các điểm khác có thể bỏ đi mà không ảnh hưởng đến mô hình
- Công thức: $$\beta = \sum_{i: w_i > 0} w_i y_i x_i$$

**Ba loại support vectors:**
1. **Trên margin** ($$\xi_i = 0, 0 < w_i < C$$): Điểm lý tưởng, quan trọng nhất
2. **Trong margin** ($$0 < \xi_i < 1, w_i = C$$): Vi phạm nhẹ, vẫn đúng
3. **Misclassified** ($$\xi_i > 1, w_i = C$$): Bị phân loại sai

### 10.6. Primal vs. Dual: Khi nào dùng cái nào?

| Tiêu chí | Primal Form | Dual Form |
|----------|-------------|-----------|
| **Số biến** | $$p + 1 + n$$ | $$n$$ |
| **Khi nào tốt** | $$p \ll n$$ (ít features) | $$n \ll p$$ (nhiều features) |
| **Kernel trick** | Không | Có ✓ |
| **Solver** | CVXOPT, MOSEK | SMO, LIBSVM ✓ |
| **Phổ biến** | Ít | Rất phổ biến ✓ |

### 10.7. Ý nghĩa thực tiễn

**Lý thuyết KKT** trong SVM không chỉ là công cụ để giải bài toán, mà còn giúp:

1. **Hiểu cấu trúc nghiệm:**
   - Tại sao nghiệm sparse (chỉ có support vectors)?
   - Điểm nào quan trọng, điểm nào không?

2. **Phát triển thuật toán:**
   - SMO (Sequential Minimal Optimization) dựa trên điều kiện KKT
   - Kiểm tra hội tụ: solution tối ưu ⟺ thỏa KKT

3. **Phân tích mô hình:**
   - Sensitivity analysis: $$w_i$$ cho biết mức độ "khó phân loại" của điểm $$i$$
   - Model interpretation: support vectors là các "hard cases"

4. **Debugging:**
   - Kiểm tra tính đúng đắn của implementation
   - Phát hiện lỗi numerical (complementary slackness vi phạm)

### 10.8. Khi nào nên dùng SVM?

**✅ SVM phù hợp khi:**
- Dữ liệu có **số chiều cao** ($$p > n$$): text classification, bioinformatics
- Cần mô hình **robust** với outliers
- Có **margin rõ ràng** giữa các classes
- Cần **interpretability** (thông qua support vectors)
- Muốn dùng **kernel trick** cho dữ liệu phi tuyến

**❌ SVM không phù hợp khi:**
- Dữ liệu **rất lớn** ($$n > 10^6$$): training chậm
- Cần **probability estimates**: SVM output là distance, không phải xác suất
- **Multi-class** với nhiều classes ($$K > 10$$): cần one-vs-one hay one-vs-all
- Dữ liệu có **nhiều noise**: neural networks có thể tốt hơn

### 10.9. So sánh với các phương pháp khác

| Phương pháp | Ưu điểm | Nhược điểm | Khi nào dùng |
|-------------|---------|-----------|--------------|
| **SVM** | Margin maximization, kernel trick, robust | Training chậm, khó tune $$C$$ | Dữ liệu chiều cao, margin rõ |
| **Logistic Regression** | Nhanh, probability output, dễ hiểu | Linear boundary, nhạy outliers | Baseline, cần probability |
| **Decision Tree** | Không cần normalize, dễ visualize | Overfitting, unstable | Tabular data, cần explain |
| **Neural Networks** | Flexible, powerful, scalable | Cần nhiều data, black box | Dữ liệu lớn, pattern phức tạp |

### 10.10. Lời khuyên thực hành

1. **Tiền xử lý dữ liệu:**
   - **Normalize/standardize** features: SVM nhạy cảm với scale
   - Xử lý missing values
   - Feature engineering quan trọng cho linear SVM

2. **Chọn kernel:**
   - **Linear kernel**: Thử đầu tiên, nhanh, tránh overfit
   - **RBF kernel**: Default choice cho non-linear
   - **Polynomial kernel**: Ít dùng, khó tune
   - **Custom kernel**: Khi có domain knowledge

3. **Tuning hyperparameters:**
   - $$C$$: Grid search [0.001, 0.01, 0.1, 1, 10, 100, 1000]
   - $$\gamma$$ (cho RBF): Grid search [0.001, 0.01, 0.1, 1]
   - Dùng **cross-validation** (5-fold hoặc 10-fold)
   - **Stratified CV** nếu classes imbalanced

4. **Đánh giá mô hình:**
   - Không chỉ nhìn accuracy
   - Xem **confusion matrix**, precision, recall, F1-score
   - Phân tích **support vectors**: Nhiều SV → có thể overfitting
   - Visualize decision boundary (nếu 2D/3D)

5. **Xử lý imbalanced data:**
   - Dùng **class_weight='balanced'** trong scikit-learn
   - Hoặc tune $$C_+$$ và $$C_-$$ khác nhau cho mỗi class
   - SMOTE (Synthetic Minority Over-sampling)

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
