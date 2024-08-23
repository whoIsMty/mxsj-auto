import os.path
from utils.PinYinUtils import PinYinUtils

class PathUtils:
    projectPath = r"C:\Users\Leo\PycharmProjects\mxsj-auto"

    @staticmethod
    def getButtonPath(name):
        return os.path.join(PathUtils.projectPath, "assets", "button", *name)

    @staticmethod
    def getFormPath(name):
        return os.path.join(PathUtils.projectPath, "assets", "form", *name)

    @staticmethod
    def getNPCPath(name):
        return os.path.join(PathUtils.projectPath, "assets", "npc",PinYinUtils.chinese_to_pinyin(name) +".png")


if __name__ == '__main__':
    print(PathUtils.getButtonPath("lookupRoute.jpg"))
