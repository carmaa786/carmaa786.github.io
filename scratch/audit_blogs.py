import os
import re

blog_dirs = [d for d in os.listdir('blogs') if os.path.isdir(os.path.join('blogs', d))]
issues = {}

for b in blog_dirs:
    idx_path = os.path.join('blogs', b, 'index.html')
    if not os.path.exists(idx_path):
        continue
        
    with open(idx_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    b_issues = []
    
    # 1. Image checks (internal view). Maybe CSS is missing or paths are wrong.
    imgs = re.findall(r'<img[^>]+>', content)
    broken_imgs = []
    missing_classes = []
    for img in imgs:
        src_match = re.search(r'src=["\']([^"\']+)["\']', img)
        if src_match:
            src = src_match.group(1)
            # check if path is relative or absolute correctly
            if not src.startswith('http') and not src.startswith('//'):
                # check if local file exists
                # typical issue: src="images/..." but it should be "../../images/..." or "/images/..."
                local_path = src.lstrip('/')
                if not os.path.exists(local_path):
                    # try relative
                    rel_path = os.path.join('blogs', b, src)
                    if not os.path.exists(rel_path):
                        broken_imgs.append(src)
                        
        # Check if img has responsive class or style
        if 'class=' not in img and 'style=' not in img and 'width=' not in img:
            missing_classes.append(img)
            
    if broken_imgs:
        b_issues.append(f"Broken/Unresolvable images: {broken_imgs}")
        
    # 2. Contact us checks
    # Check if "Contact" or link to contactus is present
    if '/contactus' not in content and 'contact us' not in content.lower():
        b_issues.append("Missing Contact Us link or section")
        
    if b_issues:
        issues[b] = b_issues

for b, errors in issues.items():
    print(f"[{b}]")
    for e in errors:
        print(f"  - {e}")
