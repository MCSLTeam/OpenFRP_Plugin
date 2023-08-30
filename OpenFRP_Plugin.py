from Adapters.Plugin import Plugin
from MCSL2Lib.windowInterface import Window
from PyQt5.QtCore import Qt
from .Interfaces.frpcConsole import OpenFrpFrpcConsoleUI
from .Interfaces.ofPluginSettings import OpenFrpSettingsUI
from .Interfaces.OfInterface import OpenFrpMainUI
from .OFSettingsController import initOFPluginConfiguration
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


def load():
    initOFPluginConfiguration()


def enable():
    try:
        Window().addSubInterface(ofInterface, FIF.WIFI, "OpenFrp")
        Window().addSubInterface(ofFrpcInterface, FIF.COMMAND_PROMPT, "OF终端")
        Window().addSubInterface(
            ofSettingInterface,
            FIF.SETTING,
            "OF设置",
            position=NavigationItemPosition.BOTTOM,
        )
        InfoBar.success(
            title="提示",
            content="OpenFrp 插件已启用。",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_LEFT,
            duration=2500,
            parent=Window().pluginsInterface,
        )
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


# 注册加载代码
OpenFRP_Plugin.register_loadFunc(load)

# 注册应用代码
OpenFRP_Plugin.register_enableFunc(enable)

# 注册应用代码
OpenFRP_Plugin.register_disableFunc(disable)
