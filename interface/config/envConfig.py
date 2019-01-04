import os, sys
import logging

# 调试模式下打开配置运行环境和BUTILD_ID
os.environ['BUILD_ID'] = '10'
os.environ['Environ'] = 'test'
casePath = 'data/interface.xlsx'
runTimes = 1
sheetIndex = 1
if os.environ['Environ'] == 'dev':
    userName = 'quanxian@dev.com'
    passWord = '123456'
    webBaseUrl = "https://dev.alphalawyer.cn/"
    boxBaseUrl = "https://devbox.alphalawyer.cn/"
    desktopBaseUrl = "https://devim.alphalawyer.cn/"
    schoolUrl = "https://devschool.icourt.cc/"
    schoolAdminUrl = "https://devadminschool.icourt.cc/"
elif os.environ['Environ'] == 'test':
    userName = 'yang@platform.com'
    passWord = '123456'
    webBaseUrl = "https://test.alphalawyer.cn/"
    boxBaseUrl = "https://testbox.alphalawyer.cn/"
    desktopBaseUrl = "https://testim.alphalawyer.cn/"
    schoolUrl = "https://testschool.icourt.cc/"
    schoolAdminUrl = "https://testadminschool.icourt.cc/"
elif os.environ['Environ'] == 'pre':
    userName = 'tester@icourt.cc'
    passWord = '123456'
    webBaseUrl = "https://pre.alphalawyer.cn/"
    boxBaseUrl = "https://prebox.alphalawyer.cn/"
    desktopBaseUrl = "https://preim.alphalawyer.cn/"
    schoolUrl = "https://preschool.icourt.cc/"
    schoolAdminUrl = "https://preadminschool.icourt.cc/"
elif os.environ['Environ'] == 'preinter':
    userName = 'huazi@online.com'
    passWord = '123456'
    webBaseUrl = "https://pre.alphalawyer.cn/"
    boxBaseUrl = "https://prebox.alphalawyer.cn/"
    desktopBaseUrl = "https://preim.alphalawyer.cn/"
    schoolUrl = "https://preschool.icourt.cc/"
    schoolAdminUrl = "https://preadminschool.icourt.cc/"
elif os.environ['Environ'] == 'internal':
    userName = 'qx1@online.com'
    passWord = '123456'
    webBaseUrl = "https://alphalawyer.cn/"
    boxBaseUrl = "https://box.alphalawyer.cn/"
    desktopBaseUrl = "https://im.alphalawyer.cn/"
    schoolUrl = "https://school.icourt.cc/"
    schoolAdminUrl = "https://adminschool.icourt.cc/"
elif os.environ['Environ'] == 'production':
    userName = 'tester@icourt.cc'
    passWord = '123456'
    webBaseUrl = "https://alphalawyer.cn/"
    boxBaseUrl = "https://box.alphalawyer.cn/"
    desktopBaseUrl = "https://im.alphalawyer.cn/"
    schoolUrl = "https://school.icourt.cc/"
    schoolAdminUrl = "https://adminschool.icourt.c/c"
else:
    logging.debug('>>>>>>>>>>>>>>>>>>>>>>>>>>>>运行环境不能识别，请检查Jenkins参数是否错误错误<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    sys.exit()
