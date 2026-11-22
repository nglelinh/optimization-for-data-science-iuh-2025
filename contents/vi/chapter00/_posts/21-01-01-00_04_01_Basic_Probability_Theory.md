---
layout: post
title: 00-04-01 Lý Thuyết Xác Suất Cơ Bản
chapter: '00'
order: 15
owner: AI Assistant
categories:
- chapter00
lang: vi
lesson_type: required
---

## Lý thuyết xác suất cơ bản

Lý thuyết xác suất cung cấp khung toán học chặt chẽ để phân tích tính bất định — nền tảng của nhiều bài toán tối ưu hóa trong học máy và khoa học dữ liệu.

### 1. Không gian mẫu và biến cố

**Không gian mẫu (Ω)**: tập hợp tất cả các kết quả có thể xảy ra của một phép thử ngẫu nhiên.

**Biến cố (A)**: một tập con của không gian mẫu, biểu diễn một nhóm kết quả cụ thể.

**Ví dụ:**
- Tung đồng xu: Ω = {S, N}
- Tung xúc xắc: Ω = {1, 2, 3, 4, 5, 6}
- Trường hợp liên tục: Ω = [0, 1] đối với biến ngẫu nhiên có phân phối đều trên [0, 1]

<div id="sample-space-demo" style="border: 2px solid #ddd; padding: 20px; margin: 20px 0; border-radius: 10px; background-color: #f9f9f9;">
    <h4 style="text-align: center; color: #333;">Trực quan hóa không gian mẫu tương tác</h4>
    
    <div style="display: flex; flex-wrap: wrap; gap: 20px; align-items: flex-start;">
        <div style="flex: 1; min-width: 400px;">
            <canvas id="sampleSpaceCanvas" width="400" height="300" style="border: 1px solid #ccc; background: white;"></canvas>
            <p style="font-size: 12px; color: #666; margin-top: 5px;">
                <strong>Trực quan hóa:</strong> Nhấp để tạo mẫu ngẫu nhiên. Các màu khác nhau biểu diễn các biến cố khác nhau.
            </p>
        </div>
        
        <div style="flex: 1; min-width: 250px;">
            <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h5 style="margin-top: 0; color: #444;">Loại phép thử</h5>
                
                <div style="margin-bottom: 15px;">
                    <label style="display: block; margin-bottom: 10px;">
                        <input type="radio" name="experiment" value="coin" checked> Tung đồng xu
                    </label>
                    <label style="display: block; margin-bottom: 10px;">
                        <input type="radio" name="experiment" value="dice"> Tung xúc xắc
                    </label>
                    <label style="display: block; margin-bottom: 10px;">
                        <input type="radio" name="experiment" value="uniform"> Phân phối đều [0,1]
                    </label>
                </div>
                
                <button id="generate-sample" style="width: 100%; padding: 10px; background: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; margin-bottom: 10px;">Tạo mẫu</button>
                <button id="clear-samples" style="width: 100%; padding: 8px; background: #6c757d; color: white; border: none; border-radius: 5px; cursor: pointer; margin-bottom: 15px;">Xóa</button>
                
                <div id="sample-stats" style="font-family: monospace; font-size: 12px; line-height: 1.4; background: #f8f9fa; padding: 10px; border-radius: 4px;">
                    <div><strong>Thống kê:</strong></div>
                    <div>Tổng mẫu: <span id="total-samples">0</span></div>
                    <div>Biến cố A: <span id="event-a-count">0</span></div>
                    <div>Biến cố B: <span id="event-b-count">0</span></div>
                    <div>P(A) ≈ <span id="prob-a">0.000</span></div>
                    <div>P(B) ≈ <span id="prob-b">0.000</span></div>
                </div>
            </div>
        </div>
    </div>
</div>

### 2. Tiên đề xác suất (Tiên đề Kolmogorov)

Mọi độ đo xác suất P đều phải thỏa mãn ba tiên đề sau:

