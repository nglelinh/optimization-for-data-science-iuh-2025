# 🔍 Tính năng Tìm kiếm - Search Feature

Tài liệu này mô tả cách triển khai và sử dụng tính năng tìm kiếm thông minh cho trang web Optimization in Data Science sử dụng Lunr.js.

## 🚀 Tính năng chính

### ✨ Tìm kiếm thông minh
- **Real-time search**: Kết quả hiển thị ngay khi gõ
- **Fuzzy matching**: Tìm được ngay cả khi gõ sai chính tả
- **Weighted fields**: Tiêu đề có trọng số cao hơn nội dung
- **Multi-field search**: Tìm kiếm qua title, content, chapter, owner

### 🌐 Đa ngôn ngữ
- Hỗ trợ tiếng Anh và tiếng Việt
- Tự động phát hiện ngôn ngữ từ URL
- Index riêng biệt cho mỗi ngôn ngữ

### 🎨 Giao diện hiện đại
- Responsive design cho mọi thiết bị
- Dark mode support
- Smooth animations
- Keyboard navigation

### ⚡ Hiệu suất cao
- Pre-built search index
- Debounced input (300ms)
- Lazy loading
- Optimized JSON parsing

## 📁 Cấu trúc Files

```
├── _plugins/
│   └── search_generator.rb          # Jekyll plugin tạo search index
├── public/
│   ├── css/
│   │   └── search.css              # Styling cho search interface
│   └── js/
│       └── search.js               # JavaScript search functionality
├── search-index.json               # Search index tiếng Anh (auto-generated)
├── search-index-vi.json            # Search index tiếng Việt (auto-generated)
└── SEARCH_README.md                # Tài liệu này
```

## 🛠️ Cài đặt

### 1. Files đã được thêm
Tất cả files cần thiết đã được tạo và tích hợp vào Jekyll site:

- ✅ `_plugins/search_generator.rb` - Jekyll plugin
- ✅ `public/css/search.css` - CSS styling
- ✅ `public/js/search.js` - JavaScript functionality
- ✅ `_includes/head.html` - Updated với Lunr.js CDN
- ✅ `_layouts/default.html` - Updated với search.js

### 2. Dependencies
- **Lunr.js**: Loaded từ CDN `https://unpkg.com/lunr/lunr.js`
- **No additional gems required**

### 3. Build Search Index

#### Tự động (Jekyll build)
Search index sẽ được tạo tự động khi Jekyll build:
```bash
bundle exec jekyll build
# hoặc
bundle exec jekyll serve
```

#### Manual Rebuild (nếu cần)
Nếu cần rebuild index manually, có thể xóa và build lại:
```bash
rm search-index*.json
bundle exec jekyll build
```

## 🎯 Cách sử dụng

### Cho người dùng cuối

#### Mở tìm kiếm
- **Click** vào icon search trong header
- **Keyboard shortcut**: `Ctrl+K` (Windows/Linux) hoặc `Cmd+K` (Mac)

#### Tìm kiếm
- Gõ từ khóa vào search box
- Kết quả hiển thị real-time
- Click vào kết quả để chuyển đến trang

#### Đóng tìm kiếm
- **Click** outside overlay
- **Press** `Esc`
- **Click** nút X

#### Keyboard Navigation
- `Enter`: Chọn kết quả đầu tiên
- `Esc`: Đóng search
- `Ctrl+K`/`Cmd+K`: Mở search

### Cho developers

#### Customize Search Fields
Trong `search_generator.rb`, bạn có thể thay đổi trọng số các trường:

```ruby
this.field('title', { boost: 10 });      # Tiêu đề - trọng số cao nhất
this.field('content', { boost: 5 });     # Nội dung - trọng số cao
this.field('chapter', { boost: 3 });     # Chapter - trọng số trung bình
this.field('owner', { boost: 2 });       # Tác giả - trọng số thấp
```

