---
layout: post
title: 16-04 Ứng dụng hiện đại của tính đối ngẫu (2022–2026)
chapter: '16'
order: 7
owner: Nguyen Le Linh
categories:
- chapter16
lang: vi
lesson_type: optional
---

Chương 16 xem lại đối ngẫu Lagrange, KKT, và liên hợp Fenchel để phương pháp điểm trong nguyên thủy–đối ngẫu ở Chương 17 có chỗ đứng. Cùng ba đối tượng — một Lagrange, một biến đối ngẫu định giá ràng buộc, và một liên hợp Fenchel đổi mất mát lấy regularizer — là cách học máy 2022–2026 *viết mục tiêu*, không chỉ cách nó chứng minh. Bốn ứng dụng dưới đây giữ toán của chương này lộ ra: bạn phải nêu được nguyên thủy, ràng buộc, và biến đối ngẫu trong từng câu chuyện.

## Mất mát Fenchel–Young: liên hợp như mục tiêu huấn luyện

Blondel, Martins và Niculae (JMLR 2020) định nghĩa **mất mát Fenchel–Young** từ một hàm dự báo đã regularize. Nếu $$\Omega$$ là regularizer lồi trên đơn hình (hoặc một tập có cấu trúc) và $$\Omega^\star$$ là liên hợp của nó, mất mát

$$
L_\Omega(\theta; y) = \Omega^\star(\theta) + \Omega(y) - \theta^\top y
$$