#### Tiên đề 1: Tính không âm
$$P(A) \geq 0 	ext{ với mọi biến cố } A$$

#### Tiên đề 2: Chuẩn hóa
$$P(\Omega) = 1$$

#### Tiên đề 3: Tính cộng đếm được
Với mọi dãy biến cố đôi một xung khắc $$A_1, A_2, \ldots$$:
$$P\left(igcup_{i=1}^{\infty} A_iight) = \sum_{i=1}^{\infty} P(A_i)$$

### 3. Tính chất và quy tắc cơ bản

#### Quy tắc phần bù
$$P(A^c) = 1 - P(A)$$

#### Quy tắc cộng
Với hai biến cố A và B bất kỳ:
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

#### Quy tắc nhân
$$P(A \cap B) = P(A|B) \cdot P(B) = P(B|A) \cdot P(A)$$

### 4. Xác suất có điều kiện

Xác suất của biến cố A khi biết biến cố B đã xảy ra:

$$P(A|B) = rac{P(A \cap B)}{P(B)}, \quad P(B) > 0$$

**Diễn giải**: Xác suất có điều kiện cập nhật mức độ tin cậy về A khi ta có thêm thông tin rằng B đã xảy ra.

<div id="conditional-prob-demo" style="border: 2px solid #ddd; padding: 20px; margin: 20px 0; border-radius: 10px; background-color: #f9f9f9;">
    <h4 style="text-align: center; color: #333;">Trực quan hóa xác suất có điều kiện</h4>
    
    <div style="display: flex; flex-wrap: wrap; gap: 20px; align-items: flex-start;">
        <div style="flex: 1; min-width: 400px;">
            <canvas id="conditionalCanvas" width="400" height="300" style="border: 1px solid #ccc; background: white;"></canvas>
            <p style="font-size: 12px; color: #666; margin-top: 5px;">
                <strong>Biểu đồ Venn:</strong> Hình tròn xanh là biến cố A, hình tròn đỏ là biến cố B. Phần giao màu tím biểu diễn A ∩ B.
            </p>
        </div>
        
        <div style="flex: 1; min-width: 250px;">
            <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h5 style="margin-top: 0; color: #444;">Điều chỉnh xác suất</h5>
                
                <div style="margin-bottom: 15px;">
                    <label for="prob-a-slider" style="display: block; margin-bottom: 5px; font-weight: bold;">P(A): <span id="prob-a-value">0.4</span></label>
                    <input type="range" id="prob-a-slider" min="0.1" max="0.9" step="0.05" value="0.4" style="width: 100%;">
                </div>
                
                <div style="margin-bottom: 15px;">
                    <label for="prob-b-slider" style="display: block; margin-bottom: 5px; font-weight: bold;">P(B): <span id="prob-b-value">0.5</span></label>
                    <input type="range" id="prob-b-slider" min="0.1" max="0.9" step="0.05" value="0.5" style="width: 100%;">
                </div>
                
                <div style="margin-bottom: 15px;">
                    <label for="overlap-slider" style="display: block; margin-bottom: 5px; font-weight: bold;">Giao: <span id="overlap-value">0.2</span></label>
                    <input type="range" id="overlap-slider" min="0" max="0.4" step="0.05" value="0.2" style="width: 100%;">
                </div>
                
                <div id="conditional-results" style="font-family: monospace; font-size: 12px; line-height: 1.4; background: #f8f9fa; padding: 10px; border-radius: 4px;">
                    <div><strong>Xác suất:</strong></div>
                    <div>P(A) = <span id="display-prob-a">0.400</span></div>
                    <div>P(B) = <span id="display-prob-b">0.500</span></div>
                    <div>P(A ∩ B) = <span id="display-prob-ab">0.200</span></div>
                    <div>P(A ∪ B) = <span id="display-prob-union">0.700</span></div>
                    <div><strong>Xác suất có điều kiện:</strong></div>
                    <div>P(A|B) = <span id="display-prob-a-given-b">0.400</span></div>
                    <div>P(B|A) = <span id="display-prob-b-given-a">0.500</span></div>
                </div>
            </div>
        </div>
    </div>
