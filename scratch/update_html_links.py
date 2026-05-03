import os
import re

css_files_to_remove = [
    'styles.css',
    'footer-new.css',
    'mobile-optimizations.css',
    'story-mobile-enhanced.css',
    'carmaa-difference-carousel.css',
    'promises-carousel.css',
    'how-it-works-carousel.css',
    'professional-animations.css',
    'stats-carousel.css',
    'car-journey.css',
    'scroll-animations.css'
]

def process_html_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    original_content = content
    
    # Remove old links
    for css in css_files_to_remove:
        pattern = r'<link[^>]*href=["\'](?:[^"\']*/)?' + re.escape(css) + r'["\'][^>]*>'
        content = re.sub(pattern, '', content)
    
    # Clean up empty lines left behind
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)

    # Insert new bundle link if we removed something
    if content != original_content and 'bundle.min.css' not in content:
        bundle_link = '    <link rel="stylesheet" href="/bundle.min.css" media="print" onload="this.media=\'all\'">\n'
        content = content.replace('</head>', bundle_link + '</head>')
        
    # Check for hero video preload
    if '<video' in content and 'heroVideo' in content and 'preload' not in content[:content.find('</head>')]:
        # find the poster image if any
        poster_match = re.search(r'<video[^>]*poster=["\']([^"\']+)["\']', content)
        if poster_match:
            poster_url = poster_match.group(1)
            preload_tag = f'    <link rel="preload" as="image" href="{poster_url}" fetchpriority="high">\n'
            content = content.replace('</head>', preload_tag + '</head>')
            
    # Fix img/video without width/height
    # This is trickier since we want to avoid UI shifts. We will only add it to the specific assets that need it
    # But wait, index.html didn't seem to have missing dimensions. Let's just write what we modified.
        
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated CSS and preloads for {filepath}")

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root: continue
    for file in files:
        if file.endswith('.html'):
            process_html_file(os.path.join(root, file))
