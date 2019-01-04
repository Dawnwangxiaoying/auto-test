import requests
from common import configUtil


def getSeafileToken(self, configName):
    config = configUtil.getconfig(configName)
    url = config["weburl"] + "ilaw/api/v1/auth/login"
    data = {"user": self.config["用户名"], "password": self.config["密码"], "deviceType": "web"}
    self.headers = {"Content-Type": "application/json;charset=UTF-8"}
    login = requests.post(url, json=data, headers=self.headers)
    print(login.json())
    url = self.config["weburl"] + "ilaw/api/v2/documents/getToken"
    seafileinfo = requests.get(url, headers={"token": login.json()["token"]})
    seafiletoken = seafileinfo.json()["authToken"]
    print(seafiletoken)
    return login.json(), seafiletoken
