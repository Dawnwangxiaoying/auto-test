import requests
import xlwt
from urllib.parse import urlencode
import os,sys
# 切换到当前脚本的上级目录
rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# # 切换到根目录
# rootPath = os.path.abspath(os.path.join(first_dir, ".."))
# 将项目目录添加到sys.path
sys.path.append(rootPath)
from common.common import IsWhiteList,OutputIntoExecl,Readyaml

def BuildSingleCase(url,method,body,mode):
    parameters = {}
    for para in body:
        if para["in"] == "header":
            break
        else:
            parameters[para["name"]] = '$'+para["name"] + '$'
    if method == 'get':
        url = ('%s%s%s' % (url, '?', urlencode(parameters)))
        parameters = ''
    return url,parameters

def BuildInterfaceBasicInfo(keys,info,mode):
    InterfaceBasicInfo = []
    for url, values in info["paths"].items():
        flag = IsWhiteList(url,whitelist)
        if flag:
            for method, para in values.items():
                if 'parameters' in para.keys():
                    url,parameters = BuildSingleCase(url,method,para["parameters"],mode)
                else:
                    parameters = ""
                url = url.replace("{","$").replace("}","$").replace("%24","$")
                InterfaceBasicInfo.append(["N",para["summary"],url,keys,"",method.upper(),str(parameters),"","","","","","N"])
    return InterfaceBasicInfo

def Buildcase(url,whitelist,mode = 'Smoke'):
    workbook = xlwt.Workbook(encoding='ascii')
    for keys, values in urls.items():
        try:
            info = requests.get(values, timeout=20).json()
            print("处理" + keys + "模块接口,共有" + str(len(info["paths"])) + "个子接口")
            case = BuildInterfaceBasicInfo(keys,info,mode)
            OutputIntoExecl(keys,case,workbook)
        except:
            pass

urls = Readyaml(os.path.join(rootPath, "BuildCase/urls.yaml"))["urls"]
whitelist = Readyaml(os.path.join(rootPath, "BuildCase/urls.yaml"))["whitelist"]
Buildcase(urls,whitelist)