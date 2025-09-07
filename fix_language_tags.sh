#!/bin/bash

# Script to fix language tags in Vietnamese chapter files
# This script changes 'lang: en' to 'lang: vi' in all Vietnamese chapter files

cd "/Users/nguyenlelinh/teaching/Optimization/convex-optimization-for-all.github.io"

echo "Fixing language tags in Vietnamese chapter files..."

# List of files that need to be fixed (found from grep search)
files=(
    "contents/vi/chapter05/index.html"
    "contents/vi/chapter06/index.html"
    "contents/vi/chapter07/index.html"
    "contents/vi/chapter08/index.html"
    "contents/vi/chapter09/index.html"
    "contents/vi/chapter10/index.html"
    "contents/vi/chapter11/index.html"
    "contents/vi/chapter12/index.html"
    "contents/vi/chapter13/index.html"
    "contents/vi/chapter14/index.html"
    "contents/vi/chapter15/index.html"
    "contents/vi/chapter16/index.html"
    "contents/vi/chapter17/index.html"
    "contents/vi/chapter18/index.html"
    "contents/vi/chapter19/index.html"
    "contents/vi/chapter20/index.html"
    "contents/vi/chapter21/index.html"
    "contents/vi/chapter22/index.html"
    "contents/vi/chapter23/index.html"
    "contents/vi/chapter24/index.html"
    "contents/vi/chapter25/index.html"
)

# Fix each file
for file in "${files[@]}"; do
    if [ -f "$file" ]; then
        echo "Fixing $file..."
        sed -i.bak 's/lang: en/lang: vi/' "$file"
        echo "✓ Fixed $file"
    else
        echo "⚠ File not found: $file"
    fi
done

echo ""
echo "All files processed. Checking results..."

# Verify the changes
echo ""
echo "Files that still have 'lang: en' in Vietnamese directory:"
grep -l "lang: en" contents/vi/chapter*/index.html 2>/dev/null || echo "None found - all files fixed!"

echo ""
echo "Files that now have 'lang: vi' in Vietnamese directory:"
grep -l "lang: vi" contents/vi/chapter*/index.html | wc -l | xargs echo "Total:"
