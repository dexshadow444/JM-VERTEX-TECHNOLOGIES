import html
from base_templates import render_head, render_header, render_footer, ICONS

def write_page(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated: {filename}")

# ==============================================================================
# GERMAN LANGUAGE COURSE
# ==============================================================================
def build_german():
    head = render_head(
        "German Language Classes & A1-B2 Goethe Prep | JM Vertex Technologies",
        "Master the German language with certified coaching. Complete A1 to B2 levels, Goethe-Zertifikat exam preparation, and German public university admission guidance.",
        "german-language-course.html"
    )
    header = render_header("lang")

    body = f"""
    <section class="section section-hero">
      <div class="container text-center">
        <div class="reveal-on-scroll">
          <div class="pill-badge"><span class="pill-dot"></span> Foreign Language Academy</div>
          <h1 class="heading-xl" style="margin-bottom: 1.5rem;">
            Master German & Unlock <br>
            <span class="text-gradient">Tuition-Free Education in Europe</span>
          </h1>
          <p class="subheading" style="margin-bottom: 2.5rem;">
            German public universities offer tuition-free bachelor's and master's degrees to international students. We provide comprehensive German language coaching from absolute beginner (A1) to professional fluency (B2) with certified Goethe exam drills.
          </p>
          <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
            <a href="https://wa.me/919092737477?text=Hi%20JM%20Vertex,%20I%20want%20to%20enroll%20in%20German%20Language%20classes." target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg">
              Enroll in German Batch {ICONS['arrow_right']}
            </a>
            <button class="btn btn-secondary btn-lg" onclick="openModal('syllabus-modal')">
              {ICONS['download']} Download German Curriculum
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Levels Grid -->
    <section class="section" style="background: rgba(9, 14, 26, 0.5);">
      <div class="container">
        <div class="section-title-wrap reveal-on-scroll">
          <span class="pill-badge"><span class="pill-dot"></span> CEFR Roadmap</span>
          <h2 class="heading-lg">German Proficiency <span class="text-gradient">Levels & Certifications</span></h2>
          <p class="subheading">Mapped directly to the Common European Framework of Reference for Languages (CEFR).</p>
        </div>

        <div class="bento-grid">
          <!-- A1 -->
          <div class="col-6 reveal-on-scroll delay-1">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%;">
              <span class="pill-badge" style="margin-bottom: 0.75rem;">Level A1 • Beginner</span>
              <h3 class="heading-sm" style="margin-bottom: 0.75rem;">Foundational German & Everyday Basics</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6; margin-bottom: 1.25rem;">
                Learn basic greetings, numbers, family introductions, grocery shopping, restaurant conversations, and sentence structures. Focuses on Goethe-Zertifikat A1 exam pass guarantees for spouse visas and university applications.
              </p>
              <div style="color: var(--primary-glow); font-size: 0.85rem; font-weight: 600;">Duration: 6 - 8 Weeks (45 Hours)</div>
            </div>
          </div>

          <!-- A2 -->
          <div class="col-6 reveal-on-scroll delay-2">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%;">
              <span class="pill-badge" style="margin-bottom: 0.75rem;">Level A2 • Elementary</span>
              <h3 class="heading-sm" style="margin-bottom: 0.75rem;">Routine Situations & Past Tense Communication</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6; margin-bottom: 1.25rem;">
                Expands vocabulary into work, shopping, local environment, and travel. Master past tenses (Perfekt / Präteritum), modal verbs, and prepositions with interactive conversational practice sessions.
              </p>
              <div style="color: var(--primary-glow); font-size: 0.85rem; font-weight: 600;">Duration: 8 Weeks (60 Hours)</div>
            </div>
          </div>

          <!-- B1 -->
          <div class="col-6 reveal-on-scroll delay-3">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%;">
              <span class="pill-badge" style="margin-bottom: 0.75rem;">Level B1 • Intermediate</span>
              <h3 class="heading-sm" style="margin-bottom: 0.75rem;">Independent User & Professional Communication</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6; margin-bottom: 1.25rem;">
                The benchmark level for German university admissions and vocational training (Ausbildung). Express opinions, formulate plans, write formal emails, and comprehend complex technical articles.
              </p>
              <div style="color: var(--primary-glow); font-size: 0.85rem; font-weight: 600;">Duration: 10 Weeks (80 Hours)</div>
            </div>
          </div>

          <!-- B2 -->
          <div class="col-6 reveal-on-scroll delay-4">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%;">
              <span class="pill-badge" style="margin-bottom: 0.75rem;">Level B2 • Upper Intermediate</span>
              <h3 class="heading-sm" style="margin-bottom: 0.75rem;">Advanced Professional & Academic Fluency</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6; margin-bottom: 1.25rem;">
                Understand complex texts on both concrete and abstract topics, including technical discussions in your field of engineering or IT. Ideal for direct corporate hiring in Germany, Austria, and Switzerland.
              </p>
              <div style="color: var(--primary-glow); font-size: 0.85rem; font-weight: 600;">Duration: 12 Weeks (100 Hours)</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Higher Education Guidance -->
    <section class="section">
      <div class="container text-center">
        <div class="glass-panel" style="padding: 3.5rem 2.5rem; max-width: 900px; margin: 0 auto; border-color: rgba(34, 197, 94, 0.4);">
          <span class="pill-badge"><span class="pill-dot"></span> Study in Germany</span>
          <h2 class="heading-md" style="margin-bottom: 1rem;">Free Higher Education in Germany Guidance</h2>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.7; margin-bottom: 2rem;">
            Our mentors assist students through the entire German university pipeline: selecting English/German-taught master's courses at top TU9 universities, drafting Statements of Purpose (SOP), preparing for APS India certification, and opening blocked bank accounts.
          </p>
          <a href="https://wa.me/919092737477?text=Hi%20JM%20Vertex,%20I%20want%20guidance%20for%20studying%20in%20Germany." target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp btn-lg">
            {ICONS['whatsapp']} Book Free Study in Germany Consultation
          </a>
        </div>
      </div>
    </section>
    """
    footer = render_footer()
    write_page("german-language-course.html", head + header + body + footer)

# ==============================================================================
# JAPANESE LANGUAGE COURSE
# ==============================================================================
def build_japanese():
    head = render_head(
        "Japanese Language Classes & JLPT N5-N1 Prep | JM Vertex Technologies",
        "Master the Japanese language with expert native coaching. Comprehensive training for JLPT N5 to N1 levels, Kanji writing, conversational fluency, and Japanese engineering career guidance.",
        "japanese-language-course.html"
    )
    header = render_header("lang")

    body = f"""
    <section class="section section-hero">
      <div class="container text-center">
        <div class="reveal-on-scroll">
          <div class="pill-badge"><span class="pill-dot"></span> Foreign Language Academy</div>
          <h1 class="heading-xl" style="margin-bottom: 1.5rem;">
            Master Japanese & Access High-Tech <br>
            <span class="text-gradient">Engineering Careers in Japan</span>
          </h1>
          <p class="subheading" style="margin-bottom: 2.5rem;">
            Japan is rapidly recruiting international engineers, IT developers, and researchers. Learn Japanese from certified instructors covering Hiragana, Katakana, Kanji, and JLPT (Japanese Language Proficiency Test) certifications.
          </p>
          <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
            <a href="https://wa.me/919092737477?text=Hi%20JM%20Vertex,%20I%20want%20to%20enroll%20in%20Japanese%20Language%20classes." target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg">
              Enroll in Japanese Batch {ICONS['arrow_right']}
            </a>
            <button class="btn btn-secondary btn-lg" onclick="openModal('syllabus-modal')">
              {ICONS['download']} Download JLPT Curriculum
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- JLPT Levels Grid -->
    <section class="section" style="background: rgba(9, 14, 26, 0.5);">
      <div class="container">
        <div class="section-title-wrap reveal-on-scroll">
          <span class="pill-badge"><span class="pill-dot"></span> JLPT Roadmap</span>
          <h2 class="heading-lg">Japanese Proficiency <span class="text-gradient">Levels (JLPT N5 to N1)</span></h2>
          <p class="subheading">Targeted training structured specifically for the Japanese Language Proficiency Test.</p>
        </div>

        <div class="bento-grid">
          <!-- N5 -->
          <div class="col-6 reveal-on-scroll delay-1">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%;">
              <span class="pill-badge" style="margin-bottom: 0.75rem;">Level JLPT N5 • Beginner</span>
              <h3 class="heading-sm" style="margin-bottom: 0.75rem;">Hiragana, Katakana & Basic Kanji</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6; margin-bottom: 1.25rem;">
                Master reading and writing Hiragana and Katakana phonetic scripts, essential 100+ Kanji characters, standard grammatical particles (wa, ga, o, ni, de), and everyday conversational phrases.
              </p>
              <div style="color: var(--primary-glow); font-size: 0.85rem; font-weight: 600;">Duration: 8 Weeks (60 Hours)</div>
            </div>
          </div>

          <!-- N4 -->
          <div class="col-6 reveal-on-scroll delay-2">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%;">
              <span class="pill-badge" style="margin-bottom: 0.75rem;">Level JLPT N4 • Elementary</span>
              <h3 class="heading-sm" style="margin-bottom: 0.75rem;">Everyday Japanese & 300+ Kanji</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6; margin-bottom: 1.25rem;">
                Understand passages on familiar daily topics written in basic vocabulary and Kanji. Learn te-form verbs, conditional clauses, honorific basics, and conversational listening comprehension.
              </p>
              <div style="color: var(--primary-glow); font-size: 0.85rem; font-weight: 600;">Duration: 10 Weeks (75 Hours)</div>
            </div>
          </div>

          <!-- N3 -->
          <div class="col-6 reveal-on-scroll delay-3">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%;">
              <span class="pill-badge" style="margin-bottom: 0.75rem;">Level JLPT N3 • Intermediate</span>
              <h3 class="heading-sm" style="margin-bottom: 0.75rem;">Bridging to Professional Workplace Japanese</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6; margin-bottom: 1.25rem;">
                The essential gateway qualification for tech job seekers and visa applicants in Japan. Understand everyday articles, grasp summarizing content, and conduct coherent workplace conversations.
              </p>
              <div style="color: var(--primary-glow); font-size: 0.85rem; font-weight: 600;">Duration: 12 Weeks (90 Hours)</div>
            </div>
          </div>

          <!-- N2 / N1 -->
          <div class="col-6 reveal-on-scroll delay-4">
            <div class="glass-panel" style="padding: 2.25rem; height: 100%;">
              <span class="pill-badge" style="margin-bottom: 0.75rem;">Level JLPT N2 / N1 • Advanced</span>
              <h3 class="heading-sm" style="margin-bottom: 0.75rem;">Business Japanese & Engineering Fluency</h3>
              <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6; margin-bottom: 1.25rem;">
                Understand business presentations, complex software specifications, editorial newspapers, and advanced Keigo (formal business honorific speech). Guarantees top corporate compensation tiers.
              </p>
              <div style="color: var(--primary-glow); font-size: 0.85rem; font-weight: 600;">Duration: 14 Weeks (110 Hours)</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Japan Career Transition -->
    <section class="section">
      <div class="container text-center">
        <div class="glass-panel" style="padding: 3.5rem 2.5rem; max-width: 900px; margin: 0 auto; border-color: rgba(34, 197, 94, 0.4);">
          <span class="pill-badge"><span class="pill-dot"></span> Work in Japan</span>
          <h2 class="heading-md" style="margin-bottom: 1rem;">Career Pathways for Engineers in Tokyo & Osaka</h2>
          <p style="color: var(--text-muted); font-size: 0.95rem; line-height: 1.7; margin-bottom: 2rem;">
            Through our industry connections and Japanese language training, engineering graduates can tap into high-demand developer visas and graduate school scholarships (MEXT) across Japan.
          </p>
          <a href="https://wa.me/919092737477?text=Hi%20JM%20Vertex,%20I%20want%20information%20on%20Japanese%20courses%20and%20career%20guidance." target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp btn-lg">
            {ICONS['whatsapp']} Inquire Japanese Batches on WhatsApp
          </a>
        </div>
      </div>
    </section>
    """
    footer = render_footer()
    write_page("japanese-language-course.html", head + header + body + footer)

build_german()
build_japanese()
