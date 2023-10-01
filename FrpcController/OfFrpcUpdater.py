from MCSL2Lib.Controllers.networkController import Session
from ..OfSettingsController import OfSettingsController, initOFPluginConfiguration
from PyQt5.QtCore import QThread, pyqtSignal
from os import makedirs

ofSettingsController = OfSettingsController()


class FrpcVersion:
    def __init__(self, ver: str):
        ver = ver.split(".")
        self.v1 = ver[0]
        self.v2 = ver[1]
        self.v3 = ver[2]


class OfFrpcUpdater(QThread):
    updateInfo = pyqtSignal(list)

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
        info = Session().get(url=self.updateAPI).json()["data"]
        onlineVer = FrpcVersion(info["latest_ver"])
        if self.oldVer is not None:
            if self.cmp(oldVer=self.oldVer, newVer=onlineVer):
                self.updateInfo.emit([info["latest"], info["source"]])
                ofSettingsController.changeSettings(
                    {"frpc_version": str(info["latest_ver"])}
                )
        else:
            ofSettingsController.changeSettings(
                {"frpc_version": str(info["latest_ver"])}
            )
            self.updateInfo.emit([info["latest"], info["source"]])

    def cmp(self, oldVer: FrpcVersion, newVer: FrpcVersion):
        return (
            True
            if newVer.v1 > oldVer.v1 or newVer.v2 > oldVer.v2 or newVer.v3 > oldVer.v3
            else False
        )
