import bs4
import os

with open('blogs/is-waterless-truly-scratch-free/index.html', 'r', encoding='utf-8') as f:
    template = f.read()

def create_blog(url_slug, title, keywords, description, image_path, breadcrumb_name, h1_text, html_content):
    soup = bs4.BeautifulSoup(template, 'html.parser')
    
    # Update Meta
    soup.find('link', rel='canonical')['href'] = f'https://carmaacarcare.com/blogs/{url_slug}/'
    soup.title.string = title
    soup.find('meta', attrs={'name': 'keywords'})['content'] = keywords
    soup.find('meta', attrs={'name': 'description'})['content'] = description
    
    # Update Header
    header_section = soup.find('header', class_='city-header-section')
    header_section.find('p').string = h1_text
    
    # Update Breadcrumbs
    breadcrumbs = header_section.find('div', class_='breadcrumb').find_all('p')
    # The last breadcrumb p tag contains the link
    breadcrumbs[-1].find('a').string = breadcrumb_name
    
    # Update Main Article Content
    left_section = soup.find('div', class_='service-left-section')
    
    # Find the main image
    img_tag = left_section.find('img')
    img_tag['src'] = image_path
    img_tag['alt'] = h1_text
    
    new_left_section_html = f'''
        <div class="service-left-section">
            <img style="border-radius:10px; height: auto; aspect-ratio: auto;" alt="{h1_text}" src="{image_path}" loading="lazy" width="1200" height="630" />
            <h1 class="service-heading">{h1_text}</h1>
            {html_content}
        </div>
    '''
    
    new_soup = bs4.BeautifulSoup(new_left_section_html, 'html.parser')
    left_section.replace_with(new_soup.div)
    
    with open(f'blogs/{url_slug}/index.html', 'w', encoding='utf-8') as f_out:
        f_out.write(str(soup))
        
# Blog 1
content_1 = '''
            <p class="service-para">If you live in Dehradun, you know the struggle: you wash your car, it dries, and suddenly you are left with chalky, white circles all over your beautiful paint. These are hard water stains, and they are much more than just a cosmetic annoyance.</p>
            
            <p class="service-para">At Carmaa Car Care, we have seen countless vehicles come into our hands with paint severely degraded by unchecked hard water. But why does this happen, and what can you do to stop it?</p>

            <h2 class="service-heading">The Science of a Hard Water Stain</h2>
            <p class="service-para">Dehradun's groundwater is notoriously rich in minerals like calcium and magnesium. When you wash your car with this water and let it air dry (or wash it under the hot sun), the water evaporates, leaving those heavy mineral deposits behind.</p>
            <p class="service-para">Here is where the real danger begins: these mineral deposits are highly alkaline. If left on the clear coat, they bake in the sun and physically <strong>etch</strong> into your paint. What starts as a simple surface stain quickly becomes a permanent crater in your clear coat.</p>

            <h2 class="service-heading">Why Traditional Washing Makes It Worse</h2>
            <p class="service-para">Trying to remove these etched stains with traditional soap and hard scrubbing is a recipe for disaster. The calcium deposits act like sandpaper. When you rub them aggressively, you create swirl marks and deep micro-scratches. Even worse, adding more hard water during the wash cycle only compounds the problem.</p>
            
            <h2 class="service-heading">The Carmaa Solution: Safe Descaling</h2>
            <p class="service-para">Removing hard water stains requires chemical precision, not brute force. Here is how our professional detailing experts handle it safely:</p>
            <ul style="margin-left: 20px; margin-bottom: 20px;">
                <li class="service-para"><strong>Acid-Based Descaling:</strong> We use mild, pH-balanced acidic mineral removers that safely break down the calcium bonds without harming your clear coat.</li>
                <li class="service-para"><strong>RO Water Formulation:</strong> Our premium washing products are formulated with purified water to ensure absolutely zero new minerals are introduced to the surface.</li>
                <li class="service-para"><strong>Protective Coating:</strong> Once the paint is purified, we strongly recommend a ceramic coating or synthetic sealant. This creates a hydrophobic barrier, meaning future water droplets slide off instead of drying and etching.</li>
            </ul>

            <h2 class="service-heading">Protect Your Pride and Joy</h2>
            <p class="service-para">Do not let the local water supply ruin your vehicle's showroom shine. If you are spotting those dreaded white rings, it is time to call in the professionals before the etching becomes permanent.</p>
            <p class="service-para">Book a doorstep detailing service with Carmaa today, and let us restore and protect your paint from Dehradun's hardest elements.</p>
'''
create_blog(
    'hard-water-stains-on-car-paint',
    'Hard Water Stains on Car Paint: Prevention and Removal | Carmaa Car Care',
    'hard water stains on car, remove water spots car, car paint etching, car wash dehradun, ceramic coating',
    'Discover why hard water stains are destroying your cars paint in Dehradun and learn how Carmaa Car Care safely removes calcium deposits to restore your shine.',
    '/assets/blogs/interior_cleaning_hard_water.png',
    'Hard Water Stains',
    'Hard Water Stains on Car Paint: Prevention and Removal in Dehradun',
    content_1
)

