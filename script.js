document.addEventListener('DOMContentLoaded', () => {
    // Smart App Store Detection
    const detectDevice = () => {
        const userAgent = navigator.userAgent || navigator.vendor || window.opera;

        // iOS detection
        if (/iPad|iPhone|iPod/.test(userAgent) && !window.MSStream) {
            return 'ios';
        }

        // Android detection
        if (/android/i.test(userAgent)) {
            return 'android';
        }

        // Default to iOS for desktop/other devices
        return 'ios';
    };

    // App Store URLs
    const APP_STORE_URLS = {
        ios: 'https://apps.apple.com/in/app/carmaa-car-care/id6746490090',
        android: 'https://play.google.com/store/apps/details?id=com.carmaacarcare.carmaa'
    };

    // Update all app download links based on device
    const deviceType = detectDevice();
    const appUrl = APP_STORE_URLS[deviceType];

    // Update all links with class 'app-download-link'
    const appLinks = document.querySelectorAll('.app-download-link');
    appLinks.forEach(link => {
        link.href = appUrl;
    });

    // Handle hero section buttons - show only relevant store button
    const heroButtons = document.querySelectorAll('.cta-group .btn');
    heroButtons.forEach(button => {
        const href = button.getAttribute('href');

        // Hide iOS button for Android users
        if (deviceType === 'android' && href && href.includes('apps.apple.com')) {
            button.style.display = 'none';
        }

        // Hide Android button for iOS users
        if (deviceType === 'ios' && href && href.includes('play.google.com')) {
            button.style.display = 'none';
        }
    });

    // Scroll Reveal Animation
    const revealElements = document.querySelectorAll('.reveal');

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target); // Only animate once
            }
        });
    }, {
        root: null,
        threshold: 0.15, // Trigger when 15% of the element is visible
        rootMargin: "0px"
    });

    revealElements.forEach(el => {
        revealObserver.observe(el);
    });

    // Google Reviews Logic
    const reviews = [
        {
            name: "Rahul Sharma",
            role: "Local Guide · 12 reviews",
            text: "Absolutely game changer! Saved me 3 hours of waiting at a car wash. The finish is showroom quality on my BMW X5. Highly recommend the ceramic coating package.",
            stars: 5,
            date: "2 days ago",
            initial: "R",
            bg: "#E0F2FE",
            color: "#0369A1"
        },
        {
            name: "Priya Patel",
            role: "Local Guide · 8 reviews",
            text: "The app is so easy to use. I booked a quick wash while at the gym and came out to a spotless car! The waterless technology is impressive.",
            stars: 5,
            date: "1 week ago",
            initial: "P",
            bg: "#FDF4FF",
            color: "#A21CAF"
        },
        {
            name: "Amit Verma",
            role: "24 reviews",
            text: "Their premium spa package is worth every rupee. My 5-year old Creta looks brand new again. Professional staff and on-time arrival.",
            stars: 5,
            date: "3 weeks ago",
            initial: "A",
            bg: "#ECFCCB",
            color: "#4D7C0F"
        },
        {
            name: "Sneha Gupta",
            role: "Local Guide · 45 reviews",
            text: "Best detailing service in Noida. I was skeptical about doorstep service quality but they exceeded expectations. The interior deep clean removed all stains.",
            stars: 5,
            date: "1 month ago",
            initial: "S",
            bg: "#FFF7ED",
            color: "#C2410C"
        },
        {
            name: "Vikram Singh",
            role: "Local Guide · 5 reviews",
            text: "Finally a service that understands luxury cars. They handled my Fortuner with care. No scratches, perfect shine. Will be a regular customer.",
            stars: 5,
            date: "1 month ago",
            initial: "V",
            bg: "#F0F9FF",
            color: "#0F766E"
        },
        {
            name: "Anjali Mehta",
            role: "3 reviews",
            text: "Quick, affordable, and eco-friendly. Love the waterless concept as we should all save water. The team was polite and efficient.",
            stars: 4,
            date: "2 months ago",
            initial: "A",
            bg: "#FFF1F2",
            color: "#BE123C"
        },
        {
            name: "Rohan Das",
            role: "18 reviews",
            text: "My Mercedes C-Class shines like new. The ceramic coating is legit. Great value for money compared to 3M or other workshops.",
            stars: 5,
            date: "2 months ago",
            initial: "R",
            bg: "#F5F3FF",
            color: "#6D28D9"
        }
    ];

    const reviewsTrack = document.getElementById('reviewsTrack');
    const reviewsTrackDuplicate = document.getElementById('reviewsTrackDuplicate');

    if (reviewsTrack && reviewsTrackDuplicate) {
        const createReviewCard = (review) => {
            const starHtml = Array(review.stars).fill('<i class="fa-solid fa-star"></i>').join('');

            return `
                <div class="review-card">
                    <div class="review-header">
                        <div class="reviewer-profile">
                            <div class="reviewer-avatar" style="background: ${review.bg}; color: ${review.color}">
                                ${review.initial}
                            </div>
                            <div class="reviewer-info">
                                <h4>${review.name}</h4>
                                <span>${review.role}</span>
                            </div>
                        </div>
                        <i class="fa-brands fa-google google-icon-small colored-google-icon"></i>
                    </div>
                    <div class="review-stars">
                        ${starHtml}
                    </div>
                    <p class="review-text">${review.text}</p>
                    <div class="review-footer">
                        <span>Posted on Google</span>
                        <span>•</span>
                        <span>${review.date}</span>
                    </div>
                </div>
            `;
        };

        const renderReviews = () => {
            const reviewsHtml = reviews.map(createReviewCard).join('');
            reviewsTrack.innerHTML = reviewsHtml;
            reviewsTrackDuplicate.innerHTML = reviewsHtml;
        };

        renderReviews();
    }
});
