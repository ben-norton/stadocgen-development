import os
from pathlib import Path

def get_project_root() -> Path:
    return os.path.dirname(os.path.abspath(__file__))
