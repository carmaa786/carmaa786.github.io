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

canonical_pattern = re.compile(r'(<link rel=["\']canonical["\'] href=["\'])([^"\']+)(" ?/?>)', re.IGNORECASE)

total_fixed = 0

for root, dirs, files in os.walk('.'):
    if any(x in root for x in ['node_modules', '.git', 'scratch', 'components']): continue
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            expected = get_expected_canonical(path)
            
            def replace_func(match):
                prefix, actual, suffix = match.groups()
                # If it's the privacy policy error we found earlier
                if "privacy-policy" in path and "terms-conditions" in actual:
                    return f'{prefix}{expected}{suffix}'
                
                # If it's a capitalization issue or missing trailing slash on non-file URL
                if actual.lower().startswith("https://carmaacarcare.com"):
                    # Check for capitalization in domain
                    if "Carmaacarcare" in actual:
                        return f'{prefix}{actual.replace("Carmaacarcare", "carmaacarcare")}{suffix}'
                    
                    # If it's a blog post and the slug is mostly the same but maybe truncated or without apostrophe,
                    # we keep the "Actual" one as it might be a deliberate SEO choice.
                    # Otherwise, if it's a location page or main page, we prefer the "Expected" one.
                    if "blogs/" in path:
                        return match.group(0) # Keep as is for blogs to avoid breaking deliberate slugs
                    
                    # For everything else, ensure it's correct
                    if actual != expected and actual.rstrip('/') != expected.rstrip('/'):
                         return f'{prefix}{expected}{suffix}'
                
                return match.group(0)

            new_content = canonical_pattern.sub(replace_func, content)
            
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Fixed: {path}")
                total_fixed += 1

print(f"Total files fixed: {total_fixed}")
