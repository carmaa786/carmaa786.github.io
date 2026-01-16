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

    // Both buttons are now always visible - removed device-specific hiding
    // const heroButtons = document.querySelectorAll('.cta-group .btn');
    // heroButtons.forEach(button => {
    //     const href = button.getAttribute('href');
    //
    //     // Hide iOS button for Android users
    //     if (deviceType === 'android' && href && href.includes('apps.apple.com')) {
    //         button.style.display = 'none';
    //     }
    //
    //     // Hide Android button for iOS users
    //     if (deviceType === 'ios' && href && href.includes('play.google.com')) {
    //         button.style.display = 'none';
    //     }
    // });


    // Enhanced Scroll Reveal Animation System
    const revealElements = document.querySelectorAll('.reveal');

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                // Keep observing for parallax effects, don't unobserve
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

    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    let lastScroll = 0;

    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;

        // Add scrolled class for styling
        if (currentScroll > 100) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        lastScroll = currentScroll;
    });

    // Parallax effect for hero section
    const hero = document.querySelector('.hero');
    const heroContent = document.querySelector('.hero-content');

    window.addEventListener('scroll', () => {
        const scrolled = window.pageYOffset;
        const parallaxSpeed = 0.5;

        if (hero && scrolled < hero.offsetHeight) {
            if (heroContent) {
                heroContent.style.transform = `translateY(${scrolled * parallaxSpeed}px)`;
                heroContent.style.opacity = 1 - (scrolled / hero.offsetHeight) * 0.8;
            }
        }
    });

    // Footer reveal animation
    const footer = document.querySelector('.footer-new');
    if (footer) {
        const footerObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                }
            });
        }, {
            threshold: 0.1
        });

        footerObserver.observe(footer);
    }

    // Smooth scroll progress indicator (optional subtle effect)
    const createScrollProgress = () => {
        const progressBar = document.createElement('div');
        progressBar.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            height: 3px;
            background: var(--gradient);
            width: 0%;
            z-index: 9999;
            transition: width 0.1s ease;
        `;
        document.body.appendChild(progressBar);

        window.addEventListener('scroll', () => {
            const windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrolled = (window.pageYOffset / windowHeight) * 100;
            progressBar.style.width = scrolled + '%';
        });
    };

    // Uncomment to enable scroll progress bar
    // createScrollProgress();

    // Auto-scroll for Services Carousel on Mobile
    const servicesGrid = document.querySelector('.services-grid');
    let isAutoScrolling = false;
    let autoScrollInterval;

    const startAutoScroll = () => {
        if (window.innerWidth <= 768 && servicesGrid) {
            isAutoScrolling = true;
            let scrollPosition = 0;
            const cardWidth = servicesGrid.querySelector('.service-card')?.offsetWidth || 300;
            const gap = 20;
            const scrollAmount = cardWidth + gap;

            autoScrollInterval = setInterval(() => {
                if (!isAutoScrolling) return;

                scrollPosition += scrollAmount;

                // Reset to start when reaching the end
                if (scrollPosition >= servicesGrid.scrollWidth - servicesGrid.clientWidth) {
                    scrollPosition = 0;
                }

                servicesGrid.scrollTo({
                    left: scrollPosition,
                    behavior: 'smooth'
                });
            }, 3000); // Scroll every 3 seconds
        }
    };

    // Pause auto-scroll when user interacts
    if (servicesGrid) {
        servicesGrid.addEventListener('touchstart', () => {
            isAutoScrolling = false;
            clearInterval(autoScrollInterval);
        });

        servicesGrid.addEventListener('touchend', () => {
            setTimeout(() => {
                startAutoScroll();
            }, 5000); // Resume after 5 seconds of no interaction
        });

        // Start auto-scroll on load
        startAutoScroll();

        // Restart on window resize
        window.addEventListener('resize', () => {
            clearInterval(autoScrollInterval);
            startAutoScroll();
        });
    }


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

    // ========================================
    // STATS COUNTER ANIMATION
    // Animates numbers from 0 to target value
    // ========================================

    const animateCounter = (element, target, duration = 2000, suffix = '') => {
        let startTime = null;
        const startValue = 0;

        // Parse the target value (remove any non-numeric characters except decimal point)
        const numericTarget = parseFloat(target.replace(/[^0-9.]/g, ''));

        const animate = (currentTime) => {
            if (!startTime) startTime = currentTime;
            const progress = Math.min((currentTime - startTime) / duration, 1);

            // Easing function for smooth animation (easeOutExpo)
            const easeOutExpo = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);

            const currentValue = startValue + (numericTarget - startValue) * easeOutExpo;

            // Format the number based on the original target format
            let displayValue;
            if (target.includes('M+')) {
                displayValue = currentValue.toFixed(1) + 'M+';
            } else if (target.includes('K+') || target.includes(',')) {
                displayValue = Math.floor(currentValue).toLocaleString() + '+';
            } else if (target.includes('/')) {
                displayValue = currentValue.toFixed(1) + '/5';
            } else {
                displayValue = Math.floor(currentValue).toLocaleString() + suffix;
            }

            element.textContent = displayValue;

            if (progress < 1) {
                requestAnimationFrame(animate);
            } else {
                element.textContent = target; // Ensure final value is exact
            }
        };

        requestAnimationFrame(animate);
    };

    // Intersection Observer for Stats Animation
    const statsItems = document.querySelectorAll('.stat-item');

    if (statsItems.length > 0) {
        const statsObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !entry.target.classList.contains('animated')) {
                    entry.target.classList.add('animated');

                    // Find the h3 element and animate its counter
                    const counterElement = entry.target.querySelector('h3');
                    if (counterElement) {
                        const targetValue = counterElement.textContent.trim();

                        // Determine animation duration based on value size
                        let duration = 2000;
                        if (targetValue.includes('M+')) {
                            duration = 2500;
                        } else if (targetValue.includes('/')) {
                            duration = 1800;
                        }

                        // Start counter animation with a slight delay for stagger effect
                        const delay = Array.from(statsItems).indexOf(entry.target) * 200;
                        setTimeout(() => {
                            animateCounter(counterElement, targetValue, duration);
                        }, delay);
                    }
                }
            });
        }, {
            root: null,
            threshold: 0.3, // Trigger when 30% of the element is visible
            rootMargin: '0px'
        });

        statsItems.forEach(item => {
            statsObserver.observe(item);
        });
    }


    // Stats auto-scroll disabled - now using grid layout on mobile
    // All three stats are visible on one screen without scrolling
    /*
    const statsContainer = document.querySelector('.infographic-stats');
    let isStatsAutoScrolling = false;
    let statsAutoScrollInterval;

    const startStatsAutoScroll = () => {
        if (window.innerWidth <= 768 && statsContainer) {
            isStatsAutoScrolling = true;
            let scrollPosition = 0;
            const statItem = statsContainer.querySelector('.stat-item');
            if (!statItem) return;

            const itemWidth = statItem.offsetWidth || 300;
            const gap = 20;
            const scrollAmount = itemWidth + gap;

            statsAutoScrollInterval = setInterval(() => {
                if (!isStatsAutoScrolling) return;

                scrollPosition += scrollAmount;

                // Reset to start when reaching the end
                if (scrollPosition >= statsContainer.scrollWidth - statsContainer.clientWidth) {
                    scrollPosition = 0;
                }

                statsContainer.scrollTo({
                    left: scrollPosition,
                    behavior: 'smooth'
                });
            }, 4000);
        }
    };

    if (statsContainer) {
        statsContainer.addEventListener('touchstart', () => {
            isStatsAutoScrolling = false;
            clearInterval(statsAutoScrollInterval);
        });

        statsContainer.addEventListener('touchend', () => {
            setTimeout(() => {
                startStatsAutoScroll();
            }, 6000);
        });

        setTimeout(() => {
            startStatsAutoScroll();
        }, 1000);

        window.addEventListener('resize', () => {
            clearInterval(statsAutoScrollInterval);
            startStatsAutoScroll();
        });
    }
    */
});

// Unified Floating WhatsApp Button Functionality
const initWhatsAppButton = () => {
    // Check if it already exists to avoid duplication
    if (document.querySelector('.unified-whatsapp-btn')) return;

    const btn = document.createElement('a');
    btn.href = 'https://wa.me/917042555401';
    btn.className = 'unified-whatsapp-btn';
    btn.target = '_blank';
    btn.rel = 'noopener noreferrer';
    btn.innerHTML = '<i class="fa-brands fa-whatsapp"></i>';
    
    // Add styling directly or via CSS
    Object.assign(btn.style, {
        position: 'fixed',
        bottom: '25px',
        right: '25px',
        width: '55px',
        height: '55px',
        backgroundColor: '#25D366',
        color: '#FFF',
        borderRadius: '50%',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        fontSize: '30px',
        boxShadow: '0 4px 15px rgba(0,0,0,0.2)',
        zIndex: '10000',
        transition: 'all 0.3s ease',
        cursor: 'pointer',
        textDecoration: 'none'
    });

    // Hover effects via JS
    btn.addEventListener('mouseenter', () => {
        btn.style.transform = 'scale(1.1) rotate(5deg)';
        btn.style.boxShadow = '0 6px 20px rgba(0,0,0,0.3)';
    });
    btn.addEventListener('mouseleave', () => {
        btn.style.transform = 'scale(1.0) rotate(0deg)';
        btn.style.boxShadow = '0 4px 15px rgba(0,0,0,0.2)';
    });

    document.body.appendChild(btn);
};

// Initialize WhatsApp on load
initWhatsAppButton();
