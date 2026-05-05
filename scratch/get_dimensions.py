from PIL import Image
import os

images = [
    "assets/before.webp",
    "assets/after.webp",
    "assets/hero_car_detailing.webp"
]

for img_path in images:
    full_path = os.path.join(r"c:\Users\jugal\OneDrive\Desktop\carmaa-work", img_path)
    if os.path.exists(full_path):
        with Image.open(full_path) as img:
            print(f"{img_path}: {img.width}x{img.height}")
    else:
        print(f"{img_path}: Not found")
