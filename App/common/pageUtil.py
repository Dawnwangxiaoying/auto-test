# coding:utf-8
import traceback
from time import sleep

import os

__author__ = 'xiaoying'
'''
description:UI页面公共类
'''
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common import mobileby
from App.common.logUtil import logUtil
from App.common.readData import readYamlAll
from App.config.driver_configure import get_driver
import allure

logger = logUtil()
driver = get_driver()


# 重写find_element方法，显式等待
def find_element(locName):
    try:
        loc = readYamlAll("data")[locName]
        element = eval('WebDriverWait(driver, 10).until(lambda x:x.find_element_by_' + loc['by'] + "('" + loc[
                'path'] + "'))")
        return element

    except:
        logger.info("查找元素：%s失败" % (str(locName)))
        logger.info('''异常信息为：''' + str(traceback.print_exc()))


def find_and_action(locName):
    try:
        loc = readYamlAll("data")[locName]
        allure.step(locName + ":" + loc['by'] + ',' + loc['path'] + ',' + loc['action'])
        if 'actionType' in loc.keys() and loc['actionType'] == 'js':
            find_element(locName).click()
            driver.execute_script("arguments[0].click();", find_element(locName))
        else:
            if loc['action'] == 'send_keys':
                eval('WebDriverWait(driver, 10).until(lambda x:x.find_element_by_' + loc['by'] + "('" + loc[
                'path'] + "'))"+"." + loc['action'] + '("' + str(loc['send_content']) + '")')

            else:
               eval('WebDriverWait(driver, 10).until(lambda x:x.find_element_by_' + loc['by'] + "('" + loc[
                'path'] + "'))"+"." + loc['action'] + '(' + ')')

        if 'pressKeyCode' in loc.keys():
            if locName == "外部数据库搜索":
                tap(driver, loc)
            driver.press_keycode(loc['pressKeyCode'])

        if 'switch_context' in loc.keys():
            sleep(5)
            switch_context(driver, 'WEBVIEW_stetho_com.icourt.alpha')
    except:
        logger.info(loc['action'] + " %s 元素失败" % (str(locName)))
        logger.info('''异常信息为：''' + str(traceback.print_exc()))


# 重写switch_frame方法
def switch_frame(driver, loc):
    return driver.switch_to_frame(str(loc))


# 断言toast信息
def find_toast(self, message):
    by = mobileby.MobileBy()
    try:
        WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_element_located((by.PARTIAL_LINK_TEXT, message)))
        return True
    except:

        return False


def switch_context(driver, context=u"WEBVIEW_*"):
    """
        1：环境不同，Native->To->Webview  or Webview->to->Native
        2：如果环境相同则不切换
    """
    contexts = driver.contexts
    print(contexts)
    if context in contexts:
        logger.info(u"切换环境前" + driver.current_context)
        driver.switch_to.context(context)
        logger.info(u"切换环境后" + driver.current_context)
        return True
    else:
        logger.error(u"没有切换到相应的环境下面，当前的环境为" + str(driver.context))
        return False


def tap(driver, loc):
    os.system("adb shell ime set com.baidu.input_huawei/.ImeService")
    sleep(2)
    eval('WebDriverWait(driver, 10).until(lambda x:x.find_element_by_' + loc['by'] + '("' + loc[
        'path'] + '")).' + 'click' + '(' + ')')
    os.system("adb shell input tap 1035 1748")
    sleep(2)
    os.system("adb shell ime set io.appium.android.ime/.UnicodeIME")
