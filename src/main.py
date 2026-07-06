from config import (
    PROJECT_NAME,
    VERSION,
    INPUT_DIR,
    OUTPUT_DIR,
    BACKUP_DIR,
    LOG_DIR,
    DOCS_DIR,
    TESTS_DIR
)

from file_manager import (
    create_folder,
    folder_exists
)


def show_banner():
    print("=" * 40)
    print(PROJECT_NAME)
    print("Version:", VERSION)
    print("=" * 40)


def check_folders():
    folders = [
        INPUT_DIR,
        OUTPUT_DIR,
        BACKUP_DIR,
        LOG_DIR,
        DOCS_DIR,
        TESTS_DIR
    ]

    for folder in folders:
        create_folder(folder)
        print(f"✅ {folder.name} Ready")


def check_input_folder():
    print("\nChecking Input Folder...")

    if folder_exists(INPUT_DIR):
        print("✅ Input Folder Found")
    else:
        print("❌ Input Folder Not Found")


def list_input_files():
    print("\n📂 Files in Input Folder:")

    files = [f for f in INPUT_DIR.iterdir() if f.is_file()]

    if not files:
        print("❌ No files found.")
        return

    for i, file in enumerate(files, start=1):
        print(f"{i}. {file.name}")

    print(f"\nTotal Files: {len(files)}")


def main():
    show_banner()
    check_folders()
    print("\nProject Setup Completed Successfully!")
    check_input_folder()
    list_input_files()


if __name__ == "__main__":
    main()
