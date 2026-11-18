import html
from base_templates import render_head, render_header, render_footer, ICONS

def write_page(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated: {filename}")

# ==============================================================================
# CONTACT.HTML
# ==============================================================================
def build_contact():
    head = render_head(
        "Contact Us | JM Vertex Technologies",
        "Get in touch with JM Vertex Technologies for website development, student final year projects, technical internships, and German/Japanese language classes.",
        "contact.html"
    )
    header = render_header("contact")

    body = f"""
    <section class="section section-hero">
      <div class="container text-center">
        <div class="reveal-on-scroll">
          <div class="pill-badge"><span class="pill-dot"></span> Get In Touch</div>
          <h1 class="heading-xl" style="margin-bottom: 1.5rem;">
            Let's Engineer Your <br>
            <span class="text-gradient">Next Big Achievement</span>
          </h1>
          <p class="subheading" style="margin-bottom: 2.5rem;">
            Whether you are a startup needing a custom web application or an engineering student looking for IEEE project mentorship, we are here to assist you.
          </p>
        </div>
      </div>
    </section>

    <section class="section" style="padding-top: 0;">
      <div class="container">
        <div class="bento-grid">
          <!-- Col 1: Direct Contact Information -->
          <div class="col-5 reveal-on-scroll delay-1">
            <div class="glass-panel" style="padding: 2.75rem 2rem; height: 100%; display: flex; flex-direction: column; justify-content: space-between;">
              <div>
                <h3 class="heading-sm" style="font-size: 1.35rem; margin-bottom: 1rem; color: #fff;">Direct Communication</h3>
                <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6; margin-bottom: 2rem;">
                  Reach out directly to our founders or message our official WhatsApp support desk for rapid 15-minute response times.
                </p>

                <div class="contact-list-wrap">
                  <!-- Phone 1: Joshua J -->
                  <div class="contact-card-item">
                    <div class="contact-icon-box">
                      {ICONS['phone']}
                    </div>
                    <div class="contact-info">
                      <strong class="contact-name">Joshua J (Founder)</strong>
                      <a href="tel:+919092737477" class="contact-link">+91 90927 37477</a>
                    </div>
                  </div>

                  <!-- Phone 2: Madhav Adithya S -->
                  <div class="contact-card-item">
                    <div class="contact-icon-box">
                      {ICONS['phone']}
                    </div>
                    <div class="contact-info">
                      <strong class="contact-name">Madhav Adithya S (Co-Founder)</strong>
                      <a href="tel:+919345699376" class="contact-link">+91 93456 99376</a>
                    </div>
                  </div>

                  <!-- Email -->
                  <div class="contact-card-item">
                    <div class="contact-icon-box">
                      {ICONS['mail']}
                    </div>
                    <div class="contact-info">
                      <strong class="contact-name">Official Email</strong>
                      <a href="mailto:jmvertextechnologies2025@gmail.com" class="contact-link">jmvertextechnologies2025@gmail.com</a>
                    </div>
                  </div>

                  <!-- WhatsApp Instant Link -->
                  <div class="contact-card-item">
                    <div class="contact-icon-box whatsapp-icon">
                      {ICONS['whatsapp']}
                    </div>
                    <div class="contact-info">
                      <strong class="contact-name">WhatsApp Business</strong>
                      <a href="https://wa.me/919092737477?text=Hi%20JM%20Vertex,%20I%20have%20an%20inquiry." target="_blank" rel="noopener noreferrer" class="contact-link" style="color: #25d366;">Chat with Engineering Team →</a>
                    </div>
                  </div>
                </div>
              </div>

              <div style="margin-top: 2.5rem; padding-top: 1.5rem; border-top: 1px solid rgba(255,255,255,0.06);">
                <p style="color: var(--text-dim); font-size: 0.85rem;">
                  📍 Serving startups, universities, and students across India and globally.
                </p>
              </div>
            </div>
          </div>

          <!-- Col 2: Interactive Contact Form -->
          <div class="col-7 reveal-on-scroll delay-2">
            <div class="glass-panel" style="padding: 2.75rem 2.5rem; border-color: rgba(34, 197, 94, 0.4);">
              <h3 class="heading-sm" style="font-size: 1.35rem; margin-bottom: 0.5rem; color: #fff;">Send an Inquiry</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem; margin-bottom: 2rem;">
                Submit your project specifications or questions. You will also get an instant WhatsApp direct connect.
              </p>

              <form class="jm-inquiry-form">
                <input type="text" name="b_fax_code" style="display:none;" tabindex="-1" autocomplete="off">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem; margin-bottom: 1.25rem;">
                  <div class="form-group" style="margin-bottom:0;">
                    <label class="form-label">Full Name *</label>
                    <input type="text" name="name" class="input-glass" placeholder="Your Name" required>
                  </div>
                  <div class="form-group" style="margin-bottom:0;">
                    <label class="form-label">WhatsApp Number *</label>
                    <input type="tel" name="phone" class="input-glass" placeholder="+91 90927 37477" required>
                  </div>
                </div>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem; margin-bottom: 1.25rem;">
                  <div class="form-group" style="margin-bottom:0;">
                    <label class="form-label">Email Address *</label>
                    <input type="email" name="email" class="input-glass" placeholder="you@domain.com" required>
                  </div>
                  <div class="form-group" style="margin-bottom:0;">
                    <label class="form-label">Service Required *</label>
                    <select name="interest" class="input-glass" style="background:#0d1527;" required>
                      <option value="Website Development">Website Development</option>
                      <option value="Student Final Year Project">Student Final Year Project</option>
                      <option value="Tech Internship & Training">Tech Internship & Training</option>
                      <option value="German Language Course">German Language Course</option>
                      <option value="Japanese Language Course">Japanese Language Course</option>
                      <option value="General Query">General Query</option>
                    </select>
                  </div>
                </div>

                <div class="form-group">
                  <label class="form-label">Message / Project Details *</label>
                  <textarea name="message" class="input-glass" placeholder="Please describe your requirements, college deadlines, tech stack preferences, or training batch questions..." required></textarea>
                </div>

                <button type="submit" class="btn btn-primary btn-lg" style="width: 100%;">
                  Submit Message & Connect via WhatsApp {ICONS['whatsapp']}
                </button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>
    """
    footer = render_footer()
    write_page("contact.html", head + header + body + footer)

# ==============================================================================
# PRIVACY POLICY & TERMS
# ==============================================================================
def build_privacy_policy():
    head = render_head(
        "Privacy & Data Protection Policy | JM Vertex Technologies",
        "Official privacy policy of JM Vertex Technologies detailing user data handling, confidentiality, and security measures.",
        "privacy-policy.html"
    )
    header = render_header("")

    body = f"""
    <section class="section" style="padding-top: 9rem; min-height: 80vh;">
      <div class="container" style="max-width: 900px;">
        <span class="pill-badge"><span class="pill-dot"></span> Compliance</span>
        <h1 class="heading-lg" style="margin-bottom: 1.5rem;">Privacy & Data Protection Policy</h1>
        <p style="color: var(--text-dim); margin-bottom: 2.5rem;">Last Updated: 2026</p>

        <div class="glass-panel" style="padding: 3rem 2.5rem; line-height: 1.8; color: #cbd5e1;">
          <h3 style="color:#fff; margin-bottom: 0.75rem;">1. Commitment to Security & Privacy</h3>
          <p style="margin-bottom: 1.5rem;">
            At JM Vertex Technologies ("we", "us", or "our"), data privacy and integrity are fundamental to our engineering ethics. This policy explains how we collect, store, and safeguard your personal information when you visit our website, enroll in training courses, or commission software development.
          </p>

          <h3 style="color:#fff; margin-bottom: 0.75rem;">2. Information We Collect</h3>
          <p style="margin-bottom: 1.5rem;">
            We collect personal contact details (such as your full name, email address, phone/WhatsApp number, and college/organization name) strictly when you submit an inquiry, download syllabus documents, or enroll in a mentorship cohort. We do not sell, rent, or lease this information to third-party advertisers.
          </p>

          <h3 style="color:#fff; margin-bottom: 0.75rem;">3. Academic & Commercial IP Protection</h3>
          <p style="margin-bottom: 1.5rem;">
            All custom software source code, client business logic, and academic IEEE research projects developed for clients and students remain confidential. We enforce strict client-side encryption and zero-knowledge data retention.
          </p>

          <h3 style="color:#fff; margin-bottom: 0.75rem;">4. Cookie & Analytics Disclosures</h3>
          <p style="margin-bottom: 1.5rem;">
            Our website uses minimal, privacy-first session cookies to remember your browsing preferences and security state. We do not utilize invasive cross-site tracking scripts.
          </p>

          <h3 style="color:#fff; margin-bottom: 0.75rem;">5. Contacting the Data Protection Officer</h3>
          <p>
            If you have questions regarding this policy or wish to request data deletion, contact us at: <a href="mailto:jmvertextechnologies2025@gmail.com" style="color: var(--primary-glow);">jmvertextechnologies2025@gmail.com</a>.
          </p>
        </div>
      </div>
    </section>
    """
    footer = render_footer()
    write_page("privacy-policy.html", head + header + body + footer)

def build_terms():
    head = render_head(
        "Terms of Service & Academic Code | JM Vertex Technologies",
        "Terms of service, mentorship conditions, and academic integrity policies of JM Vertex Technologies.",
        "terms.html"
    )
    header = render_header("")

    body = f"""
    <section class="section" style="padding-top: 9rem; min-height: 80vh;">
      <div class="container" style="max-width: 900px;">
        <span class="pill-badge"><span class="pill-dot"></span> Terms of Engagement</span>
        <h1 class="heading-lg" style="margin-bottom: 1.5rem;">Terms of Service & Code of Conduct</h1>
        <p style="color: var(--text-dim); margin-bottom: 2.5rem;">Last Updated: 2026</p>

        <div class="glass-panel" style="padding: 3rem 2.5rem; line-height: 1.8; color: #cbd5e1;">
          <h3 style="color:#fff; margin-bottom: 0.75rem;">1. Service Engagement & Scoping</h3>
          <p style="margin-bottom: 1.5rem;">
            By engaging JM Vertex Technologies for website development, tech training, or project guidance, you agree to the functional specifications, milestones, and deliverables outlined in your official project brief or cohort agreement.
          </p>

          <h3 style="color:#fff; margin-bottom: 0.75rem;">2. Academic Integrity & Project Mentorship</h3>
          <p style="margin-bottom: 1.5rem;">
            Our academic project guidance is designed as an educational accelerator. Students are required to actively participate in the 1-on-1 code walkthroughs and viva preparation sessions to ensure genuine comprehension of the underlying algorithms and architectures.
          </p>

          <h3 style="color:#fff; margin-bottom: 0.75rem;">3. Deliverables & Source Code Ownership</h3>
          <p style="margin-bottom: 1.5rem;">
            Upon final milestone sign-off and settlement of agreed fees, full ownership of custom website code, database schemas, and documentation is transferred to the client.
          </p>

          <h3 style="color:#fff; margin-bottom: 0.75rem;">4. Limitation of Liability</h3>
          <p>
            JM Vertex Technologies shall not be held liable for third-party hosting outages (e.g. cloud provider downtime) beyond our reasonable technical control.
          </p>
        </div>
      </div>
    </section>
    """
    footer = render_footer()
    write_page("terms.html", head + header + body + footer)

# ==============================================================================
# 404, 500 & OFFLINE ERROR PAGES
# ==============================================================================
def build_404():
    head = render_head(
        "404 - Page Not Found | JM Vertex Technologies",
        "The requested URL could not be located in the JM Vertex Technologies cyber directory.",
        "404.html"
    )
    header = render_header("")

    body = f"""
    <section class="section" style="min-height: 85vh; display: flex; align-items: center; justify-content: center; text-align: center; padding-top: 8rem;">
      <div class="container" style="max-width: 650px;">
        <div class="reveal-on-scroll">
          <div class="glass-panel" style="padding: 3.5rem 2rem; border-color: rgba(239, 68, 68, 0.4); box-shadow: 0 0 35px rgba(239, 68, 68, 0.2);">
            <span class="pill-badge" style="background: rgba(239, 68, 68, 0.1); border-color: rgba(239, 68, 68, 0.3); color: #f87171;">
              <span class="pill-dot" style="background:#ef4444; box-shadow: 0 0 10px #ef4444;"></span> HTTP Error 404
            </span>
            <h1 class="heading-xl" style="font-size: 5.5rem; line-height: 1; margin: 1rem 0; color: #ffffff;">404</h1>
            <h2 class="heading-sm" style="margin-bottom: 1rem; color: #f87171;">Coordinates Not Found</h2>
            <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6; margin-bottom: 2rem;">
              The digital node or resource you are looking for has been moved, archived, or does not exist in our system registry.
            </p>
            <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
              <a href="index.html" class="btn btn-primary btn-lg">Return to Base (Home) {ICONS['arrow_right']}</a>
              <a href="contact.html" class="btn btn-secondary btn-lg">Report Dead Link</a>
            </div>
          </div>
        </div>
      </div>
    </section>
    """
    footer = render_footer()
    write_page("404.html", head + header + body + footer)

def build_500():
    head = render_head(
        "500 - Server Diagnostic Error | JM Vertex Technologies",
        "Internal server exception detected. System diagnostics active.",
        "500.html"
    )
    header = render_header("")

    body = f"""
    <section class="section" style="min-height: 85vh; display: flex; align-items: center; justify-content: center; text-align: center; padding-top: 8rem;">
      <div class="container" style="max-width: 650px;">
        <div class="reveal-on-scroll">
          <div class="glass-panel" style="padding: 3.5rem 2rem; border-color: rgba(245, 158, 11, 0.4); box-shadow: 0 0 35px rgba(245, 158, 11, 0.2);">
            <span class="pill-badge" style="background: rgba(245, 158, 11, 0.1); border-color: rgba(245, 158, 11, 0.3); color: #fbbf24;">
              <span class="pill-dot" style="background:#f59e0b; box-shadow: 0 0 10px #f59e0b;"></span> System Exception 500
            </span>
            <h1 class="heading-xl" style="font-size: 5.5rem; line-height: 1; margin: 1rem 0; color: #ffffff;">500</h1>
            <h2 class="heading-sm" style="margin-bottom: 1rem; color: #fbbf24;">Server Undergoing Maintenance</h2>
            <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6; margin-bottom: 2rem;">
              Our security firewalls or edge gateway encountered an unexpected internal state. Automated diagnostics have been logged and our engineers are resolving it.
            </p>
            <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
              <button onclick="window.location.reload()" class="btn btn-primary btn-lg">Retry Connection ↻</button>
              <a href="index.html" class="btn btn-secondary btn-lg">Back to Homepage</a>
            </div>
          </div>
        </div>
      </div>
    </section>
    """
    footer = render_footer()
    write_page("500.html", head + header + body + footer)

def build_offline():
    head = render_head(
        "Network Disconnected | JM Vertex Technologies",
        "You are currently offline. Checking for network connectivity...",
        "offline.html"
    )
    header = render_header("")

    body = f"""
    <section class="section" style="min-height: 85vh; display: flex; align-items: center; justify-content: center; text-align: center; padding-top: 8rem;">
      <div class="container" style="max-width: 650px;">
        <div class="reveal-on-scroll">
          <div class="glass-panel" style="padding: 3.5rem 2rem; border-color: rgba(6, 182, 212, 0.4); box-shadow: 0 0 35px rgba(6, 182, 212, 0.2);">
            <span class="pill-badge" style="background: rgba(6, 182, 212, 0.1); border-color: rgba(6, 182, 212, 0.3); color: #22d3ee;">
              <span class="pill-dot" style="background:#06b6d4; box-shadow: 0 0 10px #06b6d4;"></span> Network State: Offline
            </span>
            <div style="margin: 2rem 0;">
              <div class="feature-icon-box" style="width: 80px; height: 80px; margin: 0 auto; color: #22d3ee;">
                {ICONS['globe']}
              </div>
            </div>
            <h2 class="heading-sm" style="margin-bottom: 1rem; color: #fff; font-size: 1.5rem;">Connection Lost</h2>
            <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.6; margin-bottom: 2rem;">
              It looks like your internet connection dropped. As soon as your device reconnects to Wi-Fi or mobile data, this page will automatically reload and resume your session.
            </p>
            <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
              <button onclick="window.location.reload()" class="btn btn-primary btn-lg">Check Connection Now ↻</button>
            </div>
            <p id="connection-status-text" style="color: var(--primary-glow); font-size: 0.85rem; margin-top: 1.5rem;">
              Monitoring network sockets in real-time...
            </p>
          </div>
        </div>
      </div>
    </section>

    <script>
      window.addEventListener('online', () => {{
        const statusText = document.getElementById('connection-status-text');
        if (statusText) statusText.textContent = 'Connection restored! Reconnecting...';
        setTimeout(() => {{
          const prev = sessionStorage.getItem('jm_prev_page') || 'index.html';
          window.location.href = prev;
        }}, 800);
      }});
    </script>
    """
    footer = render_footer()
    write_page("offline.html", head + header + body + footer)

build_contact()
build_privacy_policy()
build_terms()
build_404()
build_500()
build_offline()
