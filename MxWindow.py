import pyautogui
import win32gui
import os

wd = os.getcwd()


class MxWindow:
    location = []
    normalLocation = {"left": 500, "top": 0, }

    def __init__(self, player_name):
        self.player_name = player_name
        self.window = self.get_the_window()
        print(self.window)
        self.location = self.getGameWindowLocation()

    def getGameWindowLocation(self):

        left, top, right, bottom = win32gui.GetWindowRect(self.window)
        return [left, top, right, bottom]

    def get_all_window_handles(self):
        hwnd_title = dict()

        def get_all_hwnd(hwnd, mouse):
            if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
                hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
        win32gui.EnumWindows(get_all_hwnd, 0)
        return hwnd_title

    def get_the_window(self):
        win_title = self.get_all_window_handles()
        the_window_title = ""
        for id_, title in win_title.items():
            if self.player_name in title:
                the_window_title = title
                break
        if the_window_title != "":
            exactWindow = win32gui.FindWindow(0, the_window_title)
            return exactWindow
        else:
            print(f"窗口找不到，请确认游戏角色名称是否填写正确:{self.player_name}")
            self.rec_all_player(win_title)
            exit()

    def rec_all_player(self, dic={}):
        print("目前已经登录的角色有:")
        for id_, title in dic.items():
            if "梦 想 世 界 3" in title:
                print(f"{title.split('-')[-1].strip()}\n")

    def makeTheWindowTop(self,):
        """传入游戏角色名，将整个窗口置顶"""

        win_title = self.get_all_window_handles()
        the_window_title = ""
        for id_, title in win_title.items():
            if self.player_name in title:
                the_window_title = title
                break
        if the_window_title != "":
            exactWindow = win32gui.FindWindow(0, the_window_title)
            win32gui.SetForegroundWindow(exactWindow)

        else:
            print(f"窗口找不到，请确认游戏角色名称是否填写正确:{self.player_name}")
            self.rec_all_player(win_title)
            exit()


if __name__ == "__main__":
    test = MxWindow("°别让我走．ι")
    test.makeTheWindowTop()
