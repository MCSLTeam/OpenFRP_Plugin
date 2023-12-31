from MCSL2Lib.ProgramControllers.networkController import MCSLNetworkSession
from ..OfSettingsController import OfSettingsController, initOFPluginConfiguration
from PyQt5.QtCore import QThread, pyqtSignal, QProcess
from os import makedirs, listdir, path as osp

ofSettingsController = OfSettingsController()


class FrpcVersion:
    def __init__(self, ver: str) -> None:
        ver = ver.split(".")
        self.v1 = ver[0]
        self.v2 = ver[1]
        self.v3 = ver[2]

    @classmethod
    def getFrpcProgramVersion(cls) -> str:
        if not osp.exists("./Plugins/OpenFRP_Plugin/frpc/frpc.exe"):
            return None
        else:
            frpc = QProcess()
            frpc.setProgram("./Plugins/OpenFRP_Plugin/frpc/frpc.exe")
            frpc.setArguments(["-v"])
            frpc.setWorkingDirectory("./Plugins/OpenFRP_Plugin/frpc")
            frpc.start()
            frpc.waitForFinished()
            return FrpcVersion(frpc.readAll().data().decode("utf-8").split("_")[1])


class OfFrpcUpdater(QThread):
    updateInfo = pyqtSignal(list)

    def __init__(self, parent):
        super().__init__(parent)
        self.updateAPI = "https://of-dev-api.bfsea.xyz/commonQuery/get?key=software"
        self.oldVer: str

    def setUpFrpcEnv(self) -> None:
        makedirs(r"./Plugins/OpenFRP_Plugin/frpc", exist_ok=True)
        initOFPluginConfiguration()
        self.oldVer = FrpcVersion.getFrpcProgramVersion()

    def run(self):
        info = MCSLNetworkSession().get(url=self.updateAPI).json()["data"]
        onlineVer = FrpcVersion(info["latest_ver"])
        if self.oldVer is not None:
            if self.cmp(oldVer=self.oldVer, newVer=onlineVer) or not len(
                listdir(r"./Plugins/OpenFRP_Plugin/frpc")
            ):
                self.updateInfo.emit([info["latest"], info["source"]])
        else:
            self.updateInfo.emit([info["latest"], info["source"]])

    def cmp(self, oldVer: FrpcVersion, newVer: FrpcVersion) -> bool:
        return (
            True
            if newVer.v1 > oldVer.v1 or newVer.v2 > oldVer.v2 or newVer.v3 > oldVer.v3
            else False
        )
