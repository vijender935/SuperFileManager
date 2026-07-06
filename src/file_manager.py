# SuperFileManager
# file_manager.py
# Version: 2.2

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


def rename_file(file, new_name):
    try:
        extension = file.suffix
        new_file = file.with_name(new_name + extension)

        file.rename(new_file)

        return True, new_file

    except Exception as e:
        return False, str(e)


def copy_file(file, destination_folder):
    try:
        destination = destination_folder / file.name

        copy2(file, destination)

        return True, destination

    except Exception as e:
        return False, str(e)


def move_file(file, destination_folder):
    try:
        destination = destination_folder / file.name

        move(str(file), str(destination))

        return True, destination

    except Exception as e:
        return False, str(e)
