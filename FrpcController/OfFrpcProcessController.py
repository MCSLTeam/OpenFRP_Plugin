from os import getcwd
from typing import List, Optional
from PyQt5.QtCore import QProcess, QObject, pyqtSignal

from ..OfSettingsController import OfSettingsController

ofSettingsController = OfSettingsController()
processList = ["PlaceHolder"]
handlerList = ["PlaceHolder"]
totalLogList = []
singleProcessList = ["PlaceHolder"]

class FrpcProcess:
    """Frpc进程"""

    def __init__(self):
        self.frpcProcess: Optional[QProcess] = None
        self.LastOutputSize = 0


class FrpcHandler(QObject):
    """Frpc进程操控器"""

    # 当输出日志时发出的信号(发送一个字符串)
    frpcLogOutput = pyqtSignal(str)

    # 当关闭时发出的信号(发送一个整数exit code)
    frpcClosed = pyqtSignal(int)

    # 当重启时发出的信号
    frpcRestarted = pyqtSignal()

    def __init__(self):
        """
        初始化一个Frpc处理器
        """
        super().__init__()
        self.frpcProcessDir: str = (
            f"{getcwd()}\\Plugins\\OpenFRP_Plugin\\frpc\\frpc.exe"
        )
        self.cwd: str = f"{getcwd()}\\Plugins\\OpenFRP_Plugin\\frpc\\"
        self.partialData: str = b""
        self.AFrpc = None
        self.FrpcProcess = self.getFrpcProcess()

    def getFrpcProcess(self) -> FrpcProcess:
        """
        获取一个Frpc进程，但是并没有运行，只是创建了一个QProcess对象
        """
        self.AFrpc = FrpcProcess()
        self.AFrpc.frpcProcess = QProcess()
        self.AFrpc.frpcProcess.setProgram(self.frpcProcessDir)
        self.AFrpc.frpcProcess.setWorkingDirectory(self.cwd)
        # self.AFrpc.frpcProcess.started.connect(
        #     lambda: self.frpcLogOutput.emit("[MCSL2 | 提示]：服务器正在启动，请稍后...")
        # )
        self.AFrpc.frpcProcess.readyReadStandardOutput.connect(
            self.frpcLogOutputHandler
        )
        self.AFrpc.frpcProcess.finished.connect(
            lambda: self.frpcClosed.emit(self.AFrpc.frpcProcess.exitCode())
        )
        return self.AFrpc

    def frpcLogOutputHandler(self):
        """
        When the server outputs change, emit a signal with the updated output.
        """
        newData = self.FrpcProcess.frpcProcess.readAllStandardOutput().data()
        self.partialData += newData  # Append the incoming data to the buffer
        lines = self.partialData.split(b"\n")  # Split the buffer into lines
        self.partialData = (
            lines.pop()
        )  # The last element might be incomplete, so keep it in the buffer

        for line in lines:
            newOutput = line.decode("ansi", errors="replace")
            self.frpcLogOutput.emit(newOutput)

    def restartFrpc(self):
        """
        重启Frpc
        """
        self.killFrpc()
        self.FrpcProcess.frpcProcess.waitForFinished()
        self.FrpcProcess.frpcProcess.start()
        self.frpcRestarted.emit()

    def killFrpc(self):
        """
        强制停止Frpc
        """
        if self.isFrpcRunning():
            self.FrpcProcess.frpcProcess.kill()
            self.FrpcProcess.frpcProcess.waitForFinished()

    def isFrpcRunning(self):
        if self.FrpcProcess.frpcProcess is None:
            return False
        return self.FrpcProcess.frpcProcess.state() == QProcess.Running

    def startFrpc(self, userToken: str, tunnelId: str):
        """
        启动Frpc
        """
        self.FrpcProcess = self.getFrpcProcess()
        arg = ["-n", "-u", userToken, "-p", tunnelId]
        if ofSettingsController.fileSettings["fprc_force_tls"]:
            arg.append("--force_tls")
        if ofSettingsController.fileSettings["frpc_debug_mode"]:
            arg.append("--debug")
        self.FrpcProcess.frpcProcess.setArguments(arg)
        self.FrpcProcess.frpcProcess.start()
