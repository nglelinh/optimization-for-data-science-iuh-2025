---
layout: post
title: 01-04 Brief history of convex optimization
chapter: '01'
order: 5
owner: Kyeongmin Woo
categories:
- chapter01
lang: en
---

In 1947, George Dantzig faced an Air Force logistics planning problem so large that hand calculation was hopeless; his Simplex algorithm turned linear programming into an industrial revolution. Nearly forty years later, Narendra Karmarkar shocked the field by cutting straight through the *interior* of the feasible polytope instead of walking along its boundary edges, launching the interior-point era—and today, billion-variable machine learning models have sparked a third renaissance in first-order and stochastic methods.

## Background Knowledge Map: Four Historical Eras of Convex Optimization

- **Theoretical Foundations (1900–1970):** Minkowski, Fenchel, von Neumann, Kuhn, Tucker, and Rockafellar established separating hyperplanes, conjugate duality, and KKT optimality conditions.
- **The Simplex Breakthrough (1947–1970s):** Dantzig's Simplex method solved industrial LPs by pivoting between extreme vertices—blazingly fast in practice despite worst-case exponential vertex counts.
- **Polynomial-Time & Interior-Point Revolution (1979–1994):** Khachiyan's ellipsoid method proved LP is in P, Karmarkar's projective method made interior-point solvers practical, and Nesterov & Nemirovski unified LP, QP, SOCP, and SDP via self-concordant barriers.
- **Large-Scale First-Order Era (2000s–Present):** Accelerated gradients, proximal splitting, ADMM, and SGD traded interior-point's $$O(n^3)$$ linear algebra for cheap $$O(n)$$ iterations capable of training modern AI systems.

### Step-by-Step Worked Example (Read Slowly): Simplex Boundary Walk vs. Interior-Point Philosophy

Consider the 2D linear program:
$$\min_{x_1, x_2} \; -x_1 - 2x_2 \quad \text{s.t.} \quad x_1 \ge 0,\; x_2 \ge 0,\; x_1 + x_2 \le 4,\; x_2 \le 3.$$

1. **Simplex path (walking along boundary vertices):**
   - Start at vertex $$v_0 = (0, 0)$$: objective $$= 0$$.
   - Pivot along $$x_2$$ (steepest negative cost $$-2$$) until hitting $$x_2 = 3$$ at vertex $$v_1 = (0, 3)$$: objective $$= -6$$.
   - Pivot along $$x_1$$ until hitting $$x_1 + x_2 = 4$$ at vertex $$v_2 = (1, 3)$$: objective $$= -1 - 6 = -7$$.
   - Check remaining vertex $$(4, 0)$$ (objective $$-4 > -7$$). Thus $$v_2 = (1, 3)$$ is optimal with $$p^* = -7$$.
2. **Interior-point contrast (central path):**
   - Instead of hugging boundary edges, an interior-point method starts strictly inside the polygon—say at $$(1, 1)$$ where all four slacks are strictly positive ($$1, 1, 2, 2 > 0$$)—and minimizes $$-x_1 - 2x_2 - \mu[\ln x_1 + \ln x_2 + \ln(4 - x_1 - x_2) + \ln(3 - x_2)]$$ as $$\mu \to 0^+$$, curving smoothly through the interior directly into $$(1, 3)$$.

# Lịch sử phát triển của Tối ưu hóa Lồi

Tối ưu hóa lồi có một lịch sử phát triển phong phú, từ những nền tảng lý thuyết đầu tiên đến các ứng dụng hiện đại trong công nghệ và khoa học. Hãy cùng khám phá hành trình này qua các giai đoạn quan trọng.

## 🎯 Tổng quan Timeline

