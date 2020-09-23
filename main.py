import pyautogui
import time
pyautogui.FAILSAFE = False

#this loop will run for 3 times.
for i in range(0, 3):
    time.sleep(5)
    pyautogui.press('j')
    time.sleep(3)
    pyautogui.press('l')
    time.sleep(2)
    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')