# Hướng dẫn sử dụng hệ thống đa ngôn ngữ

## Tổng quan

Dự án này hiện đã được cấu hình để hỗ trợ đa ngôn ngữ (tiếng Anh và tiếng Việt) với khả năng chuyển đổi mượt mà giữa các ngôn ngữ.

## Cấu trúc thư mục mới

```
contents/
├── en/          # Nội dung tiếng Anh
│   ├── chapter00/
│   │   ├── index.html
│   │   └── _posts/
│   │       └── *.md
│   ├── chapter01/
│   └── ...
├── vi/          # Nội dung tiếng Việt  
│   ├── chapter00/
│   │   ├── index.html
│   │   └── _posts/
│   │       └── *.md
│   ├── chapter01/
│   └── ...
```

## Cách thêm nội dung mới

### 1. Thêm chương mới

Để thêm một chương mới, bạn cần tạo cấu trúc cho cả hai ngôn ngữ:

```bash
# Tạo thư mục cho chương mới
mkdir -p contents/en/chapter01
mkdir -p contents/vi/chapter01

# Tạo file index.html cho mỗi ngôn ngữ
```

### 2. Cấu hình front matter cho index.html

**Tiếng Anh (contents/en/chapter01/index.html):**
```yaml
---
layout: page
title: "Chapter Title in English"
chapter: "01"
owner: "Your Name"
lang: en
permalink: /contents/en/chapter01/
---
```

**Tiếng Việt (contents/vi/chapter01/index.html):**
```yaml
---
layout: page
title: "Tiêu đề chương bằng tiếng Việt"
chapter: "01"
owner: "Your Name"
lang: vi
permalink: /contents/vi/chapter01/
---
```

### 3. Thêm bài viết mới

Tạo file trong thư mục `_posts` của mỗi ngôn ngữ:

**Tiếng Anh (contents/en/chapter01/_posts/2024-01-01-post-title.md):**
```yaml
---
layout: post
title: "Post Title in English"
chapter: "01"
order: 1
owner: "Your Name"
lang: en
---

Content in English...
```

**Tiếng Việt (contents/vi/chapter01/_posts/2024-01-01-post-title.md):**
```yaml
---
layout: post
title: "Tiêu đề bài viết bằng tiếng Việt"
chapter: "01"
order: 1
owner: "Your Name"
lang: vi
---

Nội dung bằng tiếng Việt...
```

## Các tính năng đã được thêm

### 1. Nút chuyển đổi ngôn ngữ
- Xuất hiện ở góc trên bên phải của trang
- Tự động chuyển đổi giữa các URL tương ứng
- Hỗ trợ keyboard navigation (Alt + L)

### 2. Sidebar thông minh
- Chỉ hiển thị các chương của ngôn ngữ hiện tại
- Tự động fallback nếu không có nội dung cho ngôn ngữ đó

### 3. Plugin Jekyll tùy chỉnh
- `{% t key %}`: Hiển thị text đã được dịch
- `{% language_switch %}`: Tạo nút chuyển đổi ngôn ngữ
- `{% lang language %}`: Kiểm tra ngôn ngữ hiện tại

### 4. CSS và JavaScript hỗ trợ
- Hiệu ứng chuyển đổi mượt mà
- Responsive design
- Accessibility features

## Cách sử dụng các tag Jekyll

### 1. Hiển thị text đa ngôn ngữ
```liquid
<h1>{% t title %}</h1>
<a href="/">{% t home %}</a>
```

### 2. Kiểm tra ngôn ngữ hiện tại
```liquid
{% if page.lang == 'vi' %}
  <p>Nội dung chỉ hiển thị bằng tiếng Việt</p>
{% else %}
  <p>Content only shown in English</p>
{% endif %}
```

### 3. Thêm nút chuyển đổi ngôn ngữ
```liquid
{% language_switch %}
```

## Cấu hình trong _config.yml

Các cấu hình quan trọng đã được thêm:

```yaml
# Multi-language support
languages: ["en", "vi"]
default_lang: "en"

# Language-specific configurations
t:
  en:
    title: "Convex Optimization in Data Science"
    home: "Home"
    # ... thêm các key khác
  vi:
    title: "Tối ưu hóa lồi trong Khoa học Dữ liệu"
    home: "Trang chủ"
    # ... thêm các key khác
```

## Quy trình làm việc khuyến nghị

### 1. Tạo nội dung tiếng Anh trước
1. Tạo cấu trúc thư mục cho tiếng Anh
2. Viết nội dung bằng tiếng Anh
3. Test và đảm bảo hoạt động tốt

### 2. Dịch sang tiếng Việt
1. Sao chép cấu trúc sang thư mục tiếng Việt
2. Dịch nội dung
3. Cập nhật front matter với `lang: vi`
4. Test chức năng chuyển đổi ngôn ngữ

### 3. Đảm bảo tính nhất quán
- Cùng cấu trúc thư mục
- Cùng tên file (trừ nội dung)
- Cùng giá trị `chapter` và `order`
- Permalink tương ứng

## Troubleshooting

### 1. Nút chuyển đổi ngôn ngữ không hoạt động
- Kiểm tra file `multilang.js` đã được load
- Đảm bảo permalink được cấu hình đúng
- Kiểm tra cấu trúc URL

### 2. Sidebar không hiển thị đúng
- Kiểm tra front matter có `lang` và `chapter`
- Đảm bảo `layout: page` cho index.html

### 3. Text không được dịch
- Kiểm tra key có tồn tại trong `_config.yml`
- Đảm bảo syntax `{% t key %}` đúng

## Mở rộng thêm ngôn ngữ

Để thêm ngôn ngữ mới (ví dụ: tiếng Pháp):

1. Thêm `"fr"` vào `languages` trong `_config.yml`
2. Thêm section `fr:` trong `t:` với các bản dịch
3. Tạo thư mục `contents/fr/`
4. Cập nhật logic trong `_plugins/multilang.rb` nếu cần

## Best Practices

1. **Tính nhất quán**: Luôn duy trì cấu trúc tương tự giữa các ngôn ngữ
2. **SEO**: Sử dụng permalink rõ ràng cho mỗi ngôn ngữ
3. **Accessibility**: Đảm bảo `lang` attribute được set đúng
4. **Performance**: Tối ưu hóa hình ảnh và assets chung
5. **Testing**: Test trên nhiều thiết bị và trình duyệt

## Liên hệ

Nếu có vấn đề hoặc cần hỗ trợ, vui lòng tạo issue trên GitHub repository.
