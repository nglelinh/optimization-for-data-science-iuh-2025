---
layout: post
title: 00-04-02 Các Phân Phối Xác Suất Thông Dụng
chapter: '00'
order: 16
owner: AI Assistant
categories:
- chapter00
lang: vi
lesson_type: required
---

Một trong những bất ngờ thú vị nhất khi học tối ưu hóa cho khoa học dữ liệu là phát hiện ra: các hàm mất mát nổi tiếng nhất không phải do ai đó "bịa" ra ngẫu nhiên, mà mỗi hàm đều là hình bóng logarit của một **phân phối xác suất** cổ điển! Phân phối Gauss sinh ra hồi quy bình phương tối thiểu, phân phối Bernoulli sinh ra hồi quy logistic, phân phối Laplace sinh ra hồi quy chuẩn $$\ell_1$$, còn phân phối chuẩn đa biến gắn liền trực tiếp với ma trận xác định dương.

Bài học này giúp bạn không chỉ nhớ công thức các phân phối rời rạc và liên tục thông dụng, mà còn thấy ngay cấu trúc lồi ẩn sau log-mật độ của chúng.

## Kiến thức cần nhớ: Họ phân phối và hàm mất mát tương ứng

- **Phân phối rời rạc (Bernoulli, Nhị thức, Poisson, Categorical):** Mô hình hóa dữ liệu đếm và phân loại nhãn. Âm log-hợp lý của Bernoulli/Categorical chính là hàm mất mát **Binary/Multi-class Cross-Entropy** — một hàm lồi đẹp theo tham số tuyến tính.
- **Phân phối liên tục một biến (Đều, Mũ, Chuẩn Gauss, Laplace):** Phân phối Gauss có đuôi giảm theo $$e^{-x^2}$$ (tạo phạt bình phương nhạy với ngoại lai), còn Laplace có đuôi giảm theo $$e^{-|x|}$$ (tạo phạt $$\ell_1$$ bền vững và khuyến khích độ thưa).
- **Phân phối chuẩn đa biến ($$\mathcal{N}(\mu, \Sigma)$$):** Mở rộng Gauss lên $$\mathbb{R}^n$$ với mật độ tỉ lệ với $$\exp\left(-\frac{1}{2}(x-\mu)^T \Sigma^{-1}(x-\mu)\right)$$. Đường đồng mức của mật độ chính là các **ellipsoid** — đối tượng lồi quen thuộc của Chương 02.
- **Tính log-lõm (Log-concavity):** Hầu hết các phân phối kinh điển (Gauss, Mũ, Laplace, Gamma với $$\alpha \ge 1$$) đều có log-mật độ là hàm lõm, nhờ đó bài toán ước lượng tham số tự động trở thành **bài toán tối ưu hóa lồi**!

### Giải thích: So sánh âm log-hợp lý Gauss và Laplace trên cùng bộ dữ liệu

Cho $$3$$ quan sát độc lập $$x_1 = 1,\ x_2 = 2,\ x_3 = 6$$. Ta muốn ước lượng tâm vị trí $$\mu$$ dưới hai giả thiết nhiễu khác nhau:

1. **Giả thiết nhiễu chuẩn $$\mathcal{N}(\mu, 1)$$:**
   Hàm mật độ $$p(x_i \mid \mu) = \frac{1}{\sqrt{2\pi}}\exp\left(-\frac{(x_i - \mu)^2}{2}\right)$$. Lấy tổng âm log-hợp lý (bỏ hằng số):
   $$\text{NLL}_{\text{Gauss}}(\mu) = \frac{1}{2}\left[(1-\mu)^2 + (2-\mu)^2 + (6-\mu)^2\right].$$
   Đạo hàm bằng $$0$$: $$-(1-\mu) - (2-\mu) - (6-\mu) = 0 \implies 3\mu = 9 \implies \hat\mu_{\text{Gauss}} = 3$$.
2. **Giả thiết nhiễu Laplace $$\operatorname{Laplace}(\mu, 1)$$:**
   Hàm mật độ $$p(x_i \mid \mu) = \frac{1}{2}\exp(-|x_i - \mu|)$$. Lấy tổng âm log-hợp lý (bỏ hằng số):
   $$\text{NLL}_{\text{Laplace}}(\mu) = |1-\mu| + |2-\mu| + |6-\mu|.$$
   Kiểm tra giá trị:
   - Tại $$\mu = 2$$: $$|1-2| + |2-2| + |6-2| = 1 + 0 + 4 = 5$$.
   - Tại $$\mu = 3$$: $$|1-3| + |2-3| + |6-3| = 2 + 1 + 3 = 6 > 5$$.
   Vậy $$\hat\mu_{\text{Laplace}} = 2$$ (trung vị). Chỉ cần đổi giả thiết phân phối nhiễu, bài toán tối ưu lập tức đổi từ chuẩn $$\ell_2$$ sang chuẩn $$\ell_1$$!

---

## Các phân phối xác suất thông dụng

Hiểu rõ các phân phối xác suất cốt lõi là yêu cầu thiết yếu đối với nhiều bài toán tối ưu hóa trong học máy và thống kê. Các phân phối này thường đóng vai trò là giả định phân phối dữ liệu, phân phối tiên nghiệm (prior) trong suy luận Bayes hoặc mô hình nhiễu trong hồi quy.

### 1. Phân phối rời rạc

#### Phân phối Bernoulli

Mô hình hóa một phép thử đơn với hai kết quả có thể xảy ra (thành công hoặc thất bại).

