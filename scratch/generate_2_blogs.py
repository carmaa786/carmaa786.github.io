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
    
    os.makedirs(f'blogs/{url_slug}', exist_ok=True)
    with open(f'blogs/{url_slug}/index.html', 'w', encoding='utf-8') as f_out:
        f_out.write(str(soup))
        
# Blog 1
content_1 = '''
            <p class="service-para">Car ceramic coatings have taken the automotive world by storm, promising unmatched gloss and long-lasting protection. But what exactly is a ceramic coating, and is it really worth the investment?</p>
            
            <p class="service-para">At Carmaa Car Care, we receive countless questions about ceramic coatings. This comprehensive guide will walk you through everything you need to know about this revolutionary paint protection technology.</p>

            <h2 class="service-heading">What is a Ceramic Coating?</h2>
            <p class="service-para">A ceramic coating is a liquid polymer applied by hand to the exterior of a vehicle. It chemically bonds with the vehicle's factory paint, creating a semi-permanent layer of protection. Unlike traditional wax or sealants, which wash away over time, a high-quality ceramic coating can last for years.</p>

            <h2 class="service-heading">The Core Benefits</h2>
            <p class="service-para">Why do car enthusiasts swear by ceramic coatings? Here are the primary reasons:</p>
            <ul style="margin-left: 20px; margin-bottom: 20px;">
                <li class="service-para"><strong>Hydrophobic Properties:</strong> Water beads up and rolls off the surface instantly, taking dirt and grime with it.</li>
                <li class="service-para"><strong>UV Protection:</strong> It blocks harmful UV rays, preventing your paint from oxidizing and fading under the harsh Indian sun.</li>
                <li class="service-para"><strong>Chemical Resistance:</strong> It protects your clear coat from acidic bird droppings, tree sap, and harsh detergents.</li>
                <li class="service-para"><strong>Enhanced Gloss:</strong> It adds depth and a "wet look" to your paint that traditional waxes simply cannot match.</li>
            </ul>
            
            <h2 class="service-heading">What a Ceramic Coating Won't Do</h2>
            <p class="service-para">It's important to set realistic expectations. A ceramic coating is not a magical force field. It will not make your car scratch-proof, it will not stop rock chips, and it will not eliminate the need to wash your car altogether.</p>

            <h2 class="service-heading">Is It Worth It?</h2>
            <p class="service-para">If you want your car to look newer for longer, if you hate waxing every few months, and if you want washing your car to be a breeze, then a ceramic coating is absolutely worth the investment. It preserves the resale value of your vehicle while giving you that pristine showroom shine every single day.</p>
            <p class="service-para">Ready to upgrade your paint protection? Contact Carmaa Car Care today to learn more about our premium ceramic coating services!</p>
'''
create_blog(
    'ultimate-guide-car-ceramic-coating-worth-it',
    'The Ultimate Guide to Car Ceramic Coating: Is It Worth It? | Carmaa Car Care',
    'ceramic coating, car paint protection, auto detailing, hydrophobic coating, is ceramic coating worth it',
    'Discover what a ceramic coating really is, its core benefits, and whether it is worth the investment for protecting your cars paint.',
    '/assets/blogs/ceramic-coating-benefits.png',
    'Ceramic Coating Guide',
    'The Ultimate Guide to Car Ceramic Coating: Is It Worth It?',
    content_1
)

# Blog 2
content_2 = '''
            <p class="service-para">India's intense summer sun can be brutal, and it doesn't just make your steering wheel too hot to touch—it actively degrades your car's exterior. Over time, UV exposure can lead to severe paint oxidation, fading, and peeling.</p>
            
            <p class="service-para">At Carmaa Car Care, we specialize in rescuing sun-damaged vehicles. But the best cure is always prevention. Here is how you can protect your car's paint from the ravages of the sun.</p>

            <h2 class="service-heading">How Sun Damage Works</h2>
            <p class="service-para">Ultraviolet (UV) rays from the sun break down the molecular bonds in your car's clear coat. Once the clear coat is compromised, the base color layer begins to oxidize. This is what causes that chalky, faded look, particularly on the roof, hood, and trunk.</p>

            <h2 class="service-heading">Top 4 Ways to Protect Your Paint</h2>
            <p class="service-para">Follow these essential steps to keep your car looking vibrant:</p>
            <ul style="margin-left: 20px; margin-bottom: 20px;">
                <li class="service-para"><strong>1. Park in the Shade:</strong> It sounds obvious, but it is the most effective defense. If you don't have a garage, look for shaded parking spots or use a high-quality, UV-resistant car cover.</li>
                <li class="service-para"><strong>2. Wash Regularly:</strong> Dirt, bird droppings, and tree sap become baked into your paint under the hot sun. Regular washing (at least once every two weeks) prevents these contaminants from causing permanent damage.</li>
                <li class="service-para"><strong>3. Apply a Protective Layer:</strong> A high-quality synthetic wax, paint sealant, or ceramic coating acts as sunscreen for your car, absorbing UV rays before they reach your clear coat.</li>
                <li class="service-para"><strong>4. Dry Your Car Properly:</strong> Never let water air-dry on your car under the sun. The water droplets act like tiny magnifying glasses, intensifying the UV rays and causing hard water spots.</li>
            </ul>
            
            <h2 class="service-heading">The Carmaa Advantage</h2>
            <p class="service-para">If you want the ultimate sun protection, our professional doorstep detailing services include the application of premium UV-resistant sealants and coatings. We ensure your paint is fully prepped and protected without you ever having to leave your home.</p>

            <h2 class="service-heading">Don't Wait Until It Fades</h2>
            <p class="service-para">Once your clear coat begins to peel, the only fix is an expensive repaint. Protect your investment today. Book a protective detailing session with Carmaa Car Care and keep your car shining bright all year round!</p>
'''
create_blog(
    'how-to-protect-car-paint-from-sun-damage',
    'How to Protect Your Car Paint From Sun Damage and Fading | Carmaa Car Care',
    'sun damage car paint, protect car paint from sun, uv protection car, car detailing, prevent clear coat peeling',
    'Learn how UV rays degrade your cars clear coat and discover the top 4 ways to protect your paint from sun damage and fading.',
    '/assets/blogs/car_paint_pollution.png',
    'Sun Damage Protection',
    'How to Protect Your Car Paint From Sun Damage and Fading',
    content_2
)
print('New blogs generated successfully!')
