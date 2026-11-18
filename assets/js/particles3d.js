/**
 * JM VERTEX TECHNOLOGIES — 3D Cyber Particle Flow System
 * High-performance, GPU-accelerated canvas particle simulation with 
 * 3D wave undulation, mouse repulsion, and connecting data streams.
 */

(function () {
  'use strict';

  const canvas = document.getElementById('cyber-canvas');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  let width = (canvas.width = window.innerWidth);
  let height = (canvas.height = window.innerHeight);

  const particles = [];
  const particleCount = Math.min(Math.floor((width * height) / 14000), 100);
  const maxDistance = 140;

  const mouse = {
    x: width / 2,
    y: height / 2,
    targetX: width / 2,
    targetY: height / 2,
    isHovered: false
  };

  class Particle {
    constructor() {
      this.reset(true);
    }

    reset(initial = false) {
      this.x = Math.random() * width;
      this.y = initial ? Math.random() * height : height + 10;
      this.z = Math.random() * 400 - 200; // 3D depth
      this.baseZ = this.z;
      this.vx = (Math.random() - 0.5) * 0.7;
      this.vy = -(Math.random() * 0.5 + 0.3); // upward drift
      this.radius = Math.random() * 1.8 + 1;
      this.alpha = Math.random() * 0.5 + 0.2;
      this.waveAngle = Math.random() * Math.PI * 2;
      this.waveSpeed = Math.random() * 0.02 + 0.01;
    }

    update() {
      // 3D Sine Wave Motion
      this.waveAngle += this.waveSpeed;
      const waveOffsetX = Math.sin(this.waveAngle) * 0.5;
      const waveOffsetZ = Math.cos(this.waveAngle) * 1.2;

      this.x += this.vx + waveOffsetX;
      this.y += this.vy;
      this.z = this.baseZ + waveOffsetZ;

      // Mouse interactive repulsion (in 3D projected space)
      const dx = this.x - mouse.x;
      const dy = this.y - mouse.y;
      const dist = Math.sqrt(dx * dx + dy * dy);

      if (dist < 180) {
        const force = (180 - dist) / 180;
        this.x += (dx / dist) * force * 3;
        this.y += (dy / dist) * force * 3;
      }

      // Wrap around viewport
      if (this.y < -20) this.reset(false);
      if (this.x < -20) this.x = width + 10;
      if (this.x > width + 20) this.x = -10;
    }

    draw() {
      // Perspective projection
      const fov = 350;
      const scale = fov / (fov + this.z);
      const projX = (this.x - width / 2) * scale + width / 2;
      const projY = (this.y - height / 2) * scale + height / 2;
      const projRadius = Math.max(0.5, this.radius * scale);
      const projAlpha = Math.max(0.05, Math.min(1, this.alpha * scale));

      ctx.beginPath();
      ctx.arc(projX, projY, projRadius, 0, Math.PI * 2);
      ctx.fillStyle = `rgba(34, 197, 94, ${projAlpha})`;
      ctx.shadowBlur = 8 * scale;
      ctx.shadowColor = 'rgba(0, 255, 136, 0.6)';
      ctx.fill();
      ctx.shadowBlur = 0; // reset
    }
  }

  // Initialize Particles
  for (let i = 0; i < particleCount; i++) {
    particles.push(new Particle());
  }

  // Draw connecting cyber lines
  function drawConnections() {
    const fov = 350;
    for (let i = 0; i < particles.length; i++) {
      for (let j = i + 1; j < particles.length; j++) {
        const p1 = particles[i];
        const p2 = particles[j];

        const dx = p1.x - p2.x;
        const dy = p1.y - p2.y;
        const dz = (p1.z - p2.z) * 0.4;
        const dist = Math.sqrt(dx * dx + dy * dy + dz * dz);

        if (dist < maxDistance) {
          const alpha = (1 - dist / maxDistance) * 0.22;
          const scale1 = fov / (fov + p1.z);
          const scale2 = fov / (fov + p2.z);

          const x1 = (p1.x - width / 2) * scale1 + width / 2;
          const y1 = (p1.y - height / 2) * scale1 + height / 2;
          const x2 = (p2.x - width / 2) * scale2 + width / 2;
          const y2 = (p2.y - height / 2) * scale2 + height / 2;

          ctx.beginPath();
          ctx.moveTo(x1, y1);
          ctx.lineTo(x2, y2);
          ctx.strokeStyle = `rgba(16, 185, 129, ${alpha})`;
          ctx.lineWidth = 0.75 * Math.min(scale1, scale2);
          ctx.stroke();
        }
      }
    }
  }

  // Render loop
  function animate() {
    ctx.clearRect(0, 0, width, height);

    // Smooth mouse interpolation
    mouse.x += (mouse.targetX - mouse.x) * 0.08;
    mouse.y += (mouse.targetY - mouse.y) * 0.08;

    particles.forEach(p => {
      p.update();
      p.draw();
    });

    drawConnections();
    requestAnimationFrame(animate);
  }

  // Event Listeners
  window.addEventListener('resize', () => {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
  }, { passive: true });

  window.addEventListener('mousemove', (e) => {
    mouse.targetX = e.clientX;
    mouse.targetY = e.clientY;
    mouse.isHovered = true;
  }, { passive: true });

  window.addEventListener('touchmove', (e) => {
    if (e.touches.length > 0) {
      mouse.targetX = e.touches[0].clientX;
      mouse.targetY = e.touches[0].clientY;
    }
  }, { passive: true });

  animate();
})();
