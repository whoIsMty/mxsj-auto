import pyautogui
from pytesseract import pytesseract

from base.action.WindowAction import WindowAction
from base.action.Action import Action

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class ImageAction(Action):

    @staticmethod
    def findImage(player_name, image_path, confidence=0.8):
        """
        在指定的屏幕区域内查找图像。
        :param player_name:  窗口
        :param image_path: 需要查找的图像文件路径。
        :param confidence: 图像识别的置信度（0 到 1），默认 0.8。
        :return: 如果找到，返回图像在整个屏幕上的位置，否则返回 None。
        """
        # 截取指定区域的屏幕图像
        if (type(player_name) != str):
            raise print(player_name)
        region = WindowAction.get_window_region(player_name)
        region_screenshot = pyautogui.screenshot(region=region)
        try:
            location = pyautogui.locate(image_path, region_screenshot, confidence=confidence)
            if location is not None:
                # 将相对于区域的坐标转换为相对于屏幕的坐标
                screen_x = location.left + region[0]
                screen_y = location.top + region[1]
                screen_location = (screen_x, screen_y, location.width, location.height)
                return (int(i) for i in screen_location)
            else:
                print("Image not found in the specified region.")
                return None
        except Exception as e:
            return None

    @staticmethod
    def findImageInRegion(player,region, image_path, confidence=0.8):

        """
        在指定的屏幕区域内查找图像。

        :param player_name:  窗口
        :param image_path: 需要查找的图像文件路径。
        :param confidence: 图像识别的置信度（0 到 1），默认 0.8。
        :return: 如果找到，返回图像在整个屏幕上的位置，否则返回 None。
        """
        # 截取指定区域的屏幕图像
        WindowAction.bring_window_to_front(player)
        region_screenshot = pyautogui.screenshot(region=region)
        try:
            location = pyautogui.locate(image_path, region_screenshot, confidence=confidence)
            if location is not None:
                # 将相对于区域的坐标转换为相对于屏幕的坐标
                screen_x = location.left + region[0]
                screen_y = location.top + region[1]
                screen_location = (screen_x, screen_y, location.width, location.height)
                print(f"Found image at: {screen_location}")
                return (int(i) for i in screen_location)
            else:
                print("Image not found in the specified region.")
                return None
        except Exception as e:
            return None

    @staticmethod
    def isTextInRegion(region, target_text, language='chi_sim'):
        """
        在指定区域查找特定文本。

        :param region: 区域坐标，格式为 (left, top, width, height)
        :param target_text: 要查找的目标文字
        :param language: OCR使用的语言（默认是中文）
        :return: 如果找到目标文字返回True，否则返回False
        """
        # 截取指定区域的屏幕图像
        screenshot = pyautogui.screenshot(region=region)

        # 识别图像中的文本
        recognized_text = pytesseract.image_to_string(screenshot, lang=language)
        # 检查目标文字是否在识别出的文本中
        return target_text in recognized_text

    @staticmethod
    def findTextInRegin(region, target_text, language='chi_sim'):
        pass

    @staticmethod
    def isImageExists(player_name, image_path, confidence=0.8):
        location = ImageAction.findImage(player_name, image_path, confidence)
        if not location:
            return False
        else:
            return True