<div class="timeline-container">
  <div class="timeline-item">
    <div class="timeline-year">1900-1970</div>
    <div class="timeline-content">Phát triển nền tảng lý thuyết</div>
  </div>
  <div class="timeline-item">
    <div class="timeline-year">1947-1990</div>
    <div class="timeline-content">Các thuật toán đột phá</div>
  </div>
  <div class="timeline-item">
    <div class="timeline-year">1990-nay</div>
    <div class="timeline-content">Bùng nổ ứng dụng</div>
  </div>
</div>

## 📚 Giai đoạn 1: Nền tảng Lý thuyết (1900-1970)

### Những người tiên phong

**Hermann Minkowski (1864-1909)**
- Đặt nền móng cho hình học lồi với khái niệm "tập lồi"
- Phát triển lý thuyết về các đa diện lồi
- Ảnh hưởng: Tạo ra ngôn ngữ toán học cơ bản cho tối ưu hóa lồi

**Leonid Kantorovich (1912-1986)**
- Phát triển lý thuyết lập trình tuyến tính vào những năm 1930
- Giải quyết bài toán phân bổ tài nguyên tối ưu
- Đóng góp: Chứng minh tính khả thi của việc tối ưu hóa trong kinh tế

**John von Neumann (1903-1957)**
- Phát triển lý thuyết trò chơi và mối liên hệ với tối ưu hóa
- Đưa ra định lý minimax cơ bản
- Ảnh hưởng: Kết nối tối ưu hóa với lý thuyết quyết định

### Các khái niệm nền tảng được hình thành:
- **Tập lồi và hàm lồi**: Định nghĩa chính xác và tính chất cơ bản
- **Điều kiện tối ưu**: Phát triển các điều kiện cần và đủ
- **Duality theory**: Khái niệm về bài toán đối ngẫu

## ⚙️ Giai đoạn 2: Cách mạng Thuật toán (1947-1990)

### 1947: Thuật toán Simplex - Bước ngoặt lịch sử

**George Dantzig** đã tạo ra cuộc cách mạng với thuật toán Simplex:

```
Ý tưởng cốt lõi: Di chuyển dọc theo các cạnh của đa diện khả thi
để tìm điểm tối ưu tại một đỉnh.
```

**Tại sao quan trọng?**
- Lần đầu tiên có thuật toán thực tế để giải bài toán lập trình tuyến tính
- Mở ra khả năng ứng dụng trong logistics, sản xuất, quân sự
- Hiệu quả cao trong thực tế dù có độ phức tạp tệ nhất là exponential

### 1960s: Phương pháp Điểm trong đầu tiên

**Fiacco & McCormick** phát triển:
- Barrier methods cho bài toán có ràng buộc bất đẳng thức
- Ý tưởng: Thêm hàm penalty để "đẩy" nghiệm vào bên trong miền khả thi

**Dikin** đóng góp:
- Affine scaling method
- Cải thiện hướng tiếp cận của barrier methods

### 1970s: Phương pháp Ellipsoid và Subgradient

**Shor, Nemirovski, Yudin** phát triển:
- **Ellipsoid method**: Thuật toán đa thức đầu tiên cho LP
- **Subgradient methods**: Xử lý hàm không khả vi

**Ý nghĩa lý thuyết:**
- Chứng minh LP thuộc lớp P (polynomial time)
- Mở rộng khả năng giải các bài toán không trơn

### 1984: Đột phá của Karmarkar

**Narendra Karmarkar** tạo ra cuộc cách mạng thứ hai:
- Thuật toán interior-point với độ phức tạp \\(O(n^{3.5}L)\\)
- Hiệu quả thực tế cao hơn simplex cho bài toán lớn
- Khởi đầu cho kỷ nguyên interior-point methods

### Late 1980s-1990s: Tổng quát hóa

**Nesterov & Nemirovski (1994)** mở rộng:
- Interior-point methods cho tối ưu lồi phi tuyến
- Self-concordant functions
- Polynomial-time algorithms cho broader class

## 🚀 Giai đoạn 3: Bùng nổ Ứng dụng (1990-nay)

### Trước 1990: Giới hạn trong Operations Research

