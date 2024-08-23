import pyautogui
import pyperclip


class KeyboardAction:

    @staticmethod
    def keyDown(key):
        pyautogui.keyDown(key)

    @staticmethod
    def keyUp(key):
        pyautogui.keyUp(key)

    @staticmethod
    def keyPress(key):
        KeyboardAction.keyDown(key)
        KeyboardAction.keyUp(key)

    @staticmethod
    def hotKey(*keys):
        for key in keys:
            KeyboardAction.keyDown(key)
        for key in keys:
            KeyboardAction.keyUp(key)

    @staticmethod
    def write(text):
        pyperclip.copy(text)
        KeyboardAction.hotKey("ctrl", "v")
