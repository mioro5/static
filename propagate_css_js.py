#!/usr/bin/env python3
"""
Propagate CSS + JS updates from home.html to all already-processed ET pages.
Replaces only the <style> block content and the animation JS block.
"""
import re
from pathlib import Path

BASE = Path('/home/user/static')
HOME = BASE / 'et' / 'home.html'

home_text = HOME.read_text(encoding='utf-8')

# Extract new CSS from home.html
css_m = re.search(r'<style>(.*?)</style>', home_text, re.DOTALL)
NEW_CSS = css_m.group(1) if css_m else ''

# Extract animation JS block from home.html (the full <script> block for animations)
anim_m = re.search(
    r'(  <!-- Scroll & entrance animations engine -->.*?</script>)',
    home_text, re.DOTALL
)
NEW_ANIM_JS = anim_m.group(1) if anim_m else ''

if not NEW_CSS:
    print('ERROR: Could not extract CSS from home.html')
    exit(1)
if not NEW_ANIM_JS:
    print('ERROR: Could not extract animation JS from home.html')
    exit(1)

print(f'CSS length: {len(NEW_CSS)} chars')
print(f'Animation JS length: {len(NEW_ANIM_JS)} chars')

def update_page(filepath):
    rel = filepath.relative_to(BASE)
    if filepath == HOME:
        return False

    html = filepath.read_text(encoding='utf-8')

    # Skip pages not yet processed (no site-header class = unprocessed)
    if 'class="site-header"' not in html:
        return False

    original = html

    # 1. Replace <style> block content
    html = re.sub(
        r'(<style>)(.*?)(</style>)',
        lambda m: m.group(1) + NEW_CSS + m.group(3),
        html, count=1, flags=re.DOTALL
    )

    # 2. Replace animation JS script block (comment may differ between pages)
    html = re.sub(
        r'  <!-- Scroll & entrance animations[^>]*-->.*?</script>',
        NEW_ANIM_JS,
        html, count=1, flags=re.DOTALL
    )

    if html != original:
        filepath.write_text(html, encoding='utf-8')
        return True
    return False

# Process all ET html files
updated = 0
skipped = 0
for fp in sorted(BASE.glob('et/**/*.html')):
    result = update_page(fp)
    if result:
        updated += 1
        print(f'  Updated: {fp.relative_to(BASE)}')
    else:
        skipped += 1

print(f'\nDone! Updated: {updated}, Skipped: {skipped}')
