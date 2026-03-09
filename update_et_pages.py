#!/usr/bin/env python3
"""
Update all ET pages to use the new design from et/home.html.
Preserves each page's <main> content, meta tags, structured data, canonical, hreflang.
Replaces: fonts, CSS, header, footer, fixed elements, scripts.
"""
import os
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent
HOME = BASE / 'et' / 'home.html'

# ─── Extract from home.html ───────────────────────────────────────────────────
home_text = HOME.read_text(encoding='utf-8')

# New CSS
css_m = re.search(r'<style>(.*?)</style>', home_text, re.DOTALL)
NEW_CSS = css_m.group(1) if css_m else ''

# New fonts block
NEW_FONTS = """  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=DM+Serif+Display&display=swap" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=DM+Serif+Display&display=swap"></noscript>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0">"""

# New footer
NEW_FOOTER = """  <!-- FOOTER -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <strong>MV Therapy</strong>
          <div>Medical Verified Therapy</div>
          <div style="margin-top:6px;font-size:.82rem;">© 2025 MV Therapy – Massaaž Pärnus</div>
          <div class="footer-social">
            <a href="https://www.facebook.com/profile.php?id=100090837369433" target="_blank" rel="noopener noreferrer" aria-label="Facebook">
              <img src="/public/img/fb_svg.png" alt="Facebook" width="32" height="32">
            </a>
            <a href="https://www.instagram.com/medmassaaz/" target="_blank" rel="noopener noreferrer" aria-label="Instagram" style="color:#fff;font-weight:700;font-size:.85rem;">IG</a>
            <a href="https://www.tiktok.com/@medmassaaz" target="_blank" rel="noopener noreferrer" aria-label="TikTok" style="color:#fff;font-weight:700;font-size:.85rem;">TT</a>
          </div>
        </div>
        <div>
          <strong>Aadress</strong>
          <div>Rüütli 47 II korrus</div>
          <div>80010 Pärnu, Eesti</div>
          <a href="/et/map.html" style="font-size:.85rem;">📍 Vaata kaardil</a>
        </div>
        <div>
          <strong>Kontakt</strong>
          <div><a href="tel:+37258189561">+372 5818 9561</a></div>
          <div><a href="mailto:info@mvtherapy.ee">info@mvtherapy.ee</a></div>
        </div>
        <div>
          <strong>Lehed</strong>
          <div><a href="/et/services.html">Teenused</a></div>
          <div><a href="/et/Diagnosis.html">Diagnoosid</a></div>
          <div><a href="/et/blog.html">Blogi</a></div>
          <div><a href="/et/kkk.html">KKK</a></div>
        </div>
      </div>
    </div>
  </footer>"""

# Fixed elements (go-top, mobile booking bar, cookie)
FIXED_ELEMENTS = """
  <!-- GO TOP -->
  <button class="go-top" id="goTop" aria-label="Keri lehe algusesse">
    <span class="material-symbols-outlined">expand_less</span>
  </button>

  <!-- STICKY MOBILE BOOKING BAR -->
  <div class="mobile-book-bar" id="mobileBookBar">
    <div class="book-info">
      <strong>MV Therapy</strong>
      Rüütli 47, Pärnu
    </div>
    <button class="btn btn-primary book-trigger">Broneeri</button>
  </div>

  <!-- COOKIE NOTICE -->
  <div id="cookieNotice" style="display:none;" role="dialog" aria-label="Küpsiste teade">
    <p>Kasutame küpsiseid teie sirvimiskogemuse parandamiseks, isikupärastatud sisu esitamiseks ja liikluse analüüsimiseks.</p>
    <button class="cookie-btn" id="cookieAccept">OK, nõustun</button>
  </div>"""

