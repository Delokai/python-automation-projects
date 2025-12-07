import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organize_files():
    folder = filedialog.askdirectory()

    if not folder:
        messagebox.showwarning("Warning", "No folder selected.")
        return

    file_types = {
        "Images": [".png", ".jpg", ".jpeg", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mov", ".avi"],
        "Code": [".py", ".js", ".html"]
    }

    # Create folders if needed
    for category in file_types:
        os.makedirs(os.path.join(folder, category), exist_ok=True)

    os.makedirs(os.path.join(folder, "Other"), exist_ok=True)

    # Sort files
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)

        if os.path.isdir(file_path):
            continue  # skip folders

        file_ext = os.path.splitext(filename)[1].lower()

        moved = False
        for category, extensions in file_types.items():
            if file_ext in extensions:
                shutil.move(file_path, os.path.join(folder, category, filename))
                moved = True
                break

        if not moved:
            shutil.move(file_path, os.path.join(folder, "Other", filename))

    messagebox.showinfo("Success", "Files organized successfully!")

# GUI Setup
window = tk.Tk()
window.title("File Organizer")
window.geometry("300x200")

label = tk.Label(window, text="Click to organize a folder:")
label.pack(pady=10)

button = tk.Button(window, text="Choose Folder", command=organize_files)
button.pack(pady=20)

window.mainloop()
