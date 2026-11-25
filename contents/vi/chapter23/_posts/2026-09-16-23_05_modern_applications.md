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

Nếu bạn từng nghĩ hạ theo tọa độ chỉ là một mẹo hay cho bài toán Lasso bậc hai cổ điển, bức tranh công nghiệp giai đoạn 2022–2026 sẽ khiến bạn bất ngờ. Khi chạy `LassoCV` hay `LinearSVC` trong `scikit-learn`, khớp mô hình sống còn Cox trong `glmnet 4.x`, hay giải bài toán ngược tín hiệu não M/EEG hàng triệu chiều bằng `skglm`, động cơ thực sự đang chạy hết công suất bên dưới không phải Adam mà chính là **hạ theo tọa độ** được trang bị thêm hai vũ khí hiện đại: **sàng lọc an toàn theo khoảng cách đối ngẫu (gap-safe screening)** và **tăng tốc Anderson**.

Bài đọc này nối trực tiếp lý thuyết Chương 23 với các thư viện mã nguồn mở chuẩn mực đang vận hành hàng ngày trong thống kê sinh học, xử lý ngôn ngữ tự nhiên quy mô nhẹ và dữ liệu bảng nhiều chiều.

## Bản đồ kiến thức nền: Bốn mảnh ghép công nghệ biến CD thành bộ giải triệu chiều

Để nắm được vì sao các thư viện hiện đại lại đạt tốc độ vượt trội trên dữ liệu siêu cao chiều ($$p \gg n$$), hãy chú ý bốn trụ cột kỹ thuật sau:

- **Vòng ngoài Proximal-Newton / IRLS (trong `glmnet 4.x`):** Mọi mô hình tuyến tính tổng quát (logistic, Poisson, Cox) đều có hàm log-hợp lý trơn; xấp xỉ bậc hai cục bộ đưa mỗi bước ngoài về một bài toán Lasso bình phương tối thiểu *có trọng số*, cho phép tái sử dụng nguyên vẹn lõi CD của mục 23-03.
- **Sàng lọc an toàn theo khoảng cách đối ngẫu (Gap-Safe Screening):** Dựa trên khoảng cách đối ngẫu $$G = P(\beta) - D(\theta)$$, ta dựng được một hình cầu chắc chắn chứa nghiệm đối ngẫu tối ưu $$\theta^\star$$. Đặc trưng nào có tích vô hướng với mọi điểm trong hình cầu đều nhỏ hơn $$1$$ thì chắc chắn có $$\beta_j^\star = 0$$ và bị loại vĩnh viễn khỏi bộ nhớ.
- **Tập hoạt động + Tăng tốc Anderson (trong `skglm`):** Mở rộng ra ngoài chuẩn $$\ell_1$$ sang các hàm phạt không lồi (MCP, SCAD) hay chuẩn nhóm, kết hợp ngoại suy tổ hợp tuyến tính các bước lặp gần nhất (Anderson acceleration) để rút ngắn mạnh số vòng lặp.
- **Hạ theo tọa độ đối ngẫu (Dual CD trong LIBLINEAR):** Với SVM tuyến tính khi số mẫu lớn và đặc trưng thưa (văn bản túi từ, dự đoán CTR), bài toán đối ngẫu có ràng buộc hộp $$0 \le \alpha_i \le C$$ đơn giản, nên mỗi bước CD chỉ là cắt ngưỡng một nghiệm bậc hai 1 chiều.

### Khung giải thích (nên đọc chậm): Tính tay quy tắc sàng lọc an toàn (Gap-Safe Screening)

Hãy tự tay chứng nhận một đặc trưng chắc chắn bằng $$0$$ tại nghiệm tối ưu mà **chưa cần giải xong bài toán**! Xét Lasso với hai cột trực chuẩn $$X_1 = (1, 0)^T, X_2 = (0, 1)^T$$ ($$\|X_1\|_2 = \|X_2\|_2 = 1$$), nhãn $$y = (3,\; 0.2)^T$$ và $$\lambda = 1$$.

Giả sử sau vài vòng lặp, ta đang ở điểm hiện tại $$\beta = (1.8,\; 0)$$ (chưa phải nghiệm tối ưu $$(2, 0)$$).

1. **Tính phần dư và điểm khả thi đối ngẫu $$\theta$$:**
   Phần dư $$r = y - X\beta = (3 - 1.8,\; 0.2 - 0)^T = (1.2,\; 0.2)^T$$.
   Điều kiện khả thi đối ngẫu của Lasso là $$\|X^T \theta\|_\infty \le 1$$. Ta chuẩn hóa $$r$$ bằng hệ số $$\max(\lambda, \|X^T r\|_\infty) = \max(1, 1.2) = 1.2$$:
   $$\theta = \frac{r}{1.2} = \left(1,\; \frac{1}{6}\right)^T \approx (1,\; 0.1667)^T.$$
2. **Tính khoảng cách đối ngẫu $$G = P(\beta) - D(\theta)$$:**
   - Giá trị gốc: $$P(\beta) = \frac{1}{2}\|r\|_2^2 + \lambda\|\beta\|_1 = \frac{1}{2}(1.2^2 + 0.2^2) + 1.8 = 0.74 + 1.8 = 2.54$$.
   - Giá trị đối ngẫu chuẩn của Lasso: $$D(\theta) = \frac{1}{2}\|y\|_2^2 - \frac{\lambda^2}{2}\left\|\theta - \frac{y}{\lambda}\right\|_2^2 = \frac{9.04}{2} - \frac{1}{2}\left((1 - 3)^2 + \left(\frac{1}{6} - 0.2\right)^2\right) \approx 4.52 - 2.00056 = 2.51944$$.
   - Khoảng cách đối ngẫu: $$G = 2.54 - 2.51944 = 0.02056$$.
3. **Áp dụng phép thử hình cầu an toàn cho đặc trưng $$j = 2$$:**
   Bán kính hình cầu chứa $$\theta^\star$$ là $$r_{\text{safe}} = \frac{\sqrt{2G}}{\lambda} \approx \sqrt{0.04112} \approx 0.2028$$.
   Kiểm tra cận trên cho $$|X_2^T \theta^\star|$$:
   $$|X_2^T \theta| + \|X_2\|_2 \cdot r_{\text{safe}} \approx 0.1667 + 1 \cdot 0.2028 = 0.3695 < 1!$$
4. **Kết luận:** Vì $$|X_2^T \theta^\star| < 1$$ được **chứng minh chặt chẽ về mặt toán học**, theo điều kiện KKT thì $$\beta_2^\star$$ **bắt buộc bằng 0**. Thuật toán loại bỏ hoàn toàn cột $$X_2$$ khỏi mọi vòng lặp còn lại mà không đánh mất dù chỉ một chữ số chính xác nào!

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
