import os
import glob

files = [
    r"c:\Users\jugal\OneDrive\Desktop\carmaa-work\blogs\how-to-wash-your-car-without-a-hose\index.html",
    r"c:\Users\jugal\OneDrive\Desktop\carmaa-work\blogs\service-definitions-car-wash-vs-car-detailing\index.html",
    r"c:\Users\jugal\OneDrive\Desktop\carmaa-work\blogs\protecting-car-paint-delhi-ncr-pollution\index.html",
    r"c:\Users\jugal\OneDrive\Desktop\carmaa-work\blogs\seasonal-car-care-monsoon-and-summer\index.html",
    r"c:\Users\jugal\OneDrive\Desktop\carmaa-work\blogs\interior-cleaning-and-hard-water-stains\index.html",
]

for filepath in files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # We want to remove the </div> that closes .service-right-section prematurely.
        # It typically looks like:
        #         </div>
        #
        #         <div class="contact-section">
        
        old_str = '        </div>\n\n        <div class="contact-section">'
        new_str = '        <div class="contact-section">'
        
        if old_str in content:
            content = content.replace(old_str, new_str)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed {filepath}")
        else:
            old_str2 = '        </div>\n        <div class="contact-section">'
            if old_str2 in content:
                content = content.replace(old_str2, new_str)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fixed {filepath} (variation)")
            else:
                print(f"Could not find pattern in {filepath}")
    else:
        print(f"File not found: {filepath}")
