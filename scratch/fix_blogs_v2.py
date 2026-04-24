import os
import re

blog_dirs = [
    "why-carmaa-is-becoming-dehradun's-choice",
    "why-carmaa-carcare-is-perfect",
    "ultimate-guide-to-doorstep-car-wash",
    "ultimate-guide-to-car-cleaning-2025",
    "top-tips-for-exterior-and-interior-car-cleaning",
    "the-ultimate-doorstep-car-wash-service-provider-in-dehradun",
    "rise-of-car-subscription-model",
    "how-to-wash-your-car-without-a-hose",
    "how-to-maintain-your-car-shine",
    "dry-cleaning-services-at-your-doorstep",
    "doorstep-car-decor-in-dehradun",
    "car-maintenance-doorstep-services",
    "b2b-fleet-car-washing-in-dehradun"
]

base_path = r"c:\Users\jugal\OneDrive\Desktop\carmaa-work\blogs"

def fix_content(content):
    # 1. Standardize relative paths to root-relative
    # Handle both ../ and ../../ and the messy ..// variants
    content = re.sub(r'src=["\']\.\./\.\./common/', 'src="/common/', content)
    content = re.sub(r'src=["\']\.\./common/', 'src="/common/', content)
    content = re.sub(r'href=["\']\.\./\.\./css/', 'href="/css/', content)
    content = re.sub(r'href=["\']\.\./css/', 'href="/css/', content)
    content = re.sub(r'src=["\']\.\./\.\./js/', 'src="/js/', content)
    content = re.sub(r'src=["\']\.\./js/', 'src="/js/', content)
    content = re.sub(r'src=["\']\.\./\.\./images/', 'src="/images/', content)
    content = re.sub(r'src=["\']\.\./images/', 'src="/images/', content)
    content = re.sub(r'src=["\']\.\.//images/', 'src="/images/', content)
    content = re.sub(r'href=["\']\.\.//css/', 'href="/css/', content)

    # 2. Fix external-integration.js import
    content = content.replace("from './js/external-integration.js'", "from '/js/external-integration.js'")
    content = content.replace('from "./js/external-integration.js"', 'from "/js/external-integration.js"')

    # 3. Ensure service.css is present (robustly)
    if "/css/service.css" not in content:
        # Match common.css with or without space/slash at end
        pattern = r'(<link\s+rel="stylesheet"\s+href="/css/common.css"\s*/?>)'
        match = re.search(pattern, content)
        if match:
            tag = match.group(1)
            content = content.replace(tag, tag + '\n    <link rel="stylesheet" href="/css/service.css" />')

    # 4. Standardize fetch paths
    content = re.sub(r'fetch\(["\']\.\./components/', 'fetch("/components/', content)
    content = re.sub(r'fetch\(["\']\.\./\.\./components/', 'fetch("/components/', content)

    return content

for blog_dir in blog_dirs:
    file_path = os.path.join(base_path, blog_dir, "index.html")
    if not os.path.exists(file_path):
        continue

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = fix_content(content)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {blog_dir}")
    else:
        print(f"No changes needed for {blog_dir}")

# Process blogs/index.html
index_path = os.path.join(base_path, "index.html")
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = fix_content(content)
    if new_content != content:
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Fixed blogs/index.html")
