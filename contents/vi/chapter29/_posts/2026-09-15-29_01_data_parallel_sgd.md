---
layout: post
title: 29-01 SGD song song dữ liệu
chapter: '29'
order: 2
owner: Nguyen Le Linh
categories:
- chapter29
lang: vi
lesson_type: required
---


Giả sử ta chia $$n$$ mẫu cho $$P$$ worker, worker $$p$$ giữ tập chỉ số $$\mathcal{I}_p$$. Một bước **song song dữ liệu** đồng bộ là

$$
g_k = \frac{1}{P}\sum_{p=1}^P g_k^{(p)}, \qquad
g_k^{(p)} = \frac{1}{B}\sum_{i\in\mathcal{B}_{k,p}} \nabla f_i(w_k),
$$

rồi $$w_{k+1}=w_k-\eta g_k$$. Nếu hợp của các minibatch $$\mathcal{B}_{k,p}$$ là một mẫu đều, đây là SGD minibatch thường với batch $$PB$$. Phần *hệ thống* là cách lập $$g_k$$: **parameter server** cộng gradient gửi tới, hoặc **all-reduce** (vòng, cây, NCCL) lấy trung bình không cần một nút cổ chai duy nhất.

**Không có phép màu.** Song song dữ liệu không đổi toán của SGD nếu mọi worker dùng *cùng* $$w_k$$. Nó đổi thời gian tường mỗi bước và batch khả thi lớn nhất. All-reduce một vector 100 triệu tham số là bài toán băng thông; đó là lý do người ta bàn nén (lượng tử hóa, thưa hóa) như bài tùy chọn kế.

Các biến thể **bất đồng bộ** (kiểu Hogwild!) áp gradient cũ. Chúng có thể nhanh hơn trên bộ nhớ dùng chung và khó phân tích hơn. Với môn này, hãy cài bức tranh đồng bộ trước.

```python
def data_parallel_step(workers_grads, eta, w):
    g = sum(workers_grads) / len(workers_grads)
    return w - eta * g
```

Mở [parallel_computing_illustration.html](https://nglelinh.github.io/interactive_math/optimization/parallel_computing_illustration.html) để xem hoạt họa chia việc, rồi trở lại và viết all-reduce của $$g$$ lên bảng.

**Bài tập.** Nếu mỗi worker có batch $$B=32$$ và $$P=8$$, batch tương đương một nút là bao nhiêu? Nếu bạn scale tuyến tính $$\eta$$ theo $$P$$, điều gì có thể hỏng (gợi ý: lịch Chương 26 và ngưỡng gãy batch lớn)?
