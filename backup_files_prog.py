"""
Create a backup of a file only if it has been modified.
"""

from pathlib import Path
from datetime import datetime
import shutil

SOURCE_FILE = Path(r"E:\Practice\Github\Python_tutorial\file_handling05.py")
BACKUP_FOLDER = Path(r"E:\Practice\backups")

def backup_if_modified(source_file: Path, backup_folder: Path) -> None:
    """
    Create a backup of the source file if it has changed.
    """
    print(source_file)
    print(source_file.exists())

    if not source_file.exists():
        print("Source file doesn't exist")
        return

    backup_folder.mkdir(parents=True, exist_ok=True)

    pattern = f"{source_file.stem}_*{source_file.suffix}"
    backups = list(backup_folder.glob(pattern))

    source_mtime = source_file.stat().st_mtime

    if backups:
        latest_backup = max(
            backups,
            key=lambda backup: backup.stat().st_mtime
        )

        if latest_backup.stat().st_mtime >= source_mtime:
            print("No changes detected. Backup not required.")
            return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = (
        backup_folder /
        f"{source_file.stem}_{timestamp}{source_file.suffix}"
    )

    shutil.copy2(source_file, backup_file)

    print(f"Backup created: {backup_file}")


def main() -> None:
    """Main function."""
    backup_if_modified(SOURCE_FILE, BACKUP_FOLDER)

if __name__ == "__main__":
    main()