</div>

### 5. Tính độc lập

Hai biến cố A và B được gọi là **độc lập** nếu:
$$P(A \cap B) = P(A) \cdot P(B)$$

Tương đương (khi các xác suất khác 0):
$$P(A|B) = P(A) \quad 	ext{và} \quad P(B|A) = P(B)$$

**Diễn giải**: Thông tin về việc một biến cố đã xảy ra không làm thay đổi xác suất của biến cố còn lại.

### 6. Biến ngẫu nhiên

**Biến ngẫu nhiên** X là một hàm ánh xạ mỗi kết quả trong không gian mẫu thành một số thực:
$$X: \Omega ightarrow \mathbb{R}$$

#### Các loại biến ngẫu nhiên

**Rời rạc**: nhận các giá trị đếm được (ví dụ: số lần xuất hiện mặt sấp).
- Hàm khối xác suất (PMF): $$P(X = x)$$

**Liên tục**: nhận các giá trị trên một khoảng số thực (ví dụ: chiều cao, cân nặng).
- Hàm mật độ xác suất (PDF): $$f_X(x)$$
- $$P(a \leq X \leq b) = \int_a^b f_X(x) dx$$

### 7. Kết nối với tối ưu hóa

Lý thuyết xác suất gắn liền với tối ưu hóa qua nhiều bài toán điển hình:

#### Ước lượng hợp lý tối đa
Tìm tham số θ để cực đại hóa hàm hợp lý (likelihood):
$$\hat{	heta} = rg\max_	heta P(	ext{dữ liệu}|	heta)$$

#### Tối ưu hóa giá trị kỳ vọng
Cực tiểu hóa giá trị kỳ vọng của hàm mất mát:
$$\min_	heta \mathbb{E}[L(Y, f(X; 	heta))]$$

#### Tối ưu hóa Bayes
Sử dụng phân phối xác suất để mô hình hóa tính bất định của hàm mục tiêu và định hướng tìm kiếm nghiệm tối ưu.

<div id="optimization-connection" style="border: 2px solid #ddd; padding: 20px; margin: 20px 0; border-radius: 10px; background-color: #f0f8ff;">
    <h4 style="text-align: center; color: #333;">Ví dụ xác suất trong tối ưu hóa</h4>
    
    <div style="display: flex; flex-wrap: wrap; gap: 20px; align-items: flex-start;">
        <div style="flex: 1; min-width: 400px;">
            <canvas id="optimizationCanvas" width="400" height="300" style="border: 1px solid #ccc; background: white;"></canvas>
            <p style="font-size: 12px; color: #666; margin-top: 5px;">
                <strong>Ví dụ MLE:</strong> Tìm tham số μ để cực đại hóa hàm hợp lý của dữ liệu quan sát từ phân phối Normal(μ, 1).
            </p>
        </div>
        
        <div style="flex: 1; min-width: 250px;">
            <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h5 style="margin-top: 0; color: #444;">Minh họa MLE</h5>
                
                <div style="margin-bottom: 15px;">
                    <label for="true-mu-slider" style="display: block; margin-bottom: 5px; font-weight: bold;">μ thực: <span id="true-mu-value">2.0</span></label>
                    <input type="range" id="true-mu-slider" min="-2" max="4" step="0.1" value="2.0" style="width: 100%;">
                </div>
                
                <div style="margin-bottom: 15px;">
                    <label for="sample-size-slider" style="display: block; margin-bottom: 5px; font-weight: bold;">Kích thước mẫu: <span id="sample-size-value">20</span></label>
                    <input type="range" id="sample-size-slider" min="5" max="100" step="5" value="20" style="width: 100%;">
                </div>
                
                <button id="generate-mle-data" style="width: 100%; padding: 10px; background: #28a745; color: white; border: none; border-radius: 5px; cursor: pointer; margin-bottom: 15px;">Tạo dữ liệu & tìm MLE</button>
                
                <div id="mle-results" style="font-family: monospace; font-size: 12px; line-height: 1.4; background: #f8f9fa; padding: 10px; border-radius: 4px;">
                    <div><strong>Kết quả:</strong></div>
                    <div>μ thực: <span id="display-true-mu">2.000</span></div>
                    <div>Trung bình mẫu: <span id="sample-mean">--</span></div>
                    <div>Ước lượng MLE: <span id="mle-estimate">--</span></div>
                    <div>Sai số: <span id="mle-error">--</span></div>
                </div>
            </div>
        </div>
    </div>
