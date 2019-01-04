# coding:utf-8
import pytest
import os
import sys, allure

# 切换到当前脚本的上级目录
rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
print(rootPath)
# # 切换到根目录
# rootPath = os.path.abspath(os.path.join(first_dir, ".."))
# 将项目目录添加到sys.path
sys.path.append(rootPath)
from interface.common.fileUtil import readCase
from interface.config.envConfig import casePath, sheetIndex
from interface.common.baseCase import request, saveJson, login, getData, getUrl
from interface.common.assertUtil import myAssert
from interface.common.logUtil import logUtil

logger = logUtil()


@allure.feature('接口smoke')
class TestClass(object):
    caseList = readCase(os.path.join(rootPath, casePath), sheetIndex=1)
    storage = login()[0]
    headers = login()[1]
    print(headers)

    @pytest.fixture(scope="module",
                    params=caseList)
    def case(self, request):
        case = request.param
        yield case

    def test_a(self, case):
        allure.description(case["title"])
        r = ""
        url = getUrl(case["path"], case["model"], self.storage, r, case)
        print(url)
        data = getData(case["data"], self.storage, r, case)
        print(data)
        with allure.step("发送请求"):
            allure.attach("请求方式", case["method"])
            allure.attach('url', str(url))
            allure.attach('data', str(data))
        # try:
        headers = self.headers
        r = request(case, url, data, headers)
        actual = r.text
        # except:
        #     actual = ""
        if case["save"]:
            self.storage = saveJson(r, case, self.storage)
        with allure.step("存储数据"):
            allure.attach('storage', str(self.storage))
        with allure.step("返回校验"):
            if case["contain"]:
                allure.attach('期望结果', case["contain"])
            elif case["expection"]:
                allure.attach('期望结果', case["expection"])
            else:
                allure.attach('期望结果', "用例中未设定值")
            allure.attach('实际结果', str(actual))
        result = myAssert(r, case["verifycode"], case["expection"], case["contain"])
        assert True == result
