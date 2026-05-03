import os
import re

contact_block = """
<div class="blog-contact-us-section" style="margin-top: 40px; padding: 30px; background: #f8fafc; border-radius: 16px; border-left: 5px solid #1B4E9B;">
    <h3 style="color: #1B4E9B; font-family: 'Oswald', sans-serif; margin-bottom: 15px;">Need Professional Car Care? Contact Us!</h3>
    <div style="display: flex; flex-direction: column; gap: 10px; font-family: 'Inter', sans-serif; color: #333;">
        <p style="margin:0;"><strong>Phone:</strong> <a href="tel:+917042555401" style="color: #28B097; text-decoration: none;">+91-70425 55401</a></p>
        <p style="margin:0;"><strong>Email:</strong> <a href="mailto:support@carmaacarcare.com" style="color: #28B097; text-decoration: none;">support@carmaacarcare.com</a></p>
        <p style="margin:0;"><strong>Address:</strong> Tea Estate Banjarawala, Kedarpur, Dehradun</p>
    </div>
</div>
"""

blog_dirs = [d for d in os.listdir('blogs') if os.path.isdir(os.path.join('blogs', d))]

for b in blog_dirs:
    idx_path = os.path.join('blogs', b, 'index.html')
    if not os.path.exists(idx_path):
        continue
        
    with open(idx_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original_content = content
    
    # Check if a contact us section already exists
    if '/contactus' in content or 'contact us' in content.lower() or 'support@carmaacarcare.com' in content:
        continue
        
    # We need to inject the block
    # Case 1: has blog-main-content
    if '<div class="blog-main-content">' in content:
        # inject before the end of the div or before </article>
        if '</article>' in content:
            content = content.replace('</article>', contact_block + '\n        </article>')
        else:
            # try to find the end of blog-main-content... hard to do with regex
            pass
    # Case 2: has service-left-section
    elif '<div class="service-left-section">' in content:
        # inject at the end of service-left-section
        # find <div class="service-right-section"> and inject before it
        if '<div class="service-right-section">' in content:
            content = content.replace('<div class="service-right-section">', contact_block + '\n        <div class="service-right-section">')
        else:
            # inject before </section>
            if '</section>' in content:
                content = content.replace('</section>', contact_block + '\n    </section>')
                
    if content != original_content:
        with open(idx_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Injected Contact Us in {b}")
