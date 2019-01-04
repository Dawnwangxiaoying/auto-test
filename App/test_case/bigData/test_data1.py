from time import sleep

import allure
from App.common import pageUtil


@allure.step("账号密码登录")
def test_login_pwd():
    # test_login_pwd()
    sleep(10)
    pageUtil.find_and_action("工作台")
    pageUtil.find_and_action("外部数据库")
    pageUtil.find_and_action("外部数据库搜索")
    sleep(10)
    pageUtil.find_element("百度一下")