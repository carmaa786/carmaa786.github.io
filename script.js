document.addEventListener('DOMContentLoaded', () => {
    // 1. CRITICAL INITIALIZATION (Immediate & Fast)
    const initCritical = () => {
        const detectDevice = () => {
            const ua = navigator.userAgent || navigator.vendor || window.opera;
            return (/iPad|iPhone|iPod/.test(ua) && !window.MSStream) ? 'ios' : 
                   (/android/i.test(ua) ? 'android' : 'ios');
        };

        const deviceType = detectDevice();
        const urls = {
            ios: 'https://apps.apple.com/in/app/carmaa-car-care/id6746490090',
            android: 'https://play.google.com/store/apps/details?id=com.carmaacarcare.carmaa'
        };
        document.querySelectorAll('.app-download-link').forEach(link => link.href = urls[deviceType]);

        // Navbar & Hero Scroll (Hardware Accelerated)
        const navbar = document.querySelector('.navbar');
        const hero = document.querySelector('.hero');
        const heroContent = document.querySelector('.hero-content');
        if (heroContent) heroContent.style.willChange = 'auto';
        
        let ticking = false;
        const heroHeight = hero ? hero.offsetHeight : 0;

        window.addEventListener('scroll', () => {
            if (!ticking) {
                window.requestAnimationFrame(() => {
                    const scrolled = window.pageYOffset;
                    if (navbar) navbar.classList.toggle('scrolled', scrolled > 100);
                    if (hero && heroContent) {
                        if (scrolled < heroHeight) {
                            if (heroContent.style.willChange !== 'transform, opacity') {
                                heroContent.style.willChange = 'transform, opacity';
                            }
                            heroContent.style.transform = `translateY(${scrolled * 0.3}px)`;
                            heroContent.style.opacity = 1 - (scrolled / heroHeight) * 0.7;
                        } else {
                            heroContent.style.transform = '';
                            heroContent.style.opacity = '';
                            heroContent.style.willChange = 'auto';
                        }
                    }
                    ticking = false;
                });
                ticking = true;
            }
        }, { passive: true });
    };

    initCritical();

    // 2. YIELDING INITIALIZATION (Broken into sub-50ms tasks to protect TBT)
    const taskQueue = [
        // Task 1: Reveal Observer
        () => {
            const revealElements = document.querySelectorAll('.reveal');
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) entry.target.classList.add('active');
                });
            }, { threshold: 0.15 });
            revealElements.forEach(el => observer.observe(el));
        },
        // Task 2: Reviews Rendering
        () => {
            const track = document.getElementById('reviewsTrack');
            const trackDup = document.getElementById('reviewsTrackDuplicate');
            if (track && trackDup) {
                const reviews = [
                    { name: "Rahul Sharma", role: "Local Guide", text: "Absolutely game changer! Saved me 3 hours of waiting. Showroom quality finish.", stars: 5, initial: "R", bg: "#E0F2FE", color: "#0369A1" },
                    { name: "Priya Patel", role: "Local Guide", text: "The app is so easy to use. Spotless car while I was at the gym!", stars: 5, initial: "P", bg: "#FDF4FF", color: "#A21CAF" },
                    { name: "Amit Verma", role: "24 reviews", text: "Premium spa package is worth every rupee. My 5-year old Creta looks new.", stars: 5, initial: "A", bg: "#ECFCCB", color: "#4D7C0F" },
                    { name: "Sneha Gupta", role: "Local Guide", text: "Best detailing service in Noida. Interior deep clean removed all stains.", stars: 5, initial: "S", bg: "#FFF7ED", color: "#C2410C" },
                    { name: "Vikram Singh", role: "Local Guide", text: "Finally a service that understands luxury cars. Fortuner handled with care.", stars: 5, initial: "V", bg: "#F0F9FF", color: "#0F766E" }
                ];
                const frag = document.createDocumentFragment();
                reviews.forEach(r => {
                    const card = document.createElement('div');
                    card.className = 'review-card';
                    card.innerHTML = `<div class="review-header"><div class="reviewer-profile"><div class="reviewer-avatar" style="background:${r.bg};color:${r.color}">${r.initial}</div><div class="reviewer-info"><h4>${r.name}</h4><span>${r.role}</span></div></div><i class="fa-brands fa-google colored-google-icon"></i></div><div class="review-stars">${Array(r.stars).fill('<i class="fa-solid fa-star"></i>').join('')}</div><p class="review-text">${r.text}</p>`;
                    frag.appendChild(card);
                });
                track.appendChild(frag.cloneNode(true));
                trackDup.appendChild(frag);
            }
        },
        // Task 3: Stats Animation
        () => {
            const stats = document.querySelectorAll('.stat-item');
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting && !entry.target.classList.contains('animated')) {
                        entry.target.classList.add('animated');
                        const h3 = entry.target.querySelector('h3');
                        if (!h3) return;
                        const targetStr = h3.textContent.trim();
                        const targetNum = parseFloat(targetStr.replace(/[^0-9.]/g, ''));
                        let start = null;
                        const anim = (t) => {
                            if (!start) start = t;
                            const prog = Math.min((t - start) / 2000, 1);
                            const val = targetNum * (1 - Math.pow(2, -10 * prog));
                            h3.textContent = targetStr.includes('M+') ? val.toFixed(1) + 'M+' : 
                                            (targetStr.includes('/') ? val.toFixed(1) + '/5' : Math.floor(val).toLocaleString() + '+');
                            if (prog < 1) requestAnimationFrame(anim);
                            else h3.textContent = targetStr;
                        };
                        requestAnimationFrame(anim);
                    }
                });
            }, { threshold: 0.3 });
            stats.forEach(s => observer.observe(s));
        },
        // Task 4: UI Interactivity (FAQ, Carousel)
        () => {
            document.querySelectorAll('.faq-item').forEach(item => {
                item.querySelector('.faq-question')?.addEventListener('click', () => {
                    const wasActive = item.classList.contains('active');
                    document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('active'));
                    if (!wasActive) item.classList.add('active');
                });
            });

            const grid = document.querySelector('.services-grid');
            if (grid && window.innerWidth <= 768) {
                let pos = 0;
                let carouselTimer = null;
                const startCarousel = () => {
                    if (carouselTimer) return;
                    carouselTimer = setInterval(() => {
                        const w = grid.querySelector('.service-card')?.offsetWidth || 300;
                        pos = (pos + w + 20 >= grid.scrollWidth - grid.clientWidth) ? 0 : pos + w + 20;
                        grid.scrollTo({ left: pos, behavior: 'smooth' });
                    }, 4000);
                };
                const stopCarousel = () => {
                    if (carouselTimer) {
                        clearInterval(carouselTimer);
                        carouselTimer = null;
                    }
                };
                const carouselObserver = new IntersectionObserver((entries) => {
                    entries[0].isIntersecting ? startCarousel() : stopCarousel();
                }, { threshold: 0.1 });
                carouselObserver.observe(grid);
            }
        }
    ];

    const runTasks = () => {
        if (taskQueue.length === 0) return;
        const task = taskQueue.shift();
        task();
        if (window.requestIdleCallback) {
            requestIdleCallback(runTasks);
        } else {
            setTimeout(runTasks, 100);
        }
    };

    if (window.requestIdleCallback) {
        requestIdleCallback(runTasks);
    } else {
        setTimeout(runTasks, 500);
    }
});
