import os
import sys

# Add parent directory to path so base_templates can be imported
sys.path.append(os.path.abspath('.'))
from base_templates import render_head, render_header, render_footer, ICONS

def build_index():
    head = render_head(
        "JM Vertex Technologies — Creative Engineering Studio & Tech Academy",
        "JM Vertex Technologies architects high-conversion web platforms, IEEE standard final year engineering projects, intensive tech internships, and certified German & Japanese language coaching.",
        ""
    )
    header = render_header("home")

    body = f"""
    <!-- Master Engineering Studio Hero -->
    <section class="section-block" style="padding-top: clamp(3.5rem, 6vw, 6rem); padding-bottom: clamp(2.5rem, 4vw, 4rem);">
      <div class="container">
        <!-- Top Monospace Metadata Tag -->
        <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 2rem; flex-wrap: wrap;">
          <span class="eyebrow"><span class="dot"></span> EST. 2025 // COIMBATORE, TAMIL NADU</span>
          <span style="color: var(--rule-strong);">•</span>
          <span class="tag-mono tag-emerald">WEB STUDIO &amp; ACADEMIC LABS</span>
          <span class="tag-mono tag-cyan">IEEE ACCREDITED</span>
        </div>

        <!-- Monumental Hero Display Headline -->
        <div style="margin-bottom: 2.5rem; max-width: 1100px;">
          <h1 class="hero-display-title">
            ENGINEERING <br>
            <span style="color: var(--emerald);">THE NEXT</span> HORIZON.
          </h1>
        </div>

        <!-- Asymmetric Editorial Lead & Action Grid -->
        <div style="display: grid; grid-template-columns: repeat(12, 1fr); gap: 2.5rem; align-items: flex-end; margin-bottom: 3.5rem;">
          <div style="grid-column: span 7;">
            <p class="section-lead">
              We merge bespoke software craftsmanship, academic research rigor, and foreign language mastery. Architectural web applications engineered for scaling businesses, distinction-grade IEEE final year projects, and certified global engineering pathways.
            </p>
          </div>
          <div style="grid-column: span 5; display: flex; flex-direction: column; gap: 1.25rem; align-items: flex-start;">
            <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
              <a href="website-development.html" class="btn btn-primary" data-cursor-text="EXPLORE">
                Explore Web Studio {ICONS['arrow_right']}
              </a>
              <a href="student-projects.html" class="btn btn-ghost" data-cursor-text="PROJECTS">
                Student Projects (IEEE)
              </a>
            </div>
            <div style="display: flex; align-items: center; gap: 0.75rem; font-family: var(--font-mono); font-size: 0.75rem; color: var(--paper-mute);">
              <span>DIRECT FOUNDER DESK:</span>
              <a href="tel:+919092737477" style="color: var(--emerald); font-weight: 700; text-decoration: none;">+91 90927 37477</a>
            </div>
          </div>
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

    <!-- Continuous Horizontal Marquee Ribbon -->
    <div class="marquee-ribbon-wrap">
      <div class="marquee-content">
        <div class="marquee-item"><span>REACT 19 &amp; VITE APPS</span> <div class="marquee-dot"></div></div>
        <div class="marquee-item"><span>IEEE RESEARCH IMPLEMENTATION</span> <div class="marquee-dot"></div></div>
        <div class="marquee-item"><span>FULL STACK MERN &amp; PYTHON</span> <div class="marquee-dot"></div></div>
        <div class="marquee-item"><span>AWS &amp; DOCKER DEVOPS</span> <div class="marquee-dot"></div></div>
        <div class="marquee-item"><span>AI &amp; NEURAL NETWORKS</span> <div class="marquee-dot"></div></div>
        <div class="marquee-item"><span>GERMAN GOETHE A1-B2</span> <div class="marquee-dot"></div></div>
        <div class="marquee-item"><span>JAPANESE JLPT N5-N1</span> <div class="marquee-dot"></div></div>
        <div class="marquee-item"><span>WHATSAPP ORDERING CRM</span> <div class="marquee-dot"></div></div>
        <!-- Infinite loop repetition -->
        <div class="marquee-item"><span>REACT 19 &amp; VITE APPS</span> <div class="marquee-dot"></div></div>
        <div class="marquee-item"><span>IEEE RESEARCH IMPLEMENTATION</span> <div class="marquee-dot"></div></div>
        <div class="marquee-item"><span>FULL STACK MERN &amp; PYTHON</span> <div class="marquee-dot"></div></div>
        <div class="marquee-item"><span>AWS &amp; DOCKER DEVOPS</span> <div class="marquee-dot"></div></div>
        <div class="marquee-item"><span>AI &amp; NEURAL NETWORKS</span> <div class="marquee-dot"></div></div>
      </div>
    </div>

    <!-- [01] The 4 Core Disciplines — Solid Architecture -->
    <section class="section-block">
      <div class="container">
        <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 3.5rem; flex-wrap: wrap; gap: 2rem;">
          <div>
            <span class="eyebrow"><span class="dot"></span> [01] // BESPOKE CAPABILITIES</span>
            <h2 class="section-display-title" style="margin-top: 0.75rem;">
              WHAT WE <span style="color: var(--emerald);">ENGINEER.</span>
            </h2>
          </div>
          <p style="color: var(--paper-mute); max-width: 440px; font-size: 0.95rem; line-height: 1.6;">
            Every discipline is built with production depth — zero generic templates or superficial theory.
          </p>
        </div>

        <!-- 4 Disciplines Rows -->
        <div style="display: flex; flex-direction: column; gap: 1.5rem;">
          <!-- Discipline 1: Web Development -->
          <div class="discipline-row">
            <span class="discipline-num">01</span>
            <div>
              <span class="tag-mono" style="margin-bottom: 0.5rem; font-size: 0.7rem;">DIGITAL PRODUCTION</span>
              <h3 class="card-title" style="margin-bottom: 0.5rem;">Website &amp; Web App Development</h3>
              <p style="color: var(--paper-soft); font-size: 0.925rem; line-height: 1.6;">
                Custom React &amp; Vite single-page applications engineered for small businesses, restaurants, and startups. 90+ PageSpeed guarantee with integrated technical SEO and direct WhatsApp ordering CRM.
              </p>
            </div>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
              <span class="tag-mono tag-emerald">REACT / VITE</span>
              <span class="tag-mono">SUB-SECOND SPEED</span>
              <span class="tag-mono">WHATSAPP COMMERCE</span>
            </div>
            <div>
              <a href="website-development.html" class="btn btn-ghost btn-sm">
                Explore Studio {ICONS['arrow_right']}
              </a>
            </div>
          </div>

          <!-- Discipline 2: Custom Student Projects -->
          <div class="discipline-row">
            <span class="discipline-num">02</span>
            <div>
              <span class="tag-mono" style="margin-bottom: 0.5rem; font-size: 0.7rem;">ACADEMIC RESEARCH LABS</span>
              <h3 class="card-title" style="margin-bottom: 0.5rem;">Custom Projects for College Students (IEEE)</h3>
              <p style="color: var(--paper-soft); font-size: 0.925rem; line-height: 1.6;">
                End-to-end guidance for B.E., B.Tech, MCA, and MSc engineering students. Implement authentic IEEE base papers with clean production code, architecture flowcharts, comprehensive reports, and 1-on-1 viva defense training.
              </p>
            </div>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
              <span class="tag-mono tag-cyan">IEEE BASE PAPERS</span>
              <span class="tag-mono">LIVE VIVA PREP</span>
              <span class="tag-mono">COMPLETE DOCUMENTATION</span>
            </div>
            <div>
              <a href="student-projects.html" class="btn btn-ghost btn-sm">
                View Project Catalog {ICONS['arrow_right']}
              </a>
            </div>
          </div>

          <!-- Discipline 3: Tech Training & Internships -->
          <div class="discipline-row">
            <span class="discipline-num">03</span>
            <div>
              <span class="tag-mono" style="margin-bottom: 0.5rem; font-size: 0.7rem;">ENGINEERING ACADEMY</span>
              <h3 class="card-title" style="margin-bottom: 0.5rem;">Tech Training &amp; Intensive Internships</h3>
              <p style="color: var(--paper-soft); font-size: 0.925rem; line-height: 1.6;">
                Intensive cohorts across 6 specialized tracks: Python Full Stack, MERN Stack, Cloud Computing &amp; DevOps, AI/ML, Cybersecurity, and Data Science. Hands-on labs with verified credentials and live production projects.
              </p>
            </div>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
              <span class="tag-mono tag-emerald">6 SPECIALIZED TRACKS</span>
              <span class="tag-mono">HANDS-ON LABS</span>
              <span class="tag-mono">VERIFIED CREDENTIALS</span>
            </div>
            <div>
              <a href="internship-training.html" class="btn btn-ghost btn-sm">
                View Curricula {ICONS['arrow_right']}
              </a>
            </div>
          </div>

          <!-- Discipline 4: Foreign Language Academy -->
          <div class="discipline-row">
            <span class="discipline-num">04</span>
            <div>
              <span class="tag-mono" style="margin-bottom: 0.5rem; font-size: 0.7rem;">GLOBAL MOBILITY</span>
              <h3 class="card-title" style="margin-bottom: 0.5rem;">Foreign Language Coaching (German &amp; Japanese)</h3>
              <p style="color: var(--paper-soft); font-size: 0.925rem; line-height: 1.6;">
                Access tuition-free master's education in Germany and high-demand developer careers in Tokyo. Certified training for German (Goethe A1-B2) and Japanese (JLPT N5-N1) with interactive speaking sessions and exam mock drill tests.
              </p>
            </div>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
              <span class="tag-mono tag-cyan">GERMAN GOETHE A1-B2</span>
              <span class="tag-mono">JAPANESE JLPT N5-N1</span>
              <span class="tag-mono">GERMAN UNIVERSITY SOPS</span>
            </div>
            <div>
              <a href="german-language-course.html" class="btn btn-ghost btn-sm">
                Language Tracks {ICONS['arrow_right']}
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- [02] Selected Production Works Showcase — World-Class Branding Methodology -->
    <section class="section-block" style="background: #08090d; border-top: 1px solid var(--rule); border-bottom: 1px solid var(--rule);">
      <div class="container">
        <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 3.5rem; flex-wrap: wrap; gap: 1.5rem;">
          <div>
            <span class="eyebrow"><span class="dot"></span> [02] // VERIFIED PRODUCTION SHOWCASE</span>
            <h2 class="section-display-title" style="margin-top: 0.75rem;">
              FEATURED <span style="color: var(--emerald);">WORKS.</span>
            </h2>
          </div>
          <a href="portfolio.html" class="btn btn-ghost">
            View All Completed Works {ICONS['arrow_right']}
          </a>
        </div>

        <!-- 4 Prominent Browser Preview Cards with Live Links -->
        <div class="bento-grid-2" style="gap: 2rem;">

          <!-- Work 1: Pizza Crave (Live Commercial Client!) -->
          <div class="work-browser-card">
            <div class="work-browser-header">
              <div class="work-browser-dots">
                <span class="work-browser-dot"></span>
                <span class="work-browser-dot"></span>
                <span class="work-browser-dot"></span>
              </div>
              <span class="work-browser-url">https://pizzacrave.in</span>
            </div>
            <div class="work-preview-img-wrap">
              <img src="https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&q=80&w=800" alt="Pizza Crave Restaurant Ordering Platform">
              <span class="work-badge-live">
                <span class="live-dot"></span> LIVE IN PRODUCTION
              </span>
            </div>
            <div class="work-content-body">
              <div class="work-metric-chip">
                ⚡ +40% DIRECT SALES • 98 PAGESPEED SCORE
              </div>
              <h3 class="card-title" style="margin-bottom: 0.5rem; font-size: 1.4rem;">Pizza Crave — Restaurant Commerce &amp; WhatsApp Engine</h3>
              <p style="color: var(--paper-soft); font-size: 0.9rem; line-height: 1.6; margin-bottom: 1.25rem;">
                Engineered a custom, high-speed digital storefront for Pizza Crave restaurant with instantaneous WhatsApp order dispatch, interactive cart customization, and sub-second load times.
              </p>
              <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.75rem;">
                <span class="tag-mono tag-emerald">REACT 19</span>
                <span class="tag-mono">VITE</span>
                <span class="tag-mono">WHATSAPP COMMERCE</span>
                <span class="tag-mono">SEO READY</span>
              </div>
              <div style="display: flex; gap: 0.75rem; margin-top: auto;">
                <a href="https://pizzacrave.in" target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-sm" style="flex: 1;">
                  Visit Live Site <svg width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/></svg>
                </a>
                <a href="https://wa.me/919092737477?text=Hi%20JM%20Vertex,%20I%20am%20interested%20in%20a%20website%20like%20Pizza%20Crave." target="_blank" rel="noopener noreferrer" class="btn btn-ghost btn-sm">
                  Inquire Similar
                </a>
              </div>
            </div>
          </div>

          <!-- Work 2: SecureShield AI (AI & Cybersecurity) -->
          <div class="work-browser-card">
            <div class="work-browser-header">
              <div class="work-browser-dots">
                <span class="work-browser-dot"></span>
                <span class="work-browser-dot"></span>
                <span class="work-browser-dot"></span>
              </div>
              <span class="work-browser-url">https://secureshield.ai-platform.io</span>
            </div>
            <div class="work-preview-img-wrap">
              <img src="https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?auto=format&fit=crop&q=80&w=800" alt="SecureShield AI Diagnostic Platform">
              <span class="work-badge-live" style="color: var(--cyan); border-color: rgba(0, 240, 255, 0.4);">
                <span class="live-dot" style="background: var(--cyan); box-shadow: 0 0 6px var(--cyan);"></span> IEEE RESEARCH GRADE
              </span>
            </div>
            <div class="work-content-body">
              <div class="work-metric-chip" style="color: var(--cyan); border-color: rgba(0, 240, 255, 0.3); background: rgba(0, 240, 255, 0.08);">
                ⚡ 96.4% ACCURACY • REAL-TIME INFERENCE
              </div>
              <h3 class="card-title" style="margin-bottom: 0.5rem; font-size: 1.4rem;">SecureShield AI — Healthcare Diagnostic &amp; Threat Telemetry</h3>
              <p style="color: var(--paper-soft); font-size: 0.9rem; line-height: 1.6; margin-bottom: 1.25rem;">
                Deep learning neural network architecture designed for medical anomaly screening and corporate cybersecurity threat prediction. Built as an end-to-end IEEE demonstration suite.
              </p>
              <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.75rem;">
                <span class="tag-mono tag-cyan">PYTHON</span>
                <span class="tag-mono">TENSORFLOW</span>
                <span class="tag-mono">FASTAPI</span>
                <span class="tag-mono">REACT</span>
              </div>
              <div style="display: flex; gap: 0.75rem; margin-top: auto;">
                <a href="portfolio.html" class="btn btn-primary btn-sm" style="flex: 1;">
                  View Case Study {ICONS['arrow_right']}
                </a>
                <a href="student-projects.html" class="btn btn-ghost btn-sm">
                  IEEE Papers
                </a>
              </div>
            </div>
          </div>

          <!-- Work 3: NextGen E-Commerce Suite -->
          <div class="work-browser-card">
            <div class="work-browser-header">
              <div class="work-browser-dots">
                <span class="work-browser-dot"></span>
                <span class="work-browser-dot"></span>
                <span class="work-browser-dot"></span>
              </div>
              <span class="work-browser-url">https://ecommerce.jmvertextechnologies.com</span>
            </div>
            <div class="work-preview-img-wrap">
              <img src="https://images.unsplash.com/photo-1557821552-17105176677c?auto=format&fit=crop&q=80&w=800" alt="E-Commerce & Digital Storefront">
              <span class="work-badge-live">
                <span class="live-dot"></span> FULL STACK DEPLOYED
              </span>
            </div>
            <div class="work-content-body">
              <div class="work-metric-chip">
                ⚡ STRIPE READY • 10K+ SKU INVENTORY SYNC
              </div>
              <h3 class="card-title" style="margin-bottom: 0.5rem; font-size: 1.4rem;">NextGen Commerce — Digital Storefront &amp; Automation Hub</h3>
              <p style="color: var(--paper-soft); font-size: 0.9rem; line-height: 1.6; margin-bottom: 1.25rem;">
                Full-stack commerce engine with custom checkout funnel, multi-currency processing, dynamic variant filtering, and administrative inventory analytics.
              </p>
              <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.75rem;">
                <span class="tag-mono tag-emerald">MERN STACK</span>
                <span class="tag-mono">STRIPE</span>
                <span class="tag-mono">REDUX</span>
                <span class="tag-mono">TAILWIND</span>
              </div>
              <div style="display: flex; gap: 0.75rem; margin-top: auto;">
                <a href="portfolio.html" class="btn btn-primary btn-sm" style="flex: 1;">
                  View Live Demo {ICONS['arrow_right']}
                </a>
                <a href="https://wa.me/919092737477?text=Hi%20JM%20Vertex,%20I%20want%20to%20build%20an%20e-commerce%20website." target="_blank" rel="noopener noreferrer" class="btn btn-ghost btn-sm">
                  Quote Project
                </a>
              </div>
            </div>
          </div>

          <!-- Work 4: AgriSense IoT Precision Agriculture -->
          <div class="work-browser-card">
            <div class="work-browser-header">
              <div class="work-browser-dots">
                <span class="work-browser-dot"></span>
                <span class="work-browser-dot"></span>
                <span class="work-browser-dot"></span>
              </div>
              <span class="work-browser-url">https://agrisense.iot-telemetry.in</span>
            </div>
            <div class="work-preview-img-wrap">
              <img src="https://images.unsplash.com/photo-1586771107445-d3ca888129ff?auto=format&fit=crop&q=80&w=800" alt="AgriSense IoT Precision Agriculture">
              <span class="work-badge-live" style="color: var(--cyan); border-color: rgba(0, 240, 255, 0.4);">
                <span class="live-dot" style="background: var(--cyan); box-shadow: 0 0 6px var(--cyan);"></span> IEEE JOURNAL PUBLISHED
              </span>
            </div>
            <div class="work-content-body">
              <div class="work-metric-chip" style="color: var(--cyan); border-color: rgba(0, 240, 255, 0.3); background: rgba(0, 240, 255, 0.08);">
                ⚡ 40% WATER CONSERVATION • REAL-TIME MQTT
              </div>
              <h3 class="card-title" style="margin-bottom: 0.5rem; font-size: 1.4rem;">AgriSense IoT — Smart Agriculture Environmental Telemetry</h3>
              <p style="color: var(--paper-soft); font-size: 0.9rem; line-height: 1.6; margin-bottom: 1.25rem;">
                Precision crop telemetry system measuring soil NPK levels, moisture, and ambient weather with automated solar-powered irrigation valves and AWS IoT data pipelines.
              </p>
              <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 1.75rem;">
                <span class="tag-mono tag-cyan">IOT SENSORS</span>
                <span class="tag-mono">MQTT</span>
                <span class="tag-mono">PYTHON</span>
                <span class="tag-mono">AWS CLOUD</span>
              </div>
              <div style="display: flex; gap: 0.75rem; margin-top: auto;">
                <a href="student-projects.html" class="btn btn-primary btn-sm" style="flex: 1;">
                  Explore IEEE Projects {ICONS['arrow_right']}
                </a>
                <a href="https://wa.me/919092737477?text=Hi%20JM%20Vertex,%20I%20am%20interested%20in%20an%20IoT%20academic%20project." target="_blank" rel="noopener noreferrer" class="btn btn-ghost btn-sm">
                  Request Base Paper
                </a>
              </div>
            </div>
          </div>

        </div>
      </div>
    </section>

    <!-- [03] Student Hall of Fame — Verified Success -->
    <section class="section-block">
      <div class="container">
        <div style="margin-bottom: 3.5rem;">
          <span class="eyebrow"><span class="dot"></span> [03] // VERIFIED ALUMNI SUCCESS</span>
          <h2 class="section-display-title" style="margin-top: 0.75rem;">
            STUDENT <span style="color: var(--emerald);">HALL OF FAME.</span>
          </h2>
          <p style="color: var(--paper-mute); max-width: 600px; margin-top: 0.75rem; font-size: 0.95rem;">
            Real students from premier engineering colleges who built their final year projects, published IEEE papers, and secured corporate placements with JM Vertex.
          </p>
        </div>

        <div class="bento-grid-3">
          <!-- Student 1: Suriya -->
          <div class="studio-card">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1.5rem;">
              <div style="width: 48px; height: 48px; background: var(--bg-elevated); border: 1px solid var(--rule-strong); border-radius: 8px; display: flex; align-items: center; justify-content: center; font-weight: 800; color: #fff; font-family: var(--font-display);">S</div>
              <span class="tag-mono tag-emerald">7.5 LPA TIER</span>
            </div>
            <h3 style="font-size: 1.35rem; color: #fff; margin-bottom: 0.25rem;">Suriya</h3>
            <p style="font-family: var(--font-mono); font-size: 0.785rem; color: var(--paper-mute); margin-bottom: 1.25rem;">Karpagam College of Engineering</p>
            
            <div style="background: var(--bg-deep); border-left: 2px solid var(--emerald); padding: 0.85rem 1rem; border-radius: 4px; margin-bottom: 1.25rem;">
              <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--emerald); text-transform: uppercase; display: block; margin-bottom: 2px;">PLACED AT:</span>
              <strong style="color: #fff; font-size: 1rem;">TCS Digital — 7.5 LPA</strong>
            </div>

            <p style="font-size: 0.875rem; color: var(--paper-soft); margin-bottom: 1.25rem;">
              <strong style="color: #fff;">Project:</strong> AI-Powered Resume Screener
            </p>
            <div style="display: flex; gap: 0.4rem; flex-wrap: wrap;">
              <span class="tag-mono">PYTHON</span>
              <span class="tag-mono">NLP</span>
              <span class="tag-mono">REACT</span>
            </div>
          </div>

          <!-- Student 2: Vishal -->
          <div class="studio-card">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1.5rem;">
              <div style="width: 48px; height: 48px; background: var(--bg-elevated); border: 1px solid var(--rule-strong); border-radius: 8px; display: flex; align-items: center; justify-content: center; font-weight: 800; color: var(--cyan); font-family: var(--font-display);">V</div>
              <span class="tag-mono tag-cyan">BEST PROJECT AWARD</span>
            </div>
            <h3 style="font-size: 1.35rem; color: #fff; margin-bottom: 0.25rem;">Vishal</h3>
            <p style="font-family: var(--font-mono); font-size: 0.785rem; color: var(--paper-mute); margin-bottom: 1.25rem;">Thiagarajar Engineering College</p>
            
            <div style="background: var(--bg-deep); border-left: 2px solid var(--cyan); padding: 0.85rem 1rem; border-radius: 4px; margin-bottom: 1.25rem;">
              <span style="font-family: var(--font-mono); font-size: 0.7rem; color: var(--cyan); text-transform: uppercase; display: block; margin-bottom: 2px;">HONOR:</span>
              <strong style="color: #fff; font-size: 1rem;">Best Final Year Project Award 2023</strong>
            </div>

            <p style="font-size: 0.875rem; color: var(--paper-soft); margin-bottom: 1.25rem;">
              <strong style="color: #fff;">Project:</strong> E-Commerce Analytics Dashboard
            </p>
            <div style="display: flex; gap: 0.4rem; flex-wrap: wrap;">
              <span class="tag-mono">REACT</span>
              <span class="tag-mono">NODE.JS</span>
              <span class="tag-mono">MONGODB</span>
            </div>
          </div>

          <!-- Student 3: Harsha -->
          <div class="studio-card">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 1.5rem;">
              <div style="width: 48px; height: 48px; background: var(--bg-elevated); border: 1px solid var(--rule-strong); border-radius: 8px; display: flex; align-items: center; justify-content: center; font-weight: 800; color: #a78bfa; font-family: var(--font-display);">H</div>
              <span class="tag-mono tag-emerald">IEEE JOURNAL</span>
            </div>
            <h3 style="font-size: 1.35rem; color: #fff; margin-bottom: 0.25rem;">Harsha</h3>
            <p style="font-family: var(--font-mono); font-size: 0.785rem; color: var(--paper-mute); margin-bottom: 1.25rem;">Sri Eshwar College Of Engineering</p>
            
            <div style="background: var(--bg-deep); border-left: 2px solid #a78bfa; padding: 0.85rem 1rem; border-radius: 4px; margin-bottom: 1.25rem;">
              <span style="font-family: var(--font-mono); font-size: 0.7rem; color: #a78bfa; text-transform: uppercase; display: block; margin-bottom: 2px;">RESEARCH OUTCOME:</span>
              <strong style="color: #fff; font-size: 1rem;">Published in Peer-Reviewed IEEE</strong>
            </div>

            <p style="font-size: 0.875rem; color: var(--paper-soft); margin-bottom: 1.25rem;">
              <strong style="color: #fff;">Project:</strong> Smart Agriculture IoT System
            </p>
            <div style="display: flex; gap: 0.4rem; flex-wrap: wrap;">
              <span class="tag-mono">IOT</span>
              <span class="tag-mono">PYTHON</span>
              <span class="tag-mono">AWS</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- [04] Testimonials — Verified Feedback -->
    <section class="section-block" style="background: #08090d; border-top: 1px solid var(--rule); border-bottom: 1px solid var(--rule);">
      <div class="container">
        <div style="margin-bottom: 3.5rem;">
          <span class="eyebrow"><span class="dot"></span> [04] // CLIENT &amp; STUDENT VOICES</span>
          <h2 class="section-display-title" style="margin-top: 0.75rem;">
            AUTHENTIC <span style="color: var(--emerald);">FEEDBACK.</span>
          </h2>
        </div>

        <div class="bento-grid-3" style="margin-bottom: 3rem;">
          <div class="studio-card" style="display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="color: #fbbf24; font-size: 1.1rem; margin-bottom: 1rem;">★★★★★</div>
              <p style="color: var(--paper-soft); font-size: 0.95rem; line-height: 1.7;">
                "The web development internship at JM Vertex completely changed my career trajectory. The mentors are incredibly supportive and the hands-on projects gave me the confidence to ace my technical interviews."
              </p>
            </div>
            <div style="border-top: 1px solid var(--rule); padding-top: 1rem; margin-top: 1.5rem;">
              <strong style="color: #fff; font-size: 0.95rem; display: block;">Rohan Sharma</strong>
              <span style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--paper-mute);">Sri Krishna College of Engineering</span>
            </div>
          </div>

          <div class="studio-card" style="display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="color: #fbbf24; font-size: 1.1rem; margin-bottom: 1rem;">★★★★★</div>
              <p style="color: var(--paper-soft); font-size: 0.95rem; line-height: 1.7;">
                "JM Vertex built our restaurant website (pizzacrave.in) faster than we expected. The design is modern, and the WhatsApp ordering integration has significantly boosted our direct sales."
              </p>
            </div>
            <div style="border-top: 1px solid var(--rule); padding-top: 1rem; margin-top: 1.5rem;">
              <strong style="color: #fff; font-size: 0.95rem; display: block;">Pizza Crave Team</strong>
              <span style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--paper-mute);">pizzacrave.in • Commercial Client</span>
            </div>
          </div>

          <div class="studio-card" style="display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <div style="color: #fbbf24; font-size: 1.1rem; margin-bottom: 1rem;">★★★★★</div>
              <p style="color: var(--paper-soft); font-size: 0.95rem; line-height: 1.7;">
                "Learning German felt intimidating at first, but the structured approach and interactive sessions made it so easy. I cleared my Goethe A1 certification on the very first attempt!"
              </p>
            </div>
            <div style="border-top: 1px solid var(--rule); padding-top: 1rem; margin-top: 1.5rem;">
              <strong style="color: #fff; font-size: 0.95rem; display: block;">Sneha Patel</strong>
              <span style="font-family: var(--font-mono); font-size: 0.75rem; color: var(--paper-mute);">PSG College of Technology</span>
            </div>
          </div>
        </div>

        <div style="text-align: center;">
          <button class="btn btn-ghost" onclick="openModal('review-modal')">
            ★ Submit Your Verified Review
          </button>
        </div>
      </div>
    </section>

    <!-- [05] Leadership Desk — Founders Joshua J & Madhav Adithya S -->
    <section class="section-block">
      <div class="container">
        <div style="margin-bottom: 3.5rem; text-align: center;">
          <span class="eyebrow"><span class="dot"></span> [05] // EXECUTIVE LEADERSHIP</span>
          <h2 class="section-display-title" style="margin-top: 0.75rem;">
            MEET THE <span style="color: var(--emerald);">FOUNDERS.</span>
          </h2>
          <p style="color: var(--paper-mute); max-width: 540px; margin: 0.75rem auto 0; font-size: 0.95rem;">
            Direct access to decision-makers. No account managers or middle tiers.
          </p>
        </div>

        <div class="bento-grid-2" style="max-width: 940px; margin: 0 auto;">
          <!-- Joshua J -->
          <div class="studio-card" style="text-align: center; padding: 3rem 2rem;">
            <div style="width: 72px; height: 72px; background: var(--bg-elevated); border: 2px solid var(--emerald); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 800; color: #fff; font-family: var(--font-display); margin: 0 auto 1.5rem;">JJ</div>
            <h3 style="font-size: 1.5rem; color: #fff; margin-bottom: 0.25rem;">Joshua J</h3>
            <span class="tag-mono tag-emerald" style="margin-bottom: 1.25rem;">FOUNDER &amp; TECHNICAL DIRECTOR</span>
            <p style="color: var(--paper-soft); font-size: 0.9rem; line-height: 1.6; margin-bottom: 2rem;">
              Directing core system architecture, React &amp; Vite full-stack production pipelines, and IEEE student research mentorship across AI and distributed networks.
            </p>
            <div style="display: flex; gap: 0.75rem; justify-content: center; flex-wrap: wrap;">
              <a href="tel:+919092737477" class="btn btn-ghost btn-sm">
                {ICONS['phone']} +91 90927 37477
              </a>
              <a href="https://wa.me/919092737477" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp btn-sm">
                {ICONS['whatsapp']} WhatsApp
              </a>
            </div>
          </div>

          <!-- Madhav Adithya S -->
          <div class="studio-card" style="text-align: center; padding: 3rem 2rem;">
            <div style="width: 72px; height: 72px; background: var(--bg-elevated); border: 2px solid var(--cyan); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: 800; color: #fff; font-family: var(--font-display); margin: 0 auto 1.5rem;">MA</div>
            <h3 style="font-size: 1.5rem; color: #fff; margin-bottom: 0.25rem;">Madhav Adithya S</h3>
            <span class="tag-mono tag-cyan" style="margin-bottom: 1.25rem;">CO-FOUNDER &amp; OPERATIONS</span>
            <p style="color: var(--paper-soft); font-size: 0.9rem; line-height: 1.6; margin-bottom: 2rem;">
              Directing academic partnerships, German &amp; Japanese global language training cohorts, client operations, and European university admission pathways.
            </p>
            <div style="display: flex; gap: 0.75rem; justify-content: center; flex-wrap: wrap;">
              <a href="tel:+919345699376" class="btn btn-ghost btn-sm">
                {ICONS['phone']} +91 93456 99376
              </a>
              <a href="https://wa.me/919345699376" target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp btn-sm">
                {ICONS['whatsapp']} WhatsApp
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- [06] FAQs Registry -->
    <section class="section-block" style="background: #08090d; border-top: 1px solid var(--rule); border-bottom: 1px solid var(--rule);">
      <div class="container" style="max-width: 900px;">
        <div style="margin-bottom: 3rem;">
          <span class="eyebrow"><span class="dot"></span> [06] // FREQUENT INQUIRIES</span>
          <h2 class="section-display-title" style="margin-top: 0.75rem;">
            SYSTEM <span style="color: var(--emerald);">CLARIFICATIONS.</span>
          </h2>
        </div>

        <div style="display: flex; flex-direction: column; gap: 1rem;">
          <div class="studio-card" style="padding: 1.75rem 2rem;">
            <h4 style="font-family: var(--font-display); font-size: 1.15rem; color: #fff; margin-bottom: 0.5rem;">Do I need prior coding experience to join the internship cohorts?</h4>
            <p style="color: var(--paper-soft); font-size: 0.925rem; line-height: 1.6;">
              Not at all! Our training tracks are engineered progressively from ground zero. We start with foundational programming and advance into real-world architecture, suitable for both beginners and experienced coders.
            </p>
          </div>

          <div class="studio-card" style="padding: 1.75rem 2rem;">
            <h4 style="font-family: var(--font-display); font-size: 1.15rem; color: #fff; margin-bottom: 0.5rem;">How much does a custom business website cost?</h4>
            <p style="color: var(--paper-soft); font-size: 0.925rem; line-height: 1.6;">
              Pricing depends on scope, custom interactions, and backend complexity. We offer modular packages tailored for startups and local businesses. Connect directly on WhatsApp for an instant, transparent quote!
            </p>
          </div>

          <div class="studio-card" style="padding: 1.75rem 2rem;">
            <h4 style="font-family: var(--font-display); font-size: 1.15rem; color: #fff; margin-bottom: 0.5rem;">Do you provide full source code and documentation for college final year projects?</h4>
            <p style="color: var(--paper-soft); font-size: 0.925rem; line-height: 1.6;">
              Yes, 100%. All custom academic projects include clean GitHub-ready source code, database schemas, architecture flowcharts, IEEE-formatted reports, and personalized viva defense preparation.
            </p>
          </div>

          <div class="studio-card" style="padding: 1.75rem 2rem;">
            <h4 style="font-family: var(--font-display); font-size: 1.15rem; color: #fff; margin-bottom: 0.5rem;">Are the internship completion certificates verified?</h4>
            <p style="color: var(--paper-soft); font-size: 0.925rem; line-height: 1.6;">
              Yes! Upon successful completion of your internship project, you receive a tamper-proof, verified certificate from JM Vertex Technologies with individual verification IDs and recommendation letters.
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- [07] Direct Conversion Transmission Hub with Aligned Contact Cards -->
    <section class="section-block">
      <div class="container" style="max-width: 1100px;">
        <div style="display: grid; grid-template-columns: 1fr 1.35fr; gap: 2.5rem; align-items: stretch;">

          <!-- Left Col: Perfectly Aligned Contact Cards -->
          <div class="studio-card" style="padding: 2.5rem; display: flex; flex-direction: column; justify-content: space-between;">
            <div>
              <span class="eyebrow"><span class="dot"></span> DIRECT COMMISSIONS</span>
              <h3 class="card-title" style="font-size: 1.6rem; margin: 0.75rem 0 1rem;">Direct Channels</h3>
              <p style="color: var(--paper-mute); font-size: 0.9rem; line-height: 1.6; margin-bottom: 2rem;">
                Connect directly with leadership or dispatch an inquiry to receive a response within 15 minutes.
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

                <!-- WhatsApp -->
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

            <div style="margin-top: 2rem; padding-top: 1.25rem; border-top: 1px solid var(--rule);">
              <span class="tag-mono" style="font-size: 0.72rem;">📍 TAMIL NADU, INDIA • SERVING CLIENTS GLOBALLY</span>
            </div>
          </div>

          <!-- Right Col: Transmission Form -->
          <div class="studio-card" style="padding: 2.5rem; border-color: rgba(0, 255, 136, 0.4);">
            <div style="margin-bottom: 2rem;">
              <span class="tag-mono tag-emerald">INSTANT DISPATCH</span>
              <h3 class="card-title" style="font-size: 1.8rem; margin: 0.5rem 0 0.25rem;">Initiate Your Project</h3>
              <p style="color: var(--paper-mute); font-size: 0.875rem;">
                Fill details below for an automated WhatsApp deep-link connection.
              </p>
            </div>

            <form class="jm-inquiry-form">
              <input type="text" name="b_fax_code" style="display:none;" tabindex="-1" autocomplete="off">
              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1rem;">
                <div class="form-group" style="margin-bottom:0;">
                  <label class="form-label">FULL NAME *</label>
                  <input type="text" name="name" class="input-glass" placeholder="e.g. Suriya" required>
                </div>
                <div class="form-group" style="margin-bottom:0;">
                  <label class="form-label">WHATSAPP PHONE *</label>
                  <input type="tel" name="phone" class="input-glass" placeholder="+91 90927 37477" required>
                </div>
              </div>

              <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin-bottom: 1rem;">
                <div class="form-group" style="margin-bottom:0;">
                  <label class="form-label">EMAIL ADDRESS *</label>
                  <input type="email" name="email" class="input-glass" placeholder="name@domain.com" required>
                </div>
                <div class="form-group" style="margin-bottom:0;">
                  <label class="form-label">INTEREST AREA *</label>
                  <select name="interest" class="input-glass" style="background:#090a0f;" required>
                    <option value="Website Development">Website Development</option>
                    <option value="Final Year / Academic Project">Final Year / Academic Project</option>
                    <option value="Internship &amp; Tech Training">Internship &amp; Tech Training</option>
                    <option value="German Language Course">German Language Course</option>
                    <option value="Japanese Language Course">Japanese Language Course</option>
                  </select>
                </div>
              </div>

              <div class="form-group">
                <label class="form-label">PROJECT SCOPE / OBJECTIVES *</label>
                <textarea name="message" class="input-glass" placeholder="Tell us about your requirements, project timeline, or learning goals..." style="min-height: 100px;" required></textarea>
              </div>

              <button type="submit" class="btn btn-primary" style="width: 100%; padding-block: 1rem !important;" data-cursor-text="TRANSMIT">
                Transmit Inquiry &amp; Open WhatsApp {ICONS['whatsapp']}
              </button>
            </form>
          </div>

        </div>
      </div>
    </section>
    """

    footer = render_footer()
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(head + header + body + footer)
    print("Rebuilt index.html with exact stats (100+ Students, 20+ Projects, 30+ Websites, 15+ Colleges) & Aligned Contact Icons.")

if __name__ == "__main__":
    build_index()
