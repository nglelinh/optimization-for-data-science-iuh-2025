#!/usr/bin/env ruby
# Script để sửa front matter cho các file index.html trong contents/vi/

require 'fileutils'

def fix_vi_chapters(start_chapter, end_chapter)
  puts "🔧 Đang sửa front matter cho contents/vi/ từ chapter #{start_chapter} đến #{end_chapter}..."
  
  (start_chapter..end_chapter).each do |chapter_num|
    chapter_name = "chapter#{chapter_num.to_s.rjust(2, '0')}"
    index_file = File.join('contents', 'vi', chapter_name, 'index.html')
    
    if File.exist?(index_file)
      content = File.read(index_file)
      
      unless content.start_with?('---')
        if content.match(/^layout:\s*page/)
          lines = content.split("\n")
          frontmatter_end = lines.find_index { |line| line.strip == '---' }
          
          if frontmatter_end
            lines.insert(0, '---')
            new_content = lines.join("\n")
            File.write(index_file, new_content)
            puts "  ✅ Đã sửa #{chapter_name}/index.html (vi)"
          else
            puts "  ⚠️  Không tìm thấy dấu --- cuối trong #{chapter_name}/index.html (vi)"
          end
        else
          puts "  ⚠️  Không tìm thấy front matter trong #{chapter_name}/index.html (vi)"
        end
      else
        puts "  ✅ #{chapter_name}/index.html (vi) đã có format đúng"
      end
    else
      puts "  ⚠️  File không tồn tại: #{index_file}"
    end
  end
  
  puts "\n✅ Hoàn thành sửa front matter cho contents/vi/!"
end

# Chạy script
fix_vi_chapters(12, 25)
