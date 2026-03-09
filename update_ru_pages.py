#!/usr/bin/env python3
"""
Update all RU pages to use the new design from et/home.html.
Preserves each page's Russian <main> content, meta tags, structured data.
Replaces: fonts, CSS, header, footer, fixed elements, scripts.
Russian-specific: nav labels, footer text, booking button, cookie notice.
"""
import os
import re
from pathlib import Path

BASE = Path('/home/user/static')
ET_HOME = BASE / 'et' / 'home.html'   # Design reference (do NOT modify)
RU_HOME = BASE / 'ru' / 'home.html'   # RU template source (to be updated too)

# ─── Extract CSS and animation JS from et/home.html (design reference) ────────
et_home_text = ET_HOME.read_text(encoding='utf-8')

css_m = re.search(r'<style>(.*?)</style>', et_home_text, re.DOTALL)
NEW_CSS = css_m.group(1) if css_m else ''

anim_m = re.search(r'(  <!-- Scroll & entrance animations engine -->.*?</script>)', et_home_text, re.DOTALL)
NEW_ANIM_JS = anim_m.group(1) if anim_m else ''

if not NEW_CSS:
    print('ERROR: Could not extract CSS from et/home.html'); exit(1)
if not NEW_ANIM_JS:
    print('ERROR: Could not extract animation JS from et/home.html'); exit(1)

# ─── Russian font block (same as ET) ─────────────────────────────────────────
NEW_FONTS = """  <!-- Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preload" as="style" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=DM+Serif+Display&display=swap" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=DM+Serif+Display&display=swap"></noscript>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0">"""

# ─── Russian footer ───────────────────────────────────────────────────────────
NEW_FOOTER = """  <!-- FOOTER -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div>
          <strong>MV Therapy</strong>
          <div>Medical Verified Therapy</div>
          <div style="margin-top:6px;font-size:.82rem;">© 2025 MV Therapy – Массаж в Пярну</div>
          <div class="footer-social">
            <a href="https://www.facebook.com/profile.php?id=100090837369433" target="_blank" rel="noopener noreferrer" aria-label="Facebook">
              <img src="/public/img/fb_svg.png" alt="Facebook" width="32" height="32">
            </a>
            <a href="https://www.instagram.com/medmassaaz/" target="_blank" rel="noopener noreferrer" aria-label="Instagram" style="color:#fff;font-weight:700;font-size:.85rem;">IG</a>
            <a href="https://www.tiktok.com/@medmassaaz" target="_blank" rel="noopener noreferrer" aria-label="TikTok" style="color:#fff;font-weight:700;font-size:.85rem;">TT</a>
          </div>
        </div>
        <div>
          <strong>Адрес</strong>
          <div>Rüütli 47 II этаж</div>
          <div>80010 Пярну, Эстония</div>
          <a href="/ru/map.html" style="font-size:.85rem;">📍 Смотреть на карте</a>
        </div>
        <div>
          <strong>Контакты</strong>
          <div><a href="tel:+37258189561">+372 5818 9561</a></div>
          <div><a href="mailto:info@mvtherapy.ee">info@mvtherapy.ee</a></div>
        </div>
        <div>
          <strong>Страницы</strong>
          <div><a href="/ru/services.html">Услуги массажа</a></div>
          <div><a href="/ru/Diagnosis.html">Диагнозы</a></div>
          <div><a href="/ru/blog.html">Блог</a></div>
          <div><a href="/ru/kkk.html">FAQ</a></div>
        </div>
      </div>
    </div>
  </footer>"""