</div>

### Những điểm chính

1. **Nền tảng**: các tiên đề xác suất cung cấp cơ sở toán học để lập luận về tính bất định.
2. **Xác suất có điều kiện**: công cụ cốt lõi để cập nhật niềm tin khi có thông tin mới.
3. **Tính độc lập**: giúp đơn giản hóa tính toán và xây dựng các giả định mô hình.
4. **Biến ngẫu nhiên**: cầu nối giữa không gian xác suất trừu tượng và các đại lượng đo lường cụ thể.
5. **Kết nối với tối ưu hóa**: nhiều bài toán tối ưu hóa bắt nguồn trực tiếp từ mô hình hóa xác suất.

Nắm vững những khái niệm cơ bản này giúp bạn sẵn sàng tiếp cận các chủ đề chuyên sâu hơn như suy luận Bayes, ước lượng hợp lý tối đa và tối ưu hóa ngẫu nhiên — những trụ cột của học máy và khoa học dữ liệu hiện đại.

<script>
// Sample Space Visualization
class SampleSpaceDemo {
    constructor() {
        this.canvas = document.getElementById('sampleSpaceCanvas');
        this.ctx = this.canvas.getContext('2d');
        this.width = this.canvas.width;
        this.height = this.canvas.height;
        
        this.samples = [];
        this.experimentType = 'coin';
        
        this.setupControls();
        this.draw();
    }
    
    setupControls() {
        const radios = document.querySelectorAll('input[name="experiment"]');
        const generateBtn = document.getElementById('generate-sample');
        const clearBtn = document.getElementById('clear-samples');
        
        radios.forEach(radio => {
            radio.addEventListener('change', (e) => {
                this.experimentType = e.target.value;
                this.samples = [];
                this.updateStats();
                this.draw();
            });
        });
        
        generateBtn.addEventListener('click', () => this.generateSample());
        clearBtn.addEventListener('click', () => {
            this.samples = [];
            this.updateStats();
            this.draw();
        });
        
        this.canvas.addEventListener('click', () => this.generateSample());
    }
    
    generateSample() {
        let sample;
        
        switch(this.experimentType) {
            case 'coin':
                sample = {
                    value: Math.random() < 0.5 ? 'S' : 'N',
                    x: Math.random() * (this.width - 40) + 20,
                    y: Math.random() * (this.height - 40) + 20,
                    eventA: Math.random() < 0.5, // Biến cố A: Sấp
                    eventB: Math.random() < 0.3  // Biến cố B: May mắn
                };
                break;
            case 'dice':
                const diceValue = Math.floor(Math.random() * 6) + 1;
                sample = {
                    value: diceValue,
                    x: Math.random() * (this.width - 40) + 20,
                    y: Math.random() * (this.height - 40) + 20,
                    eventA: diceValue >= 4, // Biến cố A: 4, 5, hoặc 6
                    eventB: diceValue % 2 === 0 // Biến cố B: Chẵn
                };
                break;
            case 'uniform':
                const uniformValue = Math.random();
                sample = {
                    value: uniformValue.toFixed(3),
                    x: uniformValue * (this.width - 40) + 20,
                    y: Math.random() * (this.height - 40) + 20,
                    eventA: uniformValue > 0.5, // Biến cố A: > 0.5
                    eventB: uniformValue < 0.7  // Biến cố B: < 0.7
                };
                break;
        }
        
        this.samples.push(sample);
        this.updateStats();
        this.draw();
    }
    
