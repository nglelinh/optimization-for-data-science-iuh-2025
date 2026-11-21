---
layout: post
title: 04-09 Ứng dụng và phát triển gần đây
chapter: '04'
order: 12
owner: Nguyen Le Linh
categories:
- chapter04
lang: vi
lesson_type: optional
---

Chương 04 là hợp đồng của một chương trình lồi: biến, mục tiêu, ràng buộc, tối ưu, và các phép viết lại hợp lệ (tối thiểu hóa từng phần, đổi biến, khử đẳng thức, slack, nới). Cùng hợp đồng đó hiện là một *lớp* trong mạng nơ-ron và một *mất mát* cho bộ dự đoán sẽ bị một bộ giải tiêu thụ. Bài này xem ba phát triển 2019–2023 chỉ có nghĩa sau khi bạn viết được “$$0\in\partial f(x^\star)+N_{\mathcal{C}}(x^\star)$$” mà không ngần ngại.

## Lớp lồi khả vi và tối ưu ẩn

Agrawal, Amos, Barratt, Boyd, Diamond và Kolter (*Differentiable Convex Optimization Layers*, [NeurIPS 2019](https://web.stanford.edu/~boyd/papers/diff_cvxpy.html); thư viện [cvxpylayers](https://cvxpylayers.org/)) nhúng một chương trình lồi có kỷ luật vào đồ thị PyTorch hoặc TensorFlow. Lượt thuận *giải* chương trình; lượt ngược vi phân ánh xạ nghiệm bằng vi phân ẩn qua phần dư bộ giải (phân tích affine-solver-affine họ gọi là DPP). Năm 2019 hơi trước cửa sổ yêu cầu; thư viện là mặc định 2022–2026 khi bài báo nói “chúng tôi đặt một QP trong mạng.”

Ngôn ngữ tối ưu đúng là ngôn ngữ chương này. Nếu $$x^\star(\theta)$$ giải bài lồi tham số hóa, phần dư KKT $$F(x,\lambda;\theta)=0$$ là phương trình ẩn. Bạn không cần bung projected gradient; bạn tuyến tính hóa $$F$$, như Blondel và cộng sự sau đó tự động hóa trong JAXopt ([NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/hash/228b9279ecf9bbafe582406850c57115-Abstract-Conference.html)). Điều kiện cấp một của Chương 04 là *đặc tả* của $$F$$.

## Theseus: bình phương tối thiểu phi tuyến như lớp khả vi

Không phải mọi bài trong đều lồi. Robot và thị giác 3D liên tục giải bình phương tối thiểu phi tuyến

$$
\min_x \tfrac12 \sum_i \bigl\| r_i(x;\theta)\bigr\|_2^2
$$

bằng Gauss–Newton hoặc Levenberg–Marquardt. Pineda, Fan, Monge, Venkataraman, Sodhi, Chen, Ortiz, DeTone, Wang, Anderson, Dong, Amos và Mukadam (*Theseus: A Library for Differentiable Nonlinear Optimization*, [NeurIPS 2022](https://arxiv.org/abs/2207.09442); [facebookresearch/theseus](https://github.com/facebookresearch/theseus)) phát hành thư viện PyTorch coi lần giải trong đó như một lớp: bộ giải thưa, nhóm Lie, batch, GPU, và gradient bằng vi phân ẩn hoặc bằng vi phân các bước đã bung.

Vì sao nó thuộc *chương này* chứ không chỉ môn robot: tác giả vẫn xuất phát từ phần dư tối ưu (điều kiện dừng của mục tiêu bình phương tối thiểu) rồi chọn một *phép viết lại hợp lệ* — vi phân ẩn versus bung vòng — đúng thói quen “biến đổi và đổi biến” của 04-05. Khi bài trong *là* lồi, ưu tiên cvxpylayers; khi là LS phi tuyến có cấu trúc, Theseus là triển khai tham chiếu 2022.

## Tối ưu khấu hao và surrogate lồi cho quyết định

Hai ý bổ sung tái sử dụng từ vựng Chương 04.

Amos (*Tutorial on Amortized Optimization*, [*Foundations and Trends in Machine Learning* 16:592–732, 2023](https://doi.org/10.1561/2200000102); [arXiv:2202.00665](https://arxiv.org/abs/2202.00665)) khảo sát *học để tối ưu*: mạng dự đoán $$x\approx x^\star(\theta)$$ cho một họ bài toán cùng cấu trúc (suy diễn biến phân, mã hóa thưa, meta-learning, vận chuyển tối ưu, mạng cân bằng sâu). Khấu hao không thay điều kiện tối ưu; nó *xấp xỉ ánh xạ nghiệm*. Bạn vẫn cần bài trong đặt đúng, và vẫn gỡ lỗi bằng cách nhìn phần dư.

Elmachtoub và Grigas ([*Management Science* 2022](https://doi.org/10.1287/mnsc.2020.3922)) xuất phát từ mất mát quyết định thật không liên tục theo chi phí dự đoán, rồi *nới* thành surrogate lồi SPO+ suy từ đối ngẫu — cách dùng sách giáo khoa của 04-08 (nới) cộng điều kiện tối ưu của quy hoạch tuyến tính. Tập khả thi vẫn là đa diện gốc; chỉ mục tiêu huấn luyện được thay bằng thứ lồi theo tham số bộ dự đoán.

## Một khuôn mẫu tái dùng trên bài tập

Viết bài trong dạng chuẩn, gọi tên phép viết lại, và gọi tên gradient ngoài:

$$
\begin{align}
\text{trong:}&\quad x^\star(\theta)\in\arg\min_{x\in\mathcal{C}(\theta)} f(x;\theta),\\
\text{viết lại:}&\quad F(x^\star,\nu^\star;\theta)=0 \quad\text{(KKT / dừng)},\\
\text{ngoài:}&\quad \nabla_\theta \ell\bigl(x^\star(\theta)\bigr) \quad\text{qua } \nabla_x F,\;\nabla_\theta F.
\end{align}
$$

Nếu không viết được $$F$$, bạn chưa sẵn sàng vi phân qua bộ giải. Nếu viết được $$F$$ nhưng $$\mathcal{C}$$ không lồi, bạn đang ở lãnh thổ Theseus / LS phi tuyến, và tối ưu toàn cục biến mất — đúng là lý do Chương 04 dành nhiều trang cho tập nghiệm lồi.

## Nguồn

1. A. Agrawal, B. Amos, S. Barratt, S. Boyd, S. Diamond và J. Z. Kolter, “Differentiable Convex Optimization Layers,” NeurIPS 2019. [trang](https://web.stanford.edu/~boyd/papers/diff_cvxpy.html) · [cvxpylayers](https://cvxpylayers.org/)
2. M. Blondel và cộng sự, “Efficient and Modular Implicit Differentiation,” NeurIPS 2022. [tóm tắt](https://proceedings.neurips.cc/paper_files/paper/2022/hash/228b9279ecf9bbafe582406850c57115-Abstract-Conference.html)
3. L. Pineda và cộng sự, “Theseus: A Library for Differentiable Nonlinear Optimization,” NeurIPS 2022. [arXiv:2207.09442](https://arxiv.org/abs/2207.09442) · [mã](https://github.com/facebookresearch/theseus)
4. B. Amos, “Tutorial on Amortized Optimization,” *Found. Trends Mach. Learn.* 16:592–732, 2023. [DOI](https://doi.org/10.1561/2200000102) · [arXiv:2202.00665](https://arxiv.org/abs/2202.00665)
5. A. N. Elmachtoub và P. Grigas, “Smart ‘Predict, then Optimize’,” *Management Science* 2022. [DOI](https://doi.org/10.1287/mnsc.2020.3922)
