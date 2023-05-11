import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness
from PIL import Image, ImageTk

set_dpi_awareness()

root=tk.Tk()
root.geometry("800x600")
root.resizable(False,False)
root.title("Widget Examples")

lbl1 = ttk.Label(root,text="Widget Example",padding=20)
#lbl1.config(font=("Arial",20))
lbl1.config(font=("Segoe UI",20))
lbl1.pack()

img1 =Image.open(root,""

root.mainloop()
