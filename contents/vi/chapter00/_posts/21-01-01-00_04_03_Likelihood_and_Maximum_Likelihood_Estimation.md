---
layout: post
title: 00-04-03 Likelihood và Ước Lượng Hợp Lý Tối Đa (MLE)
chapter: '00'
order: 17
owner: AI Assistant
categories:
- chapter00
lang: vi
lesson_type: required
---

## Likelihood và ước lượng hợp lý tối đa

Trong xác suất thống kê, **hàm hợp lý (likelihood)** đo mức độ phù hợp của một mô hình hay một bộ tham số với dữ liệu đã quan sát. Khi giữ cố định dữ liệu và xem biểu thức xác suất như một hàm theo tham số, ta thu được hàm hợp lý; lưu ý rằng đây không phải là một phân phối xác suất theo tham số.

### Định nghĩa hàm hợp lý (Likelihood)

Hàm hợp lý của tham số $$	heta$$ ứng với dữ liệu quan sát $$x$$ được định nghĩa bằng xác suất (hoặc mật độ xác suất) quan sát được dữ liệu $$x$$ khi tham số nhận giá trị $$	heta$$. Hàm này thường ký hiệu là $$L(	heta \mid x)$$:

**Công thức:**
$$L(	heta \mid x) = P(x \mid 	heta)$$

Trong đó, $$P(x \mid 	heta)$$ là xác suất (hoặc mật độ) của dữ liệu $$x$$ khi tham số $$	heta$$ đã cho trước.

### Điểm khác biệt với xác suất

- **Xác suất** mô tả khả năng xảy ra của các kết quả ngẫu nhiên trong tương lai khi tham số của phân phối đã biết.
- **Hàm hợp lý (likelihood)** ngược lại: dữ liệu đã được quan sát và giữ cố định, còn ta thay đổi tham số để đánh giá mức độ phù hợp của từng giá trị tham số với dữ liệu đó.

<div style="background: #fff3cd; padding: 15px; border-left: 4px solid #ffc107; margin: 20px 0;">
<strong>⚠️ Lưu ý quan trọng:</strong> Hàm hợp lý không phải là phân phối xác suất của tham số θ, vì tổng hoặc tích phân của nó theo θ không nhất thiết bằng 1.
</div>

### Ví dụ minh họa: Tung đồng xu

Giả sử bạn tung một đồng xu 5 lần và quan sát được 3 lần "mặt sấp" (S) cùng 2 lần "mặt ngửa" (N). Gọi $$p$$ là xác suất xuất hiện mặt sấp.

Hàm hợp lý của $$p$$ ứng với dữ liệu (3 sấp, 2 ngửa) là:

$$L(p \mid 	ext{dữ liệu}) = P(	ext{3 sấp, 2 ngửa} \mid p) = inom{5}{3} p^3 (1-p)^2$$

Trong đó:
- $$inom{5}{3}$$ là hệ số nhị thức (số cách chọn 3 lần ra mặt sấp trong 5 lần tung).
- $$p^3$$ là xác suất cho 3 lần mặt sấp.
- $$(1-p)^2$$ là xác suất cho 2 lần mặt ngửa.

**Thử tính với các giá trị $$p$$ khác nhau:**

Với $$p = 0.6$$:
$$L(0.6 \mid 	ext{dữ liệu}) = inom{5}{3} (0.6)^3 (0.4)^2 = 10 	imes 0.216 	imes 0.16 pprox 0.3456$$

Với $$p = 0.5$$:
$$L(0.5 \mid 	ext{dữ liệu}) = inom{5}{3} (0.5)^3 (0.5)^2 = 10 	imes 0.125 	imes 0.25 pprox 0.3125$$

Giá trị hàm hợp lý tại $$p = 0.6$$ cao hơn tại $$p = 0.5$$, cho thấy $$p = 0.6$$ phù hợp với dữ liệu quan sát hơn so với $$p = 0.5$$.

### Ví dụ tương tác: Tung đồng xu

