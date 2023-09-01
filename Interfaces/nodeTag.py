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
        self.setMinimumSize(QSize(120, 25))
        self.setMaximumSize(QSize(16777215, 25))
        self.setStyleSheet(
            "BodyLabel {\n"
            "    background-color: rgba(223, 239, 232, 80%);\n"
            "    color: rgb(24, 160, 88);\n"
            "    border-radius: 3px;\n"
            "    padding-left: 3px solid rgba(223, 239, 232, 80%);\n"
            "    padding-right: 3px solid rgba(223, 239, 232, 80%);\n"
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
            "    background-color: rgba(246, 230, 234, 80%);\n"
            "    color: rgb(213, 71, 99);\n"
            "    border-radius: 3px;\n"
            "    padding-left: 2px solid rgba(246, 230, 234, 80%);\n"
            "    padding-right: 2px solid rgba(246, 230, 234, 80%);\n"
            "}"
        )
        self.setAlignment(Qt.AlignCenter)
        self.setText("! 满载")


class AllowProtocolTag(BodyLabel):
    def __init__(self):
        super().__init__()
        self.allowUDPTag = BodyLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QSize(75, 25))
        self.setMaximumSize(QSize(170, 25))
        self.setStyleSheet(
            "BodyLabel {\n"
            "    background-color: rgba(224, 236, 250, 80%);\n"
            "    color: rgb(32, 128, 241);\n"
            "    border-radius: 3px;\n"
            "    padding: 0px;\n"
            "}"
        )
        self.setAlignment(Qt.AlignCenter)

    def selfSetText(self, text):
        self.setText(f"√ {text}")


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
            "    background-color: rgba(249, 237, 219, 80%);\n"
            "    color: rgb(240, 160, 117);\n"
            "    border-radius: 3px;\n"
            "    padding-left: 2px solid rgba(249, 237, 219, 80%);\n"
            "    padding-right: 2px solid rgba(249, 237, 219, 80%);\n"
            "}"
        )
        self.setAlignment(Qt.AlignCenter)
        self.setText("VIP")
