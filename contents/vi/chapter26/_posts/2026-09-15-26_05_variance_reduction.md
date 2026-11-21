---
layout: post
title: 26-05 Giảm phương sai — SVRG và SAGA
chapter: '26'
order: 6
owner: Nguyen Le Linh
categories:
- chapter26
lang: vi
lesson_type: required
---


Trần $$O(1/\sqrt{T})$$ của SGD trên tổng hữu hạn Lipschitz lồi không phải định mệnh lý thuyết thông tin. Đó là cái giá của một gradient *không chệch nhưng nhiễu* mà phương sai vẫn cỡ một ngay cả khi $$w$$ ngồi tại cực tiểu. Các phương pháp **giảm phương sai** tái sử dụng gradient cũ để ước lượng đúng tại một ảnh chụp (hoặc trong một bảng), và nhiễu tắt khi $$w$$ tiến tới cực tiểu. Bài này là lõi Opt-for-ML — SVRG và SAGA — ở độ sâu IUH: đủ đại số để thấy *vì sao* phương sai tắt, đủ thuật toán để cài, và một ranh giới rõ “đừng huấn luyện ResNet kiểu này”.

Bạn đã gặp đường nhiễu ở [26-01]({% multilang_post_url contents/chapter26/2026-09-15-26_01_sgd_and_minibatch %}) và hoạt họa batch-đối-ngẫu nhiên ở [08-02-04]({% multilang_post_url contents/chapter08/20-03-29-08_02_04_batch_vs_stochastic_methods %}). Mở lại [stochastic_gradient_demo.html](https://nglelinh.github.io/interactive_math/optimization/stochastic_gradient_demo.html) và xem đường vẫn rung *sau khi* đã vào chén: phần rung sót đó là bệnh trang này chữa.

## Bài toán tổng hữu hạn, và vì sao SGD không tuyến tính được

Rủi ro thực nghiệm là một trung bình,

$$
F(w)=\frac{1}{n}\sum_{i=1}^n f_i(w),\qquad
\nabla F(w)=\frac{1}{n}\sum_{i=1}^n \nabla f_i(w).
$$

Một bước SGD một mẫu dùng $$g_k=\nabla f_{I_k}(w_k)$$. Nếu $$I_k$$ đều và độc lập với $$w_k$$ thì $$\mathbb{E}[g_k\mid w_k]=\nabla F(w_k)$$ — không chệch — nhưng

$$
\mathbb{E}\bigl[\|g_k-\nabla F(w_k)\|_2^2\mid w_k\bigr]
$$

không nhất thiết về không khi $$w_k\to w^\star$$. Ngay tại cực tiểu, $$\nabla f_i(w^\star)$$ vẫn có thể là vector lớn chỉ *trung bình* về không (nghĩ mô hình tuyến tính đặc tả đúng mà phần dư vẫn có phương sai). SGD phương sai bị chặn trên mục tiêu Lipschitz lồi vì thế kẹt ở $$O(1/\sqrt{T})$$ theo giá trị hàm. Lồi mạnh không cứu bạn nếu sàn nhiễu là hằng: các vòng lặp nảy trong quả cầu bán kính tỉ lệ $$\eta\sigma$$.

Gradient descent cả lô *có* tuyến tính dưới lồi mạnh (Chương 06), nhưng mỗi bước tốn $$n$$ gradient. Giảm phương sai đòi tốc độ tuyến tính với chi phí gần một gradient mỗi bước.

## Ý tưởng biến kiểm soát

Chọn một ảnh chụp $$\tilde w$$ bất kỳ mà bạn sẵn sàng tính *một lần* gradient đầy đủ $$\mu=\nabla F(\tilde w)$$. Với chỉ số ngẫu nhiên $$I$$, vector

$$
g(w)=\nabla f_I(w)-\nabla f_I(\tilde w)+\mu
$$

vẫn không chệch cho $$\nabla F(w)$$:

$$
\mathbb{E}[g(w)]
=\nabla F(w)-\nabla F(\tilde w)+\nabla F(\tilde w)
=\nabla F(w).
$$

Khi $$w=\tilde w$$ ta có $$g(\tilde w)=\mu=\nabla F(\tilde w)$$ *chính xác* — nhiễu bằng không tại ảnh chụp. Khi $$w$$ gần $$\tilde w$$ và mỗi $$\nabla f_i$$ Lipschitz, $$\nabla f_I(w)-\nabla f_I(\tilde w)$$ nhỏ, nên phương sai của $$g$$ nhỏ. Đó là **biến kiểm soát** (control variate): ta trừ một bản sao tương quan của nhiễu rồi cộng lại kỳ vọng của nó.

## SVRG (Johnson & Zhang, 2013)

SVRG làm mới ảnh chụp trên vòng ngoài và đi với biến kiểm soát trên vòng trong.

**Vòng ngoài** $$s=0,1,\ldots,S-1$$

1. Đặt ảnh chụp $$\tilde w\leftarrow w$$ và tính $$\mu\leftarrow\nabla F(\tilde w)$$ (một lượt đầy đủ, $$n$$ gradient).
2. **Vòng trong** $$t=0,1,\ldots,m-1$$: rút $$I$$ đều, đặt
   $$
   g\leftarrow\nabla f_I(w)-\nabla f_I(\tilde w)+\mu,\qquad
   w\leftarrow w-\eta g.
   $$
3. Có thể trung bình đường trong, hoặc giữ $$w$$ cuối, rồi trở lại bước 1.

Chọn chuẩn là $$m=\Theta(n)$$ bước trong, nên chi phí *phân bổ* là một hằng nhỏ nhân một gradient mỗi bước: một gradient đầy đủ mỗi $$m$$ bước, cộng hai gradient ngẫu nhiên mỗi bước trong. Bộ nhớ ngoài vector tham số là một ảnh chụp $$\tilde w$$ và một vector $$\mu$$ — $$O(d)$$, không phụ thuộc $$n$$.

**Định lý (phác, tổng hữu hạn lồi mạnh).** Nếu mỗi $$f_i$$ trơn-$$L$$ và $$F$$ lồi mạnh-$$\mu$$, một $$\eta$$ hằng đủ nhỏ và $$m\gtrsim L/\mu$$ cho

$$
\mathbb{E}\bigl[F(\tilde w_{s+1})-F^\star\bigr]
\le \rho\,\mathbb{E}\bigl[F(\tilde w_s)-F^\star\bigr]
$$

với $$\rho<1$$ không phụ thuộc chân trời. Số gradient gia lượng để đạt độ chính xác $$\varepsilon$$ là $$O\bigl((n+\kappa)\log(1/\varepsilon)\bigr)$$, $$\kappa=L/\mu$$. SGD thuần không viết được một $$\log(1/\varepsilon)$$ kiểu này khi sàn nhiễu là hằng.

Chứng minh là lập luận Lyapunov: nhiễu vòng trong được khống chế bởi $$\|w-\tilde w\|$$, bản thân đại lượng đó co khi ảnh chụp tốt hơn. Bạn không bị đòi tái tạo các hằng số; bạn bị đòi chỉ vào dòng $$g=\nabla f_I(w)-\nabla f_I(\tilde w)+\mu$$ và nói vì sao phương sai tắt.

## SAGA (Defazio, Bach, Lacoste-Julien, 2014)

SAGA bỏ vòng ngoài bằng cách lưu một **bảng** $$g^{(1)},\ldots,g^{(n)}$$ gradient gần nhất của mỗi $$f_i$$. Khởi tạo $$g^{(i)}\leftarrow\nabla f_i(w_0)$$ (hoặc không, với một đoạn đốt ngắn) và giữ trung bình chạy $$\bar g=\frac1n\sum_i g^{(i)}$$.

Mỗi bước: rút $$I$$, tính gradient mới $$\nabla f_I(w)$$, đặt

$$
g\leftarrow \nabla f_I(w)-g^{(I)}+\bar g,
$$

rồi ghi $$g^{(I)}\leftarrow\nabla f_I(w)$$, cập nhật $$\bar g$$ trong $$O(d)$$ bằng thay đổi hạng một, và bước $$w\leftarrow w-\eta g$$.

Cùng đại số biến kiểm soát, nay với ảnh chụp *từng mẫu, cũ* thay vì một $$\tilde w$$ chung. Không có lượt đầy đủ định kỳ. Cái giá là bộ nhớ: $$n$$ vector gradient, $$O(nd)$$, hoặc $$O(n)$$ vô hướng với mô hình tuyến tính nơi $$\nabla f_i(w)=(x_i^\top w-y_i)x_i$$ và chỉ cần lưu phần dư. Đó là vì sao `sklearn.linear_model.LogisticRegression(solver="saga")` là mặc định sản xuất trên ERM lồi vừa, và vì sao SAGA vô vọng như bộ tối ưu *mạng sâu* — bạn sẽ không lưu bảng gradient cho ImageNet.

**SAG** (Schmidt, Le Roux, Bach) là anh em cũ bị chệch: nó dùng trung bình bảng *không* có hiệu chỉnh $$+\nabla f_I(w)-g^{(I)}$$. Hiệu chỉnh thêm của SAGA khôi phục không chệch và làm gọn chứng minh; ưu tiên SAGA trừ khi bạn đang đọc bài SAG 2013.

## Một vòng SVRG nhỏ

```python
import numpy as np

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-np.clip(z, -40.0, 40.0)))

def svrg_logistic(X, y, lam=1e-3, eta=0.1, inner=None, epochs=20):
    n, d = X.shape
    inner = n if inner is None else inner
    w = np.zeros(d)
    for _ in range(epochs):
        p = sigmoid(X @ w)
        mu = X.T @ (p - y) / n + lam * w          # gradient đầy đủ
        w_snap = w.copy()
        for _t in range(inner):
            i = np.random.randint(n)
            xi, yi = X[i], y[i]
            g = (sigmoid(xi @ w) - yi) * xi + lam * w
            g_snap = (sigmoid(xi @ w_snap) - yi) * xi + lam * w_snap
            w = w - eta * (g - g_snap + mu)
    return w
```

So thời gian tường — không phải epoch — với SGD minibatch của 26-01 trên ridge-logistic lồi mạnh $$n=5000$$, đích $$\|\nabla F(w)\|_2\le 10^{-4}$$. Rồi tiêu cùng ngân sách trên mạng một tầng ẩn: chi phí ảnh chụp vẫn là $$n$$ lượt ngược, giấc mơ bảng gradient của SAGA trở nên bất khả, và AdamW từ 26-04 sẽ trông như lựa chọn trưởng thành.

## Dùng gì khi nào

| Phương pháp | Bộ nhớ thêm | Chi phí mỗi bước (phân bổ) | Nhà thường trú | Tốc độ tuyến tính trên SC finite-sum? |
|-------------|-------------|----------------------------|----------------|----------------------------------------|
| SGD / mini-batch | không | $$1$$ (hoặc $$B$$) gradient | học sâu | không (sàn nhiễu) |
| SVRG | một snapshot + $$\mu$$ | $$\approx 3$$ gradient | tổng hữu hạn lồi, mã nghiên cứu | có |
| SAGA | một gradient mỗi mẫu | $$1$$ gradient | ERM lồi vừa (`solver="saga"`) | có |
| AdamW | hai EMA | $$1$$ minibatch | DL mặc định | không phải điểm |

Học SVRG để đọc được ghi chú Opt-for-ML (MIT 6.7220, BU EC525) và để nhận ra khi một ERM *lồi* — hồi quy logistic, SVM tuyến tính, một bộ làm mượt Lasso — *không* nên huấn luyện bằng Adam theo thói quen. Mini-batch Adam vẫn thắng trên mạng sâu vì (i) lưu hoặc làm mới gradient đầy đủ thuộc lớp độ phức tạp sai, (ii) phong cảnh không lồi mạnh, và (iii) phần cứng muốn nhân lớn, đều, không phải một $$I$$ ngẫu nhiên trừ ảnh chụp.

Ý tưởng hàng xóm cuối, không kiểm tra: **SARAH** / **SPIDER** thay biến kiểm soát bằng ước lượng đệ quy có thể chặt hơn trên lý thuyết; **FedAvg** ở Chương 29 *không* phải giảm phương sai theo nghĩa này (nó trung bình mô hình, không phải biến kiểm soát), dù biến kiểm soát của SCAFFOLD là họ hàng liên bang của SVRG.

**Bài tập 1.** Chứng minh không chệch của ước lượng SVRG trong một dòng, rồi chỉ một toàn phương hai mẫu nơi phương sai SGD thuần tại $$w^\star$$ dương trong khi phương sai SVRG tại ảnh chụp bằng không.

**Bài tập 2.** Trên ridge-logistic $$n=5000$$, vẽ chuẩn gradient huấn luyện theo *số gradient $$f_i$$* cho SGD, SVRG, và (nếu bộ nhớ cho phép) SAGA. Đánh dấu các lượt ảnh chụp SVRG. Rồi vẽ cùng các đường theo thời gian tường. Trục $$x$$ nào đổi người thắng?

**Câu hỏi.** Biến kiểm soát $$g$$ không chệch với mọi $$w$$, không chỉ tại $$\tilde w$$. Vậy thì vì sao ta vẫn phải làm mới ảnh chụp — $$\mathrm{Var}(g)$$ xảy ra gì nếu đóng băng $$\tilde w$$ và để $$w$$ đi xa?