**Tham số**: $$p \in [0,1]$$ (xác suất thành công)

**PMF**: $$P(X = k) = p^k (1-p)^{1-k}$$ với $$k \in \{0,1\}$$

**Kỳ vọng**: $$\mathbb{E}[X] = p$$

**Phương sai**: $$	ext{Var}(X) = p(1-p)$$

**Ứng dụng**: phân loại nhị phân, tung đồng xu, kiểm định A/B.

#### Phân phối nhị thức

Mô hình hóa số lần thành công trong $$n$$ phép thử Bernoulli độc lập có cùng xác suất thành công.

**Tham số**: $$n \in \mathbb{N}$$ (số phép thử), $$p \in [0,1]$$ (xác suất thành công)

**PMF**: $$P(X = k) = inom{n}{k} p^k (1-p)^{n-k}$$ với $$k = 0,1,\ldots,n$$

**Kỳ vọng**: $$\mathbb{E}[X] = np$$

**Phương sai**: $$	ext{Var}(X) = np(1-p)$$

#### Phân phối Poisson

Mô hình hóa số sự kiện xảy ra trong một khoảng thời gian (hoặc không gian) cố định khi các sự kiện diễn ra độc lập với tốc độ trung bình không đổi.

**Tham số**: $$\lambda > 0$$ (tốc độ trung bình)

**PMF**: $$P(X = k) = rac{\lambda^k e^{-\lambda}}{k!}$$ với $$k = 0,1,2,\ldots$$

**Kỳ vọng**: $$\mathbb{E}[X] = \lambda$$

**Phương sai**: $$	ext{Var}(X) = \lambda$$

**Ứng dụng**: dữ liệu đếm, sự kiện hiếm, lý thuyết hàng đợi.

<div id="discrete-distributions-demo" style="border: 2px solid #ddd; padding: 20px; margin: 20px 0; border-radius: 10px; background-color: #f9f9f9;">
    <h4 style="text-align: center; color: #333;">Phân phối rời rạc tương tác</h4>
    
    <div style="display: flex; flex-wrap: wrap; gap: 20px; align-items: flex-start;">
        <div style="flex: 1; min-width: 400px;">
            <canvas id="discreteCanvas" width="400" height="300" style="border: 1px solid #ccc; background: white;"></canvas>
            <p style="font-size: 12px; color: #666; margin-top: 5px;">
                <strong>Trực quan hóa:</strong> Hàm khối xác suất của các phân phối rời rạc.
            </p>
        </div>
        
        <div style="flex: 1; min-width: 250px;">
            <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h5 style="margin-top: 0; color: #444;">Loại phân phối</h5>
                
                <div style="margin-bottom: 15px;">
                    <label style="display: block; margin-bottom: 10px;">
                        <input type="radio" name="discrete-dist" value="bernoulli" checked> Bernoulli
                    </label>
                    <label style="display: block; margin-bottom: 10px;">
                        <input type="radio" name="discrete-dist" value="binomial"> Nhị thức
                    </label>
                    <label style="display: block; margin-bottom: 10px;">
                        <input type="radio" name="discrete-dist" value="poisson"> Poisson
                    </label>
                </div>
                
                <div id="discrete-params">
                    <div id="p-param" style="margin-bottom: 15px;">
                        <label for="p-slider" style="display: block; margin-bottom: 5px; font-weight: bold;">p: <span id="p-value">0.5</span></label>
                        <input type="range" id="p-slider" min="0.1" max="0.9" step="0.05" value="0.5" style="width: 100%;">
                    </div>
                    
                    <div id="n-param" style="margin-bottom: 15px; display: none;">
                        <label for="n-slider" style="display: block; margin-bottom: 5px; font-weight: bold;">n: <span id="n-value">10</span></label>
                        <input type="range" id="n-slider" min="5" max="50" step="1" value="10" style="width: 100%;">
                    </div>
                    
                    <div id="lambda-param" style="margin-bottom: 15px; display: none;">
                        <label for="lambda-slider" style="display: block; margin-bottom: 5px; font-weight: bold;">λ: <span id="lambda-value">3.0</span></label>
                        <input type="range" id="lambda-slider" min="0.5" max="10" step="0.5" value="3.0" style="width: 100%;">
                    </div>
                </div>
                
                <div id="discrete-stats" style="font-family: monospace; font-size: 12px; line-height: 1.4; background: #f8f9fa; padding: 10px; border-radius: 4px;">
                    <div><strong>Thống kê:</strong></div>
                    <div>Kỳ vọng: <span id="discrete-mean">0.500</span></div>
                    <div>Phương sai: <span id="discrete-variance">0.250</span></div>
                    <div>Mode: <span id="discrete-mode">0 hoặc 1</span></div>
                </div>
            </div>
        </div>
    </div>
</div>

### 2. Phân phối liên tục

#### Phân phối đều

Mọi giá trị trong một đoạn cho trước đều có mật độ xác suất như nhau.

**Tham số**: $$a, b \in \mathbb{R}$$ với $$a < b$$

**PDF**: $$f(x) = rac{1}{b-a}$$ với $$x \in [a,b]$$, và bằng $$0$$ ở ngoài đoạn này

**Kỳ vọng**: $$\mathbb{E}[X] = rac{a+b}{2}$$

**Phương sai**: $$	ext{Var}(X) = rac{(b-a)^2}{12}$$

**Ứng dụng**: lấy mẫu ngẫu nhiên, khởi tạo tham số trong thuật toán.

#### Phân phối chuẩn (Gaussian)

Phân phối có vai trò trung tâm trong thống kê và tối ưu hóa.

