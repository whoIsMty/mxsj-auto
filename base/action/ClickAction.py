import os.path

import cv2
import numpy as np
import pyautogui
from PIL import ImageEnhance, ImageFilter
from pytesseract import pytesseract

from base.action.ImageAction import ImageAction
from decoractor.Sleep import Sleep
from utils.ImageUtils import ImageUtils
from utils.PathUtils import PathUtils

pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Windows 示例

class ClickAction:

    @Sleep
    @staticmethod
    def clickImage(player_name, image_path, times=1,down =0,left=0):
        screen_location = ImageAction.findImage(player_name, image_path)
        if screen_location:
            print(rf"found screen {image_path}")
            ClickAction.clickCenter(*screen_location, times=times,down=down,left=left)

    @Sleep
    @staticmethod
    def clickCenter(x, y, height, width, down=0, left=0, times=0):
        # 传入位置
        centerX, centerY = pyautogui.center((x - left, y + down, height, width))
        pyautogui.moveTo(centerX, centerY, duration=0.2)  # 移动时增加一点时间以更准确
        print(f"has moved to {centerX}, {centerY}")
        if times == 2:
            print(rf"double clicking {centerX}, {centerY}")
            pyautogui.doubleClick()
        else:
            for i in range(times):
                pyautogui.click()

    @Sleep
    @staticmethod
    def clickTextInRegion(player, region, target_text, times=1):

        """
        在指定区域内以滑动窗口的方式查找目标文本，如果找到则点击文本的中心位置。
        :param region: 区域坐标，格式为 (left, top, width, height)
        :param target_text: 要查找的目标文字
        :param language: OCR使用的语言（默认是中文）
        :param step: 滑动窗口的步长
        :param confidence_threshold: 识别置信度阈值，默认是80
        :return: 如果找到目标文字并点击，返回 True，否则返回 False
        """
        npcPath = PathUtils.getNPCPath(target_text)
        if os.path.exists(npcPath):
            # 如果NPC的图像已经存在
            textRegion = ImageAction.findImageInRegion(player, region, npcPath, confidence=0.9)
            if textRegion:
                print("find image in region :", region, npcPath)
                ClickAction.clickCenter(*textRegion,times=times)
            else :
                print(f"没找到{target_text}")
        else:
            raise Exception(f"{target_text}截图不存在")