# Scripts
NEW_SCRIPTS = """
  <!-- === SCRIPTS === -->

  <!-- Scroll helper -->
  <script>
    function scrollEl(id, amount) {
      requestAnimationFrame(function() {
        var el = document.getElementById(id);
        if (el) el.scrollBy({ left: amount, behavior: 'smooth' });
      });
    }
  </script>

  <!-- Mobile menu, scroll-top, cookie, booking -->
  <script>
    document.addEventListener('DOMContentLoaded', function() {
      // Mobile menu
      var toggle = document.getElementById('mobileToggle');
      var panel = document.getElementById('mobilePanel');
      if (toggle && panel) {
        toggle.addEventListener('click', function() {
          var open = panel.classList.toggle('open');
          toggle.setAttribute('aria-expanded', String(open));
        });
        panel.querySelectorAll('a').forEach(function(a) {
          a.addEventListener('click', function() { panel.classList.remove('open'); toggle.setAttribute('aria-expanded','false'); });
        });
        document.addEventListener('click', function(e) {
          if (!toggle.contains(e.target) && !panel.contains(e.target)) {
            panel.classList.remove('open');
            toggle.setAttribute('aria-expanded','false');
          }
        });
      }

      // Booking triggers
      document.querySelectorAll('.book-trigger').forEach(function(btn) {
        btn.addEventListener('click', function(e) {
          e.preventDefault();
          var container = document.getElementById('broneeri-container');
          if (!container) return;
          container.style.cssText = 'height:auto;overflow:visible;';
          var slBtn = container.querySelector('.button-cta, button, [class*="button"], [class*="btn"]');
          if (slBtn) {
            slBtn.click();
            setTimeout(function() { container.style.cssText = 'height:0;overflow:hidden;margin:0;padding:0;'; }, 300);
          } else {
            setTimeout(function() {
              var retry = container.querySelector('.button-cta, button, [class*="button"], [class*="btn"]');
              if (retry) retry.click();
              setTimeout(function() { container.style.cssText = 'height:0;overflow:hidden;margin:0;padding:0;'; }, 300);
            }, 1000);
          }
        });
      });

      // Go top
      var goTop = document.getElementById('goTop');
      var scrollTimer;
      window.addEventListener('scroll', function() {
        if (scrollTimer) return;
        scrollTimer = setTimeout(function() {
          scrollTimer = null;
          if (goTop) goTop.style.display = window.scrollY > 300 ? 'grid' : 'none';
        }, 100);
      }, { passive: true });
      if (goTop) goTop.addEventListener('click', function() { window.scrollTo({ top: 0, behavior: 'smooth' }); });

      // Cookie
      var notice = document.getElementById('cookieNotice');
      var accept = document.getElementById('cookieAccept');
      if (notice && accept) {
        if (!localStorage.getItem('cookieAccepted')) {
          setTimeout(function() { notice.style.display = 'block'; }, 1200);
        }
        accept.addEventListener('click', function() {
          localStorage.setItem('cookieAccepted','true');
          notice.style.display = 'none';
        });
      }
    });
  </script>

  <!-- Scroll & entrance animations -->
  <script>
    (function() {
      if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
      function init() {
        var main = document.getElementById('content');
        if (!main) return;
        var hero = main.querySelector('.hero');
        if (hero) {
          var map = [
            ['.eyebrow','right',0],['h1','blur',.12],['.lead','up',.25],
          ];
          map.forEach(function(m) {
            var el = hero.querySelector(m[0]);
            if (el) { el.setAttribute('data-anim', m[1]); el.style.transitionDelay = m[2] + 's'; }
          });
          hero.querySelectorAll('.pill').forEach(function(p, i) {
            p.setAttribute('data-anim','pop'); p.style.transitionDelay = (.35 + i * .08) + 's';
          });
          hero.querySelectorAll('.trust').forEach(function(t, i) {
            t.setAttribute('data-anim','scale'); t.style.transitionDelay = (.42 + i * .1) + 's';
            t.style.setProperty('--float-d', (i * .6) + 's');
          });
          var heroImg = hero.querySelector('.hero-visual img');
          if (heroImg) { heroImg.setAttribute('data-anim','scale'); heroImg.style.transitionDelay = '.15s'; }
          var loc = hero.querySelector('.location-callout');
          if (loc) { loc.setAttribute('data-anim','up'); loc.style.transitionDelay = '.3s'; }
        }
        main.querySelectorAll('.section-head h2, .section-head .btn').forEach(function(el, i) {
          el.setAttribute('data-anim', i % 2 === 0 ? 'up' : 'left');
        });
        main.querySelectorAll('.scroll-track').forEach(function(track) {
          track.querySelectorAll('.s-card').forEach(function(card, i) {
            card.setAttribute('data-anim','up'); card.style.transitionDelay = (i * .07) + 's';
          });
        });
        main.querySelectorAll('.scroll-nav .scroll-arrow').forEach(function(btn, i) {
          btn.setAttribute('data-anim', i === 0 ? 'right' : 'left');
          btn.style.transitionDelay = '.2s';
        });
        main.querySelectorAll('.faq-item').forEach(function(faq, i) {
          faq.setAttribute('data-anim', i % 2 === 0 ? 'left' : 'right');
          faq.style.transitionDelay = (i * .08) + 's';
        });
        var video = main.querySelector('.video-wrap');
        if (video) { video.setAttribute('data-anim','scale'); }
        var vH = window.innerHeight || 700;
        var obs = new IntersectionObserver(function(entries) {
          entries.forEach(function(e) {
            if (e.isIntersecting) { e.target.classList.add('in'); obs.unobserve(e.target); }
          });
        }, { threshold: 0.06, rootMargin: '0px 0px -40px 0px' });
        main.querySelectorAll('[data-anim]').forEach(function(el) {
          var rect = el.getBoundingClientRect();
          if (rect.top < vH && rect.bottom > 0) setTimeout(function() { el.classList.add('in'); }, 80);
          else obs.observe(el);
        });
        main.querySelectorAll('.scroll-track').forEach(function(track) {
          track.addEventListener('scroll', function() {
            track.querySelectorAll('[data-anim]:not(.in)').forEach(function(card) {
              var r = card.getBoundingClientRect();
              if (r.left < window.innerWidth && r.right > 0) card.classList.add('in');
            });
          }, { passive: true });
        });
      }
      if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
      else init();
    })();
  </script>

  <!-- Elfsight Google Reviews -->
  <script src="https://static.elfsight.com/platform/platform.js" async></script>

  <!-- SalonLife Booking Widget -->
  <script>
    var book_texts = { et: 'Broneeri aeg', ru: 'Записаться на приём', en: 'Book appointment' };
    !function(e,n,t){
      var i=document,o="script",a=i.createElement(o),d=i.getElementsByTagName(o)[0];
      a.async=!0;a.defer=!0;
      a.src="//widget.salon.life/static/js/widget.js?t="+(new Date).getTime();
      n&&a.addEventListener("load",function(){t.SalonLifeCb=n},!1);
      d.parentNode.insertBefore(a,d)
    }(0,function(){
      window.SalonLifeWidget.mount({
        identifier:3986,button_text:book_texts.et,language:'et',color:'#44437d',container:'#broneeri-container'
      })
    },window);
  </script>

  <!-- Matomo Analytics -->
  <script>
    var _paq=window._paq=window._paq||[];
    _paq.push(['trackPageView']);_paq.push(['enableLinkTracking']);
    (function(){var u="//mvtherapy.ee/matomo/";
    _paq.push(['setTrackerUrl',u+'matomo.php']);_paq.push(['setSiteId','1']);
    var d=document,g=d.createElement('script'),s=d.getElementsByTagName('script')[0];
    g.async=true;g.src=u+'matomo.js';s.parentNode.insertBefore(g,s);})();
  </script>"""

