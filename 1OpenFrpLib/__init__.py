# -*- coding:utf-8 -*-
"""
OpenFrpLib is a Python module that helps developers use OpenFrp OPENAPI easily.
YOU ARE NOT ALLOWED TO USE THIS MODULE TO DO THINGS THAT VIOLATE OPENFRP'S TERMS OF USE.
See https://github.com/ZGIT-Network/OPENFRP-APIDOC for the API document.
Copyright (c) 2023 LxHTT
"""
from .NetworkController import BYPASS_SYSTEM_PROXY
from .Account import login, getUserInfo, userSign
from .Proxies import getUserProxies, newProxy, editProxy, removeProxy, getNodeList

__version__ = "1.1.1"