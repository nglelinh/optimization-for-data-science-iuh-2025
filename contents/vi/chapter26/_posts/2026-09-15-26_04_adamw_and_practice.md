---
layout: post
title: 26-04 AdamW và thực hành huấn luyện
chapter: '26'
order: 5
owner: Nguyen Le Linh
categories:
- chapter26
lang: vi
lesson_type: required
---

Trong suốt nhiều năm sau khi Adam ra đời (2015), giới học sâu vướng phải một bí ẩn khó chịu: Adam huấn luyện cực nhanh trên tập train, nhưng khi đánh giá trên tập test (như phân loại ảnh ImageNet hay huấn luyện Transformer), nó lại **tổng quát hóa kém hơn SGD + Momentum** có suy giảm trọng số (weight decay).

Năm 2017–2019, Ilya Loshchilov và Frank Hutter phát hiện ra một lỗi "ghép nhầm" tinh vi nằm ngay trong cách mọi thư viện cài đặt chính quy hóa $$\ell_2$$ cho Adam: với SGD thuần, cộng $$\frac{\lambda}{2}\|w\|_2^2$$ vào hàm mất mát tương đương hệt với việc co trọng số $$(1 - \eta\lambda)w$$; nhưng với **Adam**, thành phần $$\lambda w$$ lại bị đem chia cho $$\sqrt{\hat{v}}$$, làm hỏng hoàn toàn cơ chế suy giảm trọng số! Chỉ bằng một dòng sửa duy nhất — **tách rời weight decay ra khỏi phép chia thích nghi** — **AdamW** ra đời và lập tức trở thành bộ tối ưu mặc định của kỷ nguyên LLM.

## Bản đồ kiến thức nền: Bốn trụ cột thực hành huấn luyện mạng sâu với AdamW

Để huấn luyện mạng sâu ổn định từ đầu tới cuối, AdamW luôn đi cùng ba kỹ thuật thực hành không thể thiếu:

- **Tách rời Suy giảm trọng số (Decoupled Weight Decay):** Trong AdamW, mọi trọng số chịu lực co đồng đều $$-\eta \lambda w_k$$ bất kể gradient quá khứ lớn hay nhỏ. Nhờ vậy, siêu tham số $$\lambda$$ và tốc độ học $$\eta$$ không bị quấn chặt vào nhau như trong Adam + $$\ell_2$$.
- **Lịch tốc độ học Warmup + Cosine Decay:** Ở vài trăm bước đầu, ước lượng mô-men $$\hat{v}_k$$ còn rất nhiễu và trọng số còn ngẫu nhiên; tăng dần $$\eta$$ từ $$0$$ lên $$\eta_{\max}$$ (*warmup*) giúp tránh "sốc" gradient ban đầu, sau đó giảm mượt theo đường cong cosine để hạ cánh êm vào đáy thung lũng phẳng.
- **Cắt ngưỡng Gradient (Gradient Clipping):** Giới hạn chuẩn toàn cục $$\|g\|_2 \le \tau$$ đóng vai trò van an toàn chống bùng nổ gradient khi gặp minibatch bất thường hoặc vách đá dốc trên địa hình phi lồi của Transformer/RNN.
- **Ổn định số học với $$\varepsilon$$ và Huấn luyện độ chính xác hỗn hợp:** Tham số $$\varepsilon$$ (thường $$10^{-8}$$) không chỉ tránh chia cho 0 mà còn điều tiết mức độ "thích nghi" ở các tọa độ có gradient rất nhỏ; khi huấn luyện `fp16`/`bf16`, ta thường giữ bản sao trạng thái tối ưu (`m, v`) ở `fp32` để không mất độ chính xác.

### Khung giải thích (nên đọc chậm): Tính tay sự khác biệt gây sốc giữa Adam + $$\ell_2$$ và AdamW

Giả sử ta có hai trọng số cùng giá trị $$w_1 = 1.0$$ và $$w_2 = 1.0$$, tốc độ học $$\eta = 0.1$$, hệ số phạt $$\lambda = 0.1$$. Tọa độ 1 nằm ở lớp có gradient lịch sử lớn ($$\sqrt{\hat{v}_1} = 10$$), còn tọa độ 2 nằm ở lớp có gradient lịch sử nhỏ ($$\sqrt{\hat{v}_2} = 0.1$$). Để cô lập hoàn toàn tác dụng của lực suy giảm trọng số, giả sử gradient của hàm mất mát dữ liệu tại bước này bằng $$0$$ ($$g_{\text{data}} = (0, 0)$$, $$\hat{m}_{\text{data}} = (0, 0)$$):

1. **Với Adam + chính quy hóa $$\ell_2$$ (cộng $$\lambda w$$ vào gradient trước khi chia $$\sqrt{\hat{v}}$$):**
   Gradient tổng có thêm $$\lambda w = (0.1,\; 0.1)$$. Khi đi qua phép chia thích nghi $$1/\sqrt{\hat{v}}$$:
   - Lực kéo về 0 trên tọa độ 1: $$\Delta w_1 = -0.1 \cdot \frac{0.1}{10} = -0.001$$ (chỉ giảm $$0.1\%$$!).
   - Lực kéo về 0 trên tọa độ 2: $$\Delta w_2 = -0.1 \cdot \frac{0.1}{0.1} = -0.100$$ (giảm tới $$10\%$$ — **mạnh gấp 100 lần** tọa độ 1!).
   Nghịch lý xảy ra: những trọng số có gradient lớn nhất (thường cần kiểm soát độ lớn nhất) lại hầu như **không bị suy giảm**!
