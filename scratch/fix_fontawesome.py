import os
import re
import urllib.request

fa_url = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css"

try:
    with urllib.request.urlopen(fa_url) as response:
        css = response.read().decode('utf-8')
        
    # Replace relative webfonts path with absolute CDN path
    css = css.replace('../webfonts/', 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/webfonts/')
    
    # Inject font-display: swap into @font-face
    def insert_swap(match):
        content = match.group(0)
        # FontAwesome has font-display:block in some versions, replace it or insert
        if 'font-display:' in content:
            content = re.sub(r'font-display\s*:\s*[^;]+;', 'font-display: swap;', content)
        else:
            content = content.replace('{', '{font-display:swap;', 1)
        return content
        
    css = re.sub(r'@font-face\s*\{[^}]*\}', insert_swap, css)
    
    # Append to bundle.min.css
    with open('bundle.min.css', 'a', encoding='utf-8') as f:
        f.write('\n/* FontAwesome Local Patch */\n' + css)
        
    print("Appended patched FontAwesome to bundle.min.css")
    
    # Remove FontAwesome link from all HTML files
    for root, dirs, files in os.walk('.'):
        if '.git' in root or 'node_modules' in root: continue
        for file in files:
            if file.endswith('.html'):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                pattern = r'<link[^>]*href=["\'][^"\']*font-awesome[^"\']*all\.min\.css["\'][^>]*>'
                content = re.sub(pattern, '', content)
                
                if content != original_content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Removed FontAwesome CDN link from {filepath}")

except Exception as e:
    print(f"Error: {e}")
