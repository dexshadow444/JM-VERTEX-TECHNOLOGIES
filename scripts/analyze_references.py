import urllib.request
import re

urls = [
    'https://www.bdsn.club/',
    'https://eszterbial.com/',
    'https://unseen.co/',
    'https://lusion.co/'
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'})
        with urllib.request.urlopen(req, timeout=12) as res:
            text = res.read().decode('utf-8', errors='ignore')
            print(f"=== {url} ===")
            title = re.search(r'<title>(.*?)</title>', text, re.I)
            print("Title:", title.group(1).strip() if title else "N/A")
            
            # CSS links & Fonts
            fonts = re.findall(r'fonts\.googleapis\.com[^\'"\s]+|use\.typekit\.net[^\'"\s]+', text)
            print("Fonts:", set(fonts))

            # Tech stack clues
            libraries = []
            for lib in ['three', 'gsap', 'lenis', 'locomotive', 'webgl', 'pixi', 'shader', 'canvas', 'framer-motion', 'splitting', 'barba']:
                if lib in text.lower():
                    libraries.append(lib)
            print("Detected Tech & Effects:", libraries)
            
            # Look for headline or typography samples
            h1s = re.findall(r'<h[1-2][^>]*>(.*?)</h[1-2]>', text, re.I | re.S)
            clean_h1s = [re.sub(r'<[^>]+>', '', h).strip() for h in h1s if len(h.strip()) > 3]
            print("Key Headings:", clean_h1s[:3])
            print("-" * 50)
    except Exception as e:
        print(f"Error {url}: {e}")
