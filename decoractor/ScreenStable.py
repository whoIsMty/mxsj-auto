import cv2
import numpy as np
import pyautogui
import time
from functools import wraps

from base.action.WindowAction import WindowAction


def ScreenStable(player, threshold=0.01, interval=1.5, duration=10):
    """
    装饰器工厂，只有在屏幕指定区域不再变化时才执行被装饰的函数。

    参数:
    player: 窗口名称或标识符
    threshold (float): 图像变化的阈值（默认为0.01）
    interval (int): 检查间隔的秒数（默认为1）
    duration (int): 持续时间的秒数（默认为10）

    返回:
    function: 装饰器
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            WindowAction.bring_window_to_front(player)
            windowRegion = WindowAction.get_window_region(player)
            x, y, w, h = windowRegion
            region = (x + 65, y + 60, 60, 20)  # 坐标框

            # 检查指定区域是否停止变化
            if has_region_stopped_changing(region, threshold, interval, duration):
                print("区域不再变化，执行函数...")
                return func(*args, **kwargs)
            else:
                print("区域仍在变化，函数未执行。")
                return None

        return wrapper

    return decorator


def capture_region(region):
    """
    捕获指定区域的屏幕截图。

    参数:
    region (tuple): (x, y, width, height) 矩形区域

    返回:
    numpy.ndarray: 截图图像
    """
    screenshot = pyautogui.screenshot(region=region)
    return cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)


def has_region_stopped_changing(region, threshold=0.01, interval=1.5, duration=10):
    """
    检查指定区域是否在给定持续时间内不再变化。

    参数:
    region (tuple): (x, y, width, height) 矩形区域
    threshold (float): 图像变化的阈值（默认为0.01）
    interval (float): 检查间隔的秒数（默认为1.5）
    duration (int): 持续时间的秒数（默认为10）

    返回:
    bool: 区域是否停止变化
    """
    start_time = time.time()
    previous_image = capture_region(region)

    # 每隔 interval 秒检查一次变化，直到持续时间 duration 结束
    while time.time() - start_time < duration:
        time.sleep(interval)
        current_image = capture_region(region)

        # 保存当前图像到文件
        # cv2.imwrite(f"current_image_{int(time.time())}.png", current_image)

        # 计算图像差异
        difference = cv2.absdiff(previous_image, current_image)
        non_zero_count = np.count_nonzero(difference)

        # 计算差异比例
        change_ratio = non_zero_count / float(region[2] * region[3])

        # 检查变化是否在阈值之下
        if change_ratio < threshold:
            print(f"变化比例: {change_ratio:.6f}, 在阈值以下，区域稳定。")
            return True  # 区域稳定，返回 True
        else:
            print(f"变化比例: {change_ratio:.6f}, 超过阈值。")
            previous_image = current_image  # 更新前一帧为当前帧
            start_time = time.time()  # 重置计时器

    return False  # 如果持续时间内没有达到稳定条件，返回 False


# 示例函数
def example_function():
    print("函数执行成功！")


# # 使用装饰器工厂来装饰函数
# player_name = "My Game Window"
# decorated_function = ScreenStable(player_name, threshold=0.01, interval=1.5, duration=10)(example_function)
#
# # 调用被装饰的函数
# decorated_function()
