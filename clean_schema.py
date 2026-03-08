#!/usr/bin/env python3
"""
Clean schema.org JSON-LD blocks in ET pages:
- Remove aggregateRating (self-serving, Google guideline violation)
- Remove review[] arrays (same)
- Remove slogan (marketing-speak)
- Fix "Parim" in name/alternateName
- Fix description superlatives
"""
import re
from pathlib import Path

BASE = Path('/home/user/static')


def remove_json_key(json_str, key):
    """
    Remove a JSON key (and its value, including nested objects/arrays) from a JSON string.
    Handles trailing comma after the block AND leading comma before it.
    """
    # Pattern: "key": { ... }  or  "key": [ ... ]  or  "key": "value"
    # We'll use a bracket-counting approach for objects/arrays
    result = json_str

    # Find the key
    key_pattern = rf'(\s*"{re.escape(key)}"\s*:\s*)'
    m = re.search(key_pattern, result)
    if not m:
        return result

    start = m.start()
    value_start = m.end()

    # Determine value type
    first_char = result[value_start:].lstrip()[0] if result[value_start:].strip() else None

    if first_char in ('{', '['):
        # Find matching closing bracket
        open_char = first_char
        close_char = '}' if first_char == '{' else ']'
        depth = 0
        in_string = False
        escape_next = False
        pos = result.index(first_char, value_start)
        i = pos
        while i < len(result):
            c = result[i]
            if escape_next:
                escape_next = False
            elif c == '\\' and in_string:
                escape_next = True
            elif c == '"':
                in_string = not in_string
            elif not in_string:
                if c == open_char:
                    depth += 1
                elif c == close_char:
                    depth -= 1
                    if depth == 0:
                        end = i + 1
                        break
            i += 1
        else:
            return result  # failed to find end
    elif first_char == '"':
        # String value
        pos = result.index('"', value_start)
        i = pos + 1
        while i < len(result):
            if result[i] == '\\':
                i += 2
                continue
            if result[i] == '"':
                end = i + 1
                break
            i += 1
        else:
            return result
    else:
        # Number/bool/null
        m2 = re.search(r'[,\n}]', result[value_start:])
        if not m2:
            return result
        end = value_start + m2.start()

    # Extract the full block (key + value)
    block = result[start:end]

    # Remove trailing comma
    after = result[end:]
    after_m = re.match(r'\s*,', after)
    if after_m:
        result = result[:start] + result[end + after_m.end():]
    else:
        # Try removing preceding comma
        before = result[:start]
        before_m = re.search(r',\s*$', before)
        if before_m:
            result = result[:before_m.start()] + result[start + len(block):]
        else:
            result = result[:start] + result[end:]

    return result


def clean_schema_block(html):
    """Find and clean all JSON-LD script blocks in HTML."""
    def clean_json_ld(m):
        content = m.group(1)

        # Remove aggregateRating
        content = remove_json_key(content, 'aggregateRating')
        # Remove review array
        content = remove_json_key(content, 'review')
        # Remove slogan
        content = remove_json_key(content, 'slogan')
        # Remove additionalProperty
        content = remove_json_key(content, 'additionalProperty')

        # Fix "name" field containing "Parim"
        content = re.sub(
            r'("name"\s*:\s*")[^"]*Parim[^"]*(")',
            r'\1MV Therapy\2', content
        )
        # Fix "name" field containing "Eesti Parim" pattern
        content = re.sub(
            r'("name"\s*:\s*")(MV Therapy)[^"]+(")',
            r'\1\2\3', content
        )

        # Fix alternateName: remove entries with "Parim", "#1" etc.
        def clean_alternate(am):
            arr_content = am.group(1)
            # Split by comma, keep only clean entries
            items = re.findall(r'"([^"]+)"', arr_content)
            clean_items = [i for i in items if 'Parim' not in i and '#1' not in i and 'parim' not in i.lower()]
            if not clean_items:
                clean_items = ['MV Therapy']
            return '["' + '", "'.join(clean_items) + '"]'
        content = re.sub(
            r'"alternateName"\s*:\s*\[([^\]]+)\]',
            lambda m: '"alternateName": ' + clean_alternate(m),
            content
        )

        # Fix description: remove "parim", "täiuslik" superlatives from schema description
        content = re.sub(r'(?i)Eesti #1 [^"]*massaaži[^"]*terapeut[^"]*[,.]\s*', '', content)
        content = re.sub(r'(?i)Parim massaaž[^"]*Pärnus[^"]*[,.]\s*', '', content)

        return m.group(0).replace(m.group(1), content)

    html = re.sub(
        r'<script type="application/ld\+json">(.*?)</script>',
        clean_json_ld,
        html,
        flags=re.DOTALL
    )
    return html


# Files to process
files_to_clean = [
    'et/services/15.html',
    'et/index.html',
    'et/workshops/38.html',
    'et/workshops/40.html',
    'et/workshops/41.html',
    'et/workshops/42.html',
    'et/workshops/43.html',
]

for rel in files_to_clean:
    fp = BASE / rel
    if not fp.exists():
        print(f'MISSING: {rel}')
        continue
    html = fp.read_text(encoding='utf-8')
    cleaned = clean_schema_block(html)
    if cleaned != html:
        fp.write_text(cleaned, encoding='utf-8')
        print(f'  Fixed: {rel}')
    else:
        print(f'  No changes: {rel}')

print('\nDone!')
