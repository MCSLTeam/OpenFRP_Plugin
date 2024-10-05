from PyQt5.QtWidgets import (
    QGridLayout,
    QSizePolicy,
    QFrame,
    QSpacerItem,
    QWidget,
    QApplication,
    QFileDialog,
)
from qfluentwidgets import (
    ComboBox,
    PlainTextEdit,
    TitleLabel,
    TransparentPushButton,
    PushButton,
    FluentIcon as FIF,
    InfoBarPosition,
    InfoBar,
)
import re
from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QColor, QTextCharFormat
from os import getcwd
from MCSL2Lib.singleton import Singleton
from MCSL2Lib.utils import openLocalFile
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
        sizePolicy.setHeightForWidth(self.clearFrpcConsoleBtn.sizePolicy().hasHeightForWidth())
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
        sizePolicy.setHeightForWidth(self.saveFrpcConsoleBtn.sizePolicy().hasHeightForWidth())
        self.saveFrpcConsoleBtn.setSizePolicy(sizePolicy)
        self.saveFrpcConsoleBtn.setObjectName("saveFrpcConsoleBtn")

        self.gridLayout.addWidget(self.saveFrpcConsoleBtn, 2, 2, 1, 1)

        self.clearFrpcConsoleBtn.setText("清空")
        self.titleLabel.setText("OpenFrp Frpc 终端")
        self.saveFrpcConsoleBtn.setText("保存")
        self.clearFrpcConsoleBtn.clicked.connect(self.clearFrpcLog)
        self.saveFrpcConsoleBtn.clicked.connect(self.saveFrpcLog)
        self.frpcClientComboBox.addItem("#0 全部日志")
        self.frpcClientComboBox.currentIndexChanged.connect(self.switchFrpcLog)

    @pyqtSlot(str)
    def colorConsoleText(self, frpcLogOutput: str):
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
        self.frpcOutput.appendPlainText(frpcLogOutput[:-1].replace("[0m", "").replace("[1;34m", "").replace("[1;31m", "").replace("[1;33m", ""))
        if "启动成功, 请使用" in frpcLogOutput:
            url = (
                frpcLogOutput[:-1]
                .split("启动成功, 请使用 [")[1]
                .split("] 来连接服务, 或使用IP地址")[0]
            )
            i = InfoBar.success(
                title="完成",
                content=f"{(k := frpcLogOutput.split(', 请使用 [')[0].split('] '))[3]}] {k[4]}] 启动成功",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP,
                duration=8000,
                parent=self.window(),
            )
            finishBtn = PushButton(icon=FIF.COPY, text="复制链接地址", parent=i)
            finishBtn.clicked.connect(lambda: QApplication.clipboard().setText(url))
            i.addWidget(finishBtn)

    def switchFrpcLog(self):
        if not self.sender().currentIndex():
            self.frpcOutput.setPlainText("".join(FrpcConsoleVariables.totalLogList))
        else:
            self.frpcOutput.setPlainText(
                "".join(FrpcConsoleVariables.singleLogList[self.sender().currentIndex()])
            )

    def clearFrpcLog(self):
        self.frpcOutput.clear()
        if not self.frpcClientComboBox.currentIndex():
            FrpcConsoleVariables.totalLogList = []
        else:
            FrpcConsoleVariables.singleLogList[self.frpcClientComboBox.currentIndex()] = []

    def saveFrpcLog(self):
        saveLogFileDialog = QFileDialog(self, "MCSL2 - 保存OpenFrp Frpc日志", getcwd())
        saveLogFileDialog.setAcceptMode(QFileDialog.AcceptSave)
        saveLogFileDialog.setNameFilter("Log Files (*.log);;Text Files (*.txt)")
        saveLogFileDialog.selectFile("MCSL2_OpenFRP_Plugin_Frpc.log")
        if saveLogFileDialog.exec_() == QFileDialog.Accepted:
            try:
                with open(saveLogFileDialog.selectedFiles()[0], "w+", encoding="utf-8") as f:
                    f.write(self.frpcOutput.toPlainText())
                finishBtn = PushButton(icon=FIF.LINK, text="打开文件", parent=self)
                finishBtn.clicked.connect(
                    lambda: openLocalFile(saveLogFileDialog.selectedFiles()[0])
                )
                i = InfoBar.success(
                    title="成功",
                    content=f"日志已保存至 {saveLogFileDialog.selectedFiles()[0]}",
                    isClosable=True,
                    position=InfoBarPosition.TOP,
                    duration=5000,
                    parent=self.window(),
                )
                i.addWidget(finishBtn)
            except Exception as e:
                InfoBar.error(
                    title="保存日志失败",
                    content=e,
                    isClosable=True,
                    position=InfoBarPosition.TOP,
                    duration=5000,
                    parent=self.window(),
                )
        else:
            return
