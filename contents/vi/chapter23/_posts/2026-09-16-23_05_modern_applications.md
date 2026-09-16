---
layout: post
title: 23-05 Ứng dụng hiện đại của hạ theo tọa độ
chapter: '23'
order: 6
owner: Nguyen Le Linh
categories:
- chapter23
lang: vi
lesson_type: optional
---


Hạ theo tọa độ theo đường regularization là lý do Lasso trở thành *nút mặc định* trong thống kê ứng dụng chứ không phải nguyên mẫu nghiên cứu. **glmnet** của Friedman, Hastie và Tibshirani (JSS 2010) vẫn chạy trên R; `lasso_path` / `enet_path` của scikit-learn là cùng ý tưởng trong Cython. Ghi chú tùy chọn này cập nhật câu chuyện tới 2023–2026: glmnet cho *mọi* họ GLM, screening và working set ở triệu đặc trưng, và bộ giải CD đối ngẫu vẫn huấn luyện SVM tuyến tính trong sản xuất.

Một bước tọa độ cyclic (hoặc ngẫu nhiên) trên mục tiêu hợp thành $$f(\beta)+ \lambda\|\beta\|_1$$ là soft-threshold vô hướng. Toàn bộ **đường regularization** là vòng lặp khởi động nóng trên lưới giảm $$\lambda_1>\cdots>\lambda_T$$. Đó là thuật toán; các ứng dụng dưới đây là những gì người thực hành thực sự chạy.

## 1. glmnet cho mọi GLM (2023)

Tay, Narasimhan và Hastie, *Elastic Net Regularization Paths for All Generalized Linear Models*, *Journal of Statistical Software* 106(1):1–31, 2023, [doi:10.18637/jss.v106.i01](https://doi.org/10.18637/jss.v106.i01), mở glmnet 4.x ra ngoài các họ Gaussian / binomial / Poisson / Cox có sẵn. Mọi GLM với log-likelihood trơn nay có đường elastic-net cyclic. Phiên bản 4.1 (cùng mã, tài liệu 2021–2023 tại [glmnet.stanford.edu](https://glmnet.stanford.edu/)) thêm dữ liệu sống còn `(start, stop)`, strata, và $$X$$ thưa.

Đây là bài báo để trích dẫn khi sinh viên hỏi “ta học Lasso trên bình phương tối thiểu — CD còn thắng cho logistic, Cox, hay GLM tùy chỉnh?” Có, vì vòng ngoài IRLS / proximal-Newton đưa mỗi bước về Lasso bình phương tối thiểu *có trọng số*, và bài toán trong đó đúng là hạ theo tọa độ bạn đã viết ở 23-03.

## 2. Đường scikit-learn và screening an toàn theo khe

`sklearn.linear_model.lasso_path` và `enet_path` (tài liệu hiện tại: scikit-learn 1.5–1.9) chạy hạ theo tọa độ thứ tự Fortran với **quy tắc screening an toàn theo khe**: một khi khe đối ngẫu chứng nhận một tọa độ ở lại số không, nó bị loại cho phần còn lại của $$\lambda$$ đó. Các PR bảo trì 2025–2026 (ví dụ tiền tính phần dư và chuẩn cột xuyên suốt một đường) không phải toán mới; chúng là lý do một microarray leukemia với $$p\sim 10^4$$ gene vẫn khớp đường 100 điểm trong vài giây. Khi bạn viết `LassoCV`, bạn đang chạy Chương 23, không phải Adam.

## 3. skglm: working set vượt $$\ell_1$$ (NeurIPS 2022)

Bertrand, Klopfenstein, Blondel, Vaiter, Gramfort và Massias, *Beyond L1: Faster and Better Sparse Models with skglm*, NeurIPS 2022, [bài báo](https://proceedings.neurips.cc/paper_files/paper/2022/hash/fe5c31e525e9a26a1426ab0b589f42fe-Abstract-Conference.html), đẩy hạ theo tọa độ qua bộ đặc trưng glmnet. **Working set** lần lượt phóng tập tích cực nhỏ; tăng tốc Anderson (Bertrand & Massias, 2021) cho tăng tốc thực tế mà Nesterov-trên-CD thường không có. Gói xử lý MCP / SCAD, chuẩn nhóm và đa nhiệm, và data-fit tùy chỉnh — gạch đầu dòng “penalty không lồi” đã có trên landing 23-00, nay kèm phần mềm `pip install`. Genomics, từ điển thị giác, và bài toán ngược M/EEG là ứng dụng chạy trong bài báo; khẳng định tối ưu là CD cộng working set vẫn át phương pháp proximal gradient đầy đủ khi $$p$$ vào hàng triệu.

## 4. Hạ theo tọa độ đối ngẫu cho SVM tuyến tính

Hsieh, Chang, Lin, Keerthi và Sundararajan (ICML 2008) huấn luyện SVM tuyến tính bằng hạ theo tọa độ đối ngẫu; **LIBLINEAR** vẫn là bộ giải sau `sklearn.svm.LinearSVC` và một phần lớn bộ phân loại văn bản công nghiệp. Mỗi tọa độ đối ngẫu là một quadratic 1-D bị cắt. Không có gì ở thuật toán đó lỗi thời vì transformer xuất hiện: baseline logistic / SVM túi từ, mô hình click, và GLM bảng chiều cao vẫn là sân nhà của CD. Dùng AdamW (Chương 26) cho mạng sâu; dùng glmnet / LIBLINEAR / skglm khi mô hình *tuyến tính tổng quát và thưa*.

```python
# Pathwise CD là một lời gọi thư viện — thuật toán là Chương 23
from sklearn.linear_model import lasso_path
from sklearn.datasets import make_regression
X, y = make_regression(n_samples=400, n_features=80, n_informative=8, noise=8.0)
alphas, coefs, _ = lasso_path(X, y, eps=1e-3)
# coefs.shape == (n_features, n_alphas); đếm feature vào đường muộn thế nào
```

**Bài tập.** Trên `make_regression` với $$p=200$$, $$n=150$$, năm đặc trưng thông tin, vẽ hệ số glmnet / `lasso_path` theo $$-\log\lambda$$. Rồi khớp cùng đường bằng skglm (hoặc soft-threshold cyclic tự viết nếu bỏ qua phụ thuộc thêm) và kiểm tra *support* khớp trên $$\lambda$$ chọn bằng kiểm chứng chéo. Cuối cùng, huấn luyện `LinearSVC` trên một tập con túi từ 20-newsgroups và báo thời gian tường so với mạng logistic Adam minibatch cùng quả cầu $$\ell_2$$. CD phải thắng trên mô hình tuyến tính; Adam chỉ thắng sau khi bạn thêm một lớp ẩn.

## Nguồn

- J. Friedman, T. Hastie, R. Tibshirani, *J. Stat. Softw.* 33(1), 2010 — glmnet pathwise CD.
- J. K. Tay, B. Narasimhan, T. Hastie, *J. Stat. Softw.* 106(1):1–31, 2023 — đường elastic-net cho mọi GLM.
- Q. Bertrand et al., NeurIPS 2022 — skglm, working set, mô hình thưa không lồi.
- C.-J. Hsieh et al., ICML 2008 — CD đối ngẫu cho SVM tuyến tính (LIBLINEAR).
- Hướng dẫn scikit-learn, *Coordinate descent* / gap-safe screening (v1.5+).
- S. J. Wright, *Math. Programming* 151:3–34, 2015 — khảo sát thuật toán CD.
