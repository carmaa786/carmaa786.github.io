import os
import re

domain = "https://carmaacarcare.com"

def get_expected_canonical(file_path):
    # Normalize path
    normalized = file_path.replace('\\', '/').lstrip('./')
    if normalized == 'index.html':
        return f"{domain}/"
    if normalized.endswith('/index.html'):
        return f"{domain}/{normalized[:-10]}/"
    return f"{domain}/{normalized}"

missing = []
duplicates = []
incorrect = []
total = 0

canonical_pattern = re.compile(r'<link rel=["\']canonical["\'] href=["\']([^"\']+)["\']', re.IGNORECASE)

for root, dirs, files in os.walk('.'):
    if any(x in root for x in ['node_modules', '.git', 'scratch', 'components']): continue
    for file in files:
        if file.endswith('.html'):
            total += 1
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            matches = canonical_pattern.findall(content)
            if not matches:
                missing.append(path)
            elif len(matches) > 1:
                duplicates.append(path)
            else:
                expected = get_expected_canonical(path)
                actual = matches[0]
                # Allow for minor differences like trailing slashes in blogs if they are consistent
                if actual != expected and actual != expected.rstrip('/'):
                    incorrect.append((path, actual, expected))

print(f"Total HTML files: {total}")
print(f"Missing: {len(missing)}")
print(f"Duplicates: {len(duplicates)}")
print(f"Incorrect: {len(incorrect)}")

if missing:
    print("\nMissing Canonical Tags:")
    for m in missing: print(f"  {m}")

if duplicates:
    print("\nDuplicate Canonical Tags:")
    for d in duplicates: print(f"  {d}")

if incorrect:
    print("\nIncorrect Canonical Tags (Actual vs Expected):")
    for path, actual, expected in incorrect:
        print(f"  {path}: \n    Actual:   {actual}\n    Expected: {expected}")