    updateStats() {
        const total = this.samples.length;
        const eventACount = this.samples.filter(s => s.eventA).length;
        const eventBCount = this.samples.filter(s => s.eventB).length;
        
        document.getElementById('total-samples').textContent = total;
        document.getElementById('event-a-count').textContent = eventACount;
        document.getElementById('event-b-count').textContent = eventBCount;
        document.getElementById('prob-a').textContent = total > 0 ? (eventACount / total).toFixed(3) : '0.000';
        document.getElementById('prob-b').textContent = total > 0 ? (eventBCount / total).toFixed(3) : '0.000';
    }
    
    draw() {
        this.ctx.clearRect(0, 0, this.width, this.height);
        
        // Draw background
        this.ctx.fillStyle = '#f8f9fa';
        this.ctx.fillRect(0, 0, this.width, this.height);
        
        // Draw samples
        this.samples.forEach(sample => {
            // Determine color based on events
            let color = '#666';
            if (sample.eventA && sample.eventB) color = '#9c27b0'; // Cả hai biến cố
            else if (sample.eventA) color = '#2196f3'; // Chỉ biến cố A
            else if (sample.eventB) color = '#f44336'; // Chỉ biến cố B
            
            this.ctx.fillStyle = color;
            this.ctx.beginPath();
            this.ctx.arc(sample.x, sample.y, 5, 0, 2 * Math.PI);
            this.ctx.fill();
            
            // Draw value
            this.ctx.fillStyle = '#000';
            this.ctx.font = '10px Arial';
            this.ctx.textAlign = 'center';
            this.ctx.fillText(sample.value, sample.x, sample.y - 8);
        });
        
        // Draw legend
        this.ctx.fillStyle = '#000';
        this.ctx.font = '12px Arial';
        this.ctx.textAlign = 'left';
        this.ctx.fillText('Chú thích:', 10, 20);
        
        this.ctx.fillStyle = '#2196f3';
        this.ctx.beginPath();
        this.ctx.arc(20, 35, 4, 0, 2 * Math.PI);
        this.ctx.fill();
        this.ctx.fillStyle = '#000';
        this.ctx.fillText('Chỉ biến cố A', 30, 38);
        
        this.ctx.fillStyle = '#f44336';
        this.ctx.beginPath();
        this.ctx.arc(20, 50, 4, 0, 2 * Math.PI);
        this.ctx.fill();
        this.ctx.fillStyle = '#000';
        this.ctx.fillText('Chỉ biến cố B', 30, 53);
        
        this.ctx.fillStyle = '#9c27b0';
        this.ctx.beginPath();
        this.ctx.arc(20, 65, 4, 0, 2 * Math.PI);
        this.ctx.fill();
        this.ctx.fillStyle = '#000';
        this.ctx.fillText('Cả A và B', 30, 68);
    }
}

// Conditional Probability Visualization
class ConditionalProbDemo {
    constructor() {
        this.canvas = document.getElementById('conditionalCanvas');
        this.ctx = this.canvas.getContext('2d');
        this.width = this.canvas.width;
        this.height = this.canvas.height;
        
        this.probA = 0.4;
        this.probB = 0.5;
        this.overlap = 0.2;
        
        this.setupControls();
        this.draw();
    }
    
