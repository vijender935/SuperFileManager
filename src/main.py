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


from file_manager import create_folder


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


def main():
    show_banner()
    check_folders()
    print("\nProject Setup Completed Successfully!")


if __name__ == "__main__":
    main()
