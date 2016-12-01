'''Clicks over and over again while playing Clicker Heroes in Chrome.

Safety features:
Caps lock must be toggled on
Active window title must contain "Clicker Heroes" and "Google Chrome"

Prevent resource hogging:
Only checks for caps lock once per second
'''

import win32api, win32con, win32gui
#python -m pip install pypiwin32
import time

while True:
    time.sleep(0.01)
    capsLockOn = win32api.GetKeyState(win32con.VK_CAPITAL)
    if (capsLockOn == 1):
        topWinText = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        if (("Clicker Heroes" in topWinText) and 
            ("Google Chrome" in topWinText)):
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0)
    else:
        time.sleep(1)
