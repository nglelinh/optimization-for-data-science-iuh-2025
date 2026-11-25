---
layout: post
title: 01-04 Lịch sử ngắn gọn về tối ưu hóa lồi
chapter: '01'
order: 5
owner: Kyeongmin Woo
categories:
- chapter01
lang: vi
---

Ít ai biết rằng thuật toán Đơn hình (Simplex) — viên gạch khai sinh thời đại tối ưu hóa tính toán — ra đời năm 1947 từ một bài toán hậu cần quân sự tưởng chừng đời thường của George Dantzig: làm sao lập kế hoạch cung ứng tối ưu với ngân sách thấp nhất? Kể từ đó, tối ưu hóa lồi trải qua ba làn sóng lịch sử ngoạn mục: từ nền tảng hình học thuần túy của Minkowski–Fenchel–Rockafellar, đến cuộc cách mạng đa thức của phương pháp điểm trong (Karmarkar, Nesterov–Nemirovski), và bùng nổ thành động cơ cốt lõi của học máy quy mô lớn thế kỷ 21.

Đọc lịch sử tối ưu hóa giúp bạn hiểu *tại sao* các công cụ trong khóa học lại xuất hiện theo đúng thứ tự như vậy, thay vì nhìn chúng như những định lý rời rạc.

## Bản đồ kiến thức nền: Ba làn sóng định hình tối ưu hóa lồi hiện đại

- **Làn sóng 1 — Nền tảng lý thuyết (1900–1970):** Minkowski đặt nền hình học tập lồi, Fenchel–Rockafellar xây dựng giải tích lồi và đối ngẫu, Karush–Kuhn–Tucker thiết lập điều kiện tối ưu KKT cho bài toán có ràng buộc bất đẳng thức.
- **Làn sóng 2 — Cuộc cách mạng thuật toán đa thức (1947–1995):** Simplex của Dantzig (1947) giải LP thần tốc trong thực tế nhưng có trường hợp xấu nhất hàm mũ; phương pháp Ellipsoid (Khachiyan, 1979) chứng minh LP thuộc lớp $$P$$; và phương pháp Điểm trong (Karmarkar, 1984; Nesterov–Nemirovski, 1994) mở rộng thời gian đa thức sang cả QP, SOCP và SDP.
- **Làn sóng 3 — Tối ưu hóa quy mô lớn và kỷ nguyên AI (2000–nay):** Các thư viện mô hình hóa kỷ luật (CVX, CVXPY) dân chủ hóa tối ưu hóa lồi, trong khi các thuật toán bậc nhất (FISTA, ADMM, SGD, Adam) xử lý mượt mà hàng triệu đến hàng tỷ biến trong khoa học dữ liệu.

### Khung giải thích (nên đọc chậm): Trải nghiệm ý tưởng "đường trung tâm" của phương pháp điểm trong (1984–1994)

Khác với Simplex nhảy dọc theo các đỉnh biên của đa diện, phương pháp điểm trong đi xuyên qua **lòng trong** miền khả thi bằng hàm rào chắn logarit (log-barrier). Xét bài toán LP một biến tối giản:

$$\min_{x} x \quad \text{với điều kiện} \quad x \ge 0 \quad (\text{nghiệm đúng } x^* = 0,\ p^* = 0).$$

1. **Thay ràng buộc cứng $$x \ge 0$$ bằng rào chắn mượt $$-\frac{1}{t}\ln x$$ (với $$t > 0$$ tăng dần):**
   $$\min_{x > 0} \phi_t(x) = t x - \ln x.$$
   Khi $$x \to 0^+$$, $$-\ln x \to +\infty$$ tạo một bức tường vô hình đẩy nghiệm giữ chặt trong phần trong $$x > 0$$.
2. **Giải chính xác điểm trên đường trung tâm (central path):**
   $$\phi_t'(x) = t - \frac{1}{x} = 0 \implies x^*(t) = \frac{1}{t}.$$
3. **Quan sát dãy điểm khi tăng tham số $$t$$:**
   - $$t = 1 \implies x^*(1) = 1.0$$ (sai số so với $$p^*$$ đúng bằng $$1$$).
   - $$t = 10 \implies x^*(10) = 0.1$$ (sai số $$0.1$$).
   - $$t = 1000 \implies x^*(1000) = 0.001$$ (sai số $$0.001$$).
   Ở mọi bước, sai số đối ngẫu luôn được kiểm soát chính xác bằng $$\frac{1}{t}$$ — chính cấu trúc rào chắn tự điều hòa (self-concordant) này đã giúp Nesterov và Nemirovski chứng minh tốc độ hội tụ đa thức tổng quát!

---

# Lịch sử phát triển của tối ưu hóa lồi

