import os
import shutil

def organize_folder():
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mov", ".avi"],
        "Audio": [".mp3", ".wav"],
        "Others": []
    }

    files = os.listdir(".")

    for file in files:
        if file == "organize.py":
            continue

        ext = os.path.splitext(file)[1].lower()

        moved = False
        for folder, extensions in file_types.items():
            if ext in extensions:
                if not os.path.exists(folder):
                    os.mkdir(folder)

                shutil.move(file, os.path.join(folder, file))
                print(f"Moved {file} → {folder}/")
                moved = True
                break

        if not moved:
            if not os.path.exists("Others"):
                os.mkdir("Others")

            shutil.move(file, os.path.join("Others", file))
            print(f"Moved {file} → Others/")

if __name__ == "__main__":
    organize_folder()
