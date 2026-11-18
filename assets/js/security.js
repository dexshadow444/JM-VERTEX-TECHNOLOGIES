/**
 * JM VERTEX TECHNOLOGIES — Web Security & Resilience Suite
 * Senior-level client-side defense: Anti-Clickjacking, XSS sanitization,
 * Honeypot verification, Safe Link Enforcement, and Network State Monitoring.
 */

(function (window, document) {
  'use strict';

  // 1. Anti-Clickjacking / Framebusting
  try {
    if (window.top !== window.self) {
      window.top.location = window.self.location;
    }
  } catch (e) {
    console.warn('[Security Guard] Frame isolation enforced.');
  }

  // 2. XSS Input Sanitizer & Escaping Utilities
  window.SecurityGuard = {
    escapeHTML: function (str) {
      if (typeof str !== 'string') return '';
      return str
        .replace(/&/g, '&amp;')
        .replace(/</g, '&lt;')
        .replace(/>/g, '&gt;')
        .replace(/"/g, '&quot;')
        .replace(/'/g, '&#x27;')
        .replace(/\//g, '&#x2F;');
    },

    sanitizeForm: function (formElement) {
      // Check Honeypot field (anti-spam / anti-bot)
      const honeypot = formElement.querySelector('input[name="b_fax_code"]');
      if (honeypot && honeypot.value.trim() !== '') {
        console.warn('[Security Guard] Bot submission flagged via honeypot.');
        return false;
      }

      // Validate inputs
      const textInputs = formElement.querySelectorAll('input[type="text"], input[type="email"], input[type="tel"], textarea');
      for (let input of textInputs) {
        // Enforce max reasonable length to prevent buffer/payload flooding
        if (input.value.length > 2000) {
          input.value = input.value.substring(0, 2000);
        }
        // Basic pattern validation for email
        if (input.type === 'email' && input.value) {
          const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
          if (!emailPattern.test(input.value)) {
            alert('Please enter a valid email address.');
            input.focus();
            return false;
          }
        }
      }

      return true;
    },

    generateCSRFToken: function () {
      const array = new Uint8Array(16);
      window.crypto.getRandomValues(array);
      return Array.from(array, byte => byte.toString(16).padStart(2, '0')).join('');
    }
  };

  // 3. Enforce Strict Attributes on External Links
  document.addEventListener('DOMContentLoaded', () => {
    const links = document.querySelectorAll('a[href^="http"]');
    const currentHost = window.location.hostname;

    links.forEach(link => {
      try {
        const url = new URL(link.href);
        if (url.hostname !== currentHost && !url.hostname.includes('jmvertextechnologies.com')) {
          link.setAttribute('rel', 'noopener noreferrer');
          if (!link.hasAttribute('target')) {
            link.setAttribute('target', '_blank');
          }
        }
      } catch (err) {
        // Invalid URL
      }
    });
  });

  // 4. Network Status & Offline Resilience
  function handleNetworkChange() {
    if (!navigator.onLine) {
      // If we are not already on the offline page, prompt or redirect
      if (!window.location.pathname.endsWith('offline.html')) {
        sessionStorage.setItem('jm_prev_page', window.location.href);
        window.location.href = 'offline.html';
      }
    } else {
      const prevPage = sessionStorage.getItem('jm_prev_page');
      if (prevPage && window.location.pathname.endsWith('offline.html')) {
        sessionStorage.removeItem('jm_prev_page');
        window.location.href = prevPage;
      }
    }
  }

  window.addEventListener('offline', handleNetworkChange);
  window.addEventListener('online', handleNetworkChange);

  // 5. CSP Violation Reporter Listener
  document.addEventListener('securitypolicyviolation', (e) => {
    console.warn('[CSP Violation Detected]', {
      blockedURI: e.blockedURI,
      violatedDirective: e.violatedDirective,
      originalPolicy: e.originalPolicy
    });
  });

})(window, document);
