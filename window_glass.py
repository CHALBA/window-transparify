import win32gui
import win32con
import keyboard

def set_transparent():
    # বর্তমানে যে উইন্ডোটি সামনে আছে সেটিকে সিলেক্ট করবে
    hwnd = win32gui.GetForegroundWindow()
    
    # উইন্ডো স্টাইল পরিবর্তন করে লেয়ার্ড (Layered) করবে
    style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, style | win32con.WS_EX_LAYERED)
    
    # ১২৮ মানে ৫০% স্বচ্ছতা (০ = সম্পূর্ণ অদৃশ্য, ২৫৫ = স্বাভাবিক)
    win32gui.SetLayeredWindowAttributes(hwnd, 0, 230, win32con.LWA_ALPHA)
    print("Window is now transparent!")

def set_normal():
    hwnd = win32gui.GetForegroundWindow()
    style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    
    # ২৫৫ দিয়ে উইন্ডো আবার স্বাভাবিক করা
    win32gui.SetLayeredWindowAttributes(hwnd, 0, 255, win32con.LWA_ALPHA)
    print("Window is back to normal!")

print("Script running... Press Ctrl+Alt+T to transparent, Ctrl+Alt+N for normal.")

# কিবোর্ড শর্টকাট সেট করা
keyboard.add_hotkey('ctrl+alt+t', set_transparent)
keyboard.add_hotkey('ctrl+alt+n', set_normal)

# স্ক্রিপ্টটি চালু রাখার জন্য লুপ
keyboard.wait()