Tối ưu hóa lồi có quá trình phát triển lâu dài, đi từ những nền tảng hình học và giải tích thuần túy đến các ứng dụng rộng rãi trong kỹ thuật và khoa học dữ liệu hiện đại. Bài học này điểm lại các cột mốc chính theo từng giai đoạn.

## 🎯 Tổng quan dòng thời gian

<div class="timeline-container">
  <div class="timeline-item">
    <div class="timeline-year">1900-1970</div>
    <div class="timeline-content">Hình thành nền tảng lý thuyết</div>
  </div>
  <div class="timeline-item">
    <div class="timeline-year">1947-1990</div>
    <div class="timeline-content">Phát triển các thuật toán nền tảng</div>
  </div>
  <div class="timeline-item">
    <div class="timeline-year">1990-nay</div>
    <div class="timeline-content">Mở rộng mạnh mẽ sang các lĩnh vực ứng dụng</div>
  </div>
</div>

## 📚 Giai đoạn 1: Nền tảng lý thuyết (1900–1970)

### Những người đặt nền móng

**Hermann Minkowski (1864–1909)**
- Đặt nền móng cho hình học lồi với khái niệm tập lồi.
- Phát triển lý thuyết về đa diện lồi.
- Đóng góp chính: xây dựng ngôn ngữ hình học cơ bản cho tối ưu hóa lồi.

**Leonid Kantorovich (1912–1986)**
- Phát triển lý thuyết quy hoạch tuyến tính vào thập niên 1930.
- Giải quyết bài toán phân bổ tài nguyên tối ưu trong sản xuất.
- Đóng góp chính: chứng minh khả năng ứng dụng thực tế của tối ưu hóa trong kinh tế học.

**John von Neumann (1903–1957)**
- Xây dựng lý thuyết trò chơi và làm rõ mối liên hệ với tối ưu hóa.
- Chứng minh định lý minimax cơ bản.
- Đóng góp chính: kết nối tối ưu hóa với lý thuyết ra quyết định và tính đối ngẫu.

### Các khái niệm nền tảng được hình thành
- **Tập lồi và hàm lồi**: định nghĩa chặt chẽ và các tính chất cơ bản.
- **Điều kiện tối ưu**: hệ thống các điều kiện cần và đủ cho nghiệm tối ưu.
- **Lý thuyết đối ngẫu (Duality theory)**: xây dựng bài toán đối ngẫu và quan hệ giữa bài toán gốc và bài toán đối ngẫu.

## ⚙️ Giai đoạn 2: Bước tiến về thuật toán (1947–1990)

### 1947: Thuật toán đơn hình (Simplex)

**George Dantzig** đề xuất thuật toán đơn hình (Simplex):

```
Ý tưởng cốt lõi: Di chuyển dọc theo các cạnh của đa diện khả thi
để tìm điểm tối ưu tại một đỉnh.
```

**Vì sao cột mốc này quan trọng?**
- Là thuật toán thực tế đầu tiên giải hiệu quả các bài toán quy hoạch tuyến tính (LP).
- Mở ra hàng loạt ứng dụng trong hậu cần, sản xuất và quân sự.
- Đạt hiệu năng rất cao trong thực tế dù độ phức tạp trường hợp xấu nhất là hàm mũ.

### Thập niên 1960: Các phương pháp điểm trong ban đầu

**Fiacco & McCormick** phát triển:
- Phương pháp rào chắn (barrier methods) cho bài toán có ràng buộc bất đẳng thức.
- Ý tưởng: thêm hàm rào chắn để giữ nghiệm lặp nằm bên trong miền khả thi.

**Dikin** đóng góp:
- Phương pháp co giãn affine (affine scaling method), cải tiến hướng tiếp cận của các phương pháp điểm trong.

### Thập niên 1970: Phương pháp ellipsoid và dưới gradient

**Shor, Nemirovski và Yudin** phát triển:
- **Phương pháp ellipsoid**: đặt nền tảng cho thuật toán thời gian đa thức đầu tiên cho LP (được Khachiyan áp dụng năm 1979).
- **Phương pháp dưới gradient (subgradient)**: xử lý các hàm mục tiêu lồi không khả vi.

**Ý nghĩa lý thuyết:**
- Chứng minh bài toán LP thuộc lớp P (giải được trong thời gian đa thức).
- Mở rộng phạm vi giải sang lớp các bài toán tối ưu không trơn.

### 1984: Phương pháp điểm trong của Karmarkar

**Narendra Karmarkar** tạo ra bước ngoặt mới:
- Đề xuất thuật toán điểm trong có độ phức tạp thời gian đa thức \(O(n^{3.5}L)\).
- Cho hiệu năng thực tế tốt hơn thuật toán đơn hình trên nhiều bài toán quy mô lớn.
- Mở đầu cho giai đoạn phát triển mạnh của các phương pháp điểm trong hiện đại.