**Các ứng dụng chính:**
- **Transportation problems**: Tối ưu hóa vận chuyển hàng hóa
- **Production planning**: Lập kế hoạch sản xuất
- **Resource allocation**: Phân bổ tài nguyên trong doanh nghiệp
- **Military logistics**: Ứng dụng trong quân sự (WWII và Cold War)

**Tại sao giới hạn?**
- Máy tính chưa đủ mạnh
- Thiếu software tools
- Chưa nhận thức được tiềm năng trong engineering

### Từ 1990: Cách mạng Ứng dụng

#### 🎛️ Control Systems (Hệ thống Điều khiển)
- **Model Predictive Control (MPC)**: Điều khiển dự báo
- **Robust control**: Điều khiển bền vững
- **Ví dụ**: Điều khiển nhiệt độ trong nhà máy, autopilot máy bay

#### 📡 Signal Processing (Xử lý Tín hiệu)
- **Compressed sensing**: Khôi phục tín hiệu từ ít mẫu
- **Image denoising**: Khử nhiễu ảnh
- **Ví dụ**: MRI imaging, radar processing

#### 📱 Communications (Truyền thông)
- **Beamforming**: Định hướng sóng trong antenna arrays
- **Power allocation**: Phân bổ công suất trong mạng wireless
- **Ví dụ**: 5G networks, satellite communications

#### 💻 Circuit Design (Thiết kế Mạch)
- **Gate sizing**: Tối ưu kích thước transistor
- **Power optimization**: Tối ưu tiêu thụ năng lượng
- **Ví dụ**: CPU design, mobile chip optimization

### 🆕 Các lớp bài toán mới

#### Semidefinite Programming (SDP)
```
Tối ưu hóa trên ma trận bán xác định dương
Ứng dụng: Relaxation của bài toán combinatorial
```

#### Second-Order Cone Programming (SOCP)
```
Tối ưu hóa với ràng buộc hình nón bậc hai
Ứng dụng: Robust optimization, portfolio optimization
```

#### Robust Optimization
```
Tối ưu hóa với uncertainty trong dữ liệu
Ứng dụng: Finance, supply chain management
```

## 🔮 Xu hướng Hiện tại và Tương lai

### Machine Learning Integration
- **Convex relaxations** của neural networks
- **Optimization trong training**: Adam, RMSprop
- **Regularization**: L1, L2 penalties

### Big Data Applications
- **Distributed optimization**: Xử lý dữ liệu lớn
- **Online algorithms**: Học trực tuyến
- **Streaming optimization**: Tối ưu real-time

### Quantum Computing
- **Quantum convex optimization**: Thuật toán lượng tử
- **Variational quantum algorithms**: QAOA, VQE

## 💡 Bài học từ Lịch sử

1. **Lý thuyết dẫn đường cho thực hành**: Nền tảng toán học vững chắc là cần thiết
2. **Công nghệ thúc đẩy ứng dụng**: Máy tính mạnh mở ra khả năng mới
3. **Interdisciplinary collaboration**: Sự kết hợp giữa các lĩnh vực tạo ra đột phá
4. **Practical needs drive innovation**: Nhu cầu thực tế thúc đẩy phát triển thuật toán

---

<div class="info-box">
<h4>🎯 Takeaway chính</h4>
<p>Tối ưu hóa lồi đã phát triển từ một lĩnh vực toán học thuần túy thành công cụ không thể thiếu trong công nghệ hiện đại. Sự kết hợp giữa lý thuyết vững chắc và thuật toán hiệu quả đã tạo ra những ứng dụng đột phá trong mọi lĩnh vực của cuộc sống.</p>
</div>

## 🎮 Khám phá Tương tác

### Simplex Algorithm Visualization

