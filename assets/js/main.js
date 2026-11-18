/**
 * JM VERTEX TECHNOLOGIES — Core Application Logic
 * Interactive UX, Dynamic Modals, WhatsApp Bridge, and State Handlers.
 */

(function () {
  'use strict';

  // 1. Navigation Header Scroll Effect
  const header = document.querySelector('.site-header');
  function checkHeaderScroll() {
    if (!header) return;
    if (window.scrollY > 40) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  }
  window.addEventListener('scroll', checkHeaderScroll, { passive: true });
  checkHeaderScroll();

  // 2. Mobile Drawer Navigation
  const mobileToggle = document.querySelector('.mobile-toggle');
  const mobileDrawer = document.querySelector('.mobile-drawer');
  const mobileBackdrop = document.querySelector('.mobile-backdrop');

  if (mobileToggle && mobileDrawer && mobileBackdrop) {
    function toggleDrawer(open) {
      const isOpen = open !== undefined ? open : !mobileDrawer.classList.contains('open');
      mobileDrawer.classList.toggle('open', isOpen);
      mobileBackdrop.classList.toggle('open', isOpen);
      document.body.style.overflow = isOpen ? 'hidden' : '';
    }

    mobileToggle.addEventListener('click', () => toggleDrawer());
    mobileBackdrop.addEventListener('click', () => toggleDrawer(false));

    // Close drawer when any mobile link is clicked
    mobileDrawer.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => toggleDrawer(false));
    });
  }

  // 3. Highlight Active Navigation Item
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-link, .dropdown-link, .mobile-link').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });

  // 4. Scroll Reveal Animations (IntersectionObserver)
  const revealElements = document.querySelectorAll('.reveal-on-scroll');
  if ('IntersectionObserver' in window && revealElements.length) {
    const revealObserver = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add('revealed');
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12, rootMargin: '0px 0px -50px 0px' }
    );

    revealElements.forEach(el => revealObserver.observe(el));
  } else {
    revealElements.forEach(el => el.classList.add('revealed'));
  }

  // 5. Stat Counter Animation
  const statNumbers = document.querySelectorAll('.stat-number[data-count]');
  if (statNumbers.length) {
    const countObserver = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const target = parseInt(entry.target.getAttribute('data-count'), 10);
            const suffix = entry.target.getAttribute('data-suffix') || '';
            const duration = 1800; // ms
            const startTime = performance.now();

            function updateCount(currentTime) {
              const elapsed = currentTime - startTime;
              const progress = Math.min(elapsed / duration, 1);
              // easeOutExpo
              const current = Math.floor(progress === 1 ? target : target * (1 - Math.pow(2, -10 * progress)));
              entry.target.textContent = current.toLocaleString() + suffix;

              if (progress < 1) {
                requestAnimationFrame(updateCount);
              }
            }
            requestAnimationFrame(updateCount);
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.5 }
    );

    statNumbers.forEach(num => countObserver.observe(num));
  }

  // 6. Toast Notification Helper
  window.showToast = function (message, type = 'success') {
    let container = document.getElementById('toast-container');
    if (!container) {
      container = document.createElement('div');
      container.id = 'toast-container';
      document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    const icon = type === 'success' 
      ? '<svg width="20" height="20" fill="none" stroke="#22c55e" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>' 
      : '<svg width="20" height="20" fill="none" stroke="#ef4444" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"/></svg>';
    
    toast.innerHTML = `${icon}<span>${window.SecurityGuard ? window.SecurityGuard.escapeHTML(message) : message}</span>`;
    container.appendChild(toast);

    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transform = 'translateX(100%)';
      toast.style.transition = 'all 0.3s ease';
      setTimeout(() => toast.remove(), 300);
    }, 4500);
  };

  // 7. Modals: Review Modal & Syllabus Modal
  window.openModal = function (modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
      modal.classList.add('active');
      document.body.style.overflow = 'hidden';
    }
  };

  window.closeModal = function (modalId) {
    const modal = document.getElementById(modalId);
    if (modal) {
      modal.classList.remove('active');
      document.body.style.overflow = '';
    }
  };

  // Close modal when clicking on backdrop
  document.querySelectorAll('.modal-overlay').forEach(modal => {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        closeModal(modal.id);
      }
    });
  });

  // 8. Lead Capture & Inquiry Forms
  const inquiryForms = document.querySelectorAll('.jm-inquiry-form');
  inquiryForms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();

      if (window.SecurityGuard && !window.SecurityGuard.sanitizeForm(form)) {
        return;
      }

      const name = form.querySelector('[name="name"]')?.value || 'Guest';
      const phone = form.querySelector('[name="phone"]')?.value || '';
      const email = form.querySelector('[name="email"]')?.value || '';
      const service = form.querySelector('[name="interest"]')?.value || 'Services';
      const message = form.querySelector('[name="message"]')?.value || '';

      const submitBtn = form.querySelector('button[type="submit"]');
      const originalText = submitBtn ? submitBtn.innerHTML : 'Submit';
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<span>Processing...</span>';
      }

      // Format WhatsApp pre-filled text
      const waMessage = `Hello JM Vertex Technologies!%0A%0A*Name:* ${encodeURIComponent(name)}%0A*Phone:* ${encodeURIComponent(phone)}%0A*Email:* ${encodeURIComponent(email)}%0A*Service:* ${encodeURIComponent(service)}%0A*Message:* ${encodeURIComponent(message)}`;
      const waUrl = `https://wa.me/919092737477?text=${waMessage}`;

      setTimeout(() => {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.innerHTML = originalText;
        }
        form.reset();
        showToast('Inquiry recorded! Redirecting to WhatsApp for instant response...', 'success');
        
        // Open WhatsApp in new tab for instant connectivity
        setTimeout(() => {
          window.open(waUrl, '_blank', 'noopener,noreferrer');
        }, 1200);
      }, 700);
    });
  });

  // 9. Syllabus Download Form Handler
  const syllabusForm = document.getElementById('syllabus-form');
  if (syllabusForm) {
    syllabusForm.addEventListener('submit', (e) => {
      e.preventDefault();
      if (window.SecurityGuard && !window.SecurityGuard.sanitizeForm(syllabusForm)) return;

      const course = syllabusForm.querySelector('[name="course_name"]')?.value || 'Course Syllabus';
      showToast(`Thank you! The curriculum for ${course} is downloading.`, 'success');
      closeModal('syllabus-modal');
      syllabusForm.reset();
    });
  }

  // 10. Review Submission Form Handler
  const reviewForm = document.getElementById('review-form');
  if (reviewForm) {
    reviewForm.addEventListener('submit', (e) => {
      e.preventDefault();
      if (window.SecurityGuard && !window.SecurityGuard.sanitizeForm(reviewForm)) return;

      showToast('Thank you! Your verified review has been submitted.', 'success');
      closeModal('review-modal');
      reviewForm.reset();
    });
  }

})();
