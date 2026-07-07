# SuperFileManager
# file_manager.py
# Version: 5.0

from pathlib import Path
from shutil import copy2, move


def create_folder(folder):
    folder.mkdir(parents=True, exist_ok=True)


def folder_exists(folder):
    return folder.exists() and folder.is_dir()


def list_files(folder):
    files = []

    for file in folder.iterdir():
        if file.is_file():
            files.append(file)

    return files


def get_file_size(file):
    size = file.stat().st_size

    if size < 1024:
        return f"{size} Bytes"
    elif size < 1024 * 1024:
        return f"{size / 1024:.2f} KB"
    else:
        return f"{size / (1024 * 1024):.2f} MB"


def get_image_format(file):
    try:
        from PIL import Image

        with Image.open(file) as img:
            return img.format

    except Exception:
        return "Unknown"


def get_image_resolution(file):
    try:
        from PIL import Image

        with Image.open(file) as img:
            width, height = img.size

        return f"{width} × {height}"

    except Exception:
        return "Unknown"


def get_image_orientation(file):
    try:
        from PIL import Image

        with Image.open(file) as img:
            width, height = img.size

        if width > height:
            return "Landscape"
        elif height > width:
            return "Portrait"
        else:
            return "Square"

    except Exception:
        return "Unknown"


def get_image_mode(file):
    try:
        from PIL import Image

        with Image.open(file) as img:
            return img.mode

    except Exception:
        return "Unknown"


def get_image_color_depth(file):
    try:
        from PIL import Image

        with Image.open(file) as img:
            mode = img.mode

        color_depth = {
            "1": "1-bit",
            "L": "8-bit",
            "P": "8-bit",
            "RGB": "24-bit",
            "RGBA": "32-bit",
            "CMYK": "32-bit",
            "I": "32-bit",
            "F": "32-bit",
        }

        return color_depth.get(mode, "Unknown")

    except Exception:
        return "Unknown"


def get_image_dpi(file):
    try:
        from PIL import Image

        with Image.open(file) as img:
            dpi = img.info.get("dpi")

        if dpi:
            return f"{int(dpi[0])} × {int(dpi[1])}"

        return "Not Available"

    except Exception:
        return "Unknown"


def get_unique_filename(destination_folder, file_name):
    """
    Return a unique filename if the same name already exists.
    Example:
    photo.jpg
    photo (1).jpg
    photo (2).jpg
    """

    destination = destination_folder / file_name

    if not destination.exists():
        return destination

    stem = destination.stem
    suffix = destination.suffix

    counter = 1

    while True:
        new_name = f"{stem} ({counter}){suffix}"
        new_destination = destination_folder / new_name

        if not new_destination.exists():
            return new_destination

        counter += 1


def rename_file(file, new_name):
    try:
        extension = file.suffix
        new_file = file.with_name(new_name + extension)

        file.rename(new_file)

        return True, new_file

    except Exception as e:
        return False, str(e)


def copy_file(file, destination_folder):
    try:                                                        # Fix: try ke baad nayi line
        destination = get_unique_filename(destination_folder, file.name)

        copy2(file, destination)

        return True, destination

    except Exception as e:
        return False, str(e)


def move_file(file, destination_folder):
    try:
        destination = get_unique_filename(destination_folder, file.name)

        move(str(file), str(destination))

        return True, destination

    except Exception as e:
        return False, str(e)


def delete_file(file):
    try:
        file.unlink()

        return True, "File deleted successfully."

    except Exception as e:
        return False, str(e)


def batch_rename(files, prefix):
    renamed = []

    files = sorted(files)

    for i, file in enumerate(files, start=1):
        extension = file.suffix
        new_name = f"{prefix}_{i:03}{extension}"

        new_file = file.with_name(new_name)

        file.rename(new_file)

        renamed.append((file.name, new_file.name))

    return renamed


def batch_copy(files, destination_folder):
    copied = []

    for file in files:
        success, result = copy_file(file, destination_folder)

        if success:
            copied.append((file.name, result.name))

    return copied


def batch_move(files, destination_folder):
    moved = []

    for file in files:
        success, result = move_file(file, destination_folder)

        if success:
            moved.append((file.name, result.name))

    return moved


def batch_delete(files):
    deleted = []

    for file in files:
        success, message = delete_file(file)

        if success:
            deleted.append(file.name)

    return deleted


def get_valid_file(files):
    while True:
        try:
            number = int(input("Enter file number: ")) - 1

            if 0 <= number < len(files):
                return number

            print(f"❌ Please enter a number between 1 and {len(files)}.")

        except ValueError:
            print("❌ Please enter a valid number.")


def get_non_empty_name():
    while True:
        name = input("Enter new file name (without extension): ").strip()

        if name:
            return name

        print("❌ File name cannot be empty.")


def search_files(files, keyword):
    keyword = keyword.lower().strip()

    results = []

    for file in files:
        if keyword in file.name.lower():
            results.append(file)

    return results


def filter_files(files, extension):
    extension = extension.lower().strip().lstrip(".")

    results = []

    for file in files:
        if file.suffix.lower() == f".{extension}":
            results.append(file)

    return results


def sort_files(files, option):

    if option == "1":
        return sorted(files, key=lambda file: file.name.lower())

    elif option == "2":
        return sorted(files, key=lambda file: file.stat().st_size)

    elif option == "3":
        return sorted(files, key=lambda file: file.stat().st_mtime)

    return files


def get_statistics(files):
    total_files = len(files)

    total_size = sum(file.stat().st_size for file in files)

    image_files = sum(
        1 for file in files
        if file.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp")
    )

    return {
        "total_files": total_files,
        "total_size": total_size,
        "image_files": image_files,
    }
