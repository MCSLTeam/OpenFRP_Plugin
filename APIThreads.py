from PyQt5.QtCore import QThread
from .OpenFrpLib import *
from .variables import OFVariables


class LoginThread(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("LoginThread")

    def run(self):
        try:
            OFVariables.loginData = login(
                user=OFVariables.userName, password=OFVariables.userPassword
            )
        except Exception:
            OFVariables.loginData = ["", "", False, "失败"]


class GetUserInfoThread(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("GetUserInfoThread")

    def run(self):
        try:
            OFVariables.userInfo = getUserInfo(
                Authorization=OFVariables.userAuthorization,
                session=OFVariables.userSessionID,
            )
        except Exception:
            OFVariables.userInfo = [{}, False, "失败"]


class GetNodeListThread(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("GetNodeListThread")

    def run(self):
        try:
            OFVariables.nodeListData = getNodeList(
                Authorization=OFVariables.userAuthorization,
                session=OFVariables.userSessionID,
            )
            for i in range(1, OFVariables.nodeListData[0]['total']):
                OFVariables.nodeListData[0]['list'][i]['group'] = list(OFVariables.nodeListData[0]['list'][i]['group'].split(";"))
        except Exception:
            OFVariables.nodeListData = [{}, False, "失败"]
