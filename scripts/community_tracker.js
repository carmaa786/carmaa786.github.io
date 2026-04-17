const fs = require('fs');
const path = require('path');

const OUTPUT_FILE = path.join(__dirname, '..', 'opportunities.md');

const SUBREDDITS = ['Dehradun', 'Delhi', 'Noida', 'Gurgaon', 'CarsIndia'];
const QUERIES = [
    'car wash',
    'car cleaning',
    'ceramic coating',
    'car polish'
];

async function fetchRedditOpportunities() {
    let opportunities = [];
    
    console.log('Fetching Reddit discussions...');
    for (const sub of SUBREDDITS) {
        for (const query of QUERIES) {
            try {
                const url = "https://www.reddit.com/r/" + sub + "/search.json?q=" + encodeURIComponent(query) + "&restrict_sr=1&sort=new";
                const response = await fetch(url, {
                    headers: { 'User-Agent': 'CarMaa-SEO-Tracker/1.0' }
                });
                
                if (response.ok) {
                    const data = await response.json();
                    const posts = data.data.children.slice(0, 3); // Get top 3 recent
                    
                    posts.forEach(post => {
                        opportunities.push({
                            platform: 'Reddit',
                            community: "r/" + sub,
                            title: post.data.title,
                            url: "https://reddit.com" + post.data.permalink,
                            score: post.data.score,
                            num_comments: post.data.num_comments
                        });
                    });
                } else {
                    console.log("Rate limited or error fetching r/" + sub + " for " + query);
                }
            } catch (err) {
                console.error("Failed to fetch r/" + sub + ": " + err.message);
            }
        }
    }
    
    return opportunities;
}

async function runTracker() {
    const opps = await fetchRedditOpportunities();
    
    let mdContent = '# 🚀 Community SEO Engagement Opportunities\\n\\n';
    mdContent += '> **Note:** Quora scraping requires Puppeteer/Selenium due to anti-bot protection. This report focuses on live Reddit threads.\\n\\n';
    
    if (opps.length === 0) {
        mdContent += '*No new opportunities found or rate-limited. Try again later.*\\n';
    } else {
        mdContent += '| Platform | Community | Thread Title | Engagement | Link |\\n';
        mdContent += '|----------|-----------|--------------|------------|------|\\n';
        
        opps.forEach(o => {
            mdContent += "| " + o.platform + " | " + o.community + " | " + o.title.replace(/\\|/g, '-') + " | " + o.score + " votes / " + o.num_comments + " replies | [View Thread](" + o.url + ") |\\n";
        });
    }
    
    fs.writeFileSync(OUTPUT_FILE, mdContent, 'utf8');
    console.log("✅ Generated community opportunities log at " + OUTPUT_FILE);
}

runTracker();
