import json
import html
from base_templates import render_head, render_header, render_footer, ICONS

def write_page(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Generated: {filename}")

TRAINING_TRACKS = [
    {
        "filename": "python-training.html",
        "title": "Python Full Stack Training Course | JM Vertex Technologies",
        "meta_desc": "Master Python from basics to advanced. Learn Django, Web Scraping, Pandas, and Automation with real-world projects and placement assistance.",
        "badge": "Backend & Automation Track",
        "hero_title": "Master Python <br><span class='text-gradient'>Development & Automation</span>",
        "hero_desc": "From core syntax to advanced data structures, automated web scraping, and production web frameworks with Django and FastAPI.",
        "duration": "6 - 8 Weeks",
        "icon": "code",
        "modules": [
            ("Core Python Fundamentals", "Variables, Data Types, Control Loops, Functions, OOP, Exception Handling."),
            ("Web Scraping & Crawling", "BeautifulSoup, Scrapy, and Selenium for automated data extraction from modern web apps."),
            ("Data Manipulation with Pandas", "NumPy arrays, Pandas DataFrames, and Matplotlib data visualization."),
            ("Backend Web Frameworks", "Building scalable RESTful APIs with Django and Flask with PostgreSQL database."),
            ("Automation & Scripting", "Automating repetitive workflows, Excel sheets, and file system tasks."),
            ("Capstone Project & Deployment", "Developing a complete production-grade application and deploying to cloud.")
        ]
    },
    {
        "filename": "full-stack-training.html",
        "title": "Full Stack Developer Training | MERN Stack Course | JM Vertex",
        "meta_desc": "Become a full-stack web developer. Master React, Node.js, Express, and MongoDB with our comprehensive MERN stack training program.",
        "badge": "Full Stack Engineering Track",
        "hero_title": "Master the Modern <br><span class='text-gradient'>MERN Web Stack</span>",
        "hero_desc": "Build scalable, responsive, and high-performance full stack web applications from scratch with modern React and Node.js.",
        "duration": "8 - 10 Weeks",
        "icon": "globe",
        "modules": [
            ("Modern Frontend Engineering", "HTML5, CSS3, ES6+ JavaScript, React 19, and Tailwind CSS responsive design."),
            ("Backend Architecture with Node", "Node.js runtime, Express framework, routing, middleware, and authentication."),
            ("Database Management", "MongoDB Atlas, Mongoose ODM, aggregation pipelines, and PostgreSQL relational basics."),
            ("RESTful API Design", "Designing clean, secure, and documented REST endpoints with JWT authentication."),
            ("State Management & React Hooks", "Context API, custom hooks, performance memoization, and API integrations."),
            ("Production Cloud Deployment", "Deploying frontend to Vercel/Netlify and backend to Render/AWS with CI/CD.")
        ]
    },
    {
        "filename": "cloud-computing-training.html",
        "title": "Cloud Computing & DevOps Course | AWS & GCP | JM Vertex",
        "meta_desc": "Learn Cloud Computing and DevOps engineering. Master AWS, Google Cloud, Docker, Kubernetes, and CI/CD pipelines with hands-on labs.",
        "badge": "Cloud & Infrastructure Track",
        "hero_title": "Architect Cloud Systems & <br><span class='text-gradient'>DevOps Infrastructure</span>",
        "hero_desc": "Master AWS, Google Cloud Platform, Docker containerization, Kubernetes cluster management, and Infrastructure as Code.",
        "duration": "8 Weeks",
        "icon": "server",
        "modules": [
            ("Cloud Foundations (AWS & GCP)", "Core cloud architecture, EC2 compute instances, S3 storage, and VPC virtual networking."),
            ("Identity & Security (IAM)", "Identity and Access Management, role policies, VPC security groups, and encryption keys."),
            ("Docker Containerization", "Building lightweight Docker images, multi-stage builds, and container networking."),
            ("Kubernetes Orchestration", "Pods, Deployments, Services, Ingress controllers, and cluster scaling."),
            ("Infrastructure as Code (IaC)", "Terraform fundamentals for automated, reproducible cloud provisioning."),
            ("CI/CD Automation Pipelines", "Automating builds, tests, and cloud deployments with GitHub Actions.")
        ]
    },
    {
        "filename": "ai-training.html",
        "title": "AI & Machine Learning Training Course | JM Vertex Technologies",
        "meta_desc": "Learn Artificial Intelligence, Deep Learning, and Computer Vision. Practical training with TensorFlow, PyTorch, and real-world datasets.",
        "badge": "Artificial Intelligence Track",
        "hero_title": "Shape the Future with <br><span class='text-gradient'>AI & Machine Learning</span>",
        "hero_desc": "From statistical regression and decision trees to deep convolutional neural networks, computer vision, and NLP architectures.",
        "duration": "8 - 10 Weeks",
        "icon": "brain",
        "modules": [
            ("Math & Foundations of AI", "Linear algebra, multivariable calculus, probability distributions, and Python for ML."),
            ("Supervised Learning", "Linear & Logistic Regression, Decision Trees, Random Forests, and Support Vector Machines."),
            ("Unsupervised Learning", "K-Means Clustering, Principal Component Analysis (PCA), and Anomaly Detection."),
            ("Deep Learning & Neural Networks", "Perceptrons, backpropagation, and Multi-Layer Perceptrons using TensorFlow & PyTorch."),
            ("Computer Vision & NLP", "CNNs for image classification and Transformers/RNNs for natural language processing."),
            ("Model Deployment & APIs", "Packaging ML models into lightweight FastAPI microservices for real-time inference.")
        ]
    },
    {
        "filename": "cybersecurity-training.html",
        "title": "Cybersecurity & Ethical Hacking Course | JM Vertex Technologies",
        "meta_desc": "Learn Cybersecurity and Ethical Hacking. Master Kali Linux, Network Security, and Web App Pentesting to protect digital assets.",
        "badge": "Security & Defense Track",
        "hero_title": "Become an Ethical Hacker & <br><span class='text-gradient'>Cyber Defense Specialist</span>",
        "hero_desc": "Learn to identify system vulnerabilities, conduct penetration tests, and defend critical networks against modern cyber threats.",
        "duration": "6 - 8 Weeks",
        "icon": "shield",
        "modules": [
            ("Cybersecurity Fundamentals", "Threat landscape, CIA triad, defense-in-depth, and security architecture."),
            ("Network Security & Packet Analysis", "TCP/IP handshake, Wireshark packet capture, firewall configuration, and VPNs."),
            ("Kali Linux & Penetration Testing", "Nmap network scanning, Metasploit exploitation, and privilege escalation."),
            ("Web Application Security", "OWASP Top 10 vulnerabilities: SQL Injection, Cross-Site Scripting (XSS), and CSRF."),
            ("Cryptography & Digital Signatures", "Symmetric/Asymmetric encryption, RSA, hashing algorithms, and PKI infrastructure."),
            ("Incident Response & CEH Prep", "Forensic basics, log auditing, threat containment, and Certified Ethical Hacker exam guidance.")
        ]
    },
    {
        "filename": "data-science-training.html",
        "title": "Data Science & Analytics Course | JM Vertex Technologies",
        "meta_desc": "Launch your career in Data Science. Learn Python, SQL, Tableau, and Predictive Modeling with hands-on industry projects.",
        "badge": "Analytics & Intelligence Track",
        "hero_title": "Turn Complex Data into <br><span class='text-gradient'>Actionable Intelligence</span>",
        "hero_desc": "Master data manipulation, advanced SQL querying, interactive executive dashboards with Tableau, and predictive analytics.",
        "duration": "8 Weeks",
        "icon": "database",
        "modules": [
            ("Data Science Toolkit", "Advanced Python, NumPy, Pandas, Jupyter Notebooks, and statistical workflows."),
            ("Advanced SQL & Relational Databases", "Complex joins, window functions, indexing, and data warehousing queries."),
            ("Data Wrangling & Cleaning", "Handling missing values, outlier detection, data normalization, and feature engineering."),
            ("Exploratory Data Analysis (EDA)", "Uncovering patterns, correlation heatmaps, and statistical distributions with Seaborn."),
            ("Business Intelligence & Tableau", "Building dynamic, interactive executive dashboards with Tableau and PowerBI."),
            ("Predictive Modeling Capstone", "Developing an end-to-end customer churn or sales forecasting model with live dataset.")
        ]
    }
]

def build_training_page(track):
    head = render_head(
        track['title'],
        track['meta_desc'],
        track['filename']
    )
    header = render_header("training")

    modules_html = ""
    for idx, (m_title, m_desc) in enumerate(track['modules'], 1):
        modules_html += f"""
        <div class="col-4 reveal-on-scroll delay-{(idx % 3) + 1}">
          <div class="glass-panel" style="padding: 2.25rem; height: 100%;">
            <span style="font-size: 1.8rem; font-weight: 800; color: var(--primary-glow); display:block; margin-bottom: 0.5rem;">0{idx}</span>
            <h3 class="heading-sm" style="margin-bottom: 0.5rem; color: #fff;">{m_title}</h3>
            <p style="color: var(--text-muted); font-size: 0.9rem; line-height: 1.6;">{m_desc}</p>
          </div>
        </div>
        """

    body = f"""
    <!-- Track Hero -->
    <section class="section section-hero">
      <div class="container text-center">
        <div class="reveal-on-scroll">
          <div class="pill-badge"><span class="pill-dot"></span> {track['badge']}</div>
          <h1 class="heading-xl" style="margin-bottom: 1.5rem;">
            {track['hero_title']}
          </h1>
          <p class="subheading" style="margin-bottom: 2rem;">
            {track['hero_desc']}
          </p>
          <div style="display: flex; gap: 0.75rem; justify-content: center; align-items: center; margin-bottom: 2.5rem; color: var(--primary-glow); font-weight: 600;">
            <span>Cohort Duration: {track['duration']}</span> • <span>Live Mentorship</span> • <span>Verified Certificate</span>
          </div>
          <div style="display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap;">
            <a href="https://wa.me/919092737477?text=Hi%20JM%20Vertex,%20I%20want%20to%20enroll%20in%20the%20{html.escape(track['badge'])}." target="_blank" rel="noopener noreferrer" class="btn btn-primary btn-lg">
              Enroll in Next Batch {ICONS['arrow_right']}
            </a>
            <button class="btn btn-secondary btn-lg" onclick="openModal('syllabus-modal')">
              {ICONS['download']} Download Full Syllabus
            </button>
          </div>
        </div>
      </div>
    </section>

    <!-- Detailed Curriculum Modules -->
    <section class="section" style="background: rgba(9, 14, 26, 0.5);">
      <div class="container">
        <div class="section-title-wrap reveal-on-scroll">
          <span class="pill-badge"><span class="pill-dot"></span> Curriculum</span>
          <h2 class="heading-lg">Comprehensive Course <span class="text-gradient">Module Breakdown</span></h2>
          <p class="subheading">Structured week-by-week roadmap engineered to take you from fundamentals to enterprise proficiency.</p>
        </div>

        <div class="bento-grid">
          {modules_html}
        </div>
      </div>
    </section>

    <!-- Learning Journey Steps -->
    <section class="section">
      <div class="container">
        <div class="section-title-wrap reveal-on-scroll">
          <span class="pill-badge"><span class="pill-dot"></span> The Journey</span>
          <h2 class="heading-lg">Our 4-Step <span class="text-gradient">Learning Framework</span></h2>
          <p class="subheading">How we guide every candidate to complete mastery.</p>
        </div>

        <div class="bento-grid">
          <div class="col-3 reveal-on-scroll delay-1">
            <div class="stat-card" style="text-align: left; height: 100%;">
              <span style="font-size: 2rem; font-weight: 800; color: var(--primary-glow); display:block; margin-bottom: 0.5rem;">Step 1</span>
              <h4 style="color:#fff; font-size: 1.1rem; margin-bottom: 0.5rem;">Foundations & Syntax</h4>
              <p style="color: var(--text-muted); font-size: 0.875rem;">Master core syntax, development tools, and best-practice engineering conventions.</p>
            </div>
          </div>

          <div class="col-3 reveal-on-scroll delay-2">
            <div class="stat-card" style="text-align: left; height: 100%;">
              <span style="font-size: 2rem; font-weight: 800; color: var(--primary-glow); display:block; margin-bottom: 0.5rem;">Step 2</span>
              <h4 style="color:#fff; font-size: 1.1rem; margin-bottom: 0.5rem;">Hands-on Mini Projects</h4>
              <p style="color: var(--text-muted); font-size: 0.875rem;">Build mini applications to reinforce concepts immediately after each theoretical module.</p>
            </div>
          </div>

          <div class="col-3 reveal-on-scroll delay-3">
            <div class="stat-card" style="text-align: left; height: 100%;">
              <span style="font-size: 2rem; font-weight: 800; color: var(--primary-glow); display:block; margin-bottom: 0.5rem;">Step 3</span>
              <h4 style="color:#fff; font-size: 1.1rem; margin-bottom: 0.5rem;">Framework Deep Dive</h4>
              <p style="color: var(--text-muted); font-size: 0.875rem;">Dive into enterprise tools, cloud integrations, and industry-standard architecture.</p>
            </div>
          </div>

          <div class="col-3 reveal-on-scroll delay-4">
            <div class="stat-card" style="text-align: left; height: 100%;">
              <span style="font-size: 2rem; font-weight: 800; color: var(--primary-glow); display:block; margin-bottom: 0.5rem;">Step 4</span>
              <h4 style="color:#fff; font-size: 1.1rem; margin-bottom: 0.5rem;">Capstone & Placement</h4>
              <p style="color: var(--text-muted); font-size: 0.875rem;">Develop a portfolio capstone, polish your resume, and conduct mock technical interviews.</p>
            </div>
          </div>
        </div>

        <div style="text-align: center; margin-top: 3.5rem;">
          <a href="https://wa.me/919092737477?text=Hi%20JM%20Vertex,%20I%20want%20to%20register%20for%20the%20next%20batch." target="_blank" rel="noopener noreferrer" class="btn btn-whatsapp btn-lg">
            {ICONS['whatsapp']} Inquire Batch Timings on WhatsApp
          </a>
        </div>
      </div>
    </section>
    """

    footer = render_footer()
    write_page(track['filename'], head + header + body + footer)

for track in TRAINING_TRACKS:
    build_training_page(track)
