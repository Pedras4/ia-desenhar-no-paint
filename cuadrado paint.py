import pyautogui
from time import sleep

pyautogui.press("win")
sleep(1)
pyautogui.write("paint")
sleep(1)
pyautogui.press("enter")
sleep(2)
pyautogui.click(481,170)
sleep(2)
pyautogui.mouseDown(310,450)
pyautogui.moveTo(510,450, duration=0.5)
pyautogui.moveTo(510,250, duration=0.5)
pyautogui.moveTo(310,250, duration=0.5)
pyautogui.moveTo(310,450, duration=0.5)
pyautogui.mouseUp()
