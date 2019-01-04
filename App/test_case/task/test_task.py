# coding:utf-8
import inspect
from time import sleep

'''
description:账号密码登陆
'''
from App.common import pageUtil
import allure


@allure.feature('登录')
class TestClass(object):

    def setup_class(cls):
        pass

    def teardown_class(cls):
        pageUtil.driver.quit()

    @allure.story("账号密码登录")
    def test_login_pwd(self):
        sleep(5)
        pageUtil.findAndAction("使用账号密码登录")
        pageUtil.findAndAction("邮箱")
        pageUtil.findAndAction("密码")
        pageUtil.findAndAction("登录按钮")
