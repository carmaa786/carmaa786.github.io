const fs = require('fs');
const path = require('path');

const BASE_DIR = path.join(__dirname, '..');
const TEMPLATE_PATH = path.join(__dirname, 'templates', 'industrial-blog-template.html');

// Example JSON Configuration defining what to generate
const targetPages = [
    {
        slug: "b2b-fleet-car-washing-in-dehradun",
        title: "The Ultimate Guide to B2B Fleet Car Washing Services in Dehradun",
        city: "Dehradun",
        industry: "B2B Fleet",
        keywords: "B2B fleet washing dehradun, commercial car wash, corporate car cleaning, Dehradun car care",
        description: "Discover why local enterprises in Dehradun rely on CarMaa's enterprise doorstep car washing services to maintain their commercial fleets.",
        content_para_1: "Maintaining a commercial fleet in Dehradun is a monumental task. As the central hub of Uttarakhand, businesses rely heavily on seamless transportation. A dirty fleet can negatively impact your brand's professional image.",
        content_para_2: "This is where CarMaa Car Care excels. We offer specialized B2B doorstep fleet car washing designed specifically for corporate clients, taxi companies, and logistics providers. By eliminating the transit time to a washing facility, your vehicles achieve maximum uptime while maintaining a spotless appearance.",
        content_para_3: "When choosing a commercial cleaning partner in Dehradun, reliability and scale are key. Our industrial-grade waterless washing solutions represent the pinnacle of eco-friendly corporate responsibility. CarMaa scales with your business needs.",
        conclusion: "Partnering with CarMaa for your B2B fleet car washing in Dehradun is a strategic advantage. It reduces your overheads, guarantees consistent quality, and ensures your corporate vehicles always reflect the highest standards."
    },
    {
        slug: "hotel-valet-car-cleaning-partnerships-noida",
        title: "Enhancing Guest Experience: Hotel Valet Car Wash Partnerships in Noida",
        city: "Noida",
        industry: "Hotel Valet & Hospitality",
        keywords: "Hotel car wash Noida, hospitality car cleaning, corporate valet wash Noida, guest car wash services",
        description: "Partner with CarMaa in Noida to offer premium doorstep car washing to your hotel guests. A seamless value-add to any luxury hospitality operation.",
        content_para_1: "For premium hotels in Noida, guest experience is the absolute priority. Returning a guest's car spotless is a silent yet incredibly powerful standard of luxury hospitality that guarantees positive reviews.",
        content_para_2: "CarMaa is actively partnering with top-tier hotels across Noida to provide on-site, eco-friendly car cleaning services. Our trained professionals integrate directly with your valet operations.",
        content_para_3: "Implementing an in-house car cleaning system can be expensive and logistically nightmare. Outsourcing this to a specialized provider like CarMaa in Noida ensures zero operational overhead for hotel management, while unlocking a new tier of guest satisfaction.",
        conclusion: "Integrating CarMaa's hotel valet car cleaning services in Noida elevates your brand. Secure a partnership with us and redefine your guest amenities."
    }
];

function generatePages() {
    const templateContent = fs.readFileSync(TEMPLATE_PATH, 'utf8');

    targetPages.forEach(page => {
        // Create directory in /blogs/
        const targetDir = path.join(BASE_DIR, 'blogs', page.slug);
        if (!fs.existsSync(targetDir)) {
            fs.mkdirSync(targetDir, { recursive: true });
        }

        let pageHtml = templateContent;
        // Inject parameters
        Object.keys(page).forEach(key => {
            const regex = new RegExp(`{{${key.toUpperCase()}}}`, 'g');
            pageHtml = pageHtml.replace(regex, page[key]);
        });

        const targetFilePath = path.join(targetDir, 'index.html');
        fs.writeFileSync(targetFilePath, pageHtml);
        console.log(`✅ Generated page: /blogs/${page.slug}`);
    });
}

generatePages();
