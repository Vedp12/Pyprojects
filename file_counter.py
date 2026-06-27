#!/usr/bin/env python3

import os

# Directories to completely skip
SKIP_DIRS = {
    "/proc",
    "/sys",
    "/dev",
    "/run",
    "/tmp",
    "/snap",
    "/var/cache",
    "/var/lib/docker",
    "/lost+found",
    "/linuxbrew"
}

# Folder names to ignore wherever found
SKIP_NAMES = {
    "node_modules",
    "venv",
    ".venv",
    "env",
    ".env",
    "__pycache__",
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".npm",
    ".cache"

}

total_files = 0
total_folders = 0


def should_skip(path):
    """Check if path should be skipped."""
    if path in SKIP_DIRS:
        return True

    folder_name = os.path.basename(path)

    if folder_name in SKIP_NAMES:
        return True

    return False


# Change this if you want another starting location
START_PATH = "/home"

for root, dirs, files in os.walk(
    START_PATH,
    topdown=True,
    followlinks=False
):
    # Remove skipped directories before descending
    dirs[:] = [
        d for d in dirs
        if not should_skip(os.path.join(root, d))
    ]

    folder_count = len(dirs)
    file_count = len(files)

    total_folders += folder_count
    total_files += file_count

    print(f"\nFolder: {root}")
    print(f"Files: {file_count}")
    print(f"Subfolders: {folder_count}")

print("\n" + "=" * 50)
print("SCAN COMPLETE")
print("=" * 50)
print(f"Total Folders: {total_folders:,}")
print(f"Total Files:   {total_files:,}")
print(f"Grand Total:   {total_folders + total_files:,}")