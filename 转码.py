from urllib import parse
from xlwt import Workbook
import pandas
import xlrd


def excel_encode():

    with xlrd.open_workbook('/Users/icourt2/Desktop/test/postman_bigdata/pre_data.xls') as excel1:
        sheet1 = excel1.sheet_by_index(0)

    postman_data = Workbook(encoding='utf-8')
    sheet2 = postman_data.add_sheet('sheet1', cell_overwrite_ok=True)

    for j in range(sheet1.ncols):
        sheet2.write(0, j, sheet1.cell_value(0,j))
        for i in range(1,sheet1.nrows):
            a = parse.quote(str(sheet1.cell_value(i,j)))
            sheet2.write(i,j,a)

    postman_data.save('/Users/icourt2/Desktop/test/postman_bigdata/later_data.xls')

    data_xls = pandas.read_excel('/Users/icourt2/Desktop/test/postman_bigdata/later_data.xls', index_col=0)
    data_xls.to_csv('/Users/icourt2/Desktop/later_data.csv', encoding='utf-8')


if __name__ == '__main__':
    excel_encode()