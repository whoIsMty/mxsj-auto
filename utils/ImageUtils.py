from PIL import Image, ImageDraw, ImageFont, ImageFilter
from io import BytesIO
import numpy as np
import pyautogui
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

from utils.PathUtils import PathUtils
from utils.PinYinUtils import PinYinUtils


class ImageUtils:


    @staticmethod
    def createTextImage(text, font_path="msyh.ttc", font_size=20, ):
        output_path = PathUtils.getNPCPath(text)
        # 加载字体
        font = ImageFont.truetype(font_path, font_size)
        # 创建一个空白图像
        img = Image.new('RGB', (font_size * len(text), font_size), color=(32, 76, 112))

        # 创建绘图对象
        draw = ImageDraw.Draw(img)

        # 绘制文本
        text_x = (img.width - font_size * len(text)) // 2
        text_y = (img.height - font_size) // 2 -5
        draw.text((text_x, text_y), text, font=font, fill=(255, 255, 255))

        # # 应用模糊效果
        # blurred_img = img.filter(ImageFilter.GaussianBlur(radius=0.00000001))

        # 保存图像
        img.save(output_path)
        print(f"Image saved to {output_path}")

    # 使用示例


if __name__ == '__main__':

    # 获取所有系统字体
    ImageUtils.createTextImage(f"了然和尚" )