# ─── Nav active section mapping ───────────────────────────────────────────────
def get_active_section(rel_path):
    """Return nav key for the given file path."""
    parts = rel_path.parts
    # parts[0] == 'et'
    if len(parts) == 2:
        name = parts[1]
        mapping = {
            'home.html': 'home',
            'index.html': 'home',
            'services.html': 'services',
            'Diagnosis.html': 'diagnosis',
            'campaign.html': 'campaign',
            'workshops.html': 'workshops',
            'team.html': 'team',
            'kkk.html': 'kkk',
            'blog.html': 'blog',
            'map.html': '',
        }
        return mapping.get(name, '')
    elif len(parts) == 3:
        folder = parts[1]
        mapping = {
            'services': 'services',
            'Diagnosis': 'diagnosis',
            'campaign': 'campaign',
            'workshops': 'workshops',
            'blog': 'blog',
        }
        return mapping.get(folder, '')
    return ''

# ─── Build new header ─────────────────────────────────────────────────────────
NAV_ITEMS = [
    ('/et/home.html',      'Avaleht',    'home'),
    ('/et/services.html',  'Massaažid',  'services'),
    ('/et/Diagnosis.html', 'Diagnoosid', 'diagnosis'),
    ('/et/campaign.html',  'Kampaaniad', 'campaign'),
    ('/et/workshops.html', 'Koolitused', 'workshops'),
    ('/et/team.html',      'Meeskond',   'team'),
    ('/et/kkk.html',       'KKK',        'kkk'),
    ('/et/blog.html',      'Blogi',      'blog'),
]

