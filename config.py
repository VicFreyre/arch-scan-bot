from pathlib import Path

APP_HOST = "127.0.0.1"
APP_PORT = 5000
DB_PATH = Path("./vuln_lab.sqlite")
UPLOAD_DIR = Path("./uploads")
MAX_UPLOAD_SIZE = 2 * 1024 * 1024  # 2 MB

UPLOAD_DIR.mkdir(exist_ok=True, parents=True)
