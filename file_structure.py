import os


def display_files(dst):
    total_files = 0
    total_folders = 0

    with os.scandir(dst) as entries:
        for no, entry in enumerate(entries):

            if entry.is_file():
                print(f" ├──{no+1} {entry.name}")
                total_files += 1

            elif entry.is_dir(follow_symlinks=False):
                print(f"──{os.path.join(dst, entry.name)}")

                sub_files, sub_folders = display_files(entry.path)

                total_files += sub_files
                total_folders += sub_folders + 1

    return total_files, total_folders


dst = "/home/tux_106/Documents/"
files, folders = display_files(dst)

print("\nGrand Total")
print("Files =", files)
print("Folders =", folders)
