from MCSL2Lib.Controllers.aria2ClientController import Aria2Controller
from MCSL2Lib.Controllers.networkController import Session
from MCSL2Lib.windowInterface import Window
from .Interfaces.OfInterface import OpenFrpMainUI
from .OfSettingsController import OfSettingsController, initOFPluginConfiguration
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

ofInterface = OpenFrpMainUI()
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
        self.updateAPI = "https://of-dev-api.bfsea.xyz/commonQuery/get?key=software"
        self.oldVer = None

    def setUpFrpcEnv(self):
        makedirs(r"./Plugins/OpenFRP_Plugin/frpc", exist_ok=True)
        initOFPluginConfiguration()
        if ofSettingsController.fileSettings["frpc_version"] == "":
            self.oldVer = None
        else:
            self.oldVer = FrpcVersion(ofSettingsController.fileSettings["frpc_version"])

    def run(self):
        self.getUpdateInfo()

    def getUpdateInfo(self):
        info = Session().get(url=self.updateAPI).json()["data"]
        onlineVer = FrpcVersion(info["latest_ver"])
        if self.oldVer is not None:
            if self.cmp(oldVer=self.oldVer, newVer=onlineVer):
                self.downloadFrpc(
                    latest=info["latest"],
                    source=info["source"],
                    soft_win="frpc_windows_386.zip",
                )
                OfSettingsController.changeSettings(
                    {"frpc_version": info["latest_ver"]}
                )
        else:
            self.downloadFrpc(
                latest=info["latest"],
                source=info["source"],
                soft_win="frpc_windows_386.zip",
            )

    def cmp(self, oldVer: FrpcVersion, newVer: FrpcVersion):
        return (
            True
            if newVer.v1 > oldVer.v1 or newVer.v2 > oldVer.v2 or newVer.v3 > oldVer.v3
            else False
        )



    def downloadFrpc(self, latest, source, soft_win):
        if not Aria2Controller.testAria2Service():
            if not Aria2Controller.startAria2():
                box = MessageBox(
                    title="无法下载Frpc",
                    content="MCSL2的Aria2可能未安装或启动失败。",
                    parent=self.parent(),
                )
                box.exec()
                return
        Window().switchTo(self.parent())
        uri = f"{source[randint(0, len(source)-3)]['value']}{latest}{soft_win}"
        gid = Aria2Controller.download(
            uri=uri,
            watch=True,
            info_get=self.downloadBox.onInfoGet,
            stopped=self.extract,
            interval=0.2,
        )
        self.downloadBox = ofInterface.callDownloadMsgBox(
            soft_win,
            aria2Cancel=Aria2Controller.cancelDownloadTask(gid),
            aria2Pause=Aria2Controller.pauseDownloadTask(gid),
            aria2Resume=Aria2Controller.resumeDownloadTask(gid),
        )

    def extract(self):
        print(111231)
        try:
            frpcArchive = ZipFile("MCSL2/Downloads/frpc_windows_386.zip", "r")
            frpcArchive.extractall("./Plugins/OpenFRP_Plugin/frpc")
            frpcArchive.close()
            remove("MCSL2/Downloads/frpc_windows_386.zip")
            ofInterface.downloadFinishedHelper()
        except:
            ofInterface.downloadFailedHelper()