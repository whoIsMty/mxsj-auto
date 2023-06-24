import random
import sys

import pyautogui
import time
from MxWindow import MxWindow


def shift_1():
    pyautogui.keyDown('alt')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('tab')


def shift_2():
    pyautogui.keyDown('alt')
    pyautogui.keyDown('tab')
    pyautogui.keyDown('tab')
    pyautogui.keyUp('alt')
    pyautogui.keyUp('tab')


def auto_attack():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('a')
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('a')


def auto_2():
    shift_1()
    auto_attack()
    shift_2()
    auto_attack()
    time.sleep(2)


def auto_1():
    auto_attack()


def locationPlusOffset(x, y):
    return [x[0] + y[0], x[1] + y[1]]

def location_loop(window_location: list):
    random_number = random.randint(1, 10) % 4
    map = locationPlusOffset(window_location, [30, 50])
    west = locationPlusOffset(window_location, [230, 330])
    north = locationPlusOffset(window_location, [380, 230])
    east = locationPlusOffset(window_location, [550, 330])
    south = locationPlusOffset(window_location, [380, 450])

    if random_number == 0 :
        pyautogui.click(*map)
        pyautogui.click(*north)
        pyautogui.rightClick(*north)

    elif random_number == 1 :
        pyautogui.click(*map)
        pyautogui.click(*west)
        pyautogui.rightClick(*west)

    elif random_number == 2 :
        pyautogui.click(*map)
        pyautogui.click(*east)
        pyautogui.rightClick(*east)

    elif random_number ==3 :
        pyautogui.click(*map)
        pyautogui.click(*south)
        pyautogui.rightClick(*south)
    time.sleep(1)

if __name__ == "__main__":
    test = MxWindow("°别让我走．ι")
    location_loop(test.location)
    while True:
        test.makeTheWindowTop()
        auto_attack()
        location_loop(test.location)
