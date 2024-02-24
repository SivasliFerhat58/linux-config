import keyboard
import mouse
import time

time.sleep(5)
while True:
    mouse.click('left')
    time.sleep(0.1)
    keyboard.press('a')
    keyboard.release('a')
    time.sleep(0.1)
    keyboard.press("tab")
    keyboard.release("tab")
    time.sleep(0.1)
    keyboard.press('b')
    keyboard.release('b')
    time.sleep(0.1)
    keyboard.press("tab")
    keyboard.release("tab")
    time.sleep(0.1)
    keyboard.press('enter')
    keyboard.release('enter')
    time.sleep(0.1)
    keyboard.press('enter')
    time.sleep(1)