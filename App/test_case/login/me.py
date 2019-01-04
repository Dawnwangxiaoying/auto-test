from time import sleep

from App.common import pageUtil


def test_login_pwd():
    # test_login_pwd()
    sleep(10)
    pageUtil.findAndAction("我的")
    pageUtil.findAndAction("头像")
    pageUtil.findAndAction("姓名")