def build_header(et_url, ru_url, en_url, active_section):
    desktop = ''
    mobile = ''
    for href, label, key in NAV_ITEMS:
        cur = ' aria-current="page"' if key == active_section else ''
        desktop += f'\n        <a href="{href}"{cur}>{label}</a>'
        mobile  += f'\n          <a href="{href}">{label}</a>'

    return f"""  <a class="skip-link" href="#content">Liigu põhisisu juurde</a>

  <!-- ===== HEADER ===== -->
  <header class="site-header">
    <div class="container topbar">
      <a class="brand" href="/et/home.html" aria-label="MV Therapy avaleht">
        <div class="brand-logo" aria-hidden="true"></div>
        <div class="brand-text">
          <strong>MV Therapy</strong>
          <span>Medical Verified Therapy</span>
        </div>
      </a>
      <nav class="desktop-nav" aria-label="Peamenüü">{desktop}
      </nav>
      <div class="header-actions">
        <div class="mobile-lang-header" aria-label="Keeled">
          <a href="{et_url}" class="active">EST</a>
          <a href="{ru_url}">РУС</a>
          <a href="{en_url}">ENG</a>
        </div>
        <div class="lang-switch" aria-label="Keeled">
          <a href="{et_url}" class="active">EST</a>
          <a href="{ru_url}">РУС</a>
          <a href="{en_url}">ENG</a>
        </div>
        <button class="mobile-toggle" id="mobileToggle" aria-expanded="false" aria-controls="mobilePanel" aria-label="Ava menüü">
          <span class="material-symbols-outlined">menu</span>
        </button>
      </div>
    </div>
    <div class="mobile-panel" id="mobilePanel">
      <div class="container">
        <nav aria-label="Mobiilimenüü">{mobile}
        </nav>
      </div>
    </div>
  </header>"""

# ─── CSS filtering: remove old page base styles that conflict ─────────────────
# Selectors from old pages that we no longer need (header/nav/footer/body)
OLD_BASE_SELECTORS = [
    r'\*\s*\{', r'html\s*\{', r'body\s*\{', r'img\s*\{',
    r'a\s*\{', r'\.container\s*\{', r'\.sticky-wrapper\s*\{',
    r'main\s*\{',  # old pages had main { background: #fff } card style
    r'header\s*\{', r'\.logo\b', r'\.claim\b', r'\.language-menu\b',
    r'\.nav\b', r'\.nav-inner\b', r'\.nav-item\b', r'\.hamburger\b',
    r'footer\s*\{', r'\.flx-container\b', r'\.goTop\b', r'\.go-top\b',
    r'#scrollBtn\b', r'\.page-footer\b', r'\.site-footer\b',
    r'\.footer-grid\b', r'\.footer-social\b', r'\.footer-copy\b',
    r'#cookieNotice\b', r'\.mobile-book-bar\b',
    r'\.seo-section\b', r'\.seo-grid\b', r'\.seo-col\b',  # new CSS defines these
    r'h1\s*\{',  # new CSS defines h1 with DM Serif Display
]