**Tham số**: $$\mu \in \mathbb{R}$$ (kỳ vọng), $$\sigma^2 > 0$$ (phương sai)

**PDF**: $$f(x) = rac{1}{\sqrt{2\pi\sigma^2}} \exp\left(-rac{(x-\mu)^2}{2\sigma^2}
ight)$$

**Kỳ vọng**: $$\mathbb{E}[X] = \mu$$

**Phương sai**: $$	ext{Var}(X) = \sigma^2$$

**Tính chất**:
- Đối xứng quanh $$\mu$$.
- Quy tắc 68–95–99.7.
- Gắn với định lý giới hạn trung tâm.
- Đạt entropy cực đại trong số các phân phối trên $$\mathbb{R}$$ có cùng kỳ vọng và phương sai cho trước.

#### Phân phối mũ

Mô hình hóa thời gian chờ giữa hai sự kiện liên tiếp trong một quá trình Poisson.

**Tham số**: $$\lambda > 0$$ (tham số tốc độ)

**PDF**: $$f(x) = \lambda e^{-\lambda x}$$ với $$x \geq 0$$

**Kỳ vọng**: $$\mathbb{E}[X] = rac{1}{\lambda}$$

**Phương sai**: $$	ext{Var}(X) = rac{1}{\lambda^2}$$

**Tính chất**: tính không nhớ (memoryless).

#### Phân phối Beta

Phân phối liên tục linh hoạt trên đoạn $$[0,1]$$, thường dùng để mô hình hóa xác suất hoặc tỷ lệ.

**Tham số**: $$lpha, eta > 0$$ (các tham số hình dạng)

**PDF**: $$f(x) = rac{\Gamma(lpha+eta)}{\Gamma(lpha)\Gamma(eta)} x^{lpha-1}(1-x)^{eta-1}$$ với $$x \in [0,1]$$

**Kỳ vọng**: $$\mathbb{E}[X] = rac{lpha}{lpha+eta}$$

**Phương sai**: $$	ext{Var}(X) = rac{lphaeta}{(lpha+eta)^2(lpha+eta+1)}$$

<div id="continuous-distributions-demo" style="border: 2px solid #ddd; padding: 20px; margin: 20px 0; border-radius: 10px; background-color: #f9f9f9;">
    <h4 style="text-align: center; color: #333;">Phân phối liên tục tương tác</h4>
    
    <div style="display: flex; flex-wrap: wrap; gap: 20px; align-items: flex-start;">
        <div style="flex: 1; min-width: 400px;">
            <canvas id="continuousCanvas" width="400" height="300" style="border: 1px solid #ccc; background: white;"></canvas>
            <p style="font-size: 12px; color: #666; margin-top: 5px;">
                <strong>Trực quan hóa:</strong> Hàm mật độ xác suất của các phân phối liên tục.
            </p>
        </div>
        
        <div style="flex: 1; min-width: 250px;">
            <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h5 style="margin-top: 0; color: #444;">Loại phân phối</h5>
                
                <div style="margin-bottom: 15px;">
                    <label style="display: block; margin-bottom: 10px;">
                        <input type="radio" name="continuous-dist" value="uniform" checked> Đều
                    </label>
                    <label style="display: block; margin-bottom: 10px;">
                        <input type="radio" name="continuous-dist" value="normal"> Chuẩn
                    </label>
                    <label style="display: block; margin-bottom: 10px;">
                        <input type="radio" name="continuous-dist" value="exponential"> Mũ
                    </label>
                    <label style="display: block; margin-bottom: 10px;">
                        <input type="radio" name="continuous-dist" value="beta"> Beta
                    </label>
                </div>
                
                <div id="continuous-params">
                    <div id="uniform-params">
                        <div style="margin-bottom: 15px;">
                            <label for="a-slider" style="display: block; margin-bottom: 5px; font-weight: bold;">a: <span id="a-value">0</span></label>
                            <input type="range" id="a-slider" min="-2" max="2" step="0.1" value="0" style="width: 100%;">
                        </div>
                        <div style="margin-bottom: 15px;">
                            <label for="b-slider" style="display: block; margin-bottom: 5px; font-weight: bold;">b: <span id="b-value">1</span></label>
                            <input type="range" id="b-slider" min="0.5" max="4" step="0.1" value="1" style="width: 100%;">
                        </div>
                    </div>
                    
                    <div id="normal-params" style="display: none;">
                        <div style="margin-bottom: 15px;">
                            <label for="mu-slider" style="display: block; margin-bottom: 5px; font-weight: bold;">μ: <span id="mu-value">0</span></label>
                            <input type="range" id="mu-slider" min="-3" max="3" step="0.1" value="0" style="width: 100%;">
                        </div>
                        <div style="margin-bottom: 15px;">
                            <label for="sigma-slider" style="display: block; margin-bottom: 5px; font-weight: bold;">σ: <span id="sigma-value">1.0</span></label>
                            <input type="range" id="sigma-slider" min="0.5" max="3" step="0.1" value="1.0" style="width: 100%;">
                        </div>
                    </div>
                    
                    <div id="exponential-params" style="display: none;">
                        <div style="margin-bottom: 15px;">
                            <label for="exp-lambda-slider" style="display: block; margin-bottom: 5px; font-weight: bold;">λ: <span id="exp-lambda-value">1.0</span></label>
                            <input type="range" id="exp-lambda-slider" min="0.2" max="3" step="0.1" value="1.0" style="width: 100%;">
                        </div>
                    </div>
                    
                    <div id="beta-params" style="display: none;">
                        <div style="margin-bottom: 15px;">
                            <label for="alpha-slider" style="display: block; margin-bottom: 5px; font-weight: bold;">α: <span id="alpha-value">2</span></label>
                            <input type="range" id="alpha-slider" min="0.5" max="5" step="0.1" value="2" style="width: 100%;">
                        </div>
                        <div style="margin-bottom: 15px;">
                            <label for="beta-slider" style="display: block; margin-bottom: 5px; font-weight: bold;">β: <span id="beta-value">2</span></label>
                            <input type="range" id="beta-slider" min="0.5" max="5" step="0.1" value="2" style="width: 100%;">
                        </div>
                    </div>
                </div>
                
                <div id="continuous-stats" style="font-family: monospace; font-size: 12px; line-height: 1.4; background: #f8f9fa; padding: 10px; border-radius: 4px;">
                    <div><strong>Thống kê:</strong></div>
                    <div>Kỳ vọng: <span id="continuous-mean">0.500</span></div>
                    <div>Phương sai: <span id="continuous-variance">0.083</span></div>
                    <div>Miền xác định: <span id="continuous-support">[0, 1]</span></div>
                </div>
            </div>
        </div>
    </div>