# ─── Fixed elements (Russian) ─────────────────────────────────────────────────
FIXED_ELEMENTS = """
  <!-- GO TOP -->
  <button class="go-top" id="goTop" aria-label="Прокрутить к началу страницы">
    <span class="material-symbols-outlined">expand_less</span>
  </button>

  <!-- STICKY MOBILE BOOKING BAR -->
  <div class="mobile-book-bar" id="mobileBookBar">
    <div class="book-info">
      <strong>MV Therapy</strong>
      Rüütli 47, Pärnu
    </div>
    <button class="btn btn-primary book-trigger">Записаться</button>
  </div>

  <!-- COOKIE NOTICE -->
  <div id="cookieNotice" style="display:none;" role="dialog" aria-label="Уведомление о куки">
    <p>Мы используем файлы куки для улучшения вашего опыта, персонализации контента и анализа трафика.</p>
    <button class="cookie-btn" id="cookieAccept">OK, принять</button>
  </div>"""

# ─── Scripts (Russian language for SalonLife) ─────────────────────────────────
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

  <!-- Scroll & entrance animations engine -->
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
        /* Single-box cards (Diagnosis, workshops, services pages) */
        main.querySelectorAll('.flx-container-services .single-box').forEach(function(card, i) {
          card.setAttribute('data-anim', 'up');
          card.style.transitionDelay = (i * .07) + 's';
        });
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

  <!-- SalonLife Booking Widget (Russian) -->
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
        identifier:3986,button_text:book_texts.ru,language:'ru',color:'#44437d',container:'#broneeri-container'
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
    parts = rel_path.parts  # ('ru', 'services.html') or ('ru', 'services', '1.html')
    if len(parts) == 2:
        mapping = {
            'home.html': 'home', 'index.html': 'home',
            'services.html': 'services', 'Diagnosis.html': 'diagnosis',
            'campaign.html': 'campaign', 'workshops.html': 'workshops',
            'team.html': 'team', 'kkk.html': 'kkk',
            'blog.html': 'blog', 'map.html': '',
        }
        return mapping.get(parts[1], '')
    elif len(parts) == 3:
        mapping = {
            'services': 'services', 'Diagnosis': 'diagnosis',
            'campaign': 'campaign', 'workshops': 'workshops', 'blog': 'blog',
        }
        return mapping.get(parts[1], '')
    return ''

# ─── Russian nav items ─────────────────────────────────────────────────────────
NAV_ITEMS = [
    ('/ru/home.html',      'Главная',   'home'),
    ('/ru/services.html',  'Массажи',   'services'),
    ('/ru/Diagnosis.html', 'Диагнозы',  'diagnosis'),
    ('/ru/campaign.html',  'Акции',     'campaign'),
    ('/ru/workshops.html', 'Обучение',  'workshops'),
    ('/ru/team.html',      'Команда',   'team'),
    ('/ru/kkk.html',       'FAQ',       'kkk'),
    ('/ru/blog.html',      'Блог',      'blog'),
]

def build_header(et_url, ru_url, en_url, active_section):
    desktop = ''
    mobile = ''
    for href, label, key in NAV_ITEMS:
        cur = ' aria-current="page"' if key == active_section else ''
        desktop += f'\n        <a href="{href}"{cur}>{label}</a>'
        mobile  += f'\n          <a href="{href}">{label}</a>'

    return f"""  <a class="skip-link" href="#content">Перейти к основному содержимому</a>

  <!-- ===== HEADER ===== -->
  <header class="site-header">
    <div class="container topbar">
      <a class="brand" href="/ru/home.html" aria-label="MV Therapy главная страница">
        <div class="brand-logo" aria-hidden="true"></div>
        <div class="brand-text">
          <strong>MV Therapy</strong>
          <span>Medical Verified Therapy</span>
        </div>
      </a>
      <nav class="desktop-nav" aria-label="Главное меню">{desktop}
      </nav>
      <div class="header-actions">
        <div class="mobile-lang-header" aria-label="Язык">
          <a href="{et_url}">EST</a>
          <a href="{ru_url}" class="active">РУС</a>
          <a href="{en_url}">ENG</a>
        </div>
        <div class="lang-switch" aria-label="Язык">
          <a href="{et_url}">EST</a>
          <a href="{ru_url}" class="active">РУС</a>
          <a href="{en_url}">ENG</a>
        </div>
        <button class="mobile-toggle" id="mobileToggle" aria-expanded="false" aria-controls="mobilePanel" aria-label="Открыть меню">
          <span class="material-symbols-outlined">menu</span>
        </button>
      </div>
    </div>
    <div class="mobile-panel" id="mobilePanel">
      <div class="container">
        <nav aria-label="Мобильное меню">{mobile}
        </nav>
      </div>
    </div>
  </header>"""

