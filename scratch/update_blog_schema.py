import os
import re
import json
from datetime import datetime

base_dir = r"c:\Users\jugal\OneDrive\Desktop\carmaa-work"
blogs_dir = os.path.join(base_dir, "blogs")

if not os.path.exists(blogs_dir):
    print("Blogs directory not found")
    exit()

blog_posts = [d for d in os.listdir(blogs_dir) if os.path.isdir(os.path.join(blogs_dir, d))]

for post_dir in blog_posts:
    filepath = os.path.join(blogs_dir, post_dir, "index.html")
    if not os.path.exists(filepath):
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Extract Title
    title_match = re.search(r'<title>(.*?)</title>', html, re.I)
    title = title_match.group(1).split('|')[0].strip() if title_match else post_dir.replace('-', ' ').title()
    
    # Extract Description
    desc_match = re.search(r'<meta name="description" content="(.*?)"', html, re.I)
    description = desc_match.group(1).strip() if desc_match else ""

    # Extract Headline (H1)
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.I | re.DOTALL)
    headline = re.sub(r'<[^>]+>', '', h1_match.group(1)).strip() if h1_match else title

    # Extract Image
    img_match = re.search(r'<section class="service-main-section">.*?<img.*?src="(.*?)"', html, re.I | re.DOTALL)
    image_url = img_match.group(1) if img_match else ""
    if image_url:
        if not image_url.startswith('http'):
            image_url = "https://carmaacarcare.com" + (image_url if image_url.startswith('/') else '/' + image_url)
    else:
        # Fallback to logo if no image found
        image_url = "https://carmaacarcare.com/assets/logo.png"

    # Extract FAQs
    faqs = []
    accordion_pattern = re.compile(r'<div class="accordion-item">.*?<span class="accordion-title">(.*?)</span>.*?<div class="accordion-content">.*?<p>(.*?)</p>', re.DOTALL)
    matches = accordion_pattern.findall(html)
    for q, a in matches:
        clean_q = re.sub(r'<[^>]+>', '', q).strip()
        clean_a = re.sub(r'<[^>]+>', '', a).strip()
        faqs.append({
            "@type": "Question",
            "name": clean_q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": clean_a
            }
        })

    # Date Published - Use file modification time as a proxy
    mtime = os.path.getmtime(filepath)
    date_published = datetime.fromtimestamp(mtime).strftime('%Y-%m-%dT%H:%M:%S+05:30')

    # Build Schema graph
    graph = []

    # BlogPosting
    graph.append({
        "@type": "BlogPosting",
        "@id": f"https://carmaacarcare.com/blogs/{post_dir}/#article",
        "headline": headline,
        "description": description,
        "image": image_url,
        "author": {
            "@type": "Organization",
            "name": "Carmaa Car Care",
            "url": "https://carmaacarcare.com/"
        },
        "publisher": {
            "@type": "Organization",
            "name": "Carmaa Car Care",
            "logo": {
                "@type": "ImageObject",
                "url": "https://carmaacarcare.com/assets/logo.png"
            }
        },
        "datePublished": date_published,
        "dateModified": date_published,
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": f"https://carmaacarcare.com/blogs/{post_dir}/"
        }
    })

    # FAQ schema
    if faqs:
        graph.append({
            "@type": "FAQPage",
            "@id": f"https://carmaacarcare.com/blogs/{post_dir}/#faq",
            "mainEntity": faqs
        })

    # BreadcrumbList
    graph.append({
        "@type": "BreadcrumbList",
        "@id": f"https://carmaacarcare.com/blogs/{post_dir}/#breadcrumb",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": "https://carmaacarcare.com/"
            },
            {
                "@type": "ListItem",
                "position": 2,
                "name": "Blogs",
                "item": "https://carmaacarcare.com/blogs/"
            },
            {
                "@type": "ListItem",
                "position": 3,
                "name": headline,
                "item": f"https://carmaacarcare.com/blogs/{post_dir}/"
            }
        ]
    })

    schema_json = {
        "@context": "https://schema.org",
        "@graph": graph
    }
    schema_str = f"    <script type=\"application/ld+json\">\n{json.dumps(schema_json, indent=2)}\n    </script>"

    # Remove all existing JSON-LD script tags
    html = re.sub(r'<script type="application/ld\+json">.*?</script>', '', html, flags=re.DOTALL)
    
    # Optional cleanup
    html = re.sub(r'\n\s*\n\s*</head>', '\n</head>', html)

    # Insert before </head>
    if '</head>' in html:
        html = html.replace('</head>', f"{schema_str}\n</head>")
    else:
        html += f"\n{schema_str}"

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"Updated {post_dir}")

print("Done")
