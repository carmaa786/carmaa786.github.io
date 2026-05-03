import os

missing = []
total = 0

for root, dirs, files in os.walk('.'):
    if 'node_modules' in root or '.git' in root or 'scratch' in root or 'components' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            total += 1
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                if '<link rel="canonical"' not in content and "<link rel='canonical'" not in content:
                    missing.append(path)

print(f'Total HTML files: {total}')
print(f'Missing canonical tags: {len(missing)}')
if missing:
    for m in missing[:10]:
        print(f"Missing in: {m}")
