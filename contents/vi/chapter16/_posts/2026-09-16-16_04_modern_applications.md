---
layout: post
title: 16-04 Ứng dụng hiện đại của tính đối ngẫu (2022–2026)
chapter: '16'
order: 5
owner: Nguyen Le Linh
categories:
- chapter16
lang: vi
lesson_type: optional
---

Nếu ai đó nghĩ rằng đối ngẫu Lagrange và liên hợp Fenchel chỉ dành cho các bộ giải quy hoạch tuyến tính thế kỷ trước, hãy nhìn vào những công trình định hình trí tuệ nhân tạo giai đoạn **2022–2026**: **hàm mất mát Fenchel–Young** (thống nhất Cross-Entropy, Sparsemax và học có cấu trúc), **căn chỉnh mô hình ngôn ngữ lớn bằng RLHF** (nơi hệ số $$\beta$$ trước phân kỳ KL chính là nhân tử Lagrange!), **học tăng cường an toàn (Safe RL)** chạy vòng lặp nguyên thủy – đối ngẫu trực tiếp, và **vận chuyển tối ưu (Optimal Transport / Wasserstein)** dưới góc nhìn đối ngẫu Fenchel–Kantorovich.

Bài đọc hiện đại này chỉ ra cách chính xác ba trụ cột của Chương 16 (Lagrange, KKT và Fenchel) đang giải quyết những bài toán nóng nhất của AI ngày nay.

## Kiến thức cần nhớ: Bốn cầu nối từ Đối ngẫu Chương 16 sang AI hiện đại (2022–2026)

- **Hàm mất mát Fenchel–Young:** Cho bất kỳ hàm lồi $$\Omega(p)$$ nào (như entropy âm hay bình phương $$\ell_2$$), định nghĩa $$L_\Omega(\theta; y) = \Omega^*(\theta) + \Omega(y) - \theta^T y \ge 0$$ nhờ bất đẳng thức Fenchel–Young! Khi $$\Omega$$ là entropy âm, $$L_\Omega$$ chính là **Cross-Entropy Loss** quen thuộc!
- **RLHF và ràng buộc phân kỳ KL:** Bài toán cực đại hóa phần thưởng $$\mathbb{E}_\pi[r(x, y)]$$ dưới ràng buộc $$D_{\text{KL}}(\pi \| \pi_{\text{ref}}) \le \delta$$ khi đưa vào hàm Lagrange với nhân tử $$\beta > 0$$ cho ra nghiệm đóng **phân phối Boltzmann** $$\pi^*(y \mid x) \propto \pi_{\text{ref}}(y \mid x)\exp(r(x, y)/\beta)$$ — nền tảng của cả PPO-RLHF lẫn DPO!
- **Vòng lặp nguyên thủy – đối ngẫu trong Safe RL:** Thay vì tự mò trọng số phạt an toàn cố định, thuật toán cập nhật chính sách $$\pi$$ (giảm cực tiểu Lagrange) xen kẽ với bước tăng/giảm nhân tử Lagrange $$\lambda \ge 0$$ (leo dốc đối ngẫu) cho đến khi tỷ lệ vi phạm an toàn tụt xuống dưới ngưỡng cho phép.
- **Vận chuyển tối ưu (Optimal Transport):** Đối ngẫu Fenchel–Kantorovich chuyển bài toán tìm kế hoạch vận chuyển khối lượng xác suất thành bài toán tìm hai hàm thế năng đối ngẫu $$(\phi, \psi)$$ (nền tảng của Wasserstein GAN và khớp phân phối trong mô hình sinh).

### Giải thích: Tính tay nghiệm đóng RLHF (phân phối Boltzmann) từ điều kiện KKT

