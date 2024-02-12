from os import getenv
from pathlib import Path

DATABASE_PATH = Path(getenv("TSK_DB_PATH") or "task_manager/task_manager.json")
