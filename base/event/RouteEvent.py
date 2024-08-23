import time
from abc import ABC

from base.action.ClickAction import ClickAction
from base.action.ImageAction import ImageAction
from base.action.KeyboardAction import KeyboardAction
from base.action.WindowAction import WindowAction
from decoractor.HidePlayer import HidePlayer
from decoractor.ScreenStable import ScreenStable
from utils.PathUtils import PathUtils


class RouteEvent(ABC):
    LOOKUP_ROUTE = ["map", "chazhaoluxian.png"]
    LOOKUP_ROUTE2 = ["map", "zidongxunlu.png"]
    LOOKUP_ROUTE3 = ["map", "chazhaoxitongjuese.png"]
    LOOKUP_ROUTE4 = ["map", "sousuoxitongjuese.png"]

    LOCAL1 = ["local", "zhouwei.png"]
    LOCAL2 = ["local", "zhouweixitongjueseopen.png"]
    LOCAL3 = ["local", "zhouweixitongjueseclose.png"]
    LOCAL4 = ["local", "zuijinlianxi.png"]

    SOCIAL1 = ["social", "haoyou.png"]

    @staticmethod
    def openMap(player):
        WindowAction.bring_window_to_front(player)
        RouteEvent.clear(player)
        KeyboardAction.keyPress("tab")

    @HidePlayer
    @staticmethod
    def open_map_loop_up(player):
        RouteEvent.openMap(player)
        img = PathUtils.getButtonPath(RouteEvent.LOOKUP_ROUTE)
        ClickAction.clickImage(player, img)
        # 查找路线框打开

    @staticmethod
    @HidePlayer
    def autoGoNPC(playerName, NPC):
        RouteEvent.open_map_loop_up(playerName)
        ClickAction.clickImage(playerName, PathUtils.getButtonPath(RouteEvent.LOOKUP_ROUTE3))
        KeyboardAction.write(NPC)
        ClickAction.clickImage(playerName, PathUtils.getButtonPath(RouteEvent.LOOKUP_ROUTE4), times=2, down=60)

    @staticmethod
    def clear(player):
        KeyboardAction.keyPress("esc")
        ok = ImageAction.isImageExists(player, PathUtils.getButtonPath(["rollback", "zaixianxinxi.png"]))
        if (ok):
            KeyboardAction.keyPress("esc")

    @staticmethod
    def readMessages(player):
        while True:
            # 是否已经打开好友框
            open = ImageAction.isImageExists(player, PathUtils.getButtonPath(RouteEvent.SOCIAL1))
            if open:
                print("消息已经清理。")
                RouteEvent.clear(player)
                return
            else:
                KeyboardAction.hotKey("alt", "f")

    @staticmethod
    def talkToNPC(player, npc, ):
        KeyboardAction.hotKey("alt", "f")  # 打开周围
        RouteEvent.openLocalNPC(player)
        localOpen = ImageAction.findImage(player, PathUtils.getButtonPath(RouteEvent.LOCAL2))
        if localOpen:
            x, y, w, h = localOpen
            w = w + 80
            h = h + 60
            x = x
            y = y
            localNPCRegion = (x, y + 20, w, h)
            ClickAction.clickTextInRegion(player, localNPCRegion, npc,times=2)

    @staticmethod
    def openLocalNPC(playerName):
        RouteEvent.readMessages(playerName)
        # 打开周围
        KeyboardAction.hotKey("alt", "f")  # 打开周围
        ClickAction.clickImage(playerName, PathUtils.getButtonPath(RouteEvent.SOCIAL1), times=2)
        ClickAction.clickImage(playerName, PathUtils.getButtonPath(RouteEvent.LOCAL1), times=2)
        print("周围已经打开")


if __name__ == '__main__':
    nameList =["别让我走","弥留之际"]
    x = 0
    while True:
        for name in nameList:
            result = WindowAction.bring_window_to_front(name)
            RouteEvent.autoGoNPC(name,"清风村传送人")
            KeyboardAction.hotKey("ctrl", "a")
            time.sleep(3)
            RouteEvent.autoGoNPC(name,"钱秀才")

