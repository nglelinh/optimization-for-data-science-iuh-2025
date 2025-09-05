# Troubleshooting Guide

## JavaScript 404 Errors

If you're still seeing JavaScript 404 errors after deployment, try these steps:

### 1. Clear Browser Cache
- Hard refresh: `Ctrl+F5` (Windows) or `Cmd+Shift+R` (Mac)
- Or clear browser cache completely

### 2. Check GitHub Actions Status
- Go to: https://github.com/nglelinh/optimization-for-data-science-iuh-2025/actions
- Ensure the latest "Build and Deploy Jekyll Site" workflow completed successfully
- If failed, check the logs for errors

### 3. Verify File Deployment
Test these URLs directly in your browser:
- https://nglelinh.github.io/optimization-for-data-science-iuh-2025/public/js/multilang.js
- https://nglelinh.github.io/optimization-for-data-science-iuh-2025/public/js/script.js
- https://nglelinh.github.io/optimization-for-data-science-iuh-2025/public/css/hyde.css

### 4. Check Console Errors
- Open browser developer tools (F12)
- Check Console tab for specific error messages
- Look at Network tab to see failed requests

### 5. GitHub Pages Settings
Verify in your repository settings:
- Go to Settings → Pages
- Source should be "GitHub Actions"
- Custom domain should be empty (unless you have one)

### 6. DNS/CDN Cache
GitHub Pages uses CDN caching. If files were previously missing:
- Wait 10-15 minutes for CDN cache to expire
- Or use different browser/incognito mode

### 7. Test Local Development
```bash
# Test locally with correct baseurl
bundle exec jekyll serve --baseurl="/optimization-for-data-science-iuh-2025"

# Then visit: http://localhost:4000/optimization-for-data-science-iuh-2025/
```

## Expected File Structure
After successful deployment, these files should exist:
```
optimization-for-data-science-iuh-2025/
├── public/
│   ├── js/
│   │   ├── multilang.js
│   │   └── script.js
│   └── css/
│       ├── hyde.css
│       └── poole.css
├── contents/
│   ├── en/
│   └── vi/
└── index.html
```

## Configuration Summary
Key files that were updated:

### _config.yml
```yaml
url: https://nglelinh.github.io
baseurl: '/optimization-for-data-science-iuh-2025'
```

### _layouts/default.html
```html
<script src='{{ site.baseurl }}/public/js/script.js'></script>
<script src='{{ site.baseurl }}/public/js/multilang.js'></script>
```

### _plugins/multilang.rb
```ruby
baseurl = site.config['baseurl'] || ''
# ... baseurl support added to language switching
```

## Contact
If issues persist, check:
1. GitHub Actions logs
2. Repository settings
3. Browser developer tools
4. Try different browsers/devices
