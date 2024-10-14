document.addEventListener("DOMContentLoaded", () => {
    const circle = document.querySelector(".main-timeline::before");
    
    window.addEventListener("scroll", () => {
        const scrollPosition = window.scrollY;
        const timelineHeight = document.querySelector(".main-timeline").offsetHeight;
        const windowHeight = window.innerHeight;

        // Calculate the maximum scrollable distance
        const maxScroll = timelineHeight - windowHeight;

        // Calculate the percentage of scroll
        const scrollPercent = Math.min(scrollPosition / maxScroll, 1);

        // Set the new position of the circle based on scroll percentage
        circle.style.transform = `translateY(${scrollPercent * timelineHeight}px)`;
    });
});