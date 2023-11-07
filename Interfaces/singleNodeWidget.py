from typing import Optional
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QGridLayout, QSizePolicy, QSpacerItem, QWidget
from qfluentwidgets import BodyLabel, CardWidget, FlowLayout, SubtitleLabel, InfoBadge
class SingleNodeWidget(CardWidget):
    def __init__(self):
        super().__init__()

        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setFixedSize(QSize(300, 125))

        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        self.nodeWidget = QWidget(self)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodeWidget.sizePolicy().hasHeightForWidth())
        self.nodeWidget.setSizePolicy(sizePolicy)
        self.nodeWidget.setObjectName("nodeWidget")

        self.gridLayout_2 = QGridLayout(self.nodeWidget)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.id = BodyLabel(self.nodeWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.id.sizePolicy().hasHeightForWidth())
        self.id.setSizePolicy(sizePolicy)
        self.id.setStyleSheet(
            "BodyLabel {\n"
            "    color: white;\n"
            "    background-color: #009faa;\n"
            "    border-radius: 3px;\n"
            "    padding: 2px;\n"
            "}"
        )
        self.id.setObjectName("id")
        self.gridLayout_2.addWidget(self.id, 0, 0, 1, 1)

        self.nodeInfo = BodyLabel(self.nodeWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodeInfo.sizePolicy().hasHeightForWidth())
        self.nodeInfo.setSizePolicy(sizePolicy)
        self.nodeInfo.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.nodeInfo.setObjectName("nodeInfo")
        self.gridLayout_2.addWidget(self.nodeInfo, 2, 0, 1, 3)

        self.nodeName = SubtitleLabel(self.nodeWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nodeName.sizePolicy().hasHeightForWidth())
        self.nodeName.setSizePolicy(sizePolicy)
        self.nodeName.setObjectName("nodeName")
        self.gridLayout_2.addWidget(self.nodeName, 0, 1, 1, 1)

        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)

        self.tagWidget = QWidget(self.nodeWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tagWidget.sizePolicy().hasHeightForWidth())
        self.tagWidget.setSizePolicy(sizePolicy)
        self.tagWidget.setObjectName("tagWidget")
        self.gridLayout_2.addWidget(self.tagWidget, 1, 0, 1, 3)

        self.gridLayout.addWidget(self.nodeWidget, 0, 0, 1, 1)

        self.tagFlowLayout = FlowLayout(self.tagWidget, needAni=False)

        # self.SubtitleLabel.setText("[节点名称]")
        # self.id.setText("#")
        # self.nodeInfo.setText("[详情]")

    def addNodeTag(
        self,
        type: int,
        protoType: Optional[str] = "",
        bandWidth: Optional[list] = [],
    ):
        """
        type:\n
        0 - BandWidth, but argument 'bandwidth' is required, like ['100', '1.0'].\n
        1 - Full.\n
        2 - AllowProtocol, but argument 'protoType' is required, like 'TCP'.\n
        3 - VIP.
        """
        if not type:
            self.tagFlowLayout.addWidget(InfoBadge.info(f"{bandWidth[0]}Mbps × {bandWidth[1]}"))
        elif type == 3:
            self.tagFlowLayout.addWidget(InfoBadge.warning("VIP"))
        elif type == 2:
            self.tagFlowLayout.addWidget(InfoBadge.attension(protoType))
        elif type == 1:
            self.tagFlowLayout.addWidget(InfoBadge.error("! 满载"))
