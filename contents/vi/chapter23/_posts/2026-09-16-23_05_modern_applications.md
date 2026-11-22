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


Hạ theo tọa độ dọc đường chính quy hóa (pathwise coordinate descent) là lý do giúp hồi quy Lasso trở thành công cụ tiêu chuẩn trong thống kê ứng dụng thay vì chỉ dừng ở mức nghiên cứu lý thuyết. Thư viện **glmnet** của Friedman, Hastie và Tibshirani (JSS 2010) vẫn được sử dụng rộng rãi trong R, còn `lasso_path` và `enet_path` của scikit-learn triển khai cùng ý tưởng bằng Cython. Bài đọc tùy chọn này cập nhật bối cảnh giai đoạn 2023–2026: `glmnet` mở rộng cho *mọi* họ mô hình tuyến tính tổng quát (GLM), các kỹ thuật sàng lọc an toàn và tập hoạt động ở quy mô hàng triệu đặc trưng, cùng bộ giải hạ theo tọa độ đối ngẫu tiếp tục phục vụ huấn luyện SVM tuyến tính trong thực tế.

Mỗi bước tọa độ tuần hoàn (hoặc ngẫu nhiên) trên hàm mục tiêu hợp thành $$f(\beta)+ \lambda\|\beta\|_1$$ chỉ là một phép co ngưỡng mềm vô hướng. Toàn bộ **đường chính quy hóa** là vòng lặp khởi động nóng (warm start) trên lưới giá trị giảm dần $$\lambda_1>\cdots>\lambda_T$$. Dưới đây là những hệ thống thực tế xây dựng trên nền tảng thuật toán đó.

## 1. glmnet cho mọi họ GLM (2023)

