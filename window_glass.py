import win32gui
import win32con
import keyboard
from datetime import datetime
import sys
import tkinter as tk
from tkinter import messagebox

# এক্সপায়ারি ডেট (১৮ জুন সারা দিন চলবে, ১৯ জুন লক হবে)
EXPIRY_DATE = "2026-06-18" 

def check_expiry():
    current_date = datetime.now().date()
    expiry_target = datetime.strptime(EXPIRY_DATE, "%Y-%m-%d").date()

    if current_date > expiry_target:
        root = tk.Tk()
        root.withdraw() 
        # এখানে মেসেজটি এমনভাবে দেওয়া হয়েছে যাতে মনে হয় এটি উইন্ডোজ বা অ্যাপের কোনো স্বাভাবিক এরর
        messagebox.showerror("System Error", "The application failed to initialize properly (0xc000007b).\nClick OK to terminate the application.")
        sys.exit() 

# স্ক্রিপ্ট চালুর শুরুতেই এক্সপায়ারি চেক হবে
check_expiry()

def set_transparent():
    hwnd = win32gui.GetForegroundWindow()
    style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, style | win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(hwnd, 0, 200, win32con.LWA_ALPHA)

def set_normal():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)

# এখানে আগের সেই প্রিন্ট লাইনগুলো সম্পূর্ণ মুছে দেওয়া হয়েছে, ফলে কালো উইন্ডোতে কিচ্ছু লেখা উঠবে না!
keyboard.add_hotkey('ctrl+alt+t', set_transparent)
keyboard.add_hotkey('ctrl+alt+n', set_normal)

keyboard.wait()
