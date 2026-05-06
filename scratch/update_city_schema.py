import os
import re
import json

base_dir = r"c:\Users\jugal\OneDrive\Desktop\carmaa-work"

cities = {
    "dehradun": {
        "name": "Dehradun",
        "latitude": "30.3165",
        "longitude": "78.0322"
    },
    "noida": {
        "name": "Noida",
        "latitude": "28.5355",
        "longitude": "77.3910"
    },
    "gurgaon": {
        "name": "Gurgaon",
        "latitude": "28.4595",
        "longitude": "77.0266"
    },
    "delhi": {
        "name": "Delhi",
        "latitude": "28.6139",
        "longitude": "77.2090"
    },
    "faridabad": {
        "name": "Faridabad",
        "latitude": "28.4089",
        "longitude": "77.3178"
    },
    "gaziabad": {
        "name": "Ghaziabad",
        "latitude": "28.6692",
        "longitude": "77.4538"
    }
}

for city_key, city_data in cities.items():
    city_name = city_data["name"]
    filepath = os.path.join(base_dir, f"doorstep-car-washing-service-in-{city_key}", "index.html")
    if not os.path.exists(filepath):
        print(f"Skipping {city_key}, file not found")
        continue

    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Extract FAQs
    faqs = []
    pattern = re.compile(r'<button[^>]*>\s*<span class="accordion-title">(.*?)</span>.*?<div class="accordion-content">\s*<p>(.*?)</p>\s*</div>', re.DOTALL)
    matches = pattern.findall(html)
    for q, a in matches:
        clean_a = re.sub(r'<[^>]+>', '', a).strip()
        clean_q = re.sub(r'<[^>]+>', '', q).strip()
        faqs.append({
            "@type": "Question",
            "name": clean_q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": clean_a
            }
        })

    # Build Schema graph
    graph = []

    # LocalBusiness
    graph.append({
        "@type": "AutomotiveBusiness",
        "@id": f"https://carmaacarcare.com/doorstep-car-washing-service-in-{city_key}/#localbusiness",
        "name": f"Carmaa Car Care {city_name}",
        "url": f"https://carmaacarcare.com/doorstep-car-washing-service-in-{city_key}/",
        "image": "https://carmaacarcare.com/assets/logo.png",
        "description": f"Premium doorstep car wash and waterless detailing service in {city_name}.",
        "telephone": "+91-7042555401",
        "priceRange": "₹₹",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": city_name,
            "addressCountry": "IN"
        },
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": city_data["latitude"],
            "longitude": city_data["longitude"]
        },
        "areaServed": {
            "@type": "City",
            "name": city_name
        },
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": f"Car Care Services in {city_name}",
            "itemListElement": [
                {
                    "@type": "Offer",
                    "itemOffered": {
                        "@type": "Service",
                        "name": f"doorstep car wash in {city_name}"
                    }
                },
                {
                    "@type": "Offer",
                    "itemOffered": {
                        "@type": "Service",
                        "name": f"car detailing in {city_name}"
                    }
                },
                {
                    "@type": "Offer",
                    "itemOffered": {
                        "@type": "Service",
                        "name": f"ceramic coating in {city_name}"
                    }
                },
                {
                    "@type": "Offer",
                    "itemOffered": {
                        "@type": "Service",
                        "name": f"interior cleaning in {city_name}"
                    }
                }
            ]
        }
    })

    # Service schema
    graph.append({
        "@type": "Service",
        "@id": f"https://carmaacarcare.com/doorstep-car-washing-service-in-{city_key}/#service",
        "serviceType": "Car Wash & Detailing",
        "provider": {
            "@id": f"https://carmaacarcare.com/doorstep-car-washing-service-in-{city_key}/#localbusiness"
        },
        "areaServed": {
            "@type": "City",
            "name": city_name
        }
    })

    # FAQ schema
    if faqs:
        graph.append({
            "@type": "FAQPage",
            "@id": f"https://carmaacarcare.com/doorstep-car-washing-service-in-{city_key}/#faq",
            "mainEntity": faqs
        })

    # BreadcrumbList
    graph.append({
        "@type": "BreadcrumbList",
        "@id": f"https://carmaacarcare.com/doorstep-car-washing-service-in-{city_key}/#breadcrumb",
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
                "name": f"Car Wash in {city_name}",
                "item": f"https://carmaacarcare.com/doorstep-car-washing-service-in-{city_key}/"
            }
        ]
    })

    schema_json = {
        "@context": "https://schema.org",
        "@graph": graph
    }
    schema_str = "<script type=\"application/ld+json\">\n" + json.dumps(schema_json, indent=2) + "\n    </script>"

    # Remove all existing JSON-LD
    html = re.sub(r'<script type="application/ld\+json">.*?</script>', '', html, flags=re.DOTALL)
    
    # Optional cleanup of empty lines left behind
    html = re.sub(r'\n\s*\n\s*</head>', '\n</head>', html)

    # Insert new JSON-LD before </head>
    html = html.replace('</head>', f"    {schema_str}\n</head>")

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"Updated {city_key}")

print("Done")
