/**
 * Carmaa Advanced Analytics & Tracking
 * Performance-optimized tracking for GA4, Google Ads, FB Pixel, and Clarity.
 * Inherited by all pages via global script injection.
 */

(function() {
    let trackingInitialized = false;
    const GA_ID = 'G-YV8B16R19L';
    const GADS_ID = 'AW-16789669575';
    const FB_PIXEL_ID = '1106673891043810';
    const CLARITY_ID = 'q8k6r4f6p7'; // Placeholder - Update with actual ID

    // Initialize dataLayer and gtag early for event queuing
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    window.gtag = gtag;

    /**
     * Loads third-party tracking scripts
     */
    const loadScripts = () => {
        if (trackingInitialized) return;
        trackingInitialized = true;

        // --- Google Analytics 4 & Google Ads ---
        const gtm = document.createElement('script');
        gtm.async = true;
        gtm.src = `https://www.googletagmanager.com/gtag/js?id=${GA_ID}`;
        document.head.appendChild(gtm);

        gtag('js', new Date());
        gtag('config', GA_ID, { 'anonymize_ip': true });
        gtag('config', GADS_ID);

        // --- Facebook Pixel ---
        !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?
        n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;
        n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
        t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s);
        }(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');
        fbq('init', FB_PIXEL_ID);
        fbq('track', 'PageView');

        // --- Microsoft Clarity ---
        (function(c,l,a,r,i,t,y){
            c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
            t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
            y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
        })(window, document, "clarity", "script", CLARITY_ID);
    };

    /**
     * Trigger script loading on user interaction
     */
    const initOnInteraction = () => {
        loadScripts();
        ['scroll', 'click', 'touchstart'].forEach(event => {
            window.removeEventListener(event, initOnInteraction);
        });
    };

    // Wait for interaction to load heavy scripts
    ['scroll', 'click', 'touchstart'].forEach(event => {
        window.addEventListener(event, initOnInteraction, { once: true, passive: true });
    });

    // Fallback: Load after 4 seconds if no interaction
    if (document.readyState === 'complete') {
        setTimeout(loadScripts, 4000);
    } else {
        window.addEventListener('load', () => setTimeout(loadScripts, 4000));
    }

    /**
     * Unified Event Tracking Utility
     */
    window.trackAnalyticsEvent = (action, category, label) => {
        // Track to GA4
        if (window.gtag) {
            gtag('event', action, {
                'event_category': category,
                'event_label': label
            });
        }
        // Track to FB Pixel
        if (window.fbq) {
            fbq('trackCustom', action, { category, label });
        }
        // Track to Clarity
        if (window.clarity) {
            clarity("event", action);
        }
    };

    /**
     * Auto-track interactions using event delegation
     */
    document.addEventListener('click', (e) => {
        const target = e.target.closest('a, button');
        if (!target) return;

        const href = target.getAttribute('href') || '';
        const text = (target.innerText || target.getAttribute('aria-label') || '').trim();

        // 1. WhatsApp Clicks
        if (href.includes('wa.me') || href.includes('whatsapp.com')) {
            window.trackAnalyticsEvent('click_whatsapp', 'Engagement', text || 'WhatsApp Link');
        }
        // 2. Phone Call Clicks
        else if (href.startsWith('tel:')) {
            window.trackAnalyticsEvent('click_call', 'Engagement', href);
        }
        // 3. Booking Modal & Buttons
        else if (target.classList.contains('open-booking-modal') || text.toLowerCase().includes('book now')) {
            window.trackAnalyticsEvent('click_booking_btn', 'Conversion', text || 'Book Now');
        }
        // 4. App Store / Play Store Downloads
        else if (href.includes('play.google.com') || href.includes('apps.apple.com')) {
            const platform = href.includes('play.google') ? 'Android' : 'iOS';
            window.trackAnalyticsEvent('click_app_download', 'Conversion', platform);
        }
    }, { passive: true });

    /**
     * Form Submission Tracking
     */
    document.addEventListener('submit', (e) => {
        const form = e.target;
        const formId = form.getAttribute('id') || 'unidentified_form';
        
        // Track general form submission
        window.trackAnalyticsEvent('form_submission', 'Conversion', formId);
        
        // Specific tracking for known forms
        if (formId === 'contactForm') {
            window.trackAnalyticsEvent('lead_inquiry', 'Lead', 'Footer Contact Form');
        } else if (formId === 'bookingForm') {
            window.trackAnalyticsEvent('booking_submission', 'Lead', 'Main Booking Modal');
        }
    });

})();
