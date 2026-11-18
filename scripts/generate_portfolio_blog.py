import json
import html
from base_templates import render_head, render_header, render_footer, ICONS

def write_page(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated: {filename}")

# Load blogs
with open('all_blog_posts_full.json', 'r', encoding='utf-8') as f:
    blogs = json.load(f)

# ==============================================================================
# PORTFOLIO.HTML
# ==============================================================================
def build_portfolio():
    head = render_head(
        "Portfolio & Production Showcases | JM Vertex Technologies",
        "Explore custom web applications, AI models, mobile apps, and secure systems engineered by JM Vertex Technologies for businesses and engineering researchers.",
        "portfolio.html"
    )
    header = render_header("portfolio")

    projects = [
        {
            "id": 1,
            "title": "Pizza Crave — Restaurant Commerce & WhatsApp Engine",
            "url": "https://pizzacrave.in",
            "link": "https://pizzacrave.in",
            "category": "Web Development",
            "badge": "LIVE IN PRODUCTION",
            "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&q=80&w=800",
            "tech": ["React 19", "Vite", "Tailwind CSS", "WhatsApp API"],
            "desc": "Engineered a custom, high-speed digital storefront for Pizza Crave restaurant with instantaneous WhatsApp order dispatch, interactive cart customization, and sub-second load times.",
            "metric": "⚡ +40% DIRECT SALES • 98 PAGESPEED SCORE",
            "is_external": True
        },
        {
            "id": 2,
            "title": "SecureShield AI — Healthcare Diagnostic & Threat Telemetry",
            "url": "https://secureshield.ai-platform.io",
            "link": "#",
            "category": "AI / ML",
            "badge": "IEEE RESEARCH GRADE",
            "image": "https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&q=80&w=800",
            "tech": ["Python", "TensorFlow", "FastAPI", "React", "Docker"],
            "desc": "Deep learning convolutional neural network architecture diagnosing patient symptoms and enterprise cybersecurity anomalies in real-time.",
            "metric": "⚡ 96.4% ACCURACY • REAL-TIME INFERENCE",
            "is_external": False
        },
        {
            "id": 3,
            "title": "NextGen Commerce — Digital Storefront & Automation Hub",
            "url": "https://ecommerce.jmvertextechnologies.com",
            "link": "#",
            "category": "Full Stack",
            "badge": "ENTERPRISE COMMERCE",
            "image": "https://images.unsplash.com/photo-1557821552-17105176677c?auto=format&fit=crop&q=80&w=800",
            "tech": ["React 19", "Node.js", "MongoDB", "Stripe", "Redux"],
            "desc": "End-to-end commerce suite with custom checkout funnel, multi-currency processing, dynamic variant filtering, and administrative warehouse inventory synchronization.",
            "metric": "⚡ STRIPE CHECKOUT • 10K+ SKU INVENTORY SYNC",
            "is_external": False
        },
        {
            "id": 4,
            "title": "AgriSense IoT — Smart Agriculture Environmental Telemetry",
            "url": "https://agrisense.iot-telemetry.in",
            "link": "#",
            "category": "IoT & Embedded",
            "badge": "IEEE JOURNAL PUBLISHED",
            "image": "https://images.unsplash.com/photo-1586771107445-d3ca888129ff?auto=format&fit=crop&q=80&w=800",
            "tech": ["IoT Sensors", "MQTT", "Python", "AWS Cloud", "Node.js"],
            "desc": "Precision crop telemetry system measuring soil NPK levels, moisture, and ambient weather with automated solar-powered irrigation valves and AWS IoT data pipelines.",
            "metric": "⚡ 40% WATER CONSERVATION • REAL-TIME MQTT",
            "is_external": False
        },
        {
            "id": 5,
            "title": "FinTrack Pro — Real-Time Financial Analytics Dashboard",
            "url": "https://fintrack.trading-analytics.io",
            "link": "#",
            "category": "Frontend",
            "badge": "HIGH-FREQUENCY UI",
            "image": "https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&q=80&w=800",
            "tech": ["React", "Redux Toolkit", "Chart.js", "Tailwind CSS"],
            "desc": "High-frequency analytics dashboard for tracking personal finance, visualizing asset allocations, cash flow heatmaps, and setting dynamic monthly budgets.",
            "metric": "⚡ 60 FPS RENDERING • < 0.8S DATA RENDER",
            "is_external": False
        },
        {
            "id": 6,
            "title": "SkillBridge LMS — Tech Internship & Assessment Portal",
            "url": "https://skillbridge.lms-academy.in",
            "link": "#",
            "category": "EdTech & Cloud",
            "badge": "PRODUCTION ACADEMY",
            "image": "https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&q=80&w=800",
            "tech": ["MERN Stack", "Docker", "AWS EC2", "PostgreSQL"],
            "desc": "Corporate LMS with integrated code runner, automated viva scoring, student progress tracking, and tamper-proof verified credential issuance.",
            "metric": "⚡ 100+ STUDENTS ACTIVE • TAMPER-PROOF CERTS",
            "is_external": False
        },
        {
            "id": 7,
            "title": "Secure Corporate File Sharing System",
            "url": "https://vault.enterprise-secure.io",
            "link": "#",
            "category": "Cybersecurity",
            "badge": "ZERO-KNOWLEDGE VAULT",
            "image": "https://images.unsplash.com/photo-1563986768609-322da13575f3?auto=format&fit=crop&q=80&w=800",
            "tech": ["Node.js", "AES-256 Crypto", "React", "PostgreSQL"],
            "desc": "End-to-end encrypted file sharing and digital asset repository engineered for enterprise compliance, zero-knowledge proofs, and automated audit logging.",
            "metric": "⚡ AES-256 ZERO-LEAK • AUDIT LOGGING",
            "is_external": False
        },
        {
            "id": 8,
            "title": "Customer Churn Predictive Engine",
            "url": "https://churn-predictor.analytics.ai",
            "link": "#",
            "category": "Data Science",
            "badge": "PREDICTIVE ANALYTICS",
            "image": "https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&q=80&w=800",
            "tech": ["Python", "Pandas", "Scikit-Learn", "Tableau", "Flask"],
            "desc": "Enterprise analytics model that analyzes historical user interactions, subscription patterns, and support tickets to accurately forecast customer retention risks.",
            "metric": "⚡ 89% RETENTION PREDICTION ACCURACY",
            "is_external": False
        }
    ]

    cards_html = ""
    for p in projects:
        tech_pills = "".join([f'<span class="tag-mono" style="font-size:0.7rem;">{t}</span> ' for t in p['tech']])
        
        # Primary action button
        if p.get('is_external'):
            action_btn = f"""<a href="{p['link']}" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm" style="flex: 1;">
              Visit Live Site <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
            </a>"""
        else:
            action_btn = f"""<a href="https://wa.me/919092737477?text=Hi%20JM%20Vertex,%20I%20am%20interested%20in%20a%20project%20like%20{html.escape(p['title'])}." target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm" style="flex: 1;">
              Inquire Project {ICONS['arrow_right']}
            </a>"""

        cards_html += f"""
        <div class="work-browser-card">
          <div class="work-browser-header">
            <div class="work-browser-dots">
              <span class="work-browser-dot"></span>
              <span class="work-browser-dot"></span>
              <span class="work-browser-dot"></span>
            </div>
            <span class="work-browser-url">{p['url']}</span>
          </div>
          <div class="work-preview-img-wrap">
            <img src="{p['image']}" alt="{html.escape(p['title'])}" loading="lazy">
            <span class="work-badge-live">
              <span class="live-dot"></span> {p['badge']}
            </span>
          </div>
          <div class="work-content-body">
            <div class="work-metric-chip">
              {p['metric']}
            </div>
            <h3 class="card-title" style="margin-bottom: 0.5rem; font-size: 1.35rem;">{p['title']}</h3>
            <p style="color: var(--paper-soft); font-size: 0.9rem; line-height: 1.6; margin-bottom: 1.25rem;">
              {p['desc']}
            </p>
            <div style="display: flex; gap: 0.4rem; flex-wrap: wrap; margin-bottom: 1.75rem;">
              {tech_pills}
            </div>
            <div style="display: flex; gap: 0.75rem; margin-top: auto;">
              {action_btn}
              <a href="https://wa.me/919092737477?text=Hi%20JM%20Vertex,%20tell%20me%20more%20about%20{html.escape(p['title'])}." target="_blank" rel="noopener noreferrer" class="btn btn-ghost btn-sm">
                Discuss Tech
              </a>
            </div>
          </div>
        </div>
        """

    body = f"""
    <!-- Portfolio Hero -->
    <section class="section-block" style="padding-top: clamp(3.5rem, 6vw, 6rem); padding-bottom: 2rem;">
      <div class="container text-center">
        <div style="max-width: 800px; margin: 0 auto;">
          <span class="eyebrow"><span class="dot"></span> VERIFIED DELIVERIES &amp; CASE STUDIES</span>
          <h1 class="hero-display-title" style="font-size: clamp(2.5rem, 5vw, 4.5rem); margin: 1rem 0 1.25rem;">
            OUR PRODUCTION <br>
            <span style="color: var(--emerald);">PORTFOLIO.</span>
          </h1>
          <p class="section-lead" style="margin: 0 auto 2.5rem;">
            A curated showcase of commercial web platforms, IEEE standard research implementations, and deep-tech prototypes engineered by JM Vertex Technologies.
          </p>
        </div>

        <!-- Verified Metrics Grid (Exact Official Stats matching client records) -->
        <div class="stat-cards-grid">
          <div class="stat-card-box">
            <span class="stat-card-value">100+</span>
            <span class="stat-card-label">Students Trained</span>
          </div>
          <div class="stat-card-box">
            <span class="stat-card-value">20+</span>
            <span class="stat-card-label">Projects Delivered</span>
          </div>
          <div class="stat-card-box">
            <span class="stat-card-value">30+</span>
            <span class="stat-card-label">Websites Built</span>
          </div>
          <div class="stat-card-box">
            <span class="stat-card-value">15+</span>
            <span class="stat-card-label">Schools &amp; Colleges</span>
          </div>
        </div>
      </div>
    </section>

    <!-- Project Showcases Grid with Browser Frames -->
    <section class="section-block" style="padding-top: 1rem;">
      <div class="container">
        <div class="bento-grid-2" style="gap: 2rem;">
          {cards_html}
        </div>

        <!-- Custom Project Banner -->
        <div style="text-align: center; margin-top: 4.5rem;">
          <div class="studio-card" style="padding: 3.5rem 2rem; max-width: 860px; margin: 0 auto; border-color: rgba(0, 255, 136, 0.4);">
            <span class="tag-mono tag-emerald" style="margin-bottom: 0.75rem;">BESPOKE PRODUCTION</span>
            <h3 class="card-title" style="font-size: 2rem; margin-bottom: 0.75rem;">Have a Custom Project in Mind?</h3>
            <p style="color: var(--paper-soft); font-size: 0.95rem; max-width: 600px; margin: 0 auto 2rem;">
              Whether you are launching a commercial web platform or need verified IEEE research project implementation with full reports, our engineers are ready.
            </p>
            <a href="https://wa.me/919092737477?text=Hi%20JM%20Vertex,%20I%20have%20a%20new%20custom%20project%20to%20build." target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp btn-lg">
              {ICONS['whatsapp']} Start Your Project on WhatsApp
            </a>
          </div>
        </div>
      </div>
    </section>
    """
    footer = render_footer()
    write_page("portfolio.html", head + header + body + footer)

# ==============================================================================
# BLOG.HTML (ALL 20 ARTICLES ARCHIVE)
# ==============================================================================
def build_blog():
    head = render_head(
        "Technical Publications & Insights Blog | JM Vertex Technologies",
        "Explore 20 in-depth articles on final year project ideas, website development costs in India, German language benefits, MERN stack roadmaps, and IEEE implementations.",
        "blog.html"
    )
    header = render_header("blog")

    articles_cards_html = ""
    for idx, b in enumerate(blogs):
        articles_cards_html += f"""
        <div class="col-4 reveal-on-scroll delay-{(idx % 3) + 1} blog-card-item" data-category="{html.escape(b['category'])}" data-title="{html.escape(b['title'].lower())}">
          <div class="glass-panel tilt-card" style="padding: 2.25rem; height: 100%; display: flex; flex-direction: column; justify-content: space-between;">
            <div class="tilt-inner">
              <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                <span class="pill-badge" style="margin-bottom: 0; font-size: 0.75rem;">{html.escape(b['category'])}</span>
                <span style="color: var(--text-dim); font-size: 0.8rem;">{html.escape(b['date'])}</span>
              </div>
              <h3 class="heading-sm" style="font-size: 1.15rem; line-height: 1.4; margin-bottom: 0.75rem;">
                <a href="blog-detail.html?id={b['id']}" style="color: #fff; text-decoration: none;" class="hover-underline">
                  {html.escape(b['title'])}
                </a>
              </h3>
              <p style="color: var(--text-muted); font-size: 0.875rem; line-height: 1.6; margin-bottom: 1.5rem;">
                {html.escape(b['excerpt'])}
              </p>
            </div>
            <div>
              <a href="blog-detail.html?id={b['id']}" class="btn btn-outline-emerald btn-sm" style="width: 100%;">
                Read Full Article {ICONS['arrow_right']}
              </a>
            </div>
          </div>
        </div>
        """

    body = f"""
    <section class="section section-hero">
      <div class="container text-center">
        <div class="reveal-on-scroll">
          <div class="pill-badge"><span class="pill-dot"></span> Knowledge Hub</div>
          <h1 class="heading-xl" style="margin-bottom: 1.5rem;">
            Engineering Guides & <br>
            <span class="text-gradient">Technical Publications</span>
          </h1>
          <p class="subheading" style="margin-bottom: 2.5rem;">
            Deep-dive tutorials, career roadmaps, cost breakdowns, and academic methodologies published by our engineering leads.
          </p>

          <!-- Search & Filter Bar -->
          <div class="glass-panel" style="max-width: 800px; margin: 0 auto; padding: 1.25rem 1.75rem;">
            <input type="text" id="blog-search-input" class="input-glass" placeholder="Search articles by keyword (e.g. final year, german, react, cost)..." style="margin-bottom: 1rem;">
            <div style="display: flex; gap: 0.5rem; justify-content: center; flex-wrap: wrap;" id="blog-filter-btns">
              <button class="btn btn-primary btn-sm filter-btn active" data-filter="all">All ({len(blogs)})</button>
              <button class="btn btn-secondary btn-sm filter-btn" data-filter="Student Projects">Student Projects</button>
              <button class="btn btn-secondary btn-sm filter-btn" data-filter="Web Development">Web Development</button>
              <button class="btn btn-secondary btn-sm filter-btn" data-filter="Foreign Languages">Foreign Languages</button>
              <button class="btn btn-secondary btn-sm filter-btn" data-filter="Training">Training</button>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section" style="padding-top: 0;">
      <div class="container">
        <div class="bento-grid" id="blog-grid-container">
          {articles_cards_html}
        </div>
      </div>
    </section>

    <!-- Client-Side Instant Search Script -->
    <script>
      document.addEventListener('DOMContentLoaded', () => {{
        const searchInput = document.getElementById('blog-search-input');
        const filterBtns = document.querySelectorAll('.filter-btn');
        const cards = document.querySelectorAll('.blog-card-item');

        let activeCategory = 'all';
        let searchQuery = '';

        function filterPosts() {{
          cards.forEach(card => {{
            const cat = card.getAttribute('data-category');
            const title = card.getAttribute('data-title');
            
            const matchesCat = activeCategory === 'all' || cat === activeCategory;
            const matchesSearch = searchQuery === '' || title.includes(searchQuery);

            if (matchesCat && matchesSearch) {{
              card.style.display = 'block';
            }} else {{
              card.style.display = 'none';
            }}
          }});
        }}

        if (searchInput) {{
          searchInput.addEventListener('input', (e) => {{
            searchQuery = e.target.value.toLowerCase().trim();
            filterPosts();
          }});
        }}

        filterBtns.forEach(btn => {{
          btn.addEventListener('click', () => {{
            filterBtns.forEach(b => {{
              b.classList.remove('btn-primary', 'active');
              b.classList.add('btn-secondary');
            }});
            btn.classList.add('btn-primary', 'active');
            btn.classList.remove('btn-secondary');
            activeCategory = btn.getAttribute('data-filter');
            filterPosts();
          }});
        }});
      }});
    </script>
    """
    footer = render_footer()
    write_page("blog.html", head + header + body + footer)

# ==============================================================================
# BLOG-DETAIL.HTML (DYNAMIC ARTICLE READER)
# ==============================================================================
def build_blog_detail():
    head = render_head(
        "Technical Article | JM Vertex Technologies",
        "Comprehensive technical guide, analysis, and implementation roadmap published by the JM Vertex Technologies engineering team.",
        "blog-detail.html"
    )
    header = render_header("blog")

    body = f"""
    <!-- Reading Progress Bar -->
    <div id="read-progress-bar" style="position: fixed; top: 0; left: 0; height: 3px; background: var(--primary-neon); width: 0%; z-index: 999; transition: width 0.1s ease;"></div>

    <section class="section" style="padding-top: 9rem; min-height: 80vh;">
      <div class="container" style="max-width: 900px;">
        <!-- Back Button -->
        <a href="blog.html" class="btn btn-secondary btn-sm" style="margin-bottom: 2rem;">
          ← Back to All Articles
        </a>

        <!-- Article Header Container -->
        <div id="article-header" class="reveal-on-scroll">
          <div style="display: flex; gap: 0.75rem; align-items: center; margin-bottom: 1.25rem;">
            <span class="pill-badge" id="art-category" style="margin-bottom: 0;">Category</span>
            <span style="color: var(--text-dim); font-size: 0.85rem;" id="art-date">Published Date</span>
            <span style="color: var(--primary-glow); font-size: 0.85rem;" id="art-read-time">5 min read</span>
          </div>
          <h1 class="heading-lg" id="art-title" style="margin-bottom: 1.5rem; line-height: 1.25;">
            Loading Article...
          </h1>
          <p class="subheading" id="art-excerpt" style="margin-left: 0; margin-bottom: 2.5rem; font-size: 1.15rem; color: #cbd5e1;">
            Please wait while the technical publication content loads.
          </p>
          <div class="light-beam-divider" style="margin: 2rem 0 3rem;"></div>
        </div>

        <!-- Article Body -->
        <div id="article-content-body" class="glass-panel" style="padding: 3rem 2.5rem; line-height: 1.85; font-size: 1.05rem; color: #e2e8f0; margin-bottom: 4rem;">
          <!-- Paragraphs rendered here by JS -->
        </div>

        <!-- Author / Footer Box -->
        <div class="glass-panel" style="padding: 2rem 2.5rem; display: flex; align-items: center; gap: 1.5rem; border-color: rgba(34, 197, 94, 0.4); margin-bottom: 4rem;">
          <div class="author-avatar" style="width: 56px; height: 56px; font-size: 1.35rem;">JM</div>
          <div>
            <h4 style="color: #fff; font-size: 1.1rem; margin-bottom: 0.25rem;">JM Vertex Editorial & Engineering Team</h4>
            <p style="color: var(--text-muted); font-size: 0.875rem;">
              Published by the technical leads at JM Vertex Technologies. We engineer production software and mentor the next generation of engineers.
            </p>
          </div>
        </div>

        <!-- Related Posts / Next Read -->
        <div class="text-center">
          <h3 class="heading-sm" style="margin-bottom: 1.5rem;">Explore More Industry Articles</h3>
          <a href="blog.html" class="btn btn-primary btn-lg">Browse All 20 Publications {ICONS['arrow_right']}</a>
        </div>
      </div>
    </section>

    <!-- Dynamic Article Population Script -->
    <script>
      document.addEventListener('DOMContentLoaded', () => {{
        const params = new URLSearchParams(window.location.search);
        let articleId = params.get('id');

        // Fallback if no ID specified
        if (!articleId) {{
          articleId = 'final-year-project-ideas';
        }}

        const posts = window.JM_BLOG_POSTS || [];
        const post = posts.find(p => p.id === articleId) || posts[0];

        if (post) {{
          document.title = post.title + ' | JM Vertex Technologies';
          document.getElementById('art-title').textContent = post.title;
          document.getElementById('art-category').textContent = post.category;
          document.getElementById('art-date').textContent = post.date;
          document.getElementById('art-excerpt').textContent = post.excerpt;

          const bodyContainer = document.getElementById('article-content-body');
          bodyContainer.innerHTML = '';

          const paragraphs = post.content_paragraphs || [post.excerpt];
          paragraphs.forEach((pText, i) => {{
            const p = document.createElement('p');
            p.style.marginBottom = '1.75rem';
            
            // Highlight subheadings or list items
            if (pText.includes(':') && pText.length < 120 && !pText.includes('.')) {{
              p.style.fontSize = '1.25rem';
              p.style.fontWeight = '700';
              p.style.color = '#ffffff';
              p.style.marginTop = '2.5rem';
            }}
            p.textContent = pText;
            bodyContainer.appendChild(p);
          }});

          // Reading progress bar calculation
          window.addEventListener('scroll', () => {{
            const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
            const progress = (window.scrollY / totalHeight) * 100;
            const bar = document.getElementById('read-progress-bar');
            if (bar) bar.style.width = Math.min(100, Math.max(0, progress)) + '%';
          }}, {{ passive: true }});
        }}
      }});
    </script>
    """
    footer = render_footer()
    write_page("blog-detail.html", head + header + body + footer)

build_portfolio()
build_blog()
build_blog_detail()
