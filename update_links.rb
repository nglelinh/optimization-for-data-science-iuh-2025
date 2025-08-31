#!/usr/bin/env ruby
# Script cập nhật các internal links để tương thích với cấu trúc đa ngôn ngữ

require 'fileutils'

class LinkUpdater
  def initialize(base_path = '.')
    @base_path = base_path
    @contents_path = File.join(@base_path, 'contents')
  end

  def update_all_links
    puts "🔗 Bắt đầu cập nhật các internal links..."
    
    # Cập nhật links trong contents/en/
    update_links_in_directory(File.join(@contents_path, 'en'), 'en')
    
    # Cập nhật links trong contents/vi/
    update_links_in_directory(File.join(@contents_path, 'vi'), 'vi')
    
    # Cập nhật links trong home/_posts/
    update_links_in_directory(File.join(@base_path, 'home', '_posts'), 'en')
    
    puts "\n✅ Cập nhật links hoàn thành!"
  end

  private

  def update_links_in_directory(dir_path, lang)
    return unless Dir.exist?(dir_path)
    
    puts "\n📁 Đang cập nhật links trong #{dir_path}..."
    
    # Tìm tất cả file markdown và html
    files = Dir.glob(File.join(dir_path, '**', '*.{md,html}'))
    
    files.each do |file_path|
      update_links_in_file(file_path, lang)
    end
  end

  def update_links_in_file(file_path, lang)
    content = File.read(file_path)
    original_content = content.dup
    
    # Pattern 1: {% post_url contents/chapter06/21-03-20-06_03_02_convex_function_quadratic_upper_bound %}
    content.gsub!(/\{\%\s*post_url\s+contents\/chapter(\d+)\/([^\s\}]+)\s*\%\}/) do |match|
      chapter = $1
      post_name = $2
      "{% multilang_post_url contents/chapter#{chapter}/#{post_name} %}"
    end
    
    # Pattern 2: {% link contents/chapter01/index.html %}
    content.gsub!(/\{\%\s*link\s+contents\/chapter(\d+)\/index\.html\s*\%\}/) do |match|
      chapter = $1
      "{% link contents/#{lang}/chapter#{chapter}/index.html %}"
    end
    
    # Pattern 3: Direct links như /contents/chapter06/
    content.gsub!(/\/contents\/chapter(\d+)\//) do |match|
      chapter = $1
      "/contents/#{lang}/chapter#{chapter}/"
    end
    
    # Pattern 4: Relative links trong cùng chapter
    content.gsub!(/\[([^\]]+)\]\(([^)]+\.md)\)/) do |match|
      link_text = $1
      file_name = $2
      
      # Nếu là link relative trong cùng thư mục, giữ nguyên
      if file_name.start_with?('.') || file_name.include?('/')
        match
      else
        # Convert thành absolute link với ngôn ngữ hiện tại
        current_dir = File.dirname(file_path)
        if current_dir.include?('/chapter')
          chapter_match = current_dir.match(/chapter(\d+)/)
          if chapter_match
            chapter = chapter_match[1]
            "[#{link_text}](/contents/#{lang}/chapter#{chapter}/#{file_name})"
          else
            match
          end
        else
          match
        end
      end
    end
    
    # Chỉ ghi file nếu có thay đổi
    if content != original_content
      File.write(file_path, content)
      puts "  ✅ Cập nhật #{File.basename(file_path)}"
    end
  end
end

# Chạy script nếu được execute trực tiếp
if __FILE__ == $0
  updater = LinkUpdater.new
  updater.update_all_links
end
