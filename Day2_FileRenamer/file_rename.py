import os

def rename_files():
    folder = "."  # current folder
    files = os.listdir(folder)

    for index, filename in enumerate(files):
        # Skip the Python file itself so we don't rename it
        if filename.endswith(".py"):
            continue

        extension = os.path.splitext(filename)[1]
        new_name = f"file_{index}{extension}"

        os.rename(filename, new_name)
        print(f"Renamed {filename} → {new_name}")

rename_files()