# ─── CSS filtering ─────────────────────────────────────────────────────────────
OLD_BASE_SELECTORS = [
    r'\*\s*\{', r'html\s*\{', r'body\s*\{', r'img\s*\{',
    r'a\s*\{', r'\.container\s*\{', r'\.sticky-wrapper\s*\{',
    r'main\s*\{', r'#main-app\s*\{', r'#wrap\s*\{',
    r'header\s*\{', r'\.logo\b', r'\.claim\b', r'\.language-menu\b',
    r'\.nav\b', r'\.nav-inner\b', r'\.nav-item\b', r'\.hamburger\b',
    r'footer\s*\{', r'\.flx-container\b', r'\.goTop\b', r'\.go-top\b',
    r'#scrollBtn\b', r'\.page-footer\b', r'\.site-footer\b',
    r'\.footer-grid\b', r'\.footer-social\b', r'\.footer-copy\b',
    r'#cookieNotice\b', r'\.mobile-book-bar\b',
    r'\.seo-section\b', r'\.seo-grid\b', r'\.seo-col\b',
    r'h1\s*\{', r'\.skip-link\b',
]

def filter_old_css(css_text):
    rules = []
    i = 0; depth = 0; current = ''
    while i < len(css_text):
        c = css_text[i]
        if c == '{': depth += 1; current += c
        elif c == '}':
            depth -= 1; current += c
            if depth == 0:
                rules.append(current.strip()); current = ''
        else:
            current += c
        i += 1
    if current.strip():
        rules.append(current.strip())

    kept = []
    for rule in rules:
        brace_pos = rule.find('{')
        if brace_pos == -1:
            if rule.strip(): kept.append(rule)
            continue
        selector = rule[:brace_pos].strip()
        is_base = any(re.search(pat, selector) for pat in OLD_BASE_SELECTORS)
        if not is_base:
            kept.append(rule)
    return '\n\n'.join(kept)

# ─── Extract main content ─────────────────────────────────────────────────────
def extract_main(html):
    """Extract <main> block; handle both id="main-app" and id="content"."""
    m = re.search(r'(<main\b[^>]*>)(.*?)(</main>)', html, re.DOTALL | re.IGNORECASE)
    if m:
        open_tag, content, close_tag = m.group(1), m.group(2), m.group(3)
        # Normalise id to "content"
        open_tag = re.sub(r'\bid="[^"]*"', '', open_tag)
        open_tag = open_tag.replace('<main', '<main id="content"', 1)
        open_tag = re.sub(r'\s+', ' ', open_tag).strip()
        # Remove old broneeri-container if present (we re-add in footer area)
        content = re.sub(
            r'\s*<!--\s*BOOKING SYSTEM CONTAINER\s*-->\s*<div id="broneeri-container"[^>]*>\s*</div>\s*',
            '\n', content, flags=re.DOTALL | re.IGNORECASE
        )
        return open_tag + content + close_tag
    return None

