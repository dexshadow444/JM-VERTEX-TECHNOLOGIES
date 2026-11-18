/**
 * JM VERTEX TECHNOLOGIES — 3D Card Tilt & Specular Physics
 * Smooth 3D perspective tilt with mouse-reactive specular highlights.
 */

(function () {
  'use strict';

  function initTiltCards() {
    const cards = document.querySelectorAll('.tilt-card');
    if (!cards.length) return;

    cards.forEach(card => {
      // Ensure glare element exists
      let glare = card.querySelector('.tilt-glare');
      if (!glare) {
        glare = document.createElement('div');
        glare.className = 'tilt-glare';
        card.appendChild(glare);
      }

      let bounds;

      function onMouseEnter() {
        bounds = card.getBoundingClientRect();
      }

      function onMouseMove(e) {
        if (!bounds) bounds = card.getBoundingClientRect();
        const mouseX = e.clientX - bounds.left;
        const mouseY = e.clientY - bounds.top;

        const xPct = mouseX / bounds.width;
        const yPct = mouseY / bounds.height;

        const tiltX = (0.5 - yPct) * 16; // max 16deg tilt
        const tiltY = (xPct - 0.5) * 16;

        card.style.transform = `perspective(1000px) rotateX(${tiltX}deg) rotateY(${tiltY}deg) scale3d(1.02, 1.02, 1.02)`;
        card.style.setProperty('--mouse-x', `${mouseX}px`);
        card.style.setProperty('--mouse-y', `${mouseY}px`);
      }

      function onMouseLeave() {
        card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
        bounds = null;
      }

      card.addEventListener('mouseenter', onMouseEnter, { passive: true });
      card.addEventListener('mousemove', onMouseMove, { passive: true });
      card.addEventListener('mouseleave', onMouseLeave, { passive: true });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initTiltCards);
  } else {
    initTiltCards();
  }
})();