Tay, Narasimhan và Hastie, *Elastic Net Regularization Paths for All Generalized Linear Models*, *Journal of Statistical Software* 106(1):1–31, 2023, [doi:10.18637/jss.v106.i01](https://doi.org/10.18637/jss.v106.i01), mở rộng `glmnet 4.x` vượt ra ngoài các họ phân phối cố định (Gaussian, nhị thức, Poisson, Cox). Mọi mô hình GLM có hàm log-hợp lý trơn đều có thể tính đường chính quy hóa elastic-net bằng hạ theo tọa độ tuần hoàn. Phiên bản 4.1 (tài liệu giai đoạn 2021–2023 tại [glmnet.stanford.edu](https://glmnet.stanford.edu/)) bổ sung hỗ trợ dữ liệu phân tích sống còn dạng `(start, stop)`, phân tầng (strata) và ma trận đặc trưng $$X$$ thưa.

Đây là tài liệu trực tiếp trả lời câu hỏi thường gặp: “Ta mới học Lasso trên bình phương tối thiểu — liệu hạ theo tọa độ còn hiệu quả với hồi quy logistic, Cox hay các GLM tùy chỉnh không?” Câu trả lời là có, vì vòng lặp ngoài IRLS / proximal-Newton đưa mỗi bước về một bài toán Lasso bình phương tối thiểu *có trọng số*, và bài toán vòng trong chính là thuật toán hạ theo tọa độ ở mục 23-03.

## 2. Đường chính quy hóa trong scikit-learn và sàng lọc an toàn theo khoảng cách đối ngẫu

Các hàm `sklearn.linear_model.lasso_path` và `enet_path` (scikit-learn phiên bản 1.5–1.9) chạy hạ theo tọa độ trên mảng lưu theo thứ tự Fortran kết hợp **quy tắc sàng lọc an toàn theo khoảng cách đối ngẫu (gap-safe screening)**: ngay khi khoảng cách đối ngẫu chứng nhận một tọa độ chắc chắn bằng 0 tại nghiệm, tọa độ đó bị loại khỏi các bước cập nhật còn lại của mức $$\lambda$$ hiện tại. Các cải tiến bảo trì giai đoạn 2025–2026 (như tính trước phần dư và chuẩn cột dọc theo đường nghiệm) giúp một bộ dữ liệu biểu hiện gen với $$p\sim 10^4$$ đặc trưng vẫn khớp xong đường 100 điểm trong vài giây. Khi gọi `LassoCV`, bên dưới chính là thuật toán Chương 23 chứ không phải Adam.

## 3. skglm: tập hoạt động cho các hàm phạt ngoài $$\ell_1$$ (NeurIPS 2022)

Bertrand, Klopfenstein, Blondel, Vaiter, Gramfort và Massias, *Beyond L1: Faster and Better Sparse Models with skglm*, NeurIPS 2022, [bài báo](https://proceedings.neurips.cc/paper_files/paper/2022/hash/fe5c31e525e9a26a1426ab0b589f42fe-Abstract-Conference.html), mở rộng hạ theo tọa độ vượt ra ngoài phạm vi của `glmnet`. Kỹ thuật **tập hoạt động (working set)** mở rộng dần tập đặc trưng tích cực cỡ nhỏ, kết hợp tăng tốc Anderson (Bertrand & Massias, 2021) nhằm cải thiện tốc độ thực tế. Thư viện hỗ trợ các hàm phạt không lồi MCP / SCAD, chuẩn nhóm, học đa nhiệm và hàm khớp dữ liệu tùy chỉnh — hiện thực hóa hạng mục “hàm phạt không lồi” đã nêu ở mục 23-00 thành gói phần mềm cài đặt trực tiếp qua `pip`. Các ứng dụng chính trong bài báo gồm hệ gen học, học từ điển thị giác và bài toán ngược M/EEG; kết quả thực nghiệm cho thấy hạ theo tọa độ kết hợp tập hoạt động vượt trội phương pháp proximal gradient đầy đủ khi $$p$$ lên tới hàng triệu.

## 4. Hạ theo tọa độ đối ngẫu cho SVM tuyến tính

Hsieh, Chang, Lin, Keerthi và Sundararajan (ICML 2008) đề xuất huấn luyện SVM tuyến tính bằng hạ theo tọa độ đối ngẫu; **LIBLINEAR** đến nay vẫn là bộ giải cốt lõi đằng sau `sklearn.svm.LinearSVC` và nhiều hệ thống phân loại văn bản trong công nghiệp. Mỗi bước cập nhật tọa độ đối ngẫu chỉ là cực tiểu hóa một hàm bậc hai một chiều có chặn biên. Sự phổ biến của các mô hình transformer không làm phương pháp này lỗi thời: các mô hình cơ sở logistic/SVM trên đặc trưng túi từ, mô hình dự đoán tỉ lệ nhấp (CTR) và GLM trên dữ liệu bảng nhiều chiều vẫn là thế mạnh của coordinate descent. Nói ngắn gọn, hãy dùng AdamW (Chương 26) cho mạng sâu và dùng `glmnet` / LIBLINEAR / `skglm` cho các mô hình *tuyến tính tổng quát có tính thưa*.

```python
# Pathwise CD gói gọn trong một lời gọi thư viện — nền tảng là thuật toán Chương 23
from sklearn.linear_model import lasso_path
from sklearn.datasets import make_regression
X, y = make_regression(n_samples=400, n_features=80, n_informative=8, noise=8.0)
alphas, coefs, _ = lasso_path(X, y, eps=1e-3)
# coefs.shape == (n_features, n_alphas); quan sát thứ tự các đặc trưng bước vào đường nghiệm
```

**Bài tập.** Trên dữ liệu sinh bởi `make_regression` với $$p=200$$, $$n=150$$ và 5 đặc trưng có thông tin, vẽ đường hệ số của `lasso_path` theo $$-\log\lambda$$. Sau đó khớp cùng đường nghiệm bằng `skglm` (hoặc tự viết vòng lặp co ngưỡng mềm tuần hoàn nếu không cài thêm thư viện) và kiểm tra xem tập đặc trưng khác 0 (*support*) có khớp nhau tại giá trị $$\lambda$$ chọn bằng kiểm chứng chéo hay không. Cuối cùng, huấn luyện `LinearSVC` trên một tập con túi từ của bộ dữ liệu 20-newsgroups và so sánh thời gian chạy thực tế (wall-clock time) với mô hình hồi quy logistic huấn luyện bằng Adam theo minibatch với cùng chuẩn phạt $$\ell_2$$: coordinate descent sẽ nhanh hơn trên mô hình tuyến tính, còn Adam chỉ phát huy ưu thế khi bổ sung thêm lớp ẩn phi tuyến.

## Nguồn

- J. Friedman, T. Hastie, R. Tibshirani, *J. Stat. Softw.* 33(1), 2010 — glmnet pathwise CD.
- J. K. Tay, B. Narasimhan, T. Hastie, *J. Stat. Softw.* 106(1):1–31, 2023 — đường elastic-net cho mọi GLM.
- Q. Bertrand et al., NeurIPS 2022 — skglm, working set, mô hình thưa không lồi.
- C.-J. Hsieh et al., ICML 2008 — CD đối ngẫu cho SVM tuyến tính (LIBLINEAR).
- Hướng dẫn scikit-learn, *Coordinate descent* / gap-safe screening (v1.5+).
- S. J. Wright, *Math. Programming* 151:3–34, 2015 — khảo sát thuật toán CD.
