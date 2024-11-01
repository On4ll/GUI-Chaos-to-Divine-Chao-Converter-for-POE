#Testing tkinter
import tkinter as tk

root = tk.Tk()
root.geometry("300x100")

entry = tk.Entry(root)
entry.insert("bla bla bla")
entry.pack(pady=20)

root.mainloop()
