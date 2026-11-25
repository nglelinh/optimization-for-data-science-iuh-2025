---
layout: post
title: 07-11 Ứng dụng hiện đại của subgradient
chapter: '07'
order: 15
owner: Nguyen Le Linh
categories:
- chapter07
lang: vi
lesson_type: optional
---

Từ các mô hình ngôn ngữ khổng lồ sử dụng khối kích hoạt không trơn (ReLU, GeLU cắt ngưỡng, chuẩn $$\ell_1$$) cho tới các hệ thống dự báo chuỗi thời gian năng lượng đòi hỏi khoảng tin cậy 90%–95% chống lại biến động cực đoan, **giải tích không trơn (nonsmooth analysis)** của Chương 07 không còn là chuyên đề phụ lục của tối ưu hóa lồi — mà đã trở thành ngôn ngữ nền tảng để hiểu cách các hệ thống học máy thực sự hành xử tại những "điểm gấp nếp".

Phiên bản chuyên đề ứng dụng này tổng hợp và mở rộng góc nhìn thực chiến về ba cột trụ ứng dụng của subgradient trong giai đoạn hiện đại: lý thuyết hội tụ của vi phân tự động trên mạng không trơn, các bộ giải tối ưu thưa quy mô triệu đặc trưng, và ước lượng phân vị kết hợp dự báo đồng dạng (Conformal Prediction).

## Bản đồ kiến thức nền: Kết nối Subgradient với Hệ sinh thái Học máy Hiện đại

Bốn cầu nối sau giúp bạn nhìn thấy sự hiện diện của $$\partial f(x)$$ đằng sau các công cụ lập trình hàng ngày:

- **Cầu nối 1 — Subdifferential Clarke & Trường bảo toàn (Conservative Fields):** Mở rộng khái niệm vi phân dưới từ hàm lồi sang hàm Lipschitz phi lồi (như mạng nơ-ron sâu ghép nhiều lớp ReLU), giải thích tại sao SGD trên PyTorch không bị phá vỡ dù hàm mất mát không khả vi trên một hợp các siêu phẳng!
- **Cầu nối 2 — Tối ưu hóa Tọa độ & Sàng lọc KKT (Coordinate Descent + Screening):** Dùng trực tiếp bất đẳng thức $$|X_j^T(y - X\beta)| \le \lambda$$ để bỏ qua các biến 0 và cập nhật từng tọa độ bằng Soft-Thresholding với tốc độ nhanh hơn phương pháp điểm trong hàng trăm lần trên dữ liệu thưa.
- **Cầu nối 3 — Dự báo Khoảng bất định bằng Pinball Loss:** Dùng hàm mất mát gãy khúc bất đối xứng $$\rho_\tau$$ để học đồng thời cận dưới ($$\tau = 0.05$$) và cận trên ($$\tau = 0.95$$), sau đó hiệu chỉnh bằng Conformal Prediction để có bảo đảm phủ xác suất toán học chặt chẽ.
- **Cầu nối 4 — Phương pháp Subgradient vs. Proximal Gradient:** Khi hàm mục tiêu có dạng $$f(x) + g(x)$$ (trơn + không trơn như Lasso), thay vì dùng phương pháp Subgradient chậm $$O(1/\sqrt{k})$$, thực tế tách phần không trơn ra xử lý bằng **toán tử Proximal** (như Soft-Thresholding) để khôi phục lại tốc độ $$O(1/k)$$ và $$O(1/k^2)$$!

### Khung giải thích (nên đọc chậm): Minh họa quy tắc Sàng lọc KKT cho Lasso trên 3 đặc trưng

Giả sử ta giải Lasso $$\min_\beta \frac{1}{2}\|y - X\beta\|_2^2 + \lambda\|\beta\|_1$$ với $$\lambda = 2.0$$, các cột dữ liệu chuẩn hóa $$\|X_j\|_2 = 1$$ và giá trị tương quan ban đầu với $$y$$ là:
$$X_1^T y = 5.0, \qquad X_2^T y = 0.4, \qquad X_3^T y = -3.1.$$

