from PyQt5.QtCore import QSize, Qt, QRect
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
)
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
from MCSL2Lib.variables import GlobalMCSL2Variables
from ..variables import OFVariables, variablesLogout
from ..APIThreads import *
from .loginWidget import LoginContainer
from .images import *  # noqa: F401
from .userInfoWidget import UserInfoContainer
from ..OpenFrpLib import getUserInfo


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
        self.ofProxiesSmoothScrollArea.setAlignment(Qt.AlignCenter)
        self.ofProxiesSmoothScrollArea.setObjectName("ofProxiesSmoothScrollArea")

        self.ofProxiesScrollAreaWidgetContents = QWidget()
        self.ofProxiesScrollAreaWidgetContents.setGeometry(QRect(0, 0, 648, 380))
        self.ofProxiesScrollAreaWidgetContents.setObjectName(
            "ofProxiesScrollAreaWidgetContents"
        )

        self.verticalLayout = QVBoxLayout(self.ofProxiesScrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        self.ofProxiesLayout = QVBoxLayout()
        self.ofProxiesLayout.setObjectName("ofProxiesLayout")

        self.verticalLayout.addLayout(self.ofProxiesLayout)
        self.ofProxiesSmoothScrollArea.setWidget(self.ofProxiesScrollAreaWidgetContents)
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
        spacerItem1 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 0, 2, 1, 2)
        self.newProxyBackBtn = TransparentToolButton(self.newProxyPage)
        self.newProxyBackBtn.setObjectName("newProxyBackBtn")

        self.gridLayout_5.addWidget(self.newProxyBackBtn, 0, 0, 1, 1)
        self.nodeWidget = QWidget(self.newProxyPage)
        self.nodeWidget.setObjectName("nodeWidget")

        self.gridLayout_5.addWidget(self.nodeWidget, 1, 0, 1, 3)
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
        self.configureProxyScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.configureProxyScrollArea.setWidgetResizable(True)
        self.configureProxyScrollArea.setObjectName("configureProxyScrollArea")

        self.configureProxyScrollAreaWidgetContents = QWidget()
        self.configureProxyScrollAreaWidgetContents.setGeometry(QRect(0, 0, 328, 882))
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
        self.stackedWidget.addWidget(self.newProxyPage)
        self.gridLayout.addWidget(self.stackedWidget, 1, 1, 1, 1)
        spacerItem5 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 0, 2, 1)
        spacerItem6 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem6, 0, 0, 1, 2)

        self.stackedWidget.setCurrentIndex(0)
        self.userInfoStackedWidget.setCurrentIndex(0)

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

        self.configureProxyScrollArea.viewport().setStyleSheet(
            GlobalMCSL2Variables.scrollAreaViewportQss
        )
        self.ofProxiesSmoothScrollArea.viewport().setStyleSheet(
            GlobalMCSL2Variables.scrollAreaViewportQss
        )
        proxyLayout = FlowLayout(self.nodeWidget)
        self.userImage.setPixmap(QPixmap(":/OFImages/user.png"))
        self.userImage.setFixedSize(QSize(60, 60))
        self.loginEntryBtn.clicked.connect(self.initLoginInterface)

    def initLoginInterface(self):
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
            self.getUserInfo_API()
        else:
            InfoBar.error(
                "错误",
                "登录失败",
                position=InfoBarPosition.TOP_RIGHT,
                duration=1500,
                isClosable=True,
                parent=self.window(),
            )

    def getUserInfo_API(self):
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
        self.userInfoMessageBox = MessageBox("", "", self)
        self.userInfoMessageBox.textLayout.addWidget(self.userInfoWidget.userInfoWidget)
        self.userInfoMessageBox.titleLabel.setParent(None)
        self.userInfoMessageBox.contentLabel.setParent(None)
        self.userInfoMessageBox.cancelButton.setParent(None)
        self.userInfoMessageBox.yesSignal.connect(self.userInfoMessageBox.hide)
        self.accountInfoBtn.clicked.connect(self.userInfoMessageBox.show)

    def logout(self):
        variablesLogout()
        self.accountInfoBtn.clicked.disconnect()
        self.userInfoStackedWidget.setCurrentIndex(0)
        self.userName.setText("[用户名]")
        self.userEmail.setText("[用户邮箱]")
