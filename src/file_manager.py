from pathlib import Path
import shutil


def create_folder(folder_path):
    Path(folder_path).mkdir(parents=True, exist_ok=True)


def folder_exists(folder_path):
    return Path(folder_path).exists()


def create_file(file_path):
    Path(file_path).touch(exist_ok=True)


def file_exists(file_path):
    return Path(file_path).exists()


def list_files(folder_path):
    return list(Path(folder_path).iterdir())
