import os
import uuid

import requests, time, json, traceback, random
from interface.common.logUtil import logUtil
from interface.config.envConfig import userName, passWord, runTimes, webBaseUrl, boxBaseUrl, desktopBaseUrl, schoolUrl, \
    schoolAdminUrl

logger = logUtil()
msgId = str(uuid.uuid1()).replace("-", '')
rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def login(userName=userName, passWord=passWord):
    url = webBaseUrl + "ilaw/api/v1/auth/login"
    data = {"user": userName, "password": passWord, "deviceType": "web"}
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    r = requests.post(url, json=data, headers=headers)
    userInfo = r.json()
    url = webBaseUrl + "ilaw/api/v2/documents/getToken"
    seafileInfo = requests.get(url, headers={"token": r.json()["token"]})
    seafileToken = seafileInfo.json()["authToken"]
    headers = {"Authorization": "Token " + seafileToken,
               "token": userInfo["token"]}
    storage = {"today": str(time.strftime("%Y-%m-%d")), "token": userInfo["token"],
               "officeid": userInfo["officeId"], "userid": userInfo["userId"],
               "now": int(time.time()), 'randomint': random.randint(11111111, 99999999),
               "pageIndex": 0, "pageSize": 300, "effectRepeats": False}
    return storage, headers, userInfo["token"]


def getUrl(path, model, storage, r="", case=""):
    # data为空为get，否则为post

    try:
        # if 1 == 1:
        if "$" in path:
            newUrl = ""
            url = path.split("$")
            for i in range(len(url)):
                if i % 2 == 0:
                    if i == (len(url) - 1):
                        newUrl = newUrl + url[i]
                    else:
                        print(storage.keys())
                        if url[i + 1] in storage.keys():
                            newUrl = newUrl + url[i] + str(eval("storage[url[" + str(i + 1) + "]]"))
                        else:
                            newUrl = newUrl + url[i] + url[i + 1]
                            logger.info("url中的" + url[i + 1] + "没有获取到")
            url = newUrl
        else:
            url = path

        if model == "permission":
            url = url
        elif model == "法学院":
            url = schoolUrl + url
        elif model == "法学院后台":
            url = schoolAdminUrl + url
        elif model == "文档":
            url = boxBaseUrl + url
        elif model == "客户端":
            url = desktopBaseUrl + url
        else:
            url = webBaseUrl + url

        return url
    except:
        logger.info(str(url) + " 获取url错误" + '''
        异常信息为：''' + str(traceback.print_exc()))
        return " 获取url错误" + '''
        异常信息为：''' + str(traceback.print_exc())


def getData(data, storage, r="", case=""):
    try:
        storage['msgId'] = msgId
        data = data
        newData = ""
        if "$" in data:
            data = data.split("$")
            for i in range(len(data)):
                if i % 2 == 0:
                    if i == (len(data) - 1):
                        newData = newData + data[i]
                    else:
                        newData = newData + data[i] + str(eval("storage[data[" + str(i + 1) + "]]"))
            data = newData
        return data

    except:
        logger.info(str(data) + " 获取data错误" + '''
        异常信息为：''' + str(traceback.print_exc()))
        return data


def saveJson(r, case, storage):
    try:
        if r.status_code == 200:
            if type(case["save"]) is list and type(case["datapath"]) is list:
                for i in range(len(case["save"])):
                    if case["path"] == "ilaw/api/v2/contact/namespair/?name=":
                        save1 = eval("r.json()" + case["save"][i])
                        storage[case["save"][i]] = list(eval("save1.keys()"))[0]
                    else:
                        storage[case["save"][i]] = eval("r.json()" + case["datapath"][i])

            else:
                if case["path"] == "ilaw/api/v2/contact/namespair/?name=":

                    save1 = eval("r.json()" + case["datapath"])
                    storage[case["save"]] = list(eval("save1.keys()"))[0]
                else:
                    storage[case["save"]] = eval("r.json()" + case["datapath"])
            return storage
    except:
        logger.info("保存参数错误" + '''
        请求参数为：''' + case["save"] +
                    '''异常信息为：
                    ''' + str(traceback.print_exc()))
        return "保存参数错误" + '''请求参数为：''' + case["save"] + '''异常信息为：''' + str(traceback.print_exc())


def request(case, url, data, headers):
    # try:
    num = runTimes
    r = ""
    for i in range(num):

        if case["method"] == 'GET':
            r = requests.get(url, headers=headers)
            logger.info(r.text)
        elif case["method"] == 'POST':
            if case["contentType"] == "data":
                r = requests.post(url, data=json.loads(data), headers=headers)
                logger.info(r.text)
            elif case["contentType"] == "multi":
                r = requests.post(url, data=json.loads(data), files={'file': open(rootPath+case['filePath'], 'rb')},
                                  headers=headers)
                logger.info(r.text)

            else:
                if data == "":
                    r = requests.post(url, headers=headers)
                    logger.info(r.text)
                else:
                    r = requests.post(url, json=json.loads(data), headers=headers)
                    logger.info(r.text)
        elif case["method"] == 'PUT':
            r = requests.put(url, json=json.loads(data), headers=headers)
            logger.info(r.text)
        elif case["method"] == "DELETE":
            if data == "":
                r = requests.delete(url, headers=headers)
                logger.info(r.text)
            else:
                r = requests.delete(url, data=json.loads(data), headers=headers)
                logger.info(r.text)
    return r


def login100():
    pass
