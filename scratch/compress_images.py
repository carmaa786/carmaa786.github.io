from PIL import Image
import os

input_files = [
    r"C:\Users\jugal\.gemini\antigravity\brain\60717174-4cfb-4f79-90d8-43af95ebc528\fluids_main_1777869855347.png",
    r"C:\Users\jugal\.gemini\antigravity\brain\60717174-4cfb-4f79-90d8-43af95ebc528\fluids_coolant_1777869877415.png",
    r"C:\Users\jugal\.gemini\antigravity\brain\60717174-4cfb-4f79-90d8-43af95ebc528\basics_dashboard_1777869900059.png",
    r"C:\Users\jugal\.gemini\antigravity\brain\60717174-4cfb-4f79-90d8-43af95ebc528\basics_tires_1777869920323.png"
]

output_names = [
    "fluids-main.webp",
    "fluids-coolant.webp",
    "basics-dashboard.webp",
    "basics-tires.webp"
]

output_dir = r"c:\Users\jugal\OneDrive\Desktop\carmaa-work\assets\blogs"

os.makedirs(output_dir, exist_ok=True)

for in_path, out_name in zip(input_files, output_names):
    if not os.path.exists(in_path):
        print(f"Error: {in_path} not found.")
        continue
        
    out_path = os.path.join(output_dir, out_name)
    
    with Image.open(in_path) as img:
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")
            
        max_width = 800
        if img.width > max_width:
            wpercent = (max_width / float(img.width))
            hsize = int((float(img.height) * float(wpercent)))
            img = img.resize((max_width, hsize), Image.Resampling.LANCZOS)
            
        img.save(out_path, "webp", quality=60, method=6)
        
        size_kb = os.path.getsize(out_path) / 1024
        print(f"Saved {out_path} - Size: {size_kb:.2f} KB")