<div id="coin-flip-example" style="border: 1px solid #ddd; padding: 20px; margin: 20px 0; border-radius: 8px;">
    <h4>Thí nghiệm tung đồng xu</h4>
    
    <div style="margin: 15px 0;">
        <label for="p-slider">Xác suất mặt sấp (p): <span id="p-value">0.5</span></label><br>
        <input type="range" id="p-slider" min="0.01" max="0.99" step="0.01" value="0.5" style="width: 300px;">
    </div>
    
    <div style="margin: 15px 0;">
        <label for="heads-input">Số lần sấp: </label>
        <input type="number" id="heads-input" value="3" min="0" max="20" style="width: 60px;">
        
        <label for="tails-input" style="margin-left: 20px;">Số lần ngửa: </label>
        <input type="number" id="tails-input" value="2" min="0" max="20" style="width: 60px;">
    </div>
    
    <div style="margin: 15px 0;">
        <canvas id="likelihood-plot" width="600" height="300" style="border: 1px solid #ccc;"></canvas>
    </div>
    
    <div id="likelihood-result" style="background: #f8f9fa; padding: 10px; border-radius: 4px; margin: 10px 0;">
        <strong>Likelihood hiện tại:</strong> <span id="current-likelihood">0.3125</span><br>
        <strong>Log-likelihood:</strong> <span id="current-log-likelihood">-1.16</span>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const pSlider = document.getElementById('p-slider');
    const pValue = document.getElementById('p-value');
    const headsInput = document.getElementById('heads-input');
    const tailsInput = document.getElementById('tails-input');
    const canvas = document.getElementById('likelihood-plot');
    const ctx = canvas.getContext('2d');
    const likelihoodResult = document.getElementById('current-likelihood');
    const logLikelihoodResult = document.getElementById('current-log-likelihood');
    
    function binomialCoeff(n, k) {
        if (k > n) return 0;
        if (k === 0 || k === n) return 1;
        
        let result = 1;
        for (let i = 0; i < k; i++) {
            result = result * (n - i) / (i + 1);
        }
        return result;
    }
    
    function likelihood(p, heads, tails) {
        const n = heads + tails;
        const coeff = binomialCoeff(n, heads);
        return coeff * Math.pow(p, heads) * Math.pow(1 - p, tails);
    }
    
    function logLikelihood(p, heads, tails) {
        const n = heads + tails;
        const logCoeff = Math.log(binomialCoeff(n, heads));
        return logCoeff + heads * Math.log(p) + tails * Math.log(1 - p);
    }
    
    function plotLikelihood() {
        const heads = parseInt(headsInput.value);
        const tails = parseInt(tailsInput.value);
        const currentP = parseFloat(pSlider.value);
        
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        // Vẽ trục
        ctx.strokeStyle = '#333';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(50, 250);
        ctx.lineTo(550, 250);
        ctx.moveTo(50, 250);
        ctx.lineTo(50, 50);
        ctx.stroke();
        
        // Nhãn trục
        ctx.fillStyle = '#333';
        ctx.font = '12px Arial';
        ctx.fillText('p (xác suất mặt sấp)', 250, 280);
        ctx.save();
        ctx.translate(20, 150);
        ctx.rotate(-Math.PI/2);
        ctx.fillText('Likelihood', 0, 0);
        ctx.restore();
        
        // Vẽ đường likelihood
        ctx.strokeStyle = '#2196F3';
        ctx.lineWidth = 2;
        ctx.beginPath();
        
        let maxLikelihood = 0;
        const points = [];
        
        for (let i = 0; i <= 500; i++) {
            const p = 0.01 + (i / 500) * 0.98;
            const l = likelihood(p, heads, tails);
            points.push({p: p, l: l});
            maxLikelihood = Math.max(maxLikelihood, l);
        }
        
        for (let i = 0; i < points.length; i++) {
            const x = 50 + (points[i].p - 0.01) / 0.98 * 500;
            const y = 250 - (points[i].l / maxLikelihood) * 200;
            
            if (i === 0) {
                ctx.moveTo(x, y);
            } else {
                ctx.lineTo(x, y);
            }
        }
        ctx.stroke();
        
        // Vẽ điểm hiện tại
        const currentLikelihood = likelihood(currentP, heads, tails);
        const currentX = 50 + (currentP - 0.01) / 0.98 * 500;
        const currentY = 250 - (currentLikelihood / maxLikelihood) * 200;
        
        ctx.fillStyle = '#f44336';
        ctx.beginPath();
        ctx.arc(currentX, currentY, 5, 0, 2 * Math.PI);
        ctx.fill();
        
        // Cập nhật kết quả
        likelihoodResult.textContent = currentLikelihood.toFixed(6);
        logLikelihoodResult.textContent = logLikelihood(currentP, heads, tails).toFixed(4);
        
        // Vẽ các tick marks
        ctx.fillStyle = '#666';
        ctx.font = '10px Arial';
        for (let i = 0; i <= 10; i++) {
            const p = i / 10;
            const x = 50 + (p - 0.01) / 0.98 * 500;
            ctx.fillText(p.toFixed(1), x - 10, 265);
        }
    }
    
    function updateDisplay() {
        pValue.textContent = pSlider.value;
        plotLikelihood();
    }
    
    pSlider.addEventListener('input', updateDisplay);
    headsInput.addEventListener('input', plotLikelihood);
    tailsInput.addEventListener('input', plotLikelihood);
    
    // Khởi tạo
    updateDisplay();
});
</script>

