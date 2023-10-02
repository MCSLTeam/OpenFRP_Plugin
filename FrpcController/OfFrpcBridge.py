from MCSL2Lib.singleton import Singleton
from ..Interfaces.frpcConsole import OpenFrpFrpcConsoleUI
from .OfFrpcProcessController import FrpcHandler
from ..variables import FrpcConsoleVariables, OFVariables
from PyQt5.QtCore import QObject

@Singleton
class FrpcBridge(QObject):
    def __init__(self, parent):
        super().__init__(parent)

    def newFrpc(self, proxyName: str, tunnelId: str) -> int:
        frpcConsole = OpenFrpFrpcConsoleUI()
        frpcHandler = FrpcHandler()
        frpcProcessListId = len(FrpcConsoleVariables.processList)
        frpcConsole.frpcClientComboBox.addItem(f"#{tunnelId} {proxyName}")
        FrpcConsoleVariables.singleLogList.append([])

        frpcHandler.frpcLogOutput.connect(FrpcConsoleVariables.totalLogList.append)
        frpcHandler.frpcLogOutput.connect(frpcConsole.colorConsoleText)
        frpcHandler.frpcLogOutput.connect(FrpcConsoleVariables.singleLogList[frpcProcessListId].append)

        FrpcConsoleVariables.handlerList.append(frpcHandler)
        FrpcConsoleVariables.processList.append(
            frpcHandler.startFrpc(OFVariables.userInfo[0]["token"], tunnelId)
        )
        return frpcProcessListId

    def stopFrpc(self, frpcProcessListId: int):
        FrpcConsoleVariables.handlerList[frpcProcessListId].stopFrpc()
        FrpcConsoleVariables.handlerList.pop(frpcProcessListId)
        FrpcConsoleVariables.processList.pop(frpcProcessListId)
        frpcConsole = OpenFrpFrpcConsoleUI()
        frpcConsole.frpcClientComboBox.removeItem(frpcProcessListId)