2. **Với AdamW (tách rời $$-\eta\lambda w_k$$ ra ngoài phép chia $$\sqrt{\hat{v}}$$):**
   - Lực kéo về 0 trên tọa độ 1: $$\Delta w_1 = -0.1(0.1)(1.0) = -0.01$$ (giảm $$1\%$$).
   - Lực kéo về 0 trên tọa độ 2: $$\Delta w_2 = -0.1(0.1)(1.0) = -0.01$$ (giảm đúng $$1\%$$!).
3. **Kết luận:** Chỉ một thay đổi nhỏ về vị trí dấu ngoặc đã khôi phục hoàn toàn tính đồng đều của weight decay trên mọi lớp mạng, giải thích vì sao AdamW đánh bại Adam + $$\ell_2$$ trên hầu hết các mô hình Transformer hiện đại!

Chính quy hóa $$\ell_2$$ cộng thêm số hạng $$\frac{\lambda}{2}\|w\|_2^2$$ vào hàm mất mát, khiến gradient tăng thêm $$\lambda w$$. Khi tối ưu bằng **Adam**, thành phần $$\lambda w$$ này cũng bị chia bởi $$1/(\sqrt{\hat v}+\varepsilon)$$. Hệ quả là các tọa độ có mô-men bậc hai lớn chịu lực suy giảm *nhỏ hơn* so với các tọa độ có mô-men bậc hai nhỏ; tức là bộ tối ưu không còn áp dụng đúng phép suy giảm trọng số đồng đều như mục đích ban đầu.

**AdamW** (Loshchilov & Hutter, ICLR 2019, [arXiv:1711.05101](https://arxiv.org/abs/1711.05101)) **tách rời** bước suy giảm trọng số khỏi phần thích nghi:

$$
w_{k+1} = w_k - \eta \Bigl( \hat m \oslash (\sqrt{\hat v}+\varepsilon) + \lambda w_k \Bigr).
$$

Lúc này, suy giảm trọng số (weight decay) tác động trực tiếp như một lực co về gốc tọa độ trên không gian tham số, độc lập với hệ số co giãn thích nghi $$\sqrt{\hat v}$$. Trong PyTorch, điều này tương ứng với `torch.optim.AdamW`, khác với `torch.optim.Adam` có tham số `weight_decay` (vốn cộng trực tiếp vào gradient theo kiểu chính quy hóa $$\ell_2$$).

## Các kỹ thuật thực hành gắn liền với tối ưu hóa

* **Lịch tốc độ học (learning rate schedule):** Khởi động tăng dần (warmup) rồi giảm theo hàm cosine hoặc tuyến tính chính là cách chọn dãy bước $$\eta_k$$ biến thiên. Lý thuyết SGD lồi đã chỉ ra nhu cầu giảm dần tốc độ học; học sâu mở rộng thêm giai đoạn warmup để ổn định giai đoạn đầu khi ước lượng mô-men còn nhiễu.
* **Cắt ngưỡng gradient (gradient clipping):** Thay $$g$$ bằng $$g\cdot \min(1, \tau/\|g\|)$$ đóng vai trò như một vùng tin cậy đơn giản giới hạn độ dài bước ngẫu nhiên, đặc biệt quan trọng khi huấn luyện mạng hồi quy (RNN) và transformer.
* **Quan hệ giữa kích thước lô và tốc độ học $$\eta$$:** Quy tắc tỉ lệ tuyến tính (Goyal và cộng sự) coi minibatch lớn hơn là ước lượng ít nhiễu hơn nên có thể tăng $$\eta$$ tương ứng cho tới một ngưỡng bão hòa.
* **Phân biệt rõ cơ chế weight decay:** Khi báo cáo tham số “weight decay $$\lambda$$” trong thực nghiệm, cần nêu rõ đó là dạng tách rời (kiểu AdamW) hay cộng vào hàm mất mát (chính quy hóa $$\ell_2$$).

Tài liệu đọc thêm (không thuộc phần lõi): SAM (Foret và cộng sự, ICLR 2021) hướng đến các cực tiểu *phẳng* thông qua bài toán cực đại hóa cục bộ; còn Muon và Sophia là các bộ tối ưu mới đáng chú ý giai đoạn 2023–2025. Bài seminar tùy chọn [26-06]({% multilang_post_url contents/chapter26/2026-09-16-26_06_modern_optimizers %}) tóm tắt công thức cập nhật của từng phương pháp (không lặp lại phần phân tích Sophia theo góc nhìn Newton ở mục 14-10); nội dung này không kiểm tra trong học kỳ.

**Bài tập.** Huấn luyện một mạng MLP nhỏ trên tập dữ liệu 2 chiều `two-moons` bằng cả Adam và AdamW với cùng hệ số $$\lambda$$, sau đó vẽ đồ thị chuẩn $$\|w\|_2$$ theo epoch. Dù đường hàm mất mát huấn luyện trông khá tương đồng, quỹ đạo của chuẩn tham số $$\|w\|_2$$ sẽ khác biệt rõ rệt giữa hai bộ tối ưu.
