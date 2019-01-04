
import os
import sys


rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.append(rootPath)

from interface.common.fileUtil import readCase
from interface.config.envConfig import casePath
from interface.common.baseCase import login
from interface.common.common import ReadTxt


caseList = readCase(os.path.join(rootPath, casePath), sheetIndex=1)
# storage = login()[0]
print(caseList)

def creat_py(name,case,eg):
    for case in caseList:

        newstr = eg[0:5] +["\n"]
        newstr = newstr + eg[13:23]
        newstr.append("case = " + str(case))
        newstr = newstr + ["\n"]+eg[23:28]
        if case["method"] == "GET" or case["method"] == "get":
            newstr = newstr + eg[28:29]
        elif case["method"] == "POST" or case["method"] =="post":
            newstr = newstr + eg[29:30]
        elif case["method"] == "put" or "PUT":
            newstr = newstr + eg[30:31]
        elif case["method"] == "DELETE" or "delete":
            newstr = newstr + eg[31:32]
        newstr = newstr + eg[32:40]
        with open( case['title'] + ".py", 'w') as f:
            for x in newstr:
                f.writelines(x+"\n")
eg = ReadTxt('base_case.eg')
creat_py(caseList,eg)