<div id="simplex-demo">
  <h4>Minh họa Thuật toán Simplex</h4>
  <p>Thử nghiệm với bài toán lập trình tuyến tính đơn giản:</p>
  
  <div class="problem-setup">
    <p><strong>Bài toán:</strong> Maximize \\(c_1x_1 + c_2x_2\\)</p>
    <p><strong>Subject to:</strong> \\(x_1, x_2 \geq 0\\) và các ràng buộc tuyến tính</p>
    
    <div class="controls">
      <label>c₁: <input type="range" id="c1" min="-5" max="5" value="3" step="0.1"></label>
      <span id="c1-value">3</span><br>
      <label>c₂: <input type="range" id="c2" min="-5" max="5" value="2" step="0.1"></label>
      <span id="c2-value">2</span><br>
      <button onclick="runSimplex()">Chạy Simplex</button>
      <button onclick="resetDemo()">Reset</button>
    </div>
  </div>
  
  <canvas id="simplex-canvas" width="400" height="300"></canvas>
  <div id="simplex-steps"></div>
</div>

### Timeline Explorer

<div id="timeline-explorer">
  <h4>Khám phá Timeline Tương tác</h4>
  <div class="year-slider">
    <label>Năm: <input type="range" id="year-slider" min="1900" max="2024" value="1947" step="1"></label>
    <span id="current-year">1947</span>
  </div>
  
  <div id="year-info">
    <h5 id="event-title">1947: Thuật toán Simplex</h5>
    <p id="event-description">George Dantzig phát triển thuật toán Simplex, mở đầu kỷ nguyên tối ưu hóa thực tế.</p>
    <div id="event-impact">
      <strong>Tác động:</strong> <span id="impact-text">Cách mạng trong operations research</span>
    </div>
  </div>
</div>

### Ứng dụng Hiện đại

<div id="applications-demo">
  <h4>Ứng dụng trong Cuộc sống</h4>
  <div class="app-selector">
    <button onclick="showApplication('portfolio')" class="app-btn">Portfolio Optimization</button>
    <button onclick="showApplication('supply-chain')" class="app-btn">Supply Chain</button>
    <button onclick="showApplication('machine-learning')" class="app-btn">Machine Learning</button>
    <button onclick="showApplication('signal-processing')" class="app-btn">Signal Processing</button>
  </div>
  
  <div id="app-content">
    <div class="app-example" id="portfolio">
      <h5>📈 Portfolio Optimization</h5>
      <p><strong>Bài toán:</strong> Phân bổ vốn đầu tư để tối đa hóa lợi nhuận và giảm thiểu rủi ro</p>
      <p><strong>Công thức:</strong> \\(\min \frac{1}{2}w^T\Sigma w - \mu^T w\\)</p>
      <p><strong>Ứng dụng:</strong> Quỹ đầu tư, ngân hàng, bảo hiểm</p>
    </div>
  </div>
</div>

<script>
// Simplex Algorithm Demo
function runSimplex() {
  const canvas = document.getElementById('simplex-canvas');
  const ctx = canvas.getContext('2d');
  const c1 = parseFloat(document.getElementById('c1').value);
  const c2 = parseFloat(document.getElementById('c2').value);
  
  // Clear canvas
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  
  // Draw feasible region (simple example)
  ctx.fillStyle = 'rgba(0, 122, 204, 0.2)';
  ctx.beginPath();
  ctx.moveTo(50, 250);
  ctx.lineTo(200, 250);
  ctx.lineTo(200, 100);
  ctx.lineTo(100, 50);
  ctx.lineTo(50, 100);
  ctx.closePath();
  ctx.fill();
  
  // Draw objective function direction
  ctx.strokeStyle = '#ff6b35';
  ctx.lineWidth = 3;
  ctx.beginPath();
  ctx.moveTo(125, 175);
  ctx.lineTo(125 + c1*20, 175 - c2*20);
  ctx.stroke();
  
  // Add labels
  ctx.fillStyle = '#333';
  ctx.font = '14px Arial';
  ctx.fillText('Feasible Region', 60, 200);
  ctx.fillText(`Objective: ${c1.toFixed(1)}x₁ + ${c2.toFixed(1)}x₂`, 220, 50);
  
  // Show steps
  document.getElementById('simplex-steps').innerHTML = `
    <h5>Các bước Simplex:</h5>
    <ol>
      <li>Bắt đầu tại đỉnh (0,0)</li>
      <li>Kiểm tra hướng cải thiện: (${c1.toFixed(1)}, ${c2.toFixed(1)})</li>
      <li>Di chuyển dọc theo cạnh có gradient tốt nhất</li>
      <li>Dừng khi không thể cải thiện thêm</li>
    </ol>
  `;
}

