#!/usr/bin/env python3
import os, re, glob

# Per-language: old footer tingimused line -> replacement (with privacy link appended)
REPLACEMENTS = {
    'et': (
        '          <div><a href="/et/tingimused.html">Tingimused</a></div>\n        </div>',
        '          <div><a href="/et/tingimused.html">Tingimused</a></div>\n          <div><a href="/et/privaatsuspoliitika.html">Privaatsuspoliitika</a></div>\n        </div>'
    ),
    'ru': (
        '          <div><a href="/ru/tingimused.html">Условия</a></div>\n        </div>',
        '          <div><a href="/ru/tingimused.html">Условия</a></div>\n          <div><a href="/ru/privaatsuspoliitika.html">Политика конфиденциальности</a></div>\n        </div>'
    ),
    'en': (
        '          <div><a href="/en/tingimused.html">Terms</a></div>\n        </div>',
        '          <div><a href="/en/tingimused.html">Terms</a></div>\n          <div><a href="/en/privaatsuspoliitika.html">Privacy Policy</a></div>\n        </div>'
    ),
    'fi': (
        '          <div><a href="/fi/tingimused.html">Ehdot</a></div>\n        </div>',
        '          <div><a href="/fi/tingimused.html">Ehdot</a></div>\n          <div><a href="/fi/privaatsuspoliitika.html">Tietosuojakäytäntö</a></div>\n        </div>'
    ),
}

SKIP_PATTERNS = ['privaatsuspoliitika', 'parnu', 'workshops']

total = 0
for lang, (old, new) in REPLACEMENTS.items():
    files = glob.glob('/home/user/static/{}/**.html'.format(lang)) + \
            glob.glob('/home/user/static/{}/services/*.html'.format(lang))
    for fpath in files:
        fname = os.path.basename(fpath)
        if any(s in fname for s in SKIP_PATTERNS):
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        if old in content:
            content = content.replace(old, new)
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            total += 1
            print('Updated: {}'.format(fpath))
        elif 'privaatsuspoliitika' in content:
            pass  # already has it
        else:
            print('SKIP (no match): {}'.format(fpath))

print('Total updated: {}'.format(total))
