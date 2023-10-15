from PyQt5.QtWidgets import QGridLayout, QSizePolicy, QFrame, QSpacerItem, QWidget
from qfluentwidgets import (
    ComboBox,
    PlainTextEdit,
    TitleLabel,
    TransparentPushButton,
    FluentIcon as FIF,
)
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QColor, QTextCharFormat

from MCSL2Lib.singleton import Singleton
from ..variables import FrpcConsoleVariables


@Singleton
class OpenFrpFrpcConsoleUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("OpenFrpFrpcConsoleUI")

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        spacerItem = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.clearFrpcConsoleBtn = TransparentPushButton(self)
        self.clearFrpcConsoleBtn.setIcon(FIF.DELETE)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.clearFrpcConsoleBtn.sizePolicy().hasHeightForWidth()
        )
        self.clearFrpcConsoleBtn.setSizePolicy(sizePolicy)
        self.clearFrpcConsoleBtn.setObjectName("clearFrpcConsoleBtn")

        self.gridLayout.addWidget(self.clearFrpcConsoleBtn, 2, 1, 1, 1)
        spacerItem1 = QSpacerItem(10, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 3, 1)
        self.frpcOutput = PlainTextEdit(self)
        self.frpcOutput.setFrameShape(QFrame.NoFrame)
        self.frpcOutput.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.frpcOutput.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.frpcOutput.setReadOnly(True)
        self.frpcOutput.setReadOnly(True)
        self.frpcOutput.setReadOnly(True)
        self.frpcOutput.setReadOnly(True)
        self.frpcOutput.setReadOnly(True)
        self.frpcOutput.setReadOnly(True)
        self.frpcOutput.setReadOnly(True)
        self.frpcOutput.setReadOnly(True)
        self.frpcOutput.setObjectName("frpcOutput")

        self.gridLayout.addWidget(self.frpcOutput, 3, 1, 1, 4)
        self.frpcClientComboBox = ComboBox(self)
        self.frpcClientComboBox.setObjectName("frpcClientComboBox")

        self.gridLayout.addWidget(self.frpcClientComboBox, 2, 3, 1, 1)
        self.titleLabel = TitleLabel(self)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        self.titleLabel.setObjectName("titleLabel")

        self.gridLayout.addWidget(self.titleLabel, 1, 1, 1, 3)
        spacerItem2 = QSpacerItem(5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 5, 3, 1)
        spacerItem3 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 4, 1, 1, 4)
        self.saveFrpcConsoleBtn = TransparentPushButton(self)
        self.saveFrpcConsoleBtn.setIcon(FIF.SAVE)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.saveFrpcConsoleBtn.sizePolicy().hasHeightForWidth()
        )
        self.saveFrpcConsoleBtn.setSizePolicy(sizePolicy)
        self.saveFrpcConsoleBtn.setObjectName("saveFrpcConsoleBtn")

        self.gridLayout.addWidget(self.saveFrpcConsoleBtn, 2, 2, 1, 1)

        self.clearFrpcConsoleBtn.setText("清空")
        self.titleLabel.setText("OpenFrp Frpc 终端")
        self.saveFrpcConsoleBtn.setText("保存")
        self.clearFrpcConsoleBtn.clicked.connect(self.frpcOutput.clear)
        self.saveFrpcConsoleBtn.setEnabled(False)
        self.frpcClientComboBox.addItem("#0 全部日志")
        self.frpcClientComboBox.currentIndexChanged.connect(self.switchFrpcLog)

    @pyqtSlot(str)
    def colorConsoleText(self, frpcLogOutput):
        fmt = QTextCharFormat()
        color = [
            QColor(52, 185, 96),
            QColor(196, 139, 33),
            QColor(214, 39, 21),
            QColor(22, 122, 232),
        ]
        if "[I]" in frpcLogOutput:
            fmt.setForeground(color[0])
        if "[W]" in frpcLogOutput:
            fmt.setForeground(color[1])
        if "[E]" in frpcLogOutput:
            fmt.setForeground(color[2])
        if "[D]" in frpcLogOutput:
            fmt.setForeground(color[3])
        self.frpcOutput.mergeCurrentCharFormat(fmt)
        self.frpcOutput.appendPlainText(frpcLogOutput[:-1])
        self.frpcOutput.setReadOnly(True)
        self.frpcOutput.setReadOnly(True)
        self.frpcOutput.setReadOnly(True)
        self.frpcOutput.setReadOnly(True)
        self.frpcOutput.setReadOnly(True)
        self.frpcOutput.setReadOnly(True)
        self.frpcOutput.setReadOnly(True)
        self.frpcOutput.setReadOnly(True)

    def switchFrpcLog(self):
        if not self.sender().currentIndex():
            self.frpcOutput.setPlainText("".join(FrpcConsoleVariables.totalLogList))
        else:
            self.frpcOutput.setPlainText("".join(FrpcConsoleVariables.singleLogList[self.sender().currentIndex()]))