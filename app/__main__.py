import os
import sys
from pathlib import Path

# ── Ensure “zipper.py” is importable, even inside the bundled EXE ────────────
current_dir = Path(__file__).resolve().parent
if str(current_dir) not in sys.path:
    sys.path.insert(0, str(current_dir))

import zipper  


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: zipforai.exe <folder_path>")
        sys.exit(1)

    folder = sys.argv[1]
    try:
        zipper.zip_project(folder)
    except Exception as err:
        print(f"❌ Error: {err}")
        sys.exit(1)


if __name__ == "__main__":
    main()
