---
layout: post
title: '09-05 Tăng tốc'
chapter: '09'
order: 6
owner: Kyeongmin Woo
categories:
- chapter09
lang: vi
---

Nếu bạn thả một viên bi nặng lăn xuống một hẻm núi hình lòng máng hẹp và dài, viên bi sẽ trượt đi như thế nào? Gradient descent (và proximal gradient tiêu chuẩn) hành xử giống như một người đi bộ mất trí nhớ hoàn toàn: sau mỗi bước, họ dừng hẳn lại, quên sạch hướng mình vừa đi, rồi lại đo dốc cục bộ và đi vuông góc với đường đồng mức — kết quả là họ cứ zíc-zắc qua lại giữa hai thành hẻm núi, tiến dọc theo đáy hẻm chậm như rùa!

**Tăng tốc Nesterov (Nesterov Acceleration)** trả lại "trí nhớ quán tính" cho viên bi ấy — nhưng theo một cách tinh tế hơn cả vật lý cổ điển. Thay vì chỉ cộng quán tính sau khi tính gradient (như phương pháp Heavy Ball của Polyak), Nesterov để viên bi **nhìn trước một bước theo đà quán tính** rồi mới đo gradient và áp dụng toán tử gần kề tại điểm nhìn trước đó. Chỉ một thay đổi nhỏ về thứ tự phép tính ấy đã làm chấn động ngành tối ưu năm 1983, nâng tốc độ từ $$O(1/k)$$ lên đúng giới hạn lý thuyết $$O(1/k^2)$$!

## Kiến thức cần nhớ: Bốn trực giác cốt lõi về tăng tốc bậc nhất

- **Bệnh zíc-zắc trên hàm có số điều kiện lớn (Ill-conditioned Landscapes):** Khi độ cong theo một hướng lớn gấp $$\kappa$$ lần hướng kia, bước $$t \le 1/L$$ bị khống chế bởi hướng dốc nhất, khiến bước tiến dọc theo thung lũng phẳng cực kỳ nhỏ bé. Quán tính triệt tiêu các thành phần dao động ngược dấu qua hai bước liên tiếp và cộng hưởng các thành phần cùng hướng dọc đáy thung lũng.
- **Sự khác biệt giữa Polyak Heavy Ball và Nesterov Look-ahead:**
  - *Heavy Ball:* tính gradient tại $$x^{(k)}$$, rồi cộng đà $$\beta(x^{(k)} - x^{(k-1)})$$.
  - *Nesterov:* ngoại suy trước $$y^{(k)} = x^{(k)} + \beta_k(x^{(k)} - x^{(k-1)})$$, rồi mới tính $$\nabla g(y^{(k)})$$ và $$\operatorname{prox}_{t h}$$. Nhờ "phanh sớm" nếu bước quán tính vượt quá đáy, Nesterov đảm bảo hội tụ toàn cục $$O(1/k^2)$$ cho mọi hàm lồi trơn.
- **Nesterov lý thuyết vs. "Nesterov trong PyTorch":** Trong lý thuyết tối ưu lồi, hệ số quán tính tăng dần theo lịch $$\beta_k = \frac{k-1}{k+2} \to 1$$ để khớp tốc độ $$O(1/k^2)$$; trong khi ở học sâu (`torch.optim.SGD(..., momentum=0.9, nesterov=True)`), hệ số $$\beta$$ thường giữ cố định (như $$0.9$$) để cân bằng giữa tốc độ và nhiễu mini-batch.
- **Tác dụng phụ: gợn sóng Nesterov (Nesterov Ripples):** Vì có quán tính, quỹ đạo tăng tốc có thể trượt lố qua đáy rồi quay lại, nên giá trị hàm $$f(x^{(k)})$$ không còn giảm đơn điệu như ISTA — mở ra nhu cầu kỹ thuật khởi động lại (adaptive restart).

### Giải thích: Thấy tận mắt cơ chế "nhìn trước để phanh sớm" của Nesterov

Xét hàm bậc hai 1D $$g(x) = \frac{1}{2}x^2$$ ($$L = 1$$, nghiệm $$x^* = 0$$) với bước $$t = 0.5$$ và đà $$\beta = 0.5$$. Giả sử ta đang có $$x^{(0)} = 4$$ và $$x^{(1)} = 1$$ (đà chuyển động $$x^{(1)} - x^{(0)} = -3$$ đang lao mạnh về trái qua $$0$$).

1. **Cách 1 — Không quán tính (GD thường):**
   $$x^{(2)} = 1 - 0.5(1) = 0.5$$ (an toàn nhưng chậm).
