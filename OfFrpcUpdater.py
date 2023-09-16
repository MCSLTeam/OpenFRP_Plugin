from MCSL2Lib.Controllers.networkController import Session
from .OfSettingsController import OfSettingsController
from random import randint
ofSettingsController = OfSettingsController()

class FrpcVersion:
    def __init__(self, ver: str):
        ver = ver.split(".")
        self.v1 = ver[0]
        self.v2 = ver[1]
        self.v3 = ver[2]


class OfFrpcUpdater:
    def __init__(self):
        self.updateAPI = "https://of-dev-api.bfsea.xyz/commonQuery/get?key=software"
        self.oldVer = FrpcVersion(ofSettingsController.fileSettings["frpc_version"]) if not ofSettingsController.fileSettings["frpc_version"] == "" else None

    def getUpdateInfo(self):
        info = Session.get(self.updateAPI).json()  # type: dict
        onlineVer = FrpcVersion(info["latest_ver"])
        if self.oldVer is not None:
            stat = self.cmp(oldVer=self.oldVer, newVer=onlineVer)
        if stat:
            self.downloadFrpc(latest=info["latest"], source=info["source"], soft_win=info["soft"][2])


    def cmp(self, oldVer: FrpcVersion, newVer: FrpcVersion):
        return (
            True
            if newVer.v1 > oldVer.v1 or newVer.v2 > oldVer.v2 or newVer.v3 > oldVer.v3
            else False
        )

    def downloadFrpc(self, latest, source, soft_win):
        downloadURL = f"{source[randint(0, len(source)-1)]}{latest}{soft_win}"