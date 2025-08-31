#!/usr/bin/env ruby
# Script để sửa front matter cho các file index.html từ chapter 12-25

require 'fileutils'

class FrontMatterFixer
  def initialize(base_path = '.')
    @base_path = base_path
    @contents_en_path = File.join(@base_path, 'contents', 'en')
  end

  def fix_chapters(start_chapter, end_chapter)
    puts "🔧 Đang sửa front matter cho chapter #{start_chapter} đến #{end_chapter}..."
    
    (start_chapter..end_chapter).each do |chapter_num|
      chapter_name = "chapter#{chapter_num.to_s.rjust(2, '0')}"
      index_file = File.join(@contents_en_path, chapter_name, 'index.html')
      
      if File.exist?(index_file)
        fix_index_file(index_file, chapter_name)
      else
        puts "  ⚠️  File không tồn tại: #{index_file}"
      end
    end
    
    puts "\n✅ Hoàn thành sửa front matter!"
  end

  private

  def fix_index_file(file_path, chapter_name)
    content = File.read(file_path)
    
    # Kiểm tra xem file đã có front matter đúng format chưa
    if content.start_with?('---')
      puts "  ✅ #{chapter_name}/index.html đã có format đúng"
      return
    end
    
    # Kiểm tra xem có front matter nhưng thiếu dấu --- đầu
    if content.match(/^layout:\s*page/)
      # Tìm dòng cuối của front matter (dấu --- cuối)
      lines = content.split("\n")
      frontmatter_end = lines.find_index { |line| line.strip == '---' }
      
      if frontmatter_end
        # Thêm dấu --- vào đầu
        lines.insert(0, '---')
        new_content = lines.join("\n")
        
        File.write(file_path, new_content)
        puts "  ✅ Đã sửa #{chapter_name}/index.html"
      else
        puts "  ⚠️  Không tìm thấy dấu --- cuối trong #{chapter_name}/index.html"
      end
    else
      puts "  ⚠️  Không tìm thấy front matter trong #{chapter_name}/index.html"
    end
  end
end

# Chạy script nếu được execute trực tiếp
if __FILE__ == $0
  fixer = FrontMatterFixer.new
  fixer.fix_chapters(12, 25)
end
