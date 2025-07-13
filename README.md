# 🎒 ZipForAI

**Easily prepare your code for sharing with an AI.**  
Automatically creates a clean `.zip` that excludes virtual environments, OS clutter, media, and more.

---

## 🧠 What It Does

You give it a folder.  
It creates a lightweight `.zip` that includes only what matters:
- Your scripts
- Config files
- Docs and notes

Everything else (like `venv/`, `__pycache__`, `.env`, `*.png`, etc.) is **skipped automatically**.

---

## ⚙️ How to Use (Windows)

1. **Right-click** any folder  
2. Select **“Zip for AI”** from the context menu  
3. A clean `.zip` will appear next to it

> ⚠️ *No data ever leaves your computer — 100% offline.*

---

## 🧹 What Gets Skipped?

ZipForAI automatically excludes unnecessary, sensitive, and bulky content using smart ignore rules.

### 📁 Ignored Folders

- **Version control & metadata**: `.git`, `.svn`, `.hg`
- **Virtual environments & caches**: `venv/`, `.venv/`, `env/`, `node_modules/`, `.mypy_cache/`, `.pytest_cache/`, `__pycache__/`
- **Build outputs**: `build/`, `dist/`, `out/`, `target/`, `bin/`, `obj/`
- **Editor config folders**: `.idea/`, `.vscode/`, `.vs/`
- **Temp/user data**: `uploads/`, `tmp/`, `logs/`, `flask_session/`
- **Static/media folders**: `media/`, `static/` *(optional — can be enabled)*

### 📄 Ignored Files

- **Secrets & config**: `.env`, `.env.local`, `.env.*`
- **System junk**: `.DS_Store`, `Thumbs.db`
- **Binaries & compiled files**: `*.exe`, `*.dll`, `*.pyc`, `*.so`, `*.class`, `*.jar`, etc.
- **Logs & databases**: `*.log`, `*.sqlite`, `*.sqlite3`, `*.db`
- **Office/temp files**: `~$*.docx`, `*.tmp`
- **Coverage/reports**: `.coverage`, `coverage.xml`, `coverage.*`
- **Large media assets**: `*.png`, `*.jpg`, `*.jpeg`, `*.gif`, `*.mp4`, `*.zip` *(optional)*

---

## ✅ Why ZipForAI?

Most AIs have trouble with messy projects. ZipForAI helps you:
- Avoid uploading unnecessary bulk
- Protect sensitive or irrelevant files
- Get to the point faster when asking for help

No setup. No guessing. Just right-click → zip → share.

---