### Ước lượng hợp lý tối đa (MLE)

**Ước lượng hợp lý tối đa (Maximum Likelihood Estimation — MLE)** là phương pháp tìm giá trị tham số $$	heta$$ làm cực đại hàm hợp lý $$L(	heta \mid x)$$.

**Công thức MLE:**
$$\hat{	heta}_{MLE} = rg\max_{	heta} L(	heta \mid x)$$

Trong thực hành, vì hàm logarit đơn điệu tăng, ta thường cực đại hóa hàm log-likelihood để chuyển tích thành tổng và tránh tràn số:
$$\hat{	heta}_{MLE} = rg\max_{	heta} \log L(	heta \mid x)$$

### Ví dụ MLE: Phân phối chuẩn

Giả sử ta có $$n$$ quan sát độc lập và cùng phân phối $$x_1, x_2, \ldots, x_n$$ từ phân phối chuẩn $$N(\mu, \sigma^2)$$.

**Hàm hợp lý:**
$$L(\mu, \sigma^2 \mid x_1, \ldots, x_n) = \prod_{i=1}^{n} rac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-rac{(x_i - \mu)^2}{2\sigma^2}ight)$$

**Log-likelihood:**
$$\ell(\mu, \sigma^2) = -rac{n}{2}\log(2\pi) - rac{n}{2}\log(\sigma^2) - rac{1}{2\sigma^2}\sum_{i=1}^{n}(x_i - \mu)^2$$

**Tìm ước lượng MLE:**

Lấy đạo hàm riêng theo $$\mu$$ và cho bằng 0:
$$rac{\partial \ell}{\partial \mu} = rac{1}{\sigma^2}\sum_{i=1}^{n}(x_i - \mu) = 0$$

Giải phương trình này, ta thu được trung bình mẫu: $$\hat{\mu}_{MLE} = rac{1}{n}\sum_{i=1}^{n} x_i = ar{x}$$

Tương tự, lấy đạo hàm theo $$\sigma^2$$ và cho bằng 0 ta thu được:
$$\hat{\sigma^2}_{MLE} = rac{1}{n}\sum_{i=1}^{n}(x_i - ar{x})^2$$

### Ví dụ tương tác: MLE cho phân phối chuẩn