2. **Cách 2 — Polyak Heavy Ball (đo dốc ở chỗ cũ rồi mới cộng đà):**
   $$x^{(2)}_{\text{HB}} = x^{(1)} - 0.5\nabla g(x^{(1)}) + 0.5(x^{(1)} - x^{(0)}) = 1 - 0.5(1) + 0.5(-3) = -1.0.$$
   Viên bi lao lố sang tận $$-1.0$$ (sai số giữ nguyên $$|x| = 1$$)!
3. **Cách 3 — Nesterov Look-ahead (nhìn trước rồi mới đo dốc):**
   - Điểm nhìn trước: $$y^{(1)} = 1 + 0.5(-3) = -0.5$$ (thấy ngay rằng mình sắp vượt qua đáy $$0$$ sang phía âm!).
   - Đo gradient tại $$y^{(1)} = -0.5$$: $$\nabla g(-0.5) = -0.5$$ (lực phanh kéo ngược về phải!).
   - Cập nhật: $$x^{(2)}_{\text{Nest}} = y^{(1)} - 0.5(-0.5) = -0.5 + 0.25 = -0.25$$!
   Sai số rơi ngay từ $$1.0$$ xuống $$0.25$$ (tốt gấp **4 lần** Heavy Ball và gấp **2 lần** GD thường)! Đó chính là bí mật của hai chữ *look-ahead*.

# Tăng tốc

Phương pháp gradient gần kề trên bài toán tổng hợp $$\min_x g(x)+h(x)$$ đã đạt tốc độ hội tụ $$O(1/k)$$ khi $$\nabla g$$ liên tục Lipschitz (bài 09-02). **Tăng tốc (acceleration)** là kỹ thuật bổ sung thành phần động lượng giúp nâng tốc độ hội tụ lên mức tối ưu bậc nhất $$O(1/k^2)$$ cho lớp hàm lồi trơn $$g$$ mà không cần tính ma trận Hessian. Bài học này trình bày góc nhìn trực quan theo phong cách Distill trước khi đi vào phần biến đổi đại số của FISTA. Thuật toán và chứng minh tốc độ $$O(1/k^2)$$ nằm ở [09-05-01]({% multilang_post_url contents/chapter09/20-01-08-09_05_01_accelerated_proximal_gradient_method %}) và [09-05-02]({% multilang_post_url contents/chapter09/20-01-08-09_05_02_convergence_analysis %}); biến thể ngẫu nhiên với hệ số $$\beta$$ cố định dùng trong huấn luyện mạng nơ-ron nằm ở [26-02]({% multilang_post_url contents/chapter26/2026-09-15-26_02_momentum_and_nesterov %}).

## Vì sao bước gradient gần kề tiêu chuẩn dễ dao động zíc-zắc

Có thể hình dung một bước gradient gần kề là: thực hiện một bước gradient trên phần trơn, sau đó điều chỉnh lại bằng $$\operatorname{prox}_{t h}$$. Khi $$h=0$$, thuật toán trở về gradient descent thông thường, và ví dụ kinh điển là thung lũng hẹp $$g(x)=\tfrac12 x^\top\operatorname{diag}(1,L)\,x$$: kích thước bước đủ nhỏ để không dao động theo chiều dốc lại khiến thuật toán tiến rất chậm dọc theo đáy thung lũng. Kỹ thuật động lượng — do Nesterov đề xuất cho hàm lồi trơn năm 1983, và được Beck–Teboulle (2009) mở rộng kèm ánh xạ gần kề thành **FISTA** — lưu lại điểm lặp *trước đó* để ngoại suy vị trí trước khi áp dụng toán tử gần kề.

Bước ngoại suy nhìn trước (look-ahead) của FISTA ở bài 09-05-01 có dạng:

$$
\begin{align}
v^{(k)} &= x^{(k-1)}+\frac{k-2}{k+1}\bigl(x^{(k-1)}-x^{(k-2)}\bigr),\\
x^{(k)} &= \operatorname{prox}_{t_k h}\bigl(v^{(k)}-t_k\nabla g(v^{(k)})\bigr).
\end{align}
$$