Xét bài toán chọn phân phối hành động $$\pi = (\pi_1, \pi_2)$$ trên 2 câu trả lời ($$\pi_1 + \pi_2 = 1, \pi_i > 0$$) với phân phối tham chiếu đều $$\pi_{\text{ref}} = (0.5, 0.5)$$, điểm thưởng $$r = (2, 0)$$, và nhân tử Lagrange KL cố định $$\beta = 1$$:

$$\max_{\pi_1 + \pi_2 = 1} \bigl(2\pi_1 + 0\pi_2\bigr) - 1 \cdot \left(\pi_1 \ln\frac{\pi_1}{0.5} + \pi_2 \ln\frac{\pi_2}{0.5}\right).$$

1. **Lập hàm Lagrange (với nhân tử $$\nu$$ cho $$\pi_1 + \pi_2 = 1$$):**
   $$L(\pi, \nu) = 2\pi_1 - \pi_1 \ln(2\pi_1) - \pi_2 \ln(2\pi_2) + \nu(1 - \pi_1 - \pi_2).$$
2. **Giải điều kiện dừng KKT $$\frac{\partial L}{\partial \pi_i} = 0$$:**
   - Theo $$\pi_1$$: $$2 - \ln(2\pi_1) - 1 - \nu = 0 \implies \pi_1 = \frac{1}{2} e^{1 - \nu}$$.
   - Theo $$\pi_2$$: $$0 - \ln(2\pi_2) - 1 - \nu = 0 \implies \pi_2 = \frac{1}{2} e^{-1 - \nu}$$.
3. **Chuẩn hóa bằng $$\pi_1 + \pi_2 = 1$$:**
   $$\frac{\pi_1}{\pi_2} = \frac{e^2}{e^0} = e^2 \approx 7.389 \implies \pi_1^\star = \frac{e^2}{e^2 + 1} \approx 0.8808, \qquad \pi_2^\star = \frac{1}{e^2 + 1} \approx 0.1192.$$
   Nhờ ràng buộc KL (nhân tử $$\beta = 1$$), mô hình ưu tiên câu trả lời tốt hơn (88.1%) nhưng không sụp đổ thành 100% (reward hacking) mà vẫn giữ độ đa dạng gần mô hình gốc!

---

Chương 16 hệ thống lại đối ngẫu Lagrange, điều kiện KKT và liên hợp Fenchel làm nền tảng cho phương pháp điểm trong nguyên thủy – đối ngẫu ở Chương 17. Ba đối tượng quen thuộc này — hàm Lagrange, biến đối ngẫu định giá ràng buộc và hàm liên hợp Fenchel chuyển đổi giữa hàm mất mát và hàm điều chuẩn (regularizer) — chính là cách học máy giai đoạn 2022–2026 *xây dựng hàm mục tiêu*, chứ không chỉ dùng trong chứng minh lý thuyết. Bốn ứng dụng dưới đây giữ rõ cấu trúc toán học của chương này: ở mỗi trường hợp, ta đều có thể chỉ ra rõ ràng bài toán nguyên thủy, ràng buộc và biến đối ngẫu tương ứng.

## Hàm mất mát Fenchel–Young: dùng hàm liên hợp làm mục tiêu huấn luyện

Blondel, Martins và Niculae (JMLR 2020) định nghĩa **hàm mất mát Fenchel–Young** từ một ánh xạ dự báo có điều chuẩn. Nếu $$\Omega$$ là hàm điều chuẩn lồi trên đơn hình (hoặc một tập có cấu trúc) và $$\Omega^\star$$ là hàm liên hợp của nó, thì hàm mất mát

$$
L_\Omega(\theta; y) = \Omega^\star(\theta) + \Omega(y) - \theta^\top y
$$

