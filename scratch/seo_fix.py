import os
import glob
import re

BASE_URL = "https://carmaacarcare.com"
ROOT_DIR = "c:\\Users\\jugal\\OneDrive\\Desktop\\carmaa-work"

# Directories to exclude from sitemap and indexing
EXCLUDE_DIRS = [".git", ".github", "scratch", "node_modules"]
EXCLUDE_FILES = ["old_index.html", "old_index_8a.html", "sitemap.html"]

def get_url_path(filepath):
    # Convert absolute path to relative path from ROOT_DIR
    rel_path = os.path.relpath(filepath, ROOT_DIR)
    # Replace backslashes with forward slashes
    rel_path = rel_path.replace('\\', '/')
    
    if rel_path == "index.html":
        return "/"
    elif rel_path.endswith("/index.html"):
        return "/" + rel_path[:-11] + "/"
    else:
        return "/" + rel_path

def add_canonical_tag(filepath, url):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Check if this is a redirect file
    refresh_match = re.search(r'<meta http-equiv="refresh" content="\d+;url=([^"]+)">', content)
    if refresh_match:
        target_path = refresh_match.group(1)
        # Construct target url
        if target_path.startswith('/'):
            target_url = BASE_URL + target_path
        else:
            target_url = BASE_URL + "/" + target_path
        # Use target_url as canonical
        url_encoded = target_url.replace(" ", "%20")
        is_redirect = True
    else:
        url_encoded = url.replace(" ", "%20")
        is_redirect = False

    canonical_tag = f'<link rel="canonical" href="{url_encoded}" />'
    
    # Check if canonical tag already exists
    if '<link rel="canonical"' in content:
        # Replace existing canonical tag
        content = re.sub(r'<link rel="canonical"[^>]*>', canonical_tag, content)
    else:
        # Insert before </head> or at the end of <head>
        if '</head>' in content:
            content = content.replace('</head>', f'    {canonical_tag}\n</head>')
        else:
            print(f"Warning: No </head> found in {filepath}")
            return is_redirect

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    return is_redirect

def generate_sitemap(urls):
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for url in sorted(urls):
        url_encoded = url.replace(" ", "%20")
        # Escape special characters for XML
        xml_url = url_encoded.replace("'", "&apos;").replace('"', "&quot;").replace('&', "&amp;").replace('<', "&lt;").replace('>', "&gt;")
        sitemap_content += '  <url>\n'
        sitemap_content += f'    <loc>{xml_url}</loc>\n'
        sitemap_content += '  </url>\n'
    
    sitemap_content += '</urlset>\n'
    
    with open(os.path.join(ROOT_DIR, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(sitemap_content)

def update_robots_txt():
    robots_content = """User-agent: *
Allow: /
Disallow: /old_index.html
Disallow: /old_index_8a.html
Disallow: /scratch/
Disallow: /lh-report.json
Disallow: /*.py$
Disallow: /*.md$
Disallow: /CITY_PAGE_SEO_STRATEGY.md
Disallow: /OPTIMIZATION_SUMMARY.md
Disallow: /PERFORMANCE_GUIDELINES.md

# Sitemaps
Sitemap: https://carmaacarcare.com/sitemap.xml
"""
    with open(os.path.join(ROOT_DIR, 'robots.txt'), 'w', encoding='utf-8') as f:
        f.write(robots_content)

def main():
    sitemap_urls = set()
    for root, dirs, files in os.walk(ROOT_DIR):
        # Exclude directories
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        
        for file in files:
            if file == "index.html":
                filepath = os.path.join(root, file)
                
                # Check if it's in EXCLUDE_FILES (for root dir)
                if root == ROOT_DIR and file in EXCLUDE_FILES:
                    continue
                    
                # We skip old_index.html-guide-car-ceramic-coating-worth-it etc if any
                if "old_index" in filepath or "scratch" in filepath:
                    continue
                    
                url_path = get_url_path(filepath)
                full_url = BASE_URL + url_path
                
                # Add canonical tag and check if it's a redirect
                is_redirect = add_canonical_tag(filepath, full_url)
                
                # Only add to sitemap if it's NOT a redirect
                if not is_redirect:
                    sitemap_urls.add(full_url)
                
    generate_sitemap(list(sitemap_urls))
    update_robots_txt()
    print(f"Processed URLs. Final sitemap contains {len(sitemap_urls)} URLs.")

if __name__ == "__main__":
    main()
