import os
import re

cities = ["delhi", "faridabad", "gurgaon", "noida", "gaziabad"]
base_path = r"c:\Users\jugal\OneDrive\Desktop\carmaa-work"

for city in cities:
    dir_name = f"doorstep-car-washing-service-in-{city}"
    file_path = os.path.join(base_path, dir_name, "index.html")
    
    if not os.path.exists(file_path):
        print(f"Skipping {city}, file not found: {file_path}")
        continue
        
    print(f"Processing {city}...")
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # 1. Remove inline styles for headers in Benefits section
    content = re.sub(r'<h2 style="font-size: 24px; color: #000;"\s*>BENEFITS</h2>', '<h2>BENEFITS</h2>', content)
    content = re.sub(r'<h2 style="font-size: 24px;">Choosing Carmaa’s Car Washing Service in (.*?)</h2>', r'<h2>Choosing Carmaa’s Car Washing Service in \1</h2>', content)
    
    # 2. Add width/height to icons
    icon_images = [
        "mechanic.png",
        "thumb.png",
        "tool.png",
        "car.png"
    ]
    for img in icon_images:
        pattern = fr'<img src="/images/home-page/benefits/{img}" alt="(.*?)" loading="lazy"/>'
        replacement = fr'<img src="/images/home-page/benefits/{img}" alt="\1" loading="lazy" width="50" height="50"/>'
        content = re.sub(pattern, replacement, content)
        
    # 3. Remove inline styles for Commitment header
    content = re.sub(r'<h2 style="font-size: 32px; color: #000;">Our Commitment to Quality Car Washing Service in (.*?)</h2>', r'<h2>Our Commitment to Quality Car Washing Service in \1</h2>', content)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Done.")