1. **Bước 1 — Ý tưởng sàng lọc từ điều kiện subgradient:**
   Điều kiện để $$\beta_j^\star = 0$$ là $$|X_j^T(y - X\beta^\star)| \le \lambda$$.
   Theo bất đẳng thức tam giác và Cauchy-Schwarz (với $$\|X_j\|_2 = 1$$):
   $$|X_j^T(y - X\beta^\star)| \le |X_j^T y| + \|X_j\|_2 \|X\beta^\star\|_2 = |X_j^T y| + \|X\beta^\star\|_2.$$
2. **Bước 2 — Ước lượng cận trên thô cho $$\|X\beta^\star\|_2$$:**
   Giả sử tại điểm khởi tạo hoặc từ nghiệm đối ngẫu ta biết chắc $$\|X\beta^\star\|_2 \le 1.2$$.
   Kiểm tra cho đặc trưng 2 ($$|X_2^T y| = 0.4$$):
   $$|X_2^T(y - X\beta^\star)| \le 0.4 + 1.2 = 1.6 < \lambda = 2.0!$$
3. **Bước 3 — Kết luận an toàn tuyệt đối (Safe Screening):**
   Không cần chạy thêm bất kỳ vòng lặp nào trên đặc trưng 2, điều kiện subgradient đảm bảo 100% rằng $$\beta_2^\star = 0$$! Trong dữ liệu thực có $$p = 100\,000$$ đặc trưng, quy tắc sàng lọc như thế này giúp vứt bỏ ngay >95% cột dữ liệu vô ích!

---

# Ứng dụng hiện đại của subgradient

Bài đọc tùy chọn này **không** lặp lại các phép tính cơ bản của Chương 07, mà chỉ ra nơi các khái niệm đó — một vector $$g$$ thỏa mãn $$f(y)\ge f(x)+g^\top(y-x)$$, tập vi phân dưới $$\partial f(x)$$, và điều kiện dừng $$0\in\partial f(x^\star)$$ — xuất hiện trong các hệ thống khoa học máy tính và khoa học dữ liệu giai đoạn 2022–2026. Sau bài này, bạn có thể nhận diện một hàm mất mát hoặc thành phần chính quy hóa không trơn trong hệ thống thực tế, viết được điều kiện bao hàm đặc trưng cho nghiệm tối ưu, và liên hệ trực tiếp với các công trình nghiên cứu nền tảng.

## Vì sao subgradient vẫn giữ vai trò cốt lõi

Mạng ReLU, chọn đặc trưng bằng chuẩn $$\ell_1$$, hàm mất mát pinball (cho hồi quy phân vị) và hàm mất mát Huber đều là những thành phần **lồi không trơn hoặc khả vi theo đường (path-differentiable)**. Các thư viện vi phân tự động như PyTorch hay JAX vẫn trả về một vector tại điểm gấp khúc; khái niệm toán học chính xác cho đối tượng đó là **trường bảo toàn** (conservative field), vốn trùng với subgradient trên các thành phần lồi và trùng với vi phân Clarke hầu khắp nơi. Nếu chỉ dựa vào quy tắc “gradient bằng không tại cực tiểu”, ta không thể phân tích tập giá (support) của Lasso, hiện tượng nút ReLU bất hoạt, hay nghiệm của bài toán hồi quy phân vị.

## 1. Mạng ReLU và vi phân tự động không trơn

Hàm kích hoạt chỉnh lưu $$\operatorname{ReLU}(t)=\max\{t,0\}$$ có vi phân dưới:

$$
\partial\operatorname{ReLU}(t)=\begin{cases}\{0\} & t<0,\\ [0,1] & t=0,\\ \{1\} & t>0.\end{cases}
$$

