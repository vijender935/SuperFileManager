# SuperFileManager
# main.py
# Version: 6.3

from logger import write_log
from config import (
    PROJECT_NAME,
    VERSION,
    INPUT_DIR,
    OUTPUT_DIR,
    BACKUP_DIR,
    LOG_DIR,
    DOCS_DIR,
    TESTS_DIR,
    DEFAULT_WIDTH,
    DEFAULT_HEIGHT,
    SUPPORTED_IMAGE_FORMATS,
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
    delete_file,
    batch_rename,
    batch_copy,
    batch_move,
    batch_delete,
    search_files,
    filter_files,
    sort_files,
    get_statistics,
    resize_image,
    batch_resize,
    convert_image,
    batch_convert,
    get_valid_file,
    get_non_empty_name,
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


def show_menu():
    print("\n========== MENU ==========")
    print("1. Rename File")
    print("2. Copy File")
    print("3. Move File")
    print("4. Delete File")
    print("5. Batch Rename")
    print("6. Batch Copy")
    print("7. Batch Move")
    print("8. Batch Delete")
    print("9. Search File")
    print("10. Filter Files")
    print("11. Sort Files")
    print("12. File Statistics")
    print("13. Resize Image")
    print("14. Batch Resize Images")
    print("15. Convert Image Format")
    print("16. Batch Convert Images")
    print("0. Exit")


def get_choice():
    return input("\nEnter your choice: ").strip()


def rename_menu(files):
    number = get_valid_file(files)
    new_name = get_non_empty_name()

    success, result = rename_file(files[number], new_name)

    if success:
        print(f"\n✅ Renamed to: {result.name}")
        write_log("RENAME", f"{files[number].name} -> {result.name}")
    else:
        print(f"\n❌ {result}")


def copy_menu(files):
    number = get_valid_file(files)

    success, result = copy_file(files[number], OUTPUT_DIR)

    if success:
        print("\n✅ Copied successfully!")
        print(f"Destination: {result}")
        write_log("COPY", f"{files[number].name} -> {result.name}")
    else:
        print(f"\n❌ {result}")


def move_menu(files):
    number = get_valid_file(files)

    success, result = move_file(files[number], OUTPUT_DIR)

    if success:
        print("\n✅ Moved successfully!")
        print(f"Destination: {result}")
        write_log("MOVE", f"{files[number].name} -> {result.name}")
    else:
        print(f"\n❌ {result}")


def delete_menu(files):
    number = get_valid_file(files)

    confirm = input("Are you sure? (y/n): ").strip().lower()

    if confirm != "y":
        print("\n❌ Delete cancelled.")
        return

    success, result = delete_file(files[number])

    if success:
        print(f"\n✅ {result}")
        write_log("DELETE", files[number].name)
    else:
        print(f"\n❌ {result}")


def batch_rename_menu(files):
    prefix = input("Enter file name prefix: ").strip()

    if not prefix:
        print("\n❌ Prefix cannot be empty.")
        return

    renamed_files = batch_rename(files, prefix)

    print("\n✅ Batch Rename Completed!\n")

    for old_name, new_name in renamed_files:
        print(f"{old_name} → {new_name}")
        write_log("BATCH RENAME", f"{old_name} -> {new_name}")


def batch_copy_menu(files):
    copied_files = batch_copy(files, OUTPUT_DIR)

    print("\n✅ Batch Copy Completed!\n")

    for old_name, new_name in copied_files:
        print(f"{old_name} → {new_name}")
        write_log("BATCH COPY", f"{old_name} -> {new_name}")


def batch_move_menu(files):
    moved_files = batch_move(files, OUTPUT_DIR)

    print("\n✅ Batch Move Completed!\n")

    for old_name, new_name in moved_files:
        print(f"{old_name} → {new_name}")
        write_log("BATCH MOVE", f"{old_name} -> {new_name}")


def batch_delete_menu(files):
    confirm = input(
        "\nDelete ALL files from Input folder? (y/n): "
    ).strip().lower()

    if confirm != "y":
        print("\n❌ Batch Delete Cancelled.")
        return

    deleted_files = batch_delete(files)

    print("\n✅ Batch Delete Completed!\n")

    for file_name in deleted_files:
        print(file_name)
        write_log("BATCH DELETE", file_name)


def search_menu(files):
    keyword = input(
        "\nEnter file name to search: "
    ).strip()

    if not keyword:
        print("\n❌ Search text cannot be empty.")
        return

    results = search_files(files, keyword)

    if not results:
        print("\n❌ No matching files found.")
        return

    print(f"\n✅ Found {len(results)} file(s):\n")

    for i, file in enumerate(results, start=1):
        print(f"{i}. {file.name}")
        print(f"   Size: {get_file_size(file)}")

    write_log(
        "SEARCH",
        keyword
    )


def filter_menu(files):
    extension = input(
        "\nEnter extension (jpg/png/pdf): "
    ).strip()

    if not extension:
        print("\n❌ Extension cannot be empty.")
        return

    results = filter_files(files, extension)

    if not results:
        print(f"\n❌ No .{extension} files found.")
        return

    print(f"\n✅ Found {len(results)} .{extension} file(s):\n")

    for i, file in enumerate(results, start=1):
        print(f"{i}. {file.name}")

    write_log(
        "FILTER",
        extension
    )


def sort_menu(files):
    print("\nSort By")
    print("1. Name")
    print("2. Size")
    print("3. Date")

    option = input("\nChoose: ").strip()

    if option not in ("1", "2", "3"):
        print("\n❌ Invalid option.")
        return

    results = sort_files(files, option)

    print("\n✅ Sorted Files:\n")

    for i, file in enumerate(results, start=1):
        print(f"{i}. {file.name}")
        print(f"   {get_file_size(file)}")

    write_log("SORT", option)


def statistics_menu(files):
    stats = get_statistics(files)

    print("\n========== Statistics ==========")

    print(f"Total Files : {stats['total_files']}")

    print(
        f"Total Size  : "
        f"{stats['total_size'] / (1024 * 1024):.2f} MB"
    )

    print(f"Image Files : {stats['image_files']}")

    write_log("STATISTICS", "Viewed")


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

    show_menu()

    choice = get_choice()

    if choice == "1":
        rename_menu(files)

    elif choice == "2":
        copy_menu(files)

    elif choice == "3":
        move_menu(files)

    elif choice == "4":
        delete_menu(files)

    elif choice == "5":
        batch_rename_menu(files)

    elif choice == "6":
        batch_copy_menu(files)

    elif choice == "7":
        batch_move_menu(files)

    elif choice == "8":
        batch_delete_menu(files)

    elif choice == "9":
        search_menu(files)

    elif choice == "10":
        filter_menu(files)

    elif choice == "11":
        sort_menu(files)

    elif choice == "12":
        statistics_menu(files)

    elif choice == "13":
        number = get_valid_file(files)

        destination = OUTPUT_DIR / files[number].name

        success, result = resize_image(
            files[number],
            destination,
            DEFAULT_WIDTH,
            DEFAULT_HEIGHT,
        )

        if success:
            print("\n✅ Image resized successfully!")
            print(result)

            write_log(
                "RESIZE",
                f"{files[number].name} -> {result.name}"
            )

        else:
            print(f"\n❌ {result}")

    elif choice == "14":
        resized_files = batch_resize(
            files,
            OUTPUT_DIR,
            DEFAULT_WIDTH,
            DEFAULT_HEIGHT,
        )

        print("\n✅ Batch Resize Completed!\n")

        for old_name, new_name in resized_files:
            print(f"{old_name}  →  {new_name}")

            write_log(
                "BATCH RESIZE",
                f"{old_name} -> {new_name}"
            )

    elif choice == "15":
        number = get_valid_file(files)

        fmt = input(
            "Enter format (jpg/png/webp): "
        ).strip().lower()

        formats = {
            "jpg": "JPEG",
            "png": "PNG",
            "webp": "WEBP",
        }

        if fmt not in formats:
            print("\n❌ Invalid format.")
            return

        destination = OUTPUT_DIR / (
            files[number].stem + "." + fmt
        )

        success, result = convert_image(
            files[number],
            destination,
            formats[fmt],
        )

        if success:
            print("\n✅ Image converted successfully!")
            print(result)

            write_log(
                "CONVERT",
                f"{files[number].name} -> {result.name}"
            )

        else:
            print(f"\n❌ {result}")

    elif choice == "16":
        fmt = input(
            "Convert all images to (jpg/png/webp): "
        ).strip().lower()

        formats = {
            "jpg": "JPEG",
            "png": "PNG",
            "webp": "WEBP",
        }

        if fmt not in formats:
            print("\n❌ Invalid format.")
            return

        converted_files = batch_convert(
            files,
            OUTPUT_DIR,
            formats[fmt],
        )

        print("\n✅ Batch Conversion Completed!\n")

        for old_name, new_name in converted_files:
            print(f"{old_name}  →  {new_name}")

            write_log(
                "BATCH CONVERT",
                f"{old_name} -> {new_name}"
            )

    elif choice == "0":
        print("Goodbye!")

    else:
        print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
