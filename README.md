# Window Transparify 🪟✨

A lightweight Python script that allows you to make any active window transparent with a simple keyboard shortcut. Perfect for multitasking, like watching YouTube videos in the background while coding or working in the foreground!

## Features
- 🎯 **Make Active Window Transparent:** Instantly fade the window you are currently working on.
- 🔄 **Restore to Normal:** Bring the window back to full visibility with another shortcut.
- ⚡ **Global Hotkeys:** Works seamlessly from the background while you are inside any application.

## Keyboard Shortcuts
- `Ctrl + Alt + T` : Toggle transparency.
- `Ctrl + Alt + N` : Restore window to 100% normal opacity.

## Prerequisites
This script requires **Windows OS** and **Python 3.x**.

## Installation

1. Clone this repository or download the source code:
   ```bash
   git clone https://github.com
   ```

2. Install the required dependencies:
   ```bash
   pip install pywin32 keyboard
   ```

## Usage

Run the script using Python:
```bash
python window_glass.py
```
Keep the terminal window running, switch to your desired application, and use the hotkeys!

## Customization
You can easily adjust the transparency depth by changing the number `128` inside the `win32gui.SetLayeredWindowAttributes` function (ranges from `0` for completely invisible to `255` for completely solid).

## License
This project is open-source and available under the [MIT License](LICENSE).
