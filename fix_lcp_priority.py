import sys

file_path = r'c:\Users\jugal\OneDrive\Desktop\carmaa-work\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Move Preload and fetchpriority to the absolute top for immediate LCP start
preload_tag = '<link rel="preload" as="image" href="assets/hero_car_detailing.webp" fetchpriority="high">'
content = content.replace(preload_tag, '')
content = content.replace('<head>', '<head>\n    ' + preload_tag)

# 2. Delay video initialization to prevent bandwidth competition with LCP image
# We remove the src and autoplay from the HTML and handle it in script.js later
content = content.replace('<video autoplay muted loop playsinline class="hero-video" poster="assets/hero_car_detailing.webp">', 
                          '<video muted loop playsinline class="hero-video" id="heroVideo" poster="assets/hero_car_detailing.webp">')
content = content.replace('<source src="assets/hero_video.mp4" type="video/mp4">', '')

# 3. Add a background image to .hero-bg as a CSS fallback to ensure LCP is recorded instantly
css_fallback = '        .hero-bg { background: url("assets/hero_car_detailing.webp") center/cover no-repeat; }'
content = content.replace('.hero-bg { position: absolute;', css_fallback + '\n        .hero-bg { position: absolute;')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