def filter_old_css(css_text):
    """Remove CSS rules that conflict with new base CSS. Keep page-specific ones."""
    rules = []
    # Split into individual rules by tracking brace depth
    i = 0
    depth = 0
    current = ''
    while i < len(css_text):
        c = css_text[i]
        if c == '{':
            depth += 1
            current += c
        elif c == '}':
            depth -= 1
            current += c
            if depth == 0:
                rules.append(current.strip())
                current = ''
        else:
            current += c
        i += 1
    if current.strip():
        rules.append(current.strip())

    kept = []
    for rule in rules:
        # Get the selector part (before first {)
        brace_pos = rule.find('{')
        if brace_pos == -1:
            # Comment or plain text - skip if it's whitespace
            if rule.strip():
                kept.append(rule)
            continue
        selector = rule[:brace_pos].strip()
        # Check if this selector matches old base selectors we want to remove
        is_base = False
        for pat in OLD_BASE_SELECTORS:
            if re.search(pat, selector):
                is_base = True
                break
        # Also skip @media rules (they contain nested rules about header/footer)
        # We keep @media only if they contain page-specific content
        if selector.startswith('@media') and is_base:
            is_base = True
        if not is_base:
            kept.append(rule)

    return '\n\n'.join(kept)

# ─── Extract main content from HTML ──────────────────────────────────────────
def extract_main(html):
    """Extract content between <main...> and </main>."""
    m = re.search(r'(<main\b[^>]*>)(.*?)(</main>)', html, re.DOTALL | re.IGNORECASE)
    if m:
        open_tag, content, close_tag = m.group(1), m.group(2), m.group(3)
        # Ensure id="content" is on main and avoid duplicate id attributes.
        if 'id="content"' not in open_tag:
            open_tag = open_tag.replace('<main', '<main id="content"', 1)
        # If a legacy/generated page has a second id attribute, drop it.
        open_tag = re.sub(r'(<main\b[^>]*\bid="content"[^>]*?)\s+id="[^"]+"', r'\1', open_tag)
        return open_tag + content + close_tag
    return None

