# coding: utf-8
import tkinter as tk
from datetime import datetime


def update():
    delay = 98
    now = datetime.now()
    if now.microsecond < 120000:
        lable.configure(text=datetime.strftime(now, "%H:%M:%S"))
        delay = 860
    root.after(delay, update)


if __name__ == '__main__':
    root = tk.Tk()
    lable = tk.Label(root, text=datetime.strftime(datetime.now(), "%H:%M:%S"), foreground="red", background="#ff2121",
                     font=('Segoe Script', 16))
    lable.pack()
    root.overrideredirect(True)
    root.geometry("+1860+0")  # 900 for 1080p
    root.wm_attributes('-topmost', 1)
    # root.attributes('-alpha', 0.8)
    root.attributes('-transparentcolor', "#ff2121")
    update()
    root.mainloop()
