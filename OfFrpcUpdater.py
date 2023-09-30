from MCSL2Lib.Controllers.aria2ClientController import Aria2Controller
from MCSL2Lib.Controllers.networkController import Session
from MCSL2Lib.Widgets.DownloadProgressWidget import DownloadMessageBox
from .OFSettingsController import OfSettingsController
from qfluentwidgets import (
    MessageBox,
    InfoBar,
    InfoBarPosition,
    PushButton,
    FluentIcon as FIF,
)
from PyQt5.QtCore import Qt, QThread
from random import randint
from zipfile import ZipFile
from os import remove, makedirs
ofSettingsController = OfSettingsController()


class FrpcVersion:
    def __init__(self, ver: str):
        ver = ver.split(".")
        self.v1 = ver[0]
        self.v2 = ver[1]
        self.v3 = ver[2]


class OfFrpcUpdater(QThread):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.updateAPI = "https://of-dev-api.bfsea.xyz/commonQuery/get?key=software"
        self.oldVer = (
            None
            if ofSettingsController.fileSettings["frpc_version"] == ""
            else FrpcVersion(ofSettingsController.fileSettings["frpc_version"])
        )

    def setUpFrpcEnv(self):
        makedirs(r"./Plugins/OpenFRP_Plugin/frpc", exist_ok=True)

    def run(self):
        self.getUpdateInfo()

    def getUpdateInfo(self):
        info = Session().get(url=self.updateAPI).json()
        onlineVer = FrpcVersion(info["latest_ver"])
        if self.oldVer is not None:
            if self.cmp(oldVer=self.oldVer, newVer=onlineVer):
                self.downloadFrpc(
                    latest=info["latest"], source=info["source"], soft_win="frpc_windows_386.zip"
                )
                OfSettingsController.changeSettings({"frpc_version": info["latest_ver"]})

    def cmp(self, oldVer: FrpcVersion, newVer: FrpcVersion):
        return (
            True
            if newVer.v1 > oldVer.v1 or newVer.v2 > oldVer.v2 or newVer.v3 > oldVer.v3
            else False
        )

    def hideDownloadHelper(self):
        self.downloadingInfoBar = InfoBar(
            icon=FIF.DOWNLOAD,
            title="已隐藏下载窗口",
            content="仍在下载中，点击按钮恢复下载窗口...",
            orient=Qt.Horizontal,
            isClosable=False,
            duration=-1,
            position=InfoBarPosition.TOP_RIGHT,
            parent=self.parent,
        )
        self.downloadingInfoBar.setCustomBackgroundColor("white", "#202020")
        showDownloadMsgBoxBtn = PushButton()
        showDownloadMsgBoxBtn.setText("恢复")
        showDownloadMsgBoxBtn.clicked.connect(self.downloadingBox.show)
        showDownloadMsgBoxBtn.clicked.connect(self.downloadingInfoBar.close)
        self.downloadingInfoBar.addWidget(showDownloadMsgBoxBtn)
        self.downloadingInfoBar.show()

    def downloadFinishedHelper(self):
        try:
            self.downloadingInfoBar.close()
            InfoBar.success("下载完毕")
        except:
            pass

    def downloadFrpc(self, latest, source, soft_win):
        if not Aria2Controller.testAria2Service():
            if not Aria2Controller.startAria2():
                box = MessageBox(title="无法下载Frpc", content="MCSL2的Aria2可能未安装或启动失败。", parent=self.parent)
                box.exec()
                return
        self.downloadingBox = DownloadMessageBox(soft_win, parent=self)
        self.downloadingBox.DownloadWidget().closeBoxBtnFinished.clicked.connect(
            self.downloadingBox.close
        )
        self.downloadingBox.DownloadWidget().closeBoxBtnFailed.clicked.connect(
            self.downloadingBox.close
        )
        uri = f"{source[randint(0, len(source)-1)]}{latest}{soft_win}"
        gid = Aria2Controller.download(
            uri=uri,
            watch=True,
            info_get=self.downloadingBox.onInfoGet,
            stopped=self.extract(f"MCSL2/Downloads/{soft_win}"),
            interval=0.2,
        )
        print(uri)
        self.downloadingBox.canceled.connect(
            lambda: Aria2Controller.cancelDownloadTask(gid)
        )
        self.downloadingBox.paused.connect(
            lambda x: Aria2Controller.pauseDownloadTask(gid)
            if x
            else Aria2Controller.resumeDownloadTask(gid)
        )
        self.downloadingBox.show()

    def extract(self, file):
        frpcArchive = ZipFile(file, "r")
        frpcArchive.extractall("./Plugins/OpenFRP_Plugin/frpc")
        frpcArchive.close()
        remove(file)