</div>

### 3. Phân phối đa biến

#### Phân phối chuẩn đa biến

Tổng quát hóa phân phối chuẩn sang không gian nhiều chiều.

**Tham số**: $$oldsymbol{\mu} \in \mathbb{R}^d$$ (vector kỳ vọng), $$oldsymbol{\Sigma} \in \mathbb{R}^{d 	imes d}$$ (ma trận hiệp phương sai đối xứng xác định dương)

**PDF**: $$f(\mathbf{x}) = rac{1}{(2\pi)^{d/2}|oldsymbol{\Sigma}|^{1/2}} \exp\left(-rac{1}{2}(\mathbf{x}-oldsymbol{\mu})^Toldsymbol{\Sigma}^{-1}(\mathbf{x}-oldsymbol{\mu})
ight)$$

**Tính chất**:
- Các phân phối biên đều là phân phối chuẩn.
- Tổ hợp tuyến tính của các thành phần tuân theo phân phối chuẩn.
- Các phân phối có điều kiện đều là phân phối chuẩn.

<div id="multivariate-demo" style="border: 2px solid #ddd; padding: 20px; margin: 20px 0; border-radius: 10px; background-color: #f0f8ff;">
    <h4 style="text-align: center; color: #333;">Phân phối chuẩn đa biến</h4>
    
    <div style="display: flex; flex-wrap: wrap; gap: 20px; align-items: flex-start;">
        <div style="flex: 1; min-width: 400px;">
            <canvas id="multivariateCanvas" width="400" height="300" style="border: 1px solid #ccc; background: white;"></canvas>
            <p style="font-size: 12px; color: #666; margin-top: 5px;">
                <strong>Trực quan 2D:</strong> Đồ thị đường mức của phân phối chuẩn hai biến. Các điểm mẫu được hiển thị dưới dạng chấm.
            </p>
        </div>
        
        <div style="flex: 1; min-width: 250px;">
            <div style="background: white; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h5 style="margin-top: 0; color: #444;">Tham số</h5>
                
                <div style="margin-bottom: 15px;">
                    <label for="mu1-slider" style="display: block; margin-bottom: 5px; font-weight: bold;">μ₁: <span id="mu1-value">0.0</span></label>
                    <input type="range" id="mu1-slider" min="-2" max="2" step="0.1" value="0" style="width: 100%;">
                </div>
                
                <div style="margin-bottom: 15px;">
                    <label for="mu2-slider" style="display: block; margin-bottom: 5px; font-weight: bold;">μ₂: <span id="mu2-value">0.0</span></label>
                    <input type="range" id="mu2-slider" min="-2" max="2" step="0.1" value="0" style="width: 100%;">
                </div>
                
                <div style="margin-bottom: 15px;">
                    <label for="sigma1-slider" style="display: block; margin-bottom: 5px; font-weight: bold;">σ₁: <span id="sigma1-value">1.0</span></label>
                    <input type="range" id="sigma1-slider" min="0.5" max="2" step="0.1" value="1.0" style="width: 100%;">
                </div>
                
                <div style="margin-bottom: 15px;">
                    <label for="sigma2-slider" style="display: block; margin-bottom: 5px; font-weight: bold;">σ₂: <span id="sigma2-value">1.0</span></label>
                    <input type="range" id="sigma2-slider" min="0.5" max="2" step="0.1" value="1.0" style="width: 100%;">
                </div>
                
                <div style="margin-bottom: 15px;">
                    <label for="rho-slider" style="display: block; margin-bottom: 5px; font-weight: bold;">ρ (tương quan): <span id="rho-value">0.0</span></label>
                    <input type="range" id="rho-slider" min="-0.9" max="0.9" step="0.1" value="0" style="width: 100%;">
                </div>
                
                <button id="generate-samples" style="width: 100%; padding: 10px; background: #28a745; color: white; border: none; border-radius: 5px; cursor: pointer; margin-bottom: 15px;">Tạo mẫu</button>
                
                <div id="multivariate-stats" style="font-family: monospace; font-size: 12px; line-height: 1.4; background: #f8f9fa; padding: 10px; border-radius: 4px;">
                    <div><strong>Ma trận hiệp phương sai:</strong></div>
                    <div>Σ₁₁: <span id="cov11">1.000</span></div>
                    <div>Σ₁₂: <span id="cov12">0.000</span></div>
                    <div>Σ₂₂: <span id="cov22">1.000</span></div>
                    <div>Det(Σ): <span id="det-cov">1.000</span></div>
                </div>
            </div>
        </div>
    </div>
