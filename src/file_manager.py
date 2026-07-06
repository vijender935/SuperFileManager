from pathlib import Path


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
