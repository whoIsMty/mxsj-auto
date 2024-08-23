from base.action.ImageAction import ImageAction
from base.action.KeyboardAction import KeyboardAction
from utils.PathUtils import PathUtils


def HidePlayer(func):
    def wrapper(*args, **kwargs):
        # 1.首先隐藏所有人。在有player参数的方法上加这类装饰器。
        player_name = args[0]
        ok = ImageAction.isImageExists(player_name, PathUtils.getButtonPath("f9.png"))
        if not ok:
            KeyboardAction.keyPress("f9")
        func(*args, **kwargs)
    return wrapper
