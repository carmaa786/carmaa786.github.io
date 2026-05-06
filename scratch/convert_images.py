import os
from PIL import Image
import pillow_avif

def convert_image(source_path, target_width, ext):
    img = Image.open(source_path)
    # Calculate new height
    wpercent = (target_width / float(img.size[0]))
    target_height = int((float(img.size[1]) * float(wpercent)))
    
    # Resize
    img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
    
    # Generate target path
    filename = os.path.basename(source_path).split('.')[0]
    device = "mobile" if target_width <= 768 else "desktop"
    target_name = f"{filename}_{device}.{ext}"
    target_path = os.path.join(os.path.dirname(source_path), target_name)
    
    # Save
    if ext == 'avif':
        img.save(target_path, 'AVIF', quality=85)
    else:
        img.save(target_path, 'WEBP', quality=85)
    
    print(f"Saved {target_path} ({target_width}x{target_height})")

if __name__ == "__main__":
    source_img = "assets/hero_car_detailing.webp"
    
    # Mobile versions
    convert_image(source_img, 768, "webp")
    convert_image(source_img, 768, "avif")
    
    # Desktop versions
    convert_image(source_img, 1920, "webp")
    convert_image(source_img, 1920, "avif")