# ─── Extract head meta content (keep everything before fonts/style) ────────────
def extract_head_meta(html):
    """
    Extract head content to preserve: title, meta tags, structured data,
    canonical, hreflang, icons. Remove old font links and style blocks.
    """
    head_m = re.search(r'<head>(.*?)</head>', html, re.DOTALL | re.IGNORECASE)
    if not head_m:
        return ''
    head_content = head_m.group(1)

    # Remove <meta charset> (we add it in the template already)
    head_content = re.sub(r'\s*<meta\s+charset=[^>]+>\s*', '\n', head_content, flags=re.IGNORECASE)

    # Remove old font preload/link lines (Inter font, Google Fonts, Material Symbols)
    head_content = re.sub(
        r'\s*<link[^>]*(?:Inter|fonts\.googleapis\.com|fonts\.gstatic\.com|Material\+Symbols)[^>]*>\s*',
        '\n', head_content, flags=re.IGNORECASE
    )
    # Remove noscript blocks (old font noscript fallbacks)
    head_content = re.sub(
        r'\s*<noscript>.*?</noscript>\s*',
        '\n', head_content, flags=re.DOTALL | re.IGNORECASE
    )
    # Remove dns-prefetch for fonts/widget
    head_content = re.sub(
        r'\s*<link[^>]*dns-prefetch[^>]*>\s*',
        '\n', head_content, flags=re.IGNORECASE
    )
    # Remove preconnect links (we add our own)
    head_content = re.sub(
        r'\s*<link[^>]*rel=["\']preconnect["\'][^>]*>\s*',
        '\n', head_content, flags=re.IGNORECASE
    )
    # Remove external CSS links (style.css, services.css, etc.)
    head_content = re.sub(
        r'\s*<link[^>]*rel=["\']stylesheet["\'][^>]*>\s*',
        '\n', head_content, flags=re.IGNORECASE
    )
    # Remove old <style>...</style> blocks
    head_content = re.sub(r'\s*<style>.*?</style>\s*', '\n', head_content, flags=re.DOTALL)
    # Remove orphaned HTML comments that referenced removed content
    orphan_comments = [
        r'<!--\s*Resource Hints for Performance\s*-->',
        r'<!--\s*Preload Critical Resources\s*-->',
        r'<!--\s*Preload critical resources\s*-->',
        r'<!--\s*Stylesheets\s*-->',
        r'<!--\s*Fonts\s*-->',
        r'<!--\s*Updated viewport[^-]*-->',
        r'<!--\s*Theme color[^-]*-->',
        r'<!--\s*Pärnu therapy[^-]*-->',
    ]
    for pat in orphan_comments:
        head_content = re.sub(r'\s*' + pat + r'\s*', '\n', head_content, flags=re.IGNORECASE | re.DOTALL)
    # Fix indentation: ensure each line that starts with content gets 2 spaces
    lines = head_content.split('\n')
    fixed = []
    for line in lines:
        stripped = line.strip()
        if stripped:
            fixed.append('  ' + stripped)
        else:
            fixed.append('')
    head_content = '\n'.join(fixed)
    # Collapse multiple blank lines
    head_content = re.sub(r'\n{3,}', '\n\n', head_content)

    return head_content.strip('\n')

