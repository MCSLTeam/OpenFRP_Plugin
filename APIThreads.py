from PyQt5.QtCore import QThread, pyqtSignal
from OpenFrpLib import *
from .variables import OFVariables


class LoginThread(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("LoginThread")

    def run(self):
        try:
            OFVariables.loginData = login(user=OFVariables.userName, password=OFVariables.userPassword)
        except Exception:
            OFVariables.loginData = ["", "", False, "失败"]

class GetUserInfoThread(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("GetUserInfoThread")

    def run(self):
        try:
            OFVariables.userInfo = getUserInfo(Authorization=OFVariables.userAuthorization, session=OFVariables.userSessionID)
        except Exception:
            OFVariables.userInfo = [ {}, False, "失败"]