### Cuối thập niên 1980–1990: Tổng quát hóa

**Nesterov & Nemirovski (1994)** mở rộng lý thuyết điểm trong:
- Mở rộng phương pháp điểm trong sang tối ưu hóa lồi phi tuyến.
- Xây dựng lý thuyết hàm tự tương thích (self-concordant functions).
- Cung cấp thuật toán thời gian đa thức cho một lớp bài toán lồi tổng quát hơn nhiều.

## 🚀 Giai đoạn 3: Mở rộng ứng dụng (1990–nay)

### Trước năm 1990: Chủ yếu trong vận trù học (Operations Research)

**Các ứng dụng chính:**
- **Bài toán vận tải**: tối ưu hóa chi phí vận chuyển hàng hóa.
- **Lập kế hoạch sản xuất**: tối ưu hóa lịch trình và công suất.
- **Phân bổ tài nguyên**: phân bổ nguồn lực trong doanh nghiệp.
- **Hậu cần quân sự**: lập kế hoạch cung ứng trong Thế chiến II và thời kỳ Chiến tranh Lạnh.

**Nguyên nhân phạm vi còn hạn chế:**
- Năng lực tính toán của máy tính còn thấp.
- Thiếu các công cụ và thư viện phần mềm thuận tiện.
- Chưa được phổ biến rộng rãi trong các ngành kỹ thuật khác.

### Từ năm 1990 trở đi: Ứng dụng rộng rãi trong kỹ thuật

#### 🎛️ Hệ thống điều khiển (Control Systems)
- **Điều khiển dự báo theo mô hình (MPC)**: tính toán tín hiệu điều khiển tối ưu theo từng bước thời gian.
- **Điều khiển bền vững (Robust control)**: đảm bảo ổn định hệ thống trước nhiễu và bất định.
- **Ví dụ**: điều khiển nhiệt độ trong nhà máy, hệ thống lái tự động trên máy bay.

#### 📡 Xử lý tín hiệu (Signal Processing)
- **Cảm biến nén (Compressed sensing)**: khôi phục tín hiệu thưa từ số lượng mẫu đo ít.
- **Khử nhiễu ảnh (Image denoising)**: tách nhiễu mà vẫn giữ biên ảnh sắc nét.
- **Ví dụ**: tái tạo ảnh chụp cộng hưởng từ (MRI), xử lý tín hiệu radar.

#### 📱 Truyền thông (Communications)
- **Định dạng chùm sóng (Beamforming)**: điều hướng sóng trong mảng ăng-ten.
- **Phân bổ công suất (Power allocation)**: tối ưu công suất phát trong mạng không dây.
- **Ví dụ**: mạng di động 5G, truyền thông vệ tinh.

#### 💻 Thiết kế mạch (Circuit Design)
- **Định cỡ cổng (Gate sizing)**: tối ưu kích thước transistor để cân bằng tốc độ và diện tích.
- **Tối ưu công suất (Power optimization)**: giảm tiêu thụ năng lượng.
- **Ví dụ**: thiết kế bộ vi xử lý (CPU), tối ưu chip di động.

### 🆕 Các lớp bài toán mới

#### Quy hoạch nửa xác định (Semidefinite Programming — SDP)
```
Tối ưu hóa trên nón các ma trận nửa xác định dương.
Ứng dụng: Nới lỏng lồi cho các bài toán tổ hợp, lý thuyết điều khiển.
```

#### Quy hoạch nón bậc hai (Second-Order Cone Programming — SOCP)
```
Tối ưu hóa với ràng buộc thuộc nón bậc hai.
Ứng dụng: Tối ưu hóa bền vững, tối ưu hóa danh mục đầu tư.
```

#### Tối ưu hóa bền vững (Robust Optimization)
```
Tối ưu hóa khi dữ liệu hoặc tham số chứa tính bất định.
Ứng dụng: Tài chính định lượng, quản trị chuỗi cung ứng.
```

## 🔮 Xu hướng hiện tại và tương lai

### Tích hợp với học máy (Machine Learning)
- **Nới lỏng lồi (Convex relaxations)** cho các bài toán phân tích mạng nơ-ron.
- **Thuật toán tối ưu trong huấn luyện**: SGD, Adam, RMSprop.
- **Điều chuẩn (Regularization)**: các thành phần phạt $$L_1, L_2$$.

