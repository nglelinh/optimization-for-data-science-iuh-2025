---
layout: post
title: '19-01 Phương pháp Newton proximal'
chapter: '19'
order: 2
owner: Hooncheol Shin
categories:
- chapter19
lang: vi
---

Trong phần này, chúng ta sẽ ôn lại **phương pháp proximal gradient** và xem **phương pháp Newton proximal** xuất hiện từ đó như thế nào.

Chúng ta cũng sẽ tìm hiểu định nghĩa của **phương pháp Newton proximal** và ánh xạ proximal có tỉ lệ (scaled proximal map), vốn có các tính chất tốt như tính duy nhất và tính không giãn so với ánh xạ proximal thông thường.

### Newton gần kề trong 18 giây

<div class="reel-video" style="text-align:center;margin:1.5rem 0;">
<video controls playsinline preload="metadata" style="width:100%;max-width:360px;height:auto;aspect-ratio:9/16;border-radius:12px;background:#10121a;" src="{{ site.baseurl }}/public/videos/reels/prox-newton_vi.mp4"></video>
</div>

Gradient gần kề chỉ dùng bước vô hướng; Newton gần kề cực tiểu hóa mô hình bậc hai với Hessian thật cộng $$\lambda\|x\|_1$$, nên cần ít bước lặp hơn nhiều.

### Tự tay thử: gradient gần kề so với Newton gần kề

<div class="opx-explainer" data-opx="pn" data-lang="vi"></div>