</div>

### 4. Ứng dụng trong tối ưu hóa

#### Ước lượng hợp lý tối đa
Nhiều bài toán tối ưu hóa tìm bộ tham số làm cực đại hàm hợp lý của dữ liệu quan sát dưới một phân phối giả định:

$$\hat{	heta} = rg\max_	heta \prod_{i=1}^n f(x_i; 	heta)$$

#### Tối ưu hóa Bayes
Phân phối tiên nghiệm (prior) mã hóa tri thức ban đầu về tham số trước khi quan sát dữ liệu:

$$p(	heta|dữ\ liệu) \propto p(dữ\ liệu|	heta) \cdot p(	heta)$$

#### Điều chuẩn (Regularization)
Các phân phối tiên nghiệm tương ứng trực tiếp với các thành phần điều chuẩn trong tối ưu hóa:
- Điều chuẩn $$L_2$$ ↔ phân phối tiên nghiệm Gaussian.
- Điều chuẩn $$L_1$$ ↔ phân phối tiên nghiệm Laplace.

#### Tối ưu hóa ngẫu nhiên
Các phân phối xác suất được dùng để mô hình hóa nhiễu và tính bất định trong hàm mục tiêu cũng như ràng buộc.

### Những điểm quan trọng cho tối ưu hóa

1. **Lựa chọn mô hình**: chọn phân phối phù hợp với bản chất dữ liệu.
2. **Ước lượng tham số**: dùng MLE hoặc phương pháp Bayes để ước lượng tham số phân phối.
3. **Định lượng tính bất định**: phân phối xác suất cho cách biểu diễn tự nhiên đối với sai số và độ không chắc chắn.
4. **Điều chuẩn**: phân phối tiên nghiệm giúp hạn chế quá khớp (overfitting).
5. **Hiệu quả tính toán**: nhiều phân phối kinh điển có công thức nghiệm dạng đóng cho các phép toán thống kê thông dụng.

Hiểu rõ các phân phối này cùng tính chất của chúng là nền tảng để xây dựng và giải các bài toán tối ưu hóa trong học máy, thống kê và kỹ thuật.

<script>
// Discrete Distributions Demo
class DiscreteDistributionsDemo {
    constructor() {
        this.canvas = document.getElementById('discreteCanvas');
        this.ctx = this.canvas.getContext('2d');
        this.width = this.canvas.width;
        this.height = this.canvas.height;
        
        this.distType = 'bernoulli';
        this.params = { p: 0.5, n: 10, lambda: 3.0 };
        
        this.setupControls();
        this.draw();
    }
    
    setupControls() {
        const radios = document.querySelectorAll('input[name="discrete-dist"]');
        const pSlider = document.getElementById('p-slider');
        const nSlider = document.getElementById('n-slider');
        const lambdaSlider = document.getElementById('lambda-slider');
        
        radios.forEach(radio => {
            radio.addEventListener('change', (e) => {
                this.distType = e.target.value;
                this.updateParameterVisibility();
                this.updateStats();
                this.draw();
            });
        });
        
        pSlider.addEventListener('input', (e) => {
            this.params.p = parseFloat(e.target.value);
            document.getElementById('p-value').textContent = this.params.p.toFixed(1);
            this.updateStats();
            this.draw();
        });
        
        nSlider.addEventListener('input', (e) => {
            this.params.n = parseInt(e.target.value);
            document.getElementById('n-value').textContent = this.params.n;
            this.updateStats();
            this.draw();
        });
        
        lambdaSlider.addEventListener('input', (e) => {
            this.params.lambda = parseFloat(e.target.value);
            document.getElementById('lambda-value').textContent = this.params.lambda.toFixed(1);
            this.updateStats();
            this.draw();
        });
        
        this.updateParameterVisibility();
        this.updateStats();
    }
    
    updateParameterVisibility() {
        document.getElementById('p-param').style.display = 
            (this.distType === 'bernoulli' || this.distType === 'binomial') ? 'block' : 'none';
        document.getElementById('n-param').style.display = 
            this.distType === 'binomial' ? 'block' : 'none';
        document.getElementById('lambda-param').style.display = 
            this.distType === 'poisson' ? 'block' : 'none';
    }
    
    updateStats() {
        let mean, variance, mode;
        
        switch(this.distType) {
            case 'bernoulli':
                mean = this.params.p;
                variance = this.params.p * (1 - this.params.p);
                mode = this.params.p > 0.5 ? '1' : (this.params.p < 0.5 ? '0' : '0 hoặc 1');
                break;
            case 'binomial':
                mean = this.params.n * this.params.p;
                variance = this.params.n * this.params.p * (1 - this.params.p);
                mode = Math.floor((this.params.n + 1) * this.params.p).toString();
                break;
            case 'poisson':
                mean = this.params.lambda;
                variance = this.params.lambda;
                mode = Math.floor(this.params.lambda).toString();
                break;
        }
        
        document.getElementById('discrete-mean').textContent = mean.toFixed(3);
        document.getElementById('discrete-variance').textContent = variance.toFixed(3);
        document.getElementById('discrete-mode').textContent = mode;
    }
    
    factorial(n) {
        if (n <= 1) return 1;
        return n * this.factorial(n - 1);
    }
    
    binomialCoeff(n, k) {
        if (k > n) return 0;
        return this.factorial(n) / (this.factorial(k) * this.factorial(n - k));
    }
    
