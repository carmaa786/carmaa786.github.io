/* Carmaa city-page testimonials — continuous auto-scroll carousel.
   Duplicates the testimonial cards for a seamless loop and drives the
   scroll with requestAnimationFrame. Pauses on hover. The transform is
   set with inline !important so it beats the city.min.css
   "transform:none !important" rule. */
(function () {
  function init() {
    var track = document.querySelector('.testimonial-track-2');
    if (!track || track.dataset.carmaaMarquee) return;

    var cards = Array.prototype.slice.call(track.children);
    if (cards.length === 0) return;
    track.dataset.carmaaMarquee = '1';

    /* duplicate the card set so translateX can loop seamlessly */
    cards.forEach(function (c) {
      track.appendChild(c.cloneNode(true));
    });

    /* measure the width of one full (original) set of cards */
    function measureSet() {
      var w = 0;
      cards.forEach(function (c) {
        var rect = c.getBoundingClientRect();
        var st = window.getComputedStyle(c);
        w += rect.width +
             parseFloat(st.marginLeft || 0) +
             parseFloat(st.marginRight || 0);
      });
      return w;
    }

    var setWidth = measureSet();
    var x = 0;
    var speed = 0.5; /* px per frame */
    var paused = false;

    track.addEventListener('mouseenter', function () { paused = true; });
    track.addEventListener('mouseleave', function () { paused = false; });

    /* recalc on resize so the loop point stays correct */
    window.addEventListener('resize', function () {
      setWidth = measureSet();
    });

    function step() {
      if (!paused && setWidth > 0) {
        x -= speed;
        if (Math.abs(x) >= setWidth) x = 0;
        track.style.setProperty('transform', 'translateX(' + x + 'px)', 'important');
      }
      window.requestAnimationFrame(step);
    }
    window.requestAnimationFrame(step);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
