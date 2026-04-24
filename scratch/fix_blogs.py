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

for blog_dir in blog_dirs:
    file_path = os.path.join(base_path, blog_dir, "index.html")
    if not os.path.exists(file_path):
        print(f"Skipping {file_path}, not found.")
        continue

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix configuration errors (relative paths with double slashes)
    content = content.replace("..//css/", "/css/")
    content = content.replace("..//images/", "/images/")
    content = content.replace("..//js/", "/js/")
    content = content.replace("../../common/", "/common/")
    
    # 2. Re-add service.css if it's missing (it was removed in previous turns)
    # Most of these blogs use city-header-section which needs service.css
    if "/css/service.css" not in content:
        # Insert it after common.css
        content = re.sub(r'(<link rel="stylesheet" href="/css/common.css" />)', 
                         r'\1\n    <link rel="stylesheet" href="/css/service.css" />', 
                         content)

    # 3. Fix the footer fetch path just in case
    content = content.replace('fetch("../components/footer3.html")', 'fetch("/components/footer3.html")')
    content = content.replace('fetch("../../components/footer3.html")', 'fetch("/components/footer3.html")')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed {blog_dir}")

# Also process blogs/index.html
index_path = os.path.join(base_path, "index.html")
if os.path.exists(index_path):
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace("..//css/", "/css/")
    content = content.replace("..//images/", "/images/")
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Processed blogs/index.html")
