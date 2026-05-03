import os
import glob
from bs4 import BeautifulSoup

def audit_internal_images():
    blog_files = glob.glob('blogs/*/index.html')
    missing_images = []
    
    for f in blog_files:
        if 'blogs/index.html' in f: continue
        
        try:
            with open(f, 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file.read(), 'html.parser')
                left_section = soup.find('div', class_='service-left-section')
                if left_section:
                    img = left_section.find('img')
                    if not img:
                        missing_images.append(f)
        except Exception as e:
            print(f"Error reading {f}: {e}")
            
    print("\n".join(missing_images))

if __name__ == "__main__":
    audit_internal_images()
