import requests


def getRequest(url, params, headers, expected, checkPoint, returnContent):
    response = requests.get(url, params, headers)
    assert response + '.' + checkPoint == expected
    if returnContent != "":
        return returnContent


def postRequest(url, data, expected, checkPoint, returnContent, headers):
    response = requests.post(url, data, headers)
    assert response + '.' + checkPoint == expected
    if returnContent != "":
        return returnContent


def putRequest(url, data, expected, checkPoint, returnContent, headers):
    response = requests.put(url, data, headers)
    assert response + '.' + checkPoint == expected
    if returnContent != "":
        return returnContent


def deleteRequest(url, data, expected, checkPoint, returnContent, headers):
    response = requests.delete(url, data, headers)
    assert response + '.' + checkPoint == expected
    if returnContent != "":
        return returnContent
