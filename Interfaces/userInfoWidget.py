from PyQt5.QtCore import QSize, QRect
from PyQt5.QtWidgets import (
    QWidget,
    QGridLayout,
    QSizePolicy,
    QVBoxLayout,
    QSpacerItem,
)
from qfluentwidgets import (
    BodyLabel,
    SubtitleLabel,
    TitleLabel,
)


class UserInfoContainer(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("userInfoContainer")

        self.userInfoWidget = QWidget(self)
        self.userInfoWidget.setGeometry(QRect(10, 20, 471, 361))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.userInfoWidget.sizePolicy().hasHeightForWidth())
        self.userInfoWidget.setSizePolicy(sizePolicy)
        self.userInfoWidget.setFixedSize(QSize(471, 361))
        self.userInfoWidget.setObjectName("userInfoWidget")

        self.gridLayout = QGridLayout(self.userInfoWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.widget = QWidget(self.userInfoWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")

        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.emailWidget = QWidget(self.widget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emailWidget.sizePolicy().hasHeightForWidth())
        self.emailWidget.setSizePolicy(sizePolicy)
        self.emailWidget.setMinimumSize(QSize(215, 65))
        self.emailWidget.setMaximumSize(QSize(215, 65))
        self.emailWidget.setObjectName("emailWidget")

        self.verticalLayout_2 = QVBoxLayout(self.emailWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.emailTitle = SubtitleLabel(self.emailWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emailTitle.sizePolicy().hasHeightForWidth())
        self.emailTitle.setSizePolicy(sizePolicy)
        self.emailTitle.setObjectName("emailTitle")

        self.verticalLayout_2.addWidget(self.emailTitle)
        self.email = BodyLabel(self.emailWidget)
        self.email.setObjectName("email")

        self.verticalLayout_2.addWidget(self.email)
        self.gridLayout_2.addWidget(self.emailWidget, 0, 0, 1, 1)
        self.trafficWidget = QWidget(self.widget)
        self.trafficWidget.setMinimumSize(QSize(215, 65))
        self.trafficWidget.setMaximumSize(QSize(215, 65))
        self.trafficWidget.setObjectName("trafficWidget")

        self.verticalLayout_4 = QVBoxLayout(self.trafficWidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.trafficTitle = SubtitleLabel(self.trafficWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trafficTitle.sizePolicy().hasHeightForWidth())
        self.trafficTitle.setSizePolicy(sizePolicy)
        self.trafficTitle.setObjectName("trafficTitle")

        self.verticalLayout_4.addWidget(self.trafficTitle)
        self.traffic = BodyLabel(self.trafficWidget)
        self.traffic.setObjectName("traffic")

        self.verticalLayout_4.addWidget(self.traffic)
        self.gridLayout_2.addWidget(self.trafficWidget, 0, 1, 1, 1)
        self.nickNameWidget = QWidget(self.widget)
        self.nickNameWidget.setMinimumSize(QSize(215, 65))
        self.nickNameWidget.setMaximumSize(QSize(215, 65))
        self.nickNameWidget.setObjectName("nickNameWidget")

        self.verticalLayout = QVBoxLayout(self.nickNameWidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.nickNameTitle = SubtitleLabel(self.nickNameWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.nickNameTitle.sizePolicy().hasHeightForWidth()
        )
        self.nickNameTitle.setSizePolicy(sizePolicy)
        self.nickNameTitle.setObjectName("nickNameTitle")

        self.verticalLayout.addWidget(self.nickNameTitle)
        self.nickName = BodyLabel(self.nickNameWidget)
        self.nickName.setObjectName("nickName")

        self.verticalLayout.addWidget(self.nickName)
        self.gridLayout_2.addWidget(self.nickNameWidget, 1, 0, 1, 1)
        self.realNameWidget = QWidget(self.widget)
        self.realNameWidget.setMinimumSize(QSize(215, 65))
        self.realNameWidget.setMaximumSize(QSize(215, 65))
        self.realNameWidget.setObjectName("realNameWidget")

        self.verticalLayout_5 = QVBoxLayout(self.realNameWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        self.realNameTitle = SubtitleLabel(self.realNameWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.realNameTitle.sizePolicy().hasHeightForWidth()
        )
        self.realNameTitle.setSizePolicy(sizePolicy)
        self.realNameTitle.setObjectName("realNameTitle")

        self.verticalLayout_5.addWidget(self.realNameTitle)
        self.realName = BodyLabel(self.realNameWidget)
        self.realName.setObjectName("realName")

        self.verticalLayout_5.addWidget(self.realName)
        self.gridLayout_2.addWidget(self.realNameWidget, 1, 1, 1, 1)
        self.numOfProxiesWidget = QWidget(self.widget)
        self.numOfProxiesWidget.setMinimumSize(QSize(215, 65))
        self.numOfProxiesWidget.setMaximumSize(QSize(215, 65))
        self.numOfProxiesWidget.setObjectName("numOfProxiesWidget")

        self.verticalLayout_3 = QVBoxLayout(self.numOfProxiesWidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.numOfProxiesTitle = SubtitleLabel(self.numOfProxiesWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.numOfProxiesTitle.sizePolicy().hasHeightForWidth()
        )
        self.numOfProxiesTitle.setSizePolicy(sizePolicy)
        self.numOfProxiesTitle.setObjectName("numOfProxiesTitle")

        self.verticalLayout_3.addWidget(self.numOfProxiesTitle)
        self.numOfProxies = BodyLabel(self.numOfProxiesWidget)
        self.numOfProxies.setObjectName("numOfProxies")

        self.verticalLayout_3.addWidget(self.numOfProxies)
        self.gridLayout_2.addWidget(self.numOfProxiesWidget, 2, 0, 1, 1)
        self.groupWidget = QWidget(self.widget)
        self.groupWidget.setMinimumSize(QSize(215, 65))
        self.groupWidget.setMaximumSize(QSize(215, 65))
        self.groupWidget.setObjectName("groupWidget")

        self.verticalLayout_6 = QVBoxLayout(self.groupWidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")

        self.groupTitle = SubtitleLabel(self.groupWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupTitle.sizePolicy().hasHeightForWidth())
        self.groupTitle.setSizePolicy(sizePolicy)
        self.groupTitle.setObjectName("groupTitle")

        self.verticalLayout_6.addWidget(self.groupTitle)
        self.group = BodyLabel(self.groupWidget)
        self.group.setObjectName("group")

        self.verticalLayout_6.addWidget(self.group)
        self.gridLayout_2.addWidget(self.groupWidget, 2, 1, 1, 1)
        self.inoutLimitWidget = QWidget(self.widget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.inoutLimitWidget.sizePolicy().hasHeightForWidth()
        )
        self.inoutLimitWidget.setSizePolicy(sizePolicy)
        self.inoutLimitWidget.setMinimumSize(QSize(215, 65))
        self.inoutLimitWidget.setMaximumSize(QSize(215, 65))
        self.inoutLimitWidget.setObjectName("inoutLimitWidget")

        self.verticalLayout_7 = QVBoxLayout(self.inoutLimitWidget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")

        self.inoutLimitTitle = SubtitleLabel(self.inoutLimitWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.inoutLimitTitle.sizePolicy().hasHeightForWidth()
        )
        self.inoutLimitTitle.setSizePolicy(sizePolicy)
        self.inoutLimitTitle.setObjectName("inoutLimitTitle")

        self.verticalLayout_7.addWidget(self.inoutLimitTitle)
        self.inoutLimit = BodyLabel(self.inoutLimitWidget)
        self.inoutLimit.setObjectName("inoutLimit")

        self.verticalLayout_7.addWidget(self.inoutLimit)
        self.gridLayout_2.addWidget(self.inoutLimitWidget, 3, 0, 1, 1)
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 2)
        self.userInfoTitle = TitleLabel(self.userInfoWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.userInfoTitle.sizePolicy().hasHeightForWidth()
        )
        self.userInfoTitle.setSizePolicy(sizePolicy)
        self.userInfoTitle.setObjectName("userInfoTitle")

        self.gridLayout.addWidget(self.userInfoTitle, 0, 0, 1, 1)

        self.emailTitle.setText("邮箱")
        self.trafficTitle.setText("可用流量")
        self.nickNameTitle.setText("昵称")
        self.realNameTitle.setText("实名状态")
        self.numOfProxiesTitle.setText("隧道数")
        self.groupTitle.setText("用户组")
        self.inoutLimitTitle.setText("带宽速率")
        self.userInfoTitle.setText("用户信息")

        self.email.setText("[邮箱]")
        self.traffic.setText("[流量]")
        self.nickName.setText("[昵称]")
        self.realName.setText("[实名状态]")
        self.numOfProxies.setText("[隧道数]")
        self.group.setText("[用户组]")
        self.inoutLimit.setText("[带宽速率]")