<div id="normal-mle-example" style="border: 1px solid #ddd; padding: 20px; margin: 20px 0; border-radius: 8px;">
    <h4>MLE cho phân phối chuẩn</h4>
    
    <div style="margin: 15px 0;">
        <button id="generate-data" style="background: #4CAF50; color: white; padding: 8px 16px; border: none; border-radius: 4px; cursor: pointer;">Tạo dữ liệu mới</button>
        <span style="margin-left: 20px;">Số mẫu: </span>
        <input type="number" id="sample-size" value="50" min="10" max="200" style="width: 60px;">
    </div>
    
    <div style="margin: 15px 0;">
        <label for="mu-guess">Ước lượng μ: <span id="mu-guess-value">0</span></label><br>
        <input type="range" id="mu-guess" min="-3" max="3" step="0.1" value="0" style="width: 300px;">
    </div>
    
    <div style="margin: 15px 0;">
        <label for="sigma-guess">Ước lượng σ: <span id="sigma-guess-value">1</span></label><br>
        <input type="range" id="sigma-guess" min="0.1" max="3" step="0.1" value="1" style="width: 300px;">
    </div>
    
    <div style="margin: 15px 0;">
        <canvas id="normal-plot" width="600" height="300" style="border: 1px solid #ccc;"></canvas>
    </div>
    
    <div id="mle-results" style="background: #f8f9fa; padding: 10px; border-radius: 4px; margin: 10px 0;">
        <div><strong>Dữ liệu thực:</strong> μ = <span id="true-mu">1.0</span>, σ = <span id="true-sigma">1.5</span></div>
        <div><strong>Ước lượng MLE:</strong> μ̂ = <span id="mle-mu">0.95</span>, σ̂ = <span id="mle-sigma">1.48</span></div>
        <div><strong>Ước lượng hiện tại:</strong> μ = <span id="current-mu">0</span>, σ = <span id="current-sigma">1</span></div>
        <div><strong>Log-likelihood hiện tại:</strong> <span id="current-ll">-75.2</span></div>
        <div><strong>Log-likelihood tối đa:</strong> <span id="max-ll">-72.1</span></div>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const generateBtn = document.getElementById('generate-data');
    const sampleSizeInput = document.getElementById('sample-size');
    const muGuess = document.getElementById('mu-guess');
    const sigmaGuess = document.getElementById('sigma-guess');
    const muGuessValue = document.getElementById('mu-guess-value');
    const sigmaGuessValue = document.getElementById('sigma-guess-value');
    const canvas = document.getElementById('normal-plot');
    const ctx = canvas.getContext('2d');
    
    let data = [];
    let trueMu = 1.0;
    let trueSigma = 1.5;
    
    function normalRandom(mu, sigma) {
        let u = 0, v = 0;
        while(u === 0) u = Math.random();
        while(v === 0) v = Math.random();
        return Math.sqrt(-2.0 * Math.log(u)) * Math.cos(2.0 * Math.PI * v) * sigma + mu;
    }
    
    function generateData() {
        const n = parseInt(sampleSizeInput.value);
        trueMu = (Math.random() - 0.5) * 4; // -2 to 2
        trueSigma = 0.5 + Math.random() * 2; // 0.5 to 2.5
        
        data = [];
        for (let i = 0; i < n; i++) {
            data.push(normalRandom(trueMu, trueSigma));
        }
        
        // Tính MLE
        const mleMu = data.reduce((sum, x) => sum + x, 0) / data.length;
        const mleSigma = Math.sqrt(data.reduce((sum, x) => sum + (x - mleMu) ** 2, 0) / data.length);
        
        document.getElementById('true-mu').textContent = trueMu.toFixed(2);
        document.getElementById('true-sigma').textContent = trueSigma.toFixed(2);
        document.getElementById('mle-mu').textContent = mleMu.toFixed(2);
        document.getElementById('mle-sigma').textContent = mleSigma.toFixed(2);
        
        plotData();
    }
    
    function logLikelihood(mu, sigma, data) {
        const n = data.length;
        const sumSquares = data.reduce((sum, x) => sum + (x - mu) ** 2, 0);
        return -n/2 * Math.log(2 * Math.PI) - n * Math.log(sigma) - sumSquares / (2 * sigma ** 2);
    }
    
    function normalPDF(x, mu, sigma) {
        return (1 / (sigma * Math.sqrt(2 * Math.PI))) * Math.exp(-0.5 * ((x - mu) / sigma) ** 2);
    }
    
    function plotData() {
        if (data.length === 0) return;
        
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        const currentMu = parseFloat(muGuess.value);
        const currentSigma = parseFloat(sigmaGuess.value);
        
        // Tìm phạm vi dữ liệu
        const minX = Math.min(...data) - 1;
        const maxX = Math.max(...data) + 1;
        const range = maxX - minX;
        
        // Vẽ histogram
        const bins = 20;
        const binWidth = range / bins;
        const binCounts = new Array(bins).fill(0);
        
        data.forEach(x => {
            const binIndex = Math.floor((x - minX) / binWidth);
            if (binIndex >= 0 && binIndex < bins) {
                binCounts[binIndex]++;
            }
        });
        
        const maxCount = Math.max(...binCounts);
        
        ctx.fillStyle = 'rgba(33, 150, 243, 0.3)';
        for (let i = 0; i < bins; i++) {
            const x = 50 + (i * binWidth / range) * 500;
            const height = (binCounts[i] / maxCount) * 200;
            const width = (binWidth / range) * 500;
            ctx.fillRect(x, 250 - height, width, height);
        }
        
        // Vẽ đường phân phối thực
        ctx.strokeStyle = '#4CAF50';
        ctx.lineWidth = 2;
        ctx.beginPath();
        for (let i = 0; i <= 500; i++) {
            const x = minX + (i / 500) * range;
            const y = normalPDF(x, trueMu, trueSigma);
            const plotX = 50 + (i / 500) * 500;
            const plotY = 250 - (y / (1 / (trueSigma * Math.sqrt(2 * Math.PI)))) * 200;
            
            if (i === 0) ctx.moveTo(plotX, plotY);
            else ctx.lineTo(plotX, plotY);
        }
        ctx.stroke();
        
        // Vẽ đường ước lượng hiện tại
        ctx.strokeStyle = '#f44336';
        ctx.lineWidth = 2;
        ctx.setLineDash([5, 5]);
        ctx.beginPath();
        for (let i = 0; i <= 500; i++) {
            const x = minX + (i / 500) * range;
            const y = normalPDF(x, currentMu, currentSigma);
            const plotX = 50 + (i / 500) * 500;
            const plotY = 250 - (y / (1 / (currentSigma * Math.sqrt(2 * Math.PI)))) * 200;
            
            if (i === 0) ctx.moveTo(plotX, plotY);
            else ctx.lineTo(plotX, plotY);
        }
        ctx.stroke();
        ctx.setLineDash([]);
        
        // Vẽ trục
        ctx.strokeStyle = '#333';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(50, 250);
        ctx.lineTo(550, 250);
        ctx.stroke();
        
        // Cập nhật kết quả
        const currentLL = logLikelihood(currentMu, currentSigma, data);
        const mleMu = data.reduce((sum, x) => sum + x, 0) / data.length;
        const mleSigma = Math.sqrt(data.reduce((sum, x) => sum + (x - mleMu) ** 2, 0) / data.length);
        const maxLL = logLikelihood(mleMu, mleSigma, data);
        
        document.getElementById('current-mu').textContent = currentMu.toFixed(2);
        document.getElementById('current-sigma').textContent = currentSigma.toFixed(2);
        document.getElementById('current-ll').textContent = currentLL.toFixed(2);
        document.getElementById('max-ll').textContent = maxLL.toFixed(2);
        
        // Thêm chú thích
        ctx.fillStyle = '#4CAF50';
        ctx.fillRect(450, 60, 15, 3);
        ctx.fillStyle = '#333';
        ctx.font = '12px Arial';
        ctx.fillText('Phân phối thực', 470, 65);
        
        ctx.strokeStyle = '#f44336';
        ctx.setLineDash([5, 5]);
        ctx.beginPath();
        ctx.moveTo(450, 80);
        ctx.lineTo(465, 80);
        ctx.stroke();
        ctx.setLineDash([]);
        ctx.fillText('Ước lượng hiện tại', 470, 85);
    }
    
    function updateDisplay() {
        muGuessValue.textContent = muGuess.value;
        sigmaGuessValue.textContent = sigmaGuess.value;
        plotData();
    }
    
    generateBtn.addEventListener('click', generateData);
    muGuess.addEventListener('input', updateDisplay);
    sigmaGuess.addEventListener('input', updateDisplay);
    sampleSizeInput.addEventListener('change', generateData);
    
    // Khởi tạo
    generateData();
});
</script>

