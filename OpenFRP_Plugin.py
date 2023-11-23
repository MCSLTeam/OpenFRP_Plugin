from Adapters.Plugin import Plugin
from MCSL2Lib.windowInterface import Window
from PyQt5.QtCore import Qt

from .Interfaces.frpcConsole import OpenFrpFrpcConsoleUI
from .Interfaces.ofPluginSettings import OpenFrpSettingsUI
from .Interfaces.OfInterface import OpenFrpMainUI
from .FrpcController.OfFrpcUpdater import OfFrpcUpdater
from qfluentwidgets import (
    FluentIcon as FIF,
    InfoBar,
    InfoBarPosition,
    NavigationItemPosition,
)

OpenFRP_Plugin = Plugin()

ofInterface = OpenFrpMainUI()
ofFrpcInterface = OpenFrpFrpcConsoleUI()
ofSettingInterface = OpenFrpSettingsUI()
ofFrpcUpdater = OfFrpcUpdater(ofInterface)


def load():
    ofFrpcUpdater.setUpFrpcEnv()
    ofFrpcUpdater.updateInfo.connect(ofInterface.downloadFrpc)


def enable():
    try:
        Window().addSubInterface(
            ofInterface, FIF.WIFI, "OpenFrp", position=NavigationItemPosition.SCROLL
        )
        Window().addSubInterface(
            ofFrpcInterface,
            FIF.COMMAND_PROMPT,
            "Frpc终端",
            position=NavigationItemPosition.SCROLL,
            parent=ofInterface,
        )
        Window().addSubInterface(
            ofSettingInterface,
            FIF.SETTING,
            "插件设置",
            position=NavigationItemPosition.SCROLL,
            parent=ofInterface,
        )
        Window().stackedWidget.currentChanged.connect(decideCheckFrpc)
        InfoBar.success(
            title="提示",
            content="OpenFrp 插件已启用。",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_LEFT,
            duration=2500,
            parent=Window().pluginsInterface,
        )
        ofSettingInterface.initSettings()
        ofSettingInterface.conn()
    except Exception as e:
        InfoBar.error(
            title="提示",
            content=f"OpenFrp 插件启用失败！\n{e}",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_LEFT,
            duration=2500,
            parent=Window().pluginsInterface,
        )


def disable():
    try:
        Window().navigationInterface.removeWidget(routeKey=ofInterface.objectName())
        Window().navigationInterface.removeWidget(routeKey=ofFrpcInterface.objectName())
        Window().navigationInterface.removeWidget(
            routeKey=ofSettingInterface.objectName()
        )
        ofSettingInterface.disconn()
        ofInterface.setParent(None)
        InfoBar.success(
            title="提示",
            content="OpenFrp 插件已禁用。",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_LEFT,
            duration=2500,
            parent=Window().pluginsInterface,
        )
        ofFrpcUpdater.updateInfo.disconnect()
        ofFrpcUpdater.setParent(None)
    except Exception as e:
        InfoBar.error(
            title="提示",
            content=f"OpenFrp 插件禁用失败！\n{e}",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_LEFT,
            duration=2500,
            parent=Window().pluginsInterface,
        )

def decideCheckFrpc():
    global frpcChecked
    if frpcChecked:
        Window().stackedWidget.currentChanged.disconnect(decideCheckFrpc)
        return
    if Window().stackedWidget.currentWidget() == ofInterface:
        frpcChecked = 1
        ofFrpcUpdater.start()

frpcChecked = 0

# 注册加载代码
OpenFRP_Plugin.register_loadFunc(load)

# 注册应用代码
OpenFRP_Plugin.register_enableFunc(enable)

# 注册应用代码
OpenFRP_Plugin.register_disableFunc(disable)
