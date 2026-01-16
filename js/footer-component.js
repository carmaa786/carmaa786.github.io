// Detect page depth to adjust relative paths
let pathPrefix = '';
const currentPath = window.location.pathname;

if (currentPath.includes('/blogs/')) {
    // Check if we're in a sub-subdirectory (e.g., /blogs/article-name/index.html)
    const afterBlogs = currentPath.split('/blogs/')[1];
    if (afterBlogs && afterBlogs !== 'index.html' && afterBlogs !== '') {
        pathPrefix = '../../';
    } else {
        pathPrefix = '../';
    }
} else if (
    currentPath.includes('/about/') ||
    currentPath.includes('/contactus/') ||
    currentPath.includes('/privacy-policy/') ||
    currentPath.includes('/terms-conditions/')
) {
    pathPrefix = '../';
}

const footerHTML = `
<div class="container">
    <div class="footer-top">
        <!-- Left Column: Logo and Contact Info -->
        <div class="footer-brand">
            <a href="${pathPrefix}index.html" class="footer-logo-link">
                <img src="${pathPrefix}assets/logo.jpg" alt="Carmaa Logo" class="footer-logo-img">
                <span class="footer-logo-text">carmaa</span>
            </a>

            <div class="footer-contact-list">
                <a href="mailto:support@carmaacarcare.com" class="footer-contact-item">
                    <i class="fa-solid fa-envelope"></i>
                    <span>support@carmaacarcare.com</span>
                </a>
                <a href="tel:+917042555401" class="footer-contact-item">
                    <i class="fa-solid fa-phone"></i>
                    <span>+91-70425 55401</span>
                </a>
                <a href="https://wa.me/917042555401" class="footer-contact-item" target="_blank" rel="noopener noreferrer">
                    <i class="fa-brands fa-whatsapp"></i>
                    <span>WhatsApp</span>
                </a>
                <a href="mailto:recruitment@carmaacarcare.com" class="footer-contact-item">
                    <i class="fa-solid fa-users"></i>
                    <span>recruitment@carmaacarcare.com</span>
                </a>
            </div>
        </div>

        <!-- Middle Column: Quick Links -->
        <div class="footer-links-section">
            <h4>Quick Links</h4>
            <div class="footer-links">
                <a href="${pathPrefix}blogs/index.html">Blogs</a>
                <a href="${pathPrefix}about/index.html">About Us</a>
                <a href="https://wa.me/917042555401" target="_blank" rel="noopener noreferrer">Contact Us</a>
            </div>
        </div>

        <!-- Right Column: Social Links and App Buttons -->
        <div class="footer-social-section">
            <h4>Social links</h4>
            <div class="footer-social-icons">
                <a href="https://www.facebook.com/carmaaofficialpage" target="_blank" rel="noopener noreferrer"
                    class="social-icon facebook">
                    <i class="fa-brands fa-facebook-f"></i>
                </a>
                <a href="https://www.instagram.com/carmaa_official/" target="_blank" rel="noopener noreferrer"
                    class="social-icon instagram">
                    <i class="fa-brands fa-instagram"></i>
                </a>
                <a href="https://www.linkedin.com/company/carmaatechnologies/" target="_blank" rel="noopener noreferrer"
                    class="social-icon linkedin">
                    <i class="fa-brands fa-linkedin-in"></i>
                </a>
                <a href="https://www.youtube.com/@carmaa_Official" target="_blank" rel="noopener noreferrer"
                    class="social-icon youtube">
                    <i class="fa-brands fa-youtube"></i>
                </a>
            </div>

            <div class="footer-app-buttons">
                <a href="https://play.google.com/store/apps/details?id=com.carmaacarcare.carmaa" target="_blank"
                    rel="noopener noreferrer" class="app-button">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/7/78/Google_Play_Store_badge_EN.svg"
                        alt="Get it on Google Play">
                </a>
                <a href="https://apps.apple.com/in/app/carmaa-car-care/id6746490090" target="_blank"
                    rel="noopener noreferrer" class="app-button">
                    <img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/Download_on_the_App_Store_Badge.svg"
                        alt="Download on App Store">
                </a>
            </div>
        </div>
    </div>

    <!-- Locations Section (Visually hidden for SEO crawlability) -->
    <div class="footer-locations" style="position: absolute !important; width: 1px !important; height: 1px !important; padding: 0 !important; margin: -1px !important; overflow: hidden !important; clip: rect(0,0,0,0) !important; white-space: nowrap !important; border: 0 !important;">
        <h4>Our Locations & Services</h4>
        <div class="locations-list">
            <!-- Gurgaon Keywords -->
            <a href="https://carmaacarcare.com/blogs/doorstep-car-washing-service-in-gurgaon">Car Wash near me in Gurgaon</a>
            <a href="https://carmaacarcare.com/blogs/doorstep-car-washing-service-in-gurgaon">Car Wash Gurgaon</a>
            <a href="https://carmaacarcare.com/blogs/doorstep-car-washing-service-in-gurgaon">Car Detailing Gurgaon</a>
            <a href="https://carmaacarcare.com/blogs/doorstep-car-washing-service-in-gurgaon">Car Drycleaning Gurgaon</a>
            <a href="https://carmaacarcare.com/blogs/doorstep-car-washing-service-in-gurgaon">Car Doorstep Wash Gurgaon</a>
            
            <!-- Dehradun Keywords -->
            <a href="https://carmaacarcare.com/blogs/doorstep-car-washing-service-in-dehradun">Car Wash near me in Dehradun</a>
            <a href="https://carmaacarcare.com/blogs/doorstep-car-washing-service-in-dehradun">Car Wash Dehradun</a>
            <a href="https://carmaacarcare.com/blogs/doorstep-car-washing-service-in-dehradun">Car Detailing Dehradun</a>
            <a href="https://carmaacarcare.com/blogs/doorstep-car-washing-service-in-dehradun">Car Drycleaning Dehradun</a>
            <a href="https://carmaacarcare.com/blogs/doorstep-car-washing-service-in-dehradun">Car Doorstep Wash Dehradun</a>
        </div>
    </div>

    <!-- Footer Bottom -->
    <div class="footer-bottom-new">
        <p>By continuing past this page, you agree to our <a href="https://carmaacarcare.com/terms-conditions">Terms
                of
                Service</a>,
            Cookie Policy, <a href="https://carmaacarcare.com/privacy-policy">Privacy Policy</a>, and Content
            Policies ©
            2025 Carmaa
            Technologies Pvt Ltd. All Rights Reserved.</p>
    </div>
</div>
`;

function injectFooter() {
    const placeholder = document.getElementById('common-footer');
    if (placeholder) {
        placeholder.innerHTML = footerHTML;
    }
}

// Run injection when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectFooter);
} else {
    injectFooter();
}
