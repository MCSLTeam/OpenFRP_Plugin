from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QWidget,
    QGridLayout,
    QSizePolicy,
    QVBoxLayout,
)
from qfluentwidgets import (
    BodyLabel,
    SubtitleLabel,
    TransparentPushButton,
    FluentIcon as FIF,
    SwitchButton,
)

from qfluentwidgets import BodyLabel, CardWidget, SubtitleLabel, TransparentPushButton


class SingleProxyWidget(CardWidget):
    def __init__(self):
        super().__init__()

        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setFixedSize(QSize(300, 220))
        self.gridLayout = QGridLayout(self)

        self.ProxyWidget = QWidget(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ProxyWidget.sizePolicy().hasHeightForWidth())
        self.ProxyWidget.setSizePolicy(sizePolicy)

        self.gridLayout_2 = QGridLayout(self.ProxyWidget)

        self.proxyName = SubtitleLabel(self.ProxyWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proxyName.sizePolicy().hasHeightForWidth())
        self.proxyName.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.proxyName, 0, 0, 1, 2)
        self.SwitchButton = SwitchButton(self.ProxyWidget)

        self.gridLayout_2.addWidget(self.SwitchButton, 0, 2, 1, 1)
        self.proxyInfo = QWidget(self.ProxyWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proxyInfo.sizePolicy().hasHeightForWidth())
        self.proxyInfo.setSizePolicy(sizePolicy)

        self.verticalLayout = QVBoxLayout(self.proxyInfo)

        self.proxyMode = BodyLabel(self.proxyInfo)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proxyMode.sizePolicy().hasHeightForWidth())
        self.proxyMode.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.proxyMode)
        self.proxyLinkInfo = BodyLabel(self.proxyInfo)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.proxyLinkInfo.sizePolicy().hasHeightForWidth()
        )
        self.proxyLinkInfo.setSizePolicy(sizePolicy)
        self.proxyLinkInfo.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)

        self.verticalLayout.addWidget(self.proxyLinkInfo)
        self.gridLayout_2.addWidget(self.proxyInfo, 1, 0, 1, 3)
        self.copyProxyLink = TransparentPushButton(self.ProxyWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.copyProxyLink.sizePolicy().hasHeightForWidth()
        )
        self.copyProxyLink.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.copyProxyLink, 2, 0, 1, 1)
        self.editProxy = TransparentPushButton(self.ProxyWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editProxy.sizePolicy().hasHeightForWidth())
        self.editProxy.setSizePolicy(sizePolicy)
        
        self.gridLayout_2.addWidget(self.editProxy, 2, 1, 1, 1)
        self.deleteProxy = TransparentPushButton(self.ProxyWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteProxy.sizePolicy().hasHeightForWidth())
        self.deleteProxy.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.deleteProxy, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.ProxyWidget, 0, 0, 1, 2)
        self.copyProxyLink.setIcon(FIF.COPY)
        self.editProxy.setIcon(FIF.EDIT)
        self.deleteProxy.setIcon(FIF.REMOVE)
        
        self.copyProxyLink.setText("复制链接")
        self.editProxy.setText("编辑")
        self.SwitchButton.setOnText("开")
        self.SwitchButton.setOffText("关")
        # self.proxyName.setText("[隧道名称]")
        # self.proxyMode.setText("[隧道模式]")
        # self.proxyLinkInfo.setText("[映射信息]")
        self.deleteProxy.setText("删除")
