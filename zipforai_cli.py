"""
ZipForAI – create a clean ZIP of a project folder for sharing with AI tools.
Designed to be called from a Windows right-click context-menu entry:
   zipforai.exe "<folder_path>"
"""

import os
import sys
import fnmatch
import zipfile
from pathlib import Path

# ── ignore rules ──────────────────────────────────────────────
EXCLUDED_DIRS = {
    ".git", ".svn", ".hg",
    "node_modules", "venv", ".venv", "env",
    ".mypy_cache", ".pytest_cache",
    "build", "dist", "out", "target", "bin", "obj",
    ".idea", ".vscode", ".vs",
    "__pycache__", ".next", ".parcel-cache", ".sass-cache",
    "flask_session", "uploads", "tmp", "logs",
    "media", "static",
}

EXCLUDED_FILES = {
    ".env", ".env.local", ".env.*",
    ".DS_Store", "Thumbs.db",
    "*.class", "*.jar", "*.dll", "*.exe", "*.o", "*.a", "*.so",
    "*.pyc", "*.pyo",
    "*.log", "*.sqlite", "*.sqlite3", "*.db",
    "~$*.doc*", "*.tmp",
    ".coverage", "coverage.*", "coverage.xml",
    "*.png", "*.jpg", "*.jpeg", "*.gif", "*.mp4", "*.zip",
}

match = fnmatch.fnmatch


def _is_excluded_file(name: str) -> bool:
    return any(match(name, pat) for pat in EXCLUDED_FILES)


def _is_excluded_dir(name: str) -> bool:
    return name in EXCLUDED_DIRS or any(match(name, pat) for pat in EXCLUDED_DIRS)


def zip_project(folder_path: str) -> str:
    folder = Path(folder_path).resolve()
    if not folder.is_dir():
        raise ValueError(f"Not a directory: {folder_path}")

    out_zip = folder.with_name(folder.name + "_forAI.zip")

    with zipfile.ZipFile(out_zip, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(folder):
            dirs[:] = [d for d in dirs if not _is_excluded_dir(d)]
            root_p = Path(root)
            for fname in files:
                if _is_excluded_file(fname):
                    continue
                fpath = root_p / fname
                rel = fpath.relative_to(folder)
                if any(_is_excluded_dir(p) for p in rel.parts):
                    continue
                zf.write(fpath, arcname=rel)
                print(f"✅ {rel}")

    print(f"\n🎉  Created: {out_zip}")
    return str(out_zip)


# ── CLI entry ────────────────────────────────────────────────
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: zipforai.exe <folder_to_zip>  (usually invoked via right-click)")
        sys.exit(1)

    try:
        zip_project(sys.argv[1])
    except Exception as err:
        print(f"❌ Error: {err}")
        sys.exit(1)
