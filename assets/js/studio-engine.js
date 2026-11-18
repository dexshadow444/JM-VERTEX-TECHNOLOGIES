/**
 * JM VERTEX TECHNOLOGIES — Awwwards Studio Grade Interactive Engine
 * Inspired by Lusion.co, Unseen.co, Eszter Bial & BDSN Club
 * Features: Cinematic Preloader, 3D Fluid WebGL Canvas, Magnetic Cursor,
 * Sound Synthesizer, Mask Line Triggers, and Floating Project Previews.
 */

(function (window, document) {
  'use strict';

  // ==========================================================================
  // 1. TOP PRECISION ARCHITECTURAL PROGRESS BAR
  // ==========================================================================
  const topProgress = document.getElementById('top-progress-bar');
  if (topProgress) {
    topProgress.style.transform = 'scaleX(0.65)';
    window.addEventListener('load', () => {
      topProgress.style.transform = 'scaleX(1)';
      setTimeout(() => {
        topProgress.style.opacity = '0';
        setTimeout(() => { topProgress.style.display = 'none'; }, 350);
      }, 200);
    });
  }

  // Preloader removal safety
  const preloader = document.getElementById('site-preloader');
  if (preloader) {
    preloader.style.display = 'none';
  }
  document.body.classList.add('page-revealed');

  // Mobile Drawer Toggle
  window.toggleMobileMenu = function () {
    const drawer = document.querySelector('.mobile-drawer');
    const backdrop = document.querySelector('.mobile-backdrop');
    if (drawer) {
      drawer.classList.toggle('open');
      if (backdrop) backdrop.classList.toggle('active');
    }
  };

  function triggerHeroMasks() {
    document.querySelectorAll('.hero-mask-line').forEach((el, index) => {
      setTimeout(() => {
        el.classList.add('revealed');
      }, index * 120);
    });
  }

  // ==========================================================================
  // 2. MAGNETIC FLUID DUAL CURSOR (with text mode)
  // ==========================================================================
  const cursorDot = document.querySelector('.custom-cursor-dot');
  const cursorFollower = document.querySelector('.custom-cursor-follower');

  if (cursorDot && cursorFollower) {
    let mouseX = window.innerWidth / 2;
    let mouseY = window.innerHeight / 2;
    let followerX = mouseX;
    let followerY = mouseY;

    window.addEventListener('mousemove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
      cursorDot.style.transform = `translate3d(${mouseX}px, ${mouseY}px, 0) translate(-50%, -50%)`;
    }, { passive: true });

    function renderCursor() {
      // Spring lerp
      followerX += (mouseX - followerX) * 0.14;
      followerY += (mouseY - followerY) * 0.14;
      cursorFollower.style.transform = `translate3d(${followerX}px, ${followerY}px, 0) translate(-50%, -50%)`;
      requestAnimationFrame(renderCursor);
    }
    requestAnimationFrame(renderCursor);

    // Interactive Hover Elements
    const hoverTargets = document.querySelectorAll('a, button, .studio-glass-card, .project-strip-item, input, textarea, select');
    hoverTargets.forEach(el => {
      el.addEventListener('mouseenter', () => {
        cursorFollower.classList.add('cursor-hover');
        const customText = el.getAttribute('data-cursor-text');
        if (customText) {
          cursorFollower.textContent = customText;
        }
      });
      el.addEventListener('mouseleave', () => {
        cursorFollower.classList.remove('cursor-hover');
        cursorFollower.textContent = '';
      });
    });
  }

  // ==========================================================================
  // 3. 3D FLUID CYBER CANVAS SIMULATION (Lusion / WebGL inspired)
  // ==========================================================================
  const canvas = document.getElementById('cyber-canvas');
  if (canvas) {
    const ctx = canvas.getContext('2d');
    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    let mouse = { x: width / 2, y: height / 2, vx: 0, vy: 0, prevX: width / 2, prevY: height / 2 };
    window.addEventListener('mousemove', (e) => {
      mouse.vx = e.clientX - mouse.prevX;
      mouse.vy = e.clientY - mouse.prevY;
      mouse.prevX = mouse.x = e.clientX;
      mouse.prevY = mouse.y = e.clientY;
    }, { passive: true });

    // Multi-Layer Flow Ribbons
    const ribbons = [];
    const ribbonCount = 5;
    for (let r = 0; r < ribbonCount; r++) {
      ribbons.push({
        yBase: (height / (ribbonCount + 1)) * (r + 1),
        speed: 0.0015 + r * 0.0006,
        amplitude: 35 + r * 15,
        frequency: 0.002 + r * 0.0008,
        phase: r * Math.PI * 0.5,
        color: r % 2 === 0 ? 'rgba(0, 255, 136,' : 'rgba(0, 240, 255,'
      });
    }

    // Interactive Floating Quantum Nodes
    const nodes = [];
    const nodeCount = Math.min(Math.floor((width * height) / 16000), 75);
    for (let i = 0; i < nodeCount; i++) {
      nodes.push({
        x: Math.random() * width,
        y: Math.random() * height,
        z: Math.random() * 300 - 150,
        vx: (Math.random() - 0.5) * 0.5,
        vy: (Math.random() - 0.5) * 0.5,
        size: Math.random() * 2 + 1,
        alpha: Math.random() * 0.4 + 0.2
      });
    }

    let time = 0;
    function render3DFluid() {
      ctx.clearRect(0, 0, width, height);
      time += 1;

      // Draw Fluid Energy Waves
      ribbons.forEach(rib => {
        ctx.beginPath();
        ctx.moveTo(0, rib.yBase);
        for (let x = 0; x <= width; x += 15) {
          // Dynamic mouse wave displacement
          const dx = x - mouse.x;
          const distMouse = Math.abs(dx);
          const mouseDisplace = distMouse < 220 ? Math.sin((220 - distMouse) / 220 * Math.PI) * mouse.vy * 0.4 : 0;
          const y = rib.yBase + Math.sin(x * rib.frequency + time * rib.speed + rib.phase) * rib.amplitude + mouseDisplace;
          ctx.lineTo(x, y);
        }
        ctx.strokeStyle = rib.color + ' 0.12)';
        ctx.lineWidth = 1.5;
        ctx.stroke();
      });

      // Draw Quantum Mesh Nodes & Connecting Light Beams
      const fov = 380;
      for (let i = 0; i < nodes.length; i++) {
        const n = nodes[i];
        n.x += n.vx;
        n.y += n.vy;

        if (n.x < 0) n.x = width;
        if (n.x > width) n.x = 0;
        if (n.y < 0) n.y = height;
        if (n.y > height) n.y = 0;

        // Perspective 3D
        const scale = fov / (fov + n.z);
        const px = (n.x - width / 2) * scale + width / 2;
        const py = (n.y - height / 2) * scale + height / 2;

        ctx.beginPath();
        ctx.arc(px, py, n.size * scale, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(0, 255, 136, ${n.alpha * scale})`;
        ctx.fill();

        // Connect adjacent nodes
        for (let j = i + 1; j < nodes.length; j++) {
          const n2 = nodes[j];
          const dist = Math.hypot(n.x - n2.x, n.y - n2.y);
          if (dist < 110) {
            ctx.beginPath();
            ctx.moveTo(px, py);
            const scale2 = fov / (fov + n2.z);
            ctx.lineTo((n2.x - width / 2) * scale2 + width / 2, (n2.y - height / 2) * scale2 + height / 2);
            ctx.strokeStyle = `rgba(0, 255, 136, ${(1 - dist / 110) * 0.14})`;
            ctx.lineWidth = 0.6;
            ctx.stroke();
          }
        }
      }

      requestAnimationFrame(render3DFluid);
    }
    render3DFluid();

    window.addEventListener('resize', () => {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    }, { passive: true });
  }

  // ==========================================================================
  // 4. FLOATING PROJECT HOVER PREVIEWS (Unseen style)
  // ==========================================================================
  const projectRows = document.querySelectorAll('.project-strip-item');
  const hoverPreview = document.getElementById('project-hover-preview');
  const hoverImg = document.getElementById('project-hover-img');

  if (projectRows.length && hoverPreview && hoverImg) {
    let targetX = 0, targetY = 0;
    let currX = 0, currY = 0;

    window.addEventListener('mousemove', (e) => {
      targetX = e.clientX;
      targetY = e.clientY;
    }, { passive: true });

    function updatePreviewPos() {
      currX += (targetX - currX) * 0.12;
      currY += (targetY - currY) * 0.12;
      hoverPreview.style.left = `${currX}px`;
      hoverPreview.style.top = `${currY}px`;
      requestAnimationFrame(updatePreviewPos);
    }
    requestAnimationFrame(updatePreviewPos);

    projectRows.forEach(row => {
      row.addEventListener('mouseenter', () => {
        const imgSrc = row.getAttribute('data-preview-img');
        if (imgSrc) {
          hoverImg.src = imgSrc;
          hoverPreview.classList.add('active');
        }
      });
      row.addEventListener('mouseleave', () => {
        hoverPreview.classList.remove('active');
      });
    });
  }

  // ==========================================================================
  // 5. SOUND ATMOSPHERE SYNTHESIZER (Web Audio API)
  // ==========================================================================
  let audioCtx = null;
  let isSoundEnabled = false;

  const soundBtn = document.getElementById('sound-toggle');
  if (soundBtn) {
    soundBtn.addEventListener('click', () => {
      if (!audioCtx) {
        audioCtx = new (window.AudioContext || window.webkitAudioContext)();
      }
      if (audioCtx.state === 'suspended') {
        audioCtx.resume();
      }

      isSoundEnabled = !isSoundEnabled;
      soundBtn.classList.toggle('sound-on', isSoundEnabled);
      const textSpan = soundBtn.querySelector('.sound-status-text');
      if (textSpan) textSpan.textContent = isSoundEnabled ? 'SOUND: ON' : 'SOUND: OFF';

      if (isSoundEnabled) playMicroTone(520, 0.05);
    });

    function playMicroTone(freq, dur = 0.04) {
      if (!isSoundEnabled || !audioCtx) return;
      try {
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
        gain.gain.setValueAtTime(0.015, audioCtx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + dur);
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        osc.start();
        osc.stop(audioCtx.currentTime + dur);
      } catch (err) {}
    }

    // Attach subtle feedback tone to navigation links & buttons
    document.querySelectorAll('a, button').forEach(el => {
      el.addEventListener('mouseenter', () => {
        if (isSoundEnabled) playMicroTone(440, 0.03);
      });
    });
  }

  // ==========================================================================
  // 6. SCROLL MASK & COUNTER REVEALS
  // ==========================================================================
  const scrollMasks = document.querySelectorAll('.mask-line-reveal, .reveal-on-scroll');
  if ('IntersectionObserver' in window && scrollMasks.length) {
    const observer = new IntersectionObserver((entries, obs) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('revealed');
          obs.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });

    scrollMasks.forEach(el => observer.observe(el));
  } else {
    scrollMasks.forEach(el => el.classList.add('revealed'));
  }

})(window, document);
