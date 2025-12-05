import tkinter as tk

def show_message():
    user_text = entry.get()
    output_label.config(text=f"You typed: {user_text}")

# Create window
window = tk.Tk()
window.title("My First GUI App")
window.geometry("300x200")

# Input field
entry = tk.Entry(window, width=25)
entry.pack(pady=10)

# Button
button = tk.Button(window, text="Show Message", command=show_message)
button.pack(pady=10)

# Output label
output_label = tk.Label(window, text="")
output_label.pack(pady=10)

# Start the GUI loop
window.mainloop()
