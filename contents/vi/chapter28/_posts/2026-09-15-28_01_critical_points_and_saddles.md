---
layout: post
title: 28-01 Điểm tới hạn và yên ngựa
chapter: '28'
order: 2
owner: Nguyen Le Linh
categories:
- chapter28
lang: vi
lesson_type: required
---

Trong giải tích một biến ở năm nhất đại học, khi thấy $$f'(x) = 0$$, ta thường kiểm tra ngay dấu của $$f''(x)$$: dương là cực tiểu, âm là cực đại. Nhưng ngay khi bước lên mặt phẳng 2 chiều — chứ chưa nói đến không gian 1 tỷ chiều của mạng nơ-ron — một nhân vật thứ ba lập tức chiếm lĩnh sân khấu: **điểm yên ngựa (saddle point)**, nơi địa hình cong lên theo hướng này nhưng lại dốc tụt xuống theo hướng kia.

Điều thú vị đến rùng mình của hình học nhiều chiều là: nếu mỗi hướng độc lập có xác suất $$50\%$$ cong lên và $$50\%$$ cong xuống, thì trong không gian $$d = 100$$ chiều, xác suất để một điểm tới hạn có *cả 100 hướng đều cong lên* (cực tiểu địa phương) chỉ là $$2^{-100} \approx 10^{-30}$$! Phần còn lại gần như chắc chắn là điểm yên ngựa — giải thích vì sao hiểu phổ Hessian là bước đầu tiên để hiểu động lực huấn luyện mạng sâu.

## Kiến thức cần nhớ: Ba trụ cột phân loại điểm tới hạn bằng Hessian

Bài học này đặt nền tảng giải tích bậc hai cho toàn bộ Chương 28 qua ba trụ cột:

- **Khai triển Taylor bậc hai và Dấu trị riêng Hessian:** Tại điểm tới hạn $$\nabla F(w) = 0$$, dáng điệu cục bộ hoàn toàn do dạng toàn phương $$\frac{1}{2} \Delta w^T H \Delta w$$ quyết định. Chéo hóa $$H = Q \Lambda Q^T$$ tách không gian thành $$d$$ trục độc lập: mỗi trị riêng âm $$\lambda_i < 0$$ là một "lối thoát" giúp giảm hàm mất mát khi bước theo vector riêng $$q_i$$.
- **Yên ngựa chặt (Strict Saddle) vs. Yên ngựa suy biến (Degenerate Saddle):** Yên ngựa chặt có ít nhất một $$\lambda_{\min}(H) < 0$$ rõ rệt, nên có lối thoát ngay ở bậc hai. Ngược lại, khi $$\lambda_{\min}(H) = 0$$ (như hàm $$w^3$$ hay các cao nguyên phẳng trong mạng sâu), kiểm định bậc hai bất lực và thuật toán bậc nhất có thể bò cực chậm.
- **Lời nguyền kích thước đảo ngược (High-Dimensional Blessing):** Trái với trực giác 2D lo sợ bị kẹt ở cực tiểu địa phương xấu, trong không gian chiều rất cao, hầu hết các điểm dừng có giá trị mất mát cao đều có nhiều hướng độ cong âm (điểm yên ngựa) để thuật toán thoát ra được.

### Giải thích: Tính tay phân loại đủ 3 điểm tới hạn của hàm thế hai giếng (Double-Well)

Để luyện kỹ năng phân loại bằng Hessian mà không trùng với bài tập $$x^2 - y^2$$ ở cuối bài, hãy xét hàm không lồi 2 biến:

$$
F(x, y) = \frac{1}{4}x^4 - \frac{1}{2}x^2 + \frac{1}{2}y^2.
$$

1. **Tìm tất cả điểm tới hạn ($$\nabla F = 0$$):**
   $$\nabla F(x, y) = \bigl(x^3 - x,\; y\bigr) = (0,\; 0) \implies x(x^2 - 1) = 0,\; y = 0.$$
   Có đúng 3 điểm tới hạn: $$P_1 = (0, 0)$$, $$P_2 = (1, 0)$$, và $$P_3 = (-1, 0)$$.
2. **Tính ma trận Hessian tổng quát:**
   $$H(x, y) = \begin{pmatrix} \frac{\partial^2 F}{\partial x^2} & \frac{\partial^2 F}{\partial x \partial y} \\ \frac{\partial^2 F}{\partial y \partial x} & \frac{\partial^2 F}{\partial y^2} \end{pmatrix} = \begin{pmatrix} 3x^2 - 1 & 0 \\ 0 & 1 \end{pmatrix}.$$