### Tính chất của MLE

1. **Tính vững (Consistency)**: khi kích thước mẫu tăng lên vô hạn, ước lượng MLE hội tụ theo xác suất về giá trị thực của tham số.
2. **Tính chuẩn tiệm cận (Asymptotic Normality)**: với kích thước mẫu đủ lớn, phân phối của ước lượng MLE xấp xỉ phân phối chuẩn.
3. **Tính hiệu quả tiệm cận (Asymptotic Efficiency)**: MLE đạt cận dưới Cramér–Rao về mặt tiệm cận, tức có phương sai nhỏ nhất trong lớp các ước lượng không chệch.
4. **Tính bất biến (Invariance)**: nếu $$\hat{	heta}$$ là MLE của $$	heta$$ thì $$g(\hat{	heta})$$ là MLE của $$g(	heta)$$ với mọi hàm khả nghịch $$g$$ (và mở rộng cho hàm $$g$$ tổng quát thông qua hàm hợp lý cảm sinh).

### Ứng dụng của MLE

#### 1. Ước lượng tham số

MLE được sử dụng rộng rãi để ước lượng tham số trong nhiều mô hình thống kê:
- Phân phối chuẩn: ước lượng kỳ vọng và phương sai.
- Phân phối Poisson: ước lượng tham số tốc độ $$\lambda$$.
- Hồi quy tuyến tính: ước lượng vector hệ số hồi quy.

