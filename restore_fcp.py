import sys

file_path = r'c:\Users\jugal\OneDrive\Desktop\carmaa-work\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Make mobile-optimizations and critical fixes blocking again for faster FCP
content = content.replace('<link rel="stylesheet" href="mobile-optimizations.css" media="print" onload="this.media=\'all\'">', '<link rel="stylesheet" href="mobile-optimizations.css">')
content = content.replace('<link rel="stylesheet" href="services-center-fix.css" media="print" onload="this.media=\'all\'">', '<link rel="stylesheet" href="services-center-fix.css">')
content = content.replace('<link rel="stylesheet" href="h1-seo-fix.css" media="print" onload="this.media=\'all\'">', '<link rel="stylesheet" href="h1-seo-fix.css">')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
