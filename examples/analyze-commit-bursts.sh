#!/usr/bin/env bash
set -euo pipefail

# analyze-commit-bursts.sh
# Minimal example: compute daily commit counts for a (shallow) git clone and emit CSV.
#
# Usage:
#   ./analyze-commit-bursts.sh /path/to/repo [output.csv]
# If no path is provided, the current directory is used. If no output file is provided, prints CSV to stdout.

REPO_PATH="${1:-.}"
OUT_FILE="${2:--}"

# Verify repository
if ! git -C "$REPO_PATH" rev-parse --git-dir >/dev/null 2>&1; then
  echo "Error: $REPO_PATH is not a git repository" >&2
  exit 2
fi

# Extract commit dates (YYYY-MM-DD), count per day, output CSV header + rows.
if [ "$OUT_FILE" = "-" ]; then
  printf '%s,%s\n' date count
  git -C "$REPO_PATH" log --pretty=format:%ad --date=short \
    | sort \
    | uniq -c \
    | awk '{print $2","$1}'
else
  {
    printf '%s,%s\n' date count
    git -C "$REPO_PATH" log --pretty=format:%ad --date=short \
      | sort \
      | uniq -c \
      | awk '{print $2","$1}'
  } > "$OUT_FILE"
  echo "Wrote $OUT_FILE"
fi

