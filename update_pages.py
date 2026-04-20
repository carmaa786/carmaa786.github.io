import os
import glob
import re

inp_replacement = """      const bookingOpenBtn=document.querySelectorAll('.open-booking-modal');
      bookingOpenBtn.forEach(button => {
      button.addEventListener('click', () => {
          setTimeout(() => {
              document.getElementById('nameError').textContent = '';
              document.getElementById('phoneError').textContent = '';
              document.getElementById('addressError').textContent = '';
              document.getElementById('cityError').textContent = '';
              document.getElementById('nameInput').value='';
              document.getElementById('numberInput').value='';
              document.getElementById('addressInput').value='';
              document.getElementById('cityInput').value='';
              document.getElementById('modal-booking-btn').disabled = false;
              document.querySelector('.button-text').style.display = "inline";
              document.querySelector('.button-loader').style.display = "none";
              document.getElementById("parent-div").style.display = "flex";
          }, 0);
      });
  });"""

def inject_geo(path, lat, lng):
    if not os.path.exists(path):
        return
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(path, 'r', encoding='utf-16') as f:
                content = f.read()
        except Exception:
            return

    if '"geo": {' not in content:
        target_re = re.compile(r'"addressCountry":\s*"IN"\s*},')
        replacement = f""""addressCountry": "IN"\n          }},\n          "geo": {{\n            "@type": "GeoCoordinates",\n            "latitude": "{lat}",\n            "longitude": "{lng}"\n          }},"""
        new_content = target_re.sub(replacement, content, count=1)
        if new_content != content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated geo in {path}")
        else:
            print(f"Could not find target address pattern in {path}")


files = glob.glob('**/*.html', recursive=True)
count_inp = 0
for fpath in files:
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            html = f.read()
    except UnicodeDecodeError:
        try:
            with open(fpath, 'r', encoding='utf-16') as f:
                html = f.read()
        except Exception:
            continue
    except Exception:
        continue
    
    if "const bookingOpenBtn=" in html and "document.querySelectorAll('.open-booking-modal')" in html:
        # Check if already added setTimeout
        if "setTimeout(() =>" not in html[html.find(".open-booking-modal"):html.find(".open-booking-modal")+500]:
            pattern = re.compile(r'const\s+bookingOpenBtn\s*=\s*document\.querySelectorAll\(\'.open-booking-modal\'\);\s*bookingOpenBtn\.forEach\(button\s*=>\s*\{\s*button\.addEventListener\(\'click\'\s*,\s*\(\)\s*=>\s*\{.*?document\.getElementById\("parent-div"\)\.style\.display\s*=\s*"flex";\s*\}\);\s*\}\);', re.DOTALL)
            new_html, num = pattern.subn(inp_replacement, html)
            if num > 0:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(new_html)
                count_inp += 1
            else:
                print("Failed to match INP pattern exactly in", fpath)

print(f"Updated INP in {count_inp} files")

inject_geo('doorstep-car-washing-service-in-dehradun/index.html', '30.3165', '78.0322')
inject_geo('doorstep-car-washing-service-in-noida/index.html', '28.5355', '77.3910')
