import re
content = open('index.html', encoding='utf-8').read()
content = re.sub(r'(<img[^>]*?)(loading=\"lazy\")([^>]*?>)', r'\1\2 decoding=\"async\"\3', content)
with open('index.html', 'w', encoding='utf-8') as f: f.write(content)
