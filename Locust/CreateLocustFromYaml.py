import os,sys
# 切换到当前脚本的上级目录
rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# # 切换到根目录
# rootPath = os.path.abspath(os.path.join(first_dir, ".."))
# 将项目目录添加到sys.path
sys.path.append(rootPath)
from Locust.common import readyaml,ReadTxt

def creat_py(name,case,eg):

    newstr = eg[0:5] +["\n"]
    if case["randomtoken"] == True or "ReadTxt" in case['querypara']:
        newstr = newstr + eg[5:12]
        if case["randomtoken"] == True:
            newstr.append('account = ReadTxt("'+case['accountpath']+'")')
    newstr = newstr + eg[13:23]
    newstr.append("case = " + str(case))
    if 'ReadTxt' in case['querypara']:
        newstr.append('case["querypara"] = ' + case['querypara'])
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
    print(newstr)
    with open( name + ".py", 'w',) as f:
        for x in newstr:
            f.writelines(x+"\n")
cases = readyaml(os.path.join(rootPath, "Locust/testcase.yaml"))
eg = ReadTxt(os.path.join(rootPath,'Locust/base_case.eg'))
for name,case in cases.items():
    print(name,case)
    creat_py(name,case,eg)
