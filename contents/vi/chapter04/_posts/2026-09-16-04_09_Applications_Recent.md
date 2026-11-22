---
layout: post
title: 04-09 Ứng dụng và phát triển gần đây
chapter: '04'
order: 10
owner: Nguyen Le Linh
categories:
- chapter04
lang: vi
lesson_type: optional
---

Chương 04 xây dựng nền tảng cho bài toán tối ưu hóa lồi: biến quyết định, hàm mục tiêu, ràng buộc, điều kiện tối ưu và các phép biến đổi hợp lệ (tối ưu hóa từng phần, đổi biến, loại bỏ ràng buộc đẳng thức, biến phụ và nới lỏng). Trong những năm gần đây, chính cấu trúc này được tích hợp trực tiếp như một *lớp* (layer) trong mạng nơ-ron và làm cơ sở thiết kế *hàm mất mát* cho các mô hình dự đoán phục vụ bài toán ra quyết định. Bài học này điểm qua ba hướng phát triển tiêu biểu giai đoạn 2019–2023 dựa trực tiếp trên điều kiện tối ưu dạng “$$0\in\partial f(x^\star)+N_{\mathcal{C}}(x^\star)$$”.

## Lớp tối ưu hóa lồi khả vi và vi phân ẩn

Agrawal, Amos, Barratt, Boyd, Diamond và Kolter (*Differentiable Convex Optimization Layers*, [NeurIPS 2019](https://web.stanford.edu/~boyd/papers/diff_cvxpy.html); thư viện [cvxpylayers](https://cvxpylayers.org/)) đưa một bài toán quy hoạch lồi có cấu trúc (disciplined convex program) vào đồ thị tính toán của PyTorch hoặc TensorFlow như một lớp khả vi. Ở lượt lan truyền thuận, lớp này *giải* bài toán tối ưu; ở lượt lan truyền ngược, gradient của nghiệm theo tham số được tính bằng vi phân ẩn thông qua phần dư của bộ giải (dựa trên biểu diễn affine–bộ giải–affine gọi là DPP). Dù công bố từ năm 2019, `cvxpylayers` vẫn là thư viện tiêu chuẩn trong giai đoạn 2022–2026 mỗi khi một nghiên cứu cần nhúng trực tiếp bài toán quy hoạch bậc hai (QP) hay bài toán lồi vào mạng nơ-ron.

Cách tiếp cận này gắn trực tiếp với điều kiện tối ưu của Chương 04. Nếu $$x^\star(\theta)$$ là nghiệm của một bài toán lồi phụ thuộc tham số $$\theta$$, thì hệ điều kiện KKT $$F(x,\lambda;\theta)=0$$ đóng vai trò là phương trình ẩn xác định nghiệm. Thay vì khai triển (unroll) toàn bộ các bước lặp của thuật toán hạ gradient chiếu, ta chỉ cần tuyến tính hóa hệ $$F$$ — cách làm sau này được Blondel và cộng sự hệ thống hóa và tự động hóa trong thư viện JAXopt ([NeurIPS 2022](https://proceedings.neurips.cc/paper_files/paper/2022/hash/228b9279ecf9bbafe582406850c57115-Abstract-Conference.html)). Điều kiện tối ưu bậc nhất trong Chương 04 chính là *đặc tả* trực tiếp của hệ $$F$$.

## Theseus: Bình phương tối thiểu phi tuyến dưới dạng lớp khả vi

Không phải mọi bài toán tối ưu bên trong mô hình đều lồi. Trong lĩnh vực robot và thị giác 3D, các hệ thống thường xuyên phải giải bài toán bình phương tối thiểu phi tuyến:

$$
\min_x \tfrac12 \sum_i \bigl\| r_i(x;\theta)\bigr\|_2^2
$$

bằng các thuật toán như Gauss–Newton hoặc Levenberg–Marquardt. Pineda, Fan, Monge, Venkataraman, Sodhi, Chen, Ortiz, DeTone, Wang, Anderson, Dong, Amos và Mukadam (*Theseus: A Library for Differentiable Nonlinear Optimization*, [NeurIPS 2022](https://arxiv.org/abs/2207.09442); [facebookresearch/theseus](https://github.com/facebookresearch/theseus)) đã xây dựng thư viện PyTorch coi cả quá trình giải bài toán này như một lớp khả vi, hỗ trợ bộ giải thưa, nhóm Lie, xử lý theo lô (batch) trên GPU, đồng thời cho phép tính gradient bằng vi phân ẩn hoặc vi phân qua các bước lặp đã khai triển.

Điểm kết nối của công trình này với Chương 04 nằm ở tư duy mô hình hóa: xuất phát từ điều kiện dừng của bài toán bình phương tối thiểu rồi lựa chọn *phép biến đổi tương đương* phù hợp — giữa vi phân ẩn và khai triển vòng lặp — tương tự tư duy biến đổi và đổi biến ở bài 04-05. Khi bài toán bên trong có tính lồi, `cvxpylayers` là lựa chọn ưu tiên; còn khi gặp bài toán bình phương tối thiểu phi tuyến có cấu trúc, `Theseus` là thư viện tham chiếu phổ biến từ năm 2022.

## Tối ưu hóa khấu hao và hàm thay thế lồi cho bài toán ra quyết định

Hai hướng nghiên cứu khác cũng vận dụng trực tiếp các khái niệm của Chương 04.

Thứ nhất, Amos (*Tutorial on Amortized Optimization*, [*Foundations and Trends in Machine Learning* 16:592–732, 2023](https://doi.org/10.1561/2200000102); [arXiv:2202.00665](https://arxiv.org/abs/2202.00665)) tổng hợp hướng tiếp cận *học để tối ưu* (learning to optimize): huấn luyện một mạng nơ-ron dự đoán trực tiếp $$x\approx x^\star(\theta)$$ cho cả một họ bài toán có chung cấu trúc (như suy diễn biến phân, mã hóa thưa, học siêu tham số, vận chuyển tối ưu hay mạng cân bằng sâu). Tối ưu hóa khấu hao không thay thế điều kiện tối ưu mà *xấp xỉ ánh xạ nghiệm*; bài toán bên trong vẫn cần được phát biểu chuẩn xác và vẫn được kiểm tra sai số thông qua phần dư của điều kiện tối ưu.

Thứ hai, Elmachtoub và Grigas ([*Management Science* 2022](https://doi.org/10.1287/mnsc.2020.3922)) xét bài toán ra quyết định theo quy trình "dự đoán rồi tối ưu": hàm mất mát quyết định thực tế không liên tục theo vectơ chi phí dự đoán, nên các tác giả *nới lỏng* nó thành hàm mất mát thay thế lồi SPO+ xây dựng từ lý thuyết đối ngẫu. Đây là ứng dụng điển hình kết hợp kỹ thuật nới lỏng ở bài 04-08 với điều kiện tối ưu của quy hoạch tuyến tính: tập khả thi đa diện gốc được giữ nguyên, chỉ hàm mục tiêu huấn luyện được thay bằng một hàm lồi theo tham số của mô hình dự đoán.

## Khuôn mẫu chung khi áp dụng vào bài tập

Khi phân tích hoặc thiết kế một bài toán tối ưu hóa khả vi, có thể tổ chức theo ba bước chuẩn: viết bài toán bên trong ở dạng chuẩn, xác định hệ điều kiện tối ưu (phép viết lại), và tính gradient bên ngoài:

$$
\begin{align}
\text{bài toán trong:}&\quad x^\star(\theta)\in\arg\min_{x\in\mathcal{C}(\theta)} f(x;\theta),\\
\text{điều kiện tối ưu:}&\quad F(x^\star,\nu^\star;\theta)=0 \quad\text{(KKT / điểm dừng)},\\
\text{gradient ngoài:}&\quad \nabla_\theta \ell\bigl(x^\star(\theta)\bigr) \quad\text{qua } \nabla_x F,\;\nabla_\theta F.
\end{align}
$$

Nếu chưa viết được hệ $$F$$, ta chưa thể thực hiện vi phân ẩn qua bộ giải. Nếu viết được $$F$$ nhưng tập $$\mathcal{C}$$ hoặc hàm mục tiêu không lồi, bài toán chuyển sang phạm vi của `Theseus` hay bình phương tối thiểu phi tuyến, nơi tính tối ưu toàn cục không còn được đảm bảo — đây cũng là lý do Chương 04 tập trung phân tích kỹ tính chất của tập nghiệm lồi.

## Nguồn

1. A. Agrawal, B. Amos, S. Barratt, S. Boyd, S. Diamond và J. Z. Kolter, “Differentiable Convex Optimization Layers,” NeurIPS 2019. [trang](https://web.stanford.edu/~boyd/papers/diff_cvxpy.html) · [cvxpylayers](https://cvxpylayers.org/)
2. M. Blondel và cộng sự, “Efficient and Modular Implicit Differentiation,” NeurIPS 2022. [tóm tắt](https://proceedings.neurips.cc/paper_files/paper/2022/hash/228b9279ecf9bbafe582406850c57115-Abstract-Conference.html)
3. L. Pineda và cộng sự, “Theseus: A Library for Differentiable Nonlinear Optimization,” NeurIPS 2022. [arXiv:2207.09442](https://arxiv.org/abs/2207.09442) · [mã](https://github.com/facebookresearch/theseus)
4. B. Amos, “Tutorial on Amortized Optimization,” *Found. Trends Mach. Learn.* 16:592–732, 2023. [DOI](https://doi.org/10.1561/2200000102) · [arXiv:2202.00665](https://arxiv.org/abs/2202.00665)
5. A. N. Elmachtoub và P. Grigas, “Smart ‘Predict, then Optimize’,” *Management Science* 2022. [DOI](https://doi.org/10.1287/mnsc.2020.3922)
