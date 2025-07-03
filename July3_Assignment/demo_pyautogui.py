import pyautogui
import time

# Always include a short delay to allow positioning or aborting
pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True  # Move mouse to top-left to abort

# Example 1: Open Start Menu and Search for Notepad
def open_notepad():
    pyautogui.press("win")
    time.sleep(1)
    pyautogui.write("notepad")
    pyautogui.press("enter")

# Example 2: Write a message in Notepad
def write_in_notepad():
    time.sleep(2)
    pyautogui.write("Hello, this message is typed using PyAutoGUI!", interval=0.05)

# Example 3: Move mouse in a square pattern
def move_mouse_square():
    for _ in range(4):
        pyautogui.move(200, 0, duration=0.5)
        pyautogui.move(0, 200, duration=0.5)
        pyautogui.move(-200, 0, duration=0.5)
        pyautogui.move(0, -200, duration=0.5)

# Run a demo
if __name__ == "__main__":
    open_notepad()
    write_in_notepad()
    move_mouse_square()
