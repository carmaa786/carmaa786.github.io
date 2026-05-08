import os
from PIL import Image

def optimize_image(input_path, output_dir, widths):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    img = Image.open(input_path)
    
    for width in widths:
        # Calculate height to maintain aspect ratio
        height = int((width / float(img.size[0])) * float(img.size[1]))
        resized_img = img.resize((width, height), Image.Resampling.LANCZOS)
        
        output_path = os.path.join(output_dir, f"{base_name}_{width}w.webp")
        resized_img.save(output_path, "WEBP", quality=80)
        print(f"Generated: {output_path}")

if __name__ == "__main__":
    hero_img = "assets/hero_car_detailing_desktop.webp"
    widths = [480, 768, 1200]
    optimize_image(hero_img, "assets/hero", widths)
