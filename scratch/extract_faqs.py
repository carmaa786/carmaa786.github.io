import os
import re
import json

city = "dehradun"
filepath = f"doorstep-car-washing-service-in-{city}/index.html"
with open(filepath, "r", encoding="utf-8") as f:
    html = f.read()

# Extract FAQs
faqs = []
pattern = re.compile(r'<button[^>]*>\s*<span class="accordion-title">(.*?)</span>.*?<div class="accordion-content">\s*<p>(.*?)</p>\s*</div>', re.DOTALL)
matches = pattern.findall(html)
for q, a in matches:
    # Clean up any inner HTML in the answer if desired, or keep it.
    # The user's FAQ answer contains <strong> tags, which is fine for JSON-LD but better stripped for text-only.
    # Actually, schema.org Answer allows HTML in 'text', so keeping it is okay or we can strip tags.
    # stripping tags for cleaner JSON
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

print(f"Extracted {len(faqs)} FAQs for {city}.")
print(json.dumps(faqs[:2], indent=2))
