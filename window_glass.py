import win32gui
import win32con
import keyboard
from datetime import datetime
import sys
import tkinter as tk
from tkinter import messagebox

# ১. এখানে আপনার পছন্দমতো এক্সপায়ারি ডেট সেট করুন (YYYY-MM-DD ফরম্যাটে)
# ১৮ জুন সারা দিন চলবে, ১৯ জুন রাত ১২টা বাজলেই লক হয়ে যাবে।
EXPIRY_DATE = "2026-06-18" 

def check_expiry():
    # সরাসরি পিসির লোকাল টাইম থেকে আজকের তারিখ নেওয়া হচ্ছে
    current_date = datetime.now().date()
    expiry_target = datetime.strptime(EXPIRY_DATE, "%Y-%m-%d").date()

    # পিসির তারিখ এক্সপায়ারি ডেট পার হয়ে গেলেই প্রোগ্রাম বন্ধ করে দেবে
    if current_date > expiry_target:
        root = tk.Tk()
        root.withdraw() # মূল tkinter উইন্ডো হাইড রাখা
        messagebox.showerror("Error", "This software version has expired! Please contact the developer.")
        sys.exit() # প্রোগ্রামটি চিরতরে বন্ধ করে দেওয়া

# স্ক্রিপ্ট চালুর শুরুতেই এক্সপায়ারি চেক হবে
check_expiry()

def set_transparent():
    hwnd = win32gui.GetForegroundWindow()
    style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, style | win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(hwnd, 0, 200, win32con.LWA_ALPHA)
    print("Window is now transparent!")

def set_normal():
    hwnd = win32gui.GetForegroundWindow()
    win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)
    print("Window is back to normal!")

print(f"Script running... Expiry date set to: {EXPIRY_DATE}")
print("Press Ctrl+Alt+T to transparent, Ctrl+Alt+N for normal.")

keyboard.add_hotkey('ctrl+alt+t', set_transparent)
keyboard.add_hotkey('ctrl+alt+n', set_normal)

keyboard.wait()
