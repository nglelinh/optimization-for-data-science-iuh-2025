module Jekyll
  class LanguageTag < Liquid::Tag
    def initialize(tag_name, lang, tokens)
      super
      @lang = lang.strip
    end

    def render(context)
      site = context.registers[:site]
      page = context.registers[:page]
      
      current_lang = page['lang'] || site.config['default_lang']
      
      if current_lang == @lang
        return "active"
      else
        return ""
      end
    end
  end

  class TranslateTag < Liquid::Tag
    def initialize(tag_name, key, tokens)
      super
      @key = key.strip
    end

    def render(context)
      site = context.registers[:site]
      page = context.registers[:page]
      
      current_lang = page['lang'] || site.config['default_lang']
      
      if site.config['t'] && site.config['t'][current_lang] && site.config['t'][current_lang][@key]
        return site.config['t'][current_lang][@key]
      else
        return @key
      end
    end
  end

  class LanguageSwitchTag < Liquid::Tag
    def render(context)
      site = context.registers[:site]
      page = context.registers[:page]
      
      current_lang = page['lang'] || site.config['default_lang']
      other_lang = current_lang == 'en' ? 'vi' : 'en'
      
      # Tạo URL cho ngôn ngữ khác
      current_url = page['url']
      if current_url.start_with?("/contents/#{current_lang}/")
        other_url = current_url.gsub("/contents/#{current_lang}/", "/contents/#{other_lang}/")
      elsif current_url.start_with?("/contents/")
        # Nếu URL hiện tại không có ngôn ngữ, thêm ngôn ngữ khác
        other_url = current_url.gsub("/contents/", "/contents/#{other_lang}/")
      else
        other_url = "/contents/#{other_lang}/"
      end
      
      switch_text = site.config['t'][current_lang]['switch_language']
      
      return "<a href=\"#{other_url}\" class=\"language-switch\">#{switch_text}</a>"
    end
  end
end

Liquid::Template.register_tag('lang', Jekyll::LanguageTag)
Liquid::Template.register_tag('t', Jekyll::TranslateTag)
Liquid::Template.register_tag('language_switch', Jekyll::LanguageSwitchTag)
