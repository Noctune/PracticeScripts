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
    lable = tk.Label(root, foreground="red", background="#ff2121",
                     font=('Segoe Script', 16))
    lable.pack()
    # 无边框
    root.overrideredirect(True)
    # 获取所需的窗口宽度
    window_width = root.winfo_reqwidth()
    screen_width = root.winfo_screenwidth()
    # 计算居中的x位置
    x = (screen_width - window_width) // 2 + 30
    root.geometry(f"+{x}+0")
    root.wm_attributes('-topmost', 1)
    # root.attributes('-alpha', 0.8)
    root.attributes('-transparentcolor', "#ff2121")
    update()
    root.mainloop()
