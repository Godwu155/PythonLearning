# LOVE PLUS
import tkinter as tk
import random
import time


def create_tip_window(main_window, tips, bg_colors):
    window_width = 300
    window_height = 90
    x = random.randint(-30, 1500)
    y = random.randint(-20, 900)

    window = tk.Toplevel(main_window)
    window.title('温馨提示')
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    window.attributes('-topmost', True)

    tip = random.choice(tips)
    bg = random.choice(bg_colors)

    tk.Label(
        window,
        text=tip,
        bg=bg,
        font=('微软雅黑', 16),
        width=30,
        height=3
    ).pack()

    return window


def close_windows_one_by_one(all_windows, index=0, delay=10):
    if index < len(all_windows):
        window = all_windows[index]
        if window.winfo_exists():
            window.destroy()

        all_windows[0].master.after(delay, close_windows_one_by_one, all_windows, index + 1, delay)
    else:

        create_final_window(all_windows[0].master)


def create_final_window(main_window):
    final_width = 300
    final_height = 90
    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()
    x = (screen_width - final_width) // 2
    y = (screen_height - final_height) // 2

    final_window = tk.Toplevel(main_window)
    final_window.title('温馨提示')
    final_window.geometry(f"{final_width}x{final_height}+{x}+{y}")
    final_window.attributes('-topmost', True)

    tk.Label(
        final_window,
        text='我想C你妈了',
        bg='lightpink',
        font=('微软雅黑', 18, 'bold'),
        width=30,
        height=3
    ).pack()


def main():
    main_window = tk.Tk()
    main_window.withdraw()

    tips = [
        '多喝水哦~', '保持微笑呀', '每天都要元气满满',
        '记得吃水果', '保持好心情', '好好爱自己', '我想你了',
        '梦想成真', '期待下一次见面', '顺顺利利', '早点休息',
        '愿所有烦恼都消失', '别熬夜', '今天过得开心嘛', '天冷了，多穿衣服',
        ''
    ]
    bg_colors = [
        'lightpink', 'skyblue', 'lightgreen', 'lavender',
        'lightyellow', 'plum', 'coral', 'bisque', 'aquamarine',
        'mistyrose', 'honeydew', 'lavenderblush', 'oldlace'
    ]

    all_windows = []

    for _ in range(200):
        window = create_tip_window(main_window, tips, bg_colors)
        all_windows.append(window)
        main_window.update()
        time.sleep(0.01)

    main_window.after(2000, close_windows_one_by_one, all_windows)

    main_window.mainloop()


8
if __name__ == "__main__":
    main()