#### Customize UI
Chỉnh sửa `public/css/search.css` để thay đổi giao diện:
- Colors: Thay đổi `#268bd2` thành màu khác
- Animations: Điều chỉnh `transition` properties
- Layout: Thay đổi `max-width`, `padding`, etc.

#### Add New Languages
1. Thêm ngôn ngữ vào `_config.yml`:
```yaml
languages: ["en", "vi", "fr"]  # Thêm "fr"
```

2. Update `search.js`:
```javascript
detectLanguage() {
  const path = window.location.pathname;
  if (path.includes('/vi/')) return 'vi';
  if (path.includes('/fr/')) return 'fr';  // Thêm dòng này
  if (path.includes('/en/')) return 'en';
  return 'en';
}
```

## 🧪 Testing

### Test với Jekyll Server
Chạy Jekyll server để test:
```bash
bundle exec jekyll serve
# Mở http://localhost:4000
```

### Test Cases
1. **Basic search**: Tìm "optimization"
2. **Fuzzy search**: Tìm "optimizaton" (sai chính tả)
3. **Multi-word**: Tìm "gradient descent"
4. **Chapter search**: Tìm "chapter 15"
5. **Author search**: Tìm tên tác giả
6. **Empty results**: Tìm "xyz123"

### Performance Testing
```javascript
// Trong browser console
console.time('search');
// Thực hiện search
console.timeEnd('search');
```

## 📊 Search Index Structure

### English Index (`search-index.json`)
```json
[
  {
    "id": "chapter01_01_introduction",
    "title": "01 Introduction", 
    "chapter": "01",
    "order": 1,
    "owner": "Author Name",
    "lesson_type": "required",
    "content": "Clean text content...",
    "url": "/contents/chapter01/01_introduction/",
    "lang": "en"
  }
]
```

### Vietnamese Index (`search-index-vi.json`)
Cấu trúc tương tự nhưng với `"lang": "vi"`

## 🔧 Troubleshooting

### Search không hoạt động
1. **Kiểm tra console errors**
2. **Verify Lunr.js loaded**: `typeof lunr !== 'undefined'`
3. **Check search index**: Mở network tab, xem có load được JSON không
4. **Rebuild index**: Chạy `bundle exec jekyll build`

### Kết quả không chính xác
1. **Check content cleaning**: Xem `clean_markdown_content()` function
2. **Verify field weights**: Điều chỉnh boost values
3. **Update stop words**: Thêm stop words cho Lunr

### Performance issues
1. **Reduce index size**: Giới hạn content length
2. **Increase debounce**: Tăng timeout từ 300ms
3. **Lazy load**: Chỉ load index khi cần

## 🚀 Deployment

### GitHub Pages
Search sẽ hoạt động tự động trên GitHub Pages vì:
- Sử dụng Jekyll plugins trong `_plugins/`
- CSS/JS files trong `public/`
- Search index được generate tự động

### Custom Server
Nếu deploy trên server khác:
1. Ensure Jekyll plugins enabled
2. Copy all `public/` files
3. Ensure search index files accessible
4. Update base URLs trong `search.js` nếu cần

## 📈 Analytics & Monitoring

### Track Search Usage
Thêm vào `search.js`:
```javascript
performSearch(query) {
  // Track search
  if (typeof gtag !== 'undefined') {
    gtag('event', 'search', {
      search_term: query
    });
  }
  
  // Existing search logic...
}
```

### Monitor Performance
```javascript
// Trong search.js
console.log(`Search completed in ${Date.now() - startTime}ms`);
console.log(`Found ${results.length} results for "${query}"`);
```

## 🤝 Contributing

### Thêm tính năng mới
1. Fork repository
2. Tạo feature branch
3. Update relevant files
4. Test thoroughly
5. Submit pull request

### Report bugs
Tạo issue với thông tin:
- Browser và version
- Steps to reproduce
- Expected vs actual behavior
- Console errors (nếu có)

## 📝 License

Tính năng search này được phát triển cho dự án Optimization in Data Science và tuân theo license của dự án chính.

---

**Developed with ❤️ for better learning experience**
