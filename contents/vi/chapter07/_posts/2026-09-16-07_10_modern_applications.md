---
layout: post
title: 07-10 Ứng dụng hiện đại của subgradient
chapter: '07'
order: 17
owner: Nguyen Le Linh
categories:
- chapter07
lang: vi
lesson_type: optional
---

# Ứng dụng hiện đại của subgradient

Bài tùy chọn này **không** làm lại phép tính của Chương 07. Nó chỉ ra chỗ các đối tượng ấy — một vector $$g$$ thỏa $$f(y)\ge f(x)+g^\top(y-x)$$, tập $$\partial f(x)$$, và kiểm định dừng $$0\in\partial f(x^\star)$$ — xuất hiện trong các pipeline khoa học máy tính / khoa học dữ liệu khoảng 2022–2026. Sau bài này bạn nên gọi được một hàm mất mát hoặc regularizer không trơn trong hệ thống thật, viết được bao hàm đặc trưng nghiệm cực tiểu, và chỉ được một bài báo thay vì một khẩu hiệu.

## Vì sao subgradient không phải chú thích lịch sử

Mạng ReLU, chọn đặc trưng $$\ell_1$$, hàm pinball (phân vị), và khớp Huber đều là các mảnh **lồi không trơn hoặc path-differentiable**. Autodiff trong PyTorch hay JAX vẫn trả về một vector tại điểm gãy; ngôn ngữ đúng cho vector đó là **trường bảo toàn** (conservative field), trùng subgradient trên các mảnh lồi và trùng phần tử Clarke hầu khắp nơi. Nếu chỉ nhớ “gradient bằng không tại cực tiểu,” bạn không gỡ được support của Lasso, ReLU chết, hay một khớp phân vị.

## 1. Mạng ReLU và vi phân tự động không trơn

Rectifier $$\operatorname{ReLU}(t)=\max\{t,0\}$$ có

$$
\partial\operatorname{ReLU}(t)=\begin{cases}\{0\} & t<0,\\ [0,1] & t=0,\\ \{1\} & t>0.\end{cases}
$$

Một mạng sâu gồm ánh xạ affine và ReLU là Lipschitz và semialgebraic, do đó **path-differentiable**. Bolte và Pauwels (2021) chỉ ra rằng vật backprop thực sự cài đặt là một *trường tập-giá trị bảo toàn*: nó tuân quy tắc chuỗi dù subdifferential Clarke của một chương trình ReLU không nhất thiết vậy. Bolte, Boustany, Pauwels và Pesquet (2022) chứng minh **nguyên lý gradient rẻ không trơn** cho AD chiều ngược và cho thấy việc tính *hai* phần tử Clarke khác nhau của một mạng ReLU đơn giản là NP-khó — nên các framework sản xuất không lười khi chọn một phần tử của $$\partial\operatorname{ReLU}(0)$$ (thường là $$0$$). Blondel và Roulet (2024) sắp cùng câu chuyện ấy thành *lập trình khả vi*: thiết kế chương trình sao cho đạo hàm bảo toàn tồn tại, rồi huấn luyện bằng SGD.

**Nối với giáo trình.** Các quy tắc trong [07-02-02 Phép tính subgradient]({% multilang_post_url contents/chapter07/21-03-25-07_02_02_subgradient_calculus %}) (tổng, max, hợp với ánh xạ affine) chính là quy tắc đồ thị tính ReLU dùng. Kiểm định $$0\in\partial f(x)$$ vẫn là điều một bài toán lớp cuối lồi (SVM tuyến tính, đầu Lasso) phải thỏa.

## 2. Lasso, elastic net, và đường GLM hiện đại

Lasso

$$
\min_\beta\ \tfrac12\|y-X\beta\|_2^2+\lambda\|\beta\|_1
$$

là ví dụ xuyên suốt chương: điều kiện dừng là $$X^\top(y-X\beta)=\lambda v$$ với $$v\in\partial\|\beta\|_1$$, tức $$v_j=\operatorname{sign}(\beta_j)$$ trên support và $$|v_j|\le 1$$ ngoài support ([07-03-03 Điều kiện tối ưu Lasso]({% multilang_post_url contents/chapter07/21-03-25-07_03_03_example_lasso_optimality_condition %})). Bao hàm ấy vẫn là cách `glmnet` và `skglm` quyết định tọa độ nào bằng không.