# ─── Extract head meta ─────────────────────────────────────────────────────────
def extract_head_meta(html):
    head_m = re.search(r'<head>(.*?)</head>', html, re.DOTALL | re.IGNORECASE)
    if not head_m:
        return ''
    head_content = head_m.group(1)

    head_content = re.sub(r'\s*<meta\s+charset=[^>]+>\s*', '\n', head_content, flags=re.IGNORECASE)
    head_content = re.sub(
        r'\s*<link[^>]*(?:Inter|fonts\.googleapis\.com|fonts\.gstatic\.com|Material\+Symbols)[^>]*>\s*',
        '\n', head_content, flags=re.IGNORECASE
    )
    head_content = re.sub(r'\s*<noscript>.*?</noscript>\s*', '\n', head_content, flags=re.DOTALL | re.IGNORECASE)
    head_content = re.sub(r'\s*<link[^>]*dns-prefetch[^>]*>\s*', '\n', head_content, flags=re.IGNORECASE)
    head_content = re.sub(r'\s*<link[^>]*rel=["\']preconnect["\'][^>]*>\s*', '\n', head_content, flags=re.IGNORECASE)
    head_content = re.sub(r'\s*<link[^>]*rel=["\']stylesheet["\'][^>]*>\s*', '\n', head_content, flags=re.IGNORECASE)
    head_content = re.sub(r'\s*<style>.*?</style>\s*', '\n', head_content, flags=re.DOTALL)

    orphan_comments = [
        r'<!--\s*Resource Hints[^-]*-->', r'<!--\s*Preload Critical[^-]*-->',
        r'<!--\s*Stylesheets\s*-->', r'<!--\s*Fonts\s*-->',
        r'<!--\s*Updated viewport[^-]*-->', r'<!--\s*Theme color[^-]*-->',
    ]
    for pat in orphan_comments:
        head_content = re.sub(r'\s*' + pat + r'\s*', '\n', head_content, flags=re.IGNORECASE | re.DOTALL)

    lines = head_content.split('\n')
    fixed = []
    for line in lines:
        stripped = line.strip()
        fixed.append('  ' + stripped if stripped else '')
    head_content = '\n'.join(fixed)
    head_content = re.sub(r'\n{3,}', '\n\n', head_content)
    return head_content.strip('\n')

# ─── Clean SEO meta tags (Russian specifics) ──────────────────────────────────
def clean_meta_seo(head_content):
    # Remove junk meta tags
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
        r'\s*<meta\s+property=["\']og:site_name["\'][^>]*>\s*',
        r'\s*<meta\s+name=["\']og:site_name["\'][^>]*>\s*',
    ]:
        head_content = re.sub(pat, '\n', head_content, flags=re.IGNORECASE)

    # Fix geo.region
    head_content = re.sub(r'(content=["\'])EE-6[0-9](["\'])', r'\g<1>EE-67\2', head_content)
    # Fix geo.placename
    head_content = re.sub(
        r'(<meta\s+name=["\']geo\.placename["\'][^>]*content=["\'])([^"\']+)(["\'])',
        lambda m: m.group(1) + 'Pärnu, Estonia' + m.group(3),
        head_content, flags=re.IGNORECASE
    )
    # Standardise robots
    head_content = re.sub(
        r'(<meta\s+name=["\']robots["\'][^>]*content=["\'])([^"\']+)(["\'])',
        lambda m: m.group(1) + 'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' + m.group(3),
        head_content, flags=re.IGNORECASE
    )
    # Fix user-scalable=no
    head_content = re.sub(r'user-scalable=no', 'user-scalable=yes', head_content, flags=re.IGNORECASE)
    # Standardise twitter:* to property=
    head_content = re.sub(
        r'<meta\s+name=(["\'])(twitter:[^"\']+)(\1)',
        r'<meta property=\1\2\3', head_content, flags=re.IGNORECASE
    )
    # Remove inline dimensions from og:image
    head_content = re.sub(
        r'(<meta[^>]*property=["\']og:image["\'][^>]*)\s+width=["\'][^"\']*["\'](\s+height=["\'][^"\']*["\'])?',
        r'\1', head_content, flags=re.IGNORECASE
    )
    head_content = re.sub(
        r'(<meta[^>]*property=["\']og:image["\'][^>]*)\s+height=["\'][^"\']*["\']',
        r'\1', head_content, flags=re.IGNORECASE
    )
    # Add og:image dimensions if missing
    if re.search(r'property=["\']og:image["\']', head_content, re.IGNORECASE):
        if not re.search(r'property=["\']og:image:width["\']', head_content, re.IGNORECASE):
            head_content = re.sub(
                r'(<meta[^>]*property=["\']og:image["\'][^>]*>)',
                r'\1\n  <meta property="og:image:width" content="1200">\n  <meta property="og:image:height" content="630">',
                head_content, count=1, flags=re.IGNORECASE
            )
    # Add geo tags if missing
    if not re.search(r'geo\.region', head_content, re.IGNORECASE):
        geo_block = '''
  <!-- Geo Location Meta Tags -->
  <meta name="geo.region" content="EE-67">
  <meta name="geo.placename" content="Pärnu, Estonia">
  <meta name="geo.position" content="58.3859;24.4971">
  <meta name="ICBM" content="58.3859, 24.4971">'''
        if re.search(r'theme-color', head_content, re.IGNORECASE):
            head_content = re.sub(
                r'(<meta[^>]*theme-color[^>]*>)',
                r'\1' + geo_block, head_content, count=1, flags=re.IGNORECASE
            )
        else:
            head_content += geo_block
    # Add theme-color if missing
    if not re.search(r'theme-color', head_content, re.IGNORECASE):
        head_content = re.sub(
            r'(<meta\s+name=["\']robots["\'][^>]*>)',
            r'\1\n  <meta name="theme-color" content="#44437d">',
            head_content, count=1, flags=re.IGNORECASE
        )
    # Fix postalCode
    head_content = head_content.replace('"postalCode": "80014"', '"postalCode": "80010"')
    # Fix opening hours in schema within head
    head_content = head_content.replace('"opens": "09:00"', '"opens": "10:00"')
    head_content = head_content.replace('"closes": "18:00"', '"closes": "19:00"')
    return head_content

