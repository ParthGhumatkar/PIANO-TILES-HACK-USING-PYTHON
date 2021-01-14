Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from pyautogui import * 
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('esc') == False:

    if pyautogui.pixel(580,450)[0] == 0:
        click(580,450)
    if pyautogui.pixel(680,450)[0] == 0:
        click(680,450)
    if pyautogui.pixel(770,450)[0] == 0:
        click(770,450)
    if pyautogui.pixel(865,450)[0] == 0:
        click(865,450)
