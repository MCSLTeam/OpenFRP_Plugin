from typing import List

from MCSL2Lib.singleton import Singleton
from .OfFrpcProcessController import FrpcHandler, FrpcProcess
from ..variables import OFVariables
from PyQt5.QtCore import QObject

@Singleton
class FrpcBridge(QObject):
    def __init__(self, parent):
        super().__init__(parent)
        self.processList: List[str, FrpcProcess] = ["PlaceHolder"]
        self.handlerList = ["PlaceHolder"]
        self.totalLogList: List[str] = []
        self.singleLogList: List[List[str], str] = ["PlaceHolder"]

    def newFrpc(self, tunnelId: str) -> int:
        frpcProcessListId = len(self.processList)
        self.singleLogList.append([])

        frpcHandler = FrpcHandler()
        frpcHandler.frpcLogOutput.connect(self.totalLogList.append)
        frpcHandler.frpcLogOutput.connect(self.singleLogList[frpcProcessListId].append)
        # frpcHandler.frpcClosed.connect
        # frpcHandler.frpcRestarted.connect

        self.handlerList.append(frpcHandler)
        self.processList.append(
            frpcHandler.startFrpc(OFVariables.userInfo[0]["token"], tunnelId)
        )

        return frpcProcessListId

    def stopFrpc(self, frpcProcessListId: int):
        self.handlerList[frpcProcessListId].stopFrpc()
        self.handlerList.pop(frpcProcessListId)
        self.processList.pop(frpcProcessListId)
