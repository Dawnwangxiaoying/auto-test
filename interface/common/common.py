import xlrd
import random
import string, yaml


def ReadTxt(path, blocklist=''):
    try:
        with open(path, 'r') as f:
            k = []
            for i in f.readlines():
                if i == '\n':
                    pass
                else:
                    k.append(i.replace("\n", ""))
        return k
    except:
        print("读取txt文件失败")


def readExecl(path, lenth, sheetIndex=1):
    caseList = []
    # 需在表格中加上函数名那列
    try:
        readExcel = xlrd.open_workbook(path)  # 读取指定的Excel
        table = readExcel.sheet_by_index(sheetIndex)  # 获取Excel的第一个sheet
        rowCount = table.nrows  # 获取Excel的行数
        if lenth <= 0:
            return caseList
        for n in range(1, rowCount):
            for i in range(lenth):
                tmpdict = {}  # 把一行记录写进一个{}
                tmpdict[i] = table.cell(n, i - i).value
            caseList.append(tmpdict)
        return caseList
    except:
        print("读取execl失败")


def random_string(str_len):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(str_len))


def Readyaml(path):
    with open(path) as f:
        case = yaml.load(f)
    return case

def IsWhiteList(url,whitelist):
    for i in whitelist:
        if i in url:
            return False
    return True

def OutputIntoExecl(sheetname,cases,workbook,name = "case.xls" ):

    worksheet = workbook.add_sheet(sheetname, cell_overwrite_ok=True)
    index = 0
    for case in cases:
        for i in range(len(case)):
            worksheet.write(index, i, case[i])
        index += 1
    workbook.save(name)
