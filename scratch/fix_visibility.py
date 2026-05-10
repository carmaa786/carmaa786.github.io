import os

file_path = r'c:\Users\jugal\OneDrive\Desktop\carmaa-work\css\city.css'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the missing brace after line 1957
# We search for the block and append the brace
pattern = 'max-width: 500px;\n        margin: 0 auto;\n        display: block;\n    }'
replacement = pattern + '\n}'

if pattern in content:
    content = content.replace(pattern, replacement)
    print("Found pattern and replaced.")
else:
    # Try with CRLF
    pattern = pattern.replace('\n', '\r\n')
    replacement = replacement.replace('\n', '\r\n')
    if pattern in content:
        content = content.replace(pattern, replacement)
        print("Found pattern (CRLF) and replaced.")
    else:
        print("Pattern not found.")

# Also append a final catch-all visibility fix
final_fix = """
/* FINAL DEFINITIVE VISIBILITY FIX */
@media screen and (max-width: 768px) {
    section:not(.city-header-section) p, 
    section:not(.city-header-section) li, 
    section:not(.city-header-section) span {
        color: #444 !important;
        visibility: visible !important;
        opacity: 1 !important;
    }
    section:not(.city-header-section) h2, 
    section:not(.city-header-section) h3, 
    section:not(.city-header-section) h1 {
        color: #1b4e9b !important;
        visibility: visible !important;
        opacity: 1 !important;
    }
    .our-service-main-section, .city-benefits-section, .commitment-quality, .benefits-section {
        background-color: #f9fbfd !important;
    }
}
"""
if "FINAL DEFINITIVE VISIBILITY FIX" not in content:
    content += final_fix

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("File updated.")
