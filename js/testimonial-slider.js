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


const scrollRevealOption={
    distance:'90px',
    origin:'bottom',
    duration:1200
}
ScrollReveal().reveal('.benefit-left h2, .benefit-left h1',{...scrollRevealOption,delay:'100'})
ScrollReveal().reveal(".benefit-head-desc",{...scrollRevealOption,origin:'right',delay:'200'})
ScrollReveal().reveal(".benefit-left-points",{...scrollRevealOption,origin:'right',delay:'300'})

ScrollReveal().reveal('.why-carmaa-container h1, .why-carmaa-container h2,.why-carmaa-container .header-description',{...scrollRevealOption,delay:'100'})
ScrollReveal().reveal('.why-carmaa-container .header-description',{...scrollRevealOption,delay:'200'})
ScrollReveal().reveal('.why-carmaa-card-container',{...scrollRevealOption,origin:'right',distance:'200px', duration:1500,delay:'300'})

ScrollReveal().reveal('.benefit-element-wrapper-container',{...scrollRevealOption,origin:'left',distance:'200px', duration:1500,delay:'200'})

ScrollReveal().reveal('.parallex-cta-inner',{...scrollRevealOption,distance:'100px', duration:1500,delay:'100'});





