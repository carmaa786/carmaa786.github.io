import os

workspace = r"c:\Users\jugal\OneDrive\Desktop\carmaa-work"

preloads = """    <link rel="preconnect" href="https://connect.facebook.net">
    <link rel="preconnect" href="https://www.googletagmanager.com">
    <link rel="preconnect" href="https://www.google-analytics.com">
"""

city_header_preload = '    <link rel="preload" as="image" href="/assets/header-img.jpg" fetchpriority="high">\n'

def add_preloads(file_path, is_city=False):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    added_global = False
    added_city = False
    
    for line in lines:
        new_lines.append(line)
        if '<head>' in line:
            if not added_global:
                new_lines.append(preloads)
                added_global = True
            if is_city and not added_city:
                new_lines.append(city_header_preload)
                added_city = True
                
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

# Homepage
add_preloads(os.path.join(workspace, 'index.html'))

# City pages
for root, dirs, files in os.walk(workspace):
    if 'index.html' in files and root != workspace:
        # Check if it's a city page by looking at the folder name or content
        if 'doorstep-car-washing-service-in-' in root:
            add_preloads(os.path.join(root, 'index.html'), is_city=True)