3. **Phân loại từng điểm dựa trên cặp trị riêng $$(\lambda_1, \lambda_2) = (3x^2 - 1,\; 1)$$:**
   - *Tại $$P_1 = (0, 0)$$:* $$(\lambda_1, \lambda_2) = (-1,\; +1)$$ trái dấu $$\implies$$ **Điểm yên ngựa chặt!** Giá trị $$F(0, 0) = 0$$. Nếu dịch nhẹ dọc hướng riêng âm $$u = (1, 0)$$ một đoạn $$t = 0.2$$, ta có $$F(0.2, 0) = 0.0004 - 0.02 = -0.0196 < 0$$ (giảm ngay lập tức!).
   - *Tại $$P_2 = (1, 0)$$ và $$P_3 = (-1, 0)$$:* $$(\lambda_1, \lambda_2) = (+2,\; +1)$$ đều dương $$\implies$$ **Hai cực tiểu địa phương chặt** (và đều là cực tiểu toàn cục với $$F = -\frac{1}{4} = -0.25$$).

Cho hàm $$F:\mathbb{R}^d\to\mathbb{R}$$ khả vi hai lần liên tục. Điểm $$w$$ là **điểm tới hạn (critical point)** nếu $$\nabla F(w)=0$$. Khi ma trận Hessian $$H=\nabla^2 F(w)$$ không suy biến (không có trị riêng bằng 0), ta phân loại $$w$$ như sau:

* **Cực tiểu địa phương chặt:** $$H\succ 0$$ (mọi trị riêng đều dương).
* **Cực đại địa phương chặt:** $$H\prec 0$$ (mọi trị riêng đều âm).
* **Điểm yên ngựa chặt (strict saddle):** $$H$$ không xác định dấu — có ít nhất một trị riêng dương và một trị riêng âm.

Nếu tồn tại trị riêng bằng 0, kiểm định bậc hai chưa đủ để kết luận (ví dụ hàm $$w\mapsto w^3$$ hoặc các vùng cao nguyên phẳng). Hàm mất mát của mạng nơ-ron sâu thường chứa rất nhiều phương gần suy biến.

Mặc dù **các phương pháp bậc nhất không tính trực tiếp $$H$$**, khai triển Taylor bậc hai cục bộ vẫn cho thấy hành vi tại điểm yên ngựa: dọc theo một phương $$u$$ có độ cong âm ($$u^\top H u < 0$$), giá trị $$F(w+t u)\approx F(w)+\tfrac12 t^2 u^\top H u$$ *giảm* với $$t\neq 0$$ đủ nhỏ. Do đó, điểm yên ngựa chặt không phải là cái bẫy đối với thuật toán có thể dịch chuyển theo phương độ cong âm, mà chỉ gây dừng sớm cho các thuật toán chỉ kiểm tra điều kiện $$\|\nabla F\| \approx 0$$.

Trong không gian nhiều chiều, nếu dấu các trị riêng của ma trận Hessian tại một điểm tới hạn bất kỳ ứng xử tương tự ma trận đối xứng ngẫu nhiên, xác suất để *tất cả* $$d$$ trị riêng đều dương giảm theo hàm mũ của $$d$$. Nhận xét định tính quan trọng cần nhớ là: **với các hàm tổng quát nhiều chiều, đa số điểm tới hạn là điểm yên ngựa chứ không phải cực tiểu địa phương**. Dù hàm mất mát học sâu không hoàn toàn giống hàm ngẫu nhiên Gaussian, trực giác này giải thích vì sao tình trạng chậm tiến triển khi huấn luyện thường liên quan đến điểm yên ngựa và vùng phẳng hơn là bị mắc kẹt ở một cực tiểu địa phương xấu.

### Điểm yên ngựa trong khoảng 3 phút

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/saddle-escape_vi.mp4"></video>
</div>

GD bị hút vào yên ngựa của x² − y² + ½y⁴, ngồi lâu khi lệch rất nhỏ, thoát nhờ nhiễu, và vì sao ở chiều cao hầu hết điểm tới hạn là yên ngựa.

**Bài tập.** Xét hàm yên ngựa $$F(x,y)=x^2-y^2$$: hãy viết $$\nabla F$$ và ma trận Hessian $$H$$. Thực hiện hai bước gradient descent với bước $$\eta = 0.1$$, xuất phát từ $$(0, 10^{-3})$$, sau đó giải thích vì sao nếu xuất phát chính xác từ $$(0, 0)$$ thì gradient descent lý tưởng sẽ không bao giờ rời khỏi điểm đó.
