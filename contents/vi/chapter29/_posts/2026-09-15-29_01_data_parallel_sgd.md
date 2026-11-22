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


Giả sử tập dữ liệu gồm $$n$$ mẫu được phân chia cho $$P$$ nút tính toán (worker), trong đó nút $$p$$ giữ tập chỉ số $$\mathcal{I}_p$$. Một bước **SGD song song dữ liệu** đồng bộ thực hiện:

$$
g_k = \frac{1}{P}\sum_{p=1}^P g_k^{(p)}, \qquad
g_k^{(p)} = \frac{1}{B}\sum_{i\in\mathcal{B}_{k,p}} \nabla f_i(w_k),
$$

sau đó cập nhật $$w_{k+1}=w_k-\eta g_k$$. Nếu hợp các minibatch $$\mathcal{B}_{k,p}$$ tương đương với một mẫu rút đều, phép cập nhật này hoàn toàn trùng với SGD minibatch thông thường có kích thước lô $$PB$$. Điểm khác biệt nằm ở kiến trúc *hệ thống* để tổng hợp $$g_k$$: sử dụng **máy chủ tham số (parameter server)** để gom và cộng gradient, hoặc dùng giao thức **all-reduce** (dạng vòng, cây hoặc thư viện NCCL) để lấy trung bình trực tiếp giữa các nút mà không tạo điểm nghẽn tập trung.

Về mặt toán học, song song dữ liệu đồng bộ không làm thay đổi thuật toán SGD miễn là mọi nút đều dùng *cùng một* bản sao tham số $$w_k$$; lợi ích của nó là giảm thời gian thực thi (wall-clock time) mỗi bước và cho phép huấn luyện với kích thước lô tổng lớn hơn. Khi mô hình có hàng trăm triệu tham số, thao tác all-reduce trở thành bài toán băng thông mạng — đó là động lực cho các kỹ thuật nén gradient (lượng tử hóa, làm thưa).

Các biến thể **bất đồng bộ** (như Hogwild!) cho phép cập nhật ngay bằng các gradient tính trên bản sao tham số cũ hơn; chúng có thể tận dụng tốt bộ nhớ dùng chung nhưng khó phân tích hội tụ hơn. Trong phạm vi môn học, ta tập trung nắm vững mô hình đồng bộ trước.

```python
def data_parallel_step(workers_grads, eta, w):
    g = sum(workers_grads) / len(workers_grads)
    return w - eta * g
```

Bạn có thể xem mô phỏng chia tải song song tại [parallel_computing_illustration.html](https://nglelinh.github.io/interactive_math/optimization/parallel_computing_illustration.html).

**Bài tập.** Nếu mỗi nút xử lý minibatch kích thước $$B=32$$ trên $$P=8$$ nút, kích thước lô tương đương trên một máy đơn là bao nhiêu? Nếu bạn tăng tuyến tính tốc độ học $$\eta$$ theo $$P$$, những rủi ro nào có thể xảy ra (gợi ý: xem lại phần lịch tốc độ học và giới hạn kích thước lô lớn ở Chương 26)?
