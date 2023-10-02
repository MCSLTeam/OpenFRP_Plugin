class OFVariables:
    ofPluginVersion = "1.0.0"
    userSessionID: str = ""
    userAuthorization: str = ""
    userInfo = {}
    nodeListData = []
    loginData = []
    newProxyData = []
    userProxiesData = []
    userName: str = ""
    userPassword: str = ""
    configuringNodeIndex = None
    configuringNodeMinPort: int = 1
    configuringNodeMaxPort: int = 65535
    configuringNodeID: int = 0
    configuringProxyName: str = ""
    configuringProxyType: str = ""
    configuringProxyLocalAddr: str = ""
    configuringProxyDomainBind: str = ""
    configuringProxyHostRewrite: str = ""
    configuringProxyRequestFrom: str = ""
    configuringProxyCustom: str = ""
    configuringProxyURLRoute: str = ""
    configuringRequestPass: str = ""
    configuringProxyLocalPort: int = 0
    configuringProxyRemotePort: int = 0
    configuringProxyDataEncrypt: bool = False
    configuringProxyDataGZip: bool = False
    removeProxyID: int = 0
    removeProxyData = []


class FrpcConsoleVariables:
    processList = ["PlaceHolder"]
    handlerList = ["PlaceHolder"]
    totalLogList = []
    singleLogList = ["PlaceHolder"]


def variablesLogout():
    OFVariables.userSessionID: str = ""
    OFVariables.userAuthorization: str = ""
    OFVariables.userName: str = ""
    OFVariables.userPassword: str = ""
    OFVariables.userInfo = {}


def clearNewProxyConfig():
    OFVariables.configuringNodeIndex = None
    OFVariables.configuringNodeMinPort: int = 0
    OFVariables.configuringNodeMaxPort: int = 0
    OFVariables.configuringNodeID: int = 0
    OFVariables.configuringProxyName: str = ""
    OFVariables.configuringProxyType: str = ""
    OFVariables.configuringProxyLocalAddr: str = ""
    OFVariables.configuringProxyDomainBind: str = ""
    OFVariables.configuringProxyHostRewrite: str = ""
    OFVariables.configuringProxyRequestFrom: str = ""
    OFVariables.configuringProxyCustom: str = ""
    OFVariables.configuringProxyURLRoute: str = ""
    OFVariables.configuringRequestPass: str = ""
    OFVariables.configuringProxyLocalPort: int = 0
    OFVariables.configuringProxyRemotePort: int = 0
    OFVariables.configuringProxyDataEncrypt: bool = False
    OFVariables.configuringProxyDataGZip: bool = False
    OFVariables.newProxyData = []


def clearUserProxiesData():
    OFVariables.userProxiesData = []


def clearRemoveProxyID():
    OFVariables.removeProxyID: int = 0
    OFVariables.removeProxyData = []
