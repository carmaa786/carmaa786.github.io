import os
import re

total_added = 0

def get_url_path(file_path):
    # Normalize path
    normalized = file_path.replace('\\', '/').lstrip('./')
    
    if normalized == 'index.html':
        return '/'
    elif normalized.endswith('/index.html'):
        return '/' + normalized.replace('/index.html', '/')
    else:
        return '/' + normalized

for root, dirs, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root or 'scratch' in root or 'components' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            has_canonical = '<link rel="canonical"' in content or "<link rel='canonical'" in content
            
            if not has_canonical:
                url_path = get_url_path(path)
                canonical_tag = f'\n    <link rel="canonical" href="https://carmaacarcare.com{url_path}" />'
                
                # Insert just after <head> or <head ...>
                # We use regex to find the head tag
                new_content = re.sub(r'(<head[^>]*>)', r'\1' + canonical_tag, content, count=1, flags=re.IGNORECASE)
                
                if new_content != content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Added to {path}: {url_path}")
                    total_added += 1

print(f"Total canonical tags added: {total_added}")
