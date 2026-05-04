import sys

file_path = r"c:\Users\jugal\OneDrive\Desktop\carmaa-work\styles.css"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

# The corruption starts at line 2124 (index 2123)
# We want to replace everything from line 2124 onwards with the correct CSS

correct_css = """
/* Final Overrides for rendering integrity */
.faq-question {
    padding-right: 60px !important;
}
.commitment-quality-right .img-wrapper .overlay-text img {
    display: none !important;
}
[style*='carmaa-new'], [style*='textture-bg.png'] {
    background-image: none !important;
}

/* Hover Color Removal Overrides */
.faq-item:hover, 
.step-card:hover, 
.testimonial-card:hover, 
.promises-grid .promise-card:hover {
    border-color: var(--border-light) !important;
}

.stat-item:hover .stat-icon {
    background: #F0FDFA !important;
    color: var(--secondary) !important;
    box-shadow: none !important;
}

.services .service-card:hover .icon-box {
    background: linear-gradient(135deg, rgba(27, 78, 155, 0.08) 0%, rgba(40, 176, 151, 0.08) 100%) !important;
    border-color: rgba(27, 78, 155, 0.12) !important;
}
"""

new_lines = lines[:2123] + [correct_css]

with open(file_path, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Successfully fixed styles.css")
