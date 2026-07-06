from config import (
    PROJECT_NAME,
    VERSION,
    INPUT_DIR,
    OUTPUT_DIR,
    BACKUP_DIR,
    LOG_DIR,
    DOCS_DIR,
    TESTS_DIR,
)

from file_manager import (
    create_folder,
    folder_exists,
    list_files,
    get_file_size,
    get_image_resolution,
    get_image_format,
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
        TESTS_DIR,
    ]

    for folder in folders:
        create_folder(folder)
        print(f"✅ {folder.name} Ready")


def main():
    show_banner()

    check_folders()

    print("\nProject Setup Completed Successfully!")

    print("\nChecking Input Folder...")

    if folder_exists(INPUT_DIR):
        print("✅ Input Folder Found")

        files = list_files(INPUT_DIR)

        print("\n📁 Files in Input Folder:")

        if files:
            total_size = 0

            for i, file in enumerate(files, start=1):
                print(f"\n{i}. {file.name}")

                size = file.stat().st_size
                total_size += size

                print(f"   Size: {get_file_size(file)}")
                print(f"   Resolution: {get_image_resolution(file)}")
                print(f"   Format: {get_image_format(file)}")

            print(f"\nTotal Files: {len(files)}")
            print(f"Total Size: {total_size / (1024 * 1024):.2f} MB")

        else:
            print("❌ No files found.")

    else:
        print("❌ Input Folder Not Found")


if __name__ == "__main__":
    main()
