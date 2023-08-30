from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QGridLayout, QSizePolicy
from qfluentwidgets import BodyLabel, CardWidget, StrongBodyLabel, SubtitleLabel


class SingleNodeWidget(CardWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("singleNodeWidget")

        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(280, 170))
        self.setMaximumSize(QSize(280, 170))
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        self.SubtitleLabel = SubtitleLabel(self)
        self.SubtitleLabel.setObjectName("SubtitleLabel")

        self.gridLayout.addWidget(self.SubtitleLabel, 0, 2, 1, 1)
        self.nodeTag = StrongBodyLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodeTag.sizePolicy().hasHeightForWidth())
        self.nodeTag.setSizePolicy(sizePolicy)
        self.nodeTag.setStyleSheet("StrongBodyLabel {\n" "    color: red;\n" "}")
        self.nodeTag.setObjectName("nodeTag")

        self.gridLayout.addWidget(self.nodeTag, 0, 1, 1, 1)
        self.num = BodyLabel(self)
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

        self.gridLayout.addWidget(self.num, 0, 0, 1, 1)
        self.nodeInfo = BodyLabel(self)
        self.nodeInfo.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.nodeInfo.setObjectName("nodeInfo")

        self.gridLayout.addWidget(self.nodeInfo, 1, 1, 1, 2)

        self.SubtitleLabel.setText("[节点名称]")
        self.nodeTag.setText("[状态]")
        self.num.setText("#")
        self.nodeInfo.setText("[详情]")
