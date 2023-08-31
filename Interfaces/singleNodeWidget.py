from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QGridLayout, QSizePolicy, QSpacerItem, QWidget
from qfluentwidgets import BodyLabel, CardWidget, StrongBodyLabel, SubtitleLabel


class SingleNodeWidget(CardWidget):
    def __init__(self):
        super().__init__()

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setFixedSize(QSize(300, 190))
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        self.nodeWidget = QWidget(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodeWidget.sizePolicy().hasHeightForWidth())
        self.nodeWidget.setSizePolicy(sizePolicy)
        self.nodeWidget.setFixedSize(QSize(280, 170))
        self.nodeWidget.setObjectName("nodeWidget")

        self.gridLayout_2 = QGridLayout(self.nodeWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.num = BodyLabel(self.nodeWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.num.sizePolicy().hasHeightForWidth())
        self.num.setSizePolicy(sizePolicy)
        self.num.setStyleSheet(
            "BodyLabel {\n"
            "    color: white;\n"
            "    background-color: #009faa;\n"
            "    border-radius: 3px;\n"
            "    padding: 2px;\n"
            "}"
        )
        self.num.setObjectName("num")

        self.gridLayout_2.addWidget(self.num, 0, 0, 1, 1)
        self.nodeTag = StrongBodyLabel(self.nodeWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodeTag.sizePolicy().hasHeightForWidth())
        self.nodeTag.setSizePolicy(sizePolicy)
        self.nodeTag.setStyleSheet("StrongBodyLabel {\n" "    color: red;\n" "}")
        self.nodeTag.setObjectName("nodeTag")

        self.gridLayout_2.addWidget(self.nodeTag, 0, 1, 1, 1)
        self.nodeName = SubtitleLabel(self.nodeWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodeName.sizePolicy().hasHeightForWidth())
        self.nodeName.setSizePolicy(sizePolicy)
        self.nodeName.setObjectName("nodeName")

        self.gridLayout_2.addWidget(self.nodeName, 0, 2, 1, 1)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 3, 1, 1)
        self.nodeInfo = BodyLabel(self.nodeWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodeInfo.sizePolicy().hasHeightForWidth())
        self.nodeInfo.setSizePolicy(sizePolicy)
        self.nodeInfo.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.nodeInfo.setObjectName("nodeInfo")

        self.gridLayout_2.addWidget(self.nodeInfo, 1, 0, 1, 4)
        self.gridLayout.addWidget(self.nodeWidget, 0, 0, 1, 1)

        # self.SubtitleLabel.setText("[节点名称]")
        # self.nodeTag.setText("[状态]")
        # self.num.setText("#")
        # self.nodeInfo.setText("[详情]")
