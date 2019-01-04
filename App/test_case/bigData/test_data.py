from time import sleep

import allure
from App.common import pageUtil
from App.test_case.login import test_login


@allure.step("账号密码登录")
def test_login_pwd():
    # test_login_pwd()
    sleep(10)
    locDict = ("工作台", "Alpha大数据", "点击Alpha案例库搜索框", "Alpha案例库搜索")
    for locName in locDict:
        pageUtil.find_and_action(locName)
