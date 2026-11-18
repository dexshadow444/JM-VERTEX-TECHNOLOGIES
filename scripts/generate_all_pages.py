import os
import json
import html
from base_templates import render_head, render_header, render_footer, ICONS

# Load data
with open('all_page_curricula.json', 'r', encoding='utf-8') as f:
    curricula = json.load(f)

with open('all_blog_posts_full.json', 'r', encoding='utf-8') as f:
    blogs = json.load(f)

print("Starting generation of all 22 pages...")

# Helper to write page
def write_page(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated: {filename}")

# ==============================================================================
# 1. INDEX.HTML (HOMEPAGE)
# ==============================================================================
def build_index():
    head = render_head(
        "JM Vertex Technologies | Web Development, Custom Projects & Tech Training",
        "JM Vertex Technologies delivers high-performance website development, custom IEEE student projects, tech internships in AI, Full Stack & Cloud, and certified German & Japanese language coaching.",
        ""
    )
    header = render_header("home")
    
    body = f"""
    <!-- Hero Section -->
    <section class="section section-hero">
      <div class="container text-center" style="position: relative; z-index: 2;">
        <div class="reveal-on-scroll">
          <div class="pill-badge">
            <span class="pill-dot"></span> Next-Generation Tech Ecosystem & Academy
          </div>
          <h1 class="heading-xl" style="margin-bottom: 1.5rem;">
            Architecting Future Tech & <br>
            <span class="text-gradient">Accelerating Engineering Careers</span>
          </h1>
          <p class="subheading" style="margin-bottom: 2.5rem;">
            From high-conversion web platforms for businesses to IEEE-grade final year projects, intensive industry internships, and global language mastery — we bridge the gap between vision and execution.
          </p>

          <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-bottom: 3.5rem;">
            <a href="website-development.html" class="btn btn-primary btn-lg">
              Explore Web Services {ICONS['arrow_right']}
            </a>
            <a href="student-projects.html" class="btn btn-secondary btn-lg">
              {ICONS['code']} Student Projects
            </a>
            <a href="https://wa.me/919092737477?text=Hi%20JM%20Vertex,%20I%20would%20like%20to%20discuss%20a%20project." target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp btn-lg">
              {ICONS['whatsapp']} Instant Quote
            </a>
          </div>

          <!-- Highlight Bar / Mini Stats -->
          <div class="glass-panel" style="max-width: 900px; margin: 0 auto; padding: 1.5rem 2rem; display: flex; justify-content: space-around; flex-wrap: wrap; gap: 1.5rem;">
            <div>
              <div class="stat-number" style="font-size: 2rem; color: var(--primary-neon);" data-count="500" data-suffix="+">500+</div>
              <div class="stat-label">Projects Guided & Built</div>
            </div>
            <div style="width: 1px; background: rgba(255,255,255,0.1);"></div>
            <div>
              <div class="stat-number" style="font-size: 2rem; color: var(--primary-neon);" data-count="100" data-suffix="%">100%</div>
              <div class="stat-label">Academic Approval Rate</div>
            </div>
            <div style="width: 1px; background: rgba(255,255,255,0.1);"></div>
            <div>
              <div class="stat-number" style="font-size: 2rem; color: var(--primary-neon);" data-count="98" data-suffix="%">98%</div>
              <div class="stat-label">Certification Success</div>
            </div>
            <div style="width: 1px; background: rgba(255,255,255,0.1);"></div>
            <div>
              <div class="stat-number" style="font-size: 2rem; color: var(--primary-neon);" data-count="24" data-suffix="/7">24/7</div>
              <div class="stat-label">Direct Mentor Support</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- 4 Core Pillars (Bento Grid) -->
    <section class="section">
      <div class="container">
        <div class="section-title-wrap reveal-on-scroll">
          <span class="pill-badge"><span class="pill-dot"></span> What We Do</span>
          <h2 class="heading-lg">Four Pillars of <span class="text-gradient">Technological Excellence</span></h2>
          <p class="subheading">Tailored technological solutions and immersive learning pathways designed for both corporate growth and student triumph.</p>
        </div>

        <div class="bento-grid">
          <!-- Pillar 1: Web Development -->
          <div class="col-6 reveal-on-scroll delay-1">
            <div class="glass-panel tilt-card" style="padding: 2.5rem; height: 100%;">
              <div class="tilt-inner">
                <div class="feature-icon-box">{ICONS['globe']}</div>
                <h3 class="heading-md" style="margin-bottom: 0.75rem;">Website & Web App Development</h3>
                <p style="color: var(--text-muted); margin-bottom: 1.5rem;">
                  Custom, modern, and lightning-fast web applications built for small businesses, restaurants, and tech startups. We engineer digital experiences with 90+ Google PageSpeed scores, technical SEO, and conversion optimization.
                </p>
                <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 2rem;">
                  <span class="pill-badge" style="margin-bottom:0;">React & Vite</span>
                  <span class="pill-badge" style="margin-bottom:0;">E-Commerce</span>
                  <span class="pill-badge" style="margin-bottom:0;">WhatsApp Ordering</span>
                </div>
                <a href="website-development.html" class="btn btn-outline-emerald btn-sm">Learn More {ICONS['arrow_right']}</a>
              </div>
            </div>
          </div>

          <!-- Pillar 2: Custom Student Projects -->
          <div class="col-6 reveal-on-scroll delay-2">
            <div class="glass-panel tilt-card" style="padding: 2.5rem; height: 100%;">
              <div class="tilt-inner">
                <div class="feature-icon-box">{ICONS['code']}</div>
                <h3 class="heading-md" style="margin-bottom: 0.75rem;">Custom Projects for College Students</h3>
                <p style="color: var(--text-muted); margin-bottom: 1.5rem;">
                  Don't just buy a project — learn how to build it with our senior engineers. Comprehensive mentorship for B.E., B.Tech, MCA, and MSc students with IEEE paper base implementations, full reports, architecture diagrams, and viva prep.
                </p>
                <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 2rem;">
                  <span class="pill-badge" style="margin-bottom:0;">IEEE Standard</span>
                  <span class="pill-badge" style="margin-bottom:0;">Full Documentation</span>
                  <span class="pill-badge" style="margin-bottom:0;">Live Coding</span>
                </div>
                <a href="student-projects.html" class="btn btn-outline-emerald btn-sm">Explore Projects {ICONS['arrow_right']}</a>
              </div>
            </div>
          </div>

          <!-- Pillar 3: Tech Training & Internships -->
          <div class="col-6 reveal-on-scroll delay-3">
            <div class="glass-panel tilt-card" style="padding: 2.5rem; height: 100%;">
              <div class="tilt-inner">
                <div class="feature-icon-box">{ICONS['grad']}</div>
                <h3 class="heading-md" style="margin-bottom: 0.75rem;">Tech Internships & Training</h3>
                <p style="color: var(--text-muted); margin-bottom: 1.5rem;">
                  Hands-on industry training designed from scratch. Master modern skills in Full Stack MERN, Python, Cloud Computing, AI & Machine Learning, Data Science, and Cybersecurity with verified completion certificates.
                </p>
                <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 2rem;">
                  <span class="pill-badge" style="margin-bottom:0;">Hands-On Labs</span>
                  <span class="pill-badge" style="margin-bottom:0;">Live Projects</span>
                  <span class="pill-badge" style="margin-bottom:0;">Placement Aid</span>
                </div>
                <a href="internship-training.html" class="btn btn-outline-emerald btn-sm">View Curriculum {ICONS['arrow_right']}</a>
              </div>
            </div>
          </div>

          <!-- Pillar 4: Foreign Language Courses -->
          <div class="col-6 reveal-on-scroll delay-4">
            <div class="glass-panel tilt-card" style="padding: 2.5rem; height: 100%;">
              <div class="tilt-inner">
                <div class="feature-icon-box">{ICONS['book']}</div>
                <h3 class="heading-md" style="margin-bottom: 0.75rem;">Foreign Language Coaching</h3>
                <p style="color: var(--text-muted); margin-bottom: 1.5rem;">
                  Unlock tuition-free master's degrees and lucrative global careers in Europe and Asia. We provide structured coaching for German (A1 to B2 with Goethe exam prep) and Japanese (JLPT N5 to N1) with conversational fluency.
                </p>
                <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 2rem;">
                  <span class="pill-badge" style="margin-bottom:0;">German A1-B2</span>
                  <span class="pill-badge" style="margin-bottom:0;">Japanese JLPT</span>
                  <span class="pill-badge" style="margin-bottom:0;">Study Abroad SOPs</span>
                </div>
                <a href="german-language-course.html" class="btn btn-outline-emerald btn-sm">Language Programs {ICONS['arrow_right']}</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Tech Training Tracks Grid -->
    <section class="section" style="background: rgba(9, 14, 26, 0.5);">
      <div class="container">
        <div class="section-title-wrap reveal-on-scroll">
          <span class="pill-badge"><span class="pill-dot"></span> Specialized Tracks</span>
          <h2 class="heading-lg">Industry-Grade <span class="text-gradient">Training Tracks</span></h2>
          <p class="subheading">Step into high-demand engineering roles with targeted curricula taught by experienced practitioners.</p>
        </div>

        <div class="bento-grid">
          <!-- Python -->
          <div class="col-4 reveal-on-scroll delay-1">
            <div class="border-glow-card">
              <div class="feature-icon-box">{ICONS['code']}</div>
              <h3 class="heading-sm" style="margin-bottom: 0.5rem;">Python Full Stack</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1.25rem;">
                Core syntax, Web Scraping (BeautifulSoup/Selenium), Data Analysis (Pandas), and Django/Flask backend APIs.
              </p>
              <div style="color: var(--primary-glow); font-size: 0.85rem; font-weight: 600; margin-bottom: 1.5rem;">Duration: 6 - 8 Weeks</div>
              <a href="python-training.html" class="btn btn-outline-emerald btn-sm" style="width: 100%;">View Track Details</a>
            </div>
          </div>

          <!-- MERN Stack -->
          <div class="col-4 reveal-on-scroll delay-2">
            <div class="border-glow-card">
              <div class="feature-icon-box">{ICONS['globe']}</div>
              <h3 class="heading-sm" style="margin-bottom: 0.5rem;">Full Stack MERN</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1.25rem;">
                Modern React, Node.js, Express, MongoDB, Tailwind CSS, REST APIs, and production deployment on Vercel/Netlify.
              </p>
              <div style="color: var(--primary-glow); font-size: 0.85rem; font-weight: 600; margin-bottom: 1.5rem;">Duration: 8 - 10 Weeks</div>
              <a href="full-stack-training.html" class="btn btn-outline-emerald btn-sm" style="width: 100%;">View Track Details</a>
            </div>
          </div>

          <!-- Cloud & DevOps -->
          <div class="col-4 reveal-on-scroll delay-3">
            <div class="border-glow-card">
              <div class="feature-icon-box">{ICONS['server']}</div>
              <h3 class="heading-sm" style="margin-bottom: 0.5rem;">Cloud Computing & DevOps</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1.25rem;">
                AWS EC2/S3/Lambda, Google Cloud, Docker containerization, Kubernetes cluster orchestration, and CI/CD pipelines.
              </p>
              <div style="color: var(--primary-glow); font-size: 0.85rem; font-weight: 600; margin-bottom: 1.5rem;">Duration: 8 Weeks</div>
              <a href="cloud-computing-training.html" class="btn btn-outline-emerald btn-sm" style="width: 100%;">View Track Details</a>
            </div>
          </div>

          <!-- AI & ML -->
          <div class="col-4 reveal-on-scroll delay-1">
            <div class="border-glow-card">
              <div class="feature-icon-box">{ICONS['brain']}</div>
              <h3 class="heading-sm" style="margin-bottom: 0.5rem;">AI & Machine Learning</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1.25rem;">
                Supervised/Unsupervised models, Neural Networks, Computer Vision with OpenCV, TensorFlow, and PyTorch deep learning.
              </p>
              <div style="color: var(--primary-glow); font-size: 0.85rem; font-weight: 600; margin-bottom: 1.5rem;">Duration: 8 - 10 Weeks</div>
              <a href="ai-training.html" class="btn btn-outline-emerald btn-sm" style="width: 100%;">View Track Details</a>
            </div>
          </div>

          <!-- Cybersecurity -->
          <div class="col-4 reveal-on-scroll delay-2">
            <div class="border-glow-card">
              <div class="feature-icon-box">{ICONS['shield']}</div>
              <h3 class="heading-sm" style="margin-bottom: 0.5rem;">Cybersecurity & Ethical Hacking</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1.25rem;">
                Kali Linux, Wireshark, Metasploit, OWASP Top 10 web vulnerabilities, SQLi/XSS defense, and CEH certification prep.
              </p>
              <div style="color: var(--primary-glow); font-size: 0.85rem; font-weight: 600; margin-bottom: 1.5rem;">Duration: 6 - 8 Weeks</div>
              <a href="cybersecurity-training.html" class="btn btn-outline-emerald btn-sm" style="width: 100%;">View Track Details</a>
            </div>
          </div>

          <!-- Data Science -->
          <div class="col-4 reveal-on-scroll delay-3">
            <div class="border-glow-card">
              <div class="feature-icon-box">{ICONS['database']}</div>
              <h3 class="heading-sm" style="margin-bottom: 0.5rem;">Data Science & Analytics</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1.25rem;">
                SQL databases, statistical modeling, data wrangling, Tableau & PowerBI dashboarding, and predictive intelligence.
              </p>
              <div style="color: var(--primary-glow); font-size: 0.85rem; font-weight: 600; margin-bottom: 1.5rem;">Duration: 8 Weeks</div>
              <a href="data-science-training.html" class="btn btn-outline-emerald btn-sm" style="width: 100%;">View Track Details</a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Student Achievements / Placement Hall of Fame -->
    <section class="section">
      <div class="container">
        <div class="section-title-wrap reveal-on-scroll">
          <span class="pill-badge"><span class="pill-dot"></span> Student Hall of Fame</span>
          <h2 class="heading-lg">Proven Real-World <span class="text-gradient">Student Success</span></h2>
          <p class="subheading">Our students don't just pass college vivas — they land lucrative corporate placements and publish peer-reviewed IEEE research.</p>
        </div>

        <div class="bento-grid">
          <!-- Achievement 1: Suriya -->
          <div class="col-4 reveal-on-scroll delay-1">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%; border-color: rgba(34, 197, 94, 0.4);">
              <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.25rem;">
                <div class="author-avatar">S</div>
                <div>
                  <h4 style="font-size: 1.1rem; color: #fff;">Suriya</h4>
                  <p style="color: var(--text-muted); font-size: 0.85rem;">Karpagam College of Engineering</p>
                </div>
              </div>
              <div style="background: rgba(16, 185, 129, 0.1); border-left: 3px solid var(--primary-neon); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1.25rem;">
                <strong style="color: var(--primary-neon); font-size: 0.9rem;">Achievement:</strong>
                <p style="color: #ffffff; font-weight: 600; font-size: 0.95rem;">Secured placement at TCS Digital with 7.5 LPA</p>
              </div>
              <p style="color: var(--text-muted); font-size: 0.875rem; margin-bottom: 1rem;">
                <strong>Project:</strong> AI-Powered Resume Screener
              </p>
              <div style="display: flex; gap: 0.4rem; flex-wrap: wrap;">
                <span class="pill-badge" style="font-size: 0.75rem; padding: 0.2rem 0.6rem; margin-bottom: 0;">Python</span>
                <span class="pill-badge" style="font-size: 0.75rem; padding: 0.2rem 0.6rem; margin-bottom: 0;">NLP</span>
                <span class="pill-badge" style="font-size: 0.75rem; padding: 0.2rem 0.6rem; margin-bottom: 0;">React</span>
              </div>
            </div>
          </div>

          <!-- Achievement 2: Vishal -->
          <div class="col-4 reveal-on-scroll delay-2">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%; border-color: rgba(34, 197, 94, 0.4);">
              <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.25rem;">
                <div class="author-avatar" style="background: linear-gradient(135deg, #3b82f6 0%, #06b6d4 100%);">V</div>
                <div>
                  <h4 style="font-size: 1.1rem; color: #fff;">Vishal</h4>
                  <p style="color: var(--text-muted); font-size: 0.85rem;">Thiagarajar Engineering College</p>
                </div>
              </div>
              <div style="background: rgba(16, 185, 129, 0.1); border-left: 3px solid var(--primary-neon); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1.25rem;">
                <strong style="color: var(--primary-neon); font-size: 0.9rem;">Achievement:</strong>
                <p style="color: #ffffff; font-weight: 600; font-size: 0.95rem;">Best Final Year Project Award 2023</p>
              </div>
              <p style="color: var(--text-muted); font-size: 0.875rem; margin-bottom: 1rem;">
                <strong>Project:</strong> E-Commerce Analytics Dashboard
              </p>
              <div style="display: flex; gap: 0.4rem; flex-wrap: wrap;">
                <span class="pill-badge" style="font-size: 0.75rem; padding: 0.2rem 0.6rem; margin-bottom: 0;">React</span>
                <span class="pill-badge" style="font-size: 0.75rem; padding: 0.2rem 0.6rem; margin-bottom: 0;">Node.js</span>
                <span class="pill-badge" style="font-size: 0.75rem; padding: 0.2rem 0.6rem; margin-bottom: 0;">MongoDB</span>
              </div>
            </div>
          </div>

          <!-- Achievement 3: Harsha -->
          <div class="col-4 reveal-on-scroll delay-3">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%; border-color: rgba(34, 197, 94, 0.4);">
              <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1.25rem;">
                <div class="author-avatar" style="background: linear-gradient(135deg, #8b5cf6 0%, #3b82f6 100%);">H</div>
                <div>
                  <h4 style="font-size: 1.1rem; color: #fff;">Harsha</h4>
                  <p style="color: var(--text-muted); font-size: 0.85rem;">Sri Eshwar College Of Engineering</p>
                </div>
              </div>
              <div style="background: rgba(16, 185, 129, 0.1); border-left: 3px solid var(--primary-neon); padding: 0.75rem 1rem; border-radius: 4px; margin-bottom: 1.25rem;">
                <strong style="color: var(--primary-neon); font-size: 0.9rem;">Achievement:</strong>
                <p style="color: #ffffff; font-weight: 600; font-size: 0.95rem;">Published paper in IEEE Journal</p>
              </div>
              <p style="color: var(--text-muted); font-size: 0.875rem; margin-bottom: 1rem;">
                <strong>Project:</strong> Smart Agriculture IoT System
              </p>
              <div style="display: flex; gap: 0.4rem; flex-wrap: wrap;">
                <span class="pill-badge" style="font-size: 0.75rem; padding: 0.2rem 0.6rem; margin-bottom: 0;">IoT</span>
                <span class="pill-badge" style="font-size: 0.75rem; padding: 0.2rem 0.6rem; margin-bottom: 0;">Python</span>
                <span class="pill-badge" style="font-size: 0.75rem; padding: 0.2rem 0.6rem; margin-bottom: 0;">AWS</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Testimonials & Write a Review CTA -->
    <section class="section" style="background: rgba(9, 14, 26, 0.5);">
      <div class="container">
        <div class="section-title-wrap reveal-on-scroll">
          <span class="pill-badge"><span class="pill-dot"></span> Testimonials</span>
          <h2 class="heading-lg">What Our <span class="text-gradient">Clients & Students Say</span></h2>
          <p class="subheading">Direct feedback from students who launched careers and businesses that scaled with our software.</p>
        </div>

        <div class="bento-grid" style="margin-bottom: 3rem;">
          <!-- Review 1: Rohan Sharma -->
          <div class="col-4 reveal-on-scroll delay-1">
            <div class="glass-panel testimonial-card" style="padding: 2.25rem;">
              <div>
                <div class="star-rating">{ICONS['star'] * 5}</div>
                <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.7; font-style: italic;">
                  "The web development internship at JM Vertex completely changed my career trajectory. The mentors are incredibly supportive and the hands-on projects gave me the confidence to ace my technical interviews."
                </p>
              </div>
              <div class="testimonial-author">
                <div class="author-avatar">R</div>
                <div>
                  <h4 style="font-size: 1rem; color: #fff;">Rohan Sharma</h4>
                  <p style="color: var(--text-dim); font-size: 0.8rem;">Sri Krishna College of Engineering • Student</p>
                  <span style="color: var(--primary-glow); font-size: 0.75rem;">Web Development Internship</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Review 2: Pizza Crave Team -->
          <div class="col-4 reveal-on-scroll delay-2">
            <div class="glass-panel testimonial-card" style="padding: 2.25rem;">
              <div>
                <div class="star-rating">{ICONS['star'] * 5}</div>
                <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.7; font-style: italic;">
                  "JM Vertex built our restaurant website (pizzacrave.in) faster than we expected. The design is modern, and the WhatsApp ordering integration has significantly boosted our direct sales without third-party commission fees."
                </p>
              </div>
              <div class="testimonial-author">
                <div class="author-avatar" style="background: linear-gradient(135deg, #f59e0b 0%, #ef4444 100%);">P</div>
                <div>
                  <h4 style="font-size: 1rem; color: #fff;">Pizza Crave Team</h4>
                  <p style="color: var(--text-dim); font-size: 0.8rem;">pizzacrave.in • Commercial Client</p>
                  <span style="color: var(--primary-glow); font-size: 0.75rem;">Website & Booking System</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Review 3: Sneha Patel -->
          <div class="col-4 reveal-on-scroll delay-3">
            <div class="glass-panel testimonial-card" style="padding: 2.25rem;">
              <div>
                <div class="star-rating">{ICONS['star'] * 5}</div>
                <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.7; font-style: italic;">
                  "Learning German felt intimidating at first, but the structured approach and interactive sessions made it so easy. I cleared my Goethe A1 certification on the very first attempt thanks to their exam drill tests!"
                </p>
              </div>
              <div class="testimonial-author">
                <div class="author-avatar" style="background: linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%);">S</div>
                <div>
                  <h4 style="font-size: 1rem; color: #fff;">Sneha Patel</h4>
                  <p style="color: var(--text-dim); font-size: 0.8rem;">PSG College of Technology • Student</p>
                  <span style="color: var(--primary-glow); font-size: 0.75rem;">German A1 Course</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div style="text-align: center;">
          <button class="btn btn-outline-emerald" onclick="openModal('review-modal')">
            ★ Write a Verified Review
          </button>
        </div>
      </div>
    </section>

    <!-- Founders & Leadership Section -->
    <section class="section">
      <div class="container">
        <div class="section-title-wrap reveal-on-scroll">
          <span class="pill-badge"><span class="pill-dot"></span> Leadership</span>
          <h2 class="heading-lg">Meet the <span class="text-gradient">Founding Team</span></h2>
          <p class="subheading">Direct mentorship from passionate tech leaders committed to delivering engineering excellence.</p>
        </div>

        <div class="bento-grid" style="max-width: 900px; margin: 0 auto;">
          <!-- Joshua J -->
          <div class="col-6 reveal-on-scroll delay-1">
            <div class="glass-panel founder-card tilt-card">
              <div class="tilt-inner">
                <div class="founder-avatar">JJ</div>
                <h3 class="heading-sm" style="font-size: 1.4rem; margin-bottom: 0.25rem;">Joshua J</h3>
                <p style="color: var(--primary-glow); font-weight: 600; font-size: 0.95rem; margin-bottom: 1rem;">Founder</p>
                <p style="color: var(--text-muted); font-size: 0.875rem; margin-bottom: 1.5rem;">
                  Leading product vision, technical architecture, and senior student project mentorship across AI, full stack systems, and software engineering.
                </p>
                <div class="founder-contact-actions">
                  <a href="tel:+919092737477" class="btn btn-secondary btn-sm">{ICONS['phone']} Call</a>
                  <a href="https://wa.me/919092737477" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp btn-sm">{ICONS['whatsapp']} WhatsApp</a>
                </div>
              </div>
            </div>
          </div>

          <!-- Madhav Adithya S -->
          <div class="col-6 reveal-on-scroll delay-2">
            <div class="glass-panel founder-card tilt-card">
              <div class="tilt-inner">
                <div class="founder-avatar" style="border-color: var(--accent-cyan);">MA</div>
                <h3 class="heading-sm" style="font-size: 1.4rem; margin-bottom: 0.25rem;">Madhav Adithya S</h3>
                <p style="color: var(--accent-cyan); font-weight: 600; font-size: 0.95rem; margin-bottom: 1rem;">Co-Founder</p>
                <p style="color: var(--text-muted); font-size: 0.875rem; margin-bottom: 1.5rem;">
                  Directing client partnerships, global language training frameworks, web development operations, and student career transitions.
                </p>
                <div class="founder-contact-actions">
                  <a href="tel:+919345699376" class="btn btn-secondary btn-sm">{ICONS['phone']} Call</a>
                  <a href="https://wa.me/919345699376" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp btn-sm">{ICONS['whatsapp']} WhatsApp</a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- FAQs Section -->
    <section class="section" style="background: rgba(9, 14, 26, 0.5);">
      <div class="container" style="max-width: 900px;">
        <div class="section-title-wrap reveal-on-scroll">
          <span class="pill-badge"><span class="pill-dot"></span> Common Questions</span>
          <h2 class="heading-lg">Frequently Asked <span class="text-gradient">Questions</span></h2>
          <p class="subheading">Everything you need to know about our services, student project processes, and training batches.</p>
        </div>

        <div class="reveal-on-scroll" style="display: flex; flex-direction: column; gap: 1rem;">
          <div class="glass-panel" style="padding: 1.5rem;">
            <h4 style="font-size: 1.1rem; color: #fff; margin-bottom: 0.5rem;">Do I need prior coding experience to join the internship training?</h4>
            <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6;">
              Not at all! Our training programs are designed from scratch. We begin with foundational programming principles and progressively advance to real-world frameworks, making it accessible and rewarding for beginners.
            </p>
          </div>

          <div class="glass-panel" style="padding: 1.5rem;">
            <h4 style="font-size: 1.1rem; color: #fff; margin-bottom: 0.5rem;">How much does a custom business website cost?</h4>
            <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6;">
              Website costs depend on functional complexity, features (such as online ordering, payment gateways, or custom admin dashboards), and page counts. We offer clear, transparent, highly competitive pricing tailored for startups and businesses.
            </p>
          </div>

          <div class="glass-panel" style="padding: 1.5rem;">
            <h4 style="font-size: 1.1rem; color: #fff; margin-bottom: 0.5rem;">Do you provide full source code and documentation for student projects?</h4>
            <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6;">
              Absolutely. For all custom academic projects, we provide complete, clean source code, GitHub repository access, architectural flowcharts, DFD/ER diagrams, and IEEE-format documentation reports.
            </p>
          </div>

          <div class="glass-panel" style="padding: 1.5rem;">
            <h4 style="font-size: 1.1rem; color: #fff; margin-bottom: 0.5rem;">Will I receive an industry-recognized certificate after completion?</h4>
            <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6;">
              Yes! Upon successful completion of your training modules and hands-on capstone project, you receive a verified certificate from JM Vertex Technologies along with letter of recommendation credentials.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Quick Lead Inquiry Form -->
    <section class="section">
      <div class="container" style="max-width: 800px;">
        <div class="glass-panel" style="padding: 3rem 2.5rem; border-color: rgba(34, 197, 94, 0.4);">
          <div class="text-center" style="margin-bottom: 2rem;">
            <span class="pill-badge"><span class="pill-dot"></span> Get Started</span>
            <h2 class="heading-md" style="margin-bottom: 0.5rem;">Ready to Build Something Extraordinary?</h2>
            <p style="color: var(--text-muted); font-size: 0.95rem;">
              Fill in your details and connect directly with our engineering mentors via WhatsApp within minutes.
            </p>
          </div>

          <form class="jm-inquiry-form">
            <input type="text" name="b_fax_code" style="display:none;" tabindex="-1" autocomplete="off">
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem; margin-bottom: 1.25rem;">
              <div class="form-group" style="margin-bottom:0;">
                <label class="form-label">Full Name *</label>
                <input type="text" name="name" class="input-glass" placeholder="John Doe" required>
              </div>
              <div class="form-group" style="margin-bottom:0;">
                <label class="form-label">WhatsApp Number *</label>
                <input type="tel" name="phone" class="input-glass" placeholder="+91 90927 37477" required>
              </div>
            </div>

            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem; margin-bottom: 1.25rem;">
              <div class="form-group" style="margin-bottom:0;">
                <label class="form-label">Email Address *</label>
                <input type="email" name="email" class="input-glass" placeholder="john@example.com" required>
              </div>
              <div class="form-group" style="margin-bottom:0;">
                <label class="form-label">Interested In *</label>
                <select name="interest" class="input-glass" style="background:#0d1527;" required>
                  <option value="Website Development">Website Development</option>
                  <option value="Final Year / Academic Project">Final Year / Academic Project</option>
                  <option value="Internship & Tech Training">Internship & Tech Training</option>
                  <option value="German Language Course">German Language Course</option>
                  <option value="Japanese Language Course">Japanese Language Course</option>
                </select>
              </div>
            </div>

            <div class="form-group">
              <label class="form-label">Your Message or Requirements</label>
              <textarea name="message" class="input-glass" placeholder="Tell us about your project requirements, deadline, or learning goals..."></textarea>
            </div>

            <button type="submit" class="btn btn-primary btn-lg" style="width: 100%;">
              Send Message & Connect on WhatsApp {ICONS['whatsapp']}
            </button>
          </form>
        </div>
      </div>
    </section>
    """

    footer = render_footer()
    write_page("index.html", head + header + body + footer)

build_index()
