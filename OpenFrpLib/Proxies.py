"""
Manage proxies
"""
from .NetworkController import post
from typing import Optional
from random import randint
APIURL = "https://of-dev-api.bfsea.xyz"


def getUserProxies(Authorization: str, session: str):
    r"""
    Get the list of a user's proxies.
    =
    Requirements:
    `Authorization` --> str: If you don't have one, use login() to get it.
    `session` --> str: If you don't have one, use login() to get it.

    Return: 
    `numOfProxies`, `proxiesList` --> list
        `numOfProxies` --> int: How many proxies the user have.  
        `proxiesList` --> list: The user's proxies.
    """

    # POST API
    _APIData = post(
        url=f"{APIURL}/frp/api/getUserProxies",
        json={
            "session": session
        },
        headers={'Content-Type': 'application/json',
                 'Authorization': Authorization}
    )

    _userProxies = _APIData.json()['data']
    numOfProxies = _userProxies['total']
    proxiesList = _userProxies['list']

    if not _APIData.ok:
        _APIData.raise_for_status()

    return numOfProxies, proxiesList


def newProxy(Authorization: str,
             session: str,
             node_id: int,
             type: str,
             remote_port: int,
             local_addr: Optional[str] = "127.0.0.1",
             local_port: Optional[int] = 25565,
             domain_bind: Optional[str] = "",
             host_rewrite: Optional[str] = "",
             request_from: Optional[str] = "",
             custom: Optional[str] = "",
             dataGzip: Optional[bool] = False,
             dataEncrypt: Optional[bool] = False,
             url_route: Optional[str] = "",
             name: Optional[str] = f"OfApp_{randint(30000, 99999)}",
             request_pass: Optional[str] = ""
             ):
    # POST API
    _APIData = post(
        url=f"{APIURL}/frp/api/newProxy",
        json={
            "session": session,
            "node_id": node_id,
            "name": name,
            "type": type,
            "local_addr": local_addr,
            "local_port": local_port,
            "remote_port": remote_port,
            "domain_bind": domain_bind,
            "dataGzip": dataGzip,
            "dataEncrypt": dataEncrypt,
            "url_route": url_route,
            "host_rewrite": host_rewrite,
            "request_from": request_from,
            "request_pass": request_pass,
            "custom": custom
        },
        headers={'Content-Type': 'application/json',
                 'Authorization': Authorization}
    )
    _newProxyData = _APIData.json()
    data = _newProxyData['data']
    flag = bool(_newProxyData['flag'])
    msg = str(_newProxyData['msg'])

    if not _APIData.ok:
        _APIData.raise_for_status()

    return data, flag, msg


def editProxy(Authorization: str,
              session: str,
              node_id: int,
              type: str,
              remote_port: int,
              proxy_id: int,
              local_addr: Optional[str] = "127.0.0.1",
              local_port: Optional[int] = 25565,
              domain_bind: Optional[str] = "",
              custom: Optional[str] = "",
              dataGzip: Optional[bool] = False,
              dataEncrypt: Optional[bool] = False,
              name: Optional[str] = f"OfApp_{randint(30000, 99999)}"
              ):
    # POST API
    _APIData = post(
        url=f"{APIURL}/frp/api/editProxy",
        json={
            "name": name,
            "node_id": node_id,
            "local_addr": local_addr,
            "local_port": local_port,
            "remote_port": remote_port,
            "domain_bind": domain_bind,
            "dataGzip": dataGzip,
            "dataEncrypt": dataEncrypt,
            "custom": custom,
            "type": type,
            "proxy_id": proxy_id,
            "session": session
        },
        headers={'Content-Type': 'application/json',
                 'Authorization': Authorization}
    )
    _editProxyData = _APIData.json()
    data = _editProxyData['data']
    flag = bool(_editProxyData['flag'])
    msg = str(_editProxyData['msg'])

    if not _APIData.ok:
        _APIData.raise_for_status()

    return data, flag, msg


def removeProxy(Authorization: str,
                session: str,
                proxy_id: int
                ):
    # POST API
    _APIData = post(
        url=f"{APIURL}/frp/api/removeProxy",
        json={
            "proxy_id": proxy_id,
            "session": session
        },
        headers={'Content-Type': 'application/json',
                 'Authorization': Authorization}
    )
    _removeProxyData = _APIData.json()
    data = _removeProxyData['data']
    flag = bool(_removeProxyData['flag'])
    msg = str(_removeProxyData['msg'])

    if not _APIData.ok:
        _APIData.raise_for_status()

    return data, flag, msg


def getNodeList(Authorization: str, session: str):
    # POST API
    _APIData = post(
        url=f"{APIURL}/frp/api/getNodeList",
        json={
            "session": session
        },
        headers={'Content-Type': 'application/json',
                 'Authorization': Authorization}
    )
    _getNodeListData = _APIData.json()
    data = _getNodeListData['data']
    flag = bool(_getNodeListData['flag'])
    msg = str(_getNodeListData['msg'])

    if not _APIData.ok:
        _APIData.raise_for_status()

    return data, flag, msg