chính là khe Fenchel–Young đã xét ở [16-03]({% multilang_post_url contents/chapter16/21-03-31-16_03_fenchel_duality %}). Hàm mất mát entropy chéo là trường hợp riêng với $$\Omega$$ là âm entropy; các hàm mất mát thưa và có cấu trúc khác thu được khi thay đổi $$\Omega$$. Dù khái niệm ra đời trước năm 2022, nó đã trở thành một *khuôn mẫu thiết kế* phổ biến trong những năm gần đây. Blondel, Llinares-López, Dadashi, Hussenot và Geist (NeurIPS 2022) mở rộng hướng này sang mạng năng lượng bằng cách thay tích song tuyến bằng một phép ghép tổng quát (hàm liên hợp tổng quát, bao gồm phép biến đổi $$C$$-transform của vận chuyển tối ưu). Năm 2025, hàm mất mát Fenchel–Young sắc nét (sharpened Fenchel–Young losses) được ứng dụng cho bài toán ngược vận chuyển tối ưu không cân bằng và dòng gradient JKO ngược — bao gồm mô hình hóa động lực quần thể tế bào trong hệ gen học đơn bào ([arXiv:2505.07124](https://arxiv.org/abs/2505.07124)).

Góc nhìn thực hành: hãy lấy một hàm mất mát quen thuộc, viết lại nó dưới dạng $$\Omega^\star(\theta)-\theta^\top y+\Omega(y)$$, và nhìn nhận biến đối ngẫu như một *dự báo* thay vì chỉ là nhân tử Lagrange. Lúc này, đối ngẫu không chỉ là công cụ kiểm chứng tính tối ưu mà trực tiếp trở thành hàm mất mát.

## RLHF: ràng buộc KL và nhân tử Lagrange tương ứng

Ouyang et al. (NeurIPS 2022), *Training language models to follow instructions with human feedback* (InstructGPT), tinh chỉnh mô hình đã học có giám sát bằng PPO theo mô hình phần thưởng, kết hợp với **hạng tử phạt KL theo từng token** để giữ chính sách không lệch quá xa mô hình tham chiếu SFT. Mục tiêu RLHF tiêu chuẩn chính là hàm Lagrange của bài toán

$$
\max_\pi\ \mathbb{E}_{x\sim\mathcal{D},\, y\sim\pi(\cdot\mid x)}\bigl[r_\theta(x,y)\bigr]
\quad\text{với}\quad
\mathbb{E}\bigl[\mathrm{KL}(\pi(\cdot\mid x)\,\|\,\pi_{\mathrm{SFT}}(\cdot\mid x))\bigr] \le \varepsilon.
$$

Hệ số nhân với hạng tử KL là biến đối ngẫu của ràng buộc phân kỳ KL. Tăng hệ số này tương ứng với một bước tăng đối ngẫu (dual ascent): ta nâng mức phạt cho việc rời xa mô hình tham chiếu cho đến khi ràng buộc được thỏa mãn. Các phương pháp căn chỉnh sau này (như DPO và các biến thể liên quan) viết lại *chính hàm Lagrange đó* để chính sách tối ưu có nghiệm dạng đóng và hệ số đối ngẫu trở thành tham số nhiệt độ; cấu trúc đối ngẫu vẫn được giữ nguyên, chỉ khác là được giải theo hướng giải tích.

Đây là một ví dụ thực tế gần gũi của Chương 16: đối ngẫu mạnh không được đảm bảo cho lớp chính sách không lồi, nhưng *cách mô hình hóa* — đặt ràng buộc trước, định giá ràng buộc và xem nhân tử như một tham số điều chỉnh — chính là ứng dụng trực tiếp của đối ngẫu Lagrange trong thực tiễn.

## Học tăng cường an toàn (Safe RL): vòng lặp nguyên thủy – đối ngẫu trong thực tế

Bài toán MDP có ràng buộc (CMDP) yêu cầu tìm chính sách cực đại hóa lợi tức kỳ vọng trong giới hạn ngân sách chi phí kỳ vọng. PPO-Lagrangian và TRPO-Lagrangian (OpenAI Safety Gym, Ray et al. 2019) cập nhật chính sách bằng PPO/TRPO và cập nhật nhân tử bằng bước tăng đối ngẫu dựa trên phần dư chi phí — đúng theo sơ đồ nguyên thủy – đối ngẫu kinh điển trên một bài toán điểm yên ngẫu nhiên, không lồi. CPO (Achiam et al., 2017) tuyến tính hóa ràng buộc và giải một bài toán QP nhỏ ở mỗi bước; IPO (Chương 15) dùng hàm rào cản thay cho nhân tử. Các bộ thư viện OmniSafe (Ji et al., JMLR 2024) và Safety Gymnasium (Ji et al., NeurIPS 2023) chuẩn hóa các thuật toán này để nghiên cứu và đồ án giai đoạn 2024–2026 có thể *so sánh trực tiếp* phương pháp rào cản, nguyên thủy – đối ngẫu và đối ngẫu miền tin cậy trên cùng một môi trường robot.

Paternain, Chamon, Calvo-Fullana và Ribeiro (và loạt nghiên cứu SafeRL nguyên thủy – đối ngẫu năm 2022) cung cấp nền tảng giải tích lồi cho hướng này: hàm đối ngẫu của CMDP là một bài toán quy hoạch lõm theo nhân tử, và khe đối ngẫu nhỏ giúp kiểm soát mức độ vi phạm ràng buộc. Đó chính là nội dung [16-01]({% multilang_post_url contents/chapter16/21-03-31-16_01_lagrangian_duality_revisited %}) với phép lấy kỳ vọng nằm bên trong các tích trong.

## Vận chuyển tối ưu dưới góc nhìn đối ngẫu Fenchel

Bài toán vận chuyển tối ưu có điều chuẩn entropy (entropic optimal transport),

$$
\min_{\pi\in\Pi(\mu,\nu)}\ \langle C,\pi\rangle + \varepsilon\,\mathrm{KL}(\pi\,\|\,\mu\otimes\nu),
$$

có bài toán đối ngẫu Fenchel là bài toán cực đại hóa hàm lõm không ràng buộc theo hai thế năng — chính là đối ngẫu Sinkhorn. Vận chuyển tối ưu tính toán (chuyên khảo Peyré & Cuturi; thư viện POT) được sử dụng rộng rãi trong giai đoạn 2022–2026 cho phân tích dữ liệu đơn bào, thích nghi miền và mô hình sinh nhằm vận chuyển khối lượng xác suất giữa các độ đo thực nghiệm. Hàm mất mát Fenchel–Young tổng quát (NeurIPS 2022) chuyển phép biến đổi $$C$$-transform của đối ngẫu đó thành *hàm mất mát huấn luyện* cho mô hình năng lượng. Nếu đối ngẫu Fenchel ở bài 16-03 từng có vẻ trừu tượng, thì ứng dụng này cho thấy ý nghĩa trực quan của nó: hàm liên hợp của chi phí vận chuyển là một thế năng, và việc khớp các thế năng đó trở thành bài toán học có giám sát.

## Nguồn

- M. Blondel, A. F. T. Martins, V. Niculae, “Learning with Fenchel-Young Losses,” JMLR 21(35), 2020.
- M. Blondel, F. Llinares-López, R. Dadashi, L. Hussenot, M. Geist, “Learning Energy Networks with Generalized Fenchel-Young Losses,” NeurIPS 2022.
- “Learning from Samples: Inverse Problems over Measures via Sharpened Fenchel-Young Losses,” 2025. [arXiv:2505.07124](https://arxiv.org/abs/2505.07124)
- L. Ouyang et al., “Training language models to follow instructions with human feedback,” NeurIPS 2022.
- J. Ji et al., “OmniSafe,” JMLR 25(285), 2024; “Safety Gymnasium,” NeurIPS 2023 Datasets.
- S. Paternain et al., phương pháp nguyên thủy–đối ngẫu cho RL ràng buộc (dòng 2022); G. Peyré, M. Cuturi, *Computational Optimal Transport*.
