# SuperFileManager
# logger.py
# Version: 2.6

from datetime import datetime
from config import LOG_DIR

LOG_FILE = LOG_DIR / "app.log"


def write_log(action, message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write("-" * 40 + "\n")
        log.write(f"[{timestamp}]\n")
        log.write(f"{action}\n")
        log.write(f"{message}\n\n")
