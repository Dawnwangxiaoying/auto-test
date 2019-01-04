import os, yaml

from App.common.logUtil import logUtil

log = logUtil()


# 读取指定yaml文件
def readYaml(path):
    rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    casePath = os.path.join(rootPath, path)
    with open(casePath, encoding="utf-8") as f:
        location = yaml.load(f)
    return location


# 读取指定路径所有的yaml文件
def readYamlAll(path):
    locationAll = {}
    rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    casePath = os.path.join(rootPath, path)
    list = os.listdir(casePath)  # 列出文件夹下所有的目录与文件
    for i in range(0, len(list)):
        path = os.path.join(casePath, list[i])
        with open(path, encoding="utf-8") as f:
            location = yaml.load(f)
            # 取两个list的交集
            if  [val for val in locationAll.keys() if val in location.keys()]:
                log.error('yaml文件中的key重复,' + "location:" + location.keys() + "locationAll:" + locationAll.keys())
                raise RuntimeError(
                    'yaml文件中的key重复,' + "location:" + location.keys() + "locationAll:" + locationAll.keys())
        locationAll = dict(locationAll, **location)
    return locationAll
