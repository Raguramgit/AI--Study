import  pyautogui
import time
print ("Hello from RPA with Python")

#Mouse operations using pyautogui
pyautogui.click(100, 100)
time.sleep(3)
pyautogui.rightClick(100, 100)
time.sleep(3)
pyautogui.doubleClick(100, 1000)

#Keyboard operations using pyautogui
time.sleep(3)
pyautogui.write("Hello from RPA with Python", interval=0.1)
pyautogui.press("enter")