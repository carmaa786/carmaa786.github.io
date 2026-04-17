const fs = require('fs');
const path = require('path');

// Configuration
const BASE_DIR = path.join(__dirname, '..');
const SITEMAP_OUTPUT_FILE = path.join(BASE_DIR, 'sitemap.html');
const BASE_URL = 'https://carmaacarcare.com';

// Excluded directories completely unrelated to SEO pages
const EXCLUDED_DIRS = ['.git', '.github', 'scripts', 'css', 'js', 'images', 'assets', 'common', 'components', 'node_modules'];

/**
 * Extract title from HTML content
 */
function extractTitle(htmlContent) {
    const titleMatch = htmlContent.match(/<title>(.*?)<\/title>/i);
    return titleMatch ? titleMatch[1] : null;
}

/**
 * Traverse directories recursively
 */
function walkDir(dir) {
    let results = [];
    const _walk = (currentPath) => {
        const files = fs.readdirSync(currentPath);
        for (const file of files) {
            const filePath = path.join(currentPath, file);
            const relativePath = path.relative(BASE_DIR, filePath).replace(/\\/g, '/');
            const rootDir = relativePath.split('/')[0];
            
            // Skip excluded directories
            if (EXCLUDED_DIRS.includes(rootDir) || file === '.DS_Store') continue;
            
            const stat = fs.statSync(filePath);
            
            if (stat && stat.isDirectory()) {
                _walk(filePath);
            } else if (file === 'index.html' || file.endsWith('.html')) {
                // Ignore components or templates
                if (relativePath.includes('components/')) continue;
                
                results.push(filePath);
            }
        }
    };
    
    _walk(dir);
    return results;
}

/**
 * Main execution
 */
function generateSitemap() {
    console.log('Scanning directories for HTML files...');
    const htmlFiles = walkDir(BASE_DIR);
    console.log(`Found ${htmlFiles.length} HTML files.`);
    
    const pageData = [];
    
    htmlFiles.forEach((file) => {
        const relativePath = path.relative(BASE_DIR, file).replace(/\\/g, '/');
        
        // Don't index the sitemap itself or old index files
        if (relativePath === 'sitemap.html' || relativePath === 'index_old.html') return;
        
        const content = fs.readFileSync(file, 'utf8');
        const title = extractTitle(content) || relativePath;
        
        // Convert 'index.html' to just '/' or 'directory/'
        let linkUrl = relativePath;
        if (relativePath === 'index.html') {
            linkUrl = '/';
        } else if (relativePath.endsWith('/index.html')) {
            linkUrl = '/' + relativePath.replace('/index.html', '/');
        } else {
            linkUrl = '/' + relativePath;
        }
        
        pageData.push({ title, url: linkUrl, rawRelativePath: relativePath });
    });
    
    // Sort pages
    const mainPages = pageData.filter(p => !p.rawRelativePath.includes('/'));
    const blogPages = pageData.filter(p => p.rawRelativePath.startsWith('blogs/'));
    const servicePages = pageData.filter(p => p.rawRelativePath.startsWith('doorstep-') || p.rawRelativePath.includes('-service'));
    const otherPages = pageData.filter(p => !mainPages.includes(p) && !blogPages.includes(p) && !servicePages.includes(p));

    console.log(`Categorized: ${mainPages.length} main, ${blogPages.length} blogs, ${servicePages.length} locations/services, ${otherPages.length} others.`);

    // Generate HTML string
const htmlString = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sitemap - CarMaa Car Care</title>
    <meta name="description" content="HTML Sitemap for CarMaa Car Care. Explore our doorstep car washing services, locations, blogs, and other pages.">
    <link rel="stylesheet" href="/css/common.css"/>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Inter', sans-serif; background: #fff; color: #333; margin: 0; padding: 0; }
        .sitemap-container { max-width: 1200px; margin: 40px auto; padding: 20px; }
        .sitemap-header { text-align: center; margin-bottom: 40px; }
        .sitemap-header h1 { font-size: 2.5rem; color: #1a1a1a; margin-bottom: 10px; }
        .sitemap-header p { font-size: 1.1rem; color: #666; }
        .sitemap-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; }
        .sitemap-section { background: #f9f9f9; border-radius: 8px; padding: 25px; border-top: 4px solid #65c7d0; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
        .sitemap-section h2 { font-size: 1.5rem; color: #333; margin-top: 0; margin-bottom: 20px; border-bottom: 1px solid #ddd; padding-bottom: 10px; }
        .sitemap-list { list-style: none; padding: 0; margin: 0; }
        .sitemap-list li { margin-bottom: 12px; }
        .sitemap-list a { color: #0056b3; text-decoration: none; font-size: 1.05rem; transition: color 0.2s; }
        .sitemap-list a:hover { color: #65c7d0; text-decoration: underline; }
    </style>
</head>
<body>
    <div id="navbar-placeholder"></div>
    <div class="sitemap-container">
        <div class="sitemap-header">
            <h1>Site Map</h1>
            <p>Navigate through all the pages, services, and locations offered by CarMaa Car Care.</p>
        </div>
        
        <div class="sitemap-grid">
            <div class="sitemap-section">
                <h2>Main Pages</h2>
                <ul class="sitemap-list">
                    ${mainPages.map(p => "<li><a href='" + BASE_URL + p.url + "'>" + p.title + "</a></li>").join("\\n                    ")}
                </ul>
            </div>
            
            <div class=\"sitemap-section\">
                <h2>Locations & Services</h2>
                <ul class="sitemap-list">
                    ${servicePages.map(p => "<li><a href='" + BASE_URL + p.url + "'>" + p.title + "</a></li>").join("\\n                    ")}
                </ul>
            </div>
            
            <div class=\"sitemap-section\">
                <h2>Our Blogs</h2>
                <ul class="sitemap-list">
                    ${blogPages.map(p => "<li><a href='" + BASE_URL + p.url + "'>" + p.title + "</a></li>").join("\\n                    ")}
                </ul>
            </div>
            
            <div class=\"sitemap-section\">
                <h2>Other Resources</h2>
                <ul class="sitemap-list">
                    ${otherPages.map(p => "<li><a href='" + BASE_URL + p.url + "'>" + p.title + "</a></li>").join("\\n                    ")}
                </ul>
            </div>
        </div>
    </div>
</body>
</html>
`;

    fs.writeFileSync(SITEMAP_OUTPUT_FILE, htmlString.trim());
    console.log("✅ Successfully generated sitemap.html at " + SITEMAP_OUTPUT_FILE);
}

generateSitemap();