Một mạng nơ-ron sâu tạo từ các phép biến đổi affine và hàm ReLU có tính liên tục Lipschitz và nửa đại số (semialgebraic), do đó **khả vi theo đường**. Bolte và Pauwels (2021) chỉ ra rằng đối tượng mà lan truyền ngược (backpropagation) thực sự tính toán là một *trường đa trị bảo toàn* (conservative set-valued field): nó thỏa mãn quy tắc dây chuyền ngay cả khi vi phân Clarke của mạng ReLU không nhất thiết tuân theo quy tắc này. Bolte, Boustany, Pauwels và Pesquet (2022) chứng minh **nguyên lý gradient chi phí thấp cho hàm không trơn** đối với vi phân tự động chế độ ngược, đồng thời chỉ ra rằng bài toán tính *hai* phần tử Clarke khác nhau của một mạng ReLU đơn giản đã là NP-khó — vì vậy các thư viện thực tế chọn một phần tử cố định trong $$\partial\operatorname{ReLU}(0)$$ (thường là $$0$$) là điều có cơ sở lý thuyết. Blondel và Roulet (2024) hệ thống hóa cách tiếp cận này dưới khung *lập trình khả vi*: thiết kế chương trình sao cho tồn tại đạo hàm bảo toàn, rồi huấn luyện bằng SGD.

**Liên hệ với giáo trình.** Các quy tắc trong [07-02-02 Phép tính subgradient]({% multilang_post_url contents/chapter07/21-03-25-07_02_02_subgradient_calculus %}) (phép cộng, giá trị lớn nhất, hợp thành với ánh xạ affine) chính là các quy tắc trên đồ thị tính toán của mạng ReLU. Điều kiện $$0\in\partial f(x)$$ vẫn là tiêu chuẩn tối ưu bắt buộc đối với các bài toán lớp cuối lồi như SVM tuyến tính hay đầu ra Lasso.

## 2. Lasso, elastic net và các bộ giải GLM hiện đại

Bài toán Lasso

$$
\min_\beta\ \tfrac12\|y-X\beta\|_2^2+\lambda\|\beta\|_1
$$

là ví dụ xuyên suốt chương này: điều kiện dừng là $$X^\top(y-X\beta)=\lambda v$$ với $$v\in\partial\|\beta\|_1$$, nghĩa là $$v_j=\operatorname{sign}(\beta_j)$$ trên tập giá và $$|v_j|\le 1$$ ngoài tập giá ([07-03-03 Điều kiện tối ưu Lasso]({% multilang_post_url contents/chapter07/21-03-25-07_03_03_example_lasso_optimality_condition %})). Chính điều kiện bao hàm này là cơ sở để `glmnet` và `skglm` xác định tọa độ nào bằng không.

Tay, Narasimhan và Hastie (2023) mở rộng đường chính quy hóa elastic net trong **glmnet 4.1+** cho *mọi* họ mô hình tuyến tính tổng quát (GLM) và mô hình Cox phân tầng — công cụ quen thuộc cho điểm số đa gene, phân tích sống còn và dự báo lâm sàng nhiều chiều. Bertrand, Klopfenstein, Bannier, Gidel và Massias (2022) phát triển **skglm**, bộ giải tương thích scikit-learn sử dụng chiến lược tập làm việc (working set) kết hợp kiểm định khoảng cách đối ngẫu (dual gap, cũng dựa trên bao hàm vi phân dưới) để khớp các GLM thưa với hàng triệu đặc trưng chỉ trong vài giây. Guha, Ndiaye và Huo (2023) sử dụng kỹ thuật đồng luân (homotopy) của Lasso — bám theo đúng các bước chuyển tập hoạt động suy ra từ $$\partial\|\cdot\|_1$$ — để xây dựng **tập dự báo conformal** cho GLM thưa mà không cần huấn luyện lại cho từng giá trị đầu ra ứng viên.

**Điểm cần nhớ.** Toán tử ngưỡng mềm (soft-thresholding) không chỉ là một bài tập tính toán; nó là ánh xạ gần kề của $$\lambda\|\cdot\|_1$$ và là cơ sở để chứng nhận một cột đặc trưng không hoạt động.

## 3. Hàm mất mát pinball, phân vị và khoảng dự báo không phụ thuộc phân phối

