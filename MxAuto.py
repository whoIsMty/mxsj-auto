import pyautogui
from MxWindow import MxWindow
import time


class MxAutoFB:
    def __init__(self, player_name):
        self.player_name = player_name
        pass

    def initialWindow(self):
        window = MxWindow(self.player_name)
        window.makeTheWindowTop()
        self.windowLocation = window.location

    def startInto(self):
        "实现进入FB"
        # 打开飞行旗到达副本接引人。
        pyautogui.press('f1', interval=0.4)
        pyautogui.press('1')
        # 打开周围NPC开始进入副本。
        time.sleep(1)
        pyautogui.keyDown('alt')
        pyautogui.keyDown('f')
        pyautogui.keyUp('alt')
        pyautogui.keyUp('f')
        pyautogui.click('neighborButton1.png')
        pyautogui.click('neighborButton2.png')

if __name__ == "__main__":
    test = MxAutoFB("°弥留之际．ι")
    test.initialWindow()
    test.startInto()
