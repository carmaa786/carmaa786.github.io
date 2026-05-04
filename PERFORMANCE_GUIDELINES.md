# Carmaa Car Care - Frontend Performance Guidelines

To maintain the high performance (Core Web Vitals, LCP, CLS) of the Carmaa website, please adhere to the following rules when adding new content, pages, or features.

## 1. Image Loading (Eager vs. Lazy)
Improper image loading is the #1 cause of slow LCP (Largest Contentful Paint).

- **Above-the-Fold Images:** (Hero backgrounds, logos, anything visible immediately when the site loads)
  - MUST use `loading="eager"` (or omit the loading attribute entirely).
  - MUST include `fetchpriority="high"`.
  - *Example:* `<img src="logo.webp" loading="eager" fetchpriority="high" width="200" height="39" />`

- **Below-the-Fold Images:** (Images you have to scroll down to see)
  - MUST use `loading="lazy"`.
  - *Example:* `<img src="before_after.png" loading="lazy" width="800" height="400" />`

- **Image Dimensions:**
  - EVERY image must have explicit `width` and `height` attributes in the HTML to prevent CLS (Cumulative Layout Shift).

## 2. Cache-Busting (Updating CSS/JS)
The server is configured to cache static assets for **1 year** to ensure blazing-fast repeat visits. 

Because of this, if you update the CSS or JS files, returning visitors will not see the changes unless you "bust" the cache.

- **How to update:**
  When you modify `bundle.min.css` or `script.js`, go into `index.html` (and any other HTML files where they are linked) and increment the `?v=` query parameter.
  
  *Old:* `<link rel="stylesheet" href="/bundle.min.css?v=1.0.1">`
  *New:* `<link rel="stylesheet" href="/bundle.min.css?v=1.0.2">`

## 3. Creating New HTML Pages (Preconnects)
When building new pages (e.g., new blog posts, new city landing pages), ensure the network request chains are optimized for Google Fonts.

- **Required `<head>` tags:**
  Always copy the following preconnect links to the `<head>` of new HTML documents, immediately above the Google Fonts stylesheet:
  ```html
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@600&family=Inter:wght@400;600&display=swap" rel="stylesheet">
  ```

## 4. JavaScript Reflow / Scroll Events
Layout thrashing (Forced Synchronous Layouts) tanks frame rates and hurts performance. 

- **The Rule:** NEVER read a DOM layout property (like `.offsetHeight`, `.offsetWidth`, `.getBoundingClientRect()`) inside a `scroll` event.
- **The Solution:** 
  1. Cache the layout value during the `resize` event.
  2. Use the cached variable inside the `scroll` event.
  3. Wrap DOM writes (like `style.transform`) inside a `requestAnimationFrame`.
  
*(See `script.js` parallax implementation for the correct architecture).*
