from os import path as ospath
from json import dumps, loads
from MCSL2Lib.singleton import Singleton

ofConfigTemplate = {
    "bypass_system_proxy": True,
    "fprc_force_tls": False,
    "frpc_debug_mode": False,
    "last_user": "",
    "last_password": "",
}


def initOFPluginConfiguration():
    if not ospath.exists(r"./Plugins/OpenFRP_Plugin/MCSL2_OpenFrpPluginConfig.json"):
        with open(
            "./Plugins/OpenFRP_Plugin/MCSL2_OpenFrpPluginConfig.json",
            "w+",
            encoding="utf-8",
        ) as newConfig:
            newConfig.write(dumps(ofConfigTemplate, indent=4))
        print(1111)
    OFSettingsController().readSettings()


@Singleton
class OFSettingsController:
    def __init__(self):
        self.fileSettings = {}

    def readSettings(self):
        """重新将文件中的配置强制覆盖到程序中，不管是否保存了"""
        if ospath.exists(r"./Plugins/OpenFRP_Plugin/MCSL2_OpenFrpPluginConfig.json"):
            if (
                ospath.getsize(
                    r"./Plugins/OpenFRP_Plugin/MCSL2_OpenFrpPluginConfig.json"
                )
                != 0
            ):
                with open(
                    r"./Plugins/OpenFRP_Plugin/MCSL2_OpenFrpPluginConfig.json",
                    "r",
                    encoding="utf-8",
                ) as readConfig:
                    self.fileSettings = loads(readConfig.read())

    def changeSettings(self, setting: dict):
        """改设置并且直接保存"""
        self.fileSettings.update(setting)
        with open(
            r"./Plugins/OpenFRP_Plugin/MCSL2_OpenFrpPluginConfig.json",
            "w+",
            encoding="utf-8",
        ) as writeConfig:
            writeConfig.write(dumps(self.fileSettings, indent=4))
