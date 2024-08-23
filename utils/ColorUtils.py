from PIL import Image, ImageDraw, ImageFont
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


def get_dominant_color(image_path, k=4, resize=True, resize_factor=0.5):
    """
    获取图像的主要颜色。

    :param image_path: 图像文件路径
    :param k: 聚类的簇数（默认是4）
    :param resize: 是否缩放图像以加快处理速度
    :param resize_factor: 缩放因子（0到1之间），越小速度越快
    :return: 主要颜色的RGB值
    """
    # 打开图像文件
    img = Image.open(image_path)

    # 缩放图像
    if resize:
        img = img.resize(
            (int(img.width * resize_factor), int(img.height * resize_factor)),
            Image.LANCZOS  # 使用 LANCZOS 滤波器进行高质量缩放
        )

    # 转换图像为numpy数组
    img_np = np.array(img)

    # 将图像转换为二维数组，每行一个像素的 RGB 值
    img_np = img_np.reshape((-1, 3))

    # 使用KMeans聚类
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(img_np)

    # 找到最大的簇并返回其中心颜色
    dominant_color = kmeans.cluster_centers_[np.argmax(np.bincount(kmeans.labels_))]

    # 转换为整数
    dominant_color = dominant_color.astype(int)

    return tuple(dominant_color)


def visualize_dominant_color(image_path, dominant_color):
    """
    可视化主要颜色。

    :param image_path: 图像文件路径
    :param dominant_color: 主要颜色的RGB值
    """
    # 创建一个新的图像显示主要颜色
    color_block = np.ones((100, 100, 3), dtype=np.uint8) * np.array(dominant_color, dtype=np.uint8)

    # 显示原始图像
    original_img = Image.open(image_path)

    # 使用 matplotlib 显示原始图像和主要颜色块
    plt.figure(figsize=(8, 4))

    plt.subplot(1, 2, 1)
    plt.imshow(original_img)
    plt.axis('off')
    plt.title('Original Image')

    plt.subplot(1, 2, 2)
    plt.imshow(color_block)
    plt.axis('off')
    plt.title('Dominant Color')

    plt.show()


# 示例用法
image_path = "../img.png"  # 替换为你的图像路径
dominant_color = get_dominant_color(image_path)

print(f"主要颜色: {dominant_color}")

# 可视化主要颜色
visualize_dominant_color(image_path, dominant_color)
