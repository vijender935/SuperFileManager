from pathlib import Path

# ========= PROJECT INFO =========
PROJECT_NAME = "SuperFileManager"
VERSION = "1.0.0"

# ========= PROJECT ROOT =========
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# ========= PROJECT FOLDERS =========
INPUT_DIR = PROJECT_ROOT / "input"
OUTPUT_DIR = PROJECT_ROOT / "output"
BACKUP_DIR = PROJECT_ROOT / "backup"
LOG_DIR = PROJECT_ROOT / "logs"
DOCS_DIR = PROJECT_ROOT / "docs"
TESTS_DIR = PROJECT_ROOT / "tests"
