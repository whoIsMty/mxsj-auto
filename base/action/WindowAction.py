import win32con
import win32gui

from decoractor.Singleton import Singleton


class WindowAction(metaclass=Singleton):
    @staticmethod
    def find_window_by_title(title_substring):
        """
        查找包含指定标题字符串的窗口句柄。
        :param title_substring: 窗口标题中要搜索的子字符串。
        :return: 包含该子字符串的第一个窗口的句柄，如果没有找到则返回None。
        """

        def callback(hwnd, substring):
            try:
                if win32gui.IsWindowVisible(hwnd) and substring in win32gui.GetWindowText(hwnd):
                    if 'data' not in callback.__dict__:
                        callback.data = hwnd
            except Exception as e:
                print(hwnd, substring,e )

        win32gui.EnumWindows(callback, title_substring)
        return getattr(callback, 'data', None)

    @staticmethod
    def get_window_region(window_title):
        """
        获取指定窗口的区域信息。

        :param window_title: 窗口标题的子字符串。
        :return: 窗口的区域信息 (left, top, width, height) 或 None。
        """
        # 获取所有包含指定标题的窗口
        hwnd = WindowAction.find_window_by_title(window_title)
        # 获取窗口位置和大小
        if hwnd:
            rect = win32gui.GetWindowRect(hwnd)
            # rect 是一个包含 (left, top, right, bottom) 的元组
            left, top, right, bottom = rect

            # 计算窗口的宽度和高度
            width = right - left
            height = bottom - top

            # 返回窗口的区域信息
            return left, top, width, height
        else:
            # 如果没有找到窗口，返回 None
            print(f"No window found with title containing '{window_title}'.")
            return None

    @staticmethod
    def bring_window_to_front(title_substring):
        """
        将包含指定标题字符串的窗口置顶，并返回窗口的尺寸。
        :param title_substring: 窗口标题中要搜索的子字符串。
        :return: 如果成功置顶窗口，返回窗口的长宽 (width, height)，否则返回None。
        """
        hwnd = WindowAction.find_window_by_title(title_substring)
        if hwnd and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
            win32gui.SetForegroundWindow(hwnd)

            # 获取窗口位置和大小
            rect = win32gui.GetWindowRect(hwnd)
            width = rect[2] - rect[0]
            height = rect[3] - rect[1]

            return (width, height)

        return None

    @staticmethod
    def move_window_to_top_left(title_substring, offsetX=0, offsetY=0):
        """
        将包含指定标题字符串的窗口移动到屏幕的左上角。
        :param title_substring: 窗口标题中要搜索的子字符串。
        :return: 如果成功移动窗口返回True，否则返回False。
        """
        hwnd = WindowAction.find_window_by_title(title_substring)
        if hwnd:
            # Move the window to the top-left corner of the screen (0, 0)
            win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0 + offsetX, 0 + offsetY, 0, 0,
                                  win32con.SWP_NOSIZE | win32con.SWP_NOZORDER)
            return True
        return False


# 示例用法
if __name__ == "__main__":
    result = WindowAction.bring_window_to_front("别让我走")