### Ứng dụng dữ liệu lớn (Big Data)
- **Tối ưu hóa phân tán (Distributed optimization)**: xử lý dữ liệu quy mô lớn trên nhiều nút tính toán.
- **Thuật toán trực tuyến (Online algorithms)**: cập nhật nghiệm liên tục theo luồng dữ liệu.
- **Tối ưu hóa theo luồng (Streaming optimization)**: tối ưu theo thời gian thực.

### Tính toán lượng tử (Quantum Computing)
- **Tối ưu hóa lồi lượng tử**: nghiên cứu các thuật toán lượng tử cho bài toán tối ưu.
- **Thuật toán lượng tử biến phân**: QAOA, VQE.

## 💡 Bài học từ lịch sử

1. **Lý thuyết dẫn đường cho thực hành**: nền tảng toán học chặt chẽ là cơ sở để thiết kế thuật toán đáng tin cậy.
2. **Phần cứng và phần mềm thúc đẩy ứng dụng**: năng lực tính toán tăng lên mở rộng mạnh mẽ phạm vi áp dụng.
3. **Hợp tác liên ngành**: sự giao thoa giữa toán học, khoa học máy tính và kỹ thuật tạo ra các hướng đi mới.
4. **Nhu cầu thực tiễn thúc đẩy đổi mới**: các bài toán thực tế luôn là động lực trực tiếp cho sự ra đời của thuật toán mới.

---

<div class="info-box">
<h4>🎯 Điểm cốt lõi cần ghi nhớ</h4>
<p>Tối ưu hóa lồi đã phát triển từ một nhánh toán học lý thuyết thành công cụ nền tảng trong nhiều ngành kỹ thuật và khoa học dữ liệu hiện đại. Sự kết hợp giữa lý thuyết chặt chẽ và thuật toán hiệu quả giúp giải quyết ổn định nhiều bài toán thực tiễn quy mô lớn.</p>
</div>

## 🎮 Minh họa tương tác

### Minh họa thuật toán đơn hình (Simplex)

<div id="simplex-demo">
  <h4>Minh họa thuật toán Simplex</h4>
  <p>Thử nghiệm với một bài toán quy hoạch tuyến tính hai biến:</p>
  
  <div class="problem-setup">
    <p><strong>Bài toán:</strong> Cực đại hóa \(c_1x_1 + c_2x_2\)</p>
    <p><strong>Với điều kiện:</strong> \(x_1, x_2 \geq 0\) và các ràng buộc tuyến tính</p>
    
    <div class="controls">
      <label>c₁: <input type="range" id="c1" min="-5" max="5" value="3" step="0.1"></label>
      <span id="c1-value">3</span><br>
      <label>c₂: <input type="range" id="c2" min="-5" max="5" value="2" step="0.1"></label>
      <span id="c2-value">2</span><br>
      <button onclick="runSimplex()">Chạy Simplex</button>
      <button onclick="resetDemo()">Đặt lại</button>
    </div>
  </div>
  
  <canvas id="simplex-canvas" width="400" height="300"></canvas>
  <div id="simplex-steps"></div>
</div>

### Khám phá dòng thời gian

<div id="timeline-explorer">
  <h4>Khám phá dòng thời gian tương tác</h4>
  <div class="year-slider">
    <label>Năm: <input type="range" id="year-slider" min="1900" max="2024" value="1947" step="1"></label>
    <span id="current-year">1947</span>
  </div>
  
  <div id="year-info">
    <h5 id="event-title">1947: Thuật toán Simplex</h5>
    <p id="event-description">George Dantzig phát triển thuật toán Simplex, mở đầu kỷ nguyên giải bài toán quy hoạch tuyến tính trong thực tế.</p>
    <div id="event-impact">
      <strong>Tác động:</strong> <span id="impact-text">Thay đổi căn bản lĩnh vực vận trù học</span>
    </div>
  </div>
</div>

### Ứng dụng hiện đại

<div id="applications-demo">
  <h4>Một số ứng dụng thực tế</h4>
  <div class="app-selector">
    <button onclick="showApplication('portfolio')" class="app-btn">Tối ưu danh mục</button>
    <button onclick="showApplication('supply-chain')" class="app-btn">Chuỗi cung ứng</button>
    <button onclick="showApplication('machine-learning')" class="app-btn">Học máy</button>
    <button onclick="showApplication('signal-processing')" class="app-btn">Xử lý tín hiệu</button>
  </div>
  
  <div id="app-content">
    <div class="app-example" id="portfolio">
      <h5>📈 Tối ưu hóa danh mục đầu tư</h5>
      <p><strong>Bài toán:</strong> Phân bổ vốn đầu tư nhằm cực đại hóa lợi suất kỳ vọng và cực tiểu hóa rủi ro</p>
      <p><strong>Công thức:</strong> \(\min rac{1}{2}w^T\Sigma w - \mu^T w\)</p>
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