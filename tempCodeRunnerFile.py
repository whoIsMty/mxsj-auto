import pyautogui
import time


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
    shift_1()
    auto_attack()
    time.sleep(2)


if __name__ == "__main__":

    while True:
        auto_2()