    getProbability(k) {
        switch(this.distType) {
            case 'bernoulli':
                return k === 0 ? (1 - this.params.p) : (k === 1 ? this.params.p : 0);
            case 'binomial':
                if (k < 0 || k > this.params.n) return 0;
                return this.binomialCoeff(this.params.n, k) * 
                       Math.pow(this.params.p, k) * 
                       Math.pow(1 - this.params.p, this.params.n - k);
            case 'poisson':
                if (k < 0) return 0;
                return Math.pow(this.params.lambda, k) * Math.exp(-this.params.lambda) / this.factorial(k);
        }
    }
    
    draw() {
        this.ctx.clearRect(0, 0, this.width, this.height);
        
        const marginX = 50;
        const marginY = 50;
        const plotWidth = this.width - 2 * marginX;
        const plotHeight = this.height - 2 * marginY;
        
        // Draw axes
        this.ctx.strokeStyle = '#ddd';
        this.ctx.lineWidth = 1;
        this.ctx.beginPath();
        this.ctx.moveTo(marginX, this.height - marginY);
        this.ctx.lineTo(this.width - marginX, this.height - marginY);
        this.ctx.moveTo(marginX, marginY);
        this.ctx.lineTo(marginX, this.height - marginY);
        this.ctx.stroke();
        
        // Determine range
        let maxK;
        switch(this.distType) {
            case 'bernoulli': maxK = 1; break;
            case 'binomial': maxK = this.params.n; break;
            case 'poisson': maxK = Math.min(20, this.params.lambda + 3 * Math.sqrt(this.params.lambda)); break;
        }
        
        // Find max probability for scaling
        let maxProb = 0;
        for (let k = 0; k <= maxK; k++) {
            maxProb = Math.max(maxProb, this.getProbability(k));
        }
        
        // Draw bars
        this.ctx.fillStyle = '#2196f3';
        const barWidth = plotWidth / (maxK + 2);
        
        for (let k = 0; k <= maxK; k++) {
            const prob = this.getProbability(k);
            const x = marginX + (k + 0.5) * barWidth;
            const height = (prob / maxProb) * plotHeight * 0.8;
            const y = this.height - marginY - height;
            
            this.ctx.fillRect(x - barWidth * 0.3, y, barWidth * 0.6, height);
            
            // Label
            this.ctx.fillStyle = '#000';
            this.ctx.font = '10px Arial';
            this.ctx.textAlign = 'center';
            this.ctx.fillText(k.toString(), x, this.height - marginY + 15);
            this.ctx.fillText(prob.toFixed(3), x, y - 5);
            this.ctx.fillStyle = '#2196f3';
        }
        
        // Labels
        this.ctx.fillStyle = '#000';
        this.ctx.font = '12px Arial';
        this.ctx.textAlign = 'center';
        this.ctx.fillText('k', this.width / 2, this.height - 10);
        
        this.ctx.save();
        this.ctx.translate(15, this.height / 2);
        this.ctx.rotate(-Math.PI / 2);
        this.ctx.fillText('P(X = k)', 0, 0);
        this.ctx.restore();
    }
}

// Continuous Distributions Demo
class ContinuousDistributionsDemo {
    constructor() {
        this.canvas = document.getElementById('continuousCanvas');
        this.ctx = this.canvas.getContext('2d');
        this.width = this.canvas.width;
        this.height = this.canvas.height;
        
        this.distType = 'uniform';
        this.params = { a: 0, b: 1, mu: 0, sigma: 1, lambda: 1, alpha: 2, beta: 2 };
        
        this.setupControls();
        this.draw();
    }
    
    setupControls() {
        const radios = document.querySelectorAll('input[name="continuous-dist"]');
        
        radios.forEach(radio => {
            radio.addEventListener('change', (e) => {
                this.distType = e.target.value;
                this.updateParameterVisibility();
                this.updateStats();
                this.draw();
            });
        });
        
        // Setup all sliders
        const sliders = ['a', 'b', 'mu', 'sigma', 'exp-lambda', 'alpha', 'beta'];
        sliders.forEach(slider => {
            const element = document.getElementById(slider + '-slider');
            if (element) {
                element.addEventListener('input', (e) => {
                    const value = parseFloat(e.target.value);
                    const param = slider === 'exp-lambda' ? 'lambda' : slider;
                    this.params[param] = value;
                    
                    const valueSpan = document.getElementById(slider + '-value');
                    if (valueSpan) {
                        valueSpan.textContent = value.toFixed(1);
                    }
                    
                    this.updateStats();
                    this.draw();
                });
            }
        });
        
        this.updateParameterVisibility();
        this.updateStats();
    }
    
    updateParameterVisibility() {
        document.getElementById('uniform-params').style.display = 
            this.distType === 'uniform' ? 'block' : 'none';
        document.getElementById('normal-params').style.display = 
            this.distType === 'normal' ? 'block' : 'none';
        document.getElementById('exponential-params').style.display = 
            this.distType === 'exponential' ? 'block' : 'none';
        document.getElementById('beta-params').style.display = 
            this.distType === 'beta' ? 'block' : 'none';
    }
    