    setupControls() {
        const probASlider = document.getElementById('prob-a-slider');
        const probBSlider = document.getElementById('prob-b-slider');
        const overlapSlider = document.getElementById('overlap-slider');
        
        probASlider.addEventListener('input', (e) => {
            this.probA = parseFloat(e.target.value);
            document.getElementById('prob-a-value').textContent = this.probA.toFixed(1);
            this.updateCalculations();
            this.draw();
        });
        
        probBSlider.addEventListener('input', (e) => {
            this.probB = parseFloat(e.target.value);
            document.getElementById('prob-b-value').textContent = this.probB.toFixed(1);
            this.updateCalculations();
            this.draw();
        });
        
        overlapSlider.addEventListener('input', (e) => {
            this.overlap = parseFloat(e.target.value);
            document.getElementById('overlap-value').textContent = this.overlap.toFixed(1);
            // Ensure overlap doesn't exceed min(probA, probB)
            const maxOverlap = Math.min(this.probA, this.probB);
            if (this.overlap > maxOverlap) {
                this.overlap = maxOverlap;
                overlapSlider.value = this.overlap;
                document.getElementById('overlap-value').textContent = this.overlap.toFixed(1);
            }
            this.updateCalculations();
            this.draw();
        });
        
        this.updateCalculations();
    }
    
    updateCalculations() {
        const probUnion = this.probA + this.probB - this.overlap;
        const probAGivenB = this.probB > 0 ? this.overlap / this.probB : 0;
        const probBGivenA = this.probA > 0 ? this.overlap / this.probA : 0;
        
        document.getElementById('display-prob-a').textContent = this.probA.toFixed(3);
        document.getElementById('display-prob-b').textContent = this.probB.toFixed(3);
        document.getElementById('display-prob-ab').textContent = this.overlap.toFixed(3);
        document.getElementById('display-prob-union').textContent = probUnion.toFixed(3);
        document.getElementById('display-prob-a-given-b').textContent = probAGivenB.toFixed(3);
        document.getElementById('display-prob-b-given-a').textContent = probBGivenA.toFixed(3);
    }
    
    draw() {
        this.ctx.clearRect(0, 0, this.width, this.height);
        
        // Draw universe rectangle
        this.ctx.strokeStyle = '#000';
        this.ctx.lineWidth = 2;
        this.ctx.strokeRect(50, 50, 300, 200);
        this.ctx.fillStyle = '#000';
        this.ctx.font = '14px Arial';
        this.ctx.fillText('Ω (Không gian mẫu)', 55, 45);
        
        // Calculate circle parameters
        const centerAX = 150;
        const centerAY = 150;
        const centerBX = 250;
        const centerBY = 150;
        
        // Calculate radii based on probabilities (area proportional to probability)
        const radiusA = Math.sqrt(this.probA * 10000 / Math.PI);
        const radiusB = Math.sqrt(this.probB * 10000 / Math.PI);
        
        // Draw circle A
        this.ctx.globalAlpha = 0.3;
        this.ctx.fillStyle = '#2196f3';
        this.ctx.beginPath();
        this.ctx.arc(centerAX, centerAY, radiusA, 0, 2 * Math.PI);
        this.ctx.fill();
        
        // Draw circle B
        this.ctx.fillStyle = '#f44336';
        this.ctx.beginPath();
        this.ctx.arc(centerBX, centerBY, radiusB, 0, 2 * Math.PI);
        this.ctx.fill();
        
        // Draw intersection (approximate)
        if (this.overlap > 0) {
            this.ctx.fillStyle = '#9c27b0';
            const overlapRadius = Math.sqrt(this.overlap * 5000 / Math.PI);
            this.ctx.beginPath();
            this.ctx.arc((centerAX + centerBX) / 2, (centerAY + centerBY) / 2, overlapRadius, 0, 2 * Math.PI);
            this.ctx.fill();
        }
        
        this.ctx.globalAlpha = 1.0;
        
        // Draw circle outlines
        this.ctx.strokeStyle = '#2196f3';
        this.ctx.lineWidth = 2;
        this.ctx.beginPath();
        this.ctx.arc(centerAX, centerAY, radiusA, 0, 2 * Math.PI);
        this.ctx.stroke();
        
        this.ctx.strokeStyle = '#f44336';
        this.ctx.beginPath();
        this.ctx.arc(centerBX, centerBY, radiusB, 0, 2 * Math.PI);
        this.ctx.stroke();
        
        // Labels
        this.ctx.fillStyle = '#000';
        this.ctx.font = '16px Arial';
        this.ctx.fillText('A', centerAX - 40, centerAY);
        this.ctx.fillText('B', centerBX + 30, centerBY);
        
        if (this.overlap > 0) {
            this.ctx.fillText('A∩B', (centerAX + centerBX) / 2 - 15, (centerAY + centerBY) / 2 + 5);
        }
    }
}

