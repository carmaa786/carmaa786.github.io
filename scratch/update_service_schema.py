import os
import re
import json

base_dir = r"c:\Users\jugal\OneDrive\Desktop\carmaa-work"

service_dirs = [
    "car-body-polish-and-car-waxing-service",
    "car-deep-cleaning-services",
    "car-detailing-services",
    "car-dry-cleaning-service",
    "exterior-car-cleaning-washing",
    "full-car-detailing-service",
    "full-car-wash-service",
    "glass-and-surface-coating-services",
    "interior-car-cleaning-service",
    "paint-protection-and-coating-services"
]

for service_dir in service_dirs:
    filepath = os.path.join(base_dir, service_dir, "index.html")
    if not os.path.exists(filepath):
        print(f"Skipping {service_dir}, file not found")
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Extract FAQs
    faqs = []
    
    # Method 1: Extract from existing JSON-LD
    existing_json_matches = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
    for json_str in existing_json_matches:
        try:
            data = json.loads(json_str)
            if isinstance(data, dict):
                if data.get("@type") == "FAQPage":
                    faqs.extend(data.get("mainEntity", []))
                elif data.get("@context") == "https://schema.org" and "@graph" in data:
                    for item in data["@graph"]:
                        if item.get("@type") == "FAQPage":
                            faqs.extend(item.get("mainEntity", []))
        except:
            pass

    # Method 2: Extract from HTML accordion
    accordion_pattern = re.compile(r'<div class="accordion-item">.*?<span class="accordion-title">(.*?)</span>.*?<div class="accordion-content">.*?<p>(.*?)</p>', re.DOTALL)
    matches = accordion_pattern.findall(html)
    for q, a in matches:
        clean_q = re.sub(r'<[^>]+>', '', q).strip()
        clean_a = re.sub(r'<[^>]+>', '', a).strip()
        # Avoid duplicates
        if not any(f.get("name") == clean_q for f in faqs):
            faqs.append({
                "@type": "Question",
                "name": clean_q,
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": clean_a
                }
            })

    # Extract Service Info
    title_match = re.search(r'<title>(.*?)</title>', html, re.I)
    title = title_match.group(1).split('|')[0].strip() if title_match else f"Carmaa {service_dir.replace('-', ' ').title()}"
    
    desc_match = re.search(r'<meta name="description" content="(.*?)"', html, re.I)
    description = desc_match.group(1).strip() if desc_match else ""

    # Build Schema graph
    graph = []

    # Service
    graph.append({
        "@type": "Service",
        "@id": f"https://carmaacarcare.com/{service_dir}/#service",
        "name": title,
        "description": description,
        "provider": {
            "@type": "LocalBusiness",
            "name": "Carmaa Car Care",
            "url": "https://carmaacarcare.com/",
            "image": "https://carmaacarcare.com/assets/logo.png",
            "telephone": "+91-7042555401",
            "priceRange": "₹₹",
            "address": {
                "@type": "PostalAddress",
                "addressLocality": "Dehradun",
                "addressRegion": "Uttarakhand",
                "addressCountry": "IN"
            }
        },
        "areaServed": [
            {"@type": "City", "name": "Dehradun"},
            {"@type": "City", "name": "Noida"},
            {"@type": "City", "name": "Gurgaon"},
            {"@type": "City", "name": "Delhi"},
            {"@type": "City", "name": "Faridabad"},
            {"@type": "City", "name": "Ghaziabad"}
        ]
    })

    # FAQ schema
    if faqs:
        graph.append({
            "@type": "FAQPage",
            "@id": f"https://carmaacarcare.com/{service_dir}/#faq",
            "mainEntity": faqs
        })

    # BreadcrumbList
    graph.append({
        "@type": "BreadcrumbList",
        "@id": f"https://carmaacarcare.com/{service_dir}/#breadcrumb",
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
                "name": title,
                "item": f"https://carmaacarcare.com/{service_dir}/"
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
    
    # Optional cleanup of empty lines left behind
    html = re.sub(r'\n\s*\n\s*</head>', '\n</head>', html)

    # Insert before </head>
    html = html.replace('</head>', f"{schema_str}\n</head>")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"Updated {service_dir}")

print("Done")