Hàm mất mát pinball (còn gọi là hàm check) $$\rho_\tau(r)=\tau r_+ +(1-\tau)(-r)_+$$ là hàm lồi và tuyến tính từng khúc. Ước lượng phân vị mẫu là nghiệm cực tiểu của $$\sum_i\rho_\tau(y_i-x_i^\top\beta)$$; gradient dưới theo phần dư bằng $$\tau$$ khi phần dư dương, bằng $$\tau-1$$ khi phần dư âm, và thuộc đoạn $$[\tau-1,\tau]$$ tại điểm gấp khúc bằng không. Hồi quy phân vị conformal (Conformalized Quantile Regression — Romano, Patterson và Candès, 2019) kết hợp bước khớp không trơn này với một bước hiệu chuẩn để bảo đảm độ phủ thống kê; Angelopoulos và Bates (2023) trình bày tài liệu hướng dẫn được sử dụng rộng rãi trong các hệ thống thị giác máy tính và xử lý ngôn ngữ tự nhiên khi cần **khoảng dự báo 90%** thay vì dự báo điểm. Công trình ICML 2023 nêu trên là phiên bản mở rộng cho bài toán thưa nhiều chiều.

## 4. Đoạn mã kiểm tra ngắn

Đoạn mã sau tính một gradient dưới của $$\|x\|_1$$ và của hàm ReLU tại gốc tọa độ — hai điểm gấp khúc phổ biến nhất.

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

Việc thay đổi giá trị chọn tại điểm gấp khúc không làm thay đổi bất đẳng thức lồi, nhưng *có* làm thay đổi kết quả lan truyền ngược trong mạng sâu. Đó là minh họa trực quan nhất cho khái niệm trường bảo toàn.

## Tóm lược

Gradient dưới là chứng chỉ tối ưu cho các mô hình lồi không trơn, và một lựa chọn bảo toàn của nó chính là đối tượng mà các thư viện vi phân tự động hiện đại tính toán. Khi các bài báo đề cập đến việc huấn luyện mạng ReLU, GLM-Lasso hay hồi quy phân vị, đối tượng bậc nhất đằng sau đều quay về khái niệm được định nghĩa trong chương này.

**Câu hỏi.** Nếu một tọa độ trong bài toán Lasso thỏa mãn $$|X_j^\top(y-X\hat\beta)|<\lambda$$, vì sao ta có thể loại bỏ cột $$j$$ mà không làm thay đổi nghiệm $$\hat\beta$$? Về mặt hình học, hiện tượng này tương đồng như thế nào với một đơn vị ReLU không kích hoạt?

## Nguồn

- Bolte, J., & Pauwels, E. (2021). Conservative set valued fields, automatic differentiation, stochastic gradient methods and deep learning. *Mathematical Programming*, 188, 19–51. [doi:10.1007/s10107-020-01501-5](https://doi.org/10.1007/s10107-020-01501-5)
- Bolte, J., Boustany, R., Pauwels, E., & Pesquet, B. (2022). On the complexity of nonsmooth automatic differentiation. [arXiv:2206.01730](https://arxiv.org/abs/2206.01730)
- Blondel, M., & Roulet, V. (2024). *The Elements of Differentiable Programming*. [arXiv:2403.14606](https://arxiv.org/abs/2403.14606)
- Tay, J. K., Narasimhan, B., & Hastie, T. (2023). Elastic net regularization paths for all generalized linear models. *Journal of Statistical Software*, 106(1), 1–31. [doi:10.18637/jss.v106.i01](https://doi.org/10.18637/jss.v106.i01)
- Bertrand, Q., Klopfenstein, Q., Bannier, P.-A., Gidel, G., & Massias, M. (2022). Beyond L1: Faster and better sparse models with skglm. *NeurIPS*.
- Guha, E. K., Ndiaye, E., & Huo, X. (2023). Conformalization of sparse generalized linear models. *ICML*, PMLR 202.
- Angelopoulos, A. N., & Bates, S. (2023). Conformal prediction: A gentle introduction. *Foundations and Trends in Machine Learning*, 16(4).
- Romano, Y., Patterson, E., & Candès, E. J. (2019). Conformalized quantile regression. *NeurIPS*. (nền cho pipeline pinball + hiệu chuẩn)
