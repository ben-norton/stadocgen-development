from pathlib import Path

# General purpose project untilities

def get_project_root() -> Path:
    return Path(__file__).parent.parent