# ─── Clean schema.org in head (same as ET clean_schema.py) ───────────────────
def remove_json_key(json_str, key):
    result = json_str
    key_pattern = rf'(\s*"{re.escape(key)}"\s*:\s*)'
    m = re.search(key_pattern, result)
    if not m:
        return result
    start = m.start(); value_start = m.end()
    first_char_match = re.search(r'\S', result[value_start:])
    if not first_char_match:
        return result
    first_char = first_char_match.group()
    if first_char in ('{', '['):
        open_char = first_char; close_char = '}' if first_char == '{' else ']'
        depth = 0; in_string = False; escape_next = False
        pos = result.index(first_char, value_start); i = pos
        while i < len(result):
            c = result[i]
            if escape_next: escape_next = False
            elif c == '\\' and in_string: escape_next = True
            elif c == '"': in_string = not in_string
            elif not in_string:
                if c == open_char: depth += 1
                elif c == close_char:
                    depth -= 1
                    if depth == 0: end = i + 1; break
            i += 1
        else:
            return result
    elif first_char == '"':
        pos = result.index('"', value_start); i = pos + 1
        while i < len(result):
            if result[i] == '\\': i += 2; continue
            if result[i] == '"': end = i + 1; break
            i += 1
        else:
            return result
    else:
        m2 = re.search(r'[,\n}]', result[value_start:])
        if not m2: return result
        end = value_start + m2.start()
    after = result[end:]
    after_m = re.match(r'\s*,', after)
    if after_m:
        result = result[:start] + result[end + after_m.end():]
    else:
        before = result[:start]
        before_m = re.search(r',\s*$', before)
        if before_m:
            result = result[:before_m.start()] + result[start + (end - start):]
        else:
            result = result[:start] + result[end:]
    return result