    updateStats() {
        let mean, variance, support;
        
        switch(this.distType) {
            case 'uniform':
                mean = (this.params.a + this.params.b) / 2;
                variance = Math.pow(this.params.b - this.params.a, 2) / 12;
                support = `[${this.params.a}, ${this.params.b}]`;
                break;
            case 'normal':
                mean = this.params.mu;
                variance = this.params.sigma * this.params.sigma;
                support = '(-∞, ∞)';
                break;
            case 'exponential':
                mean = 1 / this.params.lambda;
                variance = 1 / (this.params.lambda * this.params.lambda);
                support = '[0, ∞)';
                break;
            case 'beta':
                mean = this.params.alpha / (this.params.alpha + this.params.beta);
                variance = (this.params.alpha * this.params.beta) / 
                          (Math.pow(this.params.alpha + this.params.beta, 2) * 
                           (this.params.alpha + this.params.beta + 1));
                support = '[0, 1]';
                break;
        }
        
        document.getElementById('continuous-mean').textContent = mean.toFixed(3);
        document.getElementById('continuous-variance').textContent = variance.toFixed(3);
        document.getElementById('continuous-support').textContent = support;
    }
    
    gamma(z) {
        // Stirling's approximation for gamma function
        if (z < 0.5) return Math.PI / (Math.sin(Math.PI * z) * this.gamma(1 - z));
        z -= 1;
        let x = 0.99999999999980993;
        const p = [676.5203681218851, -1259.1392167224028, 771.32342877765313,
                  -176.61502916214059, 12.507343278686905, -0.13857109526572012,
                  9.9843695780195716e-6, 1.5056327351493116e-7];
        for (let i = 0; i < p.length; i++) {
            x += p[i] / (z + i + 1);
        }
        const t = z + p.length - 0.5;
        return Math.sqrt(2 * Math.PI) * Math.pow(t, z + 0.5) * Math.exp(-t) * x;
    }
    
    getPDF(x) {
        switch(this.distType) {
            case 'uniform':
                return (x >= this.params.a && x <= this.params.b) ? 
                       1 / (this.params.b - this.params.a) : 0;
            case 'normal':
                return Math.exp(-0.5 * Math.pow((x - this.params.mu) / this.params.sigma, 2)) / 
                       (this.params.sigma * Math.sqrt(2 * Math.PI));
            case 'exponential':
                return x >= 0 ? this.params.lambda * Math.exp(-this.params.lambda * x) : 0;
            case 'beta':
                if (x < 0 || x > 1) return 0;
                const B = this.gamma(this.params.alpha) * this.gamma(this.params.beta) / 
                         this.gamma(this.params.alpha + this.params.beta);
                return Math.pow(x, this.params.alpha - 1) * Math.pow(1 - x, this.params.beta - 1) / B;
        }
    }
    
    getRange() {
        switch(this.distType) {
            case 'uniform': return [this.params.a - 0.5, this.params.b + 0.5];
            case 'normal': return [this.params.mu - 4 * this.params.sigma, this.params.mu + 4 * this.params.sigma];
            case 'exponential': return [0, 5 / this.params.lambda];
            case 'beta': return [0, 1];
        }
    }
    
    draw() {
        this.ctx.clearRect(0, 0, this.width, this.height);
        
        const marginX = 50;
        const marginY = 50;
        const plotWidth = this.width - 2 * marginX;
        const plotHeight = this.height - 2 * marginY;
        
        // Draw axes
        this.ctx.strokeStyle = '#ddd';
        this.ctx.lineWidth = 1;
        this.ctx.beginPath();
        this.ctx.moveTo(marginX, this.height - marginY);
        this.ctx.lineTo(this.width - marginX, this.height - marginY);
        this.ctx.moveTo(marginX, marginY);
        this.ctx.lineTo(marginX, this.height - marginY);
        this.ctx.stroke();
        
        const [minX, maxX] = this.getRange();
        
        // Find max PDF for scaling
        let maxPDF = 0;
        for (let i = 0; i <= 200; i++) {
            const x = minX + (maxX - minX) * i / 200;
            maxPDF = Math.max(maxPDF, this.getPDF(x));
        }
        
        // Draw PDF curve
        this.ctx.strokeStyle = '#2196f3';
        this.ctx.lineWidth = 2;
        this.ctx.beginPath();
        
        for (let i = 0; i <= 200; i++) {
            const x = minX + (maxX - minX) * i / 200;
            const pdf = this.getPDF(x);
            const plotX = marginX + (x - minX) / (maxX - minX) * plotWidth;
            const plotY = this.height - marginY - (pdf / maxPDF) * plotHeight * 0.8;
            
            if (i === 0) {
                this.ctx.moveTo(plotX, plotY);
            } else {
                this.ctx.lineTo(plotX, plotY);
            }
        }
        this.ctx.stroke();
        
        // Labels
        this.ctx.fillStyle = '#000';
        this.ctx.font = '12px Arial';
        this.ctx.textAlign = 'center';
        this.ctx.fillText('x', this.width / 2, this.height - 10);
        
        this.ctx.save();
        this.ctx.translate(15, this.height / 2);
        this.ctx.rotate(-Math.PI / 2);
        this.ctx.fillText('f(x)', 0, 0);
        this.ctx.restore();
    }
}

// Multivariate Normal Demo
class MultivariateDemo {
    constructor() {
        this.canvas = document.getElementById('multivariateCanvas');
        this.ctx = this.canvas.getContext('2d');
        this.width = this.canvas.width;
        this.height = this.canvas.height;
        
        this.params = { mu1: 0, mu2: 0, sigma1: 1, sigma2: 1, rho: 0 };
        this.samples = [];
        
        this.setupControls();
        this.draw();
    }
    