# ─── Standardise / clean SEO meta tags ───────────────────────────────────────
def clean_meta_seo(head_content):
    """
    Fix SEO meta tags to match home.html standard:
    - Remove keywords, author, publisher, copyright and other junk meta
    - Fix geo.region EE-68 → EE-67
    - Fix geo.placename to "Pärnu, Estonia"
    - Standardise robots content order
    - Fix viewport user-scalable=no → yes
    - Standardise twitter:* tags to use property= (not name=)
    - Add geo block if missing
    - Add og:image dimensions if og:image is present but dimensions are missing
    - Clean up inline width/height attributes from og:image tags
    """
    # 1. Remove tags we no longer want
    for pat in [
        r'\s*<meta\s+name=["\']keywords["\'][^>]*>\s*',
        r'\s*<meta\s+name=["\']author["\'][^>]*>\s*',
        r'\s*<meta\s+name=["\']publisher["\'][^>]*>\s*',
        r'\s*<meta\s+name=["\']copyright["\'][^>]*>\s*',
        r'\s*<meta\s+name=["\']googlebot["\'][^>]*>\s*',
        r'\s*<meta\s+name=["\']format-detection["\'][^>]*>\s*',
        r'\s*<meta\s+name=["\']msapplication-TileColor["\'][^>]*>\s*',
        r'\s*<meta\s+name=["\']rating["\'][^>]*>\s*',
        r'\s*<meta\s+name=["\']distribution["\'][^>]*>\s*',
        r'\s*<meta\s+name=["\']revisit-after["\'][^>]*>\s*',
        r'\s*<meta\s+http-equiv=["\']expires["\'][^>]*>\s*',
        r'\s*<meta\s+http-equiv=["\']cache-control["\'][^>]*>\s*',
        r'\s*<meta\s+name=["\']og:site_name["\'][^>]*>\s*',
    ]:
        head_content = re.sub(pat, '\n', head_content, flags=re.IGNORECASE)

    # 2. Fix geo.region EE-68 → EE-67
    head_content = re.sub(
        r'(content=["\'])EE-6[0-9](["\'])',
        r'\g<1>EE-67\2', head_content
    )

    # 3. Fix geo.placename → "Pärnu, Estonia"
    head_content = re.sub(
        r'(<meta\s+name=["\']geo\.placename["\']?\s+content=["\'])([^"\']+)(["\'])',
        lambda m: m.group(1) + 'Pärnu, Estonia' + m.group(3),
        head_content, flags=re.IGNORECASE
    )

    # 4. Standardise robots content to home.html order
    def fix_robots(m):
        return (m.group(1) +
                'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' +
                m.group(3))
    head_content = re.sub(
        r'(<meta\s+name=["\']robots["\'][^>]*content=["\'])([^"\']+)(["\'])',
        fix_robots, head_content, flags=re.IGNORECASE
    )
    head_content = re.sub(
        r'(<meta\s+content=["\'])([^"\']+)(["\'][^>]*name=["\']robots["\'])',
        lambda m: m.group(1) + 'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' + m.group(3),
        head_content, flags=re.IGNORECASE
    )

    # 5. Fix viewport user-scalable=no → yes
    head_content = re.sub(
        r'user-scalable=no', 'user-scalable=yes', head_content, flags=re.IGNORECASE
    )

    # 6. Standardise twitter:* tags: name= → property=
    head_content = re.sub(
        r'<meta\s+name=(["\'])(twitter:[^"\']+)(\1)',
        r'<meta property=\1\2\3',
        head_content, flags=re.IGNORECASE
    )

    # 7. Remove inline width/height attributes from og:image meta tags (not valid HTML meta attrs)
    head_content = re.sub(
        r'(<meta[^>]*property=["\']og:image["\'][^>]*)\s+width=["\'][^"\']*["\'](\s+height=["\'][^"\']*["\'])?',
        r'\1', head_content, flags=re.IGNORECASE
    )
    head_content = re.sub(
        r'(<meta[^>]*property=["\']og:image["\'][^>]*)\s+height=["\'][^"\']*["\']',
        r'\1', head_content, flags=re.IGNORECASE
    )

    # 8. Add og:image:width / og:image:height if og:image present but dimensions missing
    if re.search(r'property=["\']og:image["\']', head_content, re.IGNORECASE):
        if not re.search(r'property=["\']og:image:width["\']', head_content, re.IGNORECASE):
            head_content = re.sub(
                r'(<meta[^>]*property=["\']og:image["\'][^>]*>)',
                r'\1\n  <meta property="og:image:width" content="1200">\n  <meta property="og:image:height" content="630">',
                head_content, count=1, flags=re.IGNORECASE
            )

    # 9. Add missing geo tags block if none present
    if not re.search(r'geo\.region', head_content, re.IGNORECASE):
        geo_block = '''
  <!-- Geo Location Meta Tags -->
  <meta name="geo.region" content="EE-67">
  <meta name="geo.placename" content="Pärnu, Estonia">
  <meta name="geo.position" content="58.3859;24.4971">
  <meta name="ICBM" content="58.3859, 24.4971">'''
        # Insert after theme-color if present, else after apple-mobile-web-app-capable, else append
        if re.search(r'theme-color', head_content, re.IGNORECASE):
            head_content = re.sub(
                r'(<meta[^>]*theme-color[^>]*>)',
                r'\1' + geo_block, head_content, count=1, flags=re.IGNORECASE
            )
        else:
            head_content += geo_block

    # 10. Add apple-mobile-web-app-capable if missing
    if not re.search(r'apple-mobile-web-app-capable', head_content, re.IGNORECASE):
        head_content = re.sub(
            r'(<meta\s+name=["\']robots["\'][^>]*>)',
            r'<meta name="apple-mobile-web-app-capable" content="yes">\n  \1',
            head_content, count=1, flags=re.IGNORECASE
        )

    # 11. Add theme-color if missing
    if not re.search(r'theme-color', head_content, re.IGNORECASE):
        head_content = re.sub(
            r'(<meta\s+name=["\']robots["\'][^>]*>)',
            r'\1\n  <meta name="theme-color" content="#44437d">',
            head_content, count=1, flags=re.IGNORECASE
        )

    return head_content