// MLE Optimization Demo
class MLEDemo {
    constructor() {
        this.canvas = document.getElementById('optimizationCanvas');
        this.ctx = this.canvas.getContext('2d');
        this.width = this.canvas.width;
        this.height = this.canvas.height;
        
        this.trueMu = 2.0;
        this.sampleSize = 20;
        this.data = [];
        
        this.setupControls();
        this.draw();
    }
    
    setupControls() {
        const trueMuSlider = document.getElementById('true-mu-slider');
        const sampleSizeSlider = document.getElementById('sample-size-slider');
        const generateBtn = document.getElementById('generate-mle-data');
        
        trueMuSlider.addEventListener('input', (e) => {
            this.trueMu = parseFloat(e.target.value);
            document.getElementById('true-mu-value').textContent = this.trueMu.toFixed(1);
            document.getElementById('display-true-mu').textContent = this.trueMu.toFixed(3);
        });
        
        sampleSizeSlider.addEventListener('input', (e) => {
            this.sampleSize = parseInt(e.target.value);
            document.getElementById('sample-size-value').textContent = this.sampleSize;
        });
        
        generateBtn.addEventListener('click', () => this.generateDataAndFindMLE());
    }
    
    generateDataAndFindMLE() {
        // Generate data from Normal(trueMu, 1)
        this.data = [];
        for (let i = 0; i < this.sampleSize; i++) {
            // Box-Muller transform for normal distribution
            const u1 = Math.random();
            const u2 = Math.random();
            const z = Math.sqrt(-2 * Math.log(u1)) * Math.cos(2 * Math.PI * u2);
            this.data.push(this.trueMu + z); // Normal(trueMu, 1)
        }
        
        // Calculate MLE (sample mean for normal distribution)
        const sampleMean = this.data.reduce((sum, x) => sum + x, 0) / this.data.length;
        const error = Math.abs(sampleMean - this.trueMu);
        
        // Update display
        document.getElementById('sample-mean').textContent = sampleMean.toFixed(3);
        document.getElementById('mle-estimate').textContent = sampleMean.toFixed(3);
        document.getElementById('mle-error').textContent = error.toFixed(3);
        
        this.draw();
    }
    
