from qfluentwidgets import BodyLabel
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QSizePolicy


class BandWidthTag(BodyLabel):
    def __init__(self):
        super().__init__()
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(0, 25))
        self.setMaximumSize(QSize(16777215, 25))
        self.setStyleSheet(
            "BodyLabel {\n"
            "    background-color: rgb(223, 239, 232);\n"
            "    color: rgb(24, 160, 88);\n"
            "    padding-left: 5px;\n"
            "    padding-right: 5px;\n"
            "    padding-top: 3px;\n"
            "    padding-bottom: 5px;\n"
            "    border-radius: 12px;\n"
            "}"
        )
        self.setAlignment(Qt.AlignCenter)


class FullTag(BodyLabel):
    def __init__(self):
        super().__init__()
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setFixedSize(QSize(60, 25))
        self.setStyleSheet(
            "BodyLabel {\n"
            "    background-color: rgb(246, 230, 234);\n"
            "    color: rgb(213, 71, 99);\n"
            "    padding-left: 5px;\n"
            "    padding-right: 5px;\n"
            "    padding-top: 3px;\n"
            "    padding-bottom: 5px;\n"
            "    border-radius: 12px;\n"
            "}"
        )
        self.setAlignment(Qt.AlignCenter)


class AllowProtocolTag(BodyLabel):
    def __init__(self):
        super().__init__()
        self.allowUDPTag = BodyLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setFixedSize(QSize(60, 25))
        self.setStyleSheet(
            "BodyLabel {\n"
            "    background-color: rgb(224, 236, 250);\n"
            "    color: rgb(32, 128, 241);\n"
            "    padding-left: 5px;\n"
            "    padding-right: 5px;\n"
            "    padding-top: 3px;\n"
            "    padding-bottom: 5px;\n"
            "    border-radius: 12px;\n"
            "}"
        )
        self.setAlignment(Qt.AlignCenter)


class VIPTag(BodyLabel):
    def __init__(self):
        super().__init__()
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setFixedSize(QSize(50, 25))
        self.setStyleSheet(
            "BodyLabel {\n"
            "    background-color: rgb(249, 237, 219);\n"
            "    color: rgb(240, 160, 117);\n"
            "    padding-left: 5px;\n"
            "    padding-right: 5px;\n"
            "    padding-top: 3px;\n"
            "    padding-bottom: 5px;\n"
            "    border-radius: 12px;\n"
            "}"
        )
        self.setAlignment(Qt.AlignCenter)
