#!/usr/bin/env ruby
# Script để tạo template tiếng Việt từ nội dung tiếng Anh

require 'fileutils'
require 'yaml'

class ViTemplateCreator
  def initialize(base_path = '.')
    @base_path = base_path
    @en_path = File.join(@base_path, 'contents', 'en')
    @vi_path = File.join(@base_path, 'contents', 'vi')
  end

  def create_all_templates
    puts "🚀 Đang tạo template tiếng Việt từ nội dung tiếng Anh..."
    
    # Tạo thư mục vi nếu chưa có
    FileUtils.mkdir_p(@vi_path) unless Dir.exist?(@vi_path)
    
    # Tìm tất cả các chapter trong thư mục en
    en_chapters = Dir.glob(File.join(@en_path, 'chapter*')).select { |f| File.directory?(f) }
    
    en_chapters.each do |en_chapter_path|
      chapter_name = File.basename(en_chapter_path)
      puts "\n📁 Đang tạo template cho #{chapter_name}..."
      
      create_vi_template(en_chapter_path, chapter_name)
    end
    
    puts "\n✅ Hoàn thành tạo template tiếng Việt!"
  end

  private

  def create_vi_template(en_chapter_path, chapter_name)
    vi_chapter_path = File.join(@vi_path, chapter_name)
    
    # Chỉ tạo nếu chưa tồn tại
    if Dir.exist?(vi_chapter_path)
      puts "  ⚠️  #{chapter_name} đã tồn tại trong /vi/, bỏ qua..."
      return
    end
    
    # Copy toàn bộ chapter từ en sang vi
    FileUtils.cp_r(en_chapter_path, vi_chapter_path)
    puts "  ✅ Đã copy #{chapter_name} sang /vi/"
    
    # Cập nhật front matter cho tiếng Việt
    update_frontmatter_for_vi(vi_chapter_path, chapter_name)
  end

  def update_frontmatter_for_vi(chapter_path, chapter_name)
    chapter_number = chapter_name.gsub('chapter', '')
    
    # Cập nhật index.html
    index_file = File.join(chapter_path, 'index.html')
    if File.exist?(index_file)
      update_index_frontmatter(index_file, chapter_number)
    end
    
    # Cập nhật tất cả posts
    posts_dir = File.join(chapter_path, '_posts')
    if Dir.exist?(posts_dir)
      Dir.glob(File.join(posts_dir, '*.md')).each do |post_file|
        update_post_frontmatter(post_file, chapter_number)
      end
    end
  end

  def update_index_frontmatter(file_path, chapter_number)
    content = File.read(file_path)
    
    # Parse front matter
    if content.match(/^---\s*\n(.*?)\n---\s*\n/m)
      frontmatter = YAML.load($1)
      rest_content = content.sub(/^---\s*\n.*?\n---\s*\n/m, '')
      
      # Cập nhật front matter cho tiếng Việt
      frontmatter['lang'] = 'vi'
      frontmatter['permalink'] = "/contents/vi/chapter#{chapter_number.rjust(2, '0')}/"
      
      # Dịch title cơ bản
      if frontmatter['title']
        frontmatter['title'] = translate_title(frontmatter['title'])
      end
      
      # Ghi lại file
      new_content = "---\n#{frontmatter.to_yaml.sub(/^---\n/, '')}---\n#{rest_content}"
      File.write(file_path, new_content)
      
      puts "    ✅ Cập nhật index.html cho vi"
    end
  end

  def update_post_frontmatter(file_path, chapter_number)
    content = File.read(file_path)
    
    # Parse front matter
    if content.match(/^---\s*\n(.*?)\n---\s*\n/m)
      frontmatter = YAML.load($1)
      rest_content = content.sub(/^---\s*\n.*?\n---\s*\n/m, '')
      
      # Cập nhật front matter cho tiếng Việt
      frontmatter['lang'] = 'vi'
      
      # Dịch title cơ bản
      if frontmatter['title']
        frontmatter['title'] = translate_title(frontmatter['title'])
      end
      
      # Ghi lại file
      new_content = "---\n#{frontmatter.to_yaml.sub(/^---\n/, '')}---\n#{rest_content}"
      File.write(file_path, new_content)
    end
  end

  def translate_title(english_title)
    # Bảng dịch cơ bản
    translations = {
      'Introduction' => 'Giới thiệu',
      'Convex Sets' => 'Tập lồi',
      'Convex Functions' => 'Hàm lồi',
      'Gradient Descent' => 'Gradient Descent',
      'Newton Method' => 'Phương pháp Newton',
      'Convergence' => 'Hội tụ',
      'Analysis' => 'Phân tích',
      'Proof' => 'Chứng minh',
      'Examples' => 'Ví dụ',
      'Properties' => 'Tính chất',
      'Definition' => 'Định nghĩa',
      'Duality' => 'Đối ngẫu',
      'KKT Conditions' => 'Điều kiện KKT',
      'Optimization' => 'Tối ưu hóa',
      'Linear Programming' => 'Quy hoạch tuyến tính',
      'Quadratic Programming' => 'Quy hoạch bậc hai',
      'Interior Point Methods' => 'Phương pháp điểm trong',
      'Proximal Methods' => 'Phương pháp Proximal',
      'Coordinate Descent' => 'Coordinate Descent',
      'Subgradient Methods' => 'Phương pháp Subgradient',
      'ADMM' => 'ADMM',
      'Mixed Integer Programming' => 'Quy hoạch số nguyên hỗn hợp'
    }
    
    # Thử dịch một số từ khóa cơ bản
    translated = english_title
    translations.each do |en, vi|
      translated = translated.gsub(/\b#{Regexp.escape(en)}\b/i, vi)
    end
    
    # Nếu không có thay đổi, thêm "(Cần dịch)" để đánh dấu
    if translated == english_title
      translated += " (Cần dịch)"
    end
    
    translated
  end
end

# Chạy script nếu được execute trực tiếp
if __FILE__ == $0
  creator = ViTemplateCreator.new
  creator.create_all_templates
end
