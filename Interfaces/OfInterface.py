from os import remove, rename
from typing import Optional
from zipfile import ZipFile
from PyQt5.QtCore import QSize, Qt, QRect, pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QWidget,
    QGridLayout,
    QSizePolicy,
    QStackedWidget,
    QFrame,
    QVBoxLayout,
    QSpacerItem,
    QHBoxLayout,
    QApplication,
)
from aria2p import Download
from qfluentwidgets import (
    BodyLabel,
    ComboBox,
    HorizontalSeparator,
    LineEdit,
    PixmapLabel,
    PlainTextEdit,
    PrimaryPushButton,
    PushButton,
    SmoothScrollArea,
    StrongBodyLabel,
    SubtitleLabel,
    SwitchButton,
    TitleLabel,
    TransparentPushButton,
    TransparentToolButton,
    FluentIcon as FIF,
    FlowLayout,
    MessageBox,
    InfoBarPosition,
    InfoBar,
)
from MCSL2Lib.Controllers.aria2ClientController import Aria2Controller
from MCSL2Lib.Widgets.loadingTipWidget import LoadFailedTip, LoadingTip
from MCSL2Lib.Widgets.DownloadProgressWidget import DownloadMessageBox
from MCSL2Lib.variables import GlobalMCSL2Variables
from ..FrpcController.OfFrpcBridge import FrpcBridge
from ..variables import clearNewProxyConfig, variablesLogout
from ..OfSettingsController import OfSettingsController
from ..APIThreads import *
from .loginWidget import LoginContainer
from .singleNodeWidget import SingleNodeWidget
from .singleProxyWidget import SingleProxyWidget
from .images import *  # noqa: F401
from .userInfoWidget import UserInfoContainer
from random import randint

ofSettingsController = OfSettingsController()


class UserInfoMessageBox(MessageBox):
    def __init__(self, title: str, content: str, parent=None):
        super().__init__(title, content, parent)
        self.yesSignal.connect(self.killSelf)

    def killSelf(self):
        self.yesSignal.disconnect()
        self.parent().accountInfoBtn.clicked.disconnect()
        self.parent().initUserInfoWidget()
        self.deleteLater()
        self.setParent(None)


class OpenFrpMainUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("OpenFrpMainUI")

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.setObjectName("stackedWidget")

        self.mainPage = QWidget()
        self.mainPage.setObjectName("mainPage")

        self.gridLayout_2 = QGridLayout(self.mainPage)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.userInfoStackedWidget = QStackedWidget(self.mainPage)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.userInfoStackedWidget.sizePolicy().hasHeightForWidth()
        )
        self.userInfoStackedWidget.setSizePolicy(sizePolicy)
        self.userInfoStackedWidget.setObjectName("userInfoStackedWidget")

        self.notLogin = QWidget()
        self.notLogin.setObjectName("notLogin")

        self.horizontalLayout_2 = QHBoxLayout(self.notLogin)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.notLoginTip = StrongBodyLabel(self.notLogin)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notLoginTip.sizePolicy().hasHeightForWidth())
        self.notLoginTip.setSizePolicy(sizePolicy)
        self.notLoginTip.setObjectName("notLoginTip")

        self.horizontalLayout_2.addWidget(self.notLoginTip)
        self.loginEntryBtn = PrimaryPushButton(self.notLogin)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.loginEntryBtn.sizePolicy().hasHeightForWidth()
        )
        self.loginEntryBtn.setSizePolicy(sizePolicy)
        self.loginEntryBtn.setMinimumSize(QSize(65, 32))
        self.loginEntryBtn.setMaximumSize(QSize(65, 32))
        self.loginEntryBtn.setObjectName("loginEntryBtn")

        self.horizontalLayout_2.addWidget(self.loginEntryBtn)
        self.userInfoStackedWidget.addWidget(self.notLogin)
        self.logged = QWidget()
        self.logged.setObjectName("logged")

        self.gridLayout_4 = QGridLayout(self.logged)
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.userInfo = QWidget(self.logged)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userInfo.sizePolicy().hasHeightForWidth())
        self.userInfo.setSizePolicy(sizePolicy)
        self.userInfo.setObjectName("userInfo")

        self.verticalLayout_2 = QVBoxLayout(self.userInfo)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.userName = StrongBodyLabel(self.userInfo)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userName.sizePolicy().hasHeightForWidth())
        self.userName.setSizePolicy(sizePolicy)
        self.userName.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.userName.setObjectName("userName")

        self.verticalLayout_2.addWidget(self.userName)
        self.userEmail = BodyLabel(self.userInfo)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userEmail.sizePolicy().hasHeightForWidth())
        self.userEmail.setSizePolicy(sizePolicy)
        self.userEmail.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.userEmail.setObjectName("userEmail")

        self.verticalLayout_2.addWidget(self.userEmail)
        self.gridLayout_4.addWidget(self.userInfo, 0, 0, 4, 1)
        self.loggedBtnWidget = QWidget(self.logged)
        self.loggedBtnWidget.setObjectName("loggedBtnWidget")

        self.verticalLayout_3 = QVBoxLayout(self.loggedBtnWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.accountInfoBtn = PushButton(self.loggedBtnWidget)
        self.accountInfoBtn.setObjectName("accountInfoBtn")

        self.verticalLayout_3.addWidget(self.accountInfoBtn)
        self.logoutBtn = PushButton(self.loggedBtnWidget)
        self.logoutBtn.setObjectName("logoutBtn")

        self.verticalLayout_3.addWidget(self.logoutBtn)
        self.gridLayout_4.addWidget(self.loggedBtnWidget, 2, 3, 1, 1)
        self.userImage = PixmapLabel(self.logged)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userImage.sizePolicy().hasHeightForWidth())
        self.userImage.setSizePolicy(sizePolicy)
        self.userImage.setMinimumSize(QSize(60, 60))
        self.userImage.setMaximumSize(QSize(60, 60))
        self.userImage.setObjectName("userImage")

        self.gridLayout_4.addWidget(self.userImage, 2, 1, 1, 1)
        self.userInfoStackedWidget.addWidget(self.logged)
        self.gridLayout_2.addWidget(self.userInfoStackedWidget, 0, 5, 2, 1)
        self.ofProxiesSmoothScrollArea = SmoothScrollArea(self.mainPage)
        self.ofProxiesSmoothScrollArea.setFrameShape(QFrame.NoFrame)
        self.ofProxiesSmoothScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.ofProxiesSmoothScrollArea.setWidgetResizable(True)
        self.ofProxiesSmoothScrollArea.setObjectName("ofProxiesSmoothScrollArea")

        self.ofProxiesScrollAreaWidgetContents = QWidget()
        self.ofProxiesScrollAreaWidgetContents.setGeometry(QRect(0, 0, 648, 380))
        self.ofProxiesScrollAreaWidgetContents.setObjectName(
            "ofProxiesScrollAreaWidgetContents"
        )

        self.gridLayout_2.addWidget(self.ofProxiesSmoothScrollArea, 4, 0, 1, 6)
        self.titleLimitWidget = QWidget(self.mainPage)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.titleLimitWidget.sizePolicy().hasHeightForWidth()
        )
        self.titleLimitWidget.setSizePolicy(sizePolicy)
        self.titleLimitWidget.setObjectName("titleLimitWidget")

        self.gridLayout_3 = QGridLayout(self.titleLimitWidget)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.pluginVer = BodyLabel(self.titleLimitWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pluginVer.sizePolicy().hasHeightForWidth())
        self.pluginVer.setSizePolicy(sizePolicy)
        self.pluginVer.setAlignment(Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft)
        self.pluginVer.setObjectName("pluginVer")

        self.gridLayout_3.addWidget(self.pluginVer, 0, 2, 1, 1)
        self.pluginVerTitle = BodyLabel(self.titleLimitWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pluginVerTitle.sizePolicy().hasHeightForWidth()
        )
        self.pluginVerTitle.setSizePolicy(sizePolicy)
        self.pluginVerTitle.setAlignment(
            Qt.AlignBottom | Qt.AlignLeading | Qt.AlignLeft
        )
        self.pluginVerTitle.setObjectName("pluginVerTitle")

        self.gridLayout_3.addWidget(self.pluginVerTitle, 0, 1, 1, 1)
        self.titleLabel = TitleLabel(self.titleLimitWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        self.titleLabel.setObjectName("titleLabel")

        self.gridLayout_3.addWidget(self.titleLabel, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.titleLimitWidget, 0, 0, 1, 3)
        self.newProxyBtn = TransparentPushButton(self.mainPage)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.newProxyBtn.sizePolicy().hasHeightForWidth())
        self.newProxyBtn.setSizePolicy(sizePolicy)
        self.newProxyBtn.setIcon(FIF.ADD_TO)
        self.newProxyBtn.setObjectName("newProxyBtn")

        self.gridLayout_2.addWidget(self.newProxyBtn, 1, 0, 1, 1)
        self.refreshProxyListBtn = TransparentPushButton(self.mainPage)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.refreshProxyListBtn.sizePolicy().hasHeightForWidth()
        )
        self.refreshProxyListBtn.setSizePolicy(sizePolicy)
        self.refreshProxyListBtn.setIcon(FIF.UPDATE)
        self.refreshProxyListBtn.setObjectName("refreshProxyListBtn")

        self.gridLayout_2.addWidget(self.refreshProxyListBtn, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.mainPage)
        self.newProxyPage = QWidget()
        self.newProxyPage.setObjectName("newProxyPage")

        self.gridLayout_5 = QGridLayout(self.newProxyPage)
        self.gridLayout_5.setObjectName("gridLayout_5")

        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 0, 2, 1, 2)
        self.newProxyTitle = TitleLabel(self.newProxyPage)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.newProxyTitle.sizePolicy().hasHeightForWidth()
        )
        self.newProxyTitle.setSizePolicy(sizePolicy)
        self.newProxyTitle.setObjectName("newProxyTitle")

        self.gridLayout_5.addWidget(self.newProxyTitle, 0, 1, 1, 1)
        self.newProxyBackBtn = TransparentToolButton(FIF.PAGE_LEFT, self.newProxyPage)
        self.newProxyBackBtn.setObjectName("newProxyBackBtn")

        self.gridLayout_5.addWidget(self.newProxyBackBtn, 0, 0, 1, 1)
        self.configureProxyScrollArea = SmoothScrollArea(self.newProxyPage)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.configureProxyScrollArea.sizePolicy().hasHeightForWidth()
        )
        self.configureProxyScrollArea.setSizePolicy(sizePolicy)
        self.configureProxyScrollArea.setMinimumSize(QSize(345, 0))
        self.configureProxyScrollArea.setMaximumSize(QSize(345, 16777215))
        self.configureProxyScrollArea.setFrameShape(QFrame.NoFrame)
        self.configureProxyScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.configureProxyScrollArea.setWidgetResizable(True)
        self.configureProxyScrollArea.setAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop
        )
        self.configureProxyScrollArea.setObjectName("configureProxyScrollArea")

        self.configureProxyScrollAreaWidgetContents = QWidget()
        self.configureProxyScrollAreaWidgetContents.setGeometry(QRect(0, 0, 345, 882))
        self.configureProxyScrollAreaWidgetContents.setObjectName(
            "configureProxyScrollAreaWidgetContents"
        )

        self.gridLayout_7 = QGridLayout(self.configureProxyScrollAreaWidgetContents)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")

        self.requestPassTitle = StrongBodyLabel(
            self.configureProxyScrollAreaWidgetContents
        )
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.requestPassTitle.sizePolicy().hasHeightForWidth()
        )
        self.requestPassTitle.setSizePolicy(sizePolicy)
        self.requestPassTitle.setObjectName("requestPassTitle")

        self.gridLayout_7.addWidget(self.requestPassTitle, 22, 0, 1, 1)
        self.proxyProtocolTitle = StrongBodyLabel(
            self.configureProxyScrollAreaWidgetContents
        )
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.proxyProtocolTitle.sizePolicy().hasHeightForWidth()
        )
        self.proxyProtocolTitle.setSizePolicy(sizePolicy)
        self.proxyProtocolTitle.setObjectName("proxyProtocolTitle")

        self.gridLayout_7.addWidget(self.proxyProtocolTitle, 16, 0, 1, 1)
        self.selectNodeTtle = StrongBodyLabel(
            self.configureProxyScrollAreaWidgetContents
        )
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.selectNodeTtle.sizePolicy().hasHeightForWidth()
        )
        self.selectNodeTtle.setSizePolicy(sizePolicy)
        self.selectNodeTtle.setObjectName("selectNodeTtle")

        self.gridLayout_7.addWidget(self.selectNodeTtle, 1, 0, 1, 1)
        self.customTitle = StrongBodyLabel(self.configureProxyScrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.customTitle.sizePolicy().hasHeightForWidth())
        self.customTitle.setSizePolicy(sizePolicy)
        self.customTitle.setObjectName("customTitle")

        self.gridLayout_7.addWidget(self.customTitle, 23, 0, 1, 1)
        self.remotePort = LineEdit(self.configureProxyScrollAreaWidgetContents)
        self.remotePort.setObjectName("remotePort")

        self.gridLayout_7.addWidget(self.remotePort, 6, 1, 1, 1)
        self.localPortTitle = StrongBodyLabel(
            self.configureProxyScrollAreaWidgetContents
        )
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.localPortTitle.sizePolicy().hasHeightForWidth()
        )
        self.localPortTitle.setSizePolicy(sizePolicy)
        self.localPortTitle.setObjectName("localPortTitle")

        self.gridLayout_7.addWidget(self.localPortTitle, 5, 0, 1, 1)
        self.dataTip = BodyLabel(self.configureProxyScrollAreaWidgetContents)
        self.dataTip.setObjectName("dataTip")

        self.gridLayout_7.addWidget(self.dataTip, 14, 0, 1, 2)
        self.hostRewriteTitle = StrongBodyLabel(
            self.configureProxyScrollAreaWidgetContents
        )
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.hostRewriteTitle.sizePolicy().hasHeightForWidth()
        )
        self.hostRewriteTitle.setSizePolicy(sizePolicy)
        self.hostRewriteTitle.setObjectName("hostRewriteTitle")

        self.gridLayout_7.addWidget(self.hostRewriteTitle, 21, 0, 1, 1)
        self.hostRewrite = LineEdit(self.configureProxyScrollAreaWidgetContents)
        self.hostRewrite.setObjectName("hostRewrite")

        self.gridLayout_7.addWidget(self.hostRewrite, 21, 1, 1, 1)
        self.remotePortTitle = StrongBodyLabel(
            self.configureProxyScrollAreaWidgetContents
        )
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.remotePortTitle.sizePolicy().hasHeightForWidth()
        )
        self.remotePortTitle.setSizePolicy(sizePolicy)
        self.remotePortTitle.setObjectName("remotePortTitle")

        self.gridLayout_7.addWidget(self.remotePortTitle, 6, 0, 1, 1)
        spacerItem2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem2, 15, 0, 1, 2)
        self.extendedOptionsTitle = SubtitleLabel(
            self.configureProxyScrollAreaWidgetContents
        )
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.extendedOptionsTitle.sizePolicy().hasHeightForWidth()
        )
        self.extendedOptionsTitle.setSizePolicy(sizePolicy)
        self.extendedOptionsTitle.setObjectName("extendedOptionsTitle")

        self.gridLayout_7.addWidget(self.extendedOptionsTitle, 8, 0, 1, 1)
        self.proxyProtocol = ComboBox(self.configureProxyScrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.proxyProtocol.sizePolicy().hasHeightForWidth()
        )
        self.proxyProtocol.setSizePolicy(sizePolicy)
        self.proxyProtocol.setMinimumSize(QSize(110, 33))
        self.proxyProtocol.setMaximumSize(QSize(16777215, 33))
        self.proxyProtocol.setObjectName("proxyProtocol")

        self.gridLayout_7.addWidget(self.proxyProtocol, 16, 1, 1, 1)
        self.localPort = LineEdit(self.configureProxyScrollAreaWidgetContents)
        self.localPort.setObjectName("localPort")

        self.gridLayout_7.addWidget(self.localPort, 5, 1, 1, 1)
        self.dataEncrypt = SwitchButton(self.configureProxyScrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataEncrypt.sizePolicy().hasHeightForWidth())
        self.dataEncrypt.setSizePolicy(sizePolicy)
        self.dataEncrypt.setChecked(False)
        self.dataEncrypt.setObjectName("dataEncrypt")

        self.gridLayout_7.addWidget(self.dataEncrypt, 11, 1, 1, 1)
        spacerItem3 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem3, 10, 0, 1, 2)
        self.localAddr = LineEdit(self.configureProxyScrollAreaWidgetContents)
        self.localAddr.setObjectName("localAddr")

        self.gridLayout_7.addWidget(self.localAddr, 4, 1, 1, 1)
        self.domainBindTitle = StrongBodyLabel(
            self.configureProxyScrollAreaWidgetContents
        )
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.domainBindTitle.sizePolicy().hasHeightForWidth()
        )
        self.domainBindTitle.setSizePolicy(sizePolicy)
        self.domainBindTitle.setObjectName("domainBindTitle")

        self.gridLayout_7.addWidget(self.domainBindTitle, 19, 0, 1, 1)
        self.basicConfigProxyTitle = SubtitleLabel(
            self.configureProxyScrollAreaWidgetContents
        )
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.basicConfigProxyTitle.sizePolicy().hasHeightForWidth()
        )
        self.basicConfigProxyTitle.setSizePolicy(sizePolicy)
        self.basicConfigProxyTitle.setObjectName("basicConfigProxyTitle")

        self.gridLayout_7.addWidget(self.basicConfigProxyTitle, 0, 0, 1, 1)
        self.proxyModeTitle = StrongBodyLabel(
            self.configureProxyScrollAreaWidgetContents
        )
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.proxyModeTitle.sizePolicy().hasHeightForWidth()
        )
        self.proxyModeTitle.setSizePolicy(sizePolicy)
        self.proxyModeTitle.setObjectName("proxyModeTitle")

        self.gridLayout_7.addWidget(self.proxyModeTitle, 3, 0, 1, 1)
        self.requestFrom = LineEdit(self.configureProxyScrollAreaWidgetContents)
        self.requestFrom.setObjectName("requestFrom")

        self.gridLayout_7.addWidget(self.requestFrom, 20, 1, 1, 1)
        self.extendedOptionsTip = BodyLabel(self.configureProxyScrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.extendedOptionsTip.sizePolicy().hasHeightForWidth()
        )
        self.extendedOptionsTip.setSizePolicy(sizePolicy)
        self.extendedOptionsTip.setObjectName("extendedOptionsTip")

        self.gridLayout_7.addWidget(self.extendedOptionsTip, 9, 0, 1, 2)
        self.urlRoute = LineEdit(self.configureProxyScrollAreaWidgetContents)
        self.urlRoute.setObjectName("urlRoute")

        self.gridLayout_7.addWidget(self.urlRoute, 18, 1, 1, 1)
        self.urlRouteTitle = StrongBodyLabel(
            self.configureProxyScrollAreaWidgetContents
        )
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.urlRouteTitle.sizePolicy().hasHeightForWidth()
        )
        self.urlRouteTitle.setSizePolicy(sizePolicy)
        self.urlRouteTitle.setObjectName("urlRouteTitle")

        self.gridLayout_7.addWidget(self.urlRouteTitle, 18, 0, 1, 1)
        self.proxyProtocolTip = BodyLabel(self.configureProxyScrollAreaWidgetContents)
        self.proxyProtocolTip.setObjectName("proxyProtocolTip")

        self.gridLayout_7.addWidget(self.proxyProtocolTip, 17, 0, 1, 2)
        self.dataGzipTitle = StrongBodyLabel(
            self.configureProxyScrollAreaWidgetContents
        )
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.dataGzipTitle.sizePolicy().hasHeightForWidth()
        )
        self.dataGzipTitle.setSizePolicy(sizePolicy)
        self.dataGzipTitle.setObjectName("dataGzipTitle")

        self.gridLayout_7.addWidget(self.dataGzipTitle, 13, 0, 1, 1)
        self.localAddrTitle = StrongBodyLabel(
            self.configureProxyScrollAreaWidgetContents
        )
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.localAddrTitle.sizePolicy().hasHeightForWidth()
        )
        self.localAddrTitle.setSizePolicy(sizePolicy)
        self.localAddrTitle.setObjectName("localAddrTitle")

        self.gridLayout_7.addWidget(self.localAddrTitle, 4, 0, 1, 1)
        self.HorizontalSeparator = HorizontalSeparator(
            self.configureProxyScrollAreaWidgetContents
        )
        self.HorizontalSeparator.setObjectName("HorizontalSeparator")

        self.gridLayout_7.addWidget(self.HorizontalSeparator, 7, 0, 1, 2)
        self.proxyMode = ComboBox(self.configureProxyScrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proxyMode.sizePolicy().hasHeightForWidth())
        self.proxyMode.setSizePolicy(sizePolicy)
        self.proxyMode.setMinimumSize(QSize(110, 33))
        self.proxyMode.setMaximumSize(QSize(16777215, 33))
        self.proxyMode.setObjectName("proxyMode")

        self.gridLayout_7.addWidget(self.proxyMode, 3, 1, 1, 1)
        self.requestFromTitle = StrongBodyLabel(
            self.configureProxyScrollAreaWidgetContents
        )
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.requestFromTitle.sizePolicy().hasHeightForWidth()
        )
        self.requestFromTitle.setSizePolicy(sizePolicy)
        self.requestFromTitle.setObjectName("requestFromTitle")

        self.gridLayout_7.addWidget(self.requestFromTitle, 20, 0, 1, 1)
        self.selectNode = BodyLabel(self.configureProxyScrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectNode.sizePolicy().hasHeightForWidth())
        self.selectNode.setSizePolicy(sizePolicy)
        self.selectNode.setObjectName("selectNode")

        self.gridLayout_7.addWidget(self.selectNode, 1, 1, 1, 1)
        spacerItem4 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout_7.addItem(spacerItem4, 12, 0, 1, 2)
        self.dataEncryptTitle = StrongBodyLabel(
            self.configureProxyScrollAreaWidgetContents
        )
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.dataEncryptTitle.sizePolicy().hasHeightForWidth()
        )
        self.dataEncryptTitle.setSizePolicy(sizePolicy)
        self.dataEncryptTitle.setObjectName("dataEncryptTitle")

        self.gridLayout_7.addWidget(self.dataEncryptTitle, 11, 0, 1, 1)
        self.proxyNameTitle = StrongBodyLabel(
            self.configureProxyScrollAreaWidgetContents
        )
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.proxyNameTitle.sizePolicy().hasHeightForWidth()
        )
        self.proxyNameTitle.setSizePolicy(sizePolicy)
        self.proxyNameTitle.setObjectName("proxyNameTitle")

        self.gridLayout_7.addWidget(self.proxyNameTitle, 2, 0, 1, 1)
        self.domainBind = LineEdit(self.configureProxyScrollAreaWidgetContents)
        self.domainBind.setObjectName("domainBind")

        self.gridLayout_7.addWidget(self.domainBind, 19, 1, 1, 1)
        self.proxyName = LineEdit(self.configureProxyScrollAreaWidgetContents)
        self.proxyName.setObjectName("proxyName")

        self.gridLayout_7.addWidget(self.proxyName, 2, 1, 1, 1)
        self.dataGzip = SwitchButton(self.configureProxyScrollAreaWidgetContents)
        self.dataGzip.setObjectName("dataGzip")

        self.gridLayout_7.addWidget(self.dataGzip, 13, 1, 1, 1)
        self.requestPass = LineEdit(self.configureProxyScrollAreaWidgetContents)
        self.requestPass.setObjectName("requestPass")

        self.gridLayout_7.addWidget(self.requestPass, 22, 1, 1, 1)
        self.custom = PlainTextEdit(self.configureProxyScrollAreaWidgetContents)
        self.custom.setObjectName("custom")

        self.gridLayout_7.addWidget(self.custom, 24, 0, 1, 2)
        self.configureProxyScrollArea.setWidget(
            self.configureProxyScrollAreaWidgetContents
        )
        self.gridLayout_5.addWidget(self.configureProxyScrollArea, 1, 3, 1, 1)
        self.finishNewProxyBtn = PrimaryPushButton(self.newProxyPage)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.finishNewProxyBtn.sizePolicy().hasHeightForWidth()
        )
        self.finishNewProxyBtn.setSizePolicy(sizePolicy)
        self.finishNewProxyBtn.setMinimumSize(QSize(0, 50))
        self.finishNewProxyBtn.setObjectName("finishNewProxyBtn")
        self.gridLayout_5.addWidget(self.finishNewProxyBtn, 2, 3, 1, 1)
        self.nodeStackedWidget = QStackedWidget(self.newProxyPage)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.nodeStackedWidget.sizePolicy().hasHeightForWidth()
        )
        self.nodeStackedWidget.setSizePolicy(sizePolicy)
        self.nodeStackedWidget.setObjectName("nodeStackedWidget")
        self.loadingPage = QWidget()
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadingPage.sizePolicy().hasHeightForWidth())
        self.loadingPage.setSizePolicy(sizePolicy)
        self.loadingPage.setObjectName("loadingPage")
        self.gridLayout_8 = QGridLayout(self.loadingPage)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.loadingStatusLayout = QGridLayout()
        self.loadingStatusLayout.setObjectName("loadingStatusLayout")
        self.gridLayout_8.addLayout(self.loadingStatusLayout, 0, 0, 1, 1)
        self.nodeStackedWidget.addWidget(self.loadingPage)
        self.nodePage = QWidget()
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodePage.sizePolicy().hasHeightForWidth())
        self.nodePage.setSizePolicy(sizePolicy)
        self.nodePage.setObjectName("nodePage")
        self.gridLayout_6 = QGridLayout(self.nodePage)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.nodeScrollArea = SmoothScrollArea(self.nodePage)
        self.nodeScrollArea.setFrameShape(QFrame.NoFrame)
        self.nodeScrollArea.setWidgetResizable(True)
        self.nodeScrollArea.setAlignment(Qt.AlignCenter)
        self.nodeScrollArea.setObjectName("nodeScrollArea")
        self.nodeScrollAreaWidgetContents = QWidget()
        self.nodeScrollAreaWidgetContents.setGeometry(QRect(0, 0, 287, 435))
        self.nodeScrollAreaWidgetContents.setObjectName("nodeScrollAreaWidgetContents")
        self.gridLayout_10 = QGridLayout(self.nodeScrollAreaWidgetContents)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.nodeTotalLayout = QVBoxLayout()
        self.nodeTotalLayout.setObjectName("nodeTotalLayout")
        self.cnNodeContainer = QWidget(self.nodeScrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.cnNodeContainer.sizePolicy().hasHeightForWidth()
        )
        self.cnNodeContainer.setSizePolicy(sizePolicy)
        self.cnNodeContainer.setObjectName("cnNodeContainer")
        self.gridLayout_9 = QGridLayout(self.cnNodeContainer)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.cnNodeTitle = SubtitleLabel(self.cnNodeContainer)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cnNodeTitle.sizePolicy().hasHeightForWidth())
        self.cnNodeTitle.setSizePolicy(sizePolicy)
        self.cnNodeTitle.setObjectName("cnNodeTitle")
        self.gridLayout_9.addWidget(self.cnNodeTitle, 0, 0, 1, 1)
        spacerItem5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_9.addItem(spacerItem5, 0, 1, 1, 1)
        self.cnNodeWidget = QWidget(self.cnNodeContainer)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cnNodeWidget.sizePolicy().hasHeightForWidth())
        self.cnNodeWidget.setSizePolicy(sizePolicy)
        self.cnNodeWidget.setObjectName("cnNodeWidget")
        self.gridLayout_9.addWidget(self.cnNodeWidget, 1, 0, 1, 2)
        self.nodeTotalLayout.addWidget(self.cnNodeContainer)
        self.hkTwNodeContainer = QWidget(self.nodeScrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.hkTwNodeContainer.sizePolicy().hasHeightForWidth()
        )
        self.hkTwNodeContainer.setSizePolicy(sizePolicy)
        self.hkTwNodeContainer.setObjectName("hkTwNodeContainer")
        self.gridLayout_12 = QGridLayout(self.hkTwNodeContainer)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.hkTwNodeTitle = SubtitleLabel(self.hkTwNodeContainer)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.hkTwNodeTitle.sizePolicy().hasHeightForWidth()
        )
        self.hkTwNodeTitle.setSizePolicy(sizePolicy)
        self.hkTwNodeTitle.setObjectName("hkTwNodeTitle")
        self.gridLayout_12.addWidget(self.hkTwNodeTitle, 0, 0, 1, 1)
        spacerItem6 = QSpacerItem(32, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_12.addItem(spacerItem6, 0, 1, 1, 1)
        self.hkTwNodeWidget = QWidget(self.hkTwNodeContainer)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.hkTwNodeWidget.sizePolicy().hasHeightForWidth()
        )
        self.hkTwNodeWidget.setSizePolicy(sizePolicy)
        self.hkTwNodeWidget.setObjectName("hkTwNodeWidget")
        self.gridLayout_12.addWidget(self.hkTwNodeWidget, 1, 0, 1, 2)
        self.nodeTotalLayout.addWidget(self.hkTwNodeContainer)
        self.foreignNodeContainer = QWidget(self.nodeScrollAreaWidgetContents)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.foreignNodeContainer.sizePolicy().hasHeightForWidth()
        )
        self.foreignNodeContainer.setSizePolicy(sizePolicy)
        self.foreignNodeContainer.setObjectName("foreignNodeContainer")
        self.gridLayout_11 = QGridLayout(self.foreignNodeContainer)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.foreignNodeTitle = SubtitleLabel(self.foreignNodeContainer)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.foreignNodeTitle.sizePolicy().hasHeightForWidth()
        )
        self.foreignNodeTitle.setSizePolicy(sizePolicy)
        self.foreignNodeTitle.setObjectName("foreignNodeTitle")
        self.gridLayout_11.addWidget(self.foreignNodeTitle, 0, 0, 1, 1)
        spacerItem7 = QSpacerItem(160, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem7, 0, 1, 1, 1)
        self.foreignNodeWidget = QWidget(self.foreignNodeContainer)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.foreignNodeWidget.sizePolicy().hasHeightForWidth()
        )
        self.foreignNodeWidget.setSizePolicy(sizePolicy)
        self.foreignNodeWidget.setObjectName("foreignNodeWidget")
        self.gridLayout_11.addWidget(self.foreignNodeWidget, 1, 0, 1, 2)
        self.nodeTotalLayout.addWidget(self.foreignNodeContainer)
        self.gridLayout_10.addLayout(self.nodeTotalLayout, 0, 0, 1, 1)
        self.nodeScrollArea.setWidget(self.nodeScrollAreaWidgetContents)
        self.gridLayout_6.addWidget(self.nodeScrollArea, 0, 0, 1, 1)
        self.nodeStackedWidget.addWidget(self.nodePage)
        self.gridLayout_5.addWidget(self.nodeStackedWidget, 1, 0, 2, 3)
        self.stackedWidget.addWidget(self.newProxyPage)
        self.gridLayout.addWidget(self.stackedWidget, 1, 1, 1, 1)
        spacerItem8 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 1, 0, 2, 1)
        spacerItem9 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem9, 0, 0, 1, 2)

        self.gridLayout.addWidget(self.stackedWidget, 1, 1, 1, 1)
        spacerItem5 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 0, 2, 1)
        spacerItem6 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem6, 0, 0, 1, 2)

        self.stackedWidget.setCurrentIndex(0)
        self.userInfoStackedWidget.setCurrentIndex(0)
        self.nodeStackedWidget.setCurrentIndex(0)

        self.titleLabel.setText("OpenFrp 开放映射")
        self.pluginVerTitle.setText("插件版本：")
        self.pluginVer.setText(str(OFVariables.ofPluginVersion))
        self.refreshProxyListBtn.setText("刷新隧道列表")
        self.newProxyBtn.setText("新建隧道")
        self.notLoginTip.setText("您尚未登录。")
        self.loginEntryBtn.setText("登录")
        self.accountInfoBtn.setText("信息")
        self.logoutBtn.setText("登出")
        self.newProxyTitle.setText("OpenFrp - 新建隧道")
        self.requestPassTitle.setText("访问密码：")
        self.proxyProtocolTitle.setText("Proxy Protocol")
        self.selectNodeTtle.setText("选择节点：")
        self.customTitle.setText("自定义参数：")
        self.remotePort.setPlaceholderText("不填则随机")
        self.dataTip.setText("开启数据加密 / 数据压缩可能会加大服务器\n" "和客户端压力。")
        self.hostRewriteTitle.setText("HOST重写：")
        self.hostRewrite.setPlaceholderText("frp.example.com")
        self.remotePortTitle.setText("远程端口：")
        self.extendedOptionsTitle.setText("高级选项")
        self.localPort.setPlaceholderText("必填 (如25565)")
        self.dataEncrypt.setOnText("已启用")
        self.dataEncrypt.setOffText("已关闭")
        self.localAddr.setPlaceholderText("必填 (如127.0.0.1)")
        self.domainBindTitle.setText("绑定域名：")
        self.basicConfigProxyTitle.setText("基础配置")
        self.proxyModeTitle.setText("隧道模式：")
        self.requestFrom.setPlaceholderText("frp")
        self.extendedOptionsTip.setText("这些选项仅给有需要的人使用。\n若无需求，请勿乱动。")
        self.urlRoute.setPlaceholderText("\\")
        self.urlRouteTitle.setText("URL路由：")
        self.proxyProtocolTip.setText("Proxy Protocol 开启时,如果服务并不支持,\n或未使用该协议,那么会无法访问。")
        self.dataGzipTitle.setText("数据压缩：")
        self.localAddrTitle.setText("本地地址：")
        self.requestFromTitle.setText("请求来源：")
        self.selectNode.setText("未选择")
        self.dataEncryptTitle.setText("数据加密：")
        self.proxyNameTitle.setText("隧道名称：")
        self.domainBind.setPlaceholderText("用逗号隔开")
        self.proxyName.setPlaceholderText("不填则随机")
        self.dataGzip.setOnText("已启用")
        self.dataGzip.setOffText("已关闭")
        self.requestPass.setPlaceholderText("1145141919810")
        self.finishNewProxyBtn.setText("新建")
        self.cnNodeTitle.setText("国内节点")
        self.hkTwNodeTitle.setText("中国台湾/中国香港节点")
        self.foreignNodeTitle.setText("国外节点")

        self.configureProxyScrollArea.viewport().setStyleSheet(
            GlobalMCSL2Variables.scrollAreaViewportQss
        )
        self.ofProxiesSmoothScrollArea.viewport().setStyleSheet(
            GlobalMCSL2Variables.scrollAreaViewportQss
        )
        self.nodeScrollArea.viewport().setStyleSheet(
            GlobalMCSL2Variables.scrollAreaViewportQss
        )
        self.userImage.setPixmap(QPixmap(":/OFImages/user.png"))
        self.userImage.setFixedSize(QSize(60, 60))
        self.loginEntryBtn.clicked.connect(self.initLoginInterface)
        self.newProxyBackBtn.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(0)
        )
        self.newProxyBtn.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.newProxyBtn.clicked.connect(self.getNodeList_API)
        self.newProxyBtn.setEnabled(False)
        self.refreshProxyListBtn.setEnabled(False)
        self.cnNodeLayout = FlowLayout(self.cnNodeWidget, needAni=True)
        self.hkTwNodeLayout = FlowLayout(self.hkTwNodeWidget, needAni=True)
        self.foreignNodeLayout = FlowLayout(self.foreignNodeWidget, needAni=True)
        self.nodeLayoutList = [
            "PlaceHolder",
            self.cnNodeLayout,
            self.hkTwNodeLayout,
            self.foreignNodeLayout,
        ]
        self.proxyMode.setText("选择后可用")
        self.proxyProtocol.addItems(["关闭", "V1", "V2（推荐）"])
        self.finishNewProxyBtn.setEnabled(False)
        self.refreshProxyListBtn.clicked.connect(self.getUserProxies_API)
        self.proxiesLayout = FlowLayout(self.ofProxiesSmoothScrollArea, needAni=True)
        self.finishNewProxyBtn.clicked.connect(self.newProxyCheck)

    def hideDownloadHelper(self):
        self.downloadingInfoBar = InfoBar(
            icon=FIF.DOWNLOAD,
            title="已隐藏下载窗口",
            content="仍在下载Frpc中，点击按钮恢复下载窗口...",
            orient=Qt.Horizontal,
            isClosable=False,
            duration=-1,
            position=InfoBarPosition.TOP_RIGHT,
            parent=self,
        )
        self.downloadingInfoBar.setCustomBackgroundColor("white", "#202020")
        showDownloadMsgBoxBtn = PushButton()
        showDownloadMsgBoxBtn.setText("恢复")
        showDownloadMsgBoxBtn.clicked.connect(self.downloadingBox.show)
        showDownloadMsgBoxBtn.clicked.connect(self.downloadingInfoBar.close)
        self.downloadingInfoBar.addWidget(showDownloadMsgBoxBtn)
        self.downloadingInfoBar.show()

    @pyqtSlot(list)
    def extractFrpc(self, _: list):
        self.frpcInfoBar.close()
        [dl, t] = _
        dl: Optional[Download]
        self.downloadingBox.hide()
        self.downloadingBox.show()
        if dl is not None:
            if dl.status == "complete":
                self.downloadingBox.downloadProgressWidget.downloadProgressMainWidget.setCurrentIndex(
                    1
                )
            elif dl.status == "error":
                self.downloadingBox.downloadProgressWidget.downloadProgressMainWidget.setCurrentIndex(
                    2
                )
            elif dl.status == "removed":
                self.downloadingBox.downloadProgressWidget.downloadProgressMainWidget.setCurrentIndex(
                    2
                )
        else:
            self.downloadingBox.downloadProgressWidget.downloadProgressMainWidget.setCurrentIndex(
                2
            )
        self.downloadingBox.downloadProgressWidget.downloading = False
        self.downloadingBox.DownloadWidget().closeBoxBtnFinished.click()
        InfoBar.info(title="正在解压Frpc", content="请稍后...", duration=1900, parent=self)
        try:
            try:
                remove("./Plugins/OpenFRP_Plugin/frpc/frpc.exe")
            except Exception:
                pass
            frpcArchive = ZipFile("MCSL2/Downloads/frpc_windows_386.zip", "r")
            frpcArchive.extractall("./Plugins/OpenFRP_Plugin/frpc")
            frpcArchive.close()
            rename(
                "./Plugins/OpenFRP_Plugin/frpc/frpc_windows_386.exe",
                "./Plugins/OpenFRP_Plugin/frpc/frpc.exe",
            )
            remove("MCSL2/Downloads/frpc_windows_386.zip")
            InfoBar.success(title="解压Frpc", content="成功！", duration=1900, parent=self)
        except Exception:
            InfoBar.error(title="解压Frpc", content="失败！", duration=1900, parent=self)

    @pyqtSlot(list)
    def downloadFrpc(self, updateInfo):
        if not Aria2Controller.testAria2Service():
            if not Aria2Controller.startAria2():
                box = MessageBox(
                    title="无法下载Frpc",
                    content="MCSL2的Aria2可能未安装或启动失败。",
                    parent=self.parent(),
                )
                box.exec()
                return
        self.window().switchTo(self)
        uri = f"{updateInfo[1][0]['value']}{updateInfo[0]}frpc_windows_386.zip"
        self.downloadingBox = DownloadMessageBox("frpc_windows_386.zip", parent=self)
        gid = Aria2Controller.download(
            uri=uri,
            watch=True,
            info_get=self.downloadingBox.onInfoGet,
            stopped=self.extractFrpc,
            interval=0.2,
        )
        self.frpcInfoBar = InfoBar(
            icon=FIF.DOWNLOAD,
            title="正在更新Frpc",
            content=f"链接：\n{uri}",
            orient=Qt.Horizontal,
            isClosable=False,
            duration=-1,
            position=InfoBarPosition.TOP_RIGHT,
            parent=self,
        )
        self.frpcInfoBar.show()
        self.downloadingBox.downloadProgressWidget.PrimaryPushButton.clicked.connect(
            self.hideDownloadHelper
        )
        self.downloadingBox.canceled.connect(
            lambda: Aria2Controller.cancelDownloadTask(gid)
        )
        self.downloadingBox.canceled.connect(self.downloadingBox.close)
        self.downloadingBox.paused.connect(
            lambda x: Aria2Controller.pauseDownloadTask(gid)
            if x
            else Aria2Controller.resumeDownloadTask(gid)
        )
        self.downloadingBox.show()

    def initLoginInterface(self):
        OFVariables.loginData = []
        self.loginMessageBox = MessageBox("", "", self)
        self.loginWidget = LoginContainer()
        self.loginWidget.cancelBtn.clicked.connect(self.loginMessageBox.hide)
        self.loginWidget.userNameLineEdit.clear()
        self.loginWidget.passwordLineEdit.clear()
        self.loginWidget.loginBtn.clicked.connect(
            lambda: self.login_API(
                username=self.loginWidget.userNameLineEdit.text(),
                password=self.loginWidget.passwordLineEdit.text(),
            )
        )
        if ofSettingsController.fileSettings["last_user"] != "":
            self.loginWidget.userNameLineEdit.setText(
                ofSettingsController.fileSettings["last_user"]
            )
        if ofSettingsController.fileSettings["last_password"] != "":
            self.loginWidget.passwordLineEdit.setText(
                ofSettingsController.fileSettings["last_password"]
            )
        self.loginMessageBox.textLayout.addWidget(self.loginWidget.loginWidget)
        self.loginMessageBox.titleLabel.setParent(None)
        self.loginMessageBox.contentLabel.setParent(None)
        self.loginMessageBox.buttonGroup.setParent(None)
        self.loginMessageBox.show()

    def login_API(self, username, password):
        if username == "" or password == "":
            InfoBar.error(
                "错误",
                "任何一项都不能为空",
                position=InfoBarPosition.TOP_RIGHT,
                duration=1500,
                isClosable=True,
                parent=self.loginMessageBox,
            )
        else:
            self.loginingInfoBar = InfoBar.info(
                "提示",
                "正在登录...",
                position=InfoBarPosition.TOP_RIGHT,
                duration=-1,
                isClosable=False,
                parent=self.loginMessageBox,
            )
            OFVariables.userName = username
            OFVariables.userPassword = password
            self.loginWidget.loginBtn.setEnabled(False)
            loginThread = LoginThread(self)
            loginThread.finished.connect(self.afterLogin)
            loginThread.start()

    def afterLogin(self):
        ofSettingsController.changeSettings(
            {
                "last_user": OFVariables.userName,
                "last_password": OFVariables.userPassword,
            }
        )
        self.loginWidget.loginBtn.setEnabled(True)
        self.loginingInfoBar.close()
        if OFVariables.loginData[2]:
            OFVariables.userSessionID = OFVariables.loginData[0]
            OFVariables.userAuthorization = OFVariables.loginData[1]
            self.loginMessageBox.hide()
            InfoBar.success(
                "成功",
                "登录成功",
                position=InfoBarPosition.TOP_RIGHT,
                duration=1500,
                isClosable=True,
                parent=self,
            )
            self.userInfoStackedWidget.setCurrentIndex(1)
            self.newProxyBtn.setEnabled(True)
            self.refreshProxyListBtn.setEnabled(True)
            self.getUserInfo_API()
            self.getUserProxies_API()
        else:
            InfoBar.error(
                "错误",
                "登录失败",
                position=InfoBarPosition.TOP_RIGHT,
                duration=1500,
                isClosable=True,
                parent=self,
            )

    def getUserInfo_API(self):
        OFVariables.userInfo = {}
        self.accountInfoBtn.setEnabled(False)
        self.logoutBtn.setEnabled(False)
        getUserInfoThread = GetUserInfoThread(self)
        getUserInfoThread.finished.connect(self.afterGetUserInfo)
        getUserInfoThread.start()

    def afterGetUserInfo(self):
        self.accountInfoBtn.setEnabled(True)
        self.logoutBtn.setEnabled(True)
        if OFVariables.userInfo[1]:
            self.userName.setText(OFVariables.userInfo[0]["username"])
            self.userEmail.setText(OFVariables.userInfo[0]["email"])
            self.logoutBtn.clicked.connect(self.logout)
            self.initUserInfoWidget()
        else:
            self.userName.setText("获取失败。")
            self.userEmail.setText("获取失败。")

    def initUserInfoWidget(self):
        self.userInfoWidget = UserInfoContainer()
        self.userInfoWidget.email.setText(OFVariables.userInfo[0]["email"])
        self.userInfoWidget.traffic.setText(
            f"{round(OFVariables.userInfo[0]['traffic'] / 1000, 2)}Gib"
        )
        self.userInfoWidget.nickName.setText(OFVariables.userInfo[0]["username"])
        self.userInfoWidget.realName.setText(
            "已实名" if OFVariables.userInfo[0]["realname"] else "未实名"
        )
        self.userInfoWidget.numOfProxies.setText(
            f"{OFVariables.userInfo[0]['used']} / {OFVariables.userInfo[0]['proxies']} 条"
        )
        self.userInfoWidget.group.setText(OFVariables.userInfo[0]["friendlyGroup"])
        self.userInfoWidget.inoutLimit.setText(
            f"↑ {round(OFVariables.userInfo[0]['outLimit'] / 1024 * 8, 2)}Mbps | ↓ {round(OFVariables.userInfo[0]['inLimit'] / 1024 * 8, 2)}Mbps"
        )
        self.userInfoMessageBox = UserInfoMessageBox("", "", self)
        self.userInfoMessageBox.textLayout.addWidget(self.userInfoWidget.userInfoWidget)
        self.userInfoMessageBox.titleLabel.setParent(None)
        self.userInfoMessageBox.contentLabel.setParent(None)
        self.userInfoMessageBox.cancelButton.setParent(None)
        self.userInfoMessageBox.yesSignal.connect(self.userInfoMessageBox.hide)
        self.userInfoMessageBox.yesSignal.connect(self.getUserInfo_API)
        self.accountInfoBtn.clicked.connect(self.userInfoMessageBox.show)

    def logout(self):
        variablesLogout()
        ofSettingsController.changeSettings(
            {
                "last_user": OFVariables.userName,
                "last_password": OFVariables.userPassword,
            }
        )
        self.accountInfoBtn.clicked.disconnect()
        self.userInfoStackedWidget.setCurrentIndex(0)
        self.userName.setText("[用户名]")
        self.userEmail.setText("[用户邮箱]")

    def getNodeList_API(self):
        self.finishNewProxyBtn.setEnabled(False)
        OFVariables.nodeListData = []
        try:
            for i in range(1, 3):
                self.nodeLayoutList[i].takeAllWidgets()
            for i in reversed(range(self.loadingStatusLayout.count())):
                self.loadingStatusLayout.itemAt(i).widget().deleteLater()
        except Exception:
            pass
        self.loadingWidget = LoadingTip()
        getNodeListThread = GetNodeListThread(self)
        getNodeListThread.finished.connect(self.afterGetNodeList)
        self.loadingStatusLayout.addWidget(self.loadingWidget)
        getNodeListThread.start()

    def afterGetNodeList(self):
        for i in reversed(range(self.loadingStatusLayout.count())):
            self.loadingStatusLayout.itemAt(i).widget().deleteLater()
        if OFVariables.nodeListData[1]:
            self.nodeStackedWidget.setCurrentIndex(1)
            self.initNodeListWidget()
        else:
            self.loadFailedWidget = LoadFailedTip()
            self.loadFailedWidget.refreshBtn.clicked.connect(self.getNodeList_API)
            self.loadingStatusLayout.addWidget(self.loadFailedWidget)

    def initNodeListWidget(self):
        for i in range(int(OFVariables.nodeListData[0]["total"])):
            nodeWidget = SingleNodeWidget()
            # 节点ID
            nodeWidget.id.setText(f"#{OFVariables.nodeListData[0]['list'][i]['id']}")
            # 节点名称
            nodeWidget.nodeName.setText(OFVariables.nodeListData[0]["list"][i]["name"])
            # 带宽标签
            nodeWidget.addNodeTag(
                type=0,
                bandWidth=[
                    OFVariables.nodeListData[0]["list"][i]["bandwidth"],
                    OFVariables.nodeListData[0]["list"][i]["bandwidthMagnification"],
                ],
            )
            # VIP标签
            if not "normal" in OFVariables.nodeListData[0]["list"][i]["group"]:
                nodeWidget.addNodeTag(type=3)
                if OFVariables.userInfo[0]["group"] == "normal":
                    nodeWidget.clicked.connect(
                        lambda: InfoBar.error(
                            "错误",
                            "这是VIP节点，但你并不是VIP用户。",
                            isClosable=False,
                            duration=1500,
                            position=InfoBarPosition.TOP,
                            parent=self,
                        )
                    )
            # 满载标签
            if OFVariables.nodeListData[0]["list"][i]["fullyLoaded"]:
                nodeWidget.addNodeTag(type=1)
                nodeWidget.clicked.connect(
                    lambda: InfoBar.error(
                        "错误",
                        "该节点满载了。",
                        isClosable=False,
                        duration=1500,
                        position=InfoBarPosition.TOP,
                        parent=self,
                    )
                )
            if (
                "normal" in OFVariables.nodeListData[0]["list"][i]["group"]
                and not OFVariables.nodeListData[0]["list"][i]["fullyLoaded"]
            ):
                nodeWidget.clicked.connect(self.setUpNodeInfoConfiguration)

            # 隧道模式标签
            protocolTypeList = ["tcp", "udp", "http", "https"]
            for protocolType in protocolTypeList:
                if OFVariables.nodeListData[0]["list"][i]["protocolSupport"][
                    protocolType
                ]:
                    nodeWidget.addNodeTag(type=2, protoType=protocolType.upper())
            # 节点注释
            nodeWidget.nodeInfo.setText(
                f"{OFVariables.nodeListData[0]['list'][i]['comments']}"
            )

            nodeWidget.setObjectName(
                f"singleNodeWidget_{i}_{OFVariables.nodeListData[0]['list'][i]['id']}"
            )

            self.nodeLayoutList[
                OFVariables.nodeListData[0]["list"][i]["classify"]
            ].addWidget(nodeWidget)

    def clearNodeInfoConfiguration(self):
        self.selectNode.setText("")
        self.remotePort.setPlaceholderText("1~65535")
        self.proxyMode.clear()
        clearNewProxyConfig()

    def setUpNodeInfoConfiguration(self):
        nodeIdxList = (
            self.sender().objectName().replace("singleNodeWidget_", "").split("_")
        )
        OFVariables.configuringNodeIndex = int(nodeIdxList[0])
        OFVariables.configuringNodeID = int(nodeIdxList[1])
        self.selectNode.setText(
            OFVariables.nodeListData[0]["list"][OFVariables.configuringNodeIndex][
                "name"
            ]
        )
        if (
            OFVariables.nodeListData[0]["list"][OFVariables.configuringNodeIndex][
                "allowPort"
            ]
            is None
            or OFVariables.nodeListData[0]["list"][OFVariables.configuringNodeIndex][
                "allowPort"
            ]
            == ""
        ):
            self.remotePort.setPlaceholderText("1~65535")
        else:
            self.remotePort.setPlaceholderText(
                OFVariables.nodeListData[0]["list"][OFVariables.configuringNodeIndex][
                    "allowPort"
                ]
                .replace("(", "")
                .replace(")", "")
                .replace(",", "~")
            )
            portRequirement = (
                OFVariables.nodeListData[0]["list"][OFVariables.configuringNodeIndex][
                    "allowPort"
                ]
                .replace("(", "")
                .replace(")", "")
                .split(",")
            )
            OFVariables.configuringNodeMinPort = int(portRequirement[0])
            OFVariables.configuringNodeMaxPort = int(portRequirement[1])
        availableProxyModeList = ["tcp", "udp", "http", "https"]
        for protocolType in availableProxyModeList:
            if not OFVariables.nodeListData[0]["list"][
                OFVariables.configuringNodeIndex
            ]["protocolSupport"][protocolType]:
                availableProxyModeList.remove(protocolType)
        self.proxyMode.addItems(availableProxyModeList)
        self.finishNewProxyBtn.setEnabled(True)

    def newProxyCheck(self):
        err = False
        err = bool(self.localAddr.text() == "")
        err = bool(self.localPort.text() == "")
        if self.localPort.text() != "":
            err = not self.localPort.text().isdigit()
        if self.remotePort.text() != "":
            err = bool(int(self.remotePort.text()) < OFVariables.configuringNodeMinPort)
            err = bool(int(self.remotePort.text()) > OFVariables.configuringNodeMaxPort)
        if err:
            InfoBar.error(
                "错误",
                "请正确填写必需参数！",
                position=InfoBarPosition.TOP,
                duration=1500,
                isClosable=True,
                parent=self,
            )
            return
        else:
            OFVariables.configuringProxyName = (
                self.proxyName.text()
                if self.proxyName.text() != ""
                else f"MCSL2_OfProxy_{randint(10000, 50000)}"
            )
            OFVariables.configuringProxyType = self.proxyMode.text().strip().lower()
            OFVariables.configuringProxyLocalAddr = self.localAddr.text()
            OFVariables.configuringProxyDomainBind = self.domainBind.text()
            OFVariables.configuringProxyHostRewrite = self.hostRewrite.text()
            OFVariables.configuringProxyRequestFrom = self.requestFrom.text()
            OFVariables.configuringProxyCustom = self.custom.toPlainText()
            OFVariables.configuringProxyURLRoute = self.urlRoute.text()
            OFVariables.configuringRequestPass = self.requestPass.text()
            OFVariables.configuringProxyLocalPort = int(self.localPort.text())
            OFVariables.configuringProxyRemotePort = (
                int(self.remotePort.text())
                if self.remotePort.text() != ""
                else randint(
                    OFVariables.configuringNodeMinPort,
                    OFVariables.configuringNodeMaxPort,
                )
            )
            OFVariables.configuringProxyDataEncrypt = self.dataEncrypt.isChecked()
            OFVariables.configuringProxyDataGZip = self.dataGzip.isChecked()
            self.newProxy_API()

    def newProxy_API(self):
        newProxyThread = NewProxyThread(self)
        newProxyThread.finished.connect(self.afterNewProxy)
        newProxyThread.start()

    def afterNewProxy(self):
        if OFVariables.newProxyData[1]:
            InfoBar.success(
                "成功",
                OFVariables.newProxyData[2],
                position=InfoBarPosition.TOP,
                duration=1500,
                isClosable=True,
                parent=self,
            )
            self.stackedWidget.setCurrentIndex(0)
            self.getUserInfo_API()
            self.getUserProxies_API()
            self.clearNodeInfoConfiguration()
        else:
            InfoBar.error(
                "失败",
                OFVariables.newProxyData[2],
                position=InfoBarPosition.TOP,
                duration=1500,
                isClosable=True,
                parent=self,
            )

    def getUserProxies_API(self):
        self.proxiesLayout.takeAllWidgets()
        self.gettingUserProxiesInfoBar = InfoBar.info(
            "提示",
            "正在获取用户隧道列表...",
            position=InfoBarPosition.TOP_RIGHT,
            duration=-1,
            isClosable=False,
            parent=self,
        )
        getUserProxyThread = GetUserProxiesThread(self)
        getUserProxyThread.finished.connect(self.afterGetUserProxies)
        getUserProxyThread.start()

    def afterGetUserProxies(self):
        self.gettingUserProxiesInfoBar.close()
        if OFVariables.userProxiesData[2]:
            self.initProxiesListWidget()
        else:
            InfoBar.error(
                "错误",
                "获取用户隧道列表失败",
                position=InfoBarPosition.TOP_RIGHT,
                duration=1500,
                isClosable=True,
                parent=self,
            )

    def initProxiesListWidget(self):
        for i in range(OFVariables.userProxiesData[0]):
            proxyWidget = SingleProxyWidget()
            proxyWidget.proxyName.setText(
                OFVariables.userProxiesData[1][i]["proxyName"]
            )
            proxyWidget.proxyMode.setText(
                OFVariables.userProxiesData[1][i]["proxyType"].upper()
            )
            proxyWidget.proxyLinkInfo.setText(
                f"{OFVariables.userProxiesData[1][i]['localIp']}:{OFVariables.userProxiesData[1][i]['localPort']} -> {OFVariables.userProxiesData[1][i]['remotePort']}\n#{OFVariables.userProxiesData[1][i]['nid']} {OFVariables.userProxiesData[1][i]['friendlyNode']}"
            )
            proxyWidget.SwitchButton.setChecked(
                OFVariables.userProxiesData[1][i]["online"]
            )
            proxyWidget.copyProxyLink.clicked.connect(
                lambda: QApplication.clipboard().setText(
                    OFVariables.userProxiesData[1][i]["connectAddress"]
                )
            )
            proxyWidget.copyProxyLink.clicked.connect(
                lambda: InfoBar.success(
                    "提示",
                    "已复制",
                    position=InfoBarPosition.TOP,
                    duration=1500,
                    isClosable=True,
                    parent=self,
                )
            )
            proxyWidget.editProxy.setObjectName(
                f"editProxy_{OFVariables.userProxiesData[1][i]['nid']}_{OFVariables.userProxiesData[1][i]['id']}"
            )
            proxyWidget.editProxy.setEnabled(False)
            proxyWidget.deleteProxy.setObjectName(
                f"editProxy_{OFVariables.userProxiesData[1][i]['id']}"
            )
            proxyWidget.deleteProxy.clicked.connect(self.removeProxy)
            proxyWidget.SwitchButton.setObjectName(
                f"{OFVariables.userProxiesData[1][i]['id']}|"
            )
            proxyWidget.SwitchButton.checkedChanged.connect(self.switchProxy)
            self.proxiesLayout.addWidget(proxyWidget)

    def removeProxy(self):
        self.sender().setEnabled(False)
        OFVariables.removeProxyID = int(
            self.sender().objectName().replace("editProxy_", "")
        )
        removeProxyThread = RemoveProxyThread(self)
        removeProxyThread.finished.connect(self.afterRemoveProxy)
        removeProxyThread.start()

    def afterRemoveProxy(self):
        if OFVariables.removeProxyData[1]:
            InfoBar.success(
                "成功",
                OFVariables.removeProxyData[2],
                position=InfoBarPosition.TOP_RIGHT,
                duration=1500,
                isClosable=True,
                parent=self,
            )
            self.getUserInfo_API()
            self.getUserProxies_API()
        else:
            InfoBar.error(
                "失败",
                OFVariables.removeProxyData[2],
                position=InfoBarPosition.TOP_RIGHT,
                duration=1500,
                isClosable=True,
                parent=self,
            )

    def switchProxy(self):
        id = self.sender().objectName().split("|")[0]
        if self.sender().isChecked():
            # 在|前的是隧道id，后为列表中的frpc进程id
            # 设置objectName同时启动Frpc
            self.sender().setObjectName(
                f"{id}|{FrpcBridge(self).newFrpc(proxyName=self.sender().parent().parent().proxyName.text(), tunnelId=id)}"
            )
        else:
            # 先关闭Frpc
            FrpcBridge(self).stopFrpc(int(self.sender().objectName().split("|")[1]))
            # 设置objectName
            self.sender().setObjectName(f"{self.sender().objectName().split('|')[0]}")
