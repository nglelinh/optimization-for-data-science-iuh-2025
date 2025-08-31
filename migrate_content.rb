#!/usr/bin/env ruby
# Migration script để di chuyển nội dung từ cấu trúc cũ sang cấu trúc đa ngôn ngữ mới

require 'fileutils'
require 'yaml'

class ContentMigrator
  def initialize(base_path = '.')
    @base_path = base_path
    @old_contents_path = File.join(@base_path, 'contents')
    @new_en_path = File.join(@base_path, 'contents', 'en')
    @new_vi_path = File.join(@base_path, 'contents', 'vi')
  end

  def migrate_all
    puts "🚀 Bắt đầu migration nội dung..."
    
    # Tạo thư mục đích nếu chưa có
    FileUtils.mkdir_p(@new_en_path) unless Dir.exist?(@new_en_path)
    FileUtils.mkdir_p(@new_vi_path) unless Dir.exist?(@new_vi_path)
    
    # Tìm tất cả các chapter cũ
    old_chapters = Dir.glob(File.join(@old_contents_path, 'chapter*')).select { |f| File.directory?(f) }
    
    old_chapters.each do |chapter_path|
      chapter_name = File.basename(chapter_path)
      puts "\n📁 Đang xử lý #{chapter_name}..."
      
      migrate_chapter(chapter_path, chapter_name)
    end
    
    puts "\n✅ Migration hoàn thành!"
    puts "📝 Hãy kiểm tra và cập nhật các link nội bộ bằng script update_links.rb"
  end

  private

  def migrate_chapter(old_chapter_path, chapter_name)
    # Đường dẫn đích cho tiếng Anh
    en_chapter_path = File.join(@new_en_path, chapter_name)
    
    # Chỉ migrate nếu chưa tồn tại trong thư mục tiếng Anh
    if Dir.exist?(en_chapter_path)
      puts "  ⚠️  #{chapter_name} đã tồn tại trong /en/, bỏ qua..."
      return
    end
    
    # Copy toàn bộ chapter sang tiếng Anh
    FileUtils.cp_r(old_chapter_path, en_chapter_path)
    puts "  ✅ Đã copy #{chapter_name} sang /en/"
    
    # Cập nhật front matter cho các file trong chapter tiếng Anh
    update_frontmatter_for_chapter(en_chapter_path, 'en', chapter_name)
    
    # Tạo bản sao cho tiếng Việt (để người dùng dịch sau)
    vi_chapter_path = File.join(@new_vi_path, chapter_name)
    unless Dir.exist?(vi_chapter_path)
      FileUtils.cp_r(en_chapter_path, vi_chapter_path)
      puts "  📋 Đã tạo template cho #{chapter_name} trong /vi/"
      
      # Cập nhật front matter cho tiếng Việt
      update_frontmatter_for_chapter(vi_chapter_path, 'vi', chapter_name)
    end
  end

  def update_frontmatter_for_chapter(chapter_path, lang, chapter_name)
    chapter_number = chapter_name.gsub('chapter', '')
    
    # Cập nhật index.html
    index_file = File.join(chapter_path, 'index.html')
    if File.exist?(index_file)
      update_index_frontmatter(index_file, lang, chapter_number)
    end
    
    # Cập nhật tất cả posts
    posts_dir = File.join(chapter_path, '_posts')
    if Dir.exist?(posts_dir)
      Dir.glob(File.join(posts_dir, '*.md')).each do |post_file|
        update_post_frontmatter(post_file, lang, chapter_number)
      end
    end
  end

  def update_index_frontmatter(file_path, lang, chapter_number)
    content = File.read(file_path)
    
    # Parse front matter
    if content.match(/^---\s*\n(.*?)\n---\s*\n/m)
      frontmatter = YAML.load($1)
      rest_content = content.sub(/^---\s*\n.*?\n---\s*\n/m, '')
      
      # Cập nhật front matter
      frontmatter['lang'] = lang
      frontmatter['permalink'] = "/contents/#{lang}/chapter#{chapter_number.rjust(2, '0')}/"
      
      # Dịch title nếu là tiếng Việt
      if lang == 'vi' && frontmatter['title']
        frontmatter['title'] = translate_title(frontmatter['title'])
      end
      
      # Ghi lại file
      new_content = "---\n#{frontmatter.to_yaml.sub(/^---\n/, '')}---\n#{rest_content}"
      File.write(file_path, new_content)
      
      puts "    ✅ Cập nhật index.html cho #{lang}"
    end
  end

  def update_post_frontmatter(file_path, lang, chapter_number)
    content = File.read(file_path)
    
    # Parse front matter
    if content.match(/^---\s*\n(.*?)\n---\s*\n/m)
      frontmatter = YAML.load($1)
      rest_content = content.sub(/^---\s*\n.*?\n---\s*\n/m, '')
      
      # Cập nhật front matter
      frontmatter['lang'] = lang
      
      # Dịch title nếu là tiếng Việt
      if lang == 'vi' && frontmatter['title']
        frontmatter['title'] = translate_title(frontmatter['title'])
      end
      
      # Ghi lại file
      new_content = "---\n#{frontmatter.to_yaml.sub(/^---\n/, '')}---\n#{rest_content}"
      File.write(file_path, new_content)
    end
  end

  def translate_title(english_title)
    # Bảng dịch cơ bản - có thể mở rộng
    translations = {
      'Introduction' => 'Giới thiệu',
      'Convex Sets' => 'Tập lồi',
      'Convex Functions' => 'Hàm lồi',
      'Gradient Descent' => 'Gradient Descent',
      'Convergence' => 'Hội tụ',
      'Analysis' => 'Phân tích',
      'Proof' => 'Chứng minh',
      'Examples' => 'Ví dụ',
      'Properties' => 'Tính chất',
      'Definition' => 'Định nghĩa'
    }
    
    # Thử dịch một số từ khóa cơ bản
    translated = english_title
    translations.each do |en, vi|
      translated = translated.gsub(/\b#{en}\b/i, vi)
    end
    
    # Nếu không có thay đổi, thêm "(Cần dịch)" để đánh dấu
    if translated == english_title
      translated += " (Cần dịch)"
    end
    
    translated
  end
end

# Chạy migration nếu file được execute trực tiếp
if __FILE__ == $0
  migrator = ContentMigrator.new
  migrator.migrate_all
end
