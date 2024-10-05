let currentSlideIndex = 0;
const slidesToShow = 3; // Number of cards to show at once
const slides = document.querySelectorAll('.testimonial-card');
const dots = document.querySelectorAll('.dot');
const totalSlides = slides.length - (slidesToShow - 1);

function showSlide(index) {
    const track = document.querySelector('.testimonial-track');
    track.style.transform = `translateX(-${index * (100 / slidesToShow)}%)`;

    dots.forEach(dot => dot.classList.remove('active'));
    dots[index].classList.add('active');
}

function nextSlide() {
    currentSlideIndex = (currentSlideIndex + 1) % totalSlides;
    showSlide(currentSlideIndex);
}

function currentSlide(index) {
    currentSlideIndex = index;
    showSlide(currentSlideIndex);
}

setInterval(nextSlide, 3000); // Automatically change slides every 3 seconds

// Initialize
showSlide(currentSlideIndex);





