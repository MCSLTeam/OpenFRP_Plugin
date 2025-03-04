from PyQt5.QtCore import QThread
from .OpenFrpLib.OpenFrpLib import (
    login,
    getUserInfo,
    getNodeList,
    newProxy,
    getUserProxies,
    removeProxy,
)
from .variables import OFVariables


class LoginThread(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("LoginThread")

    def run(self):
        OFVariables.loginData = login()
        print(OFVariables.loginData)


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
            for i in range(1, OFVariables.nodeListData[0]["total"]):
                OFVariables.nodeListData[0]["list"][i]["group"] = list(
                    OFVariables.nodeListData[0]["list"][i]["group"].split(";")
                )
        except Exception:
            OFVariables.nodeListData = [{}, False, "失败"]


class NewProxyThread(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("NewProxyThread")

    def run(self):
        try:
            OFVariables.newProxyData = newProxy(
                Authorization=OFVariables.userAuthorization,
                session=OFVariables.userSessionID,
                node_id=OFVariables.configuringNodeID,
                type=OFVariables.configuringProxyType,
                remote_port=OFVariables.configuringProxyRemotePort,
                local_addr=OFVariables.configuringProxyLocalAddr,
                local_port=OFVariables.configuringProxyLocalPort,
                domain_bind=OFVariables.configuringProxyDomainBind,
                host_rewrite=OFVariables.configuringProxyHostRewrite,
                request_from=OFVariables.configuringProxyRequestFrom,
                custom=OFVariables.configuringProxyCustom,
                dataGzip=OFVariables.configuringProxyDataGZip,
                dataEncrypt=OFVariables.configuringProxyDataEncrypt,
                url_route=OFVariables.configuringProxyURLRoute,
                name=OFVariables.configuringProxyName,
                request_pass=OFVariables.configuringRequestPass,
            )
        except Exception:
            OFVariables.newProxyData = [None, False, "创建失败"]


class GetUserProxiesThread(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("GetUserProxiesThread")

    def run(self):
        try:
            OFVariables.userProxiesData = getUserProxies(
                Authorization=OFVariables.userAuthorization,
                session=OFVariables.userSessionID,
            )
        except Exception:
            OFVariables.userProxiesData = [0, [], False, "失败"]


class RemoveProxyThread(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("RemoveProxyThread")

    def run(self):
        try:
            OFVariables.removeProxyData = removeProxy(
                Authorization=OFVariables.userAuthorization,
                session=OFVariables.userSessionID,
                proxy_id=OFVariables.removeProxyID,
            )
        except Exception:
            OFVariables.removeProxyData = [None, False, "失败"]