# ─── Extract page-specific inline CSS ────────────────────────────────────────
def extract_page_css(html):
    """Extract CSS from <style> blocks that is page-specific (not base styles)."""
    styles = re.findall(r'<style>(.*?)</style>', html, re.DOTALL | re.IGNORECASE)
    if not styles:
        return ''

    marker = '/* === PAGE-SPECIFIC STYLES === */'
    all_css = '\n'.join(styles)

    # Idempotency: if the page already contains our generated marker, avoid
    # re-ingesting CSS from the generated file (it can contain a full copy of
    # base styles and would keep growing on each run).
    if marker in all_css:
        return ''

    filtered = filter_old_css(all_css)
    return filtered.strip()

# ─── Process a single file ───────────────────────────────────────────────────
def process_file(filepath):
    rel = filepath.relative_to(BASE)  # e.g. et/services.html
    html = filepath.read_text(encoding='utf-8')

    # Skip home.html (template, already done)
    if filepath == HOME:
        return False

    # Get URLs for lang switch
    # rel_from_et = path relative to /et/ e.g. services.html or services/1.html
    rel_from_et = str(rel).replace('et/', '', 1)  # e.g. "services.html" or "services/1.html"
    et_url = f'/et/{rel_from_et}'
    ru_url = f'/ru/{rel_from_et}'
    en_url = f'/en/{rel_from_et}'

    active_section = get_active_section(rel)

    # Extract parts from old file
    head_meta = extract_head_meta(html)
    head_meta = clean_meta_seo(head_meta)
    page_css = extract_page_css(html)
    main_content = extract_main(html)

    if main_content is None:
        print(f'  WARNING: No <main> found in {rel}, skipping')
        return False

    # Build CSS: new base + page-specific (page-specific after, so it can override)
    combined_css = NEW_CSS
    if page_css:
        combined_css += '\n\n    /* === PAGE-SPECIFIC STYLES === */\n    ' + page_css.replace('\n', '\n    ')

    # Build new header
    header_html = build_header(et_url, ru_url, en_url, active_section)

    # Check if broneeri-container exists in main, if not add it
    broneeri = ''
    if 'broneeri-container' not in main_content:
        broneeri = '\n  <div id="broneeri-container" style="height:0;overflow:hidden;margin:0;padding:0;"></div>'

    # Build complete new file
    new_html = f"""<!DOCTYPE html>
<html lang="et">
<head>
  <meta charset="utf-8">
{head_meta}

{NEW_FONTS}

  <style>
{combined_css}
  </style>
</head>
<body>
{header_html}

  <!-- ===== MAIN ===== -->
  {main_content}
{broneeri}

{NEW_FOOTER}
{FIXED_ELEMENTS}
{NEW_SCRIPTS}
</body>
</html>"""

    filepath.write_text(new_html, encoding='utf-8')
    return True

# ─── Main ────────────────────────────────────────────────────────────────────
et_dir = BASE / 'et'
files = sorted(et_dir.rglob('*.html'))
updated = 0
skipped = 0

for f in files:
    if f == HOME:
        print(f'  SKIP (template): {f.relative_to(BASE)}')
        continue
    print(f'  Processing: {f.relative_to(BASE)}')
    try:
        ok = process_file(f)
        if ok:
            updated += 1
        else:
            skipped += 1
    except Exception as e:
        print(f'  ERROR in {f.relative_to(BASE)}: {e}')
        skipped += 1

print(f'\nDone! Updated: {updated}, Skipped/Errors: {skipped}')