function resetDemo() {
  document.getElementById('c1').value = 3;
  document.getElementById('c2').value = 2;
  document.getElementById('c1-value').textContent = '3';
  document.getElementById('c2-value').textContent = '2';
  document.getElementById('simplex-steps').innerHTML = '';
  const canvas = document.getElementById('simplex-canvas');
  const ctx = canvas.getContext('2d');
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}

// Timeline Explorer
const timelineEvents = {
  1900: {title: "1900: Nền tảng Hình học", desc: "Minkowski phát triển lý thuyết tập lồi", impact: "Tạo nền tảng toán học"},
  1930: {title: "1930: Kantorovich", desc: "Lý thuyết lập trình tuyến tính đầu tiên", impact: "Ứng dụng trong kinh tế"},
  1947: {title: "1947: Thuật toán Simplex", desc: "Dantzig tạo ra thuật toán thực tế đầu tiên", impact: "Cách mạng operations research"},
  1960: {title: "1960s: Interior Point", desc: "Fiacco & McCormick phát triển barrier methods", impact: "Mở rộng khả năng giải bài toán"},
  1984: {title: "1984: Karmarkar", desc: "Interior-point polynomial-time algorithm", impact: "Đột phá về độ phức tạp"},
  1994: {title: "1994: Nesterov & Nemirovski", desc: "Tổng quát hóa cho convex optimization", impact: "Nền tảng cho ứng dụng hiện đại"},
  2010: {title: "2010s: Machine Learning", desc: "Tích hợp với AI và Big Data", impact: "Ứng dụng rộng rãi trong công nghệ"},
  2024: {title: "2024: Quantum Computing", desc: "Thuật toán tối ưu lượng tử", impact: "Tương lai của tính toán"}
};

function updateTimeline() {
  const year = parseInt(document.getElementById('year-slider').value);
  document.getElementById('current-year').textContent = year;
  
  // Find closest event
  let closestYear = 1900;
  for (let eventYear in timelineEvents) {
    if (parseInt(eventYear) <= year) {
      closestYear = parseInt(eventYear);
    }
  }
  
  const event = timelineEvents[closestYear];
  document.getElementById('event-title').textContent = event.title;
  document.getElementById('event-description').textContent = event.desc;
  document.getElementById('impact-text').textContent = event.impact;
}

// Applications Demo
const applications = {
  portfolio: {
    title: "📈 Portfolio Optimization",
    problem: "Phân bổ vốn đầu tư để tối đa hóa lợi nhuận và giảm thiểu rủi ro",
    formula: "\\min \\frac{1}{2}w^T\\Sigma w - \\mu^T w",
    usage: "Quỹ đầu tư, ngân hàng, bảo hiểm"
  },
  "supply-chain": {
    title: "🚚 Supply Chain Optimization",
    problem: "Tối ưu hóa logistics và phân phối hàng hóa",
    formula: "\\min \\sum_{i,j} c_{ij}x_{ij}",
    usage: "Amazon, Walmart, FedEx"
  },
  "machine-learning": {
    title: "🤖 Machine Learning",
    problem: "Training neural networks và feature selection",
    formula: "\\min \\frac{1}{2}||Xw - y||^2 + \\lambda||w||_1",
    usage: "Google, Facebook, Tesla autopilot"
  },
  "signal-processing": {
    title: "📡 Signal Processing",
    problem: "Khôi phục tín hiệu từ dữ liệu nhiễu hoặc không đầy đủ",
    formula: "\\min ||x||_1 \\text{ s.t. } ||Ax - b||_2 \\leq \\epsilon",
    usage: "MRI imaging, radar, 5G communications"
  }
};

