import os
import re

html_files = []
for root, dirs, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root:
        continue
    for f in files:
        if f.endswith('.html'):
            html_files.append(os.path.join(root, f))

print(f'Found {len(html_files)} HTML files.')
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        imgs = re.findall(r'<img[^>]*>', content)
        if imgs:
            print(f'\n{f}: {len(imgs)} images')
            for i, img in enumerate(imgs):
                has_lazy = 'loading="lazy"' in img or "loading='lazy'" in img or "loading=lazy" in img
                is_above_fold = 'topbar' in img or 'logo' in img or 'hero' in img or 'whatsapp' in img or 'contactus' in img or i == 0
                print(f'  {i}: Lazy={has_lazy} - {img[:100]}...')
