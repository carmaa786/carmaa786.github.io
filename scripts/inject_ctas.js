const fs = require('fs');
const path = require('path');

const targetPaths = [
    'car-detailing-services/index.html',
    'full-car-wash-service/index.html',
    'glass-and-surface-coating-services/index.html',
    'full-car-detailing-service/index.html',
    'borophene-coating-service/index.html',
    'steam-wash-service/index.html',
    'ceramic-coating-service/index.html',
    'car-dry-cleaning-service/index.html',
    'car-body-polish-and-car-waxing-service/index.html',
    'car-deep-cleaning-services/index.html',
    'paint-protection-and-coating-services/index.html',
    'interior-car-cleaning-service/index.html'
];

const ctaHtml = `
        <!-- Global CTA Banner -->
        <div class="global-cta-banner" style="background: linear-gradient(135deg, #0b1a2b 0%, #1a365d 100%); padding: 35px 25px; border-radius: 12px; text-align: center; margin-top: 45px; margin-bottom: 20px; color: white; box-shadow: 0 10px 30px rgba(0,0,0,0.2);">
            <h3 style="margin-bottom: 15px; font-size: 1.8rem; font-weight: 600; color: #fff;">Book Your Premium Car Care Today!</h3>
            <p style="margin-bottom: 25px; font-size: 1.1rem; opacity: 0.9;">Join thousands of satisfied customers who trust CarMaa for a showroom shine right at their doorstep.</p>
            <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap;">
                <a href="tel:+917042555401" style="background: #d4af37; color: #111; text-decoration: none; padding: 14px 30px; border-radius: 8px; font-weight: 700; display: inline-flex; align-items: center; gap: 8px; font-size: 1.1rem; transition: transform 0.2s;"><i class="fa fa-phone"></i> Call +91 70425 55401</a>
                <a href="#enquiryForm" style="background: transparent; color: white; border: 2px solid white; text-decoration: none; padding: 14px 30px; border-radius: 8px; font-weight: 700; display: inline-flex; align-items: center; gap: 8px; font-size: 1.1rem; transition: background 0.2s;"><i class="fa fa-envelope"></i> Enquire Online</a>
            </div>
        </div>
`;

targetPaths.forEach(relPath => {
    const fullPath = path.join(__dirname, '..', relPath);
    if (!fs.existsSync(fullPath)) {
        console.log("File missing, skipping: " + relPath);
        return;
    }
    
    let content = fs.readFileSync(fullPath, 'utf8');
    
    // Check if it already has a CTA banner
    if (content.includes('global-cta-banner') || content.includes('cta-banner')) {
        console.log("CTA already exists in " + relPath);
        return;
    }

    const replaceTarget = /<\/div>\\s*<div class="service-right-section">/i;
    
    if (content.match(/<\/div>\s*<div class="service-right-section">/i)) {
        content = content.replace(/<\/div>\s*<div class="service-right-section">/i, ctaHtml + '\n    </div>\n    <div class="service-right-section">');
        fs.writeFileSync(fullPath, content);
        console.log("Successfully injected CTA into " + relPath);
    } else {
        console.log("Could not find insertion point in " + relPath);
    }
});
