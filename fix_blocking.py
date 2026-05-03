import sys

file_path = r'c:\Users\jugal\OneDrive\Desktop\carmaa-work\index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace font-display part
target_font = "            --font-display: 'Oswald', sans-serif;\n        }"
replacement_font = target_font + "\n        @font-face { font-family: 'Metropolis'; font-display: swap; }\n        @font-face { font-family: 'Oswald'; font-display: swap; }"
content = content.replace(target_font, replacement_font)

# Replace tracking scripts part
target_scripts = """    <script src="script.js"></script>
    <!-- Tracking Scripts Moved to Footer for Performance -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-YMHL3KW21H"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag() { dataLayer.push(arguments); }
        gtag('js', new Date());
        gtag('config', 'AW-16789669575');
        gtag('config', 'G-YMHL3KW21H');
    </script>
    <script>
        !function (f, b, e, v, n, t, s) {
            if (f.fbq) return; n = f.fbq = function () {
                n.callMethod ?
                    n.callMethod.apply(n, arguments) : n.queue.push(arguments)
            };
            if (!f._fbq) f._fbq = n; n.push = n; n.loaded = !0; n.version = '2.0';
            n.queue = []; t = b.createElement(e); t.async = !0;
            t.src = v; s = b.getElementsByTagName(e)[0];
            if (s.parentNode) s.parentNode.insertBefore(t, s);
            else b.head.appendChild(t);
        }(window, document, 'script',
            'https://connect.facebook.net/en_US/fbevents.js');
        fbq('init', '1106673891043810');
        fbq('track', 'PageView');
    </script>
    <noscript><img height="1" width="1" style="display:none"
            src="https://www.facebook.com/tr?id=1106673891043810&ev=PageView&noscript=1" /></noscript>"""

replacement_scripts = """    <script src="script.js"></script>
    <script>
        window.addEventListener('load', () => {
            setTimeout(() => {
                const gtm = document.createElement('script');
                gtm.async = true; gtm.src = 'https://www.googletagmanager.com/gtag/js?id=G-YMHL3KW21H';
                document.body.appendChild(gtm);
                window.dataLayer = window.dataLayer || [];
                function gtag(){dataLayer.push(arguments);}
                gtag('js', new Date()); gtag('config', 'AW-16789669575'); gtag('config', 'G-YMHL3KW21H');

                !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
                n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
                n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
                t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s);
                }(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
                fbq('init', '1106673891043810'); fbq('track', 'PageView');
            }, 3500);
        });
    </script>
    <noscript><img height="1" width="1" style="display:none"
            src="https://www.facebook.com/tr?id=1106673891043810&ev=PageView&noscript=1" /></noscript>"""

content = content.replace(target_scripts, replacement_scripts)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
