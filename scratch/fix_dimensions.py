import os
from bs4 import BeautifulSoup
from PIL import Image

workspace = r"c:\Users\jugal\OneDrive\Desktop\carmaa-work"

def get_dimensions(img_path):
    # Try different paths
    paths_to_try = [
        os.path.join(workspace, img_path.lstrip('/')),
        os.path.join(workspace, img_path.replace('../', '')),
    ]
    for p in paths_to_try:
        if os.path.exists(p):
            try:
                with Image.open(p) as img:
                    return img.width, img.height
            except:
                pass
    return None, None

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    modified = False
    
    for img in soup.find_all('img'):
        if not img.get('width') or not img.get('height'):
            src = img.get('src')
            if src:
                w, h = get_dimensions(src)
                if w and h:
                    img['width'] = w
                    img['height'] = h
                    modified = True
                    print(f"Added dimensions {w}x{h} to {src} in {file_path}")
    
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(str(soup))

# Process index.html and city pages
process_file(os.path.join(workspace, 'index.html'))

for root, dirs, files in os.walk(workspace):
    for file in files:
        if file == 'index.html' and root != workspace:
            process_file(os.path.join(root, file))
