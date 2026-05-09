import os

city_dirs = [
    "doorstep-car-washing-service-in-Haridwar",
    "doorstep-car-washing-service-in-Rishikesh",
    "doorstep-car-washing-service-in-aligarh",
    "doorstep-car-washing-service-in-chandigarh",
    "doorstep-car-washing-service-in-dehradun",
    "doorstep-car-washing-service-in-delhi",
    "doorstep-car-washing-service-in-faridabad",
    "doorstep-car-washing-service-in-gaziabad",
    "doorstep-car-washing-service-in-gurgaon",
    "doorstep-car-washing-service-in-haldwani",
    "doorstep-car-washing-service-in-mussoorie",
    "doorstep-car-washing-service-in-noida",
    "doorstep-car-washing-service-in-roorkee"
]

style_block = """
    <!-- DEFINTIVE MOBILE VISIBILITY FIX -->
    <style>
        @media screen and (max-width: 768px) {
            section:not(.city-header-section), 
            .our-service-main-section, 
            .city-benefits-section, 
            .commitment-quality, 
            .benefits-section,
            .city-why-choose,
            .why-choose-grid {
                background-color: #f9fbfd !important;
                background-image: none !important;
            }
            section:not(.city-header-section) p, 
            section:not(.city-header-section) li, 
            section:not(.city-header-section) span,
            section:not(.city-header-section) div:not(.social-media-icons),
            .city-why-choose p,
            .right-desc,
            .desc {
                color: #444 !important;
                visibility: visible !important;
                opacity: 1 !important;
            }
            section:not(.city-header-section) h2, 
            section:not(.city-header-section) h3, 
            section:not(.city-header-section) h1,
            section:not(.city-header-section) h4,
            section:not(.city-header-section) strong,
            .city-why-choose h2,
            .city-why-choose-heading {
                color: #1b4e9b !important;
                visibility: visible !important;
                opacity: 1 !important;
            }
            /* Force images to full width */
            .our-services-section-city-left, .why-choose-right, .img-wrapper {
                width: 100% !important;
                padding: 0 !important;
                margin: 0 !important;
            }
            .our-services-section-city-left img, .why-choose-right img, .img-wrapper img {
                width: 100% !important;
                border-radius: 0 !important;
            }
        }
    </style>
</head>"""

for city in city_dirs:
    path = os.path.join(city, "index.html")
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if "DEFINTIVE MOBILE VISIBILITY FIX" not in content:
            content = content.replace("</head>", style_block)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {path}")
        else:
            print(f"Skipping {path} (already updated)")
    else:
        print(f"File not found: {path}")
