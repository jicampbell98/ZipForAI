import os
import zipfile
from pathlib import Path
from fnmatch import fnmatch as match  

print("🧠 zipper.py loaded")
EXCLUDED_DIRS = {
    # Version-control & metadata
    ".git", ".svn", ".hg",

    # Dependency caches
    "node_modules",           
    "venv", ".venv", "env",   
    ".mypy_cache", ".pytest_cache",

    # Build / dist outputs
    "build", "dist", "out", "target", "bin", "obj",

    # IDE & editor junk
    ".idea", ".vscode", ".vs",

    # Runtime artifacts & caches
    "__pycache__", ".next", ".parcel-cache", ".sass-cache",

    # User data / sessions / uploads
    "flask_session", "uploads", "tmp", "logs",

    # Media & static bundles (optional—comment out if you need them)
    "media", "static",
}


EXCLUDED_FILES = {
    # Secrets & env
    ".env", ".env.local", ".env.*",        

    # OS cruft
    ".DS_Store", "Thumbs.db",

    # Build artefacts / binaries
    "*.class", "*.jar", "*.dll", "*.exe", "*.o", "*.a", "*.so",
    "*.pyc", "*.pyo",

    # Logs & data dumps
    "*.log", "*.sqlite", "*.sqlite3", "*.db",

    # Word & Office temp files
    "~$*.doc*", "*.tmp",

    # Coverage / reports
    ".coverage", "coverage.*", "coverage.xml",

    # Large assets (optional)
    "*.png", "*.jpg", "*.jpeg", "*.gif", "*.mp4", "*.zip",
}


def _is_excluded_file(name: str) -> bool:
    return any(match(name, pattern) for pattern in EXCLUDED_FILES)

def _is_excluded_dir(name: str) -> bool:
    return name in EXCLUDED_DIRS or any(match(name, pattern) for pattern in EXCLUDED_DIRS)

def zip_project(folder_path: str) -> str:
    folder = Path(folder_path).resolve()
    if not folder.exists() or not folder.is_dir():
        raise ValueError(f"Path '{folder_path}' is not a valid directory.")

    output_zip = folder.with_name(folder.name + "_forAI.zip")

    with zipfile.ZipFile(output_zip, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder):
            # Remove excluded dirs in-place so os.walk doesn’t descend into them
            dirs[:] = [d for d in dirs if not _is_excluded_dir(d)]

            root_path = Path(root)
            for file in files:
                if _is_excluded_file(file):
                    continue

                file_path = root_path / file
                rel_path = file_path.relative_to(folder)

                # Extra safety: skip if **any** part of the path is an excluded dir
                if any(_is_excluded_dir(part) for part in rel_path.parts):
                    print(f"⏭️ Skipped: {rel_path}")
                    continue

                zipf.write(file_path, arcname=rel_path)
                print(f"✅ Added:  {rel_path}")

    print(f"\n🎉 Done! Zip created at: {output_zip}")
    return str(output_zip)
