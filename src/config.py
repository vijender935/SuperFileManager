
from pathlib import Path

# ========= PROJECT INFO =========
PROJECT_NAME = "SuperFileManager"
VERSION = "1.0.0"

# ========= PHONE STORAGE ROOT =========
PROJECT_ROOT = Path("/storage/emulated/0/SuperFileManager")

# ========= PROJECT FOLDERS =========
INPUT_DIR = PROJECT_ROOT / "input"
OUTPUT_DIR = PROJECT_ROOT / "output"
BACKUP_DIR = PROJECT_ROOT / "backup"
LOG_DIR = PROJECT_ROOT / "logs"
DOCS_DIR = PROJECT_ROOT / "docs"
TESTS_DIR = PROJECT_ROOT / "tests"

# Image Resize Settings
DEFAULT_WIDTH = 1080
DEFAULT_HEIGHT = 2340
SUPPORTED_IMAGE_FORMATS = (".jpg", ".jpeg", ".png", ".webp")

# AI Output Settings
AI_OUTPUT_DIR = OUTPUT_DIR / "AI_Enhanced"
