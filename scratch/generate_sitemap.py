import os

base_url = "https://carmaacarcare.com"
root_dir = "."

# Paths to exclude from sitemap
exclude_prefixes = [
    "assets", "css", "js", "images", "scripts", "common", "components", "scratch", ".git", ".github"
]

# Explicitly exclude redirect folders we created earlier
redirect_paths = [
    "blogs/doorstep-car-cleaning-service-noida",
    "why-carmaa-is-becoming-dehradun's-choice",
    "blogs/doorstep-car-washing-service-in-gurgaon",
    "doorstep-car-washing-service-in-delhi/blogs",
    "best-car-mechanics-in-dehradun/blogs",
    "blogs/why-carmaa-is-becoming-dehradun's-choice/blogs",
    "blogs/dry-cleaning-services-at-your-doorstep/blogs",
    "blogs/about",
    "blogs/doorstep-car-washing-service-in-dehradun",
    "blogs/doorstep-car-washing-service-in-meerut",
    "doorstep-car-washing-service-in-Rishikesh/blogs",
    "doorstep-car-washing-service-in-Haridwar/blogs",
    "doorstep-car-washing-service-in-aligarh",
    "doorstep-car-washing-service-in-roorkee",
    "doorstep-car-washing-service-in-haldwani",
    "doorstep-car-washing-service-in-chandigarh",
    "doorstep-car-washing-service-in-mussoorie"
]

pages = []

for root, dirs, files in os.walk(root_dir):
    # Skip excluded directories
    dirs[:] = [d for d in dirs if d not in exclude_prefixes]
    
    if "index.html" in files:
        rel_path = os.path.relpath(root, root_dir)
        if rel_path == ".":
            path = "/"
        else:
            path = "/" + rel_path.replace("\\", "/") + "/"
            
        # Check if path is in redirects
        clean_path = path.strip('/')
        if any(clean_path == r.strip('/') for r in redirect_paths):
            continue
            
        pages.append(base_url + path)

pages.sort()

sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""

for page in pages:
    sitemap_content += f"  <url>\n    <loc>{page}</loc>\n  </url>\n"

sitemap_content += "</urlset>"

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_content)

print(f"Generated sitemap.xml with {len(pages)} URLs.")
