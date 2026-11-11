#!/usr/bin/env python3
"""Create redacted *copies* of text exports under data/.

No email-to-token lookup table is written. Source files are never modified.
Existing '.sanitized' files are not processed again.

Usage:
    python3 scripts/redact_emails.py
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent / "data"
EMAIL_RE = re.compile(rb"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
SAFE_SUFFIXES = {".txt", ".csv", ".json", ".md"}


def redact(data: bytes) -> tuple[bytes, int]:
    return EMAIL_RE.subn(b"<redacted-email>", data)


def main() -> None:
    files = 0
    replacements = 0
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix.lower() not in SAFE_SUFFIXES:
            continue
        if path.name.endswith(".sanitized") or path.name == "redaction_mapping.csv":
            continue
        data = path.read_bytes()
        sanitized, count = redact(data)
        if count:
            target = path.with_name(path.name + ".sanitized")
            target.write_bytes(sanitized)
            files += 1
            replacements += count
    print(f"Created redacted copies of {files} files; replaced {replacements} email occurrences.")
    print("No reversible email mapping or original addresses were written to a report.")
    print("Review sanitized copies before publishing; original source files are unchanged.")


if __name__ == "__main__":
    main()
