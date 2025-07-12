import sys
from .zipper import zip_project

def main():
    print("🟡 ZipForAI is starting...")  # DEBUG line

    if len(sys.argv) != 2:
        print("Usage: python -m app <folder_path>")
        sys.exit(1)

    folder_path = sys.argv[1]
    print(f"📁 Input folder: {folder_path}")  # DEBUG line

    try:
        zip_project(folder_path)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
