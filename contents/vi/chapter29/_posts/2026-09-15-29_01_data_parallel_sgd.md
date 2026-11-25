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

Khi bạn huấn luyện một mạng thị giác hay mô hình ngôn ngữ trên 8, 64 hay 1.024 chiếc GPU cùng lúc bằng `DistributedDataParallel` (DDP) của PyTorch, điều gì thực sự diễn ra sau dòng lệnh `loss.backward()`? Về mặt toán học, **SGD song song dữ liệu đồng bộ** giản dị đến bất ngờ: chia lô dữ liệu lớn thành $$P$$ phần nhỏ cho $$P$$ máy tính gradient song song, rồi lấy trung bình cộng lại — kết quả **trùng khớp 100%** với việc chạy SGD trên một chiếc máy khổng lồ duy nhất có kích thước lô $$PB$$!

Sự khác biệt quyết định thành bại lại nằm ở tầng *giao thức truyền thông*: nếu tất cả $$P$$ máy đều gửi gradient về một **Máy chủ tham số (Parameter Server)** trung tâm, chiếc máy chủ đó sẽ tắc nghẽn ngay khi $$P$$ tăng lên; còn với giao thức **Ring All-Reduce**, các GPU nối thành một vòng tròn chuyền từng lát dữ liệu cho nhau, giúp lượng dữ liệu mỗi GPU phải truyền **hầu như không tăng dù bạn gắn thêm hàng trăm GPU**!

## Bản đồ kiến thức nền: Ba trụ cột của SGD song song dữ liệu

Để hiểu cả tính tương đương toán học lẫn nút thắt hạ tầng của huấn luyện đa GPU, hãy nắm ba trụ cột sau:

- **Tương đương toán học với Minibatch lớn $$PB$$:** Nhờ tính tuyến tính của đạo hàm và phép lấy trung bình, $$\frac{1}{P}\sum_{p=1}^P \left(\frac{1}{B}\sum_{i \in \mathcal{B}_{k,p}} \nabla f_i(w_k)\right) = \frac{1}{PB}\sum_{i \in \mathcal{B}_k} \nabla f_i(w_k)$$. Tuy nhiên, tăng $$P$$ làm tăng kích thước lô tổng $$PB$$, nên ta phải điều chỉnh tốc độ học (linear scaling rule + warmup) và lưu ý giới hạn kích thước lô tới hạn.
- **Parameter Server vs. Ring All-Reduce:** Trong Parameter Server, máy chủ trung tâm chịu tải truyền thông tỉ lệ thuận với $$P$$ (điểm nghẽn cổ chai). Trong Ring All-Reduce (pha *reduce-scatter* + pha *all-gather*), mỗi GPU chỉ gửi và nhận tổng cộng $$2\frac{P-1}{P}M < 2M$$ byte — **độc lập với $$P$$**!
- **Đồng bộ (Synchronous) vs. Bất đồng bộ (Asynchronous / Hogwild!):** Đồng bộ đảm bảo gradient luôn tươi mới tại đúng $$w_k$$ nhưng bị chậm theo nút chạy chậm nhất (*straggler*). Bất đồng bộ loại bỏ thời gian chờ nhưng tạo ra **gradient trễ (stale gradients)** tính tại phiên bản trọng số cũ $$w_{k-\tau}$$, gây khó khăn cho hội tụ ở mô hình lớn.

### Khung giải thích (nên đọc chậm): Kiểm chứng tính tương đương toán học và so sánh băng thông Ring All-Reduce

1. **Kiểm chứng tương đương toán học với $$P = 2$$ máy, mỗi máy giữ $$B = 2$$ mẫu:**
   - Máy 1 tính gradient trên 2 mẫu được $$2$$ và $$6 \implies g^{(1)} = \frac{2 + 6}{2} = 4$$.
   - Máy 2 tính gradient trên 2 mẫu được $$8$$ và $$12 \implies g^{(2)} = \frac{8 + 12}{2} = 10$$.
   - Trung bình qua All-Reduce: $$g = \frac{4 + 10}{2} = 7$$.
   - So với chạy 1 máy duy nhất với minibatch $$PB = 4$$ mẫu: $$\frac{2 + 6 + 8 + 12}{4} = \frac{28}{4} = 7$$ — **giống hệt từng chữ số!**
2. **So sánh tải truyền thông khi mở rộng lên $$P = 4$$ GPU với kích thước mô hình $$M = 100\text{ MB}$$:**
   - *Parameter Server tập trung:* Máy chủ phải nhận $$100\text{ MB}$$ từ $$3$$ worker khác (hoặc cả $$4$$) rồi gửi lại $$100\text{ MB}$$ cho từng máy. Tổng dữ liệu đi qua nút cổ chai máy chủ là $$2(P - 1)M = 2(3)(100) = 600\text{ MB}$$ (khi $$P = 100$$ sẽ vọt lên $$19{,}800\text{ MB}$$!).
   - *Ring All-Reduce:* Chia vector $$100\text{ MB}$$ thành $$P = 4$$ lát (mỗi lát $$25\text{ MB}$$). Pha *reduce-scatter* cần $$P - 1 = 3$$ bước truyền $$25\text{ MB}$$ ($$75\text{ MB}$$), pha *all-gather* cần thêm $$3$$ bước truyền $$25\text{ MB}$$ ($$75\text{ MB}$$). Tổng lượng dữ liệu mỗi GPU gửi đi chỉ là:
     $$2\frac{P - 1}{P}M = 2 \cdot \frac{3}{4} \cdot 100 = 150\text{ MB}$$ — và ngay cả khi $$P = 1{,}000$$ GPU, con số này vẫn bị chặn chặt dưới $$200\text{ MB}$$!

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
