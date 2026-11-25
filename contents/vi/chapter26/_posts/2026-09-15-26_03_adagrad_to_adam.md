---
layout: post
title: 26-03 AdaGrad, trực giác RMSProp, và Adam
chapter: '26'
order: 4
owner: Nguyen Le Linh
categories:
- chapter26
lang: vi
lesson_type: required
---

Trong mạng nơ-ron sâu hay mô hình ngôn ngữ, các tham số sống trong những "vũ trụ" hoàn toàn khác nhau: trọng số của từ `"và"` nhận gradient lớn ở mọi minibatch, trong khi trọng số của một thuật ngữ hiếm chỉ nhận gradient khác 0 một lần sau mỗi nghìn bước. Ép cả triệu tham số khác biệt như vậy dùng chung một tốc độ học vô hướng $$\eta$$ giống như bắt cả xe tải hạng nặng lẫn xe đạp đua đi cùng một lực đạp ga.

Từ năm 2011 đến 2015, ba cột mốc liên tiếp — **AdaGrad**, **RMSProp** và **Adam** — đã cách mạng hóa việc huấn luyện học sâu bằng một ý tưởng đơn giản mà cực kỳ hiệu quả: **chia gradient của từng tọa độ cho căn bậc hai độ lớn lịch sử của chính nó**, giúp mọi tọa độ đều di chuyển với nhịp bước đồng đều bất kể độ thưa hay thang đo!

## Kiến thức cần nhớ: Ba bước tiến hóa từ AdaGrad đến Adam

Đặt ba công thức cạnh nhau, bạn sẽ thấy một chuỗi tiến hóa logic vô cùng mạch lạc:

- **AdaGrad (Cộng dồn toàn bộ lịch sử $$G_k$$):** Cộng tích lũy không quên $$G_{k+1} = G_k + g_k^2$$. Rất xuất sắc cho dữ liệu thưa lồi (từ hiếm có $$G_k$$ nhỏ nên được bước lớn), nhưng trong học sâu nhiều epoch, $$G_k$$ phình to mãi làm tốc độ học hiệu dụng chết dần về $$0$$.
- **RMSProp (Trung bình trượt mũ — EMA $$v_k$$):** Thay tổng tích lũy bằng trung bình trượt mũ $$v_{k+1} = \gamma v_k + (1-\gamma)g_k^2$$ để "quên" quá khứ xa và chỉ chuẩn hóa theo biên độ gradient gần đây, giữ cho bước học luôn sống động trên địa hình phi lồi thay đổi liên tục.
- **Adam (Kết hợp EMA bậc 1 + EMA bậc 2 + Hiệu chỉnh chệch):** Ghép động lượng $$m_k$$ (hướng đi mượt) với chuẩn hóa $$v_k$$ (thang đo thích nghi). Vì cả $$m_0 = 0, v_0 = 0$$ khởi tạo từ 0, ở các bước đầu chúng bị kéo lệch mạnh về 0 — do đó phép chia hiệu chỉnh $$\hat{m}_k = \frac{m_k}{1 - \beta_1^k},\; \hat{v}_k = \frac{v_k}{1 - \beta_2^k}$$ là bắt buộc để bước đi đầu tiên không bị méo!

### Giải thích: Tính tay 2 bước AdaGrad và kiểm chứng hiệu chỉnh chệch của Adam

Xét 2 tọa độ trọng số với dòng gradient: bước 1 là $$g^{(1)} = (10,\; 0)$$ (tọa độ 1 dày đặc, tọa độ 2 chưa xuất hiện), bước 2 là $$g^{(2)} = (10,\; 1)$$ (tọa độ 2 mới xuất hiện với gradient nhỏ). Lấy $$\eta = 0.1$$ và bỏ qua $$\varepsilon$$ nhỏ để tính tay sắc nét:

1. **Theo dõi AdaGrad ($$G_0 = (0, 0)$$):**
   - *Bước 1:* $$G_1 = (10^2,\; 0) = (100,\; 0)$$. Bước cập nhật tọa độ 1 là $$-0.1 \cdot \frac{10}{\sqrt{100}} = -0.1$$; tọa độ 2 là $$0$$.
   - *Bước 2:* $$G_2 = (100 + 100,\; 0 + 1) = (200,\; 1)$$.
     - Tọa độ 1 (xuất hiện thường xuyên): bước giảm xuống $$-0.1 \cdot \frac{10}{\sqrt{200}} \approx -0.0707$$.
     - Tọa độ 2 (đặc trưng hiếm mới xuất hiện): bước giữ nguyên kích thước đầy đủ $$-0.1 \cdot \frac{1}{\sqrt{1}} = -0.1000$$!
   Dù gradient tọa độ 2 nhỏ gấp 10 lần tọa độ 1, AdaGrad lại cho tọa độ 2 bước đi **lớn hơn** tọa độ 1!
