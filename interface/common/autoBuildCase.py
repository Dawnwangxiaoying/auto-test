from common import fileUtil
from unittest import TestCase
import os


class autoBulidCase(TestCase):
    # 获取项目的根目录
    rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


    def test(self):
        print(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")) + '/Data/interface.xlsx')
        fileUtil.bulidCase(self.rootPath + '/data/interface.xlsx', 1, self.rootPath + "/case/AlphaForAutoTest.py")
