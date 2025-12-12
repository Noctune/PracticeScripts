# coding: utf-8
import tkinter as tk
from datetime import datetime


def update():
    now = datetime.now()
    # 更新时间显示
    lable.configure(text=now.strftime("%H:%M:%S"))
    # 计算到下一个整秒的时间间隔（毫秒）
    delay = 1000 - now.microsecond // 1000
    # 确保delay至少为1毫秒，避免过快更新
    delay = max(delay, 1)
    if 0 == now.second:
        root.wm_attributes("-topmost", 1)
    root.after(delay, update)


if __name__ == "__main__":
    root = tk.Tk()
    lable = tk.Label(
        root,
        text="00:00:00",
        foreground="red",
        background="#ff2121",
        font=("Segoe Script", 16),
    )  # 个性
    lable.pack()
    # 无边框
    root.overrideredirect(True)
    # 获取所需的窗口宽度
    window_width = root.winfo_reqwidth()
    screen_width = root.winfo_screenwidth()
    # 计算居中的x坐标
    x = (screen_width - window_width // 2) // 2
    root.geometry(f"+{x}+0")
    root.wm_attributes("-topmost", 1)
    # root.attributes('-alpha', 0.8)
    root.attributes("-transparentcolor", "#ff2121")
    update()
    root.mainloop()
