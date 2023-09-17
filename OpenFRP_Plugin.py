from Adapters.Plugin import Plugin
from MCSL2Lib.windowInterface import Window
from PyQt5.QtCore import Qt
from .Interfaces.frpcConsole import OpenFrpFrpcConsoleUI
from .Interfaces.ofPluginSettings import OpenFrpSettingsUI
from .Interfaces.OfInterface import OpenFrpMainUI
from .OfSettingsController import initOFPluginConfiguration
from qfluentwidgets import (
    FluentIcon as FIF,
    InfoBar,
    InfoBarPosition,
    NavigationItemPosition,
    NavigationTreeWidget,
    NavigationPushButton,
)

OpenFRP_Plugin = Plugin()

ofInterface = OpenFrpMainUI()
ofFrpcInterface = OpenFrpFrpcConsoleUI()
ofSettingInterface = OpenFrpSettingsUI()


def load():
    initOFPluginConfiguration()


def enable():
    try:
        Window().stackedWidget.addWidget(ofInterface)
        Window().stackedWidget.addWidget(ofFrpcInterface)
        Window().stackedWidget.addWidget(ofSettingInterface)
        ofMainNav = NavigationTreeWidget(icon=FIF.WIFI, text="OpenFrp", isSelectable=False)
        # ofMainNav.set

        ofHomeNav = NavigationTreeWidget(icon=FIF.HOME, text="主页", isSelectable=True)
        ofHomeNav.clicked.connect(lambda: Window().switchTo(ofInterface))
        ofMainNav.addChild(ofHomeNav)

        ofFrpcConsoleNav = NavigationTreeWidget(icon=FIF.COMMAND_PROMPT, text="Frpc终端", isSelectable=True)
        ofFrpcConsoleNav.clicked.connect(lambda: Window().switchTo(ofFrpcInterface))
        ofMainNav.addChild(ofFrpcConsoleNav)

        ofSettingsNav = NavigationTreeWidget(icon=FIF.SETTING, text="设置", isSelectable=False)
        ofSettingsNav.clicked.connect(lambda: Window().switchTo(ofSettingInterface))
        ofMainNav.addChild(ofSettingsNav)

        Window().navigationInterface.addWidget(
            routeKey="OpenFrp",
            widget=ofMainNav,
            tooltip="OpenFrp",
            position=NavigationItemPosition.SCROLL,
        )
        # Window().addSubInterface(ofInterface, FIF.WIFI, "OpenFrp主页", position=NavigationItemPosition.SCROLL)
        # Window().addSubInterface(ofFrpcInterface, FIF.COMMAND_PROMPT, "Frpc终端", position=NavigationItemPosition.SCROLL)
        # Window().addSubInterface(
        #     ofSettingInterface,
        #     FIF.SETTING,
        #     "OpenFrp设置",
        #     position=NavigationItemPosition.SCROLL,
        # )
        InfoBar.success(
            title="提示",
            content="OpenFrp 插件已启用。\n如果看不到所有功能，请展开导航栏，\n然后点击“OpenFrp”的“展开”按钮。",
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.BOTTOM_LEFT,
            duration=2500,
            parent=Window().pluginsInterface,
        )
        ofSettingInterface.initSettings()
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
        Window().navigationInterface.removeWidget(routeKey="OpenFrp")
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
