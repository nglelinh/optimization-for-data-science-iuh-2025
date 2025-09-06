# Reusable Content Box Styles Guide

This guide explains how to use the reusable content box styles in your markdown files instead of inline styles.

## Available Box Types

### 1. Insight Box (Yellow)
For key insights, important concepts, and "aha" moments.

**Old way:**
```html
<div style="background-color: #fff8dc; padding: 15px; border-radius: 8px; margin: 20px 0;">
<strong>Key Insight:</strong> The optimal solution of a linear program always occurs at a vertex!
</div>
```

**New way:**
```html
<div class="content-box insight-box">
<strong>Key Insight:</strong> The optimal solution of a linear program always occurs at a vertex!
</div>
```

### 2. Exercise Box (Light Blue)
For interactive exercises, hands-on activities, and practice problems.

**Old way:**
```html
<div style="background-color: #f0f8ff; padding: 15px; border-radius: 8px; margin: 20px 0;">
<strong>Interactive Exercise:</strong> Use the sliders below to explore different combinations.
</div>
```

**New way:**
```html
<div class="content-box exercise-box">
<strong>Interactive Exercise:</strong> Use the sliders below to explore different combinations.
</div>
```

### 3. Summary Box (Light Green)
For summaries, takeaways, and learning objectives.

**Old way:**
```html
<div style="background-color: #e8f5e8; padding: 20px; border-radius: 8px; margin: 20px 0;">
<strong>🎯 What you've learned:</strong>
<ul>
<li>Linear Programming fundamentals</li>
<li>Geometric intuition</li>
</ul>
</div>
```

**New way:**
```html
<div class="content-box summary-box">
<strong class="emoji-title">🎯 What you've learned:</strong>
<ul>
<li>Linear Programming fundamentals</li>
<li>Geometric intuition</li>
</ul>
</div>
```

### 4. Warning Box (Light Red)
For warnings, problems, or things to be careful about.

**Old way:**
```html
<div style="background-color: #ffebee; padding: 15px; border-radius: 8px; margin: 20px 0;">
<strong>⚠️ Problem:</strong> The L₀ "norm" makes this problem non-convex!
</div>
```

**New way:**
```html
<div class="content-box warning-box">
<strong class="emoji-title">⚠️ Problem:</strong> The L₀ "norm" makes this problem non-convex!
</div>
```

### 5. Additional Box Types

#### Info Box (Light Gray)
```html
<div class="content-box info-box">
<strong>Information:</strong> General information or neutral content.
</div>
```

#### Note Box (Light Purple)
```html
<div class="content-box note-box">
<strong>Note:</strong> Side notes or additional context.
</div>
```

#### Example Box (Light Orange)
```html
<div class="content-box example-box">
<strong>Example:</strong> Concrete examples or demonstrations.
</div>
```

#### Question Box (Light Cyan)
```html
<div class="content-box question-box">
<strong class="emoji-title">🧠 Self-Check Questions:</strong>
<ol>
<li>Why does the optimal solution occur at a vertex?</li>
<li>What are the key transformations for standard form?</li>
</ol>
</div>
```

## Benefits of Using CSS Classes

1. **Consistency**: All boxes will have the same styling across all pages
2. **Maintainability**: Change the styling in one place (CSS file) and it updates everywhere
3. **Accessibility**: Better semantic structure and easier to add accessibility features
4. **Performance**: Smaller HTML files and better caching
5. **Responsive**: Built-in responsive design for mobile devices
6. **Visual Enhancement**: Added colored left borders for better visual hierarchy

## Migration Strategy

1. **Identify** all inline styled divs in your markdown files
2. **Replace** them with the appropriate CSS class
3. **Test** the styling to ensure it looks correct
4. **Customize** the CSS if needed for your specific use case

## Customization

If you need to modify the styling, edit the `/public/css/content-boxes.css` file. The styles are organized with:
- Base styles in `.content-box`
- Specific colors and borders in individual box classes
- Responsive adjustments for mobile devices