    draw() {
        this.ctx.clearRect(0, 0, this.width, this.height);
        
        if (this.data.length === 0) {
            this.ctx.fillStyle = '#666';
            this.ctx.font = '16px Arial';
            this.ctx.textAlign = 'center';
            this.ctx.fillText('Nhấp "Tạo Dữ Liệu & Tìm MLE" để bắt đầu', this.width / 2, this.height / 2);
            return;
        }
        
        // Draw axes
        this.ctx.strokeStyle = '#ddd';
        this.ctx.lineWidth = 1;
        const marginX = 50;
        const marginY = 50;
        const plotWidth = this.width - 2 * marginX;
        const plotHeight = this.height - 2 * marginY;
        
        // X-axis
        this.ctx.beginPath();
        this.ctx.moveTo(marginX, this.height - marginY);
        this.ctx.lineTo(this.width - marginX, this.height - marginY);
        this.ctx.stroke();
        
        // Y-axis
        this.ctx.beginPath();
        this.ctx.moveTo(marginX, marginY);
        this.ctx.lineTo(marginX, this.height - marginY);
        this.ctx.stroke();
        
        // Find data range
        const minX = Math.min(...this.data) - 1;
        const maxX = Math.max(...this.data) + 1;
        
        // Draw likelihood function
        this.ctx.strokeStyle = '#2196f3';
        this.ctx.lineWidth = 2;
        this.ctx.beginPath();
        
        for (let i = 0; i <= 100; i++) {
            const mu = minX + (maxX - minX) * i / 100;
            let logLikelihood = 0;
            
            // Calculate log-likelihood
            for (const x of this.data) {
                logLikelihood -= 0.5 * Math.log(2 * Math.PI);
                logLikelihood -= 0.5 * (x - mu) * (x - mu);
            }
            
            const x = marginX + (mu - minX) / (maxX - minX) * plotWidth;
            const y = this.height - marginY - (logLikelihood - (-this.data.length * 2)) / (this.data.length) * plotHeight * 0.8;
            
            if (i === 0) {
                this.ctx.moveTo(x, y);
            } else {
                this.ctx.lineTo(x, y);
            }
        }
        this.ctx.stroke();
        
        // Mark MLE
        const sampleMean = this.data.reduce((sum, x) => sum + x, 0) / this.data.length;
        const mleX = marginX + (sampleMean - minX) / (maxX - minX) * plotWidth;
        
        this.ctx.strokeStyle = '#f44336';
        this.ctx.lineWidth = 2;
        this.ctx.beginPath();
        this.ctx.moveTo(mleX, marginY);
        this.ctx.lineTo(mleX, this.height - marginY);
        this.ctx.stroke();
        
        // Mark true value
        const trueX = marginX + (this.trueMu - minX) / (maxX - minX) * plotWidth;
        this.ctx.strokeStyle = '#4caf50';
        this.ctx.lineWidth = 2;
        this.ctx.setLineDash([5, 5]);
        this.ctx.beginPath();
        this.ctx.moveTo(trueX, marginY);
        this.ctx.lineTo(trueX, this.height - marginY);
        this.ctx.stroke();
        this.ctx.setLineDash([]);
        
        // Draw data points
        this.ctx.fillStyle = '#666';
        for (const x of this.data) {
            const pointX = marginX + (x - minX) / (maxX - minX) * plotWidth;
            this.ctx.beginPath();
            this.ctx.arc(pointX, this.height - marginY + 10, 2, 0, 2 * Math.PI);
            this.ctx.fill();
        }
        
        // Labels
        this.ctx.fillStyle = '#000';
        this.ctx.font = '12px Arial';
        this.ctx.textAlign = 'center';
        this.ctx.fillText('μ', this.width / 2, this.height - 10);
        
        this.ctx.save();
        this.ctx.translate(15, this.height / 2);
        this.ctx.rotate(-Math.PI / 2);
        this.ctx.fillText('Log-Likelihood', 0, 0);
        this.ctx.restore();
        
        // Legend
        this.ctx.textAlign = 'left';
        this.ctx.fillText('— Likelihood', 10, 20);
        this.ctx.fillStyle = '#f44336';
        this.ctx.fillText('— MLE', 10, 35);
        this.ctx.fillStyle = '#4caf50';
        this.ctx.fillText('--- μ Thực', 10, 50);
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    new SampleSpaceDemo();
    new ConditionalProbDemo();
    new MLEDemo();
});
</script>

<style>
input[type="range"] {
    -webkit-appearance: none;
    appearance: none;
    height: 5px;
    background: #ddd;
    outline: none;
    border-radius: 5px;
}

input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 15px;
    height: 15px;
    background: #007bff;
    cursor: pointer;
    border-radius: 50%;
}

input[type="range"]::-moz-range-thumb {
    width: 15px;
    height: 15px;
    background: #007bff;
    cursor: pointer;
    border-radius: 50%;
    border: none;
}

canvas {
    border-radius: 5px;
}

.demo-container {
    margin: 20px 0;
}
</style>
