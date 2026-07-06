# SuperFileManager
# main.py
# Version: 2.2

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
    get_image_orientation,
    get_image_mode,
    get_image_color_depth,
    get_image_dpi,
    rename_file,
    copy_file,
    move_file,
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


def show_files(files):
    total_size = 0

    print("\n📁 Files in Input Folder:")

    for i, file in enumerate(files, start=1):
        print(f"\n{i}. {file.name}")

        size = file.stat().st_size
        total_size += size

        print(f"    Size: {get_file_size(file)}")
        print(f"    Resolution: {get_image_resolution(file)}")
        print(f"    Format: {get_image_format(file)}")
        print(f"    Orientation: {get_image_orientation(file)}")
        print(f"    Mode: {get_image_mode(file)}")
        print(f"    Color Depth: {get_image_color_depth(file)}")
        print(f"    DPI: {get_image_dpi(file)}")

    print(f"\nTotal Files: {len(files)}")
    print(f"Total Size: {total_size / (1024 * 1024):.2f} MB")


def main():
    show_banner()
    check_folders()

    if not folder_exists(INPUT_DIR):
        print("❌ Input Folder Not Found")
        return

    files = list_files(INPUT_DIR)

    if not files:
        print("❌ No files found.")
        return

    show_files(files)

    print("\n========== MENU ==========")
    print("1. Rename File")
    print("2. Copy File")
    print("3. Move File")
    print("0. Exit")

    choice = input("\nEnter your choice: ").strip()

    if choice == "1":
        number = int(input("Enter file number: ")) - 1

        if 0 <= number < len(files):
            new_name = input("Enter new file name (without extension): ").strip()

            success, result = rename_file(files[number], new_name)

            if success:
                print(f"\n✅ Renamed to: {result.name}")
            else:
                print(f"\n❌ {result}")

    elif choice == "2":
        number = int(input("Enter file number: ")) - 1

        if 0 <= number < len(files):
            success, result = copy_file(files[number], OUTPUT_DIR)

            if success:
                print(f"\n✅ Copied to: {result}")
            else:
                print(f"\n❌ {result}")

    elif choice == "3":
        number = int(input("Enter file number: ")) - 1

        if 0 <= number < len(files):
            success, result = move_file(files[number], OUTPUT_DIR)

            if success:
                print(f"\n✅ Moved to: {result}")
            else:
                print(f"\n❌ {result}")

    elif choice == "0":
        print("Goodbye!")

    else:
        print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