# Blog 2
content_2 = '''
            <p class="service-para">We have all been there: your car is dirty, you are short on time, and that local roadside car wash is offering a quick clean for a few hundred rupees. It seems like a harmless, convenient bargain. But what is it really costing you in the long run?</p>
            
            <p class="service-para">At Carmaa Car Care, we often inherit vehicles that have been subjected to months or years of cheap roadside washes. The truth is, that "bargain" wash is slowly destroying your vehicle's primary defense system: its clear coat.</p>

            <h2 class="service-heading">The Dirty Rag Reality</h2>
            <p class="service-para">The biggest culprit at unverified wash stations is cross-contamination. That single cloth being used to wipe down your hood? It was likely just used to clean the brake dust off the wheels of the car before yours.</p>
            <p class="service-para">Brake dust contains sharp metallic particles. When trapped in a cheap cotton rag and dragged across your car's delicate clear coat, it acts like sandpaper. This is the primary cause of those awful "spiderweb" swirl marks you see when the sun hits your paint.</p>

            <h2 class="service-heading">Harsh Detergents and Acidic Cleaners</h2>
            <p class="service-para">To clean cars quickly and cheaply, many roadside operations use industrial-grade detergents or even dish soap. These chemicals are highly alkaline and extremely harsh.</p>
            <ul style="margin-left: 20px; margin-bottom: 20px;">
                <li class="service-para"><strong>Stripped Protection:</strong> Dish soap instantly strips away any protective wax or sealants you had on your paint.</li>
                <li class="service-para"><strong>Fading Plastics:</strong> Harsh chemicals permanently dry out and fade your black plastic trims and rubber weather seals.</li>
                <li class="service-para"><strong>Oxidation:</strong> Left entirely unprotected, your clear coat begins to oxidize, leading to premature fading and peeling.</li>
            </ul>

            <h2 class="service-heading">The Hard Water Factor</h2>
            <p class="service-para">As discussed in our other guides, using unpurified borewell water leaves behind heavy mineral deposits. When roadside washers let your car bake dry in the sun, those minerals etch permanently into your paint, requiring expensive paint correction to remove.</p>

            <h2 class="service-heading">The Professional Alternative</h2>
            <p class="service-para">When you hire a professional doorstep detailing service like Carmaa, you are not just paying for a wash; you are investing in paint preservation. We use color-coded, premium 800 GSM microfiber towels to guarantee zero cross-contamination. Our lubricants are pH-balanced and formulated to encapsulate dirt, lifting it safely away from your paint.</p>
            
            <h2 class="service-heading">Protect Your Investment</h2>
            <p class="service-para">Your vehicle is one of your most expensive assets. Do not trust its care to dirty rags and dish soap. Switch to a professional, science-backed care routine and keep your car looking like it just rolled off the showroom floor.</p>
            <p class="service-para">Experience the Carmaa difference today. Book your safe, premium doorstep car wash now.</p>
'''
create_blog(
    'hidden-dangers-roadside-car-washes',
    'The Hidden Dangers of Roadside Car Washes | Carmaa Car Care',
    'roadside car wash dangers, car wash swirl marks, dish soap on car, carmaa car care, premium car wash',
    'Are cheap roadside car washes destroying your vehicles paint? Learn the hidden dangers of dirty rags, harsh chemicals, and why professional detailing is essential.',
    '/assets/blogs/diy_vs_pro_wash.png',
    'Roadside Wash Dangers',
    'The Hidden Dangers of Roadside Car Washes: Protect Your Investment',
    content_2
)
print('Blogs generated successfully!')