def clean_schema(html):
    def _fix_json(m):
        content = m.group(1)
        for key in ['aggregateRating', 'review', 'slogan', 'additionalProperty']:
            content = remove_json_key(content, key)
        content = re.sub(r'("name"\s*:\s*")(Лучший[^"]*|[^"]*Лучший[^"]*|Parim[^"]*)(")' ,
                         lambda x: x.group(1) + 'MV Therapy' + x.group(3), content)
        content = re.sub(
            r'"alternateName"\s*:\s*\[([^\]]+)\]',
            lambda x: '"alternateName": ["MV Therapy"]'
            if any(w in x.group(1) for w in ['Лучший', 'Parim', '#1', 'лучший'])
            else x.group(0),
            content
        )
        content = content.replace('"postalCode": "80014"', '"postalCode": "80010"')
        content = content.replace('"opens": "09:00"', '"opens": "10:00"')
        content = content.replace('"closes": "18:00"', '"closes": "19:00"')
        content = re.sub(
            r'"dayOfWeek": \["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"\]',
            '"dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]',
            content
        )
        return m.group(0).replace(m.group(1), content)
    return re.sub(r'<script type="application/ld\+json">(.*?)</script>', _fix_json, html, flags=re.DOTALL)

# ─── Extract page-specific CSS ────────────────────────────────────────────────
def extract_page_css(html):
    styles = re.findall(r'<style>(.*?)</style>', html, re.DOTALL | re.IGNORECASE)
    if not styles:
        return ''

    marker = '/* === PAGE-SPECIFIC STYLES === */'
    all_css = '\n'.join(styles)

    # Idempotency: if the page already contains our generated marker, extract
    # only the CSS after the marker (page-specific part from the previous run).
    # This preserves page-specific styles across repeated runs of this script.
    if marker in all_css:
        after_marker = all_css.split(marker, 1)[1].strip()
        return after_marker if after_marker else ''

    return filter_old_css(all_css).strip()

# ─── Build complete HTML page ─────────────────────────────────────────────────
def build_page(head_meta, page_css, main_content, et_url, ru_url, en_url, active_section):
    header = build_header(et_url, ru_url, en_url, active_section)
    css_block = f'<style>{NEW_CSS}'
    if page_css:
        css_block += '\n\n    /* === PAGE-SPECIFIC STYLES === */\n    ' + page_css.replace('\n', '\n    ')
    css_block += '\n  </style>'

    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="utf-8">
{head_meta}

{NEW_FONTS}

  {css_block}
</head>
<body>
{header}

  <!-- ===== MAIN ===== -->
{main_content}

  <!-- BRONEERI CONTAINER -->
  <div id="broneeri-container" style="height:0;overflow:hidden;margin:0;padding:0;"></div>

{NEW_FOOTER}
{FIXED_ELEMENTS}
{NEW_SCRIPTS}
</body>
</html>"""

# ─── Process a single file ────────────────────────────────────────────────────
def process_file(filepath):
    rel = filepath.relative_to(BASE)
    html = filepath.read_text(encoding='utf-8')

    rel_from_ru = str(rel).replace('ru/', '', 1)
    et_url = f'/et/{rel_from_ru}'
    ru_url = f'/ru/{rel_from_ru}'
    en_url = f'/en/{rel_from_ru}'

    active_section = get_active_section(rel)
    head_meta = extract_head_meta(html)
    head_meta = clean_meta_seo(head_meta)
    page_css = extract_page_css(html)
    main_content = extract_main(html)

    if main_content is None:
        print(f'  WARNING: No <main> found in {rel}, skipping')
        return False

    new_html = build_page(head_meta, page_css, main_content, et_url, ru_url, en_url, active_section)
    new_html = clean_schema(new_html)

    filepath.write_text(new_html, encoding='utf-8')
    return True

# ─── Main ─────────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    ru_dir = BASE / 'ru'
    files = sorted(ru_dir.rglob('*.html'))

    updated = 0
    skipped = 0
    errors = 0

    for fp in files:
        rel = fp.relative_to(BASE)
        print(f'  Processing: {rel}')
        try:
            result = process_file(fp)
            if result:
                updated += 1
            else:
                skipped += 1
                print(f'    -> skipped')
        except Exception as e:
            errors += 1
            print(f'  ERROR in {rel}: {e}')
            import traceback; traceback.print_exc()

    print(f'\nDone! Updated: {updated}, Skipped: {skipped}, Errors: {errors}')