Tay, Narasimhan và Hastie (2023) mở đường elastic net trong **glmnet 4.1+** cho *mọi* họ GLM và mô hình Cox có tầng — công cụ cho điểm số đa gene, sống sót, và dự báo lâm sàng chiều cao. Bertrand, Klopfenstein, Bannier, Gidel và Massias (2022) phát hành **skglm**, bộ giải scikit-learn dùng working set và kiểm định dual-gap (lại là bao hàm subdifferential) để khớp GLM thưa với hàng triệu đặc trưng trong vài giây. Guha, Ndiaye và Huo (2023) dùng homotopy Lasso — đúng các bước nhảy active-set bạn thấy từ $$\partial\|\cdot\|_1$$ — để tính **tập dự báo conformal** cho GLM thưa mà không khớp lại tại mọi ứng viên đáp.

**Điểm nhớ.** Soft-thresholding không phải mẹo bài tập; nó là ánh xạ proximal của $$\lambda\|\cdot\|_1$$ và lý do một cột có thể được chứng nhận không hoạt động.

## 3. Pinball, phân vị, và khoảng không phụ thuộc phân phối

Hàm pinball (check) $$\rho_\tau(r)=\tau r_+ +(1-\tau)(-r)_+$$ lồi và từng khúc tuyến tính. Phân vị mẫu là cực tiểu của $$\sum_i\rho_\tau(y_i-x_i^\top\beta)$$; subgradient theo phần dư là $$\tau$$ phía trên không, $$\tau-1$$ phía dưới, và $$[\tau-1,\tau]$$ tại gãy. Conformalised quantile regression (Romano, Patterson và Candès, 2019) bọc khớp không trơn ấy bằng một bước hiệu chuẩn; Angelopoulos và Bates (2023) là sổ tay 2023 dùng trong pipeline thị giác và NLP khi cần **khoảng 90%**, không phải một điểm. Bài ICML 2023 ở trên là phiên bản thưa, chiều cao.

## 4. Năm dòng kiểm tra bạn có thể chạy

Đoạn sau in một subgradient của $$\|x\|_1$$ và của ReLU tại gốc — hai điểm gãy sinh viên gặp trước.

```python
import numpy as np

def subgrad_l1(x):
    g = np.sign(x)
    g[x == 0] = 0.0  # một phần tử của [-1, 1]
    return g

def relu_elem(t, kink=0.0):
    return 0.0 if t < 0 else (1.0 if t > 0 else kink)

x = np.array([1.2, 0.0, -0.4])
print(subgrad_l1(x), relu_elem(0.0))
```

Đổi giá trị tại gãy không đổi bất đẳng thức lồi; nó *có* đổi chiều ngược của mạng sâu. Đó là câu chuyện trường bảo toàn thu nhỏ.

## Cần nhớ

Subgradient là chứng chỉ tối ưu của mô hình lồi không trơn, và một lựa chọn bảo toàn của nó là thứ autodiff hiện đại thực sự lấy đạo hàm. Khi bài báo nói “chúng tôi huấn luyện mạng ReLU / GLM-Lasso / đầu phân vị,” đối tượng bậc nhất chính là đối tượng định nghĩa trong chương này.

**Câu hỏi.** Nếu một tọa độ Lasso thỏa $$|X_j^\top(y-X\hat\beta)|<\lambda$$, vì sao có thể xóa cột $$j$$ mà không đổi $$\hat\beta$$? Hình học ấy giống đơn vị ReLU đứng im như thế nào?

## Nguồn

- Bolte, J., & Pauwels, E. (2021). Conservative set valued fields, automatic differentiation, stochastic gradient methods and deep learning. *Mathematical Programming*, 188, 19–51. [doi:10.1007/s10107-020-01501-5](https://doi.org/10.1007/s10107-020-01501-5)
- Bolte, J., Boustany, R., Pauwels, E., & Pesquet, B. (2022). On the complexity of nonsmooth automatic differentiation. [arXiv:2206.01730](https://arxiv.org/abs/2206.01730)
- Blondel, M., & Roulet, V. (2024). *The Elements of Differentiable Programming*. [arXiv:2403.14606](https://arxiv.org/abs/2403.14606)
- Tay, J. K., Narasimhan, B., & Hastie, T. (2023). Elastic net regularization paths for all generalized linear models. *Journal of Statistical Software*, 106(1), 1–31. [doi:10.18637/jss.v106.i01](https://doi.org/10.18637/jss.v106.i01)
- Bertrand, Q., Klopfenstein, Q., Bannier, P.-A., Gidel, G., & Massias, M. (2022). Beyond L1: Faster and better sparse models with skglm. *NeurIPS*.
- Guha, E. K., Ndiaye, E., & Huo, X. (2023). Conformalization of sparse generalized linear models. *ICML*, PMLR 202.
- Angelopoulos, A. N., & Bates, S. (2023). Conformal prediction: A gentle introduction. *Foundations and Trends in Machine Learning*, 16(4).
- Romano, Y., Patterson, E., & Candès, E. J. (2019). Conformalized quantile regression. *NeurIPS*. (nền cho pipeline pinball + hiệu chuẩn)
