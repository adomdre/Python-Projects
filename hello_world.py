import tkinter as tk

root = tk.Tk()
root.title("Hello, World!")
tk.Label(root, text="Hello, World!", font=("Arial", 16)).pack(padx=20, pady=20)

root.mainloop()