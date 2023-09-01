class OFVariables:
    ofPluginVersion = "1.0.0"
    userSessionID: str = ""
    userAuthorization: str = ""
    userInfo = {}
    nodeListData = []
    loginData = []
    newProxyData = []
    userName: str = ""
    userPassword: str = ""
    configuringNodeIndex = None
    configuringNodeMinPort: int = 0
    configuringNodeMaxPort: int = 0
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


def variablesLogout():
    OFVariables.userSessionID: str = ""
    OFVariables.userAuthorization: str = ""
    OFVariables.userName: str = ""
    OFVariables.userPassword: str = ""
    OFVariables.userInfo = []


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