Trọng số $$(k-2)/(k+1)$$ khởi đầu từ $$0$$ (bước đầu tiên trùng với gradient gần kề tiêu chuẩn) và tăng dần tiến tới $$1$$. Lịch trình này không phải lựa chọn tùy ý, mà là phiên bản rời rạc của cơ chế tắt dần trong thời gian liên tục giúp hoàn tất chứng minh tốc độ $$O(1/k^2)$$ của Nesterov. Bài viết trên Distill của Goh, *[Why Momentum Really Works](https://distill.pub/2017/momentum/)*, minh họa đúng hình học này trong trường hợp không có prox: một hệ thức truy hồi bậc hai với nghiệm đặc trưng nằm trên đường tròn bán kính $$(\sqrt{\kappa}-1)/(\sqrt{\kappa}+1)$$, cải thiện hệ số co từ $$1-\Theta(1/\kappa)$$ thành $$1-\Theta(1/\sqrt{\kappa})$$.

## Tăng tốc Nesterov lý thuyết và “Nesterov trong PyTorch”

Hai khái niệm mang cùng tên trong giáo trình này có bản chất khác nhau và không thể dùng thay thế cho nhau một cách tùy tiện.

Trên hàm $$g$$ *lồi trơn* (hoặc bài toán tổng hợp $$g+h$$ với $$h$$ lồi), Nesterov / FISTA sử dụng trọng số động lượng **thay đổi theo lịch trình** và tính gradient của phần trơn tại điểm ngoại suy $$v$$. Khi đó ta có bảo đảm $$g(x^{(k)})+h(x^{(k)})-F^\star=O(1/k^2)$$, đạt đúng cận dưới lý thuyết của các phương pháp bậc nhất ở [06-03-06]({% multilang_post_url contents/chapter06/21-03-20-06_03_06_can_we_do_better %}). Biểu đồ so sánh ISTA và FISTA trên bài toán Lasso ở [09-05-03]({% multilang_post_url contents/chapter09/20-01-08-09_05_03_example_FISTA %}) là kết quả thực nghiệm cần nắm vững.

Trên *mạng nơ-ron sâu*, `torch.optim.SGD(..., nesterov=True)` thường dùng hệ số động lượng **cố định** $$\beta\approx 0.9$$ trên hàm mất mát không lồi. Trực giác về bộ lọc vẫn hữu ích — các hướng nhất quán được tích lũy, các hướng dao động triệt tiêu nhau, và bước nhìn trước giúp giảm hiện tượng vượt đích — nhưng không còn bảo đảm lý thuyết $$O(1/k^2)$$. Bài 26-02 phân tích chi tiết sự khác biệt này, bao gồm đa thức đặc trưng của phương pháp heavy-ball và đoạn mã so sánh ngắn bằng NumPy.

<div class="content-box insight-box">
<strong>Điểm cốt lõi cần nhớ.</strong> FISTA là bước nhìn trước Nesterov <em>kết hợp</em> toán tử gần kề với trọng số thay đổi theo $$k$$. Động lượng trong học sâu dùng cùng ý tưởng nhìn trước nhưng cố định trọng số. Áp dụng định lý theo lịch trình cho các bài toán lồi như Lasso hay hồi quy logistic; dùng trực giác thung lũng của Distill cho các bài toán khác.
</div>

## Khi tăng tốc chưa chắc là lựa chọn tối ưu

Tăng tốc không mang lại lợi ích miễn phí trong mọi trường hợp. Chính quán tính giúp di chuyển nhanh dọc đáy thung lũng lồi cũng có thể khiến quỹ đạo vượt quá điểm gấp khúc không trơn hoặc vùng cực tiểu hẹp — đó là lý do tồn tại bài [09-05-04]({% multilang_post_url contents/chapter09/20-01-08-09_05_04_is_acceleration_always_useful %}) và kỹ thuật khởi động lại (restart) cho FISTA. Nếu phần trơn có chi phí tính thấp và lồi mạnh, phương pháp gradient gần kề được tinh chỉnh tốt (hoặc các phương pháp giảm phương sai ở [26-05]({% multilang_post_url contents/chapter26/2026-09-15-26_05_variance_reduction %})) có thể nhanh hơn phương pháp tăng tốc không có restart xét theo thời gian thực thi thực tế. Cần theo dõi giá trị hàm mục tiêu: nếu xuất hiện dao động kiểu “gợn sóng Nesterov”, hãy áp dụng restart hoặc giảm $$\beta$$.

### ISTA và FISTA trong khoảng 3 phút

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/ista-fista_vi.mp4"></video>
</div>

ISTA và FISTA trên lasso: ngưỡng mềm, trọng số (k − 2)/(k + 1), gợn sóng Nesterov, trường hợp tăng tốc làm chậm, và khởi động lại.

**Bài tập.** Trên thung lũng $$g(x)=\tfrac12 x^\top\operatorname{diag}(1,100)\,x$$ với $$h=0$$, hãy vẽ đường hội tụ của ISTA (GD tiêu chuẩn), FISTA với trọng số $$(k-2)/(k+1)$$, và Nesterov với $$\beta$$ cố định từ bài 26-02. Phương pháp nào đạt $$\|x\|_2\le 10^{-4}$$ sớm nhất, và phương pháp nào dao động quanh gốc tọa độ nếu không dùng restart?

**Câu hỏi.** Trọng số của FISTA tiến tới $$1$$, trong khi trọng số heavy-ball tối ưu $$\beta^\star$$ theo bài Distill (khi biết số điều kiện $$\kappa$$) luôn nhỏ hơn $$1$$ nghiêm ngặt. Vì sao cả hai kết quả này đều đúng — và điều gì thay đổi khi ta *không* biết trước $$\kappa$$?