#### 2. So sánh mô hình

Hàm hợp lý là cơ sở của nhiều tiêu chí đánh giá và chọn mô hình:
- **Kiểm định tỷ số hợp lý (Likelihood Ratio Test)**: so sánh hai mô hình lồng nhau.
- **AIC / BIC**: các tiêu chí lựa chọn mô hình cân bằng giữa log-likelihood và độ phức tạp mô hình.

#### 3. Thống kê Bayes

Trong suy luận Bayes, hàm hợp lý kết hợp với phân phối tiên nghiệm (prior) để xác định phân phối hậu nghiệm (posterior):

$$P(	heta \mid x) \propto L(	heta \mid x) \cdot P(	heta)$$

### Kết nối với tối ưu hóa

Bài toán MLE trực tiếp dẫn đến một bài toán tối ưu hóa:

$$\max_{	heta} L(	heta \mid x) \quad 	ext{hoặc} \quad \max_{	heta} \log L(	heta \mid x)$$

Tùy cấu trúc mô hình, bài toán này có thể thuộc các dạng:
- **Tối ưu hóa không ràng buộc**: khi tham số nhận giá trị tự do trên $$\mathbb{R}^d$$.
- **Tối ưu hóa có ràng buộc**: khi tham số phải thỏa mãn miền điều kiện (ví dụ $$p \in [0, 1]$$ hoặc $$\sigma > 0$$).
- **Bài toán tối ưu hóa lồi**: với nhiều mô hình, hàm log-likelihood là hàm lõm (tương đương, âm log-likelihood là hàm lồi), nên bài toán có nghiệm tối ưu toàn cục.

<div style="background: #e8f4fd; padding: 15px; border-left: 4px solid #2196F3; margin: 20px 0;">
<strong>💡 Kết nối với tối ưu hóa lồi:</strong> Nhiều bài toán MLE — đặc biệt trong họ phân phối mũ — dẫn đến bài toán tối ưu hóa lồi. Nhờ đó, mọi cực tiểu địa phương đều là cực tiểu toàn cục và các thuật toán tối ưu hội tụ ổn định về nghiệm đúng.
</div>

### Ví dụ thực tế: Hồi quy logistic

Trong hồi quy logistic, xác suất của biến nhị phân $$y \in \{0, 1\}$$ được mô hình hóa theo đặc trưng $$x$$:

$$P(y = 1 \mid x) = rac{1}{1 + e^{-(eta_0 + eta_1 x)}}$$

**Log-likelihood** (với $$p_i = P(y_i = 1 \mid x_i)$$):
$$\ell(eta_0, eta_1) = \sum_{i=1}^{n} \left[ y_i \log(p_i) + (1-y_i) \log(1-p_i) ight]$$

Đây là bài toán cực đại hóa hàm lõm (tương đương cực tiểu hóa hàm lồi là âm log-likelihood), có thể giải hiệu quả bằng gradient descent hoặc phương pháp Newton.

### Tóm tắt

- **Hàm hợp lý (Likelihood)** đo mức độ phù hợp của tham số với dữ liệu đã quan sát.
- **MLE** tìm bộ tham số làm cực đại hàm hợp lý (hoặc log-likelihood).
- MLE sở hữu nhiều tính chất tiệm cận tốt: tính vững, tính chuẩn tiệm cận và tính hiệu quả tiệm cận.
- MLE chuyển trực tiếp bài toán ước lượng thống kê thành bài toán tối ưu hóa, trong đó nhiều trường hợp quan trọng là tối ưu hóa lồi.

<div style="background: #d4edda; padding: 15px; border-left: 4px solid #28a745; margin: 20px 0;">
<strong>🎯 Điểm cốt lõi:</strong> MLE là cầu nối trực tiếp giữa thống kê và tối ưu hóa, giúp ta hiểu cách tham số của các mô hình thống kê được ước lượng bằng các phương pháp tối ưu hóa, đặc biệt là tối ưu hóa lồi.
</div>
