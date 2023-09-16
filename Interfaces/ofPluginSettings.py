from PyQt5.QtCore import QSize, Qt, QRect
from PyQt5.QtWidgets import (
    QWidget,
    QGridLayout,
    QSizePolicy,
    QFrame,
    QVBoxLayout,
    QSpacerItem,
    QHBoxLayout,
)

from qfluentwidgets import (
    BodyLabel,
    CardWidget,
    PrimaryPushButton,
    SmoothScrollArea,
    StrongBodyLabel,
    SubtitleLabel,
    SwitchButton,
    TitleLabel,
    FluentIcon as FIF,
)

from MCSL2Lib.variables import GlobalMCSL2Variables
from ..variables import OFVariables
from ..OpenFrpLib import __version__ as OFLibVersion
from ..OfSettingsController import OfSettingsController

ofSettingsController = OfSettingsController()


class OpenFrpSettingsUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("OpenFrpSettingsUI")

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        spacerItem = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 4, 1, 1, 3)
        spacerItem1 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        spacerItem2 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 2, 1)
        self.titleLabel = TitleLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        self.titleLabel.setMinimumSize(QSize(345, 50))
        self.titleLabel.setMaximumSize(QSize(345, 50))
        self.titleLabel.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.titleLabel.setObjectName("titleLabel")

        self.gridLayout.addWidget(self.titleLabel, 1, 1, 1, 2)
        self.ofSettingsSmoothScrollArea = SmoothScrollArea(self)
        self.ofSettingsSmoothScrollArea.setFrameShape(QFrame.NoFrame)
        self.ofSettingsSmoothScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.ofSettingsSmoothScrollArea.setWidgetResizable(True)
        self.ofSettingsSmoothScrollArea.setAlignment(Qt.AlignCenter)
        self.ofSettingsSmoothScrollArea.setObjectName("ofSettingsSmoothScrollArea")

        self.ofSettingsScrollAreaWidgetContents = QWidget()
        self.ofSettingsScrollAreaWidgetContents.setGeometry(QRect(0, -16, 649, 475))
        self.ofSettingsScrollAreaWidgetContents.setObjectName(
            "ofSettingsScrollAreaWidgetContents"
        )

        self.verticalLayout = QVBoxLayout(self.ofSettingsScrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.ofLibSettingsTitle = SubtitleLabel(self.ofSettingsScrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ofLibSettingsTitle.sizePolicy().hasHeightForWidth()
        )
        self.ofLibSettingsTitle.setSizePolicy(sizePolicy)
        self.ofLibSettingsTitle.setObjectName("ofLibSettingsTitle")

        self.verticalLayout.addWidget(self.ofLibSettingsTitle)
        self.moduleSettingsWidget = CardWidget(self.ofSettingsScrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.moduleSettingsWidget.sizePolicy().hasHeightForWidth()
        )
        self.moduleSettingsWidget.setSizePolicy(sizePolicy)
        self.moduleSettingsWidget.setMinimumSize(QSize(0, 110))
        self.moduleSettingsWidget.setObjectName("moduleSettingsWidget")

        self.gridLayout_2 = QGridLayout(self.moduleSettingsWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.bypassSystemProxy = QWidget(self.moduleSettingsWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bypassSystemProxy.sizePolicy().hasHeightForWidth()
        )
        self.bypassSystemProxy.setSizePolicy(sizePolicy)
        self.bypassSystemProxy.setMinimumSize(QSize(0, 50))
        self.bypassSystemProxy.setObjectName("bypassSystemProxy")

        self.horizontalLayout_2 = QHBoxLayout(self.bypassSystemProxy)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.bypassSystemProxyTitle = StrongBodyLabel(self.bypassSystemProxy)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bypassSystemProxyTitle.sizePolicy().hasHeightForWidth()
        )
        self.bypassSystemProxyTitle.setSizePolicy(sizePolicy)
        self.bypassSystemProxyTitle.setObjectName("bypassSystemProxyTitle")

        self.horizontalLayout_2.addWidget(self.bypassSystemProxyTitle)
        spacerItem3 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.bypassSystemProxyTip = BodyLabel(self.bypassSystemProxy)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.bypassSystemProxyTip.sizePolicy().hasHeightForWidth()
        )
        self.bypassSystemProxyTip.setSizePolicy(sizePolicy)
        self.bypassSystemProxyTip.setObjectName("bypassSystemProxyTip")

        self.horizontalLayout_2.addWidget(self.bypassSystemProxyTip)
        spacerItem4 = QSpacerItem(42, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.bypassSystemProxySwitchBtn = SwitchButton(self.bypassSystemProxy)
        self.bypassSystemProxySwitchBtn.setObjectName("bypassSystemProxySwitchBtn")

        self.horizontalLayout_2.addWidget(self.bypassSystemProxySwitchBtn)
        self.gridLayout_2.addWidget(self.bypassSystemProxy, 0, 0, 1, 1)
        self.ofLibVerWidget = QWidget(self.moduleSettingsWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ofLibVerWidget.sizePolicy().hasHeightForWidth()
        )
        self.ofLibVerWidget.setSizePolicy(sizePolicy)
        self.ofLibVerWidget.setObjectName("ofLibVerWidget")

        self.horizontalLayout_3 = QHBoxLayout(self.ofLibVerWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.ofLibVerTitle = StrongBodyLabel(self.ofLibVerWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ofLibVerTitle.sizePolicy().hasHeightForWidth()
        )
        self.ofLibVerTitle.setSizePolicy(sizePolicy)
        self.ofLibVerTitle.setObjectName("ofLibVerTitle")

        self.horizontalLayout_3.addWidget(self.ofLibVerTitle)
        self.ofLibVer = BodyLabel(self.ofLibVerWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ofLibVer.sizePolicy().hasHeightForWidth())
        self.ofLibVer.setSizePolicy(sizePolicy)
        self.ofLibVer.setObjectName("ofLibVer")

        self.horizontalLayout_3.addWidget(self.ofLibVer)
        spacerItem5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.gridLayout_2.addWidget(self.ofLibVerWidget, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.moduleSettingsWidget)
        spacerItem6 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem6)
        self.ofFrpcSettingsTitle = SubtitleLabel(
            self.ofSettingsScrollAreaWidgetContents
        )
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ofFrpcSettingsTitle.sizePolicy().hasHeightForWidth()
        )
        self.ofFrpcSettingsTitle.setSizePolicy(sizePolicy)
        self.ofFrpcSettingsTitle.setObjectName("ofFrpcSettingsTitle")

        self.verticalLayout.addWidget(self.ofFrpcSettingsTitle)
        self.ofFrpcSettingsWidget = CardWidget(self.ofSettingsScrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ofFrpcSettingsWidget.sizePolicy().hasHeightForWidth()
        )
        self.ofFrpcSettingsWidget.setSizePolicy(sizePolicy)
        self.ofFrpcSettingsWidget.setMinimumSize(QSize(0, 135))
        self.ofFrpcSettingsWidget.setObjectName("ofFrpcSettingsWidget")

        self.verticalLayout_2 = QVBoxLayout(self.ofFrpcSettingsWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.forceTLS = QWidget(self.ofFrpcSettingsWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.forceTLS.sizePolicy().hasHeightForWidth())
        self.forceTLS.setSizePolicy(sizePolicy)
        self.forceTLS.setMinimumSize(QSize(0, 50))
        self.forceTLS.setObjectName("forceTLS")

        self.horizontalLayout_4 = QHBoxLayout(self.forceTLS)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.forceTLSTitle = StrongBodyLabel(self.forceTLS)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.forceTLSTitle.sizePolicy().hasHeightForWidth()
        )
        self.forceTLSTitle.setSizePolicy(sizePolicy)
        self.forceTLSTitle.setObjectName("forceTLSTitle")

        self.horizontalLayout_4.addWidget(self.forceTLSTitle)
        spacerItem7 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.forceTLSTip = BodyLabel(self.forceTLS)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.forceTLSTip.sizePolicy().hasHeightForWidth())
        self.forceTLSTip.setSizePolicy(sizePolicy)
        self.forceTLSTip.setObjectName("forceTLSTip")

        self.horizontalLayout_4.addWidget(self.forceTLSTip)
        spacerItem8 = QSpacerItem(42, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem8)
        self.forceTLSSwitchBtn = SwitchButton(self.forceTLS)
        self.forceTLSSwitchBtn.setObjectName("forceTLSSwitchBtn")

        self.horizontalLayout_4.addWidget(self.forceTLSSwitchBtn)
        self.verticalLayout_2.addWidget(self.forceTLS)
        self.frpcDebugMode = QWidget(self.ofFrpcSettingsWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frpcDebugMode.sizePolicy().hasHeightForWidth()
        )
        self.frpcDebugMode.setSizePolicy(sizePolicy)
        self.frpcDebugMode.setMinimumSize(QSize(0, 50))
        self.frpcDebugMode.setObjectName("frpcDebugMode")

        self.horizontalLayout_5 = QHBoxLayout(self.frpcDebugMode)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.frpcDebugModeTitle = StrongBodyLabel(self.frpcDebugMode)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frpcDebugModeTitle.sizePolicy().hasHeightForWidth()
        )
        self.frpcDebugModeTitle.setSizePolicy(sizePolicy)
        self.frpcDebugModeTitle.setObjectName("frpcDebugModeTitle")

        self.horizontalLayout_5.addWidget(self.frpcDebugModeTitle)
        spacerItem9 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.frpcDebugModeTip = BodyLabel(self.frpcDebugMode)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frpcDebugModeTip.sizePolicy().hasHeightForWidth()
        )
        self.frpcDebugModeTip.setSizePolicy(sizePolicy)
        self.frpcDebugModeTip.setObjectName("frpcDebugModeTip")

        self.horizontalLayout_5.addWidget(self.frpcDebugModeTip)
        spacerItem10 = QSpacerItem(42, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.frpcDebugModeSwitchBtn = SwitchButton(self.frpcDebugMode)
        self.frpcDebugModeSwitchBtn.setObjectName("frpcDebugModeSwitchBtn")

        self.horizontalLayout_5.addWidget(self.frpcDebugModeSwitchBtn)
        self.verticalLayout_2.addWidget(self.frpcDebugMode)
        self.verticalLayout.addWidget(self.ofFrpcSettingsWidget)
        spacerItem11 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem11)
        self.SubtitleLabel = SubtitleLabel(self.ofSettingsScrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.SubtitleLabel.sizePolicy().hasHeightForWidth()
        )
        self.SubtitleLabel.setSizePolicy(sizePolicy)
        self.SubtitleLabel.setObjectName("SubtitleLabel")

        self.verticalLayout.addWidget(self.SubtitleLabel)
        self.checkUpdate = CardWidget(self.ofSettingsScrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkUpdate.sizePolicy().hasHeightForWidth())
        self.checkUpdate.setSizePolicy(sizePolicy)
        self.checkUpdate.setMinimumSize(QSize(0, 70))
        self.checkUpdate.setObjectName("checkUpdate")

        self.horizontalLayout = QHBoxLayout(self.checkUpdate)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.checkUpdateWidget = QWidget(self.checkUpdate)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.checkUpdateWidget.sizePolicy().hasHeightForWidth()
        )
        self.checkUpdateWidget.setSizePolicy(sizePolicy)
        self.checkUpdateWidget.setMinimumSize(QSize(0, 50))
        self.checkUpdateWidget.setObjectName("checkUpdateWidget")

        self.horizontalLayout_6 = QHBoxLayout(self.checkUpdateWidget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        self.pluginVerTitle = StrongBodyLabel(self.checkUpdateWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pluginVerTitle.sizePolicy().hasHeightForWidth()
        )
        self.pluginVerTitle.setSizePolicy(sizePolicy)
        self.pluginVerTitle.setObjectName("pluginVerTitle")

        self.horizontalLayout_6.addWidget(self.pluginVerTitle)
        self.pluginVer = BodyLabel(self.checkUpdateWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pluginVer.sizePolicy().hasHeightForWidth())
        self.pluginVer.setSizePolicy(sizePolicy)
        self.pluginVer.setObjectName("pluginVer")

        self.horizontalLayout_6.addWidget(self.pluginVer)
        spacerItem12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12)
        self.pluginCheckUpdateBtn = PrimaryPushButton(self.checkUpdateWidget)
        self.pluginCheckUpdateBtn.setIcon(FIF.UPDATE)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pluginCheckUpdateBtn.sizePolicy().hasHeightForWidth()
        )
        self.pluginCheckUpdateBtn.setSizePolicy(sizePolicy)
        self.pluginCheckUpdateBtn.setMinimumSize(QSize(0, 31))
        self.pluginCheckUpdateBtn.setObjectName("pluginCheckUpdateBtn")

        self.horizontalLayout_6.addWidget(self.pluginCheckUpdateBtn)
        self.horizontalLayout.addWidget(self.checkUpdateWidget)
        self.verticalLayout.addWidget(self.checkUpdate)
        spacerItem13 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem13)
        self.ofSettingsSmoothScrollArea.setWidget(
            self.ofSettingsScrollAreaWidgetContents
        )
        self.gridLayout.addWidget(self.ofSettingsSmoothScrollArea, 3, 1, 1, 3)

        self.titleLabel.setText("MCSL2 - OpenFrp 插件设置")
        self.ofLibSettingsTitle.setText("调用库 - OpenFrpLib 设置")

        self.bypassSystemProxyTitle.setText("绕过系统代理")
        self.bypassSystemProxyTip.setText("可防止在系统开启代理时本插件无法连接 OpenFrp API的问题。")

        self.bypassSystemProxySwitchBtn.setText("关")
        self.bypassSystemProxySwitchBtn.setOnText("开")
        self.bypassSystemProxySwitchBtn.setOffText("关")
        self.ofLibVerTitle.setText("OpenFrpLib 库当前版本：")
        self.ofLibVer.setText(OFLibVersion)
        self.ofFrpcSettingsTitle.setText("OpenFrp Frpc 设置")

        self.forceTLSTitle.setText("强制TLS流量传输")
        self.forceTLSTip.setText("启用后，Frpc所发送的数据都将经过TLS加密。")

        self.forceTLSSwitchBtn.setText("关")
        self.forceTLSSwitchBtn.setOnText("开")
        self.forceTLSSwitchBtn.setOffText("关")
        self.frpcDebugModeTitle.setText("调试模式")
        self.frpcDebugModeTip.setText("启用后，Frpc将输出调试信息。")

        self.frpcDebugModeSwitchBtn.setText("关")
        self.frpcDebugModeSwitchBtn.setOnText("开")
        self.frpcDebugModeSwitchBtn.setOffText("关")
        self.SubtitleLabel.setText("检查更新")
        self.pluginVerTitle.setText("插件当前版本：")
        self.pluginVer.setText(OFVariables.ofPluginVersion)
        self.pluginCheckUpdateBtn.setText("检查更新")
        self.ofSettingsSmoothScrollArea.viewport().setStyleSheet(
            GlobalMCSL2Variables.scrollAreaViewportQss
        )

        self.bypassSystemProxySwitchBtn.checkedChanged.connect(
            lambda: ofSettingsController.changeSettings(
                {
                    "bypass_system_proxy": self.bypassSystemProxySwitchBtn.isChecked(),
                }
            )
        )
        self.forceTLSSwitchBtn.checkedChanged.connect(
            lambda: ofSettingsController.changeSettings(
                {
                    "fprc_force_tls": self.forceTLSSwitchBtn.isChecked(),
                }
            )
        )
        self.frpcDebugModeSwitchBtn.checkedChanged.connect(
            lambda: ofSettingsController.changeSettings(
                {
                    "frpc_debug_mode": self.frpcDebugModeSwitchBtn.isChecked(),
                }
            )
        )

    def initSettings(self):
        self.bypassSystemProxySwitchBtn.setChecked(
            ofSettingsController.fileSettings["bypass_system_proxy"]
        )
        self.forceTLSSwitchBtn.setChecked(
            ofSettingsController.fileSettings["fprc_force_tls"]
        )
        self.frpcDebugModeSwitchBtn.setChecked(
            ofSettingsController.fileSettings["frpc_debug_mode"]
        )