đúng là khe Fenchel–Young từ [16-03]({% multilang_post_url contents/chapter16/21-03-31-16_03_fenchel_duality %}). Entropy chéo là trường hợp riêng $$\Omega =$$ âm entropy; các mất mát thưa và có cấu trúc xuất hiện khi đổi $$\Omega$$. Cách dựng cũ hơn 2022, nhưng nó thành *khuôn thiết kế* những năm sau. Blondel, Llinares-López, Dadashi, Hussenot và Geist (NeurIPS 2022) nâng lên mạng năng lượng bằng cách thay cặp song tuyến bằng một ghép tổng quát (liên hợp tổng quát, gồm $$C$$-transform của vận chuyển tối ưu). Năm 2025, mất mát Fenchel–Young làm sắc được dùng cho OT không cân bằng ngược và dòng gradient JKO ngược — kể cả động lực quần thể tế bào trong genomics đơn bào ([arXiv:2505.07124](https://arxiv.org/abs/2505.07124)).

Động tác lớp học: lấy một mất mát bạn đã biết, viết nó thành $$\Omega^\star(\theta)-\theta^\top y+\Omega(y)$$, và đọc biến đối ngẫu như một *dự báo* chứ không chỉ như nhân tử Lagrange. Đối ngẫu không còn chỉ là chứng chỉ; nó là mất mát.

## RLHF: ràng buộc KL và nhân tử Lagrange của nó

Ouyang et al. (NeurIPS 2022), *Training language models to follow instructions with human feedback* (InstructGPT), tinh chỉnh mô hình giám sát bằng PPO đối với mô hình thưởng, cộng **phạt KL từng token** giữ chính sách gần tham chiếu SFT. Mục tiêu RLHF chuẩn là Lagrange của

$$
\max_\pi\ \mathbb{E}_{x\sim\mathcal{D},\, y\sim\pi(\cdot\mid x)}\bigl[r_\theta(x,y)\bigr]
\quad\text{với}\quad
\mathbb{E}\bigl[\mathrm{KL}(\pi(\cdot\mid x)\,\|\,\pi_{\mathrm{SFT}}(\cdot\mid x))\bigr] \le \varepsilon.
$$

Hệ số trên số hạng KL là biến đối ngẫu của một ràng buộc phân kỳ. Tăng nó là một bước lên đối ngẫu: bạn tăng giá của việc rời tham chiếu cho tới khi ràng buộc chịu được. Các công thức căn chỉnh sau (DPO và họ hàng) viết lại *cùng* Lagrange sao cho chính sách tối ưu có dạng đóng và hệ số đối ngẫu thành nhiệt độ; đối ngẫu vẫn đó, chỉ được giải giải tích.

Đây là câu chuyện Chương 16 mà sinh viên đã dùng như chatbot: đối ngẫu mạnh không được khẳng định cho lớp chính sách không lồi, nhưng *cách mô hình hóa* — ràng buộc trước, định giá ràng buộc, đọc nhân tử như một núm — là đối ngẫu Lagrange trong sản xuất.

## RL an toàn: vòng nguyên thủy–đối ngẫu chạy được

MDP ràng buộc đòi chính sách cực đại hóa lợi tức chịu ngân sách chi phí kỳ vọng. PPO-Lagrangian và TRPO-Lagrangian (OpenAI Safety Gym, Ray et al. 2019) cập nhật chính sách bằng PPO/TRPO và nhân tử bằng lên đối ngẫu trên phần dư chi phí — phương pháp nguyên thủy–đối ngẫu sách giáo khoa trên một yên ngẫu nhiên, không lồi. CPO (Achiam et al., 2017) tuyến tính hóa ràng buộc và giải một QP nhỏ; IPO (Chương 15) dùng rào thay nhân tử. OmniSafe (Ji et al., JMLR 2024) và Safety Gymnasium (Ji et al., NeurIPS 2023) đóng gói các thuật toán này để một đồ án 2024–2026 có thể *so* rào, nguyên thủy–đối ngẫu, và đối ngẫu miền tin cậy trên cùng robot.

Paternain, Chamon, Calvo-Fullana và Ribeiro (và dòng SafeRL nguyên thủy–đối ngẫu 2022) cho xương sống giải tích lồi: hàm đối ngẫu của CMDP là chương trình lõm theo nhân tử, và một khe đối ngẫu nhỏ kiểm soát vi phạm ràng buộc. Đó là [16-01]({% multilang_post_url contents/chapter16/21-03-31-16_01_lagrangian_duality_revisited %}) với kỳ vọng bên trong mọi tích trong.

## Vận chuyển tối ưu như đối ngẫu Fenchel

Vận chuyển tối ưu entropy,

$$
\min_{\pi\in\Pi(\mu,\nu)}\ \langle C,\pi\rangle + \varepsilon\,\mathrm{KL}(\pi\,\|\,\mu\otimes\nu),
$$

có đối ngẫu Fenchel là cực đại lõm không ràng buộc trên hai thế — đối ngẫu Sinkhorn. OT tính toán (chuyên khảo Peyré & Cuturi; thư viện POT) là cách các bài đơn bào, thích nghi miền, và mô hình sinh 2022–2026 chuyển khối lượng giữa các độ đo thực nghiệm. Mất mát Fenchel–Young tổng quát (NeurIPS 2022) biến $$C$$-transform của đối ngẫu đó thành *mất mát huấn luyện* cho mô hình năng lượng. Nếu đối ngẫu Fenchel ở 16-03 từng trừu tượng, đây là bức tranh: liên hợp của chi phí vận chuyển là một thế, và khớp những thế đó là học có giám sát.

## Nguồn

- M. Blondel, A. F. T. Martins, V. Niculae, “Learning with Fenchel-Young Losses,” JMLR 21(35), 2020.
- M. Blondel, F. Llinares-López, R. Dadashi, L. Hussenot, M. Geist, “Learning Energy Networks with Generalized Fenchel-Young Losses,” NeurIPS 2022.
- “Learning from Samples: Inverse Problems over Measures via Sharpened Fenchel-Young Losses,” 2025. [arXiv:2505.07124](https://arxiv.org/abs/2505.07124)
- L. Ouyang et al., “Training language models to follow instructions with human feedback,” NeurIPS 2022.
- J. Ji et al., “OmniSafe,” JMLR 25(285), 2024; “Safety Gymnasium,” NeurIPS 2023 Datasets.
- S. Paternain et al., phương pháp nguyên thủy–đối ngẫu cho RL ràng buộc (dòng 2022); G. Peyré, M. Cuturi, *Computational Optimal Transport*.
