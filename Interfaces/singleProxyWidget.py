from PyQt5.QtCore import QSize
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
)

from qfluentwidgets import BodyLabel, CardWidget, SubtitleLabel, TransparentPushButton


class SingleProxyWidget(CardWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("singleProxyWidget")

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(640, 120))
        self.setMaximumSize(QSize(16777215, 120))
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        self.proxyName = SubtitleLabel(self)
        self.proxyName.setObjectName("proxyName")

        self.gridLayout.addWidget(self.proxyName, 0, 0, 1, 1)
        self.deleteProxy = TransparentPushButton(self)
        self.deleteProxy.setIcon(FIF.DELETE)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteProxy.sizePolicy().hasHeightForWidth())
        self.deleteProxy.setSizePolicy(sizePolicy)
        self.deleteProxy.setObjectName("deleteProxy")

        self.gridLayout.addWidget(self.deleteProxy, 3, 1, 1, 1)
        self.proxyInfo = QWidget(self)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proxyInfo.sizePolicy().hasHeightForWidth())
        self.proxyInfo.setSizePolicy(sizePolicy)
        self.proxyInfo.setObjectName("proxyInfo")

        self.verticalLayout = QVBoxLayout(self.proxyInfo)
        self.verticalLayout.setObjectName("verticalLayout")

        self.proxyMode = BodyLabel(self.proxyInfo)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.proxyMode.sizePolicy().hasHeightForWidth())
        self.proxyMode.setSizePolicy(sizePolicy)
        self.proxyMode.setObjectName("proxyMode")

        self.verticalLayout.addWidget(self.proxyMode)
        self.proxyLinkInfo = BodyLabel(self.proxyInfo)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.proxyLinkInfo.sizePolicy().hasHeightForWidth()
        )
        self.proxyLinkInfo.setSizePolicy(sizePolicy)
        self.proxyLinkInfo.setObjectName("proxyLinkInfo")

        self.verticalLayout.addWidget(self.proxyLinkInfo)
        self.gridLayout.addWidget(self.proxyInfo, 1, 0, 3, 1)
        self.copyProxyLink = TransparentPushButton(self)
        self.copyProxyLink.setIcon(FIF.COPY)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.copyProxyLink.sizePolicy().hasHeightForWidth()
        )
        self.copyProxyLink.setSizePolicy(sizePolicy)
        self.copyProxyLink.setObjectName("copyProxyLink")

        self.gridLayout.addWidget(self.copyProxyLink, 0, 1, 1, 1)
        self.editProxy = TransparentPushButton(FIF.EDIT, self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editProxy.sizePolicy().hasHeightForWidth())
        self.editProxy.setSizePolicy(sizePolicy)
        self.editProxy.setObjectName("editProxy")

        self.gridLayout.addWidget(self.editProxy, 1, 1, 1, 1)

        self.proxyName.setText("[隧道名称]")
        self.deleteProxy.setText("删除隧道")
        self.proxyMode.setText("[隧道模式]")
        self.proxyLinkInfo.setText("[映射信息]")
        self.copyProxyLink.setText("复制链接")
        self.editProxy.setText("编辑隧道")