2. **Kiểm chứng vì sao Adam cần hiệu chỉnh chệch ở bước $$k = 1$$ ($$\beta_1 = 0.9,\; \beta_2 = 0.999$$):**
   Với $$g_1^{(1)} = 10$$:
   - Chưa hiệu chỉnh: $$m_1 = 0.1(10) = 1.0$$ và $$v_1 = 0.001(10^2) = 0.1$$. Nếu chia thẳng: $$\frac{m_1}{\sqrt{v_1}} = \frac{1.0}{\sqrt{0.1}} \approx 3.162$$ — **phóng đại sai bước đi lên gấp 3.16 lần** chỉ vì $$\beta_2$$ gần 1 hơn $$\beta_1$$!
   - Có hiệu chỉnh chệch: $$\hat{m}_1 = \frac{1.0}{1 - 0.9} = 10$$ và $$\hat{v}_1 = \frac{0.1}{1 - 0.999} = 100$$. Tỷ số là $$\frac{\hat{m}_1}{\sqrt{\hat{v}_1}} = \frac{10}{10} = 1.0$$, cho bước cập nhật chuẩn xác $$-0.1 \cdot 1.0 = -0.1$$!

Không phải mọi tọa độ của vector tham số $$w$$ đều nên dùng chung một tốc độ học vô hướng $$\eta$$. Các đặc trưng ít xuất hiện (chẳng hạn vector one-hot của từ hiếm) cần bước cập nhật hiệu dụng lớn hơn, trong khi các tọa độ thường xuyên có gradient lớn sẽ dễ phân kỳ nếu dùng cùng mức $$\eta$$. Các **phương pháp thích nghi đường chéo** giải quyết vấn đề này bằng cách duy trì ước lượng mô-men bậc hai của gradient cho từng tọa độ và chia bước cập nhật cho căn bậc hai của ước lượng đó.

**AdaGrad** (Duchi, Hazan, Singer, 2011) cộng dồn bình phương gradient theo từng phần tử:

$$
G_{k+1} = G_k + g_k \odot g_k, \qquad w_{k+1} = w_k - \eta\, g_k \oslash \bigl(\sqrt{G_{k+1}}+\varepsilon\bigr),
$$

trong đó $$g_k=\nabla f_{I_k}(w_k)$$, còn $$\odot$$ và $$\oslash$$ lần lượt là phép nhân và phép chia theo từng phần tử. Vì tổng $$G_k$$ chỉ tăng mà không quên quá khứ, tốc độ học hiệu dụng **giảm đơn điệu** về 0. Điều này rất phù hợp với các bài toán lồi có đặc trưng thưa, nhưng lại gây đình trệ khi huấn luyện mạng nơ-ron sâu qua nhiều vòng lặp.

**RMSProp** (Hinton, bài giảng trực tuyến) khắc phục nhược điểm trên bằng cách thay tổng tích lũy bằng trung bình trượt mũ (EMA): $$v_{k+1}=\gamma v_k + (1-\gamma)\,g_k\odot g_k$$, cho phép hệ số tỉ lệ thích nghi linh hoạt theo độ lớn gradient gần đây.

**Adam** (Kingma & Ba, 2015) kết hợp trung bình trượt mũ của mô-men bậc hai (như RMSProp) với trung bình trượt mũ của mô-men bậc nhất (như momentum), đồng thời bổ sung hệ số hiệu chỉnh chệch vì cả hai đại lượng đều khởi tạo từ $$0$$:

$$
\begin{align}
m_{k+1} &= \beta_1 m_k + (1-\beta_1) g_k, \\
v_{k+1} &= \beta_2 v_k + (1-\beta_2)\, g_k\odot g_k, \\
\hat m &= m_{k+1}/(1-\beta_1^{k+1}), \quad
\hat v = v_{k+1}/(1-\beta_2^{k+1}), \\
w_{k+1} &= w_k - \eta\, \hat m \oslash (\sqrt{\hat v}+\varepsilon).
\end{align}
$$

Bộ tham số mặc định $$\beta_1=0.9$$, $$\beta_2=0.999$$, $$\varepsilon=10^{-8}$$ hoạt động ổn định trên rất nhiều bài toán, dù vẫn cần điều chỉnh khi huấn luyện các mô hình đặc thù. Về bản chất, Adam là **tiền điều kiện đường chéo kết hợp momentum**, không phải phương pháp bậc hai vì nó không xây dựng hay xấp xỉ đầy đủ ma trận Hessian.

```python
def adam_step(g, m, v, k, eta=1e-3, b1=0.9, b2=0.999, eps=1e-8):
    m = b1 * m + (1 - b1) * g
    v = b2 * v + (1 - b2) * (g * g)
    mhat = m / (1 - b1 ** (k + 1))
    vhat = v / (1 - b2 ** (k + 1))
    return mhat * eta / (vhat ** 0.5 + eps), m, v
```

Tham khảo bài báo gốc tại [arXiv:1412.6980](https://arxiv.org/abs/1412.6980). Bài tiếp theo sẽ phân tích vì sao việc cộng số hạng phạt $$(\lambda/2)\|w\|_2^2$$ vào hàm mất mát **không** tương đương với suy giảm trọng số (weight decay) trong AdamW.

### AdaGrad → RMSProp → Adam trong khoảng 3 phút

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/adagrad-rmsprop-adam_vi.mp4"></video>
</div>

Ba bước thích nghi trên cùng một hàm bậc hai lệch trục: AdaGrad chậm dần, RMSProp rung quanh nghiệm, Adam có hiệu chỉnh độ lệch.
