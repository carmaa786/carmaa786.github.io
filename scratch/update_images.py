import os
import re
from PIL import Image

def process_html_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    original_content = content
    
    # Find all img tags
    def replace_img(match):
        img_tag = match.group(0)
        if 'width=' in img_tag and 'height=' in img_tag:
            return img_tag # Already has dimensions
            
        src_match = re.search(r'src=["\']([^"\']+)["\']', img_tag)
        if not src_match:
            return img_tag
            
        src = src_match.group(1)
        if src.startswith('http') or src.startswith('//'):
            return img_tag
            
        # resolve path
        # remove leading slash
        local_src = src.lstrip('/')
        if not os.path.exists(local_src):
            # try relative to the html file
            local_src = os.path.join(os.path.dirname(filepath), src)
            if not os.path.exists(local_src):
                return img_tag
                
        try:
            with Image.open(local_src) as img:
                w, h = img.size
                
                # Insert width and height before the closing >
                # Handle self-closing /> or >
                if img_tag.endswith('/>'):
                    return img_tag[:-2] + f' width="{w}" height="{h}" />'
                else:
                    return img_tag[:-1] + f' width="{w}" height="{h}">'
        except Exception as e:
            return img_tag

    new_content = re.sub(r'<img[^>]+>', replace_img, content)
    
    if new_content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Added missing dimensions to {filepath}")

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root: continue
    for file in files:
        if file.endswith('.html'):
            process_html_file(os.path.join(root, file))
