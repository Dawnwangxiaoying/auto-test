import os, xlrd, logging, xlwt, time
from xlutils.copy import copy
from xlrd import open_workbook


def readCase(excelName, sheetIndex):
    caseList = []
    # 需在表格中加上函数名那列
    try:
        readExcel = xlrd.open_workbook(excelName)  # 读取指定的Excel
        table = readExcel.sheet_by_index(sheetIndex)  # 获取Excel的第一个sheet
        rowCount = table.nrows  # 获取Excel的行数
        for n in range(1, rowCount):
            if table.cell(n, 0).value.lower() == "y":
                tmpdict = {}  # 把一行记录写进一个{}
                tmpdict['id'] = n  # n是Excel中的第n行
                tmpdict['Runflag'] = table.cell(n, 0).value
                tmpdict['title'] = table.cell(n, 1).value
                tmpdict['path'] = table.cell(n, 2).value
                tmpdict['model'] = table.cell(n, 3).value
                tmpdict['verifycode'] = table.cell(n, 4).value
                tmpdict['method'] = table.cell(n, 5).value
                tmpdict['data'] = table.cell(n, 6).value
                tmpdict['filePath']=table.cell(n, 7).value
                tmpdict['expection'] = table.cell(n, 8).value
                tmpdict['save'] = table.cell(n, 10).value
                tmpdict['contain'] = table.cell(n, 9).value
                tmpdict['datapath'] = table.cell(n, 11).value
                tmpdict['contentType'] = table.cell(n, 12).value
                tmpdict['out'] = table.cell(n, 13).value
                # tmpdict['runtimes'] = table.cell(n, 12).value
                caseList.append(tmpdict)
        return caseList
        logging.info("读取用例：" + str(rowCount - 1) + "，即将执行：" + str(len(caseList)))
    except Exception as err:
        logging.error("打开execl文件出错")
        return err


def readTitle(excelName, sheetIndex):
    caseList = []
    # 需在表格中加上函数名那列
    try:
        readExcel = xlrd.open_workbook(excelName)  # 读取指定的Excel
        table = readExcel.sheet_by_index(sheetIndex)  # 获取Excel的第一个sheet
        rowCount = table.nrows  # 获取Excel的行数
        for n in range(1, rowCount):
            if table.cell(n, 0).value.lower() == "y":
                title = table.cell(n, 1).value
                caseList.append(title)
        return caseList
        logging.info("读取用例：" + str(rowCount - 1) + "，即将执行：" + str(len(caseList)))
    except Exception as err:
        logging.error("打开execl文件出错")
        return err


def bulidCase(excelName, sheetIndex, pyName):
    caseList = readCase(excelName, sheetIndex)
    print(os.path.exists(pyName))
    if os.path.exists(pyName) == False:
        with open(pyName, "w") as f:
            f.writelines("import requests" + "\n")

    with open(pyName, "a") as f:
        # global functionname
        for case in caseList:
            functionName = nameBulid(case)
            print(functionName)
            if "$" in functionName:
                functionName = functionName.split("$")[-1]
            print(functionName)

            f.writelines("# " + case["title"] + "\n")
            f.writelines("def " + functionName + "(host,token):" + "\n")
            f.writelines("\t" + "try:" + "\n")
            f.writelines("\t" + "\t" + 'headers = {"token": token}' + "\n")
            f.writelines("\t" + "\t" + "url = host + '" + case["path"] + "'\n")
            if case['method'].upper() == "POST" or case['method'].upper() == "DELETE" or case[
                'method'].upper() == "PUT":
                if case['contentType'] == "json":
                    f.writelines("\t" + "\t" + 'json = ' + case['data'] + "\n")
                    f.writelines("\t" + "\t" + 'responseinfo = requests.' + case[
                        'method'].lower() + '(url, data =' + case['data'] + ', headers = headers)' + "\n")
                else:
                    f.writelines("\t" + "\t" + 'data = ' + case['data'] + "\n")
                    f.writelines("\t" + "\t" + 'responseinfo = requests.' + case[
                        'method'].lower() + '(url, data =' + case['data'] + ', headers = headers)' + "\n")
            elif case['method'].upper() == 'GET':
                f.writelines("\t" + "\t" + 'responseinfo = requests.' + case[
                    'method'].lower() + '(url, headers = headers)' + "\n")
            f.writelines("\t\t" + "print(responseinfo.text)" + "\n")
            f.writelines("\t" + "except:" + "\n")
            f.writelines("\t" + "\t" + "print('接口错误')" + "\n\n\n")


def nameBulid(case=[]):
    for i in range(1, len(case["path"].split("/")) + 1):
        if case["path"].split("/")[-i] != '' and "?" not in case["path"].split("/")[-i]:
            functionName = case["path"].split("/")[-i]
            return functionName



