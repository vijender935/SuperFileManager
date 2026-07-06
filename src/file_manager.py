from pathlib import Path


def create_folder(folder_path):
    """
    Create a folder if it doesn't already exist.
    """
    Path(folder_path).mkdir(parents=True, exist_ok=True)
