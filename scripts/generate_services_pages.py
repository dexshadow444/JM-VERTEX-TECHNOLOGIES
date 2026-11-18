import html
from base_templates import render_head, render_header, render_footer, ICONS

# Helper to write page
def write_page(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated: {filename}")

# ==============================================================================
# 2. WEBSITE-DEVELOPMENT.HTML
# ==============================================================================
def build_webdev():
    head = render_head(
        "Premium Website & Web App Development | JM Vertex Technologies",
        "Custom, high-speed, SEO-optimized business websites, e-commerce stores, and web apps built with modern React, Vite, and Node.js. 90+ PageSpeed guarantee.",
        "website-development.html"
    )
    header = render_header("webdev")

    body = f"""
    <!-- Service Hero -->
    <section class="section section-hero">
      <div class="container text-center">
        <div class="reveal-on-scroll">
          <div class="pill-badge"><span class="pill-dot"></span> B2B Digital Engineering</div>
          <h1 class="heading-xl" style="margin-bottom: 1.5rem;">
            High-Performance <br>
            <span class="text-gradient">Websites That Drive Growth</span>
          </h1>
          <p class="subheading" style="margin-bottom: 2.5rem;">
            We build custom, blazing-fast, and highly scalable web applications engineered to turn casual visitors into loyal customers. No sluggish templates — just pure, precision-coded speed.
          </p>
          <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
            <a href="https://wa.me/919092737477?text=Hi%20JM%20Vertex,%20I%20need%20a%20website%20development%20quote." target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg">
              Get a Free Quote {ICONS['arrow_right']}
            </a>
            <a href="portfolio.html" class="btn btn-secondary btn-lg">
              View Our Work
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- Value Props (Bento Grid) -->
    <section class="section" style="background: rgba(9, 14, 26, 0.5);">
      <div class="container">
        <div class="section-title-wrap reveal-on-scroll">
          <span class="pill-badge"><span class="pill-dot"></span> Core Advantages</span>
          <h2 class="heading-lg">Why Leading Businesses <span class="text-gradient">Choose JM Vertex</span></h2>
          <p class="subheading">Engineered from the ground up for maximum conversion, rock-solid security, and search engine dominance.</p>
        </div>

        <div class="bento-grid">
          <div class="col-4 reveal-on-scroll delay-1">
            <div class="glass-panel tilt-card" style="padding: 2.25rem;">
              <div class="tilt-inner">
                <div class="feature-icon-box">{ICONS['code']}</div>
                <h3 class="heading-sm" style="margin-bottom: 0.5rem;">Modern Tech Stacks</h3>
                <p style="color: var(--text-muted); font-size: 0.9rem;">
                  Built using React, Vite, Next.js, and Node.js. Single Page Applications that load instantaneously without lag or clunky reloads.
                </p>
              </div>
            </div>
          </div>

          <div class="col-4 reveal-on-scroll delay-2">
            <div class="glass-panel tilt-card" style="padding: 2.25rem;">
              <div class="tilt-inner">
                <div class="feature-icon-box">{ICONS['globe']}</div>
                <h3 class="heading-sm" style="margin-bottom: 0.5rem;">Ultra-Responsive UX</h3>
                <p style="color: var(--text-muted); font-size: 0.9rem;">
                  Pixel-perfect rendering across all devices — smartphones, tablets, laptops, and ultra-wide screens — designed with touch-first fluidity.
                </p>
              </div>
            </div>
          </div>

          <div class="col-4 reveal-on-scroll delay-3">
            <div class="glass-panel tilt-card" style="padding: 2.25rem;">
              <div class="tilt-inner">
                <div class="feature-icon-box">{ICONS['shield']}</div>
                <h3 class="heading-sm" style="margin-bottom: 0.5rem;">Advanced SEO & Security</h3>
                <p style="color: var(--text-muted); font-size: 0.9rem;">
                  Structured Schema.org data, Open Graph tags, canonical optimization, SSL integration, and CSP protection against XSS vulnerabilities.
                </p>
              </div>
            </div>
          </div>

          <div class="col-4 reveal-on-scroll delay-1">
            <div class="glass-panel tilt-card" style="padding: 2.25rem;">
              <div class="tilt-inner">
                <div class="feature-icon-box">{ICONS['server']}</div>
                <h3 class="heading-sm" style="margin-bottom: 0.5rem;">90+ PageSpeed Scores</h3>
                <p style="color: var(--text-muted); font-size: 0.9rem;">
                  Optimized assets, dynamic code splitting, WebP image formats, and edge caching for sub-second first-contentful paint.
                </p>
              </div>
            </div>
          </div>

          <div class="col-4 reveal-on-scroll delay-2">
            <div class="glass-panel tilt-card" style="padding: 2.25rem;">
              <div class="tilt-inner">
                <div class="feature-icon-box">{ICONS['whatsapp']}</div>
                <h3 class="heading-sm" style="margin-bottom: 0.5rem;">Direct WhatsApp Ordering</h3>
                <p style="color: var(--text-muted); font-size: 0.9rem;">
                  Ideal for restaurants, boutiques, and clinics: let customers order directly into your WhatsApp inbox without paying aggregator commissions.
                </p>
              </div>
            </div>
          </div>

          <div class="col-4 reveal-on-scroll delay-3">
            <div class="glass-panel tilt-card" style="padding: 2.25rem;">
              <div class="tilt-inner">
                <div class="feature-icon-box">{ICONS['database']}</div>
                <h3 class="heading-sm" style="margin-bottom: 0.5rem;">Scalable Cloud Backend</h3>
                <p style="color: var(--text-muted); font-size: 0.9rem;">
                  Custom admin dashboards, secure REST API integrations, payment gateways (Stripe, Razorpay), and database management.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Development Process Steps -->
    <section class="section">
      <div class="container">
        <div class="section-title-wrap reveal-on-scroll">
          <span class="pill-badge"><span class="pill-dot"></span> Structured Workflow</span>
          <h2 class="heading-lg">Our 4-Stage <span class="text-gradient">Engineering Process</span></h2>
          <p class="subheading">From wireframe conception to high-traffic deployment.</p>
        </div>

        <div class="bento-grid">
          <div class="col-3 reveal-on-scroll delay-1">
            <div class="stat-card" style="text-align: left; height: 100%;">
              <span style="font-size: 2.5rem; font-weight: 800; color: var(--primary-glow); display:block; margin-bottom: 0.5rem;">01</span>
              <h4 style="color:#fff; font-size: 1.15rem; margin-bottom: 0.5rem;">UI/UX Prototyping</h4>
              <p style="color: var(--text-muted); font-size: 0.875rem;">Figma wireframes, design systems, and responsive interactive mockups tailored to your brand identity.</p>
            </div>
          </div>

          <div class="col-3 reveal-on-scroll delay-2">
            <div class="stat-card" style="text-align: left; height: 100%;">
              <span style="font-size: 2.5rem; font-weight: 800; color: var(--primary-glow); display:block; margin-bottom: 0.5rem;">02</span>
              <h4 style="color:#fff; font-size: 1.15rem; margin-bottom: 0.5rem;">Frontend & Backend</h4>
              <p style="color: var(--text-muted); font-size: 0.875rem;">Clean, modular React/Node.js coding adhering to strict security and performance standards.</p>
            </div>
          </div>

          <div class="col-3 reveal-on-scroll delay-3">
            <div class="stat-card" style="text-align: left; height: 100%;">
              <span style="font-size: 2.5rem; font-weight: 800; color: var(--primary-glow); display:block; margin-bottom: 0.5rem;">03</span>
              <h4 style="color:#fff; font-size: 1.15rem; margin-bottom: 0.5rem;">Testing & QA</h4>
              <p style="color: var(--text-muted); font-size: 0.875rem;">Cross-browser testing, mobile device audits, security vulnerability checks, and load optimization.</p>
            </div>
          </div>

          <div class="col-3 reveal-on-scroll delay-4">
            <div class="stat-card" style="text-align: left; height: 100%;">
              <span style="font-size: 2.5rem; font-weight: 800; color: var(--primary-glow); display:block; margin-bottom: 0.5rem;">04</span>
              <h4 style="color:#fff; font-size: 1.15rem; margin-bottom: 0.5rem;">Deployment & SEO</h4>
              <p style="color: var(--text-muted); font-size: 0.875rem;">Global CDN edge deployment, SSL provisioning, Google Search Console indexing, and launch.</p>
            </div>
          </div>
        </div>

        <div style="text-align: center; margin-top: 3.5rem;">
          <a href="https://wa.me/919092737477?text=Hi%20JM%20Vertex,%20I%20want%20to%20start%20my%20website%20project." target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp btn-lg">
            {ICONS['whatsapp']} Schedule Free Web Consultation
          </a>
        </div>
      </div>
    </section>
    """
    footer = render_footer()
    write_page("website-development.html", head + header + body + footer)

# ==============================================================================
# 3. STUDENT-PROJECTS.HTML
# ==============================================================================
def build_student_projects():
    head = render_head(
        "Final Year & IEEE Student Projects | JM Vertex Technologies",
        "Comprehensive final year and mini academic project guidance for engineering students. IEEE paper implementations, source code, report documentation, and viva prep.",
        "student-projects.html"
    )
    header = render_header("projects")

    body = f"""
    <!-- Student Projects Hero -->
    <section class="section section-hero">
      <div class="container text-center">
        <div class="reveal-on-scroll">
          <div class="pill-badge"><span class="pill-dot"></span> Academic Engineering Excellence</div>
          <h1 class="heading-xl" style="margin-bottom: 1.5rem;">
            IEEE Standard Final Year & <br>
            <span class="text-gradient">Custom Student Projects</span>
          </h1>
          <p class="subheading" style="margin-bottom: 2.5rem;">
            Don't just purchase a ready-made project — master how it works with senior engineers. We provide IEEE base paper code, complete thesis reports, architecture diagrams, and 1-on-1 viva preparation.
          </p>
          <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
            <a href="project-categories.html" class="btn btn-primary btn-lg">
              Browse Project Domains {ICONS['arrow_right']}
            </a>
            <a href="https://wa.me/919092737477?text=Hi%20JM%20Vertex,%20I%20need%20guidance%20for%20my%20final%20year%20project." target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp btn-lg">
              {ICONS['whatsapp']} Get Abstract Approved Today
            </a>
          </div>
        </div>
      </div>
    </section>

    <!-- What You Get Section -->
    <section class="section" style="background: rgba(9, 14, 26, 0.5);">
      <div class="container">
        <div class="section-title-wrap reveal-on-scroll">
          <span class="pill-badge"><span class="pill-dot"></span> Full Package</span>
          <h2 class="heading-lg">Everything Included in <span class="text-gradient">Every Student Project</span></h2>
          <p class="subheading">Zero stress, complete transparency, and guaranteed university approval.</p>
        </div>

        <div class="bento-grid">
          <div class="col-4 reveal-on-scroll delay-1">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%;">
              <div class="feature-icon-box">{ICONS['code']}</div>
              <h3 class="heading-sm" style="margin-bottom: 0.5rem;">Complete Clean Source Code</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem;">
                Fully commented, industry-standard code repository with installation scripts, environment configuration files, and zero hidden bugs.
              </p>
            </div>
          </div>

          <div class="col-4 reveal-on-scroll delay-2">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%;">
              <div class="feature-icon-box">{ICONS['book']}</div>
              <h3 class="heading-sm" style="margin-bottom: 0.5rem;">Full University Documentation</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem;">
                Comprehensive project reports formatted to your university's guidelines, complete with DFD, UML, ER diagrams, literature surveys, and test results.
              </p>
            </div>
          </div>

          <div class="col-4 reveal-on-scroll delay-3">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%;">
              <div class="feature-icon-box">{ICONS['grad']}</div>
              <h3 class="heading-sm" style="margin-bottom: 0.5rem;">Live Viva & Demo Mentorship</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem;">
                Step-by-step code walkthroughs. We train you on every line of code so you can confidently explain the algorithm and answer any external examiner question.
              </p>
            </div>
          </div>

          <div class="col-4 reveal-on-scroll delay-1">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%;">
              <div class="feature-icon-box">{ICONS['shield']}</div>
              <h3 class="heading-sm" style="margin-bottom: 0.5rem;">IEEE Base Papers</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem;">
                Implementations based on authentic, peer-reviewed IEEE research papers from recent conference publications to ensure academic credibility.
              </p>
            </div>
          </div>

          <div class="col-4 reveal-on-scroll delay-2">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%;">
              <div class="feature-icon-box">{ICONS['cpu']}</div>
              <h3 class="heading-sm" style="margin-bottom: 0.5rem;">Hardware & IoT Components</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem;">
                For ECE, EEE, and Mechatronics students: circuit schematics, Raspberry Pi/Arduino code, sensor interfacing, and cloud IoT dashboard setup.
              </p>
            </div>
          </div>

          <div class="col-4 reveal-on-scroll delay-3">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%;">
              <div class="feature-icon-box">{ICONS['star']}</div>
              <h3 class="heading-sm" style="margin-bottom: 0.5rem;">Publication Support</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem;">
                Assistance with converting your project findings into research manuscripts for publishing in reputed UGC-CARE or Scopus journals.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Student Project Domains Teaser -->
    <section class="section">
      <div class="container text-center">
        <div class="glass-panel" style="padding: 3.5rem 2rem; max-width: 900px; margin: 0 auto; border-color: rgba(34, 197, 94, 0.4);">
          <span class="pill-badge"><span class="pill-dot"></span> Diverse Domains</span>
          <h2 class="heading-md" style="margin-bottom: 1rem;">Choose from 50+ Trending Project Topics</h2>
          <p style="color: var(--text-muted); font-size: 1rem; max-width: 650px; margin: 0 auto 2rem;">
            We guide projects across Artificial Intelligence, Deep Learning, Blockchain, Cybersecurity, Cloud Systems, and Full Stack Web.
          </p>
          <a href="project-categories.html" class="btn btn-primary btn-lg">
            Explore All Project Categories {ICONS['arrow_right']}
          </a>
        </div>
      </div>
    </section>
    """
    footer = render_footer()
    write_page("student-projects.html", head + header + body + footer)

# ==============================================================================
# 4. PROJECT-CATEGORIES.HTML
# ==============================================================================
def build_project_categories():
    head = render_head(
        "Student Project Categories & IEEE Domains | JM Vertex Technologies",
        "Browse our extensive catalog of IEEE final year project domains: AI/ML, Full Stack Web, Data Science, IoT, Cloud Computing, and Cybersecurity.",
        "project-categories.html"
    )
    header = render_header("projects")

    body = f"""
    <section class="section section-hero">
      <div class="container text-center">
        <div class="reveal-on-scroll">
          <div class="pill-badge"><span class="pill-dot"></span> IEEE Catalog</div>
          <h1 class="heading-xl" style="margin-bottom: 1.5rem;">
            Student Project <br>
            <span class="text-gradient">Categories & Domains</span>
          </h1>
          <p class="subheading" style="margin-bottom: 2.5rem;">
            Explore approved base papers and trending technical domains for B.E., B.Tech, M.E., MCA, and MSc academic requirements.
          </p>
        </div>
      </div>
    </section>

    <section class="section" style="padding-top: 0;">
      <div class="container">
        <div class="bento-grid">
          <!-- AI & ML -->
          <div class="col-4 reveal-on-scroll delay-1">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%;">
              <div class="feature-icon-box">{ICONS['brain']}</div>
              <h3 class="heading-sm" style="margin-bottom: 0.75rem;">AI & Machine Learning</h3>
              <ul style="list-style: none; color: var(--text-muted); font-size: 0.875rem; display: flex; flex-direction: column; gap: 0.5rem; margin-bottom: 1.5rem;">
                <li>• Medical Image Diagnosis (CNNs / X-Ray / MRI)</li>
                <li>• Fake News & Sentiment Analysis using NLP</li>
                <li>• Predictive Stock & Financial Time Series (LSTM)</li>
                <li>• Autonomous Vehicle Obstacle Avoidance</li>
              </ul>
              <a href="https://wa.me/919092737477?text=Hi%20JM%20Vertex,%20I%20am%20interested%20in%20an%20AI/ML%20project." target="_blank" rel="noopener noreferrer" class="btn btn-outline-emerald btn-sm" style="width:100%;">Select AI Domain</a>
            </div>
          </div>

          <!-- Full Stack Web -->
          <div class="col-4 reveal-on-scroll delay-2">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%;">
              <div class="feature-icon-box">{ICONS['code']}</div>
              <h3 class="heading-sm" style="margin-bottom: 0.75rem;">Full Stack Web Systems</h3>
              <ul style="list-style: none; color: var(--text-muted); font-size: 0.875rem; display: flex; flex-direction: column; gap: 0.5rem; margin-bottom: 1.5rem;">
                <li>• Telehealth Remote Patient Monitoring Portal</li>
                <li>• AI-Integrated Multi-Vendor E-Commerce Engine</li>
                <li>• College ERP & Automated Exam Proctoring System</li>
                <li>• Microservices-based Supply Chain Manager</li>
              </ul>
              <a href="https://wa.me/919092737477?text=Hi%20JM%20Vertex,%20I%20am%20interested%20in%20a%20Web%20Dev%20project." target="_blank" rel="noopener noreferrer" class="btn btn-outline-emerald btn-sm" style="width:100%;">Select Web Domain</a>
            </div>
          </div>

          <!-- Cybersecurity & Blockchain -->
          <div class="col-4 reveal-on-scroll delay-3">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%;">
              <div class="feature-icon-box">{ICONS['shield']}</div>
              <h3 class="heading-sm" style="margin-bottom: 0.75rem;">Cybersecurity & Blockchain</h3>
              <ul style="list-style: none; color: var(--text-muted); font-size: 0.875rem; display: flex; flex-direction: column; gap: 0.5rem; margin-bottom: 1.5rem;">
                <li>• Decentralized E-Voting System with Ethereum</li>
                <li>• Zero-Knowledge Proof Authentication Protocol</li>
                <li>• Network Intrusion Detection using Random Forest</li>
                <li>• Secure File Sharing with End-to-End Cryptography</li>
              </ul>
              <a href="https://wa.me/919092737477?text=Hi%20JM%20Vertex,%20I%20am%20interested%20in%20a%20Security/Blockchain%20project." target="_blank" rel="noopener noreferrer" class="btn btn-outline-emerald btn-sm" style="width:100%;">Select Security Domain</a>
            </div>
          </div>

          <!-- IoT & Embedded Systems -->
          <div class="col-4 reveal-on-scroll delay-1">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%;">
              <div class="feature-icon-box">{ICONS['cpu']}</div>
              <h3 class="heading-sm" style="margin-bottom: 0.75rem;">IoT & Smart Hardware</h3>
              <ul style="list-style: none; color: var(--text-muted); font-size: 0.875rem; display: flex; flex-direction: column; gap: 0.5rem; margin-bottom: 1.5rem;">
                <li>• Smart Agriculture & Automated Irrigation IoT</li>
                <li>• Industrial Sensor Anomaly Detection System</li>
                <li>• Smart Energy Metering with Cloud Telemetry</li>
                <li>• Wearable Health Monitoring Band with LoRaWAN</li>
              </ul>
              <a href="https://wa.me/919092737477?text=Hi%20JM%20Vertex,%20I%20am%20interested%20in%20an%20IoT%20project." target="_blank" rel="noopener noreferrer" class="btn btn-outline-emerald btn-sm" style="width:100%;">Select IoT Domain</a>
            </div>
          </div>

          <!-- Cloud & DevOps -->
          <div class="col-4 reveal-on-scroll delay-2">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%;">
              <div class="feature-icon-box">{ICONS['server']}</div>
              <h3 class="heading-sm" style="margin-bottom: 0.75rem;">Cloud & Big Data</h3>
              <ul style="list-style: none; color: var(--text-muted); font-size: 0.875rem; display: flex; flex-direction: column; gap: 0.5rem; margin-bottom: 1.5rem;">
                <li>• Serverless Real-Time Data Streaming Pipeline</li>
                <li>• Kubernetes Multi-Cloud Load Balancer Simulation</li>
                <li>• Customer Churn Prediction on Large Datasets</li>
                <li>• Automated CI/CD Vulnerability Scanner</li>
              </ul>
              <a href="https://wa.me/919092737477?text=Hi%20JM%20Vertex,%20I%20am%20interested%20in%20a%20Cloud/Big%20Data%20project." target="_blank" rel="noopener noreferrer" class="btn btn-outline-emerald btn-sm" style="width:100%;">Select Cloud Domain</a>
            </div>
          </div>

          <!-- Custom Requirement -->
          <div class="col-4 reveal-on-scroll delay-3">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%; border-color: rgba(34, 197, 94, 0.4);">
              <div class="feature-icon-box">{ICONS['star']}</div>
              <h3 class="heading-sm" style="margin-bottom: 0.75rem;">Have Your Own Topic?</h3>
              <p style="color: var(--text-muted); font-size: 0.875rem; line-height: 1.6; margin-bottom: 1.5rem;">
                Already have a base paper or college-assigned topic? Send it over to our mentors. We will evaluate its technical scope and guide you to completion.
              </p>
              <a href="https://wa.me/919092737477?text=Hi%20JM%20Vertex,%20I%20have%20my%20own%20project%20topic%20to%20discuss." target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp btn-sm" style="width:100%;">{ICONS['whatsapp']} Send Your Topic</a>
            </div>
          </div>
        </div>
      </div>
    </section>
    """
    footer = render_footer()
    write_page("project-categories.html", head + header + body + footer)

# ==============================================================================
# 5. INTERNSHIP-TRAINING.HTML
# ==============================================================================
def build_internship():
    head = render_head(
        "Tech Internship Training Programs | JM Vertex Technologies",
        "Hands-on internship training in Python, Full Stack MERN, Cloud Computing, AI/ML, and Cybersecurity. Real projects and verified certification.",
        "internship-training.html"
    )
    header = render_header("training")

    body = f"""
    <section class="section section-hero">
      <div class="container text-center">
        <div class="reveal-on-scroll">
          <div class="pill-badge"><span class="pill-dot"></span> Career Accelerator</div>
          <h1 class="heading-xl" style="margin-bottom: 1.5rem;">
            Industry-Driven Tech <br>
            <span class="text-gradient">Internships & Training</span>
          </h1>
          <p class="subheading" style="margin-bottom: 2.5rem;">
            Bridge the gap between academic theory and enterprise engineering. Build real-world production projects, earn verified credentials, and accelerate your career.
          </p>
          <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
            <a href="https://wa.me/919092737477?text=Hi%20JM%20Vertex,%20I%20want%20to%20enroll%20in%20an%20internship%20batch." target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg">
              Apply for Next Batch {ICONS['arrow_right']}
            </a>
            <button class="btn btn-secondary btn-lg" onclick="openModal('syllabus-modal')">
              {ICONS['download']} Download Syllabus
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Training Programs Grid -->
    <section class="section" style="background: rgba(9, 14, 26, 0.5);">
      <div class="container">
        <div class="section-title-wrap reveal-on-scroll">
          <span class="pill-badge"><span class="pill-dot"></span> Available Programs</span>
          <h2 class="heading-lg">Choose Your <span class="text-gradient">Learning Path</span></h2>
          <p class="subheading">Intensive, mentor-guided cohorts with 100% practical lab assignments.</p>
        </div>

        <div class="bento-grid">
          <!-- Python -->
          <div class="col-4 reveal-on-scroll delay-1">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%;">
              <div class="feature-icon-box">{ICONS['code']}</div>
              <h3 class="heading-sm" style="margin-bottom: 0.5rem;">Python Full Stack</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1.25rem;">
                Variables, OOP, Web Scraping, Pandas, NumPy, Django, and REST APIs.
              </p>
              <div style="color: var(--primary-glow); font-size: 0.85rem; font-weight: 600; margin-bottom: 1.5rem;">Duration: 6 - 8 Weeks</div>
              <a href="python-training.html" class="btn btn-outline-emerald btn-sm" style="width: 100%;">View Full Syllabus</a>
            </div>
          </div>

          <!-- MERN -->
          <div class="col-4 reveal-on-scroll delay-2">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%;">
              <div class="feature-icon-box">{ICONS['globe']}</div>
              <h3 class="heading-sm" style="margin-bottom: 0.5rem;">Full Stack MERN</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1.25rem;">
                React 19, Node.js, Express, MongoDB, Tailwind, and full CRUD web applications.
              </p>
              <div style="color: var(--primary-glow); font-size: 0.85rem; font-weight: 600; margin-bottom: 1.5rem;">Duration: 8 - 10 Weeks</div>
              <a href="full-stack-training.html" class="btn btn-outline-emerald btn-sm" style="width: 100%;">View Full Syllabus</a>
            </div>
          </div>

          <!-- Cloud & DevOps -->
          <div class="col-4 reveal-on-scroll delay-3">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%;">
              <div class="feature-icon-box">{ICONS['server']}</div>
              <h3 class="heading-sm" style="margin-bottom: 0.5rem;">Cloud Computing & DevOps</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1.25rem;">
                AWS EC2/S3/IAM, Docker containers, Kubernetes clusters, and automated CI/CD.
              </p>
              <div style="color: var(--primary-glow); font-size: 0.85rem; font-weight: 600; margin-bottom: 1.5rem;">Duration: 8 Weeks</div>
              <a href="cloud-computing-training.html" class="btn btn-outline-emerald btn-sm" style="width: 100%;">View Full Syllabus</a>
            </div>
          </div>

          <!-- AI & ML -->
          <div class="col-4 reveal-on-scroll delay-1">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%;">
              <div class="feature-icon-box">{ICONS['brain']}</div>
              <h3 class="heading-sm" style="margin-bottom: 0.5rem;">AI & Machine Learning</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1.25rem;">
                Scikit-Learn, TensorFlow, Neural Networks, Computer Vision, and NLP.
              </p>
              <div style="color: var(--primary-glow); font-size: 0.85rem; font-weight: 600; margin-bottom: 1.5rem;">Duration: 8 - 10 Weeks</div>
              <a href="ai-training.html" class="btn btn-outline-emerald btn-sm" style="width: 100%;">View Full Syllabus</a>
            </div>
          </div>

          <!-- Cybersecurity -->
          <div class="col-4 reveal-on-scroll delay-2">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%;">
              <div class="feature-icon-box">{ICONS['shield']}</div>
              <h3 class="heading-sm" style="margin-bottom: 0.5rem;">Cybersecurity & Pentesting</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1.25rem;">
                Kali Linux, Wireshark, OWASP Top 10, Ethical Hacking, and CEH foundation.
              </p>
              <div style="color: var(--primary-glow); font-size: 0.85rem; font-weight: 600; margin-bottom: 1.5rem;">Duration: 6 - 8 Weeks</div>
              <a href="cybersecurity-training.html" class="btn btn-outline-emerald btn-sm" style="width: 100%;">View Full Syllabus</a>
            </div>
          </div>

          <!-- Data Science -->
          <div class="col-4 reveal-on-scroll delay-3">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%;">
              <div class="feature-icon-box">{ICONS['database']}</div>
              <h3 class="heading-sm" style="margin-bottom: 0.5rem;">Data Science & Analytics</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 1.25rem;">
                SQL query optimization, Tableau dashboards, predictive modeling, and business insights.
              </p>
              <div style="color: var(--primary-glow); font-size: 0.85rem; font-weight: 600; margin-bottom: 1.5rem;">Duration: 8 Weeks</div>
              <a href="data-science-training.html" class="btn btn-outline-emerald btn-sm" style="width: 100%;">View Full Syllabus</a>
            </div>
          </div>
        </div>
      </div>
    </section>
    """
    footer = render_footer()
    write_page("internship-training.html", head + header + body + footer)

build_webdev()
build_student_projects()
build_project_categories()
build_internship()
