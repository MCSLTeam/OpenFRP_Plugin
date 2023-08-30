class OFVariables:
    ofPluginVersion = "1.0.0"
    userSessionID: str = ""
    userAuthorization: str = ""
    userInfo = {}
    userName: str = ""
    userPassword: str = ""
    loginData = []

def variablesLogout():
    OFVariables.userSessionID: str = ""
    OFVariables.userAuthorization: str = ""
    OFVariables.userName: str = ""
    OFVariables.userPassword: str = ""
    OFVariables.userInfo.clear()