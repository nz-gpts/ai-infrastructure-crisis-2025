#!/usr/bin/env python3
"""
Redact email addresses in files under data/ by replacing them with anonymized tokens.
Produces sanitized copies alongside original files with suffix ".sanitized".
Writes a mapping CSV at data/redaction_mapping.csv with columns: token,original_email,filename,occurrences

Usage:
  python3 scripts/redact_emails.py
"""
import re
import os
import csv
from collections import defaultdict, Counter

ROOT = os.path.join(os.path.dirname(__file__), "..", "data")
EMAIL_RE = re.compile(rb"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")

def find_files(root):
    for dirpath, _, filenames in os.walk(root):
        for fn in filenames:
            yield os.path.join(dirpath, fn)

def process_file(path, mapping, counters):
    # Read bytes to avoid encoding surprises; assume UTF-8 compatible content
    with open(path, "rb") as f:
        data = f.read()

    matches = EMAIL_RE.findall(data)
    if not matches:
        return 0

    # Count matches and register mapping
    for m in matches:
        counters[m] += 1
        if m not in mapping:
            token = f"<author-{len(mapping)+1:04d}>".encode("ascii")
            mapping[m] = token

    # Replace
    out = data
    for orig, token in mapping.items():
        out = out.replace(orig, token)

    out_path = path + ".sanitized"
    with open(out_path, "wb") as f:
        f.write(out)
    return len(matches)

def main():
    mapping = {}  # bytes -> bytes token
    counters = Counter()
    files_processed = 0
    total_replacements = 0

    for path in find_files(ROOT):
        # Only process regular files
        try:
            if not os.path.isfile(path):
                continue
            # skip binary-looking files by size heuristics? we'll process all
            replaced = process_file(path, mapping, counters)
            if replaced:
                files_processed += 1
                total_replacements += replaced
        except Exception as e:
            print(f"Skipping {path}: {e}")

    # Write mapping CSV (token,original_email,occurrences)
    map_path = os.path.join(ROOT, "redaction_mapping.csv")
    with open(map_path, "w", newline='', encoding='utf-8') as csvf:
        writer = csv.writer(csvf)
        writer.writerow(["token","original_email","occurrences"])
        for orig, token in mapping.items():
            writer.writerow([token.decode("ascii"), orig.decode("utf-8", errors="replace"), counters[orig]])

    print(f"Processed {files_processed} files, made {total_replacements} replacements.")
    print(f"Mapping written to {map_path}")

if __name__ == "__main__":
    main()