function showApplication(appKey) {
  const app = applications[appKey];
  document.getElementById('app-content').innerHTML = `
    <div class="app-example">
      <h5>${app.title}</h5>
      <p><strong>Bài toán:</strong> ${app.problem}</p>
      <p><strong>Công thức:</strong> \\(${app.formula}\\)</p>
      <p><strong>Ứng dụng:</strong> ${app.usage}</p>
    </div>
  `;
  
  // Re-render MathJax
  if (window.MathJax) {
    MathJax.typesetPromise([document.getElementById('app-content')]);
  }
}

// Event listeners
document.addEventListener('DOMContentLoaded', function() {
  // Slider updates
  document.getElementById('c1').addEventListener('input', function() {
    document.getElementById('c1-value').textContent = this.value;
  });
  
  document.getElementById('c2').addEventListener('input', function() {
    document.getElementById('c2-value').textContent = this.value;
  });
  
  document.getElementById('year-slider').addEventListener('input', updateTimeline);
  
  // Initialize
  updateTimeline();
  showApplication('portfolio');
});
</script>

<style>
.timeline-container {
  position: relative;
  margin: 20px 0;
}

.timeline-item {
  display: flex;
  margin: 10px 0;
  padding: 10px;
  border-left: 3px solid #007acc;
  background: #f8f9fa;
}

.timeline-year {
  font-weight: bold;
  color: #007acc;
  min-width: 100px;
}

.timeline-content {
  margin-left: 20px;
}

.info-box {
  background: #e3f2fd;
  border: 1px solid #2196f3;
  border-radius: 5px;
  padding: 15px;
  margin: 20px 0;
}

.info-box h4 {
  margin-top: 0;
  color: #1976d2;
}

/* Interactive Demo Styles */
#simplex-demo, #timeline-explorer, #applications-demo {
  background: #f8f9fa;
  border: 1px solid #dee2e6;
  border-radius: 8px;
  padding: 20px;
  margin: 20px 0;
}

.controls {
  margin: 15px 0;
}

.controls label {
  display: inline-block;
  margin: 5px 10px 5px 0;
  min-width: 40px;
}

.controls input[type="range"] {
  width: 150px;
  margin: 0 10px;
}

.controls button {
  background: #007acc;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
  margin: 5px;
}

.controls button:hover {
  background: #005a9e;
}

#simplex-canvas {
  border: 1px solid #ccc;
  margin: 10px 0;
  background: white;
}

.year-slider {
  margin: 15px 0;
}

.year-slider input[type="range"] {
  width: 300px;
}

#year-info {
  background: white;
  padding: 15px;
  border-radius: 5px;
  border-left: 4px solid #007acc;
}

.app-selector {
  margin: 15px 0;
}

.app-btn {
  background: #28a745;
  color: white;
  border: none;
  padding: 10px 15px;
  border-radius: 5px;
  cursor: pointer;
  margin: 5px;
  font-size: 14px;
}

.app-btn:hover {
  background: #218838;
}

.app-example {
  background: white;
  padding: 15px;
  border-radius: 5px;
  border-left: 4px solid #28a745;
  margin-top: 15px;
}

.problem-setup {
  background: white;
  padding: 15px;
  border-radius: 5px;
  margin: 10px 0;
}

#simplex-steps {
  background: white;
  padding: 15px;
  border-radius: 5px;
  margin-top: 10px;
}

#simplex-steps ol {
  margin: 10px 0;
  padding-left: 20px;
}

#simplex-steps li {
  margin: 5px 0;
}
</style>