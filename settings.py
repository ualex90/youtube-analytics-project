import os
from pathlib import Path
from dotenv import load_dotenv

# Переменные окружения из файла .env
load_dotenv()
API_KEY: str = os.getenv('YT_API_KEY')

# Пути дирректорий
ROOT = Path(__file__).resolve().parent
SRC = Path(ROOT, "src")
FIXTURES = Path(SRC, "fixtures")