    setupControls() {
        const sliders = ['mu1', 'mu2', 'sigma1', 'sigma2', 'rho'];
        
        sliders.forEach(slider => {
            const element = document.getElementById(slider + '-slider');
            element.addEventListener('input', (e) => {
                this.params[slider] = parseFloat(e.target.value);
                document.getElementById(slider + '-value').textContent = this.params[slider].toFixed(1);
                this.updateStats();
                this.draw();
            });
        });
        
        document.getElementById('generate-samples').addEventListener('click', () => {
            this.generateSamples();
            this.draw();
        });
        
        this.updateStats();
    }
    
    updateStats() {
        const cov11 = this.params.sigma1 * this.params.sigma1;
        const cov12 = this.params.rho * this.params.sigma1 * this.params.sigma2;
        const cov22 = this.params.sigma2 * this.params.sigma2;
        const det = cov11 * cov22 - cov12 * cov12;
        
        document.getElementById('cov11').textContent = cov11.toFixed(3);
        document.getElementById('cov12').textContent = cov12.toFixed(3);
        document.getElementById('cov22').textContent = cov22.toFixed(3);
        document.getElementById('det-cov').textContent = det.toFixed(3);
    }
    
    generateSamples() {
        this.samples = [];
        const n = 100;
        
        for (let i = 0; i < n; i++) {
            // Box-Muller transform
            const u1 = Math.random();
            const u2 = Math.random();
            const z1 = Math.sqrt(-2 * Math.log(u1)) * Math.cos(2 * Math.PI * u2);
            const z2 = Math.sqrt(-2 * Math.log(u1)) * Math.sin(2 * Math.PI * u2);
            
            // Transform to correlated normal
            const x1 = this.params.mu1 + this.params.sigma1 * z1;
            const x2 = this.params.mu2 + this.params.sigma2 * (this.params.rho * z1 + Math.sqrt(1 - this.params.rho * this.params.rho) * z2);
            
            this.samples.push([x1, x2]);
        }
    }
    
    draw() {
        this.ctx.clearRect(0, 0, this.width, this.height);
        
        const marginX = 50;
        const marginY = 50;
        const plotWidth = this.width - 2 * marginX;
        const plotHeight = this.height - 2 * marginY;
        
        // Draw axes
        this.ctx.strokeStyle = '#ddd';
        this.ctx.lineWidth = 1;
        this.ctx.beginPath();
        this.ctx.moveTo(marginX, this.height - marginY);
        this.ctx.lineTo(this.width - marginX, this.height - marginY);
        this.ctx.moveTo(marginX, marginY);
        this.ctx.lineTo(marginX, this.height - marginY);
        this.ctx.stroke();
        
        // Draw contour ellipses
        const levels = [0.5, 1, 1.5, 2];
        const colors = ['#ff9999', '#ff6666', '#ff3333', '#ff0000'];
        
        levels.forEach((level, idx) => {
            this.ctx.strokeStyle = colors[idx];
            this.ctx.lineWidth = 1;
            this.ctx.beginPath();
            
            const a = level * this.params.sigma1;
            const b = level * this.params.sigma2;
            const angle = 0.5 * Math.atan2(2 * this.params.rho * this.params.sigma1 * this.params.sigma2,
                                          this.params.sigma1 * this.params.sigma1 - this.params.sigma2 * this.params.sigma2);
            
            for (let i = 0; i <= 100; i++) {
                const t = 2 * Math.PI * i / 100;
                const x = a * Math.cos(t) * Math.cos(angle) - b * Math.sin(t) * Math.sin(angle) + this.params.mu1;
                const y = a * Math.cos(t) * Math.sin(angle) + b * Math.sin(t) * Math.cos(angle) + this.params.mu2;
                
                const plotX = marginX + (x + 4) / 8 * plotWidth;
                const plotY = this.height - marginY - (y + 4) / 8 * plotHeight;
                
                if (i === 0) {
                    this.ctx.moveTo(plotX, plotY);
                } else {
                    this.ctx.lineTo(plotX, plotY);
                }
            }
            this.ctx.stroke();
        });
        
        // Draw samples
        if (this.samples.length > 0) {
            this.ctx.fillStyle = '#2196f3';
            this.samples.forEach(([x1, x2]) => {
                const plotX = marginX + (x1 + 4) / 8 * plotWidth;
                const plotY = this.height - marginY - (x2 + 4) / 8 * plotHeight;
                
                if (plotX >= marginX && plotX <= this.width - marginX &&
                    plotY >= marginY && plotY <= this.height - marginY) {
                    this.ctx.beginPath();
                    this.ctx.arc(plotX, plotY, 2, 0, 2 * Math.PI);
                    this.ctx.fill();
                }
            });
        }
        
        // Draw mean point
        const meanX = marginX + (this.params.mu1 + 4) / 8 * plotWidth;
        const meanY = this.height - marginY - (this.params.mu2 + 4) / 8 * plotHeight;
        this.ctx.fillStyle = '#000';
        this.ctx.beginPath();
        this.ctx.arc(meanX, meanY, 4, 0, 2 * Math.PI);
        this.ctx.fill();
        
        // Labels
        this.ctx.fillStyle = '#000';
        this.ctx.font = '12px Arial';
        this.ctx.textAlign = 'center';
        this.ctx.fillText('X₁', this.width / 2, this.height - 10);
        
        this.ctx.save();
        this.ctx.translate(15, this.height / 2);
        this.ctx.rotate(-Math.PI / 2);
        this.ctx.fillText('X₂', 0, 0);
        this.ctx.restore();
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    new DiscreteDistributionsDemo();
    new ContinuousDistributionsDemo();
    new MultivariateDemo();
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
